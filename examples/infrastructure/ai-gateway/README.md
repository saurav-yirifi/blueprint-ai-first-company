# AI Gateway Example

> Companion code for **Chapter 4: Infrastructure for AI-First Operations** --- [The AI Tool Gateway Pattern](../../../book/part-2-building/04-infrastructure-for-ai-first-operations/03-the-ai-tool-gateway-pattern.md)

A minimal AI gateway that routes completion requests through authentication, rate limiting, cost tracking, and structured logging before they reach any provider. Uses raw `httpx` --- no SDK packages --- with OpenRouter as the primary provider and automatic fallback to direct OpenAI/Anthropic.

## What This Demonstrates

The book's AI Tool Gateway pattern: a single entry point that sits between your application (or agents) and multiple AI providers. The gateway enforces security, tracks cost, and handles provider failures --- so calling code never has to.

**Key patterns:**
- **Provider abstraction** --- One interface (`BaseProvider`), multiple backends. Switching providers is a config change, not a code change.
- **Raw httpx, no SDKs** --- Every provider uses `httpx.AsyncClient` directly. Zero provider-specific dependencies to manage.
- **OpenRouter as primary** --- One API key, dozens of models (OpenAI, Anthropic, Google, Meta, Mistral). Direct OpenAI and Anthropic connections serve as fallbacks.
- **Middleware chain** --- Auth, rate limits, and cost tracking run *before* any provider API call. Invalid or throttled requests never cost you money.
- **Fallback with retry** --- If the primary provider fails, the gateway retries with exponential backoff, then falls back to the next provider automatically.
- **Structured logging** --- JSON log lines for every request, ready for any log aggregator.

## File Structure

```
ai-gateway/
├── gateway.py                 # Main gateway --- routes requests through middleware
├── config.yaml                # Provider, routing, rate limit, and cost configuration
├── .env.example               # Required environment variables
├── requirements.txt           # httpx, pyyaml, python-dotenv (no SDKs)
├── providers/
│   ├── base.py                # BaseProvider interface (the abstraction layer)
│   ├── openrouter.py          # OpenRouter adapter (PRIMARY --- one key, many models)
│   ├── openai.py              # OpenAI adapter (fallback)
│   ├── anthropic.py           # Anthropic adapter (fallback)
│   └── fallback.py            # Retry + fallback logic across providers
└── middleware/
    ├── auth.py                # API key authentication
    ├── rate_limit.py          # Sliding-window rate limiting per key/tier
    ├── cost_tracker.py        # Per-request and per-key cost tracking
    └── logger.py              # Structured JSON logging
```

## Quick Start

```bash
pip install -r requirements.txt

# Primary provider --- all you need to get started
export OPENROUTER_API_KEY="sk-or-..."

# Optional fallbacks (direct provider connections)
# export OPENAI_API_KEY="sk-..."
# export ANTHROPIC_API_KEY="sk-ant-..."

python gateway.py
```

## How the Middleware Chain Works

Every request flows through this sequence:

```
Request
  → Auth (validate API key, resolve tier)
  → Rate Limit (check requests/min and tokens/min for this tier)
  → Route (pick the right provider for the requested model)
  → Provider (call OpenRouter/OpenAI/Anthropic with retry + fallback)
  → Cost Tracker (record token usage and calculate cost)
  → Logger (emit structured JSON log line)
Response
```

Auth and rate limits execute before any provider call. If a request is unauthenticated or throttled, it never reaches the AI backend --- and never costs you anything.

## Why Raw httpx Instead of SDKs

Every provider adapter uses `httpx.AsyncClient` with raw HTTP calls instead of the `openai` or `anthropic` Python packages. This gives you:

- **Fewer dependencies** --- `httpx`, `pyyaml`, and `python-dotenv` are all you need
- **Full control** --- Timeouts, connection pooling, and retry logic are yours to configure
- **Consistent pattern** --- Every provider looks the same: build a payload dict, POST it, parse the JSON response
- **Easier debugging** --- You can see exactly what goes over the wire

The tradeoff is manual SSE parsing for streaming, but the pattern is simple and identical across OpenAI-compatible APIs.

## Configuration

Edit `config.yaml` to change providers, rate limits, or pricing. API keys always come from environment variables.

## Production Notes

This example uses in-memory stores for rate limits, cost tracking, and API keys. In production:

- Replace the API key store with your identity provider (Auth0, Supabase Auth, etc.)
- Replace the rate limiter's in-memory dict with Redis for multi-instance deployments
- Export cost data to your observability stack (see the [observability example](../observability/README.md))
- Run behind a reverse proxy (Nginx, Envoy) for TLS termination

## Related

- [Unified Auth Example](../unified-auth/README.md) --- Authentication for humans and agents
- [Observability Example](../observability/README.md) --- AI metrics, dashboards, and alerts
- [Permission Model Framework](../../../frameworks/17-permission-model-framework.md)
- [5 Infrastructure Mistakes](../../../frameworks/08-five-infrastructure-mistakes.md)
