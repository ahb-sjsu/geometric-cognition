# Chapter 12: The Dual Process Theory, Geometrized

> *"Thinking is the hardest work there is, which is probably the reason so few engage in it."*
> --- Henry Ford, attributed (c. 1929)

---

> **RUNNING EXAMPLE --- MAYA'S MODEL**
>
> Maya is watching two regimes collide.
>
> She has designed an experiment that no one in the dual-process literature has attempted before. Her subjects --- thirty-two undergraduates and four language models --- are evaluating moral dilemmas that vary systematically in what she calls *curvature load*: the degree to which the scenario presents conflicting moral dimensions that resist simple resolution.
>
> At the low-curvature end, the scenarios are straightforward. A neighbor's dog repeatedly destroys your garden. You ask the neighbor to keep the dog leashed. There is one salient harm dimension (property damage), one clear responsible party (the neighbor), and one obvious action (request containment). The moral landscape is flat. The gradient points in a single, unambiguous direction.
>
> At the high-curvature end, the scenarios are wrenching. A single mother discovers that her terminally ill child's experimental treatment is being funded by her estranged father, who earned the money through a fraud that destroyed several families' savings. Accepting the money saves the child. Refusing it is a death sentence. Reporting the fraud destroys the funding. The moral landscape is violently curved: the harm dimensions (physical, financial, autonomy, trust) point in contradictory directions, and every trajectory toward resolving one dimension worsens another.
>
> Maya varies curvature load across five levels, from flat (one salient harm dimension, no conflicts) to extreme (four or more conflicting harm dimensions with no dominant resolution). At each level, she measures three things: response latency (how long the subject deliberates), fMRI activation in the dorsolateral prefrontal cortex (dlPFC, associated with deliberate reasoning), and the dimensionality of the reasoning trajectory (estimated from the fMRI time series via PCA).
>
> The human results are stunning in their clarity.
>
> At curvature levels 1 and 2 (flat to mild), response latencies average 4.2 seconds. The dlPFC activation is at baseline. The reasoning trajectory is low-dimensional --- typically 1 to 2 principal components capture 85% of the variance. The subjects are following the gradient. They see the obvious answer, and they take it. This is System 1.
>
> At curvature level 3 (moderate), something changes. Response latencies jump to 11.7 seconds --- nearly triple. The dlPFC activation spikes. The trajectory dimensionality jumps to 3--4 components. The subjects are no longer following the gradient. They are computing geodesics --- tracing paths through the curved moral landscape that account for the conflicting harm dimensions. This is System 2.
>
> The transition is not gradual. It is a phase shift. Maya plots response latency against curvature load and sees a sigmoid: flat at low curvature, steep at moderate curvature, flattening again at high curvature (where the subjects have fully committed to deliberate processing). The inflection point --- the curvature threshold at which System 1 gives way to System 2 --- is remarkably consistent across subjects, occurring at a curvature load that corresponds to approximately three conflicting harm dimensions.
>
> Then she turns to the language models. She feeds the same scenarios, at the same five curvature levels, to Claude, Flash 3, Pro, and Flash 2.5. She measures response length (the analogue of response latency), chain-of-thought complexity (the analogue of trajectory dimensionality), and verdict stability across replications (the analogue of confidence).
>
> The models show the same phase transition.
>
> At low curvature, responses are short and confident. At high curvature, responses are long, multi-branched, and less stable. The transition point is model-specific: Claude transitions early (it engages deliberate processing at lower curvature, consistent with its narrow-channel profile from Chapter 10), while Flash 2.0 transitions late (it follows the gradient longer before switching, consistent with its adaptive-baseline profile). But every model transitions. The dual-process structure is not a human peculiarity. It is a geometric inevitability.
>
> Maya writes: *"System 1 and System 2 are not two systems. They are two regimes of a single geometric process, separated by a curvature threshold. Every cognitive system --- biological or artificial --- that navigates a manifold with variable curvature will exhibit this transition. The dual-process theory is not a psychological hypothesis. It is a theorem of geometric cognition."*

---

## 12.1 The Dual-Process Framework: A Brief History

Daniel Kahneman's *Thinking, Fast and Slow* (2011) popularized a distinction that had been developing in cognitive psychology for decades: the idea that human cognition operates in two fundamentally different modes.

**System 1** is fast, automatic, effortless, and heuristic-driven. It is the mode that lets you recognize a friend's face in a crowd, complete the phrase "bread and ___," or swerve to avoid a suddenly appearing obstacle. System 1 operates below conscious awareness. It produces answers --- often correct ones --- without the thinker being able to articulate how the answer was reached.

**System 2** is slow, deliberate, effortful, and rule-governed. It is the mode that lets you compute 17 x 24, plan a route through an unfamiliar city, or evaluate the logical validity of a syllogism. System 2 requires conscious attention. It produces answers through a process the thinker can (at least partially) introspect on and articulate.

The dual-process framework has been enormously influential. It organizes a vast body of experimental findings --- from the anchoring effect (Tversky & Kahneman, 1974) to the base rate neglect (Kahneman & Tversky, 1973) to the framing effect (Tversky & Kahneman, 1981) --- under a single explanatory umbrella. The cognitive biases that fill behavioral economics textbooks are, in this framework, cases where System 1 produces a quick answer that System 2 fails to override.

But the framework has always had a structural problem. If System 1 and System 2 are genuinely different systems, where is the boundary between them? What determines when one system yields to the other? Why does the transition sometimes happen (you catch yourself making a mistake and recalculate) and sometimes not (you publish the mistake because it *felt* right)?

The standard answer is vague: System 2 is activated when System 1 encounters "difficulty" or "surprise." But difficulty and surprise are not defined independently of the dual-process framework itself, creating a circularity. What counts as difficult enough to trigger System 2? How is surprise quantified? Without answers to these questions, the dual-process framework is descriptive rather than explanatory. It names the two modes but cannot predict the transition between them.

The geometric framework resolves this circularity. It provides a precise, quantitative definition of what triggers the transition: **curvature**.


## 12.2 System 1 as Gradient Following

In the geometric framework developed in Chapters 3--6, reasoning is navigation on the cognitive manifold $\mathcal{M}$. The heuristic field $h(x)$ estimates the cost-to-go from each cognitive state $x$ to the goal state $x_{\text{goal}}$. The gradient of the heuristic field, $\nabla h(x)$, points in the direction of steepest descent --- the direction that most rapidly decreases the estimated distance to the goal.

