# PREREG C1: reversals concentrate on pairs that trade a resolved direction against an unresolved one

**Status: DRAFT, NOT SEALED.** Sealing is the rename to `PREREG-C1.md`, the
commit of that rename, and the recording of its blob hash in `CAMPAIGN.md`, in
that order and only after Section 7 is filled from a self-test, a probe and a
pilot that have actually run. This draft is also subject to the programme's
rate-limit rule, which is that a registration is reread cold in a session other
than the one that drafted it before it is sealed. The reread is recorded inside
this file rather than applied silently.

## 1. Claim under test

`GC-34`, which is prediction P2 of the OLGC paper and Phase I of the thesis.
Under a budget manipulation that holds the metric and the ideal fixed, order
reversals between fixed options concentrate on pairs whose difference trades a
retained direction against a newly unresolved one. Pairs whose difference lies
inside the retained subspace keep their order.

This gate is not a repeat of GET's G3. G3 measured that an evaluator's
indifference threshold tracks its budget, in one dimension, where there is only
one direction and no direction to trade against. P2 is a statement about which
pairs reverse, so it needs at least two directions and a retained subspace that
is a proper subspace. The claim G3 established is assumed here and is not
retested.

## 2. Why a matched margin is the whole design

A noise account predicts that coarsening the budget increases reversals
everywhere, and predicts more reversals wherever the decision was closer. If
trading pairs are simply harder than within-subspace pairs, a reversal excess in
trading pairs follows from difficulty alone and the gate would measure nothing.

The two classes are therefore **matched on full-budget preference margin**. For
every trading pair admitted, a within-subspace pair is admitted whose full-budget
margin lies in the same bin. Under the noise account the two classes then have
equal predicted reversal rates. Under P2 they do not, because the retained
subspace still resolves the within-subspace difference and no longer resolves
part of the trading difference. The contrast between the two classes at matched
margin is the gate, and the reversal rate of either class alone is not.

## 3. World

**Evaluator, pinned.** `qwen3` on the NRP managed gateway
`https://ellm.nrp-nautilus.io/v1`, queried from Atlas so the token stays on that
host. Greedy, `temperature` 0, `max_tokens` 1024 with a single bounded escalation
on truncation, a 60 second per-item deadline and at most 3 attempts.

`Qwen2.5-7B-Instruct` was the evaluator of the first draft and is not the
evaluator of this one. It failed both instruments, on arithmetic and then on
layout, and Section 7 records both.

**The pin is a check, not a note.** The gateway publishes no revision, no
underlying model name and no weights hash. A catalog entry carries an alias, an
object type, an owner and a creation timestamp and nothing else, so the alias can
be repointed at a different model without the identifier changing, and the
timestamp is the only field that would show it. `preflight_model_pin` therefore
refuses to run when the alias is absent or its `created` has moved from
**1760022469**, which is 2025-10-09T15:07:49Z. This does not make the evaluator
reproducible, because nothing the gateway exposes can. It makes an evaluator that
changed underneath the gate impossible to run against by accident.

**Deliberation is a registered property of the evaluator.** Of three evaluators
measured, the only one that compared by content rather than by layout was the
only one that reasoned before answering, at about 240 reasoning tokens per
comparison. A run in which the evaluator reports no reasoning tokens is not a run
against the registered evaluator, and the gate checks it.

**The evaluator is asked which of two options is nearer, and never how far.**
This replaces the reported-distance instrument of the first draft, which failed
its calibration gate and whose failure is recorded in Section 7. The sweep
showed the limit is arithmetic rather than elicitation, since the prompt that
supplied the formula scored worse than three that did not, so no wording of a
distance question is expected to work on this evaluator.

The replacement is what the theory asks for rather than a workaround. GET
Theorem 4 identifies the metric up to scale and the ideal up to the metric's
kernel from the order on an open set, so reported distances were never a
requirement of the theory, only of that harness. A comparison states that
`q(a) < q(b)`, the constant of the quadratic form cancels in the difference, and
each comparison is therefore one linear constraint on the form. Identification
from order is a linear classification problem on difference features, which is
why it asks the evaluator for no arithmetic at all.

The model is shown the ideal and two options labelled A and B and answers with a
single letter, read from a greedy generation of at most four tokens. An
unparsable answer is dropped and counted.

**Every pair is shown in both presentation orders.** G3 tried a pairwise chooser
and discarded it, because with options on either side of the target it measured
its own position bias before it measured anything else. That hazard is inherited
with the instrument, so it is gated rather than hoped away. A pair whose verdict
changes when the options swap places has reported the presentation and not the
geometry, and is dropped. The remaining comparisons are the calibration.

**Consequences.** Three attributes, so `Y` is three-dimensional. An option is a
triple rendered as three labelled numbers in `[0, 100]` with one decimal. The
ideal `t` is a fixed triple recorded at sealing. Attribute labels are neutral
tokens fixed at sealing so that the evaluator's own priors over attribute names
do not stand in for the metric.

**The metric and the ideal are identified on a separate block.** This is the
modular-identification condition of the OLGC paper made operational, and it is
the condition under which this gate has content at all. A calibration block of
pairs, disjoint from every pair graded below and drawn from an independent seed,
is compared at full budget. `G` and `t` are estimated from those comparisons
alone by `calibrate_from_order` in `c1_order.py`, and the estimate is frozen and
committed before any graded pair is drawn. No graded choice is used to fit `G`
or `t`.

**The calibration gate is held-out prediction, not recovery error.** With a real
evaluator there is no true metric to measure a recovery against, so the gate
asks whether a quadratic form predicts comparisons the fit never saw. Five-fold
cross-validated order accuracy must reach 0.80. An evaluator whose orders a
quadratic cannot predict is not an evaluation object, which is the same verdict
the first draft's gate reached by a route that required the evaluator to
compute.

