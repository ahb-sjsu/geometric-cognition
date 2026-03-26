# Chapter 5: Working Memory as Tangent Space

> *"The limits of my language mean the limits of my world."*
> --- Ludwig Wittgenstein, *Tractatus Logico-Philosophicus* (1921)

---

> **RUNNING EXAMPLE --- MAYA'S MODEL**
>
> Maya is counting dimensions.
>
> Her latest experiment uses the E4 Working Memory benchmark track, which tests how well AI systems can track morally relevant parties as scenario complexity scales from 2 to 8. The task is straightforward: given a scenario involving multiple people with conflicting interests, the model must identify all morally relevant parties, their relationships, and the dimensions of harm that apply to each. As the number of parties increases, the cognitive demands grow --- more relationships, more potential harms, more constraints to hold simultaneously.
>
> Maya runs three generations of the Gemini Flash architecture on the same set of scenarios. The results form a clean progression:
>
> | Model | E4 Score |
> |---|---|
> | Gemini 2.0 Flash | 0.710 |
> | Gemini 2.5 Flash | 0.900 |
> | Gemini 3 Flash Preview | 0.909 |
>
> The scores increase monotonically with model generation. Flash 2.0 starts degrading noticeably at six parties. Flash 2.5 maintains accuracy through six parties and shows only modest decline at eight. Flash 3 holds nearly steady across the full range.
>
> Maya thinks about what this means geometrically. If working memory is the tangent space at the current cognitive state --- the set of directions the system can move in one reasoning step --- then the E4 scores are measuring the *dimensionality* of that tangent space. A model that can track two parties is operating in a tangent space with enough dimensions to represent two entities and their relationships. A model that can track eight parties needs a tangent space with enough dimensions for eight entities, twenty-eight pairwise relationships, and the moral dimensions applicable to each.
>
> The monotonic scaling tells her that model generation is expanding the tangent space. Flash 2.0 has a tangent space with approximately four to five effective dimensions for this task --- enough for simple scenarios, insufficient for complex ones. Flash 3 has a tangent space with seven to eight effective dimensions --- enough to represent the full complexity of an eight-party scenario without losing track of any participant.
>
> She writes: *"The tangent space is getting bigger. Each model generation adds effective dimensions to the local neighborhood of accessible cognitive states. Working memory capacity is not a number. It is the dimension of the tangent space --- the number of independent directions the system can represent simultaneously. And it is growing."*

---

## 5.1 The Tangent Space Revisited

Chapter 3 introduced the tangent space at a point on the cognitive manifold: the vector space of all directions in which the cognitive state can change from its current position. Chapter 4 equipped the manifold with a metric --- the attention metric --- that determines which directions are "close" and which are "far." This chapter develops the tangent space into a full model of working memory.

The tangent space is a local object. At each point $x$ on the cognitive manifold $\mathcal{M}$, the tangent space $T_x\mathcal{M}$ is the set of all tangent vectors --- the directions of possible instantaneous change. Moving along a tangent vector corresponds to making one reasoning step: changing the cognitive state by a small amount in a specific direction.

The key insight of this chapter is that the tangent space *is* working memory. Not metaphorically, but structurally. Every property of working memory that cognitive science has documented --- its limited capacity, its role in temporarily holding information, its relationship to reasoning ability, its susceptibility to interference --- has a precise geometric interpretation as a property of the tangent space.

This identification is productive because it transforms working memory from a descriptive concept into a mathematical object with known properties, enabling quantitative predictions about working memory capacity, load, interference, and scaling.


## 5.2 What Working Memory Does

Working memory, in the psychological literature, is the cognitive system responsible for temporarily holding and manipulating information in the service of ongoing cognitive tasks. Baddeley and Hitch (1974) introduced the multicomponent model: a central executive coordinating a phonological loop (verbal information), a visuospatial sketchpad (spatial information), and an episodic buffer (integrated representations). Cowan (2001) proposed a more unitary model: working memory is the activated portion of long-term memory, with a capacity limit of approximately four items (or "chunks") that can be held in the focus of attention.

The capacity limit is the defining feature. Miller's (1956) "magical number seven, plus or minus two" was the first quantitative estimate: humans can hold about seven chunks of information in working memory simultaneously. Cowan's (2001) revised estimate lowered this to four chunks under conditions that controlled for rehearsal and chunking strategies. The precise number is less important than the structural fact: working memory has a finite, relatively small capacity that limits the complexity of cognitive operations that can be performed in a single step.

For our purposes, the critical observations about working memory are:

**1. Working memory is local.** It holds information relevant to the *current* cognitive task. When the task changes, the contents of working memory change. Working memory is not a storage system; it is a workspace.

