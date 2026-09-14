# C2 registration, draft: does resource load open a class gap in order-dependence?

**Status: DRAFT. Not sealed. No run seed drawn. Section 9 is empty.**

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

**512 pairs per class per level**, margin matched, 2048 pairs in total. The
sampler produces cells of that size with margins matched to within 0.06. The size
is fixed by the power calculation in Section 6 and by nothing else.

**Both presentation orders at both levels.** A pair counts as order-dependent
when it parses in both orders and the verdict flips. A pair that fails to parse,
or that times out, is counted separately and is never added to that number.

**Generation limit 4096 tokens and per-item deadline 180 seconds.** C1's ladders
ran at 1024 and 60, and its Section 10.19 found that two of them had measured the
token cap rather than the evaluator. At load 16 mean reasoning was 918 tokens and
six items timed out.

## 5. Bars, each stated so that it can fail

**Primary.** Fisher exact, two sided, on genuine order-dependence, trading
against within-subspace, at load 16. A pass requires `p < 0.05` and the trading
rate above the within-subspace rate. A significant result in the opposite
direction is a fail, not a pass with the sign reversed.

**Baseline condition.** The same test at load 0 must return `p >= 0.05`. If the
gap is already there without load, C2-1 is not tested by this design and the run
is recorded VOID. This bar can fail, and it voids the gate when it does.

**Instrument gates, applied per level before anything at that level is graded.**
Zero unparsed comparisons, because the parse gate is registered at zero. Zero
deadline failures. Genuine order-dependence and no-verdict items counted
separately and never summed. First-position rate within 0.15 of
`q*b + (1-q)(1-b)`, the rate an unbiased evaluator of accuracy `q` returns on a
cell whose answer key has base rate `b`. At least 480 of 512 pairs graded per
cell. A level that fails any of these is INADMISSIBLE and carries no verdict.

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

*Empty. To be filled by a cold reread in a session other than the one that
drafted this, before sealing. C1's first reread returned three design defects and
eleven document defects. Its second found that two of its sections had measured a
generation limit rather than the evaluator. This section is not a formality.*

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
