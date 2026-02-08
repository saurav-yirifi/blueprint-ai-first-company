# Skills, Commands, Agents, SDK — The Vocabulary

Understanding the capabilities of modern AI coding tools.

---

<div class="yirifi-anchor" markdown>

> "Once you understand skills vs commands vs agents, you stop fighting the tool and start designing workflows. The vocabulary isn't just semantics—it's the difference between productive collaboration and frustrating misuse."

**The structural insight:** At Yirifi, we require every developer to understand these distinctions before using agentic tools. Misunderstanding them leads to either underutilizing capabilities (asking agents to do skill-level work) or overestimating them (expecting agents to do things they can't).

</div>

Most developers treat AI coding tools as "talk to the AI and hope for the best." That approach underutilizes capabilities and misses distinctions that matter. The vocabulary matters because each concept maps to a different interaction mode. Mix them up, and you'll either ask for too little or too much.

## Skills: The Atomic Capabilities

Skills are what your AI coding tool can actually do—the atomic operations. File editing. Shell execution. Web search. Code grep. Database queries through MCP connections.

MCP has become the standard for AI-tool integration—over 10,000 active servers and 97 million monthly SDK downloads, now backed by Anthropic, OpenAI, Google, and Microsoft[^mcp-stats]. Instead of copying data into prompts, you give the AI direct access.

In practice: a developer using Supabase MCP says: "Add a created_at timestamp to the workouts table." Claude Code creates a temporary database branch, tests the migration, and on confirmation applies it to production—what previously required five minutes of context-switching now takes two[^supabase-workflow]. The traditional workflow collapses into a single conversation.

Skills themselves are becoming standardized. Anthropic published Agent Skills as an open standard in December 2025—cross-platform skill definitions that work across Claude Code, Cursor, Goose, and other tools[^agent-skills-standard]. A skill is a directory with a SKILL.md file containing YAML frontmatter (name and description required) plus whatever instructions and resources the agent needs. Claude Code discovers these automatically from your filesystem. Write a skill once, use it everywhere your agents run.

Remotion Skills demonstrates this pattern at scale. A Claude Code skill teaches the agent Remotion's animation APIs, timing patterns, and rendering best practices. A developer describes a marketing video in natural language; Claude Code writes React components; Remotion renders the video file. "No After Effects. No Premiere Pro. No hiring."[^remotion-skill] Skills turn domain expertise into reusable capability.

No amount of clever prompting makes an AI do something outside its skill set. Before asking "why won't it do X," check whether X requires a skill the tool actually has.

## Commands: Your Shortcuts

Commands are the workflows you define—aliases, macros, shortcuts. Skills are built-in capabilities; commands are your custom triggers for sequences of actions.

At Yirifi, we've built commands for repeated patterns: `/microsite` scaffolds our standard Flask site structure—three-layer backend, HTMX frontend, MCP-exposed APIs. `/review` runs our code review checklist against the diff. `/deploy` handles the full deployment pipeline. Here's the rule: every time you type the same instructions twice, create a command. We have dozens now, and each one saves minutes per use across the team.

Good commands are specific and keyword-rich. "Helps with documents" is useless. "Generates API documentation following OpenAPI 3.0 spec with examples for each endpoint" tells the AI exactly what you want.

## Agents: Autonomous Execution

Agents are the capability most misunderstood—and where confusion causes the most damage. Claude Code now has 115,000 developers processing 195 million lines of code weekly[^claude-code-stats]—but many misuse the agent capabilities.

An agent is goal-oriented, tool-using, iterative, and bounded. You give it an objective. It plans. It executes using available skills. It evaluates results. It adjusts. When you ask an agent to "build the authentication flow," you're defining the goal and letting it figure out the path—reading existing code, writing new files, running tests, fixing failures, repeating.

Subagents add another layer—isolated instances spun up for specific tasks. In Claude Code, each subagent gets its own context window and persona. Need to audit security while checking test coverage? Spin up two subagents working in parallel. The orchestrating agent maintains the global plan while subagents dive deep into focused subtasks, returning compact summaries rather than full context[^claude-subagents]. This isn't just parallel processing—it's context isolation that prevents one task from polluting another.

Here's where the trust calibration from [Section 1](./01-the-5-levels-of-ai-assisted-development.md) gets concrete. I've watched developers swing between over-trusting (expecting agents to make architectural decisions) and under-trusting (manually doing what the agent could handle). Start with smaller tasks. Expand scope as confidence builds.

A failure example from Yirifi: a developer asked an agent to "refactor the authentication system." The agent happily rewrote files across the codebase, broke three integrations, and produced code that compiled but failed silently in production. The mistake: treating an architectural task (requiring human judgment about system boundaries) as an implementation task (suitable for agent autonomy). Despite 84% of developers using AI tools, agentic coding "isn't fully trusted at this point"[^trust-gap].

## Hooks: Execution Checkpoints

Hooks are the middle ground between using AI tools and building with them—custom code at specific execution points without requiring a full integration. Claude Code supports hooks for pre-edit formatting, post-edit validation, pre-shell security checks, and session notifications[^claude-code-docs].

At Yirifi, our hook configuration auto-formats Python files after every edit and requires approval for any command touching production databases. Security checks before shell commands. Code formatting after every edit. Compliance logging for audit trails. These aren't optional guardrails—they're architectural enforcement of patterns that otherwise require discipline.

TDD Guard exemplifies hook-driven discipline. The hook intercepts file modifications, blocks implementation without failing tests, and prevents over-implementation beyond test requirements[^tdd-guard]. With 1,000+ GitHub stars and 15,000 npm downloads, it's enforcement that doesn't rely on developer memory—the hook catches violations before they happen.

## Memory Files: Persistent Context

Memory files like CLAUDE.md encode project conventions that persist across sessions—test commands, architecture decisions, directory layout, coding standards[^claude-best-practices]. Every Yirifi microsite has one. Instead of re-explaining context at the start of each session, the agent reads the memory file and knows how this project works.

This is context-first pattern (see [Pattern 1](./04-the-8-patterns-for-effective-ai-coding.md)) made permanent. The thirty seconds of context that used to start every session becomes zero seconds because it's already there.

## SDK: Build Your Own

SDKs let you go beyond using AI tools to building with them. Custom integrations for proprietary systems. Specialized agents for domain-specific workflows. Quality gates that enforce standards automatically.

The Claude Agent SDK—the same harness powering Claude Code—provides access to the same tools, context management systems, and permissions frameworks for building custom agents[^claude-agent-sdk]. Python and TypeScript SDKs are available, enabling everything from simple automations to sophisticated multi-agent systems.

The landscape is maturing fast. In December 2025, the Linux Foundation established the Agentic AI Foundation with MCP, OpenAI's AGENTS.md, and Block's goose as founding projects[^linux-foundation]. Agent Skills—a standard for cross-platform skill definitions—has been adopted by Microsoft, Cursor, Goose, and more[^agent-skills]. AGENTS.md already appears in over 60,000 open source projects.

The obra/superpowers framework bundles 20+ battle-tested skills—TDD enforcement, systematic debugging (4-phase root cause: reproduce, isolate, identify, verify), parallel subagent workflows[^superpowers]. Some skills are rigid (TDD, debugging—follow exactly) and others flexible (collaboration patterns—adapt to context). The skill itself tells you which. "It's not uncommon for Claude to work autonomously for a couple hours at a time without deviating from the plan you put together."

Use existing tools for common workflows, build custom tools for proprietary or high-volume needs. The SDK investment pays off when you run the same workflow hundreds of times.

The vocabulary isn't just semantics. It's the mental model that determines whether you collaborate effectively with AI tools or fight against their nature.

---

## References

[^mcp-stats]: Model. [Context Protocol One Year Anniversary, November 2025](https://blog.modelcontextprotocol.io/posts/2025-11-25-first-mcp-anniversary/)

[^supabase-workflow]: Supabase. [MCP Server Guide, 2025](https://agnost.ai/blog/supabase-mcp-server-complete-guide)

[^claude-code-stats]: Claude. [Code reaches 115,000 developers, July 2025](https://ppc.land/claude-code-reaches-115-000-developers-processes-195-million-lines-weekly/)

[^trust-gap]: RedMonk. [analysis on agentic coding adoption, December 2025](https://redmonk.com/kholterhoff/2025/12/22/10-things-developers-want-from-their-agentic-ides-in-2025/)

[^linux-foundation]: Linux. [Foundation Announces the Formation of the Agentic AI Foundation, December 2025](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation)

[^agent-skills]: Agent Skills:. [Anthropic's Next Bid to Define AI Standards, The New Stack](https://thenewstack.io/agent-skills-anthropics-next-bid-to-define-ai-standards/)

[^agent-skills-standard]: Anthropic. [Agent Skills - Equipping Agents for the Real World](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)

[^claude-subagents]: Anthropic. [Subagents in the SDK](https://platform.claude.com/docs/en/agent-sdk/subagents)

[^claude-code-docs]: Anthropic. [Claude Code Documentation](https://code.claude.com/docs/en/overview)

[^claude-best-practices]: Anthropic. [Claude Code Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices)

[^claude-agent-sdk]: Anthropic. [Building Agents with the Claude Agent SDK](https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk)

[^remotion-skill]: Remotion. [Building with Remotion and AI](https://www.remotion.dev/docs/ai/claude-code)

[^tdd-guard]: nizos/tdd-guard. [GitHub](https://github.com/nizos/tdd-guard)

[^superpowers]: obra/superpowers. [GitHub](https://github.com/obra/superpowers)

---

[← Previous: Tool Decision Framework](./02-tool-decision-framework.md) | [Chapter Overview](./README.md) | [Next: The 8 Patterns for Effective AI Coding Sessions →](./04-the-8-patterns-for-effective-ai-coding.md)
