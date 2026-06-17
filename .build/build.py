#!/usr/bin/env python3
"""
Build script for converting book markdown chapters to HTML.

Uses Python-Markdown with math preservation for KaTeX client-side rendering.
No Pandoc dependency required.

Renders into the unified Geometric Series "modern brand-nav" look: shared
CSS (../assets/css/style.css + ../book/book.css), a #series-nav-list populated
by ../assets/js/series.js from books.json (single source of truth for the
series nav and volume count), and a per-book footer.

Usage:
    python .build/build.py                    # build all chapters
    python .build/build.py chapters/ch01.md   # build specific file
    python .build/build.py --output-dir out   # custom output directory
"""

import argparse
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    import markdown
except ImportError:
    print("ERROR: 'markdown' package not installed. Run: pip install markdown")
    sys.exit(1)


# ---------------------------------------------------------------------------
# Configuration — canonical per-book metadata for the 8 markdown-built volumes.
# Series nav + volume count come from docs/books.json via series.js, so this
# only needs THIS book's own identity.
# ---------------------------------------------------------------------------

SERIES_TAGLINE = "The geometry was always real. The scalars were always insufficient."

BOOK_CONFIGS = {
    "geometric-reasoning": {
        "number": 2, "title": "Geometric Reasoning",
        "subtitle": "From Search to Manifolds",
        "source_dirs": ["chapters"], "glob": "*.md",
    },
    "geometric-economics": {
        "number": 4, "title": "Geometric Economics",
        "subtitle": "Decision Manifolds, Equilibria, and the Geometry of Markets",
        "source_dirs": ["chapters"], "glob": "*.md",
    },
    "geometric-law": {
        "number": 5, "title": "Geometric Law",
        "subtitle": "Symmetry, Invariance, and the Structure of Legal Reasoning",
        "source_dirs": ["chapters"], "glob": "*.md",
    },
    "geometric-cognition": {
        "number": 6, "title": "Geometric Cognition",
        "subtitle": "The Mathematical Structure of Human and Artificial Thought",
        "source_dirs": ["chapters"], "glob": "*.md",
    },
    "geometric-communication": {
        "number": 7, "title": "Geometric Communication",
        "subtitle": "Language, Signal, and the Topology of Meaning",
        "source_dirs": ["manuscript/part_i", "manuscript/part_ii",
                        "manuscript/part_iii", "manuscript/part_iv",
                        "manuscript/part_v", "manuscript/appendices"],
        "glob": "*.md",
    },
    "geometric-medicine": {
        "number": 8, "title": "Geometric Medicine",
        "subtitle": "Clinical Reasoning, Triage, and the Ethics of Allocation",
        "source_dirs": ["manuscript/part_i", "manuscript/part_ii",
                        "manuscript/part_iii", "manuscript/part_iv",
                        "manuscript/appendices"],
        "glob": "*.md",
    },
    "geometric-education": {
        "number": 9, "title": "Geometric Education",
        "subtitle": "Learning, Assessment, and the Topology of Understanding",
        "source_dirs": ["manuscript/part_i", "manuscript/part_ii",
                        "manuscript/part_iii", "manuscript/appendices"],
        "glob": "*.md",
    },
    "geometric-politics": {
        "number": 10, "title": "Geometric Politics",
        "subtitle": "Representation, Polarization, and the Topology of Democratic Choice",
        "source_dirs": ["manuscript/part_i", "manuscript/part_ii",
                        "manuscript/part_iii", "manuscript/appendices"],
        "glob": "*.md",
    },
}


def detect_repo_name(repo_root: Path) -> str:
    name = repo_root.name.lower()
    if name in BOOK_CONFIGS:
        return name
    for key in BOOK_CONFIGS:
        if key in name:
            return key
    return name


def protect_math(text: str) -> tuple[str, dict[str, str]]:
    """Replace LaTeX math blocks with placeholders before Markdown processing."""
    placeholders = {}
    counter = 0

    def _replace(match: re.Match) -> str:
        nonlocal counter
        key = f"\x00MATH{counter}\x00"
        placeholders[key] = match.group(0)
        counter += 1
        return key

    text = re.sub(r'\$\$(.+?)\$\$', _replace, text, flags=re.DOTALL)
    text = re.sub(r'(?<!\$)\$(?!\$)(?!\s)(.+?)(?<!\s)\$(?!\$)', _replace, text)
    text = re.sub(r'\\\[(.+?)\\\]', _replace, text, flags=re.DOTALL)
    text = re.sub(r'\\\((.+?)\\\)', _replace, text)
    return text, placeholders


def restore_math(html: str, placeholders: dict[str, str]) -> str:
    for key, value in placeholders.items():
        html = html.replace(key, value)
    return html


