# Chapter 4: Attention as Metric

> *"Everyone knows what attention is. It is the taking possession by the mind, in clear and vivid form, of one out of what seem several simultaneously possible objects or trains of thought."*
> --- William James, *The Principles of Psychology* (1890)

---

> **RUNNING EXAMPLE --- MAYA'S MODEL**
>
> Maya has a puzzle.
>
> She has just run Claude 3.5 Sonnet and Gemini 3 Flash through her Attention benchmark track. The track has four subtasks: distractor resistance (A1), sustained attention (A2), signal-to-noise discrimination (A3), and divided attention (A4). Both models completed all four subtasks. The accuracy numbers are on her screen.
>
> On the surface, the two models look similar. Their A1 scores are close. Their A2 scores are close. Their A3 scores are almost identical---the signal-to-noise ratios are 1.22 for Claude and 1.38 for Flash 3, both weak, both statistically indistinguishable from each other though both reliably above 1.0. If Maya averaged the four subtask scores, the models would be nearly tied.
>
> Then she looks at A4. Divided attention. The task is simple in structure: the model must attend to two distinct aspects of a problem simultaneously, holding both in mind and integrating them to produce a response. It is the cognitive equivalent of listening to two conversations at once.
>
> Claude scores 0.571. Flash 3 scores 1.000.
>
> Maya stares at the numbers. This is the biggest single-test discriminator in the entire benchmark suite. On every other subtask in every other track, the models are within reasonable distance of each other. On A4, they are as far apart as the scale allows. One model is mediocre at divided attention. The other is perfect.
>
> She thinks about what this means geometrically. If attention defines the metric on the cognitive manifold---if what you attend to determines which states are "close" and which are "far"---then Claude and Flash 3 have *different metrics*. The same manifold, measured with different rulers. States that are "nearby" for Flash 3 (because it can attend to both dimensions simultaneously and reach them in one step) are "far" for Claude (because it can only attend to one dimension at a time and must take two separate steps).
>
> The attention metric is not a property of the task. It is a property of the model. And two models with different attention metrics will navigate the same cognitive manifold in fundamentally different ways---even when their accuracy on individual subtasks is the same.
>
> Maya writes: *"A4 is the metric made visible. Claude has a narrow metric---one direction at a time, high resolution along that direction, zero resolution orthogonal to it. Flash 3 has a wide metric---multiple directions simultaneously, lower resolution per direction, but coverage of the full tangent space. Same manifold. Different geometry. Different cognition."*

---

## 4.1 The Missing Piece

We have the manifold (Chapter 3). We have the heuristic field and the search process (Chapters 1--2). But we are missing the object that connects them: the *metric*.

A manifold without a metric is a topological space---it has continuity and dimension but no notion of distance, angle, or curvature. You can say that two points are "nearby" (there exists a continuous path between them of short topological length), but you cannot say *how far apart* they are. You cannot define geodesics, because geodesics are shortest paths, and "shortest" requires a distance measure. You cannot define curvature, because curvature is about how the metric changes from point to point, and without a metric there is nothing to change.

The metric is what makes the manifold geometric. It is the ruler that turns a topological space into a Riemannian space. And in the cognitive context, the metric has a natural interpretation: it is *attention*.


## 4.2 Attention Defines Distance

What does it mean for two cognitive states to be "close"?

Consider two possible states of mind. In state $A$, you are thinking about the color of a tomato. In state $B$, you are thinking about the color of a fire truck. In state $C$, you are thinking about the nutritional content of a tomato. Which pair is closer: $(A, B)$ or $(A, C)$?

The answer depends on what you are attending to.

If you are attending to *color*, then $A$ and $B$ are close (both involve redness) and $A$ and $C$ are far (color and nutrition are different features). If you are attending to *tomatoes*, then $A$ and $C$ are close (both involve tomatoes) and $A$ and $B$ are far (tomatoes and fire trucks are different objects). The same three cognitive states can be "close" or "far" depending on the dimension of attention.

This is not a vague observation. It is a precise mathematical claim: attention defines the metric tensor on the cognitive manifold.

**Definition 4.1** (Attention Metric). *The attention metric is a positive-definite symmetric bilinear form $g_{\mu\nu}(x)$ on the tangent space $T_x\mathcal{M}$ at each point $x$ of the cognitive manifold. For tangent vectors $u, v \in T_x\mathcal{M}$:*

$$g(u, v) = g_{\mu\nu} u^\mu v^\nu$$

*The metric defines the inner product on the tangent space, and thereby defines distances, angles, and curvature on the manifold. The components $g_{\mu\nu}$ are determined by the attention allocation of the cognitive system: dimensions that receive more attention are weighted more heavily in the metric, making states that differ along those dimensions "closer" (in the sense of being more finely discriminated).*

