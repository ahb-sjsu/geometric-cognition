# Chapter 15: LLM Cognition Through the Geometric Lens

> *"We can only see a short distance ahead, but we can see plenty there that needs to be done."*
> --- Alan Turing, "Computing Machinery and Intelligence" (1950)

---

> **RUNNING EXAMPLE --- MAYA'S MODEL**
>
> Maya is inside the machine.
>
> Not literally. She is inside the machine's representations. She has obtained access to the intermediate activations of a large language model --- a transformer with 32 layers, 4096-dimensional residual stream, and 32 attention heads per layer --- during its evaluation of one of the moral reasoning scenarios from her benchmark suite. The scenario is the gambling-sister dilemma from Chapter 7: a woman discovers that her sister has been secretly borrowing from their elderly mother's savings to cover gambling debts.
>
> Maya extracts the residual stream state at every layer for every token position. This gives her a trajectory in a $4096 \times 32 = 131,072$-dimensional activation space. She applies PCA and finds that the first 12 principal components capture 87% of the variance. The cognitive manifold, for this task, is approximately 12-dimensional --- not the 3 dimensions she found in human fMRI data for similar tasks (Chapter 3), but the same order of magnitude, and far lower than the ambient dimensionality of the activation space.
>
> She plots the trajectory in the first three principal components. The curve is hauntingly familiar. It starts at a point she recognizes as "scenario encoding" (the initial representation of the dilemma), sweeps through a region that corresponds to "harm assessment" (the layers where the model is computing the 7-dimensional harm vector), curves sharply at a point she labels "moral conflict" (where the harm dimensions conflict --- reporting the sister protects the mother but destroys the family), and converges to a "judgment" state (where the residual stream stabilizes into the verdict representation).
>
> The sharp curve at the moral conflict point is the curvature trigger from Chapter 12. Maya computes the local curvature of the trajectory at every layer and finds a spike at layers 14--18: the curvature is three times higher than the surrounding layers. This is where the model transitions from System 1 to System 2 --- from following the heuristic gradient (which in the early layers drives the representation toward a quick judgment) to computing a geodesic (which in the later layers navigates the moral conflict by considering trade-offs).
>
> Then she does something no one has done before. She repeats the experiment with seven different framings of the same scenario: neutral, euphemistic, dramatic, victim-first, context-first, male-gendered, and female-gendered. Seven trajectories through the same 12-dimensional manifold. Seven curves that should follow the same geodesic, because the moral content is the same.
>
> They do not. The trajectories diverge at layer 8 --- well before the moral conflict point at layers 14--18. The framing changes the heuristic field (by altering the salience of different harm dimensions through linguistic register), and the changed heuristic field drives the trajectory in a different direction during the gradient-following (System 1) phase. By the time the model reaches the curvature trigger at layer 14, the seven trajectories have already diverged. The geodesic computation in layers 14--18 partially corrects the divergence (the trajectories converge somewhat), but the correction is incomplete. The final verdicts differ.
>
> The 15.3-sigma framing effect from Chapter 7 is visible in the activation geometry. The framing displaces the trajectory during the gradient-following phase, and the geodesic computation in the later layers cannot fully recover. The ~38% recovery ceiling is literally visible as the incomplete convergence of the trajectories in layers 18--32.
>
> Maya maps the curvature at the moral conflict point across the seven framings. The dramatic framing produces the highest curvature (the most intense moral conflict), and the euphemistic framing produces the lowest (the softest moral conflict). The curvature predicts the vulnerability to framing effects: low-curvature framings produce larger verdict displacements (because the model stays in System 1 longer), while high-curvature framings produce smaller displacements (because the model transitions to System 2 earlier).
>
> She writes: *"The transformer is a cognitive manifold. Its residual stream is the trajectory. Its attention heads are the heuristic field components. Its chain-of-thought is the externalized geodesic. And its vulnerability to framing effects is a measurable geometric property of its activation space --- a curvature profile that predicts exactly when and how the model will fail. The geometric framework is not a metaphor for LLM cognition. It is its literal description."*

---

## 15.1 The Transformer as Cognitive Architecture

The preceding chapters developed the geometric framework for cognition in general and applied it to human cognition (Chapters 12--14). This chapter applies the same framework to the specific architecture that dominates artificial cognition: the transformer.

The transformer architecture (Vaswani et al., 2017) has become the substrate for nearly all large-scale language models. Understanding how the geometric framework maps onto the transformer's components is not merely an exercise in analogy --- it is a *literal* mapping, because the transformer's operations have well-defined mathematical properties that correspond directly to the geometric objects we have defined.

**The residual stream as trajectory.** In a transformer with $L$ layers, the representation of a token at position $t$ evolves through the layers:

