# AI Writing Process

**How AI was used to write an 81,000-word book with 775 citations, consistent voice, and multi-layer editorial review.**

This isn't a blog post about prompting ChatGPT and calling it a book. This is the documented system behind *Blueprint for An AI-First Company* -- 12 chapters, 775 inline citations with source URLs, and a voice that reads like one human wrote it. Every prompt, script, skill, and architectural decision is here for you to study, adapt, or steal.

---

## What This Covers

The full AI-assisted book production system, end to end:

- **Author voice encoding** -- 6 files that teach an LLM to write like a specific human, not like an AI
- **Prompt engineering** -- 27 modular prompts across 5 categories (writing, editing, review, research, analysis)
- **Multi-agent orchestration** -- 14 Claude Code skills that act as writer, reviewer, researcher, and quality auditor
- **Research pipeline** -- 180+ Perplexity prompts that generate citation-ready research with source URLs
- **Obsidian vault architecture** -- The file structure, templates, and linking system that kept 12 chapters organized
- **Automation** -- 17 Python scripts for PDF generation, word count analytics, citation management, and vault health
- **Book intelligence app** -- A Flask + PostgreSQL pipeline with 70+ modules for cross-chapter analysis
- **Editorial review** -- A 4-phase process covering structural editing, voice consistency, fact verification, and contradiction detection

---

## By the Numbers

| Metric | Count |
|--------|-------|
| Total words | 81,000+ across 12 chapters |
| Inline citations | 775 with source URLs |
| Writing prompts | 27 modular prompts in 5 categories |
| Claude Code skills | 14 (writer, reviewer, researcher, quality auditors) |
| Research prompts | 180+ for Perplexity automation |
| Python scripts | 17 for automation and analytics |
| Voice system files | 6 defining author tone, style, and guardrails |
| Editorial phases | 4-phase review process |
| Review dimensions | 10-dimension acquisition-level quality audit |
| Intelligence app modules | 70+ in the analysis pipeline |
| Documentation files | 57 across 12 directories |
| Documentation words | 51,000+ with 7 Mermaid diagrams |
| Adaptable templates | 17 fill-in-the-blank starting points |

---

## Navigation

| Section | What You'll Learn |
|---------|-------------------|
| [01 -- Overview](01-overview/README.md) | End-to-end pipeline, architecture decisions, and results |
| [02 -- Author Voice](02-author-voice/README.md) | Building a voice system, gold standard method, drift prevention |
| [03 -- Prompt Engineering](03-prompt-engineering/README.md) | 27 prompts, the master system prompt, writing and editing prompts |
| [04 -- Agent System](04-agent-system/README.md) | Multi-agent architecture, chapter writer workflow, quality skills |
| [05 -- Research Pipeline](05-research-pipeline/README.md) | 180+ prompts, Perplexity automation, citation management |
| [06 -- Obsidian Vault](06-obsidian-vault/README.md) | Vault architecture, templates, linking conventions, dashboards |
| [07 -- Automation](07-automation/README.md) | 17 scripts for PDF generation, analytics, and vault health |
| [08 -- Book Intelligence App](08-book-intelligence-app/README.md) | Flask + PostgreSQL analysis pipeline, 70+ modules |
| [09 -- Review Process](09-review-process/README.md) | Multi-layer review, editorial workflow, contradiction detection |
| [10 -- Lessons Learned](10-lessons-learned/README.md) | What worked, what failed, what I'd do differently |
| [Templates](templates/README.md) | Adaptable starting points for voice, prompts, skills, vault, and scripts |

---

## Who This Is For

- **Non-fiction authors** who want to use AI as a writing partner without losing their voice
- **Technical writers** building documentation systems that need consistency at scale
- **Content teams** exploring multi-agent workflows for long-form production
- **Anyone curious** about what AI-assisted creative work actually looks like when you take it seriously

---

## How to Use This

**Start with [01 -- Overview](01-overview/README.md)** for the full picture -- how the pieces connect, why certain architecture decisions were made, and what the results looked like.

**Jump to any section** that matches your immediate need. Each one is self-contained with enough context to be useful on its own.

**Grab from [Templates](templates/README.md)** when you're ready to build. These are fill-in-the-blank starting points adapted from the actual system -- voice profiles, prompt structures, skill definitions, vault layouts, and automation scripts.

---

## Tech Stack

| Tool | Role |
|------|------|
| **Claude Code** (Opus 4.5) | Writing, editing, review, agent orchestration |
| **Perplexity Pro** | Research and citation generation |
| **Obsidian** | Vault-based manuscript management |
| **Python** | Automation scripts, analytics, PDF generation |
| **Flask + PostgreSQL** | Book intelligence app and cross-chapter analysis |
| **Playwright** | Browser automation for research workflows |

---

## About the Book

*Blueprint for An AI-First Company* covers how companies can build AI into their core operating model -- not as an add-on, but as the foundation. 12 chapters across four parts: Foundations, Building, Operating, and Sustaining. The process documented here is itself a case study in AI-first production.

---

*Built by [Saurav](https://github.com/sauravb) as part of writing Blueprint for An AI-First Company.*
