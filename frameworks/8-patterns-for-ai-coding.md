# The 8 Patterns for Effective AI Coding Sessions

> Eight battle-tested patterns that separate productive AI-assisted development from expensive flailing.

*From [Chapter 5: Building with AI](../book/part-2-building/05-building-with-ai/README.md)*

## Overview

Most developers think they're faster with AI coding tools than they actually are. A randomized controlled trial found developers were 19% slower with AI assistance, but believed they were 20% faster -- a 43-point perception gap. The difference between those who actually get faster and those who just think they do comes down to patterns.

These eight patterns emerged from watching what works and cataloging the disasters when developers ignore them. They aren't theoretical. They are teachable, measurable practices that can be embedded into developer training and code review checklists from day one.

The productivity loss from ignoring these patterns exceeds the time spent learning them. They are the difference between AI as accelerant and AI as liability.

## The Framework

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

```mermaid
flowchart LR
    subgraph Prepare["Prepare"]
        P1["1. Context First"]
        P2["2. Concrete Examples"]
    end

    subgraph Execute["Execute"]
        P3["3. Iterative Refinement"]
        P4["4. Architecture Ownership"]
        P5["5. Test-Driven Prompting"]
    end

    subgraph Recover["Recover"]
        P6["6. Error Escalation"]
        P7["7. Checkpoint Commits"]
    end

    subgraph Verify["Verify"]
        P8["8. Review Ruthlessly"]
    end

    Prepare --> Execute
    Execute --> Recover
    Recover --> Verify
    Verify -->|"Next iteration"| Prepare

    classDef prepareNode fill:#1e6fa5,stroke:#155a85,color:#fff
    classDef executeNode fill:#1a8a52,stroke:#14693e,color:#fff
    classDef recoverNode fill:#c77d0a,stroke:#a06508,color:#fff
    classDef verifyNode fill:#7345b0,stroke:#5b3590,color:#fff

    class P1,P2 prepareNode
    class P3,P4,P5 executeNode
    class P6,P7 recoverNode
    class P8 verifyNode

    style Prepare fill:#1c1c2e,stroke:#155a85,color:#fff
    style Execute fill:#1c1c2e,stroke:#14693e,color:#fff
    style Recover fill:#1c1c2e,stroke:#a06508,color:#fff
    style Verify fill:#1c1c2e,stroke:#5b3590,color:#fff
```

### Pattern 1: Context First

**AI performs dramatically better with background information.** The time spent explaining context pays back tenfold in output quality.

Research shows 150-250 tokens hits the sweet spot for sophisticated models -- enough context to understand the task, not so much that signal drowns in noise. More context doesn't mean better answers. Bounded, specific context does.

Before any coding request, tell the AI: what's the tech stack, what problem you're solving, what constraints exist, and what you've already tried. Tools like Claude Code's CLAUDE.md files codify this context permanently -- project conventions, architecture decisions, test commands, directory layout that persist across sessions. Instead of thirty seconds per session, you invest once and reap forever.

Best practice for CLAUDE.md: under 300 lines, shorter is better. Include bash commands, code style rules, testing instructions. Prefer file:line references over code snippets -- snippets become outdated. Never use an LLM for what a linter can do.

### Pattern 2: Concrete Examples

**Showing beats telling.** AI models are pattern-matching systems -- give them patterns to match.

Instead of "make it look like our other components," paste an example component. Instead of "follow our coding conventions," show a file that demonstrates them. The more specific your examples, the less the AI has to guess.

Keep rules files under 300 lines, make them actionable and measurable. "Use consistent naming" is useless. "Function names use camelCase, component names use PascalCase, constants use SCREAMING_SNAKE_CASE" gives the AI something to work with.

### Pattern 3: Iterative Refinement

**Small, focused requests produce better results than massive ones.**

Whole-module prompting creates problems: the AI "promptly forgot about all these modules" when asked to work on a single piece of a large request. Push beyond context limits and you get placeholders, incomplete implementations, and silent failures.

