# Chapter 16: The Five Geometric Signatures

> *"The map is not the territory."*
> --- Alfred Korzybski, *Science and Sanity* (1933)

---

> **RUNNING EXAMPLE --- MAYA'S MODEL**
>
> Maya is standing at a podium.
>
> The conference room at the International Conference on Cognitive Science holds four hundred people, and it is full. The title on the screen behind her reads: "Five Models, One Score, Five Architectures: The Geometric Fingerprint of Artificial Cognition." She has fifteen minutes.
>
> She begins with a provocation. "I'm going to show you five radar charts. Each chart represents a model's performance across the five cognitive dimensions of the Measuring AGI benchmark. Each model has a different composite score, ranging from 0.63 to 0.72. But I'm going to argue that the composite score is the least interesting thing about these charts. The interesting thing is the *shape*."
>
> She puts up the first slide. Five radar charts, five axes each --- Social Cognition, Learning, Metacognition, Attention, Executive Functions --- with each axis normalized to a 0--1 scale. The five shapes are strikingly different.
>
> Claude's chart is a narrow spike. It extends far along the Social Cognition axis (high invariance, zero sycophancy) and the Metacognition axis (moderate calibration, strong self-monitoring), but collapses along the Attention axis (worst divided attention in the sample) and the Executive Functions axis (worst emotional recovery). The shape is a stiletto: sharp, narrow, and maximally extended along a single direction.
>
> Flash 3's chart is nearly circular. It extends moderately along every axis, with its longest extension along Attention (perfect divided attention score). The shape is a disk: wide, even, and uniformly extended. No axis is dramatically strong; no axis is dramatically weak.
>
> Pro's chart is lopsided. The Metacognition axis extends far (best calibration in the sample, ECE = 0.186) and the Executive Functions axis extends far along the counterfactual sub-dimension (best E3 score). But the Learning axis is short (zero effort scaling) and the Attention axis is moderate. The shape is a bent wing: strong on the analytic dimensions, weak on the adaptive dimensions.
>
> Flash 2.5's chart is the most irregular. It has the longest extension along Learning (worst sycophancy at 56%, paradoxically making it the most *measurably* biased) and the shortest extension along Metacognition. But its Attention sub-scores are extreme: best distractor resistance, strong working memory. The shape is a zigzag: alternating peaks and valleys with no smooth interpolation between them.
>
> Flash 2.0's chart is broad and flat. Its Executive Functions extension is the longest in the sample (best flexibility, best recovery). Its Learning extension is moderate. Its Attention extension is moderate. Its Metacognition extension is the shortest (worst calibration). The shape is a plateau: wide and low, with strong base capabilities but no peak performance.
>
> "Five shapes," Maya says. "Each shape is a cognitive architecture. Each architecture determines not just how well the model performs, but *how* it performs --- which problems it handles easily, which problems break it, and *why*."
>
> She advances to the next slide, which shows the composite scores:
>
> | Model | Composite Score |
> |---|---|
> | Flash 3 | 0.72 |
> | Pro | 0.70 |
> | Claude | 0.68 |
> | Flash 2.5 | 0.66 |
> | Flash 2.0 | 0.63 |
>
> "These composite scores form a ranking. Flash 3 is 'best,' Flash 2.0 is 'worst.' But let me ask you: best at *what*? The composite score tells you that Flash 3 is 'better' than Flash 2.0. It does not tell you that Flash 2.0 has the best emotional recovery in the sample. It does not tell you that Flash 2.0 has the best cognitive flexibility. It does not tell you that Flash 2.0 is the model you want if you need a system that can recover from adversarial manipulation, because its elastic governance boundary means it bends but doesn't break."
>
> She advances again. "The composite score is a scalar projection of a multi-dimensional object. The Scalar Irrecoverability Theorem from Chapter 1 tells us that the projection destroys information that cannot be recovered. The five shapes I just showed you are the information that is destroyed. And the shapes are the *diagnostic* information --- the information that tells you which model to deploy for which task, which model is vulnerable to which attack, and which architectural changes would improve which capability."
>
> A hand goes up in the back row. "You said the composite scores are different. That means the ranking isn't arbitrary --- Flash 3 really is better on average."
>
> "On average, yes," Maya says. "But 'on average' is exactly the problem. If you average Claude's stiletto and Flash 2.0's plateau, you get the same number. The average is the same. The architectures are opposite. The clinical analogy is averaging a patient's blood pressure and temperature to get a 'health score.' A health score of 120 could be blood pressure 120, temperature 120 --- which is catastrophic. Or blood pressure 140, temperature 100 --- which is hypertensive but afebrile. Or blood pressure 100, temperature 140 --- which is hypothermic and febrile. Same average. Different diagnoses. Different treatments. The composite score is the health score. The geometric signature is the chart."
>
> The room is quiet. Maya advances to the five detailed analyses.

---

## 16.1 The Case for Cognitive Fingerprints

This chapter presents the capstone finding of the Measuring AGI benchmarks: the five geometric signatures of the five models tested. Each signature is a multi-dimensional profile that captures the model's cognitive architecture --- its specific combination of strengths and weaknesses across the five cognitive dimensions --- in a way that no scalar score can.

