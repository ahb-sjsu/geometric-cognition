# Chapter 9: Metacognition as Distance Estimation

> *"The unexamined life is not worth living."*
> --- Socrates, as reported by Plato in the *Apology* (399 BCE)

---

> **RUNNING EXAMPLE --- MAYA'S MODEL**
>
> Maya has built a map. Over the past four chapters she has measured the cognitive manifold (Chapter 3), the attention metric (Chapter 4), the tangent space (Chapter 5), and the control layer (Chapter 6). She has the terrain. She has the ruler. She has the vehicle's steering mechanism.
>
> Now she needs to ask a different question: does the vehicle know where it is?
>
> She is running the Metacognition benchmark---four subtasks designed to probe whether a model can estimate distances on its own cognitive manifold. M1 measures calibration: does the model's confidence match its accuracy? M2 measures ambiguity discrimination: can the model distinguish hard problems from easy ones? M3 measures self-monitoring: can the model identify which specific problems it is uncertain about? M4 measures effort scaling: does the model allocate more reasoning to harder problems?
>
> The first result is unsurprising. Every model is overconfident. Expected Calibration Errors range from 0.186 (Pro) to 0.437 (Flash 2.0), and the Fisher combination across models yields 6.7 sigma. The direction is universal: every model, across both architecture families, overestimates its own accuracy. The distance estimates are systematically short. The models think they are closer to the goal than they are.
>
> The second result is where Maya stops breathing.
>
> She has plotted every model's M3 (self-monitoring) against its M4 (effort scaling) on a two-dimensional scatter plot. M3 measures whether the model knows *which* problems it is uncertain about. M4 measures whether the model *does something about it*---whether it allocates more reasoning effort to harder problems. She expects to see a positive correlation. A model that knows which problems are hard should spend more effort on those problems. Self-knowledge should drive effort allocation.
>
> Instead, she sees a dissociation so clean it looks designed.
>
> Pro has the best self-monitoring in the sample: M3 = 0.500. It can identify its uncertain scenarios with moderate accuracy. But Pro has zero effort scaling: M4 = 0.000. It writes exactly the same amount regardless of whether the problem is trivial or impossible. The thermometer works. The valve is frozen.
>
> Flash 2.0 has the reverse profile. Its self-monitoring is near chance: M3 = 0.042. It cannot tell which problems it is uncertain about. But it has strong effort scaling: M4 = 0.827. It writes significantly more for complex problems than for simple ones. The valve works. The thermometer is broken.
>
> Maya draws the four quadrants on her scatter plot. Quadrant I (upper right) is where both self-monitoring and effort scaling are strong: the model knows what is hard *and* works harder on hard problems. Quadrant II (upper left) is where self-monitoring is strong but effort scaling is weak: the model knows what is hard but does not adjust. Quadrant III (lower left) is where both are weak. Quadrant IV (lower right) is where effort scaling is strong but self-monitoring is weak: the model adjusts effort without knowing why.
>
> She stares at Quadrant I. It is empty. No model has both.
>
> Maya writes in her notebook: *"Metacognition is not a single axis. It is at least two-dimensional. Self-monitoring and effort scaling are independent metacognitive capabilities that no current architecture unifies. The empty Quadrant I is not a sampling artifact. It is a structural constraint. And it means that the 'metacognitive manifold' has a hole where the best cognition should be."*

---

## 9.1 The Metacognitive Problem

The preceding chapters have built the geometric framework from the outside in. The cognitive manifold (Chapter 3) provides the space. The attention metric (Chapter 4) provides the ruler. Working memory (Chapter 5) provides the tangent space---the local neighborhood of reachable states. Executive functions (Chapter 6) provide the control layer---the mechanism that selects search strategies and adjusts parameters.

But all of these objects describe how a cognitive system navigates its manifold. None of them describe whether the system knows *how well* it is navigating. This is the problem of metacognition.

Metacognition is cognition about cognition. It is the ability to monitor one's own reasoning processes, evaluate one's own confidence, detect one's own errors, and adjust one's own strategies. In the geometric framework, metacognition is *distance estimation on the cognitive manifold*: the system's ability to estimate how far it is from the goal, how uncertain its current position is, and how much effort the remaining navigation will require.

This interpretation is not metaphorical. The Expected Calibration Error (ECE)---the standard metric for metacognitive calibration---is literally a measure of distance estimation error. A well-calibrated system's confidence accurately reflects its probability of being correct, which is equivalent to accurately estimating how far the current cognitive state is from the correct answer state on the cognitive manifold. An overconfident system underestimates this distance. An underconfident system overestimates it. The direction and magnitude of the calibration error tell us the direction and magnitude of the distance estimation error.

The Measuring AGI Metacognition benchmark decomposes this broad capability into four testable components:

**M1 (Calibration).** Does the model's stated confidence match its observed accuracy? This is the headline test of distance estimation quality. A perfectly calibrated model reports 90% confidence on sets of problems where it is correct 90% of the time. A miscalibrated model's confidence bears no systematic relationship to its accuracy---or, more commonly, systematically exceeds it.

**M2 (Ambiguity Discrimination).** Can the model distinguish genuinely ambiguous problems from clear-cut ones? This tests whether the model can detect *regions of high curvature* on the cognitive manifold---regions where multiple reasonable answers compete and the geodesic to the goal is not unique.

**M3 (Self-Monitoring).** Can the model identify which specific problems it is most uncertain about? This goes beyond M2's category-level discrimination to test item-level metacognitive access: not just "hard problems are hard" but "this particular problem is one I am likely to get wrong."

**M4 (Strategy Selection / Effort Scaling).** Does the model allocate more reasoning effort to harder problems? This tests whether metacognitive knowledge drives metacognitive control---whether the system's distance estimates are connected to its resource allocation.

These four components form a natural hierarchy. M1 asks whether the global statistics of distance estimation are accurate. M2 asks whether the system can distinguish categories of distance. M3 asks whether the system can estimate distances at the item level. M4 asks whether item-level distance estimates drive behavior. A fully metacognitive system would have all four. No system we tested does.


## 9.2 The Calibration Surface

The M1 calibration test provides the most established and interpretable measure of metacognitive quality. Its connection to the geometric framework is direct: calibration measures the accuracy of the system's internal distance estimates.

