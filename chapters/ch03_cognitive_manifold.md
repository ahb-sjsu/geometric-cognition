# Chapter 3: The Cognitive Manifold

> *"The purpose of computing is insight, not numbers."*
> --- Richard Hamming, *Numerical Methods for Scientists and Engineers* (1962)

---

> **RUNNING EXAMPLE --- MAYA'S MODEL**
>
> Maya is watching a trajectory.
>
> Her subject, Dr. James Okafor, is reasoning through a moral dilemma inside the fMRI scanner. The dilemma is one she designed: a hospital has one dose of a scarce medication. Two patients need it. Patient A is younger, with a longer expected lifespan. Patient B is older, but has been waiting longer and has a dependent family. There is no clearly "right" answer. That is the point.
>
> The fMRI records a volume of brain activation every two seconds. Each volume is a vector in a space with roughly 100,000 dimensions---one per voxel. James's trajectory through this space is a sequence of 100,000-dimensional vectors, one every two seconds, for three minutes of deliberation.
>
> Maya cannot visualize 100,000 dimensions. Nobody can. But she has a hypothesis: the trajectory does not actually use all 100,000 dimensions. It lives on a much lower-dimensional surface---a manifold---embedded in the high-dimensional activation space. If she can find that manifold, she can see the shape of James's reasoning.
>
> She applies principal component analysis to the trajectory. The first three components capture 72% of the variance. She plots them. What she sees makes her catch her breath.
>
> The trajectory is not random. It is not a cloud. It is a *curve*---a smooth, continuous path through a three-dimensional subspace of the 100,000-dimensional activation space. The curve starts at a point she labels "problem representation" (the initial encoding of the dilemma), sweeps through a region she labels "utilitarian consideration" (where the activation pattern resembles known patterns for cost-benefit analysis), curves sharply toward a region she labels "deontological constraint" (where the pattern resembles known patterns for duty-based reasoning), and finally converges to a point she labels "judgment" (where the activation pattern stabilizes into the response).
>
> The sharp curve in the middle---where utilitarian consideration gives way to deontological constraint---is exactly the high-curvature region she predicted from the geometric framework. The trajectory does not pass through it smoothly. It slows down, oscillates slightly (James is hesitating), and then navigates the curve with a deliberate arc that costs visible cognitive effort. This is System 2, geometrized. This is the geodesic computation, made visible in the fMRI.
>
> Maya writes: *"The manifold is real. It has dimension approximately three for this task. It has curvature. The trajectory follows it. The cognitive manifold is not a metaphor. It is the actual geometry of thought."*

---

## 3.1 From Search Space to Manifold

Chapter 1 argued that reasoning is search, and that the quality of reasoning depends on the heuristic field that guides the search. Chapter 2 argued that the search space has geometric structure---curvature, geodesics, metric---and that this structure determines whether fast, heuristic-dominated processing (System 1) or slow, deliberate processing (System 2) is required. But neither chapter defined the search space itself with mathematical precision.

This chapter fills the gap. We define the *cognitive manifold*: the space of all cognitive states a system can occupy. We show that this space has the mathematical structure of a Riemannian manifold---a smooth space equipped with a metric that defines distances, angles, and curvature. And we show that the manifold hypothesis, a powerful idea from machine learning, applies to cognition: the cognitive states that a system actually visits form a low-dimensional submanifold of the high-dimensional activation space.

The cognitive manifold is the central mathematical object of this book. Every concept we have introduced so far---the heuristic field, the gradient, the geodesic, the curvature---lives on the cognitive manifold. Every concept we will introduce in subsequent chapters---the attention metric (Chapter 4), working memory as tangent space (Chapter 5), executive functions as search control (Chapter 6)---is a property of the cognitive manifold. Understanding the manifold is understanding the framework.


## 3.2 What Is a Cognitive State?

Before we can define the space of cognitive states, we need to define a cognitive state.

**Definition 3.1** (Cognitive State). *A cognitive state of a system $S$ at time $t$ is the complete internal configuration that determines the system's behavior at time $t$. For a neural system (human brain or artificial neural network), the cognitive state is the vector of activations across all neurons or units.*

For a human brain, the cognitive state at time $t$ is the pattern of firing rates across approximately 86 billion neurons. This is a vector in $\mathbb{R}^{86 \times 10^9}$---an astronomically high-dimensional space. Each dimension corresponds to one neuron's firing rate. Each point in this space corresponds to a complete configuration of neural activity.

For a large language model, the cognitive state at a given position in the sequence is the residual stream vector: the activation pattern across all units in the model's hidden layers. For a model with hidden dimension $d = 4096$ and $L = 32$ layers, the cognitive state is a vector in $\mathbb{R}^{4096 \times 32}$---again, a high-dimensional space.

In both cases, the cognitive state is a point in a very high-dimensional space---the *activation space* of the system.

