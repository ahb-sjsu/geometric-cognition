# -*- coding: utf-8 -*-
"""C2 pair construction: three classes, matched on decision SNR.

The C2 cold reread found that matching on geometric margin does not match the
quantity that governs order-dependence. Writing `c_i` for each attribute's
contribution to `d(a)^2 - d(b)^2`, the margin is `|sum c_i|` and the thing that
decides a flip under per-attribute noise is

    SNR = |sum c_i| / sqrt(sum c_i^2)

At matched margin the two C1 classes had SNR 1.041 and 0.719, because a trading
pair's decisive margin is the small residue of large opposing terms. A model with
no budget at all, in which load is only rising per-attribute noise, then
reproduces the entire registered signature. Matching on margin was the defect.

Three classes, not two. The reread's second finding was that `build_pairs`
generates and discards the control that separates the accounts:

    W   difference lies in the retained subspace, order preserved under
        projection. Low complexity, budget says no reversal.
    N   difference has a large discarded component, order PRESERVED under
        projection. High complexity, budget says no reversal.
    T   difference has a large discarded component, order FLIPS under
        projection. High complexity, budget says reversal.

A rank budget predicts N behaves like W. A complexity or cancellation account
predicts N behaves like T. The two-class design cannot separate those; this one
can, in the same run.

Matching is on SNR by quantile bin, with equal counts drawn from each class in
each bin, and the achieved match is asserted rather than described.
"""
from __future__ import annotations

import sys

import numpy as np

sys.path.insert(0, r"C:\source\geometric-cognition\experiments\C1")

from c1_calibrate import project, sqrtm_psd          # noqa: E402
from c1_scorer import round_to_render                # noqa: E402


def contributions(a, b, G, t) -> np.ndarray:
    """Per-attribute contributions `c_i` to `d(a)^2 - d(b)^2`.

    For a diagonal metric this is `w_i[(a_i-t_i)^2 - (b_i-t_i)^2]`. The general
    form keeps the cross terms, so it is correct for any positive definite `G`.
    """
    a, b, t = np.asarray(a, float), np.asarray(b, float), np.asarray(t, float)
    ua, ub = a - t, b - t
    Ga, Gb = G @ ua, G @ ub
    return ua * Ga - ub * Gb


def snr(a, b, G, t) -> float:
    c = contributions(a, b, G, t)
    denom = float(np.sqrt((c ** 2).sum()))
    return float(abs(c.sum()) / denom) if denom > 1e-12 else float("inf")


def covariates(a, b, G, t, Pi=None) -> dict:
    """The quantities the reread required be adjusted for, not merely reported."""
    a, b, t = np.asarray(a, float), np.asarray(b, float), np.asarray(t, float)
    c = contributions(a, b, G, t)
    pos, neg = c[c > 0].sum(), -c[c < 0].sum()
    diff = b - a
    n = np.linalg.norm(diff)
    return {"snr": snr(a, b, G, t),
            "log_noise_scale": float(np.log(np.sqrt((c ** 2).sum()) + 1e-12)),
            "opposing_mass": float(min(pos, neg) / max(pos, neg)) if max(pos, neg) > 0 else 0.0,
            "displacement": float(n),
            # how concentrated the difference is on one attribute; W pairs are
            # all parallel to one fixed direction at k=1 and this records it
            "direction_concentration": float(np.max(np.abs(diff)) / n) if n > 1e-12 else 1.0,
            "min_distance_to_ideal": float(min(np.sqrt(np.asarray(a - t) @ G @ (a - t)),
                                               np.sqrt(np.asarray(b - t) @ G @ (b - t)))),
            "mean_magnitude": float(np.mean(np.abs(np.concatenate([a, b]))))}


