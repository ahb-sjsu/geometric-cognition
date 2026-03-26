# Geometric Cognition: The Mathematical Structure of Human and Artificial Thought

**Andrew H. Bond**

---

*For everyone who has ever measured intelligence with a single number and suspected it was not enough.*

---

## Preface

This book began as a footnote that refused to stay small.

I was finishing the final chapters of *Geometric Ethics: The Mathematical Structure of Moral Reasoning* (Bond, 2026b), deep in the argument that moral deliberation is A* search on the judgment manifold, when I tried to explain---in a parenthetical, no more---why the moral case was special. Why reasoning about ethics required the geometric machinery of manifolds and heuristic fields and geodesics, while reasoning about, say, medical diagnosis or strategic planning did not.

I could not write the parenthetical. Every time I attempted to identify a geometric property unique to moral reasoning, I found the same property in non-moral domains. The heuristic field that guides a physician through differential diagnosis has the same structure as the heuristic field that guides a moral reasoner through a trolley problem. The corruption tensor that quantifies framing effects in ethical judgment has the same form as the corruption tensor that quantifies anchoring bias in numerical estimation. The recovery ceiling---the ~38% maximum improvement achievable through prompt-level metacognitive intervention---appeared identically in our Attention and Executive Functions benchmarks, neither of which had anything to do with morality.

The parenthetical became a section. The section became a chapter. The chapter became this book.

What changed my mind from suspicion to conviction was the data. The Measuring AGI benchmarks---five tracks probing Social Cognition, Learning, Metacognition, Attention, and Executive Functions across five frontier language models---returned results with geometric structure so clean it looked engineered. Framing effects at 15.3 sigma. Sycophancy gradients spanning zero to fifty-six percent. A metacognitive dissociation so stark that effort scaling and self-monitoring appeared to belong to different species of cognition. And at the center of it all, the Scalar Irrecoverability Theorem: the proof that no single composite score---no IQ, no accuracy, no g-factor---can recover the profile structure that determines how a system actually reasons.

This book is the attempt to take that theorem seriously. If scalar measures of intelligence are geometrically irrecoverable, what replaces them? The answer, I argue, is the cognitive manifold: a structured space of cognitive states, equipped with a metric defined by attention, a tangent space defined by working memory, a heuristic field defined by learned expectations, and a control layer defined by executive functions. Cognition---human and artificial---is search on this manifold. The quality of cognition is the quality of the search. And the quality of the search is determined by the geometry.

I should be transparent about the epistemic status of these claims. The empirical results are strong: five sigma values ranging from 4.6 to 15.3, convergent recovery ceilings, clean dissociations. The geometric framework is productive: it generates novel predictions, explains known phenomena, and suggests specific interventions. But the claim that cognition *is* geometric search---that the manifold is not merely a useful metaphor but the correct mathematical description---is a theoretical commitment that outruns the current evidence. This book is a progress report, not a final verdict. I have tried to mark, throughout, where the evidence is strong, where it is suggestive, and where I am speculating.

---

## Core Objects at a Glance

The framework rests on five mathematical objects. Each appears first as an intuition, then as a definition, then as an empirical measurement.

| Object | Intuition | Mathematical Structure | Measured By |
|---|---|---|---|
| **Cognitive Manifold** | The space of all cognitive states a system can occupy | Riemannian manifold $(\mathcal{M}, g)$ embedded in high-dimensional activation space | fMRI activation patterns; transformer residual stream |
| **Attention Metric** | What you attend to defines which states are "close" | Metric tensor $g_{\mu\nu}$ on $\mathcal{M}$, with selective attention contracting and divided attention expanding the metric | A3 SNR (1.22--1.38); A4 divided attention split |
| **Working Memory as Tangent Space** | The local neighborhood of states reachable in one step | Tangent space $T_x\mathcal{M}$ at current state $x$; capacity = dimension of tangent space | E4 working memory scaling (0.710--0.909) |
| **Heuristic Field** | The internal guidance signal that directs cognitive search | Scalar field $h: \mathcal{M} \to \mathbb{R}$ with gradient $\nabla h$ pointing toward estimated goal | Corruption measured by sigma values (4.6--15.3) |
| **Five Cognitive Dimensions** | The independent axes of cognitive capability | Social, Learning, Metacognition, Attention, Executive as independent submanifolds | 21 subtasks across 5 benchmark tracks |

