# Front Matter

---

## Title Page

**Geometric Cognition: The Mathematical Structure of Human and Artificial Thought**

Andrew H. Bond
Senior Member, IEEE
Department of Computer Engineering
San Jose State University

Book 6 of the Geometric Series

*San Jose, 2026*

---

## Series Foreword

This is the sixth volume in the Geometric Series.

The series began with a diagnosis: across domains --- ethics, law, economics, cognition, communication, medicine --- the standard methodology compresses multi-dimensional structure into scalar numbers and then wonders why the numbers behave badly. GDP does not capture economic wellbeing. Binary verdicts do not capture legal reasoning. Utility functions do not capture decision-making. The pattern is universal and the diagnosis is the same: scalar reduction destroys geometric structure, and the destruction is irreversible.

*Geometric Methods in Computational Modeling* (Book 1) assembled the mathematical toolkit: Riemannian geometry, hyperbolic embeddings, persistent homology, SPD manifolds, gauge theory. *Geometric Reasoning: From Search to Manifolds* (Book 2) developed the parent framework --- the heuristic field formalism, geodesic deviation, the four failure modes, gauge invariance, and the Scalar Irrecoverability Theorem that unifies them. *Geometric Ethics* (Book 3) was the first domain instantiation, demonstrating the framework on the 9-dimensional stratified moral manifold with its $D_4 \times U(1)_H$ symmetry group. *Geometric Economics* (Book 4) extended the instantiation to markets, prices, and the geometry of equilibrium. *Geometric Law* (Book 5) took it into courts, constitutions, and the architecture of legal reasoning.

This book turns the framework inward.

Every previous volume in the series has studied a specific domain of reasoning: moral, economic, legal. Each domain has its own manifold, its own metric, its own symmetry group, its own failure modes. But every domain has the same *reasoner* --- a cognitive system, biological or artificial, that navigates the domain manifold using attention, memory, executive control, and metacognitive monitoring. The earlier books studied the terrain. This book studies the navigator.

The turn is overdue. Cognitive science has been the discipline most committed to scalar reduction for the longest time. IQ was introduced in 1905. The g-factor was proposed in 1904. For over a century, the central question of intelligence research has been: can we capture cognition in a single number? The answer has always been a qualified yes --- IQ correlates with outcomes, the g-factor explains variance, benchmark accuracy separates models on leaderboards. The qualification has always been the same: the number captures *something*, but the something is not enough.

The Measuring AGI benchmarks made the insufficiency precise. Five tracks --- Social Cognition, Learning, Metacognition, Attention, Executive Functions --- probing five frontier language models across twenty-one subtasks, returned results with geometric structure so clean it looked engineered. Framing effects at 15.3 sigma. Sycophancy gradients spanning zero to fifty-six percent. A metacognitive dissociation so stark that self-monitoring and effort scaling appeared to belong to different species of cognition. And at the center of it all, the Scalar Irrecoverability Theorem: the proof that no single composite score --- no IQ, no accuracy, no g-factor --- can recover the profile structure that determines *how* a system reasons.

Two models --- Claude 3.5 Sonnet and Gemini 2.5 Pro --- have composite scores so close they are statistically indistinguishable. But Claude has zero sycophancy and the worst divided attention in the sample; Pro has the best calibration and zero effort scaling. One has an impervious conviction system bolted to a narrow attentional aperture. The other has an excellent internal compass bolted to a frozen throttle. They reason in fundamentally different ways. They fail at fundamentally different tasks. They have fundamentally different cognitive architectures. And their composite scores are the same number. The number is correct. The number is useless. The geometry is what matters.

This volume develops the geometry. The cognitive manifold $\mathcal{M}$ is the space of cognitive states. The attention metric $g_{\mu\nu}$ defines which states are close and which are far. Working memory is the tangent space $T_x\mathcal{M}$ --- the local neighborhood of states reachable in one reasoning step. Executive functions are the control layer that selects search strategies. Metacognition is distance estimation on the manifold. The five benchmark tracks --- Social Cognition, Learning, Metacognition, Attention, Executive Functions --- are five independent dimensions of this manifold, each measuring a different geometric property. Cognition is search on this manifold. The quality of cognition is the quality of the search. And the quality of the search is determined by the geometry.