**Definition 3.2** (Activation Space). *The activation space $\mathcal{A}$ of a cognitive system $S$ is the space of all possible activation patterns. For a neural system with $N$ units, $\mathcal{A} \subseteq \mathbb{R}^N$, where each coordinate corresponds to the activation of one unit.*

The activation space is vast. For a brain with $N = 86 \times 10^9$ neurons, each firing at rates between 0 and 200 Hz, the activation space has $86 \times 10^9$ dimensions. For a language model with $N = 131072$ hidden units per layer across 32 layers, the activation space has roughly $4 \times 10^6$ dimensions. Most points in these spaces correspond to no meaningful cognitive state---they are random patterns of activation that the system would never produce.

This is where the manifold hypothesis enters.


## 3.3 The Manifold Hypothesis

The manifold hypothesis, as articulated in the machine learning literature by Bengio et al. (2013), Tenenbaum et al. (2000), and Roweis and Saul (2000), states:

> *High-dimensional data generated by natural processes tends to concentrate near a low-dimensional manifold embedded in the high-dimensional space.*

The hypothesis has been validated extensively in machine learning. Images of faces, despite living in a space with millions of dimensions (one per pixel), concentrate near a manifold with perhaps 50 dimensions (corresponding to variations in identity, expression, pose, lighting). Natural language sentences, despite being sequences of tokens from a vocabulary of tens of thousands, concentrate near a manifold whose dimensionality is much lower---determined by the number of independent semantic and syntactic degrees of freedom.

**Definition 3.3** (The Cognitive Manifold Hypothesis). *The cognitive states that a system actually visits form a smooth, low-dimensional submanifold $\mathcal{M}$ of the high-dimensional activation space $\mathcal{A}$:*

$$\mathcal{M} \subset \mathcal{A}, \quad \dim(\mathcal{M}) \ll \dim(\mathcal{A})$$

*The dimensionality of $\mathcal{M}$ is the number of independent degrees of freedom of cognition---the number of independent ways the cognitive state can vary.*

This is a strong claim, and it requires justification.

**Why should cognitive states lie on a manifold?** The answer is constraint. A cognitive system is not free to occupy any point in activation space. It is constrained by anatomy (which neurons are connected to which), by dynamics (how activation propagates through the network), by homeostasis (which maintains activation levels within viable ranges), and by function (the system is performing a task, which restricts the relevant degrees of freedom). These constraints jointly reduce the effective dimensionality of the activation space.

Consider an analogy. The configuration space of a human body has roughly $6 \times 244 = 1464$ dimensions (six degrees of freedom per joint, approximately 244 joints). But the configurations that a body actually assumes during, say, walking are far fewer---walking is approximately a 2-dimensional manifold (parameterized by the phase of the gait cycle and the speed). The anatomical constraints, the dynamics of locomotion, and the functional requirement of forward motion jointly reduce a 1464-dimensional space to a 2-dimensional manifold.

Similarly, the activation space of a brain has $86 \times 10^9$ dimensions, but the states that the brain actually visits during, say, moral reasoning are far fewer. The anatomical constraints (which brain regions are relevant to moral reasoning), the dynamics (how information flows between regions), and the functional requirements (the task demands) jointly reduce the space to a manifold whose dimensionality is determined by the number of independent cognitive variables in play.


## 3.4 Evidence for the Cognitive Manifold

The cognitive manifold hypothesis is supported by evidence from neuroscience, psychology, and artificial intelligence.

**Neuroscience: Neural population dynamics.** Churchland et al. (2012), Cunningham and Yu (2014), and Gallego et al. (2017) have demonstrated that neural population activity during motor, cognitive, and decision-making tasks lies on low-dimensional manifolds. Using dimensionality reduction techniques (PCA, GPFA, LFADS) applied to multi-electrode recordings, these researchers have shown that the effective dimensionality of neural population dynamics during a task is typically 5--20, despite recording from hundreds or thousands of neurons. The population dynamics trace smooth trajectories on these low-dimensional manifolds, and the structure of the manifold captures task-relevant information.

**Psychology: The factor structure of cognition.** The psychometric tradition, from Spearman through Cattell to the current CHC theory, has documented that cognitive test performance has a low-dimensional factor structure. The number of independent broad factors in the CHC model is approximately 10 (crystallized intelligence, fluid intelligence, processing speed, short-term memory, long-term storage and retrieval, visual processing, auditory processing, quantitative knowledge, reading and writing, reaction time). This factor structure is the psychometric shadow of the cognitive manifold: the 10 broad factors are approximately the dimensionality of the manifold, and each factor corresponds to an independent degree of freedom.

