#!/usr/bin/env python3
"""
Build script for converting book markdown chapters to HTML.

Uses Python-Markdown with math preservation for KaTeX client-side rendering.
No Pandoc dependency required.

Usage:
    python .build/build.py                    # build all chapters
    python .build/build.py chapters/ch01.md   # build specific file
    python .build/build.py --output-dir out   # custom output directory
"""

import argparse
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    import markdown
    from markdown.extensions import fenced_code, tables, toc
except ImportError:
    print("ERROR: 'markdown' package not installed. Run: pip install markdown")
    sys.exit(1)


# ---------------------------------------------------------------------------
# Configuration — override per-repo via environment or edit here
# ---------------------------------------------------------------------------

BOOK_CONFIGS = {
    "geometric-reasoning": {
        "title": "Geometric Reasoning",
        "source_dirs": ["chapters"],
        "glob": "*.md",
    },
    "geometric-economics": {
        "title": "Geometric Economics",
        "source_dirs": ["chapters"],
        "glob": "*.md",
    },
    "geometric-law": {
        "title": "Geometric Law",
        "source_dirs": ["chapters"],
        "glob": "*.md",
    },
    "geometric-cognition": {
        "title": "Geometric Cognition",
        "source_dirs": ["chapters"],
        "glob": "*.md",
    },
    "geometric-communication": {
        "title": "Geometric Communication",
        "source_dirs": ["manuscript/part_i", "manuscript/part_ii",
                        "manuscript/part_iii", "manuscript/part_iv",
                        "manuscript/part_v", "manuscript/appendices"],
        "glob": "*.md",
    },
    "geometric-medicine": {
        "title": "Geometric Medicine",
        "source_dirs": ["manuscript/part_i", "manuscript/part_ii",
                        "manuscript/part_iii", "manuscript/part_iv",
                        "manuscript/appendices"],
        "glob": "*.md",
    },
    "geometric-education": {
        "title": "Geometric Education",
        "source_dirs": ["manuscript/part_i", "manuscript/part_ii",
                        "manuscript/part_iii", "manuscript/appendices"],
        "glob": "*.md",
    },
    "geometric-politics": {
        "title": "Geometric Politics",
        "source_dirs": ["manuscript/part_i", "manuscript/part_ii",
                        "manuscript/part_iii", "manuscript/appendices"],
        "glob": "*.md",
    },
}


def detect_repo_name(repo_root: Path) -> str:
    """Detect which book repo we're in from the directory name."""
    name = repo_root.name.lower()
    if name in BOOK_CONFIGS:
        return name
    # Fallback: try matching
    for key in BOOK_CONFIGS:
        if key in name:
            return key
    return name


def protect_math(text: str) -> tuple[str, dict[str, str]]:
    """
    Replace LaTeX math blocks with placeholders before Markdown processing.

    This prevents the Markdown parser from mangling math expressions.
    KaTeX auto-render will process the math client-side.
    """
    placeholders = {}
    counter = 0

    def _replace(match: re.Match) -> str:
        nonlocal counter
        key = f"\x00MATH{counter}\x00"
        placeholders[key] = match.group(0)
        counter += 1
        return key

    # Display math: $$ ... $$ (possibly multiline)
    text = re.sub(r'\$\$(.+?)\$\$', _replace, text, flags=re.DOTALL)

    # Inline math: $ ... $ (single line, non-greedy)
    # Avoid matching currency like "$5" by requiring non-space after opening $
    text = re.sub(r'(?<!\$)\$(?!\$)(?!\s)(.+?)(?<!\s)\$(?!\$)', _replace, text)

    # \[ ... \] display math
    text = re.sub(r'\\\[(.+?)\\\]', _replace, text, flags=re.DOTALL)

    # \( ... \) inline math
    text = re.sub(r'\\\((.+?)\\\)', _replace, text)

    return text, placeholders


def restore_math(html: str, placeholders: dict[str, str]) -> str:
    """Restore math expressions from placeholders."""
    for key, value in placeholders.items():
        html = html.replace(key, value)
    return html


def extract_title(md_text: str) -> str:
    """Extract the title from the first H1 heading."""
    match = re.search(r'^#\s+(.+)$', md_text, re.MULTILINE)
    if match:
        # Remove markdown formatting from title
        title = match.group(1).strip()
        title = re.sub(r'\*+(.+?)\*+', r'\1', title)  # bold/italic
        return title
    return "Untitled"