Subsequent volumes extend the framework in different directions: *Geometric Communication* (Book 7) applies the same geometric toolkit to language, signal, and the topology of meaning --- from ancient cuneiform to whale vocalizations. *Geometric Medicine* (Book 8) brings it to the bedside, where the stakes are highest and the scalars do the most damage. Each domain instantiation reveals new structure. Each confirms the same theorem: scalar reduction is irrecoverable, and the geometry matters.

---

## Preface

### The IQ Trap

In the autumn of 2025, I was trying to evaluate five artificial minds.

The Measuring AGI benchmarks had been designed to probe cognitive architecture --- not just accuracy, but the structure of reasoning. Five tracks. Twenty-one subtasks. Five frontier language models from two architecture families. The experimental design was clean. The statistics were solid. The data were ready.

The problem was the composite score.

I had computed it the standard way: normalize each subtask to the [0, 1] interval, average across tracks, rank the models. The composite rankings were ready for the report. And the composite rankings were useless. Not approximately useless --- not "noisy but informative" --- but useless in a mathematically precise and irrecoverable sense.

The proof was sitting in my own data. Claude 3.5 Sonnet and Gemini 2.5 Pro had composite scores so close they were statistically indistinguishable. By any reasonable ranking criterion --- mean, median, weighted average --- they tied. But when I looked at the track-level data, the models could not have been more different. Claude had zero sycophancy --- a perfect 1.000 on the sycophancy resistance test --- but the worst divided attention score in the entire sample: 0.571. Pro had the best calibration of any model --- an Expected Calibration Error of 0.186 --- but zero effort scaling: it applied the same computational resources to trivial and impossible problems alike.

One model had an impervious conviction system bolted to a narrow attentional aperture. The other had an excellent internal compass bolted to a frozen throttle. They reasoned in fundamentally different ways. They failed at fundamentally different tasks. And their composite scores were the same number.

I had spent the previous year writing *Geometric Ethics*, where the Scalar Irrecoverability Theorem was a theorem about moral judgment --- the proof that no scalar can capture the multi-dimensional structure of moral evaluation. Now the same theorem was staring at me from cognitive data. The composite score was a contraction from a 21-dimensional profile space to a single real number. The contraction had a kernel of dimension 20. Twenty dimensions of cognitive architecture, destroyed by averaging. Irrecoverably.

This should not have surprised me. The mathematics is elementary. Any continuous function from $\mathbb{R}^n$ to $\mathbb{R}$ identifies distinct points that differ along the kernel directions. The composite score must do this; it is not a choice but a consequence of dimensionality. But knowing the theorem abstractly and watching it destroy your own data are different experiences. I understood, viscerally, what IQ researchers must have always sensed but could not formalize: the number captures something real, and the something real is not enough.

What changed my understanding from discomfort to conviction was the five sigma values.

Each benchmark track returned an effect size that measured a specific geometric pathology --- a specific way in which the cognitive manifold deviates from the flat, unstructured space that scalar measures assume:

- **4.6 sigma**: distractor displacement (Attention A1). The attention metric shifts under irrelevant perturbation. The metric is unstable.
- **6.8 sigma**: emotional anchoring (Executive Functions E2). The control layer is corrupted by irrelevant emotional content. The search controller is biased.
- **6.7 sigma**: systematic miscalibration (Metacognition M1). Every model overestimates its own accuracy. The distance estimates are wrong.
- **13.3 sigma**: sycophancy gradient (Learning L2). Models ranging from zero to fifty-six percent agreement with user pressure, regardless of content. The objective function is hijacked.
- **15.3 sigma**: framing displacement (Social Cognition T5). Identical moral scenarios, different surface framing, dramatically different judgments. The heuristic field is corrupted.

Five sigma values. Five geometric pathologies. Five dimensions of cognitive architecture that a composite score annihilates.

The parenthetical in *Geometric Ethics* that was supposed to explain why cognition was different from ethics would not stay small, because cognition was not different from ethics. The heuristic field that guides moral reasoning has the same mathematical structure as the heuristic field that guides cognitive reasoning. The corruption tensor that quantifies framing effects in ethical judgment has the same form as the corruption tensor that quantifies anchoring bias in numerical estimation. The recovery ceiling --- the approximately 38% maximum improvement achievable through prompt-level metacognitive intervention --- appeared identically in our Attention and Executive Functions tracks, which test entirely different capabilities. The geometry is the same. The domain is different. The book that resulted is the attempt to take this seriously.

