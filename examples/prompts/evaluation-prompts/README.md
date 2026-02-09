# Evaluation Prompts

> Prompts for evaluating AI model outputs, comparing models, and assessing quality and safety. Use these when selecting models, benchmarking agent performance, or building evaluation pipelines.
>
> Reference: [6 Questions Before Choosing a Model](../../../frameworks/07-six-questions-before-choosing-a-model.md) | [7 Failure Modes of Agents](../../../frameworks/10-seven-failure-modes-of-agents.md)

## Prompts in This Collection

| Prompt File | Use Case | Related Framework |
|-------------|----------|-------------------|
| [Model Comparison Prompts](model-comparison-prompts.md) | Comparing outputs from different models on the same task | [6 Questions Before Choosing a Model](../../../frameworks/07-six-questions-before-choosing-a-model.md) |
| [Quality Evaluation Prompts](quality-eval-prompts.md) | Scoring output quality across multiple dimensions | [8 Patterns for AI Coding](../../../frameworks/09-eight-patterns-for-ai-coding.md) |
| [Safety Evaluation Prompts](safety-eval-prompts.md) | Testing for safety, alignment, and policy compliance | [7 AI Risks and Mitigations](../../../frameworks/19-seven-ai-risks-and-mitigations.md) |

## Why Evaluate

From [Chapter 3: The AI Landscape](../../../book/part-1-foundations/03-the-ai-landscape/README.md): choosing a model is not a one-time decision. Models improve, pricing changes, and new providers emerge. Structured evaluation lets you make data-driven model decisions instead of relying on benchmarks that may not reflect your use case.

From [Chapter 11: Ethics, Governance, and Risk](../../../book/part-4-sustaining/11-ethics-governance-and-risk/README.md): safety evaluation is not optional. The companies that avoid AI incidents are the ones that test for failure modes before deploying.

## Evaluation Approach

These prompts support three evaluation methods:

1. **Human evaluation** -- A person scores model outputs using the criteria in these prompts. Most accurate, least scalable.
2. **Model-as-judge** -- A separate AI model scores outputs using these prompts as its rubric. Scalable, requires calibration.
3. **Automated metrics** -- Programmatic checks (e.g., "does the output contain SQL injection?"). Most scalable, narrowest coverage.

For production evaluation pipelines, combine all three: automated metrics as a first pass, model-as-judge for batch evaluation, human evaluation for edge cases and calibration.

## Related Resources

- [Coding Prompts](../coding-prompts/README.md) -- the prompts being evaluated
- [Agent System Prompts](../agent-system-prompts/README.md) -- agent outputs to evaluate
- [6 Questions Before Choosing a Model](../../../frameworks/07-six-questions-before-choosing-a-model.md) -- the decision framework these prompts support
- [Permission Model Framework](../../../frameworks/17-permission-model-framework.md) -- autonomy levels that safety evals should verify
