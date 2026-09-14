# C3 design note: measure the sensitivity profile, select nothing

**Status: DESIGN NOTE, SECOND REBUILD, NOT YET REREAD. No bars, no seed, no
run.** Three constructions are recorded below in order. The pair construction was
refused. The multi-option rebuild was refused for a low-role cue and for being
unable to tell a capacity budget from a relevance judgement. The second rebuild,
at the end, keeps the context independent of the probe, adds a heavy-tailed low
column, and adds an oblique arm in which every per-attribute no-budget model
predicts exactly zero. A residual isolation cue and multivariate shrinkage remain
and are recorded. The second rebuild has not been reread.

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

## Reread of the rebuild, 2026-09-13

Two readers with no drafting context, given only this note and `c3_sets.py`,
fenced off from C1, C2, `CAMPAIGN.md`, the paper and the history. One checked the
construction for any difference between the three prompts of a triplet other than
the variance role. One attacked the logic with about thirty simulated evaluator
models on the built prompts. The findings marked reproduced were rerun before
being recorded.

**Verdict: the rebuild is not usable as specified.** It can show that context
changes how an evaluator compares two identical options. It cannot show that the
cause is a rank budget, because several models with no capacity limit reproduce
the budget's profile, and because the construction gives the low role a cue that
runs the other way.

The text of the three prompts is identical except for the 20 context lines, on
every one of 3,840 triplets checked. Every finding below is in the numbers.

### A cue that exists only in the low role

Reproduced. The farther probe option is the most extreme value on the target
attribute in every low-role prompt, and in no high-role prompt:

| separation | farther option extreme on target, low role | "pick the less isolated option" accuracy, high / mid / low |
|---|---|---|
| 1 | 1.00 | 0.53 / 0.51 / 0.67 |
| 4 | 1.00 | 0.52 / 0.57 / 0.89 |
| 8 | 1.00 | 0.41 / 0.70 / 0.99 |

The cause is in `c3_sets.py`. `NONTARGET_OFFSET` puts probe values outside the
tight low-variance cluster, and the exclusion window keeps context values away
from probe values. Both were chosen to avoid crowding. Together they make the
probe the outlier of its own column exactly when its attribute is low-role.

The cue makes the low role easier, which is the opposite of the budget's sign. It
would mask or cancel a real budget. At separation 8 it also lifts the medium role
above the high role, which is the profile this note used to rule out rank coding.

### The exact null is exact and does little work

The null covers evaluators whose decision uses the probe lines alone, and within
that scope it is exact by construction. But in a transformer every token's
representation depends on the whole prompt, so a context-blind evaluator is not a
plausible model, and rejecting it shows only that context matters. The weight of
inference falls on the alternatives table, and the table was missing the model
most likely to mimic the budget.

**Central tendency is that model.** Each value is shrunk toward the context by an
amount set by its column's spread, as a Bayesian observer with a prior from the
displayed set would do. It has no capacity limit. Reproduced at separation 4,
shrinkage parameter 5: 0.995 / 0.974 / 0.726. That is the budget's profile, a drop
at the low role with high and medium near ceiling. The reader's version gave 0.59
in the low role, against the rank-2 budget's 0.61; the size depends on the free
shrinkage parameter, and the shape does not. Column-scaled saturation, relevance
inference that down-weights low-variance attributes, one-sided anchoring on nearby
context values, and dilution restricted to the target column all produce the
budget's sign as well.

### The design cannot tell a capacity budget from a relevance judgement

The context is decorrelated, so its second moment is diagonal. Projecting onto the
top eigenvectors of a diagonal matrix is the same computation as giving zero weight
to the lowest-variance attributes. On these stimuli a rank budget and a rule that
ignores low-variance attributes are one model, and nothing here separates capacity
from judged importance.

The feature that would separate them is an **oblique workload**: two attributes
strongly correlated in the context with equal marginal variances, and the probe
varying along their difference. With marginals of 200 and correlation 0.9 the
variances are 380 along the sum and 20 along the difference. A rank budget predicts
a loss there. Per-attribute relevance, saturation, anchoring and outlier models
predict none, because the marginals match. Only multivariate shrinkage still
mimics the budget.

### The budget model rests on premises the note did not state

Reproduced: with the probe excluded from the workload, the rank-2 budget gives
0.500 in the low role at both separation 4 and separation 8. The weakening at
separation 8 that this note used to choose separation 4 as the primary rung came
entirely from including the probe in the workload, not from anything about the
evaluator. The probe is 43 to 68 percent of the low attribute's in-context second
moment, so the "low" variance of about 14 is mostly the probe.

