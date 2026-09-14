# -*- coding: utf-8 -*-
"""C1-D: the ladder with a generation limit that does not bind, and a check
that the manipulation moves the quantity it is named after.

10.19 found that the two previous ladders measured a token cap. Mean reasoning at
the highest load was 918 against a limit of 1024, and the scorer counted an
answer that never parsed as though it were a verdict that parsed twice and
disagreed. It also found that nothing in the record establishes that distractor
load reduces the evaluator's effective rank, which is the quantity a rank budget
is about. A null from an unverified manipulation is not evidence.

Two repairs.

**The limit is raised until it does not bind**, and every level reports its
`finish_reasons`. A level in which any comparison ends on `length` is refused,
because the parse gate is registered at zero and an unparsed answer here is
scored identically to a swap disagreement.

**The metric is recalibrated under each load.** A calibration block is drawn and
rendered WITH that level's distractors, so the fitted geometry is the loaded one,
and its workload moment gives the spectrum. If distractor load reduces effective
rank, the spectrum concentrates: the discarded trace share falls, the gap widens,
or the retained direction rotates away from its unloaded position. If none of
those moves, the manipulation did not do the thing the ladder is named after and
the graded cells below it cannot speak to a budget either way.

The graded cells keep 10.18's fixed denominator, with the ambiguity bucket now
split so truncation and genuine order-dependence are never added together.

Not a graded cell for any registered claim.

    python c1_rankcheck.py --pilot pilot3_qwen3.json --out rankcheck.json
"""
from __future__ import annotations

import argparse
import json
import os
import sys

import numpy as np

from c1_budget import ModeChooser, condition_admissible, wilson
from c1_calibrate import retained, workload_moment
from c1_distractor import DISTRACTOR_LABELS, render_loaded, run_level
from c1_ellm_chooser import preflight_model_pin
from c1_order import both_orders, calibrate_from_order, heldout_order_accuracy
from c1_scorer import build_pairs, render_option


def loaded_calibration(chooser, ideal_vec, A, B, load, rng, lo, hi) -> dict:
    """Fit the metric from comparisons the evaluator makes UNDER the load.

    The distractor block is shared within a pair, as everywhere in this design,
    so it cannot change which option is nearer. What it can change is how well
    the evaluator resolves the comparison, and that is what the fit records.
    """
    ideal_d = rng.uniform(lo, hi, size=load) if load else np.zeros(0)
    As, Bs = [], []
    for a, b in zip(A, B):
        d = rng.uniform(lo, hi, size=load) if load else np.zeros(0)
        As.append(render_loaded(a, d))
        Bs.append(render_loaded(b, d))
    ideal_str = render_loaded(ideal_vec, ideal_d)
    oo = both_orders(chooser, ideal_str, As, Bs)
    keep = np.array(oo["keep"])
    y = np.array(oo["a_nearer"], dtype=float)
    if int(keep.sum()) < 90:
        return {"note": "too few usable comparisons to fit",
                "kept": int(keep.sum()), "n": len(A),
                "agreement_rate": oo["agreement_rate"],
                "first_position_rate": oo["first_position_rate"]}
    cal = calibrate_from_order(A[keep], B[keep], y[keep])
    ho = heldout_order_accuracy(A[keep], B[keep], y[keep])
    G = np.array(cal["G"], float)
    t = np.array(cal["t"], float)
    M = workload_moment(G, t, A[keep])
    w, V = np.linalg.eigh(M)
    order = np.argsort(w)[::-1]
    w, V = w[order], V[:, order]
    tot = float(w.sum())
    return {"kept": int(keep.sum()), "n": len(A),
            "agreement_rate": oo["agreement_rate"],
            "first_position_rate": oo["first_position_rate"],
            "heldout": ho["mean"], "G": G.tolist(), "t": t.tolist(),
            "eigenvalues": w.tolist(),
            "gap_k1": float(w[0] / w[1]), "gap_k2": float(w[1] / w[2]),
            "discarded_share_k1": float(w[1:].sum() / tot),
            "discarded_share_k2": float(w[2:].sum() / tot),
            "top1": V[:, 0].tolist(), "top2": V[:, :2].tolist()}