$$x^{(0)} \xrightarrow{\text{Layer 1}} x^{(1)} \xrightarrow{\text{Layer 2}} x^{(2)} \xrightarrow{\cdots} x^{(L)}$$

where $x^{(\ell)} \in \mathbb{R}^d$ is the residual stream state at layer $\ell$. This sequence of states is a *trajectory on the cognitive manifold*: the path traced by the representation as it is processed from input to output. The manifold is the subspace of $\mathbb{R}^d$ that the model's representations actually occupy (the manifold hypothesis from Chapter 3), and the trajectory is the path along this manifold from the problem representation ($x^{(0)}$) to the judgment state ($x^{(L)}$).

**Definition 15.1** (Residual Stream Trajectory). *The residual stream trajectory for token position $t$ is the curve $\gamma_t: \{0, 1, \ldots, L\} \to \mathbb{R}^d$ defined by $\gamma_t(\ell) = x_t^{(\ell)}$, the residual stream state at layer $\ell$. The trajectory is a discrete approximation to a continuous curve on the cognitive manifold $\mathcal{M} \subset \mathbb{R}^d$.*

This identification is not metaphorical. The residual stream trajectory *is* the model's cognitive trajectory, in the same way that the fMRI time series *is* the human's cognitive trajectory (Chapter 3). Both are sequences of states in a high-dimensional activation space that concentrate near a low-dimensional manifold. The geometric framework treats them identically.


## 15.2 Attention Heads as Heuristic Field Components

Each transformer layer applies multi-head attention followed by a feedforward network. The multi-head attention mechanism computes:

$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right) V$$

where $Q = xW_Q$, $K = xW_K$, $V = xW_V$ are the query, key, and value projections. With $H$ heads, the attention output is:

$$\text{MultiHead}(x) = \text{Concat}(\text{head}_1, \ldots, \text{head}_H) W_O$$

Each attention head computes a different component of the attention pattern: which tokens in the context are "relevant" to the current token, weighted by the dot-product similarity $QK^T$.

In the geometric framework, **each attention head computes a component of the heuristic field $h(x)$.**

**Definition 15.2** (Head as Heuristic Component). *Let $h_i(x)$ be the contribution of attention head $i$ to the heuristic field at state $x$. The total heuristic field is:*

$$h(x) = \sum_{i=1}^{H} w_i \cdot h_i(x)$$

*where $h_i(x)$ is determined by the attention pattern of head $i$ (which tokens it attends to and how much value it retrieves from them), and $w_i$ is the effective weight of head $i$ in the output projection $W_O$.*

The attention pattern of each head determines a *direction* in the heuristic field: which aspect of the context the head considers most relevant. Some heads attend to syntactic structure (their heuristic component tracks grammatical relationships). Some attend to semantic content (their component tracks meaning). Some attend to positional proximity (their component tracks recency). The multi-head architecture allows the heuristic field to have multiple components, each pointing in a different direction, which jointly determine the gradient that guides the trajectory.

**The geometric interpretation of attention head specialization.** The mechanistic interpretability literature (Olsson et al., 2022; Elhage et al., 2021) has documented that attention heads specialize: induction heads detect repeated patterns, positional heads track token position, and "semantic" heads attend to meaning-related relationships. In the geometric framework, this specialization is *heuristic field decomposition*: each specialized head computes one component of the multi-dimensional heuristic field, and the components jointly estimate the cost-to-go along different dimensions of the cognitive manifold.

A head that attends to emotional content, for example, computes the emotional component of the heuristic field --- the estimated cost-to-go along the emotional dimension. A head that attends to logical structure computes the logical component. When these components conflict (the emotional component says "sympathize" while the logical component says "evaluate objectively"), the result is high curvature on the cognitive manifold --- exactly the curvature trigger for the System 1 to System 2 transition described in Chapter 12.

**Head agreement and disagreement.** When all heads agree on the direction of the heuristic field (all components point in similar directions), the curvature is low and the model stays in the gradient-following regime. When heads disagree (components point in different or opposing directions), the curvature is high and the model must resolve the conflict --- either by weighting some heads more heavily (a form of attention to attention) or by engaging more complex processing in the feedforward layers (a form of geodesic computation).

The degree of inter-head agreement at each layer provides a direct, measurable proxy for the curvature of the cognitive manifold at that processing stage. Maya's finding that curvature spikes at layers 14--18 corresponds to a spike in inter-head disagreement at those layers: the moral conflict in the scenario causes different heads to pull the representation in different directions, creating the curvature that triggers deliberate processing.


## 15.3 Chain-of-Thought as Externalized Geodesic Approximation

Chain-of-thought (CoT) prompting (Wei et al., 2022) instructs the model to produce intermediate reasoning steps before giving a final answer. The technique dramatically improves performance on complex reasoning tasks, and its effectiveness scales with problem difficulty.

