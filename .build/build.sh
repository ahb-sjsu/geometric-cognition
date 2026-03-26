#!/usr/bin/env bash
# Build book HTML from Markdown source.
# Usage:
#   ./build.sh                  # build all chapters
#   ./build.sh -o docs/         # custom output directory
#   ./build.sh chapter01.md     # build specific file

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

# Ensure markdown package is available
if ! python3 -c "import markdown" 2>/dev/null; then
    echo "Installing Python markdown package..."
    pip install markdown --quiet
fi

python3 "$SCRIPT_DIR/build.py" --repo-root "$REPO_ROOT" "$@"
