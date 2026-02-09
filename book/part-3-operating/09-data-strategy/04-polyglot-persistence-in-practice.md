# Polyglot Persistence in Practice

The Yirifi engineering team runs three database types: transactions in relational, content in documents, speed-critical in cache. What makes the difference: they didn't start there. They started with PostgreSQL. They added complexity when they had measured problems, not imagined ones.

> **Want the full implementation guide?** See Appendix: Polyglot Persistence Stages for the complete evolution path, anti-patterns, and the usage analytics flywheel.

## What Goes Where: The Matching Principle

The database decision matrix isn't mysterious. It's straightforward once you understand what each type does well.

| Question | If Yes |
|----------|--------|
| Does this data require ACID transactions? | Relational |
| Does the schema change frequently? | Document store |
| Is read latency critical (< 10ms)? | Cache layer |
| Do you need semantic/similarity search? | Vector database |
| Is this analytics, not operations? | Data warehouse |

**Relational databases** handle user accounts, billing, audit logs—anything where "eventual consistency" means "eventually wrong." Notion manages 200 billion blocks on sharded PostgreSQL[^notion-sharding]. OpenAI runs PostgreSQL as the backbone for ChatGPT. Before reaching for NoSQL because "Postgres won't scale," try proper indexing and connection pooling.

**Document databases** excel at semi-structured content with flexible schemas. Agent conversation histories. JSON-heavy API responses. Use them when schema evolution is a genuine requirement, not when you haven't thought through your data model.

**Cache layers** serve speed-critical data: session state, rate limiting, frequently accessed keys. Discord used in-memory storage to handle over 1 million concurrent users in the MidJourney server[^discord-midjourney].

**Vector databases** store embeddings for semantic search. Usage grew 377% in 2024 across enterprises[^databricks-adoption]. This is usually the first genuinely new capability you add, not a performance optimization.

## The Practical Starting Point

**Month 1-6:** PostgreSQL for everything. Seriously. Everything. Resist the urge to add complexity.

**When latency becomes measurable:** Add Redis for session state and frequently-read data. Not before.

**When schema flexibility blocks iteration:** Add a document store for the specific data type that needs flexibility.

**When AI features require embeddings:** Add a vector database.

**When analytics queries impact production:** Add a data warehouse. Separate the analytical workload from the operational workload.

The goal isn't elegance. The goal is a data architecture that accelerates your flywheel without creating operational overhead that slows everything else down.

## References

[^notion-sharding]: Sharding Postgres at Notion. [Notion Blog](https://www.notion.com/blog/sharding-postgres-at-notion)

[^discord-midjourney]: Discord MidJourney Performance. [InfoQ](https://www.infoq.com/news/2024/01/discord-midjourney-performance/)

[^databricks-adoption]: State of AI Enterprise Adoption. [Databricks](https://www.databricks.com/blog/state-ai-enterprise-adoption-growth-trends)

---

---

[← Previous: Data Moats: What's Defensible vs Replicable](./03-data-moats.md) | [Chapter Overview](./README.md) | [Next: Privacy by Design →](./05-privacy-by-design.md)
