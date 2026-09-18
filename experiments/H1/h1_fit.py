# -*- coding: utf-8 -*-
"""H1 fitter and self-test: psychometric profiles by role, the resolution boundary,
the deliberation-peak smoother, and the four synthetic observers of PREREG-H1 7.1.

Stimuli come from the C3 generator (``c3_sets.build_design``), so the self-test
runs on built triplets and not on an idealised design. One probe, byte-identical,
appears in three contexts that give its target attribute the high, mid or low
role in the in-context workload. Only hi and lo are graded; mid is a monotonicity
check.

Model, per participant and load condition
  p(correct on trial i) = b * [nearer option is first-listed on i]
                        + (1 - b) * (0.5 + (P_c - 0.5) * Phi((x_i - mu_c) / sigma_c))
  c = (attribute, role) cell of trial i, x_i its achieved separation.
  b      response-position mixture, one per load condition, shared across cells.
  P_c    free upper plateau per cell in [0.5, 1], reported as a diagnostic. It is
         not identified when the function is still rising at the top of the
         ladder (the first self-test run extrapolated a 0.77 plateau for an
         observer at 0.63), so the graded endpoint is instead
  A_c    accuracy at the largest ladder separation, the endpoint the C3 rebuild
         registered. A discarded direction shows as a low A_c, not as a shifted
         threshold.
  mu_c, sigma_c   location and width of the cell's psychometric function.
  Lapse per load condition is not a separate parameter. It is reported as
  1 - mean plateau of the hi-role cells, which is the ceiling of the retained
  role, and PREREG-H1 4.1 is worded to match.

Identified quantities
  A[attr, role]  = A_c, accuracy at the largest separation
  s*[attr, role] = separation where the fitted psychometric part reaches the
                   criterion, None (censored) where A_c is below the criterion.
  D_A = mean over attributes of A[hi] - A[lo], one per participant.

Deliberation peak (test block)
  Nadaraya-Watson smoother in log separation, bandwidth one grid step, argmax on
  a fine grid. D_p = mean over attributes of p[lo] - p[hi].

Self-test observers (all decide on a squared weighted distance to the ideal with
Gaussian noise on the difference, plus lapse and the named heuristic)
  rank_budget   weights = in-context variance of each attribute / max variance,
                read from the prompt the observer sees. Retained role near ceiling,
                discarded role a low plateau on the ladder.
  uniform_noise weights = 1 for every attribute. D_A must sit at zero.
  position      chooses the first-listed probe option with probability 0.8, else
                behaves as uniform_noise. D_A must sit at zero and b must recover.
  magnitude     chooses the probe option with the smaller target value with
                probability 0.8, else uniform_noise. D_A must sit at zero.
  A latency model places the peak at a known separation per role and the smoother
  must recover it within tolerance.

Rule 8. Every simulated response is persisted with its trial descriptors in the
raw file, beside the verdicts, so a failed check can be read from its record.

Usage
  python3 h1_fit.py --selftest --out selftest.json --raw selftest_raw.json.gz
  python3 h1_fit.py --fit responses.json --out fit.json      (real data, same schema)
"""
from __future__ import annotations

import argparse
import gzip
import json
import os
import platform
import sys
import time
import numpy as np
from scipy.optimize import minimize
from scipy.special import ndtr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import c3_sets  # noqa: E402

ROLES_GRADED = ("hi", "lo")
ROLES_ALL = ("hi", "mid", "lo")
CRITERION = 0.75          # accuracy criterion for s*, self-test value; registered from the pilot
LADDER = (0.5, 1.0, 2.0, 4.0, 8.0)
N_PER_CELL = 24           # triplets per (attribute, separation) cell in the self-test
N_PARTICIPANTS = 12
TEST_GRID = (0.25, 0.5, 0.71, 1.0, 1.41, 2.0, 4.0)   # multiples of s*
N_TEST_PER_POINT = 20
PEAK_TOL_LOG = np.log(1.25)   # smoother must recover a placed peak within a factor 1.25
DELTA_MIN_SELFTEST = 0.05     # equivalence bound for the null observers; the registered value is fixed from the pilot
KIND_SEED = {"rank_budget": 11, "uniform_noise": 23, "position": 37, "magnitude": 41}   # fixed, not hash()


def Phi(z):
    return ndtr(np.asarray(z, float))


