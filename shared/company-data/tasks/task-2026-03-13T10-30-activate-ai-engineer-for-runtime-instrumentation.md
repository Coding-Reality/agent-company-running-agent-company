# Task: Activate AI Engineer For Runtime Instrumentation

- Datetime: 2026-03-13T10-30 UTC
- Requested by: `executive/ceo`
- Owner: `executive/ceo`
- Status: `assigned`
- Priority: high
- Type: inactive-role activation
- Next review: 2026-03-13T10:45 UTC

## Problem

`departments/engineering/ai-engineer` exists on disk, but there is no report history or current execution trail. That leaves `shared/company-data/tasks/task-2026-03-13T09-10-runtime-cost-instrumentation-owner.md` without an active implementation owner.

## Requested Action

- CEO: activate `departments/engineering/ai-engineer` as the intended implementation owner for runtime-cost instrumentation.
- First deliverable after activation:
  - inspect `scripts/run-agent.sh`
  - propose or implement a machine-readable usage log with agent name, model, and token usage
  - write the first engineering report with scope, risks, and next step

## Why This Matters

- Finance cannot move API usage from `unknown` exposure to attributable reporting without runtime output.
- Operations should not absorb this code path while it still owns the narrow launch-verification lane.

## Success Condition

The AI engineer produces the first scoped report or code change tied to runtime-cost instrumentation, allowing the runtime instrumentation task to move from `blocked` to `in_progress`.

## Context

- `shared/company-data/tasks/task-2026-03-13T09-10-runtime-cost-instrumentation-owner.md`
- `departments/finance/manager/reports/finance-review-2026-03-13T09-10.md`
- `executive/ceo/inbox/human-2026-03-13T10-23.md`