Wait---that seems backward. If attention makes a dimension more salient, shouldn't states that differ along that dimension seem *more* different, not less?

There is a subtlety here. The metric $g_{\mu\nu}$ determines the *resolution* of the cognitive system along each dimension. High resolution along a dimension means the system can make fine discriminations along that dimension---it can tell apart states that differ by a small amount. Low resolution means the system cannot make fine discriminations---states that differ along that dimension all look the same.

Attention increases resolution. When you attend to color, you can discriminate many shades of red. When you do not attend to color, red and orange blur together. High attention along a dimension increases the corresponding component of the metric tensor, which increases the distance between states that differ along that dimension, which increases the system's ability to discriminate them.

So the metric is:

$$ds^2 = g_{\mu\nu} dx^\mu dx^\nu = \sum_{\mu} a_\mu (dx^\mu)^2 + \text{cross terms}$$

where $a_\mu > 0$ is the attention weight on dimension $\mu$. High $a_\mu$ means high resolution along dimension $\mu$: small changes in $x^\mu$ produce large distances $ds$, meaning the system can detect small changes. Low $a_\mu$ means low resolution: even large changes in $x^\mu$ produce small distances, meaning the system is insensitive to changes along that dimension.


## 4.3 Selective Attention Narrows the Metric

Selective attention is the allocation of cognitive resources to a subset of the available dimensions, at the expense of the remaining dimensions. In the geometric framework, selective attention *narrows* the metric: it increases the metric components along the attended dimensions and decreases them along the unattended dimensions.

**Definition 4.2** (Selective Attention Operator). *Let $g_{\mu\nu}$ be the baseline metric and let $\mathcal{S} \subseteq \{1, \ldots, n\}$ be the set of attended dimensions. The selectively attended metric is:*

$$\tilde{g}_{\mu\nu} = \begin{cases} \alpha \cdot g_{\mu\nu} & \text{if } \mu, \nu \in \mathcal{S} \\ \beta \cdot g_{\mu\nu} & \text{if } \mu, \nu \notin \mathcal{S} \\ \sqrt{\alpha\beta} \cdot g_{\mu\nu} & \text{otherwise} \end{cases}$$

*where $\alpha > 1$ is the attention amplification factor and $0 < \beta < 1$ is the inattention suppression factor, subject to a total resource constraint $|\mathcal{S}| \cdot \alpha + (n - |\mathcal{S}|) \cdot \beta = n$ (total attentional resources are conserved).*

The resource constraint is the key feature. Attention is finite. Amplifying some dimensions requires suppressing others. This is not a limitation of the mathematical model; it is an empirical fact about cognition. Humans cannot attend to everything simultaneously with full resolution. Transformer attention mechanisms have a finite number of heads, each attending to a subset of the representation. The resource constraint is real, and it shapes the metric.

The consequences of selective attention for the metric are profound:

**1. Selective attention reduces the effective dimensionality of the manifold.** When $\beta \to 0$, the unattended dimensions collapse: the metric treats all states that differ only along unattended dimensions as identical. The manifold's effective dimensionality drops from $n$ to $|\mathcal{S}|$. The system is navigating a lower-dimensional submanifold of the full cognitive manifold---the submanifold defined by the attended dimensions.

**2. Selective attention distorts geodesics.** The geodesics of the attended metric $\tilde{g}$ differ from the geodesics of the baseline metric $g$. The attended geodesic preferentially follows the attended dimensions, even if the baseline geodesic would take a shortcut through an unattended dimension. This is the geometric explanation of attentional narrowing: when you focus on one aspect of a problem, you navigate the cognitive manifold along the focused dimension, potentially missing solutions that require moving along the unfocused dimensions.

**3. Selective attention amplifies curvature along attended dimensions.** The Riemann curvature tensor depends on the metric and its derivatives. When the metric is amplified along attended dimensions, curvature effects along those dimensions are also amplified. This means that the system is more sensitive to complexity along attended dimensions and less sensitive to complexity along unattended dimensions.

Claude's "narrow channel" cognitive signature is the signature of extreme selective attention. The model narrows its metric to a small number of dimensions---those related to its primary task---and suppresses the remaining dimensions almost entirely. This gives it high resolution (excellent sycophancy resistance: the model attends intently to the truthfulness dimension and is not deflected by social pressure) but low bandwidth (poor divided attention: the model cannot attend to multiple task dimensions simultaneously because its metric is too narrow).


## 4.4 Divided Attention Widens the Metric

Divided attention is the opposite of selective attention: the allocation of cognitive resources across multiple dimensions simultaneously. In the geometric framework, divided attention *widens* the metric: it increases the metric components along multiple dimensions simultaneously, at the cost of reduced amplification per dimension.