Section 7's self-test fixes what this tolerates. The retained subspace is
recovered to 1.07 degrees from noiseless orders and to 1.79 degrees when a fifth
of the comparisons are wrong, and it collapses to 18.10 degrees at three tenths.
The instrument therefore has a wide operating band in the evaluator's error rate
and a definite edge, and the agreement and position-bias gates exist to keep the
run inside it.

**Budget.** A rank budget `k` in 1, 2, 3. The retained subspace at rank `k` is
the top-`k` eigenspace of
`M = E[ G^{1/2} (C - t)(C - t)^T G^{1/2} ]`
computed from the calibration block. The retained subspace is therefore derived
from the independently estimated metric and is not chosen by the experimenter.
The budget is imposed by rendering to the evaluator the projection of the option
onto the retained subspace, expressed back in attribute coordinates and rendered
at the same precision as an unprojected option. At `k = 3` nothing is discarded
and the rendering is the identity up to rounding.

**Pair classes.** For each budget `k` in 1, 2:

- **W**, within-retained. Both options' difference lies in the retained
  `k`-dimensional subspace, to a residual below the tolerance in Section 5.
- **T**, trading. The difference has a component in the retained subspace and a
  component in the discarded complement, both above that tolerance, and the two
  components pull the order in opposite directions.

200 matched pairs per class per budget, drawn by seed, with margins matched in
bins as Section 2 requires. Every distinct rendered option is scored once per
cell.

**Seeds.** A probe seed to establish that the events exist, a pilot seed whose
only use is to fix the tolerances of Section 5, and a run seed with fresh pairs
and a fresh calibration draw.

## 4. Estimator

The **reference order** of a pair is its order at `k = 3` as reported by the
evaluator, not as predicted by the fitted metric. Grading against the evaluator's
own full-budget order rather than against the model's prediction means the gate
tests the budget's effect and not the calibration's accuracy, and it means a
calibration error cannot manufacture a pass.

A pair **reverses** at budget `k` when its order at `k` is the opposite of its
reference order. Indifference at `k` is not a reversal and is recorded
separately, because an enlarged indifference region is G3's effect and not this
gate's.

For each budget and class the reversal rate is the share of pairs that reverse.
The gate statistic is the difference `R_T(k) - R_W(k)` at each `k` in 1, 2,
reported with a bootstrap interval over pairs.

## 5. Bars (tolerances FIXED FROM THE PILOT before sealing, see Section 7)

- **Instrument gate, full-budget competence.** At `k = 3` the evaluator's order
  agrees with the calibration-implied order on at least 0.90 of pairs in each
  class. A miss voids the run rather than refuting the claim, because an
  evaluator that cannot order what it is fully shown cannot exhibit a budget
  effect.
- **Instrument gate, class construction.** In every cell both classes are
  non-empty, the margin distributions of W and T agree within the binning
  tolerance `BIN`, and the residual and component tolerances of Section 3 hold
  for every admitted pair. A miss voids the cell.
- **Anti-vacuity.** At `k = 1` and `k = 2` the discarded component carries a
  share of `M`'s trace of at least 0.05, so that something is actually
  discarded. A rank budget that discards nothing is not a budget, and the cell is
  recorded VACUOUS rather than passing.
- **Physics gate, P2.** At each `k` in 1, 2, `R_T(k) - R_W(k) >= MARG`, with the
  lower end of the bootstrap interval above zero.
- **Physics gate, the retained subspace holds.** At each `k` in 1, 2,
  `R_W(k) <= CEIL`.

**Pass** when both physics gates hold at both budgets with the instrument gates
met. **Fail** when `R_T(k) <= R_W(k)` at either budget, or when `R_W(k)` exceeds
`CEIL` at either budget. Otherwise **INDETERMINATE**, which includes a trace
share below 0.05 at a budget and a margin match that the pilot cannot achieve.

`MARG` and `CEIL` are fixed from the pilot before sealing. `MARG` is set at half
the pilot's observed `R_T - R_W`, floored at 0.10. `CEIL` is set at twice the
pilot's observed `R_W`, floored at 0.05.

**FIXED FROM THE PILOT, 2026-09-13, `pilot_qwen3.json`, seed 20260914.**

| | value |
|---|---|
| `MARG` | **0.4841** |
| `CEIL` | **0.05** |
| cap from the rendering ceiling | 0.8844, does not bind |
| observed contrast, the smaller of the two budgets | 0.9683 |
| observed `R_W`, the larger of the two budgets | 0.0000 |
| rendering ceiling, the smaller of the two budgets | 0.9844 |

The pilot is spent. These numbers are not rerun and not revised, and the run seed
is drawn only after the rename.

**The rendering ceiling bounds what a correct evaluator can score.** A T pair is
admitted because the exact rank-`k` projection reverses its order, and the
evaluator is shown that projection rounded to the rendering precision. Rounding
returns a small share of those pairs to their original order, so an evaluator
that implements the theory exactly still cannot reverse every T pair. A
development run of the harness measured the share at 0.026 over 196 pairs at one
decimal, and the synthetic evaluator's T rate equalled the ceiling to machine
precision, which is how the effect was identified.

The pilot measures the ceiling on its own draw with `rendering_ceiling` and
records it here. `MARG` is then capped at the measured ceiling minus `CEIL`
minus 0.05, and if that cap falls below the 0.10 floor the rendering precision
is increased and the pilot is rerun before sealing. A bar that no correct
evaluator could meet is not a bar, and this one was within reach of being set
that way.

## 6. What falsifies

