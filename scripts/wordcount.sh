#!/usr/bin/env bash
# Word count for the thesis body (excludes annexes and bibliography).
# Prefers system `texcount` if available; otherwise uses vendored tools/texcount.pl.
set -euo pipefail

cd "$(dirname "$0")/.."

if command -v texcount >/dev/null 2>&1; then
  TEXCOUNT=(texcount)
elif [[ -f tools/texcount.pl ]] && command -v perl >/dev/null 2>&1; then
  TEXCOUNT=(perl tools/texcount.pl)
else
  echo "error: no texcount available." >&2
  echo "either install it once via:" >&2
  echo "    sudo tlmgr install texcount" >&2
  echo "or restore the vendored copy at tools/texcount.pl from:" >&2
  echo "    https://mirror.ctan.org/support/texcount/texcount.pl" >&2
  exit 1
fi

chapters=(
  introduction
  background
  theoretical_framework
  methods
  design
  results
  discussion
  conclusion
)

printf "%-25s %10s\n" "Chapter" "Words"
printf "%-25s %10s\n" "-------------------------" "----------"

total=0
for ch in "${chapters[@]}"; do
  file="chapters/${ch}.tex"
  if [[ ! -f "$file" ]]; then
    echo "error: missing chapter file: $file" >&2
    exit 1
  fi
  count=$("${TEXCOUNT[@]}" -1 -sum -merge "$file")
  printf "%-25s %10s\n" "$ch" "$count"
  total=$((total + count))
done

printf "%-25s %10s\n" "-------------------------" "----------"
printf "%-25s %10s\n" "TOTAL (body)" "$total"
