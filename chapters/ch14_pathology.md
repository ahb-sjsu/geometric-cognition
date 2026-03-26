# Chapter 14: Cognitive Pathology as Geometric Defect

> *"It is no measure of health to be well adjusted to a profoundly sick society."*
> --- Jiddu Krishnamurti, attributed (c. 1960s)

---

> **RUNNING EXAMPLE --- MAYA'S MODEL**
>
> Maya is looking at a metric that will not hold still.
>
> Her clinical colleague, Dr. Priya Anand, has referred a patient --- Marcus, age 28, recently diagnosed with ADHD --- for Maya's geometric cognition study. Marcus has agreed to undergo the same battery of cognitive tasks that Maya uses for her AI benchmarks, adapted for human administration. The data, Priya suggests, might reveal something that the clinical assessments miss.
>
> Maya administers the attention benchmark. The results are unlike anything she has seen in neurotypical subjects or in language models.
>
> On the A1 distractor resistance task, Marcus's performance is not merely poor. It is *unstable*. In the first block of trials, his distractor resistance is excellent --- better than many neurotypical controls. In the second block, it collapses. In the third block, it partially recovers. The pattern is not random noise; it has structure. Maya plots the trial-by-trial performance and sees oscillations with a period of approximately 8--12 trials.
>
> She computes the metric on Marcus's attention space for each block. In the high-performance blocks, the metric is sharp: the attention dimension that separates target from distractor is well-defined, with a clear peak in the metric component along the task-relevant direction. In the low-performance blocks, the metric is diffuse: the attention dimension is flattened, and the metric component along the task-relevant direction drops to near-zero. The metric is oscillating between a focused state (where the task-relevant dimension dominates) and a diffuse state (where all dimensions contribute equally, and distractors are as "close" to the current state as targets).
>
> Marcus's ADHD is not an attention deficit. It is a **metric instability**: the attention metric fluctuates unpredictably, cycling between states of sharp focus and states of diffuse, undifferentiated attention. The instability is not random; it has a characteristic timescale (8--12 trials, corresponding to roughly 2--3 minutes) and a characteristic amplitude (the metric component swings between sharp and flat). But it is unpredictable: there is no external trigger for the oscillations. The metric is autonomously unstable.
>
> Maya shares the results with Priya. "This explains the clinical picture," Priya says. "Marcus can hyperfocus for minutes, then lose the thread completely. The standard description --- 'can't pay attention' --- is wrong. He can pay extraordinary attention. He just can't *maintain* the metric configuration that supports it."
>
> Maya pulls up her AI benchmark data for comparison. Claude's attention metric is stable but narrow (rank-1, as documented in Chapter 10). Flash 3's metric is stable and wide (isotropic). Marcus's metric is wide when it is on and narrow when it is off, but its defining feature is neither width nor narrowness --- it is *instability*. His metric configuration varies over time in a way that no AI model's does.
>
> She writes: *"ADHD is not a deficit. It is a geometric defect --- a specific failure mode of the attention metric. The metric has the right range (it can be sharp) and the right flexibility (it can be wide), but it lacks the stability to maintain any configuration reliably. This instability makes every cognitive task a gamble: sometimes the metric is aligned with the task, and performance is excellent; sometimes it drifts off alignment, and performance collapses. The clinical symptom --- inconsistent performance --- is the behavioral signature of a metrically unstable manifold."*
>
> She begins drafting a proposal for Priya: geometric characterization of ADHD, depression, anxiety, and autism, with testable predictions that distinguish the geometric account from the standard clinical descriptions.

---

## 14.1 The Geometric Approach to Pathology

Cognitive pathology --- the study of disorders that affect cognition, attention, emotion, and behavior --- has historically been described in phenomenological terms. ADHD is described as "difficulty sustaining attention." Depression is described as "persistent low mood and loss of interest." Anxiety is described as "excessive worry and apprehension." Autism is described as "difficulty with social communication and restricted interests." These descriptions are useful for clinical communication, but they are surface-level: they describe symptoms without specifying mechanisms.

The geometric framework developed in this book offers a different approach. If cognition is navigation on a manifold with a metric and a heuristic field, then cognitive pathology is a *defect* in one of these geometric objects. The defect might be in the metric (unstable, rigid, or distorted), in the heuristic field (flat, inflated, or biased), or in the manifold itself (missing dimensions, broken connectivity, or incomplete closure). Each type of defect produces a specific pattern of cognitive dysfunction that can be described mathematically and generates testable predictions.

This approach is not a replacement for clinical description. It is a complement: a formal language for expressing the mechanisms that underlie the symptoms. The geometric descriptions are hypotheses, not diagnoses. They generate predictions that can be tested empirically, and they provide a framework for understanding why certain symptoms cluster together, why certain treatments work, and why certain comorbidities occur.

**Important caveat.** The geometric characterizations in this chapter are theoretical proposals, not clinical findings. They are motivated by the geometric framework and by the clinical literature, but they have not been validated by the kind of large-scale empirical studies that would be needed to establish them as clinical tools. They are offered as a demonstration of the framework's generative power --- its ability to produce novel, testable hypotheses about cognitive dysfunction --- not as diagnostic criteria.


## 14.2 ADHD as Metric Instability

