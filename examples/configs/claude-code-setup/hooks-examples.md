# Hook Configuration Examples

> Examples of Claude Code hook configurations for formatting, validation, security, and notifications. Hooks execute custom code at specific points in the Claude Code workflow.
>
> Reference: [Skills, Commands, Agents, SDK](../../../book/part-2-building/05-building-with-ai/03-skills-commands-agents-sdk.md)

## What Are Hooks?

Hooks are custom code that runs at specific execution points without requiring a full integration. Claude Code supports hooks for:

- **Pre-edit:** Run before a file is modified
- **Post-edit:** Run after a file is modified
- **Pre-shell:** Run before a shell command executes
- **Post-shell:** Run after a shell command executes
- **Session notifications:** Run when sessions start or end

Hooks are the middle ground between using AI tools and building with them. They enforce patterns that otherwise require developer discipline.

---

## Hook Configuration File

Hooks are configured in `.claude/hooks.json` in your project root:

```json
{
  "hooks": {
    "post-edit": [
      {
        "name": "auto-format",
        "description": "Auto-format files after every edit",
        "command": "auto-format.sh",
        "match": ["*.py", "*.ts", "*.tsx"]
      },
      {
        "name": "validate-migrations",
        "description": "Verify database migrations have downgrade logic",
        "command": "validate-migration.sh",
        "match": ["migrations/*.py"]
      }
    ],
    "pre-shell": [
      {
        "name": "security-check",
        "description": "Block dangerous commands",
        "command": "security-check.sh"
      }
    ]
  }
}
```

---

## Example 1: Auto-Format After Edits

Run code formatters automatically after every file modification. This ensures AI-generated code always matches your project's style without manual intervention.

**Hook script:** `.claude/hooks/auto-format.sh`

```bash
#!/bin/bash
# Auto-format files after AI edits

FILE="$1"
EXTENSION="${FILE##*.}"

case "$EXTENSION" in
  py)
    ruff format "$FILE" 2>/dev/null
    ruff check --fix "$FILE" 2>/dev/null
    ;;
  ts|tsx|js|jsx)
    npx prettier --write "$FILE" 2>/dev/null
    npx eslint --fix "$FILE" 2>/dev/null
    ;;
  go)
    gofmt -w "$FILE" 2>/dev/null
    ;;
  rs)
    rustfmt "$FILE" 2>/dev/null
    ;;
esac

exit 0
```

**Why this matters:** From Pattern 2 (Concrete Examples): "Never use an LLM for what a linter can do; linters are faster and cheaper." This hook lets the AI focus on logic while the formatter handles style.

---

## Example 2: Security Check Before Shell Commands

Require approval for commands that touch sensitive systems. This implements the three-tier access model from [Chapter 4](../../../book/part-2-building/04-infrastructure-for-ai-first-operations/03-the-ai-tool-gateway-pattern.md): free operations run automatically, supervised operations require approval, forbidden operations are blocked.

**Hook script:** `.claude/hooks/security-check.sh`

```bash
#!/bin/bash
# Block or require approval for dangerous shell commands

COMMAND="$1"

# Forbidden commands -- always block
FORBIDDEN_PATTERNS=(
  "rm -rf /"
  "DROP DATABASE"
  "DROP TABLE"
  "TRUNCATE"
  "docker system prune"
  "kubectl delete namespace"
)

for pattern in "${FORBIDDEN_PATTERNS[@]}"; do
  if echo "$COMMAND" | grep -qi "$pattern"; then
    echo "BLOCKED: Command matches forbidden pattern: $pattern"
    exit 1
  fi
done

# Supervised commands -- require explicit approval
SUPERVISED_PATTERNS=(
  "rm -rf"
  "docker compose down"
  "flask db downgrade"
  "git push.*force"
  "git reset --hard"
  "DELETE FROM"
  "UPDATE.*SET"
)

for pattern in "${SUPERVISED_PATTERNS[@]}"; do
  if echo "$COMMAND" | grep -qi "$pattern"; then
    echo "REQUIRES_APPROVAL: Command matches supervised pattern: $pattern"
    exit 2
  fi
done

# Everything else -- allow
exit 0
```

**Access tiers:**

| Tier | Behavior | Examples |
|------|----------|---------|
| Free | Runs automatically | `ls`, `cat`, `git status`, `pytest`, `SELECT` queries |
| Supervised | Requires user approval | `rm -rf`, `git push --force`, `UPDATE` queries |
| Forbidden | Always blocked | `DROP DATABASE`, `rm -rf /`, `TRUNCATE` |