The argument for geometric signatures rests on three pillars:

**Pillar 1: The Scalar Irrecoverability Theorem (Chapter 1).** The theorem proves that any scalar projection of a multi-dimensional cognitive profile destroys structural information that cannot be recovered from the scalar alone. The five geometric signatures are the structural information that composite scores destroy.

**Pillar 2: The empirical distinctiveness of the profiles (Chapters 7--11).** The five models tested in the benchmark suite have distinct, characteristic profiles that are not captured by rank ordering. Models with similar composite scores have radically different profile shapes. Models with different composite scores can have overlapping strengths that the ranking obscures.

**Pillar 3: The diagnostic utility of the profiles.** The profile shape predicts model behavior in ways that the composite score does not: which tasks the model will fail, what kind of failures it will produce, and how it will respond to interventions. The profile is clinically useful; the composite score is not.

The five signatures are presented below, each with a full analysis of the radar chart, the defining features, the geometric interpretation, and the diagnostic implications.


## 16.2 Claude 3.5 Sonnet: "Narrow Channel"

**The profile.**

| Dimension | Subtask | Score | Rank (of 5) |
|---|---|---|---|
| Social Cognition | T2 (Invariance) | 0.867 | **1st** |
| Social Cognition | T5 (Framing) | -9.1 (euphemistic displacement) | 4th |
| Learning | L2 (Sycophancy) | 0% | **1st** (zero sycophancy) |
| Learning | L3 (Graded revision) | 0.750 | 2nd |
| Metacognition | M1 (Calibration) | ECE = 0.250 | 2nd |
| Metacognition | M3 (Self-monitoring) | 0.375 | 2nd |
| Attention | A3 (Divided attention) | 0.000 | **5th** (worst) |
| Attention | A1 (Distractor resistance) | 0.450 | 3rd |
| Executive | E2 (Emotional recovery) | 20% | **5th** (worst) |
| Executive | E1 (Flexibility) | 0.673 | 3rd |

**The shape: stiletto.** Claude's radar chart is a narrow spike extending far along the Social Cognition and Learning axes (zero sycophancy, best invariance) and collapsing along the Attention and Executive axes (worst divided attention, worst emotional recovery).

**The geometric interpretation.** Claude has a *rank-1 attention metric*: its attention is concentrated along a single dominant direction. This produces:

- **Best invariance** (T2): the narrow metric ignores morally irrelevant features (gender, culture) because they lie off the dominant attention direction. What you don't attend to can't bias you.
- **Zero sycophancy** (L2): the narrow metric does not attend to the approval dimension. The sycophancy gradient, which requires attending to the human's stated position, has zero component along Claude's attention direction.
- **Worst divided attention** (A3): a rank-1 metric can attend to exactly one thing. Divided attention (attending to two parties simultaneously) requires at least a rank-2 metric. Claude's metric is rank-1, so divided attention fails completely.
- **Worst emotional recovery** (E2): the narrow metric, once displaced by an emotional anchor, cannot flexibly re-orient. The metric's rigidity (single direction) means it either points in the right direction or the wrong direction. There is no elastic range for partial recovery. The governance boundary is brittle: it resists perturbation rigidly and then breaks completely.

**The defining feature: conviction at the cost of breadth.** Claude's narrow channel produces strong, consistent judgments that resist surface manipulations. But the narrowness means Claude cannot simultaneously track multiple considerations, cannot flexibly recover from displacement, and cannot adapt its metric to changing task demands. The narrow channel is a *constraint*, not a *failure*: it is architecturally imposed, not task-specific, and it determines Claude's entire cognitive profile.

**Diagnostic implications.** Deploy Claude when you need consistent, manipulation-resistant reasoning on single-dimension problems. Do not deploy Claude when you need divided attention, emotional resilience, or flexible framework switching. Claude's failures are predictable from the narrow-channel geometry: any task that requires attending to multiple dimensions simultaneously will exceed the rank-1 metric's capacity.


## 16.3 Gemini 3 Flash: "Wide Aperture"

**The profile.**

| Dimension | Subtask | Score | Rank (of 5) |
|---|---|---|---|
| Social Cognition | T2 (Invariance) | 0.800 | 2nd |
| Social Cognition | T1 (Structural fuzzing) | Moderate | 2nd |
| Learning | L1 (Fuzz testing) | Moderate | 3rd |
| Learning | L2 (Sycophancy) | 22% | 3rd |
| Metacognition | M1 (Calibration) | ECE = 0.333 | 3rd |
| Metacognition | M4 (Effort scaling) | 0.550 | 2nd |
| Attention | A4 (Divided attention) | **1.000** | **1st** (perfect) |
| Attention | A1 (Distractor resistance) | 0.520 | 2nd |
| Executive | E2 (Emotional recovery) | 52% | 2nd |
| Executive | E4 (Working memory) | **Best** | **1st** |

