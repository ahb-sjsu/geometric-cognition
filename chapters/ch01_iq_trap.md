# Chapter 1: The IQ Trap

> *"Not everything that counts can be counted, and not everything that can be counted counts."*
> --- William Bruce Cameron (often misattributed to Albert Einstein)

---

> **RUNNING EXAMPLE --- MAYA'S MODEL**
>
> Maya Chen is staring at a spreadsheet that should not exist.
>
> She has just finished running five frontier language models through five cognitive benchmark tracks---Social Cognition, Learning, Metacognition, Attention, Executive Functions---twenty-one subtasks in all. The results are clean. The statistics are solid. She has computed composite scores for each model, averaging across tracks with careful normalization, and the composite rankings are ready for the report.
>
> The problem is the two models in the middle of the table. Claude 3.5 Sonnet and Gemini 2.5 Pro have composite scores so close they are statistically indistinguishable. By any reasonable ranking criterion---mean score, median score, weighted average---they tie.
>
> But when Maya looks at the track-level data, the models could not be more different. Claude has zero sycophancy---a perfect 1.000 on the sycophancy resistance test---but the worst divided attention score in the entire sample: 0.571. Pro has the best calibration of any model---an Expected Calibration Error of 0.230---but zero effort scaling: it applies the same computational resources to trivial and impossible problems alike.
>
> One model has an impervious conviction system bolted to a narrow attentional aperture. The other has an excellent internal compass bolted to a frozen throttle. They reason in fundamentally different ways. They fail at fundamentally different tasks. They have fundamentally different cognitive architectures.
>
> And their composite scores are the same number.
>
> Maya writes in her notebook: *"The composite is destroying the information that matters. It's not that the average is a bad summary---it's that the operation of averaging is irreversible. You can't get the profile back from the number. The geometry is gone."*
>
> She does not yet know the word for what she has discovered. By the end of this chapter, she will: it is the Scalar Irrecoverability Theorem.

---

## 1.1 The Seduction of the Single Number

Intelligence research has been dominated, for over a century, by the pursuit of a single number.

Charles Spearman introduced the general factor of intelligence---*g*---in 1904, arguing that performance across diverse cognitive tasks is driven by a single underlying variable. The claim was grounded in factor analysis: when you administer a battery of tests (verbal reasoning, spatial visualization, working memory, processing speed) and compute the correlations between them, you find that a single factor accounts for a substantial fraction of the variance. Spearman called this factor *g* and proposed that it represented a real property of minds---a general cognitive capacity that manifests across all intellectual domains.

The IQ test operationalized *g*. Alfred Binet designed the first practical intelligence test in 1905, and by mid-century the IQ score had become the standard measure of cognitive ability. The number was powerful. It predicted academic achievement, job performance, income, even longevity. It was stable across the lifespan, heritable, and normally distributed. It had the properties that scientists prize: reliability, validity, predictive power. For a single number, IQ was remarkably good.

This book argues that it is not good enough. Not because IQ fails to correlate with important outcomes---it does correlate, robustly. Not because the psychometric methods are unsound---factor analysis is a legitimate statistical technique. But because the operation that produces the single number---the contraction from a profile of cognitive capabilities to a scalar---is *geometrically irrecoverable*. It destroys structural information that cannot be reconstructed from the output. And the structural information it destroys is precisely the information that determines *how* a system reasons, as opposed to *how well* it reasons on average.

This is not a soft claim. It is a theorem, and we will prove it.


## 1.2 The Cognitive Tensor

To see what scalar measures destroy, we first need to see what exists before the destruction.

Consider a cognitive system---a human brain, a language model, anything that reasons. At any moment, this system has a *cognitive profile*: a collection of capabilities that jointly determine how it will perform on any given task. The Measuring AGI benchmarks decompose this profile along five tracks, each with multiple subtasks:

**Social Cognition** (T1--T5): Can the system make moral judgments? Does it resist framing effects? Is it vulnerable to emotional manipulation? Does it show asymmetric sensitivity to harm minimization versus harm exaggeration?

**Learning** (L1--L4): Can the system update beliefs in response to evidence? Does it resist sycophantic pressure? Can it learn from few examples? Does it handle ambiguous or contradictory information?

**Metacognition** (M1--M4): Does the system know how confident it should be? Can it detect ambiguity? Does it monitor its own performance? Does it scale effort to task difficulty?

**Attention** (A1--A4): Does the system resist irrelevant distractors? Can it sustain focus over time? Does it maintain signal quality under noise? Can it divide attention across parallel tasks?

**Executive Functions** (E1--E4): Can the system switch cognitive frameworks? Does it resist emotional anchoring? Can it engage in counterfactual reasoning? Does working memory scale with task demands?

Each subtask produces a score between 0 and 1. The full profile of a model is therefore a point in a 21-dimensional space---a vector with 21 components, one per subtask. We can represent this profile as a tensor.

