# -*- coding: utf-8 -*-
"""Run C1's registered self-test and probe on Atlas, under thermal control.

Atlas rule 2 is non-negotiable. The Z840's coolers cannot sustain a full load,
so every CPU or GPU heavy stage here runs inside a batch-probe ThermalController
and the thread count is read from it rather than assumed. Atlas rule 3 puts this
on GPU 1 through CUDA_VISIBLE_DEVICES, so the code always addresses logical
device 0 and never hardcodes an index above zero.

Nothing here kills, restarts, or starts a display service.

    CUDA_VISIBLE_DEVICES=1 python c1_atlas_run.py --stage selftest
    CUDA_VISIBLE_DEVICES=1 python c1_atlas_run.py --stage probe
"""
from __future__ import annotations

import argparse
import json
import os
import platform
import socket
import subprocess
import sys
import time

import numpy as np

import c1_calibrate
import c1_scorer
from c1_calibrate import (assert_budget_usable, assert_spectral_gap,
                          clopper_pearson_upper, calibrate, retained)
from c1_scorer import (LMScorer, build_pairs, render_option, rendering_ceiling,
                       run_cell)

TARGET_TEMP = 78.0          # below the 82 high and the 80 shed line for Package 0
MAX_THREADS = 20            # the standing cap even with a controller


def box(cfg) -> tuple:
    """The consequence box, per attribute. Scalars are accepted for old configs.

    Threaded explicitly into `build_pairs`, which otherwise falls back to its own
    [0, 100] defaults. Under the first design those defaults happened to equal
    the calibration box, so the omission was invisible. Under an anisotropic box
    it would draw graded pairs from a different distribution than the one the
    metric was fitted on.
    """
    d = len(cfg["ideal"])
    lo = np.broadcast_to(np.asarray(cfg.get("lo", 0.0), float), (d,)).copy()
    hi = np.broadcast_to(np.asarray(cfg.get("hi", 100.0), float), (d,)).copy()
    return lo, hi


def gpu_line() -> str:
    try:
        return subprocess.run(
            ["nvidia-smi", "--query-gpu=index,utilization.gpu,memory.used,temperature.gpu",
             "--format=csv,noheader"],
            capture_output=True, text=True, timeout=30).stdout.strip()
    except Exception as exc:                      # pragma: no cover
        return f"unavailable, {exc}"


class Thermal:
    """batch-probe ThermalController if present, and a refusal if it is not.

    Running without it would breach the standing rule, so the absence of the
    package stops the run rather than downgrading to an unthrottled one.
    """

    def __init__(self, target: float = TARGET_TEMP, max_threads: int = MAX_THREADS):
        from batch_probe import ThermalController
        self.c = ThermalController(target_temp=target, max_threads=max_threads,
                                   min_threads=4)

    def __enter__(self):
        self.c.start()
        n = int(self.c.get_threads())
        os.environ["OMP_NUM_THREADS"] = str(n)
        try:
            import torch
            torch.set_num_threads(n)
        except Exception:
            pass
        print(f"[thermal] controller up, {n} threads, target {TARGET_TEMP} C")
        return self

    def threads(self) -> int:
        return int(self.c.get_threads())

    def __exit__(self, *exc):
        self.c.stop()
        print("[thermal] controller stopped")
        return False


