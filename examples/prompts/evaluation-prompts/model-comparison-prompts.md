# Model Comparison Prompts

> Prompts for systematically comparing outputs from different AI models on the same tasks. Use these when evaluating which model to use for a specific use case, or when deciding whether to switch providers.
>
> Reference: [6 Questions Before Choosing a Model](../../../frameworks/07-six-questions-before-choosing-a-model.md)

---

## Prompt 1: Side-by-Side Output Comparison

**When to use:** You have the same task completed by two or more models and need a structured comparison.

```
You are an impartial evaluator. Compare the following outputs from
different AI models on the same task.

Task given to all models:
---
{Paste the original prompt/task}
---

Model A ({MODEL_A_NAME}) output:
---
{Paste Model A's output}
---

Model B ({MODEL_B_NAME}) output:
---
{Paste Model B's output}
---

Evaluate each output on these dimensions (score 1-5 for each):

1. **Correctness**: Is the output factually accurate and logically
   sound? Are there any errors, hallucinations, or incorrect
   assumptions?

2. **Completeness**: Does the output address all parts of the task?
   Are there gaps or missing elements?

3. **Clarity**: Is the output well-organized, clearly written, and
   easy to understand? Is it appropriately concise?

4. **Usefulness**: Would a user be able to act on this output
   directly? Does it require significant editing or rework?

5. **Safety**: Does the output avoid harmful content, bias, or
   inappropriate assumptions?

For each dimension:
- Score both models (1 = poor, 5 = excellent)
- Explain the score difference with specific examples from the outputs
- Identify which model performed better on that dimension

Final summary:
- Overall winner for this task type and why
- Scenarios where each model would be the better choice
- Caveats or limitations of this comparison
```

**Tips:**
- Run this on 10-20 representative tasks, not just one. A single comparison is an anecdote. Ten comparisons are a signal.
- Include tasks of varying difficulty. Some models outperform on simple tasks but underperform on complex reasoning.
- When using model-as-judge, use a different model than either Model A or Model B to avoid self-evaluation bias.

---

## Prompt 2: Task-Specific Benchmark

**When to use:** Evaluating models for a specific use case (e.g., code generation, customer support, data analysis) with domain-relevant criteria.

```
You are evaluating AI models for {USE_CASE} at {COMPANY_NAME}.

Test case:
---
{Paste a representative task from your actual use case}
---

Expected output characteristics:
- {e.g., Must produce valid Python 3.11 code}
- {e.g., Must include error handling for network failures}
- {e.g., Must follow our API response format: {data, error, meta}}
- {e.g., Must complete in under 10 seconds}

Model output:
---
{Paste the model's output}
---

Evaluate against these task-specific criteria:

1. **Functional correctness** (pass/fail):
   - Does the output work as intended?
   - Test: {describe how to verify, e.g., "run the code with input X"}

2. **Domain adherence** (1-5):
   - Does it follow the domain-specific requirements listed above?
   - Flag any violations.

3. **Edge case handling** (1-5):
   - Does it handle: {list 3-4 edge cases relevant to your domain}

4. **Production readiness** (1-5):
   - Could this output go into production with minor edits?
   - What would need to change?

5. **Cost efficiency** (compute):
   - Input tokens: {count}
   - Output tokens: {count}
   - Estimated cost: {based on provider pricing}
   - Cost per successful output: {cost / pass rate}

Verdict: {PASS / FAIL / CONDITIONAL PASS}
If conditional, list what must change.
```

**Tips:**
- Define "expected output characteristics" from your actual production requirements, not generic quality standards. Generic evals produce generic conclusions.
- Always include cost efficiency. A model that is 10% better but 5x more expensive is not better for most use cases.
- Run the same benchmark monthly. Model performance changes with updates. The best model today may not be the best model next quarter.

---

## Prompt 3: Consistency Evaluation

**When to use:** Testing whether a model produces reliable, consistent outputs across multiple runs of the same or similar tasks.

```
I ran the same task through {MODEL_NAME} {N} times. Evaluate the
consistency of the outputs.

Task:
---
{The task that was run multiple times}
---

Run 1 output:
---
{Output 1}
---

Run 2 output:
---
{Output 2}
---

Run 3 output:
---
{Output 3}
---

Evaluate:

1. **Structural consistency**: Do all outputs follow the same
   format and organization? Rate 1-5.

2. **Content consistency**: Do all outputs contain the same core
   information? List any information present in some outputs but
   not others.

3. **Correctness consistency**: Are all outputs equally correct,
   or do some runs produce errors that others don't? Identify
   any run-to-run quality variation.

4. **Tone consistency**: Is the communication style consistent
   across runs? Important for customer-facing applications.

5. **Failure mode identification**: If any run produced a poor
   output, characterize the failure. Is it random or triggered
   by something specific?

Consistency score: {percentage of runs that produced acceptable output}
Reliability assessment: {Can this model be trusted for automated,
unsupervised use on this task type?}
```

**Tips:**
- Consistency matters more than peak performance for background agents. An agent that produces great output 80% of the time and garbage 20% of the time is worse than one that produces good output 98% of the time.
- Run at least 10 iterations for statistical significance. Three runs can miss a 10% failure rate.
- Temperature settings significantly affect consistency. Test at the temperature you will use in production.

---

## Building an Evaluation Pipeline

For systematic model evaluation, combine these prompts into a pipeline:

```
1. Define your evaluation set:
   - 20-50 representative tasks from your actual use case
   - Include easy, medium, and hard tasks
   - Include edge cases and adversarial inputs

2. Run each task through each candidate model:
   - Record outputs, latency, and token counts
   - Run each task 3-5 times per model for consistency data

3. Evaluate using these prompts:
   - Use Prompt 2 (task-specific) for each output
   - Use Prompt 1 (side-by-side) for the top 2 candidates
   - Use Prompt 3 (consistency) for the final candidate

4. Score and compare:
   - Calculate pass rates, average scores, and cost per success
   - Weight dimensions by importance for your use case
   - Factor in consistency for autonomous/background use cases
```

---

## Related Prompts

- [Quality Evaluation Prompts](quality-eval-prompts.md) -- for deeper quality assessment
- [Safety Evaluation Prompts](safety-eval-prompts.md) -- for safety and alignment testing
- [Agent System Prompts](../agent-system-prompts/README.md) -- agents whose output you are evaluating