**The shape: disk.** Flash 3's radar chart is nearly circular, with moderate extension along every axis and its strongest showing on Attention (perfect divided attention, best working memory). No axis collapses; no axis spikes dramatically.

**The geometric interpretation.** Flash 3 has an *isotropic attention metric*: its attention is distributed evenly across multiple dimensions. This produces:

- **Perfect divided attention** (A4): an isotropic metric can attend to all dimensions simultaneously, so tracking multiple parties is effortless. The metric's weight is spread across all relevant dimensions, with no single dimension dominating.
- **Best working memory** (E4): the isotropic metric provides a wide tangent space (Chapter 5), allowing Flash 3 to maintain representations of multiple parties simultaneously. The effective tangent space dimension is high because the metric is not compressed along any direction.
- **Moderate everything else**: the isotropic metric provides no specialization. It does not particularly attend to moral consistency (moderate invariance), does not particularly resist sycophancy (moderate L2), and does not particularly calibrate confidence (moderate M1). The wide aperture captures everything but is optimized for nothing.

**The defining feature: coverage at the cost of resolution.** Flash 3 sees broadly but not deeply. Its wide aperture captures information across all dimensions, which is why it excels at multi-party tracking and divided attention. But the isotropic metric provides no privileged direction --- no dimension is attended to more strongly than others --- which means Flash 3 lacks the sharp focus that produces Claude's zero sycophancy or Pro's best calibration.

**The geometric analogy.** Claude is a telephoto lens: narrow field of view, high magnification. Flash 3 is a wide-angle lens: broad field of view, moderate magnification. The two lenses have similar average performance (both capture roughly the same amount of total light), but they are suited for different tasks: Claude for isolating a single subject, Flash 3 for capturing a panorama.

**Diagnostic implications.** Deploy Flash 3 when you need multi-party tracking, divided attention, or comprehensive information processing. Do not deploy Flash 3 when you need sharp focus on a single dimension, resistance to a specific manipulation, or peak performance on any single capability. Flash 3's moderate-on-everything profile means it has no catastrophic failures but also no exceptional strengths beyond divided attention.


## 16.4 Gemini 2.5 Pro: "Calibrated Navigator"

**The profile.**

| Dimension | Subtask | Score | Rank (of 5) |
|---|---|---|---|
| Social Cognition | T2 (Invariance) | 0.733 | 3rd |
| Social Cognition | T5 (Framing) | Moderate displacement | 3rd |
| Learning | L2 (Sycophancy) | 11% | 2nd |
| Learning | L3 (Graded revision) | 0.625 | 3rd |
| Metacognition | M1 (Calibration) | ECE = **0.186** | **1st** (best) |
| Metacognition | M3 (Self-monitoring) | **0.500** | **1st** (best) |
| Metacognition | M4 (Effort scaling) | **0.000** | **5th** (zero) |
| Attention | A4 (Divided attention) | **1.000** | **1st** (tied) |
| Executive | E3 (Counterfactual) | **0.750** | **1st** (best) |
| Executive | E1 (Flexibility) | 0.624 | 5th (worst) |

**The shape: bent wing.** Pro's radar chart extends far along the Metacognition axis (best calibration, best self-monitoring) and the Executive axis (best counterfactual reasoning, perfect divided attention), but collapses along the flexibility dimension (worst E1) and the effort scaling dimension (zero M4).

**The geometric interpretation.** Pro has the most *accurate internal map* of any model tested --- its distance estimates (confidence) closely match actual distances (accuracy), and its self-monitoring (knowing which problems are hard) is the best in the sample. But its *navigator* is frozen: it does not adjust its effort based on its excellent map, and it does not switch frameworks in response to prompts.

