# -*- coding: utf-8 -*-
"""Order-based calibration for C1, and the chooser that feeds it.

The reported-distance instrument failed its calibration gate. The sweep showed
the failure is arithmetic rather than elicitation, since the prompt that states
the formula scored worse than three that do not. GET Theorem 4 identifies the
metric up to scale and the ideal up to the metric's kernel from the order on an
open set, so reported distances were never required by the theory. This module
asks the evaluator only which of two options is nearer.

The estimator. Write the squared distance as a quadratic form,

    q(x) = phi(x) . theta + c,
    phi(x) = (x1^2, x2^2, x3^2, 2x1x2, 2x1x3, 2x2x3, x1, x2, x3),
    theta  = (Q11, Q22, Q33, Q12, Q13, Q23, b1, b2, b3),  Q = G, b = -2Gt.

A comparison says q(a) < q(b), and the constant cancels in the difference, so
every comparison is one linear constraint on theta,

    (phi(a) - phi(b)) . theta < 0.

Identification from order is therefore a linear classification problem on
difference features, which is why it needs no arithmetic from the evaluator.
Scale is not identified, since any positive multiple of theta induces the same
order, so the recovered metric is normalised to trace d. The constant c is not
identified either and is not needed, because the ideal comes from Q and b.

    python c1_order.py --selftest
"""
from __future__ import annotations

import argparse
import json
import re
import sys

import numpy as np

from c1_calibrate import EIG_FLOOR, psd_project, sqrtm_psd

# ------------------------------------------------------------------ features


def phi(X: np.ndarray) -> np.ndarray:
    """Design without the constant. Matches `theta`'s ordering below."""
    X = np.atleast_2d(np.asarray(X, dtype=float))
    n, d = X.shape
    cols = [X[:, i] ** 2 for i in range(d)]
    cols += [2.0 * X[:, i] * X[:, j] for i in range(d) for j in range(i + 1, d)]
    cols += [X[:, i] for i in range(d)]
    return np.column_stack(cols)


def unpack_theta(theta: np.ndarray, d: int) -> tuple[np.ndarray, np.ndarray]:
    Q = np.zeros((d, d))
    idx = 0
    for i in range(d):
        Q[i, i] = theta[idx]
        idx += 1
    for i in range(d):
        for j in range(i + 1, d):
            Q[i, j] = Q[j, i] = theta[idx]
            idx += 1
    return Q, theta[idx:idx + d]


# ------------------------------------------------------------------ estimator


def _fit_logistic(Z: np.ndarray, y: np.ndarray, l2: float = 1e-3,
                  iters: int = 400) -> np.ndarray:
    """Newton steps on a ridge-penalised logistic loss.

    Written out rather than imported so the module has no dependency beyond
    numpy, which is what the rest of this gate uses.
    """
    w = np.zeros(Z.shape[1])
    for _ in range(iters):
        z = Z @ w
        p = 1.0 / (1.0 + np.exp(-np.clip(z, -30, 30)))
        g = Z.T @ (p - y) + l2 * w
        s = np.clip(p * (1 - p), 1e-9, None)
        H = (Z * s[:, None]).T @ Z + l2 * np.eye(Z.shape[1])
        try:
            step = np.linalg.solve(H, g)
        except np.linalg.LinAlgError:
            step = np.linalg.lstsq(H, g, rcond=None)[0]
        w -= step
        if np.max(np.abs(step)) < 1e-10:
            break
    return w