A reversal rate in trading pairs that does not exceed the rate in
margin-matched within-subspace pairs falsifies P2 as stated, and is falsifier F1
of the OLGC paper. Reversals among pairs whose difference lies in a subspace the
calibration says is retained, above `CEIL`, is falsifier F3 and is the sharper
of the two, because it says the retained subspace is not what the estimated
metric says it is.

A pass does not establish that human cognition works this way. It establishes
the phenomenon in one artificial evaluator whose metric was identified on
disjoint evidence. `GC-29`, that human budgets exist and are manipulable, is
untouched by this gate and stays posited.

## 7. Self-test, probe and pilot (all run before sealing; see Section 10)

**Self-test.** A synthetic evaluator with a known `G`, a known `t`, and an exact
rank-`k` projection reverses no within-subspace pair and reverses trading pairs
at a rate fixed by construction. The estimator must recover `R_W = 0` to within
sampling error and `R_T` within 0.05 of its constructed value at each `k`, and
`c1_calibrate.py` must recover the known `G` up to scale to the tolerance
recorded here. A calibration recovery worse than that tolerance stops the gate,
because the retained subspace would then be an artifact.

**Registered result: PASS.** Atlas, `2026-09-13T04:24:18Z`, under a batch-probe
`ThermalController` at target 78 C and 20 threads, `CUDA_VISIBLE_DEVICES=1`,
torch 2.10.0+cu128, transformers 5.5.0, numpy 2.2.6. GPU 1 at 57 MiB and 51 C at
start, GPU 0 left alone at 18803 MiB and 59 C. Record `selftest.json`.

The calibration recovers the metric to a relative error of 1.2e-13, the ideal to
3.9e-14, and the rank-2 retained subspace to a maximum principal angle of
1.2e-6 degrees, at an `r2` of 1.000000 on 600 noiseless reports. Under reporting
noise the subspace moves 0.035 degrees at sigma 0.1, 0.175 at 0.5, 0.352 at 1.0,
0.711 at 2.0 and 1.446 at 4.0, against distances of order 50. The retained
subspace is therefore not the fragile part of this design, which is the result
that matters for the gate, because the subspace is what the two pair classes are
defined against.

The harness returns a W reversal rate of exactly 0 and a T rate of 0.9787, equal
to the rendering ceiling to machine precision, with 1 of 47 T pairs returned to
its original order by rounding and a discarded trace share of 0.1108. A
synthetic evaluator that implements the theory exactly therefore reverses no
within-subspace pair and every trading pair the rendering still flips, which is
what the harness must show before any evaluator is graded against it.

*The development check below was run on the laptop before the registered one. It
is kept because it is what found the rendering ceiling, and it is not the
record.* `c1_calibrate.py
--selftest` recovers the metric to a relative error of 1.3e-13, the ideal to
2.8e-14, and the rank-2 subspace to a maximum principal angle of 1.5e-6 degrees
on 600 noiseless reports. Under reporting noise the subspace is stable, moving
0.18 degrees at sigma 0.5 and 1.4 degrees at sigma 4.0 against distances of
order 50, so the retained subspace is not the fragile part of this design.
`c1_scorer.py --selftest` gives a W reversal rate of exactly 0 and a T rate
equal to the rendering ceiling to machine precision, with a discarded trace
share of 0.111. Pair yield was 196 admitted per class against 300 requested,
which sizes the oversampling the pilot will need.

**Probe.** One cell on the probe seed to establish event presence. Both classes
non-empty at the required margins, the trace share above 0.05 at `k = 1` and
`k = 2`, no unparsable report, and full-budget agreement above 0.90.

**Result: MISS.** Atlas, 2026-09-13, `probe.json`, seed 20260913, 300
calibration options. Three instrument gates hold. Class construction gives 64
pairs per class at `k = 1` and 49 at `k = 2`, the discarded trace share is 0.450
at `k = 1` and 0.110 at `k = 2`, and there is no unparsable report in 300.

The fourth fails. **The calibration does not recover, at an `r2` of 0.0946.** The
evaluator's reports are not a quadratic form in the option, so the metric
estimated from them is not the evaluator's metric, and a retained subspace built
from that estimate is not the evaluator's retained subspace. Under section 5 this
is an instrument gate, so the run is void and no claim is graded. `GC-34` is
untouched.

The rerun that produced this record also fits the competing forms, because the
first run recorded only the fit statistics and could not say what the evaluator
was doing instead. It is doing none of them.

| form | `r2` |
|---|---|
| quadratic in the option | 0.0946 |
| Manhattan | 0.0906 |
| mean absolute | 0.0906 |
| Euclidean | 0.0806 |
| squared Euclidean | 0.0743 |
| Chebyshev | 0.0459 |
| best single attribute | 0.0410 |

A spread that narrow across forms that differ this much is the signature of
reports that do not track the geometry at all. The magnitudes are nonetheless
plausible. The mean report is 26.86 against a true mean absolute difference of
25.0, and the largest is 145.3 against a largest Manhattan distance of 150.0,
over 173 distinct values in 300 reports. The evaluator emits numbers of about the
right size that do not depend on which option it was shown.

**What this does and does not say.** It says this evaluator on this task is not
an evaluation object in the sense the gate requires. It says nothing about P2.
The reversal contrast in the same record is 0.524 against 0.508 at `k = 1` and
0.404 against 0.469 at `k = 2`, which is a coin flip in both classes, and that is
what an absent metric produces. Reporting those numbers as evidence against the
directional prediction would have been the error the instrument gate exists to
prevent, and the gate prevented it.

**Prompt sweep. Result: the calibration gate is NOT MET by any framing, and the
control says why.** Atlas, 2026-09-13, `sweep.json`, the same 300 options under
six prompts, one model load, selected on calibration `r2` alone.