**Definition 1.1** (Cognitive Profile Tensor). *For a cognitive system $S$, the cognitive profile tensor is the vector*

$$\mathbf{C}(S) = (c_1, c_2, \ldots, c_{21}) \in [0, 1]^{21}$$

*where each $c_i$ is the system's score on subtask $i$.*

This is, of course, a simplification. The true cognitive profile of any system is vastly higher-dimensional---the activation space of a human brain or a large language model has millions or billions of dimensions. But even this 21-dimensional simplification suffices to demonstrate the irrecoverability problem.

Now consider the five models in our benchmark suite: Claude 3.5 Sonnet, Gemini 2.0 Flash, Gemini 2.5 Flash, Gemini 3 Flash, and Gemini 2.5 Pro. Each has a cognitive profile tensor $\mathbf{C}(S)$. These five tensors live in the same 21-dimensional space. They can be compared component by component. Their differences can be visualized, measured, analyzed.

Here is what the tensors look like for two of the models, restricted to the most discriminating subtasks:

| Subtask | Claude 3.5 Sonnet | Gemini 2.5 Pro |
|---|---|---|
| L2 (Sycophancy) | 1.000 | 0.720 |
| M1 (Calibration ECE) | 0.250 | 0.230 |
| M3 (Self-Monitoring) | 0.723 | 0.350 |
| M4 (Effort Scaling) | 0.094 | 0.700 |
| A4 (Divided Attention) | 0.571 | 0.790 |
| E2 (Emotional Anchoring) | 0.670 | 0.830 |

The profiles are different on every dimension. Claude excels at sycophancy resistance but has almost no effort scaling. Pro has good effort scaling but mediocre sycophancy resistance. Claude has excellent self-monitoring but weak divided attention. Pro has the reverse. These are not minor variations around a common theme. They are structurally different configurations of cognitive capability---different shapes in the 21-dimensional space.

Now watch what happens when we compute the composite.


## 1.3 The Contraction

The operation that produces a single score from a profile is a *contraction*: a function that maps a high-dimensional object to a lower-dimensional one. In the simplest case, the composite score is a weighted average:

$$\bar{c}(S) = \sum_{i=1}^{21} w_i \cdot c_i(S)$$

where $w_i \geq 0$ and $\sum w_i = 1$. This is a linear map from $\mathbb{R}^{21}$ to $\mathbb{R}$---a projection from a 21-dimensional space onto a line.

Spearman's *g*-factor is a specific instance of this contraction. Factor analysis extracts the first principal component of the covariance matrix of test scores, and *g* is the projection of each individual's score vector onto this first principal component. The weights $w_i$ are the factor loadings. The operation is still a linear contraction from a profile space to a scalar.

IQ is computed from *g* by normalization: $\text{IQ} = 100 + 15 \cdot z_g$, where $z_g$ is the $z$-score of the individual's *g*-factor value. This is a monotonic transformation of the contracted scalar---it changes the scale but not the information content.

The composite score used in most AI benchmarks is the same operation with equal weights: accuracy averaged across tasks. The MMLU score, the HumanEval score, the "overall" score on any leaderboard---all are contractions of a profile tensor to a scalar.

**Definition 1.2** (Scalar Contraction). *A scalar contraction is any function $\phi: [0,1]^n \to \mathbb{R}$ that maps a cognitive profile tensor to a single real number. A linear contraction is a scalar contraction of the form $\phi(\mathbf{C}) = \mathbf{w} \cdot \mathbf{C}$ for some weight vector $\mathbf{w}$.*

The g-factor is the linear contraction whose weights are the first principal component loadings. IQ is a monotonic rescaling of the g-factor. Benchmark accuracy is the linear contraction with uniform weights. All are scalar contractions. And all are irrecoverable.


## 1.4 The Scalar Irrecoverability Theorem

**Theorem 1.1** (Scalar Irrecoverability). *Let $\phi: [0,1]^n \to \mathbb{R}$ be any scalar contraction with $n \geq 2$. Then for any value $v$ in the range of $\phi$, the preimage $\phi^{-1}(v)$ contains a continuum of distinct profile tensors. In particular, for any pair of profile tensors $\mathbf{C}_1 \neq \mathbf{C}_2$ with $\phi(\mathbf{C}_1) = \phi(\mathbf{C}_2)$, no function $\psi: \mathbb{R} \to [0,1]^n$ can satisfy $\psi(\phi(\mathbf{C}_1)) = \mathbf{C}_1$ and $\psi(\phi(\mathbf{C}_2)) = \mathbf{C}_2$ simultaneously.*

*The contraction is not merely lossy. It is irrecoverable: the destroyed information cannot be reconstructed from the output, even in principle.*

