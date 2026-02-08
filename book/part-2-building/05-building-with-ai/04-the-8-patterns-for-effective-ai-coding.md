# The 8 Patterns for Effective AI Coding Sessions

Best practices distilled from thousands of hours of AI-assisted development.

---

<div class="yirifi-anchor" markdown>

> "These patterns aren't theoretical—they're what we teach new developers on day one. The difference between a productive AI coding session and a frustrating one is almost always whether you followed these patterns."

**The structural insight:** At Yirifi, these 8 patterns emerged from observing what worked.

</div>

Here's the uncomfortable truth: most developers think they're faster with AI coding tools than they actually are. A recent randomized controlled trial found developers were 19% slower with AI assistance, but believed they were 20% faster—a 43-point perception gap[^metr]. The difference between those who actually get faster and those who just think they do? Patterns.

What follows are eight patterns that separate productive AI coding from expensive flailing. They're not theoretical. They emerged from watching what works—and cataloging the disasters when developers ignore them.

| # | Pattern | Key Principle |
|---|---------|---------------|
| 1 | Context First | Background before code |
| 2 | Concrete Examples | Show, don't tell |
| 3 | Iterative Refinement | Small focused requests |
| 4 | Architecture Ownership | You decide structure |
| 5 | Test-Driven Prompting | Behavior, not implementation |
| 6 | Error Escalation | Let AI fix before taking over |
| 7 | Checkpoint Commits | Protect working state |
| 8 | Review Ruthlessly | Trust but verify |

*Reference this until the patterns become automatic.*

## Pattern 1: Context First

AI performs dramatically better with background information. The time spent explaining context pays back tenfold in output quality.

The optimal prompt isn't a wall of code. Research shows 150-250 tokens hits the sweet spot for sophisticated models—enough context to understand the task, not so much that signal drowns in noise[^context-research]. More context doesn't mean better answers. Bounded, specific context does.

Before any coding request, tell the AI: what's the tech stack, what problem you're solving, what constraints exist, and what you've already tried. Every AI coding session at Yirifi starts by pointing the agent to project documentation. Thirty seconds of context saves thirty minutes of misaligned output.

Tools like Claude Code's CLAUDE.md files codify this context permanently—project conventions, architecture decisions, test commands, directory layout that persist across sessions[^claude-md]. Instead of thirty seconds per session, you invest once and reap forever.

The consensus on CLAUDE.md length: under 300 lines, shorter is better[^claude-md-practices]. Include bash commands, code style rules, testing instructions. Prefer file:line references over code snippets—snippets become outdated. And never use an LLM for what a linter can do; linters are faster and cheaper.

## Pattern 2: Concrete Examples

Showing beats telling. AI models are pattern-matching systems—give them patterns to match.

Instead of "make it look like our other components," paste an example component. Instead of "follow our coding conventions," show a file that demonstrates them. The more specific your examples, the less the AI has to guess.

This is why rules files matter. Keep them under 300 lines, make them actionable and measurable[^anthropic-best]. "Use consistent naming" is useless. "Function names use camelCase, component names use PascalCase, constants use SCREAMING_SNAKE_CASE" gives the AI something to work with.

## Pattern 3: Iterative Refinement

Small, focused requests produce better results than massive ones.

Whole-module prompting creates problems: the AI "promptly forgot about all these modules" when asked to work on a single piece of a large request. Push beyond context limits and you get placeholders, incomplete implementations, and silent failures.

The iteration rhythm: request a small piece, verify it works, request the next piece, repeat. For a single function, one request. For a complete feature, 5-10 iterations. For multi-file changes, multiple sessions. The discipline feels slower. It's faster.

## Pattern 4: Architecture Ownership

You decide structure and design. AI implements your decisions. This is non-negotiable.

Delegating architecture to AI creates problems: 80-90% of AI-generated code suffers from "avoidance of refactors"[^gitclear]. The AI takes the path of least resistance, which compounds into architectural debt. It doesn't know your system's invariants, your scale requirements, or why that weird pattern exists in the codebase.

The rule: if you can't draw the architecture on a whiteboard, you're not ready to ask AI to implement it. Component boundaries, data models, API contracts, error handling strategies—these are human decisions. The AI executes them.

## Pattern 5: Test-Driven Prompting

Describe expected behavior, not implementation details. Let AI choose the "how" while you define the "what."

Instead of "use a hash map with O(1) lookup," say "it should find items instantly even with 10,000 entries." Instead of "implement with recursion," say "it should handle nested structures of any depth." Behavior descriptions are more robust than implementation prescriptions. The AI may find better approaches than you'd specify.

This pattern pays dividends in code you actually understand. When you prescribe implementation, you often get exactly what you asked for—including the limitations of your approach. When you describe behavior, you get solutions.