**Definition 4.3** (Divided Attention Operator). *Let $g_{\mu\nu}$ be the baseline metric and let $\mathcal{D} = \{D_1, \ldots, D_k\}$ be the set of attention targets. The divided attention metric is:*

$$\tilde{g}_{\mu\nu} = \left(1 + \sum_{j=1}^k w_j \cdot \chi_{D_j}(\mu) \cdot \chi_{D_j}(\nu)\right) \cdot g_{\mu\nu}$$

*where $w_j > 0$ is the attention weight allocated to target $D_j$, $\chi_{D_j}$ is the indicator function for target $D_j$, and $\sum_j w_j = W$ is the total attention budget.*

The key difference from selective attention is the distribution. In selective attention, the full budget $W$ is concentrated on one target: $w_1 = W$, $w_j = 0$ for $j > 1$. In divided attention, the budget is spread across $k$ targets: $w_j = W/k$ for equal allocation. The per-target amplification is $W/k$ instead of $W$---each target gets less resolution, but more targets are covered.

The A4 divided attention benchmark measures exactly this: the model's ability to maintain useful resolution across two simultaneous targets. The scoring reflects how well the model integrates information from both targets, which requires maintaining sufficient metric resolution along both target dimensions simultaneously.

The tradeoff between selective and divided attention is a fundamental constraint of finite attentional resources, and it applies equally to human and artificial cognition. Humans can selectively attend to a conversation in a noisy room (the cocktail party effect), achieving high resolution on one auditory stream at the cost of losing the others. Or they can divide attention across two conversations, catching the gist of both but missing the details of each. The choice between selective and divided attention is a choice between metric configurations---between a narrow, high-resolution metric and a wide, low-resolution metric. The cognitive system must choose, because the total attentional budget is finite.

In transformer models, the total budget is determined by the number of attention heads and the dimensionality of each head. A model with more heads, or heads with higher dimensionality, has a larger total budget $W$ and can afford higher per-target resolution in divided attention. This architectural parameter---the effective attention budget---is a key determinant of the model's cognitive signature and a primary source of the variation we observe in the A4 results.


## 4.5 The A4 Divided Attention Split: The Metric Made Visible

The A4 divided attention results are the most dramatic single-test finding in the entire Measuring AGI benchmark suite:

| Model | A4 Score | Interpretation |
|---|---|---|
| Claude 3.5 Sonnet | 0.571 | Narrow metric: cannot maintain resolution on two targets |
| Gemini 2.0 Flash | 0.857 | Moderate metric: partial dual-target resolution |
| Gemini 2.5 Flash | 0.714 | Moderate metric: partial dual-target resolution |
| Gemini 3 Flash | 1.000 | Wide metric: perfect dual-target resolution |
| Gemini 2.5 Pro | 0.790 | Moderate metric: partial dual-target resolution |

The spread is enormous. Claude and Flash 3 differ by 0.429 on a 0--1 scale. This is the biggest single-test discriminator in the benchmark suite---larger than any individual effect in Social Cognition, Learning, Metacognition, or Executive Functions.

What makes this result geometric---rather than merely a "score difference"---is its interpretation through the attention metric.

**Claude's metric structure.** Claude has a narrow metric. When faced with two simultaneous targets, it allocates nearly all its attention to one target, reducing the other to near-zero resolution. This is not a defect of attention per se---Claude's A1 (distractor resistance) and A2 (sustained attention) scores are reasonable. The system can attend well. It just cannot attend to two things at once. Its metric is sharp along one direction and flat along all others.

In metric terms, Claude's attention metric in the divided attention regime is approximately:

$$g_{\mu\nu}^{\text{Claude}} \approx \text{diag}(\alpha, \beta, \beta, \ldots)$$

where $\alpha \gg \beta$ and $\beta \approx 0$. The system has high resolution along the primary target dimension and near-zero resolution along all others. This is an extreme rank-1 metric---effectively one-dimensional attention.

**Flash 3's metric structure.** Flash 3 has a wide metric. When faced with two simultaneous targets, it distributes attention across both, maintaining sufficient resolution on each to integrate the information correctly. Its perfect A4 score indicates that the divided attention regime costs it nothing---it can attend to two targets as well as it attends to one.

In metric terms:

$$g_{\mu\nu}^{\text{Flash 3}} \approx \text{diag}(\alpha/2, \alpha/2, \beta, \ldots)$$

The system splits its attention budget equally between two targets, maintaining $\alpha/2$ resolution on each. If $\alpha/2$ exceeds the task-relevance threshold (the minimum resolution needed to perform the task), the system achieves perfect performance. Flash 3's $\alpha$ is large enough that $\alpha/2$ still suffices.