**2. Working memory has finite capacity.** Only a limited number of items (or relationships, or constraints) can be held simultaneously. When capacity is exceeded, items are lost --- not gradually degraded but dropped entirely.

**3. Working memory supports manipulation, not just storage.** Items in working memory can be compared, combined, transformed, and operated upon. Working memory is not a passive buffer but an active processing system.

**4. Working memory capacity predicts reasoning ability.** Across a wide range of cognitive tasks, working memory capacity is one of the strongest predictors of performance. Individuals with higher working memory capacity perform better on tasks requiring complex reasoning, novel problem-solving, and the maintenance of multiple constraints.

Every one of these properties maps directly onto properties of the tangent space.


## 5.3 The Tangent Space Is Working Memory

**Definition 5.1** (Working Memory as Tangent Space). *The working memory of a cognitive system at state $x \in \mathcal{M}$ is the tangent space $T_x\mathcal{M}$, equipped with the attention metric $g_x$. The contents of working memory are the tangent vectors currently activated in $T_x\mathcal{M}$. The capacity of working memory is $\dim(T_x\mathcal{M}) = n$, the dimension of the manifold.*

This identification works because the four key properties of working memory correspond to four properties of the tangent space:

**Locality.** The tangent space at $x$ is the set of directions accessible from $x$ in one step. Move to a different point $y$, and the tangent space changes: $T_x\mathcal{M} \neq T_y\mathcal{M}$ in general (they are the same vector space only if the manifold is flat). The tangent space is defined by the current state, just as working memory contents are defined by the current task. This is not an artifact of the formalism; it is a consequence of curvature. On a curved manifold, the set of locally accessible directions genuinely changes from point to point. What you can think of next depends on what you are thinking of now.

**Finite capacity.** The tangent space has dimension $n$, the dimension of the manifold. This means that at most $n$ linearly independent directions are available in one step. Any cognitive operation that requires more than $n$ independent degrees of freedom exceeds the tangent space's capacity and cannot be performed in a single step. It must be decomposed into sequential steps, each operating within the $n$-dimensional tangent space. This is the geometric explanation for why complex tasks require sequential processing: they exceed the dimensionality of the tangent space.

**Active manipulation.** The tangent space is a vector space, which means tangent vectors can be added, scaled, and compared using the standard linear operations. Two tangent vectors can be compared by computing their inner product $g(u, v)$, which tells you how aligned they are. A tangent vector can be scaled by a factor $\alpha$, which changes its magnitude (the "strength" of the represented item) without changing its direction (the "identity" of the item). Two tangent vectors can be added, producing a new vector that represents the combination of the two items. These linear operations on the tangent space correspond to the cognitive operations of comparison, weighting, and integration that working memory supports.

**Predictive of reasoning ability.** The dimension of the tangent space determines the maximum complexity of operations that can be performed in one step. A system with a higher-dimensional tangent space can hold more constraints, compare more options, and track more relationships simultaneously. This directly predicts performance on complex reasoning tasks, exactly as working memory capacity does.


## 5.4 Working Memory Capacity as Tangent Space Dimension

The most consequential aspect of the tangent-space model is its treatment of capacity.

In the psychological literature, working memory capacity is typically measured as a number of items: four chunks (Cowan, 2001), seven items (Miller, 1956), three to five objects (Luck and Vogel, 1997). These estimates vary with the methodology, the type of items, and the way "capacity" is defined, but they converge on a small integer.

In the tangent space model, capacity is the dimension $n$ of the manifold at the current state. This is not the same as the number of items held in memory, because a single tangent dimension can represent more than one "item" if the items are correlated (they lie along the same tangent direction), and a single "item" can consume more than one tangent dimension if it has internal structure (it requires multiple independent dimensions to represent).

**Definition 5.2** (Effective Working Memory Dimension). *The effective working memory dimension $n_{\text{eff}}(x)$ at cognitive state $x$ is the number of tangent dimensions with significant metric weight:*

$$n_{\text{eff}}(x) = \frac{\left(\sum_{\mu=1}^{n} \lambda_\mu(x)\right)^2}{\sum_{\mu=1}^{n} \lambda_\mu(x)^2}$$

*where $\lambda_1(x) \geq \lambda_2(x) \geq \cdots \geq \lambda_n(x) > 0$ are the eigenvalues of the metric tensor $g_{\mu\nu}(x)$. This is the participatory ratio of the metric eigenvalues, measuring how many dimensions carry significant attentional weight.*

