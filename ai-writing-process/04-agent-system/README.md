# Agent System

Three agents, 14 skills, and an orchestration layer that turns "write me a chapter" into an 8-step pipeline with research extraction, multi-agent batching, handoff protocols, and automated quality audits. This section covers how the agents interact, how skills are built, and why separation of concerns matters more than agent count.

## Contents

- **[Agent Architecture](agent-architecture.md)** -- Why separate agents exist: the writer creates, the reviewer critiques, the prompt writer researches. Covers the agent vs. skill distinction, section batching rules (max 4 per agent), the handoff protocol, and honest failure modes. Includes a Mermaid sequence diagram of the full interaction pattern.

- **[The Chapter Writer Skill](chapter-writer-skill.md)** -- The central orchestration: 8 steps from research prompt generation through final synthesis. Pre-flight checks with skip logic, the writing deep dive (research snapshot, citation formatting, argument support), the reviewing deep dive (unused research detection, cross-section pattern detection), step-by-step vs. auto mode, and what the output actually looks like.

- **[Quality Skills](quality-skills.md)** -- Six automated analysis skills that audit every chapter: voice scoring (25% weight), citation density (20%), research coverage (20%), link structure (15%), opening variety (10%), and term analysis (10%). How the weighted health score works, what the voice scoring rubric measures, and what automated quality cannot do.

- **[The Research Reader Skill](research-reader-skill.md)** -- Nine extraction tools that turn raw Perplexity output into writer-ready content. The research snapshot (start here always), citation formatting with pre-built footnote keys, credibility and confidence scoring for stats and quotes, and separate workflows for how the writer and reviewer agents use the same tools differently.

- **[Building Custom Skills](building-custom-skills.md)** -- How to design and build your own Claude Code skills: the 3-layer anatomy (SKILL.md, scripts, references), 4 design principles (concise context, appropriate freedom, progressive disclosure, scripts for repeatability), and the 6-step creation process. Includes a worked example of building the voice check skill.

## Key Takeaways

- Self-review by the same agent that wrote the content produces blind spots. Distinct writer and reviewer agents with different system prompts, tools, and success criteria catch problems neither would find alone.
- Max 4 sections per agent instance. Quality degrades past that threshold -- voice drifts, examples repeat, research references get muddled.
- Skills are procedures (steps, tools, checklists). Agents are personas (voice, priorities, judgment). Skills can invoke agents. The distinction matters for system design.

---

[Previous: Prompt Engineering](../03-prompt-engineering/README.md) | [Next: Research Pipeline](../05-research-pipeline/README.md) | [Back to AI Writing Process](../README.md)
