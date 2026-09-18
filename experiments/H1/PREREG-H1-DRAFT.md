# PREREG H1: the deliberation peak sits at the identified resolution boundary and moves with the role of the probe's attribute

**Status: DRAFT, NOT SEALED. No participant recruited, no pilot run, no bar fixed.**
Sealing is the rename to `PREREG-H1.md`, the commit of that rename, and the
recording of its blob hash in `CAMPAIGN.md`, in that order and only after
Section 7 is filled from a self-test, a probe and a pilot. Human data collection
additionally waits on ethics approval, which is an owner item and is recorded in
Section 9.

This gate is the human counterpart of the C3 design note. It reuses C3's
multi-option construction and its exact null, adds a calibration block that
identifies each participant's observer by structural fuzzing, and grades a
deliberation endpoint on a separate test block. It is the first gate in this
repository that tests the Deliberative Recruitment Hypothesis of the working
paper `paper/when_decisions_fail_to_collapse.docx`, Section 9 of which is the
prose form of this registration.

## 1. Claim under test

`GC-DRH-1`. For a participant whose sensitivity profile has been identified on a
calibration block, process measures of deliberation on a disjoint test block peak
at the separation the calibration block identified as that participant's
resolution boundary, and the peak sits at a larger separation when the probe's
target attribute carries low workload variance in the context than when it
carries high variance.

The claim has two parts and they are graded separately.

* **H1-a, identification.** The calibration block returns a role effect. The
  asymptote of the psychometric function is lower in the low role than in the
  high role, on a probe that is byte-identical across roles.
* **H1-b, recruitment.** On the test block, the location of the deliberation peak
  differs between roles in the direction and by the amount identified in H1-a.

H1-b is not graded when H1-a misses, because a peak location cannot move with a
boundary that was not found.

The secondary claim `GC-DRH-2` concerns a resource load and is stated in
Section 3.5 with its own manipulation check. It is graded only if that check
passes.

## 2. Why the design carries the load

Four designs in this programme were refused because the class label of a stimulus
was a prediction of a model fitted to the subject under test. Here no model of
the participant is fitted before the stimuli are built. The axis, the separation
and the context variance of every trial are set by the generator. The only
quantities estimated from the participant are the psychometric functions of the
calibration block, and those are used to place test trials and to predict where
the peak will be, never to select which trials count.

The null holds by construction rather than by a noise model. The probe pair is
the same in every role of a triplet, so any account in which the answer or the
effort depends on the probe alone predicts no role difference, in accuracy or in
peak location. That covers additive and multiplicative noise on the probe, generic
difficulty, reading time, and a sequential sampling process whose drift is set by
the probe's separation. The role contrast is the only graded quantity, and it is
a property of the context.

## 3. World

### 3.1 Participants

Adults recruited through the university participant pool, number fixed in
Section 5 from the pilot. Exclusions, fixed before any confirmatory participant
is run, are a calibration block whose lapse rate exceeds the registered bound, a
position bias term outside the registered bound, or fewer than the registered
number of gradeable test trials. Excluded participants are replaced and their
data are retained in the record under Rule 8.

### 3.2 Stimulus generator

The generator is `c3_sets.py` of the C3 design note, ported to a human
presentation format with the same construction rules.

* Three attributes, presented as labelled numeric values, every attribute
  spanning the same range around the registered ideal `(50, 50, 50)`. Each value
  renders as four characters.
* A set is an ideal and 22 options. Two options are the probe and differ mainly
  along one target attribute at a chosen separation. Twenty options are context,
  with one attribute at high variance, one at medium and one at low, at the
  registered floor ratio of 2 between adjacent levels.
* A triplet presents the same probe, byte for byte and at the same list
  positions, in three contexts that permute the three spreads across attributes,
  so that the target attribute plays the high, medium and low role in turn. Only
  the high and low roles are graded. The medium role is retained as a check on
  monotonicity.
* Non-target attributes of the probe are perturbed symmetrically about the ideal,
  so the two probe options differ on every attribute and the answer rests on the
  target.
* Attribute order and labels are drawn per triplet from a registered pool. The
  four sign patterns, whether the nearer option has the smaller value and whether
  the pair straddles the ideal, are stratified to exactly one half each in every
  cell. Presentation side of the nearer probe option is randomised.

Construction checks reported for the evaluator version, 768 triplets, are in
`experiments/C3/DESIGN-C3.md` under "Construction check". The human port is
rechecked on its own built stimuli before the pilot, Section 7.1.