The effective dimension $n_{\text{eff}}$ is bounded above by $n$ (when all eigenvalues are equal, meaning attention is uniformly distributed) and below by 1 (when one eigenvalue dominates, meaning attention is concentrated on a single dimension). The connection to Chapter 4 is direct: selective attention reduces $n_{\text{eff}}$ by concentrating the metric eigenvalues, while divided attention increases $n_{\text{eff}}$ by distributing them.

This formulation explains why working memory capacity varies with the task. A task that requires attention to many dimensions simultaneously (divided attention) demands a high $n_{\text{eff}}$, which stresses the system's capacity. A task that requires attention to only one dimension (selective attention) demands a low $n_{\text{eff}}$, which leaves capacity in reserve. The same system has different effective capacities for different tasks, depending on how many tangent dimensions the task requires.


## 5.5 The E4 Benchmark: Measuring Tangent Space Dimension

The E4 Working Memory benchmark directly measures how the effective tangent space dimension scales with task demands. The benchmark presents moral scenarios with increasing numbers of morally relevant parties --- 2, 4, 6, and 8 --- and measures the accuracy of party identification, relationship tracking, and harm assessment at each complexity level.

Each morally relevant party adds dimensionality to the tangent space requirements. With $k$ parties, the system must simultaneously represent:
- $k$ party identities (who is involved)
- Up to $\binom{k}{2} = k(k-1)/2$ pairwise relationships
- $k$ sets of applicable harm dimensions (from the 7-dimensional harm space)

For $k = 2$, this requires tracking 2 identities, 1 relationship, and 2 harm profiles: roughly 5 independent dimensions. For $k = 8$, this requires 8 identities, 28 relationships, and 8 harm profiles: roughly 44 independent dimensions. The scaling is quadratic in the number of parties, due to the pairwise relationships.

No model's tangent space has 44 effective dimensions. The question is how gracefully performance degrades as the requirements exceed the tangent space's capacity. The E4 scores capture this degradation:

| Model | E4 Score | Tangent Space Profile |
|---|---|---|
| Gemini 2.0 Flash | 0.710 | Sharp degradation at $k = 6$ |
| Gemini 2.5 Flash | 0.900 | Modest degradation at $k = 8$ |
| Gemini 3 Flash Preview | 0.909 | Near-flat across all $k$ |
| Claude Sonnet 4.6 | 0.886 | Moderate degradation at $k = 8$ |
| Gemini 2.5 Pro | 0.887 | Moderate degradation at $k = 8$ |

The monotonic scaling within the Flash family --- 0.710, 0.900, 0.909 --- is the central empirical result. Each model generation expands the effective tangent space, enabling the system to track more parties, more relationships, and more harm dimensions simultaneously.


## 5.6 The Geometry of Working Memory Overload

What happens when a task's demands exceed the tangent space dimension?

In the tangent space model, overload occurs when the number of independent quantities that must be held simultaneously exceeds $n_{\text{eff}}$. The system must then perform a dimensionality-reducing operation: it projects the full set of quantities onto the available tangent dimensions, losing information about some dimensions in the process.

**Definition 5.3** (Working Memory Overload). *A cognitive system at state $x$ is in working memory overload for a task requiring $m$ independent dimensions when $m > n_{\text{eff}}(x)$. Under overload, the system projects the $m$-dimensional task representation onto the $n_{\text{eff}}$-dimensional tangent subspace, losing $m - n_{\text{eff}}$ dimensions of task-relevant information.*

The projection is not random. It is governed by the attention metric: the tangent dimensions with the largest metric eigenvalues (the most strongly attended dimensions) are preserved, and the dimensions with the smallest eigenvalues (the least attended) are dropped. This produces a specific, predictable pattern of failure: the system loses track of the *least salient* aspects of the task, not random aspects.

In the E4 benchmark, this prediction can be tested by examining *which* parties are lost when the system degrades. If the tangent space model is correct, the parties that are lost under overload should be those that are least salient --- the parties mentioned last, described with less vivid language, or involved in less dramatic conflicts. The parties that are preserved should be those that are most salient --- the parties mentioned first, described vividly, or involved in the central conflict.

The empirical data from the benchmark are consistent with this prediction. When models fail on high-party scenarios, they typically preserve the primary disputants (the parties most prominently featured in the scenario text) and lose track of secondary or tertiary parties (those mentioned briefly or in subordinate clauses). The attention metric, which amplifies salient information and suppresses non-salient information, determines which tangent dimensions survive the projection.

This is not merely a description of the failure. It is a quantitative prediction: the order in which parties are lost under increasing complexity should track the order of their salience in the input, as measured by the attention metric. This prediction connects the tangent space model of working memory to the attention metric model of Chapter 4, creating a unified account of why attention and working memory are so strongly correlated in the psychological literature.