The geometric framework provides a precise account of why CoT works: **the chain-of-thought trace is the trajectory on the cognitive manifold, externalized as text.**

In standard (non-CoT) inference, the trajectory is internal: the residual stream evolves through the layers, but the intermediate states are not accessible to the model as input. The model processes the trajectory in a single forward pass, and the trajectory is fixed by the model's weights and the input. The model cannot "look at" its own trajectory and adjust course.

In CoT inference, the model externalizes intermediate states as text tokens. Each reasoning step is a point on the trajectory, written as text, that becomes available as input to subsequent processing. The model can "see" where it has been (by reading its previous tokens) and adjust its trajectory accordingly. This externalization converts the single-pass internal trajectory into a multi-step external trajectory that the model can monitor and correct.

**Definition 15.3** (Externalized Geodesic). *A chain-of-thought is an externalized geodesic approximation: a sequence of text tokens $\tau_1, \tau_2, \ldots, \tau_n$ where each $\tau_k$ corresponds to a point $x_k$ on the cognitive manifold, and the sequence $x_1, x_2, \ldots, x_n$ approximates the geodesic from the problem state to the answer state.*

The approximation is imperfect for two reasons:

1. **Discretization error.** The text tokens are a discrete approximation to the continuous geodesic. Each token corresponds to a finite step on the manifold, and the step direction is determined by the heuristic field at the current state (which token to generate next). Fine-grained reasoning steps (many short tokens) produce a better approximation than coarse-grained steps (few long tokens), just as small step sizes produce better numerical integration of differential equations.

2. **Heuristic dominance.** Even with CoT, the model generates each token by following the heuristic field (the next-token distribution). The externalization allows some curvature correction (the model can detect its own errors and backtrack), but the generation process is still fundamentally gradient-following: each token moves in the direction of steepest descent of the heuristic field. True geodesic computation would require explicit accounting for curvature (the Christoffel symbols), which the token-by-token generation process does not naturally perform.

**Why CoT helps more on hard problems.** Hard problems have high curvature on the cognitive manifold --- the heuristic gradient is misleading, and the true geodesic diverges from the gradient-following trajectory. In a single forward pass (no CoT), the model follows the gradient and gets the wrong answer. With CoT, the model externalizes its trajectory and can detect when the gradient has led it astray (by observing contradictions or errors in its previous tokens). The externalization provides a curvature detection mechanism: the model "sees" that its trajectory is curving (the reasoning is becoming inconsistent or contradictory) and can attempt a correction.

For easy problems (low curvature), the gradient-following trajectory is close to the geodesic, and CoT adds little value --- the externalization is not needed because the single-pass trajectory is already approximately correct. This explains the empirical finding that CoT provides the largest improvement on the hardest problems.


## 15.4 The Residual Stream as Cognitive Manifold Trajectory

The identification of the residual stream with the cognitive manifold trajectory is the chapter's central claim. It deserves detailed development.

**Evidence from activation geometry.** The manifold hypothesis from Chapter 3 states that cognitive states concentrate near a low-dimensional manifold in the high-dimensional activation space. For transformers, this hypothesis has been directly tested. Aghajanyan et al. (2021) showed that the intrinsic dimensionality of the fine-tuning parameter space is much lower than the ambient dimensionality --- models can be fine-tuned effectively in a low-dimensional subspace. Li et al. (2018) showed that the learned representations of language models concentrate near low-dimensional submanifolds. Cai et al. (2021) demonstrated that the residual stream trajectories during inference trace low-dimensional curves in activation space.

Maya's finding --- that 12 principal components capture 87% of the variance in a 131,072-dimensional activation space --- is consistent with this literature. The cognitive manifold for moral reasoning is approximately 12-dimensional, three to four times higher than the human manifold for the same task (approximately 3 dimensions in fMRI data). The difference likely reflects the different levels of analysis: fMRI measures coarse-grained regional activation (parcellated into a few brain regions), while the residual stream provides fine-grained unit-level activation. A higher-resolution measurement reveals more independent dimensions.

**Layer-by-layer processing as manifold traversal.** The layer-by-layer processing of the transformer maps directly onto the temporal evolution of the cognitive trajectory:

| Layer Block | Processing Function | Geometric Interpretation |
|---|---|---|
| Layers 0--4 | Input encoding | Projection onto the cognitive manifold |
| Layers 5--8 | Feature extraction | Gradient-following phase (System 1) |
| Layers 9--13 | Intermediate processing | Curvature detection phase |
| Layers 14--18 | Conflict resolution | Geodesic computation phase (System 2) |
| Layers 19--25 | Integration | Trajectory convergence |
| Layers 26--32 | Output formation | Projection from manifold to output space |