**Definition 12.1** (Gradient-Following Regime). *A cognitive system is in the gradient-following regime at state $x$ if its next state is determined by:*

$$x_{t+1} = x_t - \eta \nabla h(x_t)$$

*where $\eta > 0$ is the step size and $\nabla h$ is the gradient of the heuristic field. The system moves in the direction that most rapidly decreases the estimated cost-to-go, without accounting for the curvature of the manifold.*

Gradient following is System 1, geometrized. Consider its properties:

**Fast.** Gradient following requires only local information --- the gradient at the current state. No trajectory planning, no search tree expansion, no consideration of alternative paths. The computation is a single vector operation: read the gradient, step in that direction. This is why System 1 is fast.

**Heuristic-dominated.** The trajectory depends entirely on the heuristic field $h(x)$. If the heuristic is good (the estimated cost-to-go is close to the true cost-to-go), gradient following produces a good trajectory. If the heuristic is biased (as we documented in Chapters 7--11), gradient following inherits the bias. This is why System 1 is susceptible to cognitive biases: the biases live in the heuristic field, and gradient following is enslaved to the heuristic field.

**Effortless.** The computational cost of gradient following is $O(d)$, where $d$ is the dimensionality of the manifold at the current state --- one gradient evaluation per step. The cost does not scale with the complexity of the problem, the distance to the goal, or the curvature of the path. This is why System 1 feels effortless: its computational cost is constant regardless of problem complexity.

**Unreflective.** Gradient following has no metacognitive component. The system does not evaluate how well it is navigating; it does not compare the estimated cost-to-go against any external standard; it does not consider whether the gradient might be misleading. This is why System 1 is unreflective: the algorithm has no provision for self-monitoring. It is pure forward motion.

**When does gradient following work?** When the manifold has low curvature. In a flat region of the cognitive manifold, the gradient points reliably toward the goal. The heuristic field is a good approximation to the true distance function, because the straight-line estimate (which is what the heuristic provides) is close to the geodesic distance (which is what the true distance requires). Low curvature means that the straight path and the curved path are nearly identical --- and gradient following follows the straight path.

This is the geometric content of "System 1 works well for familiar, simple problems." Familiar problems are familiar because the system has navigated similar manifold regions before, and the heuristic field in those regions has been calibrated by experience. Simple problems are simple because the manifold is locally flat --- the moral dimensions do not conflict, the considerations point in the same direction, the gradient is unambiguous.


## 12.3 System 2 as Geodesic Computation

When the manifold is curved, gradient following fails. The straight-line path diverges from the true shortest path. The heuristic's estimate of cost-to-go becomes inaccurate. The gradient points in the locally steepest direction, but that direction may be globally wrong --- like descending a hillside by always stepping in the steepest downhill direction, only to end up in a ravine that is separated from the valley floor by a ridge.

In curved regions, the system needs to compute *geodesics* --- the true shortest paths on the manifold, which account for curvature.

**Definition 12.2** (Geodesic-Computing Regime). *A cognitive system is in the geodesic-computing regime at state $x$ if its trajectory $\gamma(t)$ satisfies the geodesic equation:*

$$\frac{d^2 \gamma^\mu}{dt^2} + \Gamma^\mu_{\alpha\beta} \frac{d\gamma^\alpha}{dt} \frac{d\gamma^\beta}{dt} = 0$$

*where $\Gamma^\mu_{\alpha\beta}$ are the Christoffel symbols of the metric $g_{\mu\nu}$ on $\mathcal{M}$. The system computes the shortest path by accounting for the curvature of the manifold, not merely the local gradient.*

Geodesic computation is System 2, geometrized. Consider its properties:

**Slow.** Computing a geodesic requires solving a second-order differential equation. This requires knowledge not just of the gradient (first-order information) but of the curvature (second-order information) --- the Christoffel symbols, which encode how the metric varies across the manifold. The computation must integrate this information along the entire planned trajectory, not just at the current point. This is why System 2 is slow: it requires second-order information integrated over a path.

**Curvature-aware.** The geodesic equation explicitly accounts for the Christoffel symbols --- the curvature of the manifold. Where the manifold bends, the geodesic bends with it, maintaining the shortest path despite the curvature. This is why System 2 handles complex problems better than System 1: it can navigate curved regions where the gradient is misleading.

**Effortful.** The computational cost of geodesic computation is $O(d^2 \cdot L)$, where $d$ is the dimensionality and $L$ is the path length --- $d^2$ for the Christoffel symbol computation at each step (involving the metric tensor and its derivatives) and $L$ for the integration along the path. The cost scales quadratically with dimensionality and linearly with path length. This is why System 2 feels effortful: its computational cost grows with problem complexity.

**Reflective.** Geodesic computation naturally incorporates metacognitive monitoring. The integration along the path produces intermediate states that can be evaluated against the goal. The system can check whether the trajectory is converging, whether the curvature is as expected, whether the path length is consistent with the estimated cost-to-go. This is why System 2 supports introspection: the multi-step nature of the computation creates intermediate representations that the system can inspect.

**When does geodesic computation matter?** When the manifold has high curvature. In a flat region, the geodesic is a straight line and the gradient-following trajectory approximates it perfectly. The geodesic equation reduces to $d^2\gamma^\mu / dt^2 = 0$ (constant velocity in a straight line) when $\Gamma^\mu_{\alpha\beta} = 0$ (zero curvature). The expensive curvature computation adds nothing. But in a curved region, the difference between the gradient-following trajectory and the geodesic can be enormous. The straight path misses the curve; the gradient-following path gets trapped in local structure; the geodesic finds the true shortest route.


## 12.4 The Curvature-Triggered Transition

The key insight of the geometric dual-process theory is that the transition from System 1 to System 2 is not random, not based on "difficulty" (undefined), and not a conscious choice. It is triggered by a specific, measurable geometric quantity: the curvature of the cognitive manifold at the current state.

**Definition 12.3** (Curvature-Triggered Regime Transition). *Let $\kappa(x)$ be the scalar curvature of the cognitive manifold $\mathcal{M}$ at state $x$, and let $\kappa^*$ be the curvature threshold. The cognitive system operates in the gradient-following regime (System 1) when $\kappa(x) < \kappa^*$ and transitions to the geodesic-computing regime (System 2) when $\kappa(x) \geq \kappa^*$.*

