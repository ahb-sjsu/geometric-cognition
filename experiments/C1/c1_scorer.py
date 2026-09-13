# -*- coding: utf-8 -*-
"""C1 harness: render options to an evaluator, build the two pair classes, run cells.

The reading discipline is GET's G3 unchanged. The evaluator is shown an ideal and
one option and asked how far the option is from the ideal. It answers with a
number, read as the first number in a greedy generation of at most twelve tokens.
Preference compares two reported distances. Equal reports and unparsable reports
are indifference. Every distinct rendered option is scored once per cell.

What this file adds to G3 is the second and third dimension and the two pair
classes that live in them. A W pair differs only inside the retained subspace. A
T pair trades a retained direction against a discarded one, and is admitted only
when the fitted metric says the full-budget order and the rank-k order disagree.
The metric that selects T pairs was estimated on a disjoint calibration block, so
the selection is a prediction and not a fit.

Classes are matched bin by bin on full-budget preference margin. Under a noise
account the two classes then have equal predicted reversal rates, so the contrast
between them is the only quantity the gate grades.

    python c1_scorer.py --selftest            # synthetic evaluator, no GPU
    python c1_scorer.py --cell --config ...   # one cell on Atlas GPU 1
"""
from __future__ import annotations

import argparse
import json
import re
import sys

import numpy as np

from c1_calibrate import project, retained, sqrtm_psd

LABELS = ("P", "Q", "R")          # neutral tokens, fixed at sealing
DECIMALS = 1


# ---------------------------------------------------------------- rendering

def render_option(x, labels=LABELS, decimals: int = DECIMALS) -> str:
    return ", ".join(f"{l} {v:.{decimals}f}" for l, v in zip(labels, np.asarray(x, float)))


def round_to_render(x, decimals: int = DECIMALS) -> np.ndarray:
    """What the evaluator actually sees. Pair construction uses this so that two
    options which render identically are never admitted as a pair."""
    return np.round(np.asarray(x, float), decimals)


# ---------------------------------------------------------------- evaluators

class SyntheticScorer:
    """Exact quadratic reporter with a rounding grid. Used by the self-test.

    It reports the true distance under a known metric, rounded to `grid`. It has
    no budget of its own, so any reversal it shows under a rendered projection is
    the projection's and not the reporter's.
    """

    def __init__(self, G, t, grid: float = 0.0, noise: float = 0.0, seed: int = 0):
        self.G, self.t = np.asarray(G, float), np.asarray(t, float)
        self.grid, self.noise = float(grid), float(noise)
        self.rng = np.random.default_rng(seed)
        self.unparsed = 0

    def scores(self, ideal_str: str, options, **_) -> list[float]:
        out = []
        for s in options:
            x = np.array([float(v) for v in re.findall(r"-?\d+(?:\.\d+)?", s)])
            dx = x - self.t
            r = float(np.sqrt(dx @ self.G @ dx))
            if self.noise:
                r += float(self.rng.normal(0.0, self.noise))
            if self.grid:
                r = round(r / self.grid) * self.grid
            out.append(r)
        return out


