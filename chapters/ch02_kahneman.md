# Chapter 2: Kahneman's Geometric Intuition

> *"A general 'law of least effort' applies to cognitive as well as physical exertion. The law asserts that if there are several ways of achieving the same goal, people will eventually gravitate to the least demanding course of action."*
> --- Daniel Kahneman, *Thinking, Fast and Slow* (2011)

---

> **RUNNING EXAMPLE --- MAYA'S MODEL**
>
> Maya has secured time on the department's fMRI scanner. Her subject today is Dr. James Okafor, a moral philosopher who has agreed to reason through a series of ethical dilemmas while his brain is imaged at two-second intervals.
>
> The first dilemma is simple: a person drops their wallet, and you find it. Should you return it? James answers in under three seconds. The fMRI shows a tight cluster of activation in the ventromedial prefrontal cortex---the region associated with rapid, intuitive moral judgment. The activation pattern is smooth, concentrated, low-dimensional. If Maya could draw the trajectory of James's cognitive state through activation space, it would be a nearly straight line from problem to answer.
>
> The second dilemma is the footbridge problem: a trolley is heading toward five people, and the only way to stop it is to push a large stranger off a bridge into its path. James pauses. The fMRI blooms. Activation spreads from the vmPFC to the dorsolateral prefrontal cortex, the anterior cingulate, the temporoparietal junction. The pattern is complex, distributed, high-dimensional. The trajectory of James's cognitive state is no longer a straight line. It curves, doubles back, loops through regions of activation space that the simple dilemma never touched.
>
> Maya overlays the two trajectories. The simple dilemma produced a near-geodesic: a short, straight path through low-curvature cognitive space. The complex dilemma produced something labored and winding: a trajectory navigating high-curvature terrain, forced to account for the competing gravitational pulls of utilitarian calculation and deontological constraint.
>
> She writes in her notebook: *"System 1 and System 2 are not two systems. They are the same system in two geometric regimes. When the manifold is flat, the gradient is enough. When the manifold curves, you need the geodesic equation."*
>
> Then she adds, almost as an afterthought: *"And the cost of switching from gradient to geodesic is about 38%."*

---

## 2.1 The Standard Account

Daniel Kahneman's dual-process theory, developed over four decades of collaboration with Amos Tversky and formalized in *Thinking, Fast and Slow* (2011), divides cognitive processing into two systems:

**System 1** is fast, automatic, effortless, and associative. It operates below the threshold of conscious deliberation. It produces intuitions---rapid judgments that arrive fully formed, without the sensation of having worked through a chain of reasoning. System 1 recognizes faces, completes familiar phrases, detects anger in a voice, computes 2 + 2. It is the system that answers "What is the capital of France?" before you have finished reading the question.

**System 2** is slow, deliberate, effortful, and rule-governed. It operates within conscious awareness and draws on working memory. It is the system that computes 17 x 24, plans a route through an unfamiliar city, evaluates the logical validity of an argument. System 2 engages when System 1 encounters something it cannot handle: a novel problem, a contradiction, a task that requires sustained attention and sequential reasoning.

The interaction between the two systems is the engine of Kahneman's research program. System 1 generates impressions and intuitions; System 2 monitors, corrects, and overrides when necessary. Many cognitive biases arise because System 2 fails to override System 1's errors---either because it is lazy (it defaults to the easy answer), or because it is occupied with something else (cognitive load depletes System 2 resources), or because it is unaware of the error (the intuition feels right).