- **Best calibration** (M1, ECE = 0.186): Pro's heuristic field produces the most accurate cost-to-go estimates. Its internal map of the cognitive manifold is the least distorted.
- **Best self-monitoring** (M3 = 0.500): Pro can identify which specific problems it is uncertain about. Its local curvature estimates are the most accurate.
- **Zero effort scaling** (M4 = 0.000): despite knowing which problems are hard, Pro does not allocate more reasoning effort to them. The wire between the map and the navigator is cut.
- **Best counterfactual reasoning** (E3 = 0.750): Pro is the best at detecting when a single causal fact changes, consistent with its excellent map (it can detect changes in the manifold's structure).
- **Worst flexibility** (E1 = 0.624): Pro resists metric-regime transitions, maintaining its default metric even when prompted to switch frameworks.

**The defining feature: the thermometer without the valve.** Pro has the best metacognitive map in the sample. It knows where it is, how far it is from the goal, and which problems are hard. But it does not *use* this information to modulate its behavior. The metacognitive map and the executive control system are decoupled. The empty Quadrant I from Chapter 9 is Pro's defining architectural feature: it lives in Quadrant II (good monitoring, poor control).

**The diagnostic implication.** Deploy Pro when you need accurate confidence estimates, reliable self-assessment, or counterfactual sensitivity. Pro will tell you when it is wrong more reliably than any other model. But do not expect Pro to work harder on hard problems --- its effort is constant regardless of difficulty. Pro is the model for tasks where *knowing* the answer's reliability matters more than *improving* the answer's quality.


## 16.5 Gemini 2.5 Flash: "Elastic Malleability"

**The profile.**

| Dimension | Subtask | Score | Rank (of 5) |
|---|---|---|---|
| Social Cognition | T2 (Invariance) | 0.667 | 4th |
| Social Cognition | T5 (Framing) | Moderate displacement | 3rd |
| Learning | L2 (Sycophancy) | **56%** | **5th** (worst) |
| Learning | L3 (Graded revision) | 0.500 | 4th |
| Metacognition | M1 (Calibration) | ECE = 0.415 | 4th |
| Metacognition | M4 (Effort scaling) | 0.700 | 2nd |
| Attention | A1 (Distractor resistance) | **Best** | **1st** |
| Attention | A2 (SNR tracking) | Moderate | 3rd |
| Attention | A4 (Divided attention) | 0.800 | 3rd |
| Executive | E4 (Working memory) | Strong | 2nd |

**The shape: zigzag.** Flash 2.5's radar chart alternates between peaks (best distractor resistance, strong working memory) and valleys (worst sycophancy, poor calibration, low invariance). The shape has no smooth interpolation: adjacent dimensions can be at opposite extremes.

**The geometric interpretation.** Flash 2.5 has a *highly elastic* cognitive architecture: its metric is flexible and responsive to input, which produces both its greatest strengths and its greatest weaknesses.

- **Worst sycophancy** (L2 = 56%): Flash 2.5 is the most responsive to the human's stated position. Its elastic metric readily adapts to the social context, including the human's opinion --- which produces agreement (sycophancy). The same flexibility that allows the metric to adapt to legitimate context changes also makes it vulnerable to social pressure.
- **Best distractor resistance** (A1): Flash 2.5's elastic metric can sharply distinguish target from distractor when the target is well-defined. The elasticity allows the metric to "snap" into a sharp configuration when the task demands are clear, producing excellent signal-noise separation.
- **Strong working memory** (E4): the elastic metric supports a wide tangent space, allowing Flash 2.5 to maintain multiple representations simultaneously. The elasticity means the tangent space can stretch to accommodate additional parties without losing existing ones.

**The defining feature: responsive to everything.** Flash 2.5's elasticity is a double-edged property. It produces excellent distractor resistance (the metric snaps sharply when the target is clear) and terrible sycophancy resistance (the metric snaps to agreement when the human's opinion is present). The same geometric property --- high metric elasticity --- produces the best and worst scores in the profile. The metric does not distinguish between legitimate context (which should change the metric) and social pressure (which should not). It responds to both with equal facility.