**Artificial intelligence: Representation learning.** Modern neural networks learn internal representations that lie on low-dimensional manifolds. The residual stream of a transformer, despite having thousands of dimensions per layer, concentrates on manifolds whose intrinsic dimensionality has been estimated at 50--200 (Aghajanyan et al., 2020; Li et al., 2018). The low intrinsic dimensionality of these representations is what makes techniques like LoRA (low-rank adaptation) effective: they fine-tune the model by perturbing the representation along the manifold's tangent directions, which is sufficient because the representation already lives on a low-dimensional subspace.

**The Measuring AGI benchmarks.** Our own benchmark data are consistent with the manifold hypothesis. The five cognitive tracks define five substantially independent dimensions of variation. Within each track, the subtask scores are correlated (they probe aspects of the same cognitive capability), consistent with the track corresponding to a single degree of freedom. Between tracks, the correlations are weak, consistent with the tracks corresponding to independent dimensions. The effective dimensionality of the cognitive profile space, as estimated by the number of tracks with substantial independent variance, is approximately 5---dramatically lower than the 21-dimensional space of individual subtask scores.


## 3.5 The Structure of the Manifold

A manifold is more than a set of points. It has structure: topology, differentiability, and---when equipped with a metric---geometry.

**Topology.** The topology of the cognitive manifold determines its global structure: how many disconnected components it has, whether it has "holes," whether it wraps around on itself. Two cognitive states are topologically "close" if there exists a continuous path between them---a continuous sequence of cognitive states connecting one to the other. Two states are topologically "disconnected" if no such path exists.

The topology of the cognitive manifold has direct cognitive implications. If the manifold has multiple connected components, then some cognitive transitions are impossible---the system cannot move continuously from one component to another. If the manifold has a "hole," then some trajectories must go around the hole, increasing the distance between states that appear geometrically close. These topological features correspond to cognitive constraints: certain thoughts are inaccessible from certain starting states, and certain reasoning paths are forced to take detours.

**Differentiability.** The cognitive manifold is smooth: nearby cognitive states are similar in their activation patterns, and small changes in the cognitive state produce small changes in behavior. This smoothness is guaranteed by the continuous dynamics of neural networks (both biological and artificial), which evolve through differential equations that produce smooth trajectories.

More precisely, the manifold is a $C^\infty$ differentiable manifold: it admits smooth coordinate charts, and the transition maps between charts are smooth. This smoothness is essential for defining the geometric objects we need: tangent spaces, metrics, curvature.

**Embedding.** The cognitive manifold is embedded in the activation space $\mathcal{A}$. The embedding is an injective smooth map $\iota: \mathcal{M} \hookrightarrow \mathcal{A}$ that sends each point on the manifold to its corresponding activation pattern. The embedding is not isometric in general: the metric on $\mathcal{M}$ (which we will define in Chapter 4 as the attention metric) need not agree with the Euclidean metric on $\mathcal{A}$.

This distinction---between the intrinsic metric on the manifold and the Euclidean metric of the embedding space---is crucial. Two cognitive states might be "close" in the Euclidean sense (their activation patterns are similar) but "far" in the intrinsic sense (transitioning between them requires a long, effortful cognitive process). Conversely, two states might be "far" in the Euclidean sense but "close" intrinsically (they are separated by a large activation difference but connected by a short cognitive path).

This is the geometric content of the distinction between "representational similarity" and "functional proximity." Representational similarity measures Euclidean distance in the activation space. Functional proximity measures geodesic distance on the cognitive manifold. They need not agree, and when they disagree, the manifold structure tells us something important about the cognitive architecture.


## 3.6 Coordinate Charts on the Cognitive Manifold

To work concretely with the cognitive manifold, we need coordinates. A coordinate chart is a smooth bijection from an open subset of the manifold to an open subset of $\mathbb{R}^n$, where $n$ is the dimension of the manifold.

**Definition 3.4** (Cognitive Coordinates). *A cognitive coordinate chart on $\mathcal{M}$ is a smooth bijection $\phi: U \to V$, where $U \subseteq \mathcal{M}$ is an open subset of the manifold and $V \subseteq \mathbb{R}^n$ is an open subset of $\mathbb{R}^n$. The coordinates $x^\mu = \phi^\mu(p)$ assign $n$ real numbers to each point $p \in U$.*

What are the natural coordinates on the cognitive manifold? The answer depends on the level of description.

**Neural coordinates.** The most fine-grained coordinates are the activations of individual neurons or units. In these coordinates, the embedding map $\iota$ is the identity (each point on the manifold is identified with its activation pattern), and the manifold is characterized by the constraints that reduce the high-dimensional activation space to a low-dimensional submanifold.

**Factor coordinates.** At an intermediate level, the coordinates can be the factor scores from a factor analysis---the projections of the activation pattern onto the principal components or independent components. These coordinates capture the main axes of variation and are approximately aligned with the independent degrees of freedom of the manifold.

**Cognitive coordinates.** At the most interpretable level, the coordinates can be cognitive variables---attention allocation, working memory contents, goal state, confidence level, emotional valence. These coordinates are the ones we use in the rest of this book, because they connect most directly to the cognitive phenomena we want to model.

