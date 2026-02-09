# Examples

> Working examples, prompt templates, and configurations to accompany *Blueprint for an AI-First Company*. Each example is self-contained with its own README, ready to copy into your project and customize.

## Provider Setup

Most code examples use **OpenRouter** as the default LLM provider, which gives you access to models from Anthropic, Google, OpenAI, and others through a single API key.

```bash
# Get your key at https://openrouter.ai/keys
export OPENROUTER_API_KEY=sk-or-your-key-here

# Install shared dependencies
pip install httpx python-dotenv
```

The agent-pattern examples use a shared provider library at [`shared/`](shared/README.md). Copy it alongside any example you use.

## All Examples

| Example | Description | Difficulty | Related Chapter |
|---------|-------------|------------|-----------------|
| **Shared Library** | | | |
| [Shared Provider Library](shared/README.md) | LLM provider abstraction, OpenRouter/OpenAI providers, MCP client | Foundation | Ch 4: Infrastructure |
| **Agent Patterns** | | | |
| [Chat Agent](agent-patterns/chat-agent/README.md) | Interactive agent with tool calling, context management, and human escalation | Intermediate | Ch 6: Agent Architecture |
| [Background Agent](agent-patterns/background-agent/README.md) | Autonomous agent with checkpointing, error recovery, and budget tracking | Intermediate | Ch 6: Agent Architecture |
| [Agent Hub](agent-patterns/agent-hub/README.md) | Centralized orchestration routing tasks to specialist agents via two-model pattern | Advanced | Ch 6: Agent Architecture |
| [Streaming Chat](agent-patterns/streaming-chat/README.md) | SSE streaming with tool calling loop and MCP integration | Advanced | Ch 6: Agent Architecture |
| **Infrastructure** | | | |
| [AI Gateway](infrastructure/ai-gateway/README.md) | Unified gateway for AI model access with rate limiting, caching, and fallback | Intermediate | Ch 4: Infrastructure |
| [Provider Abstraction](infrastructure/provider-abstraction/README.md) | Minimal provider pattern tutorial — switch between OpenRouter and OpenAI | Beginner | Ch 4: Infrastructure |
| [Unified Auth](infrastructure/unified-auth/README.md) | Authentication and authorization system for both humans and AI agents | Advanced | Ch 4: Infrastructure |
| [Observability](infrastructure/observability/README.md) | Monitoring, logging, and tracing for AI-powered applications | Intermediate | Ch 4: Infrastructure |
| **Prompts** | | | |
| [Coding Prompts](prompts/coding-prompts/README.md) | Ready-to-use prompts for AI-assisted development (context loading, TDD, architecture, review, debugging) | Beginner | Ch 5: Building with AI |
| [Agent System Prompts](prompts/agent-system-prompts/README.md) | Complete system prompts for customer support, data analysis, code review, and research agents | Intermediate | Ch 6: Agent Architecture |
| [Evaluation Prompts](prompts/evaluation-prompts/README.md) | Prompts for comparing models, evaluating output quality, and testing safety | Intermediate | Ch 3: The AI Landscape |
| **Configs** | | | |
| [Claude Code Setup](configs/claude-code-setup/README.md) | CLAUDE.md template, custom skills, and hook configurations for your project | Beginner | Ch 5: Building with AI |
| [CI AI Review](configs/ci-ai-review/README.md) | GitHub Actions workflow for AI-powered pull request reviews | Intermediate | Ch 5: Building with AI |

## By Difficulty

### Beginner

Start here. These examples require no infrastructure and can be used immediately.

- **[Provider Abstraction](infrastructure/provider-abstraction/README.md)** -- Minimal example showing how to switch between LLM providers (OpenRouter, OpenAI) without changing application code. Run the demo to compare providers side-by-side.

- **[Coding Prompts](prompts/coding-prompts/README.md)** -- Copy-paste prompt templates organized around the 8 Patterns for AI Coding. Includes context loading, test-driven development, architecture discussions, code review, and error escalation.

- **[Claude Code Setup](configs/claude-code-setup/README.md)** -- Example CLAUDE.md project file, custom skills for code review and test running, and hook configurations for formatting and security. Drop into any project.

### Intermediate

These examples involve some setup but use standard tools and services.