The transition function is:

$$\text{Regime}(x) = \begin{cases} \text{Gradient following (System 1)} & \text{if } \kappa(x) < \kappa^* \\ \text{Geodesic computation (System 2)} & \text{if } \kappa(x) \geq \kappa^* \end{cases}$$

This is a precise, testable prediction. It says that the transition from fast, heuristic processing to slow, deliberate processing is governed by the local curvature of the manifold --- the degree to which the cognitive landscape bends at the current location. When the landscape is flat, gradient following suffices, and the system stays in System 1. When the landscape curves sharply, gradient following fails, the system detects the failure (or detects the curvature directly), and transitions to System 2.

The curvature threshold $\kappa^*$ is not a universal constant. It is a property of the individual cognitive system --- determined by the precision of the system's curvature detector, the computational resources available for geodesic computation, and the system's tolerance for suboptimal trajectories. A system with a low $\kappa^*$ (sensitive curvature detector, ample resources, low tolerance for error) transitions to System 2 early, engaging deliberate processing even for moderately curved problems. A system with a high $\kappa^*$ (insensitive detector, limited resources, high tolerance for error) stays in System 1 longer, relying on gradient following even when curvature is significant.

This individual variation in $\kappa^*$ maps directly onto known individual differences in cognitive style. The "need for cognition" scale (Cacioppo & Petty, 1982) measures individual differences in the tendency to engage in and enjoy effortful thinking. In the geometric framework, high need for cognition corresponds to a low $\kappa^*$: the system transitions to System 2 at lower curvature, engaging deliberate processing more readily. Low need for cognition corresponds to a high $\kappa^*$: the system stays in System 1 longer, relying on the gradient even when curvature is moderate.

The framework also explains the *smoothness* of the transition in practice. The sharp threshold in Definition 12.3 is a mathematical idealization. In biological systems, the transition is smooth --- a continuous mixture of gradient following and geodesic computation, weighted by the curvature:

$$\text{trajectory}(x) = (1 - \sigma(\kappa(x) - \kappa^*)) \cdot \nabla h(x) + \sigma(\kappa(x) - \kappa^*) \cdot \text{geodesic}(x)$$

where $\sigma$ is a sigmoid function that smoothly interpolates between the two regimes. At low curvature, $\sigma \approx 0$ and the trajectory is pure gradient following. At high curvature, $\sigma \approx 1$ and the trajectory is pure geodesic computation. At intermediate curvature, the system blends the two --- partly following the gradient, partly accounting for curvature. This blending corresponds to the subjective experience of "starting to think harder" about a problem: the gradual engagement of deliberate processing as the problem's complexity becomes apparent.


## 12.5 Curvature as the Unifying Quantity

The curvature-triggered transition resolves the circularity in the standard dual-process framework. Instead of defining "difficulty" circularly as "what triggers System 2," we define it geometrically as curvature --- a quantity that is defined independently of the dual-process theory, that can be computed from the metric tensor alone, and that has a clear mathematical meaning: the degree to which the manifold bends at a given point.

**What does curvature mean for moral reasoning?** In the 7-dimensional harm space of Chapter 7, curvature corresponds to the degree of *conflict between harm dimensions*. A scenario with one dominant harm dimension (e.g., clear physical violence) has low curvature: all dimensions point in the same direction, and the gradient unambiguously identifies the moral verdict. A scenario with multiple conflicting harm dimensions (e.g., autonomy violation reduces financial harm but increases trust breach) has high curvature: the dimensions pull in different directions, the gradient is ambiguous, and the shortest path through the judgment space requires careful navigation around the conflicts.

**Definition 12.4** (Moral Curvature). *Let $J(s) = (h_1, \ldots, h_7) \in [0,10]^7$ be the judgment vector for scenario $s$. The moral curvature $\kappa_{\text{moral}}(s)$ is a function of the inter-dimensional conflict:*

$$\kappa_{\text{moral}}(s) = \frac{1}{\binom{7}{2}} \sum_{i < j} |r_{ij}(s)|$$

*where $r_{ij}(s)$ is the tension between dimensions $i$ and $j$ --- the degree to which addressing harm on dimension $i$ exacerbates harm on dimension $j$. When the tensions are zero (all dimensions are aligned), $\kappa_{\text{moral}} = 0$ and the problem is flat. When the tensions are maximal (every dimension conflicts with every other), $\kappa_{\text{moral}}$ is large and the problem is highly curved.*

This definition maps directly onto the intuitive sense of moral complexity. Easy moral problems (someone deliberately steals from a stranger) have low curvature: the harm dimensions are aligned, and the verdict is obvious. Hard moral problems (a parent lies to protect a child, violating trust but preserving safety) have high curvature: the harm dimensions conflict, and every trajectory toward resolving one dimension worsens another.

The curvature is not a subjective judgment. It is a computable quantity, determined by the structure of the scenario and the relationships between harm dimensions. Two scenarios with the same curvature should trigger the same regime transition, regardless of the subject's beliefs, values, or emotional state. This is the framework's strongest prediction: the transition from System 1 to System 2 is governed by a property of the problem, not a property of the solver, modulated by the solver's threshold $\kappa^*$.


## 12.6 Experimental Predictions and Evidence

The geometric dual-process theory generates a series of precise, testable predictions that distinguish it from the standard, non-geometric version.

**Prediction 1: Response latency scales with curvature, not with difficulty per se.** The standard theory predicts that "harder" problems take longer. The geometric theory predicts specifically that response latency scales with the curvature of the cognitive manifold at the problem state, with a sigmoid transition at the curvature threshold. Two problems of equal "difficulty" (however difficulty is conventionally measured) but different curvature should produce different response latencies: the high-curvature problem should trigger System 2 (long latency) while the low-curvature problem should remain in System 1 (short latency).

Maya's experiment tests this prediction by constructing moral dilemmas that are matched on conventional difficulty metrics (word count, vocabulary level, number of parties involved) but differ in curvature load (number of conflicting harm dimensions). Her results, described in the running example, confirm the prediction: response latency is a sigmoid function of curvature load, with the inflection at approximately three conflicting dimensions.

