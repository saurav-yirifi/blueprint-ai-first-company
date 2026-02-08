# Designing Agent Interfaces

What agents need that humans don't.

<div class="yirifi-anchor" markdown>

> "If an API works for agents, it works for humans. The reverse isn't true."

At Yirifi, we built APIs for human consumption—interactive forms, session-based auth, error messages for modal dialogs. Then we added agents. They broke immediately. Every shortcut surfaced as a broken agent. Implicit session state? Agents lost track. HTML error pages? Agents couldn't parse. Undocumented rate limits? Agents hammered endpoints until blocked.

When we redesigned with agents as the primary consumer, both agents and humans benefited. The structured errors agents needed made debugging easier for developers. The idempotency that prevented duplicate agent actions saved users from accidental double-clicks. Agent-friendly design includes everything human-friendly design needs, plus more—agents expose every UX problem your APIs have.

</div>

### The Four Requirements Humans Forgive But Agents Don't

Agent-callable APIs need four things that human-focused APIs routinely skip: idempotency, structured responses, explicit error handling, and programmatic authentication.

**Idempotency** matters because agents retry on failure. Network timeout during payment? Duplicate charge. Stripe extended idempotency key validity from 24 hours to 30 days in their v2 API specifically for long-running agent workflows[^stripe-v2].

**Structured responses** mean JSON with consistent schemas, not HTML pages or free-form text. Error responses need codes and context, not just HTTP status and a human-readable message. An agent can act on `{"error": {"code": "RATE_LIMIT_EXCEEDED", "retry_after_seconds": 60}}`. It can't act on a 429 status code alone.

**Explicit error handling** goes beyond "something went wrong." At Yirifi, we added three fields to every error response—a machine-readable code, a human-readable message, and a suggested action. That third field made agent reliability jump overnight.

**Programmatic authentication** eliminates interactive flows. Agents can't click through OAuth consent screens or solve CAPTCHAs. They need API keys, service account credentials, or tokens with automatic refresh. The authentication should be stateless—no session cookies, no implicit browser state, no assumptions about a persistent connection.

### What Breaks Agents in Production

The research project AutoMCP demonstrated how small details compound. When researchers converted REST APIs to agent-callable MCP servers, only 76.5% of tool calls succeeded initially[^automcp]. After fixing five recurring patterns—incorrect security schemes, malformed base URLs, undocumented headers, type mismatches, missing auth—success rates jumped to 99.9%. The fixes averaged 19 lines of changes per API.

Session timeouts designed for eight-hour business days interrupt AI workflows running overnight. Rate limiting built for human click speeds blocks machine-speed requests as "suspicious activity"—companies scaling to 100+ agents report false positive security alerts flooding their systems[^prefactor]. The fix: task-based session management and machine-scale rate limits with baseline learning.

CAPTCHAs present a surprising failure mode. Modern AI agents can often solve static challenges, creating cat-and-mouse games rather than real security. One e-commerce company saw SMS costs hit $2,800 per hour from CAPTCHA harvesting attacks lasting ten days[^geetest]. The better approach: cryptographic verification of bot identity.

A painful security example: a startup's ChatGPT-based agent implementing OAuth used a deprecated library with known vulnerabilities, ignored mandatory security parameters, and produced code that let attackers forge tokens within two weeks. Five thousand user records accessed, $200,000 spent on investigation and patches[^oauth-incident]. Agents writing security-critical code need human review—always.

### MCP: The Emerging Standard

Model Context Protocol emerged from Anthropic in November 2024 as a standardization layer for agent-tool connections[^mcp]. The protocol defines three primitives: tools (callable functions), resources (data sources), and prompts (pre-built templates).

The value is interoperability. Before MCP, every agent-tool connection required custom integration. At Yirifi, our microsites expose MCP-compatible interfaces alongside REST APIs—when new agent frameworks emerge, we're ready. Within six months, over 22,000 GitHub repositories were created for MCP implementations[^automcp]. MCP isn't universal yet, but betting against standardization rarely pays off.

### The Practical Playbook

The agent-readiness checklist: Can agents authenticate without human interaction? Does every endpoint return structured JSON? Are error responses machine-parseable with actionable codes? Do state-changing operations support idempotency keys? Are rate limits documented with retry-after headers? Every "no" is your next fix.

At Yirifi, every microsite has one API serving both UI and agents. The UI is a thin client consuming the same endpoints agents use. This isn't elegance—it's pragmatism. When agents have full API access, you can automate anything the UI can do. When the UI has special endpoints, agents become second-class citizens.

The security model is evolving. AWS launched Web Bot Auth in 2025, providing cryptographic identities for AI agents verifiable without CAPTCHAs[^aws-webbot]. DataDome reports LLM crawlers now represent 4.5% of all legitimate bot traffic—976 million OpenAI crawler requests in a single 30-day period[^datadome]. The answer isn't blocking bots—it's granting configurable access based on verified identity.

Build for agents first. Humans will thank you too.

## References

[^stripe-v2]: Stripe. [API v2 Overview](https://docs.stripe.com/api-v2-overview)

[^automcp]: AutoMCP: Automatic MCP Server Generation from OpenAPI Specifications. [arXiv](https://arxiv.org/html/2507.16044v1)

[^prefactor]: 7 Authentication Problems Deploying AI Agents at Scale. [Prefactor](https://prefactor.tech/blog/7-authentication-problems-deploying-ai-agents-at-scale)

[^oauth-incident]: Jakarta Agents: Betrayal of Silicon. [JVM Weekly](https://www.jvm-weekly.com/p/jakarta-agents-betrayal-of-silicon)

[^geetest]: AI Agent Cybersecurity Threats. [GeeTest](https://www.geetest.com/en/article/ai-agent-cybersecurity-threats)

[^mcp]: Introducing the Model Context Protocol. [Anthropic](https://www.anthropic.com/news/model-context-protocol)

[^aws-webbot]: Reduce CAPTCHAs for AI Agents Browsing the Web with Web Bot Auth. [AWS Machine Learning Blog](https://aws.amazon.com/blogs/machine-learning/reduce-captchas-for-ai-agents-browsing-the-web-with-web-bot-auth-preview-in-amazon-bedrock-agentcore-browser/)

[^datadome]: AI Agents and LLM Crawlers. [DataDome Threat Research](https://datadome.co/threat-research/ai-agents-llm-crawlers/)

---

[← Previous: The Agent Hub Pattern](./02-the-agent-hub-pattern.md) | [Chapter Overview](./README.md) | [Next: The 7 Failure Modes of Agents →](./04-the-7-failure-modes-of-agents.md)