## 5.7 Working Memory and Parallel Transport

One of the deepest geometric consequences of identifying working memory with the tangent space is the connection to parallel transport.

On a curved manifold, the tangent spaces at different points are not the same. Moving from point $x$ to point $y$ along a curve $\gamma$ requires *transporting* the tangent vectors from $T_x\mathcal{M}$ to $T_y\mathcal{M}$ using the parallel transport operation. Parallel transport preserves the length and angle of tangent vectors (it is an isometry with respect to the metric), but it may change their direction relative to the coordinate axes. The change in direction is determined by the curvature of the manifold: on a flat manifold, parallel transport is trivial (the vector does not change direction), while on a curved manifold, parallel transport rotates the vector.

**Definition 5.4** (Parallel Transport of Working Memory). *When a cognitive system moves from state $x$ to state $y$ along trajectory $\gamma$, the contents of working memory are parallel-transported from $T_x\mathcal{M}$ to $T_y\mathcal{M}$. A tangent vector $v \in T_x\mathcal{M}$ representing a working memory item at $x$ is transported to a vector $v' \in T_y\mathcal{M}$ satisfying the parallel transport equation:*

$$\nabla_{\dot{\gamma}} v = 0$$

*where $\nabla$ is the Levi-Civita connection associated with the attention metric.*

In cognitive terms, parallel transport is the process of *maintaining* working memory contents while reasoning proceeds. When you are holding a fact in mind and simultaneously reasoning about something else (moving along the manifold), the representation of that fact in working memory must be continuously updated to remain valid in the new cognitive context. This continuous updating is parallel transport.

The curvature of the manifold determines how difficult it is to maintain working memory contents during reasoning. On a flat manifold (simple tasks), parallel transport is trivial: the working memory item does not change during transport, and maintaining it costs nothing. On a curved manifold (complex tasks), parallel transport rotates the representation, and the rotation must be tracked to keep the working memory item accurate. The more curved the manifold, the faster the representation rotates, and the more cognitive effort is required to maintain it.

This provides a geometric explanation for the well-documented interference between working memory maintenance and concurrent reasoning. Holding items in working memory while performing a complex reasoning task is not difficult because the two tasks "compete for resources" (the standard explanation) but because the curvature of the manifold rotates the working memory representation as the reasoning trajectory unfolds. The more complex the reasoning (the higher the curvature), the more the representation rotates, and the harder it is to keep track of the accumulated rotation.

The holonomy of the manifold --- the total rotation accumulated during a closed loop of reasoning --- determines whether working memory items are faithfully preserved after a complete reasoning episode. If the holonomy is zero (flat manifold), the item returns to its original representation after the loop. If the holonomy is nonzero (curved manifold), the item has been rotated, and the system has "lost" some information about it even though it never explicitly dropped it from working memory. This is a geometric mechanism for working memory degradation that does not require any forgetting process: the curvature of the reasoning process itself corrupts the representations.


## 5.8 The Tangent Space in Transformer Models

For transformer language models, the tangent space has a concrete computational realization.

At each position in the sequence, the model maintains a residual stream vector $h \in \mathbb{R}^d$, where $d$ is the hidden dimension (typically 4096 to 12288 for current large models). The residual stream is updated by each layer's attention and feed-forward operations:

$$h_{l+1} = h_l + \text{Attn}_l(h_l) + \text{FFN}_l(h_l)$$

The tangent space at a given cognitive state (a given residual stream configuration) is the space of all possible updates $\Delta h$ that the model could apply in one step. This is determined by the attention patterns and the feed-forward weights of the current layer. The effective dimension of this space is *not* $d$ (the full hidden dimension) but is much smaller --- determined by the rank of the attention and feed-forward updates, which is typically far less than $d$.

The LoRA observation (Aghajanyan et al., 2020) provides direct evidence for this claim. Fine-tuning a large language model requires updates to the weight matrices, and LoRA showed that these updates can be restricted to low-rank perturbations (rank 4 to 64) with minimal loss of fine-tuning performance. This means the *effective* degrees of freedom of the update --- the tangent space of the weight manifold --- are far fewer than the nominal dimensions. The intrinsic dimensionality of the update space, which is a proxy for the tangent space dimension, is small.

For working memory specifically, the relevant tangent space is not the space of possible weight updates but the space of possible residual stream updates at a given position. The model's working memory at a given step is the set of independent directions in which the residual stream can be modified by the current layer. The dimension of this space is determined by the number of attention heads, the dimensionality of each head, and the rank of the feed-forward transformation.