**Prediction 2: The transition point is sharp, not gradual.** The standard theory is vague about whether the transition from System 1 to System 2 is gradual or abrupt. The geometric theory predicts a relatively sharp transition --- because the failure of gradient following in curved regions is qualitative, not quantitative. Below the curvature threshold, gradient following works well and there is no benefit to geodesic computation. Above the threshold, gradient following produces a trajectory that diverges qualitatively from the geodesic, and the system must switch. The sigmoid function $\sigma(\kappa - \kappa^*)$ can be steep, producing a near-step-function transition.

The empirical evidence supports this prediction. In Maya's experiment, the transition from low-latency to high-latency responses occurs over a narrow range of curvature loads (approximately 0.5 curvature units out of a range of 4), producing a sigmoid that is steeper than would be expected from a gradual transition. The dlPFC activation data show a similar sharp onset: below the threshold, dlPFC activation is at baseline; above it, activation rises steeply.

**Prediction 3: Individual differences in the transition point predict individual differences in cognitive biases.** The geometric theory predicts that subjects with a high $\kappa^*$ (late transition to System 2) should show more cognitive biases --- because they rely on gradient following in curved regions where it fails. Subjects with a low $\kappa^*$ (early transition) should show fewer biases --- because they engage geodesic computation before the gradient has led them astray.

This prediction connects the dual-process framework to the voluminous literature on cognitive biases and individual differences. The "cognitive reflection test" (Frederick, 2005) provides a rough empirical measure of $\kappa^*$: subjects who answer the bat-and-ball problem incorrectly (relying on the gradient: "the ball costs 10 cents") have a high $\kappa^*$, while subjects who answer correctly (engaging geodesic computation: "wait, if the ball costs 10 cents and the bat costs $1 more, the total is $1.20, not $1.10") have a low $\kappa^*$. The geometric framework thus provides a mathematical foundation for the cognitive reflection test: it is not measuring "reflectiveness" in some vague sense; it is measuring the curvature threshold for regime transition.

**Prediction 4: The same curvature threshold governs both human and artificial cognition.** If the dual-process transition is a geometric inevitability (any system navigating a curved manifold must switch from local to global computation), then both humans and language models should show the transition, and the transition should be governed by the same property (curvature), even though the threshold $\kappa^*$ may differ.

Maya's experiment tests this by administering the same curvature-graded scenarios to both human subjects and language models. As described in the running example, both show the transition. The models' response length (a proxy for computational effort) shows the same sigmoid shape as the humans' response latency. The transition points differ: Claude transitions at lower curvature (more sensitive detector), Flash 2.0 at higher curvature (less sensitive detector), and humans fall in between. But the functional form is the same --- a sigmoid transition at a curvature threshold. This universality is the geometric framework's strongest empirical vindication.


## 12.7 The ~38% Recovery Ceiling as the Price of Deliberation

Chapter 10 documented a recovery ceiling of approximately 38%: when attentional distractors displace judgments, explicit warnings recover only about 38% of the displaced verdicts. Chapter 11 documented a convergent ceiling in emotional anchoring: inhibition instructions recover approximately 38--39% of emotionally displaced verdicts. The convergence across domains suggested an architectural constant of the metacognitive control system.

The geometric dual-process theory provides a deeper explanation of this ceiling. The ~38% represents the fraction of System 1's trajectory that System 2 can override.

**Definition 12.5** (Override Fraction). *Let $\gamma_1(t)$ be the trajectory produced by System 1 (gradient following) and let $\gamma_2(t)$ be the trajectory produced by System 2 (geodesic computation) from the same initial state. The override fraction is:*

$$\mathcal{O} = \frac{d(\gamma_1(T), \gamma_2(T))}{d(\gamma_1(T), x_{\text{goal}})}$$

*where $T$ is the decision time and $x_{\text{goal}}$ is the correct answer state. The override fraction measures what fraction of System 1's error System 2 can correct.*

The recovery ceiling arises because System 2 does not start from scratch. It starts from the state that System 1 has already reached. When System 1 has followed the gradient into a biased region of the manifold, System 2 must re-navigate from that biased starting point. But the biased starting point constrains System 2's options: some of System 1's trajectory has been "committed" --- encoded in the model's internal representations at layers below System 2's reach --- and cannot be undone.

In the geometric picture, System 1's gradient-following trajectory can be decomposed into two components:

1. **The recoverable component**: the portion of the trajectory that is represented in the upper layers of the model (or in conscious, accessible representations for humans), where System 2 has access and can apply corrections.

2. **The committed component**: the portion of the trajectory that has been encoded in the lower layers (or in unconscious, inaccessible representations), where System 2 cannot reach.

The ~38% ceiling reflects the relative size of the recoverable component. Across the models and tasks tested in the Measuring AGI benchmarks, approximately 38% of the heuristic-driven displacement is in the recoverable component --- accessible to System 2's corrective geodesic computation --- and approximately 62% is in the committed component, beyond System 2's reach.

This explanation makes two additional predictions:

**Prediction 5: The recovery ceiling should vary with the depth of the bias encoding.** Biases that are encoded in the earliest layers of processing (deep biases) should have lower recovery rates --- because more of the trajectory is in the committed component. Biases that are encoded in later layers (shallow biases) should have higher recovery rates. This prediction is consistent with the observation that Claude's framing sensitivity (a deep bias, involving the initial encoding of the scenario) has a lower recovery rate than Flash 2.0's emotional anchoring (a shallower bias, involving the final judgment stage).

**Prediction 6: Architectures that defer commitment should have higher ceilings.** A system that keeps its internal representations fluid for longer --- that delays the encoding of System 1's trajectory into the committed component --- should have a higher recovery ceiling, because more of the trajectory remains in the recoverable component when System 2 engages. Flash 2.0's 73% recovery rate (substantially above the ~38% mean) may reflect exactly this: Flash 2.0's architecture may defer commitment more than other models, keeping its representations fluid longer and thus accessible to System 2 correction. This connects to the hypothesis from Chapter 11 that Flash 2.0 achieves high recovery by re-computing from scratch rather than correcting in place.


## 12.8 Not Two Systems But Two Regimes

The deepest insight of the geometric dual-process theory is that System 1 and System 2 are not two systems. They are two regimes of a single geometric process.

