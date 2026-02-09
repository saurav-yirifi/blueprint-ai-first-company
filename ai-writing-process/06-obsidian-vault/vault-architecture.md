# Vault Architecture

Here's what most people get wrong about writing a book in Google Docs: it works until it doesn't. A 12-chapter book isn't 12 documents. It's a network -- chapters reference each other, concepts span sections, research feeds multiple arguments, case studies appear in different contexts. By chapter 6, you're searching across tabs trying to remember where you defined "data flywheel" and whether Chapter 4 or Chapter 9 has the Spotify example. The tool becomes the bottleneck.

Obsidian eliminates this problem. It's a local Markdown editor with wiki-linking, a graph view that visualizes your entire manuscript as a network, and a file-based structure that plays well with both git and AI agents. For an AI-assisted book, the file-per-section architecture is the key design decision -- every section becomes a self-contained unit of work that an agent can research, write, and review without losing focus.

---

## The Hierarchy

The vault follows a Part, Chapter, Section hierarchy. Four levels deep, each with a clear purpose:

```
Book/drafts/Draft 1/
├── 01-Foundations/                        # Part folder
│   ├── 00-Part-Intro.md                  # Part overview (~500 words)
│   ├── 01-The-AI-First-Imperative/       # Chapter folder
│   │   ├── 00-Chapter-Intro.md           # Chapter overview + metadata
│   │   ├── 01-The-AI-Inflection-Point.md # Individual section
│   │   ├── 02-AI-First-vs-AI-Enabled.md
│   │   ├── 03-The-Competitive-Gap.md
│   │   └── ...more sections
│   ├── 02-The-AI-First-Mindset/
│   └── 03-The-AI-Landscape/
├── 02-Building/
│   ├── 04-AI-Infrastructure/
│   ├── 05-Building-With-AI/
│   ├── 06-Agent-Architecture/
│   └── 07-Microservice-Pattern/
├── 03-Operating/
│   ├── 08-AI-First-Teams/
│   ├── 09-Data-Strategy/
│   └── 10-Operations-and-GTM/
└── 04-Sustaining/
    ├── 11-Ethics-and-Governance/
    └── 12-Staying-Ahead/
```

The numbers matter. `01-Foundations` sorts before `02-Building` in every file browser and every script. `01-The-AI-First-Imperative` sorts before `02-The-AI-First-Mindset`. When you're running a Python script that processes sections in order, or when a reader navigates the vault, everything is already in reading sequence.

---

## Why File-Per-Section

This is the single most important structural decision for AI-assisted writing. Each of the 81 sections is its own Markdown file, averaging ~1,200 words. Here's why that granularity is intentional:

**AI agents work better with focused context.** A 1,200-word section file is a clear unit of work -- one research snapshot, one writing pass, one review. Compare that to a 6,500-word chapter file where the agent starts strong in section 1 but drifts by section 4. Voice degrades. Examples repeat. Research citations thin out. We tested both approaches. The section-per-file model produced measurably more consistent output.

**Parallel writing becomes possible.** When sections are separate files, independent sections can be written by parallel agents. Sections 1 and 3 might have no dependencies -- send them to different agents simultaneously. A monolithic chapter file forces sequential writing.

**Reviews are surgical.** You can review section 3 without re-reading the entire chapter. The reviewer agent gets exactly the unit it needs to check. Changes to one section don't create merge conflicts with another.

**Status tracking gets granular.** Each section has its own `status` field in frontmatter: `outline`, `drafting`, `revising`, `editing`, `done`. The Dashboard shows exactly which sections need work without reading a single word.

---

## Supporting Content

The manuscript lives in `Book/drafts/`, but it's supported by several adjacent folders:

| Folder | Content | Purpose |
|--------|---------|---------|
| `concepts/` | Atomic concept notes (Agent Systems, Data Moats, etc.) | Hub nodes that connect chapters through shared ideas |
| `mocs/` | Maps of Content | Entry points for navigating the vault by topic or structure |
| `notes/research/` | Research notes | Individual research findings with source attribution |
| `notes/case-studies/` | Case study notes | Company deep dives with structured metadata |
| `planning/` | Writing reference docs, tag index | Operational documents for the writing process |
| `templates/` | Templater templates | Auto-filled frontmatter for new files |

The concept notes deserve special attention. A concept note about "Data Flywheel" links to Chapter 9 (where it's introduced), Chapter 1 (competitive advantage), and Chapter 12 (sustaining advantage). These notes are the glue that holds a multi-chapter argument together. Without them, the same concept appears in 4 chapters with slightly different definitions and no explicit connection.

---

## Draft Management

The vault supports multiple complete drafts: `Draft 1/`, `Draft 2/`, `Draft 3/`. Each draft is a full copy of the manuscript. This book went through 3 drafts, and each one improved the *system* as much as the prose.

Why full copies instead of git branches? Two reasons. Obsidian's graph view and Dataview queries work on the file system -- they can't query a git branch. And comparing drafts side by side (literally opening Draft 1's section next to Draft 3's) is faster than git archaeology for editorial decisions.

The trade-off: disk space and duplication. At 81,000 words of Markdown, that's negligible. If your book were 500,000 words with heavy media, you'd want a different approach.

---

## What This Enables

The combination of file-per-section architecture, standardized frontmatter, and concept hub notes turns the vault into something more than a file system. It becomes a queryable database (via Dataview), a visual knowledge graph (via Obsidian's graph view), and a structured input format that AI agents can parse without guessing context.

The vault architecture is the foundation everything else builds on. Templates enforce structure. Links surface connections. Dashboards track progress. None of that works without the hierarchy being right from the start.

---

**Related:** [Templates and Frontmatter](templates-and-frontmatter.md) | [Linking and Navigation](linking-and-navigation.md) | [Obsidian Templates](../templates/obsidian/book-vault-structure.md)
