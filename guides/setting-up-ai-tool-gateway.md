# Guide: Setting Up an AI Tool Gateway

> A step-by-step guide to building the infrastructure layer between your AI agents and the tools they call -- routing, authentication, cost tracking, and security enforcement in one place.

*Based on [Chapter 4: Infrastructure for AI-First Operations](../book/part-2-building/04-infrastructure-for-ai-first-operations/README.md)*

---

## What You'll Build

By the end of this guide, you will have an AI Tool Gateway that:

- Routes agent requests to backend tools and APIs through a single controlled endpoint
- Enforces a three-tier permission model (free, supervised, forbidden) for every tool call
- Authenticates agents using delegation tokens that trace back to human principals
- Tracks costs per agent, per task, and per tool call
- Provides a kill switch for any agent or tool connection
- Logs every interaction for audit and debugging

The gateway sits between your agents and everything they touch. Without it, you are managing permissions, logging, and security per agent. With it, you manage them once.

## Prerequisites

Before starting, you should have:

- **At least one deployed agent** (or a clear plan for one). Building a gateway before you have agents is premature optimization. Building agents without a gateway is a security risk.
- **An identity provider.** Supabase Auth, Auth0, Okta, or equivalent. Your agents need identities, not just API keys.
- **Backend APIs or tools your agents will call.** REST APIs, MCP servers, database connections -- the gateway needs something to protect.
- **Basic infrastructure.** A place to deploy the gateway (any server, container, or serverless function) with network access to your agents and backend tools.

---

## Step 1: Understand the Gateway Architecture

An AI Tool Gateway is an API gateway for the agentic era. It handles three responsibilities that become unmanageable when distributed across individual agents: access control (which agents call which tools), observability (what happened, at what cost), and safety enforcement (rate limiting, circuit breakers, kill switches).

The gateway sits between your agents and your tools. Every tool call flows through it. It adds policy to the data path without owning the logic.

## Step 2: Classify Your Tools into Three Tiers

Before writing configuration, classify every tool your agents can access. This is the most important step -- get it wrong and your gateway either blocks legitimate work or allows dangerous operations.

**Free tier (DIRECT).** Operations that execute autonomously with no approval required.

- Read-only queries: fetching user profiles, listing records, checking status
- Idempotent updates: setting a preference, updating a timestamp
- Reversible changes: anything you can undo with a single operation

Expose these as individual, directly-callable tools. The agent calls `get_user_profile` or `list_orders` without any gate.

**Supervised tier (GATEWAY).** Operations requiring human-in-the-loop approval or elevated intentionality: write operations on production data, external communications, bulk operations.

Wrap these behind a single gateway tool that forces the agent to name the service and operation explicitly. The agent calls `billing_api_call(operation="create_refund", params={...})` rather than a convenient shortcut. This intentionality forcing makes the agent be explicit about what it is doing with production data.

**Forbidden tier (EXCLUDE).** Operations that never appear in the tool list, period.

- Data deletion: DELETE endpoints, DROP TABLE, purge operations
- Financial disbursements: direct payment execution, fund transfers
- Access control changes: modifying permissions, creating admin accounts
- Audit log modifications: anything that tampers with the record of what happened
- Internal infrastructure: health checks, metrics endpoints, debug interfaces

These endpoints are hidden from the agent entirely. They don't appear in tool discovery, tool listings, or documentation the agent can access.

**Decision:** Create a spreadsheet or table with four columns: Tool Name, Tier, Justification, Review Date. Every tool gets a tier. Every tier gets a justification. Review quarterly.

## Step 3: Set Up Authentication and Delegation

Agents need identities, not shared API keys. A shared key tells you "an agent called this tool." A proper identity tells you "this specific agent, acting on behalf of this specific user, called this tool for this specific task."

**Register each agent as an identity** in your identity provider. Microsoft Entra Agent ID, Auth0 for AI Agents, or your existing IAM system with agent-specific flows. Each agent gets its own credentials, permission set, and audit trail.

**Implement delegation tokens.** When a user triggers an agent, the agent receives a scoped token -- not the user's full permissions, only what the task requires. The token includes an `act` claim recording the delegation chain: "Agent B acting for Agent A acting for Alice."

**Enforce permission attenuation.** Permissions can only decrease as delegation depth increases. If Agent A spawns Agent B, Agent B gets the same or fewer permissions -- never more.