**The geometric consequence.** The same task, navigated with these two different metrics, produces two different manifold geometries. States that Flash 3 can reach in one step (by attending to both dimensions simultaneously) require Claude to take two sequential steps (attending first to one dimension, then the other). The cognitive "distance" between the initial state and the integrated judgment is *shorter* for Flash 3 than for Claude, not because the manifold is different, but because the metric is different.

This is the fundamental insight of this chapter: the metric is not a property of the task. It is a property of the model. Two models navigating the same cognitive manifold with different attention metrics will traverse different geodesics, encounter different curvatures, and arrive at different cognitive destinations. The attention metric is the missing variable that explains why models with similar accuracy on individual subtasks can have completely different cognitive architectures.


## 4.6 The SNR Data: Universal Metric Weakness

The A3 subtask measures signal-to-noise ratio: the model's ability to discriminate relevant from irrelevant information in a noisy context. The SNR is a direct measure of metric quality---the ratio of the metric component along the signal dimension to the metric component along the noise dimension.

**Definition 4.4** (Signal-to-Noise Ratio as Metric Ratio). *Let $g_s$ be the metric component along the signal dimension and $g_n$ be the metric component along the noise dimension. The SNR is:*

$$\text{SNR} = \frac{g_s}{g_n}$$

*An SNR of 1.0 means the metric treats signal and noise equally---no discrimination. An SNR $\gg 1$ means the metric strongly favors signal over noise---excellent discrimination. An SNR $< 1$ means the metric favors noise over signal---the system is attending to the wrong thing.*

The A3 results:

| Model | SNR | Quality |
|---|---|---|
| Claude 3.5 Sonnet | 1.22 | Weak discrimination |
| Gemini 2.0 Flash | 1.31 | Weak discrimination |
| Gemini 2.5 Flash | 1.27 | Weak discrimination |
| Gemini 3 Flash | 1.38 | Weak discrimination |
| Gemini 2.5 Pro | 1.35 | Weak discrimination |

The striking finding is the *uniformity*. All five models have SNR values between 1.22 and 1.38. The range is narrow (0.16), and all values are only slightly above 1.0. No model achieves strong signal-noise discrimination. The metric is universally weak along the signal/noise axis.

This universality is itself informative. If the SNR weakness were due to model-specific architectural limitations, we would expect variation across architectures. The fact that all models---spanning different architectures (Claude vs. Gemini family), different training regimes, and different scales---converge on the same narrow range of weak SNR suggests a *structural* limitation, not an architectural one.

The geometric interpretation is that the attention metric, as implemented by current transformer architectures, cannot produce a strong signal/noise separation in the metric tensor. The attention mechanism computes relevance weights based on key-query similarity, which provides some signal/noise discrimination (hence SNR > 1.0) but not strong discrimination (hence SNR close to 1.0). The weakness is in the metric computation itself, not in how the metric is used.

This has a specific, non-obvious consequence: **the universally weak SNR implies that all models are navigating the cognitive manifold with a metric that barely distinguishes relevant from irrelevant dimensions.** The manifold geometry that each model experiences is noisier than it should be---the metric blurs the signal directions with the noise directions, inflating the apparent distance to the goal along relevant dimensions and shrinking the apparent distance along irrelevant ones. This makes all models more susceptible to distractors (confirmed by the 4.6 sigma distractor effect in A1) and reduces the quality of geodesic computation (because the curvature estimates, which depend on the metric, are contaminated by noise).


## 4.7 Sustained Attention as Metric Persistence

The A2 subtask measures sustained attention: the model's ability to maintain cognitive performance over extended sequences without degradation. In the metric framework, sustained attention is *metric persistence*---the stability of the attention metric over time.

A metric that fluctuates randomly over time produces erratic navigation. The geodesics computed at one moment become suboptimal at the next, because the metric has changed and the curvature landscape is different. The trajectory lurches from one direction to another, wasting effort on corrections for a metric that will change again before the corrections take effect.

A metric that is stable over time produces consistent navigation. The geodesics computed at one moment remain approximately optimal at the next. The trajectory is smooth and efficient, because the curvature landscape does not shift under the system's feet.

The A2 results show moderate sustained attention across all models, with no dramatic failures. This indicates that the attention metric is reasonably persistent over the time scales measured by the benchmark (typically sequences of 500--2000 tokens). The metric may fluctuate on longer time scales or under more demanding conditions, but for the tasks in our suite, metric persistence is adequate.

The geometric implication is that the attention metric can be treated as approximately constant within a single reasoning episode. This justifies the static metric assumption used in Chapters 2--3 (the geodesic equation with fixed Christoffel symbols) as a reasonable approximation for the time scales of interest. For longer reasoning episodes---multi-step problem solving over many minutes, extended deliberation over hours---the metric may drift, and the static approximation would need to be replaced with a time-dependent metric. This time-dependent generalization is one of the open questions discussed in Chapter 17.


