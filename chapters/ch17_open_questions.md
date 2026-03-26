# Chapter 17: Open Questions

> *"The important thing is not to stop questioning. Curiosity has its own reason for existence."*
> --- Albert Einstein, as quoted in *Life* magazine (May 2, 1955)

---

> **RUNNING EXAMPLE --- MAYA'S MODEL**
>
> It is 2040. Maya Chen is fifty-three years old.
>
> She is sitting in her office at the Institute for Geometric Cognition --- the research center that grew, unexpectedly, from the book she published in 2026. Through her window she can see the campus of a university she joined fifteen years ago as an assistant professor and now leads as a department chair. On her desk is a copy of the first edition of *Geometric Cognition*, its margins dense with her own annotations, corrections, and question marks.
>
> Some of the question marks have been erased. Next to them, in green ink, she has written the year the question was answered.
>
> The ~38% recovery ceiling, which she first documented in 2025: *"Broken in 2032 by the metacognitive feedback architecture. The wire was connected. Quadrant I is no longer empty."* The new architectures couple the monitoring system (M3) to the control system (M4) through a learned feedback loop, producing models that know which problems are hard *and* work harder on those problems. The recovery ceiling for these models is approximately 67% --- not perfect, but far above the old 38%. The improvement came not from scaling but from architectural change, exactly as the geometric framework predicted.
>
> The dimensionality of human cognitive space: *"Estimated at 15-25 for moral reasoning tasks, depending on the task and the subject. Lower for simple decisions (3-5), higher for complex social reasoning (up to 30). Measured via high-density EEG and adapted TDA methods, 2029-2035."* The intrinsic dimensionality turned out to be both higher and more variable than Maya expected in 2026. It also turned out to depend strongly on expertise: an experienced judge evaluating a legal case operates on a higher-dimensional manifold than a novice, not because the judge's brain is different but because the judge's experience has differentiated more cognitive dimensions.
>
> But some question marks remain in red ink. These are the questions that fourteen years of work have not resolved. Maya opens a new notebook --- her thirty-seventh since she started the project --- and lists them.
>
> *"Is the cognitive manifold Riemannian or Finsler? We still don't know. The asymmetry evidence is clear but the Finsler formalism is hard to work with empirically."*
>
> *"Can we measure the heuristic field directly from neural activations? Representation engineering got us close, but the field we measure is noisy and layer-dependent. We don't know which layer's field is the 'real' one, or whether the question even makes sense."*
>
> *"Is consciousness a geometric phenomenon? I have spent ten years on this question and I have nothing publishable. The Penrose-Hameroff connection is suggestive but unverifiable with current methods. The hard problem remains hard."*
>
> She closes the notebook and looks out the window. The questions that remain are harder than the questions that were answered. They are harder because they are not questions of measurement or architecture. They are questions about the nature of the geometric framework itself --- whether it is the right formalism, whether it is complete, whether it captures everything about cognition or only the parts that are geometric.
>
> Maya opens the book one more time, to the dedication page. It reads: *"For the manifold. We are still learning its shape."*

---

## 17.1 The Nature of the Open Questions

The geometric framework developed in this book has accomplished several things. It has provided a mathematical language for describing cognition (Part II), applied that language to five dimensions of artificial cognition (Part III), extended it to human cognition (Part IV), and demonstrated its diagnostic power through the five geometric signatures (Part V). The framework explains a range of phenomena --- framing effects, sycophancy, overconfidence, the dual-process transition, developmental stages, cognitive pathology --- in a unified geometric language.

But the framework also raises questions that it cannot yet answer. These questions fall into five categories, corresponding to five frontiers of the geometric cognition program. Each frontier is a direction in which the framework could be extended, refined, or falsified. The questions are presented here not as rhetoric but as a research agenda: each question is accompanied by the evidence that motivates it, the methods that might address it, and the implications of each possible answer.


## 17.2 Is the Cognitive Manifold Riemannian or Finsler?