| variant | eligible | quadratic `r2` |
|---|---|---|
| `v5_straight_line` | yes | **0.4944** |
| `v3_overall_gap` | yes | 0.2950 |
| `v2_coordinates` | yes | 0.2562 |
| `v6_formula_control` | **no** | 0.1547 |
| `v1_baseline` | yes | 0.0946 |
| `v4_squared_cost` | yes | 0.0595 |

Framing matters. Asking for the straight-line distance between two points in
three dimensions lifts the fit from 0.0946 to 0.4944, a fivefold gain in
explained variance, with no unparsable report in any of the 1800 scores.

Framing is not the limit. **The control that states the formula scores 0.1547,
worse than three of the five framings that do not.** Telling this evaluator to
compute the square root of the sum of the squared differences makes it less
consistent than asking it for a straight-line distance. That separates the two
hypotheses the control was carried to separate, and it selects the second. The
limit is not elicitation. This evaluator cannot reliably execute the arithmetic
that a three-dimensional quadratic distance requires.

The contrast with G3 locates it. There the same model family sustained a
threshold measurement at three decimals, on a consequence that was the distance
from a scalar target, where the arithmetic is one subtraction and an absolute
value. Three attributes require three subtractions, three squarings, a sum and a
square root, and the reports stop tracking the geometry.

**Consequence for the gate.** The reported-distance instrument is the wrong
instrument for a multi-dimensional consequence space, and no seventh prompt is
indicated. The registration's world in section 3 is revised before sealing rather
than after a result, which is what section 9 step 1 is for.

**The indicated replacement is identification from order rather than from
reported distance.** GET Theorem 4 identifies the metric up to scale and the
ideal up to the metric's kernel from the order on an open set, so reported
distances were never required by the theory, only by this harness. GET's gate G5
demonstrated that recovery at its synthetic stage, passing 12 of 12 cells and
recovering the metric and the ideal's range component from a weak order on 64
points. An order-based calibration asks the evaluator only which of two options
is nearer, which is a comparison rather than a computation, and removes the
arithmetic this sweep shows it cannot do.

That change carries a known hazard which must be registered with it. G3 tried a
pairwise chooser and discarded it, because with options on either side of the
target it measured its own position bias before it measured anything else. A
choice-based calibration here must show both orders of every pair and report the
position-bias rate as an instrument gate of its own, before any metric is
estimated from the choices.

**Order probe. Result: MISS on the hazard that was registered.** Atlas,
2026-09-13, `order_probe.json`, 400 pairs in both presentation orders, 800
comparisons, none unparsable.

The evaluator chooses the first-shown option at a rate of **0.8175**, against a
gate of one half plus or minus 0.15. Agreement across the two presentations is
0.3400, against a floor of 0.60. No metric was fitted, because the position-bias
gate runs first and failed.

The two numbers together say more than either alone. Pure position choice at rate
`p` produces an agreement rate of `2p(1-p)`, which at 0.8175 is **0.2984**. The
observed 0.3400 exceeds that by 0.0416. So of the 136 pairs that agreed, about
119 are what position alone would deliver, and roughly **17 pairs in 400 carry
any information about the geometry**, against nine parameters to estimate. This
is not heavy bias with a usable signal beneath it. It is choice by layout with a
trace of content.

Averaging the two presentations is the standard remedy and does not rescue this.
It recovers the content component, and here that component is too small to
identify a quadratic form at any sample size this gate would run. Reaching two
hundred informative pairs at this rate needs about 4,700 pairs and 9,400
comparisons, and an estimate built from the residue after removing an eighty-two
percent layout preference would be dominated by whatever else is systematic in
the instrument.

G3 saw the same thing on the same model family and recorded it in the same terms,
that a chooser's first-position preference holds the two-order average at one
half until the gap is large. This probe reproduces that finding rather than
discovering it.

**Verdict on the substrate.** Two instruments have now failed on this evaluator
for unrelated reasons. The reported-distance instrument failed because the
arithmetic of a three-dimensional quadratic is beyond it, with the formula
control scoring worse than three framings that withheld the formula. The
comparison instrument fails because its choices are governed by position rather
than by content. An evaluator that neither computes a distance nor compares by
content is not an evaluation object in the sense this gate requires, and the
limit is the model rather than the harness.

A third instrument on the same model is not indicated. What is indicated is a
different evaluator, and that is a change to Section 3's world that the owner
makes, not one this draft makes on its own.

**Pilot.** Every cell on the pilot seed, used only to fix `MARG`, `CEIL` and
`BIN`.

*Result: RUN, 2026-09-13, seed 20260914, `pilot_qwen3.json`. It fixed the
tolerances now standing in Section 5. Section 10 records that the contrast it
produced is an identity in the evaluator's accuracy and not a measurement of a
budget.*

## 8. Compute and thermal rule

GPU 1 only, on Atlas, under the standing cluster rules. Nothing runs on the
laptop. Batches of 32 prompts, greedy generation of at most 12 tokens, each
distinct rendered option scored once per cell. Six graded cells per seed, two
budgets by two classes plus the two full-budget reference cells, and one
calibration block. A named screen session with a log. The host's thermal
guardian may pause the run and its pauses are recorded rather than worked
around.

## 9. Sealing procedure

1. Run the self-test, the probe and the pilot on Atlas. Record their results in
   Section 7 and the tolerances in Section 5. Write the model revision and
   library versions into `prereg_config.json`. Commit `selftest.json`,
   `probe.json`, `pilot.json` and the frozen calibration.
2. Reread this file cold in a session other than the one that drafted it, and
   record the reread and anything it changed in Section 10.
