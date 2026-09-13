# -*- coding: utf-8 -*-
"""The two controls the cold reread asked for, against the pinned evaluator.

Section 10 of the registration returned three defects. Two of them are testable
without redesigning anything, because both are re-renderings of pairs the pilot
already knows how to build, graded by the instrument already pinned.

**Placebo budget, for D1.** The workload moment is isotropic by construction,
because the ideal sits at the centroid of the cube the options are drawn from.
If that is so then the top-`k` eigenspace is not a budget, it is whichever plane
the calibration draw happened to pick, and replacing it with a uniformly random
`k`-plane should change nothing. The contrast surviving is the bad outcome. It
says the gate reports a property of orthogonal projection.

**Class W-prime, for D3.** A within-subspace pair is admitted only when its
whitened difference has no discarded component, so the projection subtracts the
same vector from both options and the rendered difference between them survives
intact. A trading pair is never of that form. The classes are therefore
separated by a property of the text, and any evaluator that tends to keep a
verdict when both options move together produces the registered result without
any geometry.

W-prime removes exactly that cue and nothing else. Each option's budget
rendering keeps its retained part and is given a discarded part of the same norm
as the one it lost, in an independent random direction. The two options then
move by different vectors. The order is unchanged, and not approximately:

    |u'_a|^2 - |u'_b|^2 = (|Pi u_a|^2 + r^2) - (|Pi u_b|^2 + r^2)
                        = |Pi u_a|^2 - |Pi u_b|^2

and for a W pair that equals the full-budget difference. So the theory predicts
the same zero reversal rate for W-prime as for W, and the assertion is checked
in code before a single comparison is sent. If W-prime reverses where W does
not, the difference is the rendering.

Neither control grades a claim. Both are diagnostics on an unsealed design, and
the registration stays unsealed whatever they return.

    CUDA_VISIBLE_DEVICES=1 python c1_controls.py --out controls.json
"""
from __future__ import annotations

import argparse
import json
import os
import sys

import numpy as np

import c1_scorer
from c1_calibrate import retained, sqrtm_psd
from c1_scorer import build_pairs, render_option, round_to_render
from c1_order import run_cell_order


def random_plane(d: int, k: int, rng) -> np.ndarray:
    """A uniformly random k-dimensional subspace of the whitened space."""
    Q, _ = np.linalg.qr(rng.normal(size=(d, d)))
    return Q[:, :k] @ Q[:, :k].T


def build_with_plane(G, t, X_cal, k, n_per_class, rng, Pi, LO, HI, OVER, POOL):
    """`build_pairs` exactly, but on a plane we hand it rather than the top-k.

    The patch is on `c1_scorer.retained`, so every other line of the admission
    logic, the margin match and the bin structure is the registered one. A
    control that reimplements the thing it controls is not a control.
    """
    real = c1_scorer.retained
    res = dict(real(G, t, X_cal, k))
    res["Pi_whitened"] = np.asarray(Pi).tolist()
    res["note"] = "placebo, a uniformly random k-plane, not the top-k eigenspace"
    c1_scorer.retained = lambda *a, **kw: res
    try:
        return build_pairs(G, t, X_cal, k=k, n_per_class=n_per_class, rng=rng,
                           lo=LO, hi=HI, oversample=OVER, pool=POOL)
    finally:
        c1_scorer.retained = real