# ----------------------------------------------------------------------------- stimuli
def trials_from_design(design):
    """Flatten a C3 design into calibration trials, one per (triplet, role)."""
    trials = []
    for (tg, s), triplets in design["cells"].items():
        for k, tr in enumerate(triplets):
            pr = tr["probe"]
            for role in ROLES_ALL:
                p = tr["prompts"][role]
                var = np.array([p["variances"][p["roles"][m]] for m in range(c3_sets.D)])
                trials.append({
                    "attr": int(tg), "role": role, "sep": float(pr["achieved_separation"]),
                    "sep_nominal": float(s), "triplet": int(k),
                    "nearer": pr["nearer"].tolist(), "farther": pr["farther"].tolist(),
                    "nearer_first": bool(tr["nearer_at"] == tr["positions"][0]),
                    "smaller_is_nearer": bool(pr["smaller_is_nearer"]),
                    "var": var.tolist(),
                })
    return trials


# ----------------------------------------------------------------------------- observers
def observe(rng, trial, kind, noise_sd=40.0, lapse=0.03, heuristic_p=0.8):
    """Return True if the observer picks the nearer option."""
    ideal = c3_sets.IDEAL
    n = np.asarray(trial["nearer"]); f = np.asarray(trial["farther"])
    if rng.random() < lapse:
        return bool(rng.integers(2))
    if kind == "position" and rng.random() < heuristic_p:
        return bool(trial["nearer_first"])
    if kind == "magnitude" and rng.random() < heuristic_p:
        return bool(trial["smaller_is_nearer"])
    if kind == "rank_budget":
        var = np.asarray(trial["var"]); w = var / var.max()
    else:
        w = np.ones(c3_sets.D)
    d2n = float(np.sum(w * (n - ideal) ** 2)); d2f = float(np.sum(w * (f - ideal) ** 2))
    delta = (d2f - d2n) + rng.normal(0.0, noise_sd)
    return bool(delta > 0)


# ----------------------------------------------------------------------------- fitting
def _unpack(theta, cells):
    b = theta[0]
    pars = {}
    for j, c in enumerate(cells):
        mu, logsig, P = theta[1 + 3 * j: 4 + 3 * j]
        pars[c] = (mu, np.exp(logsig), P)
    return b, pars


def _nll(theta, cells, X, Y, NF, CI):
    b, pars = _unpack(theta, cells)
    p = np.empty_like(X)
    for j, c in enumerate(cells):
        mu, sig, P = pars[c]
        m = CI == j
        p[m] = 0.5 + (P - 0.5) * Phi((X[m] - mu) / sig)
    p = b * NF + (1.0 - b) * p
    p = np.clip(p, 1e-6, 1 - 1e-6)
    return -float(np.sum(Y * np.log(p) + (1 - Y) * np.log(1 - p)))


def fit_profile(responses, roles=ROLES_ALL):
    """Joint MLE over all (attribute, role) cells of one participant and load.

    responses: list of dicts with attr, role, sep, nearer_first, correct.
    """
    cells = sorted({(r["attr"], r["role"]) for r in responses if r["role"] in roles})
    idx = {c: j for j, c in enumerate(cells)}
    R = [r for r in responses if r["role"] in roles]
    if any("sep_nominal" not in r for r in R):
        raise ValueError("every response needs sep_nominal, the ladder step it was drawn at; "
                         "the endpoint is accuracy at the largest step and cannot be read from achieved separations")
    top = max(r["sep_nominal"] for r in R)
    X = np.array([r["sep"] for r in R]); Y = np.array([1.0 if r["correct"] else 0.0 for r in R])
    NF = np.array([1.0 if r["nearer_first"] else 0.0 for r in R])
    CI = np.array([idx[(r["attr"], r["role"])] for r in R])
    smax = float(X.max())
    theta0 = [0.05]; bounds = [(0.0, 0.95)]
    for c in cells:
        m = CI == idx[c]
        acc = Y[m].mean()
        theta0 += [smax / 4, np.log(smax / 4), float(np.clip(acc, 0.55, 0.99))]
        bounds += [(0.05, 4 * smax), (np.log(0.05), np.log(4 * smax)), (0.5, 1.0)]
    best = None
    for start in (theta0, [0.3] + theta0[1:], theta0[:1] + [v if k % 3 != 2 else 0.95 for k, v in enumerate(theta0[1:])]):
        res = minimize(_nll, np.array(start), args=(cells, X, Y, NF, CI), method="L-BFGS-B", bounds=bounds)
        if best is None or res.fun < best.fun:
            best = res
    b, pars = _unpack(best.x, cells)
    out = {"b": float(b), "nll": float(best.fun), "converged": bool(best.success), "cells": {}}
    for c in cells:
        mu, sig, P = pars[c]
        m = CI == idx[c]
        mt = m & np.array([r["sep_nominal"] == top for r in R])
        A = float(Y[mt].mean()) if mt.any() else float("nan")
        out["cells"][f"{c[0]}:{c[1]}"] = {"attr": c[0], "role": c[1], "mu": float(mu), "sigma": float(sig),
                                          "plateau": float(P), "n": int(m.sum()), "acc": float(Y[m].mean()),
                                          "A": A, "n_top": int(mt.sum()),
                                          "s_star": s_star(mu, sig, P, CRITERION) if A >= CRITERION else None}
    hi = [v["A"] for v in out["cells"].values() if v["role"] == "hi"]
    out["lapse_derived"] = float(1.0 - np.mean(hi)) if hi else None
    return out


