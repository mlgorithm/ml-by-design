#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
BOOK_PDF="$ROOT_DIR/book.pdf"
OUT_DIR="${1:-/tmp/ai-book-review-packets}"

if ! command -v pdfjam >/dev/null 2>&1; then
  echo "pdfjam is required to build review packets." >&2
  exit 1
fi

if [ ! -f "$BOOK_PDF" ]; then
  echo "Missing compiled PDF: $BOOK_PDF" >&2
  exit 1
fi

mkdir -p "$OUT_DIR"

build_packet() {
  local name="$1"
  local pages="$2"
  local out="$OUT_DIR/$name"
  pdfjam "$BOOK_PDF" "$pages" --outfile "$out" >/dev/null
  echo "$out"
}

commit="$(git -C "$ROOT_DIR" rev-parse --short HEAD 2>/dev/null || echo unknown)"

ml_packet="$(build_packet "ml-expert-review.pdf" "15-58,147-158")"
systems_packet="$(build_packet "systems-review.pdf" "120-183")"
instructor_packet="$(build_packet "instructor-review.pdf" "15-42,120-133,169-183")"

cat >"$OUT_DIR/manifest.txt" <<EOF
Review packet source commit: $commit
Source PDF: $BOOK_PDF

ml-expert-review.pdf
  Pages: 15-58,147-158
  Chapters: 1, 2, 3, 10

systems-review.pdf
  Pages: 120-183
  Chapters: 8, 9, 10, 11, 12

instructor-review.pdf
  Pages: 15-42,120-133,169-183
  Chapters: 1, 2, 8, 12
EOF

echo "Built:"
echo "  $ml_packet"
echo "  $systems_packet"
echo "  $instructor_packet"
echo "  $OUT_DIR/manifest.txt"
