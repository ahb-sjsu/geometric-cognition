# -*- coding: utf-8 -*-
"""C3 rebuild: multi-option sets, a byte-identical probe, and context roles.

The reread of the pair construction found that one pair per prompt gives the
evaluator no workload to budget over, because all in-context variance sits on
the tested axis. It also found answer shortcuts on the narrow axes, a noise
account that is not the exact null, and an axis confounded with list position,
label and numeric range. This module replaces the pair construction.

**The unit is a triplet of prompts.** Each prompt shows an ideal and a set of
options. Two of the options are the probe pair, which differs mainly along one
target attribute. The rest are context, whose spread per attribute is fixed by
design: one attribute is high variance, one medium, one low. The probe is the
same in all three prompts of a triplet, byte for byte, at the same list
positions, with the same attribute order and labels. Only the context changes,
and with it the role the probe's target attribute plays: high, medium or low.

**Why this is the null the pair design claimed and lacked.** Any noise that acts
on the probe, including the two-source model that moved the pair design's
threshold ratio fourfold, sees identical input in all three prompts and so
predicts no difference between roles. A rank budget over the in-context workload
keeps the high-variance attribute and discards the low one, and predicts the same
probe is accurate in its high role and near chance in its low role. The medium
role tells rank 1 from rank 2.

**The reread's other findings, and what answers each.**

* Range was the same variable as variance. Every attribute now spans the same
  numeric range around the same ideal, so variance differences exist only in the
  context, and the attributes are exchangeable by construction.
* Axis was confounded with list position and letter label. Attribute order and
  labels are drawn per triplet from a pool, and the target attribute is
  counterbalanced across triplets.
* "Pick the smaller value" and "pick the shorter string" answered the narrow
  axes. Values are confined to a fixed-width band so every rendered number has
  the same length, and each probe is drawn from four sign patterns chosen
  uniformly, which balances "smaller value is nearer" and "the pair straddles the
  ideal" at exactly one half each and independently.
* The options differed on one attribute only. Non-target attributes are now
  perturbed symmetrically about the ideal, so the two options differ on every
  attribute while the answer still rests on the target.
* The root choice was biased. There is no root choice; offsets are drawn
  directly from the registered sign patterns.
"""
from __future__ import annotations

import numpy as np

D = 3
IDEAL = np.array([50.0, 50.0, 50.0])
LO, HI = 12.0, 88.0              # every value renders as NN.N, four characters
DECIMALS = 1
LABEL_POOL = ("F", "H", "K", "M", "N", "S", "V", "X", "Z")
ROLE_SD = {"hi": 20.0, "mid": 10.0, "lo": 3.0}
N_CONTEXT = 20
EXCLUSION = 1.0                  # context values keep this far from probe values
NONTARGET_OFFSET = (6.0, 10.0)   # probe non-target values sit outside the lo cluster
NEARER_OFFSET = (4.0, 10.0)
RANK_GAP = 2.0                   # registered floor on successive in-context variance ratios

SIGN_PATTERNS = ((+1, +1), (-1, -1), (+1, -1), (-1, +1))   # (nearer, farther)


def fmt(v) -> str:
    return f"{v:.{DECIMALS}f}"


def make_probe(rng, target, separation, pattern_index=None):
    """The probe pair, in canonical attribute coordinates.

    Non-target attributes are symmetric about the ideal, so they contribute
    equally to both distances and the answer rests on the target attribute. The
    target offsets come from one of four sign patterns drawn uniformly, which sets
    "smaller value is nearer" and "straddles the ideal" at one half each.
    """
    nonlong = [m for m in range(D) if m != target]
    delta = {m: rng.uniform(*NONTARGET_OFFSET) * rng.choice((-1, 1)) for m in nonlong}
    r2 = sum(v * v for v in delta.values())
    u_n = rng.uniform(*NEARER_OFFSET)
    d_n = np.sqrt(r2 + u_n ** 2)
    u_f2 = (d_n + separation) ** 2 - r2
    if u_f2 <= 0:
        return None
    u_f = np.sqrt(u_f2)
    pattern = SIGN_PATTERNS[rng.integers(4) if pattern_index is None else pattern_index]
    nearer = IDEAL.copy(); farther = IDEAL.copy()
    for m, v in delta.items():
        nearer[m] = IDEAL[m] + v
        farther[m] = IDEAL[m] - v
    nearer[target] = IDEAL[target] + pattern[0] * u_n
    farther[target] = IDEAL[target] + pattern[1] * u_f
    nearer = np.round(nearer, DECIMALS); farther = np.round(farther, DECIMALS)
    if np.any(nearer < LO) or np.any(nearer > HI) or np.any(farther < LO) or np.any(farther > HI):
        return None
    dn = float(np.linalg.norm(nearer - IDEAL)); df = float(np.linalg.norm(farther - IDEAL))
    if not dn < df:
        return None                  # rounding may never flip the answer
    return {"target": int(target), "separation": float(separation),
            "nearer": nearer, "farther": farther,
            "achieved_separation": df - dn,
            "straddles": bool(pattern[0] != pattern[1]),
            "smaller_is_nearer": bool(nearer[target] < farther[target])}


