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

*Result: NOT RUN.*

**Probe.** One cell on the probe seed to establish event presence. Both classes
non-empty at the required margins, the trace share above 0.05 at `k = 1` and
`k = 2`, no unparsable report, and full-budget agreement above 0.90.

*Result: NOT RUN.*

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
