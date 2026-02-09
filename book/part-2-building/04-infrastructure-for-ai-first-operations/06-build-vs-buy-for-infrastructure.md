# Build vs Buy for Infrastructure

When managed services win, when they don't.

<div class="yirifi-anchor" markdown>

> "Build what differentiates you. Buy everything else. The hard part is knowing which is which."

**The structural insight:** At Yirifi, we buy infrastructure by default. The bar for building is high: we must demonstrate that the custom solution provides competitive advantage that justifies ongoing maintenance cost. Databases? Buy. Auth? Buy. AI orchestration that's core to our product? Build. This isn't laziness—it's strategic focus.

</div>

Everyone thinks they're special when it comes to build vs buy. Every startup believes their use case is unique enough to justify custom infrastructure. Every enterprise worries that vendors will hold them hostage. And almost everyone gets it wrong.

The pattern I keep seeing: teams build what they should buy, then scramble to maintain it. Or they buy everything, then discover they've outsourced their competitive advantage.

### The Three-Question Framework

Before evaluating any infrastructure component, answer three questions:

**1. Is this component a core competitive differentiator?**

Linear built a custom sync engine because real-time collaboration IS their product. They evaluated Replicache, Electric SQL, and cr-sqlite before deciding to build custom. Why? CRDTs introduce overhead and struggle with partial syncing and permissions. Linear wanted an ORM-like API where developers write `issue.title = "New Title"; issue.save()` without thinking about sync logic[^linear-sync]. No off-the-shelf solution checked their boxes. That's a build decision.

But they buy managed PostgreSQL because databases aren't their competitive advantage. The sync engine creates lasting differentiation. The database maintains parity.

**2. Do you have the team to sustain it?**

Building requires at least 6 engineers and 12 months to reach feature parity with existing solutions[^inkeep]. If you're a 15-person startup and three engineers spend a year on infrastructure, you've diverted 20% of your company from product work. That's a bet-the-company decision.

**3. What's your scale certainty?**

Build makes sense when you know exactly what you need at exactly what volume. Buy makes sense when you're still figuring things out.

If you can't answer "yes" to at least two of these questions, buy.

### The Real Numbers

**Vector databases** break even at 80-100 million queries per month[^openmetal]. Below that threshold, Pinecone at $100-200/month beats self-hosted infrastructure costing approximately $1,174/month according to OpenMetal's analysis[^openmetal]. Setup costs for self-hosting run $2,400-6,000 in engineering time just to get started[^openmetal]. Most companies never hit that threshold.

**AI gateways** tip at around $10,000/month in LLM spend. OpenRouter charges a 5% markup[^helicone]. At $10K spend, that's $500/month in pure margin going to the gateway. Below that, the markup costs less than running your own infrastructure.

**Authentication** gets expensive at scale with per-user pricing. Auth0 can run $13,000+ annually for B2B workloads[^supabase]. But building custom auth means owning security incidents. The $13K suddenly looks cheap when you're explaining a breach to your board.

### The Hidden Cost Multiplier

Most build-vs-buy analyses miss this: 60-70% of infrastructure costs are invisible[^wpengine]. They don't show up on any invoice.

When you build, you own: on-call rotations (someone's getting paged at 3am), security patches, SSL renewals, DDoS mitigation, and the opportunity cost of senior engineers maintaining servers instead of building product.

Mid-size organizations spend an average of $2.6M annually maintaining digital platforms when you factor in developer salaries, hosting costs, and downtime losses[^wpengine]. That's what "self-hosted is free" actually costs.

### Component-by-Component Guidance

**Databases:** Buy managed services until you're processing millions of operations daily with predictable patterns. Database operations is a full-time job; make sure you want that job before taking it.

**AI provider access:** Start with direct APIs or an aggregator like OpenRouter. Build a gateway layer only when routing logic becomes complex enough that you're fighting the aggregator.

**Authentication:** Buy from a provider that handles human auth well and offers agent identity extensions. Build only the delegation logic specific to your agent architecture. Half of AI providers fail basic security standards[^informatica]. You don't want to be in that half.

**Observability:** Buy. Platforms like Helicone and LangSmith have solved the hard problems. The caching alone often pays for the subscription. Self-host only if you're processing 50K+ events monthly and have the DevOps capacity[^softcery].

**Vector storage:** Buy until you can't. pgvector handles most workloads. Pinecone handles the next tier. Be honest about when managed services genuinely can't meet your requirements.

### The Evolution Pattern

The smartest companies follow a progression: buy to validate, hybrid to extend, build to differentiate. Getting the timing right matters more than getting the decision right.

Pre-product-market fit? Buy everything. Speed matters more than cost optimization. As we saw in Section 1, timeline failures killed 42% of AI initiatives in 2025. Most of those teams built what they should have bought.

At scale, make case-by-case decisions based on actual data. Run small experiments—spin up self-hosted infrastructure for one component, measure the true cost including engineering time, then decide based on reality rather than spreadsheet projections.

## References

[^inkeep]: Inkeep — [Build vs Buy AI Support Decision Framework for 2025](https://inkeep.com/blog/build-vs-buy-ai-support-decision-framework-for-2025)

[^openmetal]: OpenMetal — [When Self-Hosting Vector Databases Becomes Cheaper Than SaaS](https://openmetal.io/resources/blog/when-self-hosting-vector-databases-becomes-cheaper-than-saas/)

[^helicone]: Helicone — [OpenRouter Alternatives](https://www.helicone.ai/blog/openrouter-alternatives)

[^supabase]: Supabase — [Supabase Auth: Build vs Buy](https://supabase.com/blog/supabase-auth-build-vs-buy)

[^wpengine]: WP Engine — [Hidden Costs of DIY Hosting](https://wpengine.com/blog/hidden-costs-of-diy-hosting/)

[^softcery]: Softcery — [Top 8 Observability Platforms for AI Agents in 2025](https://softcery.com/lab/top-8-observability-platforms-for-ai-agents-in-2025)

[^informatica]: Informatica — [Why AI Projects Fail](https://www.informatica.com/blogs/the-surprising-reason-most-ai-projects-fail-and-how-to-avoid-it-at-your-enterprise.html)

[^linear-sync]: Linear Sync Engine Analysis — [Fujimon](https://www.fujimon.com/blog/linear-sync-engine)

---

[← Previous: The 5 Infrastructure Mistakes That Kill AI Initiatives](./05-the-5-infrastructure-mistakes.md) | [Chapter Overview](./README.md)