- **[Agent System Prompts](prompts/agent-system-prompts/README.md)** -- Complete system prompts with role definitions, tool access, constraints, and escalation rules. Ready to deploy with any OpenRouter-supported model.

- **[Evaluation Prompts](prompts/evaluation-prompts/README.md)** -- Structured prompts for model comparison, quality evaluation, and safety testing. Use for one-off evaluations or build into a pipeline.

- **[CI AI Review](configs/ci-ai-review/README.md)** -- GitHub Actions workflow, review configuration, and prompt template. Requires an Anthropic API key. Posts review comments on every PR.

- **[Chat Agent](agent-patterns/chat-agent/README.md)** -- Interactive agent pattern with tool calling, context management, and human handoff. Uses OpenRouter with the shared provider library.

- **[Background Agent](agent-patterns/background-agent/README.md)** -- Autonomous agent with progress checkpointing, error recovery, budget tracking, and async result delivery.

- **[AI Gateway](infrastructure/ai-gateway/README.md)** -- Centralized AI model access with rate limiting, response caching, and provider fallback. Supports OpenRouter, OpenAI, and Anthropic.

- **[Observability](infrastructure/observability/README.md)** -- Monitoring and tracing setup for AI applications, including token tracking and latency monitoring.

### Advanced

These examples involve multi-component architectures and deeper infrastructure work.

- **[Streaming Chat](agent-patterns/streaming-chat/README.md)** -- Full SSE streaming with automatic tool calling via MCP (Model Context Protocol). The pattern behind production chat agents.

- **[Agent Hub](agent-patterns/agent-hub/README.md)** -- Orchestration layer using a two-model pattern: cheap model for routing, capable model for execution. All via OpenRouter.

- **[Unified Auth](infrastructure/unified-auth/README.md) ** -- Authentication system serving both human users and AI agents with tiered permissions.

## By Chapter

| Chapter | Examples |
|---------|----------|
| Ch 3: The AI Landscape | [Evaluation Prompts](prompts/evaluation-prompts/README.md) |
| Ch 4: Infrastructure | [Provider Abstraction](infrastructure/provider-abstraction/README.md), [AI Gateway](infrastructure/ai-gateway/README.md), [Unified Auth](infrastructure/unified-auth/README.md), [Observability](infrastructure/observability/README.md) |
| Ch 5: Building with AI | [Coding Prompts](prompts/coding-prompts/README.md), [Claude Code Setup](configs/claude-code-setup/README.md), [CI AI Review](configs/ci-ai-review/README.md) |
| Ch 6: Agent Architecture | [Chat Agent](agent-patterns/chat-agent/README.md), [Background Agent](agent-patterns/background-agent/README.md), [Agent Hub](agent-patterns/agent-hub/README.md), [Streaming Chat](agent-patterns/streaming-chat/README.md), [Agent System Prompts](prompts/agent-system-prompts/README.md) |

## How to Use These Examples

1. **Browse** the table above to find an example relevant to your current work.
2. **Read** the example's README for context, setup instructions, and design decisions.
3. **Copy** the files into your project. Agent-pattern examples need the `shared/` directory too.
4. **Set** your `OPENROUTER_API_KEY` environment variable (or the provider-specific key).
5. **Adapt** the examples to your tech stack, conventions, and requirements.

These examples are starting points, not finished products. Every project has unique requirements. The value is in the patterns and structure, not the specific implementation.

## Architecture

Code examples use a layered architecture based on production patterns:

```
Your Application
       │
       ▼
┌─────────────────┐
│  shared/         │  Provider abstraction layer
│  llm_factory.py  │  get_provider('openrouter') or get_provider('openai')
│  llm_base.py     │  ChatMessage, ToolDefinition, ChatResponse
│  mcp_client.py   │  MCP tool integration
└───────┬─────────┘
        │
        ▼
┌─────────────────┐
│  providers/      │  Raw httpx calls (no SDK dependencies)
│  openrouter.py   │  POST openrouter.ai/api/v1/chat/completions
│  openai.py       │  POST api.openai.com/v1/chat/completions
└─────────────────┘
```

## Related Resources

- [Frameworks](../frameworks/README.md) -- Actionable frameworks extracted from each chapter
- [Checklists](../checklists/README.md) -- Step-by-step checklists for common tasks
- [Book](../book/README.md) -- Full chapter content for deeper context
