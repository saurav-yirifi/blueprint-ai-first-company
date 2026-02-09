# Automation

17 Python scripts that handle everything manual operations can't at book scale -- word counting that filters out YAML and Mermaid syntax, PDF generation with two output modes, writing velocity tracking with GitHub-style contribution graphs, and vault validation that catches broken links before they ship. This section maps the full ecosystem and explains when to use each script.

## Contents

- **[Script Ecosystem](script-ecosystem.md)** -- The complete inventory: 4 manuscript management scripts (word count, book status, daily stats, search), 4 content validation scripts (vault validation, citation standardization, citation format audit, citation format fix), 4 research enrichment scripts (research frontmatter, research enrichment, section frontmatter enrichment, blog downloads), and 5 infrastructure scripts (PDF generation, graph health, terminal UI, backup commits, GitHub conversion). Design principles: vault-relative paths, dry-run modes, rich output with fallback, JSON output for tooling.

- **[PDF Generation](pdf-generation.md)** -- Two modes: internal (shows research source blocks) and reader (clean publication output). The multi-stage pipeline: file discovery, frontmatter stripping, link resolution, Mermaid rendering with persistent caching, markdown-to-HTML, HTML-to-PDF via WeasyPrint. Why WeasyPrint over Pandoc for book-specific layout control. Cache system that takes a full book PDF from 10+ minutes to under 60 seconds.

- **[Writing Analytics](writing-analytics.md)** -- Three scripts at different granularities: word count (the most-run script, excluding YAML, Mermaid, references, and comments from counts), book status dashboard (color-coded progress with per-chapter bars), and daily stats (velocity tracking, contribution graphs, writing streaks, git hook integration). Combined with Obsidian plugins for the real-time section-level view.

- **[Vault Health](vault-health.md)** -- Three tools: `validate_vault.py` (broken links, missing frontmatter, orphan files, invalid tags), `graph_health_report.py` (connectivity analysis, health score 0-100, orphan detection), and `enrich_section_frontmatter.py` (batch operations that added 555 new links in a single run, moving section-to-concept coverage from 0% to 68%). Maintenance cadence: validate after changes, analyze weekly, enrich after structural changes.

## Key Takeaways

- At 81,000 words across 81 sections, manual operations stop scaling somewhere around chapter 4. Scripts eliminate the cognitive overhead that eats into writing time.
- The word count script's filtering matters: raw file counts overstate by 15-20% when each file has frontmatter, Mermaid diagrams, and reference sections.
- Always preview before applying. The enrichment script ran once and added 555 links -- powerful, but run without `--dry-run` first and you'll add misleading links to sections where concepts are mentioned in passing.

---

[Previous: Obsidian Vault](../06-obsidian-vault/README.md) | [Next: Book Intelligence App](../08-book-intelligence-app/README.md) | [Back to AI Writing Process](../README.md)
