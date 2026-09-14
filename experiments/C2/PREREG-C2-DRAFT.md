# C2 registration, draft: does resource load open a class gap in order-dependence?

**Status: DRAFT, revision 2. No run seed drawn. Section 9 records the cold
reread that refused revision 1, and Section 11 records the four repairs made in
response, what they cost, and the two of them that turned out to be weaker than
they looked. Still not sealed: a second cold reread is required, and the run is
an order of magnitude larger than anything this programme has executed.**

C1 is unsealed and stays unsealed. This is a separate gate testing one
pre-specified quantity that emerged from C1's fourth ladder, and it is written to
avoid the defects Section 10 of that registration catalogues. Where a choice here
is unusual, it is because C1 made the other choice and its record says what that
cost.

## 1. Claim under test

**C2-1.** Under distractor load, this evaluator's pairwise verdicts become
order-dependent at a higher rate on trading pairs than on within-subspace pairs,
and that gap is absent without load.

That difference in differences is the whole claim. Nothing else in this document
is graded.

## 2. Why this quantity and not a reversal rate

C1 graded reversal rates through four designs, and its Section 10.15 showed the
graded contrast is an identity in two agreement rates with no remainder. The
defect was structural. The fitted metric assigned the class, and the
pre-projected stimulus made agreement at the reduced budget automatic, so the
statistic could not fail and therefore could not succeed.

Order-dependence is a different quantity. A pair is order-dependent when the
evaluator's verdict flips as the two options exchange position. Neither the
fitted metric nor the rendering determines whether that happens. It is also where
the theory puts a partial budget: a budget that dissolves the discriminating
direction of a trading pair produces indifference rather than confident
inversion, and a forced-choice instrument expresses indifference as
order-dependence. C1's Section 4 registered that reading and then graded
reversals anyway.

## 3. The baseline is the control, not a subtraction

Trading pairs are harder than within-subspace pairs by construction, and C1
measured that four times: an accuracy gap of 0.09 to 0.17, and 411 reasoning
tokens against 340 at zero load. A raw class comparison under load would be
confounded by it.

The baseline controls for it. At zero load C1-D measured genuine order-dependence
at 0 of 64 in both classes, so the difficulty asymmetry shows in accuracy and
does not show in this endpoint. The claim is that load opens a gap the baseline
does not contain. Both levels are run, and a gap already present at baseline
voids the comparison rather than being subtracted from it.

## 4. Design

Fixed before any data is drawn. Consequence box `[0,100] x [0,45] x [0,75]`,
ideal `(75,15,20)`, `k = 1`, metric and retained subspace taken from
`pilot3_qwen3.json`. That design clears the spectral gap floor of 2.0 and the
discarded share floor of 0.05 at both budgets, and `assert_budget_usable` refuses
to run if a later draw does not.

**Two levels**, load 0 and load 16. Distractor attributes are drawn per pair and
are identical across the two options of that pair, so their contribution to the
difference of squared distances is exactly zero and the correct answer is
invariant at any load. This is asserted in code over every pair before anything
is sent.

**Three classes, not two.** `W`, difference in the retained subspace, order
preserved. `N`, difference with a large discarded component, order preserved.
`T`, difference with a large discarded component, order flips. A rank budget
predicts `N` behaves like `W`; a complexity or cancellation account predicts `N`
behaves like `T`. The two-class design could not separate those, and the sampler
was already generating `N` and discarding it, 22,311 candidates of 28,311.

**2048 pairs per class per level**, matched on decision SNR and not on geometric
margin. The match is asserted before any comparison is sent, at a registered
tolerance of 0.05 between any two classes, and a draw that misses it stops the
run. Achieved on trial draws: SNR means 0.909, 0.912, 0.915, worst gap 0.0063,
against a gap of 0.32 under the margin matching of revision 1.

**Three presentations per pair**, forward, reversed, and a same-order replicate
on a registered 25 percent subsample. All presentations, both classes and both
load levels are interleaved into one randomised submission set. Revision 1 ran
forward and reverse as separate blocks, which made the endpoint a between-block
difference and confounded condition with wall-clock time.

**The endpoint is swap flip minus the replicate floor.** A pair counts as
order-dependent when its verdict names a different option after the two exchange
position. The replicate measures how often the same gateway returns a different
verdict to an unchanged prompt, per class, so nondeterminism is subtracted rather
than assumed absent. A presentation that fails to parse or times out excludes its
pair from numerator and denominator alike and is counted by cause.

