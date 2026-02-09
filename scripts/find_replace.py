#!/usr/bin/env python3
"""Find and replace across book files."""

import os
import sys

# ── Configure these ─────────────────────────────────────────────
SEARCH_DIR = os.path.join(os.path.dirname(__file__), "..", "book")
FILE_EXTENSIONS = [".md"]  # which file types to process
FIND = "---\n\n## References"
REPLACE = "## References"
# ────────────────────────────────────────────────────────────────


def find_matches(search_dir, extensions, find_text):
    """Return list of (filepath, count) tuples for files containing find_text."""
    matches = []
    for root, _, files in os.walk(search_dir):
        for fname in sorted(files):
            if not any(fname.endswith(ext) for ext in extensions):
                continue
            fpath = os.path.join(root, fname)
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()
            count = content.count(find_text)
            if count > 0:
                matches.append((fpath, count))
    return matches


def main():
    dry_run = "--dry-run" in sys.argv or "-n" in sys.argv

    search_dir = os.path.abspath(SEARCH_DIR)
    print(f"Directory:  {search_dir}")
    print(f"Extensions: {FILE_EXTENSIONS}")
    print(f"Find:       {FIND!r}")
    print(f"Replace:    {REPLACE!r}")
    print(f"Mode:       {'DRY RUN' if dry_run else 'LIVE'}")
    print()

    matches = find_matches(search_dir, FILE_EXTENSIONS, FIND)

    if not matches:
        print("No matches found.")
        return

    total = 0
    for fpath, count in matches:
        rel = os.path.relpath(fpath, search_dir)
        print(f"  {rel}  ({count} match{'es' if count > 1 else ''})")
        total += count

        if not dry_run:
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()
            content = content.replace(FIND, REPLACE)
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)

    print()
    print(f"Total: {total} replacement{'s' if total > 1 else ''} in {len(matches)} file{'s' if len(matches) > 1 else ''}")
    if dry_run:
        print("(No files changed — run without --dry-run to apply)")


if __name__ == "__main__":
    main()