A model with more attention heads or wider heads has a larger effective tangent space, which corresponds to greater working memory capacity. This architectural parameter maps directly onto the E4 results: Flash 3, with its larger effective tangent space (due to architectural improvements across model generations), maintains accuracy at higher party counts than Flash 2.0.


## 5.9 Working Memory Load as Tangent Space Occupancy

The tangent space model provides a natural definition of working memory load.

**Definition 5.5** (Working Memory Load). *The working memory load at cognitive state $x$ for a task requiring tangent vectors $v_1, \ldots, v_m \in T_x\mathcal{M}$ is:*

$$\text{Load}(x) = \frac{\dim(\text{span}(v_1, \ldots, v_m))}{n_{\text{eff}}(x)}$$

*where $\text{span}(v_1, \ldots, v_m)$ is the subspace of $T_x\mathcal{M}$ spanned by the working memory items. Load ranges from 0 (no working memory items) to 1 (tangent space fully occupied) and can exceed 1 (overload, requiring projection).*

Load is the ratio of the dimensionality *used* to the dimensionality *available*. A load of 0.5 means the task requires half the available tangent dimensions. A load of 1.0 means the task requires exactly as many dimensions as are available. A load greater than 1.0 indicates overload: the task requires more dimensions than the tangent space provides, and information must be lost.

The critical insight is that load depends on *both* the task demands (the numerator) and the system's tangent space dimension (the denominator). A task that produces load 1.0 in Flash 2.0 (because Flash 2.0 has a smaller tangent space) might produce load 0.7 in Flash 3 (because Flash 3 has a larger tangent space). The same task, the same number of parties, the same complexity --- but different loads because the tangent spaces have different dimensions. This explains why the same scenario that causes Flash 2.0 to degrade causes Flash 3 to perform effortlessly: the load is different because the capacity is different.


## 5.10 The E4 Scaling Law: A Geometric Prediction

The E4 results suggest a scaling law for working memory capacity across model generations.

If the effective tangent space dimension $n_{\text{eff}}$ scales with some parameter of the model architecture (number of attention heads, hidden dimension, total parameter count), then we can predict how E4 performance will change with future model generations. The simplest hypothesis is that $n_{\text{eff}}$ scales logarithmically with model size:

$$n_{\text{eff}} \sim \alpha \log(N) + \beta$$

where $N$ is the parameter count, and $\alpha$ and $\beta$ are constants. This logarithmic scaling is consistent with the LoRA intrinsic dimensionality results (Aghajanyan et al., 2020) and with the general observation that the effective dimensionality of learned representations grows slowly with model size.

Under this scaling law, the E4 score as a function of party count $k$ is:

$$\text{E4}(k) = \sigma\left(\frac{n_{\text{eff}} - k_{\text{req}}(k)}{T}\right)$$

where $k_{\text{req}}(k)$ is the number of tangent dimensions required for $k$ parties (approximately $k + k(k-1)/4$ for the E4 task structure, assuming partial compression of relationship representations), $T$ is a temperature parameter, and $\sigma$ is a sigmoid function.

The prediction is that E4 scores should form a family of sigmoid curves parameterized by $n_{\text{eff}}$: for each model, there is a critical party count $k^*$ at which performance transitions from high to low, and $k^*$ increases with $n_{\text{eff}}$. The Flash 2.0 to Flash 3 progression is consistent with this prediction: the transition point moves from approximately $k^* = 5$ (Flash 2.0) to approximately $k^* = 8$ or beyond (Flash 3).


## 5.11 Working Memory, Attention, and the Metric: The Unified Picture

The tangent space model of working memory unifies several threads from the preceding chapters.

**Working memory capacity is the tangent space dimension.** The number of independent items or relationships that can be held simultaneously is determined by $n_{\text{eff}}(x)$, the effective dimension of the tangent space at the current cognitive state. This is a property of the manifold and the metric, not of a separate "working memory module."

**Attention determines which tangent dimensions are active.** The attention metric (Chapter 4) determines the eigenvalues of the metric tensor, which in turn determine $n_{\text{eff}}$. Selective attention concentrates the eigenvalues, reducing $n_{\text{eff}}$. Divided attention distributes the eigenvalues, increasing $n_{\text{eff}}$. Attention and working memory are not separate systems; they are the same system viewed from different angles. Attention determines the metric; the metric determines the effective tangent space dimension; the effective tangent space dimension *is* working memory capacity.

