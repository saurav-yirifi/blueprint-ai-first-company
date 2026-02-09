# Own Your Domain, Share Your Foundation

A tension kills AI initiatives: domain teams want autonomy to ship fast, platform teams want consistency to maintain sanity. Let both run unchecked and you get chaos. Over-centralize and you get bottlenecks that strangle innovation.

The companies that actually scale AI have figured out a simple principle: own your domain, share your foundation. The pattern: domain teams own what requires business context, platform teams own what requires infrastructure expertise.

## What Domain Teams Own

If it requires understanding the customer, the business context, or the domain nuance, it belongs with the domain team:

- **Agent behavior and automation logic.** Your pricing team knows pricing. Your support team knows customer pain points. They define how AI agents behave in their domain.
- **Model selection within guardrails.** Domain teams pick which models fit their use cases. Platform provides approved options and governance. Domain chooses within it.
- **Prompt engineering and evaluation.** The people closest to the work understand what "good" looks like. They build prompt libraries, define success metrics, iterate based on real feedback.
- **Domain-specific metrics.** Central dashboards show platform health. Domain teams own the metrics that matter for their outcomes.

A 2024-2025 survey found that 89% of practitioners use AI daily, while 40% now own AI platform responsibilities directly[^vultr-survey]. Domain expertise and AI capability are converging, not separating.

## What Platform Teams Own

If it requires infrastructure expertise, security knowledge, or cross-organizational consistency, it belongs with the platform team:

- **AI gateway and routing.** One place to manage model access, track usage, enforce rate limits. When every team builds their own integration, you get ungovernable sprawl[^ai-gateway].
- **Observability and monitoring.** Real-time token consumption, cost accumulation per application, visibility into which department called which model, how often, at what cost.
- **Security and compliance infrastructure.** Audit trails for SOC2, HIPAA, GDPR. Platform builds it once, domain teams inherit automatically. Only 6% of organizations have advanced AI security strategies[^security-gap]—the ones who do treat it as platform responsibility.
- **Core infrastructure and authentication.** Model access, credential management, rate limiting. The substrate every domain team builds on.

OpenAI's internal financial engineering team articulated this philosophy: "decentralized experimentation on a centralized substrate"[^openai-substrate]. The platform provides reusable infrastructure so product teams move quickly without compromising trust.

## Making It Work at Scale

Uber's Michelangelo demonstrates this at scale. The central platform owns infrastructure—data processing, training pipelines, deployment. Domain teams make critical decisions through a domain-specific language for selecting and combining features. Teams add their own functions without platform approval[^uber-michelangelo]. The result: approximately 400 active ML projects, over 20,000 training jobs monthly, 5,000+ models in production[^uber-scale]. That's not a bottleneck. That's leverage.

Netflix built Metaflow with the same philosophy. Hundreds of domain teams maintain independent ML projects. The platform's job isn't to approve—it's to reduce friction so teams move from experimentation to production "with minimal overhead"[^netflix-metaflow].

The debate between centralized and decentralized AI teams has a predictable answer—neither extreme works. Completely centralized teams become bottlenecks. Completely decentralized teams create tool sprawl and skyrocketing spend[^linkedin-debate].

GitLab learned this the hard way. Justin Farris, VP of Monetization, described years of "circular debate" until the reporting line changed. When he began reporting directly to the CEO, "decisions became faster and clearer"[^gitlab]. The lesson: unclear ownership creates friction that compounds.

This principle isn't about drawing org chart lines. It's about answering one question clearly for every AI capability—who can change this, and what can they change without asking permission? Get that answer right, and domain teams move fast while platform teams maintain sanity.

---

## References

[^uber-michelangelo]: Planet Cassandra. Meet Michelangelo: Uber's Machine Learning Platform — [planetcassandra.org](https://planetcassandra.org/leaf/meet-michelangelo-uber-s-machine-learning-platform/)

[^uber-scale]: Uber Engineering Blog. Scaling Machine Learning at Uber with Michelangelo — [uber.com](https://www.uber.com/blog/scaling-michelangelo/)

[^netflix-metaflow]: InfoQ. Netflix Metaflow — [infoq.com](https://www.infoq.com/news/2024/03/netflix-metaflow/)

[^vultr-survey]: Vultr. Platform Engineering State of AI 2025 Report — [discover.vultr.com](https://discover.vultr.com/platform-engineering-state-of-ai-2025-report)

[^ai-gateway]: Jimmy Song. AI Gateway In Depth — [jimmysong.io](https://jimmysong.io/blog/ai-gateway-in-depth/)

[^security-gap]: Mint MCP. Enterprise AI Infrastructure Statistics 2025 — [mintmcp.com](https://www.mintmcp.com/blog/enterprise-ai-infrastructure-statistics-2025)

[^openai-substrate]: Metronome. Monetization Engineering for the AI Era — [metronome.com](https://metronome.com/blog/monetization-engineering-for-the-ai-era-platform-ownership-and-observability)

[^linkedin-debate]: Devineni, P. AI Leadership Team Topologies — [linkedin.com](https://www.linkedin.com/posts/pdevineni_aileadership-teamtopologies-aistrategy-activity-7413595065006206976-4RQa)

[^gitlab]: Metronome. Monetization Engineering for the AI Era — [metronome.com](https://metronome.com/blog/monetization-engineering-for-the-ai-era-platform-ownership-and-observability)

---

[← Previous: The 4 Team Models for AI-First Operations](./01-the-4-team-models.md) | [Chapter Overview](./README.md) | [Next: Hiring for AI-First →](./03-hiring-for-ai-first.md)