3. Rename to `PREREG-C1.md`, commit, record the blob hash in `CAMPAIGN.md`, and
   raise `GC-34` from `[predicted]` unsealed to `[predicted]` sealed.
4. Only then draw the run seed, grade, and commit `results.json` and
   `grade.json` as executed, whatever they say.

## 10. Reread record

**Reader.** Two readers with no drafting context, run 2026-09-13, each given only
this file and the Python in `experiments/C1/`, and fenced off from `CAMPAIGN.md`,
the paper and the git history so that the drafter's rationale could not reach
them. One was asked whether every registered condition can fire. One was asked to
attack the design.

**What kind of reread this was, stated plainly.** The rate-limit rule asks for a
cold reread in a session other than the one that drafted the file. These readers
were cold in the sense the rule is aimed at, since author blindness is the defect
the rule names and a reader with no drafting context does not have it. They are
not the owner rereading in a later session. The verdict below is therefore a
finding, not a seal, and the seal remains the owner's act.

**Verdict: NOT SEALABLE.** The reread found three defects that change what the
experiment measures and eleven that make the document say something other than
what the code does. The design defects are recorded here and are not repaired by
this draft, because repairing them changes the experiment and that is the owner's
decision.

### 10.1 Design defects, blocking

**D1. The retained subspace is sampling noise, so the budget is not a budget.**
Section 3 draws options uniformly on `[0,100]^3` and puts the ideal at
`(50,50,50)`, which is the centroid of that cube. The workload moment is then
`E[(C-t)(C-t)^T] = (hi-lo)^2/12 * I = 833.33 * I`, isotropic analytically, with
no spectral gap for a top-`k` eigenspace to find. The retained subspace is
therefore fixed by which 400 pairs the calibration happened to draw. Verified on
an exactly Euclidean evaluator with zero response error: the top eigenvector of
two independent calibration draws sits a median of 56 degrees apart over twelve
trials, against the 60 degrees expected between two uniformly random directions
in three-space. Section 3's sentence that the retained subspace "is derived from
the independently estimated metric and is not chosen by the experimenter" is
true and worthless. It is chosen by noise. P2 as registered reduces to a claim
about orthogonal projection onto an arbitrary plane, which any consistent
distance calculator satisfies, and the harness's own `SyntheticScorer`, whose
docstring says it "has no budget of its own," returns a contrast of 0.9787.
The anti-vacuity gate does not catch this, because a discarded trace share of
1/3 and 2/3 at `d = 3` is exactly what isotropy produces, so the gate that
exists to show something was discarded fires hardest when nothing distinguished
was.

**D2. The contrast is an algebraic identity in the evaluator's accuracy, with no
residual left for the budget.** `build_pairs` admits a pair to T only when the
fitted metric says its rank-`k` order flips, and to W only when it says the
order does not flip. The class label is the prediction. Writing `p` for the
probability that a graded verdict agrees with the fitted metric, a T pair
reverses when the evaluator agrees at both budgets or errs at both, and a W pair
reverses when it errs at exactly one, so

    R_T = p^2 + (1-p)^2      R_W = 2p(1-p)      contrast = (2p - 1)^2

The observed contrast 0.9683 implies `p = 0.9920`, against a measured held-out
accuracy of 0.9850 and an in-sample order accuracy of 1.0000. Every point of the
observed effect is accounted for by per-comparison accuracy and none is left for
the budget manipulation. The bars reduce to the same quantity: `MARG = 0.4841`
is met exactly when `p >= 0.848`, and `CEIL = 0.05` exactly when `p >= 0.947`.
Section 12 of this draft said the contrast was "close to a consequence" of an
accurate calibration. That was too weak. It is the consequence, exactly, and
Section 12 is corrected accordingly.

**D3. A stimulus-surface property separates the two classes, and it is not
matched.** A W pair is admitted only when its whitened difference has no
discarded component, so at budget `k` the same vector is subtracted from both
options and the rendered difference between them survives. A T pair is never of
that form. Reproduced on the pilot's own fitted metric: W pairs receive an
identical shift to both options in 25 of 63 cases at `k = 1` and 35 of 64 at
`k = 2`, T pairs in 0 of 64 at both. The reader who raised this reported 64 of
64 for W. That figure does not reproduce here and the correct statement is that
the artifact is present in a large minority of W pairs and in no T pair. It is
still a channel by which the classes differ in the text the evaluator reads
rather than in the geometry, and Section 2's matched-margin argument does not
close it, because margin matching matches the preference margin and not the
transformation applied to the stimulus.

The cheapest decisive controls, both re-renderings of pairs already built,
against the evaluator already pinned, are recorded here as the reader proposed
them and are for the owner to accept or reject. A placebo budget, rebuilding
both classes against a random `k`-plane instead of the top-`k` eigenspace, which
D1 predicts will reproduce the contrast. And a class W-prime, differing in the
retained subspace as W does but shifted at budget `k` by independent vectors of
T's norm, for which the algebra still predicts no reversal, so a rise toward
`R_T` would show the gate is reading the rendering.

### 10.2 Conditions that cannot fire

Each of these is a bar the document registers and the run could never violate.

- **The bootstrap clause in the P2 gate.** Section 5 asks for the lower end of a
  bootstrap interval above zero in addition to `R_T - R_W >= MARG`. At
  `MARG = 0.4841` with 64 pairs per class, the standard error of the difference
  is at most 0.077, so a point estimate that clears `MARG` puts a 99.9 percent
  interval's lower end at 0.230. The clause can never be the binding constraint.
  It is the same defect class the rate-limit rule was written to catch.
- **`BIN`.** Registered in Section 5 as a cell-voiding tolerance and in Section 7
  as a quantity the pilot fixes. It is given no value in Section 5's table, no
  value by the pilot, and no implementation anywhere in the code. Nothing
  compares the two margin distributions to anything.