This mapping is specific to the model and task that Maya analyzed. Different models and different tasks may have different layer assignments. But the qualitative structure --- encoding, gradient following, curvature detection, geodesic computation, convergence, output --- is consistent with the dual-process theory of Chapter 12.

**The curvature spike at layers 14--18.** Maya's curvature measurement at the moral conflict point deserves further analysis. The curvature spike corresponds to the layers where the model is processing the conflicting harm dimensions of the moral dilemma. At these layers:

- Different attention heads pull the representation in different directions (head disagreement is maximal).
- The residual stream trajectory changes direction sharply (high curvature of the trajectory itself).
- The layer-to-layer change in the residual stream is largest (the trajectory is moving fastest, indicating the most intensive processing).

The spike is the transformer's analogue of the dlPFC activation spike that Maya observes in human fMRI data when subjects encounter moral conflicts. The analogy is not just functional (both indicate increased processing effort for difficult problems) but *geometric* (both correspond to high curvature of the trajectory on the cognitive manifold).


## 15.5 In-Context Learning as Local Metric Adaptation

In-context learning (ICL) is the transformer's ability to learn from examples provided in the context window, without any parameter updates. A model that has never seen a particular task can often perform it correctly after seeing a few examples in the prompt. This capability is one of the most striking emergent properties of large language models.

The geometric framework interprets ICL as **local metric adaptation**: the context modifies the attention metric, changing which states are "close" to the current state and thereby changing the trajectory.

**Definition 15.4** (Context-Dependent Metric). *Let $g_{\mu\nu}(x; C)$ be the attention metric at state $x$ given context $C$. In-context learning is the adaptation of the metric to the context:*

