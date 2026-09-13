# -*- coding: utf-8 -*-
"""C1-B: manipulate the evaluator's resource, not the stimulus.

Section 10 established that C1 as registered cannot test a rank budget at any
sample size. The reason is not the class construction. It is that C1 never
manipulates a budget. GET's theorem is about fixed actions evaluated under
different budgets; C1 held the budget fixed and changed the actions, rendering
pre-projected numbers and showing those. The evaluator was never
resolution-limited. It read the numbers it was handed, which is why the
agreement rate at the reduced budget came back at exactly 1.0000 in four of six
cells and why every reversal rate fell out of two agreement rates with no
remainder.

This design holds the stimulus fixed and varies the evaluator.

**The manipulation.** Both conditions see the SAME options at full rendering
precision. The deliberate condition runs the evaluator normally, at about 250
reasoning tokens per comparison. The immediate condition sets
`enable_thinking` false through the chat template, which yields zero reasoning
tokens and a two-token answer, verified on the gateway before this was written.
Nothing about the stimulus differs between them.

**Why the outcome is no longer forced.** The fitted metric still says which
pairs are diagnostic, and that is a prediction rather than a label, because
neither condition is shown a projected option. Under the old design the evaluator
was given the rank-k numbers, so agreeing with the rank-k order was automatic.
Here it is given the full numbers in both conditions, and whether a reduced
resource makes it behave as though it had discarded directions is an open
empirical question.

**The graded quantity, and why it discriminates.** On a trading pair the full
order and the rank-k order disagree. Write `q` for the rate at which a condition
agrees with the FULL metric order.

    noise account   a thinner resource is just noisier, so q falls toward 0.5
                    from above and cannot pass it, and it falls equally in both
                    classes because they are matched on preference margin.

    budget account  a thinner resource tracks the rank-k order, which on trading
                    pairs is the opposite of the full order, so q falls BELOW
                    0.5 on trading pairs while staying high on within-subspace
                    pairs, where the two orders agree.

Crossing one half is the discriminating event, and no amount of noise produces
it. The margin match, which under the old design guarded against an alternative
that was not the live one, does the real work here: it equates difficulty so
that a noise account predicts equal degradation in the two classes.

Not a graded cell for any registered claim. C1 is unsealed and this is design
work.

    python c1_budget.py --pilot pilot3_qwen3.json --out budget.json
"""
from __future__ import annotations

import argparse
import json
import os
import sys

import numpy as np

from c1_calibrate import assert_budget_usable
from c1_scorer import build_pairs, render_option
from c1_ellm_chooser import EllmChooser, preflight_model_pin


class ModeChooser(EllmChooser):
    """The pinned chooser with the deliberation switch exposed.

    `extra` is merged into the request body, so the immediate condition differs
    from the deliberate one by exactly one field and nothing else.
    """

    def __init__(self, cfg, token, extra=None):
        super().__init__(cfg, token)
        self.extra = dict(extra or {})
        self.reasoning_seen = []

    def _one(self, ideal, first, second, budget=None, escalated=False):
        import random, re, time, urllib.request
        budget = int(budget or self.max_tokens)
        body = {"model": self.model,
                "messages": [{"role": "user", "content": self.template.format(
                    ideal=ideal, first=first, second=second)}],
                "max_tokens": budget, "temperature": self.temperature}
        body.update(self.extra)
        data = json.dumps(body).encode()
        for attempt in range(self.attempts):
            try:
                req = urllib.request.Request(
                    self.url, data=data,
                    headers={"Authorization": f"Bearer {self.token}",
                             "Content-Type": "application/json"})
                with urllib.request.urlopen(req, timeout=self.timeout) as r:
                    d = json.load(r)
                ch = d["choices"][0]
                rt = ((d.get("usage") or {}).get("completion_tokens_details") or {}
                      ).get("reasoning_tokens", 0)
                content, finish = ch["message"].get("content"), ch.get("finish_reason")
                if finish == "length" and not escalated:
                    self.escalations += 1
                    return self._one(ideal, first, second, budget * 2, True)
                return content, finish, rt
            except Exception:
                if attempt == self.attempts - 1:
                    return None, "deadline", 0
                time.sleep((2 ** attempt) + random.random())
        return None, "deadline", 0