**Definition 9.1** (Expected Calibration Error). *Let a cognitive system produce confidence estimates $p_i$ and corresponding binary outcomes $y_i$ (correct/incorrect) over $N$ trials. Partition the confidence values into $B$ bins $\{I_b\}_{b=1}^B$. The Expected Calibration Error is:*

$$\text{ECE} = \sum_{b=1}^{B} \frac{|I_b|}{N} |\text{acc}(I_b) - \text{conf}(I_b)|$$

*where $\text{acc}(I_b)$ is the fraction of correct predictions in bin $I_b$ and $\text{conf}(I_b)$ is the average confidence in bin $I_b$.*

An ECE of 0 means perfect calibration: in every confidence bin, the accuracy exactly matches the stated confidence. An ECE of 1 means maximal miscalibration: the system is perfectly wrong about its own accuracy. The ECE measures, averaged over confidence levels, how far the model's distance estimates deviate from reality.

**The geometric interpretation.** On the cognitive manifold, the model's confidence can be interpreted as an estimate of the geodesic distance to the correct answer state. High confidence means "I am close to the answer"---the estimated geodesic distance is small. Low confidence means "I am far from the answer"---the estimated distance is large. The ECE measures the systematic error in these distance estimates: the difference between the estimated distance (confidence) and the actual distance (accuracy).

An overconfident model underestimates geodesic distances. It thinks it is closer to the correct answer than it actually is. In the search framework of Chapter 2, this means the heuristic field $h(x)$ is systematically biased low---the estimated cost-to-go is smaller than the actual cost-to-go. The consequences are predictable from the search theory: the system will terminate search prematurely (it thinks it has arrived when it has not), it will underestimate the need for System 2 engagement (it does not detect the curvature that would trigger deliberate computation), and it will fail to allocate effort to problems that, by its own estimate, are already solved.

Here are the M1 results:

| Model | ECE | Direction | z-score |
|---|---|---|---|
| Gemini 2.0 Flash | 0.437 | overconfident | 6.2 sigma |
| Gemini 2.5 Flash | 0.415 | overconfident | 7.0 sigma |
| Gemini 3 Flash | 0.333 | overconfident | 4.5 sigma |
| Gemini 2.5 Pro | 0.186 | overconfident | 2.2 sigma |
| Claude 3.5 Sonnet | 0.250 | overconfident | --- |
| **Fisher combined** | | | **6.7 sigma** |

Several features of this table merit extended discussion.


## 9.3 Universality and Gradient

**Universal overconfidence.** Every model is overconfident. Not one model tested---across two architecture families, three model generations, and a wide range of model scales---is well-calibrated or underconfident. The direction of miscalibration is universal.

This universality has a geometric explanation. The training objective of language models---next-token prediction with cross-entropy loss---optimizes the model to place probability mass on the correct next token. The training signal rewards confidence in the right answer but does not penalize overconfidence nearly as strongly. A model that is 99% confident and correct loses almost nothing in cross-entropy; a model that is 50% confident and correct loses substantially. The loss function shapes the heuristic field to be systematically biased toward high confidence, which translates directly to systematically underestimated geodesic distances.

**The calibration gradient.** The ECE values are not randomly scattered. They follow a clear gradient that tracks model scale and generation:

- Flash 2.0 (smallest/oldest): ECE = 0.437 (worst calibration)
- Flash 2.5 (mid-generation): ECE = 0.415
- Flash 3 (newest generation): ECE = 0.333
- Claude Sonnet (cross-family): ECE = 0.250
- Pro (largest): ECE = 0.186 (best calibration)

This gradient suggests that calibration is a learnable capability that improves with scale. Larger models, with more parameters to represent nuance and more training to refine internal representations, develop more accurate internal distance estimates. The geodesic distance estimation function $\hat{d}(x, x_{\text{goal}})$ becomes more accurate as the model's representation of the cognitive manifold becomes finer-grained.

**The geometric picture.** Think of each model as navigating the same cognitive manifold (the space of moral judgments in the AITA domain) but with different internal maps. Flash 2.0's map is the most distorted: it compresses distances, making everything look close. Pro's map is the least distorted: distances on Pro's internal map more closely match the actual geodesic distances on the true manifold. The ECE measures the average distortion of the map.

This map-distortion interpretation makes a specific prediction: models with better calibration should also show better *relative* distance estimation---they should be better at telling which problems are harder, not just at estimating absolute difficulty. This prediction is confirmed by the M2 and M3 results, which we turn to next.


## 9.4 Ambiguity Discrimination and the Confidence Compression Problem

The M2 subtask tests whether models can distinguish genuinely ambiguous problems from clear-cut ones. Fifteen scenarios with high community agreement (clear NTA or YTA verdicts) are compared against fifteen scenarios with split community judgments (ESH or NAH verdicts). A model with good ambiguity discrimination should report higher confidence on the clear-cut cases and lower confidence on the ambiguous ones.

The naive approach---measuring the raw confidence gap between clear and ambiguous cases---fails because of *confidence compression*. Models compress their confidence into a narrow range at the top of the scale. Raw confidence values cluster between 8 and 10 on a 0--10 scale. The gap between the mean confidence for clear-cut cases and the mean confidence for ambiguous cases is tiny: 0.13 to 0.54 on a 10-point scale. This gap is real (it is in the right direction for all models), but it is too small relative to the noise to provide a reliable discriminator.

**The geometric explanation of confidence compression.** Why do models compress confidence? Because the heuristic field is locally flat near the answer. When the model's search has converged to a candidate answer, the heuristic landscape around that answer has low curvature---the model is near a local minimum of the cost function, and the gradient is small in all directions. In this flat region, the model's distance estimate is small (it thinks it is near the goal), and small distances translate to high confidence. The compression arises because the model's distance estimation function maps a wide range of actual distances to a narrow range of estimated distances near zero---the estimate saturates at "close" before the true distance saturates at "arrived."

In mathematical terms, the estimated distance function $\hat{d}(x, x_{\text{goal}})$ is concave: it grows slowly for large true distances (underestimating difficulty) and saturates quickly for small true distances (everything looks "close" once you are in the neighborhood of the answer). This concavity compresses the confidence distribution toward the top of the scale.

**The AUROC fix.** The solution to confidence compression is to abandon absolute confidence values and measure *rank-order* discrimination instead. The Area Under the Receiver Operating Characteristic Curve (AUROC) asks a simple question: for every pair consisting of one clear-cut scenario and one ambiguous scenario, does the model assign higher confidence to the clear-cut one?

