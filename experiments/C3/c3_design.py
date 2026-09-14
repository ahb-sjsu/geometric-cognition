# -*- coding: utf-8 -*-
"""C3: measure the evaluator's sensitivity profile directly. No fitted metric.

Four designs were refused because each selected its pairs by a property of a
metric fitted to the evaluator under test. The class label was then a prediction
of that model, the classes differed in the whole joint distribution rather than
in one coordinate, and matching on any single statistic unmatched another. C1 and
C2 revision 1 matched preference margin; revision 2 matched decision SNR; each
time the unmatched axis carried a confound as large as the effect or larger.

Nothing here is fitted, selected, or projected.

**The construction.** A pair differs along exactly one coordinate axis. The axis
is the design variable and is chosen, not discovered. The size of the
displacement is solved so that the pair's difference in distance from the ideal
equals a target value, computed in the design's own Euclidean geometry, which is
a property of the stimulus and not of the subject. Two pairs on different axes
with the same target are therefore the same objective discrimination problem
presented along different directions.

**What a rank budget says, in this vocabulary.** A budget retains the directions
that carry workload variance and discards the rest. The design's box fixes that
ordering with no estimation: with per-axis ranges 100, 45 and 20 the variances
are 833, 169 and 33, so a rank-1 budget keeps the first axis and discards the
third. If the evaluator has such a budget, it needs a larger displacement on the
discarded axis than on the retained one to reach the same accuracy.

**The endpoint is the shape of the profile, not its level.** Write `thr_j` for
the displacement at which the evaluator reaches a fixed accuracy on axis `j`.

    uniform noise    every `thr_j` scales by the same factor, the ratio
                     `thr_R / thr_P` is unchanged
    a rank budget    the discarded axis degrades faster, the ratio rises

A ratio of thresholds is invariant to anything that multiplies all sensitivities
together, so the noise account is the exact null rather than one adversary's
construction. That is the property the previous four designs never had.

The evaluator's static per-axis sensitivity is whatever it is, and is measured at
zero load rather than assumed uniform. The graded quantity is the change in the
ratio under load.
"""
from __future__ import annotations

import numpy as np

LABELS = ("P", "Q", "R")
DECIMALS = 1


def render(x, labels=LABELS, decimals: int = DECIMALS) -> str:
    return ", ".join(f"{l} {v:.{decimals}f}" for l, v in zip(labels, np.asarray(x, float)))


def round_to_render(x, decimals: int = DECIMALS) -> np.ndarray:
    return np.round(np.asarray(x, float), decimals)


def solve_displacement(x, axis, target, t, lo, hi, prefer_farther=False):
    """Displacement along `axis` that moves distance-from-ideal by `target`.

    Euclidean in the design's own units. `d(x + s e_j)^2 - d(x)^2 = 2 s u_j + s^2`
    with `u = x - t`, so the requirement `d(y) - d(x) = target` is a quadratic in
    `s`. The geometry here is a property of the stimulus set, chosen in advance.
    Nothing about the evaluator enters.
    """
    x = np.asarray(x, float); t = np.asarray(t, float)
    u = x - t
    d0 = float(np.linalg.norm(u))
    d1 = d0 + (target if prefer_farther else -target)
    if d1 <= 0:
        return None
    # s^2 + 2 u_j s + (d0^2 - d1^2) = 0
    c = d0 ** 2 - d1 ** 2
    disc = u[axis] ** 2 - c
    if disc < 0:
        return None
    for s in (-u[axis] + np.sqrt(disc), -u[axis] - np.sqrt(disc)):
        y = x.copy(); y[axis] += s
        if np.all(y >= lo) and np.all(y <= hi) and abs(s) > 10.0 ** (-DECIMALS):
            return float(s)
    return None


def make_pair(rng, axis, target, t, lo, hi, max_tries=400,
              dist_band=(15.0, 45.0)):
    """One single-axis pair at a registered distance separation.

    Both options are rendered at the same precision as everything else, and the
    pair is rejected if rounding changes which one is nearer, so the correct
    answer is a fact about the strings the evaluator sees.
    """
    t = np.asarray(t, float)
    for _ in range(max_tries):
        x = rng.uniform(lo, hi)
        s = solve_displacement(x, axis, target, t, lo, hi,
                               prefer_farther=bool(rng.integers(2)))
        if s is None:
            continue
        y = x.copy(); y[axis] += s
        xr, yr = round_to_render(x), round_to_render(y)
        if np.array_equal(xr, yr):
            continue
        dx = float(np.linalg.norm(xr - t)); dy = float(np.linalg.norm(yr - t))
        if abs(abs(dx - dy) - target) > 0.25 * target:
            continue          # rounding moved the separation too far
        # Distance from the ideal must sit in a registered band, the same band
        # for every axis. Without it the narrow axis is forced toward the ideal
        # to reach a large separation, and "how near the ideal the options sit"
        # becomes confounded with the axis. That is the defect class that
        # refused the previous four designs, caught here in construction rather
        # than by a reader afterwards.
        if not (dist_band[0] <= min(dx, dy) and max(dx, dy) <= dist_band[1]):
            continue
        a_first = bool(rng.integers(2))
        a, b = (xr, yr) if a_first else (yr, xr)
        da, db = (dx, dy) if a_first else (dy, dx)
        return {"axis": int(axis), "target": float(target),
                "a": a.tolist(), "b": b.tolist(),
                "a_nearer": bool(da < db),
                "separation": float(abs(da - db)),
                "displacement": float(abs(s)),
                # recorded so a reader can check the axes are not confounded
                # with anything else the stimulus carries
                "mean_magnitude": float(np.mean(np.abs(np.concatenate([a, b])))),
                "min_distance": float(min(da, db)),
                "render_len": len(render(a))}
    return None


def build_ladder(rng, axes, targets, n_per_cell, t, lo, hi):
    """A full crossing of axis by separation. Every cell is the same size.

    There is no selection step anywhere in this function. Nothing is admitted or
    rejected on the basis of a prediction; the only rejections are geometric,
    when the box or the rendering precision cannot express the requested pair.
    """
    cells, short = {}, []
    for axis in axes:
        for target in targets:
            got = []
            for _ in range(n_per_cell * 50):
                if len(got) >= n_per_cell:
                    break
                p = make_pair(rng, axis, target, t, lo, hi)
                if p is not None:
                    got.append(p)
            cells[(axis, target)] = got
            if len(got) < n_per_cell:
                short.append((axis, target, len(got)))
    return {"cells": cells, "short": short,
            "axes": list(axes), "targets": list(targets),
            "n_per_cell": n_per_cell}


def balance_report(built) -> dict:
    """Are the axes matched on everything except the axis?

    The previous designs matched one statistic and were confounded on another.
    Here the classes are defined by construction, so this is a check rather than
    a repair, and it is reported per separation so a reader can see it directly.
    """
    out = {}
    for (axis, target), pairs in built["cells"].items():
        if not pairs:
            continue
        out[f"axis{axis}_sep{target}"] = {
            "n": len(pairs),
            "separation": float(np.mean([p["separation"] for p in pairs])),
            "displacement": float(np.mean([p["displacement"] for p in pairs])),
            "mean_magnitude": float(np.mean([p["mean_magnitude"] for p in pairs])),
            "min_distance": float(np.mean([p["min_distance"] for p in pairs])),
            "render_len": float(np.mean([p["render_len"] for p in pairs])),
            "a_nearer_rate": float(np.mean([p["a_nearer"] for p in pairs]))}
    return out