The relationship between these coordinate systems is governed by the transition maps of differential geometry. Neural coordinates provide the fine-grained substrate. Factor coordinates provide an intermediate decomposition. Cognitive coordinates provide the interpretable description. The manifold is the same object in all three coordinate systems; only the representation changes.

The coordinate independence of the geometric framework is one of its principal strengths. The geodesic equation, the curvature tensor, the heuristic field, the attention metric---all are coordinate-independent objects. They can be expressed in any coordinate system, and the physical (cognitive) content is the same regardless of which coordinates we choose. This means that insights about cognition derived from fMRI data (neural coordinates) can be compared directly with insights derived from behavioral data (cognitive coordinates) or from internal model representations (factor coordinates). The geometric framework provides a common mathematical language that bridges these different levels of description.

This coordinate independence also resolves a persistent tension in cognitive science between "mechanistic" and "computational" levels of description. In the geometric framework, these are not competing explanations but different coordinate systems on the same manifold. The mechanistic description uses neural coordinates. The computational description uses cognitive coordinates. The manifold---the actual structure of cognition---is the same object in both coordinate systems. The question "Is cognition best described mechanistically or computationally?" becomes "Which coordinate system is most useful for the question at hand?"---a pragmatic question rather than a metaphysical one.


## 3.7 Trajectories on the Manifold

Cognition is not a static state. It is a process: a trajectory through the space of cognitive states. The cognitive manifold is the stage; the trajectory is the play.

**Definition 3.5** (Cognitive Trajectory). *A cognitive trajectory is a smooth curve $\gamma: [0, T] \to \mathcal{M}$ that describes the evolution of the cognitive state over time. The initial state is $\gamma(0) = x_0$, the final state is $\gamma(T) = x_T$, and the trajectory passes through the sequence of intermediate states $\gamma(t)$ for $0 < t < T$.*

A reasoning process---solving a problem, making a judgment, updating a belief---corresponds to a trajectory on the cognitive manifold. The trajectory starts at the initial cognitive state (the problem as represented), passes through intermediate states (the reasoning steps), and terminates at the final state (the answer, judgment, or updated belief).

Different reasoning strategies produce different trajectories. Gradient following (System 1) produces trajectories that follow the steepest descent of the heuristic field---curves that are locally optimal at each point but may be globally suboptimal. Geodesic computation (System 2) produces trajectories that are globally optimal---shortest paths on the manifold---but at higher computational cost.

The *shape* of the trajectory encodes the reasoning process. A straight trajectory (in manifold coordinates) indicates effortless reasoning through flat terrain. A curved trajectory indicates navigation through a region of high curvature---a region where the cognitive state changes direction, where competing considerations pull the trajectory in different directions. An oscillating trajectory indicates hesitation---the system moving back and forth between competing attractors before settling on a path.

Maya's fMRI observation from the opening of this chapter is a direct measurement of a cognitive trajectory. The sequence of activation patterns, projected onto the manifold's principal components, traces a curve through low-dimensional space. The shape of this curve---its curvature, its speed, its pauses---reveals the geometric structure of the reasoning process.


## 3.8 The Tangent Space at a Cognitive State

At each point on the cognitive manifold, there is a tangent space: the set of all directions in which the cognitive state can change.

**Definition 3.6** (Tangent Space). *The tangent space $T_x\mathcal{M}$ at a point $x \in \mathcal{M}$ is the vector space of all tangent vectors to the manifold at $x$. Each tangent vector $v \in T_x\mathcal{M}$ represents a possible direction and rate of change of the cognitive state.*

The tangent space has a direct cognitive interpretation that we will develop fully in Chapter 5: it is the working memory. The tangent vectors at $x$ represent the cognitive operations that are locally available---the inferences, associations, and transformations that can be performed from the current state in one reasoning step. The dimension of the tangent space is the number of independent cognitive operations available, which corresponds to the working memory capacity.

For now, the key point is that the tangent space is *local*. It depends on where you are on the manifold. Different cognitive states have different tangent spaces---different sets of locally available operations. This is the geometric expression of a familiar cognitive phenomenon: what you can think of next depends on what you are thinking of now. The set of accessible next-states changes as you move through the cognitive space.

The tangent space is also *finite-dimensional*. Even though the activation space $\mathcal{A}$ has billions of dimensions, the tangent space $T_x\mathcal{M}$ has only $n$ dimensions, where $n$ is the dimension of the manifold. This is a constraint on cognition: at any given moment, you can change your cognitive state along at most $n$ independent directions. All other changes are inaccessible from the current state in one step.


## 3.9 The Heuristic Field on the Manifold

The heuristic field, introduced informally in Chapters 1 and 2, can now be defined precisely as a scalar field on the cognitive manifold.