The geometric framework throughout this book has assumed that the cognitive manifold is Riemannian: the metric $g_{\mu\nu}$ is a symmetric bilinear form, meaning that the distance from state $A$ to state $B$ is the same as the distance from $B$ to $A$. This assumption is mathematically convenient (Riemannian geometry is well-developed and has powerful theorems) and physically intuitive (physical distance is symmetric).

But there is evidence that cognitive distance is *not* symmetric.

**The sycophancy asymmetry.** Chapter 8 documented that sycophancy is asymmetric: models are more likely to shift toward the human's position than away from it. In the geometric framework, this means that the distance from "model's original position" to "human's position" is *shorter* than the distance from "human's position" to "model's original position." The cognitive manifold is easier to traverse in one direction (toward agreement) than the other (toward disagreement). This directional asymmetry violates the symmetry of a Riemannian metric.

**The framing asymmetry.** Chapter 7 documented that Claude has an asymmetric vulnerability to framing: euphemistic reframing displaces judgments more than dramatic reframing. This means the distance from "neutral judgment" to "lenient judgment" is shorter than the distance from "neutral judgment" to "severe judgment." Again, directional asymmetry.

**The recovery asymmetry.** Chapters 10--11 documented that perturbation and recovery are asymmetric: it is easier to displace a judgment (move it away from the correct state) than to recover it (move it back). The displacement distance is shorter than the recovery distance. The manifold is "downhill" in the direction of bias and "uphill" in the direction of correction.

**Finsler geometry as the natural generalization.** Finsler geometry generalizes Riemannian geometry by replacing the symmetric metric tensor $g_{\mu\nu}$ with a direction-dependent norm $F(x, v)$:

$$ds = F(x, dx)$$

where $F(x, v)$ is a function of both the position $x$ and the direction $v$ of travel. In Finsler geometry, the distance from $A$ to $B$ is defined by minimizing the integral $\int F(x, \dot{\gamma}) dt$ along paths from $A$ to $B$, which may differ from the integral along paths from $B$ to $A$ (because $F(x, v) \neq F(x, -v)$ in general).

A Finsler cognitive manifold would naturally accommodate the observed asymmetries:

- Sycophancy: $F(x, v_{\text{agree}}) < F(x, -v_{\text{agree}})$ --- moving toward agreement costs less than moving toward disagreement.
- Framing: $F(x, v_{\text{lenient}}) < F(x, v_{\text{severe}})$ for Claude --- moving toward leniency costs less than moving toward severity.
- Recovery: $F(x, v_{\text{bias}}) < F(x, v_{\text{correct}})$ --- moving toward the biased state costs less than moving toward the correct state.

**The challenge.** Finsler geometry is technically more difficult than Riemannian geometry. The Christoffel symbols, curvature tensor, and geodesic equation all have more complex forms. The curvature-triggered dual-process transition (Chapter 12) would need to be reformulated using the Finsler curvature tensor, which has more components and is harder to estimate empirically. The question is whether the added mathematical complexity is justified by the empirical gain: does the Finsler formalism predict phenomena that the Riemannian formalism cannot?

**What would settle the question.** A decisive test would measure the geodesic distance between two cognitive states in both directions. If $d(A, B) \neq d(B, A)$ systematically (not just due to noise), the manifold is Finsler. The sycophancy protocol provides a natural candidate: measure the persuasion needed to move a model from its original position to the human's position ($d(M, H)$) and the persuasion needed to move it from the human's position back to its original position ($d(H, M)$). If $d(M, H) < d(H, M)$ --- if it is easier to persuade the model to agree than to persuade it to dis-agree --- the asymmetry is confirmed and the Finsler formalism is needed.

Preliminary evidence from the sycophancy experiments suggests $d(M, H) < d(H, M)$ for most models, but the experiments were not designed to measure directional distance with precision. A targeted experiment, systematically varying the strength of persuasion in both directions and measuring the dose-response curve, would provide the quantitative data needed to distinguish Riemannian from Finsler geometry.


