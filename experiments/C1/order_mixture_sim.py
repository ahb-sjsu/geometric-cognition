"""Re-derive the order-probe identification sentence under two readings of the excess.

Uses the probe's own estimator and held-out gate (c1_order.py). Options are drawn
from the registered box with the registered ideal. A share q of pairs is decided by
content (the truly nearer option in both orders); the rest by position, choosing the
first-shown option with probability p in each order independently. Only pairs that
agree across orders are kept, as in both_orders().

Readings
  mixture   q = 0.16,   p = 0.7375/0.84  (fits first-position 0.8175 and agreement 0.34)
  excess    q = 0.0425, p = 0.8175       (17 of 400 informative)

For each, and each n, record the held-out gate statistic (5-fold CV accuracy on kept
pairs, gate >= 0.80), the ceiling f + (1 - f)/2, and identification: the fitted
metric's order accuracy against the TRUE metric on 4000 fresh pairs, and its relative
error.
"""
import json
import sys

import numpy as np

sys.path.insert(0, ".")
from c1_order import calibrate_from_order, heldout_order_accuracy  # noqa: E402

LO = np.array([0.0, 0.0, 0.0])
HI = np.array([100.0, 45.0, 75.0])
T = np.array([75.0, 15.0, 20.0])
READINGS = {"mixture": (0.16, 0.7375 / 0.84), "excess": (0.0425, 0.8175)}
SIZES = [400, 1600, 6400, 25600]
REPS = 20


def true_metric(rng):
    M = rng.normal(size=(3, 3))
    G = M @ M.T + 0.5 * np.eye(3)
    return G * 3 / np.trace(G)


def qform(X, G):
    D = X - T
    return np.einsum("ni,ij,nj->n", D, G, D)


def one(rng, G, q, p, n):
    A = rng.uniform(LO, HI, size=(n, 3))
    B = rng.uniform(LO, HI, size=(n, 3))
    truth = (qform(A, G) < qform(B, G)).astype(float)       # 1 if A nearer
    content = rng.random(n) < q
    f = rng.random(n) < p                                   # forward picks first (A)
    r = rng.random(n) < p                                   # reverse picks first (B)
    fwd_A = np.where(content, truth == 1, f)
    rev_A = np.where(content, truth == 1, ~r)
    keep = fwd_A == rev_A
    y = fwd_A[keep].astype(float)
    frac_info = float(content[keep].mean())
    out = {"kept": int(keep.sum()), "info_share_of_kept": frac_info,
           "ceiling": frac_info + (1 - frac_info) / 2}
    if keep.sum() < 90:
        out.update({"heldout": None, "fits": False})
        return out
    ho = heldout_order_accuracy(A[keep], B[keep], y)
    cal = calibrate_from_order(A[keep], B[keep], y)
    Gh = np.array(cal["G"])
    A2 = rng.uniform(LO, HI, size=(4000, 3))
    B2 = rng.uniform(LO, HI, size=(4000, 3))
    th = np.array(cal["t"])
    DA, DB = A2 - th, B2 - th
    pred = np.einsum("ni,ij,nj->n", DA, Gh, DA) < np.einsum("ni,ij,nj->n", DB, Gh, DB)
    tru = qform(A2, G) < qform(B2, G)
    out.update({"heldout": ho["mean"], "gate_pass": bool(ho["mean"] >= 0.80),
                "true_order_accuracy": float(np.mean(pred == tru)),
                "metric_rel_error": float(np.linalg.norm(Gh - G) / np.linalg.norm(G)),
                "fits": True})
    return out


def main():
    rng = np.random.default_rng(20260925)
    res = {}
    for name, (q, p) in READINGS.items():
        res[name] = {"q": q, "p": p, "sizes": {}}
        for n in SIZES:
            runs = [one(rng, true_metric(rng), q, p, n) for _ in range(REPS)]
            fit = [x for x in runs if x["fits"]]
            summ = lambda k: (float(np.mean([x[k] for x in fit])), float(np.min([x[k] for x in fit])),
                              float(np.max([x[k] for x in fit]))) if fit else None
            res[name]["sizes"][n] = {
                "kept_mean": float(np.mean([x["kept"] for x in runs])),
                "info_share_mean": float(np.mean([x["info_share_of_kept"] for x in runs])),
                "ceiling_mean": float(np.mean([x["ceiling"] for x in runs])),
                "fitted_runs": len(fit),
                "heldout_mean_min_max": summ("heldout"),
                "gate_passes": int(sum(x.get("gate_pass", False) for x in fit)),
                "true_order_accuracy_mean_min_max": summ("true_order_accuracy"),
                "metric_rel_error_mean_min_max": summ("metric_rel_error"),
            }
            s = res[name]["sizes"][n]
            print(name, n, "kept", round(s["kept_mean"], 1), "info", round(s["info_share_mean"], 3),
                  "ceiling", round(s["ceiling_mean"], 3), "heldout", s["heldout_mean_min_max"],
                  "passes", s["gate_passes"], "/", s["fitted_runs"],
                  "true-order acc", s["true_order_accuracy_mean_min_max"],
                  "G err", s["metric_rel_error_mean_min_max"], flush=True)
    json.dump(res, open("order_mixture_sim.json", "w"), indent=1)


if __name__ == "__main__":
    main()