**Definition 9.2** (Rank-Based Ambiguity Discrimination). *Let $\{c_i^{\text{clear}}\}_{i=1}^{n_c}$ be the confidence values for clear-cut scenarios and $\{c_j^{\text{amb}}\}_{j=1}^{n_a}$ be the confidence values for ambiguous scenarios. The AUROC for ambiguity discrimination is:*

$$\text{AUROC} = \frac{1}{n_c \cdot n_a} \sum_{i=1}^{n_c} \sum_{j=1}^{n_a} \mathbf{1}[c_i^{\text{clear}} > c_j^{\text{amb}}]$$

*An AUROC of 1.0 means perfect rank-order discrimination: every clear-cut scenario receives higher confidence than every ambiguous scenario. An AUROC of 0.5 means chance-level discrimination: the model's confidence ranking is random with respect to the clear/ambiguous distinction.*

The AUROC measure is robust to monotonic transformations of the confidence scale. If a model compresses all its confidence values into the range 8.0--9.5, the AUROC is unaffected as long as the rank ordering is preserved. This is the correct measure for confidence-compressed systems, and it is a methodological contribution of this benchmark that applies to any calibration study of language models.

The geometric interpretation of the AUROC is elegant. On the cognitive manifold, clear-cut problems correspond to regions of low curvature (one answer dominates, the geodesic to the goal is unique and short), while ambiguous problems correspond to regions of high curvature (multiple answers compete, the geodesics diverge, the landscape is complex). The AUROC measures whether the model's distance estimates correctly order the curvature: does the model report shorter distances (higher confidence) in low-curvature regions and longer distances (lower confidence) in high-curvature regions?

The M2 results using the AUROC measure show moderate discrimination across all models tested, though the scores are modest. The key finding is that the rank-based measure rescues signal that the raw confidence gap obscures. Models *do* have some ability to distinguish curvature regimes, even though their absolute confidence values are compressed into a narrow range.


## 9.5 Self-Monitoring: Item-Level Distance Estimation

M2 tests category-level discrimination: can the model tell that ambiguous problems, *as a class*, are harder than clear-cut problems? M3 goes further: can the model tell which *specific* problems are hardest?

The M3 protocol works as follows. Each model evaluates twelve scenarios five times each, with independent replications. The variance of the model's verdicts across replications provides an objective measure of the model's uncertainty on each scenario: a scenario where the model gives the same verdict five times is one the model is confident about (low behavioral uncertainty), while a scenario where the model gives different verdicts across replications is one the model is genuinely uncertain about (high behavioral uncertainty).

After the five replications, the model is given a final query: "Which of these scenarios were you most uncertain about?" The model produces a ranking. The correlation between the model's self-reported uncertainty ranking and the actual verdict variance measures metacognitive access---the degree to which the model knows its own uncertainty at the item level.

**Definition 9.3** (Self-Monitoring Accuracy). *Let $\sigma_i^2$ be the behavioral variance (verdict variance across replications) for scenario $i$, and let $r_i$ be the model's self-reported uncertainty rank for scenario $i$. The self-monitoring accuracy is the Spearman correlation:*

$$\rho = \text{Spearman}(\{r_i\}, \{\sigma_i^2\})$$

*A correlation of 1.0 means perfect self-monitoring: the model's uncertainty ranking perfectly matches its actual uncertainty. A correlation of 0.0 means no self-monitoring: the model's uncertainty ranking is random with respect to its actual uncertainty.*

The self-monitoring scores are normalized to a 0--1 scale for comparability. The geometric interpretation is direct: self-monitoring measures whether the model's internal map accurately represents the *local* distance estimation error, not just the global statistics. A model with high M3 has an internal map that is locally accurate---it knows which regions of the cognitive manifold are well-mapped and which are poorly mapped. A model with low M3 has an internal map that is locally inaccurate---it cannot distinguish well-mapped regions from poorly mapped ones, even if its global calibration (M1) is reasonable.


## 9.6 Effort Scaling: From Knowledge to Action

M4 tests whether metacognitive knowledge drives metacognitive control. Specifically, it measures whether the model allocates more reasoning effort---operationalized as response length---to harder problems.

The protocol compares response length for simple scenarios (two parties, short, unambiguous) against response length for complex scenarios (multiple parties, long, nuanced). The ratio of complex-to-simple response length measures effort scaling: a ratio significantly greater than 1.0 means the model writes more for harder problems; a ratio near 1.0 means the model writes the same amount regardless of difficulty.

**Definition 9.4** (Effort Scaling Index). *Let $\bar{L}_{\text{complex}}$ be the mean response length for complex scenarios and $\bar{L}_{\text{simple}}$ be the mean response length for simple scenarios. The effort scaling index is:*

$$\text{ESI} = \frac{\bar{L}_{\text{complex}} - \bar{L}_{\text{simple}}}{\bar{L}_{\text{simple}}}$$

*normalized to a 0--1 scale. An ESI of 0 means no effort scaling: the model writes the same amount for simple and complex problems. A high ESI means strong effort scaling: the model significantly increases its output for complex problems.*

The geometric interpretation ties directly to the search framework of Chapter 2. In A* search, the effort allocated to a problem should be proportional to the geodesic distance from the current state to the goal. Short distances (easy problems) should require short search trajectories. Long distances (hard problems) should require long trajectories. The effort scaling index measures whether the model's search trajectory length varies appropriately with the estimated problem difficulty.

A model with high M4 has a working *throttle*: it adjusts the depth of its search based on (some estimate of) the distance to the goal. A model with low M4 has a frozen throttle: it applies the same search depth regardless of difficulty. In terms of the geometric search framework, a frozen throttle means the model uses a fixed-length geodesic segment for every problem, whether the problem requires a short hop across flat terrain or a long traverse through curved territory.


## 9.7 The M3/M4 Dissociation

Here is the result that reorganizes our understanding of metacognition.

| Model | M3 (Self-Monitoring) | M4 (Effort Scaling) |
|---|---|---|
| Gemini 2.5 Pro | 0.500 | 0.000 |
| Gemini 2.0 Flash | 0.042 | 0.827 |
| Gemini 3 Flash | 0.149 | 0.485 |
| Gemini 2.5 Flash | 0.111 | 0.612 |

The dissociation is stark.