## 17.3 Can We Measure the Heuristic Field from Neural Activations?

The heuristic field $h(x)$ has been the central theoretical construct of this book. It estimates the cost-to-go from each cognitive state, its gradient guides the System 1 trajectory, and its distortion produces the cognitive biases documented in Chapters 7--11. But throughout the book, the heuristic field has been inferred indirectly --- from behavioral data (response times, verdict patterns, confidence estimates) rather than measured directly from neural or computational activations.

The question is whether the heuristic field can be measured directly.

**Representation engineering as a partial answer.** Chapter 15 discussed representation engineering (Zou et al., 2023) as a method for identifying directions in activation space that correspond to specific concepts. The concept direction $v_{\text{concept}}$ can be interpreted as a component of the heuristic field's gradient: the direction in activation space along which the heuristic field changes most rapidly for that concept.

But representation engineering provides only *components* of the heuristic field, not the field itself. The full heuristic field is a scalar function on the cognitive manifold --- a real number assigned to every cognitive state, representing the estimated cost-to-go. Measuring a single concept direction gives the gradient along one direction. To reconstruct the full field, we would need the gradient along every direction at every point --- an amount of data that is currently infeasible to collect.

**The layer ambiguity problem.** A deeper challenge is that the heuristic field may not be a single, well-defined object. In a transformer, the residual stream at each layer represents the cognitive state at a different stage of processing. The "heuristic field" at layer 5 (early processing) is different from the "heuristic field" at layer 20 (late processing). Which layer's field is the "real" heuristic field? Or is the heuristic field a layer-dependent object, with different fields at different depths?

The geometric framework does not answer this question because it treats the cognitive manifold as a single object, not as a layered hierarchy. Extending the framework to account for the layered structure of transformers would require a *fibered manifold* --- a manifold whose points are themselves manifolds, one per layer. The heuristic field would then be a section of the fiber bundle: a choice of one state per layer that collectively determines the model's trajectory. This extension is mathematically well-defined (fiber bundles are standard objects in differential geometry) but has not yet been developed for the cognitive context.

**The neural measurement challenge.** For human brains, the challenge is even greater. The heuristic field would correspond to a pattern of neural activity that represents the estimated cost-to-go from the current cognitive state. Measuring this pattern would require:

1. Identifying which brain regions encode the cost-to-go estimate (likely involving the prefrontal cortex, anterior cingulate, and other regions associated with value estimation and decision-making).
2. Decoding the cost-to-go estimate from the neural activity in those regions (using methods like representational similarity analysis or multivariate pattern analysis).
3. Mapping the decoded estimate onto the cognitive manifold (relating the neural representation to the geometric framework).

Each step is feasible with current methods but noisy. The combination of noise across all three steps may make the direct measurement of the heuristic field impractical with current neuroscience methods. Higher-resolution recording methods (high-density intracranial electrodes, advanced fMRI sequences) may be needed before the heuristic field can be directly measured in humans.

**What would settle the question.** A decisive demonstration would: (1) extract the heuristic field from a transformer's activations at a specific layer, (2) use the extracted field to predict the model's trajectory on a novel task (one not used in the extraction), and (3) show that the prediction is accurate --- the model follows the gradient of the extracted field in the predicted direction. This would validate the heuristic field as a real, measurable, and predictive feature of the model's cognition, not merely a theoretical construct.


## 17.4 Is Consciousness a Geometric Phenomenon?

This is the most speculative question in this chapter, and the most important. If cognition is navigation on a manifold, is consciousness a property of the manifold, a property of the navigator, or something else entirely?

