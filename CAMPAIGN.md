# Campaign record

Every gate of the Observer-Limited Geometric Cognition programme, with its
registration, its sealing hash, and its verdict as executed. A gate appears here
when it is drafted, not when it passes. A miss is recorded at the same size as a
pass.

The protocol is the one inherited from `ahb-sjsu/observation-theory-campaigns`,
`ahb-sjsu/geometric-observation` and `ahb-sjsu/geometric-evaluation-theory`, and
is summarised in `README.md`.

## Gates

| Gate | Claim | Registration | Sealed | Verdict |
|---|---|---|---|---|
| C1 | `GC-34`, reversals concentrate on pairs trading a resolved direction against an unresolved one | [`experiments/C1/PREREG-C1-DRAFT.md`](experiments/C1/PREREG-C1-DRAFT.md) | **no** | not run |

## C1, Phase I

Drafted 2026-09-13. The gate tests prediction P2 of the foundational paper,
which is the directional claim and not the threshold claim. GET's G3 established
that an evaluator's indifference threshold tracks its budget, in one dimension.
One dimension has no direction to trade against, so P2 needs a proper retained
subspace and at least two directions, and that is what C1 adds.

The design's load is carried by two things rather than by the reversal count.
The metric and the ideal are estimated on a calibration block disjoint from every
graded pair, so the retained subspace is derived from an independently identified
metric rather than chosen. And the two pair classes are matched on full-budget
preference margin, so that a noise account predicts equal reversal rates in both
and the contrast between them is the only quantity graded.

**Before sealing.** A self-test on a synthetic evaluator with known metric and
known projection, a probe for event presence and anti-vacuity, and a pilot to fix
the tolerances.

| Stage | Run | Verdict | Record |
|---|---|---|---|
| Self-test | Atlas, 2026-09-13T04:24:18Z | **PASS** | [`experiments/C1/selftest.json`](experiments/C1/selftest.json) |
| Probe | Atlas, 2026-09-13 | **MISS**, calibration does not recover at `r2` 0.0946 | [`experiments/C1/probe.json`](experiments/C1/probe.json) |
| Prompt sweep | Atlas, 2026-09-13 | **gate NOT MET**, best eligible framing `r2` 0.4944, formula control 0.1547 | [`experiments/C1/sweep.json`](experiments/C1/sweep.json) |
| Order probe | Atlas, 2026-09-13 | **MISS**, first-position rate 0.8175, agreement 0.3400 | [`experiments/C1/order_probe.json`](experiments/C1/order_probe.json) |
| NRP viability, `qwen3` | Atlas to `ellm`, 2026-09-13 | **comparison OK**, first-position 0.4956, agreement 1.0000. Distance 7 of 60 parsed | [`experiments/C1/ellm-gptoss-stalled.log`](experiments/C1/ellm-gptoss-stalled.log), log only |
| NRP viability, `gpt-oss` | Atlas to `ellm`, 2026-09-13 | **stalled**, 16 idle connections and no response for 43 minutes, stopped with permission | [`experiments/C1/ellm-gptoss-stalled.log`](experiments/C1/ellm-gptoss-stalled.log) |
| NRP viability, `gemma4-12b` | Atlas to `ellm`, 2026-09-13 | **MISS both**, distance `r2` 0.7661, first-position 0.7000 | [`experiments/C1/ellm_viability_gemma.json`](experiments/C1/ellm_viability_gemma.json) |
| Pilot | not run | | |

The self-test recovers the metric to 1.2e-13 and the rank-2 retained subspace to
1.2e-6 degrees, and shows the subspace moving only 1.4 degrees under reporting
noise of sigma 4.0 against distances of order 50. The harness reverses no
within-subspace pair and reverses every trading pair the rendering still flips.
It ran under a batch-probe `ThermalController` at target 78 C with 20 threads, on
GPU 1 through `CUDA_VISIBLE_DEVICES`, with GPU 0 left alone at 18803 MiB.

