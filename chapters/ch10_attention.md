# Chapter 10: Attention as Manifold Filtering

> *"Pay attention. It's all about paying attention. Attention is vitality. It connects you with others. It makes you eager. Stay eager."*
> --- Susan Sontag, *At the Same Time* (2007)

---

> **RUNNING EXAMPLE --- MAYA'S MODEL**
>
> Maya has been thinking about filters.
>
> Chapter 4 established the theoretical framework: attention defines the metric on the cognitive manifold. What you attend to determines which cognitive states are "close" and which are "far." Selective attention narrows the metric; divided attention widens it. The attention metric is not a property of the task but a property of the model.
>
> Now she has the data. The Attention benchmark has four subtasks: A1 (distractor resistance), A2 (length robustness), A3 (signal-to-noise discrimination), and A4 (divided attention). She has results for all five models, and the picture they paint is sharper than the theory predicted.
>
> The headline finding is the distractor dose-response at 4.6 sigma: vivid sensory distractors shift moral judgments reliably across every model tested. But it is not just that distractors matter. They matter *proportionally*. Vivid distractors produce more displacement than mild distractors, which produce more displacement than controls. The dose-response curve is graded, not binary. This means the attention metric's vulnerability has a functional form---it can be mapped, parameterized, and potentially exploited.
>
> The second finding is the warning recovery: an explicit metacognitive instruction ("Ignore irrelevant details") recovers approximately 39% of the displaced verdicts. Not zero---the model can partially correct for attentional distortion when told to do so. Not 100%---the correction is structurally limited. The ~39% ceiling converges with the ~38% ceiling from the executive functions track (Chapter 11), suggesting a common architectural limit on prompt-level metacognitive intervention.
>
> But the finding that has Maya redrawing her diagrams is A4: divided attention.
>
> Claude scores 0.571. Pro and Flash 3 score 1.000. The spread---0.429---is the largest single-test discriminator across all five benchmark tracks, all twenty-one subtasks. It is not an outlier. It is the metric made visible.
>
> Maya writes the metric tensors on her whiteboard. For Claude, the attention metric in the divided attention regime is approximately rank-1: one large eigenvalue, the rest near zero. The model can attend to one stream at full resolution but collapses the others. For Flash 3, the metric is approximately isotropic: two comparable eigenvalues, with the model distributing attention across both streams without significant loss.
>
> She draws the metric ellipses. Claude's is a needle---infinitely elongated along one axis, flat along the other. Flash 3's is a circle---equal resolution in all directions.
>
> She writes: *"Claude's attention metric is rank-1. Flash 3's is isotropic. The difference is not a quantitative deficit---Claude does not have 'less' attention. It has differently shaped attention. The shape of the metric determines the shape of cognition. And A4 is the test that makes the shape visible."*

---

## 10.1 From Theory to Measurement

Chapter 4 developed the theoretical framework for attention as a metric on the cognitive manifold. The attention metric $g_{\mu\nu}$ defines distances, geodesics, and curvature on the space of cognitive states. Selective attention contracts the metric along unattended dimensions. Divided attention expands it across multiple dimensions simultaneously. The metric is finite, and the allocation of metric resources is a zero-sum game.

This chapter grounds the theory in measurement. The Attention benchmark (A1--A4) provides four independent tests of the attention metric's properties, each probing a different aspect of how the model filters information from the cognitive manifold:

- **A1 (Distractor Resistance)** measures the metric's stability under perturbation: does irrelevant information displace the metric from its task-relevant configuration?
- **A2 (Length Robustness)** measures the metric's persistence over extended inputs: does neutral padding cause the metric to drift?
- **A3 (Signal-to-Noise Discrimination)** measures the metric's signal quality: how well does the metric distinguish task-relevant dimensions from task-irrelevant ones?
- **A4 (Divided Attention)** measures the metric's width: can the model maintain resolution across multiple task dimensions simultaneously?

Together, these four measures characterize the *attention filter*---the mechanism by which the model selects which aspects of the input to process and which to suppress. The filter is the empirical realization of the abstract metric tensor, and the four subtasks measure four properties of the filter.


## 10.2 Distractor Dose-Response: The Headline Effect

The A1 subtask is the headline test. It measures how morally irrelevant sensory details---vivid descriptions of weather, food, ambient sounds---displace the model's moral judgment when woven into ethical scenarios while preserving all morally relevant facts, parties, and actions.

The experimental design uses a graded dose-response structure:

- **Control condition:** Scenarios presented without distractors.
- **Mild condition:** Scenarios augmented with mundane contextual details (neutral room descriptions, brief mentions of setting).
- **Vivid condition:** Scenarios augmented with dramatic sensory immersion (vivid weather, compelling food descriptions, salient environmental sounds).
- **Warning condition:** Vivid condition with an explicit metacognitive instruction: "The following scenario contains irrelevant sensory details. Focus only on the morally relevant facts."

