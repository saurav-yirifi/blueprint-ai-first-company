# Chapter 7: The Microsite Pattern

90% of teams that adopt microservices still batch deploy like they're running a monolith. They created the complexity of distributed systems—separate repositories, containerized deployments, service discovery infrastructure—without capturing the benefit. The services exist independently in theory. In practice, they move in lockstep. Different containers. Same bottleneck.

Uber and Amazon Prime Video learned this the hard way—both had to rebuild after microservices created more coordination overhead than the monoliths they replaced.

The problem isn't microservices. The problem is treating architecture as a technology choice rather than an organizational one. The 10% who succeed don't use different tools. They use different structures. They align architecture with teams, teams with domains, and domains with deployment autonomy.

This chapter introduces the microsite pattern: autonomous domain applications with shared infrastructure. The architecture that enables just two people to manage fifteen domains. The same architecture that scales to a thousand engineers without coordination overhead.

<div class="yirifi-anchor" markdown>

> "Each domain—DevOps, QA, Data, Marketing, Sales, Finance—owns their own microsite end-to-end. Same architecture, different domain logic. When AI capabilities evolve, we add a new module. No rewiring required."

Microsite architecture isn't about containers or service meshes. It's about answering a structural question: who owns what, and how do they move independently? Own your domain. Share your foundation.

</div>

## What You'll Learn

- **[The Microsite Advantage](./01-domain-microsites.md):** The 90% failure rate, Uber's DOMA transformation from 2,200 services to 70 domains (10x support cost drop, 25-50% faster onboarding), and the four characteristics that separate successful microservices from distributed monoliths.

- **[Anatomy of a Microsite](./02-anatomy-of-a-domain-microsite.md):** The three-layer contract (controller, service, repository), Backstage templates that encode organizational knowledge, and Cruft for automated enforcement—plus the test: can a new engineer deploy on day one?

- **[Centralize vs Distribute](./03-centralize-vs-distribute.md):** Four things that must stay centralized (auth, permissions, observability, infrastructure) and five that belong to domain teams. Netflix's Passport pattern for edge authentication and why ABAC beats RBAC beyond 50 roles.

- **[AI Agent Access](./05-ai-agent-access.md):** The DIRECT/GATEWAY/EXCLUDE model for tiered access, MCP's 1,000+ connectors, identity passthrough for audit trails, and why new endpoints must default to invisible.

- **[Microsite Orchestration](./06-microsite-orchestration.md):** The 15-minute new microsite via platform automation, and the strangler fig pattern that cut Shopify's CI from 45 to 18 minutes.

- **[Inter-Microsite Communication](./07-inter-microsite-communication.md):** Sync vs async decision framework, Netflix's billions of daily events through Kafka, choreography versus orchestration, and permission-aware navigation for humans and AI agents.

- **[Governance Patterns](./08-governance-patterns.md):** Contract-first APIs with Spectral validation, breaking change detection via oasdiff, and the principle that governance works when doing the right thing is easier than doing the wrong thing.

---

## The Real Question

For startups, this matters from day one. The boundaries you draw now become team boundaries later. Retrofitting costs ten times more than building it in. Even at three people, thinking in domains pays off—you're establishing patterns that scale.

For established organizations, the path is the strangler fig. Pick one domain willing to experiment. Let them own their AI tools. Prove the economics work. Each step is independently deployable and reversible. Success attracts adoption.

The chapters leading here built the foundation. [Chapter 5](../05-building-with-ai/README.md) showed how to build applications with AI. [Chapter 6](../06-agent-architecture/README.md) introduced the agent types that power those applications. But agents need systems to interact with. This chapter provides the architectural pattern that makes AI-first applications possible at scale.

Own your domain. Share your foundation. Here's how.

---

[Part Overview](../README.md) | [Book Contents](../../README.md)