A budget defined on the two named options alone predicts no role effect at all,
because a rank-2 projection of two points loses nothing. The design's prediction
therefore depends on the budget being computed over the whole displayed set before
the question is read. The question comes last in every prompt, and
`render_prompt`'s `question_first` argument swaps the two option numbers without
moving the question. Centring about the ideal and about the context mean give the
same answer, because the context is centred on the ideal by construction, so the
design cannot tell which the evaluator uses.

### Other construction differences between roles

* **The probe's distance rank among the 22 options shifts with role.** Context
  options closer to the ideal than the nearer probe, high minus low, paired within
  triplet: +0.27 at separation 4 and +0.36 at 8. The exclusion window is the cause;
  regenerating contexts without it gives about -0.04. The note's claim that context
  distance from the ideal has the same distribution in every role holds pooled and
  fails per prompt.
* **Context rejection is heavily role-dependent.** A low-role context needs about
  292 draws per success against 80 for high and 66 for medium. All 235 failed
  triplets across five seeds fail on the low-role context, and they select probes:
  those with a nearer target offset in the lowest band are kept 65 percent of the
  time against at least 99 percent otherwise. The "64 to 70 attempts" figure counts
  whole triplets and hides this.
* **Crowding is asymmetric within the pair and only in the low role.** On the
  target attribute the farther option's nearest context value has a median distance
  of 7.0 in the low role against about 2 elsewhere; the "4.00" in this note pooled
  both options. The low-role context sits entirely on the ideal's side of the probe,
  which favours the budget's sign for any anchoring model.
* **Variance role comes bundled with in-context range and shape.** In-context range
  has a median of 63.7, 33.9 and 16.6 by role. "Every attribute spans the same
  range" is true of the permitted box and not of what the evaluator sees. The box
  truncates the high column, and QR orthogonalisation makes column shape depend on
  the attribute's index, so attributes are not exchangeable within a cell.
* **Smaller items.** The probe adds a cross-product between its two non-target
  attributes, correlation up to 0.16. Context values rendered as "50.0", the same
  string as the ideal, occur 0.03, 0.07 and 0.19 per prompt by role. Target-attribute
  position and nearer-first position are random draws rather than stratified, and
  the note's counts were one seed.

### The profile test, the sample and the instrument

"High at least medium at least low, with the drop at the low role" names no test
and no decision rule. Read literally, a rank-1 result, high above medium equal to
low, fails it, which contradicts this note's claim that the medium role separates
rank 1 from rank 2. A usable version tests the three paired differences by exact
McNemar and classifies with equivalence tests into drop-at-low, drop-at-medium,
graded, medium-on-top, or indeterminate, with ceiling cells indeterminate by rule.
That test separates rank 1, graded relevance and rank coding. It does not separate
rank 2 from central tendency, relevance of the saturating kind, or column-scaled
saturation.

Detecting a high-minus-low difference of 0.10 needs roughly 70 to 330 triplets
depending on baseline accuracy and correlation within a triplet. Telling rank 1
from rank 2 by equivalence needs roughly 350 to 700 at the primary rung, several
times the 64 per cell built here.

Choosing separation 4 from a simulation of the favoured model is a problem. It
also sits where the opposite-sign models are at ceiling and rank coding is weakest.
A principled choice is to measure the evaluator's own accuracy curve in a pilot
with a flat context, and register the separation where it reaches about 0.85 to
0.90 before any role data exist.

The instrument adds failure modes that can depend on role. Reading a target value
from a context row is role-dependent, because low-role context values sit near 50.
A reasoning model computing distances exactly would sit at ceiling in every role,
so the reasoning mode must be registered and reasoning tokens logged. Answers
outside the two named options have to be scored as errors rather than dropped, or
the harder roles are censored. Parse and swap-consistency gates must be reported
per role. The mirror-symmetric non-target values repeat in every probe and can be
learned, which turns the task into a one-number comparison.

The simulation behind this note's table is not in the repository. The rank-coding
row does not reproduce as described, because its best high-role accuracy at
separation 1 without noise is 0.539, below the 0.75 the calibration targets.

### What the readers found sound

The probe lines are byte-identical across roles in every triplet. The prompt text
differs only in the 20 context lines. Sign patterns are exactly balanced in every
cell. Context-only correlations stay below 0.003 after rounding. The variance-rank
floor never binds, with a smallest ratio near 3 against a floor of 2. Nothing is
selected on a fitted model. Per-column noise that follows role is roughly neutral
when every column is processed, because each prompt contains all three roles.

