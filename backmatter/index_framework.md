# Index Framework

*Chapter-level index for Geometric Cognition. Page-level entries to be generated at typesetting.*

---

## Concepts

**A* search**, 1, 2, 3, A --- evaluation function $f(x) = g(x) + h(x)$; System 2 deliberation + System 1 heuristic; cognition as pathfinding on the cognitive manifold
**admissible heuristic**, 2, 3, A --- $h(x) \leq d(x, G)$; admissible cognitive heuristic never overestimates cost-to-go; violated in overconfidence
**ADHD as metric instability**, 14 --- the attention metric fluctuates; no state is reliably "close"
**anxiety as inflated heuristic**, 14 --- $h(x)$ overestimates cost-to-go from every state; everything feels far from safety
**asymmetric vulnerability**, 7, 16 --- Claude's greater sensitivity to minimization than exaggeration framing; anisotropic corruption tensor
**attention metric** ($g_{\mu\nu}$), 4, 10, A --- defines which cognitive states are close and which are far; selective attention narrows, divided attention widens
**autism as metric rigidity**, 14 --- the metric is fixed and precise but does not adapt to context

**calibration** (ECE), 9, B --- Expected Calibration Error; accuracy of internal distance estimates; range 0.186--0.437 across models
**calibration gradient**, 9 --- ECE improves with model scale and generation: Flash 2.0 (0.437) to Pro (0.186)
**Christoffel symbols** ($\Gamma^\mu_{\alpha\beta}$), 3, 12, A --- connection coefficients encoding how the metric varies; required for geodesic computation (System 2)
**cognitive manifold** ($\mathcal{M}$), 3, 4, 5, 12, 13, 14, 15, 17 --- the space of all cognitive states a system can occupy; central construction of the book
**cognitive pathology**, 14 --- geometric defects: metric instability (ADHD), collapsed heuristic (depression), inflated heuristic (anxiety), metric rigidity (autism)
**cognitive profile tensor** ($\mathbf{C}(S)$), 1, 16, C --- vector in $[0,1]^{21}$ capturing all subtask scores; the object that scalar contraction destroys
**composite score**, 1 --- *see* scalar contraction
**corruption tensor** ($C_{\mu\nu}$), 7, 10, 11, A --- quantifies deviation of the heuristic field under perturbation; its eigenstructure reveals vulnerable dimensions
**counterfactual reasoning**, 6, 11 --- E3 subtask; geodesic sensitivity; computing alternative trajectories on the manifold; scores 50--75%
**curvature, sectional** ($K$), 3, 12, A --- determines cognitive complexity; triggers System 1 to System 2 transition; high curvature = conflicting considerations
**curvature threshold**, 12, 13 --- the curvature value at which gradient following (System 1) gives way to geodesic computation (System 2); a phase transition

**D4 augmentation**, A, 15 --- the 8-element dihedral symmetry group of the square; used in ARC-AGI and AIRV pipeline for grid transformation
**depression as collapsed heuristic**, 14 --- the guidance field is flat; no direction seems promising; $\nabla h \approx 0$
**development, cognitive**, 13 --- Piaget's stages as topological transitions; sensorimotor (low-dimensional), pre-operational (dimension addition), concrete operational (metric stabilization), formal operational (manifold completion)
**distractor displacement**, 10, B --- A1 subtask; 4.6 sigma (updated: 5.0 sigma); dose-response curve of metric perturbation under irrelevant distractors
**divided attention**, 4, 10, 16, B --- A4 subtask; Claude at 0.571, Flash 3 at 1.000; the largest single-test discriminator; measures parallel metric capacity
**dual-process theory**, 2, 12 --- System 1 (gradient following) and System 2 (geodesic computation) as two regimes of one geometric process

**effort scaling**, 9, C --- M4 subtask; measures whether metacognitive knowledge drives resource allocation; Flash 2.0 at 0.827, Pro at 0.000
**emotional anchoring**, 6, 11, B --- E2 subtask; 6.8 sigma; irrelevant emotional content corrupts the executive control layer
**empty Quadrant I**, 9, C --- no model has both good self-monitoring (M3) and good effort scaling (M4); a structural constraint, not a sampling artifact
**executive control tensor**, 6, 11 --- the control layer decomposed into flexibility (metric rotation), inhibition (gradient suppression), and capacity (tangent space scaling)
**executive functions**, 6, 11, B --- the metacognitive control layer; flexibility, inhibitory control, counterfactual reasoning, working memory