**The probe missed and the miss is the useful part.** Three instrument gates
hold. Class construction, anti-vacuity and parsing are all fine, with 64 pairs
per class at rank 1, a discarded trace share of 0.450 there and 0.110 at rank 2,
and no unparsable report in 300. The calibration does not recover, at an `r2` of
0.0946, and no competing form does better. Manhattan reaches 0.0906, Euclidean
0.0806, Chebyshev 0.0459, and the best single attribute 0.0410. The evaluator
emits numbers of roughly the right magnitude, a mean of 26.86 against a true mean
absolute difference of 25.0, that do not depend on the option it was shown.

The reversal contrast in the same record is a coin flip in both classes, 0.524
against 0.508 at rank 1. Reported as a result that would have been a clean
refutation of the directional prediction, and it would have been false, because
an evaluator with no metric cannot exhibit a metric's budget effect. The
calibration gate is an instrument gate precisely so that this voids the run
instead of grading `GC-34`, and it did.

**The sweep settled it, and the control is the reason.** Six prompts over the
same 300 options. Framing matters, lifting the fit from 0.0946 to 0.4944 for a
straight-line-distance framing. Framing is not the limit. The control that states
the formula outright scores 0.1547, worse than three of the five framings that do
not, so telling this evaluator how to compute the distance makes it less
consistent than asking it for one. The limit is arithmetic, not elicitation, and
no seventh prompt is indicated.

G3 sustained the same model family at three decimals on a scalar target, where
the arithmetic is one subtraction. Three attributes need three subtractions,
three squarings, a sum and a square root, and the reports stop tracking the
geometry.

**The instrument is being replaced rather than retuned.** GET Theorem 4
identifies the metric from the order on an open set, so reported distances were
never required by the theory, only by this harness, and GET's G5 demonstrated
that recovery synthetically at 12 of 12 cells from a weak order on 64 points. An
order-based calibration asks only which of two options is nearer. It carries G3's
known hazard, that a pairwise chooser measures its position bias first, so the
replacement must gate on a position-bias rate before it estimates anything.

**The order instrument missed on the hazard that was registered for it, and the
substrate is the verdict.** The evaluator chooses the first-shown option at
0.8175 against a gate of one half plus or minus 0.15, and agreement across
presentations is 0.3400 against a floor of 0.60. Pure position choice at that
rate predicts an agreement of 0.2984, so the observed excess is 0.0416, and of
400 pairs roughly 17 carry information about the geometry against nine parameters
to fit. Averaging the presentations recovers that component and cannot identify a
quadratic from it at any sample size this gate would run.

Two instruments have now failed on this evaluator for unrelated reasons. The
reported-distance instrument failed on arithmetic, with the formula control
scoring worse than three framings that withheld the formula. The comparison
instrument fails on layout. An evaluator that neither computes a distance nor
compares by content is not an evaluation object in the sense C1 requires.

**A third instrument on Qwen2.5-7B-Instruct is not indicated.** What is indicated
is a different evaluator, which is a change to the registration's world and the
owner's to make.

**A hosted evaluator changes the picture, and the first result is partial.** NRP
runs a managed OpenAI-compatible gateway whose fair-use rules govern inference
rather than pods, so none of the Nautilus job policy applies. Queried from Atlas
so the token stays on the box. Against `qwen3` the comparison instrument that
this repository's local evaluator failed comes back clean. The first-position
rate is **0.4956** against a gate of one half plus or minus 0.15, and agreement
across both presentation orders is **1.0000** on 60 pairs. The local model chose
the first option 81.75 percent of the time with agreement at 0.3400. One model
reports its layout and the other reports the geometry.

The distance instrument still misses on the same model, at 7 of 60 parsed over
187 seconds, and the cause is not yet read from the record. A reasoning model
spends hundreds of tokens before it writes an answer, and the first run of this
probe starved one on an 8-token budget, so truncation at the raised budget is the
first hypothesis and the record now carries `finish_reason` to settle it.