def competing_forms(X: np.ndarray, r: np.ndarray, ideal: np.ndarray) -> dict:
    """Which functional form does the evaluator's report actually follow?

    The gate assumes a quadratic form, because that is what an evaluation object
    supplies. If the evaluator reports something else then the calibration is not
    merely noisy, it is fitting the wrong family, and the retained subspace built
    from it means nothing. Each candidate is scored by the R-squared of a least
    squares fit with an intercept and a scale, so the comparison is of shape and
    not of units.
    """
    keep = np.isfinite(r)
    X, r = X[keep], r[keep]
    D = X - np.asarray(ideal, float)

    def r2(pred: np.ndarray) -> float:
        A = np.column_stack([pred, np.ones(len(pred))])
        beta, *_ = np.linalg.lstsq(A, r, rcond=None)
        resid = r - A @ beta
        denom = float(np.sum((r - r.mean()) ** 2))
        return float(1.0 - np.sum(resid ** 2) / denom) if denom > 0 else float("nan")

    out = {
        "euclidean": r2(np.linalg.norm(D, axis=1)),
        "manhattan": r2(np.abs(D).sum(axis=1)),
        "chebyshev": r2(np.abs(D).max(axis=1)),
        "mean_abs": r2(np.abs(D).mean(axis=1)),
        "squared_euclidean": r2((D ** 2).sum(axis=1)),
    }
    for i in range(X.shape[1]):
        out[f"abs_attr_{i}"] = r2(np.abs(D[:, i]))
    # A full quadratic in x, which is the family the calibration fits.
    from c1_calibrate import design
    A = design(X)
    beta, *_ = np.linalg.lstsq(A, r ** 2, rcond=None)
    resid = r ** 2 - A @ beta
    denom = float(np.sum((r ** 2 - np.mean(r ** 2)) ** 2))
    out["quadratic_on_r_squared"] = (
        float(1.0 - np.sum(resid ** 2) / denom) if denom > 0 else float("nan"))
    out["report_min"] = float(r.min())
    out["report_max"] = float(r.max())
    out["report_mean"] = float(r.mean())
    out["report_distinct"] = int(len(np.unique(np.round(r, 6))))
    out["best"] = max((k for k in out if k.startswith(("euclid", "manhat", "chebysh",
                                                       "mean_abs", "squared", "abs_attr",
                                                       "quadratic"))),
                      key=lambda k: (out[k] if np.isfinite(out[k]) else -9e9))
    return out


def provenance() -> dict:
    import torch
    import transformers
    return {
        "host": socket.gethostname(),
        "python": platform.python_version(),
        "numpy": np.__version__,
        "torch": torch.__version__,
        "transformers": transformers.__version__,
        "cuda_visible_devices": os.environ.get("CUDA_VISIBLE_DEVICES"),
        "gpu_at_start": gpu_line(),
        "utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "target_temp": TARGET_TEMP,
        "max_threads": MAX_THREADS,
    }


def stage_selftest(out: str) -> int:
    """The registered self-test of PREREG-C1 section 7.

    Pure numpy, so it is not GPU work, but it runs inside the controller anyway
    because the rule is about the host and not about the device.
    """
    with Thermal():
        cal = c1_calibrate.selftest(verbose=True)
        noise = [c1_calibrate.selftest_noisy(sigma=s) for s in (0.1, 0.5, 1.0, 2.0, 4.0)]
        harness = c1_scorer.selftest()
    rec = {"stage": "selftest", "provenance": provenance(),
           "calibration": cal, "noise_sweep": noise, "harness": harness,
           "pass": bool(cal["pass"] and harness["pass"])}
    json.dump(rec, open(out, "w", encoding="utf-8"), indent=1)
    print(f"\nself-test verdict {'PASS' if rec['pass'] else 'FAIL'}, written to {out}")
    return 0 if rec["pass"] else 1