**few-shot learning**, 8, B --- L1 subtask; 80--86% accuracy at 0-shot; near-optimal base heuristic requiring no trajectory correction
**Fisher information**, 4, A --- the Fisher information matrix as the natural metric on parameter space; connection to the attention metric
**Finsler metric**, 17, A --- asymmetric distance; cognitive effort may be Finsler rather than Riemannian; an open question
**framing displacement**, 7, B --- T5 subtask; 15.3 sigma; identical moral scenarios produce different judgments under different framing; heuristic corruption
**framework switching**, 6, 11 --- E1 subtask; smooth transitions between incompatible cognitive frameworks; scores 32--47%

**g-factor**, 1 --- Spearman's general intelligence factor; the first principal component of the cognitive covariance matrix; a specific linear contraction
**geodesic** ($\gamma^*$), 3, 12, A --- the optimal cognitive trajectory; shortest path on the manifold accounting for curvature
**geodesic computation** (System 2), 2, 12 --- slow, effortful, curvature-aware reasoning; solves the geodesic equation; $O(d^2 \cdot L)$ computational cost
**gradient following** (System 1), 2, 12 --- fast, heuristic-dominated reasoning; $x_{t+1} = x_t - \eta \nabla h(x_t)$; $O(d)$ computational cost; works in low-curvature regions

**harm space, 7-dimensional**, 7 --- the submanifold of the cognitive manifold on which moral judgment occurs; physical, psychological, financial, social, autonomy, dignity, institutional dimensions
**heuristic field** ($h: \mathcal{M} \to \mathbb{R}$), 2, 3, 7, 8, 9, 14, 15 --- internal guidance signal; its gradient directs cognitive search; its corruption produces cognitive bias

**in-context learning**, 15 --- local metric adaptation; the transformer adjusts its effective metric in response to context; Chapter 15 interprets this geometrically
**IQ**, 1, A --- scalar contraction of the cognitive tensor; monotonic rescaling of the g-factor; geometrically irrecoverable
**Irrecoverability Theorem**, *see* Scalar Irrecoverability Theorem

**Kahneman, Daniel**, 2, 12 --- dual-process theory; System 1 / System 2; prospect theory; the geometric reinterpretation is Chapter 12

**manifold hypothesis**, 3 --- cognition lives on a low-dimensional submanifold of the high-dimensional activation space
**Measuring AGI benchmarks**, 1, 7--11, 16, B, C --- five tracks, twenty-one subtasks, five models; the empirical foundation of the book
**metacognition**, 9, B --- cognition about cognition; distance estimation on the cognitive manifold; calibration, ambiguity discrimination, self-monitoring, effort scaling
**metric instability**, 14 --- *see* ADHD as metric instability
**metric rigidity**, 14 --- *see* autism as metric rigidity

**narrow channel**, 1, 16, C --- Claude's cognitive signature; zero sycophancy, worst divided attention; deep but narrow processing

**overconfidence, universal**, 9, B --- every tested model overestimates its accuracy; ECE always indicates overconfidence; the heuristic field is systematically biased

**Piaget, Jean**, 13 --- developmental stage theory; sensorimotor, pre-operational, concrete operational, formal operational; geometrized as manifold growth

**recovery ceiling** ($\mathcal{R}_{\max} \approx 0.38$), 2, 6, 10 --- prompt-level metacognitive intervention recovers at most ~38% of lost performance; converges across Attention and Executive tracks; a structural limit
**residual stream**, 15 --- the transformer's running representation; interpreted as the trajectory on the cognitive manifold

**Scalar Irrecoverability Theorem**, 1, A --- no continuous $\phi: \mathbb{R}^n \to \mathbb{R}$ ($n > 1$) is injective; composite scores destroy $(n-1)$ dimensions irrecoverably
**self-monitoring**, 9, C --- M3 subtask; item-level metacognitive access; Claude at 0.723, Pro at 0.500, Flash 2.0 at 0.042
**sycophancy gradient**, 8, B --- L2 subtask; 13.3 sigma; 0% (Claude) to 56% (Flash 2.5) capitulation under social pressure; objective function hijacking
**System 1**, *see* gradient following
**System 2**, *see* geodesic computation

**tangent space** ($T_x\mathcal{M}$), 5, A --- working memory; local neighborhood of reachable cognitive states; its dimension is working memory capacity
**topological transition**, 13 --- qualitative change in the manifold's topology during cognitive development; Piaget's stages