---

## Key Results

The following empirical results, drawn from the Measuring AGI benchmarks, anchor the theoretical development:

1. **Scalar Irrecoverability** (Chapter 1). No single composite score correctly ranks five frontier models across all five cognitive tracks. The proof is constructive: Claude and Pro have nearly identical composite scores but completely different cognitive architectures---Claude's "narrow channel" (zero sycophancy, worst divided attention) versus Pro's "calibrated navigator" (best calibration, zero effort scaling). The composite destroys the information that matters.

2. **Five Sigma Values** (Chapters 7--11). The five headline effects, each measuring a different geometric pathology:
   - 15.3 sigma: framing displacement (heuristic corruption by surface features)
   - 13.3 sigma: sycophancy gradient (objective function hijacking)
   - 6.7 sigma: systematic miscalibration (distance estimation error)
   - 6.8 sigma: emotional anchoring (control layer corruption)
   - 4.6 sigma: distractor displacement (metric perturbation)

3. **The ~38% Recovery Ceiling** (Chapters 2, 6, 10). Prompt-level metacognitive intervention recovers at most 38--39% of performance lost to heuristic corruption. This ceiling converges across the A1 (attention) and E2 (executive) tracks, which test entirely different cognitive capabilities. It is a structural limit of the control architecture, not a domain-specific phenomenon.

4. **The Empty Quadrant** (Chapter 9). In the metacognitive plane defined by self-monitoring (M3) and effort scaling (M4), no model occupies Quadrant I---the quadrant where both components work well. Every model has either a working thermometer or a working valve, never both.

5. **The Biggest Single-Test Discriminator** (Chapter 4). The A4 divided attention test produces the largest single-test difference between models: Claude scores 0.571, Flash 3 scores 1.000. Same task, same scoring, nearly opposite outcomes. This is the attention metric made visible.

---

## How to Read This Book

This book supports four reading paths, each designed for a different audience.

**Path 1: The Cognitive Scientist** (Chapters 1--4, 12--14). Start with the problem (scalar measures fail), learn the framework (manifold, metric, tangent space, heuristic field), then see how the framework applies to human cognition (dual process theory, cognitive development, cognitive pathology). Skip the five benchmark chapters (7--11) on first reading and return to them for empirical grounding.

**Path 2: The AI Researcher** (Chapters 1, 3--4, 7--11, 15--16). Start with the scalar irrecoverability theorem, learn enough framework to read the benchmarks, then work through all five cognitive dimension chapters for the empirical results. Finish with the LLM cognition chapters to see how the framework applies to transformer architectures.

**Path 3: The Mathematician** (Chapters 3--6, Technical Appendices). The framework chapters contain the mathematical development: Riemannian manifolds, metric tensors, tangent spaces, scalar fields, geodesic equations. The technical appendices provide formal proofs and connections to information geometry, gauge theory, and Finsler geometry.

**Path 4: The Generalist** (Chapters 1--2, then any chapter of interest). The first two chapters---The IQ Trap and Kahneman's Geometric Intuition---are self-contained introductions to the central ideas. Each subsequent chapter is written to be accessible after reading Chapters 1--2, with forward references to the framework chapters for readers who want the full mathematical treatment.

---

## Epistemic Status Classification

Each major claim in this book is tagged with one of four epistemic status labels:

- **[Established]**: Standard results from mathematics, computer science, or cognitive science. The claim would be accepted by a majority of researchers in the relevant field.
- **[Empirical]**: Claims supported by the Measuring AGI benchmark data at $p < 0.001$ or better. The data are strong, but the experimental program is young (five models, one experimental cycle).
- **[Theoretical]**: Claims that follow from the geometric framework given its assumptions. Sound if the framework is correct; the framework itself is the object of evaluation.
- **[Speculative]**: Claims that extend beyond both current data and current theory. Included because they are interesting, clearly marked because they are unproven.