def extract_title(md_text: str) -> str:
    match = re.search(r'^#\s+(.+)$', md_text, re.MULTILINE)
    if match:
        title = match.group(1).strip()
        title = re.sub(r'\*+(.+?)\*+', r'\1', title)
        return title
    return "Untitled"


def _make_converter() -> "markdown.Markdown":
    return markdown.Markdown(
        extensions=["fenced_code", "tables", "toc", "smarty", "attr_list"],
        extension_configs={
            "toc": {"permalink": False, "toc_depth": "2-4"},
            "smarty": {"smart_quotes": True, "smart_dashes": True},
        },
    )


def _fill(template: str, *, title: str, body: str, config: dict, build_date: str) -> str:
    html = template.replace("{{content}}", body)
    html = html.replace("{{title}}", title)
    html = html.replace("{{book_title}}", config["title"])
    html = html.replace("{{book_subtitle}}", config["subtitle"])
    html = html.replace("{{book_slug}}", config["slug"])
    html = html.replace("{{footer_note}}", config.get("footer_note", SERIES_TAGLINE))
    html = html.replace("{{build_date}}", build_date)
    return html


def convert_md_to_html(md_path: Path, template: str, config: dict, build_date: str) -> str:
    md_text = md_path.read_text(encoding="utf-8")
    title = extract_title(md_text)
    protected_text, placeholders = protect_math(md_text)
    html_body = _make_converter().convert(protected_text)
    html_body = restore_math(html_body, placeholders)
    return _fill(template, title=title, body=html_body, config=config, build_date=build_date)


def find_source_files(repo_root: Path, config: dict) -> list[Path]:
    files = []
    for src_dir in config["source_dirs"]:
        search_dir = repo_root / src_dir
        if search_dir.exists():
            for f in sorted(search_dir.glob(config["glob"])):
                if f.is_file() and f.suffix == ".md":
                    files.append(f)
    return files


def generate_index(chapters: list[tuple[str, str, str]], template: str,
                   config: dict, build_date: str) -> str:
    """Generate index.html: a modern hero + chapter list (styled by shared CSS)."""
    items = [f'    <li><a href="{html_filename}">{title}</a></li>'
             for _, title, html_filename in chapters]
    body = (
        f'<header class="book-hero">\n'
        f'  <p class="book-number">Book {config["number"]} of the Geometric Series</p>\n'
        f'  <h1>{config["title"]}</h1>\n'
        f'  <p class="book-subtitle">{config["subtitle"]}</p>\n'
        f'  <p class="book-byline">A volume in the <em>Geometric Series</em> by Andrew H. Bond.</p>\n'
        f'</header>\n'
        f'<h2>Contents</h2>\n<ol class="toc-chapters">\n'
        + "\n".join(items) + "\n</ol>"
    )
    return _fill(template, title="Contents", body=body, config=config, build_date=build_date)


def main():
    parser = argparse.ArgumentParser(description="Build book HTML from Markdown")
    parser.add_argument("files", nargs="*", help="Specific .md files (default: all)")
    parser.add_argument("--output-dir", "-o", default="output", help="Output directory")
    parser.add_argument("--repo-root", default=None, help="Repo root (default: cwd)")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve() if args.repo_root else Path.cwd()
    repo_name = detect_repo_name(repo_root)
    config = BOOK_CONFIGS.get(repo_name)
    if config is None:
        print(f"ERROR: Unknown repo '{repo_name}'. Add it to BOOK_CONFIGS.")
        sys.exit(1)
    config = {**config, "slug": repo_name, "footer_note": SERIES_TAGLINE}

    build_date = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    template_path = repo_root / ".build" / "template.html"
    if not template_path.exists():
        print(f"ERROR: Template not found at {template_path}")
        sys.exit(1)
    template = template_path.read_text(encoding="utf-8")

    output_dir = Path(args.output_dir)
    if not output_dir.is_absolute():
        output_dir = repo_root / output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    source_files = ([Path(f).resolve() for f in args.files] if args.files
                    else find_source_files(repo_root, config))
    if not source_files:
        print("No source Markdown files found.")
        sys.exit(0)

    print(f"Building {config['title']} (Book {config['number']})")
    print(f"  Source files: {len(source_files)}\n  Output: {output_dir}\n")

    chapters = []
    for md_path in source_files:
        html_filename = f"{md_path.stem}.html"
        title = extract_title(md_path.read_text(encoding="utf-8"))
        print(f"  {md_path.name} -> {html_filename}  [{title}]")
        html = convert_md_to_html(md_path, template, config, build_date)
        (output_dir / html_filename).write_text(html, encoding="utf-8")
        chapters.append((md_path.name, title, html_filename))

    index_html = generate_index(chapters, template, config, build_date)
    (output_dir / "index.html").write_text(index_html, encoding="utf-8")
    print(f"\n  index.html  [Contents]")
    print(f"\nDone. {len(chapters)} chapters built -> {output_dir}")


if __name__ == "__main__":
    main()