def wprime(pairs, G, t, Pi, rng, lo=0.0, hi=100.0):
    """Re-render W pairs so the two options move by different vectors.

    Keeps each option's retained part, restores a discarded part of the norm it
    lost in an independent direction, and asserts that the predicted order is
    unchanged at both budgets before returning.
    """
    G, t = np.asarray(G, float), np.asarray(t, float)
    Gh, Ghi = sqrtm_psd(G), sqrtm_psd(G, inverse=True)
    d = G.shape[0]
    I, Pi = np.eye(d), np.asarray(Pi, float)
    # dimension of the discarded complement. At k = d-1 it is a line, so two
    # independent directions do not exist and the largest available difference
    # between the two options is antipodal. That is still a differential shift,
    # and the order argument is unchanged because both add r^2.
    dim_disc = int(round(np.trace(I - Pi)))
    out, shifts = [], []
    drops = {"no_discarded_norm": 0, "degenerate_direction": 0, "out_of_box": 0,
             "renders_equal": 0, "rounding_flipped_order": 0}

    for p in pairs:
        a, b = np.asarray(p["a"], float), np.asarray(p["b"], float)
        ua, ub = (a - t) @ Gh, (b - t) @ Gh
        ra, rb = ua @ Pi, ub @ Pi
        # the norm each option loses to the projection, which we give back
        r = 0.5 * (np.linalg.norm(ua @ (I - Pi)) + np.linalg.norm(ub @ (I - Pi)))
        if r <= 1e-9:
            drops["no_discarded_norm"] += 1
            continue

        def disc_dir():
            v = rng.normal(size=d) @ (I - Pi)
            n = np.linalg.norm(v)
            return v / n if n > 1e-12 else None

        ea, eb = disc_dir(), disc_dir()
        if ea is None or eb is None:
            drops["degenerate_direction"] += 1
            continue
        if dim_disc <= 1:
            eb = -ea                     # a line admits only the antipode
        elif abs(float(ea @ eb)) > 0.95:
            eb = eb - float(ea @ eb) * ea      # orthogonalise rather than drop
            n = np.linalg.norm(eb)
            if n < 1e-12:
                drops["degenerate_direction"] += 1
                continue
            eb = eb / n
        xa = t + (ra + r * ea) @ Ghi
        xb = t + (rb + r * eb) @ Ghi
        if not (np.all(xa >= lo) and np.all(xa <= hi)
                and np.all(xb >= lo) and np.all(xb <= hi)):
            drops["out_of_box"] += 1
            continue
        ka, kb = round_to_render(xa), round_to_render(xb)
        if np.array_equal(ka, kb):
            drops["renders_equal"] += 1
            continue
        # the order the theory predicts at this budget, on the rendered points
        dka = float(np.sqrt((ka - t) @ G @ (ka - t)))
        dkb = float(np.sqrt((kb - t) @ G @ (kb - t)))
        if (dka < dkb) != p["a_pref_full"]:
            drops["rounding_flipped_order"] += 1
            continue
        shifts.append(float(np.linalg.norm((xa - a) - (xb - b))))
        q = dict(p)
        q["a_render_k"] = render_option(ka)
        q["b_render_k"] = render_option(kb)
        out.append(q)
    return {"pairs": out, "dropped": sum(drops.values()), "drop_reasons": drops,
            "discarded_dimension": dim_disc,
            "mean_differential_shift": float(np.mean(shifts)) if shifts else 0.0}


def common_shift_share(pairs, tol=0.06):
    """Share of pairs whose budget rendering moves both options by one vector.

    This is the cue D3 names, measured directly on the strings the evaluator is
    shown rather than inferred from the construction.
    """
    import re
    n = 0
    for p in pairs:
        ak = np.array([float(x) for x in re.findall(r"-?\d+\.?\d*", p["a_render_k"])])
        bk = np.array([float(x) for x in re.findall(r"-?\d+\.?\d*", p["b_render_k"])])
        a, b = np.asarray(p["a"], float), np.asarray(p["b"], float)
        if ak.shape == a.shape and np.allclose(a - ak, b - bk, atol=tol):
            n += 1
    return (n / len(pairs)) if pairs else float("nan")