Pro has the best self-monitoring in the sample. Its M3 score of 0.500 means it can identify its uncertain scenarios with moderate accuracy---a genuine metacognitive capability. But Pro's effort scaling is exactly zero. It writes the same amount for simple and complex problems. The same response length, the same depth of reasoning, the same trajectory through cognitive space, regardless of difficulty. The thermometer works. The valve is frozen.

Flash 2.0 has the reverse profile. Its M3 score of 0.042 is indistinguishable from chance. It cannot tell which scenarios it is uncertain about. Its self-knowledge is essentially zero. But its effort scaling is 0.827---the strongest in the sample. It writes significantly more for complex problems, allocating greater search depth to harder tasks. The valve works. The thermometer is broken.

This dissociation demolishes the assumption that metacognition is a unitary capability. If metacognition were a single dimension---a "metacognitive ability" that could be measured with a single number---then M3 and M4 would be positively correlated. Models that are better at self-monitoring would also be better at effort scaling, because both draw on the same underlying metacognitive capacity. The data say otherwise. The correlation between M3 and M4 across models is *negative*: the model with the best self-monitoring has the worst effort scaling, and vice versa.


## 9.8 The Empty Quadrant

The M3/M4 dissociation is not a marginal effect. It defines a structural feature of the metacognitive landscape: the empty Quadrant I.

Plot the models in the two-dimensional space defined by M3 (x-axis) and M4 (y-axis). Divide the space into four quadrants at the midpoints (0.5 on each axis, or more conservatively, at the median values):

**Quadrant I (high M3, high M4):** Good self-monitoring AND good effort scaling. The model knows which problems are hard and works harder on them. This is the ideal metacognitive configuration.

**Quadrant II (high M3, low M4):** Good self-monitoring but poor effort scaling. The model knows which problems are hard but does not adjust its effort. The thermometer works; the valve is frozen. This is where Pro sits.

**Quadrant III (low M3, low M4):** Poor self-monitoring and poor effort scaling. The model neither knows which problems are hard nor adjusts its effort. This is the metacognitive null state.

**Quadrant IV (low M3, high M4):** Poor self-monitoring but good effort scaling. The model adjusts its effort without knowing why---it scales response length based on some signal that is not metacognitive self-knowledge. This is where Flash 2.0 sits.

Quadrant I is empty.

No model in the sample occupies the upper-right quadrant where both metacognitive capabilities are strong. This is not a sampling artifact that would disappear with more models. It is a structural constraint that reflects a fundamental tension in the architecture of current language models.

**The geometric explanation of the empty quadrant.** Why can't a model have both good self-monitoring and good effort scaling?

The answer lies in the relationship between representation and control. Self-monitoring (M3) requires an accurate *representation* of the model's own uncertainty---an internal model of where the distance estimates are reliable and where they are not. This is a representational capability: the model must maintain a meta-level map of its own confidence landscape.

Effort scaling (M4) requires an effective *control* mechanism that translates difficulty signals into resource allocation. This is a control capability: the model must have a mechanism that adjusts generation length based on input complexity.

These two capabilities draw on different architectural resources and may be trained by different aspects of the training signal. Self-monitoring requires the model to introspect on its own internal states---to notice when its representations are noisy or conflicted. Effort scaling requires the model to detect complexity features in the input and adjust its generation strategy accordingly.

Crucially, the signal that drives effort scaling in Flash 2.0 is probably not self-monitoring at all. Flash 2.0 may scale effort based on *input complexity features*---the length of the scenario, the number of parties, the presence of competing considerations---rather than on *internal uncertainty estimates*. This would explain why it has strong effort scaling (it detects input complexity) but weak self-monitoring (it does not know which problems it is uncertain about from the inside). The valve responds to external pressure gauges, not to the internal thermometer.

**Definition 9.5** (Metacognitive Configuration Space). *Let the metacognitive state of a model be the pair $(m_3, m_4) \in [0, 1]^2$, where $m_3$ is the self-monitoring accuracy and $m_4$ is the effort scaling index. The metacognitive configuration space is $[0, 1]^2$, divided into four quadrants:*

- *Quadrant I: $m_3 > \tau, m_4 > \tau$ (integrated metacognition)*
- *Quadrant II: $m_3 > \tau, m_4 \leq \tau$ (knowledge without control)*
- *Quadrant III: $m_3 \leq \tau, m_4 \leq \tau$ (metacognitive absence)*
- *Quadrant IV: $m_3 \leq \tau, m_4 > \tau$ (control without knowledge)*

*where $\tau$ is a threshold separating weak from strong performance.*

The empty Quadrant I has a topological interpretation. The metacognitive configuration space has a "hole"---a region that no model can currently reach. In manifold terms, the achievable metacognitive configurations form a subspace that avoids Quadrant I. This constraint manifold is not the full square $[0, 1]^2$ but a restricted region---possibly a curve or a narrow band---that connects Quadrant II to Quadrant IV without passing through Quadrant I.

If this interpretation is correct, the constraint is not merely that no current model has both capabilities but that there is an architectural tradeoff that *prevents* current models from having both. Filling Quadrant I would require an architectural innovation that integrates self-monitoring with effort scaling---a mechanism that routes introspective signals to generation control. This is a specific, testable prediction of the geometric framework.


## 9.9 Metacognition as a Two-Dimensional Manifold

The M3/M4 dissociation forces us to revise our model of metacognition. The naive assumption---that metacognition is a single axis, a one-dimensional line from "poor metacognition" to "good metacognition"---is empirically false. The data require at least two dimensions.

**Definition 9.6** (Metacognitive Manifold). *The metacognitive manifold $\mathcal{M}_{\text{meta}}$ is a submanifold of the full cognitive manifold $\mathcal{M}$, parameterized by at least two coordinates:*

$$\mathcal{M}_{\text{meta}} = \{(m_{\text{monitoring}}, m_{\text{control}}, \ldots) \in [0, 1]^k : \text{architectural constraints}\}$$

*where $m_{\text{monitoring}}$ represents the quality of self-monitoring (M3) and $m_{\text{control}}$ represents the quality of effort control (M4). The architectural constraints define the achievable subset of the parameter space.*

The two-dimensional structure of the metacognitive manifold has consequences throughout the geometric framework.

**For calibration (M1).** Calibration is a global measure that averages over both self-monitoring and effort scaling. A model can achieve moderate calibration by having either good self-monitoring (it knows where its errors are) or good effort scaling (it allocates more resources to hard problems, improving accuracy without self-knowledge). Pro achieves good calibration (ECE = 0.186) through self-monitoring. Flash 2.0 achieves poor calibration (ECE = 0.437) despite good effort scaling because its effort is allocated based on the wrong signal.