def subspace_angle(V1, V2, k) -> float:
    """Largest principal angle between two k-subspaces, in degrees.

    The SMALLEST is identically zero whenever two k-planes in d-space must
    intersect, which 10.10 got backwards; the largest is the informative one.
    """
    A1 = np.array(V1, float).reshape(len(V1), -1)[:, :k] if k > 1 else np.array(V1, float).reshape(-1, 1)
    A2 = np.array(V2, float).reshape(len(V2), -1)[:, :k] if k > 1 else np.array(V2, float).reshape(-1, 1)
    Q1, _ = np.linalg.qr(A1)
    Q2, _ = np.linalg.qr(A2)
    sv = np.clip(np.abs(np.linalg.svd(Q1.T @ Q2, compute_uv=False)), 0, 1)
    return float(np.degrees(np.arccos(sv.min())))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="prereg_config.json")
    ap.add_argument("--pilot", default="pilot3_qwen3.json")
    ap.add_argument("--out", default="rankcheck.json")
    ap.add_argument("--seed", type=int, default=20260923)
    ap.add_argument("--n-per-class", type=int, default=64)
    ap.add_argument("--n-cal", type=int, default=200)
    ap.add_argument("--loads", default="0,4,8,16")
    ap.add_argument("--max-tokens", type=int, default=4096)
    ap.add_argument("--k", type=int, default=1)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    loads = [int(x) for x in args.loads.split(",")]
    cfg = json.load(open(args.config, encoding="utf-8"))
    cfg = dict(cfg)
    cfg["evaluator"] = dict(cfg["evaluator"])
    cfg["evaluator"]["max_tokens"] = args.max_tokens      # repair 1
    pilot = json.load(open(args.pilot, encoding="utf-8"))
    from c1_atlas_run import box
    LO, HI = box(cfg)
    G0 = np.array(pilot["calibration"]["G"], float)
    t0 = np.array(pilot["calibration"]["t"], float)
    ideal_vec = np.array(cfg["ideal"], float)
    d = len(cfg["ideal"])
    rng = np.random.default_rng(args.seed)

    Aref = np.random.default_rng(pilot["seed"]).uniform(
        LO, HI, size=(int(cfg.get("n_order_pairs", 400)), d))
    built = build_pairs(G0, t0, Aref, k=args.k, n_per_class=args.n_per_class,
                        rng=rng, lo=LO, hi=HI,
                        oversample=int(cfg.get("oversample", 400)),
                        pool=int(cfg.get("pool", 3)))
    print(f"[rankcheck] k={args.k}  W {len(built['W'])}  T {len(built['T'])}  "
          f"max_tokens {args.max_tokens}  calibration {args.n_cal} pairs per load")
    if args.dry_run:
        print("[rankcheck] dry run, nothing sent")
        return 0

    from c1_atlas_run import Thermal, provenance
    with Thermal():
        token = os.environ.get("NRP_LLM_TOKEN")
        if not token:
            raise RuntimeError("NRP_LLM_TOKEN absent")
        pin = preflight_model_pin(cfg, token)
        print(f"[rankcheck] pin verified, {pin['model_id']} created {pin['created']}")

        Acal = rng.uniform(LO, HI, size=(args.n_cal, d))
        Bcal = rng.uniform(LO, HI, size=(args.n_cal, d))
        levels, base_cal = {}, None
        for load in loads:
            lev = {"load": load}

            # --- repair 2: does the load move the geometry at all? ---
            ch = ModeChooser(cfg, token, {})
            cal = loaded_calibration(ch, ideal_vec, Acal, Bcal, load,
                                     np.random.default_rng(args.seed + 1000 + load),
                                     LO[0], HI[0])
            cal["finish_reasons"] = dict(ch.finish_reasons)
            cal["unparsed"] = ch.unparsed
            lev["calibration"] = cal
            if "eigenvalues" in cal:
                if base_cal is None:
                    base_cal = cal
                cal["angle_top1_vs_load0_deg"] = subspace_angle(
                    base_cal["top1"], cal["top1"], 1)
                cal["angle_top2_vs_load0_deg"] = subspace_angle(
                    base_cal["top2"], cal["top2"], 2)
                print(f"[rankcheck] load {load:>2} calibration: kept {cal['kept']}/{cal['n']}  "
                      f"heldout {cal['heldout']:.4f}  eig "
                      f"{np.round(cal['eigenvalues'],1).tolist()}")
                print(f"             gap_k1 {cal['gap_k1']:.3f}  "
                      f"discarded_k1 {cal['discarded_share_k1']:.4f}  "
                      f"top1 angle vs load 0 {cal['angle_top1_vs_load0_deg']:.2f} deg  "
                      f"unparsed {cal['unparsed']}")
            else:
                print(f"[rankcheck] load {load:>2} calibration FAILED: {cal.get('note')}")

            # --- the graded cells, fixed denominator, ambiguity split ---
            cell = {}
            for cls in ("W", "T"):
                ch2 = ModeChooser(cfg, token, {})
                r = run_level(ch2, ideal_vec, built[cls], load,
                              np.random.default_rng(args.seed + load), LO[0], HI[0])
                cell[cls] = r
                print(f"[rankcheck] load {load:>2} {cls}: score {r['score_fixed']:.4f} "
                      f"strict {r['score_strict']:.4f} surv {r['q_agree_full_survivors']:.4f}  "
                      f"amb {r['ambiguous']} (trunc {r['ambiguous_truncated']}, "
                      f"genuine {r['ambiguous_genuine_disagreement']})  "
                      f"unparsed {r['unparsed']}  reasoning {r['mean_reasoning_tokens']:.0f}")
            adm = condition_admissible(cell)
            cell["admissible"] = adm
            if not adm["admissible"]:
                print(f"[rankcheck] load {load} INADMISSIBLE")
                for w in adm["reasons"]:
                    print(f"             {w}")
            else:
                cell["class_gap"] = float(cell["W"]["score_fixed"]
                                          - cell["T"]["score_fixed"])
            lev["cells"] = cell
            levels[str(load)] = lev

    rec = {"stage": "rankcheck", "seed": args.seed, "k": args.k,
           "max_tokens": args.max_tokens, "loads": loads,
           "provenance": provenance(), "evaluator_pin": pin,
           "grades_no_claim": True, "levels": levels}
    json.dump(rec, open(args.out, "w", encoding="utf-8"), indent=1)

    print("\n[rankcheck] manipulation check, did the load move the geometry")
    print(f"{'load':>5} {'gap_k1':>8} {'disc_k1':>9} {'top1 angle':>11} {'heldout':>8} {'trunc':>6}")
    for L in loads:
        c = levels[str(L)].get("calibration", {})
        if "eigenvalues" not in c:
            print(f"{L:>5}   calibration failed"); continue
        tr = sum(v for k, v in c.get("finish_reasons", {}).items() if "length" in k)
        print(f"{L:>5} {c['gap_k1']:>8.3f} {c['discarded_share_k1']:>9.4f} "
              f"{c['angle_top1_vs_load0_deg']:>11.2f} {c['heldout']:>8.4f} {tr:>6}")
    print(f"rankcheck written to {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
