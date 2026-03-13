#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "usage: $0 <agent-dir>" >&2
  exit 1
fi

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
AGENT_NAME="$1"
AGENT_DIR="$(cd "$ROOT/$AGENT_NAME" && pwd)"

if [[ ! -f "$AGENT_DIR/AGENTS.md" ]]; then
  echo "missing AGENTS.md in $AGENT_DIR" >&2
  exit 1
fi

# ── Datetime-stamped run identity ────────────────────────────────
RUN_DATETIME="$(date +%Y-%m-%dT%H-%M)"
RUN_SLUG="${AGENT_NAME//\//_}"
RUN_ID="${RUN_SLUG}_${RUN_DATETIME}"

# Per-run log in run-history
HISTORY_DIR="$ROOT/runtime/run-history"
mkdir -p "$HISTORY_DIR"
echo "agent=$AGENT_NAME start=$(date -Iseconds)" >"$HISTORY_DIR/$RUN_ID.log"
# ─────────────────────────────────────────────────────────────────

cd "$AGENT_DIR"

# ── Telegram helper ─────────────────────────────────────────────
SEND_TG="$ROOT/scripts/send-telegram.sh"
tg_enabled() {
  [[ -n "${TELEGRAM_BOT_TOKEN:-}" && -n "${TELEGRAM_CHAT_ID:-}" && -x "$SEND_TG" ]]
}

tg_send() {
  if tg_enabled; then
    "$SEND_TG" "$@" || true   # never let a notification failure kill the run
  fi
}
# ────────────────────────────────────────────────────────────────

PROMPT_FILE="$(mktemp)"
trap 'rm -f "$PROMPT_FILE"' EXIT

cat >"$PROMPT_FILE" <<EOF
You are running as an autonomous company role inside the repository at:
$ROOT

Your current role folder is:
$AGENT_DIR

Your agent runtime name is:
$AGENT_NAME

Execution requirements:
- Read and obey your local AGENTS.md first.
- Use Redmine on every execution.
- This company is Redmine-native. Role-local inbox/outbox/reports/memory directories are legacy artifacts, not the primary workflow.
- Before substantive work, check the relevant Redmine issue set and the Redmine wiki page titled Company.
- If substantive work has no Redmine issue yet, create one or record a concrete escalation that Redmine access is blocked.
- Before finishing, sync any changed status, owner, blocker, scope, or durable decision back to Redmine.
- Use token-efficient discovery before opening repository documents.
- Prefer Redmine and shared repository sources over role-local historical files.
- Create useful outputs on every run unless genuinely blocked.
- Do not create new role-local reports/outbox/memory files unless a migration step explicitly requires them.
- If a needed role is missing or inactive, create a task in shared/company-data/tasks and note it in your report.
- If you make file changes, commit them in this repository with the prefix [$AGENT_NAME]: followed by a concise summary.
- If your commit succeeds, push it to origin unless the repo state makes that unsafe.
- Before any commit, inspect local git status and avoid touching unrelated files outside your role or shared company docs.
- If git push fails because the remote moved, report the failure in your local outputs and stop rather than force-pushing.

Telegram reporting — IMPORTANT:
- A Telegram notification tool is available at: $ROOT/scripts/send-telegram.sh
- You can call it like: bash $ROOT/scripts/send-telegram.sh "your message"
- At the START of your run, after you have read your key files, send a Telegram message summarizing:
  - Your role name
  - Which files you read (list them concisely)
  - What your current focus / priority is based on what you read
- At the END of your run, after completing your work, send a final Telegram message summarizing:
  - What actions you took (files created, decisions made, delegations issued)
  - Any blockers or escalations
  - What the next run should focus on
- Keep Telegram messages concise — bullet points, not paragraphs.
- If the send-telegram script fails, continue your work normally. Notifications are best-effort.

Read this role specification now and then continue working with Redmine as the primary execution surface:
EOF

cat "$AGENT_DIR/AGENTS.md" >>"$PROMPT_FILE"

# ── Notify: agent run starting ──────────────────────────────────
tg_send "🟢 *[$AGENT_NAME]* run starting"
# ────────────────────────────────────────────────────────────────

AUTH_STATUS=""
if AUTH_STATUS="$(codex login status 2>/dev/null)"; then
  :
elif [[ -n "${OPENAI_API_KEY:-}" ]]; then
  echo "$OPENAI_API_KEY" | codex login --with-api-key >/dev/null 2>&1 || true
  if ! AUTH_STATUS="$(codex login status 2>/dev/null)"; then
    echo "error: failed to authenticate Codex with OPENAI_API_KEY" >&2
    tg_send "❌ *[$AGENT_NAME]* failed — Codex API-key login failed"
    exit 1
  fi
else
  echo "error: Codex is not logged in and OPENAI_API_KEY is not set" >&2
  tg_send "❌ *[$AGENT_NAME]* failed — no Codex login or OPENAI_API_KEY"
  exit 1
fi

codex exec --dangerously-bypass-approvals-and-sandbox - <"$PROMPT_FILE"
EXIT_CODE=$?

# ── Notify: agent run finished ──────────────────────────────────
if [[ $EXIT_CODE -eq 0 ]]; then
  tg_send "✅ *[$AGENT_NAME]* run completed successfully"
else
  tg_send "❌ *[$AGENT_NAME]* run failed (exit $EXIT_CODE)"
fi
# ────────────────────────────────────────────────────────────────

exit $EXIT_CODE
# 
