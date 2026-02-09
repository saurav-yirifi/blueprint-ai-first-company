# The 6 Questions Before Choosing Any Model

Most teams approach this backwards: they read the benchmarks, watch the demos, get excited about the latest frontier release, and then try to figure out where to apply it. The model is the answer. Start with the question.

I've watched teams burn months evaluating every new model release, running endless POCs, and still ending up paralyzed by choice. Meanwhile, the teams that move fastest use a simple framework: six questions that cut through the noise and point you toward the right answer.

Answer these in sequence. Each eliminates options; by the time you reach #6, your realistic choices have narrowed considerably.

## 1. What's Your Primary Use Case?

Not "what could AI do for us?"---that question has infinite answers. The real question: what specific job are you hiring AI to do?

Different jobs demand different capabilities. Simple classification or extraction doesn't need a frontier model. GPT-3.5 handles FAQ responses and basic categorization at a fraction of the cost. But multi-step reasoning or complex code generation? That's frontier territory.

Harvey discovered this through hard experience. Their evaluation on proprietary legal benchmarks revealed that Gemini 2.5 Pro excels at drafting but struggles with trial preparation—it has difficulty reasoning through complex evidentiary rules like hearsay[^harvey-models].

**The practical test:** Can you describe the job in one sentence? If not, you're not ready to evaluate models.

## 2. What's Your Latency Tolerance?

Latency isn't just a technical metric. It's a business constraint that determines which solutions are viable.

Stripe's fraud detection requires sub-300ms response times[^stripe-latency]. Any model that can't hit that threshold is automatically disqualified, regardless of reasoning capabilities. Meanwhile, batch document processing for compliance reviews can take minutes---cost per query matters more than speed.

The thresholds: sub-second for real-time products (voice, fraud), 1-3s for chatbots and search, 3-10s for internal tools, and minutes or more for batch processing[^latency-research].

## 3. What's Your Compliance Landscape?

For regulated industries, this question should actually be first. Compliance requirements eliminate entire categories of models before other considerations matter.

Healthcare organizations dealing with PHI need HIPAA-compliant environments and Business Associate Agreements. The FDA authorized over 1,000 AI-enabled medical devices between 2015-2024, each requiring specific compliance documentation[^healthcare-compliance].

Financial services prioritize explainability---regulators want to understand how the AI reached conclusions. Government agencies need FedRAMP authorization. Google's Gemini achieved the first FedRAMP High authorization for generative AI in productivity suites in March 2025[^fedramp]. Claude earned multi-cloud FedRAMP High approvals that same year.

Get this wrong, and you're facing regulatory penalties, not just technical debt.

## 4. What's Your Cost Structure?

The cost per million tokens varies by over 200x between premium and budget tiers[^token-pricing]. That's not a typo.

At a thousand queries per day, the difference between models is rounding error. At a million queries per day, it's the difference between a sustainable business and bankruptcy.

**Per-query pricing** works for low or unpredictable volume---you pay for what you use. **Committed capacity** provides 40-80% discounts at the highest tiers---OpenAI enterprise customers report up to 80% off list prices[^enterprise-pricing]. But you're committing to volume you might not hit. **Self-hosted models** have high upfront costs but near-zero marginal costs. Dell Enterprise Strategy Group found self-hosting can be 4x more cost-effective for sustained, heavy usage[^dell-study].

## 5. How Important Is Explainability?

Some use cases require knowing not just what the AI concluded, but why.

Financial services regulators want audit trails. Healthcare requires documentation for risk analysis. Legal teams need to cite sources. When an AI recommendation leads to a bad outcome, can you trace back the reasoning and explain it to an auditor, a patient, or a judge?

If explainability matters for your use case, it needs to be a filter, not an afterthought. Some models are better at this than others. Some architectures make it nearly impossible.

## 6. What's Your Switching Tolerance?

Here's the question nobody wants to ask: if you choose wrong, how painful is it to change?

Switching costs go beyond technical migration. There's interface lock-in---the workflow configurations and prompt libraries embedded in platforms. And organizational friction---retraining users, rebuilding trust, managing disruption.

42% of AI initiatives are now abandoned before reaching production---up from 17% the year before---and vendor lock-in is a primary driver[^abandonment-rate]. Establish migration triggers in advance: what price increase justifies switching? What security incident? Pre-define your exit criteria so you're not making emotional decisions under pressure.

## Putting It Together

Six questions. Write down your answers before you evaluate a single model.

The teams that struggle treat model selection as a technology decision. The teams that succeed treat it as a business decision with technology implications.

One more thing: these answers change. The model that was right six months ago might not be right today. Build in regular re-evaluation---quarterly at minimum---and don't let inertia keep you locked into a suboptimal choice. The landscape is moving fast. Your selection process needs to move with it.

## References

[^harvey-models]: Harvey Blog. [- Expanding Harvey's Model Offerings](https://www.harvey.ai/blog/expanding-harveys-model-offerings)

[^latency-research]: ItsOli. [AI - The Real Cost of Latency: Why Model Performance Should Be a Business Metric](https://itsoli.ai/the-real-cost-of-latency-why-model-performance-should-be-a-business-metric/)

[^stripe-latency]: Latent. [Space Podcast - Stripe](https://www.latent.space/p/stripe)

[^healthcare-compliance]: Kaelio. [- Best AI Analytics Tools for Healthcare Organizations](https://kaelio.com/blog/best-ai-analytics-tools-for-healthcare-organizations)

[^fedramp]: Fedramp. [FedRAMP - AI](https://www.fedramp.gov/ai/)

[^token-pricing]: AllAboutAI. [- 2025 AI Model Benchmark Report](https://www.allaboutai.com/resources/ai-statistics/ai-models/)

[^enterprise-pricing]: GetMonetizely. [- GenAI Enterprise Pricing Models](https://www.getmonetizely.com/articles/genai-enterprise-pricing-models-finding-the-balance-between-volume-discounts-and-premium-features)

[^dell-study]: Rohan. [Paul - Building vs Buying an LLM: Key Decision](https://www.rohan-paul.com/p/building-vs-buying-an-llm-key-decision)

[^abandonment-rate]: The. [Agent Architect - AI Vendor Lock-in Escape Strategy](https://theagentarchitect.substack.com/p/ai-vendor-lock-in-escape-strategy)

---

[← Previous: The Aggregator Layer](./04-the-aggregator-layer.md) | [Chapter Overview](./README.md) | [Next: When to Fine-Tune →](./06-when-to-fine-tune.md)