def build_three_classes(G, t, X_cal, k, n_per_class, rng, *, lo, hi,
                        min_component=0.5, n_bins=8, oversample=4000,
                        pool=16, snr_tol=0.05):
    """W, N and T, matched on SNR by quantile bin.

    `snr_tol` is the registered tolerance on the achieved match between any two
    classes. It is asserted before the pairs are returned, so a draw that misses
    it stops the run instead of being discovered afterwards.
    """
    from c1_calibrate import retained
    G, t = np.asarray(G, float), np.asarray(t, float)
    res = retained(G, t, X_cal, k)
    Pi = np.array(res["Pi_whitened"], float)
    d = G.shape[0]
    Gh, Ghi = sqrtm_psd(G), sqrtm_psd(G, inverse=True)
    I = np.eye(d)
    lo, hi = np.asarray(lo, float), np.asarray(hi, float)

    def dist(x):
        dx = np.asarray(x, float) - t
        return float(np.sqrt(dx @ G @ dx))

    W, N, T = [], [], []
    target = n_per_class * pool
    for _ in range(oversample * n_per_class):
        if len(W) >= target and len(N) >= target and len(T) >= target:
            break
        a = rng.uniform(lo, hi, size=d)
        u = rng.normal(size=d)
        within = (u @ Gh) @ Pi @ Ghi
        across = (u @ Gh) @ Pi @ Ghi + (rng.normal(size=d) @ Gh) @ (I - Pi) @ Ghi
        for cand, is_within in ((a + within * rng.uniform(0.5, 6.0), True),
                                (a + across * rng.uniform(0.5, 6.0), False)):
            if not (np.all(cand >= lo) and np.all(cand <= hi)):
                continue
            ar, br = round_to_render(a), round_to_render(cand)
            if np.array_equal(ar, br):
                continue
            dw = (br - ar) @ Gh
            disc = float(np.linalg.norm(dw @ (I - Pi)))
            ret = float(np.linalg.norm(dw @ Pi))
            da, db = dist(ar), dist(br)
            pa, pb = project(ar, G, t, Pi), project(br, G, t, Pi)
            flip = (da < db) != (dist(pa) < dist(pb))
            rec = {"a": ar.tolist(), "b": br.tolist(),
                   "a_pref_full": bool(da < db),
                   "a_pref_k": bool(dist(pa) < dist(pb)),
                   "margin": abs(da - db), **covariates(ar, br, G, t, Pi)}
            if is_within:
                if disc > min_component or flip:
                    continue
                if len(W) < target:
                    W.append(rec)
            else:
                if disc < min_component or ret < min_component:
                    continue
                bucket = T if flip else N
                if len(bucket) < target:
                    bucket.append(rec)

    matched = _match_on_snr(W, N, T, n_per_class, n_bins)
    matched["retained"] = res
    if matched["W"] and matched["N"] and matched["T"]:
        means = {c: float(np.mean([p["snr"] for p in matched[c]])) for c in "WNT"}
        worst = max(abs(means[x] - means[y]) for x in "WNT" for y in "WNT")
        matched["snr_means"] = means
        matched["snr_worst_gap"] = worst
        if worst > snr_tol:
            raise ValueError(
                f"SNR match missed: means {means}, worst gap {worst:.4f} against "
                f"a registered tolerance of {snr_tol}. The run stops here rather "
                f"than discovering this after sealing.")
    return matched


def _match_on_snr(W, N, T, n_per_class, n_bins):
    """Equal counts from each class in each SNR quantile bin."""
    if not (W and N and T):
        return {"W": [], "N": [], "T": [], "bins": [], "note": "a class came out empty"}
    allv = np.array([p["snr"] for p in W + N + T])
    edges = np.quantile(allv, np.linspace(0, 1, n_bins + 1))
    edges[-1] += 1e-9

    def binof(p):
        return int(np.clip(np.searchsorted(edges, p["snr"], side="right") - 1,
                           0, n_bins - 1))

    per = max(1, n_per_class // n_bins)
    out = {"W": [], "N": [], "T": []}
    bins = []
    for bi in range(n_bins):
        cells = {c: [p for p in lst if binof(p) == bi]
                 for c, lst in (("W", W), ("N", N), ("T", T))}
        take = min(len(cells["W"]), len(cells["N"]), len(cells["T"]), per)
        for c in "WNT":
            out[c].extend(cells[c][:take])
        bins.append({"bin": bi, "lo": float(edges[bi]), "hi": float(edges[bi + 1]),
                     "taken": take})
    out["bins"] = bins
    return out


def report(built) -> str:
    lines = []
    for c in "WNT":
        if not built[c]:
            lines.append(f"  {c}: empty"); continue
        v = {k: float(np.mean([p[k] for p in built[c]]))
             for k in ("snr", "margin", "displacement", "opposing_mass",
                       "direction_concentration", "log_noise_scale")}
        lines.append(f"  {c} n={len(built[c]):<4} snr {v['snr']:.3f}  "
                     f"margin {v['margin']:.3f}  ||b-a|| {v['displacement']:.2f}  "
                     f"oppose {v['opposing_mass']:.3f}  "
                     f"concen {v['direction_concentration']:.3f}")
    return "\n".join(lines)
