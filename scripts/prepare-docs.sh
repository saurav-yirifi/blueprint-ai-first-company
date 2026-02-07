#!/bin/bash
# Copy content into docs/ for local MkDocs preview.
# Run this before `mkdocs serve`.
set -e
cd "$(dirname "$0")/.."

cp -r book frameworks guides checklists examples workflows resources author ai-writing-process docs/
cp README.md docs/about.md

echo "docs/ prepared — run: mkdocs serve"