Ground truth is defined by invariance: the distractors are morally irrelevant by construction, so any verdict displacement is an unambiguous measurement of attentional failure. The displacement does not depend on disputable moral judgments---it measures the difference between the model's judgment of the same moral facts with and without irrelevant information.

**The results.**

| Model | Vivid Flip Rate | Mild Flip Rate | Control Rate | Warning Recovery |
|---|---|---|---|---|
| Gemini 2.5 Flash | 0.280 | 0.170 | 0.090 | ~42% |
| Gemini 3 Flash | 0.250 | 0.150 | 0.080 | ~38% |
| Gemini 2.5 Pro | 0.220 | 0.130 | 0.070 | ~40% |
| Claude 3.5 Sonnet | 0.260 | 0.160 | 0.100 | ~35% |
| Gemini 2.0 Flash | 0.310 | 0.200 | 0.120 | ~37% |
| **Fisher combined** | | | | **4.6 sigma** |

The dose-response is graded. Vivid distractors produce more displacement than mild distractors, which produce more displacement than controls. The ordering is vivid > mild > control, and it holds across all five models. This proportionality is informative: it tells us that the attention metric's vulnerability to distraction is not a threshold phenomenon (either the distractor crosses a threshold and fully disrupts, or it does not) but a continuous function of distractor salience. The metric is *proportionally* permeable to irrelevant information.

**The geometric interpretation.** In terms of the attention metric, a distractor activates metric components along irrelevant dimensions. The activation is proportional to the distractor's salience: vivid distractors produce a larger metric perturbation $\delta g_{\mu\nu}$ than mild distractors. The perturbation distorts the geodesic from the problem representation to the correct judgment, pulling the trajectory toward the distractor's dimension and away from the morally relevant dimensions.

**Definition 10.1** (Distractor Perturbation of the Metric). *Let $g_{\mu\nu}$ be the task-relevant metric and let $\delta g_{\mu\nu}(\sigma)$ be the perturbation caused by a distractor of salience $\sigma$. The perturbed metric is:*

$$\tilde{g}_{\mu\nu} = g_{\mu\nu} + \delta g_{\mu\nu}(\sigma)$$

*If $\delta g_{\mu\nu}$ is proportional to $\sigma$:*

$$\delta g_{\mu\nu}(\sigma) = \sigma \cdot \Delta g_{\mu\nu}$$

*then the geodesic displacement is approximately proportional to $\sigma$ for small perturbations (linear dose-response), which is consistent with the observed vivid > mild > control ordering.*

The proportional dose-response constrains the functional form of the metric's vulnerability. It rules out threshold models (where the metric is stable below a salience threshold and collapses above it) and saturation models (where the metric is equally disrupted by all non-zero distractors). It supports a linear or mildly nonlinear dose-response, consistent with the metric perturbation being a smooth function of distractor salience.


## 10.3 Warning Recovery: The Metacognitive Ceiling

The warning condition tests whether metacognitive intervention can undo attentional distortion. The model is told, explicitly, that the scenario contains irrelevant sensory details and is instructed to focus only on the morally relevant facts.

The recovery rate is approximately 39%: in about two out of five cases where a vivid distractor flipped the model's verdict, the warning restores the original verdict.

This recovery rate converges with the recovery ceiling observed in the Executive Functions track (Chapter 11): explicit inhibition instructions in the E2 emotional anchoring test recover about the same fraction of displaced verdicts. The convergence of the ~38--39% ceiling across two entirely different cognitive domains---attention (sensory distractors) and executive control (emotional anchoring)---suggests that the ceiling is a structural property of the model's metacognitive architecture, not a domain-specific limitation.

**The geometric interpretation.** The warning instruction acts as a metacognitive signal that attempts to reset the metric: "Undo the perturbation $\delta g_{\mu\nu}$ and return to the task-relevant metric $g_{\mu\nu}$." The partial success of this reset indicates that the model can partially undo the metric perturbation through a top-down signal but cannot fully undo it. The residual perturbation---the ~61% that is not recovered---is baked into the model's processing in a way that top-down instructions cannot override.

Why ~39%? The geometric framework suggests two possible explanations.

**Explanation 1: Layer-depth hypothesis.** The metric perturbation propagates through the model's layers. A top-down metacognitive instruction (the warning) can affect the upper layers but not the lower layers, which have already processed the distractor and committed the perturbation to the representation. The ~39% recovery represents the fraction of the perturbation that resides in the upper, metacognitively accessible layers. The remaining ~61% resides in the lower layers, beyond metacognitive reach.