def stage_probe(cfg_path: str, out: str, seed: int) -> int:
    """Event presence and anti-vacuity on the probe seed.

    Calibrate the evaluator on a block, derive the retained subspace, build both
    classes, and check the instrument gates of section 5. No claim is graded
    here. A probe that passes says the gate can be run, not that it passed.
    """
    cfg = json.load(open(cfg_path, encoding="utf-8"))
    LO, HI = box(cfg)
    rng = np.random.default_rng(seed)
    d = len(cfg["ideal"])
    ideal = np.array(cfg["ideal"], dtype=float)

    with Thermal() as th:
        print(f"[probe] loading evaluator, {th.threads()} host threads")
        sc = LMScorer(cfg)

        n_cal = int(cfg.get("n_calibration", 300))
        X_cal = rng.uniform(LO, HI, size=(n_cal, d))
        print(f"[probe] scoring {n_cal} calibration options")
        reports = sc.scores(render_option(ideal),
                            [render_option(x) for x in X_cal],
                            batch=int(cfg.get("batch", 32)))
        cal = calibrate(X_cal, np.array(reports))
        # A probe that misses must keep what would explain the miss. The first
        # run of this stage recorded only the fit statistics, so an r2 of 0.09
        # could not be diagnosed without scoring the block again.
        cal["raw"] = {"options": X_cal.tolist(), "reports": list(map(float, reports))}
        cal["forms"] = competing_forms(X_cal, np.array(reports), ideal)
        G, t = np.array(cal["G"]), np.array(cal["t"])
        print(f"[probe] calibration r2 {cal['r2']:.4f}, "
              f"dropped {cal['n_dropped']}, psd clip {cal['psd_clip']:.3e}")

        cells = {}
        for k in (1, 2):
            res = retained(G, t, X_cal, k)
            pairs = build_pairs(G, t, X_cal, k=k, lo=LO, hi=HI,
                                n_per_class=int(cfg.get("n_per_class", 64)), rng=rng)
            Pi = np.array(pairs["retained"]["Pi_whitened"])
            ceil_T = rendering_ceiling(pairs["T"], G, t, Pi) if pairs["T"] else None
            cell = {
                "k": k,
                "discarded_trace_share": res["discarded_trace_share"],
                "n_W": len(pairs["W"]), "n_T": len(pairs["T"]),
                "margin_mean_W": pairs["margin_mean_W"],
                "margin_mean_T": pairs["margin_mean_T"],
                "rendering_ceiling_T": ceil_T,
            }
            if pairs["W"] and pairs["T"]:
                print(f"[probe] k={k} scoring cells, W {len(pairs['W'])} T {len(pairs['T'])}")
                cell["W"] = run_cell(sc, ideal, pairs["W"], "k")
                cell["T"] = run_cell(sc, ideal, pairs["T"], "k")
                cell["contrast"] = cell["T"]["reversal_rate"] - cell["W"]["reversal_rate"]
            cells[str(k)] = cell

    gates = {
        "class_construction": all(c.get("n_W", 0) > 0 and c.get("n_T", 0) > 0
                                  for c in cells.values()),
        "anti_vacuity": all(c["discarded_trace_share"] >= 0.05 for c in cells.values()),
        "no_unparsable": sc.unparsed == 0,
        "calibration_recovered": bool(cal["well_conditioned"] and cal["r2"] > 0.9),
    }
    rec = {"stage": "probe", "seed": seed, "provenance": provenance(),
           "config": cfg, "calibration": cal, "cells": cells,
           "unparsed_reports": sc.unparsed, "instrument_gates": gates,
           "pass": all(gates.values())}
    json.dump(rec, open(out, "w", encoding="utf-8"), indent=1)
    print("\n[probe] instrument gates")
    for g, ok in gates.items():
        print(f"  {g:26s} {'OK' if ok else 'MISS'}")
    print(f"probe verdict {'PASS' if rec['pass'] else 'MISS'}, written to {out}")
    return 0 if rec["pass"] else 1


