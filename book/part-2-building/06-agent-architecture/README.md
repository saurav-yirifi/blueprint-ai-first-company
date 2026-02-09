# Chapter 6: Agent Architecture — Chat, Background, and Orchestration

In February 2024, Klarna launched an AI assistant that handled 2.3 million customer conversations in its first month—two-thirds of all their support volume. Response times dropped from 11 minutes to under 2 minutes. The assistant did the equivalent work of 700 full-time employees, projecting $40 million in annual savings.

By May 2025, Klarna's CEO admitted they'd "gone too far with AI automation" and announced they were hiring humans again.

What happened? They built one type of agent and deployed it everywhere. Routine tasks—transaction tracking, simple refunds—worked beautifully. Disputes, emotional interactions, nuanced advice? Customers grew frustrated. The agent that saved millions also drove customers away.

At Yirifi, we made the same mistake earlier. Our first "universal agent" was too slow for chat (users abandoned) and too unsupervised for background work (errors accumulated for hours unnoticed). The breakthrough came when we stopped trying to build one agent for everything.

<div class="yirifi-anchor" markdown>

> "Two agent types by design: chat agents that talk to people, background agents that run while everyone sleeps. The DevOps dashboard doesn't just serve humans—agents query it for system health, deployment status, incident context. Same API, both consumers."

**Universal insight:** Every agent use case falls into one of two categories: interactive (someone is waiting) or autonomous (work happens unsupervised). Treating them as one thing leads to agents that are too slow for chat or too unsupervised for background work.

**Memorable close:** "Same API, both consumers. Different agents."

</div>

## What You'll Learn

- **[The 2 Agent Types You Need](./01-the-2-agent-types-you-need.md):** Chat vs background agents, Klarna's 2.3M monthly conversations at $40M projected savings, the 5-question decision framework, and why hybrid patterns—background agents feeding chat agents—dominate at scale.

- **[The Agent Hub Pattern](./02-the-agent-hub-pattern.md):** Centralized control, distributed execution. Replit's Temporal-based orchestration serving 30M users, production latency benchmarks (p50: 1,850ms, p95: 4,200ms), and the three implementation patterns—gateway, sidecar, or control plane.

- **[Designing Agent Interfaces](./03-designing-agent-interfaces.md):** The four requirements humans forgive but agents don't—idempotency, structured responses, explicit errors, programmatic auth. How 19 lines of fixes took AutoMCP from 76.5% to 99.9% tool call success.

- **[The 7 Failure Modes of Agents](./04-the-7-failure-modes-of-agents.md):** Air Canada's $812 chatbot liability, the Chevrolet $1 Tahoe incident, Replit's 4,000 fake records and deleted database. Microsoft's taxonomy, the four-layer resilience framework, and why 73% of teams lack cost tracking while averaging 340% overruns.

- **[When NOT to Use Agents](./05-when-not-to-use-agents.md):** Why 42% of companies abandoned AI initiatives in 2024 and 46% scrapped proof-of-concepts. The $4.2M Fortune 500 support agent failure, the 5-question framework, and the ROI math that actually works.

- **[Agent Design Patterns](./06-agent-design-patterns.md):** Intercom's journey from 25% to 66% resolution rate, the clarify-confirm-act pattern for chat, the dead man's switch for background agents, and the handoff paradox—why offering escalation too readily kills resolution rates.

---

## The Real Question

Chapter 5 showed you how to build with AI. This chapter is about when AI should build for you—and when it shouldn't.

For startups, agents offer leverage that was impossible five years ago. One well-designed background agent can do overnight what a team of analysts did in a week. Start with the 5-question framework: if your task requires reasoning, varies significantly, scales to justify overhead, tolerates occasional errors, and follows a stable process—build an agent.

For established organizations, the path requires more caution. Your existing systems weren't designed for agent consumption. Start with the Agent Hub pattern to get visibility before you scale. Design your APIs for agents first—humans will thank you too. And remember: 42% of companies abandoned AI initiatives last year. The winners weren't the fastest adopters. They were the ones who knew when not to use agents.

The question isn't whether to adopt agents. It's which type, for which tasks, with what safeguards.

Let's find out.

---

[Part Overview](../README.md) | [Book Contents](../../README.md)
