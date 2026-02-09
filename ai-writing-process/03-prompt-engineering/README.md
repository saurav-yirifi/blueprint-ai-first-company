# Prompt Engineering

27 modular prompts across 5 categories -- the control surface for steering AI output without micromanaging every sentence. This section covers the architecture, the master system prompt that loads into every session, the individual writing and editing prompts, and how the system evolved across three drafts.

## Contents

- **[Prompt Architecture](prompt-architecture.md)** -- Why modular prompts beat monolithic instructions. The 27 prompts organized into 5 categories (writing, editing, review, linking, fix), how they compose at runtime with the master system prompt, and 3 workflow patterns for new chapters, edit passes, and final reviews. Includes a Mermaid diagram of the composition model.

- **[Anatomy of the Master System Prompt](master-system-prompt.md)** -- A 339-line prompt broken down section by section: core principle (Dense, Direct, Human), voice DNA, calibration spectrums, 19 craft techniques, phrase tables, audience internal monologues, density test, and the 9-point verification check. The single most important artifact in the writing system.

- **[Writing Prompts](writing-prompts.md)** -- The 8 prompts that create content: chapter opening, section body (the workhorse), framework, case study, analogy, executive summary, chapter closing, and technical deep dive. Detailed breakdown of the section prompt's 6 required elements and the framework prompt's signature style.

- **[Editing and Review Prompts](editing-and-review-prompts.md)** -- The 14 prompts that make content publishable. Three layers: 5 editing prompts (voice, audience, de-AI, balance, simplify), 4 review prompts (chapter complete, authenticity, audience fit, final quality), and 5 fix prompts (generic language, examples, action items, two-audience, tighten prose). The de-AI prompt is the single most valuable editing prompt in the system.

- **[Prompt Evolution](prompt-evolution.md)** -- How the system grew from 5 ad hoc prompts in Draft 1 to 27 modular prompts in Draft 3. Five evolution patterns: inline to structured, single to modular, manual to automated, generic to specific, trust to verify. What stayed constant (Dense, Direct, Human) and what changed (everything else).

## Key Takeaways

- Start with three prompts: master system prompt, section writing prompt, de-AI editing prompt. That's enough for consistent, voice-accurate sections.
- The master system prompt is the DNA -- 339 lines of encoded voice, audience profiles, phrase tables, and constraints that get prepended to every AI interaction.
- Each of the 27 prompts earned its place by fixing something that broke. Don't build prompts for theoretical problems.

---

[Previous: Author Voice](../02-author-voice/README.md) | [Next: Agent System](../04-agent-system/README.md) | [Back to AI Writing Process](../README.md)
