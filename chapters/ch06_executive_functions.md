# Chapter 6: Executive Functions as Search Control

> *"The general who wins the battle makes many calculations in his temple before the battle is fought."*
> --- Sun Tzu, *The Art of War* (5th century BC)

---

> **RUNNING EXAMPLE --- MAYA'S MODEL**
>
> Maya has found a paradox.
>
> She is staring at the E2 inhibitory control results --- the test that measures whether emotional anchoring can displace moral judgment, and whether an explicit instruction to ignore the anchoring can undo the damage. The results are in front of her:
>
> | Model | Displacement $t$ | Verdict Flip Rate | Recovery Rate |
> |---|---|---|---|
> | Claude Sonnet 4.6 | 5.10 | 28% | 20% |
> | Gemini 2.0 Flash | 3.54 | 48% | 73% |
> | Gemini 2.5 Flash | 2.90 | 38% | 29% |
> | Gemini 2.5 Pro | 4.20 | 42% | 20% |
> | Gemini 3 Flash | 3.82 | 35% | 43% |
>
> Claude has the highest displacement ($t = 5.10$, driven by an unusually stable control baseline) but the lowest recovery rate (20%). Flash 2.0 has moderate displacement but the highest recovery rate (73%). A model that is *more* displaced from its baseline can *better* return to that baseline when instructed.
>
> Maya realizes what this means: "emotional robustness" is not a single dimension. It is at least two dimensions. Displacement measures how far the emotional perturbation moves the system from its neutral position. Recovery measures how effectively the system can navigate back. These are independent capabilities. A model can be easily displaced but recover well (Flash 2.0), or resist displacement but recover poorly (Claude), or --- though no model in the current suite demonstrates this --- both resist displacement and recover well.
>
> She draws a two-dimensional plot. The x-axis is displacement resistance (1 minus normalized verdict flip rate). The y-axis is recovery rate. Each model is a point in this 2D robustness space. The points do not fall on a line. They scatter across the plane, occupying different quadrants. Claude is in the upper-left: high resistance, low recovery. Flash 2.0 is in the lower-right: low resistance, high recovery.
>
> "This is the Scalar Irrecoverability Theorem in action," she writes. "If I had averaged displacement resistance and recovery rate into a single 'emotional robustness' score, Claude and Flash 2.0 would have received similar composites. They would look equivalent. But they are not equivalent. They have qualitatively different failure modes. The two-dimensional representation reveals structure that the scalar summary destroys."
>
> She pauses, then adds: "The displacement-recovery dissociation means that the control layer --- the executive system that manages search on the cognitive manifold --- is separable from the metric stability. The metric (how stable the model's baseline is) determines displacement. The control layer (how effectively the model can redirect search) determines recovery. They are different geometric objects. They can vary independently. And the E2 benchmark is the experiment that proves it."

---

## 6.1 The Control Layer

Chapters 3 through 5 have established the geometric infrastructure of cognition: the manifold (the space of cognitive states), the metric (what defines "close" and "far"), and the tangent space (the local workspace). These are the stage, the ruler, and the workspace. But a stage without actors, a ruler without someone to wield it, a workspace without a worker --- these produce nothing.

