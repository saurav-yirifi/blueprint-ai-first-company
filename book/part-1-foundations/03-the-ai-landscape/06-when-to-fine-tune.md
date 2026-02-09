# When to Fine-Tune

Here's a pattern I keep seeing: teams that jump straight to fine-tuning as their first optimization move. Six months later, they're maintaining a bespoke model that underperforms the latest base model release. The foundation model providers ship improvements quarterly. Your fine-tuned model stops improving while base models keep advancing.

Fine-tuning is powerful. It's also expensive, time-consuming, and creates ongoing maintenance obligations. It works—but only when it's the right tool for your specific situation, right now.

---

## The Decision Hierarchy

Before you fine-tune anything, exhaust the cheaper options first.

**Start with prompt engineering.** Most teams underestimate how much performance they can extract from better prompts. System messages, few-shot examples, chain-of-thought reasoning—these cost nothing to iterate and can often close the gap you thought required model customization.

**Then consider RAG.** If your model needs domain knowledge it doesn't have, retrieval-augmented generation is usually the answer. Need your model to cite company policies? Reference product documentation? RAG handles these without any model modification. When your knowledge base changes, you update the retrieval system—not the model.

**Fine-tuning is for the last mile.** When the model has the right knowledge but needs to answer in a different style, follow specific output formats, or consistently use certain tools—that's when fine-tuning earns its cost. You're not teaching it new facts. You're adjusting how it applies what it knows.

---

## The Math That Actually Matters

Fine-tuning can deliver 300-400% ROI in the first year—but only under specific conditions[^udit-goenka].

**Volume threshold:** Consider fine-tuning when monthly API costs exceed $5,000–$10,000. Below that, the overhead of training, evaluation, and maintenance rarely justifies the savings[^genloop].

**Hidden costs compound.** Beyond initial training, expect maintenance around $5,000 monthly, drift monitoring at $3,000 monthly, and quarterly retraining at $20,000 each. Total hidden costs can exceed $200,000 annually—this is why 73% of fine-tuning projects fail to deliver positive ROI[^real-cost].

**Per-token costs tell a misleading story.** Fine-tuning through OpenAI increases token costs 4-6x versus the base model[^scopic]. But fine-tuned models often need fewer tokens per query because they require less prompting. The real comparison is cost per successful task completion.

---

## LoRA: The Pragmatic Middle Ground

LoRA (Low-Rank Adaptation) freezes original model weights and adds small trainable matrices for task-specific adjustments—reducing GPU memory requirements by up to 3x[^lora-linkedin]. This changes the economics entirely: instead of expensive cloud GPUs, you can run specialized models on modest hardware.

Capital Fund Management (CFM) demonstrates the potential. They fine-tuned open-source models for financial Named Entity Recognition and achieved solutions up to 80x cheaper than large LLMs while improving accuracy by 6.4%[^cfm-case]. A B2B SaaS startup fine-tuned on 5,000 sales conversations and saw lead qualification accuracy jump from 34% to 89%[^udit-goenka].

The pattern: specific task, substantial data, clear evaluation criteria, and a use case where prompting and RAG weren't enough.

---

## What You Need Before Starting

**Quality data.** Minimum 50-100 high-quality examples for simple tasks; 500-2,000 for content generation. Quality matters more than quantity—errors in training data get amplified by millions of parameters.

**Stable requirements.** If your product is still finding product-market fit, don't fine-tune. The model you train today optimizes for yesterday's understanding of the problem.

**Evaluation infrastructure.** How will you know if your fine-tuned model is actually better? You need benchmarks that matter to your business. Glean built their AI Evaluator to measure context relevance and recall rates specific to enterprise search[^glean-eval]. Harvey created BigLaw Bench for legal reasoning. Generic benchmarks won't tell you if your fine-tuned model actually performs better on your tasks.

---

## The Decision Framework

Before committing engineering time to fine-tuning, answer honestly:

1. **Have you exhausted prompt engineering?** If you haven't systematically tested different prompting strategies, you don't know what fine-tuning needs to solve.

2. **Is the problem knowledge or behavior?** Knowledge gaps are for RAG. Behavioral adjustments—style, format, tool use—are for fine-tuning.

3. **Do you have enough quality data?** Hundreds of examples, not dozens.

4. **Are your requirements stable?** If the use case is still evolving, fine-tuning locks you into a snapshot of current understanding.

5. **Can you justify the ongoing costs?** Training is one-time. Monitoring, maintenance, and retraining are perpetual.

If you can't confidently answer all five, fine-tuning is probably premature. That's not failure—it's recognizing where you actually are in the optimization journey.

## References

[^udit-goenka]: Udit. [Goenka - The $47K Fine-Tuning Revolution](https://uditgoenka.co/p/small-language-model)

[^scopic]: Scopic. [- The Real Cost of Fine-Tuning LLMs](https://scopicsoftware.com/blog/cost-of-fine-tuning-llms/)

[^genloop]: GenLoop. [- The Why, When, and How Guide to LLM Fine-Tuning](https://genloop.ai/collection/the-why-when-and-how-guide-to-llm-fine-tuning-making-ai-work-for-your-enterprise)

[^real-cost]: AIFormaking. [- The Real Cost of Fine-Tuning](https://www.aiformak.ing/articles/real-cost-of-fine-tuning)

[^lora-linkedin]: LinkedIn. [- LoRA vs QLoRA: Efficient Techniques for Fine-Tuning LLMs](https://www.linkedin.com/pulse/lora-vs-qlora-efficient-techniques-fine-tuning-llms-padhy-6ff3c)

[^cfm-case]: HuggingFace. [- CFM Case Study](https://huggingface.co/blog/cfm-case-study)

[^glean-eval]: Glean — [Using AI Evaluator to ensure Glean Assistant meets modern enterprise needs](https://www.glean.com/blog/glean-ai-evaluator)

---

[← Previous: The 6 Questions Before Choosing Any Model](./05-the-6-questions-before-choosing.md) | [Chapter Overview](./README.md) | [Next: Future-Proofing Your Stack →](./07-future-proofing-your-stack.md)
