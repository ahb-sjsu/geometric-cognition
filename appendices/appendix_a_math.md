# Appendix A: Mathematical Prerequisites

This appendix collects the mathematical definitions and results used throughout the book. It is self-contained for readers unfamiliar with differential geometry, cognitive modeling, or the specific constructions of the geometric framework; those with background in these areas may skip directly to the chapters. Full proofs and extended treatments can be found in *Geometric Methods in Computational Modeling* (Bond, 2026a) and *Geometric Reasoning* (Bond, 2026c).

---

## A.1 Smooth Manifolds and Riemannian Geometry

**Definition A.1 (Topological Manifold).** A *topological manifold* of dimension $n$ is a Hausdorff, second-countable topological space $M$ such that every point $p \in M$ has a neighborhood homeomorphic to an open subset of $\mathbb{R}^n$.

**Definition A.2 (Smooth Manifold).** A *smooth manifold* is a topological manifold equipped with a maximal smooth atlas --- a collection of charts $\{(U_\alpha, \varphi_\alpha)\}$ covering $M$ such that all transition maps $\varphi_\beta \circ \varphi_\alpha^{-1}$ are $C^\infty$.

*Cognitive interpretation*: The cognitive manifold $\mathcal{M}$ is the space of all cognitive states a system can occupy. Each "chart" corresponds to a particular representation scheme --- a particular way of encoding cognitive state, such as an fMRI activation pattern, a transformer residual stream snapshot, or a psychometric test battery result. Transition maps are the conversions between these representations. The smoothness requirement says that small changes in one representation produce small changes in any other. (See Chapter 3.)

**Definition A.3 (Tangent Space).** The *tangent space* $T_pM$ at a point $p \in M$ is the vector space of derivations at $p$ --- equivalence classes of curves through $p$, or equivalently, the space of directional derivatives. If $M$ has dimension $n$, then $T_pM \cong \mathbb{R}^n$.

*Cognitive interpretation*: The tangent space at a cognitive state $x$ represents working memory --- the set of cognitive states reachable in one reasoning step from $x$. Working memory capacity is the effective dimension of this tangent space. The E4 benchmark (working memory scaling: 0.710 to 0.909 across models) measures how well this tangent space grows with task demands. (See Chapter 5.)

**Definition A.4 (Riemannian Metric).** A *Riemannian metric* on a smooth manifold $M$ is a smooth assignment of a positive-definite inner product $g_p: T_pM \times T_pM \to \mathbb{R}$ to each tangent space $T_pM$. In local coordinates, $g = g_{\mu\nu} \, dx^\mu \otimes dx^\nu$.

*Cognitive interpretation*: The attention metric $g_{\mu\nu}$ defines which cognitive states are "close" (easily reached) and which are "far" (requiring effort). Selective attention narrows the metric, reducing effective dimensionality. Divided attention widens it, increasing the number of simultaneously accessible states. (See Chapter 4.)

**Definition A.5 (Geodesic).** A curve $\gamma: [0,1] \to M$ is a *geodesic* if it satisfies the geodesic equation:

$$\frac{d^2 \gamma^\mu}{dt^2} + \Gamma^\mu_{\alpha\beta} \frac{d\gamma^\alpha}{dt} \frac{d\gamma^\beta}{dt} = 0$$

where $\Gamma^\mu_{\alpha\beta}$ are the Christoffel symbols of the Levi-Civita connection.

**Definition A.6 (Geodesic Distance).** The geodesic distance between $p, q \in M$ is

$$d(p, q) = \inf_\gamma \int_0^1 \sqrt{g_{\gamma(t)}(\dot{\gamma}(t), \dot{\gamma}(t))} \, dt$$

where the infimum is over all smooth curves from $p$ to $q$.

*Cognitive interpretation*: Geodesics are the optimal cognitive trajectories --- the paths of least total cost through the cognitive manifold. System 2 reasoning computes (approximate) geodesics; System 1 reasoning follows the gradient of the heuristic field, which approximates geodesics only in regions of low curvature. (See Chapter 12.)