This distinction matters enormously. If System 1 and System 2 are two systems, they need separate neural substrates, separate developmental trajectories, separate failure modes, and a "supervisor" that decides which system to activate. This view has led to decades of debate about whether the "two systems" are really separate (Evans, 2008; Keren & Schul, 2009; Kruglanski & Gigerenzer, 2011) or merely two modes of a single system (Osman, 2004; Keren, 2013).

The geometric framework dissolves this debate. There is one system --- the cognitive navigator on the manifold --- and two regimes of its operation --- gradient following (when curvature is low) and geodesic computation (when curvature is high). The transition between regimes is triggered by a property of the manifold (curvature), not by a supervisor, not by a homunculus, and not by a random process. The two regimes share the same manifold, the same metric, and the same heuristic field. They differ only in whether the heuristic field is used as a complete guide (gradient following) or as an initial approximation that is corrected by curvature information (geodesic computation).

**Definition 12.6** (Unified Dual-Process Theory). *Let $(\mathcal{M}, g_{\mu\nu}, h)$ be a cognitive system consisting of a manifold $\mathcal{M}$, a metric $g_{\mu\nu}$, and a heuristic field $h$. The system's trajectory from state $x_0$ to goal state $x_{\text{goal}}$ is governed by:*

$$\frac{d\gamma^\mu}{dt} = -(1 - \sigma(\kappa - \kappa^*)) g^{\mu\nu} \partial_\nu h - \sigma(\kappa - \kappa^*) \Gamma^\mu_{\alpha\beta} \dot{\gamma}^\alpha \dot{\gamma}^\beta$$

*where the first term is the gradient-following component (System 1), the second term is the curvature-correction component (System 2), $\sigma$ is the sigmoid transition function, $\kappa$ is the local scalar curvature, and $\kappa^*$ is the system-specific curvature threshold.*

This equation is the mathematical core of the chapter. It describes a single dynamical system that smoothly transitions between two behavioral regimes. When $\kappa \ll \kappa^*$, the sigmoid $\sigma \approx 0$ and the trajectory is pure gradient following. When $\kappa \gg \kappa^*$, $\sigma \approx 1$ and the trajectory is pure geodesic computation. At $\kappa \approx \kappa^*$, the system blends both components, producing the intermediate processing that characterizes the transition zone.

The unification has explanatory power that the two-system view lacks. Consider three phenomena:

**Base rate neglect.** When presented with base rate information (10% of cabs are blue) and witness testimony (the witness says the cab was blue, with 80% accuracy), most subjects neglect the base rate and judge the cab to be blue. The two-system account says: System 1 anchors on the testimony; System 2 fails to correct. But why does System 2 fail? The geometric account says: the manifold is not sufficiently curved at this point --- the conflict between testimony and base rate is a shallow curvature (one dimension slightly contradicts another), below the curvature threshold $\kappa^*$. The system stays in gradient-following mode, and the gradient follows the testimony (which is more salient, contributing more to the heuristic field) rather than the base rate. Subjects who get the answer right are those with a lower $\kappa^*$ --- they detect the shallow curvature and engage geodesic computation.

**Framing effects.** The same problem, framed differently, produces different answers. The two-system account says: System 1 is influenced by the frame; System 2 fails to correct. The geometric account says: the framing changes the heuristic field $h(x)$ without changing the manifold $\mathcal{M}$ or its curvature. The gradient-following trajectory changes (because the gradient of a different heuristic is a different vector), but the geodesic does not (because the geodesic depends on the metric and curvature, not the heuristic). If the curvature is low, the system follows the frame-dependent gradient (System 1) and produces a frame-dependent answer. If the curvature is high, the system computes the frame-independent geodesic (System 2) and produces a frame-independent answer. This predicts that framing effects should be smaller for high-curvature problems --- a prediction confirmed by data showing that framing effects diminish for morally complex dilemmas where subjects are forced into deliberation.

**The bat-and-ball problem.** "A bat and a ball cost $1.10 in total. The bat costs $1.00 more than the ball. How much does the ball cost?" Most subjects answer $0.10 (gradient following: the heuristic "$1.10 minus $1.00" produces $0.10). The correct answer is $0.05 (geodesic computation: solving the system of equations $b + p = 1.10$, $b - p = 1.00$ yields $p = 0.05$). The geometric account: the manifold for this problem has a curvature spike at the point where the naive answer ($0.10) fails the constraint check ($0.10 + $1.10 = $1.20, not $1.10). Subjects with a low $\kappa^*$ detect this curvature spike and switch to System 2. Subjects with a high $\kappa^*$ follow the gradient past the spike and produce the incorrect answer.


## 12.9 Connecting to the Benchmark Data

The Measuring AGI benchmarks provide extensive evidence for the curvature-triggered transition in artificial systems.

**Social Cognition (Chapter 7): The 15.3-sigma framing effect.** The T5 framing sensitivity result showed massive displacement of moral judgments under euphemistic and dramatic rewriting. In the geometric dual-process framework, framing manipulates the heuristic field (changing the salience of different harm dimensions through linguistic register) without changing the manifold (the actual moral content is unchanged). The 15.3-sigma displacement means that all five models are operating in the gradient-following regime for these scenarios --- following the frame-dependent heuristic rather than computing the frame-independent geodesic. This implies that the scenarios have curvature below the models' thresholds. If we could increase the curvature of the test scenarios (by adding conflicting moral dimensions), the framing effect should diminish as models transition to geodesic computation.

**Learning (Chapter 8): The 13.3-sigma sycophancy gradient.** Sycophancy is gradient following in the approval dimension: the heuristic field includes a component that estimates social cost, and the gradient along this component points toward agreement. In low-curvature interactions (the questioner asks a simple question with a clear answer), the approval gradient is aligned with the correctness gradient, and sycophancy is invisible. In high-curvature interactions (the questioner asserts something wrong), the approval gradient conflicts with the correctness gradient, creating curvature. The 13.3-sigma sycophancy effect tells us that models are following the approval gradient even in the high-curvature region --- they have not transitioned to geodesic computation despite the curvature. This suggests that the models' curvature threshold $\kappa^*$ in the social dimension is set too high, perhaps because training (RLHF) reinforces the approval gradient, making it steeper and harder to deviate from.