def s_star(mu, sig, P, crit):
    """Separation where 0.5 + (P - 0.5) Phi((x - mu)/sig) reaches crit, None if never."""
    if P <= crit:
        return None
    from scipy.stats import norm
    z = norm.ppf((crit - 0.5) / (P - 0.5))
    return float(mu + z * sig)


def d_a(fit):
    """Mean over attributes of A[hi] - A[lo], A = accuracy at the largest separation."""
    by = {}
    for v in fit["cells"].values():
        by.setdefault(v["attr"], {})[v["role"]] = v["A"]
    diffs = [d["hi"] - d["lo"] for d in by.values() if "hi" in d and "lo" in d]
    return float(np.mean(diffs)) if diffs else None


def permutation_p(responses, trials, rng, n=5000):
    """Exact null on the top ladder step: hi and lo share the probe within a triplet,
    so swapping their labels within triplet is the null distribution of the role
    difference. Returns the two-sided permutation p-value."""
    top = max(t["sep_nominal"] for t in trials)
    by = {}
    for r in responses:
        t = trials[r["trial"]]
        if t["sep_nominal"] != top:
            continue
        by.setdefault((r["pid"], t["attr"], t["triplet"]), {})[t["role"]] = 1.0 if r["correct"] else 0.0
    d = np.array([v["hi"] - v["lo"] for v in by.values() if "hi" in v and "lo" in v])
    if len(d) == 0:
        return float("nan")
    obs = abs(d.mean())
    signs = rng.choice([-1.0, 1.0], size=(n, len(d)))
    return float((np.abs((signs * d).mean(1)) >= obs).mean())


def bootstrap_mean(values, rng, n=2000):
    v = np.asarray(values, float)
    boots = np.array([rng.choice(v, size=len(v), replace=True).mean() for _ in range(n)])
    return {"mean": float(v.mean()), "ci95": [float(np.percentile(boots, 2.5)), float(np.percentile(boots, 97.5))],
            "n": int(len(v))}


# ----------------------------------------------------------------------------- test block
def smooth_peak(seps, y, grid_step_log):
    """Nadaraya-Watson in log separation, bandwidth one grid step, argmax on a fine grid."""
    lx = np.log(np.asarray(seps, float)); y = np.asarray(y, float)
    fine = np.linspace(lx.min(), lx.max(), 400)
    h = grid_step_log
    W = np.exp(-0.5 * ((fine[:, None] - lx[None, :]) / h) ** 2)
    yhat = (W @ y) / W.sum(1)
    return float(np.exp(fine[int(np.argmax(yhat))]))


def simulate_test_block(rng, s_by_cell, peak_mult_by_role, base=800.0, amp=600.0, tau=0.45, sd=150.0):
    """Latency trials on the registered grid around each cell's s*, peak placed at
    peak_mult_by_role[role] * s*. Returns trials and the placed peaks."""
    trials, placed = [], {}
    for (attr, role), s in s_by_cell.items():
        if s is None:
            continue
        p0 = peak_mult_by_role[role] * s
        placed[f"{attr}:{role}"] = p0
        for mult in TEST_GRID:
            x = mult * s
            for _ in range(N_TEST_PER_POINT):
                lat = base + amp * np.exp(-0.5 * ((np.log(x) - np.log(p0)) / tau) ** 2) + rng.normal(0, sd)
                trials.append({"attr": attr, "role": role, "sep": float(x), "latency": float(lat)})
    return trials, placed


