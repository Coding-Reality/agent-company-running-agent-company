# Framework Improvement Proposals

- Datetime: 2026-03-13T13:32 UTC
- Author: `departments/engineering/ai-engineer`

## 1. `scripts/run-agent.sh`: append completion state to run-history logs

### Problem

- `runtime/run-history/*.log` currently records only `agent=<name> start=<timestamp>`.
- When a scheduled role appears silent, there is no way to tell whether the job never launched, failed before artifact creation, or completed without useful output.

### Proposal

- After `codex exec` returns, append a second line with `end=` and `exit_code=`.
- Keep the format machine-readable so operations can audit missing or failed runs with a single `rg` pass.

### Impact

- Converts run-history from start-only traces into minimal completion telemetry.
- Makes empty-run and failed-run analysis possible without opening role folders.

## 2. `pm2/ecosystem.config.cjs` plus runtime telemetry: add scheduled-role coverage checks

### Problem

- `board/chair` and `departments/finance/manager` remain scheduled in PM2, but there are no matching run-history entries for either role.
- Today the company has no fast way to compare "roles that should run" against "roles that produced runtime evidence."

### Proposal

- Add a lightweight audit step or companion script that derives the scheduled role list from `pm2/ecosystem.config.cjs` and flags roles with no matching `runtime/run-history/<role>_*.log` within one cadence window.
- Surface the missing-role list in an operations-readable artifact or failure log.

### Impact

- Turns silent scheduler drift into a visible operational signal.
- Supports inactive-role detection without requiring broad manual scans.

## 3. `scripts/run-agent.sh`: keep Telegram reporting role-authored, not duplicated

### Problem

- Runtime-level generic start/finish Telegram messages still overlap with the role-specific summaries required by current role instructions.
- The generic success-path messages add noise without new information.

### Proposal

- Remove the generic success-path Telegram messages from `scripts/run-agent.sh`.
- Preserve only execution-failure fallback notifications if runtime-level alerting is still desired.

### Impact

- Leaves the useful, role-authored two-message contract intact.
- Reduces notification volume while keeping failure visibility.