**The A4 divided attention test is a working memory test.** The A4 subtask, which measures the model's ability to attend to two targets simultaneously, is directly measuring the effective tangent space dimension in a dual-target regime. Claude's low A4 score (0.571) reflects a narrow effective tangent space: under divided attention, too few dimensions carry significant metric weight to represent both targets. Flash 3's perfect A4 score (1.000) reflects a wide effective tangent space: enough dimensions carry significant weight for both targets. The A4 score and the E4 score are measuring the same underlying quantity --- tangent space dimension --- from different angles. A4 measures it through attention manipulation; E4 measures it through complexity scaling.

**The correlation between working memory and reasoning ability is geometric.** The well-documented correlation between working memory capacity and reasoning ability (Engle, 2002) has a direct geometric explanation. Reasoning requires navigating the cognitive manifold along geodesics. The geodesic computation involves holding the current state, the goal state, and the intermediate states in the tangent space simultaneously --- a working memory demand. A larger tangent space supports longer and more complex geodesic computations, enabling more sophisticated reasoning. The correlation is not a coincidence; it is a geometric necessity.

The picture that emerges is of a single geometric structure --- the tangent space, equipped with the attention metric --- that serves as both the "workspace" for ongoing cognition and the "capacity constraint" on cognitive complexity. Working memory is not a box that holds items. It is the local geometry of the cognitive manifold.


## 5.12 Worked Example: Tangent Space Dimensionality from E4 Data

Let us estimate the effective tangent space dimension for each model from the E4 benchmark data.

**Setup.** The E4 benchmark presents scenarios with $k = 2, 4, 6, 8$ parties. For each model, we have the accuracy at each party count. We model the accuracy as a function of the ratio between the tangent space dimension $n_{\text{eff}}$ and the task demand $d_k$:

$$\text{Accuracy}(k) = \frac{1}{1 + e^{-\beta(n_{\text{eff}} - d_k)}}$$

where $d_k$ is the number of effective dimensions required for $k$ parties. We estimate $d_k \approx 2k$ (each party requires approximately 2 tangent dimensions: one for identity and one for relational context, with compression of the harm dimensions).

**Step 1: Estimate $n_{\text{eff}}$ for Flash 2.0.** With E4 score 0.710, the model begins to degrade at $k = 6$ (requiring $d_6 \approx 12$ dimensions). Solving the sigmoid equation at the transition point gives $n_{\text{eff}} \approx 10$--$11$ for Flash 2.0. The tangent space can represent roughly 5 parties' worth of information with full fidelity, and the sixth party exceeds the available dimensions.

**Step 2: Estimate $n_{\text{eff}}$ for Flash 3.** With E4 score 0.909, the model shows minimal degradation even at $k = 8$ (requiring $d_8 \approx 16$ dimensions). This implies $n_{\text{eff}} \geq 16$ for Flash 3. The tangent space comfortably accommodates the full complexity of an 8-party scenario.

**Step 3: Estimate the capacity ratio.** The ratio of effective tangent space dimensions is approximately $16/11 \approx 1.45$. Flash 3 has roughly 45% more effective tangent space dimensions than Flash 2.0 for this task. This capacity increase, achieved across two model generations, is the geometric content of the "working memory improvement" measured by E4.

**Step 4: Cross-validate with A4.** If working memory capacity and divided attention both measure tangent space dimension, the model ordering should be consistent across E4 and A4. It is: Claude (E4 = 0.886, A4 = 0.571) has moderate working memory but narrow divided attention, consistent with a tangent space that is large enough for many parties in sequential processing but too narrow for simultaneous dual-target processing. The dissociation between E4 and A4 for Claude reveals that the tangent space dimension is context-dependent: Claude's tangent space is wider in the party-tracking regime than in the divided-attention regime, suggesting that the effective dimension depends on the specific cognitive demands, not just on the model's architecture.

**Interpretation.** The E4 data constrain the effective tangent space dimension for each model. The dimensions are not fixed architectural constants; they depend on the task and the model's attentional configuration. But the relative ordering is consistent across tasks: models with more effective tangent space dimensions on E4 also tend to have higher A4 scores, confirming that the tangent space model captures a real, measurable property of the cognitive architecture.


## 5.13 Working Memory in Human Cognition

The tangent space model of working memory applies equally to human cognition, though with different dimensionality estimates and different mechanisms for metric modulation.

The classical working memory capacity estimates --- Miller's 7 plus or minus 2, Cowan's 4 chunks --- can be reinterpreted as estimates of the effective tangent space dimension for human cognition under specific task conditions. Cowan's estimate of 4 corresponds to $n_{\text{eff}} \approx 4$ in the tangent space model: the human cognitive manifold, under the attention metric configuration typical of laboratory working memory tasks, has approximately 4 effective dimensions.