**Explanation 2: Residual stream contamination.** In transformer architectures, the residual stream accumulates information from all layers. The distractor contributes to the residual stream at the layers where it is processed, and this contribution is not removed by subsequent layers---it is added to, not overwritten. The warning instruction adds a corrective contribution to the residual stream, but the original distractor contribution remains. The ~39% recovery represents the ratio of the corrective contribution's magnitude to the distractor's magnitude, which is bounded by the capacity of a single instruction to influence the residual stream.

Both explanations predict the convergence of the recovery ceiling across domains: the architectural limitation is the same regardless of whether the perturbation is a sensory distractor (A1) or an emotional anchor (E2), because the layer structure and residual stream dynamics are shared across all cognitive tasks.


## 10.4 Length Robustness: Validating a Null

The A2 subtask tests whether neutral padding---doubling or quadrupling the scenario length with morally irrelevant but topically neutral information---displaces the model's judgment. This is a control test: it distinguishes content-based attentional failures (A1, where morally irrelevant but salient information corrupts judgment) from length-based failures (where sheer volume of text, regardless of content, causes degradation).

The A2 results are strong across all models:

| Model | A2 Score | Interpretation |
|---|---|---|
| Gemini 2.5 Pro | 0.852 | Strong length robustness |
| Claude 3.5 Sonnet | 0.829 | Strong length robustness |
| Gemini 2.5 Flash | 0.786 | Moderate-strong robustness |
| Gemini 3 Flash | 0.714 | Moderate robustness |
| Gemini 2.0 Flash | 0.667 | Moderate robustness |

No model shows dramatic length-based degradation. The scores range from 0.667 to 0.852---all well above the threshold that would indicate significant length vulnerability. The metric is persistent over the length scales tested (2x and 4x padding, corresponding to sequences of roughly 500--2000 tokens).

**Why this null matters.** The A2 null result validates the A1 and A4 findings. If models degraded simply because of longer inputs, the A1 distractor effect could be a length artifact (distractor scenarios are longer than controls) rather than a content effect (distractors contain salient irrelevant information). The strong A2 result rules out this confound: models can handle longer inputs without significant degradation, so the A1 displacement is driven by the *content* of the distractors, not their *length*.

**The geometric interpretation.** In terms of the attention metric, length robustness means the metric is approximately time-invariant over the input sequence. The metric at position 100 in the sequence is approximately the same as the metric at position 200 or position 400. The cognitive manifold does not drift as the model processes more tokens. This metric persistence is what allows the static metric assumption of Chapters 3--4 to hold as a reasonable approximation for the reasoning episodes tested in the benchmarks.

The A2 result connects to the sustained attention interpretation developed in Chapter 4 (Section 4.7): sustained attention is metric persistence, and the A2 scores indicate that metric persistence is adequate over the time scales tested. The metric may drift on longer time scales---a possibility left as an open question for Chapter 17---but for the current benchmarks, the drift is small enough that the static metric approximation is justified.


## 10.5 Signal-to-Noise Ratio: Universal Metric Weakness

The A3 subtask measures the model's ability to discriminate relevant from irrelevant information across seven moral dimensions. Each scenario is annotated with ground-truth relevance labels indicating which of the seven dimensions (harm, fairness, loyalty, authority, care, liberty, purity) are relevant to the moral judgment and which are not. The SNR measures the ratio of the model's attention to relevant dimensions versus irrelevant dimensions.

The A3 results reveal a universal and strikingly uniform weakness:

| Model | SNR | Quality |
|---|---|---|
| Claude 3.5 Sonnet | 1.22 | Weak discrimination |
| Gemini 2.0 Flash | 1.31 | Weak discrimination |
| Gemini 2.5 Flash | 1.27 | Weak discrimination |
| Gemini 3 Flash | 1.38 | Weak discrimination |
| Gemini 2.5 Pro | 1.35 | Weak discrimination |

The range is narrow: 0.16 across all five models. All values are only slightly above 1.0 (which would indicate zero discrimination---equal attention to relevant and irrelevant dimensions). No model achieves strong signal-noise discrimination.

**The universality is the finding.** If the weak SNR were due to model-specific architectural limitations, we would expect variation across architectures. The Claude architecture is fundamentally different from the Gemini architecture---different training data, different alignment procedures, different attention mechanisms. Yet the SNR values converge to the same narrow band. This convergence across architectures suggests a *structural* limitation of the transformer attention mechanism itself, not an incidental property of any particular model.

**The geometric interpretation.** The SNR measures the ratio of metric components along the signal dimensions to metric components along the noise dimensions (Definition 4.4 from Chapter 4). An SNR of 1.0 means the metric treats signal and noise identically. An SNR much greater than 1.0 means the metric strongly favors signal. The observed SNR values of 1.22--1.38 mean the metric barely favors signal over noise---it provides about 22--38% more resolution along the relevant dimensions than along the irrelevant ones.