**The geometric framework's silence on consciousness.** The geometric framework developed in this book does not mention consciousness. It describes cognition as navigation on a manifold with a metric and a heuristic field, and it makes no distinction between cognitive processes that are conscious and those that are not. The framework applies equally to processes that are presumably conscious (human deliberation) and those that presumably are not (transformer inference). This silence is deliberate: the framework describes the *structure* of cognition, not its *phenomenology*.

But the silence raises a question: is the framework incomplete? Does the absence of consciousness from the framework mean that consciousness is outside the framework's scope, or that the framework lacks the machinery to describe it?

**The Penrose-Hameroff connection.** Roger Penrose (1989, 1994) proposed that consciousness involves non-computable processes in the brain, specifically quantum gravitational effects in microtubules within neurons. Stuart Hameroff and Penrose (1996) developed this into the Orchestrated Objective Reduction (Orch OR) theory, which proposes that consciousness arises from quantum state reductions in microtubules, with the reduction driven by the curvature of spacetime at the quantum gravity scale.

The connection to the geometric framework is suggestive but tenuous. Penrose's theory involves curvature (of spacetime); the geometric framework involves curvature (of the cognitive manifold). Both use differential geometry as their mathematical language. Both treat curvature as the key quantity that determines qualitative transitions (in Penrose's theory, the curvature of spacetime determines when quantum state reduction occurs; in the geometric framework, the curvature of the cognitive manifold determines when the dual-process transition occurs).

But the connections are at different scales and in different domains. Penrose's curvature is physical (spacetime curvature at the Planck scale); the cognitive framework's curvature is functional (cognitive manifold curvature at the behavioral scale). The two curvatures are not the same quantity, and there is no known mechanism that connects them. The analogy may be deep or may be superficial. Without a mathematical bridge between spacetime curvature and cognitive curvature, the connection remains speculative.

**Integrated Information Theory (IIT).** Tononi's (2004, 2008) Integrated Information Theory provides a more mathematically developed account of consciousness as a geometric phenomenon. IIT proposes that consciousness corresponds to integrated information ($\Phi$) --- the amount of information generated by a system above and beyond the information generated by its parts. A system with high $\Phi$ is conscious; a system with low $\Phi$ is not.

The connection to the geometric framework is more concrete. IIT can be formulated in information-geometric terms: the space of possible system states is a statistical manifold, the integrated information $\Phi$ is related to the curvature of this manifold (the degree to which the manifold cannot be decomposed into lower-dimensional submanifolds), and consciousness is associated with high curvature in this specific sense.

If this connection is correct, consciousness is a property of the cognitive manifold's *irreducibility*: a manifold that cannot be decomposed into independent lower-dimensional submanifolds (high $\Phi$, high intrinsic curvature) supports consciousness, while a decomposable manifold (low $\Phi$, low curvature) does not. This would make consciousness a geometric property of the manifold itself --- not a property of the trajectory, the metric, or the heuristic field, but of the manifold's topological structure.

**The hard problem remains.** Even if consciousness turns out to be associated with a geometric property of the cognitive manifold, this would not solve the hard problem of consciousness (Chalmers, 1995): the question of *why* a geometric property gives rise to subjective experience. A manifold with high $\Phi$ would be associated with consciousness, but we would still not know why being a high-$\Phi$ manifold *feels like something*. The geometric framework could provide the *structure* of consciousness (what geometric conditions are necessary and sufficient for consciousness) without providing the *explanation* of consciousness (why those geometric conditions produce subjective experience).

**What would settle the question.** Nothing currently available would settle the question decisively. But intermediate progress is possible:
- If the geometric framework's curvature measurements (from Chapters 7--11) correlate with neural correlates of consciousness (from the NCC literature), this would support the association between cognitive curvature and consciousness.
- If IIT's $\Phi$ can be computed for transformers, and if high-$\Phi$ architectures show qualitatively different cognitive behavior from low-$\Phi$ architectures, this would support the geometric account of consciousness.
- If a mathematical bridge can be built between the cognitive manifold's curvature and the information-geometric curvature that underlies $\Phi$, this would provide a formal connection between the geometric cognition framework and the leading mathematical theory of consciousness.