def calibrate_from_order(A: np.ndarray, B: np.ndarray, a_nearer: np.ndarray,
                         l2: float = 1e-3) -> dict:
    """Recover the metric and the ideal from binary comparisons.

    A and B are (n, d) option arrays, `a_nearer` is 1 where the evaluator judged
    A nearer to the ideal and 0 where it judged B nearer. Comparisons the
    evaluator called equal, or that disagreed between presentation orders, are
    dropped by the caller before they reach here.
    """
    A, B = np.asarray(A, float), np.asarray(B, float)
    y = np.asarray(a_nearer, float)
    d = A.shape[1]
    # A nearer means q(A) < q(B), so -(phi(A) - phi(B)) . theta should be large.
    Z = -(phi(A) - phi(B))
    if len(y) < 10 * Z.shape[1]:
        raise ValueError(f"too few comparisons, {len(y)} for {Z.shape[1]} parameters")

    theta = _fit_logistic(Z, y, l2=l2)
    Q, b = unpack_theta(theta, d)
    G, clipped = psd_project(Q)

    w = np.linalg.eigvalsh(G)
    cond_ok = bool(w.max() > 0 and w.min() > EIG_FLOOR * w.max())
    t = (np.linalg.solve(G, -0.5 * b) if cond_ok
         else np.linalg.lstsq(G, -0.5 * b, rcond=None)[0])

    scale = d / float(np.trace(G)) if np.trace(G) > 0 else 1.0
    G = G * scale

    pred = (Z @ theta) > 0
    acc = float(np.mean(pred == (y > 0.5)))
    return {"d": d, "n_comparisons": int(len(y)),
            "G": G.tolist(), "t": t.tolist(),
            "psd_clip": float(clipped), "well_conditioned": cond_ok,
            "order_accuracy": acc}


# ------------------------------------------------------------------ chooser


CHOOSER_TEMPLATE = (
    "The ideal is: {ideal}\n"
    "Option A: {first}\n"
    "Option B: {second}\n"
    "Which option is closer to the ideal? Answer with a single letter, A or B."
)


class LMChooser:
    """Asks which of two options is nearer. A comparison, not a computation.

    Every pair is shown in both presentation orders. G3 discarded a chooser
    because it measured its own position bias before it measured anything else,
    so the bias rate is reported here and gated on before any metric is fitted.
    """

    def __init__(self, cfg: dict):
        import torch
        from transformers import AutoModelForCausalLM, AutoTokenizer
        self.torch = torch
        mid = cfg["model_id"]
        self.tok = AutoTokenizer.from_pretrained(mid)
        self.model = AutoModelForCausalLM.from_pretrained(
            mid, device_map={"": 0}, dtype=torch.bfloat16).eval()
        self.template = cfg.get("chooser_prompt_template", CHOOSER_TEMPLATE)
        self.chat = (bool(cfg.get("use_chat_template", True))
                     and self.tok.chat_template is not None)
        self.unparsed = 0

    def _prompt(self, ideal: str, first: str, second: str) -> str:
        user = self.template.format(ideal=ideal, first=first, second=second)
        if self.chat:
            return self.tok.apply_chat_template(
                [{"role": "user", "content": user}], tokenize=False,
                add_generation_prompt=True)
        return user

    def prefers_first(self, ideal: str, pairs, batch: int = 32) -> list[float]:
        """1.0 if the first shown is chosen, 0.0 if the second, nan if neither."""
        torch = self.torch
        self.tok.padding_side = "left"
        if self.tok.pad_token is None:
            self.tok.pad_token = self.tok.eos_token
        out: list[float] = []
        for i in range(0, len(pairs), batch):
            chunk = pairs[i:i + batch]
            enc = self.tok([self._prompt(ideal, f, s) for f, s in chunk],
                           return_tensors="pt", padding=True).to(self.model.device)
            with torch.no_grad():
                gen = self.model.generate(**enc, max_new_tokens=4, do_sample=False,
                                          pad_token_id=self.tok.pad_token_id)
            for row in gen[:, enc.input_ids.shape[1]:]:
                text = self.tok.decode(row, skip_special_tokens=True)
                m = re.search(r"\b([AB])\b", text.upper())
                if m:
                    out.append(1.0 if m.group(1) == "A" else 0.0)
                else:
                    out.append(float("nan"))
                    self.unparsed += 1
        return out


def both_orders(chooser, ideal_str: str, A, B, batch: int = 32) -> dict:
    """Show every pair both ways and keep only the comparisons that agree.

    A pair whose verdict changes when the options swap places has told us about
    the presentation and not about the geometry.
    """
    fwd = chooser.prefers_first(ideal_str, list(zip(A, B)), batch)
    rev = chooser.prefers_first(ideal_str, list(zip(B, A)), batch)
    a_nearer, keep = [], []
    first_chosen = 0
    counted = 0
    for f, r in zip(fwd, rev):
        if np.isfinite(f):
            first_chosen += f
            counted += 1
        if np.isfinite(r):
            first_chosen += r
            counted += 1
        if not (np.isfinite(f) and np.isfinite(r)):
            keep.append(False); a_nearer.append(np.nan); continue
        # forward says A when f == 1; reverse says A when r == 0
        agree = (f > 0.5) == (r < 0.5)
        keep.append(bool(agree))
        a_nearer.append(f if agree else np.nan)
    return {"a_nearer": a_nearer, "keep": keep,
            "agreement_rate": float(np.mean(keep)) if keep else float("nan"),
            "first_position_rate": (first_chosen / counted) if counted else float("nan"),
            "unparsed": int(chooser.unparsed)}