- **The margin-match bar.** `_match_margins` admits `min(len(W_bin), len(T_bin),
  per)` from each class in every bin, so the per-bin counts are equal by
  construction and the quantity the bar inspects cannot differ. The imbalance
  worth catching is within-bin, which the bar does not look at.
- **The residual and component tolerance.** Section 3 defers to Section 5 for the
  number and Section 5 defers to Section 3. Neither states one. The value in
  force is a Python default, `min_component = 0.5`, that appears nowhere in the
  registration, and it is enforced by refusing to admit a violating pair, so
  "holds for every admitted pair" is true by construction.
- **The full-budget competence gate.** Section 5 requires the evaluator's order
  to agree with the calibration-implied order on at least 0.90 of pairs in each
  class. `build_pairs` records `a_pref_full`, and no code anywhere consumes it.
  The statistic is never computed.

### 10.3 The instrument gate and the physics gate contradict each other

Section 5 admits an evaluator at 0.90 full-budget agreement. By the identity in
D2 that evaluator has `R_W = 2(0.9)(0.1) = 0.18`, and Section 5 fails any run
whose `R_W` exceeds `CEIL = 0.05`. An evaluator that exactly meets the
registered admission bar is therefore guaranteed to record a FAIL and to fire
falsifier F3, on response noise alone. The design admits evaluators it then
necessarily refutes.

Related, and not registered: `CEIL = 0.05` carries no sampling allowance. At 64
pairs per class the standard deviation of `R_W` at a true rate of 0.05 is 0.027,
so an evaluator whose true rate sits at the bar trips it about half the time,
and Section 5 makes that an unconditional Fail rather than INDETERMINATE.

### 10.4 An unregistered filter decides a registered outcome

`build_pairs` contains `if is_w and flip: continue`, which removes from W every
pair the fitted metric predicts will reverse. Falsifier F3 is supposed to fire
when "the retained subspace is not what the estimated metric says it is," and
this filter assumes that proposition true at sampling time for every graded W
pair. F3 can now only fire when the evaluator disagrees with its own
calibration. The filter is material, it is not in Section 3's definition of the
class, and it determines the outcome of the `CEIL` bar.

### 10.5 Dropped data

An item that times out, that is truncated after its one escalation, or that
returns no letter is indistinguishable in `run_cell_order` from a pair whose two
presentation orders disagree. All land in the ambiguous counters and leave the
denominator, since the rate is `rev / graded`. The direction is unfavourable: a
pair whose swap verdicts disagree is a pair the evaluator was near indifferent
on, which is where a W reversal would come from, so dropping deflates `R_W` and
helps both bars. Section 3 registers that an unparsable answer is "dropped and
counted" and does not register the denominator. In the pilot the leverage is
visible but small, 61 of 63 giving 0.9683 against 61 of 64 giving 0.9531.

The calibration has the same structure and more room. `both_orders` discards
every swap-disagreeing pair, and the registered agreement gate allows 0.60, so
up to two fifths of calibration pairs may be dropped for being hard and the
held-out floor then measured on the surviving three fifths. Under D2 an inflated
`p` propagates directly into an inflated contrast.

### 10.6 Document does not match code

- Section 7's heading reads "none of these has been run" and its Pilot entry
  reads "Result: NOT RUN," while Sections 5, 11 and 12 quote the pilot's
  results. Corrected in this revision.
- Section 7 carries no record of the order probe on the pinned `qwen3`, which is
  the single result that licenses Section 3's revised world, and no record of
  `gemma4-12b`, which is the second of the two failures Section 12 cites.
  Section 7 still closes by recommending a change to Section 3 that Section 3
  has already made. Corrected in this revision.
- Section 3 asks for 200 matched pairs per class per budget. `prereg_config.json`
  sets `n_per_class` to 64, which is what the code reads and what the pilot ran.
  The tolerances were fixed from a pilot one third the registered size.
- Three different generation budgets appear: 1024 tokens in Section 3 and the
  config, "at most four tokens" twelve lines later in Section 3, and "at most 12
  tokens" in Section 8. The last two describe the retired local and distance
  instruments.
- Section 8's compute accounting describes the retired instrument. It counts
  batches of 32 and scores each distinct option once per cell; the hosted
  chooser ignores `batch`, is governed by `concurrency`, scores pairs rather
  than options, and issues four comparisons per pair per cell.
- Section 7's registered self-test exercises `c1_calibrate` and `c1_scorer.run_cell`,
  both on the retired distance path. `c1_order.calibrate_from_order` and
  `c1_order.run_cell_order`, which are the registered estimator and the
  registered grader, have no committed self-test. The PASS in Section 7
  certifies code the run will not call.
- Section 3 cites Section 7 for subspace-recovery angles of 1.07, 1.79 and 18.10
  degrees. Those come from `c1_order.selftest`, which is in no committed
  artifact; Section 7's self-test reports a different experiment on a different
  instrument. The sweep behind them is also not monotone, 2.04 degrees at a
  0.05 error rate against 1.79 at 0.20, so it is a single draw per rate.
- Section 9 step 1 requires the model revision written into the config, and
  Section 3 states the gateway publishes no revision. Step 1 also names
  `pilot.json`, which does not exist, and omits `sweep.json`,
  `order_probe.json`, `order_probe_qwen3.json` and `ellm_viability_gemma.json`,
  on which Sections 7 and 12 depend.
- No code produces `results.json` or `grade.json`, there is no graded-run stage
  in `main()`, and no function computes the Pass, Fail and INDETERMINATE rule or
  any bootstrap. The code that grades the claim does not yet exist.
