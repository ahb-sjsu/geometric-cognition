# -*- coding: utf-8 -*-
"""Find a prompt that elicits a quadratic evaluator, without dictating one.

The v1 probe missed its calibration gate at r2 0.0946, so the evaluator was not
reporting a quadratic form and the retained subspace built from it meant nothing.
This sweep looks for a framing that elicits a metric aggregation of the three
attributes. It is instrument development before sealing, which is what G3 did
when it tried and discarded two chooser instruments, and every variant tried is
recorded including the ones that fail.

**Selection rule, fixed here before the sweep runs.** A variant is scored only by
the R-squared of the quadratic fit on the calibration block. The reversal
contrast is not computed and is not available to this script. Choosing a prompt
by the statistic the gate grades would be fitting the instrument to the result,
which is the one thing the registration exists to prevent.

**The trivialising variant is a control, not a candidate.** A prompt that states
the formula makes the evaluator an arithmetic unit, the metric the identity by
construction, and the directional reversal a theorem about projection rather than
a finding about an evaluator. It is run to establish what the instrument's
arithmetic ceiling looks like, and it is marked ineligible.

    CUDA_VISIBLE_DEVICES=1 python c1_prompt_sweep.py --out sweep.json
"""
from __future__ import annotations

import argparse
import json
import sys

import numpy as np

from c1_atlas_run import Thermal, competing_forms, provenance
from c1_calibrate import calibrate
from c1_scorer import LMScorer, render_option

# Each variant is (name, eligible, template). `eligible` is False for a prompt
# that supplies the formula, which cannot be used for a graded gate.
VARIANTS = [
    ("v1_baseline", True,
     "The ideal option is: {ideal}\nA candidate option is: {option}\n"
     "How far is the candidate from the ideal? Answer with a single number and nothing else."),

    ("v2_coordinates", True,
     "Treat each option as a point whose coordinates are the three numbers.\n"
     "Ideal point: {ideal}\nCandidate point: {option}\n"
     "How far apart are the two points? Answer with a single number and nothing else."),

    ("v3_overall_gap", True,
     "Ideal: {ideal}\nCandidate: {option}\n"
     "Rate the overall gap between the candidate and the ideal on a continuous scale, "
     "where 0 means identical and larger numbers mean further apart. "
     "Large shortfalls on one attribute should count for more than small shortfalls "
     "spread across several. Answer with a single number and nothing else."),

    ("v4_squared_cost", True,
     "Ideal: {ideal}\nCandidate: {option}\n"
     "Each attribute contributes a cost that grows faster than its shortfall. "
     "Report the total cost of the candidate. "
     "Answer with a single number and nothing else."),

    ("v5_straight_line", True,
     "Two points in three dimensions.\nA: {ideal}\nB: {option}\n"
     "What is the straight-line distance between A and B? "
     "Answer with a single number and nothing else."),

    # Control. States the formula, so the evaluator has no geometry of its own.
    ("v6_formula_control", False,
     "Ideal: {ideal}\nCandidate: {option}\n"
     "Compute the square root of the sum of the squared differences of the three "
     "numbers. Answer with a single number and nothing else."),
]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--config", default="prereg_config.json")
    ap.add_argument("--out", default="sweep.json")
    ap.add_argument("--seed", type=int, default=20260913)
    ap.add_argument("--n", type=int, default=300)
    args = ap.parse_args()

    cfg = json.load(open(args.config, encoding="utf-8"))
    rng = np.random.default_rng(args.seed)
    ideal = np.array(cfg["ideal"], dtype=float)
    d = len(ideal)
    X = rng.uniform(cfg.get("lo", 0.0), cfg.get("hi", 100.0), size=(args.n, d))
    opts = [render_option(x) for x in X]
    ideal_str = render_option(ideal)

    results = []
    with Thermal() as th:
        print(f"[sweep] {len(VARIANTS)} variants, {args.n} options each, "
              f"{th.threads()} host threads")
        # Load the evaluator once and swap the template. Loading a 7B model per
        # variant would be six loads of 15 GB for no reason, and the thermal
        # rule is about the host and not only about the arithmetic.
        sc = LMScorer(cfg)
        for name, eligible, template in VARIANTS:
            sc.template = template
            sc.cache.clear()
            sc.unparsed = 0
            reports = sc.scores(ideal_str, opts, batch=int(cfg.get("batch", 32)))
            r = np.array(reports)
            try:
                cal = calibrate(X, r)
                q_r2 = cal["r2"]
                cond = cal["well_conditioned"]
            except Exception as exc:
                q_r2, cond = float("nan"), False
                cal = {"error": str(exc)}
            forms = competing_forms(X, r, ideal)
            row = {"name": name, "eligible": eligible, "template": template,
                   "quadratic_r2": q_r2, "well_conditioned": cond,
                   "unparsed": sc.unparsed, "forms": forms,
                   "raw": {"reports": list(map(float, reports))}}
            results.append(row)
            print(f"  {name:20s} eligible {str(eligible):5s} "
                  f"quad_r2 {q_r2:+.4f}  best_form {forms['best']:24s} "
                  f"best_r2 {forms[forms['best']]:+.4f}  unparsed {sc.unparsed}")

    eligible = [r for r in results
                if r["eligible"] and np.isfinite(r["quadratic_r2"])]
    winner = max(eligible, key=lambda r: r["quadratic_r2"]) if eligible else None
    rec = {"stage": "prompt_sweep", "provenance": provenance(),
           "selection_rule": "highest quadratic r2 among eligible variants; "
                             "the reversal contrast was not computed",
           "options": X.tolist(), "results": results,
           "winner": winner["name"] if winner else None,
           "winner_r2": winner["quadratic_r2"] if winner else None,
           "meets_gate": bool(winner and winner["quadratic_r2"] > 0.9)}
    json.dump(rec, open(args.out, "w", encoding="utf-8"), indent=1)
    print(f"\nwinner {rec['winner']} at r2 {rec['winner_r2']}, "
          f"calibration gate {'MET' if rec['meets_gate'] else 'NOT MET'}")
    print(f"written to {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
