# Chapter 9: Data Strategy — Flywheels, Moats, and Ethics

Harvey had zero proprietary legal data in mid-2022. No case law databases. No contract archives. No litigation records. They were a startup trying to build AI for one of the most data-intensive industries on the planet, competing against companies with decades of accumulated legal documents.

Three years later, Harvey reached $8 billion valuation, $100 million ARR, and deployment in 42 countries[^harvey-valuation]. Meanwhile, IBM invested over $4 billion in Watson Health, acquiring massive healthcare datasets from MD Anderson and Memorial Sloan Kettering, then sold the entire unit for approximately $1 billion[^watson-failure]. More data. Less outcome.

The difference wasn't luck. It was architecture. Harvey designed a flywheel before they had data to spin it. IBM collected data without a flywheel to compound it. One approach creates accelerating advantage. The other creates an expensive storage bill.

The uncomfortable truth: the data moats you think you have probably don't exist. Translation companies spent decades building linguistic databases. Foundation models trained on public web data approximated their capability in months. Volume has lost its edge. The game has changed, and companies still playing the "accumulate everything" strategy are building sandcastles while the tide rises.

What replaces volume-based moats? Systems that generate unique data through usage. Architectures where every interaction compounds into advantage.

This chapter is about building that kind of advantage—and the ethical architecture that lets you sustain it.

<div class="yirifi-anchor" markdown>

> "Three database types, each matched to its data: transactions in relational, content in documents, speed-critical in cache. But the real flywheel is usage analytics—every agent interaction becomes training data for better agent interactions."

**Universal insight:** The data moats you think you have probably don't exist. The new advantage comes from data you generate through product usage that competitors can't buy, scrape, or synthesize.

**Memorable close:** "Data that improves as you use it."

</div>

## What You'll Learn

- **[Data Strategy Fundamentals](./01-data-strategy-fundamentals.md):** The three strategic questions that separate real data strategy from expensive storage—plus why 93% of CDOs say data strategy is crucial to GenAI, yet 57% haven't made necessary changes[^cdo-gap].

- **[Building Data Flywheels](./02-building-data-flywheels.md):** The 5 components of high-velocity flywheels, the cold start paradox that kills 80% of AI projects, and how Duolingo's Birdbrain drove 59% DAU growth while Klarna's flywheel plateaued.

- **[Data Moats](./03-data-moats.md):** The moat test that separates weeks of defensibility from years. Tesla earns $7K per vehicle as a data collector versus Waymo's $150K. Cursor grew from $1M to $100M in one year through execution velocity, not dataset size.

- **[Polyglot Persistence in Practice](./04-polyglot-persistence-in-practice.md):** Start with PostgreSQL. Notion manages 200 billion blocks on sharded Postgres. Add complexity only when you have measured problems—vector databases saw 377% growth in 2024, but that doesn't mean you need one on day one.

- **[Privacy by Design](./05-privacy-by-design.md):** GDPR fines hit EUR 1.2 billion in 2024, up 38%[^dla-piper]. The EU AI Act high-risk deadline is August 2, 2026. The strategic reframe: privacy as competitive advantage, not compliance burden.

- **[The 6 Data Strategy Mistakes That Stall Flywheels](./06-the-6-data-strategy-mistakes.md):** Why 92% of AI startups fail within 18 months, 95% of enterprise pilots never reach production, and 43% build products nobody wanted. The six patterns that kill flywheels—all avoidable.

---

## The Real Question

The data strategies that succeed in 2025 and beyond share a common architecture: they generate unique data through product usage, compound that data through automated feedback loops, and protect it through privacy practices that build trust rather than erode it.

For startups, this is both opportunity and discipline. You don't have legacy data systems to migrate, which is actually an advantage. Your data strategy and your product strategy can be the same thing from day one. Design products that generate unique data. Build the flywheel architecture before you have data to spin it. Validate product-market fit through manual processes before investing in data infrastructure—43% of AI startups fail specifically because they build products nobody wanted.

For established organizations, the path is different but not closed. You likely have years of historical data across multiple systems. The strategic question isn't "how do we get more data?" but "which existing data, if connected and activated, creates compounding advantage?" AT&T achieved 94% accuracy versus 78% for generic GPT-4 by activating data they already had[^att]. The advantage came from fine-tuning on their own customer service patterns, not collecting new data.

Both audiences face the same truth: the proprietary data flywheel—not the model—determines who compounds. And flywheels that spin without ethical guardrails eventually spin backward—through regulatory action, user distrust, or the compounding degradation of data quality.

The companies winning at data strategy aren't the ones with the most data. They're the ones whose data generates the most advantage.

## References

[^harvey-valuation]: TechCrunch. [Legal AI startup Harvey confirms $8B valuation](https://techcrunch.com/2025/12/04/legal-ai-startup-harvey-confirms-8b-valuation/)

[^watson-failure]: Slate. [IBM Watson Health Failure Analysis](https://slate.com/technology/2022/01/ibm-watson-health-failure-artificial-intelligence.html)

[^cdo-gap]: AWS. [CDO Survey on Data Strategy and GenAI](https://aws.amazon.com/executive-insights/content/data-and-ai-strategy/)

[^dla-piper]: DLA. [Piper GDPR Fines and Data Breach Survey 2024](https://www.dlapiper.com/en/insights/publications/2024/01/dla-piper-gdpr-fines-and-data-breach-survey-2024)

[^att]: AT&T. [LLM Fine-Tuning Case Study](https://www.linkedin.com/pulse/how-att-uses-llms-improve-customer-service/)

---

[Part Overview](../README.md) | [Book Contents](../../README.md)