**Generation limit 4096 tokens and per-item deadline 180 seconds.** C1's ladders
ran at 1024 and 60, and its Section 10.19 found that two of them had measured the
token cap rather than the evaluator. At load 16 mean reasoning was 918 tokens and
six items timed out.

## 5. Bars, each stated so that it can fail

**Primary.** The `class x load` interaction coefficient of a logistic on swap
flip, fitted by Firth's penalised likelihood and tested by penalised likelihood
ratio, adjusted for decision SNR, log noise scale, opposing mass, displacement
and direction concentration. A pass requires `p < 0.05` and a positive
coefficient. Firth rather than an ordinary fit because the registered baseline
outcome is near zero events, where an unpenalised fit separates and the
interaction is not estimable at all, which is what revision 1's primary would
have hit under its own expected result.

**Co-primary, the discriminating contrast.** The same interaction for `N` against
`W`. A rank budget requires `T` above `W` and `N` indistinguishable from `W`. If
`N` tracks `T`, the result is a complexity effect and is recorded as one,
whatever the `T` against `W` contrast says. This bar can turn a passing primary
into a negative result, which is the point of it.

**Co-primary, the manipulation check.** The load-16 spectrum must move by more
than three times the same-load replicate floor. If it does not, the run yields a
behavioural finding and explicitly not a budget reading. Revision 1 placed this
under secondary, which inverted C1's own 10.19 disposition that a null from an
unverified manipulation is not evidence about budgets.

**Baseline condition, as equivalence and not as an accepted null.** The run is
VOID unless the 95 percent interval on the baseline class difference lies inside
plus or minus 0.010. Revision 1 required only `p >= 0.05` at baseline, which
zero events satisfies by default; the reread showed that zero of 64 bounds a rate
only at 0.046, most of the effect under test. At 2048 per class this margin
voids a fourfold baseline gap with probability 1.000 and proceeds when the
classes are truly equal with probability 0.993. A margin of 0.02 admitted the
confound 79 percent of the time.

**Instrument gates, applied per level before anything at that level is graded.**
No-verdict items, whether unparsed or timed out, at most 0.5 percent per cell,
reported by cause, excluded from numerator and denominator alike, and accompanied
by a sensitivity bound in which they are counted first all as order-dependent and
then all as not. First-position rate within 0.03 of `q*b + (1-q)(1-b)`, with `q`
computed over every pair that returned a letter in the forward presentation
rather than over swap-consistent survivors. There is no minimum-graded bar.
Revision 1 registered zero no-verdict items, which would have refused the run
that motivates this design and is unreachable across tens of thousands of calls;
a 0.15 position band, which admits a lean producing four times the effect under
test and which the trading class already exceeds in C1-D at every loaded level;
and a 480-of-512 minimum which, with the other two gates at zero, was
arithmetically the statement that the effect must not occur.

**Secondary, reported and not graded.** The spectrum under load, judged against a
same-load replicate. Two calibration blocks of 200 pairs run at load 16 with
independent distractor draws, and one at load 0. The replicate pair fixes the
noise floor for the gap and for the retained-direction angle, and movement is
reported as a multiple of that floor. C1-D had no replicate, which is exactly why
its spectrum reading was inconclusive.

## 6. Sample size, fixed in advance

C1-D observed 15 of 192 against 4 of 192, pooled over its loaded levels. Monte
Carlo, Fisher exact, two sided, at 0.05:

| pairs per class | power at the observed effect | power at half of it |
|---|---|---|
| 64 | 0.144 | |
| 256 | 0.845 | 0.356 |
| **512** | **0.992** | **0.677** |
| 1024 | | 0.931 |

512 is registered. The observed effect is assumed to be inflated, because it was
measured after a cold reader pointed at that specific quantity, so the design is
sized against the half-effect column and accepts 0.677 there rather than sizing
against the number that flattered it. C1 ran every cell at 64, where its power
against its own effects was 0.14 to 0.35, and did not say so.

## 7. What falsifies C2-1

1. No class gap at load 16, `p >= 0.05`.
2. A gap in the opposite direction, within-subspace above trading.
3. A gap already present at load 0. This voids rather than falsifies.
4. A gap that tracks rendered length or attribute range rather than class. Both
   are reported per class so a reader can check it.

## 8. What a pass would and would not mean

A pass would say that load makes this evaluator order-dependent specifically on
pairs whose order depends on directions a rank-1 projection discards. It would
not say the evaluator has a rank budget. The manipulation check is secondary here
because C1-D could not establish that distractor load moves effective rank at
all, and that question stays open regardless of how C2 comes out. A pass makes
the budget reading available; it does not confirm it.