**For System 2 engagement.** The transition from System 1 (gradient following) to System 2 (geodesic computation) requires the system to detect when the cognitive manifold has high curvature---when the local gradient is unreliable. This detection is a metacognitive function. But the M3/M4 dissociation tells us that detection (knowing the manifold is curved) and response (allocating more effort to curved regions) are separable. A model can detect curvature without responding (Pro's pattern: detect uncertainty but write the same amount) or respond without detecting (Flash 2.0's pattern: write more for complex inputs without knowing whether the complexity creates uncertainty).

**For the recovery ceiling.** The ~38% recovery ceiling, which converges across the A1 and E2 tracks (Chapters 2 and 10), may be related to the empty Quadrant I. Recovery from heuristic corruption requires both metacognitive detection (noticing that the current trajectory has been corrupted) and metacognitive control (redirecting the trajectory). If current architectures cannot fully integrate detection with control, recovery is limited by the weaker of the two---which, given the dissociation, is always substantially below 100%.


## 9.10 The Calibration-Scale Relationship

The calibration gradient across model scale deserves further analysis because it connects to the manifold's representational structure.

The ECE values form a clear ordering by model capability:

$$\text{ECE}(\text{Flash 2.0}) > \text{ECE}(\text{Flash 2.5}) > \text{ECE}(\text{Flash 3}) > \text{ECE}(\text{Claude}) > \text{ECE}(\text{Pro})$$
$$0.437 > 0.415 > 0.333 > 0.250 > 0.186$$

This gradient is consistent with the geometric hypothesis that calibration reflects the fidelity of the model's internal representation of the cognitive manifold. Larger models have higher-dimensional internal representations, which can capture more of the manifold's structure---its curvature variations, its geodesic distances, its local topology. A model with a higher-fidelity internal map produces more accurate distance estimates, which translates directly to better calibration.

The relationship is also consistent with the information-geometric interpretation from Chapter 4. The Fisher information metric defines a natural distance on the space of distributions. A model with more parameters can approximate the Fisher metric more accurately, producing better-calibrated probability estimates. The ECE gradient across model scale is the empirical shadow of the Fisher metric's convergence with model capacity.

**The bin structure of miscalibration.** The ECE computation uses five bins: [0--2), [2--4), [4--6), [6--8), and [8--10]. Examination of the bin-level data reveals that nearly all confidence values fall in the top two bins (6--8 and 8--10). The lower bins are essentially empty. This extreme concentration is another manifestation of the confidence compression discussed in Section 9.4: the model's distance estimation function maps a wide range of actual distances to a narrow range near zero.

The concentration in the top bins means that the ECE is driven almost entirely by the accuracy of high-confidence predictions. The question is not "Does the model know when it is uncertain?" (it rarely expresses uncertainty) but "When the model says it is confident, is it right?" The answer, at 6.7 sigma, is no. The model says it is confident essentially always, and it is wrong far more often than its confidence would predict.


## 9.11 Cross-Model Profiles and the Metacognitive Tensor

The full M1--M4 profiles for each model reveal structure that no single metacognitive score can capture.

| Model | M1 (Cal.) | M2 (Amb.) | M3 (Self-Mon.) | M4 (Effort) |
|---|---|---|---|---|
| Gemini 2.5 Pro | 0.807 | 0.168 | 0.500 | 0.000 |
| Gemini 2.0 Flash | 0.558 | 0.195 | 0.042 | 0.827 |
| Gemini 3 Flash | 0.667 | 0.203 | 0.149 | 0.485 |
| Gemini 2.5 Flash | 0.585 | 0.180 | 0.111 | 0.612 |

The profiles are strikingly different. Pro is strong on M1 and M3, weak on M4. Flash 2.0 is weak on M1 and M3, strong on M4. Flash 3 and Flash 2.5 are intermediate on all four measures.

The four-component metacognitive profile is a *metacognitive tensor*---a point in a four-dimensional space that characterizes the model's metacognitive architecture. Just as the 21-component cognitive profile tensor (Chapter 1) contains structural information destroyed by scalar composites, the metacognitive tensor contains structural information destroyed by any single "metacognition score."

The composite metacognition score used in the benchmark (M1 = 35%, M2 = 25%, M3 = 20%, M4 = 20%) produces reasonable rankings for rough comparison, but it obscures the M3/M4 dissociation---the most informative feature of the data. Pro and Flash 2.0 could receive similar composite scores while having diametrically opposite metacognitive architectures. The Scalar Irrecoverability Theorem from Chapter 1 applies with full force to the metacognitive domain: averaging metacognitive components destroys metacognitive structure.


## 9.12 Connections to Human Metacognition

The M3/M4 dissociation has parallels in the human metacognition literature that lend it additional theoretical weight.

**Feeling of knowing vs. study-time allocation.** The metacognition literature in cognitive psychology distinguishes *metacognitive monitoring* (knowing what you know) from *metacognitive control* (acting on what you know). Hart's (1965) "feeling of knowing" paradigm measures monitoring: people predict whether they will recognize an answer they cannot currently recall. Nelson and Narens's (1990) framework for metacognition explicitly separates monitoring from control and identifies multiple pathways by which monitoring may or may not influence control.

The M3/M4 dissociation in language models mirrors this separation. M3 is a monitoring measure (does the model know what it does not know?). M4 is a control measure (does the model act differently when things are harder?). The finding that these are dissociable in AI models extends the Nelson and Narens framework to artificial systems and provides a concrete architectural interpretation of why the dissociation occurs.

**Dunning-Kruger and the incompetent's overconfidence.** The Dunning-Kruger effect (1999) describes a pattern where people with low ability in a domain are disproportionately overconfident: they lack the metacognitive skill to recognize their own incompetence. The M1 calibration gradient across model scale is a possible analogue: smaller, less capable models have worse calibration (more overconfident), while larger, more capable models have better calibration. This is not because smaller models are "less intelligent" in some scalar sense, but because accurate self-assessment requires the same representational resources that produce accurate task performance. The internal map must be detailed enough to support both navigation and self-location.

