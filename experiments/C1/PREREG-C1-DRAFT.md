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

**Evaluator.** `Qwen/Qwen2.5-7B-Instruct` from the HuggingFace cache on Atlas
(revision recorded in `prereg_config.json` at sealing), on GPU 1, bfloat16. The
scorer instrument of GET's G3 is reused unchanged in its reading discipline. The
model is shown an ideal and one option and asked how far the option is from the
ideal, and answers with a number, read as the first number in a greedy generation
of at most 12 tokens. Preference between two options compares reported distances.
Equal reports and unparsable reports are indifference. The G3 record established
that this instrument parses and resolves at three decimals, which is why a
chooser instrument is not used here.

**Consequences.** Three attributes, so `Y` is three-dimensional. An option is a
triple rendered as three labelled numbers in `[0, 100]` with one decimal. The
ideal `t` is a fixed triple recorded at sealing. Attribute labels are neutral
tokens fixed at sealing so that the evaluator's own priors over attribute names
do not stand in for the metric.

**The metric and the ideal are identified on a separate block.** This is the
modular-identification condition of the OLGC paper made operational, and it is
the condition under which this gate has content at all. A calibration block of
pairs, disjoint from every pair graded below and drawn from an independent seed,
is scored at full budget. `G` is estimated from those reports alone by the
procedure in `c1_calibrate.py`, and the estimate is frozen and committed before
any graded pair is drawn. No graded choice is used to fit `G` or `t`. If `G`
cannot be recovered on the calibration block to the tolerance of Section 7's
self-test, the gate does not run.

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