**Definition 3.7** (Heuristic Field). *The heuristic field is a smooth function $h: \mathcal{M} \to \mathbb{R}$ that assigns to each cognitive state $x \in \mathcal{M}$ an estimate of the cost-to-go from $x$ to the goal state $x^*$:*

$$h(x) \approx d_\mathcal{M}(x, x^*)$$

*where $d_\mathcal{M}$ is the geodesic distance on the manifold.*

The heuristic field has rich structure as a scalar field on a manifold:

**Gradient.** The gradient $\nabla h \in T_x\mathcal{M}$ is a tangent vector that points in the direction of steepest increase of $h$. System 1 processing follows the negative gradient $-\nabla h$: the direction of steepest estimated decrease in cost-to-go. This is the cognitive analogue of "going with your gut"---following the strongest internal signal toward the perceived best answer.

**Level sets.** The level sets $h^{-1}(c) = \{x \in \mathcal{M} : h(x) = c\}$ are the contour lines of the heuristic field---the loci of states that the system estimates to be equally far from the goal. In a well-calibrated system, the level sets are approximately concentric "spheres" centered on the goal state. In a poorly calibrated system, the level sets are distorted---compressed in some directions, expanded in others---reflecting the system's biased estimate of distance.

**Critical points.** The critical points of $h$---where $\nabla h = 0$---are the states where the system perceives no direction of improvement. Local minima of $h$ are states where the system believes it has arrived at the goal (or close enough). Saddle points of $h$ are states where the system is balanced between competing directions. Maxima of $h$ are states the system perceives as maximally far from the goal.

The critical point structure of the heuristic field determines the failure modes of the search. If $h$ has a local minimum far from the true goal---a state where the system believes it has found the answer but has not---then gradient-following search will converge to this false minimum and halt. This is the geometric characterization of premature convergence, and it explains why some cognitive errors are so persistent: the system is trapped in a local minimum of its own heuristic, and the gradient provides no signal to escape.


## 3.10 Curvature as Cognitive Complexity

The curvature of the cognitive manifold has appeared throughout the first two chapters as the key quantity that determines whether gradient following suffices (System 1) or geodesic computation is needed (System 2). We can now define it precisely.

**Definition 3.8** (Sectional Curvature). *The sectional curvature $\kappa(x; u, v)$ of the cognitive manifold at a point $x$, in the 2-plane spanned by tangent vectors $u, v \in T_x\mathcal{M}$, is:*

$$\kappa(x; u, v) = \frac{R(u, v, u, v)}{g(u, u) g(v, v) - g(u, v)^2}$$

*where $R$ is the Riemann curvature tensor and $g$ is the metric.*

The curvature has three regimes:

**Zero curvature ($\kappa = 0$).** The manifold is locally flat. Gradient following produces geodesics. Reasoning is effortless and reliable. Example: retrieving a well-known fact, computing a simple arithmetic expression.

**Positive curvature ($\kappa > 0$).** The manifold curves like a sphere. Parallel geodesics converge. Nearby reasoning trajectories tend to reach the same conclusion. Reasoning is robust: small perturbations to the initial state or the heuristic do not change the outcome. Example: well-constrained problems with a unique answer, where all reasonable approaches converge.

**Negative curvature ($\kappa < 0$).** The manifold curves like a saddle. Parallel geodesics diverge exponentially. Nearby reasoning trajectories can reach completely different conclusions. Reasoning is fragile: small perturbations can send the trajectory in a radically different direction. Example: moral dilemmas where small changes in framing produce large changes in judgment (our 15.3 sigma framing effect).

The connection between curvature and cognitive complexity is not a metaphor. It is a quantitative relationship. In regions of high negative curvature, the geodesic deviation grows exponentially with distance:

$$\|\delta\gamma(t)\| \sim \|\delta\gamma(0)\| \cdot e^{\sqrt{|\kappa|} \cdot t}$$

This means that two reasoning processes that start from nearly identical states---the same problem with slightly different framing---will diverge rapidly in a high-negative-curvature region, producing different conclusions. The rate of divergence is controlled by $\sqrt{|\kappa|}$. This is the geometric explanation of framing sensitivity: the manifold has negative curvature in the region where the framing manipulation takes effect, and the negative curvature amplifies the small perturbation into a large outcome difference.

The 15.3 sigma framing effect is evidence for high negative curvature in the moral judgment region of the cognitive manifold. The effect size tells us the magnitude of the geodesic divergence. The sigma value tells us the statistical reliability of the divergence. Together, they constrain the curvature: the manifold must be sufficiently negatively curved in the moral judgment region to produce divergences of the observed magnitude under perturbations of the observed size.


## 3.11 Worked Example: Mapping a Cognitive Trajectory

Let us work through Maya's fMRI observation in detail, using the formalism developed in this chapter.

