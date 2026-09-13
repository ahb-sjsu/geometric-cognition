# -*- coding: utf-8 -*-
"""Count the ledger's classes and check the identifier sequence is gap-free.

The accounting block in LEDGER.md is produced by this script rather than typed.
A count that is typed drifts from the table the first time a row is added, and
the first draft of that block was wrong by four.

Usage: python claims/count_classes.py
"""
import collections
import io
import os
import re
import sys

LEDGER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "LEDGER.md")


def main():
    rows = [l for l in io.open(LEDGER, encoding="utf-8").read().split("\n")
            if l.startswith("| GC-")]
    counts = collections.Counter()
    ids = []
    unparsed = []
    for r in rows:
        cells = [c.strip() for c in r.strip().strip("|").split("|")]
        ids.append(cells[0])
        m = re.search(r"`\[([a-z]+)\]`", cells[2])
        if m:
            counts[m.group(1)] += 1
        else:
            unparsed.append(cells[0])

    nums = sorted({int(re.match(r"GC-(\d+)", i).group(1)) for i in ids})
    gaps = [n for n in range(nums[0], nums[-1] + 1) if n not in nums]
    split = sorted({i.split("-")[1] for i in ids if i.endswith(("-S", "-I"))},
                   key=int)

    print(f"rows {len(rows)} over identifiers GC-{nums[0]} to GC-{nums[-1]}")
    for k, v in sorted(counts.items(), key=lambda kv: -kv[1]):
        print(f"  {k:14s} {v}")
    print(f"  {'TOTAL':14s} {sum(counts.values())}")
    print(f"gaps in the identifier sequence: {gaps or 'none'}")
    print(f"identifiers split into -S and -I: {', '.join(split) or 'none'}")
    if unparsed:
        print(f"rows whose class did not parse: {unparsed}")
    # P2 wants a gap-free sequence, and an unparsed class is a row with no
    # disposition, which is the same defect in a different place.
    return 1 if (gaps or unparsed) else 0


if __name__ == "__main__":
    sys.exit(main())
