# C3 design note: measure the sensitivity profile, select nothing

**Status: DESIGN NOTE, REREAD, NOT USABLE AS SPECIFIED. No bars, no seed, no
run.** The reread record at the end finds that the construction carries answer
shortcuts on the narrow axes, that the noise account is not the exact null this
note claims, and that one pair per prompt gives the evaluator no workload to
budget over. The change of approach, selecting nothing on a fitted metric,
survives.

The sections before the record set out the change of approach and the
construction as first written, so that a registration can be written against
something checked rather than against an idea.

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

## Reread record, 2026-09-13

Two readers with no drafting context, given only this note and `c3_design.py`,
and fenced off from C1, C2, `CAMPAIGN.md`, the paper and the history. One
verified the construction by running it. One attacked the logic by simulating
evaluator models on the stimuli the code builds. The load-bearing findings below
were reproduced before being recorded.

**Verdict: the construction is not usable as specified, and the property this
note claimed distinguishes C3 from the four refused designs does not hold.** The
change of approach survives: nothing here selects on a fitted metric, and the
readers found no defect of that kind. The endpoint and the stimuli do not.

### The noise account is not the exact null

The note says a ratio of thresholds is invariant to anything multiplying all
sensitivities, so uniform noise leaves `thr_R / thr_P` unchanged. The statement
about ratios is true. It covers only noise added in decision-variable units whose
profile across axes matches the zero-load baseline, and the design measures the
baseline precisely because that profile is not assumed flat.

Take a model with no budget and two noise sources: fixed encoding noise on the
one number that differs between the options, and decision noise that load adds
uniformly. Reproduced on this note's box and the ideal `(75, 15, 8)`, 300 pairs
per cell:

| load-added decision noise | `thr_P` | `thr_R` | ratio |
|---|---|---|---|
| 0 | 0.763 | 0.186 | 0.24 |
| 1 | 1.083 | 0.723 | 0.67 |
| 2 | 1.566 | 1.371 | 0.88 |
| 4 | 2.750 | 2.659 | 0.97 |

The ratio rises fourfold with no budget. Whenever the zero-load profile is not
flat, adding flat noise pulls the ratio toward one, and when `R` starts easier that
movement is exactly the budget prediction. A position bias in decision units does
the same, moving the ratio from 0.68 to 1.11 in the reader's simulation. Weber
noise and range-proportional noise move it too, in the other direction. Of the
no-budget models tested, only independent noise on every number and noise added
directly to the distance difference leave it fixed.

The first reader tested absolute and Weber noise and found the ratio stable under
a doubling. That is consistent with the second reader: independent per-number
noise is one of the two cases that does leave the ratio fixed. The case that
breaks the null is the two-source one, which the first reader did not test.

**The claim "none of the previous four designs had that property" is withdrawn.**
C3 does not have it either.

### The axes are not the same objective problem

Checked on a fresh seed. Two rules that ignore geometry entirely:

| axis | pick the smaller varied value | pick the shorter string |
|---|---|---|
| `P` | 0.47 to 0.53 | 0.49 to 0.50 |
| `Q` | 0.88 to 0.98 | 0.49 to 0.56 |
| `R` | 0.92 to 1.00 | 0.65 to 0.98 |

On `R` a heuristic scores up to 100 percent, and at separation 4.0 the shorter
string is the nearer option in 98 percent of pairs. Both rules sit at chance on
`P`. If load shifts the evaluator toward a heuristic, `R` gets relatively easier
and the ratio falls, which would mask a real budget.

The cause is in `solve_displacement`, which takes the first valid root, and the
first root always places the derived point above the ideal's coordinate. That
happens in 100 percent of `Q` and `R` pairs and 62 to 77 percent of `P` pairs,
because `P` has little room above its ideal. The direction of the shortcut depends
on where the ideal sits: the second reader, using a different ideal, found the
reverse rule, "pick the larger value", scoring 100 percent on `R`. The ideal is not
registered anywhere in this note or the code, and it changes the sign of the
confound.

