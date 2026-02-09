# Book Intelligence App

A Flask + PostgreSQL application with 70+ modules that provides persistent analysis, semantic search, and API access for the writing system. This section covers when scripts stop being enough, the app architecture, the 6-dimension analysis pipeline, and how Claude Code skills call the API instead of spawning scripts.

## Contents

- **[When Scripts Aren't Enough](why-build-an-app.md)** -- The tipping point: no persistent state, no trend tracking, cross-chapter analysis requiring full vault loads, embeddings needing vector storage, and skills needing HTTP endpoints. When you don't need an app (under 50K words, fewer than 6 chapters, single-draft workflow) versus when you do. The honest ROI question and the simpler SQLite alternative. Progression: scripts, then SQLite, then full app -- each transition forced by a specific limitation.

- **[App Architecture](app-architecture.md)** -- The stack (Flask, PostgreSQL, pgVector, Docker Compose, SQLAlchemy, Alembic) and why each was chosen over alternatives. Three-layer architecture: API layer (skills and dashboards), service layer (analysis and search logic), repository layer (data access). Ten data models covering sections, research, embeddings, analysis cache, links, quotes, statistics, metrics, indexing state, and draft comparisons. Five schema migrations that evolved with the system.

- **[Analysis Pipeline](analysis-pipeline.md)** -- Six quality dimensions analyzed across all 81 sections: voice, citations, links, terms, openings, and research. Four pipeline stages: indexing (content hash optimization), analysis (per-dimension scoring with draft versioning), aggregation (weighted chapter health scores), and trending (time-series tracking across editorial passes). Embedding-based analysis for conceptual similarity, overlap detection, and research matching via pgVector.

- **[Skill API Integration](skill-api-integration.md)** -- How skills call the API instead of re-running analysis from scratch. Endpoint mapping for each skill (review-chapter, check-voice, check-citations, map-research, audit-links, find-similar, compare-drafts). The flow from skill invocation to cached response in under a second. Deep review mode for semantic similarity, cross-chapter consistency, citation source diversity, and company example distribution. When to build the API layer: the decision framework based on skill count and shared state needs.

## Key Takeaways

- Don't build the app until scripts hit real limits. For this project, the tipping point came around 50,000 words when skills needed persistent state and semantic search.
- The key architectural insight: skills call the API, not the database. Schema changes don't break skill integrations.
- Analysis results are cached and only recompute when content changes. Edit one section and only that section gets re-analyzed -- the other 80 keep their cached scores.

---

[Previous: Automation](../07-automation/README.md) | [Next: Review Process](../09-review-process/README.md) | [Back to AI Writing Process](../README.md)