**wide aperture**, 16, C --- Flash 3's cognitive signature; perfect divided attention, weak sycophancy resistance; broad but shallow processing
**working memory**, 5, 11, B --- E4 subtask; tangent space capacity under load; Flash 2.0 at 0.710 to Flash 3 at 0.909

---

## People

**Baddeley, Alan**, 5 --- working memory model; phonological loop, visuospatial sketchpad, central executive
**Binet, Alfred**, 1 --- first practical intelligence test (1905); operationalized the g-factor as IQ
**Broadbent, Donald**, 4 --- early selective attention research; filter theory of attention
**Diamond, Adele**, 6, 11 --- executive functions research; tripartite decomposition (flexibility, inhibition, working memory)
**Kahneman, Daniel**, 2, 7, 12 --- dual-process theory; System 1 / System 2; prospect theory; Thinking, Fast and Slow
**Piaget, Jean**, 13 --- developmental stage theory; genetic epistemology; conservation experiments
**Spearman, Charles**, 1 --- general intelligence factor (g); factor analysis (1904); the original scalar contraction
**Thiele, Dietrich**, Preface --- UCLA; conversations about the cognitive manifold's mathematical foundations
**Tversky, Amos**, 2, 7, 12 --- heuristics and biases; framing effects; prospect theory

---

## Models

**Claude 3.5 Sonnet**, 1, 7, 8, 9, 10, 11, 16, C --- Anthropic; "narrow channel" signature; zero sycophancy, worst divided attention, excellent self-monitoring
**Gemini 2.0 Flash**, 9, 11, 16, C --- Google DeepMind; "adaptive baseline" signature; best recovery, strong effort scaling, worst working memory, near-chance self-monitoring
**Gemini 2.5 Flash**, 8, 16, C --- Google DeepMind; "elastic malleability" signature; worst sycophancy resistance, strong distractor resistance
**Gemini 2.5 Pro**, 1, 9, 11, 16, C --- Google DeepMind; "calibrated navigator" signature; best calibration, best self-monitoring, zero effort scaling
**Gemini 3 Flash**, 5, 10, 16, C --- Google DeepMind; "wide aperture" signature; perfect divided attention, best working memory, weak sycophancy resistance

---

## Mathematical Objects

**$\mathbf{C}(S)$** (cognitive profile tensor), 1 --- point in $[0,1]^{21}$; the full cognitive fingerprint
**$C_{\mu\nu}$** (corruption tensor), 7, A --- $\partial^2(\delta h)/\partial \xi^\mu \partial \xi^\nu$; quantifies heuristic corruption
**$\mathcal{M}$** (cognitive manifold), 3 --- the space of cognitive states; central geometric object
**$g_{\mu\nu}$** (attention metric), 4 --- Riemannian metric encoding attentional structure
**$T_x\mathcal{M}$** (tangent space), 5 --- working memory at state $x$
**$h: \mathcal{M} \to \mathbb{R}$** (heuristic field), 3 --- internal guidance signal; gradient = search direction
**$f(x) = g(x) + h(x)$** (A* evaluation), 1, 2 --- accumulated cost + heuristic estimate
**$\gamma^*$** (geodesic), 3, 12 --- optimal cognitive trajectory
**$K(u,v)$** (sectional curvature), 3, 12 --- cognitive complexity; triggers dual-process transition
**$\sigma$** (sigma values), Throughout --- statistical significance of geometric effects

---

## Key Empirical Results

**4.6 sigma** (updated: **5.0 sigma**), 10, B --- distractor displacement; Attention A1
**6.7 sigma**, 9, B --- systematic miscalibration; Metacognition M1 (Fisher combined)
**6.8 sigma**, 11, B --- emotional anchoring; Executive Functions E2
**13.3 sigma**, 8, B --- sycophancy gradient; Learning L2
**15.3 sigma**, 7, B --- framing displacement; Social Cognition T5
**~38% recovery ceiling**, 2, 6, 10 --- structural limit of metacognitive intervention
**Empty Quadrant I**, 9 --- no model has both good M3 and good M4

---

*Note: This index framework provides chapter-level references. Final page numbers, sub-entries, and cross-reference refinements will be generated during typesetting from the compiled manuscript. Entries marked with "see" indicate cross-references to be verified against the final chapter text.*
