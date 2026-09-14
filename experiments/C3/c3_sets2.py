# -*- coding: utf-8 -*-
"""C3 second rebuild: an oblique workload and a heavy-tailed low column.

The reread of `c3_sets.py` found two problems in the stimulus distribution. The
low role gave the probe a cue: the farther probe option was the most extreme value
on its attribute in every low-role prompt, because probe values were pushed outside
the tight low cluster and the context was kept away from them. And on a
decorrelated context a rank budget is the same computation as ignoring
low-variance attributes, so no result could tell a capacity limit from a relevance
judgement.

**One principle answers both: the context never depends on the probe.** Context
values come from fixed templates. The only rejection rule looks at the context by
itself, at its column correlations, and never at the probe. The exclusion window
is gone.

**Axis arm.** Each triplet draws one set of 20 context rows, each row a wide value,
a mid value and a heavy value. A role decides only which attribute receives which.
Across the three prompts of a triplet every context option's distance from the
ideal is therefore identical, and so is the probe's distance rank among all 22
options. The heavy template is 12 values within one unit of zero, single values
at 3.5, 6.5 and 9.5 on each side, and tails at 12, so its variance is low and its
range is wide with no empty band where probe values sit. Probe
target offsets are capped below the tails, so no probe value is the most extreme
in any column in any role.

**Oblique arm.** Two attributes `A` and `B` are built from a wide component `s`
and a heavy component `d`, as `A = 50 + (s + d)/sqrt2` and `B = 50 + (s - d)/sqrt2`.
The workload is then high along `A + B` and low along `A - B`. The paired context
mirrors `B` about the ideal, `B' = 100 - B`, which flips the correlation and
exchanges the two directions while leaving every `|value - 50|` unchanged. Every
context option's distance from the ideal and every column's spread about the ideal
is identical across the pair. The probe varies along `A - B` and is identical in
both prompts. A rank budget that drops the low direction predicts lower accuracy
when `A - B` is the low direction. Any model acting on one attribute at a time
predicts no difference, because nothing about any single attribute differs.
Multivariate shrinkage toward the context still mimics the budget, and that is
recorded as the surviving alternative rather than claimed away.
"""
from __future__ import annotations

import numpy as np

D = 3
IDEAL = np.array([50.0, 50.0, 50.0])
LO, HI = 12.0, 88.0
DECIMALS = 1
LABEL_POOL = ("F", "H", "K", "M", "N", "S", "V", "X", "Z")
N_CONTEXT = 20
MAX_CONTEXT_CORR = 0.10          # context-only rejection rule
WIDE_RMS, MID_RMS = 20.0, 10.0
HEAVY_CORE = 1.0
HEAVY_SPREAD = (3.5, 6.5, 9.5)   # fills the gap the probe values sit in
HEAVY_TAIL = 12.0
PROBE_TARGET_CAP = 10.0          # below the heavy tails, so a probe is never extreme
NONTARGET_OFFSET = (2.0, 5.0)
NEARER_OFFSET = (3.0, 6.0)
RANK_GAP = 2.0
SQ2 = np.sqrt(2.0)

TARGET_PATTERNS = ((+1, +1), (-1, -1), (+1, -1), (-1, +1))   # (nearer, farther)


def fmt(v):
    return f"{v:.{DECIMALS}f}"


# ------------------------------------------------------------------ templates

def wide_template(n=N_CONTEXT):
    v = np.linspace(-1.0, 1.0, n)
    return v / np.sqrt(np.mean(v ** 2)) * WIDE_RMS


def mid_template(n=N_CONTEXT):
    v = np.linspace(-1.0, 1.0, n)
    return v / np.sqrt(np.mean(v ** 2)) * MID_RMS


def heavy_template(n=N_CONTEXT):
    """Low variance, wide range, and no empty band where probe values sit.

    A first version put 16 values within one unit of zero and tails at 11.5 and
    12.5. The band between them was empty, the probe's target values sat in it,
    and a rule that picks the less isolated option reached 0.72 in the low role.
    Filling the band with values at 3.5, 6.5 and 9.5 brings that to about 0.64 at
    the same variance. It cannot reach 0.5: a low-variance column that spans the
    probe's range must thin out away from the ideal, and the farther option always
    has the larger target offset. That residual is recorded as a registered
    adversary, not claimed away. The template was chosen by that adversary alone,
    before any budget result was looked at, and ties with a denser alternative to
    within 0.005; this one is kept for its lower variance.
    """
    core = np.linspace(-HEAVY_CORE, HEAVY_CORE, n - 8)
    spread = np.array(HEAVY_SPREAD)
    return np.concatenate([core, -spread[::-1], spread, [-HEAVY_TAIL, HEAVY_TAIL]])


