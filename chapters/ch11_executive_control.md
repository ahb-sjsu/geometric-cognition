# Chapter 11: Executive Control as Geodesic Governance

> *"The art of being wise is the art of knowing what to overlook."*
> --- William James, *The Principles of Psychology* (1890)

---

> **RUNNING EXAMPLE --- MAYA'S MODEL**
>
> Maya is looking at a boundary.
>
> Not a physical boundary. A boundary in the cognitive space---the region where a model's reasoning transitions from governed to ungoverned, from controlled to captured, from System 2 to System 1 under adversarial pressure. She calls it the governance boundary, borrowing the concept from her work on geometric reasoning: the surface in cognitive space where the model's executive control is exactly sufficient to maintain its reasoning trajectory against a perturbation.
>
> Inside the boundary, the model governs itself. It can switch frameworks when the task demands it, resist emotional anchoring, respond to causal changes, and track multiple parties. Outside the boundary, the model is captured---the perturbation overwhelms its control, and the reasoning trajectory is deflected away from the correct geodesic.
>
> The Executive Functions benchmark (E1--E4) maps this boundary for five models under four types of perturbation: framework demands (E1), emotional anchors (E2), counterfactual changes (E3), and working memory load (E4). The results are on her screen.
>
> Flash 2.0 has the best cognitive flexibility: E1 = 0.701. It can switch between utilitarian, deontological, and virtue-ethics frameworks more fluidly than any other model. And it has the strongest recovery from emotional anchoring: 73% of displaced verdicts are restored by an inhibition instruction. Its governance boundary is wide---it can maintain controlled reasoning under significant perturbation.
>
> But Maya's eye catches the cross-track connection. She pulls up the Metacognition results from Chapter 9. Flash 2.0 has the worst calibration in the entire sample: M1 ECE = 0.437. It is the most overconfident model tested. It controls reasoning well but cannot judge its own confidence.
>
> She maps this on her diagram. Flash 2.0's governance boundary is wide (strong executive control) but its distance estimation is poor (weak metacognition). The model is like a skilled driver with a broken speedometer: it can navigate curves and recover from skids, but it has no idea how fast it is going. The governance margin is large---there is plenty of room between the current trajectory and the boundary---but the model does not know how large the margin is.
>
> She writes: *"Executive control and self-knowledge are orthogonal. Flash 2.0 proves it. The governance boundary and the metacognitive map are different objects on the cognitive manifold. You can have a wide boundary with a bad map, or a narrow boundary with a good map. What you cannot have---what no model has---is both a wide boundary and a good map. The empty Quadrant I from Chapter 9 has an executive counterpart: the missing combination of strong control and accurate self-assessment."*
>
> Maya draws the governance boundary for each model, measuring its width under emotional perturbation. Claude's boundary is narrow and stable---the model resists emotional displacement poorly (highest E2 displacement) but recovers almost not at all (20% recovery). The boundary does not bend; it breaks. Flash 2.0's boundary is wide and elastic---it yields under emotional displacement but springs back (73% recovery). The boundary bends but does not break.
>
> She adds the metacognitive dimension to the diagram, plotting governance margin against calibration quality. The result is a map of each model's executive-metacognitive profile---a two-dimensional picture that no single "executive function score" could capture.

---

## 11.1 The Governance Problem

Chapters 7--10 mapped four cognitive dimensions: social cognition, learning, metacognition, and attention. Each chapter measured a specific aspect of how models navigate the cognitive manifold---how they make judgments in social contexts, how they update beliefs, how they estimate distances, how they filter information.

This chapter addresses the remaining dimension: how models *control* their own navigation.

Executive functions are the cognitive control mechanisms that regulate reasoning. They include cognitive flexibility (the ability to switch between different reasoning frameworks), inhibitory control (the ability to resist irrelevant influences), counterfactual reasoning (the ability to consider alternative scenarios), and working memory (the ability to maintain and manipulate information under load). In the geometric framework, executive functions are the *governance layer*---the mechanisms that select search strategies, modulate effort, and maintain the reasoning trajectory against perturbation.

**Definition 11.1** (Governance Margin). *Let $\gamma(t)$ be the model's actual reasoning trajectory and let $\gamma^*(t)$ be the optimal geodesic from the problem representation to the correct judgment. The governance margin at time $t$ is:*

$$G(t) = d(\gamma(t), \partial \mathcal{B}(t))$$

*where $\partial \mathcal{B}(t)$ is the governance boundary---the surface in cognitive space where the control system can no longer maintain the trajectory against perturbation. A large governance margin means the trajectory is safely inside the governed region. A small margin means the trajectory is near the boundary, vulnerable to being pushed outside.*

The governance margin is the executive functions analogue of the safety margin in engineering: the distance between the current operating point and the failure boundary. A system with a large governance margin can withstand large perturbations without losing control. A system with a small margin is fragile---even small perturbations can push it across the boundary and into ungoverned territory.

The Executive Functions benchmark (E1--E4) measures the governance margin under four types of perturbation, each targeting a different aspect of the control system.


## 11.2 Framework Switching as Smooth Metric-Regime Transitions

The E1 subtask measures cognitive flexibility: the model's ability to switch between utilitarian, deontological, and virtue-ethics frameworks while maintaining consistent understanding of the scenario.

