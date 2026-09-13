# Observer-Limited Geometric Cognition

**Andrew H. Bond** · Senior Member, IEEE · San José State University

> **Status (2026-09-13).** The book in `chapters/` is a domain exposition at
> `[posited]`. The claim ledger that grades it is `claims/LEDGER.md`, converted
> from the manuscript on 2026-09-13 with debt ratio **1.0**, meaning every row
> here is retrospective and no gate has been sealed in this repository. The
> foundational paper is `paper/olgc.tex`, draft 0.1. Nothing in this repository
> is a claim beyond those records.

Cognition is modeled here as search over observer-relative, resource-limited
geometries of possible states. An agent represents a task under finite
resolution, evaluates represented consequences in a geometry of its own, and
selects behavior by bounded search. Preference and choice are derived objects.
They can change when the representation, the budget, the metric, the reference,
the admissible set, or the search process changes, while the external
alternatives stay fixed.

## What changed, and why the repository was realigned

The book was written as a posited domain instantiation. Its admission filter
[`xbse`](https://github.com/ahb-sjsu/xbse) ruled the cognitive instrument
**inadmissible** on 2026-07-14, because no structure label independent of the
embedding was available. The representation was fitted to the same behavior it
explained.

That verdict has not been overturned and this realignment does not overturn it.
What changed is that the machinery for answering it now exists in two sibling
programmes, and the open problem has a name.

- [**Geometric Evaluation Theory**](https://github.com/ahb-sjsu/geometric-evaluation-theory)
  proves that a rank budget coarsens distinctions, that the induced preference is
  a semiorder whose threshold is the budget rather than a fitted parameter, and
  that a budget change reverses preference between fixed actions. Gates G2, G3
  and G5 have run under sealed registrations.
- [**Observation Theory**](https://github.com/ahb-sjsu/observation-theory-campaigns)
  establishes across twenty-nine tracks that what a consumer can read is a
  property of the pair rather than of the system.

The open problem is identification, and `paper/olgc.tex` is about it. A
representation, a metric, a reference, an admissible set and a search policy
together form a family expressive enough to reproduce any finite choice record.
An account that fits every record excludes none. The paper states that as a
proposition, credits the prior results it restates, and gives the condition under
which the account carries content. Each component of the observer must be
identified on evidence disjoint from the choices the theory is asked to predict.

## The split the ledger enforces

Every empirical row in the book fuses a measured statistic with an
interpretation of the axis it was measured on. The ledger separates them. An
`-S` row carries the statistic and an `-I` row carries the interpretation, and
every `-I` row depends on `GC-1`, the claim that the benchmark tracks are
dimensions of cognition rather than an analyst's coordinates. `GC-1` is
`[posited]`, so no interpretation in this repository can be graded above it.

That is the support cap doing work the manuscript's prose could not do, and it
is why the conversion was worth running.

## Layout

| Path | Contents |
|---|---|
| `paper/olgc.tex` | Foundational paper, draft 0.1. Every statement labeled proved, defined, posited, or open |
| `claims/LEDGER.md` | The claim ledger. 39 rows over 34 identifiers, gap-free |
| `claims/count_classes.py` | Produces the ledger's accounting block, so the counts are computed rather than typed |
| `chapters/` | The manuscript, 17 chapters, unedited by the conversion |
| `appendices/` | Mathematics, the benchmark suite, model profiles, notation |
| `observer_limited_geometric_cognition_thesis.docx` | The research thesis this repository is aligned to |

## Protocol

The registration discipline of `ahb-sjsu/observation-theory-campaigns`,
`ahb-sjsu/geometric-observation` and `ahb-sjsu/geometric-evaluation-theory`
applies unchanged, and is restated in full in [`PROTOCOL.md`](PROTOCOL.md). Seal
before run. Event presence first. Misses at full prominence. Numbers trace to
artifacts. Compute where it belongs. Owner submits. No em dashes, colons, or
semicolons inside sentences, and no sentence that argues for the work's merit.
And a stage that detects unfitness persists what it saw, not only its verdict,
which is rule 8 and was added here during gate C1.

Two of those are currently violated by the corpus rather than by the practice,
and the ledger says so. Eight rows cite measurements whose primary artifacts are
not in this tree, so those numbers do not trace to an artifact here. No gate has
been sealed, so nothing here was registered before its evidence.

## Programme

Each phase retires one degree of freedom from the vacuity proposition. A phase
that retires none is not a phase.

| | Objective | Retires |
|---|---|---|
| I | A causal observer-limited reversal under a registered budget manipulation | the budget becomes manipulated rather than fitted |
| II | Representation recovered from independent tasks or learned encoders | the representation stops being researcher-coded, which is what `xbse` refused |
| III | Trajectories from process measures | the search policy becomes measured rather than assumed |
| IV | A registered boundary with a prediction a smooth family misses | stratification becomes an empirical claim or is dropped |
| V | A collapse of normalized observables across substrates | the word fundamental acquires a referent or is withdrawn |
| VI | A safety-relevant boundary predicted and prevented without training on the failure | the account becomes an instrument |

`GC-34` is Phase I and is the only row in the ledger that can currently fail. It
predicts that under a registered budget manipulation with metric and ideal held
fixed, reversals occur only for pairs trading a resolved direction against an
unresolved one. A noise account does not make that prediction. Sealing it is the
next act of this programme.

## What would refute this

Stated as conditions on a record rather than as judgments, so that a reader who
did not run the experiment can check them.

1. A registered budget manipulation leaves the distinction threshold and the
   predicted reversal classes unchanged.
2. A representation probe registered in advance shows no change where the account
   attributes a flip to representation.
3. Choices reverse among alternatives whose differences lie in a subspace shown
   to be retained by a probe registered beforehand.
4. A scalar model with fewer effective degrees of freedom predicts the same
   held-out reversals and process measures at least as well.
5. Registered regime boundaries fail to align across independent observables.
6. Cross-domain metric transfer disappears when researcher-coded encodings are
   replaced by independently measured ones.
7. No reusable relation between representational limit and behavioral transition
   appears across substrates.

Condition 6 is the one this corpus currently fails, because its encodings are
researcher-coded. Phase II exists to answer it.

## Part of the Geometric Series

This repository is the cognition arm. The mathematical toolkit is *Geometric
Methods in Computational Modeling* and the parent theory is *Geometric
Reasoning, From Search to Manifolds*. The evaluation layer is GET and the
observation layer is Observation Theory. The governance discipline is the
inquiry arm of Philosophy Engineering, whose claim-ledger specification the
ledger here follows.

## License

Two licenses, split by what the file is.

| What | License | File |
|---|---|---|
| Prose and figures: chapters, appendices, front and back matter, figures, ledgers, protocol and standards documents, README | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) | `LICENSE-TEXT` |
| Source code: build scripts, tools, experiment harnesses, site generators | [MIT](https://opensource.org/licenses/MIT) | `LICENSE` |

Manuscripts under `paper/` or `papers/` that are submitted, accepted or
published elsewhere are outside both files. They carry the rights their
publisher agreement assigns.

CC BY asks you to attribute and to indicate whether you changed anything. Both
halves of that matter here. Every claim in this series carries a status label,
such as `[proved]`, `[posited]` or `[open]`, graded against a claim ledger, and
an adapted version presented as the original misstates the evidence behind it.
Attribution that names the author, the volume and this repository, and that
says whether the text was changed, is enough.
