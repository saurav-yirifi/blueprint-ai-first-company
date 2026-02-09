# Lessons Learned

The honest retrospective -- what produced the most value, what wasted time, and the lean version of this system you should actually build if starting from scratch. No revisionist history. Every lesson came from doing it wrong first.

## Contents

- **[What Worked](what-worked.md)** -- The 8 highest-impact decisions: voice system before everything (2-day investment, saved weeks of editing), research-first pipeline (flipped the economics of evidence), separate writer and reviewer agents (caught blind spots neither would find alone), section batching at max 4 per agent, the living kill list, automated quality audits with weighted health scores, Obsidian over Google Docs, and planning for 3 drafts instead of 1 perfect draft. The common thread: front-loading effort to reduce rework.

- **[What Failed](what-failed.md)** -- The 8 most expensive mistakes: starting without voice encoding (Draft 1 was a very expensive outline), monolithic "write a chapter" prompts (wasted several weeks), write-then-research (evidence decorating opinions instead of shaping them), trusting AI self-review, over-engineering the intelligence app early, inconsistent frontmatter, mixed metaphor blindness, and no cross-chapter consistency checking until late (26 contradictions accumulated). The meta-lesson: every failure shares a root cause of optimizing for speed over system quality.

- **[If Starting Over](if-starting-over.md)** -- The lean version: 5 phases that capture 80% of the value with 20% of the infrastructure. Phase 1: voice foundation (4 files, 1-2 days). Phase 2: research pipeline (Perplexity prompts, synthesis files). Phase 3: writing system (8 prompts, separate writer/reviewer). Phase 4: quality pipeline (kill list, voice check, citation audit). Phase 5: editorial (one pass per focus, cross-chapter checks every 4 chapters). What to skip on day one and the scaling sequence from chapters 1-3 through 10-12.

## Key Takeaways

- The voice system is non-negotiable from day one. Everything else can wait until the problem it solves actually shows up.
- Build infrastructure in response to problems, not in anticipation of them. The scaling sequence: scripts first, SQLite when scripts hit limits, full app only at 50K+ words.
- Every shortcut tried early -- skipping voice files, writing without research, trusting self-review -- cost more to fix than doing it right from the start. The system rewarded doing things right the first time, every single time.

---

[Previous: Review Process](../09-review-process/README.md) | [Back to AI Writing Process](../README.md)
