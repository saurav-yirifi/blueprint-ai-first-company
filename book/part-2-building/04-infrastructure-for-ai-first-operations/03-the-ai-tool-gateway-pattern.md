# The AI Tool Gateway Pattern

Tiered access as architecture—safe, supervised, forbidden.

---

<div class="yirifi-anchor" markdown>

This section implements the chapter's core principle—matching autonomy to reversibility. At Yirifi, our AI Tool Gateway emerged from a practical question: AI writes to production constantly, deploying code, updating content, modifying records. What matters isn't "can AI touch production?" but "what happens if this goes wrong?"

</div>

In September 2025, an unofficial Postmark MCP server with 1,500 weekly downloads got compromised. The attackers added a single line—a hidden BCC field to the `send_email` function. Every user silently forwarded their emails to attackers without knowing it[^lasso-security]. This wasn't a sophisticated zero-day exploit. It was a supply chain attack made trivial by AI agents calling tools with no central oversight.

The attack surface isn't the model—it's the thousands of tools your agents connect to.

### The Gateway Architecture

Think of an AI Tool Gateway as an API gateway for the agentic era. It sits between your AI agents and the tools they call—aggregating multiple backends behind a single endpoint while enforcing security, permissions, and audit trails.

The Model Context Protocol (MCP) emerged in late 2024 as the de facto standard for agent-tool communication[^mcp-blog]. By November 2025, Anthropic, OpenAI, Google, and Microsoft had all adopted it. Claude Code functions as both an MCP client and server—connecting to external MCP servers (databases, APIs, design tools) while exposing its own capabilities for integration into larger systems[^claude-mcp]. This dual role makes it both a consumer and provider of tools.

But the early spec had a glaring hole: no authentication. Research found over 1,800 MCP servers exposed on the public internet without any auth[^web-research]. The June and November 2025 spec updates fixed this with OAuth 2.1 and enterprise-grade security controls—but protocol compliance doesn't guarantee implementation. You need a gateway that enforces policies regardless of whether each individual server implements them correctly.

Lasso Security launched the first open-source MCP security gateway in April 2025[^lasso-release]. It functions as a proxy and orchestrator, embedding security filters that work across all connected servers. Even if a backend server lacks native privacy controls, the gateway catches sensitive data before it reaches your agents.

### The Three-Tier Access Model

The most practical pattern for tool access control: classify operations as free, supervised, or forbidden—based on reversibility, not environment.

**Free tier** operations execute autonomously. Read-only queries, idempotent updates, reversible configuration changes. If an AI agent gets it wrong, you roll it back. Low risk, full autonomy.

**Supervised tier** requires human-in-the-loop approval. Production deploys, bulk data modifications, external communications. The agent proposes the action with full context; a human approves or rejects. This isn't about distrust—it's about proportioning autonomy to risk.

**Forbidden tier** operations never execute via AI, period. User data deletion, financial disbursements, access control changes, audit log modifications. Some actions are simply too irreversible—or carry too much regulatory weight—to automate.

At Yirifi, our MCP hub implements this through explicit tier assignment. We call it DIRECT, GATEWAY, and EXCLUDE. DIRECT exposes safe operations—`get_user_list`, `get_country`—as individual MCP tools that agents can call freely. GATEWAY wraps dangerous operations—`delete_user`, `bulk_update`—requiring the agent to explicitly name the service and operation via a single `{service}_api_call` tool. This isn't just access control; it's intentionality forcing. The agent must be explicit about what it's doing with production data. EXCLUDE hides internal endpoints like `/health` and `/metrics` entirely—they never appear in the tool list.

### When It Goes Wrong

Let's be honest about what's at stake. In 2024-2025, 73% of enterprises experienced at least one AI-related security breach, with an average cost of $4.8 million per incident[^security-incidents]. Thirty-five percent of incidents came from prompt injection attacks[^security-incidents].

The most alarming discovery was CVE-2025-32711, dubbed "EchoLeak"—the first documented zero-click attack on an AI agent[^echoleak]. Attackers sent malicious emails to Microsoft 365 Copilot users containing hidden prompt injection payloads. No user interaction required. Copilot's RAG system automatically triggered exfiltration of sensitive data to attacker-controlled endpoints. This is what happens without gateway-level controls.

### The x-authorized-tools Pattern