### 3.3 Calibration block, the fuzz

Cells are attribute by role by separation. Separations form a ladder fixed from
the pilot, with the largest separation chosen so that the high role reaches
ceiling in the pilot. Trials per cell are fixed from the pilot so that the
asymptote's confidence interval meets the width in Section 5.

The participant's task on every trial is to say which of the two probe options
is nearer the ideal. Accuracy is the only quantity read from this block.

### 3.4 Test block, deliberation

New triplets, constructed and not selected, at a grid of separations placed
around the boundary identified for that participant on that attribute and role.
The grid is registered as a set of multiples of the identified boundary and is
the same for every participant.

Dependent measures, all recorded on every trial.

* Response latency from the end of a reading phase to the response. The reading
  phase ends when the participant advances, and its duration is recorded.
* Confidence on a registered scale, collected after the response.
* Options inspected. The context is presented masked and each option is revealed
  on request. The count and order of reveals are recorded.

The reading phase and masked context are pilot items. If the pilot shows that
masking changes the role effect of the calibration block, the masked version is
dropped and the reveal count is not collected.

### 3.5 Second budget, resource load

Both blocks are repeated under a response deadline fixed from the pilot at the
latency quantile registered in Section 5. Order of load conditions is
counterbalanced across participants.

The load is read as a budget manipulation only if its manipulation check passes.
The check is the difference of differences of calibration asymptotes,
high minus low role, under load minus without load. A positive value above the
bar in Section 5 means the load lowered the participant's effective rank. Below
the bar, the load's test block data are reported at full size and are not read as
evidence about budgets, following the C1 record in which three of four resource
manipulations degraded the instrument before they touched the resolution.

## 4. Estimator

### 4.1 Psychometric model, per participant, attribute, role and load

Accuracy as a function of separation, with a response position mixture per load
condition shared across cells, and a free upper plateau per cell. The plateau is
a diagnostic and is not the endpoint, because it is not identified when the
function is still rising at the top of the ladder. The first self-test run
recorded that failure, Section 7.1. The endpoint per cell is accuracy at the
largest ladder separation, which is the endpoint the C3 rebuild registered. The
threshold is censored where that accuracy is below the criterion, so a discarded
direction reads as a low ceiling and not as an extrapolated threshold. The lapse
per load condition is reported as one minus the mean endpoint of the retained
role rather than fitted separately. The fitting code and its self-test are
`h1_fit.py`, Section 7.

### 4.2 Identified quantities

* `A[attr, role, load]`, accuracy at the largest ladder separation, with the
  fitted plateau reported beside it.
* `s*[attr, role, load]`, the separation at which the fitted function reaches the
  registered accuracy criterion, censored where it never does.

### 4.3 Statistics

* **H1-a.** `D_A = mean over attributes of (A[high] - A[low])`, without load. One
  number per participant, and a group mean with its interval.
* **H1-b.** For each cell with an uncensored `s*`, the location of the peak of
  each process measure over the test grid, `p[attr, role]`, estimated by a
  registered smoother. The statistic is
  `D_p = mean over attributes of (p[low] - p[high])`, and the prediction is
  `D_p` positive and within the registered tolerance of
  `mean over attributes of (s*[low] - s*[high])`.
* **GC-DRH-2.** The manipulation check `M = D_A[load] - D_A[no load]`, and, where
  it passes, the displacement `D_p[load] - D_p[no load]` against the identified
  displacement of `s*`.

Every statistic is computed over the full registered trial set. No statistic
conditions on a filter the manipulation can move, following the estimand rule in
the foundational paper. Ungradeable trials are counted as uninformative and their
count is reported per cell.

## 5. Bars (FIXED FROM THE PILOT before sealing, see Section 7)

| Quantity | Bar | Fixed by |
|---|---|---|
| Trials per calibration cell | `[ ]` | interval width on `A` of `[ ]` in the pilot |
| Participants | `[ ]` | power for `D_A` at the pilot effect, with the equivalence bound below |
| Lapse rate exclusion | `[ ]` | pilot distribution |
| Position bias exclusion | `[ ]` | pilot distribution |
| Accuracy criterion for `s*` | `[ ]` | between the low role floor and the high role ceiling in the pilot |
| Test grid, multiples of `s*` | `[ ]` | pilot latency curve |
| Deadline for the load, latency quantile | `[ ]` | pilot no-load latency distribution |
| Equivalence bound `delta_min` for `D_A` | `[ ]` | the smallest role effect the theory is not permitted to survive, stated before the pilot is read |
| Equivalence bound `delta_min` for `D_p` | `[ ]` | as above |
| Tolerance on `D_p` against the identified displacement | `[ ]` | measurement error of `p` in the pilot |
| Manipulation check bar for `M` | `[ ]` | pilot |

