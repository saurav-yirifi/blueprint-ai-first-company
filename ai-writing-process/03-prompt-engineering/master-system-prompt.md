# Anatomy of the Master System Prompt

The master system prompt is the single most important artifact in the entire writing system. It's 339 lines of encoded voice, audience profiles, phrase tables, and quality constraints that get prepended to every AI interaction. Without it, you get competent generic prose. With it, reviewers can't reliably distinguish AI-assisted sections from hand-written ones.

This document breaks down what's in it, why each section exists, and the design decisions that make it work.

---

## What It Contains

The prompt has 11 sections, each solving a specific problem:

| Section | ~Lines | Purpose |
|---------|--------|---------|
| Core Principle | 15 | Dense, Direct, Human -- the three-word DNA |
| Voice DNA (5 elements) | 40 | Non-negotiables: numbered frameworks, balanced skepticism, pop culture bridges, honest complexity, practitioner perspective |
| Voice Calibration | 30 | Three spectrums with "too much / sweet spot / too much" examples |
| 19 Craft Techniques | 25 | Extracted from gold standard analysis -- one line each |
| Signature Phrases | 40 | Tables of phrases to use: opening gambits, transitions, balance markers, action orientation |
| Generic Phrases to Avoid | 35 | Corporate speak kills, AI-generated patterns, filler detection |
| 10 Learnings | 25 | Encoded mistakes from real writing failures |
| Two Audiences | 50 | Sarah (enterprise COO) and Marcus (startup founder) -- full profiles with internal monologues |
| Density Test | 15 | Scorecard from gold standard benchmark |
| Structural Requirements | 10 | No emojis, subheadings, analogies, action items |
| Voice Calibration Check | 15 | Final 9-point verification table |

Total: ~339 lines of active prompt content inside a 387-line file (the rest is markdown formatting and usage notes).

---

## Key Design Decisions

### Phrases Live in Tables, Not Prose

The signature phrases section uses four tables organized by function: opening gambits, mid-section transitions, balanced perspective markers, and action orientation. Each row is a phrase paired with when to use it.

Why tables? Two reasons. First, they're faster to scan -- the AI processes structured data more reliably than buried instructions. Second, tables are easier to maintain. Adding a new signature phrase means adding one row, not rewriting a paragraph.

The "avoid" section works the same way. Corporate buzzwords, AI-generated patterns, and filler phrases each get their own table with the pattern, why it's a problem, and the fix.

### Audiences Have Internal Monologues

Sarah and Marcus aren't just demographic profiles. Each has a section called "Internal Monologue" -- the skeptical thoughts running through their heads while reading.

Sarah's monologue: "Here we go again, another AI book promising miracles..." and "Get to the point or I'm closing this book."

Marcus's monologue: "Every paragraph I read is time I'm not shipping. Make it count." and "Is this just enterprise advice repackaged for startups?"

This forces empathy at the prompt level. The AI isn't just targeting "enterprise executives" -- it's writing for someone who survived 3 failed transformation initiatives and manages 2,000 employees resistant to change. The monologue makes the audience visceral instead of demographic.

### Learnings Are Rules, Not Stories

The 10 Learnings section encodes mistakes as constraints: "One vivid anchor, not seven" and "Pick one metaphor. Commit. Don't mix." Each learning is 2-3 sentences max.

The AI doesn't need the story of how we discovered these patterns. It needs the rule. The full narrative lives in the separate Learnings file (`06-Learnings.md`) for human reference. The prompt gets the compressed version.

### Calibration Spectrums Define by Negation

The voice calibration section uses three spectrums -- formality, density, and authority -- each with three columns: too casual, sweet spot, and too formal.

The sweet spot is defined by what it's *not*. "Here's a practical framework for getting started" sits between "Just throw some AI at it lol" and "Organizations should endeavor to implement..." You understand the target by seeing the boundaries, not just a description that could mean anything.

This is harder to write than simple instructions like "be moderately formal." But it's dramatically more effective at constraining output. The AI can pattern-match against concrete examples much better than it can interpret subjective adjectives.

---

## How It Gets Used

The master system prompt never runs alone. It's system context that gets composed with task-specific prompts:

```
[Master System Prompt]  <-- always present, sets voice/audience/rules
+
[Task Prompt]           <-- specific to what you're doing (write section, edit voice, review chapter)
+
[Content Input]         <-- research, draft text, or topic outline
```

The orchestration skill (chapter-writer) handles the composition automatically. When you invoke it, the master prompt is loaded as system context without you pasting it manually. Individual prompts are written assuming it's already present -- they reference voice elements and audience profiles without redefining them.

For standalone use outside the agent system, copy the full prompt content (between the code fences in the file) as system context in any Claude session before adding your task-specific instructions.

---

## Adapting It For Your Voice

The structure transfers. The content doesn't.

To build your own master system prompt, you need your own versions of each section: your core principle (what three words define your voice?), your non-negotiables (what makes your writing distinctly yours?), your calibration spectrums (where does your sweet spot fall?), your phrase tables (what do you actually say vs. what generic writers say?), and your audience profiles (who are you really writing for, and what are they thinking while reading?).

The [Voice System](../02-author-voice/README.md) section covers how to build these from scratch. The [Master Prompt Template](../templates/prompts/master-system-prompt-template.md) provides a fill-in-the-blank starting point.

Here's the thing most people skip: the encoded learnings section. It's tempting to start with the voice DNA and phrase tables. But the learnings -- the specific mistakes you've caught in AI output and encoded as rules -- are what separate a good master prompt from a great one. They grow over time as you discover new failure modes. My prompt's 10 learnings came from 3 drafts of a 12-chapter book. Your first version might have 2-3. By your third draft, you'll have more.

---

**Related:** [Prompt Architecture](prompt-architecture.md) | [Building a Voice System](../02-author-voice/building-a-voice-system.md) | [Master Prompt Template](../templates/prompts/master-system-prompt-template.md)