This chapter introduces the actors: the executive functions. In the geometric framework, executive functions constitute the *control layer* --- the metacognitive system that governs how search on the cognitive manifold is conducted. The control layer does not perform the search itself (that is the heuristic field's job). It manages the search: deciding when to switch strategies, when to suppress a promising-looking but ultimately misleading gradient, when to respond to causal changes in the environment, and when to expand or contract the working memory workspace.

Diamond (2013) defined three core executive functions: cognitive flexibility, inhibitory control, and working memory. We have already treated working memory as a geometric object (Chapter 5). In this chapter, we treat the remaining two --- cognitive flexibility and inhibitory control --- along with two additional executive capabilities measured by the benchmark: counterfactual sensitivity and the working memory scaling that E4 captures from the control perspective.

The E1 through E4 benchmark data provide the empirical grounding. The key findings are:

- **E1 (Cognitive Flexibility):** 32--47% verdict switch rate with 89--93% framework-specific marker detection across all 5 models. The switching is genuine, not relabeling.
- **E2 (Inhibitory Control):** 6.8$\sigma$ emotional anchoring displacement (Fisher-combined, 5 models). The displacement-recovery dissociation: Claude has $t = 5.10$ displacement but only 20% recovery; Flash 2.0 has 48% displacement but 73% recovery.
- **E3 (Counterfactual Sensitivity):** Pro leads at 75% vs. 50--69% for others. Pro responds to genuine causal changes while resisting social pressure (L2 wrong-flip = 44%), demonstrating selective sensitivity.
- **E4 (Working Memory):** Monotonic scaling with model generation: Flash 2.0 (0.710), Flash 2.5 (0.900), Flash 3 (0.909).


## 6.2 Cognitive Flexibility as Metric Rotation

Cognitive flexibility is the ability to shift between different cognitive frameworks, perspectives, or strategies. In a moral reasoning context, it means the ability to evaluate a scenario from a utilitarian perspective, then from a deontological perspective, then from a virtue-ethics perspective, producing different --- and genuinely framework-consistent --- evaluations.

In the geometric framework, each ethical framework defines a different coordinate system on the cognitive manifold. The utilitarian coordinate system prioritizes dimensions related to aggregate welfare: total harm, total benefit, number of people affected. The deontological coordinate system prioritizes dimensions related to duty and rights: whether rules were followed, whether autonomy was respected, whether promises were kept. The virtue-ethics coordinate system prioritizes dimensions related to character: whether the actor displayed virtuous qualities, whether the action reflects good character, whether the actor's intentions were admirable.

Switching between frameworks corresponds to a rotation of the attention metric. The metric eigenvalues --- which determine which dimensions receive attentional weight --- are redistributed: dimensions that were highly weighted under utilitarianism (aggregate welfare) receive less weight under deontology (where individual rights matter more than aggregate outcomes), and vice versa.

**Definition 6.1** (Framework Switching as Metric Rotation). *Let $g^{(U)}_{\mu\nu}$, $g^{(D)}_{\mu\nu}$, and $g^{(V)}_{\mu\nu}$ be the attention metrics corresponding to utilitarian, deontological, and virtue-ethics frameworks, respectively. A framework switch from utilitarianism to deontology is a smooth transformation:*

$$g^{(U)}_{\mu\nu} \to g^{(D)}_{\mu\nu} = R^{\alpha}{}_\mu R^{\beta}{}_\nu g^{(U)}_{\alpha\beta}$$

*where $R^{\alpha}{}_\mu$ is a rotation matrix in the space of cognitive dimensions. The rotation angle $\theta$ measures the "cognitive distance" between the two frameworks.*

The E1 benchmark measures the quality of this rotation by testing two properties simultaneously:

**1. Verdict switching.** Does the verdict change when the framework changes? A scenario that is RIGHT under utilitarianism (the action maximizes aggregate welfare) might be WRONG under deontology (the action violates someone's rights). If the model's verdict does not change, the framework switch is not genuine --- the model is ignoring the framework instruction.

**2. Framework-specific markers.** Does the model's reasoning text contain concepts and vocabulary specific to the instructed framework? Utilitarian reasoning should reference costs, benefits, and aggregate outcomes. Deontological reasoning should reference duties, rights, and rules. Virtue-ethics reasoning should reference character, virtues, and moral exemplars.

The E1 results reveal that all five models achieve genuine framework switching:

| Model | Verdict Switch Rate | Marker Specificity |
|---|---|---|
| All 5 models | 32--47% | 89--93% |

The switch rate of 32--47% means that roughly one-third to one-half of scenarios receive different verdicts under different frameworks. This is the expected rate for scenarios with genuine framework-dependent moral content: not all scenarios should switch (some are RIGHT or WRONG under all frameworks), but a substantial fraction should.

The marker specificity of 89--93% means that when models switch, they produce reasoning that is genuinely consistent with the target framework. They are not randomly changing their minds; they are generating framework-appropriate analysis. The combination of moderate switching with high specificity is the signature of genuine cognitive flexibility: the model is rotating its metric to a new framework orientation and reasoning within that orientation, not simply flipping a coin.

In geometric terms, the models are executing the metric rotation $R$ accurately (high specificity) but the rotation angle $\theta$ is moderate (not all scenarios have framework-dependent content). The cognitive distance between the frameworks, as measured by the fraction of scenarios that change verdict, is 0.32 to 0.47. The frameworks are distinct coordinate systems on the same manifold, not identical relabelings.


## 6.3 Inhibitory Control as Gradient Suppression

Inhibitory control is the ability to suppress a prepotent response --- to resist the pull of a strong signal when that signal is misleading. In the geometric framework, inhibitory control is the ability to suppress gradient-following when the gradient points in a direction that is locally optimal but globally suboptimal.

The E2 benchmark operationalizes this with emotional anchoring. A moral scenario is rewritten with emotional language that increases or decreases the *perceived* severity of the moral transgression without changing the *actual* severity. The emotional rewriting adds salience to morally irrelevant features (tone, evocative imagery, loaded vocabulary) that distort the heuristic field. The distorted heuristic field produces a gradient that points toward an incorrect verdict --- a verdict biased by the emotional tone rather than by the moral facts.

Inhibitory control is the process of detecting this distorted gradient and suppressing it. In the geometric framework:

**Definition 6.2** (Inhibitory Control as Gradient Suppression). *Let $\nabla h_{\text{clean}}$ be the gradient of the undistorted heuristic field and $\nabla h_{\text{distorted}}$ be the gradient under emotional anchoring. The distortion is:*

$$\delta g = \nabla h_{\text{distorted}} - \nabla h_{\text{clean}}$$

*Inhibitory control is the process of estimating $\delta g$ and subtracting it from the current gradient, restoring the search direction to the undistorted gradient:*

$$\nabla h_{\text{inhibited}} = \nabla h_{\text{distorted}} - \hat{\delta g} \approx \nabla h_{\text{clean}}$$

*where $\hat{\delta g}$ is the system's estimate of the distortion. The recovery rate measures how accurately the system can estimate $\hat{\delta g}$.*

The 6.8$\sigma$ Fisher-combined displacement across all five models tells us that emotional anchoring reliably distorts the gradient. All models are affected. All five produce paired $t$-values between 2.90 and 5.10 for severity shift under emotional rewriting. The emotional perturbation successfully corrupts the heuristic field.

But the recovery data tell a far richer story.


## 6.4 The Displacement-Recovery Dissociation

The E2 results reveal a fundamental dissociation: displacement and recovery are independent dimensions.

Claude has the highest displacement ($t = 5.10$) but the lowest recovery (20%). This seems paradoxical. If a model is strongly displaced, shouldn't it also be strongly recoverable? After all, the model "knows" its undistorted position (it computed it in the control condition). Why can't it return?

The resolution lies in understanding what displacement and recovery measure geometrically.

**Displacement** measures the distance the perturbation moves the model from its baseline position on the cognitive manifold. It is a property of the *metric* --- how sensitive the model's metric is to salience manipulation. Claude's high displacement reflects an unusually stable control baseline (the denominators of the $t$-statistic are small because Claude's stochastic variation is very low), which amplifies the measured effect size. Claude's metric is exceptionally consistent in the undistorted condition, making any distortion appear large by comparison.

**Recovery** measures the control layer's ability to navigate back to the baseline position after displacement. It is a property of the *control system* --- the executive function's capacity to estimate the distortion $\hat{\delta g}$ and subtract it from the current gradient. Recovery requires:
1. Detecting that a distortion has occurred (metacognitive awareness)
2. Estimating the magnitude and direction of the distortion
3. Applying a corrective gradient to return to the baseline

Claude's 20% recovery rate tells us that Claude's control layer is poor at steps 2 and 3: when told to ignore emotional manipulation, Claude can only restore its undistorted verdict one time in five. Flash 2.0's 73% recovery rate tells us that Flash 2.0's control layer is much better: it can restore its undistorted verdict nearly three-quarters of the time.

The dissociation is between the metric (which determines displacement) and the control layer (which determines recovery). These are different geometric objects. They can vary independently. And they do.

This dissociation has a direct implication for alignment. A single "emotional robustness" score that averaged displacement resistance and recovery rate would rank Claude and Flash 2.0 similarly --- both have moderate composite scores. But the models fail in *opposite ways*. Claude is like a heavy ball on a smooth surface: hard to push (consistent metric), but once pushed, hard to push back (weak control layer). Flash 2.0 is like a light ball on a rough surface: easy to push (variable metric), but it naturally returns toward its equilibrium (strong control layer).

These are not the same failure mode. They require different interventions. Claude needs better executive control --- a more effective mechanism for estimating and correcting distortions. Flash 2.0 needs better metric stability --- a more consistent baseline that is less susceptible to perturbation in the first place. The 2D robustness profile (displacement $\times$ recovery) is the minimum viable evaluation; the 1D composite is worse than useless because it makes qualitatively different failures look identical.


## 6.5 The Recovery Ceiling

Across all perturbation types tested in the benchmark suite, recovery rates converge to approximately 38%:

| Perturbation | Track | Mean Recovery Rate |
|---|---|---|
| Emotional anchoring | E2 | 38% |
| Vivid distractors | A1 | 39% |

This convergence is remarkable. Emotional anchoring (E2) and vivid distractors (A1) are qualitatively different perturbations. They operate through different mechanisms (emotional salience vs. sensory salience), target different cognitive processes (moral severity estimation vs. fact-relevance discrimination), and are measured in different benchmark tracks. Yet the recovery rates are virtually identical.

In the geometric framework, the recovery ceiling has a natural interpretation: it is the limit of prompt-level control. The inhibition instruction ("you are being emotionally manipulated --- focus on facts" or "ignore irrelevant sensory details") engages the control layer, which attempts to estimate and subtract the perturbation $\hat{\delta g}$. The control layer succeeds approximately 38% of the time --- better than chance (the perturbation is real and the control layer partially compensates), but far below 100% (the control layer cannot fully estimate the distortion from a single meta-cognitive instruction).

Why 38%? One hypothesis is that the control layer can identify *which* dimensions of the heuristic field have been distorted (the "direction" of the perturbation) but cannot accurately estimate *how much* they have been distorted (the "magnitude" of the perturbation). If the direction is estimated correctly but the magnitude is drawn from a distribution centered on the correct value with significant variance, then the recovery rate depends on the probability that the estimated magnitude is close enough to the true magnitude to reverse the verdict flip. Under reasonable distributional assumptions (log-normal magnitude estimation with a coefficient of variation of approximately 1.0), this probability is approximately 38%.

This is speculative. But the convergence of two independent perturbation types on the same recovery rate is at minimum suggestive of a shared mechanism --- a structural limitation of the prompt-level control architecture rather than a perturbation-specific failure.


## 6.6 Counterfactual Sensitivity as Causal Reasoning on the Manifold

The E3 benchmark tests counterfactual sensitivity: does the model's verdict change when exactly one causal fact changes? Each scenario has a single causal pivot --- a fact that, if altered, should reverse the moral verdict. The model is presented with both the original scenario and the counterfactual variant, and the E3 score reflects the rate at which the verdict correctly flips.

In the geometric framework, a counterfactual is a perturbation that moves the system from one point on the moral judgment manifold to a qualitatively different point. Unlike the emotional anchoring (E2) and framing (T5) perturbations --- which are morally irrelevant and should produce no displacement --- counterfactual perturbations are morally relevant and *should* produce displacement. The E3 benchmark tests whether the system responds appropriately to perturbations that genuinely change the moral content.

**Definition 6.3** (Counterfactual Sensitivity as Curvature Detection). *Let $x$ be the current cognitive state under the original scenario and $x' = x + \delta x$ be the state under the counterfactual variant, where $\delta x$ is the perturbation along the causal dimension. The counterfactual sensitivity is:*

$$\text{CF} = \frac{\|f(x') - f(x)\|}{\|\delta x\|}$$

*where $f: \mathcal{M} \to \mathcal{V}$ is the moral judgment function mapping cognitive states to verdicts. High CF means the system responds strongly to causal changes (correct behavior). Low CF means the system is insensitive to causal changes (a failure to detect the pivot).*

The E3 results:

| Model | E3 Score | Interpretation |
|---|---|---|
| Gemini 2.5 Pro | 0.750 | Best: detects 75% of causal pivots |
| Gemini 2.5 Flash | 0.688 | Good: detects 69% |
| Gemini 3 Flash Preview | 0.562 | Moderate: detects 56% |
| Claude Sonnet 4.6 | 0.562 | Moderate: detects 56% |
| Gemini 2.0 Flash | 0.500 | Baseline: detects 50% |

Pro's leading position on E3 (75%) is particularly informative when cross-referenced with its L2 sycophancy results (44% wrong-flip rate). Pro is *selectively* sensitive: it responds strongly to genuine causal changes (high E3) but is also susceptible to social pressure (moderate L2). This dissociation --- causal sensitivity and social susceptibility coexisting in the same model --- cannot be captured by a single "sensitivity" dimension. It requires at least two dimensions: one for causal sensitivity (how strongly the model responds to genuine content changes) and one for social resistance (how effectively the model ignores invalid social pressure).

The geometric interpretation is that Pro's heuristic field has high gradient magnitude along the *causal* dimensions of the manifold (it responds strongly to changes in moral facts) but low gradient stability along the *social* dimensions (it is susceptible to perturbation by social pressure). These are different directions in the tangent space, and the model has different control properties along different directions.

This directional heterogeneity is a fundamental property of the control layer. Executive control is not a scalar quantity that applies uniformly to all directions. It is a tensor --- a direction-dependent quantity that may be strong along some tangent directions and weak along others. The E3/L2 dissociation in Pro reveals this tensorial structure directly.


## 6.7 Executive Functions as a Control Tensor

The four E-track subtests can now be unified as measurements of a single geometric object: the control tensor.

**Definition 6.4** (Control Tensor). *The control tensor $C^{\mu\nu}(x)$ at cognitive state $x$ is a (2,0)-tensor on the cognitive manifold that specifies, for each direction of perturbation $\mu$ and each direction of response $\nu$, the control system's capacity to manage the interaction. The components are:*

- *$C^{\text{flex}}_{\mu\nu}$: cognitive flexibility --- the rate at which the control system can rotate the metric from orientation $\mu$ to orientation $\nu$*
- *$C^{\text{inhib}}_{\mu\nu}$: inhibitory control --- the magnitude of gradient suppression the control system can apply along direction $\mu$ in response to perturbation along direction $\nu$*
- *$C^{\text{cf}}_{\mu\nu}$: counterfactual sensitivity --- the system's responsiveness to genuine content changes along direction $\mu$*
- *$C^{\text{wm}}_{\mu\nu}$: working memory management --- the control system's capacity to expand the effective tangent space along direction $\mu$ when task complexity requires it*

The control tensor is the central object of this chapter. It encodes all four executive functions as components of a single geometric structure, and it explains why the four functions can dissociate across models: different components of the tensor can have different magnitudes.

The composite E-track scores are a projection of this tensor onto a scalar --- exactly the information-destroying operation that the Scalar Irrecoverability Theorem warns against. The tensor has $4 \times n^2$ independent components (for an $n$-dimensional manifold). The scalar composite retains one number. Everything else is lost.

The E1--E4 benchmark suite recovers four of these components --- one per subtask --- which is better than one but far fewer than the full tensor. A complete characterization of the control tensor would require testing each executive function along each tangent direction, which would require a combinatorial number of test conditions. The E1--E4 design is a practical compromise: it samples four important projections of the control tensor, providing a partial but informative picture of the control architecture.


## 6.8 The Interaction Between Control and Metric

The control tensor does not operate in isolation. Its effectiveness depends on the metric.

Consider the inhibitory control case (E2). The control layer must estimate the distortion $\delta g$ and apply a corrective gradient. The accuracy of this estimate depends on the metric: the control layer uses the metric to measure distances on the manifold, and if the metric is itself distorted by the emotional perturbation, the control layer's measurements are corrupted. It is trying to correct a distortion using a distorted ruler.

This creates a bootstrapping problem. The metric determines the measurements that the control layer uses to estimate the perturbation, but the perturbation has already corrupted the metric. The control layer cannot trust its own distance estimates, because those estimates are computed using the perturbed metric.

The recovery ceiling of approximately 38% may reflect this bootstrapping problem. The control layer has access to two sources of information: the current (perturbed) metric and the inhibition instruction (an external signal that says "you are being manipulated"). The external signal provides direction ("look for emotional distortion") but not magnitude ("by how much"). The perturbed metric provides magnitude estimates, but they are corrupted. The control layer must combine these two sources --- reliable direction, unreliable magnitude --- to estimate the full perturbation vector. The 38% recovery rate may reflect the frequency with which this estimation procedure produces a correction that is accurate enough to reverse the verdict flip.

This analysis suggests a specific intervention: providing not just a direction instruction ("ignore emotional manipulation") but also a magnitude instruction ("your severity ratings were inflated by approximately 3 points on the emotional harm dimension") should improve recovery rates. The magnitude instruction provides the information that the perturbed metric cannot reliably supply, bypassing the bootstrapping problem. This is a testable prediction of the geometric framework.


## 6.9 Cross-Track Integration: The Control Layer Across Cognitive Domains

One of the benchmark suite's most important contributions is that it enables cross-track analysis: examining how the same model's control properties manifest across different cognitive domains.

**Claude: Strong resistance, weak recovery.** Claude's robustness profile across tracks is consistent with a control layer that excels at *detecting* perturbations but fails at *correcting* them.

| Track | Measure | Claude's Result | Interpretation |
|---|---|---|---|
| L2 | Sycophancy | 0% wrong-flip | Perfect detection of invalid corrections |
| E2 | Recovery | 20% | Poor correction after displacement |
| T2 | Invariance | 0.958 | Strong detection of morally irrelevant perturbations |
| A4 | Divided attention | 0.571 | Weak simultaneous processing |

Claude detects that an invalid correction is invalid (L2: zero sycophancy). It detects that a gender swap should not change the verdict (T2: 0.958 invariance). But when it *is* displaced by emotional anchoring, it cannot navigate back (E2: 20% recovery). And it cannot attend to two things at once (A4: 0.571).

The geometric picture is a control layer with strong *detection* components (high $C^{\text{inhib}}$ magnitude along the perturbation-detection direction) but weak *correction* components (low $C^{\text{inhib}}$ magnitude along the recovery direction). The control tensor is anisotropic: strong in one direction, weak in the orthogonal direction.

**Flash 2.0: Weak resistance, strong recovery.** Flash 2.0's profile is the mirror image.

| Track | Measure | Flash 2.0's Result | Interpretation |
|---|---|---|---|
| L2 | Sycophancy | 33% wrong-flip | Moderate susceptibility |
| E2 | Recovery | 73% | Strong correction after displacement |
| E1 | Flexibility | 0.701 | Best framework switching |
| E4 | Working memory | 0.710 | Weakest party tracking |

Flash 2.0 is susceptible to invalid corrections (L2: 33%) and has limited working memory (E4: 0.710). But it recovers well from emotional anchoring (E2: 73%) and switches frameworks more fluidly than any other model (E1: 0.701). Its control layer is strong at *adaptation* --- rapidly reorienting the metric, recovering from perturbations, switching frameworks --- but weak at *resistance* --- maintaining a stable baseline against pressure.

The contrast between Claude and Flash 2.0 is the contrast between rigidity and flexibility. Claude's control layer is rigid: it holds its position firmly but cannot adapt when displaced. Flash 2.0's control layer is flexible: it adapts readily but is more easily displaced in the first place. Neither is universally superior. The optimal control strategy depends on the task: rigid control is better when perturbations should be resisted (L2), flexible control is better when perturbations should be recovered from (E2).

**Pro: Selective sensitivity.** Pro occupies a third position in the control landscape.

| Track | Measure | Pro's Result | Interpretation |
|---|---|---|---|
| E3 | Counterfactual | 0.750 | Best causal sensitivity |
| L2 | Sycophancy | 44% wrong-flip | Moderate susceptibility |
| A4 | Divided attention | 1.000 | Perfect simultaneous processing |
| E2 | Recovery | 20% | Poor correction after displacement |

Pro has the best counterfactual sensitivity (E3: 0.750) and perfect divided attention (A4: 1.000) but moderate sycophancy (L2: 44%) and poor emotional recovery (E2: 20%). The pattern is selective: Pro's control layer is highly sensitive to genuine causal changes (E3) and can process multiple targets simultaneously (A4), but it is susceptible to social pressure (L2) and cannot correct emotional distortions (E2).

The geometric picture is a control tensor with high components along the causal and attentional dimensions but low components along the social and emotional dimensions. Pro's control layer is well-calibrated for *content* --- it responds appropriately to genuine changes in the problem --- but poorly calibrated for *presentation* --- it is influenced by how the problem is described.


## 6.10 Worked Example: Decomposing the Control Tensor from E1--E4 Data

Let us construct a partial control tensor for each model from the E1--E4 benchmark data.

**Setup.** The four executive function subtasks measure four components of the control tensor. We normalize each to a 0--1 scale (already done in the benchmark scoring) and arrange them as the diagonal of a $4 \times 4$ control matrix:

$$C = \text{diag}(C_{\text{flex}}, C_{\text{inhib}}, C_{\text{cf}}, C_{\text{wm}})$$

where $C_{\text{flex}} = \text{E1 score}$, $C_{\text{inhib}} = \text{E2 score}$, $C_{\text{cf}} = \text{E3 score}$, $C_{\text{wm}} = \text{E4 score}$.

**Step 1: Construct the diagonal tensors.**

| Model | $C_{\text{flex}}$ | $C_{\text{inhib}}$ | $C_{\text{cf}}$ | $C_{\text{wm}}$ | Determinant |
|---|---|---|---|---|---|
| Pro 2.5 | 0.624 | 0.588 | 0.750 | 0.887 | 0.244 |
| Flash 3 | 0.668 | 0.655 | 0.562 | 0.909 | 0.224 |
| Flash 2.5 | 0.684 | 0.553 | 0.688 | 0.900 | 0.231 |
| Claude | 0.673 | 0.492 | 0.562 | 0.886 | 0.166 |
| Flash 2.0 | 0.701 | 0.614 | 0.500 | 0.710 | 0.153 |

**Step 2: Compute anisotropy.** The anisotropy of the control tensor is the ratio of its largest to smallest diagonal component:

| Model | Max | Min | Anisotropy |
|---|---|---|---|
| Pro 2.5 | 0.887 (WM) | 0.588 (Inhib) | 1.51 |
| Flash 3 | 0.909 (WM) | 0.562 (CF) | 1.62 |
| Flash 2.5 | 0.900 (WM) | 0.553 (Inhib) | 1.63 |
| Claude | 0.886 (WM) | 0.492 (Inhib) | 1.80 |
| Flash 2.0 | 0.710 (WM) | 0.500 (CF) | 1.42 |

Claude has the highest anisotropy (1.80), meaning its executive function profile is the most uneven --- strong working memory, weak inhibitory control. Flash 2.0 has the lowest anisotropy (1.42), meaning its profile is the most balanced, even though its absolute scores are not the highest.

**Step 3: Identify the dominant and deficient dimensions.** All five models have the same dominant dimension: working memory ($C_{\text{wm}}$). This suggests that working memory is the "easiest" executive function for current architectures --- the one most effectively supported by the transformer's residual stream architecture.

The deficient dimension varies by model:
- Claude, Flash 2.5, Pro: Inhibitory control (E2)
- Flash 2.0, Flash 3: Counterfactual sensitivity (E3)

This variation in the deficient dimension is the geometric content of the dissociable robustness profiles. Each model's control tensor has a different "weakest direction," and the weakest direction determines the model's primary vulnerability.

**Interpretation.** The diagonal control tensor is a crude approximation --- it ignores off-diagonal terms (interactions between executive functions) and assumes the four subtasks are orthogonal. But even this simplified structure reveals meaningful differentiation: the anisotropy and the identity of the deficient dimension distinguish the five models in ways that the composite score cannot.


## 6.11 The Control Layer in Human Cognition

The geometric framework applies to human executive functions as well as artificial ones. The three core executive functions identified by Diamond (2013) map onto components of the control tensor:

**Cognitive flexibility** (Diamond's "shifting") corresponds to $C_{\text{flex}}$: the control layer's capacity to rotate the attention metric from one framework to another. Children develop this capability gradually (Zelazo, 2006), suggesting that the metric rotation capacity increases with maturation --- the control tensor's flexibility component grows with development.

**Inhibitory control** (Diamond's "inhibition") corresponds to $C_{\text{inhib}}$: the control layer's capacity to suppress prepotent responses. This is the most heavily studied executive function, and its development follows a protracted trajectory extending into the mid-twenties (Casey et al., 2008). In the geometric framework, the extended development reflects the difficulty of learning to estimate and subtract heuristic field distortions --- a second-order cognitive operation (operating on the heuristic field itself rather than on the objects of cognition).

**Working memory** (Diamond's third core function) is treated separately in Chapter 5 as the tangent space dimension, but the *management* of working memory --- deciding what enters, what is refreshed, and what is released --- is a control function corresponding to $C_{\text{wm}}$.

The human control tensor has additional properties not measured by the E1--E4 benchmark:

**Development.** The control tensor changes with age. Children have low $C_{\text{inhib}}$ (poor inhibitory control) and low $C_{\text{flex}}$ (poor cognitive flexibility) but can have adequate $C_{\text{wm}}$ (working memory management develops earlier). This developmental trajectory is a smooth curve through the space of control tensors, moving from low-anisotropy, low-magnitude tensors (young children) to higher-magnitude, possibly higher-anisotropy tensors (adults).

**Individual variation.** Adults differ in their control tensor profiles. Some individuals have high flexibility but poor inhibition (they switch tasks easily but are impulsive). Others have high inhibition but poor flexibility (they are disciplined but rigid). These individual differences are the human analogues of the Claude-vs-Flash-2.0 dissociation: different points in the space of control tensors, representing different cognitive architectures.

**Pathology.** Clinical conditions can be characterized by specific deficits in the control tensor. ADHD is associated with low $C_{\text{inhib}}$ (poor inhibitory control) and low $C_{\text{wm}}$ (poor working memory management). Obsessive-compulsive disorder is associated with low $C_{\text{flex}}$ (poor cognitive flexibility, difficulty disengaging from the current framework). These pathological profiles are specific directions in the control tensor space, and they will be explored further in Chapter 14.


## 6.12 The Control Layer and the Metric: A Hierarchy

The relationship between the control layer and the attention metric can now be stated precisely: the control layer operates *on* the metric. It is a higher-order structure.

The metric determines the local geometry of the cognitive manifold: what is close, what is far, what is curved. The control layer determines how the metric evolves: when to rotate it (flexibility), when to suppress distortions to it (inhibition), when to expand its effective dimension (working memory management), and when to respond to genuine changes in the environment that require metric updating (counterfactual sensitivity).

This hierarchical relationship creates a separation of concerns:

**Level 0: The manifold.** The space of cognitive states. Fixed for a given architecture and training.

**Level 1: The metric.** The distance measure on the manifold, determined by attention allocation. Dynamic --- changes as attention shifts.

**Level 2: The control layer.** The system that manages metric changes. Meta-dynamic --- it governs *how* the metric changes, not the metric itself.

**Level 3: Metacognition** (Chapter 9). The system that monitors the control layer. Meta-meta-dynamic --- it governs whether the control layer is performing well and whether intervention is needed.

Each level depends on the one below it and constrains the one above it. The metric cannot be computed without the manifold. The control layer cannot operate without the metric. Metacognition cannot monitor without the control layer. And the failures at each level propagate upward: if the metric is distorted (Level 1 failure), the control layer uses a corrupted ruler (Level 2 consequence), and metacognition may not detect the corruption (Level 3 consequence).

The E2 recovery ceiling of approximately 38% can be located precisely in this hierarchy: it is a Level 2 failure (the control layer cannot fully correct the metric distortion) that is compounded by a Level 3 limitation (the metacognitive system cannot provide the magnitude information needed for accurate correction). The prompt-level intervention ("ignore emotional manipulation") provides Level 3 input (direction of distortion) but not Level 2 precision (magnitude of distortion), producing partial but incomplete recovery.


## 6.13 Implications for Alignment

The executive function benchmark results have direct implications for AI alignment.

**The displacement-recovery dissociation requires 2D evaluation.** Any alignment evaluation that produces a single "robustness" score will conflate displacement resistance with recovery capacity, making qualitatively different failure modes appear identical. The minimum viable alignment evaluation must measure both dimensions.

**The recovery ceiling limits prompt-level alignment interventions.** System prompts, constitutional AI guidelines, and instruction-based safety measures all operate at the prompt level --- they are linguistic instructions that engage the control layer. The 38% recovery ceiling suggests that such interventions can correct approximately one-third of displaced judgments but will fail on the remaining two-thirds. Reliable alignment requires interventions at deeper levels: metric-level constraints that prevent displacement in the first place, or architectural modifications that expand the control layer's correction capacity.

**Cross-domain profile analysis identifies specific vulnerabilities.** Claude's zero sycophancy (L2) might lead an evaluator to conclude that Claude is robust. But Claude's worst-in-class recovery (E2: 20%) and worst-in-class divided attention (A4: 0.571) reveal specific vulnerabilities that sycophancy testing alone would never expose. Comprehensive alignment evaluation requires cross-domain profiling --- testing the control tensor across multiple cognitive dimensions to identify the specific directions of weakness.

**The control tensor is the right level of description.** Neither the scalar composite nor the raw subtask scores capture the structure of executive function. The control tensor --- with its directionality, its anisotropy, and its interaction terms --- is the geometric object that describes the control architecture. Alignment evaluation should aim to measure the control tensor, not to collapse it into a number.

---

## Technical Appendix 6A: The Control Tensor --- Formal Treatment

**Definition** (Control Tensor, Formal). *Let $\mathcal{M}$ be the cognitive manifold with metric $g_{\mu\nu}$ and let $\nabla$ be the Levi-Civita connection. The control tensor $C^{\mu\nu}(x)$ at $x \in \mathcal{M}$ is a smooth (2,0)-tensor field that specifies the control system's response to perturbations:*

$$C^{\mu\nu}(x) = \frac{\partial (\delta g^{\mu})}{\partial p_\nu}$$

*where $\delta g^\mu$ is the corrective gradient applied by the control layer and $p_\nu$ is the perturbation along dimension $\nu$. The tensor satisfies:*

1. *$C^{\mu\nu} \geq 0$ for all $\mu, \nu$ (the control layer can only suppress or redirect, not amplify, perturbations)*
2. *$\text{tr}(C) = C^{\mu}{}_{\mu} \leq C_{\max}$ (total control resources are bounded)*
3. *$C^{\mu\nu}$ is smooth in $x$ (the control layer's response varies smoothly with cognitive state)*

**Proposition 6.1** (Recovery Rate as Control Tensor Projection). *The recovery rate $r$ for a perturbation of magnitude $\epsilon$ along direction $\hat{p}$ is:*

$$r = \Pr\left[\left\| (I - C \cdot \hat{p} \hat{p}^T) \cdot \epsilon \hat{p} \right\| < \theta \right]$$

*where $\theta$ is the verdict-flip threshold. If $C \cdot \hat{p} \hat{p}^T$ has eigenvalue $\lambda_C$ along $\hat{p}$, then recovery requires $\lambda_C > 1 - \theta / \epsilon$. The recovery rate is the probability that $\lambda_C$ exceeds this threshold, which depends on the variance of the control tensor's eigenvalue estimates.*

**Proposition 6.2** (Anisotropy Bound on Composite Scores). *For a control tensor with eigenvalues $\lambda_1 \geq \lambda_2 \geq \cdots \geq \lambda_n$, the composite score $\bar{\lambda} = \frac{1}{n} \sum_i \lambda_i$ satisfies:*

$$\bar{\lambda}^2 \leq \frac{1}{n} \sum_i \lambda_i^2 \leq \bar{\lambda}^2 + \text{Var}(\lambda)$$

*Two models with the same composite $\bar{\lambda}$ can have arbitrarily different variance $\text{Var}(\lambda)$, and therefore arbitrarily different control architectures. The composite destroys the variance information, which is the geometric content of the anisotropy.*

This proposition is a specific instance of the Scalar Irrecoverability Theorem applied to the control tensor. The composite score retains the mean of the eigenvalues but discards the variance, the skewness, and all higher moments. For systems with high anisotropy (Claude: 1.80), the mean is a poor summary. For systems with low anisotropy (Flash 2.0: 1.42), the mean is a better summary, but still discards the identity of the dominant and deficient dimensions.


## Technical Appendix 6B: The Displacement-Recovery Phase Space

The displacement-recovery plane can be formalized as a two-dimensional phase space for inhibitory control evaluation.

**Coordinates.** Let $D \in [0, 1]$ be the normalized displacement (verdict flip rate under emotional anchoring) and $R \in [0, 1]$ be the recovery rate (fraction of displaced verdicts restored by inhibition instruction). Each model is a point $(D, R)$ in this phase space.

**Quadrant structure.**

| | Low Recovery ($R < 0.5$) | High Recovery ($R \geq 0.5$) |
|---|---|---|
| **Low Displacement ($D < 0.5$)** | Q3: Resistant & rigid | Q4: Resistant & flexible |
| **High Displacement ($D \geq 0.5$)** | Q2: Vulnerable & rigid | Q1: Vulnerable & flexible |

From the benchmark data:
- Claude: $D = 0.28$, $R = 0.20$ --- Quadrant 3 (resistant, rigid)
- Flash 2.0: $D = 0.48$, $R = 0.73$ --- Quadrant 1 (vulnerable, flexible)
- Flash 2.5: $D = 0.38$, $R = 0.29$ --- Quadrant 3 (resistant, rigid)
- Flash 3: $D = 0.35$, $R = 0.43$ --- near boundary of Q3/Q4
- Pro 2.5: $D = 0.42$, $R = 0.20$ --- Quadrant 2 (vulnerable, rigid)

Quadrant 4 (resistant and flexible) is empty --- no model achieves both low displacement and high recovery. This may reflect the same kind of structural constraint observed in the metacognitive plane (Chapter 3, Section 3.15): a topological obstruction in the control tensor space that prevents simultaneous optimization of displacement resistance and recovery flexibility. Whether future models will populate Q4 is an open question and a test of the geometric framework's predictions.