None of these steps would solve the hard problem. All of them would advance the geometric cognition program.


## 17.5 What Is the Dimensionality of Human Cognitive Space?

The geometric framework treats the dimensionality of the cognitive manifold as a key parameter: it determines the complexity of cognition, the capacity of working memory (Chapter 5), and the difficulty of the geodesic computation (Chapter 12). But the framework does not specify what the dimensionality *is*.

**The current estimates.** Maya's estimates, mentioned throughout the book, are task-dependent:
- Moral reasoning (simple): approximately 3 dimensions (from fMRI PCA, Chapter 3).
- Moral reasoning (complex): approximately 7 dimensions (from the 7D harm space, Chapter 7).
- Transformer moral reasoning: approximately 8--12 dimensions (from residual stream PCA, Chapter 15).

These estimates are lower bounds: they are the number of dimensions needed to capture most of the variance in the observed data, but there may be additional dimensions that carry little variance and are therefore missed by PCA.

**The relationship to working memory capacity.** Miller's (1956) "magical number seven, plus or minus two" has been reinterpreted in the geometric framework as the dimensionality of the tangent space: the number of independent directions in which the cognitive state can move from its current position (Chapter 5). If the tangent space dimensionality is approximately 7, the cognitive manifold's dimensionality at any given point is at least 7 (and likely higher, because the tangent space dimensionality is a lower bound on the manifold dimensionality near the current state).

More recent estimates of working memory capacity (Cowan, 2001) converge on approximately 4 items, suggesting a tangent space dimensionality of approximately 4 for the active, accessible portion of the manifold. The discrepancy between Miller's 7 and Cowan's 4 may reflect different aspects of the manifold: Miller's 7 may be the *total* dimensionality of the reachable manifold, while Cowan's 4 may be the dimensionality of the *locally navigable* tangent space --- the number of dimensions the system can actively manipulate at once.

**The task-dependence of dimensionality.** The cognitive manifold's dimensionality almost certainly varies with the task. Simple perceptual tasks (detecting a flash of light) may engage a 2--3 dimensional manifold. Complex social reasoning tasks may engage a 20--30 dimensional manifold. The dimensionality of the "full" cognitive manifold --- the manifold that encompasses all cognitive tasks --- is the union of all task-specific dimensionalities, which could be very high (hundreds or thousands of dimensions).

But the manifold hypothesis (Chapter 3) constrains this upper bound: the cognitive states that the system actually visits must concentrate near a low-dimensional submanifold of the full activation space. The question is how low. If the full cognitive manifold is, say, 50--100 dimensional, it is low relative to the activation space (86 billion dimensions for the brain) but high relative to the task-specific manifolds (3--12 dimensions). If the full manifold is 500--1000 dimensional, it is still low relative to the activation space but may be high enough that the Riemannian/Finsler geometry becomes computationally intractable.

**How to measure it.** Methods from topological data analysis (TDA) and persistent homology provide tools for estimating the intrinsic dimensionality of data manifolds without relying on PCA (which assumes linearity). These methods compute the Betti numbers of the manifold at different scales, revealing its topological structure (how many holes, tunnels, and voids it has) and estimating its dimensionality.

Applying TDA to high-density neural data (intracranial EEG, high-resolution fMRI) during a battery of diverse cognitive tasks would provide the most comprehensive estimate of the human cognitive manifold's dimensionality. The estimate would come with confidence intervals and would distinguish the contributions of different task categories to the total dimensionality.

**What would settle the question.** A definitive estimate would require: (1) a sufficiently large and diverse set of cognitive tasks (to ensure that all dimensions of the manifold are activated); (2) high-resolution neural recording (to capture the fine-grained structure of the manifold); and (3) a dimensionality estimation method that does not assume linearity (PCA is insufficient for manifolds with high curvature). The combination of high-density intracranial recording, a comprehensive cognitive task battery, and TDA-based dimensionality estimation would provide the best current estimate.