The distance band does not equate the axes at a given separation. The note
compared the spread across all cells, which is the wrong comparison. At separation
4.0 the mean minimum distance is 26.7 on `P` and 15.4 on `R`, pinned to the band's
lower edge. At that rung `R` pairs are also drawn from a different population of
base points than `P` pairs, with a two-sample KS statistic of 0.91, and only 0.2
percent of attempts on `R` are accepted against 41 percent on `P`. The profile's
shape is confounded exactly where it is read.

"Same objective problem" holds only for an evaluator that integrates Euclidean
distance on raw units. The non-varied coordinates are identical within a pair, so
any separable monotone metric answers by comparing one number, and at equal
separation that number moves 2.9 times further on `R` than on `P`. An evaluator
that scales each attribute by its range is near ceiling on `R` across the whole
ladder, where no threshold exists to estimate.

### The endpoint is the wrong prediction

A hard rank-1 budget makes a pair that differs only on a discarded axis identical,
so accuracy is at chance at every separation and no threshold exists. A soft
budget attenuates the axis until its threshold leaves the ladder, where a fitted
curve simply extrapolates. The sharper signature, which no noise model tested
produces, is a low upper asymptote on the discarded axis while the retained axis
is near ceiling. The endpoint should be accuracy at the largest separation, or a
free per-axis asymptote, with thresholds treated as censored.

### The box is not the evaluator's workload

Each prompt contains two options that differ on one axis, so the only variance in
the context window is on the tested axis: `(111, 0, 0)` on `P` trials and
`(0, 0, 29)` on `R` trials. A budget computed on what the evaluator actually sees
retains the tested axis every time and predicts nothing. The evaluator is never
shown the box. Pooled over all presented options the ordering `P > Q > R` survives,
but at a variance ratio near 11 rather than the 25 the note derives from the box,
and no single prompt carries the pool.

This is the most consequential of the logic findings. The rank budget in the
theory is a property of the workload the evaluator is resolving, and a design that
presents one pair per prompt gives it no workload to budget over.

### Also confirmed

The axis is confounded with list position, letter label and numeric range. With
uniform draws from the box, narrow range and low variance are the same variable by
construction. The psychometric model needs a lapse rate per load condition, a
response-position bias term and a free upper asymptote per axis; without a lapse
term an increase in guessing drifts the ratio. At 64 pairs per cell the minimum
detectable change in the ratio is about threefold; detecting 1.5-fold needs around
500 per cell. The note's "within 0.5 percent of target" came from one seed; every
seed tried has at least one cell off by up to 1.05 percent, which is sampling
noise. The docstring's rounding-flip check is not what the code enforces, though
it cannot bite at current settings. And `balance_report` cannot see any of the
confounds above, because it reports only quantities balanced by construction.

### What the readers confirmed is sound

`solve_displacement` is algebraically exact, to 2.8e-14 over 124,000 solves, and
never moves distance the wrong way. Every pair differs on exactly one axis after
rounding. Cells fill, `R` cannot reach 8.0 inside the band on any seed, the order
never flips under rounding in practice, presentation side is randomised, and
nothing is selected on a fitted model. Noise added directly to the distance
difference is genuinely invariant.

### What changes before anything is registered

1. **Put a workload in the context window.** Each prompt carries a multi-option
   set whose spread per axis is controlled, with the probe pair embedded in it. The
   budget prediction is then about variance the evaluator can see, and the
   high-variance axis can be rotated across blocks.
2. **Test the asymptote, not the threshold.** Accuracy at the largest separation
   on each axis, with a psychometric model carrying lapse, position bias and a free
   per-axis ceiling.
3. **Counterbalance axis against list position, letter label and numeric range**,
   so a budget, which follows in-context variance, can be told apart from
   heuristics, which follow position or magnitude.
4. **Register the ideal and remove the shortcuts**: choose roots at random,
   stratify each cell to 50/50 on "smaller value is nearer" and on string length,
   and perturb non-target coordinates so the options differ on every attribute
   while the answer rests on the target axis.
5. **Register the two-source noise model as the adversary**, so a budget reading
   requires movement that model cannot produce.

The first item changes the stimulus unit from a pair to a set, which is a larger
change than the others and should be settled before the rest are built.