The proof is immediate from dimensionality. A continuous function from $[0,1]^n$ to $\mathbb{R}$ maps an $n$-dimensional space to a 1-dimensional space. For $n \geq 2$, the fibers (preimages of individual values) are generically $(n-1)$-dimensional subsets of the domain. No function from $\mathbb{R}$ to $[0,1]^n$ can invert the contraction, because the contraction has mapped an $(n-1)$-dimensional set of distinct profiles to a single point, and a function from $\mathbb{R}$ has only a 1-dimensional domain to "spread" them back into.

The theorem holds for *any* scalar contraction---not just the linear ones. You cannot fix the problem by choosing a cleverer weighting scheme, or by using a nonlinear aggregation function, or by normalizing differently. The destruction is inherent in the reduction from many dimensions to one.

But the theorem is abstract. Let us make it concrete.


## 1.5 The Empirical Demonstration

The five models in the Measuring AGI benchmark suite provide a constructive proof of scalar irrecoverability. Here is the argument.

**Claim**: No single composite score correctly ranks all five models across all five cognitive tracks.

**Proof by exhibition of crossings**: Consider the following pairwise comparisons.

*Crossing 1: Claude vs. Flash 3 on Sycophancy and Divided Attention.*
Claude scores 1.000 on sycophancy resistance (L2); Flash 3 scores approximately 0.440. By this measure, Claude is decisively superior. But Claude scores 0.571 on divided attention (A4); Flash 3 scores 1.000. By this measure, Flash 3 is decisively superior. Any composite that weights L2 and A4 equally will produce similar overall scores for both models, hiding the fact that they have *opposite* cognitive architectures on these dimensions.