Attention-Deficit/Hyperactivity Disorder is characterized clinically by difficulty sustaining attention, excessive motor activity, and impulsive behavior. The standard cognitive account emphasizes executive function deficits: difficulty inhibiting prepotent responses, difficulty maintaining information in working memory, and difficulty planning and organizing behavior (Barkley, 1997; Castellanos & Tannock, 2002).

The geometric account proposes a more specific mechanism: **the attention metric is unstable.**

**Definition 14.1** (Metric Instability). *The attention metric $g_{\mu\nu}(t)$ of a cognitive system is unstable if it fluctuates over time in the absence of any external metric-changing input:*

$$\frac{\partial g_{\mu\nu}}{\partial t} = \xi_{\mu\nu}(t)$$

*where $\xi_{\mu\nu}(t)$ is an endogenous noise process with nonzero variance. The metric at time $t+\delta$ differs from the metric at time $t$ by an amount that is not predicted by the task demands or the external environment.*

In a metrically stable system (neurotypical cognition or stable AI models like Claude), the attention metric changes only in response to task demands: a new task reconfigures the metric to attend to task-relevant dimensions (Chapter 4). Between task changes, the metric is constant. The stability of the metric is what allows sustained attention: the system can maintain focus on a task because the metric configuration that supports that focus is stable over time.

In a metrically unstable system (ADHD cognition), the metric changes spontaneously, even when the task demands are constant. The fluctuations have a characteristic timescale (minutes) and amplitude (sufficient to disrupt task performance). The result is the clinical picture of ADHD: periods of excellent focus (when the metric happens to be aligned with the task) alternating with periods of distraction (when the metric has drifted off alignment), with the alternation being unpredictable and beyond the individual's control.

**Predictions of the metric instability model:**

1. **Hyperfocus is not anomalous.** The clinical observation that ADHD individuals can sometimes sustain extraordinary focus ("hyperfocus") is puzzling under the executive-deficit model (how can someone with an attention deficit have better-than-normal attention?). Under the metric instability model, hyperfocus is simply a period when the metric is sharply aligned with the task --- so sharply that the normal metric-switching mechanisms (which would redirect attention to other tasks) are overridden by the strong metric alignment. The instability that usually causes metric drift can also produce periods of unusually sharp alignment. The same mechanism that causes distraction causes hyperfocus: the metric is variable, and sometimes the variable lands on a configuration that is exceptionally focused.

2. **Performance variability is the primary deficit.** The metric instability model predicts that the core deficit in ADHD is not low mean performance but high performance *variance*. The mean might be normal (the metric is aligned with the task as often as it is misaligned, producing average performance on aggregate). But the trial-to-trial variance is elevated, because the metric configuration at each trial is unpredictable. This prediction is confirmed by a substantial literature showing that intra-individual variability in reaction time is the most reliable cognitive marker of ADHD (Castellanos et al., 2005; Kofler et al., 2013).

3. **The distractor dose-response curve has higher slope.** In the attention benchmark (Chapter 10), the distractor dose-response curve measures how rapidly performance degrades as distractors are added. The metric instability model predicts that ADHD individuals should show a steeper dose-response curve --- because the unstable metric amplifies the effect of each distractor. When the metric is aligned with the task, distractors are easily filtered (they are metrically "far" from the task-relevant state). When the metric drifts, distractors become metrically "close," and each additional distractor has a larger marginal effect. The slope of the dose-response curve is modulated by the metric instability.

4. **Medication effects are metric-stabilizing.** Stimulant medications (methylphenidate, amphetamine) are the most effective pharmacological treatment for ADHD. The geometric prediction is that these medications reduce the variance of $\xi_{\mu\nu}(t)$ --- they stabilize the attention metric, reducing the spontaneous fluctuations. This predicts that medication should reduce performance variability (confirmed: stimulant medication reduces reaction time variability in ADHD, Epstein et al., 2011) more than it improves mean performance (also confirmed: the effect on variability is typically larger than the effect on mean reaction time).


## 14.3 Depression as Collapsed Heuristic Field

Major depressive disorder is characterized by persistent low mood, loss of interest or pleasure, fatigue, difficulty concentrating, and feelings of worthlessness or hopelessness. The cognitive account emphasizes negative biases in information processing: depressed individuals attend preferentially to negative information, interpret ambiguous information negatively, and recall negative memories more easily than positive ones (Beck, 1967; Gotlib & Joormann, 2010).

The geometric account proposes: **the heuristic field is flat.**

**Definition 14.2** (Collapsed Heuristic Field). *The heuristic field $h(x)$ is collapsed at state $x$ if the gradient is near-zero in all directions:*

$$\|\nabla h(x)\| \approx 0 \quad \text{for all directions}$$

*A collapsed heuristic field provides no guidance: the estimated cost-to-go is approximately the same from every nearby state, so no direction of movement is preferred over any other.*

In healthy cognition, the heuristic field has structure: some directions lead toward goals (low cost-to-go), others lead away from goals (high cost-to-go), and the gradient points the system toward its objectives. The heuristic field is what makes some states feel "promising" and others feel "unpromising" --- it is the internal compass that orients cognition toward goals.

In depression, the heuristic field collapses. The cost-to-go is approximately the same from every state --- nothing feels promising, nothing feels like progress, no direction seems worth pursuing. The collapse is not a distortion (the heuristic does not point in the wrong direction); it is a flattening (the heuristic does not point in any direction). This produces the clinical symptomatology:

