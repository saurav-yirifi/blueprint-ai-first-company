# Research Pipeline

180+ Perplexity prompts, automated browser-driven search, synthesis scripts that extract stats and quotes with credibility scores, and a citation management system that kept 775 footnotes consistent across 81 sections. This section covers how research runs before writing starts -- and why that order matters.

## Contents

- **[Research Architecture](research-architecture.md)** -- The 4-phase pipeline: preparation (web research pre-search), execution (Perplexity automation), processing (synthesis extraction), and integration (writer and reviewer agents). Covers the folder structure that mirrors prompts to answers, two-phase prompt design, prompt types, and how research-first flipped the economics of evidence. Includes a Mermaid diagram of the full flow.

- **[Perplexity Automation](perplexity-automation.md)** -- Playwright-driven browser automation that submits prompts to Perplexity Pro, waits for responses, and saves them to the matching answers folder. Key details: context bleed prevention (delete thread every 4 prompts), 12-second delays to avoid rate limits, failure handling with skip-existing logic, and practical tips from running 180+ prompts.

- **[Citation Management](citation-management.md)** -- The citation format (named footnote keys with source URLs), the one-tag-per-source-URL rule, the audit and standardization scripts, citation density benchmarks (1 per 105 words achieved), internal research tracking blocks, and the fact verification protocol. Covers the 3-stage citation workflow from pre-staged through reviewer-caught.

- **[Synthesis and Extraction](synthesis-and-extraction.md)** -- How raw Perplexity output gets transformed into writer-ready material. Credibility scoring for statistics (HIGH/MEDIUM/LOW), confidence scoring for quotes, the synthesize-research skill, output format, and integration with the research reader's 9 extraction scripts. The gap between a 1,500-word research dump and the 3 specific pieces a writer actually needs.

## Key Takeaways

- Research before writing. Always. The pipeline made citation cheap, which made citation ubiquitous -- 775 citations weren't a goal, they were a side effect.
- Two-phase prompt design (pre-research web search, then informed prompts) produces dramatically sharper results than writing prompts cold.
- Not all research is equal. Credibility and confidence scoring at extraction time offloads source evaluation from the creative process.

---

[Previous: Agent System](../04-agent-system/README.md) | [Next: Obsidian Vault](../06-obsidian-vault/README.md) | [Back to AI Writing Process](../README.md)