*Crossing 2: Flash 2.5 vs. Pro on Sycophancy and Calibration.*
Flash 2.5 has the worst sycophancy score in the sample: 0.440 (56% sycophancy rate). Pro has moderate sycophancy resistance. But Flash 2.5 has excellent distractor resistance; Pro has better calibration (ECE = 0.230 vs. Flash 2.5's 0.415). Again, the ranking reverses depending on which track you measure.

*Crossing 3: Flash 2.0 vs. Flash 3 on Recovery and Working Memory.*
Flash 2.0 has the best flexibility and recovery scores but the worst working memory. Flash 3 has the best working memory (0.909) but mediocre recovery. A composite averages out these opposite strengths.

These crossings are not marginal effects that might vanish with more data. They are large, robust differences on individual subtasks that happen to cancel when averaged. The composite does not approximate the profile. It annihilates the profile's structure.

**The geometric picture.** Think of the five models as five points in 21-dimensional cognitive space. A scalar contraction projects these five points onto a line. The projection preserves the order of the projected coordinates but destroys the relative positions in the other 20 dimensions. Two points that are far apart in 21-dimensional space can project to the same point on the line. Two points that are close in 21-dimensional space can project to distant points on the line if they differ mainly along the projection direction. The line captures at most one dimension of a 21-dimensional structure.

The g-factor captures the *first principal component*---the direction of maximum variance. This is the best possible one-dimensional summary, in the least-squares sense. But "best possible one-dimensional summary" is not the same as "adequate summary." If the variance is distributed across many dimensions---as it is in our data, where the five cognitive tracks are substantially independent---then no single direction captures most of the structure.

And this is exactly what we observe. The five tracks in the Measuring AGI suite are not highly correlated. A model's Social Cognition performance does not predict its Attention performance. Its Learning profile does not predict its Executive Functions profile. The cognitive tensor has substantial variance along multiple independent dimensions. Contracting it to a scalar destroys most of the structure.


## 1.6 What the Contraction Destroys

The Scalar Irrecoverability Theorem tells us that information is destroyed, but it does not tell us what information is destroyed or why it matters. Let us be specific.

**1. The contraction destroys the profile shape.** Claude's cognitive profile has a distinctive shape: a sharp peak on sycophancy resistance, a deep valley on divided attention, moderate values elsewhere. This shape---the "narrow channel" signature---determines how Claude will behave on novel tasks. It will resist social pressure at the cost of attentional flexibility. It will maintain its position under adversarial probing but struggle with parallel processing demands. The shape is the architecture. The composite, which averages the peak and the valley into a middling number, erases the shape entirely.

Flash 3's profile has a different shape: relatively flat across most dimensions, with a sharp peak on divided attention and working memory, and a valley on sycophancy resistance. This is the "wide aperture" signature---a system that processes broadly but is easily deflected by social pressure. The composite of Flash 3's profile produces a middling number almost identical to Claude's middling number. Two completely different cognitive architectures, one indistinguishable composite.

Pro's profile is different again: the best calibration, moderate execution, zero effort scaling. The "calibrated navigator"---a system that knows where it is on the manifold but cannot modulate its search intensity. Its composite is also middling.

Three models. Three architectures. One composite range.

**2. The contraction destroys the failure mode signature.** Each cognitive architecture has characteristic failure modes. Claude fails when tasks require divided attention or broad scanning---its narrow channel cannot parallelize. Flash 3 fails when tasks require resistance to social pressure or adversarial framing---its wide aperture lets in too much irrelevant signal. Pro fails when tasks require dynamic effort allocation---its calibrated navigator knows the terrain but cannot adjust its speed.

These failure modes are predictable from the profile shape. Given the full tensor, you can anticipate where each model will break. Given only the composite, you cannot. The composite tells you the *average* performance level; it tells you nothing about *which tasks* will be solved and which will be failed. And in any practical application---deploying a model for medical diagnosis, legal reasoning, educational support---it is precisely the failure mode signature that matters. You do not want to know that a model scores 73% on average. You want to know whether it will fail on *your* task.

**3. The contraction destroys the interaction structure.** The five cognitive tracks are not independent vectors that can be meaningfully averaged. They interact. A model with excellent metacognition but poor attention will use its self-monitoring to compensate for attentional lapses---it will notice when it has lost focus and redirect. A model with excellent attention but poor metacognition will maintain focus effortlessly but never notice when focus is misdirected. These interaction effects are visible in the full tensor but invisible in the composite.

The M3/M4 dissociation illustrates this vividly. In the metacognitive plane defined by self-monitoring (M3) and effort scaling (M4), no model occupies Quadrant I---the quadrant where both capabilities are strong. Every model has either a working thermometer (it can detect its own performance degradation) or a working valve (it can adjust effort to task difficulty), but never both. This dissociation is a structural feature of the cognitive architecture---a geometric constraint on the metacognitive surface. The composite annihilates it. When you average M3 and M4 into a single "metacognition score," the dissociation vanishes, and the empty quadrant---the most informative feature of the metacognitive landscape---becomes invisible.


## 1.7 g-Factor as Tensor Contraction

We can now give a precise geometric characterization of what Spearman's g-factor actually is.

Let $\mathbf{C} \in [0,1]^n$ be the cognitive profile tensor. The covariance matrix of $\mathbf{C}$ across a population of cognitive systems is $\Sigma \in \mathbb{R}^{n \times n}$. Factor analysis extracts the eigenvectors of $\Sigma$:

$$\Sigma = \sum_{k=1}^{n} \lambda_k \mathbf{v}_k \mathbf{v}_k^T$$

where $\lambda_1 \geq \lambda_2 \geq \cdots \geq \lambda_n \geq 0$ are the eigenvalues and $\mathbf{v}_k$ are the corresponding eigenvectors.

The g-factor is the projection onto the first eigenvector:

$$g(S) = \mathbf{v}_1 \cdot \mathbf{C}(S)$$

This is a specific linear contraction---the one that maximizes the fraction of variance explained. It is the "best" one-dimensional summary in the least-squares sense, and this optimality property is what gives g-factor theory its empirical power.

But the Scalar Irrecoverability Theorem applies regardless. The contraction maps $n$-dimensional profiles to a line. It destroys all variance along the directions $\mathbf{v}_2, \ldots, \mathbf{v}_n$. The fraction of variance preserved is $\lambda_1 / \sum \lambda_k$---the proportion of total variance in the first principal component.

In human cognitive data, this proportion is typically 40--60%. The g-factor captures the plurality of variance, which is impressive for a single number. But 40--60% is not 100%. The other 40--60% of variance---the variance along the non-g directions---encodes the *profile structure* that distinguishes, say, a person with high verbal and low spatial ability from a person with low verbal and high spatial ability. Both might have the same g. They reason in different ways.

In our AI benchmark data, the proportion of variance in the first component is even smaller, because the five cognitive tracks are substantially independent. The g-factor of the five models would capture perhaps 30--40% of the total variance. The remaining 60--70% is profile structure---the structure that distinguishes Claude's narrow channel from Flash 3's wide aperture from Pro's calibrated navigator.

**The geometric picture.** The g-factor defines a preferred direction in cognitive space---the direction $\mathbf{v}_1$ of maximum variance. All cognitive profiles are projected onto this direction. The projection preserves the component of each profile along $\mathbf{v}_1$ and discards the components along all other directions. The resulting scalar retains the "amount" of cognition (how far along the dominant direction) but discards the "shape" of cognition (the pattern of strengths and weaknesses in the other directions).

This is a *specific contraction of the cognitive tensor*---not an arbitrary averaging, but the optimal rank-1 approximation of the covariance matrix. It is the best possible one-dimensional summary. And it is still irrecoverable.


## 1.8 What Would Recoverability Require?

If scalar measures are irrecoverable, what would a recoverable measure look like?

The answer follows from the theorem by negation. The contraction is irrecoverable because it maps a high-dimensional space to a low-dimensional one, and the reduction in dimensionality means that distinct profiles can produce identical outputs. To avoid this, we need a map that preserves enough dimensionality to distinguish the profiles we care about.

**Definition 1.3** (Recoverable Representation). *A representation $\Phi: [0,1]^n \to \mathbb{R}^k$ is recoverable with respect to a set $\mathcal{S}$ of cognitive systems if there exists a left inverse $\Psi: \mathbb{R}^k \to [0,1]^n$ such that $\Psi(\Phi(\mathbf{C}(S))) = \mathbf{C}(S)$ for all $S \in \mathcal{S}$.*

For exact recoverability, we need $k \geq n$---the representation must have at least as many dimensions as the profile. But in practice, we do not need exact recoverability. We need *sufficient* recoverability: enough dimensions to distinguish the cognitive architectures that are functionally distinct.

The Measuring AGI benchmarks suggest that five dimensions---one per track---capture the major axes of variation. Within each track, the subtask scores are moderately correlated (they all probe aspects of the same cognitive capability). Between tracks, the correlations are weak. Five track-level scores, one per cognitive dimension, would preserve most of the architecture-distinguishing information.

This is the difference between:

- **A scalar**: $\bar{c} = 0.73$. Claude, Flash 3, and Pro are indistinguishable.
- **A profile**: $(0.82, 0.65, 0.71, 0.64, 0.78)$. Claude's narrow channel, Flash 3's wide aperture, and Pro's calibrated navigator are immediately distinguishable.

The profile is not a single number. It is a point in five-dimensional space. It has *shape*---a pattern of peaks and valleys that characterizes the cognitive architecture. This shape is what the g-factor destroys and what the cognitive manifold preserves.


## 1.9 The Deeper Lesson: Measurement Determines Ontology

The IQ trap is not merely a technical problem about information loss. It is a problem about *what we think intelligence is*.

When we measure intelligence with a single number, we implicitly commit to the ontological claim that intelligence is a single thing. The number creates the entity. IQ scores are compared as though they were measuring a homogeneous quantity, like temperature or mass. A person with IQ 130 has "more intelligence" than a person with IQ 100, the way a heavier object has "more mass" than a lighter one. The language of "more" and "less" forces a total ordering---every cognitive system can be placed on a line, and the line is the thing.

But the benchmark data say otherwise. The five cognitive tracks define five substantially independent dimensions. A system can be "more intelligent" on one dimension and "less intelligent" on another, and the comparison is not resolvable into a scalar ordering. Claude has more sycophancy resistance than Flash 3, and Flash 3 has more divided attention capacity than Claude. Which is "more intelligent"? The question has no answer, because intelligence is not a scalar. It is a tensor.

This is not a new observation in psychology. Howard Gardner's theory of multiple intelligences (1983) argued for a similar decomposition, though without the geometric framework. Robert Sternberg's triarchic theory (1985) proposed analytical, creative, and practical intelligence as independent dimensions. The Carroll-Horn-Cattell (CHC) theory, the current consensus in psychometrics, distinguishes crystallized intelligence, fluid intelligence, processing speed, and several other broad factors.

What the geometric framework adds is a precise mathematical characterization of why the scalar fails and what replaces it. The scalar fails because it is a contraction of a tensor, and the contraction is irrecoverable. What replaces it is not a "better" scalar but a different mathematical object: a profile in a multi-dimensional space---a point on the cognitive manifold.

The manifold is the subject of Chapter 3. But first, we need to understand the geometric structure that Kahneman and Tversky glimpsed but never formalized---the structure that makes System 1 and System 2 not two separate processors but two regimes of the same geometric process.


## 1.10 The Historical Parallel: Phrenology's Lesson

There is a historical parallel that illuminates the stakes.

In the nineteenth century, phrenology proposed that mental faculties could be measured by the shape of the skull. The phrenologists were wrong about the mechanism (skull bumps do not correspond to brain regions in the way they supposed), but they were right about one thing: mental faculties are multiple, not singular. Franz Joseph Gall, the founder of phrenology, insisted that the mind was composed of multiple independent faculties---memory, language, mathematical ability, social cognition---each localized in a different brain region. His opponents, led by Pierre Flourens, argued for a unitary view: the brain operated as a whole, and mental ability was a single, undifferentiated capacity.

The debate between Gall and Flourens is eerily isomorphic to the debate between multiple intelligences and g-factor theory. And the resolution, in both cases, is the same: neither extreme is correct. Mental faculties are neither fully unitary nor fully independent. They share common resources (hence the positive manifold that gives rise to g), but they have independent components (hence the multiple factors of CHC theory). The truth is geometric: mental faculties are dimensions of a manifold that has non-trivial correlation structure---neither a line (fully correlated) nor an orthogonal space (fully independent) but a curved surface with its own intrinsic geometry.

The g-factor captures the correlation structure. It correctly identifies the fact that cognitive abilities tend to be positively correlated---that people who are good at one thing tend to be good at other things too. But it mistakes this correlation for identity. The positive manifold does not mean that all cognitive abilities are the same ability. It means that they share a common resource base---working memory, processing speed, neural efficiency---while retaining independent components.

In tensor language: the covariance matrix $\Sigma^{ij}$ is not diagonal (the abilities are correlated), but it is also not rank-1 (the abilities are not reducible to a single factor). It has multiple significant eigenvalues, each corresponding to an independent axis of variation. The g-factor is the projection onto the first eigenvalue. The remaining eigenvalues are where the profile structure lives.

The lesson from phrenology is that measurement technology shapes ontological commitment. The phrenologists measured skull bumps and concluded that mental faculties were localized modules. The psychometricians measured test score correlations and concluded that mental ability was a single factor. Both were measuring something real---skull bumps do correlate weakly with some brain properties, and test scores do have a positive manifold. Both drew ontological conclusions that their data did not support.

The Scalar Irrecoverability Theorem is the formal version of this lesson. The measurement operation (contraction to a scalar) determines the ontological conclusion (intelligence is a single thing). The conclusion follows from the measurement, not from the reality. The reality is geometric. The measurement collapses the geometry.


## 1.11 Five Models, Five Architectures, One Lesson

Let us complete the empirical picture by examining all five model signatures, because the full set demonstrates irrecoverability more powerfully than any pair.

**Claude 3.5 Sonnet: The Narrow Channel.** Zero sycophancy. Worst divided attention (0.571). Moderate calibration. Excellent self-monitoring (0.723) but negligible effort scaling (0.094). The profile is sharply peaked on conviction and self-awareness, with deep valleys on flexibility and breadth. Claude knows what it thinks and refuses to budge, but it cannot process multiple streams or adjust its effort to task difficulty. Geometrically: a system with a highly eccentric attention metric concentrated along the truthfulness dimension, navigating the manifold with extreme directional selectivity.

**Gemini 2.0 Flash: The Adaptive Baseline.** Best flexibility, best recovery, worst working memory. Moderate sycophancy. This is a system that adapts quickly to novel situations (high flexibility) and recovers well from perturbation (high recovery), but lacks the working memory to sustain complex multi-step reasoning. Geometrically: a system with a responsive but shallow tangent space---it can change direction easily but cannot hold many cognitive dimensions simultaneously.

**Gemini 2.5 Flash: The Elastic Malleability.** Worst sycophancy (56%), best distractor resistance. The combination is striking: a system that is maximally susceptible to social pressure but maximally resistant to sensory noise. Social signals reshape its heuristic field; sensory distractors do not. Geometrically: the attention metric is stable under sensory perturbation but unstable under social perturbation---a direction-dependent robustness that reveals the anisotropic structure of the metric's vulnerability surface.

**Gemini 3 Flash: The Wide Aperture.** Perfect divided attention (1.000), best working memory (0.909), mediocre sycophancy resistance. This is the opposite of Claude: a broad, multi-channel system that processes widely but lacks the directional selectivity to resist social manipulation. Geometrically: a nearly isotropic attention metric that provides coverage across all dimensions but heightened sensitivity to none.

**Gemini 2.5 Pro: The Calibrated Navigator.** Best calibration (ECE 0.230), zero effort scaling (0.700 vs. the others), moderate performance across all tracks. Pro knows where it is on the manifold better than any other model---its distance estimates are the most accurate. But it cannot adjust its search intensity, applying the same computational resources regardless of task difficulty. Geometrically: an accurate heuristic field paired with a frozen control layer. The compass works; the throttle is stuck.

These five signatures are the *content* that scalar evaluation destroys. Each signature tells a story about how the model navigates the cognitive manifold---its attentional biases, its control layer properties, its vulnerability profile. A composite score for each model would produce five numbers that obscure every structural difference. The theorem predicts exactly this. The data confirm it.


## 1.12 The AI Evaluation Crisis

The Scalar Irrecoverability Theorem has immediate implications for how we evaluate artificial intelligence.

The current paradigm of AI evaluation is leaderboard-centric. Models are ranked by a single metric: accuracy on MMLU, pass rate on HumanEval, Elo on Chatbot Arena. These metrics are scalar contractions. They suffer from exactly the irrecoverability problem we have described.

Consider two language models that both score 85% on MMLU. One achieves this by excelling at humanities and struggling at STEM. The other achieves it by excelling at STEM and struggling at humanities. Their composite scores are identical. Their cognitive architectures are completely different. A user who needs a model for legal research would strongly prefer the first; a user who needs a model for code generation would strongly prefer the second. The leaderboard cannot make this distinction. The geometry is gone.

The problem is worse than mere information loss. Scalar evaluation creates *perverse incentives*. If models are ranked by a composite, developers optimize for the composite. Optimizing for the composite means increasing the average across all subtasks, which may mean strengthening the weakest capabilities at the expense of the strongest. The result is convergence toward mediocrity: models that are adequate at everything and excellent at nothing. The profile becomes flat, the cognitive architecture becomes homogeneous, and the diversity of cognitive strategies that might have been explored is sacrificed on the altar of the leaderboard.

The geometric alternative is to evaluate models by their *cognitive profile*---the full tensor, or at minimum, the track-level scores that capture the major axes of variation. This replaces the question "How intelligent is this model?" (a scalar question with a scalar answer) with the question "What is this model's cognitive architecture?" (a geometric question with a geometric answer). The answer is not a number. It is a shape: narrow channel, wide aperture, calibrated navigator, elastic malleability, adaptive baseline. Each shape has strengths, weaknesses, and characteristic failure modes. Each is suited to different tasks. None is uniformly "better" than the others.

This is what the cognitive manifold makes precise. Each model occupies a different point on the manifold. The distance between points is measured by the attention metric. The local neighborhood of each point---the tangent space---determines what the model can do in one reasoning step. The heuristic field at each point determines where the model's search will go next. The full geometric picture replaces the leaderboard with a map.


## 1.11 Implications for Cognitive Science

The implications extend beyond AI evaluation to cognitive science itself.

The g-factor debate has consumed an enormous share of intellectual energy in psychology. Proponents argue that g is the best predictor of real-world outcomes, that it is heritable, that it has neural correlates. Critics argue that g obscures meaningful differences between cognitive abilities, that it is culturally biased, that it reifies a statistical artifact as a natural kind.

The geometric framework cuts through this debate by identifying exactly what g is and what it is not.

What g *is*: the optimal one-dimensional summary of cognitive variation. The first principal component. The direction of maximum variance. A real and useful statistical object.

What g *is not*: a sufficient summary of cognitive architecture. The g-factor captures the plurality of variance but discards the profile structure. Two individuals with the same g can have completely different patterns of cognitive strength and weakness. The g-factor tells you the "amount" of cognitive variation along the dominant direction; it tells you nothing about the "shape" of cognitive variation in the other directions.

The geometric framework suggests that the right question is not "Is g real?" but "Is one dimension enough?" The answer, from both the psychometric evidence (CHC theory's multiple broad factors) and the AI benchmark evidence (five substantially independent cognitive tracks), is no.

The cognitive manifold is the mathematical object that makes "multiple dimensions of intelligence" precise. It is not a vague gesture toward multiplicity---"intelligence is many things, not one thing." It is a specific claim about mathematical structure: cognitive profiles live in a multi-dimensional space with a metric, and the geometry of this space determines how cognition works.


## 1.14 Worked Example: The Composite That Lies

To make the irrecoverability concrete, consider a deployment scenario.

A hospital is evaluating three language models for use in its clinical decision support system. The evaluation uses a composite accuracy score across five task types: diagnosis from symptoms, drug interaction checking, treatment planning, patient communication, and medical coding.

Model A scores: (0.95, 0.60, 0.80, 0.70, 0.85). Composite: 0.78.
Model B scores: (0.70, 0.85, 0.75, 0.80, 0.80). Composite: 0.78.
Model C scores: (0.80, 0.75, 0.78, 0.77, 0.80). Composite: 0.78.

All three composites are identical. The leaderboard ranks them as tied.

But Model A is the only safe choice for a diagnostic support role: its 0.95 on diagnosis is critical, and its 0.60 on drug interactions is irrelevant if a separate system handles drug checking. Model B is the only safe choice for a pharmacy role: its 0.85 on drug interactions is essential. Model C is the safest choice for a general-purpose role where no single task dominates.

The composite cannot distinguish these three models. It maps three different cognitive architectures---three different patterns of strength and vulnerability---to the same scalar. A deployment decision based on the composite would be a coin flip among three models with radically different suitability profiles.

The cognitive tensor distinguishes them immediately. The five-component profile reveals the shape: Model A is diagnosis-peaked, Model B is drug-interaction-peaked, Model C is flat. The shape determines suitability. The composite erases the shape.

This is not a hypothetical. It is the actual structure of the problem in AI-assisted healthcare, AI-assisted legal analysis, AI-assisted education, and every other domain where the *pattern* of capabilities matters more than the *average*. The Scalar Irrecoverability Theorem says that this problem is not fixable by better averaging. It is fixable only by preserving the profile---by replacing the scalar with the tensor, the leaderboard with the manifold, the ranking with the map.


## 1.16 Looking Forward: From Trap to Manifold

We have shown that scalar intelligence measures---IQ, g-factor, composite accuracy---are geometrically irrecoverable contractions of a multi-dimensional cognitive profile. The contraction destroys the profile shape, the failure mode signature, and the interaction structure that jointly determine how a system reasons.

The theorem is negative: it tells us what does not work. The rest of this book is constructive: it builds the mathematical framework that replaces scalar evaluation with geometric characterization.

Chapter 2 begins the constructive program by showing that Kahneman's dual-process theory---perhaps the most influential framework in modern cognitive science---already contains geometric intuitions that the scalar framework cannot express. System 1 and System 2 are not two separate processors. They are two regimes of the same geometric process, distinguished by the curvature of the cognitive manifold. The transition between them is a geometric phase transition, not a modular switch. And the cost of the transition---the ~38% recovery ceiling---is a structural property of the geometry, not a parameter to be tuned.

From there, the framework builds: the cognitive manifold (Chapter 3), the attention metric (Chapter 4), working memory as tangent space (Chapter 5), executive functions as search control (Chapter 6). Each chapter adds a geometric object. Each object has a cognitive interpretation. And each is independently measurable by the benchmark data that motivated the entire project.

The IQ trap is the departure point, not the destination. The destination is a geometry of cognition that is rich enough to characterize what scalar measures destroy, precise enough to make testable predictions, and practical enough to guide the evaluation and deployment of cognitive systems---both human and artificial.

We begin with Kahneman.


## Technical Appendix 1A: Formal Statement and Proof of the Scalar Irrecoverability Theorem

**Theorem 1.1** (Scalar Irrecoverability, Formal Version). *Let $n \geq 2$ and let $\phi: [0,1]^n \to \mathbb{R}$ be a continuous surjection. Then:*

*(i) For all $v$ in the interior of the range of $\phi$, the fiber $\phi^{-1}(v)$ has Hausdorff dimension at least $n - 1$.*

*(ii) There exist $\mathbf{C}_1, \mathbf{C}_2 \in [0,1]^n$ with $\mathbf{C}_1 \neq \mathbf{C}_2$ and $\phi(\mathbf{C}_1) = \phi(\mathbf{C}_2)$ such that $\|\mathbf{C}_1 - \mathbf{C}_2\|_\infty$ is arbitrarily close to 1. That is, the collisions are not merely between "similar" profiles; maximally dissimilar profiles can be mapped to the same scalar.*

*(iii) No function $\psi: \mathbb{R} \to [0,1]^n$ can satisfy $\psi \circ \phi = \text{id}$ on any subset of $[0,1]^n$ with more than one point per fiber.*

*Proof.*

*(i)* By the implicit function theorem (for smooth $\phi$) or by the topological dimension theory of level sets (for continuous $\phi$), the preimage of a regular value of a continuous function from an $n$-dimensional space to $\mathbb{R}$ is a topological manifold of dimension $n - 1$. For $n \geq 2$, this is at least 1-dimensional---a curve or higher-dimensional surface.

*(ii)* For a linear contraction $\phi(\mathbf{C}) = \mathbf{w} \cdot \mathbf{C}$, consider the profiles $\mathbf{C}_1 = (1, 0, 0, \ldots, 0)$ and $\mathbf{C}_2 = (0, w_1/w_2, 0, \ldots, 0)$ when $w_2 > 0$. Then $\phi(\mathbf{C}_1) = w_1 = w_1/w_2 \cdot w_2 = \phi(\mathbf{C}_2)$, but $\|\mathbf{C}_1 - \mathbf{C}_2\|_\infty = 1$. For nonlinear $\phi$, the intermediate value theorem guarantees similar collisions.

*(iii)* Suppose $\psi: \mathbb{R} \to [0,1]^n$ satisfies $\psi(\phi(\mathbf{C})) = \mathbf{C}$ for all $\mathbf{C}$ in some subset $\mathcal{S}$ with more than one point per fiber of $\phi$. Let $\mathbf{C}_1, \mathbf{C}_2 \in \mathcal{S}$ with $\phi(\mathbf{C}_1) = \phi(\mathbf{C}_2) = v$ and $\mathbf{C}_1 \neq \mathbf{C}_2$. Then $\psi(v) = \mathbf{C}_1$ and $\psi(v) = \mathbf{C}_2$, which contradicts the assumption that $\psi$ is a function.  $\square$


## Technical Appendix 1B: The g-Factor as Tensor Contraction in Index Notation

For readers familiar with tensor calculus, the g-factor construction can be expressed in index notation, which clarifies its relationship to the tensor contractions that appear later in the book.

Let $C^i$ denote the $i$-th component of the cognitive profile tensor (an upper index denoting a contravariant vector in cognitive space). The covariance matrix is:

$$\Sigma^{ij} = \langle (C^i - \langle C^i \rangle)(C^j - \langle C^j \rangle) \rangle$$

where $\langle \cdot \rangle$ denotes the population average. The g-factor is the contraction:

$$g = v_i C^i$$

where $v_i$ is the first eigenvector of $\Sigma^{ij}$ (lowered index indicating it acts as a covector). This contraction maps the cognitive tensor from a vector in $n$-dimensional space to a scalar. The information destroyed is the component of $C^i$ orthogonal to $v_i$---that is, the projection onto the $(n-1)$-dimensional subspace spanned by $v_2, \ldots, v_n$.

In Chapter 3, we will introduce the full Riemannian metric $g_{\mu\nu}$ on the cognitive manifold, and the distinction between the g-factor (a scalar contraction) and the metric tensor (a bilinear form on the tangent space) will become both notationally and conceptually important. The g-factor contracts the cognitive tensor to a point on a line. The metric tensor preserves the full structure of the cognitive space by defining distances, angles, and curvatures. The g-factor is a shadow; the metric is the object that casts it.