---

## Table of Contents

### Part I: The Problem
1. **The IQ Trap** --- Why scalar intelligence measures are geometrically irrecoverable
2. **Kahneman's Geometric Intuition** --- System 1 and System 2 as regimes of the same geometric process

### Part II: The Framework
3. **The Cognitive Manifold** --- The space of cognitive states
4. **Attention as Metric** --- What you attend to defines "close"
5. **Working Memory as Tangent Space** --- The local neighborhood of accessible states
6. **Executive Functions as Search Control** --- The metacognitive control layer

### Part III: The Five Cognitive Dimensions
7. **Social Cognition as Navigation in Judgment Space** --- Moral judgment, framing, asymmetric vulnerability
8. **Learning as Belief Trajectory Revision** --- Belief updating, sycophancy, few-shot learning
9. **Metacognition as Distance Estimation** --- Calibration, self-monitoring, the empty Quadrant I
10. **Attention as Manifold Filtering** --- Distractors, sustained attention, divided attention
11. **Executive Control as Geodesic Governance** --- Framework switching, inhibitory control, working memory

### Part IV: Human Cognition
12. **The Dual Process Theory, Geometrized** --- System 1 as gradient following, System 2 as geodesic computation
13. **Cognitive Development as Manifold Growth** --- Piaget's stages as topological transitions
14. **Cognitive Pathology as Geometric Defect** --- ADHD, depression, anxiety, autism

### Part V: Artificial Cognition
15. **LLM Cognition Through the Geometric Lens** --- Attention heads, chain-of-thought, residual streams
16. **The Five Geometric Signatures** --- Model cognitive fingerprints

### Part VI: Horizons
17. **Open Questions** --- Finsler geometry, neural measurement, consciousness, dimensionality

### Appendices
A. Mathematical Prerequisites (Riemannian Geometry, Tensor Calculus)
B. Benchmark Methodology and Raw Data
C. Proofs of Main Theorems
D. Connections to Information Geometry and Gauge Theory

---

## Notation

| Symbol | Meaning | First Introduced |
|---|---|---|
| $\mathcal{M}$ | Cognitive manifold | Ch. 3 |
| $g_{\mu\nu}$ | Attention metric tensor | Ch. 4 |
| $T_x\mathcal{M}$ | Tangent space (working memory) at state $x$ | Ch. 5 |
| $h: \mathcal{M} \to \mathbb{R}$ | Heuristic field (guidance signal) | Ch. 3 |
| $\nabla h$ | Gradient of the heuristic field | Ch. 3 |
| $\Gamma^\mu_{\alpha\beta}$ | Christoffel symbols (connection coefficients) | Ch. 3 |
| $R^\mu{}_{\nu\alpha\beta}$ | Riemann curvature tensor | Ch. 3 |
| $\gamma(t)$ | Cognitive trajectory (path on the manifold) | Ch. 3 |
| $\gamma^*(t)$ | Geodesic (optimal cognitive trajectory) | Ch. 3 |
| $\delta\gamma$ | Geodesic deviation (reasoning error) | Ch. 3 |
| $f(x) = g(x) + h(x)$ | A* evaluation function | Ch. 1 |
| $C_{\mu\nu}$ | Corruption tensor | Ch. 7 |
| $\text{ECE}$ | Expected Calibration Error | Ch. 9 |
| $\text{SNR}$ | Signal-to-noise ratio (attention metric quality) | Ch. 4 |
| $\sigma$ | Standard deviations (statistical significance) | Throughout |
| $\dim(T_x\mathcal{M})$ | Working memory capacity | Ch. 5 |
| $\kappa(x)$ | Sectional curvature at state $x$ | Ch. 3 |
| $\mathcal{G}$ | Symmetry group of the cognitive manifold | Ch. 7 |
| $\Phi: \mathcal{M} \to \mathcal{M}$ | Cognitive symmetry transformation | Ch. 7 |
| $\mathcal{R}$ | Recovery rate (fraction of lost performance recovered) | Ch. 2 |
| $\mathcal{R}_{\max} \approx 0.38$ | Recovery ceiling | Ch. 2 |
