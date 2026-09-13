# Protocol

The registration discipline of `ahb-sjsu/observation-theory-campaigns`,
`ahb-sjsu/geometric-observation` and `ahb-sjsu/geometric-evaluation-theory`
applies unchanged. Restated here so that this repository does not depend on a
reader knowing where to look.

1. Seal before run. A gate's registration, meaning its hypothesis, world,
   statistic, bars, exclusions and null, is committed and its hash recorded
   before any data is opened. The registration file is
   `experiments/<gate>/PREREG-<gate>.md` and its hash goes into `CAMPAIGN.md`
   beside the gate.
2. Event presence first. Every registration cites a committed probe showing that
   the events the gate will count are present in every cell. A gate that could
   pass on empty cells is not sealed.
3. Misses at full prominence. A miss is recorded in `claims/LEDGER.md`, in
   `CAMPAIGN.md` and in the paper at the same size as a pass. A rerun after a
   miss is a new registration that names the miss.
4. Numbers trace to artifacts. Every number names its file and commit. A number
   without a record is removed.
5. Compute where it belongs. Nothing runs on the laptop. Experiments run on
   Atlas under the standing thermal and GPU rules, or on NRP through the burst
   flow, or against the managed inference gateway where that is the instrument.
6. Owner submits. The repository builds submission-ready files. The owner
   uploads, signs and publishes.
7. Prose. No em dashes, colons, or semicolons in sentences. No sentence that
   argues for the work's merit. Every caveat sits beside the result it bounds.
8. **A stage that detects unfitness persists what it saw, not only its verdict.**
   Self-tests, probes, sweeps and any gate that can void a run record the raw
   responses, the parse outcomes, and the reason each item terminated, beside the
   statistic. A miss whose cause cannot be read from its own record is a miss
   that has to be run again to be understood, and the second run is not the one
   that failed.

## Where rule 8 came from

It was added on 2026-09-13 during gate C1, after three diagnostics in one
session each returned a verdict that could not be diagnosed from the file it
wrote.

The first recorded a calibration `r2` of 0.0946 and did not keep the reports, so
establishing that the evaluator was following no distance function at all needed
a second run of the same block. The second recorded choice rates and did not keep
the letters. The third reported a parse failure on 80 items of 80 and did not
record `finish_reason`, which was the one field that would have shown
immediately that an 8-token budget had truncated a reasoning model before it
wrote an answer, rather than that the model could not answer. That third case is
the sharpest, because the missing field turned a defect in the harness into what
looked like a property of the model.

Each was repaired in the script where it appeared. Repairing three instances and
not the rule is the orphan correction that `PE-BRW-1.0` names, and the ledger
arm's whole argument is that a correction applied where it was found and nowhere
else is invisible to the next person. So the rule is written in the canonical
protocol of `geometric-evaluation-theory` and restated here, rather than left as
three patched files.

## The rate-limit rule

A registration is reread cold, in a session other than the one that drafted it,
before it is sealed. The reread and anything it changed are recorded inside the
registration. In the sibling programme's record this rule caught a falsification
condition that could not fire, so a draft that has not been reread is a draft.

## Discovery records

The two record classes defined for the programme in
`observation-theory-campaigns/standards/DPE-RECORDS.md` apply here.
`[witness]` is a row whose content is a reduced counterexample together with the
component that absorbed it. `[revised]` is a row recording a commitment changed
in response to a named witness. A verdict of FAIL or INDETERMINATE is not
complete until its witness row is written, or until the record says what stopped
the reduction.