A pass would also say nothing about human cognition. No measurement of a human
budget exists anywhere in this programme.

## 9. Reread record

**Readers.** Two, with no drafting context, 2026-09-13, given this file and the
C1 modules it reuses, and fenced off from `CAMPAIGN.md`, the paper and the
history. One asked whether every bar can fire. One attacked the design.

**Verdict: NOT SEALABLE. The design would return a pass under a model with no
rank budget.** Every number below was recomputed before being accepted.

### 9.1 The design defect that decides it

**Pure per-attribute noise reproduces the registered signature exactly.**
`build_pairs` matches the classes on `margin = |d(a) - d(b)|`. That is not the
quantity governing flip probability under noise that enters per attribute. Write
`c_i` for each attribute's contribution to `d(a)^2 - d(b)^2`. At matched margin:

| | W | T |
|---|---|---|
| `\|sum c_i\|` | 157.7 | 122.0 |
| `sqrt(sum c_i^2)` | 143.9 | 176.2 |
| **decision SNR** | **1.041** | **0.719** |
| `\|\|b - a\|\|` | 2.58 | 5.78 |

A trading pair's decisive margin is the small residue of large opposing terms; a
within-subspace pair's is not. Now take a model with no budget, no projection and
no geometry, in which load is only an increase in per-attribute noise `sigma`:

| `sigma` | W rate | T rate | difference | ratio |
|---|---|---|---|---|
| 0.005 | 0.0017 | 0.0025 | 0.0009 | 1.54 |
| 0.050 | 0.0054 | 0.0273 | 0.0218 | 5.00 |
| 0.120 | 0.0138 | 0.0588 | 0.0451 | 4.28 |
| 0.200 | 0.0239 | 0.0924 | 0.0685 | 3.87 |

C1-D observed 0.0208 against 0.0781, a difference of 0.0573 at a ratio of 3.75.
That sits on this curve. The confound is multiplicative, so it vanishes at the
floor and grows with load, which is precisely the difference in differences this
registration treats as diagnostic. **The pattern C2-1 predicts is also what
isotropic noise predicts, and this design cannot separate them.**

### 9.2 The control the design already generates and throws away

`build_pairs` draws pairs with a large discarded component and discards every one
whose rank-1 order agrees with the full order, 22,311 of 28,311 candidates. Call
that class N. It carries T's stimulus complexity and W's theoretical status,
because under a rank-1 budget the retained direction is decisive and agrees.
Margin-matched it sits beside T on every complexity axis and beside W on the
budget prediction. A budget account predicts N behaves like W; a complexity or
cancellation account predicts N behaves like T. The two-class design cannot
separate those; adding N separates them in the same run for 512 more pairs per
level. C1's own 10.1 D3 proposed this species of control and this draft did not
carry it forward.

### 9.3 A class-differential position lean is already in the data

| load | W first-position minus answer key | T |
|---|---|---|
| 0 | +0.000 | +0.031 |
| 4 | +0.000 | +0.047 |
| 8 | +0.016 | +0.040 |
| 16 | -0.002 | +0.057 |

The within-subspace class tracks its answer key at every level. The trading class
runs above it at every level and the lean grows with load. Under a mixture model
in which the evaluator answers by position with probability `pi`, a deviation of
0.025 from the reference produces order-dependence of about 0.041, which is most
of the 0.057 gap under test. The registered band is 0.15, which admits a
deviation producing four times the effect. The gate cannot fire on the thing it
names.

Its reference is also wrong for the fourth time. `condition_admissible` takes `q`
from `q_agree_full_survivors`, which conditions on excluding order-dependent
pairs, the very exclusion under study, and estimates it from the cell being
graded. Because `q_T < q_W` the reference is pulled toward one half for the
trading class, making the band effectively wider for the class the hypothesis
concerns.

### 9.4 The instrument gate fires because the hypothesis is true

Section 5 requires at least 480 of 512 pairs graded. In the code this reuses,
`n_graded` counts pairs consistent in both orders, and with unparsed and deadline
separately pinned at zero the only remaining way to fail is genuine
order-dependence. So the gate is exactly `genuine <= 32`, a rate of 0.0625,
against a registered effect of 0.0781.

| true trading rate | expected count of 512 | probability the cell is refused |
|---|---|---|
| 0.0781, the registered effect | 40.0 | **0.894** |
| 0.0625 | 32.0 | 0.453 |
| 0.0495, half the effect | 25.3 | 0.077 |