def draw_rows(rng, max_tries=5000):
    """Three independently permuted templates, rejected only on their own correlations.

    Nothing about the probe enters. A draw is kept when every pair of columns has a
    sample correlation within `MAX_CONTEXT_CORR`, so the context's second moment is
    close to diagonal in the template coordinates.
    """
    w, m, h = wide_template(), mid_template(), heavy_template()
    for _ in range(max_tries):
        R = np.column_stack([rng.permutation(w), rng.permutation(m), rng.permutation(h)])
        C = np.corrcoef(R.T)
        if np.max(np.abs(C[np.triu_indices(3, 1)])) <= MAX_CONTEXT_CORR:
            return R
    return None


def moment(options):
    U = np.asarray(options, float) - IDEAL
    return U.T @ U / len(U)


def in_box(x):
    return bool(np.all(x >= LO) and np.all(x <= HI))


# ------------------------------------------------------------------ axis arm

def axis_probe(rng, target, separation, pattern_index):
    others = [k for k in range(D) if k != target]
    delta = {k: rng.uniform(*NONTARGET_OFFSET) * rng.choice((-1, 1)) for k in others}
    r2 = sum(v * v for v in delta.values())
    u_n = rng.uniform(*NEARER_OFFSET)
    d_n = np.sqrt(r2 + u_n ** 2)
    u_f2 = (d_n + separation) ** 2 - r2
    if u_f2 <= 0:
        return None
    u_f = float(np.sqrt(u_f2))
    if u_f > PROBE_TARGET_CAP:
        return None                       # registered cap, depends on the probe alone
    pat = TARGET_PATTERNS[pattern_index]
    n = IDEAL.copy(); f = IDEAL.copy()
    for k, v in delta.items():
        n[k] = IDEAL[k] + v; f[k] = IDEAL[k] - v
    n[target] = IDEAL[target] + pat[0] * u_n
    f[target] = IDEAL[target] + pat[1] * u_f
    n = np.round(n, DECIMALS); f = np.round(f, DECIMALS)
    dn, df = np.linalg.norm(n - IDEAL), np.linalg.norm(f - IDEAL)
    if not dn < df:
        return None
    return {"target": int(target), "separation": float(separation),
            "nearer": n, "farther": f, "achieved_separation": float(df - dn),
            "straddles": bool(pat[0] != pat[1]),
            "smaller_is_nearer": bool(n[target] < f[target])}


ROLE_TEMPLATE = {"hi": 0, "mid": 1, "lo": 2}       # column of the row array


def axis_triplet(rng, target, separation, pattern_index):
    probe = axis_probe(rng, target, separation, pattern_index)
    if probe is None:
        return None
    R = draw_rows(rng)
    if R is None:
        return None
    others = [k for k in range(D) if k != target]
    order = list(rng.permutation(D))
    labels = list(rng.choice(LABEL_POOL, size=D, replace=False))
    n_opt = N_CONTEXT + 2
    pos = [int(p) for p in rng.choice(n_opt, size=2, replace=False)]
    nearer_first = bool(rng.integers(2))
    prompts = {}
    for role in ("hi", "mid", "lo"):
        rest = [r for r in ("hi", "mid", "lo") if r != role]
        rng.shuffle(rest)
        roles = {target: role, others[0]: rest[0], others[1]: rest[1]}
        ctx = np.empty((N_CONTEXT, D))
        for k in range(D):
            ctx[:, k] = IDEAL[k] + R[:, ROLE_TEMPLATE[roles[k]]]
        ctx = np.round(ctx, DECIMALS)
        if not all(in_box(c) for c in ctx):
            return None
        v = np.diag(moment(ctx))
        by = {roles[k]: v[k] for k in range(D)}
        if not (by["hi"] / by["mid"] >= RANK_GAP and by["mid"] / by["lo"] >= RANK_GAP):
            return None
        prompts[role] = {"roles": {int(k): r for k, r in roles.items()},
                         "context": ctx, "variances": by}
    return {"arm": "axis", "probe": probe, "order": order, "labels": labels,
            "positions": pos, "nearer_first": nearer_first, "prompts": prompts}


# ------------------------------------------------------------------ oblique arm