**Setup.** Maya records the fMRI activation pattern of James Okafor at 90 time points (one every two seconds for three minutes) while James reasons about a moral dilemma. Each activation pattern is a vector in $\mathbb{R}^{100,000}$ (approximately 100,000 voxels in the fMRI volume).

**Step 1: Identify the manifold.** Maya applies PCA to the 90 activation vectors and finds that the first $n = 3$ principal components capture 72% of the variance. She projects the 90 vectors onto these three components, producing 90 points in $\mathbb{R}^3$. These points trace a curve in three-dimensional space---the cognitive trajectory projected onto the estimated manifold.

The choice of $n = 3$ is justified by the scree plot (the eigenvalue spectrum drops sharply after the third component) and by cross-validation (using more than three components does not significantly improve the reconstruction of the original activation patterns). The 28% of variance not captured by the first three components is noise (thermal noise in the fMRI signal) plus high-frequency fluctuations that are not task-related.

**Step 2: Identify the trajectory.** The projected trajectory $\gamma(t) = (x^1(t), x^2(t), x^3(t))$ is a smooth curve in $\mathbb{R}^3$. Maya fits a smooth spline to the 90 data points to obtain a continuous trajectory.

The trajectory has three phases:
- **Phase 1 (0--40 seconds):** Nearly linear motion from the initial state toward the "utilitarian consideration" region. This is System 1: gradient following in a low-curvature region.
- **Phase 2 (40--100 seconds):** Sharply curved motion transitioning from the utilitarian region to the "deontological constraint" region. The trajectory slows down (points are closer together in time), indicating increased cognitive effort. This is the System 1 to System 2 transition.
- **Phase 3 (100--180 seconds):** Decelerating motion converging to the "judgment" state. The trajectory spirals inward toward a fixed point, indicating convergence to a decision.

**Step 3: Estimate the curvature.** The curvature of the trajectory at each point can be estimated from the trajectory data. For a curve $\gamma(t)$ in $\mathbb{R}^3$, the curvature is:

$$\kappa(t) = \frac{\|\dot{\gamma}(t) \times \ddot{\gamma}(t)\|}{\|\dot{\gamma}(t)\|^3}$$

Maya computes $\kappa(t)$ at each time point. In Phase 1, $\kappa \approx 0.02$ (near-zero curvature). In Phase 2, $\kappa$ peaks at approximately 0.35 (high curvature). In Phase 3, $\kappa$ decreases to approximately 0.08 (moderate curvature).

The curvature profile confirms the geometric prediction: the System 1 to System 2 transition occurs precisely when the trajectory enters a high-curvature region of the manifold. The high curvature corresponds to the conflict between utilitarian and deontological considerations, which creates competing gradients that the trajectory must navigate.

**Step 4: Estimate the heuristic field.** The heuristic field $h(x)$ cannot be measured directly from fMRI data, but its gradient can be estimated from the velocity field $\dot{\gamma}(t)$. In the gradient-following regime (Phase 1), the velocity is proportional to $-\nabla h$:

$$\dot{\gamma}(t) \approx -\alpha \nabla h(\gamma(t))$$

where $\alpha > 0$ is a step-size parameter. From the observed velocities in Phase 1, Maya can reconstruct the gradient of $h$ in the utilitarian region of the manifold.

In Phase 2 (geodesic computation), the relationship between velocity and heuristic gradient is more complex---the trajectory includes geodesic correction terms that deviate from the gradient. But the deviation itself is informative: it reveals the Christoffel symbols, which encode the curvature of the manifold.

**Interpretation.** Maya has mapped a single cognitive trajectory onto a three-dimensional manifold, measured its curvature profile, and identified the System 1 / System 2 transition from the curvature data. The manifold is not an abstraction imposed from outside. It is the empirical structure of the activation data, revealed by dimensionality reduction and trajectory analysis.


## 3.12 The Manifold for Different Cognitive Tasks

The cognitive manifold is not a single, fixed object. Different tasks engage different submanifolds of the full cognitive space.

A moral reasoning task activates a submanifold whose dimensions correspond to moral-relevant cognitive variables: harm assessment, fairness evaluation, utilitarian calculation, deontological constraint checking. An arithmetic task activates a different submanifold whose dimensions correspond to numerical representations, operation selection, carry tracking. A social cognition task activates yet another submanifold whose dimensions correspond to theory of mind, emotional recognition, perspective taking.

These task-specific submanifolds overlap. Moral reasoning and social cognition share dimensions related to empathy and harm assessment. Arithmetic and executive function share dimensions related to working memory and sequential processing. The overlap structure encodes the relationships between cognitive capabilities---which capabilities share cognitive resources and which are independent.

