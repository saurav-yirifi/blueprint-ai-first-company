# CI AI Review

> How to set up AI-powered pull request reviews in your CI pipeline. This example uses GitHub Actions to automatically review every PR for correctness, security, and adherence to project conventions.
>
> Reference: [Pattern 8: Review Ruthlessly](../../../book/part-2-building/05-building-with-ai/04-the-8-patterns-for-effective-ai-coding.md) | [Code Review Agent](../../prompts/agent-system-prompts/code-review-agent.md)

## What's in This Example

| File | Purpose |
|------|---------|
| `.github/workflows/ai-review.yml` | GitHub Actions workflow triggered on PR events |
| [review-config.yaml](review-config.yaml) | Review configuration (severity thresholds, ignored files, custom rules) |
| [prompts/review-prompt.md](prompts/review-prompt.md) | The review prompt template sent to the AI model |

## How It Works

```
PR Opened/Updated
      |
      v
GitHub Actions Trigger
      |
      v
Fetch PR diff + changed files
      |
      v
Load review-config.yaml
      |
      v
Send diff + review prompt to AI model
      |
      v
Parse AI response into findings
      |
      v
Post findings as PR review comments
      |
      v
Set review status (approve / request changes)
```

## Setup Steps

### 1. Add the Workflow

Copy `.github/workflows/ai-review.yml` to your repository's `.github/workflows/` directory.

### 2. Configure Secrets

Add these secrets to your GitHub repository (Settings > Secrets and Variables > Actions):

| Secret | Required | Description |
|--------|----------|-------------|
| `ANTHROPIC_API_KEY` | Yes | API key for Claude |
| `REVIEW_GITHUB_TOKEN` | No | GitHub token with PR comment access (uses `GITHUB_TOKEN` by default) |

### 3. Customize the Configuration

Edit `review-config.yaml` to match your project:

- Set severity thresholds for blocking vs non-blocking findings
- Add file patterns to ignore (generated code, vendored dependencies)
- Add project-specific review rules
- Configure which finding categories to check

### 4. Customize the Prompt

Edit `prompts/review-prompt.md` to include your project's specific conventions, architecture decisions, and security requirements.

### 5. Test with a PR

Open a test PR to verify the workflow runs and posts comments correctly. Check the Actions tab for any configuration errors.

## What Gets Reviewed

By default, the workflow reviews:

- All files changed in the PR
- Excluding patterns in `review-config.yaml` (e.g., `*.lock`, `*.generated.*`)

The review checks for:

- **Security:** Injection vulnerabilities, hardcoded secrets, missing auth checks
- **Correctness:** Logic errors, unhandled edge cases, broken error handling
- **Performance:** N+1 queries, unbounded loops, missing timeouts
- **Conventions:** Violations of project-specific rules from the review config

## Review Verdicts

| Verdict | When | Effect |
|---------|------|--------|
| APPROVE | No CRITICAL or WARNING findings | PR is approved (human review still needed) |
| REQUEST_CHANGES | Any CRITICAL finding | PR is blocked until fixed |
| COMMENT | WARNING findings but no CRITICAL | PR is not blocked, issues noted |

## Limitations

- AI review is an assistant, not a replacement for human review. The workflow footer always states this.
- Review quality depends on the prompt and context provided. Keep the review prompt updated as your project evolves.
- The AI may produce false positives. Configure the severity thresholds to balance noise vs coverage.
- Large PRs (500+ lines) produce less accurate reviews. Consider enforcing PR size limits.

## Cost Estimation

Approximate cost per PR review (varies by PR size):

| PR Size | Input Tokens | Output Tokens | Estimated Cost |
|---------|-------------|---------------|----------------|
| Small (< 100 lines) | ~2,000 | ~500 | ~$0.03 |
| Medium (100-300 lines) | ~5,000 | ~1,000 | ~$0.08 |
| Large (300-500 lines) | ~10,000 | ~2,000 | ~$0.15 |

For a team producing 50 PRs per week, expect approximately $4-8 per week in API costs.

## Related Resources

- [Code Review Agent System Prompt](../../prompts/agent-system-prompts/code-review-agent.md) -- the full system prompt for a review agent
- [Review Prompts](../../prompts/coding-prompts/review-prompts.md) -- manual review prompt templates
- [Claude Code Setup](../claude-code-setup/README.md) -- local review configuration
- [8 Patterns for AI Coding](../../../frameworks/09-eight-patterns-for-ai-coding.md) -- the framework this implements
