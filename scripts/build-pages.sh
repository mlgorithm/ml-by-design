#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEST_DIR="${1:-$ROOT_DIR/_site}"

rm -rf "$DEST_DIR"
mkdir -p "$DEST_DIR"

cp -R "$ROOT_DIR/pages/." "$DEST_DIR/"

if [[ -f "$ROOT_DIR/ml-by-design.pdf" ]]; then
  cp "$ROOT_DIR/ml-by-design.pdf" "$DEST_DIR/ml-by-design.pdf"
elif [[ -f "$ROOT_DIR/book.pdf" ]]; then
  cp "$ROOT_DIR/book.pdf" "$DEST_DIR/ml-by-design.pdf"
elif [[ -f "$ROOT_DIR/build/book.pdf" ]]; then
  cp "$ROOT_DIR/build/book.pdf" "$DEST_DIR/ml-by-design.pdf"
else
  echo "No compiled book PDF found in repository root or build/." >&2
  exit 1
fi

if [[ -f "$ROOT_DIR/cover-preview.png" ]]; then
  cp "$ROOT_DIR/cover-preview.png" "$DEST_DIR/cover-preview.png"
fi

cp "$ROOT_DIR/CITATION.cff" "$DEST_DIR/CITATION.cff"
cp "$ROOT_DIR/LICENSE" "$DEST_DIR/LICENSE"

touch "$DEST_DIR/.nojekyll"
