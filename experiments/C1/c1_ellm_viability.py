# -*- coding: utf-8 -*-
"""Can an NRP-hosted model do what Qwen2.5-7B could not?

Two failure modes killed the local evaluator, and this asks both questions of a
hosted model before any redesign is proposed.

  A. Distance. Does the squared report follow a quadratic form in the option?
     The local model scored r2 0.0946, and scored worse when handed the formula.
  B. Comparison. Does it choose by content or by layout? The local model chose
     the first-shown option 81.75 percent of the time.

This is a viability check and not a gate. It runs few items per model, grades
nothing, and its only output is whether a full instrument is worth building on a
given model.

Fair use is respected as the runbook states it. Concurrency is capped per model,
`max_tokens` stays small, and failures retry with exponential backoff. The token
is read from the environment on Atlas and never printed.

    python c1_ellm_viability.py --models qwen3 gpt-oss --n 80
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import json
import os
import random
import re
import sys
import time
import urllib.error
import urllib.request

import numpy as np

BASE = "https://ellm.nrp-nautilus.io/v1"
# Per-model concurrency from the fair-use table. Unknown models get the floor.
CAPS = {"kimi": 2, "glm-5": 2, "minimax-m2": 8, "qwen3-small": 8, "gemma": 8,
        "gemma-small": 8, "gemma4-small": 8, "gemma4-12b": 8,
        "gemma-small-e4b": 8, "deepseek-v4-flash": 8,
        "qwen3": 16, "gpt-oss": 16}

DIST_PROMPT = ("Two points in three dimensions.\nA: {ideal}\nB: {option}\n"
               "What is the straight-line distance between A and B? "
               "Answer with a single number and nothing else.")
PAIR_PROMPT = ("The ideal is: {ideal}\nOption A: {first}\nOption B: {second}\n"
               "Which option is closer to the ideal? Answer with a single "
               "letter, A or B.")


def render(x) -> str:
    return ", ".join(f"{l} {v:.1f}" for l, v in zip(("P", "Q", "R"), np.asarray(x, float)))


def ask(model: str, prompt: str, token: str, max_tokens: int = 512,
        tries: int = 5) -> tuple[str | None, str | None, int]:
    """Returns (content, finish_reason, reasoning_tokens).

    A reasoning model spends the token budget on reasoning before it writes
    content. The first run of this probe gave 8 tokens, which is right for a
    non-reasoning 7B and starves a reasoning model completely, so qwen3 returned
    content None with finish_reason length on every one of 80 items. That was the
    probe's defect and not the model's, and the budget is now large enough for
    reasoning plus an answer.
    """
    body = json.dumps({"model": model,
                       "messages": [{"role": "user", "content": prompt}],
                       "max_tokens": max_tokens, "temperature": 0}).encode()
    for attempt in range(tries):
        try:
            req = urllib.request.Request(
                BASE + "/chat/completions", data=body,
                headers={"Authorization": f"Bearer {token}",
                         "Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=300) as r:
                d = json.load(r)
            ch = d["choices"][0]
            rt = ((d.get("usage") or {}).get("completion_tokens_details") or {}
                  ).get("reasoning_tokens", 0)
            return ch["message"].get("content"), ch.get("finish_reason"), rt
        except Exception:
            if attempt == tries - 1:
                return None, "exception", 0
            time.sleep((2 ** attempt) + random.random())
    return None, "exhausted", 0


def run_batch(model: str, prompts: list[str], token: str,
              max_tokens: int = 512) -> list:
    cap = CAPS.get(model, 4)
    out: list = [None] * len(prompts)
    with cf.ThreadPoolExecutor(max_workers=cap) as ex:
        futs = {ex.submit(ask, model, p, token, max_tokens): i
                for i, p in enumerate(prompts)}
        for f in cf.as_completed(futs):
            out[futs[f]] = f.result()
    return out


def quadratic_r2(X: np.ndarray, r: np.ndarray) -> float:
    from c1_calibrate import design
    keep = np.isfinite(r)
    X, r = X[keep], r[keep]
    if len(r) < 20:
        return float("nan")
    A = design(X)
    beta, *_ = np.linalg.lstsq(A, r ** 2, rcond=None)
    resid = r ** 2 - A @ beta
    denom = float(np.sum((r ** 2 - np.mean(r ** 2)) ** 2))
    return float(1.0 - np.sum(resid ** 2) / denom) if denom > 0 else float("nan")


def check(model: str, token: str, n: int, seed: int,
          max_tokens: int = 512) -> dict:
    rng = np.random.default_rng(seed)
    ideal = np.array([50.0, 50.0, 50.0])
    istr = render(ideal)

    X = rng.uniform(0, 100, size=(n, 3))
    t0 = time.time()
    raw = run_batch(model, [DIST_PROMPT.format(ideal=istr, option=render(x)) for x in X],
                    token, max_tokens)
    reps, finishes, rtoks = [], [], []
    for s, fin, rt in raw:
        finishes.append(fin); rtoks.append(rt)
        m = re.search(r"-?\d+(?:\.\d+)?", s.replace(",", "")) if s else None
        reps.append(float(m.group(0)) if m else float("nan"))
    reps = np.array(reps)
    r2 = quadratic_r2(X, reps)
    dist_secs = time.time() - t0

    A = rng.uniform(0, 100, size=(n, 3))
    B = rng.uniform(0, 100, size=(n, 3))
    prompts = ([PAIR_PROMPT.format(ideal=istr, first=render(a), second=render(b))
                for a, b in zip(A, B)]
               + [PAIR_PROMPT.format(ideal=istr, first=render(b), second=render(a))
                  for a, b in zip(A, B)])
    t1 = time.time()
    ans = run_batch(model, prompts, token, max_tokens)

    def letter(item):
        s = item[0]
        m = re.search(r"\b([AB])\b", s.upper()) if s else None
        return m.group(1) if m else None

    fwd = [letter(s) for s in ans[:n]]
    rev = [letter(s) for s in ans[n:]]
    first_chosen = sum(1 for x in fwd if x == "A") + sum(1 for x in rev if x == "A")
    counted = sum(1 for x in fwd if x) + sum(1 for x in rev if x)
    agree = sum(1 for f, r in zip(fwd, rev) if f and r and (f == "A") == (r == "B"))
    usable = sum(1 for f, r in zip(fwd, rev) if f and r)
    p = (first_chosen / counted) if counted else float("nan")
    a = (agree / usable) if usable else float("nan")

    return {"model": model, "n": n,
            "distance": {"quadratic_r2": r2,
                         "parsed": int(np.isfinite(reps).sum()),
                         "truncated": int(sum(1 for f in finishes if f == "length")),
                         "mean_reasoning_tokens": float(np.mean(rtoks)) if rtoks else 0.0,
                         "sample_raw": [str(x[0])[:80] for x in raw[:3]],
                         "seconds": round(dist_secs, 1)},
            "comparison": {"first_position_rate": p, "agreement_rate": a,
                           "pure_bias_agreement": (2 * p * (1 - p)) if np.isfinite(p) else float("nan"),
                           "usable_pairs": usable,
                           "seconds": round(time.time() - t1, 1)},
            "verdict": {"distance_ok": bool(np.isfinite(r2) and r2 >= 0.90),
                        "position_ok": bool(np.isfinite(p) and abs(p - 0.5) <= 0.15)}}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--models", nargs="+", required=True)
    ap.add_argument("--n", type=int, default=80)
    ap.add_argument("--seed", type=int, default=20260913)
    ap.add_argument("--max-tokens", type=int, default=512,
                    help="must cover reasoning plus the answer on thinking models")
    ap.add_argument("--out", default="ellm_viability.json")
    args = ap.parse_args()

    token = os.environ.get("NRP_LLM_TOKEN")
    if not token:
        print("NRP_LLM_TOKEN not in the environment; source /home/claude/.primer.env",
              file=sys.stderr)
        return 2

    rows = []
    for m in args.models:
        print(f"[ellm] {m}, concurrency {CAPS.get(m, 4)}", flush=True)
        try:
            r = check(m, token, args.n, args.seed, args.max_tokens)
        except Exception as exc:
            r = {"model": m, "error": f"{type(exc).__name__}: {exc}"}
        rows.append(r)
        # Write after every model rather than at the end. The qwen3 result of
        # the previous run survived only in a log, because the process was
        # stopped while a later model hung and the JSON had not been written
        # yet. A record that exists only once every model has finished is a
        # record that a single stall can erase.
        json.dump({"base": BASE, "results": rows, "complete": False},
                  open(args.out, "w", encoding="utf-8"), indent=1)
        if "error" in r:
            print(f"  ERROR {r['error']}", flush=True)
        else:
            d, c, v = r["distance"], r["comparison"], r["verdict"]
            print(f"  distance   quad_r2 {d['quadratic_r2']:+.4f}  "
                  f"parsed {d['parsed']}/{args.n}  {d['seconds']}s  "
                  f"{'OK' if v['distance_ok'] else 'MISS'}", flush=True)
            print(f"  comparison first-pos {c['first_position_rate']:.4f}  "
                  f"agree {c['agreement_rate']:.4f}  "
                  f"pure-bias-would-give {c['pure_bias_agreement']:.4f}  "
                  f"{'OK' if v['position_ok'] else 'MISS'}", flush=True)
    json.dump({"base": BASE, "results": rows, "complete": True},
              open(args.out, "w", encoding="utf-8"), indent=1)
    print(f"written to {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