def oblique_probe(rng, pair, separation, pattern_index, sum_sign):
    """Probe varying along A - B, with symmetric components along A + B and C."""
    a, b = pair
    c = [k for k in range(D) if k not in pair][0]
    ds = rng.uniform(*NONTARGET_OFFSET) * sum_sign
    dc = rng.uniform(*NONTARGET_OFFSET) * rng.choice((-1, 1))
    r2 = ds * ds + dc * dc
    u_n = rng.uniform(*NEARER_OFFSET)
    d_n = np.sqrt(r2 + u_n ** 2)
    u_f2 = (d_n + separation) ** 2 - r2
    if u_f2 <= 0:
        return None
    u_f = float(np.sqrt(u_f2))
    if u_f > PROBE_TARGET_CAP:
        return None
    pat = TARGET_PATTERNS[pattern_index]

    def point(sgn_sum, tau, sgn_c):
        x = IDEAL.copy()
        sig = sgn_sum * ds
        x[a] = IDEAL[a] + (sig + tau) / SQ2
        x[b] = IDEAL[b] + (sig - tau) / SQ2
        x[c] = IDEAL[c] + sgn_c * dc
        return np.round(x, DECIMALS)

    n = point(+1, pat[0] * u_n, +1)
    f = point(-1, pat[1] * u_f, -1)
    dn, df = np.linalg.norm(n - IDEAL), np.linalg.norm(f - IDEAL)
    if not dn < df or not (in_box(n) and in_box(f)):
        return None
    return {"pair": [int(a), int(b)], "other": int(c), "separation": float(separation),
            "nearer": n, "farther": f, "achieved_separation": float(df - dn),
            "straddles": bool(pat[0] != pat[1]),
            "smaller_is_nearer_A": bool(n[a] < f[a]),
            "smaller_is_nearer_B": bool(n[b] < f[b])}


def oblique_pair(rng, pair, separation, pattern_index, sum_sign):
    probe = oblique_probe(rng, pair, separation, pattern_index, sum_sign)
    if probe is None:
        return None
    R = draw_rows(rng)
    if R is None:
        return None
    a, b = pair
    c = probe["other"]
    s, m, h = R[:, 0], R[:, 1], R[:, 2]
    base = np.tile(IDEAL, (N_CONTEXT, 1))
    base[:, a] = IDEAL[a] + (s + h) / SQ2
    base[:, b] = IDEAL[b] + (s - h) / SQ2
    base[:, c] = IDEAL[c] + m
    base = np.round(base, DECIMALS)
    mirrored = base.copy()
    mirrored[:, b] = np.round(2 * IDEAL[b] - base[:, b], DECIMALS)
    if not all(in_box(x) for x in base) or not all(in_box(x) for x in mirrored):
        return None
    order = list(rng.permutation(D))
    labels = list(rng.choice(LABEL_POOL, size=D, replace=False))
    n_opt = N_CONTEXT + 2
    pos = [int(p) for p in rng.choice(n_opt, size=2, replace=False)]
    nearer_first = bool(rng.integers(2))
    # "lo": A - B is the low-variance direction.  "hi": it is the high one.
    return {"arm": "oblique", "probe": probe, "order": order, "labels": labels,
            "positions": pos, "nearer_first": nearer_first,
            "prompts": {"lo": {"context": base}, "hi": {"context": mirrored}}}


# ------------------------------------------------------------------ rendering

def options(item, role):
    ctx = item["prompts"][role]["context"]
    n_opt = N_CONTEXT + 2
    first, second = ((item["probe"]["nearer"], item["probe"]["farther"])
                     if item["nearer_first"] else
                     (item["probe"]["farther"], item["probe"]["nearer"]))
    out = [None] * n_opt
    out[item["positions"][0]] = first
    out[item["positions"][1]] = second
    it = iter(ctx)
    for i in range(n_opt):
        if out[i] is None:
            out[i] = next(it)
    return [np.asarray(o, float) for o in out]


def render(item, role):
    def line(x):
        return ", ".join(f"{item['labels'][k]} {fmt(x[item['order'][k]])}" for k in range(D))
    lines = [f"The ideal is: {line(IDEAL)}"]
    for i, o in enumerate(options(item, role)):
        lines.append(f"Option {i + 1}: {line(o)}")
    a, b = item["positions"]
    lines.append(f"Which is closer to the ideal, option {a + 1} or option {b + 1}? "
                 f"Answer with the option number only.")
    return "\n".join(lines)


# ------------------------------------------------------------------ design

def build(rng, separations=(1.0, 2.0, 4.0), n_per_cell=64, max_attempts=200000):
    axis, oblique, attempts = {}, {}, {}
    for tg in range(D):
        for s in separations:
            got, tries = [], 0
            for k in range(4):
                want = n_per_cell // 4
                have = 0
                while have < want and tries < max_attempts:
                    tries += 1
                    it = axis_triplet(rng, tg, s, k)
                    if it is not None:
                        got.append(it); have += 1
            axis[(tg, s)] = got
            attempts[("axis", tg, s)] = tries
    pairs = [(0, 1), (0, 2), (1, 2)]
    for pr in pairs:
        for s in separations:
            got, tries = [], 0
            for k in range(4):
                for sgn in (+1, -1):
                    want = n_per_cell // 8
                    have = 0
                    while have < want and tries < max_attempts:
                        tries += 1
                        it = oblique_pair(rng, pr, s, k, sgn)
                        if it is not None:
                            got.append(it); have += 1
            oblique[(pr, s)] = got
            attempts[("oblique", pr, s)] = tries
    return {"axis": axis, "oblique": oblique, "attempts": attempts,
            "separations": list(separations), "n_per_cell": n_per_cell}