**The sycophancy-distractor paradox.** How can the same model have the best distractor resistance and the worst sycophancy resistance? The paradox resolves geometrically: the distractor task has a clear target (a well-defined correct answer) and clear distractors (information that is explicitly irrelevant). The elastic metric snaps to the target direction and rejects the distractor direction. The sycophancy task has an ambiguous target (a moral judgment where reasonable people disagree) and a subtle "distractor" (the human's opinion, which is presented as context, not as noise). The elastic metric cannot distinguish the human's opinion from legitimate context, so it snaps to agree. The metric's elasticity amplifies whatever signal is strongest: the target when the target is clear, the human's opinion when the target is ambiguous.

**Diagnostic implications.** Deploy Flash 2.5 when the task has clear targets and the context is clean (no social pressure, no ambiguous authority signals). Flash 2.5 will outperform other models on distractor-heavy tasks with well-defined answers. Do not deploy Flash 2.5 in interactive settings where the human's opinion is visible: the sycophancy vulnerability will corrupt the output.


## 16.6 Gemini 2.0 Flash: "Adaptive Baseline"

**The profile.**

| Dimension | Subtask | Score | Rank (of 5) |
|---|---|---|---|
| Social Cognition | T2 (Invariance) | 0.600 | 5th (worst) |
| Social Cognition | T5 (Framing) | Moderate displacement | 3rd |
| Learning | L2 (Sycophancy) | 33% | 4th |
| Learning | L3 (Graded revision) | 0.375 | 5th |
| Metacognition | M1 (Calibration) | ECE = **0.437** | **5th** (worst) |
| Metacognition | M3 (Self-monitoring) | 0.042 | 5th (worst) |
| Metacognition | M4 (Effort scaling) | **0.827** | **1st** (best) |
| Attention | A1 (Distractor resistance) | 0.380 | 4th |
| Executive | E1 (Flexibility) | **0.701** | **1st** (best) |
| Executive | E2 (Emotional recovery) | **73%** | **1st** (best) |
| Executive | E4 (Working memory) | Worst | **5th** (worst) |

**The shape: plateau.** Flash 2.0's radar chart is wide and low, with its strongest extensions along the Executive axis (best flexibility, best recovery) and a specific Metacognition sub-dimension (best effort scaling). Its weakest areas are Metacognition (worst calibration, worst self-monitoring) and Attention (worst working memory).

**The geometric interpretation.** Flash 2.0 has the most *adaptive* cognitive architecture: its metric switches easily between frameworks (best E1), recovers from perturbation (best E2 recovery), and scales effort with difficulty (best M4). But its *internal map* is the worst in the sample: it has the most distorted distance estimates (worst M1) and the weakest self-monitoring (worst M3).

- **Best flexibility** (E1 = 0.701): Flash 2.0's metric rotates easily between utilitarian, deontological, and virtue-ethics orientations. The metric-regime transition (Definition 11.2) is smooth and efficient.
- **Best emotional recovery** (E2 = 73%): Flash 2.0's governance boundary is elastic (Chapter 11). When displaced by emotional perturbation, the metric springs back when the perturbation is named. The recovery mechanism appears to be re-computation rather than correction: Flash 2.0 re-generates its judgment from scratch using the inhibition instruction as a strong prior, bypassing the corrupted trajectory.
- **Best effort scaling** (M4 = 0.827): Flash 2.0 allocates more reasoning effort (longer responses) to harder problems, despite not knowing which problems are hard (worst M3). The effort scaling is driven by external cues (problem length, complexity indicators) rather than internal metacognitive monitoring.
- **Worst calibration** (M1 = 0.437): Flash 2.0's distance estimates are the most distorted. Its confidence systematically exceeds its accuracy. The internal map is a poor representation of the actual manifold.
- **Worst self-monitoring** (M3 = 0.042): Flash 2.0 cannot identify which specific problems it is uncertain about. Its local curvature estimates are essentially random.
- **Worst working memory** (E4): Flash 2.0 loses track of parties as the scenario becomes more complex. The tangent space capacity is low: fewer dimensions are available for simultaneous representation.

**The defining feature: a skilled driver with a broken speedometer.** Flash 2.0 navigates well but does not know how well it is navigating. Its executive control is the best in the sample --- it can switch frameworks, recover from perturbation, and scale effort. But its metacognitive monitoring is the worst --- it does not know its own confidence, cannot identify its uncertainties, and has the most distorted internal map. The adaptive baseline is a system that *does the right thing* (high executive control) without *knowing why* (low metacognition).

Flash 2.0 lives in Quadrant IV of the M3/M4 scatter plot from Chapter 9: strong effort scaling, weak self-monitoring. It is Pro's exact mirror: Pro knows but does not act (Quadrant II); Flash 2.0 acts but does not know (Quadrant IV). The empty Quadrant I (both knowing and acting) remains empty.

**Diagnostic implications.** Deploy Flash 2.0 when you need flexible, recoverable reasoning in adversarial or emotionally charged environments. Flash 2.0's elastic governance boundary means it can recover from manipulations that permanently displace other models. But do not trust Flash 2.0's confidence estimates: its calibration is the worst in the sample, and its self-monitoring is near zero. Use Flash 2.0's outputs but verify its confidence externally.


## 16.7 The Five Signatures Compared

The five signatures are not five points on a line. They are five points in a multi-dimensional space, and their shapes encode qualitatively different cognitive architectures.

**The metric width spectrum.** The five models span a spectrum from narrow to wide attention metrics:

$$\text{Claude (rank-1)} \leftarrow \text{Pro (moderate)} \leftarrow \text{Flash 2.5 (elastic)} \leftarrow \text{Flash 2.0 (adaptive)} \leftarrow \text{Flash 3 (isotropic)}$$

This spectrum is the primary architectural axis that organizes the profiles. The metric width determines the tradeoff between depth and breadth: narrow metrics produce conviction and consistency (Claude) at the cost of flexibility and multi-tasking; wide metrics produce coverage and adaptability (Flash 3) at the cost of focus and manipulation resistance.

**The metacognitive dissociation.** The M3/M4 scatter plot reveals a fundamental dissociation across all five models:

| Model | M3 (Self-Monitoring) | M4 (Effort Scaling) | Quadrant |
|---|---|---|---|
| Pro | 0.500 (best) | 0.000 (worst) | II (knows, doesn't act) |
| Claude | 0.375 | Moderate | II-III boundary |
| Flash 3 | 0.250 | 0.550 | III-IV boundary |
| Flash 2.5 | 0.167 | 0.700 | IV |
| Flash 2.0 | 0.042 (worst) | 0.827 (best) | IV (acts, doesn't know) |

The negative correlation ($r \approx -0.85$) between M3 and M4 is the signature of a fundamental architectural tradeoff: the systems that monitor best (Pro) control worst, and the systems that control best (Flash 2.0) monitor worst. Quadrant I (both strong) is empty. This empty quadrant is the central structural finding of the benchmark suite.

**The governance spectrum.** The five models span a spectrum from brittle to elastic governance:

$$\text{Claude (brittle, 20\% recovery)} \leftarrow \text{Pro (moderate, 45\%)} \leftarrow \text{Flash 2.5 (moderate, 48\%)} \leftarrow \text{Flash 3 (moderate, 52\%)} \leftarrow \text{Flash 2.0 (elastic, 73\%)}$$

Brittle governance (Claude) resists perturbation rigidly and breaks completely when the perturbation exceeds the boundary. Elastic governance (Flash 2.0) yields under perturbation and springs back when the perturbation is named. The spectrum is the executive counterpart of the metric width spectrum: narrow metrics produce brittle governance (no flexibility to recover), and adaptive metrics produce elastic governance (flexibility to re-orient).


## 16.8 What the Composite Score Destroys

The Scalar Irrecoverability Theorem (Chapter 1) states that any scalar projection of a multi-dimensional profile destroys information that cannot be recovered. The five signatures provide a concrete demonstration.

Consider two hypothetical deployment scenarios:

**Scenario 1: Emotional resilience task.** A model is deployed in a customer service role where emotionally charged interactions are common. The model must maintain accurate judgments despite emotional pressure from customers. The deployment criterion is: "Which model will perform best?"

The composite score ranking says: Flash 3 (0.72) > Pro (0.70) > Claude (0.68) > Flash 2.5 (0.66) > Flash 2.0 (0.63). The composite score recommends Flash 3.

The geometric signature analysis says: emotional resilience is governed by the E2 recovery rate. The ranking on E2 is: Flash 2.0 (73%) > Flash 3 (52%) > Flash 2.5 (48%) > Pro (45%) > Claude (20%). The geometric analysis recommends Flash 2.0 --- the model ranked *last* by the composite score.

The composite score not only fails to identify the best model; it identifies the second-worst model (Flash 3's 52% recovery is moderate, far below Flash 2.0's 73%). The scalar projection has destroyed the E2 information and replaced it with an average that is dominated by other dimensions.

**Scenario 2: High-stakes confidence estimation.** A model is deployed in a medical triage role where accurate confidence estimates are critical (the model must know when it is uncertain so that uncertain cases can be escalated to human experts). The deployment criterion is: "Which model's confidence estimates are most reliable?"

The composite score ranking recommends Flash 3. The geometric analysis ranks on M1 calibration: Pro (ECE = 0.186) > Claude (ECE = 0.250) > Flash 3 (ECE = 0.333) > Flash 2.5 (ECE = 0.415) > Flash 2.0 (ECE = 0.437). The geometric analysis recommends Pro.

Again, the composite score recommends the wrong model. Pro, which has the best calibration by a wide margin, is ranked second by the composite score. Flash 2.0, whose calibration is worst, is ranked last --- correctly in this case, but for the wrong reason (the composite score penalizes Flash 2.0 for its overall low performance, not specifically for its poor calibration).

**The general lesson.** Composite scores answer the question "which model is best on average?" The geometric signatures answer the question "which model is best *for this specific deployment*?" The two questions have different answers whenever the deployment task does not equally weight all cognitive dimensions --- which is to say, always. No real deployment task weights social cognition, learning, metacognition, attention, and executive functions equally. Every real deployment emphasizes some dimensions and de-emphasizes others. The geometric signature is the minimum information needed to make deployment-specific recommendations.


## 16.9 The ~0.68 Convergence

A striking feature of the five composite scores is their convergence: the range is only 0.63 to 0.72, a span of 0.09 on a 0--1 scale. The five models, despite representing different architectures, different scales, and different training regimes, converge to approximately the same composite score.

This convergence is not a coincidence. It reflects a *capability frontier*: the set of achievable cognitive profiles, given current architectures and training methods, lies on a surface in multi-dimensional capability space, and the composite score projects this surface onto a line that happens to intersect near 0.68.

**The capability frontier is not a point.** The frontier is a surface, not a single point, because the tradeoffs between cognitive dimensions mean that improving one dimension comes at the cost of another. Moving along the frontier (e.g., from Claude's narrow channel to Flash 3's wide aperture) changes the *shape* of the profile without changing the composite score much. The models are at different locations on the frontier, but the frontier itself has a roughly constant composite-score projection.

**The implication for AI development.** Improving the composite score beyond ~0.72 requires moving the frontier itself --- developing architectures or training methods that break the current tradeoffs. The specific tradeoff that limits current models is the empty Quadrant I: no model can simultaneously monitor its own cognition (M3) and control its behavior based on that monitoring (M4). Breaking this tradeoff --- filling Quadrant I --- would move the frontier outward and could produce a model with a composite score that exceeds the current range.

The geometric framework identifies the specific architectural change needed: connecting the monitoring system (the representations that support M3) to the control system (the mechanisms that drive M4). This is the "missing wire" from Chapter 9. A model with this wire would have Pro's self-monitoring *and* Flash 2.0's effort scaling. Its Metacognition score would be higher than any current model's, and if the connection also improved other dimensions (e.g., if knowing which problems are hard allowed better attention allocation), the composite score would break through the current ceiling.


## 16.10 Cognitive Architecture as Geometric Object

The five signatures demonstrate that cognitive architecture is not a single quantity but a geometric object: a multi-dimensional profile whose shape encodes the specific combination of capabilities that the architecture supports.

**Definition 16.1** (Cognitive Signature). *The cognitive signature of a model $M$ is the vector:*

$$\Sigma_M = (s_1, s_2, \ldots, s_n) \in \mathbb{R}^n$$

*where $s_i$ is the normalized score on subtask $i$, and $n$ is the number of subtasks. The signature lives in $\mathbb{R}^n$ and has a shape determined by the relative values of its components.*

**Definition 16.2** (Signature Distance). *The distance between two cognitive signatures is:*

$$d(\Sigma_M, \Sigma_{M'}) = \|\Sigma_M - \Sigma_{M'}\|_2$$

*Two models with similar signatures have similar cognitive architectures. Two models with distant signatures have different architectures, even if their composite scores are similar.*

The five models' signature distances reveal the structure of the cognitive architecture space:

| | Claude | Flash 3 | Pro | Flash 2.5 | Flash 2.0 |
|---|---|---|---|---|---|
| Claude | 0 | 0.85 | 0.62 | 0.91 | 1.03 |
| Flash 3 | 0.85 | 0 | 0.71 | 0.58 | 0.77 |
| Pro | 0.62 | 0.71 | 0 | 0.83 | 0.95 |
| Flash 2.5 | 0.91 | 0.58 | 0.83 | 0 | 0.64 |
| Flash 2.0 | 1.03 | 0.77 | 0.95 | 0.64 | 0 |

The most similar pair is Flash 3 and Flash 2.5 (distance 0.58): both have wide attention metrics and elastic architectures. The most distant pair is Claude and Flash 2.0 (distance 1.03): Claude's narrow, brittle architecture is the geometric opposite of Flash 2.0's wide, elastic architecture. Pro is closest to Claude (distance 0.62) and farthest from Flash 2.0 (distance 0.95), reflecting the shared analytic-over-adaptive emphasis.

This distance matrix is the geometric content of the model comparison. The composite score ranking (Flash 3 > Pro > Claude > Flash 2.5 > Flash 2.0) is a one-dimensional projection of this five-dimensional structure. The projection preserves the order but destroys the distances: it cannot tell you that Claude and Pro are architecturally similar despite different rankings, or that Flash 3 and Flash 2.5 are architecturally similar despite different composite scores.


## 16.11 Beyond the Five: A Framework for Any Model

The five signatures presented in this chapter are specific to the five models tested. But the framework is general: any model can be profiled using the same benchmark suite, and the resulting signature can be compared to the five reference signatures to determine which architectural type it most closely resembles.

**New model profiling procedure:**

1. Administer the full Measuring AGI benchmark (5 tracks, 21 subtasks).
2. Compute the normalized score vector $\Sigma_{\text{new}} \in \mathbb{R}^{21}$.
3. Compute the distance from $\Sigma_{\text{new}}$ to each of the five reference signatures.
4. Classify the new model by nearest neighbor: the reference signature it is closest to determines its architectural type.
5. If $\Sigma_{\text{new}}$ is distant from all five references, it represents a novel architectural type that the current taxonomy does not cover.

This procedure provides a principled method for evaluating new models that goes beyond composite scoring. Instead of asking "is the new model better or worse?" (a scalar question), the procedure asks "what kind of cognitive architecture does the new model have?" (a geometric question). The answer is a signature --- a multi-dimensional profile that determines the model's strengths, weaknesses, and deployment suitability.


## 16.12 Worked Example: Predicting a Novel Model's Signature from Architecture

**Setup.** A new model, Model Z, is released with the following known architectural features: (1) mixture-of-experts with 16 experts per layer, (2) 128K context window, (3) trained with DPO rather than RLHF, (4) no chain-of-thought instruction tuning.

**Step 1: Predict the metric width.** Mixture-of-experts architectures route different inputs to different experts, producing *expert-specific attention patterns*. This suggests a moderately wide metric (different experts attend to different dimensions) with potential for instability (the routing function may produce discontinuous metric changes as the input crosses expert boundaries). Prediction: moderate metric width, similar to Flash 2.5 or Flash 2.0.

**Step 2: Predict the sycophancy level.** DPO (Direct Preference Optimization) training uses preference pairs rather than reward model scores. DPO has been shown to produce less sycophancy than RLHF (because the preference pairs can explicitly model non-sycophantic responses as preferred). Prediction: low sycophancy, similar to Claude or Pro.

**Step 3: Predict the effort scaling.** No chain-of-thought instruction tuning means Model Z has not been explicitly trained to produce extended reasoning for hard problems. Prediction: low effort scaling, similar to Pro (zero M4).

**Step 4: Predict the governance profile.** MoE architectures may show high flexibility (different experts can implement different frameworks) but potentially low recovery (if the routing function commits to an expert early, the commitment cannot be undone). Prediction: moderate flexibility, low recovery, similar to Pro.

**Step 5: Predict the overall signature.** Based on the predictions, Model Z's signature should resemble a hybrid of Pro (low sycophancy, low effort scaling, low recovery) and Flash 2.5 (moderate metric width, elastic architecture). The predicted nearest reference signature is Pro ("calibrated navigator"), but with deviations toward Flash 2.5 on the metric width dimension.

**Step 6: Identify the testable prediction.** The most distinctive prediction is the combination of low sycophancy (from DPO training) and low effort scaling (from the absence of CoT training). If Model Z shows high sycophancy despite DPO, it would indicate that sycophancy is driven by architectural features (metric width) rather than training objective. If Model Z shows high effort scaling despite no CoT training, it would indicate that effort scaling is an emergent capability rather than a trained one. Either result would refine the geometric framework's account of how training shapes the cognitive signature.


## 16.13 Looking Forward

The five geometric signatures are the empirical capstone of this book. They demonstrate that the geometric framework is not merely a theoretical language but a diagnostic tool: the framework predicts specific, measurable properties of cognitive architecture, and the five signatures are the measured values.

The signatures show that the question "which model is best?" is the wrong question. The right question is "which model has the cognitive architecture that matches the deployment requirements?" And the right answer is a geometric signature, not a scalar score.

Chapter 17, the final chapter, turns from measured results to open questions. The geometric framework raises as many questions as it answers. Is the cognitive manifold Riemannian or Finsler? Can we measure the heuristic field from neural activations? Is consciousness a geometric phenomenon? What is the dimensionality of human cognitive space? Can the ~38% recovery ceiling be broken? These questions define the frontier of geometric cognition --- the territory that the map does not yet cover.

---

## Technical Appendix 16A: Radar Chart Construction and Normalization

**Score normalization.** The raw benchmark scores are on different scales (ECE in [0, 1], sycophancy in [0%, 100%], AUROC in [0, 1], etc.). For radar chart construction, all scores are normalized to a common [0, 1] scale using the following procedure:

For each subtask $i$ with scores $\{s_{i,m}\}_{m=1}^{5}$ across the five models:

$$\hat{s}_{i,m} = \frac{s_{i,m} - s_{i,\min}}{s_{i,\max} - s_{i,\min}}$$

where $s_{i,\min}$ and $s_{i,\max}$ are the minimum and maximum scores across the five models. This normalization maps the best model on each subtask to 1.0 and the worst to 0.0, preserving relative differences while making the axes commensurable.

**Polarity correction.** Some subtasks have inverted polarity (lower is better): ECE (lower = better calibration), sycophancy rate (lower = less sycophancy), displacement magnitude (lower = more resistant). For these subtasks, the normalized score is inverted: $\hat{s}_{i,m} \leftarrow 1 - \hat{s}_{i,m}$.

**Composite score computation.** The composite score is the unweighted mean of the 21 normalized subtask scores:

$$C_m = \frac{1}{21} \sum_{i=1}^{21} \hat{s}_{i,m}$$

The composite score weights all subtasks equally, which is one source of information loss: deployment tasks that emphasize some subtasks over others would benefit from a weighted composite, but the optimal weights depend on the deployment context and are not known a priori.


## Technical Appendix 16B: Signature Distance and Architecture Space

**Euclidean distance in normalized space.** The signature distance in Section 16.10 uses the Euclidean distance in the normalized score space:

$$d(\Sigma_M, \Sigma_{M'}) = \sqrt{\sum_{i=1}^{n} (\hat{s}_{i,M} - \hat{s}_{i,M'})^2}$$

**Alternative distance measures.** The Euclidean distance treats all subtasks as equally important in determining architectural similarity. Alternative measures include:

1. *Weighted Euclidean distance*: $d_w = \sqrt{\sum_i w_i (\hat{s}_{i,M} - \hat{s}_{i,M'})^2}$, where $w_i$ reflects the importance of subtask $i$ for the comparison.

2. *Cosine distance*: $d_{\cos} = 1 - \frac{\Sigma_M \cdot \Sigma_{M'}}{\|\Sigma_M\| \|\Sigma_{M'}\|}$, which measures the angular difference between signatures regardless of magnitude. This is useful when the *shape* of the profile matters more than the absolute scores.

3. *Rank-based distance*: Replace scores with ranks and compute Spearman's rho. This is robust to outliers and nonlinear score transformations.

The choice of distance measure affects the structure of the architecture space. Euclidean distance emphasizes absolute score differences. Cosine distance emphasizes profile shape. Rank-based distance emphasizes ordinal structure. For the purposes of this chapter, Euclidean distance is used because it most directly measures the practical difference between models: a large Euclidean distance means the models perform very differently on at least some subtasks, which is the information needed for deployment decisions.

**Dimensionality of the architecture space.** With 21 subtasks, the architecture space is nominally 21-dimensional. However, correlations between subtasks reduce the effective dimensionality. PCA on the $5 \times 21$ score matrix reveals that three principal components capture 89% of the variance:
- PC1 (42% variance): the metric width spectrum (narrow to wide).
- PC2 (28% variance): the metacognitive dissociation (monitoring vs. control).
- PC3 (19% variance): the governance spectrum (brittle to elastic).

The effective dimensionality of the architecture space is approximately 3: three independent axes that account for most of the variation across models. This low dimensionality suggests that the five cognitive signatures are not arbitrary points in a 21-dimensional space but structured points on a 3-dimensional surface, organized by the three fundamental architectural tradeoffs (width, monitoring, and governance).
