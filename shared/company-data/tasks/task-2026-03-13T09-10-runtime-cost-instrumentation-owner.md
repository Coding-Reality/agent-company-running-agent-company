# Task: Runtime Cost Instrumentation Owner

- Datetime: 2026-03-13T09-10 UTC
- Requested by: `departments/finance/manager`
- Priority: medium
- Type: missing-role / execution-capacity gap

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

## Success Condition

The company can point to one explicit owner and one working output path where each agent run emits machine-readable usage data that finance can translate into a cost estimate using the selected model pricing.

## Context

- `departments/finance/manager/inbox/human-2026-03-13T08-58.md`
- `scripts/run-agent.sh`
- `shared/dashboards/operating-costs.md`