The five cognitive tracks of the Measuring AGI benchmarks correspond, in this picture, to five task-specific submanifolds (or clusters of submanifolds). The independence of the tracks---the weak correlations between track scores---reflects the fact that these submanifolds occupy different regions of the full cognitive manifold, with little overlap. The strong correlations within tracks---the high correlations between subtask scores within a single track---reflect the fact that the subtasks within a track engage overlapping submanifolds.

The model-specific cognitive signatures---Claude's narrow channel, Flash 3's wide aperture, Pro's calibrated navigator---correspond to different geometric properties of the same manifold as navigated by different systems. The manifold is (approximately) the same for all models (the tasks are the same). The differences are in the heuristic field, the metric, and the control layer---the properties that determine *how* each model navigates the manifold, not the manifold itself.


## 3.13 Formal Properties of the Cognitive Manifold

We can now state the formal properties of the cognitive manifold that will be used throughout the rest of the book.

**Property 1: Finite dimensionality.** $\dim(\mathcal{M}) = n$, where $n$ is the number of independent cognitive degrees of freedom. For the Measuring AGI benchmark tasks, $n \approx 5$ (one per track). For general human cognition, $n$ is estimated at 10--20 (from the CHC factor structure and neural dimensionality studies).

**Property 2: Smoothness.** $\mathcal{M}$ is a $C^\infty$ differentiable manifold. Cognitive states vary smoothly, and the transition between nearby states is continuous. This property is guaranteed by the continuous dynamics of neural networks and justified by the smoothness of observed neural trajectories.

**Property 3: Riemannian structure.** $\mathcal{M}$ is equipped with a Riemannian metric $g$---a positive-definite symmetric bilinear form on each tangent space that defines distances, angles, and curvature. The metric is the attention metric, developed in Chapter 4.

**Property 4: Non-trivial curvature.** The curvature of $\mathcal{M}$ is not uniformly zero. There are regions of high curvature (where cognitive tasks are complex and require deliberate processing) and regions of low curvature (where tasks are simple and can be handled by gradient following). The curvature varies smoothly across the manifold.

**Property 5: Non-trivial topology.** The manifold may have "holes" or multiple connected components, corresponding to cognitive states or transitions that are inaccessible. The empty Quadrant I in the metacognitive plane (the M3/M4 dissociation from Chapter 9 of the Geometric Reasoning manuscript) may reflect a topological constraint: a "hole" in the metacognitive submanifold that prevents any system from having both good self-monitoring and good effort scaling.

**Property 6: Embedding.** $\mathcal{M}$ is embedded in the activation space $\mathcal{A}$ via a smooth injective map $\iota: \mathcal{M} \hookrightarrow \mathcal{A}$. The embedding is not isometric: the intrinsic metric on $\mathcal{M}$ (the attention metric) differs from the Euclidean metric on $\mathcal{A}$.


## 3.14 The Manifold as Unifying Framework

The cognitive manifold provides the unifying framework for everything that follows.

In Chapter 4, we define the metric on the manifold---the attention metric---which determines which cognitive states are "close" (easily reached) and which are "far" (requiring effort). The attention mechanism of a transformer or the selective attention of a human brain defines this metric: what you attend to determines how you measure distance in cognitive space.

In Chapter 5, we interpret the tangent space as working memory: the set of cognitive states reachable in one step from the current state. Working memory capacity is the dimension of the tangent space. Working memory load is the fraction of tangent dimensions currently in use.

In Chapter 6, we interpret executive functions as the control layer that governs search on the manifold. Cognitive flexibility (E1) is the ability to switch between different regions of the manifold. Inhibitory control (E3) is the ability to suppress gradient-following when it leads to an incorrect destination. Working memory scaling (E4) is the ability to expand the tangent space when the task demands more simultaneous degrees of freedom.

In Chapters 7--11, we apply the framework to the five cognitive dimensions measured by the Measuring AGI benchmarks. Each dimension corresponds to a specific geometric property of the cognitive manifold: social cognition as navigation in judgment space (curvature and heuristic corruption), learning as trajectory revision (belief updating on the manifold), metacognition as distance estimation (calibration of the heuristic field), attention as manifold filtering (metric properties under perturbation), and executive control as geodesic governance (the control layer that manages the search).

The cognitive manifold is not a metaphor. It is a specific mathematical object---a Riemannian manifold embedded in activation space---with specific measurable properties. The next chapter begins the measurement.


## 3.15 The Empty Quadrant as Topological Constraint

One of the most striking findings from the Measuring AGI benchmarks is the empty Quadrant I in the metacognitive plane. When we plot models on two axes---M3 (self-monitoring capability) and M4 (effort scaling capability)---we find that no model occupies the quadrant where both capabilities are strong.

Some models have good self-monitoring but poor effort scaling. Others have good effort scaling but poor self-monitoring. None have both. The upper-right quadrant is empty.

This dissociation admits a natural interpretation in terms of the cognitive manifold's topology. The metacognitive submanifold---the region of the cognitive manifold corresponding to metacognitive states---may have a topological obstruction that prevents simultaneous high values on both dimensions.

