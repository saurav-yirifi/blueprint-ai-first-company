# Agent System Prompts

> Complete system prompts for building AI agents. Each prompt includes role definition, constraints, tool access, and escalation rules -- the elements discussed in [Chapter 6: Agent Architecture](../../../book/part-2-building/06-agent-architecture/README.md).

## Prompts in This Collection

| Agent Type | Description | Agent Category | Related Chapter Section |
|-----------|-------------|---------------|------------------------|
| [Customer Support Agent](customer-support-agent.md) | Handles customer inquiries with escalation to humans | Chat Agent | [The 2 Agent Types](../../../book/part-2-building/06-agent-architecture/01-the-2-agent-types-you-need.md) |
| [Data Analyst Agent](data-analyst-agent.md) | Analyzes data and generates reports autonomously | Background Agent | [Agent Design Patterns](../../../book/part-2-building/06-agent-architecture/06-agent-design-patterns.md) |
| [Code Review Agent](code-review-agent.md) | Reviews pull requests for quality and security | Background Agent | [The 8 Patterns](../../../book/part-2-building/05-building-with-ai/04-the-8-patterns-for-effective-ai-coding.md) |
| [Research Agent](research-agent.md) | Gathers and synthesizes information from multiple sources | Background Agent | [Designing Agent Interfaces](../../../book/part-2-building/06-agent-architecture/03-designing-agent-interfaces.md) |

## System Prompt Structure

Every system prompt in this collection follows the same structure:

1. **Role** -- who the agent is and what it does
2. **Capabilities** -- what the agent can do (tools, data access)
3. **Constraints** -- what the agent must not do (safety, scope)
4. **Behavior Rules** -- how the agent should respond in specific situations
5. **Escalation Rules** -- when and how to hand off to humans
6. **Output Format** -- how to structure responses

This structure maps to the four requirements from Chapter 6 that humans forgive but agents don't: idempotency, structured responses, explicit errors, and programmatic auth.

## Chat Agent vs Background Agent

These prompts fall into two categories matching the [two agent types](../../../book/part-2-building/06-agent-architecture/01-the-2-agent-types-you-need.md) covered in the book:

**Chat Agents** (someone is waiting):
- Optimized for response time and user experience
- Include escalation rules for human handoff
- Handle ambiguity through clarifying questions
- Customer Support Agent is a chat agent

**Background Agents** (work happens unsupervised):
- Optimized for accuracy and completeness
- Include checkpointing and error recovery
- Report results asynchronously
- Data Analyst, Code Review, and Research agents are background agents

## How to Use These Prompts

1. Copy the system prompt for the agent type you need
2. Replace placeholders (marked with `{BRACKETS}`) with your specific details
3. Add domain-specific constraints for your use case
4. Test with representative scenarios before deploying
5. Monitor and refine based on real-world behavior

The prompts are starting points. Every production agent needs customization for its specific domain, company policies, and user expectations.

## Related Resources

- [Coding Prompts](../coding-prompts/README.md) -- prompts for development tasks
- [Evaluation Prompts](../evaluation-prompts/README.md) -- prompts for evaluating agent output quality
- [7 Failure Modes of Agents Framework](../../../frameworks/10-seven-failure-modes-of-agents.md) -- what can go wrong
- [Permission Model Framework](../../../frameworks/17-permission-model-framework.md) -- setting autonomy levels