class LMScorer:
    """A causal language model as the evaluator. G3's instrument, three attributes."""

    def __init__(self, cfg: dict):
        import torch
        from transformers import AutoModelForCausalLM, AutoTokenizer
        self.torch = torch
        mid = cfg["model_id"]
        self.tok = AutoTokenizer.from_pretrained(mid)
        self.model = AutoModelForCausalLM.from_pretrained(
            mid, device_map={"": 0}, dtype=torch.bfloat16).eval()
        self.template = cfg["scorer_prompt_template"]
        self.max_new = int(cfg.get("max_new_tokens", 12))
        self.chat = bool(cfg.get("use_chat_template", True)) and self.tok.chat_template is not None
        self.cache: dict[tuple[str, str], tuple[float, str]] = {}
        self.unparsed = 0

    def _prompt(self, ideal: str, option: str) -> str:
        user = self.template.format(ideal=ideal, option=option)
        if self.chat:
            return self.tok.apply_chat_template(
                [{"role": "user", "content": user}], tokenize=False, add_generation_prompt=True)
        return user

    def scores(self, ideal_str: str, options, batch: int = 32) -> list[float]:
        torch = self.torch
        todo = [v for v in dict.fromkeys(options) if (ideal_str, v) not in self.cache]
        self.tok.padding_side = "left"
        if self.tok.pad_token is None:
            self.tok.pad_token = self.tok.eos_token
        for i in range(0, len(todo), batch):
            chunk = todo[i:i + batch]
            enc = self.tok([self._prompt(ideal_str, v) for v in chunk],
                           return_tensors="pt", padding=True).to(self.model.device)
            with torch.no_grad():
                gen = self.model.generate(**enc, max_new_tokens=self.max_new, do_sample=False,
                                          pad_token_id=self.tok.pad_token_id)
            for v, row in zip(chunk, gen[:, enc.input_ids.shape[1]:]):
                text = self.tok.decode(row, skip_special_tokens=True)
                m = re.search(r"-?\d+(?:\.\d*)?", text.replace(",", ""))
                if m:
                    self.cache[(ideal_str, v)] = (float(m.group(0).rstrip(".")), text)
                else:
                    self.cache[(ideal_str, v)] = (float("nan"), text)
                    self.unparsed += 1
        return [self.cache[(ideal_str, v)][0] for v in options]


# ---------------------------------------------------------------- pair build

def _dist(x, G, t) -> float:
    dx = np.asarray(x, float) - np.asarray(t, float)
    return float(np.sqrt(dx @ np.asarray(G, float) @ dx))


def build_pairs(G, t, X_cal, k: int, n_per_class: int, rng, *,
                lo: float = 0.0, hi: float = 100.0,
                min_component: float = 0.5, n_bins: int = 8,
                oversample: int = 400, pool: int = 3) -> dict:
    """Draw W and T candidates, then match them bin by bin on full-budget margin.

    A T candidate is admitted only when the fitted metric says the rank-k order
    disagrees with the full-budget order. A W candidate is admitted only when the
    whitened difference lies in the retained subspace to within `min_component`
    in the discarded directions.
    """
    G, t = np.asarray(G, float), np.asarray(t, float)
    res = retained(G, t, X_cal, k)
    Pi = np.array(res["Pi_whitened"])
    d = G.shape[0]
    Gh, Ghi = sqrtm_psd(G), sqrtm_psd(G, inverse=True)
    I = np.eye(d)

    def in_box(x):
        return bool(np.all(x >= lo) and np.all(x <= hi))

    W, T = [], []
    for _ in range(oversample * n_per_class):
        a = rng.uniform(lo, hi, size=d)
        u = rng.normal(size=d)
        # within-retained: difference has no discarded component
        wdir = (u @ Gh) @ Pi @ Ghi
        b = a + wdir * rng.uniform(0.5, 6.0)
        # trading: retained and discarded components both present
        tdir = (u @ Gh) @ Pi @ Ghi + (rng.normal(size=d) @ Gh) @ (I - Pi) @ Ghi
        b2 = a + tdir * rng.uniform(0.5, 6.0)

        for cand, bucket, is_w in ((b, W, True), (b2, T, False)):
            if not in_box(cand):
                continue
            ar, br = round_to_render(a), round_to_render(cand)
            if np.array_equal(ar, br):
                continue
            diff_w = (br - ar) @ Gh
            disc = float(np.linalg.norm(diff_w @ (I - Pi)))
            ret = float(np.linalg.norm(diff_w @ Pi))
            if is_w and disc > min_component:
                continue
            if (not is_w) and (disc < min_component or ret < min_component):
                continue
            da, db = _dist(ar, G, t), _dist(br, G, t)
            pa = project(ar, G, t, Pi)
            pb = project(br, G, t, Pi)
            dka, dkb = _dist(pa, G, t), _dist(pb, G, t)
            flip = (da < db) != (dka < dkb)
            if is_w and flip:
                continue          # a W pair the metric says flips is not a W pair
            if (not is_w) and not flip:
                continue          # a T pair must be one the metric says flips
            bucket.append({"a": ar.tolist(), "b": br.tolist(),
                           "margin": abs(da - db),
                           "a_pref_full": bool(da < db),
                           "a_render_k": render_option(round_to_render(pa)),
                           "b_render_k": render_option(round_to_render(pb))})
            if len(W) >= n_per_class * pool and len(T) >= n_per_class * pool:
                break
        if len(W) >= n_per_class * pool and len(T) >= n_per_class * pool:
            break

    matched = _match_margins(W, T, n_per_class, n_bins)
    matched["retained"] = res
    return matched


