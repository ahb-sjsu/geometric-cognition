# Geometric Cognition claim ledger

One row per headline claim. Classes follow the observation-theory ledger and
GET's, `[proved]`, `[demonstrated]`, `[replicated]`, `[predicted]`,
`[exploratory]`, `[refuted]`, `[posited]`, `[open]`. A class is raised only by a
sealed pass and lowered by a sealed miss. Identifiers are assigned contiguously
and every identifier carries a disposition, including the ones that carry no
result.

**Converted 2026-09-13** from the book manuscript under PE-BRW-1.0, descriptive
first. No chapter was edited and no claim was re-derived. Conversion records what
support each claim actually has, not what the manuscript asserts for it.

## The split this ledger enforces

Every empirical row in the book fuses two claims that have different support.

1. A statistic computed on the Measuring AGI instrument differs from its null.
   That is measured.
2. The axis the statistic is computed on is a dimension of cognition. That is
   the representation, and in this corpus the representation was chosen by the
   author of the analysis.

The rows below separate them. An `-S` row carries the statistic and an `-I` row
carries the interpretation. Every `-I` row uses `GC-1`, the representation
posit, so no interpretation in this ledger can be graded above `GC-1` while
`GC-1` is `[posited]`. This is the support cap doing the work that the
manuscript's prose could not do, and it is the reason the conversion was worth
running.

The admission filter `xbse` ruled the cognitive instrument **inadmissible** on
2026-07-14, on the ground that no structure label independent of the embedding
was available. That verdict stands and it is what holds `GC-1` at `[posited]`.

---

## Representation and structure

| ID | Claim | Class | Stated | Uses |
|---|---|---|---|---|
| GC-1 | The five benchmark tracks are dimensions of cognition rather than an analyst's coordinates | `[posited]` | Appendix B, Ch 3 | none |
| GC-2 | Cognitive states form a manifold on which distance is meaningful | `[posited]` | Ch 3 | none |
| GC-3 | Attention is the metric, in the sense that what is attended defines which states are near | `[posited]` | Ch 4 | GC-2 |
| GC-4 | Working memory is the tangent space, the locally accessible neighbourhood | `[posited]` | Ch 5 | GC-2 |
| GC-5 | Executive function is search control over that manifold | `[posited]` | Ch 6 | GC-2 |
| GC-6 | System 1 is gradient following and System 2 is geodesic computation | `[posited]` | Ch 12 | GC-2, GC-5 |
| GC-7 | Development is manifold growth, with Piagetian stages as topological transitions | `[posited]` | Ch 13 | GC-2 |
| GC-8 | Cognitive pathology is geometric defect | `[posited]` | Ch 14 | GC-2, GC-3 |

## Scalar irrecoverability

| ID | Claim | Class | Stated | Uses |
|---|---|---|---|---|
| GC-9 | Contraction of a profile vector to a scalar is not invertible, so the discarded structure is not recoverable from the output | `[proved]` | Ch 1, Appendix A | none |
| GC-10 | What that contraction discards is what determines how a system reasons rather than how well | `[posited]` | Ch 1 | GC-9, GC-1 |

`GC-9` is linear algebra and holds whatever the axes mean. `GC-10` is the claim
that makes it matter, and it uses `GC-1`.

## Measured statistics, and their interpretations

Sigma values are transcribed from `BOOK_PLAN.md` and Appendix B. **The primary
run records are not in this repository.** No row below cites a result file, a
seed, or a configuration in this tree, so none can be re-executed here. That is
the conversion's sharpest finding and it is recorded rather than repaired.

| ID | Claim | Class | Stated | Uses |
|---|---|---|---|---|
| GC-11-S | Framing displacement on Social Cognition T5 differs from null at 15.3 sigma | `[exploratory]` | Ch 7, Appendix B | none |
| GC-11-I | That displacement is a framing effect in a social-cognitive dimension | `[posited]` | Ch 7 | GC-1, GC-11-S |
| GC-12-S | The sycophancy gradient on Learning L2 differs from null at 13.3 sigma | `[exploratory]` | Ch 8, Appendix B | none |
| GC-12-I | That gradient is belief revision under social pressure | `[posited]` | Ch 8 | GC-1, GC-12-S |
| GC-13-S | Systematic miscalibration on Metacognition M1 differs from null at 6.7 sigma | `[exploratory]` | Ch 9, Appendix B | none |
| GC-13-I | That miscalibration is a metacognitive monitoring failure | `[posited]` | Ch 9 | GC-1, GC-13-S |
| GC-14-S | Emotional anchoring on Executive Functions E2 differs from null at 6.8 sigma | `[exploratory]` | Ch 11, Appendix B | none |
| GC-14-I | That anchoring is an executive control failure | `[posited]` | Ch 11 | GC-1, GC-14-S |
| GC-15-S | Distractor displacement on Attention A1 differs from null at 4.6 sigma | `[exploratory]` | Ch 10, Appendix B | none |
| GC-15-I | That displacement is attentional capture | `[posited]` | Ch 10 | GC-1, GC-15-S |

The `-S` rows are `[exploratory]` and not `[demonstrated]`, because
`[demonstrated]` requires a registration predating the run, a committed result,
and a re-runnable instrument. None of the three is present in this repository.
The sigma values are not in doubt as arithmetic. Their class records what the
record here can show, which is less than the manuscript states.

## Model signatures and the frontier

