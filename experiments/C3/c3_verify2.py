# -*- coding: utf-8 -*-
"""Construction checks and simulated evaluators for `c3_sets2.py`.

The reread of the first rebuild found its simulation table had no committed code.
Every number reported for the second rebuild comes from this file.

    python c3_verify2.py            # build, check, simulate, print
"""
from __future__ import annotations

import sys
from math import erf, sqrt

import numpy as np

import c3_sets2 as S

T = S.IDEAL
PHI = np.vectorize(lambda z: 0.5 * (1 + erf(z / sqrt(2))))


def items(design, arm):
    for key, lst in design[arm].items():
        for it in lst:
            yield key, it


def roles_of(arm):
    return ("hi", "mid", "lo") if arm == "axis" else ("hi", "lo")


def ctx_and_all(it, role):
    ctx = it["prompts"][role]["context"]
    return ctx, np.vstack([ctx, it["probe"]["nearer"], it["probe"]["farther"]])


# ------------------------------------------------------------------ checks

def construction_checks(design):
    out = []
    say = out.append
    for arm in ("axis", "oblique"):
        R = roles_of(arm)
        its = [it for _, it in items(design, arm)]
        say(f"\n[{arm}] {len(its)} items")
        fill = {k: len(v) for k, v in design[arm].items()}
        say(f"  fill per cell: min {min(fill.values())} max {max(fill.values())} "
            f"of {design['n_per_cell']}")
        texts_ok = 0
        dist_identical = rank_identical = 0
        for it in its:
            probe_lines = set()
            dsets, ranks = [], []
            for r in R:
                lines = S.render(it, r).split("\n")
                a, b = it["positions"]
                probe_lines.add((lines[a + 1], lines[b + 1]))
                ctx, allo = ctx_and_all(it, r)
                dctx = np.sort(np.linalg.norm(ctx - T, axis=1))
                dsets.append(dctx)
                dn = np.linalg.norm(it["probe"]["nearer"] - T)
                ranks.append(int(np.sum(np.linalg.norm(ctx - T, axis=1) < dn)))
            texts_ok += len(probe_lines) == 1
            dist_identical += all(np.allclose(dsets[0], d, atol=1e-9) for d in dsets[1:])
            rank_identical += len(set(ranks)) == 1
        say(f"  probe lines byte-identical across prompts: {texts_ok}/{len(its)}")
        say(f"  context distances to the ideal identical across prompts: {dist_identical}/{len(its)}")
        say(f"  probe distance rank identical across prompts: {rank_identical}/{len(its)}")

        # extremeness and isolation, by role
        say("  role   farther extreme on any column   nearer extreme on any column   isolation-rule acc   extremeness-rule acc")
        for r in R:
            fe = ne = 0; iso = []; ext = []
            for it in its:
                _, allo = ctx_and_all(it, r)
                n, f = it["probe"]["nearer"], it["probe"]["farther"]
                ctx = it["prompts"][r]["context"]
                mins, maxs = allo.min(axis=0), allo.max(axis=0)
                fx = np.sum((f == mins) | (f == maxs)); nx = np.sum((n == mins) | (n == maxs))
                fe += fx > 0; ne += nx > 0
                dn = np.min(np.linalg.norm(ctx - n, axis=1)); dfar = np.min(np.linalg.norm(ctx - f, axis=1))
                iso.append(1.0 if dfar > dn else (0.5 if dfar == dn else 0.0))
                ext.append(1.0 if fx > nx else (0.5 if fx == nx else 0.0))
            say(f"  {r:>4}   {fe / len(its):>28.3f}   {ne / len(its):>28.3f}   "
                f"{np.mean(iso):>18.3f}   {np.mean(ext):>20.3f}")

        # context correlation and variance structure
        corr = [np.max(np.abs(np.corrcoef(it["prompts"][R[0]]["context"].T)[np.triu_indices(3, 1)]))
                for it in its]
        if arm == "axis":
            say(f"  max |column corr| per prompt: median {np.median(corr):.3f} max {np.max(corr):.3f}")
            for r in R:
                v = {q: np.mean([it['prompts'][r]['variances'][q] for it in its]) for q in ("hi", "mid", "lo")}
                say(f"  target role {r:>3}: context variances hi {v['hi']:.1f} mid {v['mid']:.1f} lo {v['lo']:.1f}")
        else:
            for r in R:
                vs, vd, vA, vB = [], [], [], []
                for it in its:
                    a, b = it["probe"]["pair"]
                    ctx = it["prompts"][r]["context"]
                    U = ctx - T
                    vs.append(np.mean(((U[:, a] + U[:, b]) / S.SQ2) ** 2))
                    vd.append(np.mean(((U[:, a] - U[:, b]) / S.SQ2) ** 2))
                    vA.append(np.mean(U[:, a] ** 2)); vB.append(np.mean(U[:, b] ** 2))
                say(f"  {r:>3}: var along A+B {np.mean(vs):6.1f}  along A-B {np.mean(vd):6.1f}  "
                    f"marginal A {np.mean(vA):6.1f}  B {np.mean(vB):6.1f}")
            same_marg = 0
            for it in its:
                a, b = it["probe"]["pair"]
                lo_, hi_ = it["prompts"]["lo"]["context"], it["prompts"]["hi"]["context"]
                same_marg += all(np.allclose(np.sort(np.abs(lo_[:, k] - 50)), np.sort(np.abs(hi_[:, k] - 50)), atol=1e-9)
                                 for k in range(3))
            say(f"  every column's |value - 50| multiset identical across the pair: {same_marg}/{len(its)}")
        if arm == "axis":
            say(f"  smaller value is nearer: {np.mean([it['probe']['smaller_is_nearer'] for it in its]):.3f}"
                f"   straddles: {np.mean([it['probe']['straddles'] for it in its]):.3f}")
        else:
            say(f"  smaller value nearer on A: {np.mean([it['probe']['smaller_is_nearer_A'] for it in its]):.3f}"
                f"  on B: {np.mean([it['probe']['smaller_is_nearer_B'] for it in its]):.3f}"
                f"  straddles: {np.mean([it['probe']['straddles'] for it in its]):.3f}")
        err = [abs(it["probe"]["achieved_separation"] - it["probe"]["separation"]) / it["probe"]["separation"] for it in its]
        say(f"  separation error: mean {100 * np.mean(err):.2f}%  max {100 * np.max(err):.2f}%")
    return "\n".join(out)


