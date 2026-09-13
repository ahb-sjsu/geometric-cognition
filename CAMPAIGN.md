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
| Prompt sweep | Atlas, 2026-09-13 | running | |
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

A prompt sweep is running to find whether any framing elicits a reliable distance
from this evaluator. It selects on calibration `r2` alone and cannot compute the
reversal contrast, and it carries one ineligible control that states the formula
outright, to tell a failure of elicitation apart from a failure of arithmetic.

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