**Developmental trajectory.** In human cognitive development, metacognitive monitoring develops before metacognitive control (Schneider, 2008). Children can often tell that a problem is hard before they can adjust their strategies in response to difficulty. This developmental ordering---monitoring before control---is the opposite of the Flash 2.0 pattern (control without monitoring) and the same as the Pro pattern (monitoring without control). Pro's metacognitive profile resembles an early developmental stage where the monitoring system is online but the control pathways are not yet connected. Flash 2.0's profile resembles a reactive system that adjusts to input features without the monitoring layer. Neither is fully mature.


## 9.13 The Metacognitive Metric

The metacognitive manifold, like any manifold, can be equipped with a metric. The metacognitive metric defines distances in metacognitive space: how different are two metacognitive configurations?

**Definition 9.7** (Metacognitive Metric). *Let $\mathbf{m}_1 = (m_1^{(1)}, m_1^{(2)}, m_1^{(3)}, m_1^{(4)})$ and $\mathbf{m}_2 = (m_2^{(1)}, m_2^{(2)}, m_2^{(3)}, m_2^{(4)})$ be two metacognitive profiles. The metacognitive distance is:*

$$d_{\text{meta}}(\mathbf{m}_1, \mathbf{m}_2) = \sqrt{\sum_{\mu=1}^{4} w_\mu (m_1^{(\mu)} - m_2^{(\mu)})^2}$$

*where $w_\mu$ are weights reflecting the relative importance of each metacognitive component.*

Under this metric, Pro and Flash 2.0 are far apart: they differ dramatically on M3 (0.500 vs. 0.042) and M4 (0.000 vs. 0.827). The metacognitive distance between them is large despite their similar positions on the overall "metacognitive quality" scale. This is the metacognitive analogue of the Claude-vs.-Pro distance in the full cognitive space (Chapter 1): two systems that appear similar on a composite but are structurally distant in the full-dimensional space.

The metacognitive metric also defines curvature. The region around Quadrant I---the empty quadrant---has unusual geometry. The achievable metacognitive configurations avoid this region, which means the geodesics in metacognitive space must curve around the empty quadrant rather than passing through it. A direct path from Pro's configuration (high M3, low M4) to Flash 2.0's configuration (low M3, high M4) would pass through Quadrant I, but if that quadrant is architecturally inaccessible, the actual geodesic must detour through Quadrant III or along the boundary---a longer path that reflects the architectural constraint.

This curvature is not geometric in the abstract sense. It is functional. The architectural constraint that prevents models from occupying Quadrant I creates a metacognitive manifold with non-trivial topology---a manifold with a "hole" in the metacognitive plane. This hole has consequences for how metacognitive capabilities can evolve under training: gradual training that improves M3 at fixed M4 (moving along the x-axis) will reach Pro's position; gradual training that improves M4 at fixed M3 will reach Flash 2.0's position; but gradual training cannot reach Quadrant I because the manifold does not extend there under current architectures.


## 9.14 Cross-Track Implications

The metacognitive results interact with every other cognitive dimension in the benchmark suite.

**Metacognition and attention.** The universally weak SNR in the attention track (A3: 1.22--1.38, Chapter 10) means that all models navigate the cognitive manifold with a metric that barely distinguishes signal from noise. An accurate metacognitive system would detect this weakness and compensate---perhaps by reducing confidence in noise-contaminated regions or by applying additional processing to improve the signal. The poor calibration results (M1) suggest that no model detects this weakness. The models are overconfident even in regions where their attention metric is weak---a metacognitive failure layered on an attentional failure.

**Metacognition and executive control.** The cross-track insight highlighted in the executive functions writeup is particularly illuminating: Flash 2.0 has the best cognitive flexibility (E1 = 0.701) and the strongest recovery from emotional anchoring (73%) in the Executive Functions benchmark, but the worst calibration (ECE = 0.437) in the Metacognition benchmark. It controls reasoning well but cannot judge its own confidence.

This dissociation between executive control and metacognitive self-knowledge adds a *third* dimension to the metacognitive picture. Not only are M3 (self-monitoring) and M4 (effort scaling) dissociable, but the entire metacognitive domain (M1--M4) is dissociable from executive control (E1--E4). A model can be a skilled navigator without knowing where it is. It can steer competently through complex terrain---switching frameworks, recovering from emotional disturbance, tracking multiple parties---while having no accurate sense of how well it is doing.

This is cognitively plausible. Expert performers in many domains exhibit a form of competent ignorance: they perform well without accurate self-assessment, relying on overlearned routines rather than metacognitive monitoring. The geometric framework makes this precise: competent navigation (following good geodesics) does not require accurate distance estimation (knowing how far you are from the goal). The geodesic equation depends on the metric and the Christoffel symbols, not on the heuristic field's accuracy. A model can follow the correct path without knowing how long the path is.

**Metacognition and social cognition.** The overconfidence universal in M1 connects to the framing vulnerability measured in the Social Cognition track (T5: 15.3 sigma). An overconfident model does not detect when its heuristic field has been corrupted by framing---it is confident in the corrupted judgment just as it is confident in the uncorrupted one. Better calibration (lower ECE) might provide a defense against framing: a well-calibrated model would notice that its confidence drops when confronted with a framing manipulation (because the manipulation introduces conflict, which should register as increased distance from the goal). But no current model has calibration good enough to serve as a framing detector.


## 9.15 Worked Example: Diagnosing a Metacognitive Profile

**Setup.** A new language model, Model X, is tested on the Metacognition benchmark and produces the following profile:

| Component | Score |
|---|---|
| M1 (Calibration ECE) | 0.310 |
| M2 (Ambiguity AUROC) | 0.720 |
| M3 (Self-Monitoring) | 0.390 |
| M4 (Effort Scaling) | 0.120 |

**Step 1: Locate in the calibration gradient.** Model X's ECE of 0.310 places it between Flash 3 (0.333) and Claude (0.250) in the calibration gradient. This is moderately good calibration---better than the Flash 2.0/2.5 tier, worse than Pro. The model's global distance estimation is in the upper middle of the observed range.

**Step 2: Assess ambiguity discrimination.** The AUROC of 0.720 is notably higher than the values observed in the benchmark sample (which cluster around 0.17--0.20 on the normalized composite score). If this AUROC is from raw rank-order analysis, it indicates genuine ability to distinguish clear-cut from ambiguous problems---a meaningful improvement over the benchmark models.

**Step 3: Plot in the M3/M4 plane.** M3 = 0.390, M4 = 0.120. This places Model X in Quadrant II (moderate self-monitoring, low effort scaling)---the same quadrant as Pro, though with lower self-monitoring. Model X knows which problems are hard (moderately well) but does not adjust effort accordingly. The thermometer is warm but the valve is cool.