Each `delta_min` is stated before the pilot is opened and is recorded in Section 7
with its date. A falsifier that rests on observing no effect is not a falsifier
without it.

## 6. What falsifies

* H1-a misses when `D_A` is below `delta_min` with the interval excluding larger
  values. The observer then has no measurable rank budget on this stimulus set,
  and H1-b is not graded.
* H1-b misses when the peak location does not differ between roles, `D_p` below
  its `delta_min`, or differs in the wrong direction, or differs by an amount
  outside the tolerance of the identified displacement. The first two outcomes
  count against the Deliberative Recruitment Hypothesis directly. The third
  counts against the specific claim that the peak tracks the identified boundary
  and is recorded as such.
* GC-DRH-2 misses when the manipulation check passes and the peak does not move
  with it. Where the check fails, the gate records a non-result and not a miss.
* The gate is void, not missed, when the self-test of Section 7.1 fails, when
  the probe of Section 7.2 finds a cell without events, or when the built
  stimuli fail any construction check.

## 7. Self-test, probe and pilot (all run before sealing; see Section 9)

### 7.1 Self-test, synthetic observers

`h1_fit.py` is run on responses simulated from three registered observers on the
built stimuli, with the raw simulated responses persisted beside the verdict.

* A rank budget observer with known retained subspace. The fit must recover the
  low asymptote in the discarded role and the ceiling in the retained role.
* A uniform noise observer. The fit must return `D_A` within its interval of
  zero.
* A position heuristic observer and a magnitude heuristic observer. Each must
  return `D_A` within its interval of zero, which is the check that the built
  stimuli carry no cue a heuristic can follow.

The self-test also simulates the test block from a latency model whose peak is
placed at a known separation, and the smoother must recover the placed peak
within the tolerance of Section 5.

**Record, 2026-09-18.** `h1_fit.py` self-test, seed 20260918, run on Atlas with the
agi-hpc venv Python from `/home/claude/h1/` (the repository has no clone on Atlas,
so `h1_fit.py` and `c3_sets.py` were copied there). Twelve synthetic participants,
ladder 0.5, 1, 2, 4, 8, twenty-four triplets per attribute and separation cell,
1,080 calibration trials per participant. Four runs, each kept.

| Run | Started UTC | Verdict | What it found | Record |
|---|---|---|---|---|
| 1 | 15:47 | FAIL 1 of 17 | The graded endpoint was the fitted plateau. The discarded role fitted a plateau of 0.766 for an observer at about 0.63 on the ladder, because the free plateau extrapolates while the function is still rising at the top step. Endpoint changed to accuracy at the largest step, 4.1. | `record/selftest_run1_plateau_endpoint.json`, `record/h1self_run1.log` |
| 2 | 15:54 | FAIL 10 of 17 | Response records lacked the ladder step, so the top-step filter matched one trial and every endpoint was undefined. The fitter now refuses data without `sep_nominal`. Fitted plateaus reproduced run 1. | `record/selftest_run2_missing_sep_nominal.json`, `record/h1self_run2.log` |
| 3 | 15:59 | FAIL 2 of 17 | Null observers graded by "bootstrap interval covers zero" over twelve participants. Two intervals excluded zero at means of 0.009 and 0.021. A within-triplet permutation of role labels, the exact null, gave p of 0.149, 0.124 and 0.256 for the three null observers and below 0.001 for the rank budget observer, so the bootstrap was anticonservative at that size. Null checks changed to the equivalence bound of Section 5 plus the permutation test. Per-observer seeds had used Python's string hash, which is not stable across processes, and were made fixed. | `record/selftest_run3_bootstrap_null.json`, `record/h1self_run3.log` |
| 4 | 16:06 | **PASS 20 of 20** | See below. | `selftest.json` (sha256 4a6d568ce07669cf...), `selftest_raw.json.gz` (da5f20dc9ca63ee4...), `h1_fit.py` (886c6a75394d6bad...), `c3_sets.py` (6b3493d17d6a7364...) |

