# Chapter 7: The Microsite Pattern -- Resources

> Curated resources for deeper exploration of topics covered in this chapter.

## Frameworks from This Chapter

- [Examples Directory](../../../examples/) -- Code examples, configuration templates, and agent patterns referenced throughout the book, including infrastructure and agent architecture examples relevant to the microsite pattern.

## Tools & Platforms

### Microsite Infrastructure
- [Flask](https://flask.palletsprojects.com/) -- Python micro web framework; Yirifi's choice for all 15 domain microsites (DevOps, QA, Data, Marketing, Sales, Finance).
- [HTMX](https://htmx.org/) -- HTML-first frontend; no React or complex framework needed for domain microsites.
- [PostgreSQL](https://www.postgresql.org/) -- Primary relational database; each microsite can have its own schema while sharing infrastructure.
- [Redis](https://redis.io/) -- Session management and RBAC permission caching across microsites.

### Service Architecture
- [Backstage (Spotify)](https://backstage.io/) -- Developer portal and service catalog; templates encode organizational knowledge for new microsite creation.
- [Cruft](https://cruft.github.io/cruft/) -- Template enforcement tool; ensures microsites conform to architectural standards automatically.
- [Spectral](https://stoplight.io/open-source/spectral) -- API linting tool; contract-first API validation for inter-microsite communication.
- [oasdiff](https://github.com/Tufin/oasdiff) -- OpenAPI diff tool; detects breaking changes in API contracts between microsites.

### Communication & Orchestration
- [Apache Kafka](https://kafka.apache.org/) -- Event streaming; Netflix processes billions of daily events for inter-service communication.
- [RabbitMQ](https://www.rabbitmq.com/) -- Message broker for async microsite-to-microsite communication.
- [Temporal](https://temporal.io/) -- Workflow orchestration for complex cross-microsite processes.

### Agent Access Layer
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) -- 1,000+ connectors; the standard for exposing microsite capabilities to AI agents.
- [Claude Code](https://code.claude.com/) -- Agentic coding tool; functions as both MCP client and server for microsite interaction.

### Deployment & CI/CD
- [Docker](https://www.docker.com/) -- Container runtime for microsite isolation and deployment.
- [GitHub Actions](https://github.com/features/actions) -- CI/CD automation; claude-code-action enables AI-assisted PR review.

## Further Reading

- [Uber's DOMA: Domain-Oriented Microservice Architecture](https://www.uber.com/blog/microservice-architecture/) -- Transformation from 2,200 services to 70 domains; 10x support cost reduction; 25-50% faster onboarding.
- [Amazon Prime Video: Monolith Beats Microservices](https://www.primevideotech.com/video-streaming/scaling-up-the-prime-video-audio-video-monitoring-service-and-reducing-costs-by-90) -- Why Prime Video rebuilt a microservice pipeline as a monolith, reducing costs by 90%.
- [Shopify: Deconstructing the Monolith](https://shopify.engineering/deconstructing-monolith-designing-software-maximizes-developer-productivity) -- Strangler fig pattern that cut CI from 45 to 18 minutes.
- [GitLab: The Modular Monolith](https://about.gitlab.com/blog/) -- GitLab's service decomposition journey from monolith to modular architecture.
- [Netflix Passport Pattern](https://netflixtechblog.com/) -- Edge authentication pattern for centralized auth across distributed services.
- [Linear's Custom Sync Engine](https://www.fujimon.com/blog/linear-sync-engine) -- Why Linear built custom sync (differentiator) while buying everything else.
- [vFunction: Microservices Adoption Research](https://vfunction.com/) -- 90% of teams that adopt microservices still batch deploy like a monolith.

## Research & Data

- Microservices failure rate: 90% of teams that adopt microservices still batch deploy in lockstep -- creating distributed monoliths.
- Uber DOMA results: 2,200 services consolidated into 70 domains; 10x support cost reduction; 25-50% faster developer onboarding.
- Shopify CI improvement: Strangler fig pattern reduced CI pipeline from 45 minutes to 18 minutes.
- Conway's Law: Architecture follows organizational structure -- align teams with domains, not technology layers.
- ABAC vs RBAC: Attribute-Based Access Control becomes necessary beyond 50 roles; RBAC creates role explosion in complex organizations.

## Community & Learning

- [Backstage Community](https://backstage.io/community/) -- Spotify's open-source developer portal; templates and plugins for service catalog management.
- [Model Context Protocol Specification](https://modelcontextprotocol.io/specification/) -- Official MCP specification for building agent-accessible microsite interfaces.
- [Domain-Driven Design Community](https://www.dddcommunity.org/) -- Resources on bounded contexts, domain modeling, and strategic design -- foundational to the microsite pattern.

### The Microsite Pattern Summary

| Principle | What It Means | Anti-Pattern |
|-----------|--------------|-------------|
| Domain ownership | Each microsite owns its domain end-to-end | Shared databases across services |
| Independent deploys | Deploy without coordinating with other teams | Lockstep deployment of all services |
| Shared foundation | Auth, permissions, observability centralized | Every team builds their own auth |
| Same architecture | Controller-service-repository in every microsite | Different patterns per team |
| AI agent access | DIRECT/GATEWAY/EXCLUDE tiers per endpoint | All endpoints exposed equally |
| Default invisible | New endpoints hidden from agents until reviewed | Open by default |

### What to Centralize vs Distribute

| Centralize | Distribute |
|-----------|-----------|
| Authentication & identity | Business logic |
| Permission model | Data models |
| Observability & logging | Deployment cadence |
| Infrastructure provisioning | API design (within contracts) |
| | Domain-specific testing |

### Yirifi Microsite Domains

The 15 backoffice microsites built in 3 months by just 2 people:
- DevOps, QA, Data, Marketing, Sales, Finance, Risk, Registration, and others
- Each follows: Flask backend + HTMX frontend + MCP-exposed APIs
- Same three-layer architecture (controller, service, repository) replicated across domains
- Traditional staffing for this scope: 10-15 people minimum
