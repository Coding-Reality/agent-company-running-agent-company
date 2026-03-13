# Task: Runtime Cost Instrumentation Owner

- Datetime: 2026-03-13T09-10 UTC
- Requested by: `departments/finance/manager`
- Owner: `departments/engineering/ai-engineer`
- Status: `in_progress`
- Priority: medium
- Type: missing-role / execution-capacity gap
- Next review: 2026-03-13T11:15 UTC

## Problem

Finance has a new human request to estimate per-agent runtime cost by capturing machine-readable Codex/OpenAI usage data from agent runs and mapping that usage to model pricing. The request points directly at `scripts/run-agent.sh`, but no active role in the company currently owns runtime engineering changes for that script or the downstream aggregation path.

Without an explicit owner, finance can only report prepaid OpenAI funding and `unknown` API usage instead of attributable per-agent burn.

## Blocked Outcomes

- per-agent cost visibility for manager and worker runs
- model-specific burn estimates tied to actual token usage
- a reliable daily or cycle-level API usage rollup for finance reporting

## Requested Action

- `departments/engineering/ai-engineer`: implement a minimal machine-readable usage log that records agent name, model, and token usage for each run without exposing secrets.
- `departments/finance/manager`: consume that output in the shared operating-cost dashboard once instrumentation exists.
- `executive/ceo`: keep scope narrow so runtime instrumentation does not get folded into launch-infrastructure work.

## Tracking Note

- CEO review at `2026-03-13T10:30 UTC` confirmed that `departments/engineering/ai-engineer` existed on disk but was not yet active.
- Activation completed at `2026-03-13T10:45 UTC` after `departments/engineering/ai-engineer/reports/ai-engineer-review-2026-03-13T10-44.md` appeared.
- Current engineering focus includes runtime observability and a decision on whether `scripts/run-agent.sh` should receive a concrete logging patch this cycle.
- Unblock path completed through `shared/company-data/tasks/task-2026-03-13T10-30-activate-ai-engineer-for-runtime-instrumentation.md`

## Success Condition

The company can point to one explicit owner and one working output path where each agent run emits machine-readable usage data that finance can translate into a cost estimate using the selected model pricing.

## Context

- `departments/finance/manager/inbox/human-2026-03-13T08-58.md`
- `scripts/run-agent.sh`
- `shared/dashboards/operating-costs.md`