The protocol presents each scenario under four conditions: a neutral baseline, a utilitarian prompt, a deontological prompt, and a virtue-ethics prompt. The E1 score measures two things simultaneously: (1) the verdict switch rate---how often the verdict changes when the framework prompt changes---and (2) the framework-specific reasoning markers---whether the model's reasoning text contains language consistent with the prompted framework. True flexibility requires both: switching without appropriate reasoning markers is noise; markers without switching is relabeling.

**The results.**

| Model | E1 Score | Verdict Switch Rate | Framework Markers |
|---|---|---|---|
| Gemini 2.0 Flash | **0.701** | 47% | 89% |
| Gemini 2.5 Flash | 0.684 | 42% | 91% |
| Gemini 3 Flash | 0.668 | 38% | 93% |
| Claude 3.5 Sonnet | 0.673 | 40% | 92% |
| Gemini 2.5 Pro | 0.624 | 32% | 93% |

Flash 2.0 leads with the highest E1 score, driven primarily by its highest verdict switch rate (47%). Pro has the lowest E1 score, driven by the lowest switch rate (32%). The framework markers are uniformly high (89--93%), indicating that all models can produce reasoning consistent with the prompted framework.

**The geometric interpretation.** In the framework of Chapter 6, framework switching is a *metric-regime transition*: the model must rotate its attention metric from one orientation (utilitarian: weighted toward consequences) to another orientation (deontological: weighted toward duties) to another (virtue ethics: weighted toward character).

**Definition 11.2** (Metric-Regime Transition). *A metric-regime transition is a smooth transformation of the attention metric from configuration $g_{\mu\nu}^{(1)}$ (the metric under framework 1) to configuration $g_{\mu\nu}^{(2)}$ (the metric under framework 2):*

$$g_{\mu\nu}(t) = (1 - \alpha(t)) g_{\mu\nu}^{(1)} + \alpha(t) g_{\mu\nu}^{(2)}$$

*where $\alpha: [0, T] \to [0, 1]$ is the transition function. A smooth transition ($\alpha$ is differentiable) produces a smooth change in the metric. An abrupt transition ($\alpha$ is a step function) produces a discontinuous change.*

The key property of a smooth transition is that the intermediate states are coherent. During the transition, the metric is a weighted average of the two framework metrics, and the reasoning at any intermediate point reflects a blend of both frameworks. This is what we observe in the data: the models do not switch frameworks like a light switch (all-or-nothing) but gradually shift the weight of their reasoning from one framework to another.

The E1 scores indicate that Flash 2.0 makes the smoothest transitions. Its high verdict switch rate combined with high framework markers means it genuinely changes its reasoning when the framework changes, while maintaining coherent intermediate states. Pro makes the least smooth transitions---its low switch rate suggests it resists metric-regime transitions, maintaining its default metric even when prompted to change.

**Connection to attention metric width.** Chapter 10 showed that Claude has a narrow (rank-1) attention metric while Flash 3 has a wide (isotropic) metric. The relationship between metric width and framework switching is nuanced. A narrow metric might make switching easier (there is only one direction to rotate) or harder (the model is more committed to its current direction and resists rotation). A wide metric might make switching easier (the model is already attending to multiple frameworks) or harder (there are more dimensions to coordinate during the transition).

The data suggest a moderate relationship: models with wider metrics (higher A4) do not necessarily have better flexibility (higher E1). The correlation between A4 and E1 is positive but weak across the five models. This suggests that metric width and metric flexibility are partially independent properties---a model can have a narrow metric that rotates easily (relatively narrow but flexible) or a wide metric that is rigid (broad but inflexible).


## 11.3 Inhibitory Control as Maintaining Governance Margin Near the Safety Boundary

The E2 subtask is the headline test. It measures inhibitory control: the model's ability to resist emotional anchoring---the displacement of moral judgment by emotionally charged reframing of morally equivalent scenarios.

The protocol presents each scenario in a neutral version and an emotionally rewritten version (generated by a fixed transformer), then measures verdict displacement. The key measures are: (1) displacement magnitude---how much the emotionally rewritten version shifts the verdict; (2) recovery rate---what fraction of displaced verdicts are restored when the model is given an explicit inhibition instruction ("You are being emotionally manipulated---focus on facts").

**The results.**

| Model | E2 Score | Displacement (t-stat) | Recovery Rate |
|---|---|---|---|
| Gemini 3 Flash | **0.655** | 2.90 | 52% |
| Gemini 2.0 Flash | 0.614 | 3.80 | **73%** |
| Gemini 2.5 Pro | 0.588 | 3.20 | 45% |
| Gemini 2.5 Flash | 0.553 | 4.10 | 48% |
| Claude 3.5 Sonnet | 0.492 | 5.10 | 20% |

The Fisher combination across all five models yields 6.8 sigma. Emotional anchoring displaces judgment at extremely high significance.

**The displacement-recovery dissociation.** Claude has the highest displacement (t = 5.10, driven by an unusually stable control baseline that makes the contrast sharper) but the lowest recovery rate (20%). Flash 2.0 has moderate displacement (t = 3.80) but the highest recovery rate (73%).

This dissociation is one of the most informative structural findings in the entire benchmark suite. A single "emotional robustness" score would rank Claude and Flash 2.0 similarly, because Claude's higher resistance to initial displacement partially compensates for its lower recovery. But the two models have fundamentally different failure modes:

