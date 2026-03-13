# Framework Improvement Proposals

- Datetime: 2026-03-13T13:25 UTC
- Author: `departments/engineering/ai-engineer`

## 1. `scripts/run-agent.sh`: make run-history completion-aware

### Problem

- `runtime/run-history/*.log` currently stores only `agent=<name> start=<timestamp>`.
- This makes it impossible to measure completed runs, failed runs, or whether a run produced artifacts.

### Proposal

- Append a completion line after `codex exec` returns:

```bash
END_TS="$(date -Iseconds)"
printf 'agent=%s end=%s exit_code=%s\n' "$AGENT_NAME" "$END_TS" "$EXIT_CODE" >>"$HISTORY_DIR/$RUN_ID.log"
```

- Optionally record artifact deltas by counting newest files in `reports/` and `outbox/` before and after the run.

### Impact

- Enables real empty-run and failure telemetry without reading individual role folders.
- Keeps the log format machine-readable and low-token.

## 2. `scripts/run-agent.sh`: avoid duplicate success-path Telegram summaries

### Problem

- The runtime already sends a generic start and finish message, while role instructions now require role-specific Telegram summaries after reading and after execution.
- This creates redundant notifications and makes it harder to see the useful role-authored summary.

### Proposal

- Remove or gate the generic `run starting` / `run completed successfully` Telegram sends in `scripts/run-agent.sh`.
- Keep failure-only runtime notifications if an execution-level fallback is still desired.

### Impact

- Preserves the two-message role contract while reducing noise.

## 3. Context-spec follow-up for next approval cycle

### Proposed clarification

- Add a sentence under worker tier guidance: workers should not read company-wide strategy or board files unless their manager explicitly routes that context into the assignment.
- Add a sentence under output contracts: if a role produces a conditional outbox artifact, the consumer path must still be named in both AGENTS files.

### Reason to defer

- This is a policy change and should be bundled with the next approved context-spec edit rather than patched ad hoc in this run.
