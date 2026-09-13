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

## 7. Self-test, probe and pilot (BEFORE sealing, none of these has been run)

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

*Result: NOT RUN.*

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

*Not yet performed. The rate-limit rule exists because a draft reread cold in a
later session has, in this programme's record, caught a falsification condition
that could not fire. Until this section names a reader and a date, this file is
a draft and no result graded against it counts.*

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
that large invites being read for more than it carries.

The pilot's reversal contrast is 0.9683 at both budgets, with no within-subspace
pair reversing in 128 graded and no ambiguous verdict anywhere. The trading rate
sits essentially at the rendering ceiling, 0.9683 against 0.9844 at rank 2. That
is the synthetic self-test reproduced on a language model.

**The informativeness of this gate is concentrated in the calibration, not in the
contrast.** The held-out order accuracy of the fitted quadratic is 0.9850, so
this evaluator is very nearly a quadratic evaluation object. A trading pair is
admitted precisely because the fitted metric says the rank-`k` order disagrees
with the full-budget order, so an evaluator that the metric describes almost
exactly will reverse those pairs almost exactly. The contrast is then close to a
consequence of the calibration being accurate rather than an independent test of
the budget.

What is not near-tautological, and what carries the content, is the calibration
itself. That a language model's pairwise comparisons are described by a quadratic
form on a three-dimensional consequence space, well enough to predict unseen
comparisons at 0.99, is a falsifiable claim that this programme has now seen fail
twice. `Qwen2.5-7B-Instruct` failed it at a fit of 0.0946 and by choosing the
first-shown option 0.8175 of the time, and `gemma4-12b` failed it at 0.7661 and
0.7000. The gate's discriminating stage is the instrument gate, and the reversal
contrast confirms that the budget manipulation does what the identified metric
says it will.

**A consequence for the design worth registering.** The reversal prediction is
most at risk where an evaluator is approximately rather than almost exactly
quadratic, because that is where the projection's predicted flips and the
evaluator's actual flips can come apart. A held-out accuracy near one leaves the
prediction little room to fail. A future gate of this shape should therefore
treat held-out accuracy as a band rather than a floor, since too low means the
metric is not identified and too high means the reversal test is nearly implied
by the fit. C1 keeps the floor it registered and records the observation instead
of acting on it after the fact.
