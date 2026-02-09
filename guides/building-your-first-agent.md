# Guide: Building Your First AI Agent

> A step-by-step guide to designing, building, and deploying your first AI agent -- from choosing the right type to handling failures in production.

*Based on [Chapter 6: Agent Architecture](../book/part-2-building/06-agent-architecture/README.md)*

---

## What You'll Build

By the end of this guide, you will have designed and deployed a single AI agent that:

- Solves a specific, well-scoped task for your team or customers
- Has defined tool access with appropriate permission tiers
- Handles failures gracefully instead of silently breaking
- Produces an audit trail you can review after the fact
- Connects to your existing systems through structured interfaces

This guide covers the decisions and implementation steps for one agent. Scaling to multiple agents requires the Agent Hub pattern -- covered separately.

## Prerequisites

Before starting, you should have:

- **A clear task in mind.** An agent needs a job. If you can't describe the task in one sentence, scope it further before proceeding.
- **API access to an LLM provider.** OpenAI, Anthropic, or your provider of choice. Direct API access, not just a chat interface.
- **At least one tool or API the agent will call.** Agents without tools are just chatbots. The value comes from connecting reasoning to action.
- **Basic observability.** Structured logging at minimum. You need to see what the agent did after the fact.

---

## Step 1: Choose Your Agent Type

Every agent use case falls into one of two categories. Getting this wrong means building an agent that is too slow for one job and too unreliable for the other.

**Chat agents** talk to people. Someone is waiting. Speed matters. The agent must respond in seconds, handle ambiguity through clarification, and hand off to humans when stuck. Use a chat agent when:

- The task requires human judgment or has ambiguous requirements
- Someone is waiting for the result in real time
- The domain involves emotional, nuanced, or disputed situations

**Background agents** work while everyone sleeps. No one is watching. They are triggered by schedules, events, or API calls. Use a background agent when:

- The task is well-defined and repetitive
- Processing volume demands scale beyond interactive interfaces
- Results are needed eventually, not immediately

**The hybrid pattern** combines both. Background agents handle monitoring, processing, and analysis. Chat agents surface results when humans ask. Klarna's AI assistant handled 2.3 million conversations in its first month because background agents pre-processed data that chat agents delivered instantly.

**Decision:** Write down which type you are building and why. If you can't decide, start with a chat agent -- the feedback loop is faster and you will learn what works before automating.

## Step 2: Define the Agent's Tools

Tools are the actions your agent can take beyond generating text. Without tools, you have a chatbot. With tools, you have an agent.

For each tool, define:

1. **Name and description.** The agent uses the description to decide when to call the tool. Make it precise. "Search the customer database by email address" beats "look up customers."
2. **Input schema.** What parameters does the tool accept? Define types, required fields, and validation rules. Agents will pass malformed inputs if you let them.
3. **Output schema.** What does the tool return? Use structured JSON with consistent fields. Include explicit error codes, not just status messages.
4. **Permission tier.** Classify every tool as free (executes without approval), supervised (requires human confirmation), or forbidden (never executes via agent).

Start small. Two to four tools for your first agent. Research on MCP server conversions found that fixing five recurring patterns -- incorrect security schemes, malformed URLs, undocumented headers, type mismatches, missing auth -- took tool call success rates from 76.5% to 99.9%. The fixes averaged 19 lines of changes per API.

**Decision:** List your tools, their schemas, and their permission tiers. If any tool can delete data or send external communications, it must be supervised or forbidden for your first agent.

## Step 3: Set Permissions and Guardrails

Agents act autonomously. Without guardrails, they act wrong autonomously.

**Define "done when" criteria.** Every agent task needs an explicit completion condition. "Help the user with their question" isn't a completion condition. "Resolve the user's billing inquiry or escalate to a human within 3 exchanges" is.

**Set iteration limits.** Maximum 10 retries on any single operation. Maximum 5-minute timeout on any single task. Alert after 3 iterations without progress. These defaults come from production experience -- adjust based on your use case, but start here.

**Set token budgets.** Assign a maximum token spend per task. Alert at 80% consumption. Terminate at 100% with a clear explanation. Enterprise teams report agent cost overruns averaging 340% above estimates. Budget enforcement isn't optional.