def _match_margins(W, T, n_per_class, n_bins):
    """Bin by full-budget margin and admit equal counts per bin from each class."""
    if not W or not T:
        return {"W": [], "T": [], "bins": [], "note": "a class came out empty"}
    allm = np.array([p["margin"] for p in W + T])
    edges = np.quantile(allm, np.linspace(0, 1, n_bins + 1))
    edges[-1] += 1e-9

    def binof(p):
        return int(np.clip(np.searchsorted(edges, p["margin"], side="right") - 1, 0, n_bins - 1))

    wb, tb = {}, {}
    for p in W:
        wb.setdefault(binof(p), []).append(p)
    for p in T:
        tb.setdefault(binof(p), []).append(p)

    Wm, Tm, report = [], [], []
    per = max(1, n_per_class // n_bins)
    for b in range(n_bins):
        take = min(len(wb.get(b, [])), len(tb.get(b, [])), per)
        Wm += wb.get(b, [])[:take]
        Tm += tb.get(b, [])[:take]
        report.append({"bin": b, "lo": float(edges[b]), "hi": float(edges[b + 1]), "taken": take})
    return {"W": Wm, "T": Tm, "bins": report,
            "margin_mean_W": float(np.mean([p["margin"] for p in Wm])) if Wm else float("nan"),
            "margin_mean_T": float(np.mean([p["margin"] for p in Tm])) if Tm else float("nan")}


# ---------------------------------------------------------------- the cell

def run_cell(scorer, ideal, pairs, budget_key: str) -> dict:
    """Reversal rate of one class at one budget, graded against the evaluator's
    own full-budget order rather than against the fitted metric's prediction."""
    ideal_str = render_option(ideal)
    full = [render_option(p["a"]) for p in pairs] + [render_option(p["b"]) for p in pairs]
    fr = scorer.scores(ideal_str, full)
    n = len(pairs)
    ra_full, rb_full = fr[:n], fr[n:]

    if budget_key == "full":
        ka = [render_option(p["a"]) for p in pairs]
        kb = [render_option(p["b"]) for p in pairs]
    else:
        ka = [p["a_render_k"] for p in pairs]
        kb = [p["b_render_k"] for p in pairs]
    kr = scorer.scores(ideal_str, ka + kb)
    ra_k, rb_k = kr[:n], kr[n:]

    rev = indiff = undefined = 0
    for i in range(n):
        af, bf, ak, bk = ra_full[i], rb_full[i], ra_k[i], rb_k[i]
        if not all(np.isfinite([af, bf, ak, bk])) or af == bf:
            undefined += 1
            continue
        if ak == bk:
            indiff += 1
            continue
        if (af < bf) != (ak < bk):
            rev += 1
    graded = n - undefined
    return {"n": n, "graded": graded, "reversals": rev, "indifferent": indiff,
            "undefined_reference": undefined,
            "reversal_rate": (rev / graded) if graded else float("nan")}


def rendering_ceiling(pairs, G, t, Pi) -> dict:
    """The highest T reversal rate an exact evaluator could reach.

    A T pair is admitted because the EXACT rank-k projection reverses its order.
    The evaluator is shown the projection ROUNDED to the rendering precision, and
    rounding returns a small share of those pairs to their original order. An
    evaluator that implements the theory perfectly therefore cannot reverse every
    T pair, and a bar set at 1.0 could not be met by anything.

    The pilot measures this on its own draw and the registration's margin is
    bounded below it.
    """
    lost = 0
    for q in pairs:
        pa, pb = project(q["a"], G, t, Pi), project(q["b"], G, t, Pi)
        exact = _dist(pa, G, t) < _dist(pb, G, t)
        rendered = _dist(round_to_render(pa), G, t) < _dist(round_to_render(pb), G, t)
        if exact != rendered:
            lost += 1
    n = len(pairs)
    return {"n": n, "lost_to_rounding": lost,
            "share_lost": (lost / n) if n else float("nan"),
            "ceiling": (1.0 - lost / n) if n else float("nan")}


def selftest(seed: int = 20260913) -> dict:
    """A synthetic evaluator with the calibration's own metric.

    By construction it must reverse no W pair and must reverse T pairs, because
    a T pair is admitted only when the rank-k order disagrees. A failure here is
    a bug in the harness and not a finding about any evaluator.
    """
    rng = np.random.default_rng(seed)
    d = 3
    B = rng.normal(size=(d, d))
    G = B @ B.T + 0.5 * np.eye(d)
    G *= d / np.trace(G)
    t = np.array([50.0, 50.0, 50.0])
    X_cal = rng.uniform(0, 100, size=(600, d))

    pairs = build_pairs(G, t, X_cal, k=2, n_per_class=64, rng=rng)
    sc = SyntheticScorer(G, t)
    Pi = np.array(pairs["retained"]["Pi_whitened"])
    ceil_T = rendering_ceiling(pairs["T"], G, t, Pi)
    out = {
        "n_W": len(pairs["W"]), "n_T": len(pairs["T"]),
        "margin_mean_W": pairs["margin_mean_W"], "margin_mean_T": pairs["margin_mean_T"],
        "discarded_trace_share": pairs["retained"]["discarded_trace_share"],
        "rendering_ceiling_T": ceil_T,
        "W": run_cell(sc, t, pairs["W"], "k"),
        "T": run_cell(sc, t, pairs["T"], "k"),
    }
    out["contrast"] = out["T"]["reversal_rate"] - out["W"]["reversal_rate"]
    # An exact evaluator reverses no W pair and reverses every T pair the
    # rendering still flips. Anything less is a harness bug.
    out["pass"] = bool(out["n_W"] > 0 and out["n_T"] > 0
                       and out["W"]["reversal_rate"] == 0.0
                       and abs(out["T"]["reversal_rate"] - ceil_T["ceiling"]) < 1e-9
                       and out["discarded_trace_share"] >= 0.05)
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--config")
    ap.add_argument("--out")
    args = ap.parse_args()

    if args.selftest:
        r = selftest()
        print("C1 harness self-test, synthetic evaluator")
        print(f"  pairs                 W {r['n_W']}  T {r['n_T']}")
        print(f"  margin mean           W {r['margin_mean_W']:.3f}  T {r['margin_mean_T']:.3f}")
        print(f"  discarded trace share {r['discarded_trace_share']:.4f}")
        print(f"  reversal rate         W {r['W']['reversal_rate']:.4f}  "
              f"T {r['T']['reversal_rate']:.4f}")
        print(f"  contrast T minus W    {r['contrast']:.4f}")
        c = r['rendering_ceiling_T']
        print(f"  rendering ceiling on T {c['ceiling']:.4f} "
              f"({c['lost_to_rounding']} of {c['n']} returned to order by rounding)")
        print(f"  verdict               {'PASS' if r['pass'] else 'FAIL'}")
        if args.out:
            json.dump(r, open(args.out, "w", encoding="utf-8"), indent=1)
        return 0 if r["pass"] else 1

    ap.error("a graded cell needs --config and runs on Atlas, see PREREG-C1 section 8")
    return 2


if __name__ == "__main__":
    sys.exit(main())