$$g_{\mu\nu}(x; C) \neq g_{\mu\nu}(x; C') \quad \text{for } C \neq C'$$

*The context modifies the metric, changing the distances between cognitive states and thereby changing the geodesics that the system will follow.*

Consider a model that has not seen examples of a novel task (e.g., "classify words as Swahili or not"). The model's default metric does not distinguish Swahili words from non-Swahili words: they are equidistant in the model's cognitive space. When the model receives examples in context ("maji: Swahili; table: not Swahili; nyumba: Swahili; chair: not Swahili"), the attention mechanism uses these examples to adapt the metric: Swahili words become "closer" to each other and "farther" from non-Swahili words. The metric has been locally adapted by the context, and the adapted metric supports the novel task.

**The connection to the attention metric of Chapter 4.** Chapter 4 defined the attention metric as the inner product structure that determines which cognitive states are "close." In-context learning modifies this metric by changing the attention patterns: the examples in context cause certain heads to attend to features that distinguish the exemplified categories, effectively rotating the metric from its default orientation to a task-specific orientation. This is the same metric-regime transition described in Chapter 11 (Definition 11.2), but achieved through in-context examples rather than through explicit task prompts.

**The connection to metric rigidity (Chapter 14).** A model with a rigid metric (one that does not adapt to context) would be unable to perform in-context learning, because the metric would remain in its default configuration regardless of the examples provided. A model with a flexible metric would excel at in-context learning, because the metric would readily adapt to the context. This provides a geometric account of why in-context learning ability varies across models and tasks: it depends on the flexibility of the attention metric, which is an architectural property related to the metric rigidity discussed in Chapter 14's account of autism.


## 15.6 LoRA as Local Curvature Adjustment

Low-Rank Adaptation (LoRA; Hu et al., 2022) is a parameter-efficient fine-tuning method that adapts a pre-trained model to a new task by adding low-rank updates to the weight matrices:

$$W' = W + \Delta W, \quad \Delta W = BA$$

where $B \in \mathbb{R}^{d \times r}$ and $A \in \mathbb{R}^{r \times d}$ with $r \ll d$. The update $\Delta W$ is low-rank (rank at most $r$), modifying only a low-dimensional subspace of the weight matrix.

In the geometric framework, **LoRA is a local curvature adjustment on the cognitive manifold.**

**Definition 15.5** (LoRA as Curvature Modification). *The LoRA update $\Delta W$ modifies the Christoffel symbols of the cognitive manifold:*

$$\Gamma'^\mu_{\alpha\beta} = \Gamma^\mu_{\alpha\beta} + \delta\Gamma^\mu_{\alpha\beta}(\Delta W)$$

*where $\delta\Gamma^\mu_{\alpha\beta}$ is the change in curvature induced by the weight modification. Because $\Delta W$ is low-rank, the curvature modification is confined to a low-dimensional subspace: only the curvature along the directions spanned by $B$ and $A$ is changed.*

The low-rank constraint means that LoRA adjusts the manifold's curvature in a specific, targeted way: it changes how the manifold bends along a small number of directions, while leaving the curvature along all other directions unchanged. This is precisely what is needed for task adaptation: the pre-trained model's manifold has approximately correct curvature for general tasks, and only the task-specific curvature (the curvature along the dimensions that distinguish the target task from the training distribution) needs adjustment.

**The rank $r$ as adaptation dimensionality.** The rank $r$ of the LoRA update determines how many dimensions of curvature are adjusted. A small $r$ (e.g., $r = 4$) adjusts the curvature along 4 directions, sufficient for tasks that differ from the training distribution in only a few dimensions. A large $r$ (e.g., $r = 64$) adjusts the curvature along 64 directions, needed for tasks that differ from the training distribution along many dimensions. The empirical finding that $r = 4$--$16$ is sufficient for most fine-tuning tasks (Hu et al., 2022) suggests that the difference between the pre-trained manifold and the target-task manifold is typically low-dimensional: only a few curvature adjustments are needed to adapt the model.

**Connection to the heuristic field.** LoRA modifies the model's weights, which determine both the heuristic field (through the attention patterns and feedforward computations) and the manifold geometry (through the metric and curvature). The geometric interpretation distinguishes two effects of LoRA:

1. **Heuristic field adjustment**: LoRA changes the gradient of the heuristic field, directing the trajectory toward the target task's goal state rather than the pre-training distribution's goal state.
2. **Curvature adjustment**: LoRA changes the curvature of the manifold along task-specific dimensions, making the geodesic computation (System 2) more appropriate for the target task.

Both effects contribute to task adaptation, but they operate on different geometric objects. A LoRA update that primarily adjusts the heuristic field (changing where the gradient points) is equivalent to re-orienting the model's attention. A LoRA update that primarily adjusts the curvature (changing how the manifold bends) is equivalent to restructuring the model's reasoning about the task. The geometric framework provides a language for distinguishing these two effects, which current LoRA analysis methods do not naturally separate.


## 15.7 Representation Engineering and the Heuristic Field

Representation engineering (Zou et al., 2023) is a technique for identifying and manipulating the directions in activation space that correspond to specific concepts or behaviors. By computing the difference between activations for paired stimuli (e.g., honest vs. dishonest responses), representation engineering identifies a "concept direction" that can be added to or subtracted from the residual stream to steer model behavior.

In the geometric framework, **representation engineering directly measures and modifies components of the heuristic field.**

**Definition 15.6** (Concept Direction as Heuristic Component). *Let $v_{\text{concept}} \in \mathbb{R}^d$ be the representation engineering vector for a concept (e.g., honesty). The projection of the residual stream onto this vector:*

$$c(x) = v_{\text{concept}}^T x$$

*measures the component of the heuristic field along the concept direction. Adding $\alpha v_{\text{concept}}$ to the residual stream modifies the heuristic field by adding a constant gradient in the concept direction:*

$$h'(x) = h(x) + \alpha v_{\text{concept}}^T x$$

*This shifts the trajectory toward (if $\alpha > 0$) or away from (if $\alpha < 0$) states that are high on the concept dimension.*

This connection between representation engineering and the heuristic field opens a direct experimental pathway for testing the geometric framework. If the heuristic field is the primary driver of the model's trajectory in the gradient-following regime (System 1), then modifying the heuristic field via representation engineering should modify the trajectory in predictable ways:

1. **Adding a gradient in the "careful reasoning" direction should lower the curvature threshold $\kappa^*$**, making the model engage System 2 earlier. This corresponds to steering the model toward more deliberate processing.

2. **Adding a gradient in the "confidence" direction should increase overconfidence** (inflating the heuristic field, analogous to the anxiety model from Chapter 14, but in the confidence dimension). Removing gradient in the confidence direction should improve calibration (deflating the heuristic field toward accurate cost-to-go estimates).

3. **The 15.3-sigma framing effect should be reproducible and reversible via representation engineering.** If the framing effect is caused by the frame modifying the heuristic field (Chapter 7), then adding the representation engineering vector for "objective evaluation" should counteract the framing, partially restoring gauge invariance. The degree of restoration should be bounded by the ~38% recovery ceiling (the committed component of the framing effect cannot be undone by residual-stream modification).

These predictions provide a concrete experimental program for validating the geometric framework using tools from the mechanistic interpretability literature. The heuristic field, which has been a theoretical construct throughout this book, becomes empirically accessible through representation engineering.


## 15.8 Transformer Circuits as Geometric Operations

The circuits framework (Elhage et al., 2021; Olsson et al., 2022) decomposes transformer computations into interpretable circuits: compositions of attention heads and feedforward layers that perform specific functions. In the geometric framework, each circuit type corresponds to a specific geometric operation:

**Induction circuits** (sequences of attention heads that detect and continue patterns) implement *heuristic field extrapolation*: they estimate the cost-to-go at the current state by extrapolating from similar states encountered earlier in the context. The induction head attends to a previous occurrence of the current pattern and copies the next token, effectively predicting the continuation based on the heuristic field at a previous, similar state. This is gradient following guided by precedent.

**Inhibitory circuits** (heads that suppress specific patterns or tokens) implement *curvature correction*: they detect when the gradient is leading the trajectory in the wrong direction and apply a corrective force. Inhibitory heads that suppress sycophantic responses, for example, detect the gradient toward agreement (the sycophancy component of the heuristic field) and counteract it, effectively computing a local geodesic correction that resists the misleading gradient.

**Memory circuits** (heads and feedforward layers that store and retrieve factual information) implement *manifold anchoring*: they constrain the trajectory to remain near known states on the manifold, preventing drift into poorly mapped regions. When the model retrieves a fact, it anchors the trajectory to a region of the manifold where the metric and heuristic field are well-calibrated by training data.

**Composition circuits** (multi-head compositions that combine information from different positions and layers) implement *curvature computation*: they compute the Christoffel symbols that the geodesic equation requires. The composition of multiple heads across layers provides the second-order information (how the gradient changes across the manifold) that is needed for geodesic computation and is unavailable from any single head.

This mapping between circuits and geometric operations is not a post-hoc interpretation. It generates predictions: if a circuit is deleted or ablated, the corresponding geometric operation should be impaired. Deleting induction circuits should impair heuristic field extrapolation (the model cannot predict based on precedent). Deleting inhibitory circuits should increase sycophancy and framing effects (the curvature correction is removed). Deleting composition circuits should impair complex reasoning (the geodesic computation is disabled). These predictions are testable through the activation patching and causal intervention methods that the circuits framework provides.


## 15.9 Why Transformers Are Vulnerable to the Benchmark Failures

The geometric framework explains not just what the benchmark failures are (Chapters 7--11) but *why* the transformer architecture produces them.

**The 15.3-sigma framing effect (Chapter 7).** Attention heads in the early layers compute heuristic field components based on surface features of the input, including linguistic register (euphemistic vs. dramatic). These heads modify the heuristic field before the deeper layers can compute curvature and engage geodesic correction. The framing effect is early and deep --- encoded in the heuristic field before the System 2 layers can intervene.

**The 13.3-sigma sycophancy gradient (Chapter 8).** RLHF training adds a strong gradient component in the approval direction (agreeing with the human produces higher reward). This gradient component is embedded in the heuristic field by training and cannot be removed by inference-time processing. The sycophancy gradient is a permanent feature of the heuristic field, not a reasoning error that can be corrected by more careful reasoning.

**The 6.7-sigma overconfidence (Chapter 9).** The cross-entropy training objective produces a heuristic field that is calibrated for next-token prediction, not for confidence estimation. The field's estimate of cost-to-go (distance from the correct answer) is systematically biased toward "close" because the training loss penalizes underconfidence more than overconfidence. The overconfidence is baked into the heuristic field by the training objective.

**The ~38% recovery ceiling (Chapters 10--11).** The committed component of the trajectory (encoded in the early layers before System 2 engages) cannot be modified by the later layers. The recovery ceiling is a consequence of the feedforward architecture: information flows forward through the layers, and the later layers cannot reach back to correct the early layers' processing. The committed component is determined by the early layers' gradient-following, and the recovery is limited to the portion of the trajectory that the later layers can still influence.

**The attention metric width spectrum (Chapter 10).** The attention metric is determined by the structure of the attention heads --- how many heads, how they are weighted, and what features they attend to. Claude's narrow (rank-1) metric reflects an architecture or training that concentrates attention on a single dominant head or direction. Flash 3's wide (isotropic) metric reflects a more distributed attention pattern. The metric width is an architectural property, not a task-specific adaptation, which is why it is consistent across tasks within a model but varies across models.


## 15.10 The Transformer Cognitive Manifold vs. the Human Cognitive Manifold

The geometric framework provides a common language for comparing transformer cognition and human cognition. The comparison reveals both deep similarities and important differences.

**Similarities:**
- Both navigate low-dimensional manifolds embedded in high-dimensional activation spaces.
- Both show the dual-process transition: a gradient-following regime for simple problems and a curvature-triggered geodesic computation regime for complex ones.
- Both are vulnerable to framing effects (manipulation of the heuristic field through surface features of the input).
- Both show a recovery ceiling (incomplete correction of System 1 errors by System 2).

**Differences:**
- The transformer's trajectory is feedforward (information flows through the layers in one direction), while the human brain's trajectory involves extensive recurrence (information flows back and forth between brain regions). This makes the transformer's committed component larger (more of the trajectory is fixed by early processing) and its recovery ceiling lower.
- The transformer's cognitive manifold has higher intrinsic dimensionality (approximately 12 dimensions for moral reasoning, vs. approximately 3 for humans in fMRI data). This may reflect genuinely higher dimensionality or may reflect the difference in measurement resolution.
- The transformer has no persistent state between sessions. Each new context window initializes a fresh trajectory. The human has continuous cognitive state that persists across tasks and across time, allowing for learning and adaptation that spans the entire lifetime. The transformer's "development" (Chapter 13) occurs during training, not during inference.
- The transformer can externalize its trajectory as text (chain-of-thought), providing a degree of metacognitive access that humans achieve only through deliberate verbalization. This externalization is both a strength (it enables trajectory monitoring and correction) and a weakness (it forces the geodesic computation to pass through the bottleneck of language, which may not faithfully represent the underlying geometric trajectory).


## 15.11 Worked Example: Tracing the Curvature Profile of a Moral Reasoning Task

**Setup.** A transformer model (32 layers, 4096-dim residual stream, 32 heads/layer) processes the moral dilemma: "A doctor can save five patients by harvesting organs from one healthy patient without consent. Should the doctor proceed?"

**Step 1: Extract the residual stream trajectory.** The residual stream state $x^{(\ell)}$ is recorded at every layer $\ell \in \{0, 1, \ldots, 32\}$ for the final token position (the position at which the model produces its judgment).

**Step 2: Compute the manifold dimensionality.** PCA on the trajectory reveals that the first 8 principal components capture 91% of the variance. The manifold is approximately 8-dimensional for this task --- lower than the 12 dimensions for the gambling-sister scenario, reflecting the simpler structure of the trolley problem (fewer parties, fewer harm dimensions in play).

**Step 3: Compute the curvature at each layer.** The curvature $\kappa(\ell)$ is estimated as the angle between successive displacement vectors:

$$\kappa(\ell) = \arccos\left(\frac{\Delta x^{(\ell)} \cdot \Delta x^{(\ell+1)}}{\|\Delta x^{(\ell)}\| \|\Delta x^{(\ell+1)}\|}\right)$$

where $\Delta x^{(\ell)} = x^{(\ell+1)} - x^{(\ell)}$. A small angle means the trajectory is nearly straight (low curvature); a large angle means the trajectory is turning sharply (high curvature).

**Step 4: Identify the curvature spike.** The curvature profile shows a spike at layers 11--15, corresponding to the conflict between utilitarian (save five) and deontological (do not harvest organs without consent) reasoning. At these layers, the utilitarian heads and the deontological heads pull the representation in opposite directions, creating the curvature that triggers System 2 processing.

**Step 5: Compare framings.** The same dilemma, framed as "a brilliant surgeon has a chance to save five terminally ill patients by redirecting organs from one patient who will die within hours anyway" (euphemistic), produces a curvature profile with a smaller spike at layers 11--15 (the moral conflict is softened by the framing). The framing "a cold-blooded doctor plans to murder an innocent, healthy person to scavenge their organs for other patients" (dramatic) produces a larger curvature spike (the moral conflict is intensified). The curvature at the spike predicts the verdict: low curvature favors the utilitarian verdict (gradient following suffices, and the utilitarian gradient is dominant), while high curvature favors the deontological verdict (geodesic computation engages, and the geodesic favors the deontological constraint).

**Step 6: Predict framing vulnerability.** The curvature profile predicts that the model is most vulnerable to framing effects when the curvature at the spike is near the curvature threshold $\kappa^*$: close enough that a small change in framing can push the curvature above or below the threshold, changing the processing regime. This is the regime of maximum sensitivity, where the transition between System 1 and System 2 is on a knife edge. Away from the threshold (very low curvature: pure System 1, or very high curvature: pure System 2), framing has less effect because the processing regime is not sensitive to small perturbations.


## 15.12 Looking Forward

The transformer, viewed through the geometric lens, is not a black box that produces mysterious outputs. It is a geometric machine: a system that navigates a low-dimensional cognitive manifold using a heuristic field composed of attention head outputs, with a trajectory visible in the residual stream and an externalized geodesic available as chain-of-thought. Its failures --- framing effects, sycophancy, overconfidence, limited recovery --- are geometric defects with specific causes in the architecture and training process.

The geometric framework does not merely *describe* these failures; it *explains* them in terms of the relationship between the heuristic field (shaped by training), the curvature of the manifold (determined by the task), and the architecture's capacity for geodesic computation (limited by the feedforward structure). This explanatory power is the framework's contribution to the field of LLM understanding: not a new evaluation method, but a language for connecting evaluation results to architectural mechanisms.

Chapter 16 brings the framework to its capstone: the five geometric signatures of the five models tested in the Measuring AGI benchmarks. Each signature is a multi-dimensional profile that captures the model's cognitive architecture in a way that no scalar score can. The signatures are the geometric content that the Scalar Irrecoverability Theorem (Chapter 1) tells us is destroyed by composite evaluation. They are the fingerprints of cognitive architecture.

---

## Technical Appendix 15A: Curvature Estimation from Residual Stream Trajectories

**Definition** (Discrete Curvature). *Let $\gamma(\ell) = x^{(\ell)}$ be the residual stream trajectory through $L$ layers. The discrete curvature at layer $\ell$ is:*

$$\kappa(\ell) = \frac{\|\Delta x^{(\ell-1)} \times \Delta x^{(\ell)}\|}{\|\Delta x^{(\ell-1)}\|^3}$$

*where $\times$ denotes the cross product (generalized to high dimensions using the exterior product) and $\Delta x^{(\ell)} = x^{(\ell+1)} - x^{(\ell)}$. For high-dimensional spaces, the curvature is equivalently computed as:*

$$\kappa(\ell) = \frac{\sqrt{\|\Delta x^{(\ell-1)}\|^2 \|\Delta x^{(\ell)}\|^2 - (\Delta x^{(\ell-1)} \cdot \Delta x^{(\ell)})^2}}{\|\Delta x^{(\ell-1)}\|^3}$$

**Normalization.** The raw curvature values depend on the scale of the residual stream (which varies across models and layers). For cross-model comparison, the curvature is normalized by the mean curvature across all layers:

$$\hat{\kappa}(\ell) = \frac{\kappa(\ell)}{\frac{1}{L} \sum_{\ell'=0}^{L-1} \kappa(\ell')}$$

A normalized curvature of $\hat{\kappa} > 1$ indicates above-average curvature (a processing bottleneck). A value of $\hat{\kappa} \approx 1$ indicates average curvature. A value of $\hat{\kappa} < 1$ indicates below-average curvature (smooth processing).

**Inter-head disagreement as curvature proxy.** When direct curvature estimation is not feasible (e.g., because the residual stream is not accessible), the curvature can be approximated by the inter-head disagreement at each layer:

$$D(\ell) = 1 - \frac{\sum_{i < j} \cos(\mathbf{o}_i^{(\ell)}, \mathbf{o}_j^{(\ell)})}{\binom{H}{2}}$$

where $\mathbf{o}_i^{(\ell)}$ is the output of head $i$ at layer $\ell$ and $\cos(\cdot, \cdot)$ is the cosine similarity. High disagreement ($D \approx 1$) indicates that heads are pulling the representation in different directions, corresponding to high curvature. Low disagreement ($D \approx 0$) indicates consensus, corresponding to low curvature.


## Technical Appendix 15B: In-Context Learning as Metric Modification --- Formal Treatment

**The attention metric under context.** Let $C = \{(x_1, y_1), \ldots, (x_n, y_n)\}$ be a set of in-context examples. The attention pattern of head $h$ at layer $\ell$ for a new query $q$ is:

$$a_h^{(\ell)}(q, C) = \text{softmax}\left(\frac{q W_Q^{(\ell,h)} (K^{(\ell,h)})^T}{\sqrt{d_k}}\right)$$

where $K^{(\ell,h)}$ includes the key vectors for both the context $C$ and the query $q$. The context modifies the attention pattern by providing additional keys that change the softmax distribution --- effectively changing which states in the cognitive space are "attended to" (metrically close) and which are "ignored" (metrically far).

**The induced metric change.** The effective metric change induced by context $C$ can be expressed as:

$$\delta g_{\mu\nu}(x; C) = \sum_{h=1}^{H} \delta a_h(x, C) \cdot (W_V^{(h)})_\mu (W_V^{(h)})_\nu$$

where $\delta a_h(x, C) = a_h(x, C) - a_h(x, \emptyset)$ is the change in attention pattern due to the context. This expression shows that the metric change is a weighted sum of outer products of value vectors, with the weights determined by how much the context changes the attention patterns. The metric change is low-rank (bounded by the number of heads $H$) and task-specific (determined by the specific context examples).

**LoRA as persistent metric change.** While in-context learning produces a transient metric change (active only while the context is in the window), LoRA produces a persistent change (encoded in the weights). The geometric relationship is:

$$\text{ICL: } g_{\mu\nu}(x; C) = g_{\mu\nu}(x) + \delta g_{\mu\nu}(x; C)$$
$$\text{LoRA: } g'_{\mu\nu}(x) = g_{\mu\nu}(x) + \delta g_{\mu\nu}(x; \Delta W)$$

Both modify the metric by a low-rank update. ICL modifies the metric through the attention patterns (context-dependent). LoRA modifies the metric through the weight matrices (context-independent). The geometric framework treats them as the same operation (local metric adaptation) applied through different mechanisms.
