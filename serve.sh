#!/usr/bin/env bash
# Local MkDocs dev server — mirrors the CI copy step from deploy-pages.yml
set -euo pipefail
cd "$(dirname "$0")"

# Same copy step as .github/workflows/deploy-pages.yml L31-32
cp -r book frameworks guides checklists examples workflows resources author ai-writing-process docs/
cp README.md docs/about.md

# Kill any existing server on port 8000
lsof -ti :8000 | xargs kill -9 2>/dev/null || true
sleep 0.5

echo "Serving at http://127.0.0.1:8000/blueprint-ai-first-company/"
exec mkdocs serve "$@"