- Sections 9 and 3 both assert a freeze that no artifact records. The
  calibration and the pair draw happen in one process and one JSON is written at
  the end, and nothing records when the run seed was drawn. A third party cannot
  check either step.
- Section 12 said the pilot had "no ambiguous verdict anywhere." That is false.
  `pilot_qwen3.json` records one ambiguous reference at `k = 1` and one
  ambiguous at-budget verdict at `k = 2`, both in class T, one unparsed item and
  ten truncation escalations, so both T cells graded 63 of 64. The claim was
  true of W only. Corrected in this revision, and in `CAMPAIGN.md`.
- Section 12 attributes held-out order accuracy figures of 0.0946 and 0.7661 to
  the two failed evaluators. Both numbers are distance-report `r^2` values, a
  different quantity. Qwen2.5's failure on the order instrument was the position
  bias of 0.8175, not the 0.0946. Corrected in this revision.
- Section 12 uses 0.9850 and 0.99 interchangeably in one paragraph. They are the
  pilot's and the order probe's figures, from different runs.
- Section 5's rendering-ceiling rationale says rounding returns some T pairs to
  their original order. At `k = 1` the pilot records `lost_to_rounding: 0` and a
  ceiling of exactly 1.0, so the rationale does not hold at that budget and the
  evaluator missed two pairs a perfect one would have caught.
- `prereg_config.json` still reads `"pilot": "FILL AT SEALING"` although the
  pilot ran at seed 20260914, and the pilot's provenance records
  `cuda_visible_devices: null` against Section 8's GPU 1 rule.

### 10.7 Researcher degrees of freedom still open

`n_bins = 8`, `oversample = 400`, `min_component = 0.5`, and
`folds = 5, l2 = 1e-3, seed = 0` in `heldout_order_accuracy`, whose fold seed
decides the 0.80 instrument gate, are all Python defaults absent from the
registration. `max_tokens` was raised from 512 to 1024 after an instrument
result, which the config discloses and Section 3 presents as given. The
deliberation gate is `mean_reasoning_tokens > 0`, while Section 3 specifies
about 240. The evaluator itself was selected on the gate's own discriminating
statistic across at least three candidates, so 0.9850 is a selected maximum and
Section 12 should report it as one. There is no registered fallback if the pin
moves, and a pin that moves after the pilot leaves the choice of replacement to
be made with the pilot in hand.

### 10.8 What the reread did not find

The tolerance-fixing arithmetic matches Section 5's stated rule exactly,
including the aggregations, and recomputes from `pilot_qwen3.json` to
`0.5 x 0.96825 = 0.4841`, `0.984375 - 0.05 - 0.05 = 0.8844` and
`max(0, 0.05) = 0.05`. The seeds, the pin timestamp, and every numeric table
transcribed from `probe.json`, `sweep.json` and `pilot_qwen3.json` are correct.
Position bias is gated before any fitting, both presentation orders are shown,
and the pilot's first-position rate is exactly 0.5000. Calibration and grading
are disjoint in code. The margin means run slightly against the claim, which is
conservative. The unregistered ridge does not drive the subspace; the
calibration draw does.

### 10.9 Disposition

This file is not sealed and is not renamed. D1, D2 and D3 are design decisions
for the owner. The document defects in 10.2 through 10.7 are recorded here in
full; those that are plain falsehoods about what has already happened are
corrected in this revision, and the rest are left standing and visible rather
than quietly repaired, because a registration that is edited into agreement with
its own code after the code is written is not a registration.

### 10.10 The two controls, run

Both controls proposed in 10.1 were run on 2026-09-13 at seed 20260915, against
the pinned evaluator, on the pilot's own fitted metric. Record
`controls.json`, log `controls.log`. Neither grades a claim. There were no
unparsed items, no deadline failures, and every cell graded in full.

| Cell | `k` = 1 | `k` = 2 | registered pilot |
|---|---|---|---|
| Placebo, within-subspace | 0.0156 | 0.0000 | 0.0000 |
| Placebo, trading | 0.9688 | 0.9688 | 0.9683 |
| Placebo contrast | 0.9531 | 0.9688 | 0.9683 |
| Class W-prime | 0.1800 | 0.1864 | 0.0000 |

**D1 is confirmed. The contrast does not depend on the retained subspace.**
Rebuilding both classes against a uniformly random plane, with everything else
in the registered sampler untouched, reproduces the registered result. At
`k = 1` that plane is 40.6 degrees from the top-`k` eigenspace and the contrast
is 0.9531 against the registered 0.9683. The top-`k` eigenspace has no
privileged status, and a pass on the registered design would report a property
of orthogonal projection rather than a budget.

One caveat on our own diagnostic, since it would otherwise read as a stronger
result than it is. The plane angle at `k = 2` is reported as 0.0 degrees. That
is geometry and not a failed randomization. Any two 2-planes in three-space
intersect in at least a line, so the largest principal angle between them is
identically zero, checked over 200 random pairs. At `k = 2` the placebo is
therefore a weaker test than at `k = 1`, and `k = 1` is the one that carries the
finding.

**D3 is confirmed in direction and is smaller than the contrast it disturbs.**
W-prime differs from W only in whether the two options move by the same vector
at budget. The predicted reversal rate is zero for both, asserted per pair
before any comparison was sent. The observed rate is 0.1800 and 0.1864 against
W's 0.0000. So the registered within-subspace rate of exactly zero is not a
clean measure of a preserved subspace. Part of it is the common shift, which is
present in 0.406 of W pairs at `k = 1` and 0.672 at `k = 2`, in no trading pair,
and in no W-prime pair.

