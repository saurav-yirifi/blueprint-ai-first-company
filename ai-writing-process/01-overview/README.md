# Overview

The full picture -- how the writing system works end to end, what it produced, and the architecture decisions behind every component. Start here if you want to understand the pipeline before diving into any one piece.

## Contents

- **[End-to-End Flow](end-to-end-flow.md)** -- The complete 8-phase pipeline from encoding your voice into reference files to generating a publication-ready PDF. Includes time estimates per phase and a Mermaid diagram showing how all components connect.

- **[Results and Metrics](results-and-metrics.md)** -- The numbers: 81,122 words, 775 citations, 14 skills, 3 complete drafts. Breaks down what the system produced across manuscript metrics, quality pipeline results, editorial review outcomes, and vault health improvements.

- **[Architecture Decisions](architecture-decisions.md)** -- Eight battle-tested decisions that shaped the system: voice as system files, modular prompts, multi-agent batching, research-first writing, Obsidian as the writing environment, separate writer/reviewer agents, the book intelligence app, and 4-phase editorial review. Each one includes the problem it solved, the trade-off it accepted, and why it was worth it.

## Key Takeaways

- The system took roughly 200-250 hours of human time for a 12-chapter, 81,000-word book. AI handled the volume; the human handled the judgment.
- Three complete drafts -- each one improved the system as much as the manuscript. Draft 1 was tuition. Draft 3 was the payoff.
- Every architecture shortcut tried early (skipping voice files, monolithic prompts, write-then-research) cost more time to fix than doing it right from the start.

---

[Next: Author Voice](../02-author-voice/README.md) | [Back to AI Writing Process](../README.md)
