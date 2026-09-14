# -*- coding: utf-8 -*-
"""C1-C: load the evaluator with distractors, keeping deliberation on.

10.16 killed the previous manipulation. Turning `enable_thinking` off did not
give the evaluator a coarser geometry, it stopped the evaluator comparing the
options: between 89 and 98 percent of its verdicts were position-driven and
between 1 and 11 percent of pairs survived the swap check. A manipulation that
removes the instrument cannot test anything the instrument measures.

This one keeps deliberation on and makes the evaluator carry more.

**The distractors are identical across the two options within a pair.** That is
the whole design. Writing `w` for the metric weights, the quantity that decides
the comparison is

    d(a)^2 - d(b)^2 = sum_i w_i [ (a_i - t_i)^2 - (b_i - t_i)^2 ]

and every distractor coordinate has `a_i = b_i`, so its term is exactly zero.
The correct answer is invariant to the distractors, provably and not
approximately, however many are added and whatever values they take. Anything
the load does to the evaluator's accuracy is the load, not a change in the task.

**What the budget account predicts.** A rank budget discards low-variance
directions. Trading pairs are exactly those whose full-budget order disagrees
with the rank-`k` order, so an evaluator whose effective resolution falls under
load should lose accuracy on trading pairs specifically, and past the halfway
point should invert on them, while within-subspace pairs hold. A noise account
predicts equal degradation in both classes, since they are matched on preference
margin, and predicts accuracy approaching one half from above without crossing.

**Every level is gated before any of it is graded.** That is the lesson of
10.16, where a graded design was built on a condition that had never been put
through the instrument gate the registration already specifies. A load level
whose pairs do not survive the swap check is reported as inadmissible and
carries no verdict, and the ladder stops at the first level that fails rather
than reporting numbers from the wreckage.

Not a graded cell for any registered claim. C1 is unsealed and this is design
work.

    python c1_distractor.py --pilot pilot3_qwen3.json --out distractor.json
"""
from __future__ import annotations

import argparse
import json
import os
import sys

import numpy as np

from c1_budget import ModeChooser, condition_admissible, wilson, MIN_GRADED
from c1_calibrate import assert_budget_usable
from c1_ellm_chooser import preflight_model_pin
from c1_scorer import DECIMALS, LABELS, build_pairs, render_option

# Distractor labels, disjoint from the three real ones so nothing collides.
DISTRACTOR_LABELS = ("S", "T", "U", "V", "W", "X", "Y", "Z",
                     "AB", "AC", "AD", "AE", "AF", "AG", "AH", "AJ")


def render_loaded(x, distractors, labels=LABELS, decimals: int = DECIMALS) -> str:
    """Render the real attributes, then the distractor attributes.

    `distractors` is the same vector for both options of a pair, which is what
    makes the correct answer invariant.
    """
    parts = [f"{l} {v:.{decimals}f}" for l, v in zip(labels, np.asarray(x, float))]
    parts += [f"{l} {v:.{decimals}f}"
              for l, v in zip(DISTRACTOR_LABELS, np.asarray(distractors, float))]
    return ", ".join(parts)


def verify_invariance(pairs, load, rng, lo=0.0, hi=100.0) -> dict:
    """Check in code that the distractors cannot change any correct answer.

    Cheap, and it is the claim the whole design rests on, so it is asserted
    rather than assumed.
    """
    bad = 0
    for p in pairs:
        d = rng.uniform(lo, hi, size=load)
        a = render_loaded(np.asarray(p["a"], float), d)
        b = render_loaded(np.asarray(p["b"], float), d)
        # the distractor substring must be byte-identical in both renderings
        if load and a.split(", ", len(LABELS))[-1] != b.split(", ", len(LABELS))[-1]:
            bad += 1
    return {"checked": len(pairs), "mismatched_distractors": bad}


