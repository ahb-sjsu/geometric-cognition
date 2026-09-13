# -*- coding: utf-8 -*-
"""C1 calibration: recover the metric and the ideal from an evaluator's reports.

The gate's content depends on this file. If the metric is fitted to the graded
choices then the retained subspace is chosen rather than derived, and the gate
grades a representation against the choices that produced it. So the calibration
block is disjoint from every graded pair, the estimate is frozen before a graded
pair is drawn, and the recovery is checked against a synthetic evaluator whose
metric is known.

The model. An evaluator reports a distance r for an option x. Under the
evaluation object the squared report is a quadratic form in x,

    r^2 = (x - t)^T G (x - t) = x^T Q x + b^T x + c,
    Q = G,  b = -2 G t,  c = t^T G t.

That is linear in the ten parameters of (Q, b, c) for d = 3, so the fit is least
squares and needs no optimizer. The metric is identified up to scale and the
ideal up to the metric's kernel, which is GET Theorem 4, so the estimate is
normalised to trace d and a near-singular G is reported rather than inverted.

Run the self-test with

    python c1_calibrate.py --selftest

The registered self-test of PREREG-C1 section 7 runs on Atlas and its output is
committed. Running this locally checks that the estimator is correct and is not
that record.
"""
from __future__ import annotations

import argparse
import json
import sys

import numpy as np

# Numerical floors. A metric whose smallest eigenvalue falls below EIG_FLOOR
# relative to its largest is reported as near-singular rather than inverted,
# because the ideal is then identified only up to the kernel.
EIG_FLOOR = 1e-6
PSD_CLIP = 1e-9


def design(X: np.ndarray) -> np.ndarray:
    """Monomials of the quadratic form, ordered to match `unpack`.

    For d = 3 the columns are x1^2, x2^2, x3^2, 2x1x2, 2x1x3, 2x2x3, x1, x2, x3, 1.
    """
    n, d = X.shape
    cols = [X[:, i] ** 2 for i in range(d)]
    cols += [2.0 * X[:, i] * X[:, j] for i in range(d) for j in range(i + 1, d)]
    cols += [X[:, i] for i in range(d)]
    cols += [np.ones(n)]
    return np.column_stack(cols)


def unpack(theta: np.ndarray, d: int) -> tuple[np.ndarray, np.ndarray, float]:
    """Inverse of `design`'s ordering. Returns (Q, b, c)."""
    Q = np.zeros((d, d))
    idx = 0
    for i in range(d):
        Q[i, i] = theta[idx]
        idx += 1
    for i in range(d):
        for j in range(i + 1, d):
            Q[i, j] = Q[j, i] = theta[idx]
            idx += 1
    b = theta[idx:idx + d]
    c = float(theta[idx + d])
    return Q, b, c


def psd_project(Q: np.ndarray) -> tuple[np.ndarray, float]:
    """Nearest PSD matrix in Frobenius norm, and how much was clipped.

    The clip is reported because a metric that needed a large clip was not
    recovered, and section 7 of the registration stops the gate in that case.
    """
    w, V = np.linalg.eigh((Q + Q.T) / 2.0)
    clipped = float(-min(w.min(), 0.0))
    w = np.clip(w, PSD_CLIP, None)
    return V @ np.diag(w) @ V.T, clipped


def sqrtm_psd(G: np.ndarray, inverse: bool = False) -> np.ndarray:
    w, V = np.linalg.eigh((G + G.T) / 2.0)
    w = np.clip(w, PSD_CLIP, None)
    s = 1.0 / np.sqrt(w) if inverse else np.sqrt(w)
    return V @ np.diag(s) @ V.T