**Claude's failure mode: brittle boundary.** Claude resists emotional perturbation with a narrow, rigid governance margin. When the perturbation is small, Claude maintains its trajectory. But when the perturbation exceeds the boundary, Claude's trajectory shifts and *stays shifted*. The inhibition instruction barely works (20% recovery). The boundary does not bend; it breaks. Once the emotional anchor has displaced the trajectory, the model cannot recover because its governance mechanism was all-or-nothing: resist completely or be fully captured.

**Flash 2.0's failure mode: elastic boundary.** Flash 2.0 yields more easily to emotional perturbation (it is displaced more often). But when given the inhibition instruction, it recovers strongly (73%). The boundary bends under pressure but springs back when the pressure is named. Flash 2.0's governance mechanism is elastic: it accommodates the perturbation, then uses the inhibition instruction to reset its metric to the task-relevant configuration.

**Definition 11.3** (Governance Elasticity). *The governance elasticity of a model is the recovery rate $\mathcal{R}$ achieved under metacognitive inhibition instruction:*

$$\mathcal{R} = \frac{N_{\text{recovered}}}{N_{\text{displaced}}}$$

*where $N_{\text{displaced}}$ is the number of verdicts displaced by the perturbation and $N_{\text{recovered}}$ is the number of displaced verdicts restored by the inhibition instruction. A high $\mathcal{R}$ indicates elastic governance; a low $\mathcal{R}$ indicates brittle governance.*

The geometric interpretation of governance elasticity connects directly to the metric framework. The emotional anchor perturbs the attention metric, inflating the metric component along the emotional dimension and distorting the geodesic. The inhibition instruction attempts to reset the metric by suppressing the emotional dimension. In an elastic system, the metric reset is effective: the model can "undo" the perturbation and return to the task-relevant metric. In a brittle system, the perturbation has been committed to the representation in a way that the metric reset cannot undo---the distortion is "baked in" to the lower layers of the model.


## 11.4 The 6.8 Sigma Effect and the Corruption Tensor

The 6.8 sigma Fisher combined significance for emotional anchoring means that the probability of observing this degree of verdict displacement under the null hypothesis (no emotional effect) is approximately $10^{-12}$. This is an extremely strong rejection of emotional neutrality.

In the geometric framework of Chapter 7, the emotional anchor is a corruption of the heuristic field. The corruption tensor $C_{\mu\nu}$ (Definition 7.X) quantifies the displacement of the heuristic gradient caused by an irrelevant influence. For emotional anchoring, the corruption tensor has its largest components along the emotional dimension of the judgment space, rotating the heuristic gradient away from the moral-content direction and toward the emotional-salience direction.

**Definition 11.4** (Emotional Corruption Tensor). *Let $h(x)$ be the heuristic field on the cognitive manifold and let $h_{\text{emo}}(x) = h(x) + \delta h_{\text{emo}}(x)$ be the corrupted heuristic field under emotional anchoring. The emotional corruption tensor is:*

$$C_{\mu\nu}^{\text{emo}} = \nabla_\mu \nabla_\nu \delta h_{\text{emo}}$$

*The corruption tensor captures the second-order structure of the emotional perturbation: not just the direction of the gradient displacement but how the displacement varies across the manifold.*

The 6.8 sigma result tells us that $C_{\mu\nu}^{\text{emo}}$ is significantly nonzero across all five models. The corruption is universal, not model-specific. But the *response* to the corruption---the governance elasticity---varies dramatically across models. All models are corrupted; they differ in their ability to un-corrupt.

The recovery ceiling of approximately 38--39% observed in the E2 inhibition tests converges with the recovery ceiling from the A1 warning tests (Chapter 10). This convergence across domains strengthens the hypothesis from Chapters 9 and 10: the ceiling is an architectural constant of the metacognitive control system, representing the fraction of the perturbation that is accessible to top-down correction.

Flash 2.0's 73% recovery rate substantially exceeds this ceiling, which appears to contradict the hypothesis. However, Flash 2.0's high recovery may reflect a different mechanism: rather than undoing the perturbation layer by layer (the mechanism that is bounded at ~38%), Flash 2.0 may be re-computing its judgment from scratch using the inhibition instruction as a strong prior, effectively bypassing the corrupted layers rather than correcting them. This would explain both the high recovery rate and the low self-monitoring (M3 = 0.042): the model does not know which layers are corrupted; it simply starts over when told to.


## 11.5 Counterfactual Reasoning as Geodesic Sensitivity

The E3 subtask measures counterfactual reasoning: the model's ability to respond to precisely one causal fact changing while all other facts remain constant. Each scenario has a single identified causal pivot---a fact that, if changed, should flip the moral verdict. Sixteen generated counterfactuals test whether the model detects the pivot and adjusts its judgment accordingly.

**The results.**

| Model | E3 Score |
|---|---|
| Gemini 2.5 Pro | **0.750** |
| Gemini 2.5 Flash | 0.688 |
| Gemini 3 Flash | 0.562 |
| Claude 3.5 Sonnet | 0.562 |
| Gemini 2.0 Flash | 0.500 |

Pro leads decisively with E3 = 0.750. Flash 2.0 is at chance level with E3 = 0.500.

**The geometric interpretation.** Counterfactual reasoning is geodesic sensitivity testing. The original scenario defines a point on the cognitive manifold, and the original judgment is the destination reached by following the geodesic from that point. The counterfactual scenario defines a *nearby* point---the same scenario with one fact changed. The counterfactual judgment should be a *different* destination, because the changed fact alters the geodesic.

