# C3 design note: measure the sensitivity profile, select nothing

**Status: DESIGN NOTE, not a registration. No bars, no seed, no run.** This
records the change of approach and the construction, so that a registration can
be written against something that has already been checked rather than against an
idea.

## Why the previous four designs were refused

C1, C1-D, C2 revision 1 and C2 revision 2 all did the same thing: fit a metric to
the evaluator, project it, select pairs by whether the projection flips the order,
and compare classes. Three consequences followed every time.

The class label was a prediction of a model fitted to the subject under test. The
classes then differed in the entire joint distribution of the stimulus, not in one
coordinate, so matching on any single statistic left another unmatched. And the
unmatched one carried a confound as large as the effect or larger: C1 and revision
1 matched preference margin and were confounded under multiplicative noise at
`+0.046`; revision 2 matched decision SNR and was confounded under absolute noise
at `-0.128`. Each repair produced the next defect.

A fifth design matching on a third statistic should be expected to fail the same
way. The problem is not the choice of statistic. It is selection on a fitted
model.

## What replaces it

A rank budget says sensitivity to low-variance directions is lost first. That is a
claim about the evaluator's **sensitivity profile across directions**, not about
any classification of pairs. So measure the profile.

**Construction.** A pair differs along exactly one coordinate axis. The axis is
chosen, not discovered. The displacement is solved so the pair's difference in
distance from the ideal equals a target value, in the design's own Euclidean
geometry. Two pairs on different axes at the same target are the same objective
discrimination problem presented along different directions.

**No estimation anywhere.** The box fixes which directions carry workload
variance: per-axis ranges 100, 45 and 20 give variances 833, 169 and 33, so a
rank-1 budget keeps `P` and discards `R`. That ordering is a property of the
stimulus set and needs no fit. Nothing is admitted or rejected on the basis of a
prediction; the only rejections are geometric.

**The endpoint is the shape of the profile, not its level.** Write `thr_j` for the
separation at which the evaluator reaches a fixed accuracy on axis `j`.

| account | prediction |
|---|---|
| uniform noise | every `thr_j` scales together, `thr_R / thr_P` unchanged |
| rank budget | the discarded axis degrades faster, `thr_R / thr_P` rises |

A ratio of thresholds is invariant to anything multiplying all sensitivities
together, so the noise account is the **exact null** rather than one adversary's
construction. None of the previous four designs had that property, which is why
each of them could be reproduced by a noise model.

The evaluator's static per-axis sensitivity is whatever it is and is measured at
zero load rather than assumed uniform. The graded quantity would be the change in
the ratio under load, which is a difference in differences on a quantity with no
fitted metric in it anywhere.

## What the construction check found

All fifteen cells of a three-axis by five-separation ladder fill to 64, with
achieved separations within 0.5 percent of target and rendered length equal across
axes.

**One confound was found in construction and fixed there.** Distance from the
ideal drifted with the axis: at a separation of 8.0 the narrow axis sat 3.2 from
the ideal against 32.5 for the wide one, because reaching a large separation along
a short axis forces the options toward the ideal. A registered distance band, the
same for every axis, removes it. Spread across cells falls from 3.2 to 40.9, down
to 15.4 to 28.6.

**The band exposes a real limit.** Axis `R` cannot produce a separation of 8.0
inside the band at all, because its range is only 20. The usable ladder is 0.5,
1.0, 2.0 and 4.0, and it is bounded by the narrowest axis. This is a property of
the design rather than a defect, and it bounds what the profile can be measured
over.

## What this note does not do

There is no registration, no bar, no sample size and no power calculation. The
threshold estimator is not written. The load manipulation is not specified, and
the record of C1 says three of the four manipulations tried degraded the
instrument rather than the resolution, which is unresolved and independent of this
change.

The construction is also not yet checked by anyone who did not write it. On this
programme's record that is where the defects have surfaced every time, in four
consecutive designs, so this note is the input to a cold reread and not a result.