# ------------------------------------------------------------------ evaluator models

def m_blind(n, f, ctx, allo):
    return np.linalg.norm(n - T) - np.linalg.norm(f - T)


def m_budget(k, with_probe=False):
    def g(n, f, ctx, allo):
        M = S.moment(allo if with_probe else ctx)
        w, V = np.linalg.eigh(M)
        Vk = V[:, np.argsort(w)[::-1][:k]]
        P = Vk @ Vk.T
        return np.linalg.norm(P @ (n - T)) - np.linalg.norm(P @ (f - T))
    return g


def m_uni_shrink(tau):
    def g(n, f, ctx, allo):
        v = np.diag(S.moment(ctx)); kf = v / (v + tau ** 2)
        return np.linalg.norm(kf * (n - T)) - np.linalg.norm(kf * (f - T))
    return g


def m_multi_shrink(tau):
    def g(n, f, ctx, allo):
        Sg = S.moment(ctx); K = Sg @ np.linalg.inv(Sg + tau ** 2 * np.eye(3))
        return np.linalg.norm(K @ (n - T)) - np.linalg.norm(K @ (f - T))
    return g


def m_relevance(n, f, ctx, allo):
    v = np.diag(S.moment(ctx)); w = v / v.max()
    return np.sqrt(np.sum(w * (n - T) ** 2)) - np.sqrt(np.sum(w * (f - T) ** 2))


def m_saturate(n, f, ctx, allo):
    s = np.sqrt(np.diag(S.moment(ctx)))
    tr = lambda x: s * np.tanh((x - T) / (2 * s))
    return np.linalg.norm(tr(n)) - np.linalg.norm(tr(f))


def m_anchor(n, f, ctx, allo, lam=0.5):
    def an(x):
        y = x.copy()
        for k in range(3):
            near = np.sort(np.abs(ctx[:, k] - x[k]))[:3]
            idx = np.argsort(np.abs(ctx[:, k] - x[k]))[:3]
            y[k] = (1 - lam) * x[k] + lam * ctx[idx, k].mean()
        return y
    return np.linalg.norm(an(n) - T) - np.linalg.norm(an(f) - T)


def m_rank(n, f, ctx, allo):
    def rk(v, k):
        return np.mean(allo[:, k] < v)
    rn = np.array([rk(n[k], k) for k in range(3)])
    rf = np.array([rk(f[k], k) for k in range(3)])
    ri = np.array([rk(50.0, k) for k in range(3)])
    return np.linalg.norm(rn - ri) - np.linalg.norm(rf - ri)


MODELS = {
    "no budget, noise on the probe": m_blind,
    "rank-1 budget, context workload": m_budget(1),
    "rank-2 budget, context workload": m_budget(2),
    "rank-2 budget, probe in workload": m_budget(2, True),
    "univariate shrinkage, tau 5": m_uni_shrink(5.0),
    "multivariate shrinkage, tau 5": m_multi_shrink(5.0),
    "relevance weight var/max": m_relevance,
    "column-scaled saturation": m_saturate,
    "anchor on 3 nearest per column": m_anchor,
    "rank coding within prompt": m_rank,
}


def simulate(design):
    seps = design["separations"]
    out = []
    say = out.append
    for name, fn in MODELS.items():
        X = {}
        for arm in ("axis", "oblique"):
            for (key, it) in items(design, arm):
                s = it["probe"]["separation"]
                for r in roles_of(arm):
                    ctx, allo = ctx_and_all(it, r)
                    X.setdefault((arm, r, s), []).append(fn(it["probe"]["nearer"], it["probe"]["farther"], ctx, allo))
        X = {k: np.array(v) for k, v in X.items()}
        ref = X[("axis", "hi", seps[0])]
        lo, hi = 1e-8, 1e4
        for _ in range(80):
            m = np.sqrt(lo * hi)
            lo, hi = (m, hi) if np.mean(PHI(-ref / m)) > 0.75 else (lo, m)
        sig = np.sqrt(lo * hi)
        acc = {k: float(np.mean(PHI(-v / sig))) for k, v in X.items()}
        say(f"\n{name}   (noise {sig:.4g})")
        say(f"   sep   axis hi   mid    lo   hi-lo  |  oblique hi    lo   hi-lo")
        for s in seps:
            a = [acc[("axis", r, s)] for r in ("hi", "mid", "lo")]
            o = [acc[("oblique", r, s)] for r in ("hi", "lo")]
            say(f"   {s:>3}   {a[0]:.3f}  {a[1]:.3f}  {a[2]:.3f}  {a[0] - a[2]:+.3f}  |  "
                f"{o[0]:.3f}  {o[1]:.3f}  {o[0] - o[1]:+.3f}")
    return "\n".join(out)


def main(seed=20260914):
    design = S.build(np.random.default_rng(seed))
    print(f"seed {seed}")
    print(construction_checks(design))
    print(simulate(design))
    return 0


if __name__ == "__main__":
    sys.exit(main(int(sys.argv[1]) if len(sys.argv) > 1 else 20260914))