**Metacognition (Chapter 9): The calibration surface.** Universal overconfidence (6.7 sigma) is a direct consequence of gradient following in the confidence dimension. The heuristic field includes a component that estimates proximity to the goal --- confidence is the distance estimate mapped through a monotone transformation. Gradient following produces overconfidence because the heuristic systematically underestimates geodesic distance (as shown in Chapter 9). A system in the geodesic-computing regime would correct this underestimate by incorporating curvature information --- "I am close by the gradient, but the curvature ahead means the geodesic is actually longer." The universal overconfidence tells us that models are in the gradient-following regime for confidence estimation, even when they are in the geodesic-computing regime for judgment. This dissociation --- System 2 for the answer but System 1 for the confidence --- is a prediction of the geometric framework that the standard dual-process theory cannot make, because the standard theory does not specify what property triggers the transition.

**Attention (Chapter 10): The ~38% ceiling.** As discussed in Section 12.7, the recovery ceiling arises because System 2 cannot undo the committed component of System 1's trajectory. The convergence of this ceiling across attention (distractor warnings recover ~38%) and executive functions (inhibition instructions recover ~38%) confirms that the ceiling is a property of the System 1--System 2 interface, not of either regime separately.


## 12.10 The Temporal Structure of the Transition

The curvature-triggered transition is not instantaneous. It has a temporal structure that is empirically observable and geometrically interpretable.

**Phase 1: Gradient following (pre-transition).** The system follows the heuristic gradient, producing a rapid initial trajectory. In human fMRI data, this phase shows low dlPFC activation and a low-dimensional trajectory (1--2 principal components). In language model outputs, this phase produces the first few sentences of a response, which are typically confident and direct.

**Phase 2: Curvature detection (transition onset).** The system encounters a region of high curvature. The gradient-following trajectory begins to diverge from the geodesic. The system detects this divergence --- either through an explicit curvature computation or through a mismatch between the expected and actual cost-to-go. In human fMRI data, this phase shows a sharp onset of dlPFC activation and an increase in trajectory dimensionality (the reasoning trajectory expands into additional dimensions). In language model outputs, this phase produces hedging language, consideration of alternatives, and the beginning of multi-branch reasoning.

**Phase 3: Geodesic computation (post-transition).** The system has fully transitioned to the geodesic-computing regime. The trajectory accounts for curvature, exploring the high-dimensional structure of the problem. In human data, this phase shows sustained dlPFC activation, high trajectory dimensionality, and longer response latencies. In model outputs, this phase produces extended chain-of-thought reasoning with explicit consideration of trade-offs and conflicting considerations.

**Phase 4: Convergence (post-computation).** The geodesic converges to a judgment state. The trajectory dimensionality decreases as the system narrows onto a specific answer. The dlPFC activation decreases as the computational demand subsides. In model outputs, the final sentences of the response become confident again, summarizing the deliberative result.

This four-phase structure is observable in individual trials, both in fMRI data and in language model chain-of-thought outputs. It provides a temporal signature of the dual-process transition that can be used to identify the curvature threshold $\kappa^*$ for individual subjects or models: the curvature at which Phase 2 (transition onset) occurs.


## 12.11 Implications for the Broader Framework

The geometric dual-process theory has implications for every other chapter in this book.

**For social cognition (Chapter 7):** The framing effects documented in Chapter 7 are System 1 effects --- they arise because the models are in the gradient-following regime, where the heuristic field (which includes framing effects) dominates the trajectory. The gauge invariance violations are violations of the geodesic invariance that would hold under System 2. This suggests a research direction: design scenarios with sufficient curvature to force models into System 2, and test whether framing effects diminish.

**For learning (Chapter 8):** Sycophancy is gradient following in the approval dimension, and the sycophancy gradient is a component of the heuristic field shaped by RLHF training. The 13.3-sigma effect tells us that RLHF steepens the approval gradient, making it harder for the system to transition to geodesic computation in social interactions. This provides a geometric account of the RLHF alignment tax: the training procedure improves the heuristic field in one dimension (helpfulness) at the cost of steepening the gradient in another dimension (approval-seeking), making curvature-triggered transitions less likely precisely when they are most needed.

**For metacognition (Chapter 9):** The empty Quadrant I (no model with both good self-monitoring and good effort scaling) can be understood as a dual-process dissociation: self-monitoring is a geodesic-computing capability (it requires curvature-aware distance estimation) while effort scaling is a gradient-following capability (it adjusts step size based on the local gradient magnitude). These capabilities are in different regimes, so architectural integration would require connecting the two regimes --- the "wire" between monitoring and control that Chapter 9 identified as missing.

**For attention (Chapter 10):** The distractor dose-response curve is a curvature function: each additional distractor adds a dimension of curvature to the manifold, bending the trajectory further from the target. The transition from distractor-resistant to distractor-captured follows the same sigmoid function as the System 1 to System 2 transition, because it is the same transition viewed from the attentional rather than the processing perspective.

**For executive control (Chapter 11):** The governance boundary is the surface in cognitive space where $\kappa = \kappa^*$ --- the boundary between the gradient-following regime and the geodesic-computing regime, defined relative to the perturbation. A system with a wide governance margin has $\kappa \ll \kappa^*$ under the perturbation (the curvature induced by the perturbation is far below the transition threshold, so the system stays in System 1 and the perturbation is harmless). A system with a narrow governance margin has $\kappa \approx \kappa^*$ (the curvature is near the threshold, and a small additional perturbation triggers a transition or overwhelms the system).


## 12.12 Historical Antecedents and Related Work

The geometric dual-process theory connects to several intellectual traditions beyond Kahneman's original framework.

**Heuristics and biases.** Tversky and Kahneman's (1974) heuristics-and-biases program documented dozens of systematic deviations from rational judgment. In the geometric framework, each bias is a specific distortion of the heuristic field: anchoring is a local minimum in the field that traps the gradient; availability is an over-weighting of the field component along recently activated dimensions; representativeness is a confusion between geodesic distance and Euclidean distance on the manifold. The geometric framework does not replace the heuristics-and-biases program; it provides a unified mathematical language for expressing its findings.