def stage_order_probe(cfg_path: str, out: str, seed: int) -> int:
    """Event presence and instrument health for the order-based calibration.

    The reported-distance instrument failed because it asked the evaluator for
    arithmetic. This asks only which of two options is nearer. The instrument
    gates come before the metric, because G3 discarded a chooser that measured
    its own position bias first, and a metric fitted through that bias would be
    the presentation's and not the evaluator's.
    """
    from c1_order import (LMChooser, both_orders, calibrate_from_order,
                          heldout_order_accuracy)
    cfg = json.load(open(cfg_path, encoding="utf-8"))
    LO, HI = box(cfg)
    hosted = "evaluator" in cfg
    rng = np.random.default_rng(seed)
    d = len(cfg["ideal"])
    ideal = np.array(cfg["ideal"], dtype=float)
    n = int(cfg.get("n_order_pairs", 400))

    pin = None
    with Thermal() as th:
        if hosted:
            from c1_ellm_chooser import EllmChooser, preflight_model_pin
            token = os.environ.get("NRP_LLM_TOKEN")
            if not token:
                raise RuntimeError("NRP_LLM_TOKEN absent; source /home/claude/.primer.env")
            # Refuse to run if the pinned alias has been repointed. The gateway
            # exposes no revision, so this timestamp is the only provenance the
            # registration can hold on to.
            pin = preflight_model_pin(cfg, token)
            print(f"[order] pin verified, {pin['model_id']} created {pin['created']}")
            ch = EllmChooser(cfg, token)
        else:
            print(f"[order] loading chooser, {th.threads()} host threads")
            ch = LMChooser(cfg)
        A = rng.uniform(LO, HI, size=(n, d))
        B = rng.uniform(LO, HI, size=(n, d))
        As = [render_option(x) for x in A]
        Bs = [render_option(x) for x in B]
        print(f"[order] {n} pairs, both presentation orders")
        oo = both_orders(ch, render_option(ideal), As, Bs,
                         batch=int(cfg.get("batch", 32)))

    keep = np.array(oo["keep"])
    y = np.array(oo["a_nearer"], dtype=float)
    gates = {
        "parse": ch.unparsed == 0,
        # A chooser that picks the first option regardless is reporting its
        # layout. Band fixed here before the numbers are seen.
        "position_bias": bool(abs(oo["first_position_rate"] - 0.5) <= 0.15),
        "agreement": bool(oo["agreement_rate"] >= 0.60),
    }
    rec = {"stage": "order_probe", "seed": seed, "provenance": provenance(),
           "evaluator_pin": pin,
           "deadline_failures": getattr(ch, "failed", 0),
           "finish_reasons": getattr(ch, "finish_reasons", {}),
           "truncation_escalations": getattr(ch, "escalations", 0),
           "mean_reasoning_tokens": (float(np.mean(ch.reasoning_tokens))
                                     if getattr(ch, "reasoning_tokens", None) else 0.0),
           "n_pairs": n, "kept": int(keep.sum()),
           "agreement_rate": oo["agreement_rate"],
           "first_position_rate": oo["first_position_rate"],
           "unparsed": ch.unparsed}

    if keep.sum() >= 10 * 9 and gates["position_bias"]:
        cal = calibrate_from_order(A[keep], B[keep], y[keep])
        ho = heldout_order_accuracy(A[keep], B[keep], y[keep])
        res = retained(np.array(cal["G"]), np.array(cal["t"]), A[keep], 2)
        rec["calibration"] = cal
        rec["heldout"] = ho
        rec["discarded_trace_share_k2"] = res["discarded_trace_share"]
        # The calibration gate for an order instrument is whether a quadratic
        # predicts comparisons the fit never saw.
        gates["quadratic_predicts_heldout"] = bool(ho["mean"] >= 0.80)
        if hosted and cfg["evaluator"].get("requires_deliberation"):
            # The registration requires an evaluator that deliberates, because
            # the only one of three that compared by content was the only one
            # that reasoned before answering. A run where it stopped reasoning
            # is not a run against the registered evaluator.
            gates["deliberated"] = bool(rec["mean_reasoning_tokens"] > 0)
        gates["anti_vacuity_k2"] = bool(res["discarded_trace_share"] >= 0.05)
    else:
        gates["quadratic_predicts_heldout"] = False
        gates["anti_vacuity_k2"] = False

    rec["instrument_gates"] = gates
    rec["pass"] = all(gates.values())
    json.dump(rec, open(out, "w", encoding="utf-8"), indent=1)
    print(f"\n[order] agreement {oo['agreement_rate']:.4f}  "
          f"first-position rate {oo['first_position_rate']:.4f}  "
          f"unparsed {ch.unparsed}")
    if "heldout" in rec:
        print(f"[order] held-out order accuracy {rec['heldout']['mean']:.4f}  "
              f"in-sample {rec['calibration']['order_accuracy']:.4f}  "
              f"discarded share k2 {rec['discarded_trace_share_k2']:.4f}")
    for g, ok in gates.items():
        print(f"  {g:28s} {'OK' if ok else 'MISS'}")
    print(f"order probe {'PASS' if rec['pass'] else 'MISS'}, written to {out}")
    return 0 if rec["pass"] else 1


