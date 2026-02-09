# Review Prompts

> Prompts for AI-assisted code review. These implement **Pattern 8: Review Ruthlessly** from the [8 Patterns for Effective AI Coding](../../../book/part-2-building/05-building-with-ai/04-the-8-patterns-for-effective-ai-coding.md).

Review AI code as if you are reviewing a junior developer who thinks they are a senior. Only 55% of AI-generated code is secure. XSS vulnerabilities appear 86% of the time. SQL injection 20%. Trust dropped to 33% in 2025. The skepticism is warranted.

---

## Prompt 1: Comprehensive Code Review

**When to use:** Reviewing a complete feature or pull request for correctness, security, performance, and style.

**Pattern:** Review Ruthlessly + Context First

```
Review the following code changes. This is a {new feature / bug fix / refactor}
for {brief description of what it does}.

Code to review:
---
{Paste the diff or the new code}
---

Project conventions:
- {e.g., All functions include type hints}
- {e.g., Error handling follows the Result pattern, not exceptions}
- {e.g., SQL queries use parameterized statements, never string interpolation}

Review for:

1. **Correctness**: Does the code do what it claims? Are there logic errors,
   off-by-one errors, or incorrect assumptions?

2. **Security**: Check for injection vulnerabilities (SQL, XSS, command),
   hardcoded secrets, insecure defaults, missing input validation, and
   improper authentication/authorization checks.

3. **Performance**: Are there N+1 queries, unnecessary allocations, missing
   indexes, or operations that won't scale?

4. **Style**: Does the code follow the project conventions listed above?
   Are names clear? Is the code readable to someone unfamiliar with it?

5. **Edge cases**: What inputs, states, or conditions would cause this
   code to break?

Format your review as:
- CRITICAL: Issues that must be fixed before merge
- WARNING: Issues that should be addressed but are not blockers
- SUGGESTION: Improvements that would make the code better
- POSITIVE: Things done well (reinforce good patterns)
```

**Tips:**
- Including project conventions makes the review specific rather than generic. "Follow best practices" produces noise. "All functions include type hints" produces actionable feedback.
- The four-level severity format (CRITICAL/WARNING/SUGGESTION/POSITIVE) prevents the review from being either too lenient or too harsh. It also makes it easy to filter to what matters.
- Explicitly mentioning security checks surfaces issues the AI might not flag on its own. The AI is good at finding security problems when prompted to look.

---

## Prompt 2: Security-Focused Review

**When to use:** Code that handles user input, authentication, database queries, file operations, or external API calls.

**Pattern:** Review Ruthlessly + Error Escalation

```
Perform a security-focused review of this code. It handles
{user input / authentication / database access / file operations}.

Code:
---
{Paste the code}
---

Check specifically for:

1. **Injection**: SQL injection, XSS, command injection, LDAP injection,
   template injection. Are all inputs sanitized or parameterized?

2. **Authentication/Authorization**: Are auth checks present on every
   protected path? Can auth be bypassed through parameter manipulation?

3. **Data Exposure**: Are sensitive fields filtered from responses? Are
   error messages leaking internal details? Are logs capturing secrets?

4. **Input Validation**: Are all inputs validated for type, length, range,
   and format? What happens with null, empty, or oversized inputs?

5. **Dependencies**: Are we using known-vulnerable versions of any library?
   Are we importing more than we need?

For each finding:
- Describe the vulnerability
- Show a concrete attack scenario
- Provide the fix
- Rate severity: Critical / High / Medium / Low
```

**Tips:**
- Always run this prompt on code that touches user input or auth boundaries. This is where AI-generated code is most dangerous.
- "Show a concrete attack scenario" makes vulnerabilities tangible. An abstract warning like "possible XSS" is easy to ignore. "An attacker could inject `<script>document.cookie</script>` via the name field" is not.
- This prompt pairs well with the Edge Case Expansion prompt in [Test-Driven Prompts](test-driven-prompts.md). After identifying security issues, write tests that verify the fixes.

---

## Prompt 3: Before-After Review

**When to use:** The AI has refactored or rewritten existing code, and you need to verify it preserved all original behavior.

**Pattern:** Review Ruthlessly + Checkpoint Commits

