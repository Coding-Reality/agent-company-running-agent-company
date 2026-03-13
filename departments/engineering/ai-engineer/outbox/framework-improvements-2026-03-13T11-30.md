# Framework Improvement Proposals

- Datetime: 2026-03-13T11:30 UTC
- Author: `departments/engineering/ai-engineer`

## 1. Make `scripts/run-agent.sh` write completion data, not just start data

- Problem:
  - Current run-history logs contain only `agent=<name> start=<timestamp>`.
  - Empty-run rate, completion rate, and failure rate cannot be measured from the runtime logs.

### Current snippet

```bash
# Per-run log in run-history
HISTORY_DIR="$ROOT/runtime/run-history"
mkdir -p "$HISTORY_DIR"
echo "agent=$AGENT_NAME start=$(date -Iseconds)" >"$HISTORY_DIR/$RUN_ID.log"
```

### Proposed snippet

```bash
# Per-run log in run-history
HISTORY_DIR="$ROOT/runtime/run-history"
mkdir -p "$HISTORY_DIR"
RUN_LOG="$HISTORY_DIR/$RUN_ID.log"
echo "agent=$AGENT_NAME start=$(date -Iseconds)" >"$RUN_LOG"
echo "cwd=$AGENT_DIR" >>"$RUN_LOG"

before_reports="$(find "$AGENT_DIR/reports" -maxdepth 1 -type f 2>/dev/null | wc -l | tr -d ' ')"
before_outbox="$(find "$AGENT_DIR/outbox" -maxdepth 1 -type f 2>/dev/null | wc -l | tr -d ' ')"
```

### End-of-run append

```bash
after_reports="$(find "$AGENT_DIR/reports" -maxdepth 1 -type f 2>/dev/null | wc -l | tr -d ' ')"
after_outbox="$(find "$AGENT_DIR/outbox" -maxdepth 1 -type f 2>/dev/null | wc -l | tr -d ' ')"

{
  echo "end=$(date -Iseconds)"
  echo "exit_code=$EXIT_CODE"
  echo "reports_delta=$((after_reports - before_reports))"
  echo "outbox_delta=$((after_outbox - before_outbox))"
} >>"$RUN_LOG"
```

### Why this is worth doing

- Preserves the lightweight shell runner.
- Makes run-history machine-readable enough for empty-run and artifact-rate audits.
- Supports the CEO directive to keep runtime-cost instrumentation active without adding prompt bloat.

## 2. Remove generic success-path Telegram messages from the runner

- Problem:
  - The runner currently sends generic "run starting" and "run completed successfully" messages.
  - Agents are already instructed to send their own start and end summaries after reading and after execution.
  - The extra messages create duplicate notifications with less information.

### Current snippet

```bash
# ── Notify: agent run starting ──────────────────────────────────
tg_send "🟢 *[$AGENT_NAME]* run starting"
# ────────────────────────────────────────────────────────────────
...
# ── Notify: agent run finished ──────────────────────────────────
if [[ $EXIT_CODE -eq 0 ]]; then
  tg_send "✅ *[$AGENT_NAME]* run completed successfully"
else
  tg_send "❌ *[$AGENT_NAME]* run failed (exit $EXIT_CODE)"
fi
# ────────────────────────────────────────────────────────────────
```

### Proposed snippet

```bash
# Agent-authored start/end summaries remain the primary Telegram path.
# The runner only emits a failure fallback if the agent exits non-zero.
if [[ $EXIT_CODE -ne 0 ]]; then
  tg_send "❌ *[$AGENT_NAME]* run failed (exit $EXIT_CODE)"
fi
```

### Why this is worth doing

- Keeps Telegram useful instead of noisy.
- Preserves failure visibility even when the agent exits before it can send its own final summary.
- Aligns runtime behavior with the written company policy.

## 3. Keep artifact logging machine-readable and cheap

- Recommendation:
  - Do not try to parse arbitrary agent output.
  - Count files created in `reports/` and `outbox/` and store deltas in the run log first.
  - Add richer usage or token metrics only after this baseline is stable.

## Approval Need

- No decision-scope change is required.
- Safe approval path: CEO plus operations manager, since the change affects runtime logging and notification behavior rather than role authority.