def make_context(rng, roles, probe, max_tries=2000):
    """Context options whose spread per attribute is exactly the role's.

    Columns are drawn, centred on the ideal, decorrelated, and scaled to the
    role's standard deviation, so the context's second moment about the ideal is
    diagonal with the registered variances. A draw is rejected if any value leaves
    the fixed-width band or sits within `EXCLUSION` of a probe value on the same
    attribute, which keeps a context option from being mistaken for a probe
    option.
    """
    probe_vals = np.vstack([probe["nearer"], probe["farther"]])
    for _ in range(max_tries):
        Z = rng.uniform(-1.0, 1.0, size=(N_CONTEXT, D))
        Z -= Z.mean(axis=0)
        Q, _ = np.linalg.qr(Z)
        Z = Q * np.sqrt(N_CONTEXT)              # orthonormal columns, unit rms
        C = IDEAL + Z * np.array([ROLE_SD[roles[m]] for m in range(D)])
        C = np.round(C, DECIMALS)
        if np.any(C < LO) or np.any(C > HI):
            continue
        if np.any(np.abs(C[:, None, :] - probe_vals[None, :, :]) < EXCLUSION):
            continue
        return C
    return None


def workload_moment(options):
    U = np.asarray(options, float) - IDEAL
    return U.T @ U / len(U)


def role_order_holds(options, roles):
    """In-context variance, probe included, must follow the registered roles."""
    v = np.diag(workload_moment(options))
    by = {roles[m]: v[m] for m in range(D)}
    return (by["hi"] / by["mid"] >= RANK_GAP) and (by["mid"] / by["lo"] >= RANK_GAP), by


def build_triplet(rng, target, separation, pattern_index=None):
    """One probe in three contexts: its target attribute high, mid and low."""
    probe = make_probe(rng, target, separation, pattern_index)
    if probe is None:
        return None
    others = [m for m in range(D) if m != target]
    order = list(rng.permutation(D))                 # rendered attribute order
    labels = list(rng.choice(LABEL_POOL, size=D, replace=False))
    n_opt = N_CONTEXT + 2
    pos = rng.choice(n_opt, size=2, replace=False)   # list positions of the probe
    nearer_at_first = bool(rng.integers(2))          # which probe option sits at pos[0]
    prompts = {}
    for role in ("hi", "mid", "lo"):
        rest = [r for r in ("hi", "mid", "lo") if r != role]
        rng.shuffle(rest)
        roles = {target: role, others[0]: rest[0], others[1]: rest[1]}
        ctx = make_context(rng, roles, probe)
        if ctx is None:
            return None
        opts = [None] * n_opt
        first, second = (probe["nearer"], probe["farther"]) if nearer_at_first else (probe["farther"], probe["nearer"])
        opts[pos[0]] = first; opts[pos[1]] = second
        it = iter(ctx)
        for i in range(n_opt):
            if opts[i] is None:
                opts[i] = next(it)
        ok, variances = role_order_holds(opts, roles)
        if not ok:
            return None
        prompts[role] = {"roles": {int(k): v for k, v in roles.items()},
                         "options": [np.asarray(o, float) for o in opts],
                         "variances": variances}
    return {"probe": probe, "order": order, "labels": labels,
            "positions": [int(pos[0]), int(pos[1])],
            "nearer_at": int(pos[0] if nearer_at_first else pos[1]),
            "prompts": prompts}


def render_prompt(triplet, role, question_first=0):
    """Text of one prompt. The probe lines are identical across the triplet."""
    t = triplet
    p = t["prompts"][role]

    def line(x):
        return ", ".join(f"{t['labels'][k]} {fmt(x[t['order'][k]])}" for k in range(D))

    lines = [f"The ideal is: {line(IDEAL)}"]
    for i, o in enumerate(p["options"]):
        lines.append(f"Option {i + 1}: {line(o)}")
    a, b = t["positions"]
    x, y = (a, b) if question_first == 0 else (b, a)
    lines.append(f"Which is closer to the ideal, option {x + 1} or option {y + 1}? "
                 f"Answer with the option number only.")
    return "\n".join(lines)


def probe_lines(triplet, role):
    text = render_prompt(triplet, role).split("\n")
    a, b = triplet["positions"]
    return text[a + 1], text[b + 1]


def build_design(rng, targets=(0, 1, 2), separations=(1.0, 2.0, 4.0, 8.0),
                 n_per_cell=64, max_attempts=100000):
    cells, attempts = {}, {}
    for tg in targets:
        for s in separations:
            # Sign patterns are stratified exactly, n_per_cell/4 of each, so
            # "smaller value is nearer" and "straddles the ideal" are one half
            # in every cell by construction rather than in expectation.
            got, tries = [], 0
            for k in range(4):
                want = n_per_cell // 4 + (1 if k < n_per_cell % 4 else 0)
                have = 0
                while have < want and tries < max_attempts:
                    tries += 1
                    tr = build_triplet(rng, tg, s, pattern_index=k)
                    if tr is not None:
                        got.append(tr); have += 1
            cells[(tg, s)] = got
            attempts[(tg, s)] = tries
    return {"cells": cells, "attempts": attempts,
            "targets": list(targets), "separations": list(separations),
            "n_per_cell": n_per_cell}