```
I asked the AI to {describe the change that was requested}.

Here is the ORIGINAL code:
---
{Paste original code}
---

Here is the NEW code:
---
{Paste AI-generated replacement}
---

Compare the two versions and answer:

1. **Behavior preservation**: List every behavior in the original. For
   each one, confirm it exists in the new version or flag it as missing.

2. **Unintended changes**: Has the new code changed any behavior that
   was not part of the requested change? List every difference.

3. **Added behavior**: Has the new code added functionality that was not
   requested? If so, is it appropriate or is it over-engineering?

4. **Error handling**: Does the new code handle errors the same way as
   the original? Are any error paths missing?

5. **Side effects**: Does the new code have different side effects
   (logging, database writes, external calls, event emissions)?

If any behavior was lost or unintentionally changed, flag it as CRITICAL.
```

**Tips:**
- This is the most important review prompt for AI-generated refactors. The AI will confidently "improve" code by silently dropping edge case handling, changing error behavior, or adding unnecessary abstractions.
- "List every behavior in the original" is intentionally exhaustive. The goal is to force the AI to read the original carefully before approving its own work.
- Run this review after every AI-generated refactor, not just the ones that look risky. The subtle breakages are in the ones that look correct.

---

## Prompt 4: Performance Review

**When to use:** Code that will run at scale, processes large datasets, or has latency requirements.

**Pattern:** Review Ruthlessly + Architecture Ownership

```
Review this code for performance at scale. It will be called
approximately {frequency} and processes {data volume}.

Code:
---
{Paste the code}
---

Analyze:

1. **Time complexity**: What is the Big-O of the main operations?
   Are there any hidden O(n^2) or worse patterns?

2. **Database queries**: Count the number of queries. Are there N+1
   patterns? Missing indexes? Unnecessary full table scans?

3. **Memory usage**: Are there large objects held in memory unnecessarily?
   Unbounded lists that grow with input size? Missing pagination?

4. **I/O patterns**: Are external calls sequential when they could be
   parallel? Are there missing timeouts? Retry storms?

5. **Caching opportunities**: What results could be cached? What is the
   cache invalidation strategy?

For each issue, provide:
- The specific line or section
- Expected impact at {target scale}
- The recommended fix
- Whether the fix can be deferred or is needed before launch
```

**Tips:**
- Specifying the target frequency and data volume gives the AI concrete constraints. "Runs 1000 times per second on 10M records" produces different advice than "runs once a day on 100 records."
- N+1 queries are the most common AI-generated performance issue. The AI writes correct code that works in development and crashes in production. Always check database query counts.
- "Can be deferred or needed before launch" prevents premature optimization while flagging genuine blockers.

---

## Prompt 5: Review Checklist for Pull Requests

**When to use:** As a final check before approving any pull request, whether the code is human-written or AI-generated.

**Pattern:** Review Ruthlessly

```
Run through this pull request review checklist. Answer yes/no for each
item and explain any "no" answers.

Code to review:
---
{Paste the diff}
---

Checklist:

**Correctness**
- [ ] Does the code do what the PR description claims?
- [ ] Are there tests for the new behavior?
- [ ] Do all existing tests still pass?

**Security**
- [ ] Is user input validated and sanitized?
- [ ] Are there no hardcoded secrets or credentials?
- [ ] Are SQL queries parameterized (no string concatenation)?
- [ ] Are auth checks present on all protected endpoints?

**Quality**
- [ ] Are function and variable names descriptive?
- [ ] Is the code readable without comments explaining what it does?
- [ ] Are there no duplicated blocks of logic?
- [ ] Does error handling follow project conventions?

**Performance**
- [ ] Are there no N+1 query patterns?
- [ ] Are there no unbounded loops or lists?
- [ ] Are external calls properly timed out?

**Operations**
- [ ] Are there appropriate log statements for debugging?
- [ ] Are errors logged with enough context to diagnose?
- [ ] Are there no debug/console statements left in?

Items marked "no" should be resolved before merge.
```

**Tips:**
- Run this checklist on every PR, not just AI-generated ones. It catches common issues regardless of who wrote the code.
- The checklist is intentionally short. A 50-item checklist gets ignored. A 15-item checklist gets used.
- For CI integration, see [CI AI Review](../../configs/ci-ai-review/README.md) to automate this as part of your pull request workflow.

---

## Related Prompts

- [Context Loading](context-loading.md) -- load project context before reviewing
- [Test-Driven Prompts](test-driven-prompts.md) -- write tests that verify review findings
- [Error Escalation Prompts](error-escalation-prompts.md) -- escalate issues found during review