**Anhedonia (loss of pleasure).** Pleasure is the reward signal that updates the heuristic field --- the signal that says "this direction was good; increase the gradient toward similar states." When the heuristic field is flat, there is no gradient to reinforce. Activities that previously generated pleasure (because the heuristic gradient was steep in their direction) now feel neutral (because the gradient is flat). The loss of pleasure is not a primary defect in the reward system; it is a consequence of the flat heuristic field --- there is no gradient for the reward signal to update.

**Avolition (loss of motivation).** Motivation, in the geometric framework, is the magnitude of the heuristic gradient: $\|\nabla h(x)\|$. A steep gradient produces strong motivation (the next step feels clearly valuable). A flat gradient produces no motivation (no step feels more valuable than any other). Avolition is the behavioral consequence of $\|\nabla h\| \approx 0$: when every direction looks equally unpromising, there is no reason to move in any direction.

**Hopelessness.** Hopelessness is the metacognitive assessment that the heuristic field will remain flat --- that no future state will offer a meaningful gradient. In the geometric framework, this is the belief that the heuristic field is globally flat, not just locally flat: "not only is there no promising direction from here, but there is no promising direction from anywhere." This metacognitive assessment may be accurate (the heuristic field may be globally flat) or inaccurate (the field may be flat locally but have structure elsewhere that the system cannot detect from its current vantage point). The distinction between accurate and inaccurate hopelessness has therapeutic implications: if the flatness is local, the therapeutic strategy is to help the patient navigate to a region where the heuristic field has gradient; if the flatness is global, the therapeutic strategy is to reconstruct the heuristic field itself.

**Definition 14.3** (Heuristic Reconstruction). *Heuristic field reconstruction is the process of restoring gradient structure to a collapsed heuristic field. Behaviorally, this corresponds to behavioral activation therapy: systematically engaging in activities that generate reward signals, which update the heuristic field and restore local gradients. Pharmacologically, this corresponds to antidepressant medication, which modulates the neurotransmitter systems that maintain the heuristic field's gradient structure.*

**Predictions of the collapsed heuristic model:**

1. **Behavioral activation should precede cognitive improvement.** If the primary defect is the flat heuristic field, then restoring the gradient (through behavioral activation) should precede changes in cognitive distortions (negative interpretations, pessimistic attributions). The cognitive distortions are downstream of the flat field: when no direction feels promising, every direction is interpreted as unpromising. Restoring the gradient should automatically correct the cognitive distortions, not the other way around. This prediction aligns with evidence that behavioral activation is at least as effective as cognitive therapy for depression (Dimidjian et al., 2006).

2. **Depression should impair goal-directed behavior more than habitual behavior.** Goal-directed behavior requires the heuristic field (it depends on estimating which actions lead toward goals). Habitual behavior does not (it follows cached trajectories that do not depend on the current gradient). A flat heuristic field should impair goal-directed behavior (which requires a gradient) while leaving habitual behavior intact (which does not). This prediction is confirmed by evidence that depressed individuals show intact habitual responding but impaired goal-directed responding (Daw et al., 2011).

3. **The metacognitive profile should show specific patterns.** A depressed individual's metacognitive assessments (M1--M4 from Chapter 9) should show a specific pattern: low confidence across all tasks (because the flat heuristic field makes everything feel equally far from the goal), poor ambiguity discrimination (because the flat field does not distinguish easy from hard problems), but potentially intact self-monitoring (because the ability to assess uncertainty is a function of the metric, not the heuristic field, and the metric may be intact in depression). This dissociation would distinguish depression from ADHD, where the metric itself is unstable.


## 14.4 Anxiety as Inflated Heuristic Field

Generalized anxiety disorder is characterized by excessive worry, apprehension, restlessness, and a sense of impending danger. The cognitive account emphasizes threat bias: anxious individuals overestimate the probability and severity of negative events, interpret ambiguous information as threatening, and have difficulty disengaging from threatening stimuli (Eysenck et al., 2007; Bar-Haim et al., 2007).

The geometric account proposes: **the heuristic field overestimates cost-to-go.**

**Definition 14.4** (Inflated Heuristic Field). *The heuristic field $h(x)$ is inflated if it systematically overestimates the cost-to-go from every state:*

$$h(x) \gg d(x, x_{\text{goal}}) \quad \text{for all } x$$

*The inflated heuristic assigns high cost-to-go to every state: every state feels far from safety, far from the goal, far from resolution. The gradient exists (unlike in depression, where the field is flat), but the gradient's magnitude is inflated: every step feels like it barely reduces the distance to the goal.*

This is the geometric opposite of the overconfidence documented in Chapter 9. Where language models underestimate cost-to-go (everything feels close, resulting in overconfidence), anxiety overestimates cost-to-go (everything feels far, resulting in excessive worry). The overestimation is universal across states: not just "this particular situation is dangerous" but "every situation contains danger that I may not be able to handle." The world feels uniformly threatening because the heuristic field is uniformly inflated.