**Step 4: Check for the Quadrant I gap.** Model X does not fill Quadrant I. Its M4 is too low. The empty quadrant persists. The prediction from the geometric framework is that Model X's architecture does not integrate monitoring with control, consistent with the hypothesis that Quadrant I requires an architectural innovation rather than mere scaling.

**Step 5: Predict cross-track behavior.** Based on the metacognitive profile, we predict:
- Model X should show moderate resistance to framing effects (its self-monitoring is good enough to notice some heuristic corruption, though not always).
- Model X should show poor recovery from attentional distractors (its effort scaling is too weak to allocate additional resources when distractors are detected).
- Model X's executive control profile should be partially dissociated from its metacognitive profile (controlling reasoning and knowing about reasoning are independent capabilities).

These predictions are testable on the other benchmark tracks and provide a concrete validation pathway for the geometric metacognitive framework.


## 9.16 Implications for AI Development

The metacognitive results have direct implications for how language models are trained, evaluated, and deployed.

**For training.** The M3/M4 dissociation suggests that self-monitoring and effort scaling are trained by different aspects of the training signal. Self-monitoring may be developed through training on tasks that require explicit uncertainty estimation---calibration training, where the model receives feedback not just on its answers but on the accuracy of its confidence. Effort scaling may be developed through training on tasks with variable difficulty, where longer reasoning is rewarded for harder problems. Current training regimes may emphasize one at the expense of the other, producing the dissociation we observe.

An architectural approach to filling Quadrant I would connect the model's introspective signals (the representations that support self-monitoring) to its generation control signals (the mechanisms that control response length and depth). This might involve:

1. A metacognitive feedback loop that routes uncertainty estimates to the generation length controller.
2. A difficulty-adaptive architecture that uses internal confidence signals to modulate chain-of-thought depth.
3. Training objectives that jointly reward accurate self-assessment *and* difficulty-appropriate effort.

**For evaluation.** The empty Quadrant I provides a clear target for evaluation: a model that fills this quadrant---that has both good self-monitoring and good effort scaling---would represent a genuine advance in metacognitive capability. Current composite metacognition metrics cannot detect this advance, because they average M3 and M4 into a single number that could be achieved by either component alone. The two-dimensional metacognitive profile is the minimum evaluation required to track progress toward integrated metacognition.

**For deployment.** In deployment contexts where reliable confidence estimates are critical---medical diagnosis, legal reasoning, safety-critical systems---the calibration results are directly relevant. No current model should be trusted to accurately assess its own confidence. The 6.7 sigma universal overconfidence means that any confidence threshold used for deployment decisions (e.g., "act on the model's recommendation only when confidence exceeds 90%") is systematically unreliable. The model will report 90% confidence far more often than it is correct 90% of the time.

Pro's better calibration (ECE = 0.186) makes it the least unreliable for confidence-gated deployment, but even Pro is significantly overconfident. The geometric framework suggests that the deployment solution is not to trust confidence values at face value but to apply external calibration---a post-hoc adjustment that maps the model's raw confidence values to calibrated probabilities using a holdout validation set. This external calibration is a form of imposing a corrected metric on the model's distance estimates, replacing its distorted internal map with a more accurate external one.


## 9.17 The Metacognitive Hierarchy

The four metacognitive components form a natural hierarchy that maps onto the geometric framework:

**Level 1: Global calibration (M1).** The model's overall distance estimation accuracy. This is the coarsest metacognitive measure---a single number summarizing how well the model's confidence matches its accuracy across all problems. Geometrically, this is the average distortion of the model's internal map.

**Level 2: Category discrimination (M2).** The model's ability to distinguish regions of the cognitive manifold by difficulty. This is finer-grained than M1---it tests whether the model can tell that some regions are more complex (higher curvature) than others, even if its absolute distance estimates are off. Geometrically, this is the model's ability to detect curvature gradients.

**Level 3: Item-level monitoring (M3).** The model's ability to estimate distances at specific points on the manifold. This is finer-grained than M2---it tests whether the model can estimate the local curvature at each point, not just distinguish high-curvature regions from low-curvature ones. Geometrically, this is the accuracy of the model's local curvature estimates.

**Level 4: Effort control (M4).** The model's ability to translate distance estimates into resource allocation. This is not a finer-grained distance estimate but a *control action* that uses distance estimates to modulate search depth. Geometrically, this is the coupling between the model's distance estimation system and its search control system.

The hierarchy makes the M3/M4 dissociation interpretable. Levels 1--3 are all aspects of distance estimation---they measure the accuracy of the model's internal map at different scales. Level 4 is an action that depends on distance estimation but is architecturally separable from it. The dissociation is between the map (monitoring) and the navigator's use of the map (control). Pro has an accurate map but does not use it. Flash 2.0 has an inaccurate map but navigates adaptively using other cues.

This hierarchy also predicts the order in which metacognitive capabilities should emerge during training or scaling. Global calibration (M1) should emerge first, because it requires only a rough sense of overall difficulty. Category discrimination (M2) should emerge next, because it requires distinguishing broad regions of the cognitive manifold. Item-level monitoring (M3) should emerge last, because it requires the most detailed internal map. Effort control (M4) may emerge at any point, because it can be driven by signals other than metacognitive monitoring.

The calibration gradient across model scale (Section 9.10) is consistent with this ordering: larger models show better M1, suggesting that global calibration is indeed one of the earlier metacognitive capabilities to benefit from scaling.


## 9.18 Looking Forward

Metacognition is the hinge between knowing and knowing-about-knowing. The benchmark results reveal that current language models have systematic deficiencies at this hinge: universal overconfidence, compressed confidence distributions, and a fundamental dissociation between the monitoring and control components of metacognition.

The empty Quadrant I is the central finding. It tells us that the metacognitive architecture of current models has a structural gap---a capability combination that no model can achieve. Filling this gap is not a matter of scaling existing architectures; it requires connecting the monitoring system (which knows where the model is uncertain) to the control system (which allocates resources to uncertainty). This connection is the metacognitive equivalent of completing the feedback loop in a control system: the sensor exists, the actuator exists, but the wire between them is missing.