Run 4 results, endpoint `A` = accuracy at separation 8 by role, mean over
participants and attributes.

| Observer | A hi | A mid | A lo | D_A | 95% interval | b recovered |
|---|---|---|---|---|---|---|
| rank budget | 0.988 | 0.971 | 0.691 | +0.297 | [0.274, 0.323] | 0.002 |
| uniform noise | 0.986 | 0.984 | 0.986 | 0.000 | [-0.012, 0.010] | 0.000 |
| position heuristic (0.8) | 0.565 | 0.557 | 0.571 | -0.006 | [-0.043, 0.027] | 0.777 |
| magnitude heuristic (0.8) | 0.591 | 0.589 | 0.591 | 0.000 | [-0.029, 0.028] | 0.000 |

The rank budget observer's low-role `s*` is censored in most cells, as the
endpoint rule requires. The position mixture recovers at 0.777 against the
simulated 0.8 times one minus the lapse of 0.03, which is 0.776. The smoother
recovered every placed latency peak within a factor of 1.25 and `D_p` tracked
the placed displacement. Runtime about five minutes per run at four threads.

What the self-test does not establish. The rank budget observer is a soft budget
with weights equal to in-context variance ratios and a fixed decision noise, and
its low-role endpoint of 0.69 is a property of that choice and the ladder. A
different noise level moves it. The self-test shows the estimator reads the
endpoints and the nulls correctly on built stimuli, not that a human observer
will produce them. The equivalence bound of 0.05 used here is the self-test
value and the registered value is fixed from the pilot.

### 7.2 Probe, event presence

The pilot's calibration block must show, in every attribute by role by
separation cell, a count of gradeable responses at or above the registered
trials per cell, and the test block must show gradeable latencies at every grid
point. A gate that could pass on an empty cell is not sealed.

### 7.3 Pilot

A pilot of a registered small number of participants fixes every bar in
Section 5. The pilot data are not pooled with the confirmatory data. The pilot
also decides the two open presentation questions, the reading phase and the
masked context, and records the decision.

## 8. Compute and thermal rule

Stimulus generation, fitting and self-tests run on Atlas under the standing
thermal rule. Human sessions run on a lab machine or a hosted experiment
platform, and their raw logs are copied to Atlas under `/archive` before any
analysis. Nothing is analysed on the laptop.

## 9. Sealing procedure and owner items

1. Ethics approval for the human protocol. Owner item.
2. Fill Section 5 from the pilot, with the `delta_min` values dated before the
   pilot was opened.
3. Record the self-test, probe and pilot artifacts in Section 7 with commit
   hashes.
4. Rename to `PREREG-H1.md`, commit, record the blob hash in `CAMPAIGN.md`.
5. Only then recruit the confirmatory sample.

## 10. Reread record

Empty. A cold reread by a reader with no drafting context, fenced from the
working paper, precedes the pilot.

## 11. Known weaknesses of this design

* The fuzz measures sensitivity only to the three constructed attributes. A
  retained direction that is not one of them is invisible. The spectral probe of
  `structural-fuzzing` is the discovery instrument for that case and is not part
  of this gate.
* Trial counts at psychometric resolution are large. The design is sized on the
  calibration block, and the recruitment effect may need more participants than
  the identification does. That is recorded, not hidden, and the power section
  states which claim the participant number was chosen for.
* Latency after a self-paced reading phase is contaminated by any deliberation
  that begins during reading. The reveal count is the cleaner process measure
  and depends on the masked presentation surviving the pilot.
* Role and context are confounded with the crowding of context values near the
  probe, recorded in the C3 construction check as favouring the low role. That
  bias runs against the predicted sign and is carried as a known conservative
  factor.

## 12. What a pass on this design would and would not mean

A pass on H1-a means a human observer showed a rank budget on workload variance
in a stimulus set where the probe could not have carried the effect. A pass on
H1-b means the location of deliberative effort tracked a boundary identified on
disjoint evidence, which is the claim of the working paper in its testable form.
Neither says anything about curvature, about noncommutative normative
transformations, or about language models. A pass on GC-DRH-2 adds that a
resource load moved the boundary and the effort with it, which is the
displacement test of Prediction 3. A miss on H1-b with a pass on H1-a is the
outcome the working paper names as most informative against it, path dependence
of the representation without recruitment of effort.
