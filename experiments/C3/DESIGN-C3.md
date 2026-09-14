# C3 design note: measure the sensitivity profile, select nothing

**Status: DESIGN NOTE, REBUILT, NOT YET REREAD. No bars, no seed, no run.** The
pair construction described first was refused by the reread recorded below it. The
rebuild at the end of this note replaces it with multi-option sets in which a
byte-identical probe is shown in three contexts that differ only in the variance
role of the probe's target attribute. Simulated on the built prompts, every
no-budget model acting on the probe gives a role effect of exactly zero, and a
rank budget gives a large one. The rebuild has not been reread.

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

## Rebuild: multi-option sets, 2026-09-13

This section supersedes the pair construction above, which the reread found
unusable. The pair code stays in `c3_design.py` as a record; the rebuild is
`c3_sets.py`.

### The unit is a triplet of prompts

Each prompt shows an ideal and 22 options. Two of them are the probe pair, which
differs mainly along one target attribute. The other 20 are context, and their
spread per attribute is set by design: one attribute high variance, one medium,
one low.

**The same probe appears in three prompts, byte for byte**, at the same list
positions, with the same attribute order and labels. Only the context changes, and
with it the role the probe's target attribute plays: high, medium or low.

This is the change the reread's most consequential finding called for. The
evaluator now has a workload in its context window, the budget prediction is about
variance it can see, and the variance rank is manipulated while the probe is held
fixed.

### Why the null is now exact

Any noise that acts on the probe, including the two-source model that moved the
pair design's threshold ratio fourfold, sees identical input in all three prompts
of a triplet. It therefore predicts no difference between roles. The null holds by
construction and does not depend on a noise model.

### What answers each reread finding

| finding | answer |
|---|---|
| one pair per prompt gives no workload | a controlled 20-option context in every prompt |
| range was the same variable as variance | every attribute spans the same range around the same ideal, `(50, 50, 50)`, so variance differs only in the context and attributes are exchangeable |
| axis confounded with list position and label | attribute order and labels drawn per triplet from a pool; target attribute counterbalanced |
| "pick the smaller value" answered the narrow axes | four sign patterns stratified exactly per cell, so smaller-value-is-nearer and straddling the ideal are each exactly 0.500 in every cell |
| "pick the shorter string" answered `R` | every value renders as four characters |
| options differed on one attribute only | non-target attributes perturbed symmetrically about the ideal, so options differ on every attribute and the answer still rests on the target |
| biased root choice | no root choice; offsets come directly from the sign patterns |
| threshold is undefined where the budget bites | the endpoint is accuracy by role at a fixed separation |
| ideal unregistered | registered at `(50, 50, 50)` |

Load is not part of this design. The rank budget is defined on workload variance,
and in-context variance is a workload manipulation. The role contrast tests whether
a budget exists. Whether load lowers its rank is a separate question. That keeps
this design away from C1's record, where three of four resource manipulations
degraded the instrument before the resolution.

### Construction check, 768 triplets

Three target attributes by four separations (1, 2, 4, 8), 64 triplets per cell.

* Every cell fills to 64 within 64 to 70 attempts.
* The probe lines are byte-identical across roles in 768 of 768 triplets.
* Non-target offsets are exactly symmetric about the ideal in every probe.
* Smaller-value-is-nearer and straddle are exactly 0.500 in every cell.
* The nearer option sits at the first probe position in 0.496 of triplets.
* Separation error has a mean of 0.92 percent and a maximum of 5.9 percent, at
  the smallest separation, from rounding.
* The target attribute's rendered position is 263, 242 and 263 across the three
  slots.
* In-context variance, probe included, follows the roles in every prompt at the
  registered floor ratio of 2: about 370, 98 and 14 for high, medium and low.
* The top eigenvector of the in-context workload lies within 3.44 degrees of the
  high attribute in every prompt, median 1.44.
* Context distance from the ideal has the same distribution in every role,
  because the roles permute the same three spreads across attributes.

Two differences between roles remain, and both are recorded rather than removed.

**Option-line length differs with option-number digits.** It differs in 369 of 768
probe pairs. It is identical across the three roles of a triplet, and the shorter
line is the nearer option in 0.526 of those pairs, so it cannot produce a role
effect.

**Crowding differs by role.** The nearest context value to a probe value on the
target attribute has a median distance of 2.10 in the high role, 1.50 in the medium
role and 4.00 in the low role. The low-role probe sits outside a tight cluster.
Crowding would therefore favour the low role, which is the opposite of the budget
sign, and the simulation below finds it negligible.

### Simulated evaluators on the built prompts

Accuracy by role, pooled over target attributes. Each model has one noise level,
set so its high role sits at 0.75 at separation 1.

| model | separation | high | medium | low | high minus low |
|---|---|---|---|---|---|
| no budget, noise on the probe | 1 | 0.750 | 0.750 | 0.750 | +0.000 |
| | 4 | 0.996 | 0.996 | 0.996 | +0.000 |
| rank-1 budget on the in-context workload | 1 | 0.750 | 0.506 | 0.504 | +0.246 |
| | 4 | 0.989 | 0.526 | 0.520 | +0.469 |
| rank-2 budget on the in-context workload | 1 | 0.750 | 0.766 | 0.524 | +0.226 |
| | 4 | 0.995 | 0.997 | 0.609 | +0.387 |
| | 8 | 1.000 | 1.000 | 0.753 | +0.247 |
| normalisation by in-context spread | 1 | 0.750 | 0.994 | 1.000 | -0.250 |
| | 4 | 0.998 | 1.000 | 1.000 | -0.002 |
| confusion with nearby context values | 1 | 0.704 | 0.699 | 0.702 | +0.002 |
| | 4 | 0.963 | 0.959 | 0.966 | -0.003 |
| rank coding within the prompt | 4 | 0.570 | 0.792 | 0.607 | -0.036 |
| | 8 | 0.680 | 0.872 | 0.570 | +0.109 |

The no-budget model's role effect is zero exactly, not approximately. A rank-1
budget leaves the medium and low roles at chance while the high role is at ceiling.
A rank-2 budget keeps the medium role and loses only the low one, so the medium role
tells the two ranks apart. Normalisation predicts the opposite sign. Confusion with
nearby context predicts nothing measurable.

### Limits the simulation exposed

**The largest separation weakens the signature.** At separation 8 the rank-2
budget's low role rises to 0.753. A large probe offset adds variance to its own
attribute and tilts the workload toward it, so at that rung the probe partly
un-discards the attribute it is testing. Separation 4 is where the high role is at
ceiling and the probe's own contribution is still small. The primary rung should
be registered there in advance, not at the top of the ladder as the reread
suggested for the pair design.

**Rank coding is excluded only by the full profile.** At separation 8 it produces
a positive high-minus-low of 0.109, the budget's sign. It also puts the medium role
above the high role, 0.872 against 0.680, and neither budget does that. So the
registered signature must be the whole profile: high at least medium, at least low,
with the drop at the low role. A high-minus-low contrast alone would not exclude it.

### What this rebuild does not do

There is no registration, no bar, no sample size and no runner, and nothing has
been sent to the gateway.

The instrument has never been used in this format. Prompts are now 22 options
long, and the position-bias, parse and swap-consistency gates C1 needed have not
been measured on it. A pilot of the instrument gates on the set format has to come
before anything is graded.

The simulated models are the ones the readers raised plus the budget. A real
evaluator may do something none of them does. That is what the cold reread of this
rebuild is for, and on this programme's record it is where the defects have
surfaced in five consecutive designs.