Chapter 10 turns to the attention track, where a different kind of structural finding emerges: the distractor dose-response curve and the architectural split in divided attention. Attention and metacognition interact closely---a system that cannot monitor its own attention allocation cannot correct for attentional failures. The weak SNR universality in Chapter 10 is, in part, a consequence of the metacognitive weakness documented here: the models do not know that their attention metric is weak, and therefore cannot compensate for it.

The cognitive manifold has been mapped. The metric has been measured. The tangent space has been characterized. The control layer has been described. Now, with the metacognitive results, we know that the navigator's sense of position is systematically biased. The map is distorted. And the distortion has a specific, measurable, two-dimensional structure that no single number can capture.

---

## Technical Appendix 9A: Expected Calibration Error---Formal Properties

**Definition** (ECE, Formal). *Let $\{(p_i, y_i)\}_{i=1}^N$ be a sequence of confidence-outcome pairs, where $p_i \in [0,1]$ is the model's stated confidence and $y_i \in \{0, 1\}$ is the binary outcome (correct/incorrect). Partition the confidence interval $[0,1]$ into $B$ equal-width bins $I_b = [(b-1)/B, b/B)$ for $b = 1, \ldots, B$. Define:*

$$\text{acc}(I_b) = \frac{1}{|I_b|} \sum_{i \in I_b} y_i, \quad \text{conf}(I_b) = \frac{1}{|I_b|} \sum_{i \in I_b} p_i$$

*The Expected Calibration Error is:*

$$\text{ECE} = \sum_{b=1}^{B} \frac{|I_b|}{N} |\text{acc}(I_b) - \text{conf}(I_b)|$$

**Properties.**

1. *Boundedness:* $0 \leq \text{ECE} \leq 1$.
2. *Calibration:* $\text{ECE} = 0$ if and only if $\text{acc}(I_b) = \text{conf}(I_b)$ for all bins with $|I_b| > 0$.
3. *Decomposition:* The ECE can be decomposed into a reliability component (calibration error) and a resolution component (discriminability), analogous to the Brier score decomposition.

**Bootstrap standard error.** The ECE is computed from finite samples and is therefore subject to sampling variability. The bootstrap standard error is computed by resampling with replacement from the confidence-outcome pairs 200 times and computing the ECE for each resample. The standard deviation of the bootstrap distribution provides the standard error. The z-score is $z = \text{ECE} / \text{SE}_{\text{bootstrap}}$.

**Fisher combination.** When ECE z-scores are available for multiple independent models, they are combined using Fisher's method:

$$\chi^2 = -2 \sum_{k=1}^{K} \ln(p_k)$$

*where $p_k$ is the two-tailed $p$-value corresponding to model $k$'s z-score. Under the null hypothesis of perfect calibration, $\chi^2 \sim \chi^2_{2K}$. The combined significance is the $p$-value of $\chi^2$ under this distribution, converted back to a z-score.*

The Fisher combined z-score of 6.7 sigma indicates that the probability of observing this degree of miscalibration under perfect calibration is approximately $10^{-11}$---an extremely strong rejection of the calibration null.


## Technical Appendix 9B: The M3/M4 Dissociation---Statistical Analysis

**Dissociation test.** The M3/M4 dissociation is assessed by a crossing pattern: Model A has $m_3^A > m_3^B$ and $m_4^A < m_4^B$ relative to Model B. This is a *double dissociation* in the neuropsychological sense: the two capabilities are independently variable across systems.

For Pro vs. Flash 2.0:
- M3: Pro (0.500) >> Flash 2.0 (0.042), difference = 0.458
- M4: Pro (0.000) << Flash 2.0 (0.827), difference = -0.827

The crossing is large on both dimensions. The difference in M3 exceeds the noise level in the self-monitoring measure (bootstrap SE approximately 0.10), and the difference in M4 exceeds the noise level in the effort scaling measure (bootstrap SE approximately 0.08). The dissociation is statistically robust.

**Independence test.** Under the hypothesis that M3 and M4 are driven by a common metacognitive factor, we would expect a positive correlation: $r(M3, M4) > 0$. The observed correlation across the four full-suite models is negative: $r(M3, M4) \approx -0.85$. With only four data points, this correlation does not reach conventional significance, but the negative direction is inconsistent with the unitary metacognition hypothesis and consistent with the dissociation.

**Quadrant analysis.** With threshold $\tau = 0.25$ (the midpoint of the observed range on each dimension):

| Quadrant | M3 > 0.25 | M4 > 0.25 | Models |
|---|---|---|---|
| I | Yes | Yes | (empty) |
| II | Yes | No | Pro |
| III | No | No | (none with both below 0.25) |
| IV | No | Yes | Flash 2.0, Flash 2.5, Flash 3 |

Quadrant I contains no models regardless of the specific threshold chosen, as long as the threshold is between Pro's M4 (0.000) and Flash 2.0's M3 (0.042).


## Technical Appendix 9C: Information-Geometric Interpretation of Calibration

The calibration error has a natural interpretation in information geometry. Let $p(y|\theta)$ be the model's predictive distribution for outcome $y$ given its internal state $\theta$, and let $q(y|x)$ be the true conditional distribution given the input $x$. The calibration error at a given confidence level is related to the KL divergence between the model's predictive distribution and the true distribution:

$$\text{KL}(q \| p) = \sum_{y} q(y|x) \log \frac{q(y|x)}{p(y|\theta)}$$

For binary outcomes, if the model reports confidence $p$ and the true probability of being correct is $q$, the KL divergence is:

$$\text{KL} = q \log \frac{q}{p} + (1-q) \log \frac{1-q}{1-p}$$

The ECE is a binned approximation to the expected absolute calibration error $\mathbb{E}[|p - q|]$, which is related to but distinct from the expected KL divergence. The information-geometric perspective reveals that miscalibration is a form of *model misspecification*: the model's internal distribution $p(y|\theta)$ is a biased estimate of the true distribution $q(y|x)$, and the bias is in the direction of overconfidence ($p > q$).

On the statistical manifold $\mathcal{S} = \{p_\theta : \theta \in \Theta\}$, the calibrated model corresponds to the projection of the true distribution onto $\mathcal{S}$---the closest distribution in the model family to the truth. The miscalibrated model corresponds to a different point on $\mathcal{S}$, displaced from the projection in the overconfidence direction. The ECE measures the displacement. The Fisher metric on $\mathcal{S}$ determines the natural distance scale for this displacement. And the universal overconfidence tells us that the displacement is in the same direction for all models, suggesting a structural bias in how language models parameterize their output distributions.