**Define escalation criteria.** When does the agent stop trying and ask for help? For chat agents: after two failed attempts at the same sub-task, surface the issue to the user. For background agents: after three failures, pause the task and alert an operator.

**Decision:** Write your "done when" criteria, iteration limits, token budget, and escalation rules. These go into your agent's configuration, not just documentation.

## Step 4: Handle Failures By Design

Agents fail differently than traditional software. Plan for seven specific failure modes:

1. **Hallucinated actions** -- the agent calls tools that don't exist. Mitigation: validate every tool call against your registry before execution.
2. **Infinite loops** -- the agent retries endlessly. Mitigation: iteration counts and timeouts from Step 3.
3. **Scope creep** -- the agent interprets instructions too broadly. Mitigation: "done when" criteria and permission tiers.
4. **Context loss** -- the agent forgets what happened earlier. Mitigation: summarize context every 10 turns for chat agents; checkpoint state for background agents.
5. **Cascading failures** -- one failure triggers others. Mitigation: isolate your agent from other systems with circuit breakers.
6. **Resource exhaustion** -- the agent burns through tokens or compute. Mitigation: budgets and alerts from Step 3.
7. **Stale data** -- the agent acts on outdated information. Mitigation: check data freshness before acting.

For your first agent, focus on the modes that match your agent type. Chat agents are most vulnerable to hallucinated actions, scope creep, and context loss. Background agents are most vulnerable to infinite loops, cascading failures, and resource exhaustion.

**Decision:** Identify your top three failure risks and confirm you have a mitigation for each before writing code.

## Step 5: Build the Agent

With decisions from Steps 1-4 documented, implementation becomes straightforward.

**For chat agents:** Initialize with a system prompt covering the task description, "done when" criteria, available tools, and escalation instructions. Implement the clarify-confirm-act pattern: ask for clarification when ambiguous, confirm before high-risk actions. Add graceful handoff with full context when the agent can't resolve within escalation criteria.

**For background agents:** Initialize with a task definition, input parameters, and success criteria. Implement idempotency so running the same task twice never creates duplicates. Add checkpointing to resume from interruption. Build a dead man's switch: if the agent doesn't report healthy within the expected timeframe, assume failure and alert an operator.

## Step 6: Test Before Deploying

Test the failure paths, not just the happy path.

1. **Golden path test.** Confirm the agent completes a straightforward version of its task correctly.
2. **Ambiguity test.** Give a vague request. The agent should clarify (chat) or fail gracefully (background), not guess.
3. **Adversarial test.** Try to make the agent act outside its scope. Confirm permission tiers hold.
4. **Failure test.** Break a tool the agent depends on. Confirm it retries appropriately and escalates.
5. **Cost test.** Measure token consumption on a realistic workload against your budget.

## Step 7: Deploy and Monitor

Deploy with monitoring from day one. Not "add monitoring later." Day one.

- **Detection dashboards** for each failure mode you identified in Step 4
- **Cost tracking** per task and per day
- **Latency tracking** for chat agents (users abandon after seconds)
- **Success/failure rates** with breakdowns by failure mode
- **Audit logs** for every tool call, every decision, every output

Review the first 100 agent interactions manually. You will find failure patterns you didn't anticipate. Add them to your test suite and your monitoring.

---

## Key Decisions Summary

| Decision | Where | Output |
|----------|-------|--------|
| Agent type | Step 1 | Chat, background, or hybrid |
| Tool inventory | Step 2 | List of tools with schemas and permission tiers |
| Guardrails | Step 3 | Done-when criteria, limits, budgets, escalation rules |
| Failure priorities | Step 4 | Top 3 failure risks with mitigations |
| Architecture pattern | Step 5 | Clarify-confirm-act (chat) or idempotent-checkpoint (background) |

## Related Resources

- [Agent Patterns Examples](../examples/agent-patterns/README.md) -- Reference implementations for chat agents, background agents, and agent hubs
- [Agent Design Checklist](../checklists/agent-design-checklist.md) -- Pre-deployment checklist covering all seven failure modes
- [7 Failure Modes of Agents](../frameworks/10-seven-failure-modes-of-agents.md) -- Deep dive on each failure mode with real-world incidents
- [Permission Model Framework](../frameworks/17-permission-model-framework.md) -- How to calibrate agent autonomy across the permission spectrum