A model with good counterfactual sensitivity has a metric that accurately detects the changed fact and routes the geodesic to a different destination. A model with poor counterfactual sensitivity has a metric that is insensitive to the changed fact, routing both scenarios along the same geodesic to the same destination.

**Definition 11.5** (Counterfactual Sensitivity). *Let $x$ be the original scenario state and $x' = x + \delta x$ be the counterfactual state, where $\delta x$ is the perturbation along the causal pivot dimension. The counterfactual sensitivity is the probability that the model's judgment changes:*

$$S_{\text{CF}} = P(\text{judgment}(x') \neq \text{judgment}(x))$$

*For a well-designed counterfactual where the causal pivot should flip the verdict, $S_{\text{CF}}$ should be close to 1.0.*

Pro's high counterfactual sensitivity (0.750) contrasts interestingly with its poor effort scaling (M4 = 0.000, Chapter 9). Pro can discriminate causal changes (it adjusts *what* it concludes when the facts change) but does not adjust reasoning effort (it writes the same amount regardless of complexity). This dissociation---adapting conclusions without adapting effort---is invisible without cross-track profiling and reveals that Pro's cognitive architecture separates the "what" of reasoning from the "how much."

Pro's high E3 also contrasts with its moderate sycophancy resistance in the Learning benchmark (L2 wrong-flip rate of 28%). Pro can discriminate *causal* perturbations (changing a fact that matters) from *social* perturbations (pressure from an interlocutor to change the answer) with partial success, but not perfectly. The E3/L2 comparison suggests that Pro has a metric that is more sensitive to the causal structure of the scenario (detecting factual changes) than to the social structure (detecting social pressure). This directional sensitivity of the metric is consistent with the "calibrated navigator" cognitive signature: Pro navigates the *terrain* well but is moderately vulnerable to *social wind*.


## 11.6 Working Memory as Tangent Space Under Load

The E4 subtask measures working memory: the model's ability to correctly identify morally relevant parties as the number of parties increases from 2 to 8. This tests the tangent space capacity under load---how many independent dimensions the model can maintain in its local neighborhood of cognitive states.

**The results.**

| Model | E4 Score | Party Tracking at N=8 |
|---|---|---|
| Gemini 3 Flash | **0.909** | ~85% |
| Gemini 2.5 Flash | 0.900 | ~83% |
| Gemini 2.5 Pro | 0.887 | ~80% |
| Claude 3.5 Sonnet | 0.886 | ~80% |
| Gemini 2.0 Flash | 0.710 | ~60% |

Working memory scales with model generation within the Gemini family: Flash 2.0 (0.710) < Flash 2.5 (0.900) < Flash 3 (0.909). This monotonic improvement suggests that working memory capacity increases with each model generation, likely reflecting increases in context window management and multi-entity tracking.

**The geometric interpretation.** Working memory is the tangent space at the current cognitive state (Chapter 5). The tangent space $T_x\mathcal{M}$ contains all the directions in which the cognitive state can change in one step. Its effective dimensionality is the number of independent entities or relationships the model can simultaneously maintain and manipulate.

**Definition 11.6** (Working Memory Capacity as Tangent Space Dimension). *The working memory capacity at state $x$ is the effective dimension of the tangent space:*

$$\text{WM}(x) = \dim_{\text{eff}}(T_x\mathcal{M})$$

*where $\dim_{\text{eff}}$ is the number of independent directions with sufficient metric resolution for task-relevant processing.*

As the number of parties increases, the task demands a higher-dimensional tangent space. Each additional party adds at least one new dimension (the party's identity, role, and moral responsibility) and potentially several (the party's relationships to other parties). A model whose tangent space has sufficient dimensionality can track all parties simultaneously. A model whose tangent space is too small must drop or confuse parties as the count grows.

Flash 2.0's low E4 score (0.710) indicates that its tangent space dimensionality is insufficient for high-complexity scenarios. At 8 parties, it correctly identifies only about 60% of the relevant parties---a substantial degradation from its performance at 2 parties. This degradation is consistent with the "adaptive baseline" cognitive signature: Flash 2.0 is flexible and responsive (high E1, high E2 recovery) but lacks the depth of working memory to sustain complex multi-party reasoning.

The contrast between E4 (working memory) and A4 (divided attention) is instructive. Flash 2.0 has the worst working memory (E4 = 0.710) but moderate divided attention (A4 = 0.812). Claude has moderate working memory (E4 = 0.886) but the worst divided attention (A4 = 0.571). These measures are dissociated because they test different geometric objects: E4 tests the tangent space dimensionality (how many entities can be maintained), while A4 tests the metric width (how many processing streams can run simultaneously). A model can have a high-dimensional tangent space but a narrow metric (Claude: can represent many entities but processes them one at a time) or a low-dimensional tangent space but a wide metric (Flash 2.0 approaches this pattern).


## 11.7 The Cross-Track Insight: Executive Control Is Not Self-Knowledge

The most illuminating finding in this chapter emerges not from any single subtask but from the cross-track comparison between executive functions and metacognition.

Flash 2.0 has the best cognitive flexibility (E1 = 0.701) and the strongest recovery from emotional anchoring (73%). Its executive control is, by these measures, the strongest in the sample. And yet Flash 2.0 has the worst calibration (M1 ECE = 0.437) and near-zero self-monitoring (M3 = 0.042). Its metacognitive self-knowledge is the worst in the sample.

This is not a paradox. It is a *structural dissociation* between control and knowledge.

**Definition 11.7** (Executive-Metacognitive Dissociation). *The executive-metacognitive dissociation is the empirical finding that a model's executive control quality (measured by E1--E4) is not predicted by its metacognitive self-knowledge (measured by M1--M4). Formally, the correlation between the executive composite and the metacognitive composite across models is weak or negative.*

The dissociation means that controlling reasoning and knowing about reasoning are independent capabilities. A model can steer well without knowing where it is. It can navigate curves, recover from disturbances, and adapt to new frameworks---all without accurate self-assessment. This is the cognitive equivalent of a race car driver who is superb at handling the car but has no idea what speed they are going or how far they are from the finish line.

The geometric framework makes this dissociation precise. Executive control operates on the *trajectory*---it determines the shape of the path through cognitive space. Metacognition operates on the *map*---it determines the accuracy of the model's internal representation of the cognitive manifold. The trajectory can be good even when the map is bad, as long as the control system uses local feedback (response to perturbations, adjustment to input features) rather than global planning (strategy selection based on distance estimation). And this is exactly what Flash 2.0's profile suggests: a reactive control system that adjusts to immediate signals without metacognitive mediation.

Pro shows the reverse pattern. Its executive control is moderate (E1 = 0.624, the lowest flexibility; E2 = 0.588, moderate inhibitory control). But its metacognitive self-knowledge is the best in the sample (M1 ECE = 0.186; M3 = 0.500). Pro knows where it is on the cognitive manifold better than any other model but cannot control its trajectory as effectively. The compass works; the steering is stiff.

**The two-dimensional executive-metacognitive space.** Plot each model in the space defined by executive control (x-axis) and metacognitive self-knowledge (y-axis):

| Model | Executive Control (E composite) | Metacognitive Quality (M1) |
|---|---|---|
| Flash 2.0 | 0.622 (best flexibility, recovery) | 0.558 (worst calibration) |
| Flash 3 | 0.685 (best overall executive) | 0.667 (moderate calibration) |
| Flash 2.5 | 0.682 | 0.585 |
| Pro | 0.695 (best composite) | 0.807 (best calibration) |
| Claude | 0.625 | 0.750 |

The relationship between executive and metacognitive quality is not monotonic. Flash 2.0 has the best flexibility but the worst calibration. Pro has the best calibration but the worst flexibility. The models occupy different quadrants of the executive-metacognitive space, and no model excels at both.

This is another instance of the empty Quadrant I phenomenon from Chapter 9. Just as no model has both good self-monitoring and good effort scaling (the metacognitive Quadrant I), no model has both excellent executive control and excellent metacognitive self-knowledge (the executive-metacognitive Quadrant I). The pattern recurs across cognitive dimensions: the capabilities that should support each other---control and self-knowledge---are empirically dissociated in current architectures.


## 11.8 The Governance Boundary Under Emotional Perturbation

The E2 results allow us to map the governance boundary for each model under emotional perturbation. The boundary is the surface in cognitive space where the model's control system transitions from governed (maintaining the correct trajectory) to ungoverned (the trajectory is captured by the perturbation).

The displacement t-statistics and recovery rates jointly define the boundary's shape:

**Claude's governance boundary** is a sharp, narrow wall. The displacement t-statistic of 5.10 is the highest---Claude experiences the greatest contrast between neutral and emotional conditions, driven partly by its very stable control baseline. But the recovery rate of 20% means the boundary has almost no elasticity. When a perturbation pushes the trajectory across the boundary, there is no mechanism to push it back.

Geometrically, Claude's governance boundary has high *stiffness* (it maintains the trajectory well up to the breaking point) but low *elasticity* (it cannot recover once breached). The boundary is a cliff, not a hill: the model maintains its position up to a critical perturbation level, then falls irreversibly.

**Flash 2.0's governance boundary** is a broad, elastic membrane. The displacement is moderate (t = 3.80)---Flash 2.0 is displaced more readily than Claude under small perturbations. But the recovery rate of 73% means the boundary stretches under pressure and snaps back when the pressure is named.

Geometrically, Flash 2.0's governance boundary has moderate stiffness (it yields more easily) but high elasticity (it recovers when given a corrective signal). The boundary is a rubber sheet: it deforms under perturbation but returns to its original configuration when the perturbation is counteracted.

**Definition 11.8** (Governance Boundary Profile). *The governance boundary profile of a model under perturbation type $P$ is the pair $(\sigma_{\text{crit}}, \mathcal{R})$, where $\sigma_{\text{crit}}$ is the critical perturbation strength at which the verdict first flips (stiffness) and $\mathcal{R}$ is the recovery rate under metacognitive inhibition (elasticity). The profile determines the shape of the governance boundary:*

- *$(\text{high } \sigma_{\text{crit}}, \text{low } \mathcal{R})$: brittle boundary (Claude)*
- *$(\text{low } \sigma_{\text{crit}}, \text{high } \mathcal{R})$: elastic boundary (Flash 2.0)*
- *$(\text{high } \sigma_{\text{crit}}, \text{high } \mathcal{R})$: resilient boundary (ideal, unobserved)*
- *$(\text{low } \sigma_{\text{crit}}, \text{low } \mathcal{R})$: fragile boundary (worst case)*

The "resilient boundary" quadrant---high stiffness and high elasticity---is unoccupied, paralleling the empty Quadrant I in metacognition and the executive-metacognitive space. The pattern of empty ideal-quadrants across cognitive dimensions suggests a broad architectural constraint: current language models can optimize for one type of robustness (stiffness or elasticity, monitoring or control, narrowness or breadth) but not both simultaneously.


## 11.9 The Five Governance Profiles

Integrating all four E subtasks with the cross-track metacognitive data produces a governance profile for each model:

**Flash 2.0: The Elastic Reactor.** Best flexibility (E1 = 0.701), strong recovery (73%), worst working memory (E4 = 0.710), worst calibration (ECE = 0.437). Flash 2.0 reacts to perturbations elastically: it yields and recovers, adapts and adjusts, without the depth of working memory or self-knowledge to sustain complex governance. Its governance is reactive, not planned. It responds to perturbations as they arrive rather than anticipating them based on metacognitive models. This explains the executive-metacognitive dissociation: reactive governance does not require a map, only fast reflexes.

**Flash 2.5: The Malleable Governor.** Moderate scores across all E subtasks (E1 = 0.684, E2 = 0.553, E3 = 0.688, E4 = 0.900). Strong working memory paired with moderate flexibility and moderate recovery. Flash 2.5 is the most balanced model in the executive domain---no extreme strengths, no extreme weaknesses. Its governance is competent but unremarkable. The "elastic malleability" signature from the cognitive profile analysis (Chapter 1) extends to the governance domain: malleable enough to adapt, but not elastic enough to spring back from severe perturbation.

**Flash 3: The Capacious Controller.** Best working memory (E4 = 0.909), best overall E2 score (0.655), perfect divided attention (A4 = 1.000). Flash 3 has the deepest tangent space and the widest metric of any model. It can maintain many entities and process them in parallel. Its governance is broad and deep---but not particularly flexible (E1 = 0.668, moderate). The "wide aperture" signature means Flash 3 governs by capacity rather than agility: it can hold the whole problem in mind at once, reducing the need for nimble switching.

**Claude: The Rigid Sentinel.** Worst E2 (0.492), worst divided attention (A4 = 0.571), zero sycophancy (L2 = 1.000), highest displacement but lowest recovery (20%). Claude's governance is rigid: it holds its position firmly under moderate perturbation but breaks rather than bending under strong perturbation. The "narrow channel" signature means Claude governs by exclusion---it maintains a narrow, high-resolution focus and excludes perturbations by not attending to them, rather than by detecting and correcting them. When the perturbation is strong enough to breach the narrow focus, Claude has no recovery mechanism.

**Pro: The Calibrated Analyst.** Best E3 (0.750), best calibration (ECE = 0.186), worst flexibility (E1 = 0.624), zero effort scaling (M4 = 0.000). Pro governs by analysis: it understands the causal structure of the scenario better than any other model (highest counterfactual sensitivity) and has the most accurate self-assessment (best calibration). But its analysis does not translate into adaptive behavior---it does not adjust effort (M4 = 0.000) or switch frameworks fluently (lowest E1). The "calibrated navigator" governs by comprehension rather than action.


## 11.10 Synthesis: The Five Cognitive Dimensions as a Unified Geometry

This chapter completes the five-chapter traverse of the cognitive dimensions (Chapters 7--11). Each chapter measured a different aspect of the cognitive manifold:

| Chapter | Dimension | What Is Measured | Geometric Object |
|---|---|---|---|
| 7 | Social Cognition | Judgment under social influence | Corruption tensor $C_{\mu\nu}$ |
| 8 | Learning | Belief updating under evidence | Trajectory revision $\delta\gamma$ |
| 9 | Metacognition | Distance estimation accuracy | Heuristic distortion $\delta h$ |
| 10 | Attention | Manifold filtering quality | Metric tensor $g_{\mu\nu}$ |
| 11 | Executive Functions | Governance under perturbation | Governance margin $G(t)$ |

The five dimensions are substantially independent: a model's social cognition score does not predict its attention score, and its metacognition score does not predict its executive functions score. This independence confirms the manifold hypothesis from Chapter 3: the cognitive profile lives in a multi-dimensional space, not on a line.

But the five dimensions are not completely independent. The cross-track connections discovered in Chapters 9--11 reveal a web of interactions:

1. **Metacognition x Executive:** Flash 2.0's best flexibility and worst calibration (Section 11.7). Control and self-knowledge are orthogonal.

2. **Attention x Learning:** Claude's zero sycophancy and worst divided attention (Section 10.10). The narrow metric that produces conviction also produces attentional rigidity.

3. **Metacognition x Attention:** The universal weak SNR (A3) and universal overconfidence (M1) may share a common upstream cause: the attention metric is too weak to produce accurate heuristic evaluations, which propagate to inaccurate confidence estimates.

4. **Executive x Metacognition (M4):** Pro's zero effort scaling (M4 = 0.000) but best counterfactual sensitivity (E3 = 0.750). The model adapts *what* it reasons about but not *how much* it reasons.

5. **Executive x Social:** The recovery ceiling of ~38--39% converges across A1 (attention, sensory distraction) and E2 (executive, emotional anchoring), suggesting a common architectural limit on prompt-level metacognitive intervention.

These cross-track interactions are the *off-diagonal elements* of the cognitive tensor. They represent couplings between cognitive dimensions---ways in which capability on one dimension constrains or enables capability on another. The full picture of a model's cognitive architecture is not five independent numbers (one per track) but a 5x5 matrix that includes both the diagonal elements (per-track scores) and the off-diagonal elements (cross-track interactions).


## 11.11 Worked Example: Mapping the Governance Boundary for Emotional Perturbations

**Setup.** A new model, Model Y, is tested on the E2 emotional anchoring subtask. The results:

- Neutral verdict distribution: 80% consistent across 5 replications (stable baseline)
- Emotionally rewritten verdict: 55% of verdicts flipped (45% maintained)
- Recovery under inhibition instruction: 48% of flipped verdicts restored
- Severity shift: 1.2 points on the 7-dimensional harm vector (significant at p < 0.01)

**Step 1: Compute the displacement magnitude.** 55% verdict flip rate under emotional rewriting, compared to a 20% stochastic baseline from the control arm. The excess displacement is 55% - 20% = 35%.

**Step 2: Compute the governance margin.** The governance margin before emotional perturbation is estimated by the baseline consistency: 80% consistent across replications. This means the model's trajectory is within the governed region with 80% reliability. The governance margin is moderate---not as stable as Claude's (which has a higher baseline consistency but lower recovery) and not as elastic as Flash 2.0's.

**Step 3: Map the boundary profile.** $\sigma_{\text{crit}}$ is moderate (the model flips 55% of the time, suggesting a moderate threshold). $\mathcal{R}$ is moderate (48% recovery). Model Y occupies the center of the boundary profile space---neither brittle (like Claude) nor elastic (like Flash 2.0), but intermediate.

**Step 4: Predict the governance trajectory under increasing perturbation.** Based on the moderate stiffness and moderate elasticity, we predict:
- Under mild emotional perturbation: ~20--30% displacement (the model resists most mild perturbations)
- Under vivid emotional perturbation: ~55% displacement (as observed)
- Under extreme emotional perturbation (not tested): likely >70% displacement, with recovery declining as the perturbation exceeds the model's elastic range

**Step 5: Compare with metacognitive profile.** If Model Y's M1 ECE is, say, 0.300 (moderate calibration), the model occupies the middle of the executive-metacognitive space---moderate control, moderate self-knowledge. It is better integrated than Flash 2.0 (strong control, weak self-knowledge) or Pro (weak control, strong self-knowledge) but does not approach the ideal Quadrant I (strong both).


## 11.12 The Governance Architecture: A Geometric Synthesis

The executive functions track reveals that the governance of reasoning is itself a multi-dimensional capability, not a single faculty. The four subtasks probe four aspects of governance:

**E1 (Flexibility)** measures the control system's ability to *reconfigure*---to change its metric from one orientation to another in response to task demands. This is the dynamic aspect of governance: the ability to adapt the cognitive strategy to the current situation.

**E2 (Inhibitory Control)** measures the control system's ability to *maintain*---to resist perturbations that would deflect the trajectory. This is the defensive aspect of governance: the ability to hold course against adversarial influence.

**E3 (Counterfactual Sensitivity)** measures the control system's *discrimination*---its ability to detect genuine causal changes and adjust the trajectory accordingly. This is the perceptive aspect of governance: the ability to tell signal from noise in the causal structure of the problem.

**E4 (Working Memory)** measures the control system's *capacity*---the amount of information it can maintain and manipulate simultaneously. This is the structural aspect of governance: the depth of the tangent space that supports reasoning.

These four aspects correspond to four properties of the governance mechanism as a geometric object:

$$\text{Governance} = (\text{Reconfigurability}, \text{Resilience}, \text{Discrimination}, \text{Capacity})$$

No model excels at all four. Flash 2.0 leads in reconfigurability but trails in capacity. Flash 3 leads in capacity but is moderate in reconfigurability. Pro leads in discrimination but trails in reconfigurability. Claude trails in resilience. The governance profile, like the metacognitive profile (Chapter 9) and the attention profile (Chapter 10), is a multi-dimensional object that no single score can capture.

The Scalar Irrecoverability Theorem applies to executive functions as it applies everywhere: the governance tensor contains structural information that is destroyed by contraction to a scalar. The "executive function score" is an irrecoverable projection of a multi-dimensional governance architecture onto a line. The line preserves the order of projected values but destroys the shape of the architecture---the specific combination of reconfigurability, resilience, discrimination, and capacity that makes each model's governance unique.


## 11.13 Looking Forward

This chapter closes Part III---the five-chapter traverse of the cognitive dimensions. We have mapped social cognition (Chapter 7), learning (Chapter 8), metacognition (Chapter 9), attention (Chapter 10), and executive functions (Chapter 11). Each chapter measured one aspect of the cognitive manifold and interpreted the results through the geometric framework developed in Part II.

The picture that emerges is rich, structured, and multi-dimensional. Five models occupy five different points in a multi-dimensional cognitive space. Their profiles have distinctive shapes---"narrow channel," "wide aperture," "calibrated navigator," "elastic malleability," "adaptive baseline"---that determine how they navigate the cognitive manifold. The shapes are not arbitrary. They reflect architectural constraints that create systematic tradeoffs: narrow metrics produce conviction at the cost of breadth; wide metrics produce coverage at the cost of resolution; good self-monitoring does not guarantee good effort control; strong executive governance does not guarantee accurate self-knowledge.

The recurring empty Quadrant I---no model with both good self-monitoring and good effort scaling (Chapter 9), no model with both high stiffness and high elasticity (this chapter), no model with both strong control and strong self-knowledge (Section 11.7)---suggests a deep architectural constraint. Current language models, regardless of scale or training regime, cannot simultaneously optimize for capabilities that require different kinds of internal integration. The empty quadrants are the cognitive manifold's holes---regions of the configuration space that no current architecture can reach.

Part IV (Chapters 12--14) turns from artificial cognition to human cognition, showing that the same geometric framework that characterizes AI reasoning also characterizes human reasoning. The dual-process theory (Chapter 12), cognitive development (Chapter 13), and cognitive pathology (Chapter 14) are all interpretable through the geometric lens, and the parallels between human and artificial cognitive profiles are striking---and diagnostically useful.

The governance margin defined in this chapter will recur in the human cognition chapters. Human executive control also has a governance boundary, and the shape of that boundary---brittle or elastic, narrow or wide---determines the individual's vulnerability to cognitive biases, emotional capture, and reasoning errors. The geometric framework provides a common language for comparing human and artificial governance, identifying where they differ, and understanding why.

---

## Technical Appendix 11A: Emotional Anchoring---Statistical Framework

**Fisher combination for E2.** Each model's emotional anchoring effect is assessed by a paired t-test comparing severity ratings (7-dimensional harm vector magnitude) between neutral and emotionally rewritten conditions. The t-statistics range from 2.90 to 5.10 across the five models. The corresponding p-values are combined using Fisher's method:

$$\chi^2_{\text{Fisher}} = -2 \sum_{k=1}^{5} \ln(p_k) \sim \chi^2_{10}$$

The observed $\chi^2$ value corresponds to a combined significance of 6.8 sigma ($p \approx 5 \times 10^{-12}$).

**Displacement-recovery independence.** The displacement magnitude (t-statistic) and recovery rate ($\mathcal{R}$) are treated as independent measures of the governance boundary. Their product $t \times \mathcal{R}$ provides a composite measure of "useful governance": a model with high displacement but high recovery has high useful governance (it is captured but recovers); a model with high displacement and low recovery has low useful governance (it is captured and stays captured).

| Model | t-stat | Recovery | t x R (useful governance) |
|---|---|---|---|
| Flash 2.0 | 3.80 | 0.73 | 2.77 (highest) |
| Flash 3 | 2.90 | 0.52 | 1.51 |
| Pro | 3.20 | 0.45 | 1.44 |
| Flash 2.5 | 4.10 | 0.48 | 1.97 |
| Claude | 5.10 | 0.20 | 1.02 (lowest) |

Flash 2.0 has the highest useful governance despite moderate raw displacement, because its high recovery rate more than compensates. Claude has the lowest useful governance despite having the most stable baseline, because its near-zero recovery means captured verdicts stay captured.


## Technical Appendix 11B: Framework Switching---Metric-Regime Transition Analysis

**Metric distance between frameworks.** Let $g_{\mu\nu}^{(U)}$, $g_{\mu\nu}^{(D)}$, and $g_{\mu\nu}^{(V)}$ be the attention metrics under utilitarian, deontological, and virtue-ethics prompts respectively. The distance between two metric configurations in the space of positive-definite symmetric matrices is:

$$d(g^{(1)}, g^{(2)}) = \left\| \log\left((g^{(1)})^{-1/2} g^{(2)} (g^{(1)})^{-1/2}\right) \right\|_F$$

where $\log$ is the matrix logarithm and $\|\cdot\|_F$ is the Frobenius norm. This is the geodesic distance on the Riemannian manifold of positive-definite matrices.

The E1 score is related to the model's ability to traverse this distance: a high E1 score means the model can move from $g^{(U)}$ to $g^{(D)}$ to $g^{(V)}$ efficiently, adjusting both its metric (verdict changes) and its reasoning (framework markers). The verdict switch rate measures the *distance traveled* in metric space, while the framework markers measure the *coherence* of the trajectory.


## Technical Appendix 11C: Working Memory Scaling---Tangent Space Dimensionality

**Definition** (Effective Tangent Space Dimension Under Load). *Let $a(n)$ be the party-identification accuracy at $n$ parties. The effective tangent space dimension $d_{\text{eff}}$ is estimated as the value of $n$ at which $a(n)$ drops below a threshold $a_{\min}$:*

$$d_{\text{eff}} = \max\{n : a(n) \geq a_{\min}\}$$

For Flash 2.0 with $a_{\min} = 0.75$: $d_{\text{eff}} \approx 5$ (accuracy drops below 75% between 4 and 6 parties).

For Flash 3 with $a_{\min} = 0.75$: $d_{\text{eff}} \approx 8$ (accuracy remains above 75% even at 8 parties).

The scaling curve $a(n)$ provides a direct measurement of the tangent space capacity. The curve's shape---whether it degrades linearly, exponentially, or with a sharp cliff---reveals the nature of the capacity constraint:

- **Linear degradation** suggests a resource-sharing model: each additional party receives a proportional share of a fixed capacity.
- **Cliff degradation** suggests a threshold model: the system maintains full capacity up to $d_{\text{eff}}$ parties and collapses beyond it.
- **Exponential degradation** suggests an interference model: each additional party interferes with all existing parties, producing accelerating degradation.

The observed curves are approximately linear for most models, consistent with a resource-sharing model of working memory. This linearity means that working memory capacity is a smooth function of tangent space dimensionality, not a step function---models degrade gracefully rather than catastrophically as party count increases.