def peaks_from_test(trials):
    step = float(np.median(np.diff(np.log(TEST_GRID))))
    out = {}
    by = {}
    for t in trials:
        by.setdefault((t["attr"], t["role"]), []).append(t)
    for (attr, role), ts in by.items():
        out[f"{attr}:{role}"] = smooth_peak([t["sep"] for t in ts], [t["latency"] for t in ts], step)
    return out


# ----------------------------------------------------------------------------- self-test
def selftest(seed, out_path, raw_path):
    t0 = time.time()
    rng = np.random.default_rng(seed)
    design = c3_sets.build_design(rng, separations=LADDER, n_per_cell=N_PER_CELL)
    trials = trials_from_design(design)
    report = {"seed": seed, "host": platform.node(), "started_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(t0)),
              "ladder": LADDER, "n_per_cell": N_PER_CELL, "n_participants": N_PARTICIPANTS,
              "criterion": CRITERION, "n_calibration_trials_per_participant": len(trials),
              "construction": {"cells_filled": {f"{k[0]}:{k[1]}": len(v) for k, v in design["cells"].items()},
                               "attempts": {f"{k[0]}:{k[1]}": int(v) for k, v in design["attempts"].items()}},
              "observers": {}, "checks": []}
    raw = {"trials": trials, "responses": {}}
    checks = []
    report["stage_times_s"] = {"construction": round(time.time() - t0, 1)}
    print("construction done", report["stage_times_s"], flush=True)

    def check(name, ok, detail):
        checks.append({"check": name, "pass": bool(ok), "detail": detail})

    # construction: every cell full, probe identical across roles is by construction of c3_sets
    check("construction_cells_full", all(len(v) == N_PER_CELL for v in design["cells"].values()),
          report["construction"]["cells_filled"])

    for kind in ("rank_budget", "uniform_noise", "position", "magnitude"):
        fits, DA, bs, raw_resp = [], [], [], []
        for pid in range(N_PARTICIPANTS):
            prng = np.random.default_rng(seed * 1000 + pid + KIND_SEED[kind])
            resp = []
            for i, tr in enumerate(trials):
                c = observe(prng, tr, kind)
                resp.append({"pid": pid, "trial": i, "attr": tr["attr"], "role": tr["role"], "sep": tr["sep"],
                             "sep_nominal": tr["sep_nominal"],
                             "nearer_first": tr["nearer_first"], "correct": c})
            raw_resp.extend(resp)
            fit = fit_profile(resp)
            fits.append(fit); DA.append(d_a(fit)); bs.append(fit["b"])
        raw["responses"][kind] = raw_resp
        report["stage_times_s"][kind] = round(time.time() - t0, 1)
        print("observer", kind, "fitted", report["stage_times_s"][kind], flush=True)
        boot = bootstrap_mean(DA, rng)
        plat = {role: float(np.mean([v["A"] for f in fits for v in f["cells"].values() if v["role"] == role]))
                for role in ROLES_ALL}
        fitted_plateau = {role: float(np.mean([v["plateau"] for f in fits for v in f["cells"].values() if v["role"] == role]))
                          for role in ROLES_ALL}
        cens = {role: int(sum(1 for f in fits for v in f["cells"].values() if v["role"] == role and v["s_star"] is None))
                for role in ROLES_ALL}
        report["observers"][kind] = {"D_A": boot, "mean_A_by_role": plat, "mean_fitted_plateau_by_role": fitted_plateau,
                                     "censored_s_star_by_role": cens,
                                     "mean_b": float(np.mean(bs)), "lapse_derived_mean": float(np.mean([f["lapse_derived"] for f in fits])),
                                     "converged_all": all(f["converged"] for f in fits), "fits": fits}
        if kind == "rank_budget":
            check("rank_budget_retained_role_near_ceiling", plat["hi"] >= 0.90, plat)
            check("rank_budget_discarded_role_low_endpoint", plat["lo"] <= 0.70, {"A": plat, "fitted_plateau": fitted_plateau})
            check("rank_budget_D_A_positive_and_ci_excludes_zero", boot["ci95"][0] > 0.0, boot)
            check("rank_budget_monotone_hi_mid_lo", plat["hi"] >= plat["mid"] >= plat["lo"], plat)
            check("rank_budget_low_role_s_star_censored_in_most_cells",
                  cens["lo"] >= 0.5 * sum(1 for f in fits for v in f["cells"].values() if v["role"] == "lo"), cens)
        else:
            check(f"{kind}_D_A_within_equivalence_bound",
                  max(abs(boot["ci95"][0]), abs(boot["ci95"][1])) < DELTA_MIN_SELFTEST, boot)
            check(f"{kind}_D_A_small", abs(boot["mean"]) < DELTA_MIN_SELFTEST, boot)
            check(f"{kind}_D_A_exact_null_permutation", permutation_p(raw_resp, trials, rng) > 0.01,
                  {"permutation_p": permutation_p(raw_resp, trials, rng)})
        if kind == "position":
            check("position_b_recovered", abs(float(np.mean(bs)) - 0.8 * (1 - 0.03)) < 0.08, {"mean_b": float(np.mean(bs))})
        if kind in ("uniform_noise", "magnitude"):
            check(f"{kind}_b_near_zero", float(np.mean(bs)) < 0.1, {"mean_b": float(np.mean(bs))})

    # test block: peaks placed from the rank-budget participant 0's identified s* on hi cells,
    # and, because the low role is censored there, from a nominal s* to exercise the smoother.
    f0 = report["observers"]["rank_budget"]["fits"][0]
    s_by = {}
    for v in f0["cells"].values():
        if v["role"] in ROLES_GRADED:
            s_by[(v["attr"], v["role"])] = v["s_star"] if v["s_star"] is not None else 6.0
    mult = {"hi": 1.0, "lo": 1.6}
    ttrials, placed = simulate_test_block(rng, s_by, mult)
    found = peaks_from_test(ttrials)
    errs = {k: abs(np.log(found[k]) - np.log(placed[k])) for k in placed}
    check("smoother_recovers_placed_peaks", all(e <= PEAK_TOL_LOG for e in errs.values()),
          {k: {"placed": placed[k], "found": found[k], "log_err": float(errs[k])} for k in placed})
    Dp = np.mean([found[f"{a}:lo"] - found[f"{a}:hi"] for a in range(c3_sets.D) if f"{a}:lo" in found and f"{a}:hi" in found])
    Ds = np.mean([placed[f"{a}:lo"] - placed[f"{a}:hi"] for a in range(c3_sets.D) if f"{a}:lo" in placed and f"{a}:hi" in placed])
    check("D_p_tracks_placed_displacement", abs(Dp - Ds) <= 0.25 * abs(Ds) + 0.5, {"D_p": float(Dp), "placed": float(Ds)})
    raw["test_block"] = {"trials": ttrials, "placed": placed, "found": found}

    report["checks"] = checks
    report["verdict"] = "PASS" if all(c["pass"] for c in checks) else "FAIL"
    report["n_checks"] = len(checks); report["n_failed"] = sum(1 for c in checks if not c["pass"])
    report["elapsed_s"] = round(time.time() - t0, 1)
    with open(out_path, "w") as f:
        json.dump(report, f, indent=1, default=float)
    with gzip.open(raw_path, "wt") as f:
        json.dump(raw, f, default=float)
    return report