def run_level(chooser, ideal_vec, pairs, load, rng, lo, hi, batch=32) -> dict:
    """One load level, one class. Both presentation orders, swap check as usual."""
    # The ideal's distractor coordinates are drawn ONCE for the cell and differ
    # from the options', so the distractors are not trivially ignorable: each
    # contributes a real, nonzero term to both distances. It cancels anyway,
    # because the two options share the value, which is the point. A first
    # version reused one pair's vector for the ideal, which made that pair's
    # distractors match the ideal exactly and left the prompt inconsistent
    # across the rest of the cell.
    ideal_d = rng.uniform(lo, hi, size=load) if load else np.zeros(0)
    rows = []
    for p in pairs:
        d = rng.uniform(lo, hi, size=load) if load else np.zeros(0)
        rows.append((render_loaded(np.asarray(p["a"], float), d),
                     render_loaded(np.asarray(p["b"], float), d)))
    ideal_str = render_loaded(ideal_vec, ideal_d)
    fwd = chooser.prefers_first(ideal_str, rows, batch)
    rev = chooser.prefers_first(ideal_str, [(b, a) for a, b in rows], batch)

    # Scored over the FIXED set of every pair in the class, never over the
    # survivors. 10.17 found that conditioning accuracy on swap-consistency
    # inverts the result, because load moves consistency and the pairs it drops
    # are disproportionately ones the evaluator was getting wrong. An estimand
    # whose denominator is itself affected by the manipulation cannot measure
    # the manipulation.
    #
    #   consistent and correct    -> 1.0
    #   consistent and incorrect  -> 0.0
    #   swap-inconsistent         -> 0.5, the evaluator supplied no information
    #
    # Noise and instrument degradation both drive this toward 0.5 from above and
    # neither can push it below. A rank budget inverts trading pairs, so only a
    # budget puts it under one half. The discriminating test survives the fix.
    # Truncation and genuine swap disagreement are DIFFERENT events and were
    # scored identically here, which is how a generation limit came to be
    # reported as a behavioural effect. An answer that never parsed tells us
    # nothing about the evaluator's ordering; an answer that parsed twice and
    # disagreed tells us the verdict depends on presentation. Only the second
    # is where a partial budget would show.
    n = hit = amb = first = nfirst = 0
    truncated = genuine = 0
    scores, strict = [], []
    for p, f, r in zip(pairs, fwd, rev):
        if np.isfinite(f):
            nfirst += 1
            first += int(f > 0.5)
        parsed_both = np.isfinite(f) and np.isfinite(r)
        consistent = parsed_both and (f > 0.5) == (r < 0.5)
        if not consistent:
            amb += 1
            if parsed_both:
                genuine += 1      # parsed twice, disagreed: real order-dependence
            else:
                truncated += 1    # never produced a letter: no information
            scores.append(0.5)
            strict.append(0.0)
            continue
        n += 1
        ok = int(bool(f > 0.5) == bool(p["a_pref_full"]))
        hit += ok
        scores.append(float(ok))
        strict.append(float(ok))
    N = len(pairs)
    sc = np.array(scores, float)
    mean_score = float(sc.mean()) if N else float("nan")
    se = float(sc.std(ddof=1) / np.sqrt(N)) if N > 1 else float("nan")
    return {"load": load, "n": N, "n_graded": n, "ambiguous": amb,
            "ambiguous_truncated": truncated,
            "ambiguous_genuine_disagreement": genuine,
            "finish_reasons": dict(chooser.finish_reasons),
            "escalations": chooser.escalations,
            # the answer-key rate this cell's position statistic must be read
            # against; an unbiased evaluator returns first_position_rate == this
            "a_correct_rate": float(np.mean([bool(p["a_pref_full"]) for p in pairs])),
            # the fixed-set estimand, which is the one to read
            "score_fixed": mean_score,
            "score_fixed_se": se,
            "score_fixed_ci95": (mean_score - 1.96 * se, mean_score + 1.96 * se),
            "score_strict": float(np.mean(strict)) if N else float("nan"),
            "consistency_rate": (n / N) if N else float("nan"),
            # the survivor-conditioned rate, retained only so the bias in 10.17
            # stays visible beside the corrected number
            "q_agree_full_survivors": (hit / n) if n else float("nan"),
            "ci95": wilson(hit, n),
            "first_position_rate": (first / nfirst) if nfirst else float("nan"),
            "mean_reasoning_tokens": (float(np.mean(chooser.reasoning_tokens))
                                      if chooser.reasoning_tokens else 0.0),
            "unparsed": chooser.unparsed, "deadline": chooser.failed}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="prereg_config.json")
    ap.add_argument("--pilot", default="pilot3_qwen3.json")
    ap.add_argument("--out", default="distractor.json")
    ap.add_argument("--seed", type=int, default=20260921)
    ap.add_argument("--n-per-class", type=int, default=64)
    ap.add_argument("--loads", default="0,4,8,16")
    ap.add_argument("--k", type=int, default=1)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    loads = [int(x) for x in args.loads.split(",")]
    if max(loads) > len(DISTRACTOR_LABELS):
        raise SystemExit(f"max load {max(loads)} exceeds {len(DISTRACTOR_LABELS)} labels")

    cfg = json.load(open(args.config, encoding="utf-8"))
    pilot = json.load(open(args.pilot, encoding="utf-8"))
    from c1_atlas_run import box
    LO, HI = box(cfg)
    G = np.array(pilot["calibration"]["G"], float)
    t = np.array(pilot["calibration"]["t"], float)
    ideal_vec = np.array(cfg["ideal"], float)
    rng = np.random.default_rng(args.seed)
    A = np.random.default_rng(pilot["seed"]).uniform(
        LO, HI, size=(int(cfg.get("n_order_pairs", 400)), len(cfg["ideal"])))

    k = args.k
    assert_budget_usable(G, t, A, k, float(cfg.get("spectral_gap_floor", 2.0)),
                         float(cfg.get("discarded_share_floor", 0.05)))
    built = build_pairs(G, t, A, k=k, n_per_class=args.n_per_class, rng=rng,
                        lo=LO, hi=HI, oversample=int(cfg.get("oversample", 400)),
                        pool=int(cfg.get("pool", 3)))
    print(f"[distractor] k={k}  W {len(built['W'])}  T {len(built['T'])}  "
          f"margins {built['margin_mean_W']:.3f} / {built['margin_mean_T']:.3f}")
    for cls in ("W", "T"):
        v = verify_invariance(built[cls], max(loads), np.random.default_rng(0))
        print(f"[distractor] invariance check {cls}: "
              f"{v['mismatched_distractors']} of {v['checked']} pairs differ in "
              f"their distractor block (must be 0)")
        if v["mismatched_distractors"]:
            raise SystemExit("distractors are not identical across options")
    if args.dry_run:
        d = rng.uniform(0, 100, size=max(loads))
        print("\n[distractor] example at max load:")
        print("  ideal:  " + render_loaded(ideal_vec, d))
        print("  opt A:  " + render_loaded(np.asarray(built['T'][0]['a'], float), d))
        print("  opt B:  " + render_loaded(np.asarray(built['T'][0]['b'], float), d))
        print("[distractor] dry run, nothing sent")
        return 0

    from c1_atlas_run import Thermal, provenance
    with Thermal():
        token = os.environ.get("NRP_LLM_TOKEN")
        if not token:
            raise RuntimeError("NRP_LLM_TOKEN absent")
        pin = preflight_model_pin(cfg, token)
        print(f"[distractor] pin verified, {pin['model_id']} created {pin['created']}")

        levels, stopped = {}, None
        for load in loads:
            cell = {}
            for cls in ("W", "T"):
                ch = ModeChooser(cfg, token, {})     # deliberation stays ON
                r = run_level(ch, ideal_vec, built[cls], load,
                              np.random.default_rng(args.seed + load), LO[0], HI[0])
                cell[cls] = r
                print(f"[distractor] load {load:>2} {cls}: score {r['score_fixed']:.4f} "
                      f"[{r['score_fixed_ci95'][0]:.3f}, {r['score_fixed_ci95'][1]:.3f}] "
                      f"over {r['n']}  consistency {r['consistency_rate']:.3f}  "
                      f"survivor-q {r['q_agree_full_survivors']:.4f}  "
                      f"first-pos {r['first_position_rate']:.3f}  "
                      f"reasoning {r['mean_reasoning_tokens']:.0f}")
            adm = condition_admissible(cell)
            cell["admissible"] = adm
            if not adm["admissible"]:
                cell["verdict"] = {"verdict": "NO VERDICT",
                                   "why": "level failed the instrument gate",
                                   "detail": adm["reasons"]}
                print(f"[distractor] load {load} INADMISSIBLE, ladder stops here")
                for w in adm["reasons"]:
                    print(f"             {w}")
                levels[str(load)] = cell
                stopped = load
                break
            cell["class_gap"] = float(cell["W"]["score_fixed"]
                                      - cell["T"]["score_fixed"])
            cell["class_gap_survivors"] = float(
                cell["W"]["q_agree_full_survivors"]
                - cell["T"]["q_agree_full_survivors"])
            cell["T_below_half"] = bool(cell["T"]["score_fixed_ci95"][1] < 0.5)
            print(f"[distractor] load {load:>2} gap {cell['class_gap']:+.4f}  "
                  f"T below half: {cell['T_below_half']}")
            levels[str(load)] = cell

    base = levels.get(str(loads[0]), {})
    rec = {"stage": "distractor", "seed": args.seed, "k": k,
           "provenance": provenance(), "evaluator_pin": pin,
           "grades_no_claim": True, "loads": loads, "stopped_at": stopped,
           "design": ("distractor attributes identical across the two options of "
                      "a pair, so the correct answer is invariant by cancellation; "
                      "deliberation left on"),
           "baseline_gap": base.get("class_gap"), "levels": levels}
    json.dump(rec, open(args.out, "w", encoding="utf-8"), indent=1)

    print("\n[distractor] ladder")
    for load in loads:
        c = levels.get(str(load))
        if c is None:
            print(f"  load {load:>2}  not reached"); continue
        if "class_gap" not in c:
            print(f"  load {load:>2}  INADMISSIBLE"); continue
        print(f"  load {load:>2}  score_W {c['W']['score_fixed']:.4f}  "
              f"score_T {c['T']['score_fixed']:.4f}  gap {c['class_gap']:+.4f}  "
              f"T<0.5 {c['T_below_half']}  "
              f"(survivor gap {c['class_gap_survivors']:+.4f})")
    print(f"distractor written to {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