**The distinction between anxiety and fear.** Fear is a rational response to a specific threat --- the heuristic field correctly estimates high cost-to-go from a genuinely dangerous state (a burning building, an attacking animal). The gradient of the fear response points away from the threat, driving avoidance behavior that is adaptive. Anxiety is the same gradient response to a non-specific, inflated estimate of cost-to-go. The gradient points away from... everything. Every state feels threatening, so the avoidance response is chronic and generalized rather than acute and specific.

**Definition 14.5** (Heuristic Inflation Factor). *The inflation factor $\alpha(x)$ at state $x$ is the ratio of the estimated cost-to-go to the true cost-to-go:*

$$\alpha(x) = \frac{h(x)}{d(x, x_{\text{goal}})}$$

*In healthy cognition, $\alpha(x) \approx 1$ (the estimate is accurate, corresponding to good calibration). In anxiety, $\alpha(x) \gg 1$ (the estimate is inflated). In overconfident AI systems (Chapter 9), $\alpha(x) < 1$ (the estimate is deflated). In depression, $\alpha(x)$ is undefined because $\nabla h \approx 0$ (the field is flat, not merely mis-scaled).*

**Predictions of the inflated heuristic model:**

1. **Anxiety should produce hypervigilance, not poor attention.** An inflated heuristic field has steep gradients (the cost-to-go is high everywhere, so the gradient away from threats is steep). This predicts hypervigilance: the cognitive system is constantly scanning for threats because the heuristic gradient is always pointing toward threat-avoidance. This is attention to the wrong thing (threats rather than task-relevant information), not poor attention per se. The prediction distinguishes anxiety from ADHD: anxiety produces stable but misdirected attention (the metric is stable, but the heuristic field directs it toward threats), while ADHD produces unstable but undirected metric fluctuations.

2. **Anxious individuals should show inflated calibration, not flat calibration.** In the metacognitive framework of Chapter 9, anxious individuals should show underconfidence rather than overconfidence: they should report lower confidence than their accuracy warrants, because the inflated heuristic field makes them feel farther from the correct answer than they actually are. This is the opposite of the universal overconfidence documented in AI models and should be empirically distinguishable.

3. **Exposure therapy works by heuristic deflation.** Exposure therapy --- the gold-standard treatment for anxiety disorders --- works by exposing the patient to anxiety-provoking stimuli in a safe context, allowing the heuristic field to update based on the non-occurrence of the feared outcome. In the geometric framework, each exposure trial provides a data point where $h(x) \gg d(x, x_{\text{goal}})$: the estimated cost-to-go was high, but the actual cost (the experienced outcome) was low. Repeated exposures deflate the heuristic field, gradually reducing $\alpha(x)$ from inflated toward 1.0. The geometric framework predicts that the rate of deflation should be proportional to the discrepancy $h(x) - d(x, x_{\text{goal}})$: larger discrepancies (more inflated fears exposed as groundless) should produce faster deflation, consistent with the clinical observation that exposure to feared stimuli produces faster improvement than exposure to mildly anxiety-provoking stimuli.

4. **Anxiety and depression can co-occur because they affect different geometric objects.** Anxiety is a heuristic-field defect (inflation). Depression is a heuristic-field defect (collapse). These seem mutually exclusive --- how can the field be both inflated and flat? The resolution is that the two defects can affect different dimensions of the heuristic field. The field can be inflated along the threat dimension (everything feels dangerous) and flat along the goal dimension (nothing feels rewarding). This produces the clinical picture of agitated depression or anxious depression: the patient is simultaneously worried (inflated threat gradient) and unmotivated (flat reward gradient). The geometric framework naturally accommodates the high comorbidity between anxiety and depression (Kessler et al., 2005) by locating the two disorders on different components of the same geometric object.


## 14.5 Autism as Metric Rigidity