**Definition A.7 (Sectional Curvature).** The sectional curvature at a point $p$ in the plane spanned by tangent vectors $u, v \in T_pM$ is

$$K(u,v) = \frac{R(u,v,v,u)}{g(u,u)g(v,v) - g(u,v)^2}$$

where $R$ is the Riemann curvature tensor. Curvature measures how rapidly nearby geodesics diverge or converge.

*Cognitive interpretation*: High curvature corresponds to cognitive complexity --- regions where conflicting considerations (moral dimensions, task demands, contextual factors) make the landscape non-trivial. The curvature threshold triggers the System 1 to System 2 transition (Chapter 12). Low curvature permits fast, heuristic-driven reasoning; high curvature demands slow, deliberate geodesic computation.

---

## A.2 The Attention Metric and Fisher Information

The attention metric $g_{\mu\nu}$ has a natural connection to Fisher information geometry.

**Definition A.8 (Fisher Information Matrix).** Given a parametric family of probability distributions $p(x|\theta)$, the Fisher information matrix is:

$$I_{ij}(\theta) = \mathbb{E}\left[\frac{\partial \log p(x|\theta)}{\partial \theta_i} \frac{\partial \log p(x|\theta)}{\partial \theta_j}\right]$$

The Fisher information matrix is a Riemannian metric on the parameter space. When the parameters represent cognitive states and the distributions represent the system's output distribution conditioned on those states, the Fisher information metric measures how distinguishable nearby cognitive states are --- which is precisely what the attention metric captures.

*Cognitive interpretation*: A cognitive system that attends strongly to a stimulus dimension has high Fisher information along that dimension: small changes in the stimulus produce large, detectable changes in the system's internal representation. A system that ignores a dimension has low Fisher information: the stimulus can change without affecting the representation. The SNR data from the Measuring AGI benchmarks (1.22--1.38, universally weak) measures the quality of this Fisher information. (See Chapter 4, Technical Appendix 4A.)

---

## A.3 Heuristic Fields and A* Search

**Definition A.9 (Heuristic Field).** A *heuristic field* on a manifold $M$ is a smooth scalar function $h: M \to \mathbb{R}_{\geq 0}$ that estimates the geodesic distance from any point to a designated goal region $G \subseteq M$.

**Definition A.10 (Admissibility).** A heuristic $h$ is *admissible* if $h(x) \leq d(x, G)$ for all $x \in M$, where $d(x,G)$ is the true geodesic distance to the nearest goal state.

**Definition A.11 (A* Search).** Given a weighted graph $(V, E, w)$ with start vertex $v_0$ and goal set $G \subseteq V$, the A* algorithm finds the minimum-cost path by maintaining:

$$f(v) = g(v) + h(v)$$

where $g(v)$ is the cost of the best known path from $v_0$ to $v$, and $h(v)$ is the heuristic estimate of the remaining cost to the goal.