### What would have to change

These are design decisions for the owner, recorded in order of what they separate.

1. **An oblique workload.** Correlated attributes with equal marginals, probe along
   the low-variance diagonal. It is the only change that separates a rank budget
   from per-attribute relevance, saturation, anchoring and outlier models.
2. **Break the probe's standing from its column's variance.** A heavy-tailed
   low-variance column, most values tight to the ideal and a few beyond the probe,
   so the probe sits inside its column's range. That removes the isolation cue and
   the saturation, outlier and one-sided anchoring mimics. Budget and central
   tendency both still predict a drop.
3. **Register the workload premise and vary question placement.** A budget over what
   is encoded before the question should shrink when the two options are named
   first; a relevance judgement should not.
4. **A registered decision table and a sample to match.** McNemar and equivalence
   tests per the classes above, the primary separation fixed from a flat-context
   pilot, and several hundred triplets at that separation.
5. **Commit the simulation code**, and register the family of context-dependent
   no-budget models, central tendency first, as the adversaries a budget reading must
   beat.

The first two change the stimulus distribution itself and should be settled before
the rest are built.

## Second rebuild: an oblique workload and a heavy-tailed low column, 2026-09-14

This section answers the first two changes the reread of the multi-option rebuild
required. The code is `c3_sets2.py`, and every number below is printed by
`c3_verify2.py`, which is committed with it. The reread found that the previous
simulation table had no code behind it. The two earlier constructions stay in the
repository as the record of what was refused.

### One principle: the context never depends on the probe

The low-role cue in the first rebuild came from conditioning the context on the
probe. Probe values were pushed outside the tight low cluster, and an exclusion
window kept context values away from them. Both are gone. Context values now come
from fixed templates: wide (root-mean-square 20), mid (10) and heavy. The only
rejection rule looks at the context by itself. It keeps a draw when every pair of
columns has a sample correlation within 0.10, and it never looks at the probe.

**Axis arm.** Each triplet draws one set of 20 context rows, each row holding one
wide, one mid and one heavy value. A role decides only which attribute receives
which. Across the three prompts of a triplet, every context option's distance from
the ideal is therefore identical, and so is the probe's distance rank among the 22
options. This answers the reread's findings that probe rank and per-prompt distance
distributions shifted with role.

**Heavy-tailed low column.** The heavy template has 12 values within one unit of
the ideal, single values at 3.5, 6.5 and 9.5 on each side, and tails at 12. Its
variance is 29, against 100 for mid and 400 for wide. Probe target offsets are
capped at 10, inside the tails.

**Oblique arm.** Two attributes `A` and `B` are built from a wide component `s`
and a heavy component `d`, as `A = 50 + (s + d)/sqrt2` and `B = 50 + (s - d)/sqrt2`.
The workload is then 400 along `A + B` and 29 along `A - B`. The paired prompt
mirrors `B` about the ideal. That exchanges the two directions and leaves every
`|value - 50|` unchanged, so each context option's distance from the ideal and each
column's spread about the ideal is identical across the pair. The only thing that
changes is the sign of the correlation. The probe varies along `A - B` and is
identical in both prompts. The third attribute takes the mid template, and which
two attributes form the pair is counterbalanced.

### Construction checks, two seeds

Both seeds give 576 items per arm, with every cell filled.

| check | axis arm | oblique arm |
|---|---|---|
| probe lines byte-identical across prompts | 576/576, 576/576 | 576/576, 576/576 |
| each context option's distance to the ideal identical | 576/576, 576/576 | 576/576, 576/576 |
| probe distance rank identical | 576/576, 576/576 | 576/576, 576/576 |
| a probe value is the most extreme in its column, any role | 0.000 | 0.000 |
| each column's `\|value - 50\|` multiset identical across the pair | n/a | 576/576, 576/576 |
| smaller value is nearer | 0.500, 0.500 | on `A` 0.486 and 0.498; on `B` 0.495 and 0.493 |
| pair straddles the ideal | 0.500, 0.500 | 0.500, 0.500 |

In the axis arm the context variances are exactly the registered 400, 100 and 29
in every role. The largest column correlation in any prompt is 0.102. In the
oblique arm the marginal variances of `A` and `B` are 215 and 214 in both prompts,
and the directional variances swap between 400 and 29. Separation error has a mean
of about 1.5 percent and a maximum of 9.3 percent, at the smallest separation, from
rounding.

