# Thinking in Capabilities, Not Features

Winston Weinberg had a choice. As a first-year litigation associate, he could build AI tools the way everyone else was building them: one feature at a time. Contract review here. Research assistant there. Document summarizer over here.

Instead, he co-founded Harvey with a different bet: build an AI that can *reason* like a junior associate, not one that performs isolated tasks. The results from this chapter's opening tell the story—$100M ARR, 42% of the AmLaw 100, valuations that jumped 10x in two years[^harvey-arr][^harvey-valuation].

Harvey didn't win by shipping features faster than competitors. They built legal reasoning as a *capability*, then pointed it at whatever task appeared. The mental shift is subtle but decisive—they didn't compete on what they'd built. They competed on what they *could* build, because the underlying capability extended to problems they hadn't solved yet.

That's what separates AI-first companies from AI-enabled ones.

---

## The Fundamental Distinction

Features solve known problems. Capabilities enable solutions to problems you haven't discovered yet.

A feature is a contract review tool that highlights risky clauses. A capability is an AI that understands legal reasoning well enough to highlight risky clauses, draft counterproposals, explain implications to a client, and spot issues in a jurisdiction it's never seen before—all without rebuilding anything.

Think of it like the difference between a calculator and mathematical fluency. A calculator gives you the answer to 347 times 29. Mathematical fluency lets you estimate whether a business deal makes sense, spot when numbers don't add up, and teach someone else how to think about quantitative problems. One is a tool. The other is a foundation.

Harvey's engineering approach: "From the beginning, our strategy has been to expand the platform with increasingly specific, high-value tools, and then collapse that complexity into a simple, unified interface"[^harvey-strategy]. Notice the sequence. Build specific tools first, yes. But the goal is collapsing them into unified capability, not accumulating disconnected features.

---

## The Capability Mindset in Practice

This pattern shows up across AI-first companies that are breaking out.

**Dust** was founded on a contrarian thesis: one AI model will never rule them all. Co-founder Stanislas Polu, who left OpenAI to start the company, explains: "it's not one assistant but it's many assistants...one assistant will never be great at every task because it has access to too much data"[^dust-thesis].

A feature-first company would build separate AI products for sales, customer support, and engineering. Dust built multi-agent reasoning infrastructure instead. In 2025, Dust users created over 80,000 agents that conducted 12 million conversations[^dust-metrics]. Dust didn't build 80,000 features. They built one capability layer that customers configured into 80,000 applications.

**Glean** made an even more dramatic pivot. They started as enterprise search—arguably the most feature-like of AI applications. But CEO Arvind Jain recognized the limitation. Search is a feature. *Understanding* is a capability.

Glean transformed into "agentic reasoning" where "agents break down complex questions into multi-step plans. Each step is executed using various tools, including search, reasoning, data analysis, employee search, and expert search"[^glean-agentic]. One question from the user. Multiple capabilities coordinated automatically.

---

## When Capability Thinking Fails

Teams try capability thinking and miss the mark. The failure pattern: they build something "general" that turns out to be general at nothing.

A company decides they want "reasoning capability" instead of features. They spend six months building an AI that can supposedly handle anything. But because they never grounded it in a specific, demanding use case, the capability is shallow. It can do a little bit of everything and nothing well. Meanwhile, a feature-first competitor built contract review that actually works, captured the market, and now has data to expand into adjacent capabilities.

Here's the paradox: you discover capabilities by building specific applications, but you sequence investments around the underlying system, not the application. The companies that win build one thing brilliantly first—contract review, code completion, customer support—then discover it generalizes. They don't try to build "general reasoning" in a vacuum.

The right question isn't "How many features have we shipped?" It's "How many different problems can our AI solve with the foundation we've built?" Harvey's growth tells this story: weekly active users grew 4x, monthly queries increased 5.5x, and files stored expanded 36x in a single year[^harvey-growth]. Users found more ways to apply the same capability.

---

## The Shift

Stop asking "What features should our AI have?" Start asking "What capabilities should our AI develop?"

Features accumulate complexity. Ten features means ten things to maintain, ten surfaces that can break. Capabilities compound value. When Stripe improves their fraud detection model, every product using it—payments, invoicing, subscriptions—gets better automatically. One investment, multiple returns.

One-third of global IT leaders have already implemented agentic AI systems, with another 44% planning adoption within the next year[^agentic-adoption]. The companies leading that adoption aren't building feature lists. They're building capability layers.

Stripe's evolution illustrates the long game. They didn't start with their Payments Foundation Model—they started with specific fraud detection features. But they architected those features as training grounds for broader capabilities. Their fraud detection improvement from 59% to 97% came from capability investment that had been compounding for years[^stripe-capability].

Get this right, and you're building a platform. Get it wrong, and you're building a feature factory that competitors can replicate one tool at a time.

## References

[^harvey-arr]: Harvey Year in Review 2024 — [harvey.ai](https://www.harvey.ai/year-in-review/2024)

[^harvey-valuation]: Sparkco AI — [Harvey AI Analysis](https://sparkco.ai/blog/harvey-ai)

[^harvey-strategy]: Harvey Engineering Blog — [A More Unified Harvey Experience](https://www.harvey.ai/blog/a-more-unified-harvey-experience)

[^dust-thesis]: Sequoia Capital Podcast — [Training Data: Dust](https://sequoiacap.com/podcast/training-data-dust/)

[^dust-metrics]: Dust Blog — [Dust Wrapped 2025](https://dust.tt/blog/dust-wrapped-2025)

[^glean-agentic]: Arvind Jain on LinkedIn — [Agentic Reasoning](https://www.linkedin.com/posts/jain-arvind_agentic-reasoning-the-future-of-work-ai-activity-7285449768867188736-e4_P)

[^harvey-growth]: SaaStr on LinkedIn — [Harvey AI Growth](https://www.linkedin.com/posts/saastr_harvey-ai-just-crossed-100m-arr-one-activity-7358629131200180225-nsYO)

[^agentic-adoption]: BCG — [How Agentic AI is Transforming Enterprise Platforms](https://www.bcg.com/publications/2025/how-agentic-ai-is-transforming-enterprise-platforms)

[^stripe-capability]: Stripe Payments Foundation Model Announcement — [stripe.com](https://stripe.com/blog/using-ai-optimize-payments-performance-payments-intelligence-suite)

---

[Chapter Overview](./README.md) | [Next: The 7 Mental Models of AI-First Thinking →](./02-the-7-mental-models.md)
