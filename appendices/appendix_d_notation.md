# Appendix D: Notation and Conventions

This appendix collects the notation used throughout the book. Notation is consistent with the Geometric Series; where domain-specific symbols are introduced, they are listed separately.

---

## D.1 Manifolds and Geometry

| Symbol | Meaning | First Introduced |
|---|---|---|
| $\mathcal{M}$ | Cognitive manifold --- the space of all cognitive states | Ch. 3 |
| $g_{\mu\nu}$ | Attention metric tensor on $\mathcal{M}$ | Ch. 4 |
| $T_x\mathcal{M}$ | Tangent space (working memory) at cognitive state $x$ | Ch. 5 |
| $\dim(T_x\mathcal{M})$ | Working memory capacity at state $x$ | Ch. 5 |
| $\gamma(t)$ | Cognitive trajectory --- a path on the manifold | Ch. 3 |
| $\gamma^*(t)$ | Geodesic --- the optimal cognitive trajectory | Ch. 3 |
| $\delta\gamma$ | Geodesic deviation --- the reasoning error | Ch. 3 |
| $\Gamma^\mu_{\alpha\beta}$ | Christoffel symbols (connection coefficients on $\mathcal{M}$) | Ch. 3 |
| $R^\mu{}_{\nu\alpha\beta}$ | Riemann curvature tensor on $\mathcal{M}$ | Ch. 3 |
| $K(u,v)$ | Sectional curvature in the plane spanned by $u, v$ | Ch. 3 |
| $\kappa(x)$ | Sectional curvature at state $x$ (scalar shorthand) | Ch. 3 |
| $d(p,q)$ | Geodesic distance between states $p$ and $q$ | Ch. 3 |
| $F: TM \to \mathbb{R}_{\geq 0}$ | Finsler metric (for asymmetric cognitive distance) | Ch. 17 |

---

## D.2 Search and Heuristics

| Symbol | Meaning | First Introduced |
|---|---|---|
| $h: \mathcal{M} \to \mathbb{R}$ | Heuristic field --- the internal guidance signal | Ch. 3 |
| $\nabla h$ | Gradient of the heuristic field | Ch. 3 |
| $f(x) = g(x) + h(x)$ | A* evaluation function | Ch. 1 |
| $g(x)$ | Accumulated path cost (System 2 deliberation) | Ch. 1 |
| $h(x)$ | Heuristic estimate of cost-to-go (System 1 intuition) | Ch. 1 |
| $\eta$ | Step size for gradient following | Ch. 12 |
| $\mathcal{R}$ | Recovery rate (fraction of lost performance recovered) | Ch. 2 |
| $\mathcal{R}_{\max} \approx 0.38$ | Recovery ceiling (structural limit of control architecture) | Ch. 2 |

---

## D.3 Corruption and Perturbation

| Symbol | Meaning | First Introduced |
|---|---|---|
| $C_{\mu\nu}$ | Corruption tensor | Ch. 7 |
| $C^\mu{}_\mu$ | Trace of corruption tensor (total corruption magnitude) | Ch. 7 |
| $\xi^\mu$ | Perturbation vector (framing change, distractor, etc.) | Ch. 7 |
| $\delta h$ | Change in heuristic field under perturbation | Ch. 7 |
| $\sigma$ | Standard deviations (sigma value for statistical significance) | Throughout |

---

## D.4 Cognitive Profile and Benchmark Measures

| Symbol | Meaning | First Introduced |
|---|---|---|
| $\mathbf{C}(S)$ | Cognitive profile tensor for system $S$ | Ch. 1 |
| $c_i$ | Score on subtask $i$ | Ch. 1 |
| $\phi: [0,1]^n \to \mathbb{R}$ | Scalar contraction (composite score function) | Ch. 1 |
| $\text{ECE}$ | Expected Calibration Error (metacognitive quality) | Ch. 9 |
| $\text{SNR}$ | Signal-to-noise ratio (attention metric quality) | Ch. 4 |

---

## D.5 Benchmark Subtask Codes

| Code | Subtask | Track | Chapter |
|---|---|---|---|
| T1--T5 | Social Cognition subtasks | Social Cognition | Ch. 7 |
| L1--L4 | Learning subtasks | Learning | Ch. 8 |
| M1--M4 | Metacognition subtasks | Metacognition | Ch. 9 |
| A1--A4 | Attention subtasks | Attention | Ch. 10 |
| E1--E4 | Executive Functions subtasks | Executive Functions | Ch. 11 |

---

## D.6 Symmetry and Gauge Theory

| Symbol | Meaning | First Introduced |
|---|---|---|
| $\mathcal{G}$ | Symmetry group of the cognitive manifold | Ch. 7 |
| $\Phi: \mathcal{M} \to \mathcal{M}$ | Cognitive symmetry transformation | Ch. 7 |
| $D_4$ | Dihedral group of the square (8 elements) | App. A |
| $V_{ij}$ | Gauge violation tensor | Ch. 7 |

---

## D.7 Model Abbreviations

| Abbreviation | Full Name | Signature |
|---|---|---|
| Claude | Claude 3.5 Sonnet (Anthropic) | Narrow Channel |
| Flash 2.0 | Gemini 2.0 Flash (Google DeepMind) | Adaptive Baseline |
| Flash 2.5 | Gemini 2.5 Flash (Google DeepMind) | Elastic Malleability |
| Flash 3 | Gemini 3 Flash (Google DeepMind) | Wide Aperture |
| Pro | Gemini 2.5 Pro (Google DeepMind) | Calibrated Navigator |

---

## D.8 Conventions

- **Index conventions.** Greek indices ($\mu, \nu, \alpha, \beta$) run over manifold dimensions. Latin indices ($i, j, k$) run over subtasks or model indices. Einstein summation convention is used unless otherwise noted.
- **Units.** All benchmark scores are normalized to $[0, 1]$. ECE is on $[0, 1]$ with 0 = perfect calibration. Sigma values are standard deviations from the null distribution.
- **Sign conventions.** The heuristic field $h(x)$ is non-negative, with $h(x) = 0$ at the goal. Overconfidence corresponds to $h(x) < d(x, G)$ (underestimated distance). The corruption tensor $C_{\mu\nu}$ is positive semi-definite.
- **Series consistency.** Notation follows the conventions established in *Geometric Methods* (Book 1), *Geometric Reasoning* (Book 2), and *Geometric Ethics* (Book 3). Where cognitive-specific notation diverges from the series standard, the divergence is noted at first use.