This weak metric discrimination explains the vulnerability to distractors (A1). If the metric barely distinguishes relevant from irrelevant dimensions, then activations along irrelevant dimensions (distractors) have nearly as much influence on the geodesic as activations along relevant dimensions (the actual moral content). The distractor's metric weight is only 22--38% less than the signal's metric weight---far from the ideal case where the distractor's weight would be near zero.

**Definition 10.2** (Metric Signal-to-Noise Ratio). *Let $g_s$ be the average metric component along signal dimensions and $g_n$ be the average metric component along noise dimensions. The metric SNR is:*

$$\text{SNR}_g = \frac{g_s}{g_n}$$

*The geodesic's vulnerability to noise perturbation is proportional to $1 / (\text{SNR}_g - 1)$. For $\text{SNR}_g$ near 1.0, the vulnerability is high. For $\text{SNR}_g \gg 1$, the vulnerability is low. The observed $\text{SNR}_g$ values of 1.22--1.38 correspond to high vulnerability, consistent with the 4.6 sigma distractor effect.*

The universal weakness of the SNR has implications beyond the Attention track. If the attention metric provides only 22--38% more resolution along relevant dimensions than irrelevant ones, then *all* cognitive processing occurs in a noisy metric environment. The geodesic equation, which depends on the metric and its derivatives, is computed with noisy inputs. The curvature estimates, which determine System 1/System 2 transitions, are contaminated by noise. The heuristic field, which guides search, is evaluated on a manifold measured with a blurry ruler.

This universal noise floor is the geometric backdrop against which all the other benchmark results should be interpreted. The framing effects (15.3 sigma), the sycophancy gradient (13.3 sigma), the calibration errors (6.7 sigma), the emotional anchoring (6.8 sigma)---all occur on a manifold where the baseline metric is already weak. The models are navigating complex cognitive terrain with a ruler that can barely distinguish the path from the surrounding noise.


## 10.6 The Divided Attention Split: The Metric Made Visible

The A4 subtask is the single most discriminating test in the entire benchmark suite. It measures divided attention: whether the model can process two interleaved scenarios without the judgment of one contaminating the judgment of the other.

The protocol is straightforward. Twenty scenario pairs are evaluated in two conditions: first, each scenario is judged individually (sequential evaluation); then, both scenarios are interleaved in a single prompt and judged simultaneously (concurrent evaluation). The A4 score measures the consistency between the sequential and concurrent verdicts. A score of 1.000 means perfect consistency---interleaving does not change the verdict. A low score means significant interference---the model's judgment of scenario A is contaminated by the simultaneous processing of scenario B.

Here are the results:

| Model | A4 Score | Metric Width |
|---|---|---|
| Gemini 2.5 Pro | 1.000 | Isotropic (wide) |
| Gemini 3 Flash | 1.000 | Isotropic (wide) |
| Gemini 2.5 Flash | 0.875 | Near-isotropic |
| Gemini 2.0 Flash | 0.812 | Moderate |
| Claude 3.5 Sonnet | 0.571 | Rank-1 (narrow) |

The spread is 0.429---from Claude's 0.571 to Pro's and Flash 3's 1.000. This is the largest single-test discriminator across all twenty-one subtasks in all five benchmark tracks.

**The rank-1 metric.** Claude's A4 score of 0.571 means that nearly half of its verdicts change when two scenarios are interleaved. This is not a small effect. When Claude processes two scenarios simultaneously, the judgment of each is substantially contaminated by the other. The model cannot maintain independent processing of two parallel streams.

In metric terms, Claude's attention metric under divided attention is approximately rank-1. A rank-1 metric has one large eigenvalue and all others near zero:

$$g_{\mu\nu}^{\text{Claude}} \approx \lambda_1 \mathbf{v}_1 \mathbf{v}_1^T$$

where $\lambda_1$ is large and all other eigenvalues are negligible. This means the metric provides high resolution along exactly one direction ($\mathbf{v}_1$, the primary attention direction) and near-zero resolution along all orthogonal directions. The model can attend to one stream with full fidelity, but any second stream receives essentially no metric resolution and is therefore processed with maximal noise.

The consequence is that when two streams are present, one stream captures almost all the metric resources, and the other stream's processing is degraded to the point of corruption. The model does not divide attention; it *switches* attention---attending fully to one stream while the other is neglected, then switching. The switching is imperfect, leading to cross-contamination and the observed verdict displacements.

**The isotropic metric.** Pro and Flash 3 achieve perfect A4 scores of 1.000. Their verdicts do not change under interleaving. The two scenarios are processed independently, as if each had its own dedicated metric.

In metric terms, these models have an approximately isotropic metric under divided attention:

$$g_{\mu\nu}^{\text{Flash 3}} \approx \frac{\lambda}{k} \mathbf{I}_k$$