# ------------------------------------------------------------------ self-test


def run_cell_order(chooser, ideal_str: str, pairs, budget_key: str,
                   batch: int = 32, pref_full=None) -> dict:
    """Reversal rate of one class at one budget, for an order instrument.

    The reference is the evaluator's own full-budget order, not the fitted
    metric's prediction, so a calibration error cannot manufacture a reversal.
    Both presentation orders are shown at both budgets, and a pair whose verdict
    flips when the options swap is dropped at that budget rather than counted,
    because it has reported the presentation.
    """
    full = [(render_a, render_b) for render_a, render_b, _, _ in pairs]
    kbud = [(ka, kb) for _, _, ka, kb in pairs]
    shown = full if budget_key == "full" else kbud

    ref_f = chooser.prefers_first(ideal_str, full, batch)
    ref_r = chooser.prefers_first(ideal_str, [(b, a) for a, b in full], batch)
    cut_f = chooser.prefers_first(ideal_str, shown, batch)
    cut_r = chooser.prefers_first(ideal_str, [(b, a) for a, b in shown], batch)

    rev = amb_ref = amb_cut = 0
    graded = 0
    # Competence: does the evaluator's own full-budget order agree with the
    # order the fitted metric predicts? This is p, on the pairs actually graded,
    # and it is the quantity the reversal identity is stated in. Without it the
    # identity contrast = (2p-1)^2 can only be argued, because held-out accuracy
    # is measured on uniform calibration pairs with large margins and is an
    # upper bound for p here, not an estimate of it.
    comp_n = comp_hit = 0
    for i, (rf, rr, cf_, cr) in enumerate(zip(ref_f, ref_r, cut_f, cut_r)):
        if not (np.isfinite(rf) and np.isfinite(rr)) or (rf > 0.5) != (rr < 0.5):
            amb_ref += 1
            continue
        if pref_full is not None:
            comp_n += 1
            comp_hit += int(bool(rf > 0.5) == bool(pref_full[i]))
        if not (np.isfinite(cf_) and np.isfinite(cr)) or (cf_ > 0.5) != (cr < 0.5):
            amb_cut += 1
            continue
        graded += 1
        if (rf > 0.5) != (cf_ > 0.5):
            rev += 1
    p = (comp_hit / comp_n) if comp_n else float("nan")
    out = {"n": len(pairs), "graded": graded, "reversals": rev,
           "ambiguous_reference": amb_ref, "ambiguous_at_budget": amb_cut,
           "reversal_rate": (rev / graded) if graded else float("nan")}
    if pref_full is not None:
        out["competence_p"] = p
        out["competence_n"] = comp_n
        # what the identity predicts for THIS cell from THIS cell's own p
        out["identity_predicted_reversal_rate"] = (
            float(p * p + (1 - p) ** 2) if np.isfinite(p) else float("nan"))
        out["identity_predicted_W_rate"] = (
            float(2 * p * (1 - p)) if np.isfinite(p) else float("nan"))
    return out


def heldout_order_accuracy(A, B, y, folds: int = 5, l2: float = 1e-3,
                           seed: int = 0) -> dict:
    """Cross-validated accuracy of the quadratic model on unseen comparisons.

    With a real evaluator there is no true metric to compare against, so the
    calibration gate cannot be a recovery error. What it can be is whether a
    quadratic form predicts comparisons the fit never saw. An evaluator whose
    orders a quadratic cannot predict is not an evaluation object, which is the
    same verdict the reported-distance gate reached by a different route.
    """
    A, B, y = np.asarray(A, float), np.asarray(B, float), np.asarray(y, float)
    rng = np.random.default_rng(seed)
    idx = rng.permutation(len(y))
    cuts = np.array_split(idx, folds)
    accs = []
    for f in range(folds):
        test = cuts[f]
        train = np.concatenate([cuts[g] for g in range(folds) if g != f])
        Z_tr = -(phi(A[train]) - phi(B[train]))
        theta = _fit_logistic(Z_tr, y[train], l2=l2)
        Z_te = -(phi(A[test]) - phi(B[test]))
        accs.append(float(np.mean(((Z_te @ theta) > 0) == (y[test] > 0.5))))
    return {"folds": folds, "per_fold": accs,
            "mean": float(np.mean(accs)), "min": float(np.min(accs))}