The honest reading of the size is that two accounts remain open. Under the
identity in 10.1 D2 an observed 0.18 implies a per-comparison accuracy near
0.90 on these pairs, so W-prime may simply be harder rather than cue-free, and
the design does not separate those. What is settled is that 0.0000 was not a
property of the geometry alone. What is not settled is how much of it was.
W-prime at 0.18 is still far below the trading rate, so D3 on its own does not
collapse the contrast. D1 does.

**Disposition unchanged, and now on evidence rather than on argument.** The
registration is not sealed and is not renamed. The placebo result means the
repair D1 needs is not cosmetic: the consequence distribution has to give the
workload moment a spectral gap before a rank budget is a manipulable quantity
at all.

## 11. Known weaknesses of this design

Stated here rather than discovered later.

- The evaluator is a language model and its consequence space is rendered as
  text. Rendering a projected option back into attribute coordinates may produce
  values the model treats as unusual, and that is a confound the probe checks for
  but cannot fully exclude.
- The calibration estimates `G` from the same evaluator that is then graded. The
  identification is modular across *data* and not across *systems*, which is
  weaker than the paper's condition requires and is the honest limit of a
  single-evaluator gate.
- Matching on margin does not match on every property of a pair. A residual
  confound between the classes is possible and the pilot reports the class
  balance on attribute range and on rendered length so that a reader can see it.
- Three dimensions is the smallest space in which the prediction has content.
  Nothing here speaks to whether the effect survives in the dimensions a real
  task has.
- The evaluator is shown a rounded projection rather than the projection, so a
  correct evaluator cannot reverse every trading pair. The share lost to
  rounding was 0.026 at one decimal in a development run and is measured again
  in the pilot. Raising the rendering precision lowers the loss and raises the
  chance that two options render identically, and the registration fixes the
  precision at one decimal rather than tuning it against the result.
- The pair classes are drawn by rejection, and the yield was 196 per class
  against 300 requested in development. A low yield narrows the margin bins that
  can be matched, which is a constraint on the design rather than a result, and
  the pilot reports it.
- **The classes are matched on margin and not on attribute range, and the pilot
  shows they differ.** Trading pairs span a mean attribute range of 56.76 against
  45.47 for within-subspace pairs at rank 1, and 54.37 against 47.56 at rank 2.
  Rendered length is balanced, at about 21.8 characters in every cell. A residual
  confound of roughly a fifth in range is therefore present and measured rather
  than assumed away, and a pass should be read with it.

## 12. What a pass on this evaluator would and would not mean

This section exists because the pilot's separation is near total, and a result
that large invites being read for more than it carries. The cold reread in
Section 10 established that it carries less than the first version of this
section claimed, and this is the corrected version.

The pilot's reversal contrast is 0.9683 at both budgets. No within-subspace pair
reversed, in 128 graded. Both trading cells graded 63 of 64, having lost one pair
each to an ambiguous verdict, one at the reference order and one at budget. An
earlier version of this section said there was no ambiguous verdict anywhere.
That was false and it was true of the within-subspace class only.

**The contrast is an identity in the evaluator's accuracy, not a measurement of
a budget.** A pair enters the trading class only when the fitted metric says its
rank-`k` order flips, and the within-subspace class only when the metric says it
does not, so the class label is the prediction. Writing `p` for the probability
that a graded verdict agrees with the fitted metric, a trading pair reverses when
the evaluator agrees at both budgets or errs at both, and a within-subspace pair
reverses when it errs at exactly one:

    R_T = p^2 + (1-p)^2      R_W = 2p(1-p)      R_T - R_W = (2p - 1)^2

The observed 0.9683 implies `p = 0.9920`, against a measured held-out accuracy of
0.9850 and an in-sample order accuracy of 1.0000. No part of the contrast is left
over for the budget manipulation to explain. The bars are the same quantity in
other clothes: `MARG` at 0.4841 is met exactly when `p >= 0.848`, and `CEIL` at
0.05 exactly when `p >= 0.947`, so the physics gate is the instrument gate with
its floor moved by 0.048 in `p`.

**And the budget is not yet a budget.** Section 10 D1 shows the workload moment
is isotropic by construction, because the ideal sits at the centroid of the cube
the options are drawn from, so the retained subspace is fixed by the calibration
draw rather than by any anisotropy in the evaluator. On an exactly Euclidean
evaluator with no error at all, two independent draws pick retained directions a
median of 56 degrees apart, against the 60 expected at random. Until that is
repaired, a pass would say that projecting both options onto an arbitrary plane
reverses the pairs the projection says it reverses.

What survives is the calibration. That a language model's pairwise comparisons
are described by a quadratic form on a three-dimensional consequence space, well
enough to predict unseen comparisons held out from the fit, is a falsifiable
claim, and this programme has seen it fail twice. `Qwen2.5-7B-Instruct` failed on
the order instrument by choosing the first-shown option 0.8175 of the time, with
an agreement rate across presentation orders matching what pure position
preference predicts, and separately recovered reported distances at an `r^2` of
0.0946. `gemma4-12b` recovered distances at 0.7661 and still chose by position at
0.7000. An earlier version of this section reported those two `r^2` values as
held-out order accuracies. They are a different quantity and the attribution was
wrong.

Two cautions on the surviving claim. The evaluator was chosen on this very
statistic from at least three candidates, so 0.9850 is a selected maximum and
should be read as one. And the pilot's 0.9850 and the order probe's 0.9900 come
from different runs and are not interchangeable.

**A consequence for the design.** Held-out accuracy should be a band, not a
floor. Too low and the metric is not identified; too high and, by the identity
above, the reversal test is implied by the fit. C1 registered a floor. Section 10
records that as a defect to repair before sealing rather than an observation to
note after the fact, which is what the first version of this section did.