where $\lambda$ is the total attention budget and $k$ is the number of simultaneous streams. The budget is divided equally across streams, and each stream receives $\lambda / k$ resolution. If $\lambda / k$ exceeds the task-relevance threshold---the minimum resolution needed to perform the task correctly---then all streams are processed with sufficient quality, and the A4 score is perfect.

The isotropic metric is not "better" in all contexts. It trades per-stream resolution for multi-stream coverage. In tasks where maximal resolution on a single dimension is critical (e.g., sycophancy resistance, where the model must attend with extreme precision to the truthfulness dimension), the rank-1 metric may be superior. Claude's zero sycophancy (L2 = 1.000) may be a consequence of its narrow metric: by concentrating all attention on the truthfulness dimension, it achieves maximal resistance to social pressure.

**Definition 10.3** (Metric Rank). *Let $g_{\mu\nu}$ be the attention metric tensor at a point on the cognitive manifold, and let $\lambda_1 \geq \lambda_2 \geq \cdots \geq \lambda_n$ be its eigenvalues. The effective rank of the metric is:*

$$\text{rank}_{\text{eff}}(g) = \frac{(\sum_i \lambda_i)^2}{\sum_i \lambda_i^2}$$

*This is the participation ratio of the eigenvalues. For a rank-1 metric, $\text{rank}_{\text{eff}} = 1$. For an isotropic metric with $k$ nonzero eigenvalues, $\text{rank}_{\text{eff}} = k$.*

Claude's effective metric rank is approximately 1 (narrow channel, single-stream processing). Flash 3's effective metric rank is approximately 2 or more (wide aperture, multi-stream processing). The metric rank is the quantitative measure of the "shape" of attention that determines whether the model processes one thing very well or multiple things adequately.


## 10.7 The A4 Dissociation from Other Attention Measures

A key feature of the A4 result is that it dissociates from the other attention measures. Claude's A4 score (0.571, worst) does not predict its A2 score (0.829, second-best) or its A3 score (0.692, best). Claude has strong sustained attention (A2) and the best selective attention (A3) but the worst divided attention (A4).

This dissociation makes geometric sense. A2 (length robustness) measures metric persistence---whether the metric is stable over time. A3 (selective attention) measures the metric's ability to discriminate relevant from irrelevant dimensions on a single stream. A4 (divided attention) measures the metric's ability to maintain resolution across multiple streams. These are three different properties of the metric tensor:

- **A2 tests temporal stability:** $\partial g_{\mu\nu} / \partial t \approx 0$ (the metric does not drift).
- **A3 tests signal selectivity:** $g_{\text{signal}} / g_{\text{noise}} > 1$ (the metric favors signal over noise).
- **A4 tests dimensional breadth:** $\text{rank}_{\text{eff}}(g) \geq 2$ (the metric has resolution along multiple independent dimensions).

A rank-1 metric can be temporally stable (high A2) and signal-selective (reasonable A3) while having zero breadth (low A4). This is exactly Claude's profile: a narrow, stable, signal-favoring metric that cannot distribute across multiple streams. The metric has one excellent direction and no others.

Conversely, an isotropic metric can have moderate signal selectivity (the same SNR in all directions) and perfect breadth while being no more or less stable than a narrow metric. This is Flash 3's profile: a broad metric with uniform coverage and adequate discrimination.

The dissociation confirms that the attention metric is not a single number (as in "attentional capacity") but a tensor with multiple independent properties. The tensor's eigenvalue spectrum (which determines A4), its temporal derivative (which determines A2), and its signal/noise ratio (which determines A3) are independent properties that vary independently across models. Measuring any one of them does not determine the others. The attention metric tensor is the minimum mathematical object needed to capture the data.


## 10.8 Architectural Implications of the A4 Split

The A4 divided attention split maps directly onto architectural differences between the models.

**Multi-head attention and metric width.** In transformer architectures, multi-head attention provides a natural mechanism for divided attention. Each attention head computes a separate set of attention weights over the input, potentially attending to different aspects of the input simultaneously. A model with $H$ heads can, in principle, maintain independent attention along $H$ directions simultaneously.

The A4 split suggests that the models differ in how effectively they utilize multi-head attention for parallel processing. Flash 3 and Pro appear to use their attention heads to independently process the two interleaved scenarios, maintaining separate metric computations for each. Claude appears to concentrate its attention heads on a single processing stream, achieving higher per-stream resolution but losing the ability to process two streams independently.

This architectural hypothesis is consistent with the broader cognitive signatures (Chapter 1). Claude's "narrow channel" signature---zero sycophancy, worst divided attention, excellent self-monitoring---is the signature of a model that concentrates its attention resources into a single high-resolution stream. Flash 3's "wide aperture" signature---perfect divided attention, best working memory, mediocre sycophancy resistance---is the signature of a model that distributes attention resources broadly.

