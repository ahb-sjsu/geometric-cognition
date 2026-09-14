# -*- coding: utf-8 -*-
"""C2 execution and analysis: replicate, interleaving, and a graded interaction.

Three repairs from the cold reread live here.

**The same-order replicate.** C1's runner called `prefers_first` twice per cell,
all forward comparisons and then all reverse ones, so the endpoint was literally
a between-block difference. Any drift on a shared gateway, batch composition,
node, queue depth, read as order-dependence and concentrated on near-indifferent
items. Every pair is now presented three times: forward, reversed, and forward
again. The third presentation measures the gateway's own flip floor, so the
endpoint becomes

    flip(order swapped)  minus  flip(order unchanged)

and nondeterminism is subtracted rather than assumed absent.

**Interleaving.** All presentations, all classes and both load levels go into one
randomised submission set. C1 ran a block schedule in which condition was
perfectly confounded with wall-clock time.

**A graded interaction.** The primary is the `class x load` coefficient of a
logistic fitted by Firth's penalised likelihood, which is finite when a cell has
zero events. The registered baseline outcome is zero in both classes, under which
an unpenalised fit separates and no difference in differences exists at all. The
baseline is an equivalence test rather than an accepted null.
"""
from __future__ import annotations

import numpy as np


# ----------------------------------------------------------------- presentation

def presentation_set(built, classes, loads, rng, render, ideal_vec):
    """One randomised list of every comparison the run will make.

    Each pair contributes three presentations at each load: forward, reversed,
    and a same-order replicate. Class, load and presentation are all interleaved,
    so none of them is confounded with position in the queue.
    """
    items = []
    for load in loads:
        d_ideal = rng.uniform(0.0, 100.0, size=load) if load else np.zeros(0)
        for cls in classes:
            for i, p in enumerate(built[cls]):
                d = rng.uniform(0.0, 100.0, size=load) if load else np.zeros(0)
                a = render(np.asarray(p["a"], float), d)
                b = render(np.asarray(p["b"], float), d)
                ideal = render(ideal_vec, d_ideal)
                for role, pair in (("forward", (a, b)),
                                   ("reversed", (b, a)),
                                   ("replicate", (a, b))):
                    items.append({"load": load, "cls": cls, "idx": i,
                                  "role": role, "ideal": ideal,
                                  "first": pair[0], "second": pair[1]})
    order = rng.permutation(len(items))
    return [items[i] for i in order]


def score_presentations(items, verdicts, built, classes, loads):
    """Per pair: did the verdict flip on swap, and did it flip on a repeat?

    A pair contributes to the endpoint only if all three presentations returned a
    letter. Items that did not are counted by cause and excluded from numerator
    and denominator alike, which is the reread's required treatment.
    """
    by = {}
    for it, v in zip(items, verdicts):
        by.setdefault((it["load"], it["cls"], it["idx"]), {})[it["role"]] = v
    rows, dropped = [], {}
    for load in loads:
        for cls in classes:
            for i, p in enumerate(built[cls]):
                r = by.get((load, cls, i), {})
                f, rv, rp = r.get("forward"), r.get("reversed"), r.get("replicate")
                if any(x is None or not np.isfinite(x) for x in (f, rv, rp)):
                    dropped[(load, cls)] = dropped.get((load, cls), 0) + 1
                    continue
                fwd = f > 0.5
                rows.append({
                    "load": load, "cls": cls, "idx": i,
                    # swapped: the verdict named a different OPTION when the two
                    # exchanged position
                    "swap_flip": int(fwd == (rv > 0.5)),
                    # same order, asked twice: the gateway's own flip floor
                    "repeat_flip": int(fwd != (rp > 0.5)),
                    "first_position": int(fwd),
                    "a_pref_full": bool(p["a_pref_full"]),
                    **{k: p[k] for k in ("snr", "log_noise_scale", "opposing_mass",
                                         "displacement", "direction_concentration")}})
    return rows, dropped


# ----------------------------------------------------------------- the statistic

def firth_logit(X, y, max_iter=200, tol=1e-9):
    """Logistic regression by Firth's penalised likelihood.

    Finite when a cell has zero events, which the registered baseline expects.
    An unpenalised fit separates there and reports an infinite coefficient, which
    is why C1's difference in differences was not estimable under its own
    predicted outcome.
    """
    X = np.asarray(X, float); y = np.asarray(y, float)
    n, k = X.shape
    beta = np.zeros(k)
    for _ in range(max_iter):
        eta = X @ beta
        mu = 1.0 / (1.0 + np.exp(-np.clip(eta, -35, 35)))
        w = mu * (1 - mu)
        XW = X * w[:, None]
        I = X.T @ XW
        try:
            Iinv = np.linalg.inv(I + 1e-10 * np.eye(k))
        except np.linalg.LinAlgError:
            return beta, None
        # leverages of the weighted design
        h = np.einsum("ij,jk,ik->i", X, Iinv, X) * w
        U = X.T @ (y - mu + h * (0.5 - mu))
        step = Iinv @ U
        beta = beta + step
        if np.max(np.abs(step)) < tol:
            break
    eta = X @ beta
    mu = 1.0 / (1.0 + np.exp(-np.clip(eta, -35, 35)))
    w = mu * (1 - mu)
    try:
        cov = np.linalg.inv(X.T @ (X * w[:, None]) + 1e-10 * np.eye(k))
    except np.linalg.LinAlgError:
        cov = None
    return beta, cov