**The property does not generalise across the catalog, and the pattern in three
evaluators is that deliberation removes the layout preference.**

| evaluator | reasoning tokens | distance `r2` | first-position | agreement | pure bias predicts |
|---|---:|---:|---:|---:|---:|
| local Qwen2.5-7B | none | 0.0946 | 0.8175 | 0.3400 | 0.2984 |
| `qwen3` hosted | about 237 | 7 of 60 parsed | **0.4956** | **1.0000** | 0.5000 |
| `gemma4-12b` hosted | 0.0 | **0.7661** | 0.7000 | 0.5667 | 0.4200 |

`gemma4-12b` answers directly and fast, 60 of 60 parsed in 4.2 seconds with no
truncation and no reasoning tokens, and its reports track the geometry far better
than the local model at an `r2` of 0.7661. It still misses the 0.90 calibration
gate, and it still prefers the first-shown option at 0.7000. Its agreement of
0.5667 does exceed the 0.4200 that pure position choice predicts, so content is
present, but the bias is outside the registered band.

`qwen3` is the only evaluator of the three that compares by content alone. It is
also the only one that deliberates before answering. The mechanism this suggests
is that a single forward pass answering A or B is dominated by the label prior,
and that a model which reasons first is choosing after it has compared. **That is
a pattern in three models and not a result.** Reasoning is confounded here with
family, size and training, and nothing in this probe separates them.

For the gate the consequence is concrete. The comparison instrument requires an
evaluator that deliberates, and that is a property the registration must state
rather than a preference among models.

`gpt-oss` was stopped with permission after 43 minutes in which it held 16
established connections with empty queues, no retransmit timers, and frozen
process CPU. It accepted connections and never answered. That is a third failure
mode for a hosted world, beside arithmetic and layout, and the registration needs
a hard per-item deadline and a declared attempt budget because the current policy
of five attempts at a 300 second timeout makes a stall indistinguishable from
slow work for hours.

**The `qwen3` numbers survive only in a log.** The probe wrote its JSON after all
models finished, so stopping the stalled run destroyed the structured record of
the model that had already succeeded. The probe now writes after every model and
marks the file complete only at the end. This is rule 8 again, one level up, and
it is the fourth instance in one session.

The rotation risk is now live rather than theoretical. The catalog has already
drifted from what the runbook recorded on 2026-07-18, gaining
`deepseek-v4-flash`, `gemma4-12b`, `gemma4-small` and `gemma-small-e4b`. A sealed
registration naming a hosted model can lose its evaluator without notice, which
is weaker priority evidence than a local cache with a pinned revision, and the
registration must say so. The gate is otherwise ready. Its self-test passes, its class
construction and anti-vacuity hold, its estimator recovers a retained subspace to
under two degrees while a fifth of comparisons are wrong, and its instrument
gates have now caught two unfit instruments before either could grade a claim.

The registration also carries the programme's rate-limit rule, which requires the
draft to be reread cold in a later session before it is sealed, and Section 10 of
the registration is empty until that happens.

**What a pass would and would not establish.** A pass establishes the phenomenon
in one artificial evaluator whose metric was identified on disjoint evidence. It
leaves `GC-29`, that human cognitive budgets exist and are manipulable, posited
and untouched. Phase II, which replaces a researcher-coded representation with
one recovered independently, is what answers the admission filter's refusal, and
C1 does not answer it.

## Accounting

| | count |
|---|---|
| gates drafted | 1 |
| gates sealed | 0 |
| gates run | 0 |
| pre-sealing stages passed | 1 of 3 |
| claims raised by a sealed pass | 0 |

No claim in `claims/LEDGER.md` has been raised or lowered by a gate in this
repository. The ledger's debt ratio is 1.0 and C1 is the first thing that can
move it.
