#!/usr/bin/env bash
# Push the Chapter 1 lecture deck into noki/ioai-2026 under crash-course/.
# Run this from your terminal — uses your local gh/ssh auth.

set -euo pipefail

# ── Edit these two lines if the repo URL or folder name is different ───────
REPO_URL="git@github.com:noki/ioai-2026.git"     # or https://github.com/noki/ioai-2026.git
FOLDER="crash-course"
# ────────────────────────────────────────────────────────────────────────────

DECK_SRC="/Users/farhad.vadiee/Documents/github/books/ml-by-design/ML_by_Design_Ch01_Framing.pptx"
WORKDIR="$(mktemp -d)"

echo "Cloning into $WORKDIR …"
git clone "$REPO_URL" "$WORKDIR/repo"
cd "$WORKDIR/repo"

mkdir -p "$FOLDER"
cp "$DECK_SRC" "$FOLDER/"

# Optional README so the folder isn't bare
if [ ! -f "$FOLDER/README.md" ]; then
  cat > "$FOLDER/README.md" <<'EOF'
# Crash Course

Lecture slides adapted from *Machine Learning by Design* (Sam Urmian).

## Chapter 1 — Framing Learning Problems
- `ML_by_Design_Ch01_Framing.pptx` — 24-slide deck for a 50-minute introductory session.
EOF
fi

git add "$FOLDER"
git commit -m "crash-course: add Chapter 1 (Framing Learning Problems) slides"
git push origin HEAD

echo "Done. Pushed to $REPO_URL on branch $(git rev-parse --abbrev-ref HEAD)."