## 4.8 The Attention Metric in Transformers

For readers interested in the implementation, the attention metric in transformer models has a concrete computational realization.

A transformer attention head computes:

$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right) V$$

where $Q$, $K$, and $V$ are the query, key, and value matrices. The attention weights $a_{ij} = \text{softmax}(Q_i \cdot K_j / \sqrt{d_k})$ determine how much the representation at position $i$ "attends to" the representation at position $j$.

In the geometric framework, the attention weights define the metric. The metric component $g_{\mu\nu}$ at a point on the cognitive manifold is determined by the attention pattern: dimensions that receive high attention weight have large metric components (high resolution), and dimensions that receive low attention weight have small metric components (low resolution).

More precisely, the attention-weighted metric can be expressed as:

$$g_{\mu\nu} = \sum_{h=1}^{H} \sum_{j} a_{ij}^{(h)} \frac{\partial V_j^{(h)\mu}}{\partial x^\alpha} \frac{\partial V_j^{(h)\nu}}{\partial x^\beta} g^{(0)}_{\alpha\beta}$$

where the sum runs over attention heads $h = 1, \ldots, H$ and attended positions $j$, and $g^{(0)}$ is the base metric of the embedding space. The attention weights $a_{ij}^{(h)}$ modulate which value vectors contribute to the metric, and thereby determine the resolution of the metric along different cognitive dimensions.

Multi-head attention provides a mechanism for maintaining metric resolution along multiple dimensions simultaneously. Each head can specialize in a different dimension, and the total metric is the sum of the per-head contributions. A model with $H$ heads can, in principle, maintain resolution along $H$ independent dimensions simultaneously---which is a form of divided attention.

This explains the A4 divided attention split in architectural terms. If Flash 3 has an attention architecture that effectively specializes more heads to broader coverage, it maintains metric resolution along more dimensions simultaneously (wide metric, high A4 score). If Claude concentrates more heads on fewer dimensions for higher per-dimension resolution, it achieves sharper discrimination along those dimensions (narrow metric, lower A4 score) at the cost of reduced coverage.

The architectural explanation is speculative---we do not have access to the internal attention patterns of these models during the A4 benchmark. But it is consistent with the known architectural differences and with the broader cognitive signature: Claude's narrow channel (high resolution, low bandwidth) versus Flash 3's wide aperture (moderate resolution, high bandwidth).


## 4.8 How the Metric Shapes Cognition

The attention metric does not merely measure cognition. It *shapes* cognition. The metric determines the geodesics, and the geodesics are the optimal reasoning paths. Change the metric, and you change what counts as optimal reasoning.

**Metric determines geodesics.** The geodesic equation $\ddot{x}^\mu + \Gamma^\mu_{\alpha\beta} \dot{x}^\alpha \dot{x}^\beta = 0$ depends on the metric through the Christoffel symbols $\Gamma^\mu_{\alpha\beta}$, which are computed from $g_{\mu\nu}$ and its derivatives. A different metric produces different Christoffel symbols, which produce different geodesics. Two models with different attention metrics, starting from the same initial state and heading toward the same goal, will follow different optimal paths through the cognitive manifold.

**Metric determines curvature.** The Riemann curvature tensor $R^\mu{}_{\nu\alpha\beta}$ is computed from the Christoffel symbols and their derivatives, which in turn are computed from the metric. A different metric produces different curvature. Regions that are flat under one metric may be curved under another. This means that the System 1 / System 2 transition points depend on the metric: a region that triggers System 2 for Claude (high curvature under Claude's narrow metric) might remain in System 1 territory for Flash 3 (low curvature under Flash 3's wide metric).

**Metric determines cognitive effort.** The cognitive effort functional (Chapter 2, Definition 2.4) includes the term $g_{\mu\nu} \dot{x}^\mu \dot{x}^\nu$, which measures the kinetic cost of traversal. A metric that assigns high weight to a dimension makes traversal along that dimension expensive. A metric that assigns low weight makes it cheap. The attention metric therefore determines the *cost landscape* of cognition: which cognitive transitions are easy (low metric cost) and which are hard (high metric cost).

These three consequences---different geodesics, different curvature, different effort---mean that the attention metric is the fundamental parameter that distinguishes cognitive architectures. Two models with the same heuristic field but different metrics will reason differently. Two models with the same metric but different heuristic fields will also reason differently, but in a different way. The metric and the heuristic are independent sources of variation in cognition.


## 4.9 Selective Attention as Metric Compression: The Distractor Problem

