# Agent Patterns

> Reference implementations for the agent architecture patterns described in [Chapter 6: Agent Architecture](../../book/part-2-building/06-agent-architecture/README.md). Each example is self-contained with its own README, dependencies, and runnable code.

All examples use the [shared provider library](../shared/README.md) for LLM access via OpenRouter.

## Patterns

| Pattern | Description | Difficulty |
|---------|-------------|------------|
| [Chat Agent](chat-agent/README.md) | Interactive conversational agent with tool use, context management, and human escalation | Intermediate |
| [Background Agent](background-agent/README.md) | Autonomous task processor with checkpointing, monitoring, and resource budgets | Intermediate |
| [Agent Hub](agent-hub/README.md) | Central orchestrator that routes requests to specialist agents via a two-model pattern | Advanced |
| [Streaming Chat](streaming-chat/README.md) | SSE streaming agent with tool calling via MCP during response generation | Advanced |

## Which Pattern to Start With

- **New to agents?** Start with [Chat Agent](chat-agent/README.md). The feedback loop is immediate and you will learn what works before automating.
- **Need autonomous processing?** Use [Background Agent](background-agent/README.md) for well-defined, repetitive tasks that run without human supervision.
- **Scaling to multiple agents?** The [Agent Hub](agent-hub/README.md) provides centralized routing, observability, and circuit breakers across specialist agents.
- **Need low-latency responses with tools?** [Streaming Chat](streaming-chat/README.md) combines token streaming with mid-response tool execution.

## Related Resources

- [Building Your First Agent](../../guides/building-your-first-agent.md) -- Step-by-step guide from design to deployment
- [Agent Failure Recovery](../../workflows/agent-failure-recovery.md) -- Workflow for diagnosing and recovering from the seven failure modes
- [Agent Design Checklist](../../checklists/agent-design-checklist.md) -- Pre-deployment checklist covering all seven failure modes
