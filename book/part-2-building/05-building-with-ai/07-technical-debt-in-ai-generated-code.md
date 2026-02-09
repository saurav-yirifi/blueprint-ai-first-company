# Technical Debt in AI-Generated Code

Same as human debt, but faster.

---

AI-generated technical debt isn't new. It's the same patterns humans create—inconsistent naming, duplicated logic, expedient shortcuts. The difference is speed. AI can accumulate in a week what took teams months.

GitClear analyzed over 153 million lines of changed code in 2024 and found code blocks with five or more duplicated lines increased eightfold[^gitclear]. For the first time in their tracking history, developers pasted code more often than they refactored or reused it. That's a debt factory.

## The Army of Juniors Problem

The Ox Security research team coined a phrase that should make every engineering leader uncomfortable: AI coding assistants function like "an army of juniors"[^ox-juniors]. Junior developers write functional code that works in isolation. They lack the architectural judgment to understand how changes ripple through a system.

This isn't a criticism of the tools. It's what happens when you remove the natural bottleneck of typing speed without adding proportional review rigor. A senior developer writes 50-100 lines of production code per hour. With AI, that jumps to 500-1000 lines. If review thoroughness stays constant—or drops because "the AI wrote it"—you're compounding debt at unprecedented rates.

Math doesn't lie. Code churn—lines discarded within two weeks—nearly doubled, from 3-4% in 2020-2022 to roughly 7% in 2024[^gitclear]. There's a Pearson correlation of 0.98 between AI adoption rates and code churn increases.

The DORA 2024 report confirms this: a 25% increase in AI usage correlates with a 7.2% decrease in delivery stability[^dora-2024]. Kin Lane, an API evangelist with 35 years in technology, put it bluntly: "I don't think I have ever seen so much technical debt being created in such a short period of time"[^lane-quote].

## Six Debt Patterns AI Accelerates

AI doesn't invent new ways to create bad code. It creates the old kinds faster.

**1. Inconsistent patterns** emerge because AI doesn't remember what it wrote yesterday. Authentication on Monday and payments on Tuesday yield two completely different approaches to error handling.

**2. Duplicated logic** multiplies because AI optimizes for the immediate request. It will happily write a date formatting function in three different files rather than using the one that already exists.

**3. Missing abstractions** accumulate when AI implements inline what should be shared. Every feature generates fresh code rather than extracting patterns.

**4. Over-abstraction** happens when AI adds layers that serve no purpose. Interfaces with single implementations. Factory patterns for classes that will never have siblings.

**5. Incomplete error handling** is endemic because AI excels at happy paths. The main flow works beautifully. Edge cases? Silent failures.

**6. Stale dependencies** creep in because AI training data ages. It recommends patterns from two years ago. Security vulnerabilities ship because the code "looked right."

## Prevention Costs Less Than Remediation

Prevention requires 10-20% of project budget for automated gates and rigorous review. Remediation consumes 40-60% of maintenance budgets[^mit-sloan]. MIT Sloan researchers described AI-generated code as "borrowing at a higher interest rate."

What does effective prevention look like?

**Living documentation in prompts.** Every AI session starts with relevant architecture docs, style guides, and pattern libraries in context. When we added naming conventions and error handling standards to system prompts, pattern violations dropped by roughly 60% (internal Yirifi data).

**Review standards calibrated to volume.** Review AI code the way you'd review submissions from a talented new hire: assume competence, verify architecture, check for integration with existing patterns.

**Automated checks that catch what humans miss.** Duplication detection, linting, dependency scanning, security analysis—all running in pre-commit hooks and CI/CD pipelines. Humans are terrible at catching copy-paste code across files. Machines excel at it.

**Scheduled debt paydown.** Allocate 20% of development time explicitly to debt paydown. Not "when we have time." Scheduled. On the sprint board. Teams that skip this find themselves drowning within six months.

Same debt. Faster accumulation. Same solutions. More rigor.

## References

[^gitclear]: GitClear. [2024 Coding Agent Research Report](https://www.gitclear.com/coding_on_copilot_data_shows_ais_downward_pressure_on_code_quality)

[^ox-juniors]: Ox. [Security "The Army of Juniors" Research](https://www.ox.security/the-army-of-juniors-llm-assisted-code-poses-elevated-security-risks/)

[^mit-sloan]: MIT. [Sloan Management Review on AI Code Economics](https://sloanreview.mit.edu/article/technical-debt-ai-code/)

[^dora-2024]: DORA. [Accelerate State of DevOps Report 2024 — AI and delivery stability](https://dora.dev/research/2024/dora-report/)

[^lane-quote]: Kin. [Lane on AI Technical Debt, InfoQ November 2025](https://www.infoq.com/news/2025/11/ai-code-technical-debt/)

---

[← Previous: When AI Coding Fails](./06-when-ai-coding-fails.md) | [Chapter Overview](./README.md)