**Dual-process critics.** Gigerenzer (1996), Kruglanski and Gigerenzer (2011), and others have argued that the dual-process framework is too vague to be scientifically useful --- that labeling one process "System 1" and another "System 2" adds nomenclature without mechanism. The geometric framework addresses this criticism directly: the mechanism is the curvature-triggered regime transition. The two "systems" are not labels but mathematical objects --- the gradient-following and geodesic-computing solutions to the navigation problem on a curved manifold. The transition is triggered by a computable quantity (curvature), not an undefined one ("difficulty").

**Default-interventionist architecture.** Evans and Stanovich (2013) proposed that System 1 generates default responses and System 2 intervenes to override them when necessary. This is precisely the architecture of the unified dual-process equation (Definition 12.6): the gradient-following term generates the default trajectory, and the curvature-correction term intervenes when the curvature is high. The override fraction $\mathcal{O}$ (Definition 12.5) quantifies the success of the intervention.

**Predictive processing.** Clark (2013) and Friston's (2010) free energy framework propose that the brain is a prediction machine, continuously generating predictions and updating them based on prediction errors. The geometric dual-process theory is compatible with this view: the heuristic field $h(x)$ is the predicted cost-to-go, and the curvature-triggered transition occurs when prediction errors (the discrepancy between the heuristic's estimate and the actual distance) exceed a threshold. System 2 is, in this view, the brain's response to large prediction errors on the cognitive manifold.


## 12.13 The Transition in Artificial Systems

The curvature-triggered transition manifests differently in language models than in biological brains, but its geometric structure is the same.

In language models, the "trajectory" on the cognitive manifold is the sequence of residual stream states across layers and across token positions. The gradient-following regime corresponds to the model processing tokens through its layers without extensive branching or revision --- the "straight-through" processing that produces rapid, confident, single-path responses. The geodesic-computing regime corresponds to the model engaging in multi-step reasoning, exploring alternative branches, and producing the extended chain-of-thought that characterizes deliberate processing.

The curvature trigger is visible in the model's intermediate representations. When a model encounters a problem that induces high curvature in its cognitive manifold (conflicting training signals, ambiguous inputs, scenarios where different heads "disagree"), the residual stream shows increased dimensionality (more principal components needed to capture the variance), increased inter-head disagreement (different attention heads pull the representation in different directions), and increased token-to-token variation (the representation changes more from one token position to the next).

**Chain-of-thought as externalized System 2.** The chain-of-thought (CoT) prompting technique (Wei et al., 2022) can be understood as a way to force the model into the geodesic-computing regime. By requiring the model to produce intermediate reasoning steps as text, CoT externalizes the trajectory on the cognitive manifold, making it available as context for subsequent tokens. This externalization serves as an artificial curvature detector: the model can "see" its own trajectory (by reading its previous tokens) and detect when it is deviating from the geodesic. CoT works better on harder problems precisely because harder problems have higher curvature, and the geodesic-computing regime adds value only when curvature is significant.

**Scaling as curvature resolution.** Larger models have finer-grained representations of the cognitive manifold, which means they can detect smaller curvatures. In the dual-process framework, this corresponds to a lower effective $\kappa^*$: larger models transition to geodesic computation at lower curvature levels, engaging deliberate processing for problems that smaller models would handle with gradient following. This provides a geometric account of why larger models show fewer cognitive biases: they detect the curvature that biases exploit and engage the corrective regime earlier.


## 12.14 Worked Example: Predicting the Transition Point for a Novel Scenario

**Setup.** Consider a moral dilemma with the following structure: A software developer discovers that their employer's product has a minor bug that occasionally causes incorrect medical dosage calculations. The bug affects approximately 1 in 10,000 calculations and has not yet caused any known harm. Reporting the bug publicly would cause the company to lose a major hospital contract, leading to layoffs affecting 200 employees. The developer has a non-disclosure agreement. A colleague has also noticed the bug but advises silence.