**Set token expiration.** Tokens die with tasks. When a task completes, all associated tokens expire. This prevents stale permissions from becoming security risks.

**Decision:** Choose your identity provider and configure agent-specific identity types.

## Step 4: Configure Routing and Rate Limiting

The gateway routes requests to the right backend and prevents any single agent from consuming excessive resources.

**Route configuration.** Map each tool to its backend endpoint. For MCP-compatible tools, the gateway aggregates multiple backend servers into a unified tool set. For REST APIs, it proxies requests with added headers (authentication, request IDs, tier classification).

**Rate limiting.** Set per-agent limits based on usage patterns -- background agents processing overnight batches need different limits than chat agents handling user queries. Set per-tool limits based on cost -- expensive tools get tighter caps. Start conservative and relax based on observed behavior.

**Cost budgets.** Track cumulative cost across all tool calls within a task. At 80% of budget, log a warning. At 100%, terminate with a clear explanation. Enterprise teams report cost overruns averaging 340% without enforcement.

**Circuit breakers.** If a backend tool fails three consecutive times, stop routing to it until it recovers.

## Step 5: Build the Observability Layer

You can't secure what you can't see. The gateway's position in the data path makes it the ideal place to capture everything.

**Log every request.** For each tool call, log: timestamp, agent identity, delegating user, tool name, tier, input parameters (sanitized of secrets), output summary, latency, cost, and success/failure status.

**Correlate by task.** Every request gets a task ID linking all tool calls within a single agent task. When debugging, pull the task ID and see the complete sequence.

**Track cost in real time.** Aggregate costs by agent, user, task, and day. Surface top cost drivers in a dashboard.

**Alert on anomalies.** Set alerts for unusual request volume, cost spikes above baseline, repeated failures on the same tool, and requests outside normal operating hours. Per-action policy checks add less than 12 milliseconds of latency -- invisible compared to LLM inference time.

## Step 6: Add the Kill Switch

When something goes wrong at 2 AM, you need one button that stops the damage.

**Per-agent kill switch.** Instantly revoke all tokens for a specific agent. Every subsequent request is rejected. The agent sees a clear "agent suspended" error, not a cryptic timeout.

**Per-tool kill switch.** Disable a specific tool across all agents. If a backend is compromised or misbehaving, shut off access without touching individual agent configurations.

**Global pause.** Stop all agent-to-tool traffic through the gateway. Nuclear option, but necessary for severe incidents. Resume requires explicit human action.

**Latency requirement.** Kill switch activation must take effect in seconds, not minutes. If your revocation latency is measured in minutes, it is incident response, not security.

## Step 7: Test the Gateway

Before routing production agent traffic through the gateway, verify each layer.

1. **Permission test.** Attempt to call a forbidden-tier tool through the gateway. Confirm it is rejected.
2. **Tier enforcement test.** Attempt a supervised-tier operation without the required approval flow. Confirm it blocks.
3. **Delegation test.** Trigger an agent as a user with limited permissions. Confirm the agent can't exceed those permissions.
4. **Rate limit test.** Send requests above the configured rate. Confirm throttling engages.
5. **Cost budget test.** Run a task designed to exceed its cost budget. Confirm termination at the budget limit.
6. **Circuit breaker test.** Break a backend tool. Confirm the circuit breaker opens and the gateway stops routing.
7. **Kill switch test.** Activate the kill switch for one agent. Confirm immediate effect. Deactivate and confirm recovery.

---

## Key Decisions Summary

| Decision | Where | Output |
|----------|-------|--------|
| Tool tier classification | Step 2 | Every tool assigned free, supervised, or forbidden |
| Identity approach | Step 3 | Agent identity provider and delegation pattern |
| Rate and cost limits | Step 4 | Per-agent and per-tool limits with budgets |
| Observability scope | Step 5 | What to log, how to correlate, what to alert on |
| Kill switch design | Step 6 | Per-agent, per-tool, and global controls |

## Related Resources

- [AI Gateway Example](../examples/infrastructure/ai-gateway/) -- Reference implementation of the gateway pattern
- [Infrastructure Audit Checklist](../checklists/infrastructure-audit.md) -- Pre-deployment infrastructure review
- [5 Infrastructure Mistakes](../frameworks/5-infrastructure-mistakes.md) -- Common infrastructure failures to avoid
- [Unified Auth Pattern](../examples/infrastructure/unified-auth/) -- Detailed auth implementation examples