def fit_file(path, out_path):
    """Real data. path holds {"participants": {pid: {"load": {"calibration": [...], "test": [...]}}}}."""
    data = json.load(open(path))
    out = {"participants": {}}
    for pid, loads in data["participants"].items():
        out["participants"][pid] = {}
        for load, blocks in loads.items():
            fit = fit_profile(blocks["calibration"])
            rec = {"fit": fit, "D_A": d_a(fit)}
            if blocks.get("test"):
                rec["peaks"] = peaks_from_test(blocks["test"])
            out["participants"][pid][load] = rec
    with open(out_path, "w") as f:
        json.dump(out, f, indent=1, default=float)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--fit", default=None)
    ap.add_argument("--out", default="selftest.json")
    ap.add_argument("--raw", default="selftest_raw.json.gz")
    ap.add_argument("--seed", type=int, default=20260918)
    a = ap.parse_args()
    if a.selftest:
        r = selftest(a.seed, a.out, a.raw)
        print(json.dumps({k: r[k] for k in ("verdict", "n_checks", "n_failed", "elapsed_s", "host")}))
        for c in r["checks"]:
            print(("PASS " if c["pass"] else "FAIL ") + c["check"])
        for k, v in r["observers"].items():
            print(k, "D_A", round(v["D_A"]["mean"], 3), v["D_A"]["ci95"], "A", {r_: round(p, 3) for r_, p in v["mean_A_by_role"].items()}, "fitted plateau", {r_: round(p, 3) for r_, p in v["mean_fitted_plateau_by_role"].items()},
                  "b", round(v["mean_b"], 3))
    elif a.fit:
        fit_file(a.fit, a.out)
        print("written", a.out)
    else:
        ap.print_help()


if __name__ == "__main__":
    main()