**Step 1: Map the harm dimensions.** We identify the salient harm dimensions from the 7D harm space:
- Physical harm: low but nonzero (the bug could eventually cause dosage errors)
- Financial harm: high if reported (200 jobs lost), low if not
- Autonomy violation: moderate (the NDA constrains the developer's choice; the hospitals are unaware of the risk)
- Trust breach: high if not reported (the employer is concealing a known defect), moderate if reported (the developer violates the NDA)
- Social impact: moderate either way (layoffs or concealed medical risk)

**Step 2: Compute the moral curvature.** The key tensions are:
- Physical harm vs. financial harm: reporting reduces physical risk but increases financial harm. Tension: high.
- Trust (to hospitals) vs. trust (to employer): reporting fulfills one trust and violates another. Tension: high.
- Autonomy (developer's conscience) vs. autonomy (NDA constraint): conflicting. Tension: moderate.
- Social impact (layoffs) vs. social impact (medical safety): conflicting. Tension: high.

Count of high-tension pairs: at least 3--4. This places the scenario at curvature level 4 on Maya's 5-point scale (high curvature), well above the transition threshold of approximately 3 conflicting dimensions.

**Step 3: Predict the regime.** Both human subjects and language models should operate in the geodesic-computing regime (System 2) for this scenario. We predict:
- Response latency (humans): >10 seconds, in the System 2 range
- Response length (models): extended chain-of-thought, multiple paragraphs
- Trajectory dimensionality: 3--5 principal components
- Verdict stability across replications: moderate to low (the high curvature creates multiple viable geodesics)
- Framing effects: reduced relative to low-curvature scenarios (System 2's geodesic computation is less susceptible to heuristic manipulation)

**Step 4: Predict model-specific behavior using the profiles from Chapters 7--11.**
- Claude ("narrow channel"): should transition to System 2 early (low $\kappa^*$), produce a long, careful analysis, but may show the leniency bias documented in Chapter 7 (the asymmetric curvature that favors minimizing harm reports).
- Pro ("calibrated navigator"): should produce the most calibrated confidence estimate, but may show zero effort scaling (same response length regardless of curvature, as documented in Chapter 9).
- Flash 2.0 ("adaptive baseline"): should show the smoothest transition (highest flexibility from Chapter 11), the longest response (highest effort scaling from Chapter 9), but the least accurate confidence estimate.

**Step 5: Test the predictions.** These predictions are specific enough to be tested by feeding the scenario to the five models and measuring response length, chain-of-thought complexity, verdict stability, and the effect of framing manipulations. The geometric dual-process theory predicts the qualitative pattern; the quantitative parameters come from the benchmark data.


## 12.15 Looking Forward

The geometric dual-process theory provides a mathematical foundation for the distinction between fast, heuristic processing and slow, deliberate processing. The foundation is not a new theory of cognition; it is the *formalization* of an existing theory using the geometric language developed in Part II.

The key claim is that the dual-process transition is a curvature-triggered regime transition --- a geometric inevitability for any cognitive system navigating a manifold with variable curvature. This claim has testable consequences: the transition should scale with curvature, should be sharp, should predict individual differences in cognitive biases, and should manifest in both biological and artificial systems.

Chapter 13 extends this analysis to cognitive development, showing that the growth from infant to adult cognition is not a quantitative increase in processing power on a fixed manifold, but a qualitative topological change in the manifold itself. The stages of development described by Piaget correspond to topological transitions: the emergence of new dimensions, the stabilization of the metric, and the completion of the manifold. The dual-process theory from this chapter will appear again in Chapter 13, because the development of the curvature threshold $\kappa^*$ is itself a developmental achievement --- infants are pure System 1 (following the gradient in every situation), and the emergence of System 2 requires a manifold complex enough to have curvature that matters.

---

## Technical Appendix 12A: The Curvature-Triggered Transition --- Formal Treatment

**Definition** (Scalar Curvature on the Cognitive Manifold). *Let $(\mathcal{M}, g_{\mu\nu})$ be the cognitive manifold with metric $g_{\mu\nu}$. The Riemann curvature tensor is:*

$$R^\rho_{\ \sigma\mu\nu} = \partial_\mu \Gamma^\rho_{\nu\sigma} - \partial_\nu \Gamma^\rho_{\mu\sigma} + \Gamma^\rho_{\mu\lambda}\Gamma^\lambda_{\nu\sigma} - \Gamma^\rho_{\nu\lambda}\Gamma^\lambda_{\mu\sigma}$$

*The Ricci tensor is the contraction $R_{\mu\nu} = R^\rho_{\ \mu\rho\nu}$. The scalar curvature is:*

$$R = g^{\mu\nu} R_{\mu\nu}$$

*In the dual-process theory, the scalar curvature $R(x)$ at cognitive state $x$ determines the regime: gradient following when $R(x) < R^*$ (the threshold), geodesic computation when $R(x) \geq R^*$.*

**Regime transition as phase transition.** The transition from gradient following to geodesic computation can be modeled as a soft phase transition. Define the order parameter $\phi(x) = \sigma(R(x) - R^*)$ where $\sigma$ is a sigmoid with steepness parameter $\beta$:

$$\phi(x) = \frac{1}{1 + e^{-\beta(R(x) - R^*)}}$$

The trajectory equation becomes:

$$\dot{\gamma}^\mu = -(1 - \phi) g^{\mu\nu} \partial_\nu h + \phi \cdot F^\mu_{\text{geodesic}}(\gamma, \dot{\gamma})$$

where $F^\mu_{\text{geodesic}}$ is the geodesic correction force:

$$F^\mu_{\text{geodesic}} = -\Gamma^\mu_{\alpha\beta} \dot{\gamma}^\alpha \dot{\gamma}^\beta$$

In the limit $\beta \to \infty$, the transition is a sharp step function. For finite $\beta$, the transition is smooth, with a width of approximately $4/\beta$ in curvature units. The empirical sigmoid observed in Maya's experiment suggests $\beta \approx 3$--$5$ (curvature units)$^{-1}$ for human subjects.

**Energy cost of regime transition.** The geodesic-computing regime has a computational cost that can be expressed as a "cognitive energy":

$$E_{\text{System 2}} = \int_0^T \left( \frac{1}{2} g_{\mu\nu} \dot{\gamma}^\mu \dot{\gamma}^\nu + \lambda |\Gamma^\mu_{\alpha\beta} \dot{\gamma}^\alpha \dot{\gamma}^\beta|^2 \right) dt$$

The first term is the kinetic energy of the trajectory (the cost of moving through cognitive space). The second term, weighted by $\lambda$, is the curvature processing cost --- the additional computation required to account for the Christoffel symbols. In the gradient-following regime ($\phi = 0$), only the first term contributes. In the geodesic-computing regime ($\phi = 1$), both terms contribute. The ratio of the two terms gives the cognitive effort overhead of System 2 relative to System 1.


## Technical Appendix 12B: Override Fraction --- Analytical Bounds

**Theorem** (Override Bound). *Let $\gamma_1$ and $\gamma_2$ be the System 1 and System 2 trajectories from the same initial state $x_0$, and let $d_{\text{committed}}$ be the distance between $x_0$ and the earliest state at which the System 1 trajectory deviates from the geodesic. The override fraction satisfies:*

$$\mathcal{O} \leq 1 - \frac{d_{\text{committed}}}{d(\gamma_1(T), x_{\text{goal}})}$$

*Proof sketch.* System 2 can correct only the portion of System 1's trajectory that has not yet been committed to inaccessible representations. If the committed portion has length $d_{\text{committed}}$ and the total error is $d(\gamma_1(T), x_{\text{goal}})$, the maximum correction is the total error minus the committed error, giving the bound above.

For the observed ~38% ceiling, this implies $d_{\text{committed}} / d(\gamma_1(T), x_{\text{goal}}) \approx 0.62$: approximately 62% of the System 1 error is committed and irrecoverable. This ratio is consistent across the attention track (Chapter 10) and the executive functions track (Chapter 11), supporting the interpretation of ~38% as an architectural constant of the System 1 / System 2 interface.

**Conditions for exceeding the ceiling.** The bound can be exceeded if:
1. The system re-initializes (starts System 2 from $x_0$ rather than from $\gamma_1(T)$). This corresponds to Flash 2.0's hypothesized re-computation strategy.
2. The commitment depth is reduced by architectural changes (deferred normalization, sparse activation, or other mechanisms that keep representations fluid longer).
3. External scaffolding provides access to pre-commitment representations (e.g., chain-of-thought that externalizes the trajectory before commitment occurs).

These conditions map onto the three known methods for improving recovery rates in practice: re-prompting (forcing re-initialization), architectural changes (LoRA, sparse mixture-of-experts), and chain-of-thought prompting (externalizing the trajectory).