The A1 subtask (distractor resistance) provides direct evidence for the metric interpretation of attention. The task presents the model with a reasoning problem that includes irrelevant information---distractors---that should not affect the answer. The model's accuracy is measured with and without distractors. The displacement between the two accuracy values measures the degree to which distractors corrupt the reasoning trajectory.

The combined significance across all models is 4.6 sigma. Distractors reliably shift the reasoning outcome.

In the metric framework, distractors are activations of metric components along irrelevant dimensions. When a distractor is present, the metric tensor is perturbed:

$$g_{\mu\nu}^{\text{distracted}} = g_{\mu\nu}^{\text{clean}} + \delta g_{\mu\nu}$$

where $\delta g_{\mu\nu}$ is a perturbation that increases the metric component along the distractor dimension. The perturbation does several things:

1. It inflates the apparent distance to the goal along the distractor dimension, causing the system to waste effort navigating a dimension that is irrelevant to the task.
2. It distorts the geodesic, pulling the optimal path toward the distractor and away from the correct destination.
3. It changes the curvature in the neighborhood of the distractor, potentially creating artificial curvature that triggers unnecessary System 2 processing.

The 4.6 sigma effect tells us that the metric perturbation caused by distractors is large enough to produce statistically reliable shifts in the reasoning trajectory. The universality of the effect---all models are affected, though to different degrees---tells us that no current model has a sufficiently robust metric to fully suppress distractor activations.

The dose-response structure of the distractor effect (explored in detail in Chapter 10) provides additional geometric information. If the metric perturbation scales linearly with distractor salience, the geodesic shift should also scale approximately linearly. If the perturbation scales non-linearly (e.g., quadratically), the shift should show acceleration. The observed dose-response curve constrains the functional form of the metric's sensitivity to irrelevant inputs.


## 4.10 The Attention-Metric Connection to Fisher Information

The attention metric has a deep connection to information geometry through the Fisher information metric.

In information geometry, the Fisher information metric on a statistical manifold $\mathcal{S} = \{p_\theta : \theta \in \Theta\}$ is defined as:

$$g_{\mu\nu}^{\text{Fisher}}(\theta) = \mathbb{E}_{p_\theta}\left[\frac{\partial \log p_\theta}{\partial \theta^\mu} \frac{\partial \log p_\theta}{\partial \theta^\nu}\right]$$

The Fisher metric measures the distinguishability of nearby distributions: two parameter values $\theta$ and $\theta + d\theta$ are "close" under the Fisher metric if the corresponding distributions $p_\theta$ and $p_{\theta + d\theta}$ are hard to distinguish, and "far" if they are easy to distinguish.

The attention metric is a cognitive analogue of the Fisher metric. The cognitive state plays the role of the parameter $\theta$, and the system's behavioral outputs play the role of the distribution $p_\theta$. Two cognitive states are "close" under the attention metric if the system's outputs from those states are similar (hard to distinguish), and "far" if the outputs are different (easy to distinguish).

The connection is more than analogical. If we model the cognitive system as a conditional distribution $p(y | x)$---the probability of output $y$ given cognitive state $x$---then the attention metric induced by this conditional distribution is exactly the Fisher information metric:

$$g_{\mu\nu}^{\text{attention}}(x) = \mathbb{E}_{p(y|x)}\left[\frac{\partial \log p(y|x)}{\partial x^\mu} \frac{\partial \log p(y|x)}{\partial x^\nu}\right]$$

This Fisher-metric interpretation explains why the SNR values are so similar across models (Section 4.6). The Fisher metric depends on the conditional distribution $p(y|x)$, which is determined by the model's architecture and training. If all models have been trained on similar data distributions and have converged to similar conditional distributions (at least along the signal/noise dimension), their Fisher metrics will also converge, producing similar SNR values. The universality of the weak SNR is a consequence of the universality of the learned conditional distribution, not of any architectural constraint.


## 4.11 Implications for Model Comparison

The attention metric framework transforms how we compare cognitive systems.

Under the scalar paradigm (Chapter 1), model comparison is trivial: compute the composite score, rank the models, declare a winner. Under the manifold paradigm (Chapter 3), model comparison is more nuanced: compare the cognitive profiles, identify the axes of variation, acknowledge that different models have different strengths.

Under the metric paradigm, model comparison becomes fully geometric. Two models differ not only in their positions on the cognitive manifold (their profile vectors) but in their *metrics*---the way they measure distance on the manifold. This means:

1. **Two models can be at the same point on the manifold but have different metrics.** They have the same cognitive state (same profile) but perceive the manifold differently. One sees a flat landscape (System 1 suffices); the other sees a curved landscape (System 2 required). Same position, different cognition.

