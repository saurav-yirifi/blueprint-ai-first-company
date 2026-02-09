# Workflow: Agent Failure Recovery

> A step-by-step workflow for diagnosing and recovering from agent failures, organized by the seven failure modes.

*Based on [Chapter 6: Agent Architecture](../book/part-2-building/06-agent-architecture/README.md)*

---

## When to Use This Workflow

Use this when an agent is behaving incorrectly, has stopped producing expected output, is consuming abnormal resources, or has triggered an alert. Agent failures follow different patterns than traditional software because agents reason probabilistically and act autonomously. This workflow helps you classify the failure quickly so you apply the right fix.

---

## The Workflow

### Step 1: Stop the Bleeding

Before diagnosing, contain the damage.

- **Agent actively running and causing harm:** Activate the kill switch. Diagnose after.
- **Agent has stopped:** Confirm nothing downstream is still processing its last outputs.
- **Unsure:** Pause the agent. A paused agent wastes idle time. A running broken agent wastes everything else.

### Step 2: Classify and Recover by Failure Mode

Pull the agent's recent logs and match symptoms to the correct mode below.

**Mode 1: Hallucinated Actions.** Logs show 404 errors, "unknown tool" rejections, or references to non-existent policies. Recovery: review failed calls against the tool registry, tighten the system prompt to reference only registered tools, add validation that rejects any unregistered tool call before execution.

**Mode 2: Infinite Loops.** Token usage climbing steadily, same tool calls repeating in logs, task running far longer than expected. Recovery: terminate the task, identify the loop pattern, add exponential backoff for API retries and progress checks that require forward movement after N iterations.

**Mode 3: Scope Creep.** Agent modified files, records, or systems outside the task scope, or agreed to requests it should have refused. Recovery: identify and revert out-of-scope changes, tighten "done when" criteria, restrict permissions to the minimum required, test with adversarial inputs.

**Mode 4: Context Loss.** Agent contradicted earlier statements, re-asked for provided information, or ignored previously established constraints. Recovery: for chat agents, trigger a context summary and confirm with the user. For background agents, roll back to the last checkpoint. Add automatic summarization every 10 turns.

**Mode 5: Cascading Failures.** Multiple agents or systems failed in sequence, with downstream effects spreading beyond the original agent. Recovery: isolate all affected agents, trace the failure chain to the root cause, fix the root cause first, validate downstream data, restart agents one at a time.

**Mode 6: Resource Exhaustion.** Token usage, compute, or costs spiked beyond expected levels. Recovery: terminate or pause the task, audit cost breakdown by tool call, optimize expensive operations or break broad tasks into smaller pieces, set or adjust token budgets.

**Mode 7: Stale Data.** Agent made decisions correct for a previous state but wrong now -- API schemas changed, data is outdated. Recovery: identify the stale source, refresh and validate, rerun the task, add freshness checks before acting.

> **Tip:** Do not assume the first symptom is the root cause. Resource exhaustion is often caused by an infinite loop. Context loss can look like hallucinated actions. Classify carefully.

### Step 3: Post-Incident Review

Every failure is a training example. After recovery:

1. Document the incident: what happened, when, impact, resolution
2. Classify the failure mode using the categories above
3. Add a test case that reproduces the failure
4. Update monitoring to detect this pattern earlier
5. Update the agent's configuration with new guardrails

---

## Tips

- **Chat agents** are most vulnerable to Modes 1, 3, and 4 (hallucinated actions, scope creep, context loss).
- **Background agents** are most vulnerable to Modes 2, 5, 6, and 7 (infinite loops, cascading failures, resource exhaustion, stale data).
- **The kill switch isn't a failure.** It is the system working as designed.
- **Post-incident reviews aren't optional.** Teams that treat every failure as a learning opportunity build agents that fail less. Teams that fix and forget repeat the same failures.

## Related Resources

- [7 Failure Modes of Agents](../frameworks/10-seven-failure-modes-of-agents.md) -- The complete framework with real-world incidents for each mode
- [Agent Design Checklist](../checklists/agent-design-checklist.md) -- Pre-deployment checklist to prevent these failures
- [Agent Patterns Examples](../examples/agent-patterns/README.md) -- Reference implementations with built-in failure handling