def firth_lrt(X, y, idx):
    """Penalised likelihood ratio test that coefficient `idx` is zero."""
    def pll(Xs, ys):
        b, _ = firth_logit(Xs, ys)
        eta = Xs @ b
        mu = 1.0 / (1.0 + np.exp(-np.clip(eta, -35, 35)))
        ll = float(np.sum(ys * np.log(mu + 1e-300) + (1 - ys) * np.log(1 - mu + 1e-300)))
        w = mu * (1 - mu)
        I = Xs.T @ (Xs * w[:, None])
        sign, logdet = np.linalg.slogdet(I + 1e-10 * np.eye(Xs.shape[1]))
        return ll + 0.5 * logdet, b
    full, bfull = pll(X, y)
    keep = [j for j in range(X.shape[1]) if j != idx]
    red, _ = pll(X[:, keep], y)
    stat = 2.0 * (full - red)
    from math import erfc, sqrt
    p = erfc(sqrt(max(stat, 0.0) / 2.0))          # chi2 with 1 df
    return {"coef": float(bfull[idx]), "lrt_stat": float(stat), "p": float(p)}


def interaction_test(rows, cls_a="W", cls_b="T", adjust=True):
    """The primary: is the class difference in swap-flip larger under load?

    Outcome is swap flip. Predictors are class, load, their interaction, and, when
    `adjust` is set, the covariates the reread required be adjusted for rather
    than merely reported. The graded quantity is the interaction coefficient.
    """
    sel = [r for r in rows if r["cls"] in (cls_a, cls_b)]
    if not sel:
        return {"note": "no rows"}
    y = np.array([r["swap_flip"] for r in sel], float)
    cls = np.array([1.0 if r["cls"] == cls_b else 0.0 for r in sel])
    load = np.array([1.0 if r["load"] > 0 else 0.0 for r in sel])
    cols = [np.ones(len(sel)), cls, load, cls * load]
    names = ["intercept", "class", "load", "class:load"]
    if adjust:
        for k in ("snr", "log_noise_scale", "opposing_mass",
                  "displacement", "direction_concentration"):
            v = np.array([r[k] for r in sel], float)
            s = v.std()
            cols.append((v - v.mean()) / s if s > 1e-12 else v * 0.0)
            names.append(k)
    X = np.column_stack(cols)
    out = firth_lrt(X, y, 3)
    out.update({"terms": names, "n": len(sel),
                "contrast": f"{cls_b} vs {cls_a}", "adjusted": adjust})
    return out


def equivalence_baseline(rows, cls_a="W", cls_b="T", margin=0.02, alpha=0.05):
    """The baseline as an equivalence test, not an accepted null.

    The reread's finding: zero of 64 bounds a rate only at 0.046, which is most of
    the effect under test, so 'we saw no baseline gap' does not license 'there is
    none'. The run is VOID unless the baseline difference is demonstrably SMALLER
    than `margin`, which is a bar that can fail.
    """
    base = [r for r in rows if r["load"] == 0]
    a = [r["swap_flip"] for r in base if r["cls"] == cls_a]
    b = [r["swap_flip"] for r in base if r["cls"] == cls_b]
    if not a or not b:
        return {"note": "baseline missing"}
    na, nb = len(a), len(b)
    pa, pb = float(np.mean(a)), float(np.mean(b))
    diff = pb - pa
    se = float(np.sqrt(pa * (1 - pa) / na + pb * (1 - pb) / nb))
    z = 1.959963985
    lo, hi = diff - z * se, diff + z * se
    return {"p_a": pa, "p_b": pb, "difference": diff, "ci95": (lo, hi),
            "margin": margin,
            "equivalent": bool(hi < margin and lo > -margin),
            "verdict": ("baseline equivalent, the run may proceed"
                        if (hi < margin and lo > -margin) else
                        "VOID, the baseline is not demonstrably smaller than the margin")}


def replicate_floor(rows):
    """The gateway's own flip rate on an unchanged presentation, per class."""
    out = {}
    for key in {(r["load"], r["cls"]) for r in rows}:
        sel = [r for r in rows if (r["load"], r["cls"]) == key]
        out[f"load{key[0]}_{key[1]}"] = {
            "n": len(sel),
            "repeat_flip_rate": float(np.mean([r["repeat_flip"] for r in sel])),
            "swap_flip_rate": float(np.mean([r["swap_flip"] for r in sel])),
            "excess": float(np.mean([r["swap_flip"] for r in sel])
                            - np.mean([r["repeat_flip"] for r in sel]))}
    return out
