# Shared Provider Library

> LLM provider abstraction, OpenRouter/OpenAI providers, and MCP client used by all agent-pattern examples.

## What This Is

A lightweight provider abstraction layer based on production patterns. Instead of importing vendor SDKs (`openai`, `anthropic`), all examples use this shared library which makes raw HTTP calls via `httpx`.

This gives you:
- **Provider switching** without changing application code
- **No SDK dependencies** — just `httpx` and `python-dotenv`
- **Consistent types** across all examples (`ChatMessage`, `ToolCall`, `ChatResponse`)
- **Streaming support** with SSE parsing and tool call reassembly

## Quick Start

```bash
# From the examples/ directory
export OPENROUTER_API_KEY=sk-or-your-key-here
pip install httpx python-dotenv
```

```python
import asyncio
from shared import get_provider, ChatMessage, MessageRole

async def main():
    provider = get_provider()  # defaults to OpenRouter
    response = await provider.chat([
        ChatMessage(role=MessageRole.USER, content="What is 2+2?")
    ])
    print(response.content)

asyncio.run(main())
```

## Files

| File | Purpose |
|------|---------|
| `llm_base.py` | Core types: `MessageRole`, `ChatMessage`, `ToolDefinition`, `ToolCall`, `ChatResponse`, `StreamChunk`, `UsageInfo`, abstract `LLMProvider` |
| `llm_exceptions.py` | Exception hierarchy: auth, rate limit, timeout, context length, content filter |
| `llm_factory.py` | `get_provider()` factory — pass a name or read from env vars |
| `mcp_client.py` | MCP (Model Context Protocol) client for tool integration via JSON-RPC 2.0 |
| `providers/openrouter.py` | OpenRouter provider with tool calling and SSE streaming |
| `providers/openai_provider.py` | Direct OpenAI provider (same interface) |

## Provider Factory

```python
from shared import get_provider

# Default: OpenRouter with google/gemini-2.5-flash
provider = get_provider()

# Explicit provider and model
provider = get_provider('openrouter', model='anthropic/claude-sonnet-4.5')

# Switch to OpenAI
provider = get_provider('openai', model='gpt-4o')
```

Environment variables:
- `OPENROUTER_API_KEY` — Required for OpenRouter (get one at https://openrouter.ai/keys)
- `OPENAI_API_KEY` — Required for OpenAI
- `LLM_PROVIDER` — Default provider name (default: `openrouter`)
- `MODEL` — Default model (default: `google/gemini-2.5-flash`)

## Core Types

### ChatMessage

```python
from shared import ChatMessage, MessageRole

messages = [
    ChatMessage(role=MessageRole.SYSTEM, content="You are helpful."),
    ChatMessage(role=MessageRole.USER, content="Hello!"),
]
```

### Tool Calling

```python
from shared import ToolDefinition

tools = [
    ToolDefinition(
        name="get_weather",
        description="Get current weather for a city",
        parameters={
            "type": "object",
            "properties": {
                "city": {"type": "string", "description": "City name"}
            },
            "required": ["city"],
        },
    )
]

response = await provider.chat(messages, tools=tools)
if response.has_tool_calls:
    for tc in response.tool_calls:
        print(f"Call {tc.name} with {tc.arguments}")
```

### Streaming

```python
async for chunk in provider.chat_stream(messages):
    if chunk.content:
        print(chunk.content, end="", flush=True)
    if chunk.tool_calls:
        # Handle tool calls from stream
        pass
```

## MCP Client

For examples that integrate with MCP servers (like the streaming-chat example):

```python
from shared.mcp_client import MCPClient, MCPServerConfig

config = MCPServerConfig(
    name="my-server",
    url="https://mcp.example.com/mcp",
    headers={"Authorization": "Bearer sk-..."},
)
client = MCPClient(config)
await client.initialize()
tools = await client.list_tools()
result = await client.call_tool("search", {"query": "hello"})
print(result.text)
```

## Architecture

```
Your Example Code
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

## Supported Models

The OpenRouter provider tracks which models support tool calling:

**Tool-capable models:**
`anthropic/claude-sonnet-4.5`, `anthropic/claude-opus-4.5`, `anthropic/claude-sonnet-4`, `anthropic/claude-haiku-4.5`, `openai/gpt-5.2`, `openai/gpt-5`, `openai/gpt-4o`, `openai/gpt-4.1`, `google/gemini-3-flash-preview`, `google/gemini-2.5-flash`, `google/gemini-2.0-flash-001`

**Unstable tool support (use with caution):**
`deepseek/deepseek-chat`, `deepseek/deepseek-v3`, `deepseek/deepseek-v3.2`

## Related

- [Provider Abstraction Tutorial](../infrastructure/provider-abstraction/README.md) — Standalone walkthrough of the pattern
- [Chat Agent](../agent-patterns/chat-agent/README.md) — Interactive agent using this library
- [Streaming Chat](../agent-patterns/streaming-chat/README.md) — SSE streaming with MCP tools