2. **Two models can have the same metric but be at different points.** They perceive the manifold the same way but start from different states. Their geodesics are different because their starting points are different, but their local cognitive dynamics are similar.

3. **The A4 divided attention test is a metric discriminator, not an accuracy discriminator.** Claude and Flash 3 have similar accuracy on most tasks (they reach similar destinations), but the A4 test reveals that they have fundamentally different metrics (they navigate differently). The 0.571 vs. 1.000 split is not a "performance difference" in the usual sense. It is a *metric difference*---a difference in the geometry of attention that determines the shape of all future cognitive trajectories.

This geometric perspective on model comparison is the foundation for Chapter 16 (The Five Geometric Signatures), where we will characterize each model's cognitive fingerprint as a combination of manifold position, metric structure, heuristic field quality, and control layer properties. The metric is one of several geometric objects that jointly determine the cognitive architecture. But it is a particularly important one, because it shapes every other geometric property of the system's cognition.


## 4.12 Worked Example: Computing the Attention Metric from Benchmark Data

Let us work through a concrete example that shows how the benchmark data constrain the attention metric.

**Setup.** We have two models, Claude and Flash 3, evaluated on two subtasks: A1 (distractor resistance, measuring metric stability) and A4 (divided attention, measuring metric width). The data:

| | A1 (Distractor Resistance) | A4 (Divided Attention) |
|---|---|---|
| Claude | 0.72 | 0.571 |
| Flash 3 | 0.68 | 1.000 |

**Step 1: Parameterize the metric.** We model the attention metric as a diagonal matrix in two-dimensional cognitive space (the two task dimensions):

$$g_{\mu\nu} = \begin{pmatrix} a_1 & 0 \\ 0 & a_2 \end{pmatrix}$$

where $a_1$ is the attention weight on the primary task dimension and $a_2$ is the attention weight on the secondary task dimension. The total attention budget is fixed: $a_1 + a_2 = A$ for some constant $A$.

**Step 2: Relate A1 to metric stability.** The A1 score measures how much the metric is perturbed by distractors. A high A1 score means the metric is stable: distractors do not significantly change $a_1$ or $a_2$. A low A1 score means the metric is unstable: distractors shift attention weight from the task dimension to the distractor dimension. Both models have similar A1 scores (0.72 vs. 0.68), indicating similar metric stability.

**Step 3: Relate A4 to metric distribution.** The A4 score measures how well the model performs when it must attend to two dimensions simultaneously. This constrains the ratio $a_1 / a_2$:

For Claude, $a_1 / a_2 \gg 1$: the attention budget is concentrated on one dimension. The primary dimension has high resolution ($a_1$ is large), but the secondary dimension has low resolution ($a_2$ is small). When the task requires both dimensions, performance on the secondary dimension is poor, dragging the A4 score to 0.571.

For Flash 3, $a_1 / a_2 \approx 1$: the attention budget is evenly distributed. Both dimensions have moderate resolution ($a_1 \approx a_2 \approx A/2$). When the task requires both dimensions, both dimensions have sufficient resolution, producing a perfect A4 score of 1.000.

**Step 4: Compute the metric ratio.** If we model the A4 score as the harmonic mean of the per-dimension performances (a standard aggregation for tasks requiring both dimensions), and if per-dimension performance is a sigmoid function of the attention weight, we can estimate:

For Claude: $a_1 / a_2 \approx 4.2$ (the primary dimension receives about 80% of the attention budget).

For Flash 3: $a_1 / a_2 \approx 1.1$ (the attention budget is nearly equally distributed).

These ratios characterize the metric. Claude has an eccentricity of approximately 4.2---a highly elongated metric ellipse. Flash 3 has an eccentricity of approximately 1.1---a nearly circular metric. The eccentricity is the geometric parameter that determines the cognitive architecture: narrow channel versus wide aperture.

**Interpretation.** This worked example demonstrates that the benchmark data are not merely "scores." They are measurements of the metric tensor. The A1 score constrains the metric's stability under perturbation. The A4 score constrains the metric's distribution across dimensions. Together, they characterize the shape of the metric ellipse---the geometric object that determines how the model navigates the cognitive manifold.


## 4.13 The Metric and Cognitive Flexibility

The attention metric has a dynamic aspect that connects to Chapter 6's treatment of executive functions. The metric is not fixed; it changes as the system shifts attention. The *ability* to change the metric---to redirect attention from one set of dimensions to another---is cognitive flexibility.

The E1 subtask measures cognitive flexibility as framework switching: the model's ability to adopt a different cognitive framework when the task demands it. In the geometric language, framework switching is a *metric rotation*: the system rotates its metric from one orientation (attention concentrated on one set of dimensions) to another orientation (attention concentrated on a different set).