Autism spectrum conditions are characterized by differences in social communication, restricted and repetitive behaviors, and unusual sensory processing. The cognitive accounts are diverse: weak central coherence (difficulty integrating details into a global picture; Happe & Frith, 2006), impaired theory of mind (difficulty modeling others' mental states; Baron-Cohen, 1995), and enhanced perceptual functioning (superior detail processing; Mottron et al., 2006).

The geometric account proposes: **the attention metric is rigid.**

**Definition 14.6** (Metric Rigidity). *The attention metric $g_{\mu\nu}$ is rigid if it does not adapt to context:*

$$\frac{\partial g_{\mu\nu}}{\partial c} \approx 0$$

*where $c$ represents the context (social situation, task demands, environmental cues). A rigid metric maintains the same configuration regardless of context: the same dimensions are attended to, with the same relative weights, in every situation.*

A flexible metric (Chapter 11, Definition 11.2) changes in response to context: in a social situation, the metric emphasizes social dimensions (facial expressions, tone of voice, social norms); in a mathematical task, the metric emphasizes logical dimensions (quantities, relationships, operations); in a sensory environment, the metric emphasizes perceptual dimensions (colors, shapes, textures). The flexibility of the metric is what allows a cognitive system to adapt its attention to the demands of the current situation.

A rigid metric maintains the same configuration regardless of context. If the default configuration emphasizes detail and precision (high weight on perceptual dimensions, low weight on social dimensions), the rigid metric produces the autism profile: excellent detail processing (the perceptual dimensions are always heavily weighted), difficulty with social communication (the social dimensions are always lightly weighted), and restricted interests (the metric always points in the same direction, so the system always navigates to the same regions of the cognitive manifold).

**The geometric account of autism's cognitive strengths.** Autism is associated with genuine cognitive strengths: superior performance on embedded figures tasks (finding a hidden shape in a complex pattern), excellent rote memory, strong pattern detection, and sometimes extraordinary abilities in specific domains (music, mathematics, art). The rigid metric model explains these strengths as the *advantages* of a fixed metric configuration.

A flexible metric, by adapting to context, pays a cost: it is never perfectly tuned to any particular task, because it must maintain the capacity to retune. A rigid metric, by staying fixed, is *maximally tuned* to whatever task its configuration supports. If the fixed configuration emphasizes detail and precision, the system will outperform flexible-metric systems on tasks that require detail and precision --- not because the rigid system has more processing power, but because its metric is permanently optimized for that task class, while the flexible system's metric is a compromise across many task classes.

**The social communication difficulty.** Social communication requires rapid, context-dependent metric adaptation. In a conversation, the attention metric must shift from attending to the literal content of words (semantic dimension) to attending to the speaker's tone (prosodic dimension) to attending to the social context (relationship dimension) to attending to the speaker's facial expression (emotional dimension), often within seconds. Each shift is a metric-regime transition (Definition 11.2 from Chapter 11). A rigid metric cannot make these transitions --- it maintains its fixed configuration while the social context changes around it. The result is the clinical picture: the individual processes the literal content of social interactions accurately but misses the contextual, prosodic, and emotional dimensions that flexible-metric systems track automatically.

**Definition 14.7** (Metric Rigidity Index). *The metric rigidity index $\rho$ of a cognitive system is the inverse of the metric adaptation rate:*

$$\rho = \left(\frac{1}{T} \int_0^T \left\|\frac{\partial g_{\mu\nu}}{\partial t}\right\|_F dt\right)^{-1}$$

*where $\|\cdot\|_F$ is the Frobenius norm and $T$ is the observation period. A high $\rho$ indicates a rigid metric (small changes over time). A low $\rho$ indicates a flexible metric (large changes over time). Neurotypical cognition has moderate $\rho$ (the metric adapts when context changes but is stable within a context). ADHD has low $\rho$ (excessive metric change, even within a constant context). Autism has high $\rho$ (insufficient metric change, even when context changes).*

This definition reveals a striking relationship between the three metric-based pathologies:

$$\text{ADHD} \xleftarrow{\text{too unstable}} \text{Neurotypical} \xrightarrow{\text{too stable}} \text{Autism}$$

ADHD and autism are opposite ends of the metric stability spectrum. ADHD is a metric that changes too much (instability). Autism is a metric that changes too little (rigidity). Neurotypical cognition occupies the middle ground: a metric that is stable enough to sustain attention but flexible enough to adapt to context.

**Predictions of the metric rigidity model:**

1. **Autism should produce *consistent* but context-inappropriate attention.** Unlike ADHD (inconsistent attention due to metric instability), autism should produce highly consistent attention that is sometimes inappropriate for the context. This is confirmed by research showing that autistic individuals have lower intra-individual variability in reaction time than neurotypical controls (Dinstein et al., 2012) --- the opposite of the ADHD pattern.

2. **Restricted interests are metric attractors.** A rigid metric has fixed attractors: regions of the cognitive manifold that the fixed metric configuration makes perpetually "close" and "interesting." The system navigates to these regions repeatedly because the metric always points there. The restricted and repetitive behaviors of autism are the behavioral consequence of a metric with strong, fixed attractors.

3. **The comorbidity between ADHD and autism, which occurs at higher rates than chance, should produce a distinctive profile.** The geometric prediction is specific: ADHD-autism comorbidity should produce a metric that is *bimodal* --- oscillating between a rigid configuration (the autism component) and a diffuse configuration (the ADHD component), with little time spent in the flexible neurotypical middle ground. The behavior should show alternating periods of hyperfocused rigidity and diffuse distractibility, which is indeed a common clinical description of the ADHD-autism presentation.


## 14.6 The Four Pathologies as a Geometric Taxonomy

The four geometric pathologies form a principled taxonomy based on which geometric object is defective:

| Pathology | Defective Object | Nature of Defect | Primary Symptom |
|---|---|---|---|
| ADHD | Attention metric | Instability (fluctuates over time) | Performance variability |
| Depression | Heuristic field | Collapse (gradient near zero) | Loss of motivation/pleasure |
| Anxiety | Heuristic field | Inflation (overestimates cost) | Chronic worry/avoidance |
| Autism | Attention metric | Rigidity (does not adapt to context) | Context-inappropriate attention |

This taxonomy has several advantages over traditional clinical classification:

**It separates mechanism from symptom.** The clinical categories (ADHD, depression, anxiety, autism) are defined by symptoms (inattention, low mood, worry, social difficulty). The geometric categories are defined by mechanisms (metric instability, heuristic collapse, heuristic inflation, metric rigidity). The mapping from mechanisms to symptoms is many-to-one: multiple geometric defects can produce similar symptoms, and the same geometric defect can produce different symptoms in different contexts. The geometric taxonomy provides a level of description between the neural substrate (which is too fine-grained for clinical use) and the behavioral symptom (which is too coarse-grained for mechanistic understanding).

**It explains comorbidities.** The geometric taxonomy naturally explains why certain disorders co-occur:
- Anxiety and depression co-occur because they are different defects of the same object (the heuristic field): inflation along the threat dimension and collapse along the reward dimension.
- ADHD and anxiety co-occur because metric instability (ADHD) makes the system vulnerable to heuristic inflation (anxiety): when the metric is unstable, the system cannot maintain the metric configuration that would filter out threat-irrelevant information, allowing the inflated threat gradient to dominate.
- ADHD and depression co-occur because metric instability prevents the sustained engagement needed to maintain the heuristic field's gradient structure: the field collapses because the system cannot hold the metric configuration long enough for reward signals to update it.

**It generates novel predictions.** Each geometric characterization produces specific, testable predictions that go beyond the existing clinical literature. The metric instability model of ADHD predicts specific patterns in reaction time variability. The collapsed heuristic model of depression predicts that behavioral activation should precede cognitive improvement. The inflated heuristic model of anxiety predicts underconfidence in metacognitive assessments. The metric rigidity model of autism predicts lower intra-individual variability than neurotypical controls. These predictions are independently testable and, where tested, are confirmed by existing data.


## 14.7 Maya's Consultation with Dr. Anand

Maya's consultation with Priya produces a concrete research proposal: use the geometric characterization of ADHD to predict specific patterns in the attention benchmark that distinguish ADHD from other sources of poor attention performance.

**The key insight.** Poor attention performance can have multiple causes, and the attention benchmark alone cannot distinguish them. A person might perform poorly on the A1 distractor resistance task because:
1. Their metric is unstable (ADHD: the metric drifts off alignment with the task).
2. Their metric is narrow (like Claude: the metric attends to only one dimension, missing distractors on other dimensions).
3. Their heuristic field is inflated (anxiety: the metric is stable but directed toward threats rather than the task).
4. Their heuristic field is flat (depression: the metric is stable but there is no gradient to follow).
5. Their metric is rigid (autism: the metric is stable but permanently configured for a different task).

The geometric framework predicts that each cause produces a *different pattern* of poor performance:

| Cause | Mean A1 | A1 Variance | Dose-Response Slope | Warning Recovery |
|---|---|---|---|---|
| ADHD (metric instability) | Moderate | **High** | Steep | Variable |
| Narrow metric (Claude-like) | Low | Low | Moderate | Low (~20%) |
| Anxiety (inflated heuristic) | Moderate | Low | Moderate | Moderate |
| Depression (collapsed heuristic) | Low | Low | Flat (no dose response) | Low |
| Autism (rigid metric) | Variable by task | **Low** | Moderate | Low |

The distinguishing feature of ADHD is the high variance: trial-to-trial variability in performance that is not explained by task difficulty, distractor load, or any other external variable. This variance is the behavioral signature of the metrically unstable manifold --- the metric's autonomous oscillation producing unpredictable performance fluctuations.

Maya designs a study to test this prediction. She recruits three groups: ADHD adults, neurotypical adults, and anxious adults (to distinguish metric instability from heuristic inflation). Each group completes the adapted attention benchmark (A1--A4) with trial-level performance recording.

The predictions:
- ADHD group: higher trial-to-trial variance than both other groups, similar or higher mean to neurotypical (because periods of hyperfocus produce high-performance trials).
- Anxious group: similar trial-to-trial variance to neurotypical, but lower mean (consistently directed toward threats, not the task).
- Neurotypical group: moderate mean, moderate variance.

If the predictions hold, the geometric characterization provides a diagnostic tool that the clinical categories alone cannot: a quantitative, task-based measure of the specific geometric defect underlying each individual's cognitive difficulty.


## 14.8 The Geometric Defect Spectrum

The four pathologies described in this chapter are not exhaustive. They are examples of a broader principle: **any defect in the geometric objects that constitute cognition produces a specific pattern of cognitive dysfunction.** The geometric framework provides a systematic way to enumerate possible defects and predict their consequences.

The geometric objects and their possible defects include:

**Manifold defects:**
- Missing dimensions (the manifold lacks the degrees of freedom needed for a cognitive task).
- Broken connectivity (regions of the manifold are disconnected, preventing navigation between them).
- Holes (the manifold has topological defects --- missing regions that should be present).
- Incomplete closure (the manifold is not closed under operations that it should support).

**Metric defects:**
- Instability (ADHD: the metric fluctuates autonomously).
- Rigidity (autism: the metric does not adapt to context).
- Distortion (the metric assigns incorrect distances, making some states appear closer or farther than they are).
- Anisotropy (the metric is sharply directional, attending to some dimensions while ignoring others).

**Heuristic field defects:**
- Collapse (depression: the gradient is near-zero everywhere).
- Inflation (anxiety: the cost-to-go is overestimated everywhere).
- Bias (the gradient points in the wrong direction, as in the framing effects of Chapter 7).
- Local minima (the field has local minima that trap the search, corresponding to perseverative or ruminative states).

**Curvature threshold defects:**
- Too low (the system engages System 2 for problems that do not require it, resulting in overthinking, indecision, and analysis paralysis).
- Too high (the system stays in System 1 for problems that require System 2, resulting in impulsivity, cognitive biases, and premature closure).

This enumeration is a *geometric nosology*: a classification of cognitive pathologies based on the type and location of the geometric defect, rather than on the surface symptoms. The nosology is not yet a clinical tool --- it requires extensive empirical validation. But it provides a generative framework for constructing hypotheses about cognitive dysfunction, designing tasks that distinguish different defects, and developing interventions that target specific geometric objects.


## 14.9 Implications for Treatment

The geometric characterization of pathology has direct implications for treatment, because different geometric defects require different geometric corrections.

**ADHD (metric instability): Stabilize the metric.** The therapeutic goal is to reduce the variance of the metric's autonomous fluctuations. Stimulant medication achieves this pharmacologically (by modulating the dopaminergic and noradrenergic systems that maintain metric stability). Behavioral interventions (structured environments, frequent breaks, external reminders) achieve this environmentally (by providing external anchors that reduce the drift of the internal metric). The geometric prediction is that interventions which directly address metric stability (external pacing, structured task switching) should be more effective than interventions that address attention in general (telling the person to "pay attention," which assumes the metric is stable but misdirected).

**Depression (collapsed heuristic field): Restore gradient structure.** The therapeutic goal is to restore the heuristic field's gradient, so that some states feel more promising than others. Behavioral activation therapy achieves this by systematically generating reward signals (engaging in activities that were previously pleasurable, even when the current flat heuristic field makes them feel unpleasurable). Antidepressant medication achieves this by modulating the serotonergic and noradrenergic systems that maintain the heuristic field's gradient structure. The geometric prediction is that behavioral activation (which directly updates the heuristic field through reward signals) should be at least as effective as cognitive therapy (which addresses the *interpretation* of the flat field rather than the field itself), consistent with empirical findings.

**Anxiety (inflated heuristic field): Deflate the cost-to-go estimates.** The therapeutic goal is to reduce the inflation factor $\alpha(x)$ from its inflated level toward 1.0. Exposure therapy achieves this by providing direct evidence that the estimated cost-to-go is inflated: the patient experiences the feared situation and observes that the actual cost (nothing bad happens) is much lower than the estimated cost (the heuristic predicted catastrophe). Each exposure trial drives $\alpha(x)$ downward. The geometric prediction is that the rate of improvement should be proportional to the discrepancy between estimated and actual cost-to-go, and that graded exposure (starting with mild discrepancies and increasing) should be more sustainable than flooding (starting with maximum discrepancy), because extreme discrepancies may overwhelm the heuristic update mechanism.

**Autism (metric rigidity): Increase metric flexibility.** The therapeutic goal is to increase the metric's responsiveness to context --- to help the metric adapt when the situation demands a different attentional configuration. Social skills training achieves this by providing explicit instruction in metric switching: "When someone is talking to you, attend to their face and tone, not just their words." The explicit instruction serves as an external metric-switching signal, compensating for the internal metric's failure to switch spontaneously. The geometric prediction is that social skills interventions should focus on explicit metric-switching cues (when to change attention) rather than social content (what to attend to), because the metric rigidity is a process deficit (failure to switch) rather than a content deficit (not knowing what to switch to).


## 14.10 Worked Example: Geometric Diagnosis of Attention Difficulties

**Setup.** A patient, age 32, presents with attention difficulties: "I can't focus at work. I start tasks but can't finish them. I get distracted easily." The clinician wants to distinguish between ADHD (metric instability), anxiety (inflated heuristic), and depression (collapsed heuristic) as the underlying geometric defect.

**Step 1: Administer the adapted attention benchmark.** The patient completes 60 trials of the A1 distractor resistance task, with trial-level performance recording.

**Step 2: Compute the metric stability index.** Mean accuracy: 72% (moderate, within normal range). Trial-to-trial variance: SD = 28% (high, above the 95th percentile for neurotypical controls). Autocorrelation at lag 1: r = 0.35 (positive, indicating that performance clusters in runs of good and bad trials). Oscillation period: approximately 10 trials (consistent with metric instability with a 2-3 minute timescale).

**Step 3: Evaluate the heuristic field.** Confidence ratings: mean = 5.2 on a 0-10 scale (moderate, not inflated). Confidence-accuracy correlation: r = 0.12 (weak, indicating poor self-monitoring --- consistent with ADHD, where the metric instability produces variable performance that is hard to predict). Error pattern: errors are not systematically biased toward threat-relevant distractors (which would suggest anxiety) or uniformly distributed (which would suggest depression). Errors cluster in runs, consistent with metric instability.

**Step 4: Geometric diagnosis.** The pattern --- high trial-to-trial variance, positive autocorrelation, clustered errors, no systematic bias --- is consistent with metric instability (ADHD) and inconsistent with inflated heuristic (anxiety: would show bias toward threat-relevant distractors, lower variance, inflated confidence) or collapsed heuristic (depression: would show uniformly low performance, low variance, low confidence).

**Step 5: Generate treatment predictions.** Based on the metric instability diagnosis:
- Stimulant medication should reduce trial-to-trial variance (stabilize the metric) before it improves mean performance.
- Structured task scheduling (short blocks with breaks) should outperform extended task periods (because breaks allow the metric to reset before it drifts too far).
- Mindfulness training (which trains sustained attention, i.e., metric stability) should be more effective than cognitive-behavioral therapy (which addresses thought content, i.e., heuristic field).

These predictions are specific enough to guide treatment selection and to validate the geometric diagnosis: if the predictions hold, the geometric characterization was correct; if they fail, the defect is elsewhere.


## 14.11 Looking Forward

Cognitive pathology, viewed through the geometric lens, is not a collection of arbitrary symptom clusters but a systematic taxonomy of defects in the geometric objects that constitute cognition. The metric can be unstable (ADHD), rigid (autism), or distorted. The heuristic field can be collapsed (depression) or inflated (anxiety). Each defect produces a specific pattern of cognitive dysfunction that is distinguishable by task-based measurement and amenable to targeted intervention.

The geometric approach does not replace clinical diagnosis. It complements it, providing a level of mechanistic description that bridges the gap between neural substrate and behavioral symptom. The predictions generated by the geometric characterizations are testable, and their validation or refutation will determine whether the geometric approach adds clinical value beyond the existing frameworks.

This chapter closes Part IV --- the three chapters on human cognition. We have shown that the geometric framework, developed for artificial cognition in Parts II and III, applies equally to human cognition: the dual-process transition (Chapter 12), cognitive development (Chapter 13), and cognitive pathology (Chapter 14) are all interpretable as geometric phenomena on the cognitive manifold.

Part V turns to artificial cognition, first examining how the geometric framework illuminates the internal workings of large language models (Chapter 15) and then presenting the capstone finding: the five geometric signatures that characterize the five models tested in the Measuring AGI benchmarks (Chapter 16).

---

## Technical Appendix 14A: Metric Instability --- Formal Treatment

**Definition** (Metric Stability Index). *Let $g_{\mu\nu}(t)$ be the attention metric at time $t$, measured at discrete intervals $t_1, \ldots, t_N$. The metric stability index is:*

$$\text{MSI} = \frac{1}{N-1} \sum_{k=1}^{N-1} \|g_{\mu\nu}(t_{k+1}) - g_{\mu\nu}(t_k)\|_F$$

*where $\|\cdot\|_F$ is the Frobenius norm. A low MSI indicates a stable metric (small changes between successive measurements). A high MSI indicates an unstable metric (large changes).*

**Operationalization.** In practice, the attention metric is not directly observable. The MSI can be estimated from behavioral data by computing the task-performance correlation matrix in successive blocks of trials. If the correlation structure changes substantially between blocks (the dimensions that predict performance shift), the MSI is high. If the correlation structure is stable (the same dimensions predict performance throughout), the MSI is low.

**The ADHD prediction.** Let $\text{MSI}_{\text{ADHD}}$, $\text{MSI}_{\text{NT}}$, and $\text{MSI}_{\text{ASD}}$ be the metric stability indices for ADHD, neurotypical, and autistic populations. The geometric framework predicts:

$$\text{MSI}_{\text{ADHD}} > \text{MSI}_{\text{NT}} > \text{MSI}_{\text{ASD}}$$

This ordering is a direct consequence of the metric instability / stability / rigidity characterization and is testable with standard psychophysical methods.


## Technical Appendix 14B: Heuristic Field Defects --- The Depression-Anxiety Spectrum

**The heuristic field as a vector field.** Let $\mathbf{h}(x) = \nabla h(x)$ be the gradient of the heuristic field, viewed as a vector field on $\mathcal{M}$. The pathologies can be characterized by properties of this vector field:

| Pathology | $\|\mathbf{h}(x)\|$ | Direction of $\mathbf{h}$ | Divergence $\nabla \cdot \mathbf{h}$ |
|---|---|---|---|
| Healthy | Moderate | Toward goals | Near zero (balanced) |
| Depression | ~0 (collapsed) | Undefined (no direction) | ~0 (flat) |
| Anxiety | High (inflated) | Away from perceived threats | Positive (expanding) |
| Mixed anxiety-depression | Variable by dimension | Threat-avoidant, goal-flat | Positive on threat, zero on reward |

**The inflation factor as a diagnostic measure.** The inflation factor $\alpha(x) = h(x) / d(x, x_{\text{goal}})$ can be estimated from behavioral data by comparing the subject's estimated difficulty of a task (self-reported before the task) to the actual difficulty (measured by performance). For each task:

$$\hat{\alpha} = \frac{\text{self-reported difficulty}}{\text{actual difficulty (inverse of performance)}}$$

If $\hat{\alpha} > 1$ systematically, the heuristic field is inflated (anxiety). If $\hat{\alpha} < 1$ systematically, the field is deflated (overconfidence). If $\hat{\alpha}$ is undefined (the subject cannot estimate difficulty because nothing feels more or less difficult than anything else), the field is collapsed (depression).

**Comorbidity as multi-dimensional field defect.** Let $\mathbf{h} = (h_{\text{reward}}, h_{\text{threat}}, h_{\text{social}}, \ldots)$ be the decomposition of the heuristic field into domain-specific components. Comorbid anxiety-depression is characterized by:

$$\|\nabla h_{\text{reward}}\| \approx 0 \quad \text{(depression: collapsed reward gradient)}$$
$$\|\nabla h_{\text{threat}}\| \gg 1 \quad \text{(anxiety: inflated threat gradient)}$$

This multi-dimensional characterization explains why the two conditions frequently co-occur despite seeming phenomenologically opposite: they affect different components of the same geometric object.