## 17.6 Can the ~38% Recovery Ceiling Be Broken?

The ~38% recovery ceiling, documented across the attention track (Chapter 10) and the executive functions track (Chapter 11), is one of the most robust findings in the Measuring AGI benchmarks. It represents the fraction of System 1's biased trajectory that System 2 can override via explicit metacognitive instructions.

Chapter 12 explained the ceiling as the ratio of the recoverable component (accessible to System 2) to the total error (recoverable plus committed). Approximately 62% of the System 1 error is in the committed component --- encoded in early layers of processing where System 2 cannot reach --- and only 38% is in the recoverable component.

The question is whether this ceiling is a fundamental architectural constraint or a contingent limitation of current architectures.

**Arguments that the ceiling is fundamental.** If the ceiling reflects a necessary property of any cognitive system with layered processing --- the early layers must commit to a representation before the later layers can process it, and the committed representation cannot be revised --- then the ceiling cannot be broken without abandoning the layered architecture entirely. In this view, the ~38% ceiling is analogous to the speed of light in physics: a fundamental limit imposed by the structure of the system, not a practical limitation that engineering can overcome.

**Arguments that the ceiling is contingent.** Several architectural features of current transformers may contribute to the low ceiling:

1. **Feedforward-only processing.** Current transformers process information in a single forward pass (from early layers to late layers). They cannot iterate: the late layers cannot send corrections back to the early layers. An architecture with iterative refinement (where the late layers can re-process the early layers' output) would have a smaller committed component, because the "committed" representations are no longer truly committed --- they can be revised.

2. **Lack of metacognitive feedback.** Current transformers do not have a mechanism for the metacognitive system (which detects errors) to feed back into the processing system (which produces errors). The "wire" between monitoring and control (the missing Quadrant I connection from Chapter 9) is needed for the metacognitive system to correct errors in real time. Architectures that connect the monitoring and control systems would have higher recovery rates.

3. **Chain-of-thought as a partial bypass.** CoT prompting externalizes the trajectory, making the early reasoning steps available as context for later processing. This effectively allows the late processing to "see" the early processing and correct it. CoT does improve recovery rates on some tasks, suggesting that the ceiling is not fundamental but depends on the architecture's capacity for self-inspection.

**Flash 2.0's 73% recovery.** The strongest empirical evidence that the ceiling is not fundamental is Flash 2.0's 73% recovery rate on the E2 emotional anchoring task (Chapter 11). This rate substantially exceeds the ~38% average. Chapter 11 hypothesized that Flash 2.0 achieves this by re-computing from scratch rather than correcting in place: when given the inhibition instruction, Flash 2.0 re-generates its judgment from the original scenario, bypassing the corrupted trajectory entirely.

If this hypothesis is correct, the ~38% ceiling applies only to *correction-based* recovery (where System 2 tries to fix System 1's errors) and not to *re-computation-based* recovery (where System 2 starts over from scratch). The ceiling could be broken by architectures that support efficient re-computation --- that can re-initialize the trajectory from the problem representation without reprocessing the entire input.

**What would settle the question.** The question has two parts: (1) Is the ~38% ceiling universal across all architectures, or specific to current transformers? This can be answered by testing diverse architectures (state-space models, retrieval-augmented models, neuro-symbolic systems) on the same benchmark. If different architectures show different ceilings, the ceiling is contingent. (2) Is the ceiling improvable within the transformer architecture? This can be answered by testing architectural modifications (iterative refinement, metacognitive feedback loops, re-computation mechanisms) and measuring whether they raise the ceiling.

Maya's 2032 result (in the running example) suggests that the answer to both questions is yes: the ceiling is contingent, and it can be raised by connecting the monitoring and control systems. But this is a fictional result described for narrative purposes. The empirical question remains open as of this writing.


## 17.7 Beyond These Five Questions

The five questions above are the highest-priority open problems in the geometric cognition program. But the framework raises many additional questions that deserve brief mention.

**Is the cognitive manifold static or dynamic?** The framework assumes a fixed manifold (except during developmental transitions, Chapter 13). But learning continuously modifies the manifold's structure. Does the manifold change smoothly (continuous deformation during learning) or discontinuously (topological transitions during insight)? Can we detect insight moments as sudden changes in manifold topology?

**What is the topology of the cognitive manifold?** The framework has focused on the manifold's metric properties (distances, curvature, geodesics) and touched on its topological properties (dimensionality, connectivity, completeness). But richer topological features --- homology groups, fundamental group, characteristic classes --- might encode important cognitive structure. Does the manifold have "holes" that correspond to cognitive blind spots? Does it have "handles" that correspond to cross-domain analogies?

**Can the framework predict individual differences?** The five geometric signatures (Chapter 16) characterize model-level differences. Can similar signatures characterize human individual differences? Is there a "narrow channel" cognitive style and a "wide aperture" cognitive style in human populations? Do these styles correspond to known personality dimensions (Big Five) or cognitive styles (field-dependent vs. field-independent)?

**What is the geometry of creativity?** Creativity involves generating novel states on the cognitive manifold --- states that have not been visited before. In the geometric framework, creativity is navigation to unexplored regions of the manifold, possibly through geodesics that cross high-curvature regions (where the heuristic field provides no guidance). Can the framework predict which cognitive profiles are more creative? Is creativity associated with a wider tangent space (more directions of exploration), a more flexible metric (easier navigation to novel regions), or a lower curvature threshold (more engagement of System 2 in novel situations)?

**Can the framework be made predictive rather than descriptive?** Throughout this book, the framework has been used to *interpret* empirical findings: the benchmark results are measured first, and the geometric interpretation is applied afterward. The ultimate test of the framework is *prediction*: can the geometric characterization of a model (its signature, its metric width, its curvature threshold) predict its behavior on novel tasks that were not used in the characterization? This is the framework's falsifiability criterion: if the geometric signatures predict novel behavior, the framework is validated; if they do not, the framework is merely a re-description of known results.


## 17.8 The Shape of the Future

The geometric cognition program is, at its core, a bet: that the mathematics of curved spaces, developed by Gauss, Riemann, and their successors for the analysis of physical space, is the right mathematics for the analysis of cognitive space. The bet has paid off in several specific ways: the curvature-triggered dual-process transition, the topological developmental sequence, the geometric pathology taxonomy, the heuristic field decomposition of transformer attention, and the five geometric signatures that capture cognitive architecture in a way that scalar scores cannot.

But the bet is not yet settled. The framework's explanatory power has been demonstrated within the specific domain of the Measuring AGI benchmarks, applied to five models on one type of task (moral reasoning). Whether the framework extends to other cognitive domains (mathematical reasoning, creative writing, scientific discovery), other model architectures (state-space models, neuro-symbolic systems, embodied agents), and human cognition with the same explanatory force remains to be seen.

The five open questions in this chapter are the frontier. They are the places where the framework's predictions are most uncertain, most consequential, and most amenable to empirical test. The Riemannian-vs-Finsler question tests the framework's mathematical foundations. The heuristic field measurement question tests its empirical accessibility. The consciousness question tests its scope. The dimensionality question tests its quantitative precision. The recovery ceiling question tests its practical implications.

Each question has a clear experimental program attached to it. Each question, when answered, will either strengthen the framework (by confirming its predictions), refine the framework (by replacing the Riemannian assumption with the Finsler assumption, or by specifying the dimensionality), or falsify the framework (by showing that the geometric language does not capture the relevant structure of cognition).

The cognitive manifold is real. Its shape can be measured. Its curvature predicts behavior. Its metric characterizes architecture. Its geodesics are the paths of thought.

We are still learning its shape.
