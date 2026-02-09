#!/usr/bin/env python3
"""Fix Mermaid subgraph label overlap by converting <br/> subtitles to styled nodes.

Scans .md files for mermaid code blocks where subgraph labels use <br/> to add
a subtitle. This causes text overlap in rendered diagrams because Mermaid doesn't
allocate enough vertical space for multi-line subgraph labels.

The fix moves the subtitle into a dedicated node with a transparent style class.
"""

import argparse
import re
import sys
from pathlib import Path

BOOK_DIR = Path(__file__).resolve().parent.parent / "book"
SUBGRAPH_RE = re.compile(
    r'^(\s*)subgraph\s+(\w+)\["(.*?)<br/>\s*(.+?)"\]',
)
CLASSDEF_LINE = "    classDef subtitle fill:none,stroke:none,color:#fff,font-size:1.1em"


def find_mermaid_blocks(lines: list[str]) -> list[tuple[int, int]]:
    """Return (start, end) line indices for each ```mermaid ... ``` block."""
    blocks = []
    start = None
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped == "```mermaid":
            start = i
        elif start is not None and stripped == "```":
            blocks.append((start, i))
            start = None
    return blocks


def fix_block(lines: list[str], block_start: int, block_end: int) -> tuple[list[str], int]:
    """Fix subgraph labels within a single mermaid block. Returns (new_lines, fix_count)."""
    result = []
    fixes = 0
    has_classdef = False
    needs_classdef = False
    i = block_start

    while i <= block_end:
        line = lines[i]

        # Check if classDef subtitle already exists
        if "classDef subtitle" in line:
            has_classdef = True

        m = SUBGRAPH_RE.match(line)
        if m:
            indent = m.group(1)
            sg_id = m.group(2)
            title = m.group(3)
            subtitle = m.group(4)
            node_id = sg_id + "S"
            content_indent = indent + "    "

            # Rewrite subgraph line without <br/>subtitle
            result.append(f'{indent}subgraph {sg_id}["{title}"]\n')

            # Look ahead: if next non-blank line is `direction XX`, insert after it
            j = i + 1
            while j <= block_end and lines[j].strip() == "":
                result.append(lines[j])
                j += 1

            if j <= block_end and lines[j].strip().startswith("direction "):
                result.append(lines[j])
                j += 1

            # Insert subtitle node
            result.append(f'{content_indent}{node_id}["<i>{subtitle}</i>"]:::subtitle\n')
            needs_classdef = True
            fixes += 1
            i = j
            continue

        result.append(line)
        i += 1

    # Add classDef if needed and not already present
    if needs_classdef and not has_classdef:
        # Insert before the closing ``` (last line in result)
        closing = result.pop()
        # Add blank line before classDef if the previous line isn't blank
        if result and result[-1].strip() != "":
            pass  # style lines are usually right before, no blank line needed
        result.append(CLASSDEF_LINE + "\n")
        result.append(closing)

    return result, fixes


def process_file(filepath: Path, dry_run: bool = False) -> int:
    """Process a single file. Returns number of fixes applied."""
    with open(filepath) as f:
        lines = f.readlines()

    blocks = find_mermaid_blocks(lines)
    if not blocks:
        return 0

    # Check if any block has subgraph <br/> pattern
    has_pattern = False
    for start, end in blocks:
        for i in range(start, end + 1):
            if SUBGRAPH_RE.match(lines[i]):
                has_pattern = True
                break
        if has_pattern:
            break

    if not has_pattern:
        return 0

    # Process blocks in reverse order to preserve line indices
    total_fixes = 0
    new_lines = list(lines)

    for block_start, block_end in reversed(blocks):
        block_lines = new_lines[block_start : block_end + 1]
        # Check if this specific block needs fixing
        block_has_pattern = any(SUBGRAPH_RE.match(l) for l in block_lines)
        if not block_has_pattern:
            continue

        fixed, count = fix_block(new_lines, block_start, block_end)
        if count > 0:
            new_lines[block_start : block_end + 1] = fixed
            total_fixes += count

    if total_fixes > 0:
        rel = filepath.relative_to(BOOK_DIR.parent)
        if dry_run:
            print(f"  [DRY RUN] {rel}: {total_fixes} subgraph(s) to fix")
        else:
            with open(filepath, "w") as f:
                f.writelines(new_lines)
            print(f"  [FIXED] {rel}: {total_fixes} subgraph(s) fixed")

    return total_fixes


def main():
    parser = argparse.ArgumentParser(description="Fix Mermaid subgraph label overlap")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without writing")
    parser.add_argument("--path", type=str, default=str(BOOK_DIR), help="Directory to scan")
    args = parser.parse_args()

    scan_dir = Path(args.path)
    if not scan_dir.exists():
        print(f"Error: {scan_dir} does not exist")
        sys.exit(1)

    md_files = sorted(scan_dir.rglob("*.md"))
    print(f"Scanning {len(md_files)} .md files in {scan_dir}...")

    total_files = 0
    total_fixes = 0
    for f in md_files:
        fixes = process_file(f, dry_run=args.dry_run)
        if fixes > 0:
            total_files += 1
            total_fixes += fixes

    print(f"\n{'[DRY RUN] ' if args.dry_run else ''}Summary: {total_fixes} subgraph(s) in {total_files} file(s)")


if __name__ == "__main__":
    main()
