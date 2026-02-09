# Inter-Microsite Communication

Your microsites don't exist in isolation. Finance needs data from Sales. DevOps triggers deployments that affect QA. AI agents orchestrate workflows spanning multiple domains. How these communications happen determines whether your architecture remains flexible or becomes a distributed monolith—services that must deploy together despite living in separate repositories, giving you all the complexity of microservices with none of the benefits.

The common mistake: picking one communication pattern and applying it everywhere. I've seen a payments company bring down their entire checkout flow because they made inventory checks synchronous—one slow database query cascaded into a fifteen-minute outage. Both all-sync and all-async approaches fail because different use cases have fundamentally different requirements.

## The Coupling Tradeoff

Every communication pattern creates coupling. The question is which kind you can tolerate.

**Synchronous creates temporal coupling.** When Service A calls Service B directly, both must be available simultaneously. Chain three services together, and your reliability is the product of all three. One slow service makes everything slow. One failed service makes everything fail.

**Asynchronous creates consistency challenges.** After publishing an event, different services have inconsistent views of system state until propagation completes. If a workflow fails midway, you need compensating transactions. Events may arrive out of order. Without idempotency, duplicate events corrupt state.

There's no coupling-free option. Choose the coupling that matches your requirements.

## Sync vs. Async Decision Framework

| Pattern | When to Use | Trade-off |
|---------|-------------|-----------|
| **Sync API calls** | User waiting for feedback, simple operations | Caller blocks; cascading failures |
| **Async events** | Background operations, multi-consumer workflows | Eventually consistent; harder to debug |
| **Shared data** | Analytics, reporting, aggregation | Governance overhead; hidden dependencies |
| **Agent-to-agent** | Cross-domain AI automation | Flexible but requires AI access controls |

**Use synchronous** when the user is waiting for feedback, the operation is simple, and failure should be visible immediately. The user clicks "submit order"—they need to know whether it succeeded.

**Use asynchronous** when operations happen outside the core user flow, services need to operate independently, and you require high scalability and fault tolerance.

Netflix demonstrates the async approach at scale. They process billions of events daily through Kafka. User actions become events consumed by recommendation engines, analytics pipelines, and monitoring systems. Multiple services react to the same event without knowing about each other[^netflix-kafka]. When the recommendation engine goes down, users can still watch videos. Each service operates in its own failure domain.

## Choreography vs. Orchestration

Two models for coordinating multi-step workflows across domains.

**Choreography** uses event-driven communication where services react autonomously. Each service publishes events about what happened ("Order Placed") without dictating what should happen next. Like dancers who know their roles without a choreographer[^serverside].

Pros: Loose coupling. Services evolve independently. No single point of failure.
Cons: Troubleshooting is difficult. Event chains are invisible.

**Orchestration** uses a central coordinator that explicitly directs interactions. The orchestrator sends commands ("Check Inventory," "Process Payment") and manages the overall workflow[^serverside].

Pros: Visibility. Easier troubleshooting. The workflow is explicit and traceable.
Cons: Creates a potential single point of failure. The orchestrator becomes a bottleneck.

The practical approach: use orchestration within a bounded context where services require specific execution order. Use choreography across contexts when events leave the domain.

A Sales workflow might orchestrate steps like "validate order," "check inventory," "process payment." But when the order is complete, it publishes an event that Marketing, Finance, and Support consume independently. Central control where you need it. Loose coupling where you don't.

## Permission-Aware Navigation

When users navigate between microsites, permissions must be respected automatically. Before rendering a link to another microsite, check if the user has access. If not accessible, don't show the link. Don't show a link that returns 403 when clicked.

The centralized permission service provides a bulk-check API. One call returns all permission results for a user across every microsite. The UI renders only accessible links. No code changes per microsite. No per-link permission logic scattered across your frontend.

This extends to AI agents. When an agent requests cross-domain data, the permission check happens before the call. The agent receives only what it's authorized to access. No mix of data and errors.

## Practical Guidance

**For startups:** Start with synchronous calls. They're simpler to debug, simpler to reason about, simpler to implement. When you hit scale problems—when a single service failure cascades across your system, when you need multiple consumers for the same events—then introduce async. Don't add complexity before you need it.

**For established organizations:** You likely have a mix already. The work is making it intentional. Map your current communication patterns. Identify where synchronous chains create brittleness. Identify where eventual consistency causes business problems. Match patterns to requirements, service by service.

## References

[^netflix-kafka]: LinkedIn. [How Apache Kafka Powers Real World Systems at Netflix and Uber](https://www.linkedin.com/pulse/how-apache-kafka-powers-real-world-inside-netflix-uber-abel-mendon%C3%A7a-nttre)

[^serverside]: TheServerSide. [Synchronous vs Asynchronous Microservices Communication Patterns](https://www.theserverside.com/answer/Synchronous-vs-asynchronous-microservices-communication-patterns)

---

[← Previous: Microsite Orchestration](./06-microsite-orchestration.md) | [Chapter Overview](./README.md) | [Next: Governance Patterns →](./08-governance-patterns.md)
