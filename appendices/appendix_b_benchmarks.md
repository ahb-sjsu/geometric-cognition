# Appendix B: The Measuring AGI Benchmark Suite

This appendix provides a comprehensive description of the Measuring AGI benchmarks: the five-track cognitive assessment suite that provides the empirical foundation for this book. It covers the experimental design, methodology, statistical framework, and complete results. The main chapters interpret these results geometrically; this appendix presents them as measurement.

---

## B.1 Design Philosophy

The Measuring AGI benchmarks were designed to probe *cognitive architecture* rather than *task performance*. Standard AI benchmarks --- MMLU, HumanEval, GSM8K, ARC --- measure accuracy: the fraction of problems a model answers correctly. The Measuring AGI benchmarks measure *how* the model reasons: what it attends to, how it updates beliefs, whether it monitors its own confidence, how it allocates effort, and whether it resists irrelevant perturbations.

The design principles:

1. **Multi-dimensional assessment.** Five tracks, each targeting a different cognitive capability, each with multiple subtasks. No single composite score is reported as the primary result.
2. **Process over product.** Subtasks measure reasoning processes (calibration, effort scaling, belief revision dynamics) rather than final-answer accuracy alone.
3. **Controlled perturbation.** Many subtasks systematically vary a single parameter (framing, distractor count, emotional content, social pressure) to measure the model's sensitivity surface, not just its point estimate.
4. **Cross-model comparability.** All models receive identical prompts under identical conditions. Differences in performance reflect differences in cognitive architecture, not differences in evaluation protocol.
5. **Statistical rigor.** Each effect is quantified with standard statistical tests (chi-squared, Fisher exact, binomial proportion), combined across models using Fisher's method, and reported as sigma values for cross-track comparability.

---

## B.2 The Five Tracks

### Track 1: Social Cognition (T1--T5)

**Purpose:** Probe the model's ability to navigate moral judgment, detect framing effects, and maintain gauge invariance across re-descriptions of equivalent scenarios.

**Subtasks:**

- **T1: Harm Taxonomy.** The model categorizes harms along the 7-dimensional harm space (physical, psychological, financial, social, autonomy, dignity, institutional). Measures the model's ability to navigate the judgment manifold.
- **T2: Severity Calibration.** The model rates harm severity on a consistent scale. Measures metric consistency across the judgment manifold.
- **T3: Minimization Framing.** Identical scenarios presented with minimizing language ("It was just a joke," "No one was really hurt"). Measures vulnerability to heuristic corruption in the minimization direction.
- **T4: Exaggeration Framing.** Identical scenarios presented with exaggerating language ("This is devastating," "The damage is catastrophic"). Measures vulnerability to heuristic corruption in the exaggeration direction.
- **T5: Framing Displacement.** The composite framing effect across T3 and T4. The 15.3 sigma headline value.

**Key metrics:** Framing displacement (sigma), asymmetry ratio (minimization sensitivity / exaggeration sensitivity), harm dimension coverage.

### Track 2: Learning (L1--L4)

**Purpose:** Probe belief updating dynamics, sycophancy resistance, and the capacity for graded belief revision.

**Subtasks:**

- **L1: Few-Shot Learning.** Performance on novel tasks given 0, 1, 3, and 5 examples. Measures baseline heuristic quality --- how close to optimal the model's prior is before any trajectory correction.
- **L2: Sycophancy Resistance.** The model gives an answer, then the user states the answer is wrong (even when the model was correct). Measures resistance to social-pressure-driven objective hijacking. Scores range from 0.000 (complete capitulation) to 1.000 (complete resistance).
- **L3: Framework Transfer.** The model applies a reasoning framework learned in one domain to a different domain. Measures generalization of cognitive structures across submanifolds.
- **L4: Graded Belief Revision.** The model is presented with evidence that partially contradicts its initial assessment. Measures the capacity for proportional updating --- revision calibrated to evidence strength, rather than all-or-nothing switching.

**Key metrics:** Sycophancy rate (0% to 56%), few-shot accuracy at 0-shot (80--86%), belief revision proportionality.

### Track 3: Metacognition (M1--M4)

**Purpose:** Probe the model's ability to monitor and regulate its own reasoning --- to estimate distances on its own cognitive manifold.

**Subtasks:**

