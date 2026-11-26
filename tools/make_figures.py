"""Draw the book's figures as SVG and embed them in the chapters.

Run from the repository root:  python tools/make_figures.py [--no-embed] [module ...]
Runs every `fig_*` function of every module `tools/figs_*.py` (or only the modules named),
writes figures/*.svg, and inserts each figure in its chapter. See `tools/figkit.py` for the
conventions and the rule every figure follows.
"""

import glob
import importlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import figkit  # noqa: E402

args = [a for a in sys.argv[1:] if not a.startswith("--")]
names = args or sorted(os.path.basename(p)[:-3] for p in glob.glob(os.path.join(HERE, "figs_*.py")))
for name in names:
    mod = importlib.import_module(name)
    for fn in sorted(n for n in dir(mod) if n.startswith("fig_")):
        getattr(mod, fn)()
if "--no-embed" not in sys.argv:
    figkit.embed()
print(len(figkit.FIGS), "figures written to", figkit.FIG)