| ID | Claim | Class | Stated | Uses |
|---|---|---|---|---|
| GC-16 | Five models occupy five distinct profile shapes rather than one shape at five scales | `[exploratory]` | Ch 16 | GC-1 |
| GC-17 | Composite scores converge in 0.63 to 0.72, and that band is a capability frontier rather than a coincidence | `[posited]` | Ch 16.9 | GC-1, GC-16 |
| GC-18 | The frontier is a surface rather than a point, because dimensions trade against one another | `[posited]` | Ch 16.9 | GC-17 |
| GC-19 | A divided-attention ceiling near 38 percent | `[exploratory]` | Ch 10 | GC-1 |
| GC-20 | Metacognitive Quadrant I is empty, no model both monitors and controls well | `[exploratory]` | Ch 9 | GC-1 |
| GC-21 | A model's signature is predictable from its architecture | `[open]` | Ch 16.12 | GC-16 |

`GC-17` is the row most exposed to the instrument's status. A convergence band
computed from composite scores is a statement about the composite, and Ch 1
argues the composite discards the structure the book is about.

## Inherited, not established here

| ID | Claim | Class | Stated | Uses |
|---|---|---|---|---|
| GC-22 | A rank budget coarsens distinctions and the induced preference is a semiorder with threshold the budget | `[proved]` | GET Thm 1, Thm 2, machine-checked | none |
| GC-23 | A rank-budget change reverses preference between fixed actions | `[proved]` (existence) | GET Thm 5, machine-checked | none |
| GC-24 | An evaluator's indifference threshold tracks its budget | `[demonstrated]` on a computational evaluator | GET gate G3, sealed | GC-22 |
| GC-25 | What a consumer can read is a property of the pair rather than of the system | `[demonstrated]` in other domains | Observation Theory campaign record | none |

These four are the machinery the thesis proposes to apply. They are graded by
their own repositories' sealed records and are listed here so that the cognitive
rows cannot borrow their strength silently.

## The thesis layer

| ID | Claim | Class | Stated | Uses |
|---|---|---|---|---|
| GC-26 | A cognitive observer is the quadruple representation, metric, budget, admissible set, together with a search policy | `[posited]` (definition) | OLGC paper Def 2 | none |
| GC-27 | With all four observer components fitted to a choice record, any finite record is reproduced, so choice alone cannot disconfirm the account | `[proved]`, and not new | OLGC paper Prop 3 | GC-26 |
| GC-28 | Under modular identification the induced order is determined and the account excludes records outside the budget's own indifference band | `[proved]` | OLGC paper Prop 5 | GC-26, GC-22 |
| GC-29 | Human cognitive budgets exist and are experimentally manipulable | `[posited]` | thesis 2.3, 7.1 | none |
| GC-30 | Bounded search is the right dynamical abstraction for cognition | `[posited]` | thesis 4.2 | none |
| GC-31 | Cognitive state space is Whitney stratified | `[posited]` | thesis 5.4 | GC-2 |
| GC-32 | Normalized transition observables collapse across substrates | `[posited]` | thesis 7.5 | none |
| GC-33 | How much a single unidentified component can absorb is not characterized, so identifying three of four is not known to beat identifying none | `[open]` | OLGC paper Open 6 | GC-27, GC-28 |

## Registrable, not yet sealed

| ID | Claim | Class | Stated | Uses |
|---|---|---|---|---|
| GC-34 | Under a registered budget manipulation with metric and ideal held fixed, reversals occur only for pairs trading a resolved direction against an unresolved one | `[predicted]`, unsealed | thesis 7.2, 8.1, OLGC paper P2 | GC-22, GC-23, GC-29 |

`GC-34` is Phase I and is the first row in this ledger that can fail. It is
`[predicted]` rather than `[demonstrated]` because no registration has been
sealed. Sealing it is the next act of this programme.

---

## Accounting

Identifiers `GC-1` through `GC-34` are assigned contiguously with no gaps. The
`-S` and `-I` suffixes split five identifiers and are counted once each.

Counted from this file rather than stated, by the script in
`claims/count_classes.py`. 39 rows over 34 identifiers, five of which split into
an `-S` and an `-I`.

| | count |
|---|---|
| `[posited]` | 21 |
| `[exploratory]` | 8 |
| `[proved]` | 5 |
| `[open]` | 2 |
| `[demonstrated]`, inherited from a sibling repository | 2 |
| `[predicted]`, unsealed | 1 |

Twenty-one of thirty-nine rows are posited and two are open, so more than half
of this ledger is commitment rather than evidence. Five of the remaining rows are
proved and belong to linear algebra or to a sibling repository's machine-checked
development, not to this one.

**Debt ratio 1.0.** Every row in this repository is retrospective. No claim here
was registered before the evidence that bears on it, and no gate has been sealed
in this repository. Near unity is expected at conversion. The number that matters
is its trajectory, and `GC-34` is the first thing that can move it.

**Dangling records.** Eight rows cite measurements whose primary artifacts are
not in this tree, `GC-11-S` through `GC-15-S`, `GC-16`, `GC-19` and `GC-20`. Under the inquiry arm's coherence property these are dependencies
that do not resolve, and a dependency that cannot be resolved is not one that can
be relied on. Locating those artifacts, or re-running them under a registration,
is the cheapest available reduction in debt after `GC-34`.

**What conversion did not do.** No chapter was edited, no claim re-derived,
nothing deleted. The manuscript states several of these rows more strongly than
the class assigned here. That disagreement is the conversion's output and is left
standing rather than resolved by rewriting the book.

*Verify with `pe_lint` once the rows are emitted as native claim objects. The
markdown form above cannot carry dependency edges in a form the checker reads,
which caps this ledger at L2 under PE-CLS-1.0 section 9.1.*