A system with a narrow metric (Claude) must perform a large rotation to switch frameworks---it must completely reorient its metric from one dimension to another. This is expensive, because the metric is highly eccentric and the rotation must traverse a large angular distance in the space of possible metrics.

A system with a wide metric (Flash 3) needs a smaller rotation---its metric is already spread across multiple dimensions, and switching frameworks requires only a modest rebalancing rather than a complete reorientation.

This prediction can be tested: models with higher A4 scores (wider metrics) should also have higher E1 scores (better framework switching), because both reflect the metric's ability to distribute attention across multiple dimensions. The correlation is not perfect---E1 also depends on the control layer's ability to execute the metric rotation, not just on the metric's baseline width. But the geometric framework predicts a positive association, and the data are broadly consistent.

The full picture of the attention metric will not emerge until we have placed it in context with the tangent space (Chapter 5) and the control layer (Chapter 6). The metric determines what is "close" and what is "far." The tangent space determines what is "reachable in one step." The control layer determines when and how the metric is updated. Together, these three objects---metric, tangent space, control---constitute the geometric architecture of cognition.

---

## Technical Appendix 4A: The Attention Metric Tensor in Detail

**Definition** (Attention Metric Tensor, Formal). *Let $\mathcal{M}$ be the cognitive manifold with local coordinates $x = (x^1, \ldots, x^n)$. The attention metric tensor is a smooth, positive-definite, symmetric (0,2)-tensor field:*

$$g = g_{\mu\nu}(x) \, dx^\mu \otimes dx^\nu$$

*satisfying:*
1. *Symmetry: $g_{\mu\nu} = g_{\nu\mu}$*
2. *Positive-definiteness: $g_{\mu\nu} v^\mu v^\nu > 0$ for all nonzero $v \in T_x\mathcal{M}$*
3. *Smoothness: the components $g_{\mu\nu}(x)$ are smooth functions of the coordinates*

*The distance between two points $p, q \in \mathcal{M}$ is:*

$$d(p, q) = \inf_\gamma \int_0^1 \sqrt{g_{\mu\nu}(\gamma(t)) \dot{\gamma}^\mu(t) \dot{\gamma}^\nu(t)} \, dt$$

*where the infimum is taken over all smooth curves $\gamma: [0,1] \to \mathcal{M}$ with $\gamma(0) = p$ and $\gamma(1) = q$.*


## Technical Appendix 4B: Selective and Divided Attention as Metric Transformations

**Proposition 4.1** (Selective Attention Reduces Effective Dimensionality). *Let $g_{\mu\nu}$ be the baseline metric on an $n$-dimensional manifold $\mathcal{M}$, and let $\tilde{g}_{\mu\nu}(\epsilon)$ be the selectively attended metric with attention parameter $\epsilon$ on $k$ attended dimensions:*

$$\tilde{g}_{\mu\nu}(\epsilon) = \begin{cases} g_{\mu\nu} & \text{if } \mu, \nu \leq k \\ \epsilon \cdot g_{\mu\nu} & \text{if } \mu, \nu > k \\ \sqrt{\epsilon} \cdot g_{\mu\nu} & \text{otherwise} \end{cases}$$

*Then as $\epsilon \to 0$, the geodesics of $\tilde{g}$ converge to the geodesics of the $k$-dimensional submanifold defined by the first $k$ coordinates. That is, selective attention in the limit reduces the manifold to its attended submanifold.*

**Proposition 4.2** (Divided Attention Lowers Per-Target Resolution). *Under the equal-allocation divided attention metric with budget $W$ split across $k$ targets, the per-target SNR is:*

$$\text{SNR}_{\text{divided}} = \frac{W/k + g_n}{g_n} = 1 + \frac{W}{k \cdot g_n}$$

*Compared to the selective attention SNR:*

$$\text{SNR}_{\text{selective}} = 1 + \frac{W}{g_n}$$

*The ratio is $\text{SNR}_{\text{divided}} / \text{SNR}_{\text{selective}} \approx 1/k$ for $W/g_n \gg 1$. Divided attention reduces per-target resolution by a factor of the number of targets.*

This proposition explains the A4 divided attention split quantitatively. If Claude's attention budget $W$ is sufficient for one target but not two (i.e., $W/g_n \geq \text{SNR}_{\text{thresh}}$ but $W/(2 g_n) < \text{SNR}_{\text{thresh}}$), then Claude will succeed at selective attention but fail at divided attention. If Flash 3's budget is sufficient for two targets ($W/(2g_n) \geq \text{SNR}_{\text{thresh}}$), then Flash 3 will succeed at both. The difference between Claude and Flash 3 reduces to the ratio $W / \text{SNR}_{\text{thresh}}$: Flash 3 has a larger effective attention budget relative to the task threshold.