def agreement_with_full(chooser, ideal_str, pairs, batch=32):
    """Rate at which a condition's order matches the FULL metric order.

    Both presentation orders are shown and a pair whose verdict flips on swap is
    dropped, exactly as elsewhere in this experiment. The options are rendered at
    full precision here; no projection is applied to anything the evaluator sees.
    """
    rows = [(render_option(np.asarray(p["a"], float)),
             render_option(np.asarray(p["b"], float))) for p in pairs]
    fwd = chooser.prefers_first(ideal_str, rows, batch)
    rev = chooser.prefers_first(ideal_str, [(b, a) for a, b in rows], batch)
    n = hit = amb = 0
    for p, f, r in zip(pairs, fwd, rev):
        if not (np.isfinite(f) and np.isfinite(r)) or (f > 0.5) != (r < 0.5):
            amb += 1
            continue
        n += 1
        hit += int(bool(f > 0.5) == bool(p["a_pref_full"]))
    return {"n_graded": n, "ambiguous": amb, "n": len(pairs),
            "q_agree_full": (hit / n) if n else float("nan"),
            "mean_reasoning_tokens": (float(np.mean(chooser.reasoning_tokens))
                                      if chooser.reasoning_tokens else 0.0)}


MIN_GRADED = 32          # below this a cell reports no verdict, only a refusal


def condition_admissible(cell, min_graded=MIN_GRADED) -> dict:
    """Is a condition's output usable at all, before any of it is graded?

    This is the check that should have run before C1-B was built. The
    registration already gates the instrument on swap agreement and position
    bias; a condition that fails those is not a coarser evaluator, it is an
    evaluator that has stopped reading the options. Turning deliberation off
    produced exactly that, and it was caught only after a graded design had been
    built on top of it, because the switch had been verified on a single
    hand-made pair rather than against the gate.
    """
    bad = []
    for cls in ("W", "T"):
        r = cell.get(cls, {})
        n, tot = r.get("n_graded", 0), r.get("n", 0)
        keep = (n / tot) if tot else 0.0
        if n < min_graded:
            bad.append(f"{cls}: only {n} of {tot} pairs survived the swap check "
                       f"({keep:.1%}), below the minimum of {min_graded}")
    return {"admissible": not bad, "reasons": bad, "min_graded": min_graded}


