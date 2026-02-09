# Obsidian Vault

The structural backbone of the manuscript -- a file-per-section architecture with YAML frontmatter, wiki-linking, concept notes as hubs, and Dataview queries that turn a folder of Markdown files into a live project management system. This section covers how the vault was organized, why each structural decision was made, and how 1,199 internal links kept 81 sections coherent.

## Contents

- **[Vault Architecture](vault-architecture.md)** -- The Part / Chapter / Section hierarchy, why file-per-section is the single most important structural decision for AI-assisted writing, supporting content folders (concepts, MOCs, research, planning), and draft management with full copies instead of git branches. How the architecture enables parallel agent writing, surgical reviews, and granular status tracking.

- **[Templates and Frontmatter](templates-and-frontmatter.md)** -- Chapter intro frontmatter (aliases, key concepts, related chapters), section frontmatter (research sources, word targets, status), the 5-stage status workflow (outline through done), and Templater templates that auto-fill metadata. Why frontmatter is a system contract between the human author, AI agents, and automation scripts -- not documentation.

- **[Linking and Navigation](linking-and-navigation.md)** -- Three linking layers (section links, concept links, MOC links), concept notes as hubs that prevent the same idea from being defined inconsistently across chapters, bidirectional linking as a consistency check, and the vault health transformation: 0% to 68% section-to-concept coverage, 630 to 1,199 total links. Graph view as an editorial tool for finding structural gaps.

- **[Dataview and Dashboards](dataview-and-dashboards.md)** -- How Dataview queries treat the vault as a database. The Dashboard as nerve center (progress overview, per-part breakdowns, word count targets, graph health, currently drafting). Queries worth stealing: sections progress by chapter, sections missing concept links. The 6-plugin stack for tracking and productivity, and why Obsidian + Dataview + standardized frontmatter eliminates manual progress tracking.

## Key Takeaways

- File-per-section architecture is non-negotiable for AI-assisted writing. Each 1,200-word section becomes a self-contained unit of work that an agent can research, write, and review without losing focus.
- Concept notes are the glue that holds a multi-chapter argument together. Without them, the same concept appears in 4 chapters with slightly different definitions.
- Frontmatter consistency is the foundation everything else builds on. One typo in a status field makes a section vanish from every dashboard query.

---

[Previous: Research Pipeline](../05-research-pipeline/README.md) | [Next: Automation](../07-automation/README.md) | [Back to AI Writing Process](../README.md)