**Theorem A.1 (Optimality of A*).** If $h$ is admissible and consistent ($h(v) \leq w(v,v') + h(v')$ for all edges $(v,v')$), then A* returns an optimal path.

*Cognitive interpretation*: Cognition is A* search on the cognitive manifold. The $g(v)$ component is deliberate reasoning --- the accumulated, verified cost of the reasoning path so far. The $h(v)$ component is the cognitive heuristic --- the fast, approximate estimate of how much further reasoning is needed. System 1 dominates when $h$ is reliable (low curvature); System 2 engages when $h$ is unreliable (high curvature). Heuristic corruption --- measured by the five sigma values --- is the mechanism of cognitive bias. (See Chapters 1--2.)

---

## A.4 The Scalar Irrecoverability Theorem

**Theorem A.2 (Scalar Irrecoverability).** Let $n > 1$. No continuous function $\phi: \mathbb{R}^n \to \mathbb{R}$ is injective.

*Proof.* By the rank-nullity theorem, $\ker(D\phi_p)$ has dimension $\geq n - 1$ at every regular point $p$. Thus $\phi$ identifies distinct points in $\mathbb{R}^n$ that differ only along the kernel directions. No continuous function $\psi: \mathbb{R} \to \mathbb{R}^n$ satisfies $\psi \circ \phi = \text{id}$, because such a $\psi$ would imply injectivity of $\phi$. $\square$

**Corollary A.3 (IQ Irrecoverability).** IQ is a continuous function $\phi: \mathbb{R}^{21} \to \mathbb{R}$ on the cognitive profile space (or $\mathbb{R}^5$ on the track-level space). By Theorem A.2, IQ identifies distinct cognitive profiles that differ on at least 20 (or 4) dimensions. No post-hoc adjustment can recover the information that IQ discards.

*Cognitive interpretation*: This is the mathematical foundation of the book's critique of scalar intelligence measures. The g-factor, IQ, benchmark accuracy, and composite leaderboard scores all fall under the scope of the theorem. Chapter 1 develops the full implications with constructive examples from the Measuring AGI benchmarks.

---

## A.5 Symmetry Groups and D4 Augmentation

**Definition A.12 (Dihedral Group $D_4$).** The dihedral group $D_4$ is the symmetry group of the square, consisting of 8 elements: the identity, three rotations ($90°$, $180°$, $270°$), and four reflections (horizontal, vertical, and two diagonal). It has generators $r$ (rotation) and $s$ (reflection) with relations $r^4 = e$, $s^2 = e$, $srs = r^{-1}$.

*Cognitive interpretation*: The $D_4$ group appears in two contexts in this book. First, in the Social Cognition benchmark (Chapter 7), the $D_4$ symmetry of Hohfeldian jural relations inherited from *Geometric Ethics* is used to test gauge invariance of moral judgment. Second, in the ARC-AGI benchmark context, $D_4$ augmentation --- applying all 8 symmetry transformations (rotations and reflections) of a grid input --- is a standard technique for improving pattern recognition. The AIRV (Augment, Infer, Reverse, Vote) pipeline from the MindsAI approach uses $D_4$ augmentation to generate 8 candidate solutions from each input, then votes across the augmented solutions to select the most consistent answer. (See Chapter 15.)

---

## A.6 The Corruption Tensor

**Definition A.13 (Corruption Tensor).** The *corruption tensor* $C_{\mu\nu}$ quantifies the deviation of the heuristic field from its uncorrupted value under perturbation. Given a perturbation $\xi^\mu$ applied to the input and the resulting change $\delta h$ in the heuristic field:

$$C_{\mu\nu} = \frac{\partial^2 (\delta h)}{\partial \xi^\mu \partial \xi^\nu}$$

The tensor is symmetric. Its trace $C^\mu{}_\mu$ gives the total corruption magnitude. Its eigenstructure reveals which dimensions of the cognitive manifold are most vulnerable to perturbation.

*Cognitive interpretation*: The corruption tensor is the mathematical object behind the five sigma values. Framing effects (15.3 sigma) correspond to large off-diagonal components of $C_{\mu\nu}$ in the social cognition submanifold. Emotional anchoring (6.8 sigma) corresponds to coupling between the emotional dimension and the executive control dimension. Distractor displacement (4.6 sigma) corresponds to perturbation of the attention metric itself. (See Chapters 7--11.)

---

## A.7 Finsler Metrics and Asymmetric Cognition

**Definition A.14 (Finsler Metric).** A *Finsler metric* on a manifold $M$ is a smooth function $F: TM \to \mathbb{R}_{\geq 0}$ that is positively homogeneous of degree 1 in each fiber ($F(x, \lambda v) = \lambda F(x, v)$ for $\lambda > 0$) and strictly convex in $v$. Unlike a Riemannian metric, a Finsler metric need not satisfy $F(x, v) = F(x, -v)$.

*Cognitive interpretation*: Cognitive effort is asymmetric: acquiring a belief is easier than revising it; attending to a salient stimulus is easier than disengaging from it; switching into a new framework is harder than maintaining the current one. These asymmetries are naturally captured by a Finsler metric, where the cost of moving from state $A$ to state $B$ differs from the cost of moving from $B$ to $A$. Chapter 17 discusses whether the cognitive manifold is fundamentally Riemannian (symmetric distance) or Finsler (asymmetric distance), and what evidence could distinguish the two.
