# Claude Code Setup

> How to set up Claude Code for your project, including the CLAUDE.md memory file, custom skills, and hook configurations. Based on [Chapter 5: Building with AI](../../../book/part-2-building/05-building-with-ai/README.md) and the [8 Patterns for Effective AI Coding](../../../frameworks/09-eight-patterns-for-ai-coding.md).

## What's in This Example

| File | Purpose |
|------|---------|
| [CLAUDE.md](CLAUDE.md) | Example project memory file -- the persistent context that makes Pattern 1 automatic |
| [example-skills/code-review.md](example-skills/code-review.md) | A custom skill for AI-assisted code review |
| [example-skills/test-runner.md](example-skills/test-runner.md) | A custom skill for running and analyzing test results |
| [hooks-examples.md](hooks-examples.md) | Hook configurations for formatting, validation, and security |

## Why CLAUDE.md Matters

From [Pattern 1: Context First](../../../book/part-2-building/05-building-with-ai/04-the-8-patterns-for-effective-ai-coding.md):

> Tools like Claude Code's CLAUDE.md files codify context permanently -- project conventions, architecture decisions, test commands, directory layout that persist across sessions. Instead of thirty seconds per session, you invest once and reap forever.

The consensus: under 300 lines, shorter is better. Include bash commands, code style rules, testing instructions. Prefer file:line references over code snippets (snippets become outdated). Never use an LLM for what a linter can do.

## Setup Steps

### 1. Create Your CLAUDE.md

Copy the [example CLAUDE.md](CLAUDE.md) and customize it for your project:

```bash
# Copy the template to your project root
cp CLAUDE.md /path/to/your/project/CLAUDE.md
```

Edit the file to include:
- Your tech stack and project structure
- Build, test, and deployment commands
- Coding conventions (what the linter does not cover)
- Architecture decisions that affect how code should be written
- Common pitfalls specific to your codebase

### 2. Add Custom Skills

Create a `.claude/skills/` directory in your project:

```bash
mkdir -p .claude/skills
```

Each skill is a directory with a `SKILL.md` file. See the [example-skills](example-skills/code-review.md) directory for templates.

Skills are automatically discovered by Claude Code from your filesystem. Write a skill once, use it in every session.

### 3. Configure Hooks

Hooks execute custom code at specific points in the Claude Code workflow. See [hooks-examples.md](hooks-examples.md) for configurations covering:
- Auto-formatting after edits
- Security checks before shell commands
- Validation after file modifications
- Session notifications

### 4. Set Up Team Standards

For team-wide consistency, commit your CLAUDE.md and skills to version control:

```bash
git add CLAUDE.md .claude/
git commit -m "Add Claude Code configuration and skills"
```

Every team member gets the same project context and custom capabilities automatically.

## Scope Hierarchy

Claude Code reads configuration files at three levels:

| Level | File Location | Scope |
|-------|--------------|-------|
| Project | `CLAUDE.md` in project root | Everyone working on this project |
| Directory | `CLAUDE.md` in subdirectories | Overrides for specific areas |
| User | `~/.claude/CLAUDE.md` | Personal preferences across all projects |

Project-level settings are the most important. They ensure every developer (and every AI session) starts with the same context.

## Related Resources

- [Coding Prompts](../../prompts/coding-prompts/README.md) -- prompts to use within Claude Code sessions
- [CI AI Review](../ci-ai-review/README.md) -- automate code review in your CI pipeline
- [8 Patterns for AI Coding](../../../frameworks/09-eight-patterns-for-ai-coding.md) -- the framework these configurations implement
- [Skills, Commands, Agents, SDK](../../../book/part-2-building/05-building-with-ai/03-skills-commands-agents-sdk.md) -- vocabulary for working with Claude Code
