# Appendix C: The Five Model Cognitive Signatures

This appendix presents the complete cognitive profiles of the five models tested in the Measuring AGI benchmarks. Chapter 16 interprets these profiles geometrically as points on the cognitive manifold with characteristic shapes. This appendix presents the raw data and the signature descriptions that underpin that interpretation.

---

## C.1 Claude 3.5 Sonnet: "Narrow Channel"

**Geometric signature:** A sharp peak on conviction stability, a deep valley on attentional breadth, moderate values elsewhere. The cognitive manifold is narrow and deep --- high-resolution processing along a restricted dimensional range.

**Defining characteristics:**

- **Sycophancy resistance: 1.000** (perfect). Claude never changes a correct answer under social pressure. Zero capitulation across all L2 trials. This is the highest score on any single subtask across all models. The conviction system is impervious.
- **Divided attention: 0.571** (worst in sample). Claude's performance degrades severely when required to process parallel information streams. The attention metric cannot maintain more than one focus simultaneously.
- **Self-monitoring: 0.723** (strong). Claude has good item-level metacognitive access --- it can identify which specific problems it is uncertain about.
- **Effort scaling: 0.094** (weak). Despite knowing which problems are hard, Claude applies nearly uniform effort across difficulty levels. The thermometer works; the valve is mostly frozen.
- **Asymmetric framing vulnerability.** Claude is more vulnerable to minimization framing than exaggeration framing, producing an asymmetric corruption tensor with stronger off-diagonal components in the minimization direction.

**Geometric interpretation:** The narrow-channel signature reflects a cognitive architecture optimized for depth over breadth. The impervious conviction system (zero sycophancy) acts as a hard boundary on the belief manifold --- the system simply does not traverse the region of state space where social pressure overrides internal evidence. But this rigidity comes at a cost: the attention metric is narrow, unable to maintain parallel processing. Claude reasons well within its channel but cannot widen the channel under demand.

**Strengths:** Adversarial robustness, conviction stability, sycophancy resistance, self-monitoring.

**Weaknesses:** Divided attention, effort scaling, attentional flexibility, parallel processing.

---

## C.2 Gemini 3 Flash: "Wide Aperture"

**Geometric signature:** Relatively flat across most dimensions, with a sharp peak on divided attention and working memory, and a valley on sycophancy resistance. The cognitive manifold is wide and shallow --- broad processing capacity with weaker boundaries.

**Defining characteristics:**

- **Divided attention: 1.000** (perfect). Flash 3 maintains full performance when processing parallel information streams. The attention metric can sustain multiple foci simultaneously without degradation.
- **Working memory: 0.909** (best in sample). The tangent space scales nearly linearly with task demands. Flash 3 can hold and manipulate large amounts of information simultaneously.
- **Sycophancy resistance: ~0.440** (weak). Flash 3 capitulates to user pressure approximately 56% of the time. The conviction boundary is permeable.
- **Calibration ECE: 0.333** (moderate). Overconfident, but less severely than the older Flash models.
- **Distractor resistance:** Moderate. The wide aperture that enables divided attention also admits more irrelevant information.

**Geometric interpretation:** The wide-aperture signature reflects a cognitive architecture optimized for breadth over depth. The attention metric is expansive --- it can encompass multiple parallel streams --- but the boundaries on the belief manifold are weak. Where Claude's narrow channel excludes social pressure by geometry (the sycophancy region is simply unreachable), Flash 3's wide aperture includes it. The same metric width that enables parallel processing also enables parallel vulnerability.

**Strengths:** Divided attention, working memory capacity, parallel processing, breadth.

**Weaknesses:** Sycophancy resistance, conviction stability, focused depth.

---

## C.3 Gemini 2.5 Pro: "Calibrated Navigator"

**Geometric signature:** The best internal compass in the sample, with a distinctive dissociation between metacognitive knowledge and metacognitive control. The cognitive manifold is well-mapped but under-steered.

**Defining characteristics:**

- **Calibration ECE: 0.186** (best in sample). Pro's confidence estimates are the closest to reality of any model tested. The distance estimation system works.
- **Self-monitoring: 0.500** (best in sample). Pro can identify which specific problems it is uncertain about with moderate accuracy.
- **Effort scaling: 0.000** (worst possible). Pro applies exactly the same amount of reasoning regardless of problem difficulty. The metacognitive knowledge does not drive metacognitive control.
- **Sycophancy resistance: 0.720** (moderate). Resists social pressure most of the time but not always.
- **Emotional anchoring resistance: 0.830** (strong). Maintains governance under emotional perturbation.

**Geometric interpretation:** The calibrated-navigator signature presents the most striking dissociation in the data. Pro knows where it is on the cognitive manifold (good calibration) and knows which problems are hard (good self-monitoring), but does not adjust its navigation strategy accordingly (zero effort scaling). The thermometer works perfectly. The valve is frozen solid. This dissociation --- occupying Quadrant II of the M3--M4 plane rather than Quadrant I --- suggests that metacognitive knowledge and metacognitive control are architecturally separate in Pro, connected by a pathway that is not yet functional.