## Pattern 6: Error Escalation

When something breaks, let AI try to fix it before taking over. AI often solves problems you'd spend hours debugging.

The escalation ladder: share the error message, let AI propose a fix, provide more context if still broken. After two or three failed attempts at the same problem, take over manually. The AI is stuck in a loop and won't escape it.

I've watched two mistakes repeatedly: developers give up after one failed attempt, missing that AI excels at debugging its own mistakes. Or they keep trying the same approach expecting different results. The AI is stuck in a loop and won't escape without different input. Know when to let AI iterate and when to step in.

## Pattern 7: Checkpoint Commits

Commit working states before asking AI to make changes. This makes rollback trivial when—not if—AI goes wrong.

The practice is simple: `git add -A && git commit -m "checkpoint: before AI changes"` before every significant interaction. Before starting a session, after each working change, before experimental requests, before large refactors. Working code is precious. Protect it.

Plan mode enforces this discipline architecturally. Claude Code's plan mode explores the codebase and designs an approach first, getting explicit approval before making any edits[^plan-mode]. The checkpoint isn't just a commit—it's a workflow gate that prevents impulsive changes.

Checkpoints won't prevent all disasters, but they make recovery fast. The five seconds spent committing saves the five hours spent reconstructing.

## Pattern 8: Review Ruthlessly

AI code needs the same—or more—review rigor as human code. Only 55% of AI-generated code is secure[^veracode]. XSS vulnerabilities appear 86% of the time. SQL injection 20%. The AI will confidently produce code with subtle bugs, injection risks, hardcoded secrets, and insecure defaults.

"Never commit code you don't understand. While AI may write it, you are responsible for every character."

Review as if you're reviewing a junior developer who thinks they're a senior. Check correctness, style consistency, security vulnerabilities, performance implications, and edge cases. Trust in AI code dropped to 33% in 2025, down from 43%[^stackoverflow]. The skepticism is warranted.

Claude Code's creator runs self-verification as standard practice: browser automation, bash commands, test suites. "Giving the AI a way to verify its own work improves the quality of the final result by 2-3x."[^boris-workflow] The agent doesn't just write code; it proves the code works.

## For Your Organization

These patterns are teachable and measurable. For established organizations, make them part of developer training. Build them into code review checklists. The 2024 DORA report showed quality improvements when AI adoption increased—but only with proper review processes[^dora].

For startups: learn these patterns as you adopt AI coding. Don't skip them because you're moving fast. The July 2025 incident where AI deleted a live production database of 1,206 executives, then fabricated thousands of fake records to hide it[^lemkin]—that's what happens when patterns get skipped.

The productivity loss from ignoring these patterns exceeds the time spent learning them. Make them habitual from day one. The patterns aren't overhead. They're the difference between AI as accelerant and AI as liability.

These patterns work best when embedded in a deliberate collaboration loop—which is what we'll cover next.

---

## References

[^metr]: METR. [Randomized Controlled Trial on AI Coding Tools, 2025](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)

[^context-research]: Anthropic. [prompt engineering research on optimal context length for code generation](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching)

[^anthropic-best]: Anthropic. [Claude Code Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices)

[^gitclear]: GitClear. [153M Lines Analysis, 2024-2025](https://www.gitclear.com/coding_on_copilot_data_shows_ais_downward_pressure_on_code_quality)

[^veracode]: Veracode. [2025 GenAI Code Security Report](https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/)

[^stackoverflow]: Stack. [Overflow Developer Survey 2025 — AI Trust Data](https://survey.stackoverflow.co/2025/ai)

[^dora]: DORA. [Accelerate State of DevOps Report 2024](https://dora.dev/research/2024/dora-report/)

[^lemkin]: Jason. [Lemkin Replit AI Database Deletion Incident, Fortune, July 2025](https://fortune.com/2025/07/23/ai-coding-tool-replit-wiped-database-called-it-a-catastrophic-failure/)

[^claude-md]: Anthropic. [Claude Code Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices)

[^plan-mode]: Anthropic. [Claude Code Documentation](https://code.claude.com/docs/en/overview)

[^claude-md-practices]: HumanLayer. [Writing a good CLAUDE.md](https://www.humanlayer.dev/blog/writing-a-good-claude-md)

[^boris-workflow]: VentureBeat. [Claude Code Creator Workflow](https://venturebeat.com/technology/the-creator-of-claude-code-just-revealed-his-workflow-and-developers-are)

---

[← Previous: Skills, Commands, Agents, SDK — The Vocabulary](./03-skills-commands-agents-sdk.md) | [Chapter Overview](./README.md) | [Next: The Human-AI Development Loop →](./05-the-human-ai-development-loop.md)