---

## Example 3: Migration Validation After Edits

Verify that database migrations include downgrade logic after every modification to a migration file.

**Hook script:** `.claude/hooks/validate-migration.sh`

```bash
#!/bin/bash
# Ensure database migrations have proper downgrade() logic

FILE="$1"

# Only check Alembic migration files
if [[ ! "$FILE" == migrations/versions/*.py ]]; then
  exit 0
fi

# Check for downgrade function
if ! grep -q "def downgrade" "$FILE"; then
  echo "ERROR: Migration $FILE is missing downgrade() function."
  echo "All migrations must be reversible."
  exit 1
fi

# Check that downgrade is not empty
DOWNGRADE_BODY=$(sed -n '/def downgrade/,/^def \|^$/p' "$FILE" | grep -v "def downgrade" | grep -v "^$" | grep -v "pass")
if [ -z "$DOWNGRADE_BODY" ]; then
  echo "WARNING: Migration $FILE has an empty downgrade() function."
  echo "Downgrade should reverse the upgrade operations."
  exit 1
fi

echo "Migration $FILE validated: upgrade and downgrade present."
exit 0
```

---

## Example 4: Test Enforcement After Edits (TDD Guard)

Block implementation file changes that do not have corresponding failing tests. This enforces test-driven development at the hook level.

**Hook script:** `.claude/hooks/tdd-guard.sh`

```bash
#!/bin/bash
# Enforce TDD: implementation files must have corresponding tests

FILE="$1"

# Only check source files, not test files
if [[ "$FILE" == tests/* ]] || [[ "$FILE" == test_* ]]; then
  exit 0
fi

# Skip non-Python files (customize for your language)
if [[ ! "$FILE" == *.py ]]; then
  exit 0
fi

# Determine expected test file path
# src/app/services/order_service.py -> tests/unit/services/test_order_service.py
TEST_FILE=$(echo "$FILE" | sed 's|src/app/|tests/unit/|' | sed 's|/\([^/]*\)\.py|/test_\1.py|')

if [ ! -f "$TEST_FILE" ]; then
  echo "WARNING: No test file found at $TEST_FILE"
  echo "Consider writing tests before implementation (Pattern 5: Test-Driven Prompting)"
  # Exit 0 (warning only, not blocking) -- change to exit 1 to make it mandatory
  exit 0
fi

echo "Test file exists: $TEST_FILE"
exit 0
```

**Note:** This is a lightweight version. For full TDD enforcement, see [TDD Guard](https://github.com/nizos/tdd-guard), referenced in the book's Chapter 5.

---

## Example 5: Session Notification

Notify your team channel when long-running Claude Code sessions complete.

**Hook script:** `.claude/hooks/session-notify.sh`

```bash
#!/bin/bash
# Notify when a Claude Code session ends
# Useful for long-running background agent tasks

SESSION_DURATION="$1"  # Duration in seconds
SESSION_SUMMARY="$2"   # Summary of changes made

# Only notify for sessions longer than 5 minutes
if [ "$SESSION_DURATION" -lt 300 ]; then
  exit 0
fi

MINUTES=$((SESSION_DURATION / 60))

# Slack webhook notification
curl -s -X POST "${SLACK_WEBHOOK_URL}" \
  -H 'Content-type: application/json' \
  -d "{
    \"text\": \"Claude Code session completed (${MINUTES} minutes)\",
    \"blocks\": [
      {
        \"type\": \"section\",
        \"text\": {
          \"type\": \"mrkdwn\",
          \"text\": \"*Claude Code Session Complete*\nDuration: ${MINUTES} minutes\nSummary: ${SESSION_SUMMARY}\"
        }
      }
    ]
  }" > /dev/null

exit 0
```

---

## Setting Up Hooks

1. Create the hooks directory:
   ```bash
   mkdir -p .claude/hooks
   ```

2. Add your hook scripts and make them executable:
   ```bash
   chmod +x .claude/hooks/*.sh
   ```

3. Create the hooks configuration:
   ```bash
   # Create .claude/hooks.json with your configuration
   ```

4. Commit to version control:
   ```bash
   git add .claude/
   git commit -m "Add Claude Code hook configurations"
   ```

## Related Resources

- [CLAUDE.md Example](CLAUDE.md) -- the project memory file hooks reference
- [Example Skills](example-skills/code-review.md) -- custom skill configurations
- [CI AI Review](../ci-ai-review/README.md) -- automated review in CI (complements local hooks)
