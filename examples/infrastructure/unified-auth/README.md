# Unified Auth Example

> Companion code for **Chapter 4: Infrastructure for AI-First Operations** --- [Unified Auth for Humans AND Agents](../../../book/part-2-building/04-infrastructure-for-ai-first-operations/04-unified-auth-for-humans-and-agents.md)

A minimal implementation of unified authentication for humans and AI agents. Demonstrates the delegation model where agents inherit scoped, attenuated permissions from the human who triggered them.

## What This Demonstrates

The book's four principles of unified auth:

1. **One model, different authentication methods** --- Humans authenticate interactively (email/password here; SSO/MFA in production). Agents authenticate via delegation tokens. Both flow through the same permission model and audit system.

2. **Permissions flow down, never up** --- Every delegation hop attenuates permissions. A sub-agent can never have more access than its parent. The `PermissionSet.attenuate()` method enforces this structurally.

3. **Every action traces to a human** --- No orphan agents. The `delegation_chain` field on every `AgentIdentity` records the full path from human principal to leaf agent. The audit log captures every permission check.

4. **Tokens die with tasks** --- Agent tokens are short-lived (5 minutes by default) and bound to a specific task. When a task completes, `revoke_task()` atomically removes all downstream tokens.

**Key patterns:**
- **Three-tier access model** --- Operations classified as FREE (autonomous), SUPERVISED (human approval required), or FORBIDDEN (never automated).
- **Permission attenuation** --- Each delegation reduces permissions. `attenuate()` scopes to specific resources; `attenuate_to_read_only()` strips all write access.
- **Audit trail** --- Append-only log with full delegation chain on every entry. Query by actor, event type, or task.

## File Structure

```
unified-auth/
├── auth.py            # Main module --- single entry point for human + agent auth
├── human_auth.py      # Human user authentication (login, sessions)
├── agent_auth.py      # Agent delegation with scoped permissions
├── permissions.py     # Permission model (FREE / SUPERVISED / FORBIDDEN tiers)
├── audit.py           # Append-only audit logging for all auth events
└── requirements.txt
```

## Quick Start

```bash
# No external dependencies required
python auth.py
```

This runs a demo that walks through the full flow: human login, agent delegation, permission checks, sub-delegation with attenuation, task revocation, and audit trail output.

## Example Output

```
=== Unified Auth Demo ===

1. Alice logged in: usr-alice-001 (role=admin)
2. Delegated to agent: scheduling-agent-001
   Delegation chain: ['usr-alice-001', 'scheduling-agent-001']
3. documents:read = allowed
   documents:delete = supervised
   users:read = denied (not in scoped resources)
4. Sub-delegated to: analysis-agent-002
   Chain: ['usr-alice-001', 'scheduling-agent-001', 'analysis-agent-002']
   documents:read = allowed
   documents:update = denied (attenuated to read-only)
5. Revoked 2 token(s) for task-abc
```

## The Three-Tier Permission Model

| Tier | Behavior | Examples |
|------|----------|----------|
| FREE | Execute autonomously | Read queries, idempotent updates |
| SUPERVISED | Requires human approval | Production writes, external comms |
| FORBIDDEN | Never execute via AI | Data deletion, financial ops, audit modification |

This maps directly to the book's DIRECT / GATEWAY / EXCLUDE model from the AI Tool Gateway pattern.

## Production Notes

This example uses in-memory stores. In production:

- Replace `HumanAuth` with your identity provider (Auth0, Supabase Auth, Okta)
- Replace in-memory token stores with Redis for multi-instance deployments
- Use JWT tokens with DPoP (Demonstration of Proof-of-Possession) for agent credentials
- Write audit entries to an append-only database or object store
- Implement OAuth 2.1 Token Exchange (RFC 8693) for the delegation chain

## Related

- [AI Gateway Example](../ai-gateway/README.md) --- Gateway that uses auth middleware
- [Observability Example](../observability/README.md) --- Monitor auth events and anomalies
- [Permission Model Framework](../../../frameworks/17-permission-model-framework.md)
- [AI Governance Framework](../../../frameworks/18-ai-governance-framework.md)