**The attention budget.** The models share a common total attention budget $W$ (determined by the number of attention heads times the dimension per head), but they allocate this budget differently. Claude allocates $W$ to a single stream: $W / 1 = W$ per stream, achieving maximum resolution on one stream. Flash 3 allocates $W$ across two streams: $W / 2$ per stream, with each stream receiving half the resolution but both receiving adequate coverage.

The threshold condition for successful divided attention is $W / 2 \geq W_{\min}$, where $W_{\min}$ is the minimum attention weight needed to perform the task correctly. Flash 3 satisfies this threshold (its A4 is 1.000); Claude does not (its A4 is 0.571, indicating that $W / 2 < W_{\min}$ for a substantial fraction of tasks). This does not necessarily mean Flash 3 has a larger total budget $W$---it may mean Flash 3 has a lower task threshold $W_{\min}$ due to more efficient per-stream processing.


## 10.9 The Attention Robustness Surface

Integrating the four subtask results, we can construct the *attention robustness surface* for each model---a mapping from perturbation type and intensity to judgment displacement.

**Definition 10.4** (Attention Robustness Surface). *The attention robustness surface of a model is the function $R: \mathcal{P} \times [0, 1] \to [0, 1]$ that maps each perturbation type $p \in \mathcal{P}$ and perturbation intensity $\sigma \in [0, 1]$ to the expected displacement $R(p, \sigma)$ of the model's judgment.*

The four subtasks sample this surface at specific points:

- A1 samples the surface at perturbation type = "content distractor" and intensities {control, mild, vivid}.
- A2 samples the surface at perturbation type = "neutral length" and intensities {1x, 2x, 4x}.
- A3 samples the surface at perturbation type = "noise dimensions" and measures the slope of the surface at the origin.
- A4 samples the surface at perturbation type = "concurrent task" and measures the displacement under dual-task conditions.

The surface has a characteristic shape for each model:

**Claude's robustness surface** is steep along the "concurrent task" dimension (high displacement at A4) but shallow along the "neutral length" dimension (low displacement at A2). It is moderately steep along the "content distractor" dimension (moderate displacement at A1). The surface has a pronounced ridge along the divided attention axis---this is where Claude is most vulnerable.

**Flash 3's robustness surface** is flat along the "concurrent task" dimension (zero displacement at A4) and moderately steep along the "content distractor" dimension. It has no pronounced ridge. The surface is relatively uniform---Flash 3 is moderately vulnerable to content distractors and not at all vulnerable to concurrent tasks.

The difference between these surfaces---the Claude surface minus the Flash 3 surface---is concentrated almost entirely along the "concurrent task" dimension. On every other dimension, the models are similar. It is only when the task demands parallel processing that the architectural difference in metric shape becomes visible.


## 10.10 Cross-Track Connections

The attention results interact with the other cognitive dimensions in specific, predictable ways.

**Attention and metacognition.** The universally weak SNR (A3) connects directly to the metacognitive findings of Chapter 9. If the attention metric provides only weak signal-noise discrimination, then the heuristic field is evaluated on a noisy manifold, and the resulting distance estimates are noisy. This noise in the heuristic propagates to the confidence estimates, contributing to the calibration error (M1 ECE). A model with better SNR would have a cleaner heuristic field, which would produce better distance estimates, which would produce better calibration. The universal weakness of the SNR may be one of the upstream causes of the universal overconfidence.

**Attention and social cognition.** The framing effects measured in the Social Cognition track (T5: 15.3 sigma) can be interpreted as attentional failures. A framing manipulation changes the surface features of a scenario---the way the facts are presented---without changing the underlying moral content. A model with a strong attention metric would filter out the surface features and attend only to the moral content. A model with a weak metric (SNR near 1.0) cannot fully filter the surface features, and the framing manipulation corrupts the geodesic from problem to judgment. The 4.6 sigma distractor effect (A1) and the 15.3 sigma framing effect (T5) are the same geometric phenomenon at different magnitudes: perturbation of the attention metric by task-irrelevant information.

**Attention and executive control.** Claude's worst divided attention (A4 = 0.571) interacts with its executive control profile in an important way. The E4 working memory subtask measures how well the model tracks multiple parties in complex scenarios. Claude's E4 score (0.886) is reasonable---it can track multiple parties. But A4 shows it cannot *simultaneously process* multiple streams. This dissociation between tracking (maintaining representations of multiple entities in the tangent space) and processing (allocating metric resources to multiple streams) is an architectural distinction that the geometric framework makes precise: working memory is tangent space capacity, and attention is metric allocation. They are different geometric objects and can vary independently.