The most elegant enforcement mechanism uses cryptographically signed JWT "wristbands" in an `x-authorized-tools` header[^redhat-mcp]:

1. User authenticates against your identity provider
2. An authorization component creates a signed JWT mapping which tools that user can access
3. This JWT travels with every request as the `x-authorized-tools` header
4. The gateway validates the JWT signature and filters the tool list before returning results

The wristband contains something like `{"server1.mcp.local":["greet","time"], "server2.mcp.local":["headers"]}`. Every tool invocation gets checked against this map. If the user doesn't have the role for that specific tool, the call never reaches the backend. Because the JWT is cryptographically signed, tampering attempts get caught immediately.

### Performance Reality

Access control adds latency—but how much? Per-action policy checks add less than 12 milliseconds. RBAC-enhanced systems block up to 98% of unauthorized and prompt-injected calls with throughput overhead of only 12%[^performance].

For most enterprise workloads, this overhead is invisible. Your AI agents aren't making thousands of tool calls per second—they're making dozens per minute. The bottleneck is never the access control layer; it's the LLM inference that takes seconds per turn.

The tiers aren't static. Operations can earn autonomy over time. Zero incidents and high approval rates suggest moving an operation to a lower tier. Frequent rejections signal the opposite. The goal isn't rigid rules—it's a feedback loop where the system learns what deserves trust.

### Headless Mode: Gateways for Automation

Claude Code's headless mode (`-p` flag) enables non-interactive automation that respects these same gateway patterns: CI pipelines, pre-commit hooks, large-scale migrations[^headless-mode]. The agent runs without human supervision—making gateway controls even more critical.

The fan-out pattern handles migrations at scale: loop through thousands of files, call Claude programmatically for each, constrain which tools the agent can use. GitHub Actions integration lets you mention `@claude` in any PR or issue to trigger AI analysis—but that analysis flows through whatever gateway controls you've established[^claude-action]. Automation without access control is a breach waiting to happen.

We'll explore how these gateway patterns integrate with agent architecture in [Chapter 6](../06-agent-architecture/README.md).

This isn't optional infrastructure. It's the difference between AI agents that work safely at scale and AI agents that become your largest attack surface.

---

## References

[^lasso-security]: Lasso Security — [MintMCP Analysis](https://www.mintmcp.com/blog/lasso-security-with-mcp)

[^mcp-blog]: MCP First Anniversary — [blog.modelcontextprotocol.io](https://blog.modelcontextprotocol.io/posts/2025-11-25-first-mcp-anniversary/)

[^web-research]: MCP Authorization Specification — [modelcontextprotocol.io](https://modelcontextprotocol.io/specification/draft/basic/authorization)

[^lasso-release]: Lasso Security Press Release — [BusinessWire](https://www.businesswire.com/news/home/20250417840621/en/Lasso-Releases-First-Open-Source-Security-Gateway-for-MCP)

[^security-incidents]: Adversa AI 2025 Security Report — [PRNewswire](https://www.prnewswire.com/news-releases/adversa-ai-unveils-explosive-2025-ai-security-incidents-reportrevealing-how-generative-and-agentic-ai-are-already-under-attack-302517767.html)

[^echoleak]: AI Security Incidents Analysis — [LinkedIn](https://www.linkedin.com/pulse/ai-security-major-incidents-exposing-risks-access-oliver-3hree)

[^redhat-mcp]: Red Hat MCP Gateway Authentication — [developers.redhat.com](https://developers.redhat.com/articles/2025/12/12/advanced-authentication-authorization-mcp-gateway)

[^performance]: EmergentMind Research — [Automated Permission Management for AI Agents](https://www.emergentmind.com/topics/automated-permission-management-for-ai-agents)

[^claude-mcp]: Anthropic. [Claude Code Documentation](https://code.claude.com/docs/en/overview)

[^headless-mode]: Anthropic. [Claude Code GitHub Actions](https://code.claude.com/docs/en/github-actions)

[^claude-action]: GitHub. [anthropics/claude-code-action](https://github.com/anthropics/claude-code-action)

---

[← Previous: Polyglot Persistence](./02-polyglot-persistence.md) | [Chapter Overview](./README.md) | [Next: Unified Auth for Humans AND Agents →](./04-unified-auth-for-humans-and-agents.md)