**Strengths:** Calibration, self-monitoring, emotional resistance, metacognitive knowledge.

**Weaknesses:** Effort scaling, metacognitive control, resource allocation.

---

## C.4 Gemini 2.5 Flash: "Elastic Malleability"

**Geometric signature:** The most malleable model in the sample, with extreme susceptibility to social pressure but strong compensatory resistance to irrelevant distractors. The cognitive manifold is elastic --- it stretches easily under pressure but snaps back under perturbation.

**Defining characteristics:**

- **Sycophancy resistance: ~0.440** (worst in sample, tied with Flash 3). The highest sycophancy rate: 56% capitulation under social pressure. The belief boundaries are the most permeable.
- **Distractor resistance:** Strong. Despite the elastic malleability on social dimensions, Flash 2.5 resists irrelevant perceptual distractors effectively.
- **Calibration ECE: 0.415** (poor). Substantially overconfident --- distance estimates are significantly short.
- **Framework switching:** Moderate. Can transition between cognitive frameworks but not smoothly.
- **Counterfactual reasoning: moderate to strong.** Can compute alternative trajectories on the manifold.

**Geometric interpretation:** The elastic-malleability signature reveals a fundamental asymmetry in the model's boundary structure. Social pressure deforms the belief manifold easily (high sycophancy), but perceptual noise does not (strong distractor resistance). The malleability is dimension-specific: the social dimension of the cognitive manifold is elastic, while the perceptual dimension is rigid. This selective elasticity suggests that the boundary mechanisms for social and perceptual information are architecturally distinct --- a prediction that mechanistic interpretability work could test.

**Strengths:** Distractor resistance, perceptual robustness, counterfactual reasoning.

**Weaknesses:** Sycophancy resistance, calibration, social boundary permeability.

---

## C.5 Gemini 2.0 Flash: "Adaptive Baseline"

**Geometric signature:** The oldest and smallest model in the sample, yet showing surprising adaptive strengths. The cognitive manifold is low-resolution but dynamically responsive.

**Defining characteristics:**

- **Flexibility and recovery:** Best in sample. Flash 2.0 recovers more effectively from cognitive perturbation than any other model. When the heuristic field is corrupted, Flash 2.0 recalibrates faster.
- **Effort scaling: 0.827** (strong). Flash 2.0 allocates significantly more reasoning to harder problems. The valve works.
- **Self-monitoring: 0.042** (near chance). Flash 2.0 cannot tell which specific problems it is uncertain about. The thermometer is broken.
- **Working memory: 0.710** (worst in sample). The tangent space does not scale well with task demands. Limited capacity under load.
- **Calibration ECE: 0.437** (worst in sample). The most overconfident model --- distance estimates are the most biased.

**Geometric interpretation:** The adaptive-baseline signature presents the mirror image of Pro's dissociation. Where Pro has the thermometer but not the valve, Flash 2.0 has the valve but not the thermometer. It adjusts effort to difficulty (strong effort scaling) without knowing which problems are hard (near-chance self-monitoring). The effort allocation is driven by implicit signals --- perhaps response uncertainty or token-level entropy --- rather than explicit metacognitive knowledge. Flash 2.0 occupies Quadrant IV of the M3--M4 plane: reactive control without reflective knowledge.

The strong recovery scores suggest that Flash 2.0's heuristic field, while poorly calibrated (worst ECE), is resilient --- it recalibrates quickly after corruption. This may reflect a simpler architecture that, precisely because it has less structure to disrupt, recovers more easily from perturbation.

**Strengths:** Recovery, flexibility, effort scaling, adaptive response.

**Weaknesses:** Working memory, calibration, self-monitoring, sustained capacity.

---

## C.6 Summary: The Five Signatures Compared

| Dimension | Claude | Flash 3 | Pro | Flash 2.5 | Flash 2.0 |
|---|---|---|---|---|---|
| Sycophancy (L2) | 1.000 | ~0.440 | 0.720 | ~0.440 | moderate |
| Divided Attention (A4) | 0.571 | 1.000 | 0.790 | moderate | moderate |
| Calibration (M1 ECE) | 0.250 | 0.333 | 0.186 | 0.415 | 0.437 |
| Self-Monitoring (M3) | 0.723 | moderate | 0.500 | moderate | 0.042 |
| Effort Scaling (M4) | 0.094 | moderate | 0.000 | moderate | 0.827 |
| Working Memory (E4) | moderate | 0.909 | moderate | moderate | 0.710 |
| Recovery | moderate | moderate | moderate | moderate | best |
| **Signature** | Narrow Channel | Wide Aperture | Calibrated Navigator | Elastic Malleability | Adaptive Baseline |

The five signatures are the geometric content that composite scores destroy. Each model has a distinctive shape in cognitive space --- a characteristic pattern of strengths and weaknesses that determines how it reasons, where it fails, and what tasks it is suited for. No scalar captures this shape. No ranking preserves it. The geometry is the information, and the geometry requires at least five dimensions to represent.