def rows(pairs):
    return [(render_option(np.asarray(p["a"], float)),
             render_option(np.asarray(p["b"], float)),
             p["a_render_k"], p["b_render_k"]) for p in pairs]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="prereg_config.json")
    ap.add_argument("--pilot", default="pilot_qwen3.json")
    ap.add_argument("--out", default="controls.json")
    ap.add_argument("--seed", type=int, default=20260915)
    ap.add_argument("--n-per-class", type=int, default=64)
    ap.add_argument("--dry-run", action="store_true",
                    help="build and check the controls without sending anything")
    args = ap.parse_args()

    cfg = json.load(open(args.config, encoding="utf-8"))
    from c1_atlas_run import box
    LO, HI = box(cfg)
    OVER = int(cfg.get('oversample', 400))
    POOL = int(cfg.get('pool', 3))
    pilot = json.load(open(args.pilot, encoding="utf-8"))
    G = np.array(pilot["calibration"]["G"], float)
    t = np.array(pilot["calibration"]["t"], float)
    d = G.shape[0]
    ideal_str = render_option(np.array(cfg["ideal"], float))
    rng = np.random.default_rng(args.seed)
    # the calibration options, redrawn from the pilot's own seed and stream
    A = np.random.default_rng(pilot["seed"]).uniform(
        LO, HI, size=(int(cfg.get("n_order_pairs", 400)), d))

    M_eig = retained(G, t, A, k=1)["eigenvalues"]
    print(f"[controls] workload moment eigenvalues {np.round(M_eig, 1).tolist()}, "
          f"gap ratio top/next {M_eig[0] / M_eig[1]:.4f}")

    built = {}
    for k in (1, 2):
        real_Pi = np.array(retained(G, t, A, k)["Pi_whitened"], float)
        rand_Pi = random_plane(d, k, rng)
        # ALL principal angles, not just the one from the largest singular
        # value. The first run reported only the largest, which is identically
        # zero whenever the two subspaces must intersect: any two 2-planes in
        # three-space share a line. That made the k=2 placebo look like a null
        # rotation when it was a real one. The informative summary is the
        # smallest angle that is not forced to zero, so report the whole set.
        sv = np.clip(np.abs(np.linalg.svd(real_Pi @ rand_Pi, compute_uv=False)), 0, 1)
        angs = np.degrees(np.arccos(sv))[:k]
        ang = float(np.max(angs))
        real = build_pairs(G, t, A, k=k, n_per_class=args.n_per_class, rng=rng,
                           lo=LO, hi=HI, oversample=OVER, pool=POOL)
        plac = build_with_plane(G, t, A, k, args.n_per_class, rng, rand_Pi,
                                LO, HI, OVER, POOL)
        wp = wprime(real["W"], G, t, real_Pi, rng, LO, HI)
        built[k] = {"real": real, "placebo": plac, "wprime": wp,
                    "plane_angle_deg": float(ang),
                    "principal_angles_deg": [float(a) for a in angs],
                    "forced_zero_angles": int(k - np.count_nonzero(angs > 1e-6))}
        print(f"[controls] k={k}  principal angles {np.round(angs, 1).tolist()} deg")
        print(f"[controls] k={k}  real W {len(real['W'])} T {len(real['T'])}  "
              f"placebo W {len(plac['W'])} T {len(plac['T'])}  "
              f"W-prime {len(wp['pairs'])} kept, {wp['dropped']} dropped "
              f"{wp['drop_reasons']}")
        print(f"           common-shift share  W {common_shift_share(real['W']):.3f}  "
              f"T {common_shift_share(real['T']):.3f}  "
              f"W-prime {common_shift_share(wp['pairs']):.3f}")

    if args.dry_run:
        print("[controls] dry run, nothing sent")
        return 0

    from c1_atlas_run import Thermal, provenance
    from c1_ellm_chooser import EllmChooser, preflight_model_pin

    with Thermal():
        token = os.environ.get("NRP_LLM_TOKEN")
        if not token:
            raise RuntimeError("NRP_LLM_TOKEN absent")
        pin = preflight_model_pin(cfg, token)
        print(f"[controls] pin verified, {pin['model_id']} created {pin['created']}")
        ch = EllmChooser(cfg, token)

        cells = {}
        for k in (1, 2):
            b = built[k]
            cell = {"plane_angle_deg": b["plane_angle_deg"],
                    "principal_angles_deg": b["principal_angles_deg"],
                    "forced_zero_angles": b["forced_zero_angles"],
                    "mean_differential_shift": b["wprime"]["mean_differential_shift"],
                    "wprime_drops": b["wprime"]["drop_reasons"],
                    "wprime_discarded_dimension": b["wprime"]["discarded_dimension"],
                    "common_shift_share": {
                        "W": common_shift_share(b["real"]["W"]),
                        "T": common_shift_share(b["real"]["T"]),
                        "W_prime": common_shift_share(b["wprime"]["pairs"])}}
            for name, pairs in (("placebo_W", b["placebo"]["W"]),
                                ("placebo_T", b["placebo"]["T"]),
                                ("W_prime", b["wprime"]["pairs"])):
                if not pairs:
                    cell[name] = {"note": "empty"}
                    continue
                print(f"[controls] k={k} {name}, {len(pairs)} pairs")
                cell[name] = run_cell_order(ch, ideal_str, rows(pairs), "k")
                print(f"           rate {cell[name]['reversal_rate']:.4f} "
                      f"({cell[name]['graded']} graded)")
            if "placebo_W" in cell and "reversal_rate" in cell.get("placebo_T", {}):
                cell["placebo_contrast"] = (cell["placebo_T"]["reversal_rate"]
                                            - cell["placebo_W"]["reversal_rate"])
            cells[str(k)] = cell

    rec = {"stage": "controls", "seed": args.seed, "provenance": provenance(),
           "evaluator_pin": pin, "grades_no_claim": True,
           "workload_eigenvalues": M_eig,
           "pilot_reference": {"contrast": 0.9682539682539683,
                               "R_W": 0.0, "R_T": 0.9682539682539683},
           "unparsed": ch.unparsed, "deadline_failures": ch.failed,
           "finish_reasons": ch.finish_reasons,
           "escalations": ch.escalations, "cells": cells}
    json.dump(rec, open(args.out, "w", encoding="utf-8"), indent=1)

    print("\n[controls] summary, against the pilot's 0.0000 / 0.9683")
    for k, c in cells.items():
        pc = c.get("placebo_contrast")
        wp = c.get("W_prime", {}).get("reversal_rate")
        print(f"  k={k}  placebo W {c['placebo_W'].get('reversal_rate', float('nan')):.4f}  "
              f"placebo T {c['placebo_T'].get('reversal_rate', float('nan')):.4f}  "
              f"placebo contrast {pc if pc is None else round(pc, 4)}  "
              f"W-prime {wp if wp is None else round(wp, 4)}")
    print(f"controls written to {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