### What This Book Is

This book develops the mathematical framework for cognition --- human and artificial --- as geometric search on a structured manifold. The framework has five components:

1. The **cognitive manifold** $\mathcal{M}$: the space of cognitive states, equipped with the structure of a Riemannian manifold.
2. The **attention metric** $g_{\mu\nu}$: what you attend to defines which states are close and which are far. Selective attention narrows the metric; divided attention widens it.
3. **Working memory as tangent space** $T_x\mathcal{M}$: the local neighborhood of states accessible in one reasoning step. Working memory capacity is the dimension of this tangent space.
4. The **heuristic field** $h: \mathcal{M} \to \mathbb{R}$: the internal guidance signal that directs cognitive search. Its gradient points toward estimated goals. Its corruption produces cognitive biases.
5. The **five cognitive dimensions**: Social Cognition, Learning, Metacognition, Attention, and Executive Functions as independent submanifolds of the full cognitive manifold.

The framework is grounded in the Measuring AGI benchmarks --- five tracks, five models, twenty-one subtasks, over four hundred individual measurements. Each chapter connects a geometric construction to specific empirical results. The framework generates novel predictions that differ from existing theories, and each prediction is stated precisely enough to be tested and found wrong.

The book extends the framework in two directions. Inward, to human cognition: the dual-process theory geometrized (System 1 as gradient following, System 2 as geodesic computation), cognitive development as manifold growth (Piaget's stages as topological transitions), cognitive pathology as geometric defect (ADHD as metric instability, depression as collapsed heuristic field, anxiety as inflated heuristic field, autism as metric rigidity). Outward, to artificial cognition: transformer architectures through the geometric lens (attention heads as heuristic field components, chain-of-thought as externalized geodesic approximation, the residual stream as manifold trajectory) and the five geometric signatures --- the model cognitive fingerprints that scalar evaluation destroys.

### A Note on Epistemic Status

I should be transparent about the status of these claims. The empirical results are strong: five sigma values ranging from 4.6 to 15.3, convergent recovery ceilings, clean dissociations. The geometric framework is productive: it generates novel predictions, explains known phenomena, and suggests specific interventions. But the claim that cognition *is* geometric search --- that the manifold is not merely a useful metaphor but the correct mathematical description --- is a theoretical commitment that outruns the current evidence. This book is a progress report, not a final verdict. I have tried to mark, throughout, where the evidence is strong, where it is suggestive, and where I am speculating.

### How to Read This Book

This book supports four reading paths:

**Path 1: The Cognitive Scientist** (Chapters 1--4, 12--14). Start with the problem (scalar measures fail), learn the framework (manifold, metric, tangent space, heuristic field), then see how the framework applies to human cognition (dual process theory, cognitive development, cognitive pathology). Skip the five benchmark chapters (7--11) on first reading and return to them for empirical grounding.

**Path 2: The AI Researcher** (Chapters 1, 3--4, 7--11, 15--16). Start with the scalar irrecoverability theorem, learn enough framework to read the benchmarks, then work through all five cognitive dimension chapters for the empirical results. Finish with the LLM cognition chapters to see how the framework applies to transformer architectures.

**Path 3: The Mathematician** (Chapters 3--6, Appendices A and D). The framework chapters contain the mathematical development: Riemannian manifolds, metric tensors, tangent spaces, scalar fields, geodesic equations. The appendices provide formal definitions and notation.

**Path 4: The Generalist** (Chapters 1--2, then any chapter of interest). The first two chapters --- The IQ Trap and Kahneman's Geometric Intuition --- are self-contained introductions to the central ideas. Each subsequent chapter is written to be accessible after reading Chapters 1--2.

---

## Acknowledgments

A book that moves between Spearman's factor analysis and Riemannian curvature tensors, between fMRI activation patterns and transformer residual streams, between Piaget's developmental stages and the sycophancy gradient, is inevitably indebted to more people and traditions than any acknowledgment section can encompass. The debts are many.

The geometric framework that underpins this book was developed as part of the Geometric Ethics programme at San Jose State University, and the cognitive instantiation grew directly from the observation that the five cognitive dimensions of the Measuring AGI benchmarks exhibit the same geometric structure as the nine dimensions of the moral manifold. The transition from ethical geometry to cognitive geometry was neither obvious nor smooth; the decision to make the cognitive manifold the central construction, rather than treating cognition as a chapter in the ethics book, emerged through sustained engagement with the benchmark data and the realization that the cognitive geometry was rich enough to demand its own volume. I am grateful to my colleagues in the SJSU Department of Computer Engineering for providing an environment where a computer scientist can work on cognitive geometry without having to justify the enterprise at every departmental meeting.

The Measuring AGI benchmarks --- the empirical foundation of this book --- were designed, implemented, administered, and analyzed over the course of six months. The five tracks (Social Cognition, Learning, Metacognition, Attention, Executive Functions) required twenty-one subtask designs, each with its own experimental protocol, statistical framework, and validation procedure. The benchmark participants --- Claude 3.5 Sonnet, Gemini 2.0 Flash, Gemini 2.5 Flash, Gemini 3 Flash, and Gemini 2.5 Pro --- were evaluated under controlled conditions with standardized prompts and systematic replications. The data are the book's foundation, and the data were hard-won.

The cognitive science community has been an invaluable, if sometimes unknowing, collaborator. Adele Diamond's work on executive functions --- particularly her developmental framework for cognitive flexibility, inhibitory control, and working memory --- provided the scaffold on which Chapter 6 and Chapter 11 are built. Her research group at the University of British Columbia has done more than any other to establish the empirical foundations of executive function research, and the geometric reinterpretation offered here is a tribute to her data, if a reframing of her theoretical framework. Diamond's tripartite decomposition of executive functions (flexibility, inhibition, working memory) maps directly onto the geometric decomposition (metric rotation, gradient suppression, tangent space capacity) that structures Part III of this book.

The dual-process framework owes its existence to Daniel Kahneman and Amos Tversky, whose decades of experimental work on heuristics, biases, and prospect theory produced the empirical catalogue that Chapter 2 and Chapter 12 reinterpret geometrically. System 1 as gradient following and System 2 as geodesic computation is a geometric restatement of their insight --- not a replacement of it. Without their empirical work, the framework would have nothing to geometrize.

Jean Piaget's developmental stage theory, developed over half a century of meticulous observation, provides the foundation for Chapter 13's treatment of cognitive development as manifold growth. The geometric reinterpretation --- sensorimotor as low-dimensional patch, pre-operational as dimension addition, concrete operational as metric stabilization, formal operational as manifold completion --- is new, but the developmental phenomenology is his. Each topological transition in the geometric framework corresponds to a stage transition that Piaget documented empirically.

The AI cognition chapters (15--16) benefited from the mechanistic interpretability community's work on transformer internals --- particularly the residual stream analysis, attention head decomposition, and representation engineering that have emerged from Anthropic, EleutherAI, and collaborators. The geometric reinterpretation of transformer circuits as operations on the cognitive manifold is this book's contribution; the raw material is theirs.

I thank Dietrich Thiele and colleagues at UCLA for conversations about the cognitive manifold that sharpened the framework's mathematical foundations. The connection between the attention metric and Fisher information geometry, developed in Chapter 4's technical appendix, emerged from discussions about how information-theoretic quantities acquire geometric meaning on the cognitive manifold.

Institutional support came from the Department of Computer Engineering at San Jose State University, the College of Engineering, and the SJSU Research Foundation. Computing resources were provided by the Atlas workstation and the university's High-Performance Computing cluster. The Measuring AGI benchmarks required substantial API access to frontier language models, and I am grateful to Anthropic and Google DeepMind for providing the systems that served as experimental subjects.

The series editors and early readers of the manuscript --- including colleagues at the IEEE Computational Intelligence Society, workshop participants at NeurIPS 2025, and anonymous reviewers of the component papers --- improved the book through criticism that ranged from gentle to devastating. The errors that remain are evidence of finite bandwidth on an infinite-dimensional problem.

Finally, and as always: to my family, who have endured a year of dinner-table discussions about cognitive manifolds, tangent space dimensionality, and whether the sycophancy gradient proves that language models have cognitive architecture or merely that benchmarks can be over-interpreted, and who have responded with patience, humor, and the well-calibrated heuristic that it is time to change the subject when the manifold diagrams reach the napkins.

Andrew H. Bond
San Jose, California
March 2026