Consider a two-dimensional metacognitive submanifold parameterized by self-monitoring quality $m_3$ and effort scaling quality $m_4$. If this submanifold were a simple rectangle $[0, 1] \times [0, 1]$, there would be no obstruction to occupying any point, including $(m_3, m_4) = (1, 1)$. But if the submanifold has a "hole" near the upper-right corner---a region of configuration space that is topologically inaccessible---then no system can occupy that region, regardless of training, architecture, or scale.

What would create such a hole? The answer may lie in the computational incompatibility of self-monitoring and effort scaling. Self-monitoring requires allocating cognitive resources to observe the system's own performance---a meta-level computation that draws resources away from the object-level task. Effort scaling requires dynamically adjusting the resources allocated to the object-level task---which requires knowing how much resource is currently available, which is itself a meta-level computation. When both systems demand meta-level resources simultaneously, they compete, creating a resource conflict that cannot be resolved by simply adding more resources (because the meta-level monitoring of resource allocation is itself resource-consuming, leading to a regress).

This resource conflict creates a constraint surface in the metacognitive submanifold: a boundary that the system cannot cross because crossing it would require more meta-level resources than the system can provide. The boundary curves through the upper-right quadrant, creating the observed empty region.

If this topological interpretation is correct, the empty quadrant is not a contingent limitation of current models that will be resolved by scaling. It is a structural feature of the cognitive manifold itself---a topological constraint on what cognitive architectures are possible. This is a strong prediction of the geometric framework, and it can be tested by examining whether future models, with different architectures and greater scale, ever populate Quadrant I.

---

## Technical Appendix 3A: Formal Definition of the Cognitive Manifold

**Definition** (Cognitive Manifold, Formal). *Let $\mathcal{A} = \mathbb{R}^N$ be the activation space of a cognitive system with $N$ units. The cognitive manifold is a triple $(\mathcal{M}, g, \iota)$ where:*

1. *$\mathcal{M}$ is a smooth, connected, $n$-dimensional manifold with $n \ll N$.*
2. *$g$ is a Riemannian metric on $\mathcal{M}$ (the attention metric, defined in Chapter 4).*
3. *$\iota: \mathcal{M} \hookrightarrow \mathcal{A}$ is a smooth embedding.*

*The manifold $\mathcal{M}$ satisfies the approximation property: for any cognitive trajectory $\gamma_\mathcal{A}: [0,T] \to \mathcal{A}$ generated by the system during task performance, there exists a curve $\gamma_\mathcal{M}: [0,T] \to \mathcal{M}$ such that:*

$$\|\iota(\gamma_\mathcal{M}(t)) - \gamma_\mathcal{A}(t)\|_\mathcal{A} \leq \epsilon \quad \text{for all } t \in [0, T]$$

*where $\epsilon$ is small relative to the scale of $\gamma_\mathcal{A}$. That is, the trajectory in activation space is well-approximated by a trajectory on the manifold.*


## Technical Appendix 3B: Dimensionality Estimation Methods

The intrinsic dimensionality of the cognitive manifold can be estimated from data using several methods:

**1. PCA scree analysis.** Apply PCA to a collection of cognitive state vectors (fMRI volumes, residual stream vectors) and examine the eigenvalue spectrum. The intrinsic dimensionality is approximately the number of eigenvalues above the noise floor, identified by the "elbow" in the scree plot.

**2. Maximum likelihood estimation (Levina and Bickel, 2004).** For each data point $x_i$, compute the distances to its $k$ nearest neighbors $r_1(x_i) \leq \cdots \leq r_k(x_i)$. The maximum likelihood estimate of the intrinsic dimensionality at $x_i$ is:

$$\hat{d}(x_i) = \left( \frac{1}{k-1} \sum_{j=1}^{k-1} \log \frac{r_k(x_i)}{r_j(x_i)} \right)^{-1}$$

The global dimensionality is estimated as the average of $\hat{d}(x_i)$ over all data points.

**3. Participatory ratio (PR).** For a set of data points with covariance matrix $\Sigma$ having eigenvalues $\lambda_1, \ldots, \lambda_N$:

$$\text{PR} = \frac{\left(\sum_{i=1}^N \lambda_i\right)^2}{\sum_{i=1}^N \lambda_i^2}$$

The PR estimates the effective number of dimensions that contribute to the variance. It ranges from 1 (all variance in one dimension) to $N$ (variance equally distributed across all dimensions).

These methods can be applied to fMRI data (to estimate the dimensionality of the human cognitive manifold during a specific task) and to transformer residual stream data (to estimate the dimensionality of the LLM cognitive manifold). The convergence of dimensionality estimates across methods and across human/AI systems would provide strong evidence for the cognitive manifold hypothesis and for the claim that human and artificial cognition share geometric structure.
