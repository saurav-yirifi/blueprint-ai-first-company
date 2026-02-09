# Chapter 2: The AI-First Mindset

Harvey hit $100M ARR in three years[^harvey-arr]. The legal AI company serves 42% of the AmLaw 100 and operates in 120+ countries[^harvey-reach]. Their valuation jumped from $715M to $8B in under two years[^harvey-valuation].

But here's what matters: Harvey didn't win by building more features faster than competitors. They built a *capability*—legal reasoning—that could be applied to any task. Contract review, due diligence, regulatory analysis, memo drafting. One underlying capability. Unlimited applications. That's not a product strategy. That's a different way of thinking about what you're building.

At Yirifi, we stumbled into a similar insight from a different direction: "Every API we built assumed the first consumer would be an AI agent, not a person clicking buttons." When you design for agents first, humans benefit automatically. When you design for humans first and try to bolt on agent access later, you're retrofitting. This chapter teaches the mental models that make AI-first thinking instinctive.

<div class="yirifi-anchor" markdown>

> "Every API we built assumed the first consumer would be an AI agent, not a person clicking buttons."

**Universal insight:** Agent-first design creates a forcing function for clarity. If an AI can call your API, your interface is well-defined. If an AI can interpret your response, your data structure is clean. Design for agents, and humans get better interfaces for free.

**Memorable close:** "Build for agents. Humans will thank you."

</div>

## What You'll Learn

- **[Thinking in Capabilities, Not Features](./01-thinking-in-capabilities.md):** Features solve known problems. Capabilities enable solutions to problems you haven't discovered yet. The paradox: you discover capabilities by building specific applications first—Harvey's approach of "collapsing complexity into a unified interface."

- **[The 7 Mental Models of AI-First Thinking](./02-the-7-mental-models.md):** Agent-first design, probabilistic thinking, data as product, permission spectrum, compound iteration, build vs buy inversion, and human-AI collaboration. These work as a system—miss one, and you undermine the others.

- **[The Build vs Buy Calculus](./03-the-build-vs-buy-calculus.md):** MIT's "Buy, Boost, or Build" framework—65% of costs occur after deployment. Klarna saved $40M buying. Morgan Stanley boosted with 70,000 proprietary documents. Bloomberg spent $8M building. Three questions determine your path.

- **[Data as Product](./04-data-as-product.md):** Jensen Huang's flywheel: usage generates signal, signal improves the model, better models drive more usage. Three requirements: structured data for learning, fast feedback loops, visible improvement to users. Spotify processes 500 billion events daily.

- **[Iteration Speed and Learning Loops](./05-iteration-speed-and-learning-loops.md):** 720 learning cycles per year (daily iteration) versus 52 (weekly). Meta's "Time to First Batch" metric. Vercel iterates almost daily. Your slowest loop sets your learning pace.

- **[Human-AI Collaboration](./06-human-ai-collaboration.md):** MIT reviewed 100+ studies—human-AI combinations don't automatically outperform the best single performer. Partner under direction, not teammate. 84% of designers collaborate with developers weekly, but fewer than half feel AI makes them *better*.

---

## The Real Question

The economics from [Chapter 1](../01-the-ai-first-imperative/README.md) tell you AI-first is possible. This chapter tells you how AI-first founders actually think. Seven mental models that work as a system—miss one, and you undermine the others.

For startups, these mental models are structural advantage. Bake agent-first design and data flywheel thinking into your culture from day one. No retrofitting required. The companies pulling ahead aren't just building better AI—they're building systems where using the AI makes it better.

For established organizations, the path requires deliberate practice. Your next internal API project: design the agent interface first, even if no agent exists yet. Your next data decision: treat it as a product decision, not engineering plumbing. Start small. Let the mental models become instinctive before scaling them.

Understanding these concepts intellectually is table stakes. The question is whether they shape how you make decisions.

Let's find out.

## References

[^harvey-arr]: Harvey Year in Review 2024 — [harvey.ai](https://www.harvey.ai/downloadable/year-in-review/2024/Harvey-2024-year-in-review.pdf)
[^harvey-reach]: Harvey Year in Review 2024 — [harvey.ai](https://www.harvey.ai/downloadable/year-in-review/2024/Harvey-2024-year-in-review.pdf)
[^harvey-valuation]: Forbes — [forbes.com](https://www.forbes.com/sites/alexkonrad/2024/12/18/harvey-ai-legal-startup-reaches-8-billion-valuation/)

---

[Part Overview](../README.md) | [Book Contents](../../README.md)