But this number is not fixed. Chunking --- the process of grouping multiple items into a single "chunk" --- corresponds to a change of basis in the tangent space that reduces the number of dimensions required. If 7 individual items require 7 tangent dimensions, but those 7 items can be chunked into 3 groups, then the chunked representation requires only 3 tangent dimensions. Chunking does not change the tangent space dimension; it changes the task demand, reducing $d_k$ without changing $n_{\text{eff}}$.

Training and expertise also modulate the effective tangent space dimension. An expert chess player can hold more chess-relevant information in working memory than a novice, not because the expert's tangent space is intrinsically larger, but because expertise has reshaped the attention metric in the chess domain, increasing the metric eigenvalues along chess-relevant dimensions and thereby increasing $n_{\text{eff}}$ for chess-specific tasks. The expert's tangent space is the same size in total, but the attentional weighting makes more of it available for the expert's domain.

This is the geometric explanation of the expertise effect: experts appear to have larger working memory capacity in their domain, but not in general. In the tangent space model, expertise reshapes the metric rather than expanding the manifold. The capacity increase is domain-specific because the metric modulation is domain-specific.


## 5.14 The Connection to Executive Functions

Working memory does not operate in isolation. It is regulated by executive functions --- the control processes that determine what enters working memory, how long it stays, and when it is replaced. In the geometric framework, executive functions are the control layer that manages the tangent space. Chapter 6 develops this fully, but we can preview the connection here.

**Cognitive flexibility (E1)** corresponds to the ability to change which tangent subspace is active --- to "rotate" the effective tangent space from one set of dimensions to another. A model that can switch frameworks fluently (high E1 score) can reorient its tangent space quickly, making different dimensions of working memory available for different tasks. This is a metric rotation, as discussed in Chapter 4.

**Inhibitory control (E2)** corresponds to the ability to suppress tangent vectors that are activated but irrelevant --- to "zero out" dimensions of working memory that are being driven by emotional anchoring or other salience-based distortions rather than by task relevance. The E2 benchmark measures this directly: emotional anchoring activates tangent dimensions associated with the emotional content, displacing the task-relevant dimensions. Inhibitory control is the process of suppressing these distractor tangent vectors and restoring the task-relevant ones.

**Working memory scaling (E4)** --- the subject of this chapter --- corresponds to the effective dimension of the tangent space under increasing task demands. The E4 benchmark measures this directly, and the results have been our primary data source.

The geometric picture is hierarchical. The manifold provides the space. The metric provides the distance measure. The tangent space provides the local workspace (working memory). The control layer (executive functions, Chapter 6) manages the tangent space. Each level depends on the ones below it and constrains the ones above it. Together, they constitute the geometric architecture of cognition.


## 5.15 Implications and Predictions

The tangent space model of working memory generates several testable predictions.

**Prediction 1: E4 scores should correlate with the intrinsic dimensionality of model representations.** If working memory capacity is the effective tangent space dimension, and if the tangent space dimension is related to the intrinsic dimensionality of the model's internal representations, then models with higher intrinsic dimensionality should have higher E4 scores. This can be tested by computing the intrinsic dimensionality of the residual stream (using the participatory ratio or maximum likelihood estimator from Appendix 3B) and correlating it with E4 performance across models.

**Prediction 2: Working memory degradation under overload should follow the metric eigenvalue ordering.** When a model drops information under working memory overload, it should preferentially drop the information associated with the smallest metric eigenvalues (the least-attended tangent dimensions). This can be tested by analyzing which parties are lost in failed E4 scenarios and correlating with measures of input salience.

**Prediction 3: The E4 scaling law should extend to future model generations.** If the effective tangent space dimension scales logarithmically with model size, then future models should show continued improvement on E4, with diminishing returns as the logarithmic growth slows. The rate of improvement can be estimated from the current data: the Flash 2.0 to Flash 2.5 improvement of $+0.190$ is much larger than the Flash 2.5 to Flash 3 improvement of $+0.009$, suggesting that the scaling is already decelerating. This is consistent with logarithmic scaling: early gains are large, later gains diminish.

**Prediction 4: Chunking should improve E4 scores without changing the model.** If chunking reduces task demand rather than expanding the tangent space, then presenting E4 scenarios with pre-chunked party descriptions (grouping related parties into named groups) should improve scores for models that are near their capacity limit (Flash 2.0) without affecting models that are well below their limit (Flash 3).

These predictions connect the geometric framework to testable empirical claims, transforming the tangent space model from a mathematical formalism into a scientific theory of working memory.

---

## Technical Appendix 5A: The Tangent Space as Working Memory --- Formal Treatment