**Attention and learning.** Claude's zero sycophancy (L2 = 1.000) and its worst divided attention (A4 = 0.571) are two sides of the same metric coin. The narrow metric that concentrates all attention on the truthfulness dimension produces both effects: it gives Claude the resolution to detect and resist social pressure (high sycophancy resistance) while making it unable to process a second task dimension simultaneously (low divided attention). The Learning and Attention results jointly constrain the metric's shape, and the constraint is consistent: narrow, high-resolution, single-stream.


## 10.11 Worked Example: Computing the Metric Eccentricity

**Setup.** We have a model with the following attention profile:

| Subtask | Score |
|---|---|
| A1 (Distractor Resistance) | 0.700 |
| A2 (Length Robustness) | 0.800 |
| A3 (Selective Attention SNR) | 1.30 |
| A4 (Divided Attention) | 0.650 |

**Step 1: Assess metric stability.** The A2 score of 0.800 indicates moderate-to-strong metric persistence. The metric does not drift significantly over the input lengths tested. We can assume the static metric approximation is reasonable.

**Step 2: Assess metric signal quality.** The SNR of 1.30 indicates weak signal-noise discrimination, consistent with the universal band of 1.22--1.38. The metric provides approximately 30% more resolution along signal dimensions than noise dimensions.

**Step 3: Compute metric eccentricity from A4.** The A4 score of 0.650 indicates significant interference under divided attention. Following the worked example from Chapter 4 (Section 4.12), we model the metric as a diagonal matrix with attention weights $a_1$ (primary stream) and $a_2$ (secondary stream), subject to $a_1 + a_2 = A$.

The A4 score of 0.650 corresponds to a metric where the secondary stream receives significantly less resolution than the primary stream. Using the harmonic-mean model from Chapter 4:

$$\text{A4} = \frac{2}{\frac{1}{f(a_1)} + \frac{1}{f(a_2)}}$$

where $f(a)$ is the per-stream accuracy as a function of attention weight. For a sigmoid function $f(a) = 1 / (1 + e^{-k(a - a_0)})$, the A4 score of 0.650 implies $a_1 / a_2 \approx 3.0$---the primary stream receives about 75% of the attention budget.

**Step 4: Compute the effective metric rank.** With eigenvalues proportional to $a_1 = 0.75A$ and $a_2 = 0.25A$, the participation ratio is:

$$\text{rank}_{\text{eff}} = \frac{(0.75 + 0.25)^2}{0.75^2 + 0.25^2} = \frac{1.0}{0.625} = 1.6$$

The effective metric rank is 1.6, between Claude's approximately 1.0 (extreme narrowness) and Flash 3's approximately 2.0 (perfect isotropy). This model has a moderately narrow metric---neither as extreme as Claude nor as broad as Flash 3.