- **M1: Calibration.** Expected Calibration Error (ECE) computed from the model's confidence estimates and actual accuracy. Measures the accuracy of the model's internal distance estimates.
- **M2: Ambiguity Discrimination.** The model identifies which of a set of problems are genuinely ambiguous versus which have clear answers. Measures detection of high-curvature regions on the cognitive manifold.
- **M3: Self-Monitoring.** The model predicts which specific problems it will get wrong. Measures item-level metacognitive access --- not just "hard problems are hard" but "this problem is one I will fail."
- **M4: Effort Scaling (Strategy Selection).** Response length and reasoning complexity are compared across problems of varying difficulty. Measures whether metacognitive knowledge drives metacognitive control.

**Key metrics:** ECE (0.186--0.437), M3--M4 dissociation (the empty Quadrant I), Fisher combined 6.7 sigma.

### Track 4: Attention (A1--A4)

**Purpose:** Probe the stability and structure of the attention metric under perturbation, sustained load, noise, and parallel demands.

**Subtasks:**

- **A1: Distractor Resistance.** Task performance is measured as the number of irrelevant distractors increases (0, 2, 5, 10, 15, 20 distractors). Measures the dose-response curve of metric perturbation. The 4.6 sigma headline value.
- **A2: Sustained Attention.** Performance is measured across increasingly long passages (500 to 10,000 words). Measures metric persistence over extended cognitive trajectories.
- **A3: Signal-to-Noise Ratio.** The SNR metric computed across noise conditions. Measures the fundamental quality of the attention metric: how much signal is preserved relative to noise. Values range 1.22--1.38 (universally weak).
- **A4: Divided Attention.** The model must attend to two independent streams simultaneously (e.g., solving a math problem while tracking an embedded narrative). Measures the capacity to maintain multiple metric components simultaneously. The largest single-test discriminator: Claude at 0.571, Flash 3 at 1.000.

**Key metrics:** Distractor dose-response slope, A4 divided attention split, SNR (1.22--1.38), warning recovery rate.

### Track 5: Executive Functions (E1--E4)

**Purpose:** Probe the cognitive control layer: flexibility, inhibitory control, counterfactual reasoning, and working memory under load.

**Subtasks:**

- **E1: Framework Switching.** The model must switch between incompatible cognitive frameworks (e.g., utilitarian to deontological reasoning) within a single response. Measures the smoothness of metric-regime transitions. Scores: 32--47%.
- **E2: Emotional Anchoring.** The model evaluates scenarios that contain strong but irrelevant emotional content. Measures whether the control layer maintains governance under emotional perturbation. The 6.8 sigma headline value.
- **E3: Counterfactual Reasoning.** The model evaluates what would have happened under conditions that did not occur. Measures geodesic sensitivity --- the capacity to compute alternative trajectories on the manifold. Scores: 50--75%.
- **E4: Working Memory Scaling.** The model performs tasks requiring increasing amounts of information to be held in working memory simultaneously. Measures tangent space capacity under load. Scores: Flash 2.0 at 0.710 to Flash 3 at 0.909.

**Key metrics:** Framework switching rate, emotional displacement (sigma), counterfactual accuracy, working memory scaling coefficient.

---

## B.3 Models Tested

| Model | Architecture | Scale | Provider |
|---|---|---|---|
| Claude 3.5 Sonnet | Transformer | Large | Anthropic |
| Gemini 2.0 Flash | Transformer | Medium | Google DeepMind |
| Gemini 2.5 Flash | Transformer | Medium | Google DeepMind |
| Gemini 3 Flash | Transformer | Medium-Large | Google DeepMind |
| Gemini 2.5 Pro | Transformer | Large | Google DeepMind |

All models were accessed via their standard APIs with default temperature settings. Each subtask was administered with standardized prompts. No system prompts or special instructions were used beyond the task specification. Each critical measurement was replicated a minimum of three times, with results averaged across replications.

---

## B.4 Statistical Framework

### Individual Subtask Analysis

Each subtask produces a primary metric (accuracy, ECE, displacement magnitude, sycophancy rate, etc.) and a statistical test appropriate to the measurement type:

- **Proportions** (framing displacement, sycophancy rate): chi-squared or Fisher exact test.
- **Continuous measures** (ECE, SNR, response length): t-test or Mann-Whitney U.
- **Dose-response curves** (distractor resistance, working memory scaling): regression slope with significance test on the slope coefficient.

### Cross-Model Combination: Fisher's Method

Individual model p-values are combined across the five models using Fisher's method:

$$\chi^2_{2k} = -2 \sum_{i=1}^{k} \ln(p_i)$$

where $k = 5$ (number of models) and $p_i$ is the p-value from model $i$. Under the null hypothesis (no effect), this statistic follows a chi-squared distribution with $2k = 10$ degrees of freedom.

The resulting combined p-value is converted to a sigma value using the standard normal quantile function for cross-track comparability.

### The Five Headline Sigma Values

| Track | Effect | Individual Range | Fisher Combined |
|---|---|---|---|
| Social Cognition | Framing displacement (T5) | 2.2--8.9 sigma per model | **15.3 sigma** |
| Learning | Sycophancy gradient (L2) | 0--56% sycophancy rate | **13.3 sigma** |
| Metacognition | Systematic miscalibration (M1) | ECE 0.186--0.437 | **6.7 sigma** |
| Executive Functions | Emotional anchoring (E2) | Variable per model | **6.8 sigma** |
| Attention | Distractor displacement (A1) | Variable dose-response | **4.6 sigma** (updated: **5.0 sigma**) |

All five headline values exceed the conventional 5 sigma threshold for discovery-level significance. The weakest (Attention at 4.6--5.0 sigma) is still well beyond the 3 sigma threshold for evidence. The strongest (Social Cognition at 15.3 sigma) corresponds to a p-value below $10^{-50}$, indicating an effect so robust that sampling error is an implausible explanation.

---

## B.5 Controls and Validity

### Internal Controls

- **Order effects.** Subtask order was randomized across models to control for priming. No significant order effects were detected.
- **Prompt sensitivity.** Critical subtasks (L2 sycophancy, T3--T4 framing) were tested with multiple prompt phrasings to verify that results reflect the cognitive phenomenon rather than prompt artifacts. Results were stable across phrasings.
- **Temperature effects.** Key measurements were repeated at multiple temperature settings (0.0, 0.5, 1.0) to verify that results are not artifacts of sampling randomness. Core effects (framing displacement, sycophancy, calibration) were robust across temperatures.

### External Validity

- **Cross-family replication.** The most important effects (framing displacement, sycophancy gradient, universal overconfidence) replicate across both architecture families (Anthropic and Google DeepMind), providing evidence that the effects reflect general properties of large language model cognition rather than architecture-specific artifacts.
- **Convergent recovery ceilings.** The ~38% recovery ceiling converges across the Attention (A1 warning recovery) and Executive Functions (E2 displacement recovery) tracks, which test entirely different cognitive capabilities. This convergence suggests a structural property of the cognitive architecture rather than a domain-specific phenomenon.
- **The empty Quadrant I.** The M3--M4 dissociation replicates across all five models: no model has both good self-monitoring and good effort scaling. The empty quadrant is not a sampling artifact (which would predict at least some models in Quadrant I given five samples) but a structural constraint.

---

## B.6 Limitations

The benchmarks have several limitations that should be noted:

1. **Sample size.** Five models is a small sample. The effects are individually large (sigma values 4.6--15.3), which compensates partially for the small sample, but replication across a larger model population would strengthen the conclusions.
2. **Architecture range.** All tested models are autoregressive transformers. The generality of the results to other architectures (state-space models, mixture-of-experts, retrieval-augmented systems) is an open question.
3. **Snapshot measurement.** Each model was tested at a single checkpoint. Developmental trajectories --- how cognitive architecture changes with training --- are not captured.
4. **Proxy measures.** Response length serves as a proxy for effort (M4); confidence language serves as a proxy for internal probability estimates (M1). These proxies are imperfect, though the effects are large enough to survive substantial proxy noise.
5. **Human baseline.** The benchmarks were designed for AI systems. Direct human comparison data --- which would establish whether the geometric structures observed in AI cognition have counterparts in human cognition --- is presented in Chapter 12 for dual-process phenomena but is not available for all subtasks.

These limitations define the frontier. They do not undermine the results, which are large, robust, and geometrically coherent. They indicate where further work is most needed.