def convert_md_to_html(
    md_path: Path,
    template: str,
    book_title: str,
    build_date: str,
) -> str:
    """Convert a single Markdown file to HTML using the template."""
    md_text = md_path.read_text(encoding="utf-8")

    # Extract title before any processing
    title = extract_title(md_text)

    # Protect math from Markdown parser
    protected_text, placeholders = protect_math(md_text)

    # Convert Markdown to HTML
    md_converter = markdown.Markdown(
        extensions=[
            "fenced_code",
            "tables",
            "toc",
            "smarty",
            "attr_list",
        ],
        extension_configs={
            "toc": {"permalink": True, "toc_depth": "2-4"},
            "smarty": {"smart_quotes": True, "smart_dashes": True},
        },
    )
    html_body = md_converter.convert(protected_text)

    # Restore math expressions
    html_body = restore_math(html_body, placeholders)

    # Fill template
    html = template.replace("{{content}}", html_body)
    html = html.replace("{{title}}", title)
    html = html.replace("{{book_title}}", book_title)
    html = html.replace("{{build_date}}", build_date)

    return html


def find_source_files(repo_root: Path, config: dict) -> list[Path]:
    """Find all Markdown source files for this book."""
    files = []
    for src_dir in config["source_dirs"]:
        search_dir = repo_root / src_dir
        if search_dir.exists():
            for f in sorted(search_dir.glob(config["glob"])):
                if f.is_file() and f.suffix == ".md":
                    files.append(f)
    return files


def generate_index(
    chapters: list[tuple[str, str, str]],
    template: str,
    book_title: str,
    build_date: str,
) -> str:
    """
    Generate an index.html listing all chapters.

    chapters: list of (filename, title, html_filename)
    """
    items = []
    for _, title, html_filename in chapters:
        items.append(f'  <li><a href="{html_filename}">{title}</a></li>')

    body = f"<h1>{book_title}</h1>\n"
    body += '<p>Part of the <em>Geometric Series</em> by A.H. Bowers.</p>\n'
    body += "<h2>Chapters</h2>\n<ol>\n"
    body += "\n".join(items)
    body += "\n</ol>"

    html = template.replace("{{content}}", body)
    html = html.replace("{{title}}", "Table of Contents")
    html = html.replace("{{book_title}}", book_title)
    html = html.replace("{{build_date}}", build_date)

    return html


def main():
    parser = argparse.ArgumentParser(description="Build book HTML from Markdown")
    parser.add_argument(
        "files",
        nargs="*",
        help="Specific .md files to convert (default: all chapters)",
    )
    parser.add_argument(
        "--output-dir", "-o",
        default="output",
        help="Output directory (default: output/)",
    )
    parser.add_argument(
        "--repo-root",
        default=None,
        help="Repository root (default: auto-detect from cwd)",
    )
    args = parser.parse_args()

    # Determine repo root
    if args.repo_root:
        repo_root = Path(args.repo_root).resolve()
    else:
        repo_root = Path.cwd()

    # Detect book config
    repo_name = detect_repo_name(repo_root)
    config = BOOK_CONFIGS.get(repo_name)
    if config is None:
        print(f"WARNING: Unknown repo '{repo_name}', using defaults")
        config = {
            "title": repo_name.replace("-", " ").title(),
            "source_dirs": ["chapters"],
            "glob": "*.md",
        }

    book_title = config["title"]
    build_date = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    # Load template
    template_path = repo_root / ".build" / "template.html"
    if not template_path.exists():
        print(f"ERROR: Template not found at {template_path}")
        sys.exit(1)
    template = template_path.read_text(encoding="utf-8")

    # Create output directory
    output_dir = Path(args.output_dir)
    if not output_dir.is_absolute():
        output_dir = repo_root / output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    # Collect source files
    if args.files:
        source_files = [Path(f).resolve() for f in args.files]
    else:
        source_files = find_source_files(repo_root, config)

    if not source_files:
        print("No source Markdown files found.")
        sys.exit(0)

    print(f"Building {book_title}")
    print(f"  Source files: {len(source_files)}")
    print(f"  Output: {output_dir}")
    print()

    # Convert each file
    chapters = []
    for md_path in source_files:
        basename = md_path.stem
        html_filename = f"{basename}.html"
        out_path = output_dir / html_filename

        title = extract_title(md_path.read_text(encoding="utf-8"))
        print(f"  {md_path.name} -> {html_filename}  [{title}]")

        html = convert_md_to_html(md_path, template, book_title, build_date)
        out_path.write_text(html, encoding="utf-8")

        chapters.append((md_path.name, title, html_filename))

    # Generate index
    index_html = generate_index(chapters, template, book_title, build_date)
    index_path = output_dir / "index.html"
    index_path.write_text(index_html, encoding="utf-8")
    print(f"\n  index.html  [Table of Contents]")

    print(f"\nDone. {len(chapters)} chapters built -> {output_dir}")


if __name__ == "__main__":
    main()