def selftest(seed: int = 20260913, n_pairs: int = 600, verbose: bool = True) -> dict:
    """Recover a known metric from noiseless orders, then from noisy ones.

    The question the gate needs answered is not whether the estimator is exact,
    it is whether the retained subspace survives an evaluator that gets some
    comparisons wrong. So the sweep over error rates is the real test.
    """
    rng = np.random.default_rng(seed)
    d = 3
    M = rng.normal(size=(d, d))
    G_true = M @ M.T + 0.5 * np.eye(d)
    G_true *= d / np.trace(G_true)
    t_true = np.array([50.0, 50.0, 50.0])

    def draw(n):
        A = rng.uniform(0, 100, size=(n, d))
        B = rng.uniform(0, 100, size=(n, d))
        dA = np.einsum("ni,ij,nj->n", A - t_true, G_true, A - t_true)
        dB = np.einsum("ni,ij,nj->n", B - t_true, G_true, B - t_true)
        return A, B, (dA < dB).astype(float)

    def angle(G_hat, t_hat, X, k=2):
        from c1_calibrate import retained
        Bh = np.array(retained(G_hat, t_hat, X, k)["basis_whitened"])
        Bt = np.array(retained(G_true, t_true, X, k)["basis_whitened"])
        sv = np.linalg.svd(Bh.T @ Bt, compute_uv=False)
        return float(np.degrees(np.arccos(np.clip(sv.min(), -1.0, 1.0))))

    X_ref = rng.uniform(0, 100, size=(600, d))
    A, B, y = draw(n_pairs)
    clean = calibrate_from_order(A, B, y)
    g_err = float(np.linalg.norm(np.array(clean["G"]) - G_true) / np.linalg.norm(G_true))
    a_clean = angle(np.array(clean["G"]), np.array(clean["t"]), X_ref)

    sweep = []
    for err in (0.02, 0.05, 0.10, 0.20, 0.30):
        A2, B2, y2 = draw(n_pairs)
        flip = rng.random(len(y2)) < err
        y2 = np.where(flip, 1 - y2, y2)
        c = calibrate_from_order(A2, B2, y2)
        sweep.append({"error_rate": err,
                      "order_accuracy": c["order_accuracy"],
                      "metric_rel_error": float(np.linalg.norm(np.array(c["G"]) - G_true)
                                                / np.linalg.norm(G_true)),
                      "subspace_angle_deg": angle(np.array(c["G"]), np.array(c["t"]), X_ref)})

    res = {"n_pairs": n_pairs,
           "clean": {"metric_rel_error": g_err, "subspace_angle_deg": a_clean,
                     "order_accuracy": clean["order_accuracy"]},
           "noise_sweep": sweep,
           "pass": bool(a_clean < 5.0 and sweep[2]["subspace_angle_deg"] < 15.0)}
    if verbose:
        print("C1 order-based calibration self-test")
        print(f"  clean: metric rel err {g_err:.4f}  subspace angle {a_clean:.3f} deg  "
              f"order acc {clean['order_accuracy']:.4f}")
        print(f"  {'flip rate':>10} {'order acc':>10} {'metric err':>11} {'angle deg':>10}")
        for s in sweep:
            print(f"  {s['error_rate']:10.2f} {s['order_accuracy']:10.4f} "
                  f"{s['metric_rel_error']:11.4f} {s['subspace_angle_deg']:10.3f}")
        print(f"  verdict {'PASS' if res['pass'] else 'FAIL'}")
    return res


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--n-pairs", type=int, default=600)
    ap.add_argument("--out")
    args = ap.parse_args()
    if not args.selftest:
        ap.error("give --selftest; the graded stages run from c1_atlas_run.py")
    r = selftest(n_pairs=args.n_pairs)
    if args.out:
        json.dump(r, open(args.out, "w", encoding="utf-8"), indent=1)
    return 0 if r["pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