def wilson(k, n, z=1.96):
    """Interval for a rate, so the crossing of one half can be judged."""
    if n == 0:
        return (float("nan"), float("nan"))
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * ((p * (1 - p) / n + z * z / (4 * n * n)) ** 0.5) / d
    return (c - h, c + h)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="prereg_config.json")
    ap.add_argument("--pilot", default="pilot3_qwen3.json")
    ap.add_argument("--out", default="budget.json")
    ap.add_argument("--seed", type=int, default=20260920)
    ap.add_argument("--n-per-class", type=int, default=64)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    cfg = json.load(open(args.config, encoding="utf-8"))
    pilot = json.load(open(args.pilot, encoding="utf-8"))
    from c1_atlas_run import box
    LO, HI = box(cfg)
    OVER = int(cfg.get("oversample", 400))
    POOL = int(cfg.get("pool", 3))
    G = np.array(pilot["calibration"]["G"], float)
    t = np.array(pilot["calibration"]["t"], float)
    ideal_str = render_option(np.array(cfg["ideal"], float))
    rng = np.random.default_rng(args.seed)
    A = np.random.default_rng(pilot["seed"]).uniform(
        LO, HI, size=(int(cfg.get("n_order_pairs", 400)), len(cfg["ideal"])))

    built = {}
    for k in (1, 2):
        assert_budget_usable(G, t, A, k, float(cfg.get("spectral_gap_floor", 2.0)),
                             float(cfg.get("discarded_share_floor", 0.05)))
        b = build_pairs(G, t, A, k=k, n_per_class=args.n_per_class, rng=rng,
                        lo=LO, hi=HI, oversample=OVER, pool=POOL)
        built[k] = b
        print(f"[budget] k={k}  W {len(b['W'])}  T {len(b['T'])}  "
              f"margin W {b['margin_mean_W']:.3f} T {b['margin_mean_T']:.3f}")
    if args.dry_run:
        print("[budget] dry run, nothing sent")
        return 0

    from c1_atlas_run import Thermal, provenance
    with Thermal():
        token = os.environ.get("NRP_LLM_TOKEN")
        if not token:
            raise RuntimeError("NRP_LLM_TOKEN absent")
        pin = preflight_model_pin(cfg, token)
        print(f"[budget] pin verified, {pin['model_id']} created {pin['created']}")

        conditions = {
            "deliberate": {},
            "immediate": {"chat_template_kwargs": {"enable_thinking": False}},
        }
        cells = {}
        for k in (1, 2):
            cells[str(k)] = {}
            for cond, extra in conditions.items():
                ch = ModeChooser(cfg, token, extra)
                cells[str(k)][cond] = {}
                for cls in ("W", "T"):
                    r = agreement_with_full(ch, ideal_str, built[k][cls])
                    hit = int(round(r["q_agree_full"] * r["n_graded"])) if r["n_graded"] else 0
                    r["ci95"] = wilson(hit, r["n_graded"])
                    cells[str(k)][cond][cls] = r
                    print(f"[budget] k={k} {cond:>10} {cls}: q {r['q_agree_full']:.4f} "
                          f"[{r['ci95'][0]:.3f}, {r['ci95'][1]:.3f}] "
                          f"n {r['n_graded']}/{r['n']}  "
                          f"reasoning {r['mean_reasoning_tokens']:.0f}")
                cells[str(k)][cond]["unparsed"] = ch.unparsed
                cells[str(k)][cond]["deadline"] = ch.failed
            d = cells[str(k)]
            adm = {c: condition_admissible(d[c]) for c in conditions}
            d["admissibility"] = adm
            # The deliberate baseline gap is a confound on the class-gap
            # statistic and is recorded whether or not a verdict follows.
            d["baseline_gap_deliberate"] = float(
                d["deliberate"]["W"]["q_agree_full"]
                - d["deliberate"]["T"]["q_agree_full"])
            if not all(a["admissible"] for a in adm.values()):
                d["verdict"] = {
                    "verdict": "NO VERDICT",
                    "why": "a condition failed the instrument gate",
                    "detail": {c: a["reasons"] for c, a in adm.items() if a["reasons"]}}
                print(f"[budget] k={k} NO VERDICT, a condition failed the "
                      f"instrument gate")
                for c, a in adm.items():
                    for why in a["reasons"]:
                        print(f"           {c}: {why}")
                continue
            qT = d["immediate"]["T"]["q_agree_full"]
            qW = d["immediate"]["W"]["q_agree_full"]
            d["verdict"] = {
                "verdict": "graded",
                "q_T_immediate": qT, "q_W_immediate": qW,
                "class_gap": float(qW - qT),
                "gap_change_from_baseline":
                    float((qW - qT) - d["baseline_gap_deliberate"]),
                "T_below_half": bool(d["immediate"]["T"]["ci95"][1] < 0.5),
                "reading": ("budget: the thinner resource tracks the rank-k order"
                            if d["immediate"]["T"]["ci95"][1] < 0.5 else
                            "no budget effect distinguishable from noise")}
            print(f"[budget] k={k} VERDICT  q_T {qT:.4f}  q_W {qW:.4f}  "
                  f"gap {qW-qT:+.4f}  T below half: {d['verdict']['T_below_half']}")

    rec = {"stage": "budget", "seed": args.seed, "provenance": provenance(),
           "evaluator_pin": pin, "grades_no_claim": True,
           "design": ("stimulus identical in both conditions at full rendering "
                      "precision; the manipulation is enable_thinking"),
           "cells": cells}
    json.dump(rec, open(args.out, "w", encoding="utf-8"), indent=1)
    print(f"budget written to {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