The iteration rhythm: request a small piece, verify it works, request the next piece, repeat. For a single function, one request. For a complete feature, 5-10 iterations. For multi-file changes, multiple sessions. The discipline feels slower. It's faster.

### Pattern 4: Architecture Ownership

**You decide structure and design. AI implements your decisions. This is non-negotiable.**

Delegating architecture to AI creates problems: 80-90% of AI-generated code suffers from "avoidance of refactors." The AI takes the path of least resistance, which compounds into architectural debt. It doesn't know your system's invariants, your scale requirements, or why that weird pattern exists in the codebase.

The rule: if you can't draw the architecture on a whiteboard, you're not ready to ask AI to implement it. Component boundaries, data models, API contracts, error handling strategies -- these are human decisions. The AI executes them.

### Pattern 5: Test-Driven Prompting

**Describe expected behavior, not implementation details.** Let AI choose the "how" while you define the "what."

Instead of "use a hash map with O(1) lookup," say "it should find items instantly even with 10,000 entries." Instead of "implement with recursion," say "it should handle nested structures of any depth." Behavior descriptions are more robust than implementation prescriptions. The AI may find better approaches than you'd specify.

### Pattern 6: Error Escalation

**When something breaks, let AI try to fix it before taking over.** AI often solves problems you'd spend hours debugging.

The escalation ladder: share the error message, let AI propose a fix, provide more context if still broken. After two or three failed attempts at the same problem, take over manually. The AI is stuck in a loop and won't escape it.

Two common mistakes: developers give up after one failed attempt, missing that AI excels at debugging its own mistakes. Or they keep trying the same approach expecting different results. Know when to let AI iterate and when to step in.

### Pattern 7: Checkpoint Commits

**Commit working states before asking AI to make changes.** This makes rollback trivial when -- not if -- AI goes wrong.

The practice: `git add -A && git commit -m "checkpoint: before AI changes"` before every significant interaction. Before starting a session, after each working change, before experimental requests, before large refactors. Working code is precious. Protect it.

Plan mode enforces this discipline architecturally. Claude Code's plan mode explores the codebase and designs an approach first, getting explicit approval before making any edits. The checkpoint isn't just a commit -- it's a workflow gate that prevents impulsive changes.

### Pattern 8: Review Ruthlessly

**AI code needs the same -- or more -- review rigor as human code.** Only 55% of AI-generated code is secure. XSS vulnerabilities appear 86% of the time. SQL injection 20%. The AI will confidently produce code with subtle bugs, injection risks, hardcoded secrets, and insecure defaults.

Review as if you're reviewing a junior developer who thinks they're a senior. Check correctness, style consistency, security vulnerabilities, performance implications, and edge cases. Trust in AI code dropped to 33% in 2025, down from 43%. The skepticism is warranted.

Self-verification as standard practice: browser automation, bash commands, test suites. Giving the AI a way to verify its own work improves the quality of the final result by 2-3x.

## How to Use This

Make these patterns part of your team's developer training and embed them into code review checklists. Reference the summary table until the patterns become automatic. For established organizations, build them into onboarding. For startups, learn these patterns as you adopt AI coding -- don't skip them because you're moving fast. The patterns aren't overhead; they are the guardrails that prevent AI-generated disasters.

## Related Frameworks

- [7 Mental Models of AI-First](7-mental-models-of-ai-first.md) -- The thinking frameworks that inform these coding patterns
- [Human-AI Collaboration](human-ai-collaboration.md) -- The broader collaboration model these patterns implement
- [7 Failure Modes of Agents](7-failure-modes-of-agents.md) -- What goes wrong when agents operate without guardrails
- [Probabilistic AI](probabilistic-ai.md) -- Why AI outputs require the review rigor in Pattern 8

## Deep Dive

Read the full chapter: [Chapter 5: Building with AI](../book/part-2-building/05-building-with-ai/README.md)