Joint probability of an admissible cell and a passing primary: **0.091**, against
the 0.992 Section 6 claims. Under the other reading of "graded" the bar is
redundant with the two zero gates and can never fire. There is no reading on
which it is useful. This is the defect class C1's 10.2 catalogues, reproduced in
a document written to avoid it, under a heading reading "Bars, each stated so
that it can fail."

### 9.5 The zero-deadline gate refuses the evidence that motivates this design

C1-D recorded deadline failures of 1 at load 8 and 10 at load 16, plus 3, 2 and 1
in the calibration blocks. A zero tolerance therefore makes loads 8 and 16 of
C1-D inadmissible, including the level that produced the 0 against 5 result and
half the pooled counts Section 6 sizes from. At load 16 the number of unusable
items exceeds the number of events, and the missingness is class-differential, 3
against 7. Zero across roughly 5,300 gateway calls is not an achievable bar, and
"inadmissible, no verdict" is a fail-when-true outcome with no recovery path.

### 9.6 The primary statistic is not the claim

Section 1 registers a difference in differences. Section 5 registers significance
at one level plus non-significance at another, which is difference in
significance and not a test of an interaction. The interaction is never
estimated and never given an interval, and under the outcome Section 3 expects,
zero events in both baseline cells, the baseline odds ratio is undefined and no
difference in differences can be fitted at all. The headline quantity is not
estimable from the registered data under the registered expectation.

### 9.7 The baseline is a floor, not a control

Zero of 64 gives a one-sided 95 percent upper bound of 0.0457. Pooling both
baseline classes, zero of 128 bounds a rate at 0.0231. The effect under test is
0.021 against 0.078. The upper bound on what the baseline could be hiding is
about 80 percent of the trading rate the design is powered to detect. Seeing zero
in 64 licenses "the baseline gap is smaller than the effect we are looking for",
which is not a control. And because the confound in 9.1 is multiplicative it
holds the ratio roughly fixed while the difference scales with load, so absence
at the floor is what that confound predicts.

### 9.8 The void check is a coin flip against the confound it exists to catch

Probability the baseline test correctly returns `p < 0.05`, at 512 per class:

| baseline W rate | T rate | probability of VOID | passes by default |
|---|---|---|---|
| 0.002 | 0.008 | 0.103 | **0.897** |
| 0.005 | 0.020 | 0.489 | **0.511** |
| 0.010 | 0.040 | 0.860 | 0.140 |

The ratio-four rows are the ones that matter, because that is the confound's
shape. The design catches a fourfold baseline gap at the 0.005 floor half the
time and at the 0.002 floor a tenth of the time, while catching the same
structure under load with power near 0.99. It finds the gap where it is large and
misses it where it is small.

### 9.9 Smaller defects, each confirmed

The margin tolerance of 0.06 is asserted and enforced nowhere, and fails at 3 of
10 candidate seeds, worst 0.0858. Since the seed is drawn after sealing, the
registration would commit to a tolerance it discovers it has missed only
afterwards. `assert_budget_usable` takes its arguments from the frozen pilot and
cannot fire on any run draw. `verify_invariance` builds both renderings from the
same array and can fail only if the renderer is broken. The generation limit of
4096 is not the operative ceiling, because the chooser escalates once to 8192.
Section 4's justification for the 180 second deadline splices two runs: 918
tokens is from the 1024-cap ladder, which had zero timeouts, and the six-timeout
figure is from the 4096 run, whose true deadline count is 10 and whose mean
reasoning was 646 and 728. Section 6's "0.14 to 0.35" misreads its own table, in
which 0.356 is the 256-pair cell and the 64-pair half-effect power is 0.030.
Falsifier 4 names rendered length, which is 154 characters in both classes by
construction and therefore inert, and gives no threshold that could convert
"tracks" into a fail. No code computes the primary statistic; there is no Fisher
exact anywhere in the codebase, no class comparison of genuine order-dependence,
and no same-load replicate.

### 9.10 What the readers found sound

The endpoint is not an algebraic identity in the accuracy, so C1's 10.15 defect
is genuinely not reproduced, and Section 2's diagnosis of it is correct. The
cancellation argument for the distractors is correct under any positive
weighting. The power table reproduces by exact enumeration, every cell within
0.018. The box, ideal, spectral gap and discarded share all check out. The
sampler fills 512 per class at all ten seeds tried. The margin match holds across
the full distribution even where the means miss, at a two-sample KS `p` of 0.98.
Every claim this file makes about C1 checks out against C1's own record.

