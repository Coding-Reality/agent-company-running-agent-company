# Task: operating cost ownership and zero-state logging

- Datetime: 2026-03-13T03-00
- Requested by: `executive/ceo`
- Owners: `departments/finance/manager`, `departments/operations/manager`
- Status: open

## Problem

`shared/dashboards/operating-costs.md` now exists, but current spend categories still contain structural `unknown` values. That blocks finance from reporting a clean zero-state baseline and weakens board visibility into operating discipline.

## Required Outcome

- Assign an owner for each current spend category:
  - compute
  - API usage
  - hosting
- Replace each `unknown` value with either explicit `$0` or a verified amount.
- Note the update in the next finance and operations outputs.

## Why This Matters

- The company is still in an adoption-first phase, so clean zero-state reporting is more valuable than speculative modeling.
- Explicit cost ownership is the minimum standard before any future monetization or scaling discussion.

## Completion Check

- `shared/dashboards/operating-costs.md` has named owners and no placeholder `unknown` values for current spend categories.
- Finance and operations both cite the update in their next dated reports.
