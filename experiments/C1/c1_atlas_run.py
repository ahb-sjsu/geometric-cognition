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
from c1_calibrate import calibrate, retained
from c1_scorer import (LMScorer, build_pairs, render_option, rendering_ceiling,
                       run_cell)

TARGET_TEMP = 78.0          # below the 82 high and the 80 shed line for Package 0
MAX_THREADS = 20            # the standing cap even with a controller


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
    rng = np.random.default_rng(seed)
    d = len(cfg["ideal"])
    ideal = np.array(cfg["ideal"], dtype=float)

    with Thermal() as th:
        print(f"[probe] loading evaluator, {th.threads()} host threads")
        sc = LMScorer(cfg)

        n_cal = int(cfg.get("n_calibration", 300))
        X_cal = rng.uniform(cfg.get("lo", 0.0), cfg.get("hi", 100.0), size=(n_cal, d))
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
            pairs = build_pairs(G, t, X_cal, k=k,
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


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--stage", choices=("selftest", "probe"), required=True)
    ap.add_argument("--config", default="prereg_config.json")
    ap.add_argument("--out")
    ap.add_argument("--seed", type=int, default=20260913)
    args = ap.parse_args()
    out = args.out or f"{args.stage}.json"
    if args.stage == "selftest":
        return stage_selftest(out)
    return stage_probe(args.config, out, args.seed)


if __name__ == "__main__":
    sys.exit(main())