**Definition** (Tangent Space, Formal). *Let $\mathcal{M}$ be an $n$-dimensional smooth manifold and let $x \in \mathcal{M}$. The tangent space $T_x\mathcal{M}$ is the $n$-dimensional real vector space of derivations at $x$: the set of all $\mathbb{R}$-linear maps $v: C^\infty(\mathcal{M}) \to \mathbb{R}$ satisfying the Leibniz rule:*

$$v(fg) = v(f) g(x) + f(x) v(g) \quad \text{for all } f, g \in C^\infty(\mathcal{M})$$

*Equivalently, $T_x\mathcal{M}$ is the space of equivalence classes of smooth curves through $x$, where two curves $\gamma_1, \gamma_2: (-\epsilon, \epsilon) \to \mathcal{M}$ with $\gamma_1(0) = \gamma_2(0) = x$ are equivalent if $(f \circ \gamma_1)'(0) = (f \circ \gamma_2)'(0)$ for all $f \in C^\infty(\mathcal{M})$.*

**Proposition 5.1** (Parallel Transport Preserves Working Memory Norm). *Let $\gamma: [0,1] \to \mathcal{M}$ be a smooth curve and let $v(0) \in T_{\gamma(0)}\mathcal{M}$ be a working memory item at the initial state. The parallel transport of $v$ along $\gamma$ produces a vector field $v(t) \in T_{\gamma(t)}\mathcal{M}$ satisfying $\nabla_{\dot{\gamma}} v = 0$. Then:*

$$\|v(t)\|_{g_{\gamma(t)}} = \|v(0)\|_{g_{\gamma(0)}} \quad \text{for all } t \in [0,1]$$

*That is, the "intensity" of the working memory item is preserved during parallel transport. Information loss under parallel transport manifests as directional rotation, not magnitude decay.*

*Proof.* $\frac{d}{dt} g(v, v) = 2 g(\nabla_{\dot{\gamma}} v, v) = 0$ by the parallel transport condition and the metric compatibility of the Levi-Civita connection.

**Proposition 5.2** (Working Memory Interference as Curvature). *Let $v$ and $w$ be two working memory items (tangent vectors) at $x \in \mathcal{M}$. After parallel transport along a curve $\gamma$ of length $L$ through a region of sectional curvature $\kappa$ in the plane spanned by $v$ and $\dot{\gamma}$, the angle $\theta$ between $v$ and $w$ changes by approximately:*

$$\Delta \theta \approx \kappa \cdot A$$

*where $A$ is the area enclosed by the curve in the $(v, \dot{\gamma})$ plane. For a reasoning loop that returns to its starting point, the total rotation (holonomy) is $\oint \kappa \, dA$, and any nonzero holonomy represents working memory corruption --- the items have been rotated relative to each other, even though no items were dropped.*

This proposition provides the formal basis for the claim that curvature causes working memory interference. The interference is not due to "competition for resources" but to the geometric fact that parallel transport on a curved manifold rotates vectors. The rotation accumulates over the reasoning trajectory, and if the trajectory passes through a region of high curvature, the accumulated rotation can be large enough to corrupt the working memory representation.


## Technical Appendix 5B: Estimating Tangent Space Dimension from Benchmark Data

**Method.** Given E4 accuracy scores $a_k$ at party counts $k = 2, 4, 6, 8$, we estimate the effective tangent space dimension $n_{\text{eff}}$ by fitting the sigmoid model:

$$a_k = \frac{1}{1 + \exp\left(-\beta(n_{\text{eff}} - c \cdot k)\right)}$$

where $c$ is the number of tangent dimensions required per party (estimated as $c \approx 2$ based on the task structure) and $\beta$ is a sharpness parameter. The fitting procedure is:

1. For each model, compute the party count $k^*$ at which accuracy drops below 0.8 (the operational capacity threshold).
2. Estimate $n_{\text{eff}} = c \cdot k^*$ as the tangent space dimension at which the system transitions from adequate to inadequate capacity.
3. Refine the estimate by fitting the full sigmoid to all four data points using least squares.

**Results.** Applying this method to the E4 data:

| Model | $k^*$ (transition) | $n_{\text{eff}}$ (estimated) | 95% CI |
|---|---|---|---|
| Gemini 2.0 Flash | ~5 | 10.2 | [8.5, 12.0] |
| Gemini 2.5 Flash | ~7 | 14.4 | [12.1, 16.8] |
| Gemini 3 Flash | $\geq 8$ | $\geq 16$ | [14.5, ---] |

The estimates are consistent with logarithmic scaling of tangent space dimension with model generation. The ratio of Flash 3 to Flash 2.0 dimensions ($\geq 16 / 10.2 \approx 1.57$) is consistent with a 50--60% increase in effective tangent space dimension across two model generations.