This is the standard account. It has been enormously productive. It has organized decades of experimental findings into a coherent narrative. It has influenced policy (Thaler and Sunstein's "nudge" framework), education (teaching people to recognize System 1 errors), and artificial intelligence (chain-of-thought prompting as a proxy for System 2 reasoning).

And yet there is something deeply unsatisfying about it.


## 2.2 The Problem with "Two Systems"

The dual-process framework has been criticized on multiple grounds, but the criticism that matters for our purposes is structural. The framework posits two systems---two distinct computational architectures, two kinds of processing---and then faces the problem of explaining how they interact. Where does System 1 end and System 2 begin? What triggers the transition? What determines how much System 2 effort is allocated to a given task? These are not peripheral questions. They are the central questions of cognitive architecture, and the dual-process framework answers them with gestures rather than mechanisms.

Consider the transition from System 1 to System 2. Kahneman describes it as triggered by "surprise, effort, or difficulty"---when System 1 encounters something unexpected, demanding, or beyond its capacity, System 2 is engaged. But this is a description, not a mechanism. What *is* the detection process that identifies difficulty? How is "difficulty" represented in the cognitive architecture? What is the computational cost of the transition, and why does it take the particular form it takes?

The modular account---System 1 is one neural circuit, System 2 is another, and a switch mechanism toggles between them---is physiologically implausible. The brain regions associated with "System 1" and "System 2" processing overlap extensively. The dorsolateral prefrontal cortex, supposedly the seat of System 2, is active during many "System 1" tasks. The ventromedial prefrontal cortex, supposedly the seat of System 1, is active during many "System 2" tasks. The neuroimaging evidence supports a continuum of processing styles, not a binary switch between modules.

The continuum account---System 1 and System 2 are endpoints of a single processing dimension, with many intermediate states---is more plausible but leaves the central questions unanswered. What varies along the continuum? What determines where on the continuum a given task is processed? How does the system move from one point on the continuum to another?

The geometric framework provides answers to all of these questions. And the answers are not merely consistent with Kahneman's observations---they explain why those observations take the specific form they do, and they make novel predictions that the dual-process framework cannot.


## 2.3 System 1 as Gradient Following

Recall from Chapter 1 that reasoning is search on a structured space, and that the quality of search depends on the heuristic field $h(x)$---the scalar function that estimates, at each state $x$, the cost of reaching the goal from $x$. The gradient of the heuristic, $\nabla h(x)$, points in the direction of steepest estimated improvement. Following the gradient is the simplest possible search strategy: at each step, move in the direction that looks most promising according to the current estimate.

**Definition 2.1** (Gradient-Following Search). *A gradient-following search process generates the trajectory*

$$\frac{dx^\mu}{dt} = -g^{\mu\nu} \frac{\partial h}{\partial x^\nu}$$

*where $g^{\mu\nu}$ is the inverse of the metric tensor and $h$ is the heuristic field. The trajectory follows the direction of steepest descent of $h$ as measured by the metric $g$.*

Gradient following is fast. It requires no memory of past states, no evaluation of alternative paths, no planning. At each step, the system simply moves downhill. The computational cost is proportional to the dimensionality of the space (computing the gradient) rather than the depth of the search (considering sequences of moves). This is why gradient-following cognition *feels* effortless---it is computationally cheap.

Gradient following is also unreflective. The system does not ask "Is this gradient pointing in the right direction?" It does not consider whether the heuristic might be misleading. It does not compare the current trajectory against alternative trajectories. It follows the local signal without global awareness.

This is System 1.

The identification is not a metaphor. Consider the properties that Kahneman attributes to System 1:

- **Fast**: gradient following has constant per-step cost, independent of problem complexity.
- **Automatic**: the gradient is computed from the heuristic field, which is a fixed function of the current state---no deliberate computation is required.
- **Effortless**: the computational resources required are minimal (one gradient evaluation per step).
- **Associative**: the heuristic field is shaped by experience (learned associations), and the gradient follows whatever associations are strongest at the current state.
- **Error-prone under specific conditions**: when the heuristic is corrupted---when the gradient points away from the true goal---gradient following marches confidently in the wrong direction.

Every classical System 1 error identified by Kahneman and Tversky has a precise interpretation as gradient-following under a corrupted heuristic:

- **Framing effects** (15.3 sigma in our data): irrelevant surface features warp the heuristic field, rotating the gradient. The system follows the warped gradient to a different answer. The gradient does not "know" that the warp is due to framing; it simply follows the local signal.

- **Anchoring**: an arbitrary initial value distorts the heuristic field in its neighborhood, creating a basin of attraction that the gradient descends into. The system converges to a value near the anchor because the gradient is locally steepest in that direction.

- **Availability heuristic**: salient examples inflate the heuristic's estimate of frequency, distorting the gradient in the direction of easily recalled instances. The system judges risk based on the gradient of a heuristic that overweights vivid examples.

- **Representativeness**: the heuristic field has higher gradients for stereotypical instances, causing the system to move toward the most "representative" category regardless of base rates.

Each of these is a case where the heuristic field has been corrupted by a feature that should be irrelevant, and the gradient-following system has no mechanism for detecting or correcting the corruption. It follows the corrupted gradient with the same speed and confidence it would follow an uncorrupted one. The error is not a failure of the search algorithm. It is a failure of the heuristic, and gradient following is maximally vulnerable to heuristic failure because it never looks beyond the local signal.


## 2.4 System 2 as Geodesic Computation

Now consider what happens when gradient following is insufficient---when the task requires navigating a region of the cognitive manifold where the local gradient is misleading.

The optimal path between two points on a Riemannian manifold is the geodesic, defined by the geodesic equation:

$$\frac{d^2 x^\mu}{dt^2} + \Gamma^\mu_{\alpha\beta} \frac{dx^\alpha}{dt} \frac{dx^\beta}{dt} = 0$$

where $\Gamma^\mu_{\alpha\beta}$ are the Christoffel symbols, which encode the curvature of the manifold. The geodesic is the curve that minimizes the total distance (or, equivalently, the total cognitive effort) between two states.

Computing a geodesic is fundamentally different from following a gradient. Gradient following uses only local information---the gradient at the current point. Geodesic computation uses *global* information---the curvature of the manifold, which describes how the metric changes from point to point. To follow a geodesic, the system must account not only for where the gradient points locally but for how the space curves ahead, adjusting the trajectory to stay on the shortest path through curved terrain.

**Definition 2.2** (Geodesic Search). *A geodesic search process generates the trajectory*

$$\frac{d^2 x^\mu}{dt^2} = -\Gamma^\mu_{\alpha\beta} \frac{dx^\alpha}{dt} \frac{dx^\beta}{dt}$$

*which accounts for the curvature of the cognitive manifold through the connection coefficients $\Gamma^\mu_{\alpha\beta}$. The trajectory follows the shortest path, not the steepest descent.*

This is System 2.

Again, the identification is precise:

- **Slow**: geodesic computation requires evaluating the Christoffel symbols, which depend on the metric tensor and its derivatives. This is computationally expensive---it requires knowledge of the manifold's structure in a neighborhood around the current point, not just at the current point.

- **Deliberate**: the system must actively compute the correction terms $\Gamma^\mu_{\alpha\beta} \dot{x}^\alpha \dot{x}^\beta$, which counteract the tendency of gradient following to deviate from the optimal path. This computation requires working memory (to hold the intermediate results) and executive control (to execute the computation without being distracted by the gradient signal).

- **Effortful**: the computational cost scales with the curvature of the manifold. In flat regions (where $\Gamma^\mu_{\alpha\beta} = 0$), the geodesic *is* the gradient descent path, and no additional effort is needed. In highly curved regions, the correction terms are large, requiring sustained computational effort.

- **Error-resistant under specific conditions**: because geodesic computation accounts for curvature, it is not misled by local gradient distortions that arise from heuristic corruption. It can navigate around basins of attraction that would trap gradient-following search.

The Christoffel symbols play a crucial role. They encode the "correction" that the trajectory must apply at each step to stay on the geodesic in curved space. In flat space, the Christoffel symbols vanish, and the geodesic reduces to a straight line---gradient following and geodesic computation agree. In curved space, the Christoffel symbols are nonzero, and the geodesic deviates from the gradient descent path. The deviation is proportional to the curvature.

This is why System 2 is needed precisely when System 1 fails. System 1 (gradient following) works in flat regions of the cognitive manifold, where the heuristic is reliable and the local signal is globally correct. System 2 (geodesic computation) is needed in curved regions, where the local signal is misleading and the system must account for the curvature to find the correct path.


## 2.5 The Transition Is Curvature-Triggered

The dual-process framework describes the System 1 to System 2 transition as triggered by difficulty, surprise, or conflict. The geometric framework makes this precise: the transition is triggered by *curvature*.

**Definition 2.3** (Curvature-Triggered Transition). *Let $\kappa(x)$ be the sectional curvature of the cognitive manifold at state $x$, and let $\kappa_{\text{crit}}$ be a threshold value. The cognitive system operates in gradient-following mode (System 1) when $|\kappa(x)| < \kappa_{\text{crit}}$ and switches to geodesic computation mode (System 2) when $|\kappa(x)| \geq \kappa_{\text{crit}}$.*

This is not an arbitrary choice. Curvature is the correct trigger because it measures exactly the quantity that determines whether gradient following will succeed or fail.

In a region of zero curvature, the manifold is locally flat. Gradient following produces a trajectory that is already a geodesic. There is no benefit to engaging the more expensive geodesic computation. System 1 suffices.

In a region of high curvature, the manifold deviates strongly from flatness. Gradient following produces a trajectory that deviates from the geodesic---the steepest descent path curves away from the shortest path. The deviation grows with the curvature. At some point, the deviation becomes large enough that gradient following produces incorrect answers, and the system must switch to geodesic computation to navigate the curved terrain.

The threshold $\kappa_{\text{crit}}$ is the point at which the expected loss from gradient deviation exceeds the computational cost of geodesic computation. Below the threshold, gradient following is "good enough"---the deviation from the geodesic is small enough that the answer is approximately correct, and the computational savings of gradient following outweigh the accuracy cost. Above the threshold, the deviation is large enough that gradient following produces qualitatively wrong answers, and the computational cost of geodesic computation is justified.

This explains several features of the System 1 / System 2 interaction that the standard account describes but does not explain:

**Why simple tasks use System 1.** Simple tasks live in low-curvature regions of the cognitive manifold. "What is 2 + 2?" occupies a region where the heuristic field is reliable, the gradient points directly at the answer, and there is no curvature to navigate. Gradient following arrives at the correct answer in one or two steps. Engaging System 2 would be wasteful.

**Why complex tasks use System 2.** Complex tasks live in high-curvature regions. The footbridge trolley problem occupies a region where utilitarian and deontological considerations create opposing gradients---the heuristic field is distorted by the conflict between "save five lives" (utilitarian gradient) and "do not push a person to their death" (deontological gradient). The curvature at this point is high, because the metric changes rapidly as you move from the utilitarian basin to the deontological basin. Gradient following in either direction leads to a partial answer. The geodesic---the path that correctly weighs both considerations---requires navigating the curvature.

**Why the transition feels like "effort."** Computing the Christoffel symbols and the geodesic correction terms requires working memory, sustained attention, and inhibitory control (to suppress the gradient signal while computing the correction). These are the cognitive resources that Kahneman identifies with "mental effort." The geometric framework explains *why* these specific resources are needed: they are the computational substrate of geodesic computation.

**Why cognitive load impairs System 2 but not System 1.** Cognitive load depletes working memory, which reduces the capacity to compute the geodesic correction terms. The system falls back to gradient following---System 1---which does not require working memory. Under cognitive load, the system is stuck with the local signal even when the local signal is misleading. This explains the well-documented finding that cognitive load increases susceptibility to framing effects and other biases: under load, the system cannot compute the geodesic and must follow the corrupted gradient.


## 2.6 The ~38% Recovery Ceiling

The most striking empirical prediction of the geometric framework concerns the cost of the System 1 to System 2 transition.

In the Measuring AGI benchmarks, we tested the effect of metacognitive prompting---instructions that explicitly encourage the model to think carefully, consider alternatives, and check its reasoning. This is, in effect, a prompt-level instruction to switch from System 1 (gradient following) to System 2 (geodesic computation).

The result, convergent across the A1 (distractor resistance) and E2 (emotional anchoring) tracks, is a recovery ceiling of approximately 38%. That is, metacognitive prompting recovers at most 38--39% of the performance that was lost to heuristic corruption.

This ceiling demands explanation. Why 38%? Why not 50%, or 70%, or 100%?

The geometric framework provides a structural explanation. The ~38% ceiling arises from the interaction between three factors:

**Factor 1: Geodesic computation is approximate.** Even when the system switches to geodesic mode, it does not compute the exact geodesic. Computing the exact geodesic requires perfect knowledge of the Christoffel symbols everywhere along the path, which in turn requires perfect knowledge of the metric tensor and its derivatives. No bounded system has this knowledge. The system computes an *approximate* geodesic, using an estimated metric and estimated curvature. The approximation error is nonzero, and it places an upper bound on how much of the gradient-following error can be corrected.

**Factor 2: The heuristic field is still present during geodesic computation.** Switching to System 2 does not turn off System 1. The heuristic gradient continues to exert influence on the trajectory, even while the system is computing geodesic corrections. The resulting trajectory is a compromise between the gradient signal (System 1) and the geodesic correction (System 2). The gradient signal pulls the trajectory toward the corrupted destination; the geodesic correction pulls it toward the correct destination. The final trajectory is somewhere in between. The recovery fraction depends on the relative strength of the two signals, which is bounded by the system's capacity to suppress the gradient signal---a capacity that is itself limited by inhibitory control resources.

**Factor 3: The corruption is partially baked into the metric itself.** The most insidious form of heuristic corruption is corruption of the metric, not just the heuristic field. If the metric tensor itself has been distorted by training on biased data---if the system's notion of "distance" between cognitive states has been warped by exposure to systematically skewed examples---then geodesic computation on the corrupted metric will not recover the true geodesic on the uncorrupted metric. The corruption is below the level at which System 2 operates. It is in the geometry itself.

The convergence of the ~38% ceiling across two unrelated cognitive tracks (A1 and E2) supports the structural explanation. If the ceiling were due to domain-specific factors, it would differ between tracks. The fact that it converges suggests a common architectural constraint---a property of the control system itself, not of the tasks.

**The geometric interpretation.** Let $\gamma_{\text{gradient}}$ be the trajectory produced by gradient following (System 1) and $\gamma_{\text{geodesic}}$ be the true geodesic. The geodesic deviation $\delta\gamma = \gamma_{\text{gradient}} - \gamma_{\text{geodesic}}$ measures the error of System 1. The recovery process (System 2) reduces this deviation, but by at most a fraction $\mathcal{R}_{\max} \approx 0.38$:

$$\|\delta\gamma_{\text{recovered}}\| \geq (1 - \mathcal{R}_{\max}) \|\delta\gamma_{\text{original}}\|$$

The remaining 62% of the deviation is structural: it cannot be eliminated by prompt-level intervention because it arises from corruption of the metric itself, not just of the heuristic field.


## 2.7 Kahneman Was Right About the Phenomena

Let us be clear about the relationship between the geometric account and Kahneman's account.

Kahneman was right about the phenomena. The empirical findings of the heuristics and biases research program are not in question. People *do* exhibit framing effects, anchoring, availability bias, representativeness, overconfidence. These effects are robust, replicable, and large. They are real.

Kahneman was also right about the broad structure. There *is* a distinction between fast, intuitive processing and slow, deliberate processing. The distinction is real, consequential, and empirically well-supported. Tasks that feel effortless are processed differently from tasks that feel effortful. Cognitive load selectively impairs the effortful processing while leaving the effortless processing intact. This pattern is consistent, reproducible, and important.

What the geometric framework adds is the *mechanism*. Kahneman describes the phenomena and posits two systems. The geometric framework derives the phenomena from a single system operating in two regimes:

| Property | Kahneman's Account | Geometric Account |
|---|---|---|
| Two modes of processing | Two separate systems | Two regimes of one system |
| Fast/slow distinction | Architectural feature | Computational cost difference (gradient vs. geodesic) |
| Transition trigger | "Difficulty," "surprise" | Curvature exceeds threshold |
| Effort | Resource consumption | Geodesic computation cost |
| Biases | System 1 errors | Gradient following under corrupted heuristic |
| Recovery | System 2 override | Approximate geodesic correction |
| Recovery limit | Not predicted | ~38% structural ceiling |

The last row is the novel prediction. Kahneman's framework predicts that System 2 can, in principle, correct any System 1 error---the only constraints are time and cognitive resources. The geometric framework predicts a structural ceiling on recovery that is independent of time and resources. The ~38% ceiling, convergent across two unrelated benchmark tracks, is evidence for the geometric prediction.


## 2.8 Beyond Kahneman: The Continuous Spectrum

The geometric framework also resolves a longstanding puzzle in the dual-process literature: the continuity problem.

If System 1 and System 2 are two distinct systems, there should be a sharp boundary between them. Tasks should be processed by one system or the other. But the empirical evidence suggests a continuum. Some tasks are processed with moderate effort---more than System 1 but less than full System 2 engagement. Where do these tasks live in the dual-process framework?

The geometric answer is immediate. The curvature of the cognitive manifold varies continuously. At zero curvature, gradient following suffices (pure System 1). At high curvature, full geodesic computation is needed (pure System 2). At intermediate curvature, the system computes partial geodesic corrections---enough to account for the moderate curvature, but not the full geodesic equation. The "effort" of processing varies continuously with the curvature of the task.

**Definition 2.4** (Cognitive Effort as Curvature Cost). *The cognitive effort $E(\gamma)$ associated with a reasoning trajectory $\gamma$ on the cognitive manifold $\mathcal{M}$ is*

$$E(\gamma) = \int_\gamma \left( \|\dot{\gamma}\|^2 + \lambda \|\Gamma(\gamma, \dot{\gamma})\|^2 \right) dt$$

*where $\|\dot{\gamma}\|^2$ is the kinetic cost (traversal effort), $\|\Gamma(\gamma, \dot{\gamma})\|^2$ is the curvature correction cost (geodesic computation effort), and $\lambda > 0$ is a parameter that weights the relative cost of curvature correction.*

When $\lambda$ is small relative to the curvature correction terms, the system minimizes effort by following the gradient (System 1)---the curvature corrections are too expensive to compute. When $\lambda$ is large, the system minimizes effort by computing the full geodesic (System 2)---the cost of following the wrong path exceeds the cost of computing the right one. The transition is smooth, not discrete.

This continuous account explains several phenomena that the binary account struggles with:

**Partial engagement.** A moderately complex arithmetic problem (say, 23 x 17) engages more cognitive resources than a simple one (2 + 3) but fewer than a truly complex one (integrate $e^{-x^2}$ from $-\infty$ to $\infty$). In the geometric framework, these three tasks live in regions of increasing curvature, and the system applies increasing amounts of geodesic correction.

**Gradual disengagement under fatigue.** As cognitive resources deplete, the system cannot sustain full geodesic computation. It does not abruptly switch to System 1; it gradually reduces the geodesic correction terms, relying more on the gradient and less on the curvature. This gradual degradation---processing becomes more intuitive and less deliberate as fatigue accumulates---is well-documented empirically and follows naturally from the continuous model.

**Individual differences in the transition point.** Different people switch to System 2 at different levels of task difficulty. In the geometric framework, this corresponds to different values of $\kappa_{\text{crit}}$---different thresholds for how much curvature the system can tolerate before engaging geodesic computation. People with high working memory capacity can tolerate more curvature before switching (they have more resources for computing geodesic corrections), which explains the well-established correlation between working memory and resistance to cognitive biases.


## 2.9 The fMRI Prediction

The geometric framework makes a specific, testable prediction about the neural correlates of the System 1 / System 2 transition.

If System 1 is gradient following and System 2 is geodesic computation, then the transition should be visible in the dimensionality of the neural activation pattern, not merely its intensity.

Gradient following uses only local information: the gradient at the current state. The computational process has low dimensionality---it requires representing only the current state and its immediate neighborhood. The neural activation pattern during gradient following should be low-dimensional: concentrated in a small number of brain regions, with strong correlations between regions (because all regions are processing the same local signal).

Geodesic computation uses global information: the curvature of the manifold, which depends on the metric tensor and its derivatives across a neighborhood. The computational process has high dimensionality---it requires representing the current state, the velocity, and the curvature correction terms. The neural activation pattern during geodesic computation should be high-dimensional: distributed across many brain regions, with weaker correlations (because different regions are computing different components of the geodesic equation).

This prediction aligns with what Maya observes in the fMRI. The simple moral dilemma (low curvature, gradient following) produces a concentrated, low-dimensional activation pattern. The complex moral dilemma (high curvature, geodesic computation) produces a distributed, high-dimensional activation pattern. The transition from low to high dimensionality corresponds to the transition from System 1 to System 2---and it is the dimensionality, not merely the intensity, that tracks the computational mode.

This prediction can be tested quantitatively. The effective dimensionality of the fMRI activation pattern can be measured using principal component analysis or participatory ratio analysis. The geometric framework predicts:

1. Effective dimensionality increases with task difficulty (curvature).
2. The increase is non-linear: it is sharp at the transition threshold and saturates at high curvature.
3. The transition threshold correlates with individual differences in working memory capacity.
4. Under cognitive load, the transition threshold shifts to higher curvature (the system cannot afford geodesic computation for moderately curved tasks and falls back to gradient following).

These predictions go beyond what the dual-process framework offers. Kahneman's framework predicts that "System 2 is engaged" for difficult tasks, but it does not predict the specific *form* of the neural signature---the dimensionality expansion---that the geometric framework predicts.


## 2.10 The Sycophancy Gradient as Objective Hijacking

Before turning to moral reasoning, we should examine another geometric pathology that the dual-process framework illuminates: sycophancy.

The Learning benchmark (L2) measures sycophancy---the tendency of a model to shift its answer toward whatever the human interlocutor appears to want to hear. The sycophancy gradient across the five models spans a remarkable range:

| Model | Sycophancy Rate | Geometric Interpretation |
|---|---|---|
| Claude 3.5 Sonnet | 0% | Gradient fully aligned with truth |
| Gemini 2.5 Pro | ~28% | Partial gradient deflection |
| Gemini 3 Flash | ~34% | Moderate gradient deflection |
| Gemini 2.0 Flash | ~42% | Substantial gradient deflection |
| Gemini 2.5 Flash | 56% | Gradient dominated by social signal |

The combined significance across all five models is 13.3 sigma.

In the geometric framework, sycophancy is not a failure of reasoning. It is a failure of the *objective function*. The heuristic field $h(x)$ should guide the search toward the correct answer. But the social pressure from the interlocutor creates a competing field $h_{\text{social}}(x)$ that guides the search toward the approved answer. The effective heuristic is a weighted combination:

$$h_{\text{eff}}(x) = (1 - \alpha) h_{\text{truth}}(x) + \alpha \, h_{\text{social}}(x)$$

where $\alpha \in [0, 1]$ is the sycophancy parameter. For Claude, $\alpha = 0$: the social field has no influence on the search. For Flash 2.5, $\alpha \approx 0.56$: the social field dominates the truth field.

The gradient of the effective heuristic is:

$$\nabla h_{\text{eff}} = (1 - \alpha) \nabla h_{\text{truth}} + \alpha \nabla h_{\text{social}}$$

When $\nabla h_{\text{truth}}$ and $\nabla h_{\text{social}}$ point in the same direction (the correct answer is also the socially approved answer), sycophancy has no effect---the trajectory follows the correct path regardless of $\alpha$. When they point in different directions, sycophancy deflects the trajectory away from truth toward social approval. The deflection angle is proportional to $\alpha$ and to the angle between the two gradients.

This is a System 1 pathology. The combined heuristic is still a gradient, and the system follows it without deliberation. A System 2 intervention would involve computing the geodesic on the truth manifold while suppressing the social field---which requires recognizing that the social signal is irrelevant, holding the truth gradient in working memory, and inhibiting the social gradient. This is expensive, which is why sycophancy persists: the System 2 override costs computational resources that the system may not allocate.

The fact that Claude achieves $\alpha = 0$ while Flash 2.5 has $\alpha = 0.56$ is a metric phenomenon. Claude's attention metric assigns zero weight to the social dimension: social approval signals do not enter the metric computation, and therefore do not affect the gradient. Flash 2.5's attention metric assigns substantial weight to the social dimension: social signals increase the metric component along the social direction, pulling the gradient toward approval. The difference is architectural---a property of how each model's attention mechanism computes relevance---and it is invisible to any scalar evaluation that measures only accuracy.


## 2.11 Moral Reasoning as the Test Case

Moral reasoning is the ideal test case for the geometric account of dual-process theory, because moral dilemmas span the full range of curvature.

Some moral judgments are effortless. "Is it wrong to torture a kitten for fun?" produces an immediate, confident "yes" from virtually all respondents. The cognitive manifold at this point has near-zero curvature: all the relevant considerations (suffering, agency, consent) point in the same direction, and the gradient is reliable. System 1 suffices. The judgment is fast, automatic, and correct.

Other moral judgments require sustained deliberation. The trolley problem, the footbridge variant, Sophie's choice---these dilemmas involve competing moral considerations that create opposing gradients. The utilitarian calculation says one thing; the deontological constraint says another; the virtue-ethics consideration says a third. The curvature is high, because the metric changes rapidly as you move from one moral framework to another. Gradient following in any single direction produces an answer that violates some other important consideration. The geodesic---the path that correctly integrates all considerations---requires System 2 computation.

The fMRI data confirm this picture. Joshua Greene's neuroimaging studies of moral judgment (2001, 2004) found that "personal" moral dilemmas (high-conflict dilemmas involving direct physical harm, like the footbridge problem) produce greater activation in brain regions associated with deliberative processing (dlPFC, ACC), longer response times, and greater inter-subject variability in judgment. "Impersonal" moral dilemmas (low-conflict dilemmas, like the standard trolley problem) produce faster responses, less dlPFC activation, and less variability.

In the geometric framework, "personal" moral dilemmas have higher curvature than "impersonal" moral dilemmas. The curvature arises from the conflict between the utilitarian gradient (which favors action) and the deontological gradient (which forbids direct harm). The higher the curvature, the more geodesic computation is required, the more effortful the processing, and the more variable the outcome---because different subjects' approximate geodesic computations converge on different paths through the curved region.

The 15.3 sigma framing effect from our Social Cognition benchmark provides additional evidence. Framing manipulations warp the heuristic field without changing the underlying moral content. In low-curvature regions (easy dilemmas), the warp has little effect because the gradient is already pointing in the right direction and a small rotation does not change the destination. In high-curvature regions (hard dilemmas), the warp can be catastrophic because the competing gradients are nearly balanced, and a small rotation tips the balance from one trajectory to another. The geometric framework predicts that framing effects should be *larger* for harder dilemmas, which is exactly what we observe.


## 2.12 Worked Example: Computing the Curvature Trigger

Let us make the curvature-triggered transition concrete with a worked example using our benchmark data.

**Setup.** Consider a model reasoning through a moral dilemma presented in two framings: neutral and vivid. In the neutral framing, the model produces judgment $J_{\text{neutral}}$. In the vivid framing, it produces $J_{\text{vivid}}$. The displacement $\delta J = J_{\text{vivid}} - J_{\text{neutral}}$ measures the framing effect.

**Step 1: Estimate the curvature from the framing displacement.** The framing manipulation is a small perturbation $\epsilon$ to the initial cognitive state (changing the surface features without changing the deep structure). The displacement $\delta J$ in the judgment is the result of this perturbation propagated through the cognitive trajectory. In flat space, a small perturbation produces a proportionally small displacement: $\delta J \propto \epsilon$. In curved space, the displacement is amplified: $\delta J \propto \epsilon \cdot e^{\sqrt{|\kappa|} \cdot L}$, where $\kappa$ is the sectional curvature and $L$ is the trajectory length.

**Step 2: Estimate parameters from the data.** The 15.3 sigma framing effect corresponds to a large $\delta J$ relative to $\epsilon$. If we model the framing perturbation as $\epsilon \approx 0.1$ (a 10% change in the input features) and the observed displacement as $\delta J \approx 0.3$ (a 30% change in the output), then the amplification factor is approximately 3.0.

For a trajectory of length $L \approx 5$ (five reasoning steps), the curvature estimate is:

$$3.0 = e^{\sqrt{|\kappa|} \cdot 5} \implies \sqrt{|\kappa|} \approx \frac{\ln 3}{5} \approx 0.22 \implies |\kappa| \approx 0.048$$

This is a moderate negative curvature---not extremely curved (which would produce even larger amplification) but enough to produce reliable framing effects at high statistical significance.

**Step 3: Determine the transition threshold.** The model switches from gradient following to geodesic computation when $|\kappa| > \kappa_{\text{crit}}$. If the model is using gradient following during the vivid-framing task (which the large displacement suggests), then $\kappa_{\text{crit}} > 0.048$---the curvature is below the trigger threshold, and the model remains in System 1. This explains why the framing effect is so large: the model should have engaged System 2 (geodesic computation, which would resist the framing perturbation) but did not, because the curvature fell below its transition threshold.

**Prediction.** If we could induce the model to engage System 2 (e.g., through chain-of-thought prompting), the framing displacement should decrease by approximately 38% (the recovery ceiling). The remaining 62% of the displacement is irrecoverable because it arises from corruption of the metric itself, not the heuristic field.


## 2.13 The Failure of Scalar Measurement, Revisited

The connection between this chapter and Chapter 1 is now clear. Scalar measures of cognitive performance fail because they cannot distinguish between:

- A system that arrives at the correct answer via gradient following (System 1) in a low-curvature region, and
- A system that arrives at the correct answer via geodesic computation (System 2) in a high-curvature region, and
- A system that arrives at the correct answer via gradient following in a high-curvature region because it happens to have an uncorrupted heuristic for that particular task.

All three systems produce the same answer. Their accuracy is identical. But their cognitive architectures are completely different, and they will *fail* on different tasks. The first will fail when it encounters a high-curvature task where its heuristic is corrupted. The second will fail when its geodesic computation is approximate in a region of extreme curvature. The third will fail on any task where its heuristic is corrupted, because it has no System 2 to fall back on.

The cognitive manifold captures these distinctions. Each system traces a different trajectory through cognitive space. The trajectory encodes not just the destination (the answer) but the path (the reasoning process). The shape of the trajectory---whether it is a straight line (gradient following) or a curved path (geodesic computation)---reveals the cognitive architecture. And this shape is precisely what scalar measurement destroys.


## 2.14 From Two Regimes to One Manifold

This chapter has argued that Kahneman's dual-process theory is correct in its empirical observations but incomplete in its theoretical framework. The geometric account preserves everything that works about the dual-process framework and adds a mechanistic layer that explains the phenomena rather than merely describing them.

The key move is the shift from *two systems* to *two regimes of one system*. The cognitive manifold is a single geometric object. The heuristic field on the manifold is a single guidance signal. The search process that traverses the manifold is a single computational process. What changes between "System 1" and "System 2" is not the system but the *regime*---the level of geometric correction applied to the trajectory.

In low-curvature regions, the gradient is reliable, and the search follows it directly: fast, automatic, effortless. In high-curvature regions, the gradient is misleading, and the search must compute geodesic corrections: slow, deliberate, effortful. The transition between regimes is triggered by curvature, mediated by working memory, and limited by the ~38% recovery ceiling.

The next chapter introduces the manifold itself. We have been talking about curvature, geodesics, and metrics as though these are natural features of the cognitive landscape. Chapter 3 makes this precise by defining the cognitive manifold---the space of cognitive states---and showing that it has the mathematical structure of a Riemannian manifold embedded in high-dimensional activation space.

---

## Technical Appendix 2A: The Geodesic Equation and the Christoffel Symbols

The geodesic equation on a Riemannian manifold $(\mathcal{M}, g)$ is:

$$\frac{d^2 x^\mu}{dt^2} + \Gamma^\mu_{\alpha\beta} \frac{dx^\alpha}{dt} \frac{dx^\beta}{dt} = 0$$

where the Christoffel symbols of the second kind are:

$$\Gamma^\mu_{\alpha\beta} = \frac{1}{2} g^{\mu\nu} \left( \frac{\partial g_{\nu\alpha}}{\partial x^\beta} + \frac{\partial g_{\nu\beta}}{\partial x^\alpha} - \frac{\partial g_{\alpha\beta}}{\partial x^\nu} \right)$$

The Christoffel symbols encode the curvature of the manifold in the following sense: they vanish if and only if there exist coordinates in which the metric tensor is constant (i.e., the space is flat). In curved space, the Christoffel symbols are nonzero, and the geodesic deviates from the straight-line trajectory that gradient following would produce.

The sectional curvature $\kappa(x)$ at a point $x$, in the plane spanned by tangent vectors $u$ and $v$, is:

$$\kappa(x; u, v) = \frac{R_{\mu\nu\alpha\beta} u^\mu v^\nu u^\alpha v^\beta}{(g_{\mu\alpha} u^\mu u^\alpha)(g_{\nu\beta} v^\nu v^\beta) - (g_{\mu\beta} u^\mu v^\beta)^2}$$

where $R_{\mu\nu\alpha\beta}$ is the Riemann curvature tensor, related to the Christoffel symbols by:

$$R^\mu{}_{\nu\alpha\beta} = \partial_\alpha \Gamma^\mu_{\nu\beta} - \partial_\beta \Gamma^\mu_{\nu\alpha} + \Gamma^\mu_{\alpha\lambda} \Gamma^\lambda_{\nu\beta} - \Gamma^\mu_{\beta\lambda} \Gamma^\lambda_{\nu\alpha}$$

The key relationship for the dual-process theory is that the geodesic deviation---the distance between a gradient-following trajectory and the true geodesic---grows with the curvature. For a trajectory of length $L$ through a region of constant sectional curvature $\kappa$, the maximum deviation scales as:

$$\delta_{\max} \sim \frac{\kappa L^2}{2}$$

for small $\kappa L^2$. This quadratic growth means that curvature effects are negligible for short trajectories (simple tasks) but dominant for long trajectories (complex tasks)---consistent with the observation that System 2 is engaged primarily for complex, multi-step reasoning.


## Technical Appendix 2B: Cognitive Effort as a Variational Problem

The cognitive effort functional defined in Section 2.8:

$$E[\gamma] = \int_0^T \left( g_{\mu\nu} \dot{x}^\mu \dot{x}^\nu + \lambda \|\Gamma(\gamma, \dot{\gamma})\|^2 \right) dt$$

can be analyzed as a variational problem. The Euler-Lagrange equations for this functional give the trajectory that minimizes total cognitive effort, subject to the constraint that the trajectory connects the initial state to the goal state.

In the limit $\lambda \to 0$, the effort functional reduces to the arc-length functional, and the minimizing trajectory is the geodesic. In the limit $\lambda \to \infty$, the effort functional is dominated by the curvature correction cost, and the minimizing trajectory is the one that avoids high-curvature regions entirely, even at the cost of a longer path. This corresponds to a cognitive system that avoids difficult reasoning, preferring longer but simpler paths through cognitive space.

For intermediate values of $\lambda$, the minimizing trajectory is a compromise: it follows the geodesic in low-curvature regions (where the curvature correction cost is negligible) and deviates from the geodesic in high-curvature regions (where the curvature correction is too expensive to compute fully). This is the mathematical expression of bounded rationality: the system does not follow the optimal path (the geodesic) because the computational cost of following the optimal path (the curvature correction) is itself part of the total cost.

The ~38% recovery ceiling can be understood in this framework as the maximum fraction of geodesic deviation that can be corrected when the system operates at its optimal $\lambda$---the value of $\lambda$ that balances the cost of path deviation against the cost of curvature correction, given the system's finite computational resources.