The extremeness cue that made the first rebuild unusable is gone. The farther
probe option was the most extreme value on its attribute in every low-role prompt.
It is now never the most extreme value in any column, in either arm.

### Simulated evaluators, seed 20260914

Accuracy at separation 4. Each model's noise is set so the axis arm's high role
sits at 0.75 at separation 1.

| model | axis arm: high / mid / low | axis high minus low | oblique: high / low | oblique high minus low |
|---|---|---|---|---|
| no budget, noise on the probe | 0.996 / 0.996 / 0.996 | +0.000 | 0.996 / 0.996 | +0.000 |
| rank-1 budget | 0.991 / 0.505 / 0.504 | +0.487 | 0.991 / 0.502 | **+0.489** |
| rank-2 budget | 0.995 / 0.994 / 0.496 | +0.498 | 0.994 / 0.505 | **+0.490** |
| univariate shrinkage, tau 5 | 0.995 / 0.979 / 0.858 | +0.137 | 0.989 / 0.989 | **+0.000** |
| relevance weight, variance over maximum | 0.993 / 0.809 / 0.617 | +0.376 | 0.983 / 0.983 | **+0.000** |
| column-scaled saturation | 0.996 / 0.992 / 0.963 | +0.033 | 0.995 / 0.995 | **+0.000** |
| multivariate shrinkage, tau 5 | 0.995 / 0.978 / 0.856 | +0.139 | 0.995 / 0.859 | **+0.136** |
| anchoring on the 3 nearest per column | 0.999 / 1.000 / 1.000 | -0.001 | 0.998 / 0.998 | -0.000 |
| rank coding within the prompt | 0.701 / 0.948 / 0.919 | -0.219 | 0.852 / 0.852 | +0.000 |

The second seed agrees within 0.005 on every oblique contrast.

**The oblique arm does what it was built for.** In the axis arm, three models with
no capacity limit give the budget's sign: univariate shrinkage, relevance weighting
and saturation. In the oblique arm all three give exactly zero, because nothing
about any single attribute differs between the two prompts. A rank budget gives
about 0.49 in both arms. The axis arm on its own cannot tell a budget from a
relevance judgement, and the oblique arm can.

**Multivariate shrinkage survives, as expected.** Shrinking toward the context
along its full covariance moves the probe most along the low-variance direction
whatever that direction is. It gives the budget's sign in both arms, at about a
quarter of the budget's size at this setting. The design cannot exclude it, and a
budget reading has to carry it as a live alternative.

**Two smaller results.** With the heavier low column, a rank-2 budget that includes
the probe in its own workload now stays near chance at separation 4 (0.529, then
0.533 on the second seed). In the first rebuild that figure rose to 0.753 at
separation 8. Rank coding still cannot be calibrated to 0.75, as the reread found,
and its sign is opposite or zero.

### The residual cue, recorded rather than removed

A rule that picks whichever probe option has the nearer context option in three
dimensions still scores above chance in the low role:

| arm, role | seed 20260914 | seed 20260915 |
|---|---|---|
| axis, high | 0.510 | 0.488 |
| axis, mid | 0.476 | 0.486 |
| axis, low | **0.644** | **0.651** |
| oblique, high | 0.502 | 0.509 |
| oblique, low | **0.630** | **0.668** |

This cannot be designed away. A column with low variance that still spans the
probe's range has to thin out away from the ideal. With the non-target attributes
symmetric, the farther option always has the larger target offset, so in the low
role it always sits in sparser territory.

The template was chosen to minimise this cue before any budget result was
examined. The first heavy template left an empty band between its core and its
tails, and there the rule reached 0.72 in the low role. Four candidates were
compared on the rule alone. Filling the band brought it to about 0.64. Two
candidates tied within 0.005, and the one with lower variance was kept.

The cue makes the low role easier, which is the opposite of the budget's sign.
It cannot produce a budget reading. It can mask one, so a null result in the low
role or the low-variance direction is not interpretable on its own. The analysis
has to carry the isolation-rule prediction as a registered covariate, item by item.

### What remains from the reread's list

Items 3 to 5 of the reread's required changes are not done. The whole-set premise
is not registered, and question placement is not varied. There is no decision
table, and no primary separation has been fixed from a flat-context pilot. The
family of no-budget adversaries is not registered either, though the verification
script now implements the models used here.

The instrument has never been run on 22-option prompts, the reread's sample-size
estimate of several hundred triplets at the primary separation still applies, and
the non-target values are still mirror-symmetric about the ideal in every probe,
which a reader flagged as a learnable regularity. Nothing has been sent to the
gateway. This rebuild has not been reread.