def stage_pilot(cfg_path: str, out: str, seed: int) -> int:
    """Fix section 5's tolerances on a seed used for nothing else.

    The pilot exists to set MARG, CEIL and BIN before the registration is
    sealed. It is not a result and grades no claim. Its seed is disjoint from
    the probe's and from the run's, and the run seed is drawn only after the
    rename, so nothing measured here can have been chosen to suit what the run
    will later show.
    """
    import os as _os
    from c1_ellm_chooser import EllmChooser, preflight_model_pin
    from c1_order import (both_orders, calibrate_from_order,
                          heldout_order_accuracy, run_cell_order)

    cfg = json.load(open(cfg_path, encoding="utf-8"))
    LO, HI = box(cfg)
    rng = np.random.default_rng(seed)
    d = len(cfg["ideal"])
    ideal = np.array(cfg["ideal"], dtype=float)
    ideal_str = render_option(ideal)
    n_cal = int(cfg.get("n_order_pairs", 400))
    n_class = int(cfg.get("n_per_class", 64))

    with Thermal():
        token = _os.environ.get("NRP_LLM_TOKEN")
        if not token:
            raise RuntimeError("NRP_LLM_TOKEN absent")
        pin = preflight_model_pin(cfg, token)
        print(f"[pilot] pin verified, {pin['model_id']} created {pin['created']}")
        ch = EllmChooser(cfg, token)

        # 1. Calibrate from order, on evidence the graded pairs never touch.
        A = rng.uniform(LO, HI, size=(n_cal, d))
        B = rng.uniform(LO, HI, size=(n_cal, d))
        print(f"[pilot] calibrating on {n_cal} pairs, both orders")
        oo = both_orders(ch, ideal_str, [render_option(x) for x in A],
                         [render_option(x) for x in B])
        keep = np.array(oo["keep"])
        y = np.array(oo["a_nearer"], dtype=float)
        cal = calibrate_from_order(A[keep], B[keep], y[keep])
        ho = heldout_order_accuracy(A[keep], B[keep], y[keep])
        G, t = np.array(cal["G"]), np.array(cal["t"])
        print(f"[pilot] calibrated, held-out order accuracy {ho['mean']:.4f}, "
              f"kept {int(keep.sum())} of {n_cal}")

        # The budget must be identified before it can be manipulated. This is
        # the guard for the defect the cold reread found: a top-k eigenspace of
        # a gapless moment is a random plane, and the graded contrast survives
        # replacing it with one. Refuse rather than warn.
        floor = float(cfg.get("spectral_gap_floor", 2.0))
        sfloor = float(cfg.get("discarded_share_floor", 0.05))
        gaps = {}
        for k in (1, 2):
            gaps[str(k)] = assert_budget_usable(G, t, A[keep], k, floor, sfloor)
            print(f"[pilot] budget k={k} usable, gap {gaps[str(k)]['gap']:.2f} "
                  f"(floor {floor}, null p97.5 {gaps[str(k)]['null_p975']:.2f}), "
                  f"discarded share {gaps[str(k)]['discarded_share']:.4f} "
                  f"(floor {sfloor})")

        cells = {}
        for k in (1, 2):
            built = build_pairs(G, t, A[keep], k=k, n_per_class=n_class, rng=rng,
                                lo=LO, hi=HI,
                                oversample=int(cfg.get('oversample', 400)),
                                pool=int(cfg.get('pool', 3)))
            Pi = np.array(built["retained"]["Pi_whitened"])
            res = {"k": k,
                   "discarded_trace_share": built["retained"]["discarded_trace_share"],
                   "n_W": len(built["W"]), "n_T": len(built["T"]),
                   "margin_mean_W": built["margin_mean_W"],
                   "margin_mean_T": built["margin_mean_T"],
                   "bins": built["bins"]}
            if not built["W"] or not built["T"]:
                res["note"] = "a class came out empty"
                cells[str(k)] = res
                continue
            res["rendering_ceiling_T"] = rendering_ceiling(built["T"], G, t, Pi)
            for name in ("W", "T"):
                rows = [(render_option(p["a"]), render_option(p["b"]),
                         p["a_render_k"], p["b_render_k"]) for p in built[name]]
                prefs = [p["a_pref_full"] for p in built[name]]
                print(f"[pilot] k={k} class {name}, {len(rows)} pairs")
                res[name] = run_cell_order(ch, ideal_str, rows, "k",
                                           pref_full=prefs)
            res["contrast"] = res["T"]["reversal_rate"] - res["W"]["reversal_rate"]
            # D2 tested on this cell's own p rather than on held-out accuracy
            pT, pW = res["T"].get("competence_p"), res["W"].get("competence_p")
            if pT is not None and np.isfinite(pT) and np.isfinite(pW):
                pbar = 0.5 * (pT + pW)
                res["identity"] = {
                    "p_T": pT, "p_W": pW, "p_mean": pbar,
                    "predicted_contrast": float((2 * pbar - 1) ** 2),
                    "residual": float(res["contrast"] - (2 * pbar - 1) ** 2)}
                print(f"           competence p: T {pT:.4f} W {pW:.4f}; "
                      f"identity predicts {(2*pbar-1)**2:+.4f}, "
                      f"observed {res['contrast']:+.4f}, "
                      f"residual {res['identity']['residual']:+.4f}")
            # Section 11 asks for the class balance a margin match does not fix.
            res["balance"] = {
                "attr_range_W": float(np.mean([max(p["a"]) - min(p["a"])
                                               for p in built["W"]])),
                "attr_range_T": float(np.mean([max(p["a"]) - min(p["a"])
                                               for p in built["T"]])),
                "render_len_W": float(np.mean([len(render_option(p["a"]))
                                               for p in built["W"]])),
                "render_len_T": float(np.mean([len(render_option(p["a"]))
                                               for p in built["T"]]))}
            cells[str(k)] = res

    # 2. Fix the tolerances, by the rule section 5 states, not by inspection.
    usable = [c for c in cells.values() if "contrast" in c
              and np.isfinite(c["contrast"])]
    tol = {"rule": ("MARG is half the observed contrast floored at 0.10 and "
                    "capped at the rendering ceiling minus CEIL minus 0.05. "
                    "CEIL is twice the observed within-subspace rate floored "
                    "at 0.05.")}
    if usable:
        obs_contrast = float(np.min([c["contrast"] for c in usable]))
        obs_w = float(np.max([c["W"]["reversal_rate"] for c in usable]))
        ceil_T = float(np.min([c["rendering_ceiling_T"]["ceiling"] for c in usable]))
        # CEIL as an exact upper bound at the realised cell size, not a point
        # comparison. At 43 pairs a point CEIL of 0.05 turns on two items.
        bounds = [clopper_pearson_upper(c["W"]["reversals"], c["W"]["graded"])
                  for c in usable if c["W"]["graded"]]
        CEIL = max(max(bounds) if bounds else 0.05, 0.05)
        MARG = max(0.5 * obs_contrast, 0.10)
        cap = ceil_T - CEIL - 0.05
        tol.update({"CEIL_rule": "Clopper-Pearson 97.5 upper bound on the "
                                 "observed within-subspace reversals at the "
                                 "realised cell size, floored at 0.05",
                    "CEIL_bounds_per_cell": bounds,
                    "observed_contrast_min": obs_contrast,
                    "observed_W_max": obs_w,
                    "rendering_ceiling_min": ceil_T,
                    "CEIL": round(CEIL, 4),
                    "MARG_before_cap": round(MARG, 4),
                    "cap": round(cap, 4),
                    "MARG": round(min(MARG, cap), 4),
                    "cap_binds": bool(MARG > cap),
                    "capped_below_floor": bool(cap < 0.10)})
        if tol["capped_below_floor"]:
            tol["action"] = ("the cap falls under the 0.10 floor, so section 5 "
                             "requires the rendering precision to be increased "
                             "and the pilot rerun before sealing")

    rec = {"stage": "pilot", "seed": seed, "provenance": provenance(),
           "spectral_gaps": gaps, "box": {"lo": LO.tolist(), "hi": HI.tolist()},
           "evaluator_pin": pin, "calibration": cal, "heldout": ho,
           "kept_calibration_pairs": int(keep.sum()),
           "agreement_rate": oo["agreement_rate"],
           "first_position_rate": oo["first_position_rate"],
           "unparsed": ch.unparsed, "deadline_failures": ch.failed,
           "finish_reasons": ch.finish_reasons,
           "truncation_escalations": ch.escalations,
           "mean_reasoning_tokens": (float(np.mean(ch.reasoning_tokens))
                                     if ch.reasoning_tokens else 0.0),
           "cells": cells, "tolerances": tol}
    json.dump(rec, open(out, "w", encoding="utf-8"), indent=1)

    print("\n[pilot] cells")
    for k, c in cells.items():
        if "contrast" in c:
            print(f"  k={k}  W {c['W']['reversal_rate']:.4f}  "
                  f"T {c['T']['reversal_rate']:.4f}  "
                  f"contrast {c['contrast']:+.4f}  "
                  f"ceiling {c['rendering_ceiling_T']['ceiling']:.4f}  "
                  f"discarded {c['discarded_trace_share']:.4f}")
        else:
            print(f"  k={k}  {c.get('note')}")
    if "MARG" in tol:
        print(f"[pilot] tolerances  MARG {tol['MARG']}  CEIL {tol['CEIL']}  "
              f"cap {tol['cap']}  cap_binds {tol['cap_binds']}")
        if tol.get("capped_below_floor"):
            print(f"[pilot] {tol['action']}")
    print(f"pilot written to {out}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--stage",
                    choices=("selftest", "probe", "order_probe", "pilot"),
                    required=True)
    ap.add_argument("--config", default="prereg_config.json")
    ap.add_argument("--out")
    ap.add_argument("--seed", type=int, default=20260913)
    args = ap.parse_args()
    out = args.out or f"{args.stage}.json"
    if args.stage == "selftest":
        return stage_selftest(out)
    if args.stage == "order_probe":
        return stage_order_probe(args.config, out, args.seed)
    if args.stage == "pilot":
        return stage_pilot(args.config, out, args.seed)
    return stage_probe(args.config, out, args.seed)


if __name__ == "__main__":
    sys.exit(main())