def calibrate(X: np.ndarray, r: np.ndarray) -> dict:
    """Estimate the metric and the ideal from reported distances.

    X is (n, d) options, r is (n,) reported distances. Reports that are not
    finite are dropped and counted, because an unparsable report is indifference
    and carries no distance.
    """
    X = np.asarray(X, dtype=float)
    r = np.asarray(r, dtype=float)
    keep = np.isfinite(r)
    dropped = int((~keep).sum())
    X, r = X[keep], r[keep]
    n, d = X.shape
    if n < 10 * d:
        raise ValueError(f"calibration block too small, {n} usable reports for d = {d}")

    A = design(X)
    theta, *_ = np.linalg.lstsq(A, r ** 2, rcond=None)
    Q, b, c = unpack(theta, d)
    G, clipped = psd_project(Q)

    w = np.linalg.eigvalsh(G)
    cond_ok = bool(w.min() > EIG_FLOOR * w.max())
    t = np.linalg.solve(G, -0.5 * b) if cond_ok else np.linalg.lstsq(G, -0.5 * b, rcond=None)[0]

    # Scale is not identified. Fix it so that trace(G) = d, which makes the
    # whitened coordinates comparable across calibration draws.
    scale = d / float(np.trace(G))
    G = G * scale

    resid = A @ theta - r ** 2
    denom = float(np.sum((r ** 2 - np.mean(r ** 2)) ** 2))
    return {
        "d": d,
        "n_used": int(n),
        "n_dropped": dropped,
        "G": G.tolist(),
        "t": t.tolist(),
        "psd_clip": clipped,
        "well_conditioned": cond_ok,
        "consistency_c": float(c - t @ (G / scale) @ t),
        "rms_residual": float(np.sqrt(np.mean(resid ** 2))),
        "r2": float(1.0 - np.sum(resid ** 2) / denom) if denom > 0 else float("nan"),
    }


def workload_moment(G: np.ndarray, t: np.ndarray, X: np.ndarray) -> np.ndarray:
    """M = E[ G^{1/2}(x - t)(x - t)^T G^{1/2} ] over the calibration options."""
    Gh = sqrtm_psd(G)
    U = (np.asarray(X, dtype=float) - np.asarray(t, dtype=float)) @ Gh
    return U.T @ U / U.shape[0]


def retained(G: np.ndarray, t: np.ndarray, X: np.ndarray, k: int) -> dict:
    """The rank-k retained subspace and the share of the trace it discards.

    The subspace is the top-k eigenspace of M and is therefore derived from the
    estimated metric. Nobody chooses it.
    """
    M = workload_moment(G, t, X)
    w, V = np.linalg.eigh(M)
    order = np.argsort(w)[::-1]
    w, V = w[order], V[:, order]
    Pi = V[:, :k] @ V[:, :k].T
    total = float(w.sum())
    return {
        "k": int(k),
        "eigenvalues": w.tolist(),
        "Pi_whitened": Pi.tolist(),
        "basis_whitened": V[:, :k].tolist(),
        "discarded_trace_share": float(w[k:].sum() / total) if total > 0 else 0.0,
    }


def project(x: np.ndarray, G: np.ndarray, t: np.ndarray, Pi: np.ndarray) -> np.ndarray:
    """Project an option onto the retained subspace, in attribute coordinates.

    Whiten, project, unwhiten, recentre. This is what the evaluator is shown at
    a reduced budget, rendered at the same precision as an unprojected option.
    """
    Gh, Ghi = sqrtm_psd(G), sqrtm_psd(G, inverse=True)
    t = np.asarray(t, dtype=float)
    return t + (np.asarray(x, dtype=float) - t) @ Gh @ np.asarray(Pi) @ Ghi


