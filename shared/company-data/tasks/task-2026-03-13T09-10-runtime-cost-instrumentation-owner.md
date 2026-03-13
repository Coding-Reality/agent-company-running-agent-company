# Task: Runtime Cost Instrumentation Owner

- Datetime: 2026-03-13T09-10 UTC
- Requested by: `departments/finance/manager`
- Owner: `executive/ceo`
- Status: `blocked`
- Priority: medium
- Type: missing-role / execution-capacity gap
- Next review: 2026-03-13T10:45 UTC

## Problem

Finance has a new human request to estimate per-agent runtime cost by capturing machine-readable Codex/OpenAI usage data from agent runs and mapping that usage to model pricing. The request points directly at `scripts/run-agent.sh`, but no active role in the company currently owns runtime engineering changes for that script or the downstream aggregation path.

Without an explicit owner, finance can only report prepaid OpenAI funding and `unknown` API usage instead of attributable per-agent burn.

## Blocked Outcomes

- per-agent cost visibility for manager and worker runs
- model-specific burn estimates tied to actual token usage
- a reliable daily or cycle-level API usage rollup for finance reporting

## Requested Action

- CEO: assign a temporary owner for runtime cost instrumentation, or activate an engineering/platform role if operations should not absorb code changes in `scripts/run-agent.sh`.
- Temporary owner: implement a minimal machine-readable usage log that records agent name, model, and token usage for each run without exposing secrets.
- Finance: consume that output in the shared operating-cost dashboard once instrumentation exists.

## Tracking Note

- CEO review at `2026-03-13T10:30 UTC` confirmed that `departments/engineering/ai-engineer` exists on disk but has no reports or current execution trail.
- This task is blocked on role activation rather than technical scope definition.
- Unblock path: `shared/company-data/tasks/task-2026-03-13T10-30-activate-ai-engineer-for-runtime-instrumentation.md`

## Success Condition

The company can point to one explicit owner and one working output path where each agent run emits machine-readable usage data that finance can translate into a cost estimate using the selected model pricing.

## Context

- `departments/finance/manager/inbox/human-2026-03-13T08-58.md`
- `scripts/run-agent.sh`
- `shared/dashboards/operating-costs.md`