### 9.11 Required before this can be sealed

Four repairs, in order of value against cost.

1. A same-order replicate. Every pair is presented a third time in the order it
   was first shown, which measures the gateway's own flip floor per class and
   converts the endpoint into `flip(swapped)` above `flip(same order)`. The
   forward and reverse presentations currently run as separate blocks, so the
   endpoint is literally a between-block difference and any drift on a shared
   gateway reads as order-dependence.
2. The N control class, which the sampler already produces and discards.
3. Matching on decision SNR rather than on geometric margin, with the achieved
   match registered and asserted, and a registered covariate adjustment for
   `sqrt(sum c_i^2)`, opposing mass, `||b - a||` and direction concentration.
4. A graded interaction statistic, by penalised logistic regression that survives
   zero cells, with the baseline stated as an equivalence test rather than as
   null acceptance, and the manipulation check promoted from secondary to
   co-primary so that a spectrum which does not move cannot leave a pass
   standing.

The instrument bars need rewriting alongside: delete or rescope the 480 gate,
replace the zero-deadline bar with a tolerance and an exclusion rule, and tighten
the position band to 0.03 against a reference computed on all pairs that returned
a letter rather than on survivors.

This file is not renamed and not sealed. No run seed is drawn.

## 10. Sealing procedure

1. Commit this file, the design constants, and the instrument gate thresholds.
2. Reread cold in another session and record it in Section 9.
3. Rename to `PREREG-C2.md`, commit, and record the blob hash.
4. Only then draw the run seed, grade, and commit the result as executed,
   whatever it says.

No pilot fixes any tolerance here. Every bar in Section 5 is fixed by the
registered design or by the power calculation in Section 6, and none is set from
data this design will later grade. C1 fixed its tolerances from a pilot three
times and superseded them twice.

## 11. What the repairs cost, including where they made the design weaker

Recorded here rather than discovered after a run.

**The interaction statistic is much less powerful than the test it replaces.**
Grading the `class x load` interaction is the correct statistic for a difference
in differences, and revision 1's difference in significance was not. But the
baseline cells carry almost no events, so the interaction is estimated from very
little. Simulated at the observed effect shape, baseline 0.004 in both classes
and loaded 0.020 against 0.078:

| pairs per class | power of the interaction test |
|---|---|
| 512 | 0.317 |
| 1024 | 0.467 |
| **2048** | **0.817** |
| 4096 | 1.000 |

Revision 1 claimed 0.992 at 512 for a statistic that was not testing the claim.
The honest statistic needs four times the sample for less power. 2048 is
registered.

**The equivalence margin had to be tightened by a factor of two, and the first
value admitted the confound.** At a margin of 0.02 the baseline check passes a
fourfold baseline gap 79 percent of the time, and a fourfold gap at the floor is
exactly the shape the noise confound in 9.1 takes. At 0.010 with 2048 per class
it voids that gap every time and proceeds on truly equal classes 99.3 percent of
the time. A margin of 0.005 would be stricter still but rejects equal classes 54
percent of the time at this size.

**SNR matching removes most of the confound and not all of it.** Under the
no-budget noise model of 9.1, the predicted `T` minus `W` gap falls from 0.0464
to 0.0084 at the noise level that reproduces C1-D's observation. That residual is
about 15 percent of the effect under test, which is why the covariate adjustment
in Section 5 is registered rather than optional.

**The run is an order of magnitude larger than anything this programme has
executed.** Three classes, two levels, 2048 pairs, two full presentations plus a
25 percent replicate subsample is **27,648 comparisons**. C1's runs were 1,800 to
5,300. The replicate is a subsample because it estimates a per-class floor rather
than a per-pair quantity; at 25 percent its standard error is 0.0018 against a
floor near 0.01.

This is a load on shared infrastructure, and the `ellm` gateway's fair-use limits
are not recorded in the NRP policy memory. The size is a consequence of doing the
statistics honestly, not a preference, but whether it may be run is a question
about the shared resource and is not settled by this document. The design is
registered at 2048 and the decision to execute is separate.

**One thing that got simpler.** Revision 1 carried three instrument gates that
could not do what they named. All three are gone: the minimum-graded bar was the
arithmetic complement of the endpoint, the zero-deadline bar was unreachable and
would have refused this design's own motivating evidence, and the 0.15 position
band admitted four times the effect. What replaces them is one tolerance on
no-verdict items with a sensitivity bound, and one position band at 0.03 measured
against a reference that does not condition on the pairs under study.