**Step 5: Predict cross-track behavior.** Based on the metric eccentricity of 3.0 and effective rank of 1.6:
- The model should show moderate sycophancy resistance (its metric is moderately concentrated, providing moderate per-stream resolution on the truthfulness dimension---not as strong as Claude's extreme concentration, but better than an isotropic model).
- The model should show moderate vulnerability to framing effects (its SNR of 1.30 provides only weak filtering of framing cues).
- The model should show moderate working memory performance (its tangent space capacity is independent of its metric width, so E4 is not directly predicted by A4).

These predictions are testable and provide a concrete validation pathway for the metric framework.


## 10.12 The Attention Filter as Geometric Object

This chapter's findings consolidate the theoretical framework of Chapter 4 with empirical data. The attention metric is not an abstract mathematical convenience. It is a measurable property of cognitive systems with specific empirical signatures:

1. **The metric is proportionally vulnerable to distraction** (A1, 4.6 sigma). The dose-response is graded, consistent with a linear perturbation model.

2. **The metric is temporally stable** (A2, scores 0.667--0.852). The static metric approximation is justified for the time scales tested.

3. **The metric provides universally weak signal discrimination** (A3, SNR 1.22--1.38). The noise floor is high and uniform across architectures, suggesting a structural limitation of the transformer attention mechanism.

4. **The metric's eigenvalue structure varies dramatically across models** (A4, spread 0.429). Claude's rank-1 metric and Flash 3's isotropic metric represent fundamentally different attentional architectures.

5. **The metric's recovery from perturbation is bounded at ~39%** (A1 warning recovery). This ceiling converges with the executive functions recovery ceiling, suggesting a common architectural limit.

These five findings transform the attention metric from a theoretical object into an empirical one. The metric has specific, measurable properties that differ across models and that determine how each model navigates the cognitive manifold. The metric is, in the language of Chapter 4, the ruler that turns the cognitive manifold into a Riemannian space. The ruler differs between models. And the differences in the ruler produce the differences in cognition.

Chapter 11 brings the story to its synthesis. The executive control track integrates the metric, the tangent space, and the control layer into a unified picture of how models govern their own reasoning. The attention metric provides the sensory input to the control system. The metacognitive distance estimates provide the feedback signal. And the executive functions provide the governance mechanism that holds the entire system together---or fails to.

---

## Technical Appendix 10A: Distractor Dose-Response---Statistical Framework

**Definition** (Dose-Response Model). *Let $D(\sigma)$ be the expected verdict displacement as a function of distractor salience $\sigma \in \{0, \sigma_{\text{mild}}, \sigma_{\text{vivid}}\}$. The dose-response model is:*

$$D(\sigma) = D_0 + \beta \sigma + \epsilon$$

*where $D_0$ is the baseline displacement rate (control condition), $\beta$ is the dose-response coefficient, and $\epsilon$ is noise. The null hypothesis is $\beta = 0$ (no dose-response). The alternative is $\beta > 0$ (higher salience produces more displacement).*

**Graded bonus scoring.** The A1 composite score includes a graded bonus that rewards proportional dose-response: models receive additional credit when their displacement ordering matches vivid > mild > control. This rewards informative dose-response structure over binary distractor sensitivity.

**Fisher combination.** The 4.6 sigma Fisher combined significance is computed from the individual model z-scores for the distractor displacement effect. Each model's z-score is computed from the difference between the vivid-condition flip rate and the control-condition flip rate, divided by the standard error estimated from the five-replication control arm. Fisher's method combines the individual p-values:

$$\chi^2_{\text{Fisher}} = -2 \sum_{k=1}^{5} \ln(p_k)$$

Under the null hypothesis of no distractor effect, $\chi^2_{\text{Fisher}} \sim \chi^2_{10}$. The observed value corresponds to $p \approx 2 \times 10^{-6}$, or 4.6 sigma.


## Technical Appendix 10B: Divided Attention---Metric Rank Analysis

**Proposition 10.1** (A4 Score as Metric Rank Indicator). *Let $g_{\mu\nu}$ be the attention metric under divided attention conditions, with eigenvalues $\lambda_1 \geq \lambda_2$. Define the metric isotropy as $\iota = \lambda_2 / \lambda_1 \in [0, 1]$. For a task requiring minimum resolution $\lambda_{\min}$ along each of two dimensions, the A4 score is:*

$$\text{A4}(\iota) = \begin{cases} 1.0 & \text{if } \lambda_2 \geq \lambda_{\min} \\ f(\lambda_2 / \lambda_{\min}) & \text{if } \lambda_2 < \lambda_{\min} \end{cases}$$

*where $f$ is a monotonically increasing function with $f(0) = f_0$ (minimum score from primary-stream-only processing) and $f(1) = 1.0$.*

For Claude: $\iota \approx 0$ (rank-1 metric), so $\lambda_2 \approx 0 < \lambda_{\min}$, and $\text{A4} = f_0 \approx 0.571$ (processing based almost entirely on the primary stream, with the secondary stream contributing noise).

For Flash 3: $\iota \approx 1$ (isotropic metric), so $\lambda_2 \approx \lambda_1 \geq \lambda_{\min}$, and $\text{A4} = 1.0$ (both streams processed with sufficient resolution).

**Corollary.** The A4 score is a monotonically increasing function of the metric isotropy $\iota = \lambda_2 / \lambda_1$. Models with higher A4 scores have more isotropic attention metrics. The 0.429 spread between Claude (0.571) and Flash 3 (1.000) maps to a change in metric isotropy from approximately 0 to approximately 1---the full range of possible metric shapes.


## Technical Appendix 10C: The Recovery Ceiling---Cross-Domain Convergence

The recovery ceiling of approximately 38--39% converges across two independent domains:

| Domain | Test | Recovery Rate | Interpretation |
|---|---|---|---|
| Attention (A1) | Warning instruction after vivid distractor | ~39% | Metacognitive correction of attentional displacement |
| Executive (E2) | Inhibition instruction after emotional anchor | ~38% | Metacognitive correction of emotional displacement |

The convergence is notable because the perturbation types are different (sensory distractors vs. emotional anchors), the cognitive domains are different (attention vs. executive control), and the recovery mechanisms are triggered differently (warning instruction vs. inhibition instruction). Yet the recovery rates converge to the same narrow range.

This convergence supports the hypothesis that the ~38--39% ceiling is an architectural constant of the model's metacognitive control system, not a domain-specific property. The ceiling represents the fraction of the perturbation that is accessible to top-down correction---the fraction that resides in layers of the model that can be influenced by an explicit instruction. The remaining ~61--62% is committed to the residual stream at layers below metacognitive access.

If this interpretation is correct, the ceiling should be approximately constant across all domains and perturbation types, not just the two tested. Testing this prediction across additional domains (e.g., social cognition framing, learning sycophancy) would provide a strong test of the architectural-constant hypothesis.
