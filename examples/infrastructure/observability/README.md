# Observability Example

> Companion code for **Chapter 4: Infrastructure for AI-First Operations** --- [The Infrastructure Stack](../../../book/part-2-building/04-infrastructure-for-ai-first-operations/01-the-infrastructure-stack.md)

AI-specific metrics collection, dashboard definitions, and alert rules. Tracks the four metric categories the book identifies as non-optional from day one: latency, tokens, cost, and quality.

## What This Demonstrates

Traditional APM tools track HTTP latency and error rates. AI workloads need different signals:

- **Latency** --- Per-model response times with p50/p95/p99 percentile breakdowns. A slow model isn't a 500 error, but it kills user experience.
- **Tokens** --- Input and output token counts per model without which you cannot explain cost or optimize prompts.
- **Cost** --- Per-request and aggregate AI spend, broken down by model, feature, and team. The number your CFO cares about.
- **Quality** --- Optional quality scores for AI responses. The only signal that tells you whether the AI is actually working.

Without early tracking, AI costs grow faster than usage and you miss optimization opportunities that compound over time.

## File Structure

```
observability/
├── metrics.py                 # AI metrics collector (latency, tokens, cost, quality)
├── alerts.py                  # Alert rules and threshold evaluation
├── dashboards/
│   └── ai-ops.json            # Dashboard definition for AI operations
└── requirements.txt
```

## Quick Start

```bash
# No external dependencies required
python metrics.py    # Run the metrics demo
python alerts.py     # Run the alerts demo
```

## Metrics Demo

`metrics.py` simulates 50 requests across two models and shows:

- **Cost breakdown** --- Total spend, per-model cost, cost by feature tag
- **Latency summary** --- p50/p95/p99 per model
- **Tag-level cost attribution** --- Which features and teams are driving spend

## Alert Rules

`alerts.py` includes default alert rules for the most common AI failure modes:

| Alert | Severity | Threshold | What It Catches |
|-------|----------|-----------|-----------------|
| Daily budget warning | WARNING | > $50/day | Unexpected cost growth |
| Daily budget critical | CRITICAL | > $100/day | Budget breach |
| Cost per request spike | WARNING | > $0.10/req | Runaway agent or prompt regression |
| P95 latency warning | WARNING | > 5,000ms | Model or provider slowdown |
| P99 latency critical | CRITICAL | > 10,000ms | Severe performance degradation |
| Quality degradation | WARNING | < 0.7 score | Model drift or prompt issues |
| Quality critical drop | CRITICAL | < 0.5 score | Possible model failure |
| High token usage | WARNING | > 1M tokens | Token consumption spike |

## Dashboard Definition

`dashboards/ai-ops.json` defines a complete AI operations dashboard with five rows:

1. **Cost Overview** --- Total spend, cost per request, breakdowns by model and feature
2. **Latency** --- p50/p95/p99 time series, latency distribution histogram
3. **Token Usage** --- Input/output by model, tokens per request, input/output ratio
4. **Quality** --- Quality scores over time, quality by feature
5. **Operational Health** --- Request volume, error rate, provider status, active alerts

Import this into Grafana, Datadog, or your preferred dashboard tool. Adjust metric names to match your exporter format.

## Production Notes

This example uses in-memory storage. In production:

- Export metrics via Prometheus client, OpenTelemetry, or Datadog SDK
- Use Helicone or Langfuse for LLM-specific observability (built-in caching can cut costs 20-30%)
- Send alerts to PagerDuty, Slack, or your incident management platform
- Store metric history in a time-series database for trend analysis

## Related

- [AI Gateway Example](../ai-gateway/README.md) --- The gateway that generates these metrics
- [Unified Auth Example](../unified-auth/README.md) --- Auth events feed into observability
- [Infrastructure Audit Checklist](../../../checklists/infrastructure-audit.md)
- [5 Infrastructure Mistakes](../../../frameworks/08-five-infrastructure-mistakes.md)