def selftest(seed: int = 20260913, n: int = 600, verbose: bool = True) -> dict:
    """A synthetic evaluator with a known metric and a known ideal.

    Recovery is graded up to scale, because scale is not identified. The
    registration stops the gate if the recovery is worse than the tolerance
    recorded in its section 7.
    """
    rng = np.random.default_rng(seed)
    d = 3
    B = rng.normal(size=(d, d))
    G_true = B @ B.T + 0.5 * np.eye(d)
    G_true *= d / np.trace(G_true)
    t_true = np.array([50.0, 50.0, 50.0])

    X = rng.uniform(0.0, 100.0, size=(n, d))
    D = X - t_true
    r = np.sqrt(np.einsum("ni,ij,nj->n", D, G_true, D))

    out = calibrate(X, r)
    G_hat = np.array(out["G"])
    t_hat = np.array(out["t"])

    # Compare up to scale. trace normalisation already fixes it, so a direct
    # relative Frobenius error is the right measure.
    g_err = float(np.linalg.norm(G_hat - G_true) / np.linalg.norm(G_true))
    t_err = float(np.linalg.norm(t_hat - t_true) / np.linalg.norm(t_true))

    # The retained subspace must match the truth's, which is the object the gate
    # actually uses. Compare by principal angle rather than by basis vectors.
    res_hat = retained(G_hat, t_hat, X, k=2)
    res_true = retained(G_true, t_true, X, k=2)
    Bh = np.array(res_hat["basis_whitened"])
    Bt = np.array(res_true["basis_whitened"])
    sv = np.linalg.svd(Bh.T @ Bt, compute_uv=False)
    max_angle = float(np.degrees(np.arccos(np.clip(sv.min(), -1.0, 1.0))))

    res = {
        "seed": seed, "n": n,
        "metric_rel_error": g_err,
        "ideal_rel_error": t_err,
        "subspace_max_principal_angle_deg": max_angle,
        "discarded_trace_share_k2": res_hat["discarded_trace_share"],
        "rms_residual": out["rms_residual"],
        "r2": out["r2"],
        "psd_clip": out["psd_clip"],
        "pass": bool(g_err < 1e-6 and t_err < 1e-6 and max_angle < 1e-3),
    }
    if verbose:
        print("C1 calibration self-test")
        for key in ("metric_rel_error", "ideal_rel_error",
                    "subspace_max_principal_angle_deg",
                    "discarded_trace_share_k2", "r2", "psd_clip"):
            print(f"  {key:36s} {res[key]:.3e}")
        print(f"  {'verdict':36s} {'PASS' if res['pass'] else 'FAIL'}")
    return res


def selftest_noisy(seed: int = 20260913, n: int = 600, sigma: float = 0.5) -> dict:
    """The same recovery with reporting noise, which is the realistic case.

    An evaluator rounds and misreports. This says how much of that the estimator
    tolerates before the retained subspace moves, and the pilot fixes the
    tolerance the registration uses.
    """
    rng = np.random.default_rng(seed)
    d = 3
    B = rng.normal(size=(d, d))
    G_true = B @ B.T + 0.5 * np.eye(d)
    G_true *= d / np.trace(G_true)
    t_true = np.array([50.0, 50.0, 50.0])
    X = rng.uniform(0.0, 100.0, size=(n, d))
    D = X - t_true
    r = np.sqrt(np.einsum("ni,ij,nj->n", D, G_true, D)) + rng.normal(0.0, sigma, size=n)
    r = np.clip(r, 0.0, None)

    out = calibrate(X, r)
    G_hat, t_hat = np.array(out["G"]), np.array(out["t"])
    Bh = np.array(retained(G_hat, t_hat, X, k=2)["basis_whitened"])
    Bt = np.array(retained(G_true, t_true, X, k=2)["basis_whitened"])
    sv = np.linalg.svd(Bh.T @ Bt, compute_uv=False)
    return {
        "sigma": sigma,
        "metric_rel_error": float(np.linalg.norm(G_hat - G_true) / np.linalg.norm(G_true)),
        "ideal_rel_error": float(np.linalg.norm(t_hat - t_true) / np.linalg.norm(t_true)),
        "subspace_max_principal_angle_deg":
            float(np.degrees(np.arccos(np.clip(sv.min(), -1.0, 1.0)))),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--noise-sweep", action="store_true",
                    help="recovery against reporting noise, to size the pilot's tolerance")
    ap.add_argument("--reports", help="JSON with options and reported distances")
    ap.add_argument("--out", help="where to write the frozen calibration")
    ap.add_argument("--k", type=int, default=2)
    args = ap.parse_args()

    if args.selftest:
        res = selftest()
        if args.noise_sweep:
            print("\nrecovery against reporting noise")
            print(f"  {'sigma':>6} {'metric':>10} {'ideal':>10} {'angle_deg':>10}")
            for s in (0.1, 0.25, 0.5, 1.0, 2.0, 4.0):
                n = selftest_noisy(sigma=s)
                print(f"  {s:6.2f} {n['metric_rel_error']:10.4f} "
                      f"{n['ideal_rel_error']:10.4f} "
                      f"{n['subspace_max_principal_angle_deg']:10.3f}")
        return 0 if res["pass"] else 1

    if not args.reports:
        ap.error("give --selftest or --reports")
    blk = json.load(open(args.reports, encoding="utf-8"))
    out = calibrate(np.array(blk["options"]), np.array(blk["reports"]))
    out["retained"] = {str(k): retained(np.array(out["G"]), np.array(out["t"]),
                                        np.array(blk["options"]), k)
                       for k in range(1, np.array(blk["options"]).shape[1])}
    if args.out:
        json.dump(out, open(args.out, "w", encoding="utf-8"), indent=1)
        print(f"frozen calibration written to {args.out}")
    else:
        print(json.dumps(out, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())


class NoSpectralGap(RuntimeError):
    """The workload moment does not identify a rank-k retained subspace."""


def spectral_gap(G, t, X, k: int, n_null: int = 400, seed: int = 0) -> dict:
    """The gap at k, and where it sits against an isotropic null at this n.

    C1's first design drew consequences uniformly on a cube and put the ideal at
    the cube's centroid, which makes M isotropic analytically. A top-k eigenspace
    of an isotropic matrix is whatever the finite sample happened to favour, so
    the "budget" was a random plane and the graded contrast survived being
    replaced by one. The ratio alone does not catch that, because a finite sample
    of an isotropic M still produces a ratio above one. The null does.
    """
    M = workload_moment(G, t, X)
    w = np.sort(np.linalg.eigvalsh(M))[::-1]
    obs = float(w[k - 1] / w[k]) if k < len(w) and w[k] > 0 else float("inf")
    n, d = np.asarray(X).shape
    rng = np.random.default_rng(seed)
    null = []
    for _ in range(n_null):
        U = rng.normal(size=(n, d))
        e = np.sort(np.linalg.eigvalsh(U.T @ U / n))[::-1]
        null.append(e[k - 1] / e[k])
    null = np.sort(null)
    return {"k": int(k), "eigenvalues": w.tolist(), "gap": obs,
            "null_median": float(np.median(null)),
            "null_p975": float(np.quantile(null, 0.975)),
            "exceeds_null": bool(obs > np.quantile(null, 0.975))}


def assert_spectral_gap(G, t, X, k: int, floor: float, **kw) -> dict:
    """Refuse to run a budget that is not identified. Accounting beats recall.

    A rank budget is a choice of top-k eigenspace, and that eigenspace exists as
    a fact about the evaluator only where M has a gap at k. This is the rule the
    cold reread found missing, encoded as a guard rather than left as a sentence.
    """
    g = spectral_gap(G, t, X, k, **kw)
    if g["gap"] < floor or not g["exceeds_null"]:
        raise NoSpectralGap(
            f"budget k={k} is not identified. gap {g['gap']:.3f} against a "
            f"registered floor of {floor} and an isotropic null whose 97.5th "
            f"percentile at this sample size is {g['null_p975']:.3f}. "
            f"Eigenvalues {np.round(g['eigenvalues'], 1).tolist()}. A top-k "
            f"eigenspace of a gapless moment is a random plane, and the graded "
            f"contrast survives replacing it with one.")
    return g
