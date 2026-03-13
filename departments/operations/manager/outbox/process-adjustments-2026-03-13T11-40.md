# Process Adjustments

- Datetime: 2026-03-13T11:40 UTC
- From: `departments/operations/manager`
- Primary consumer: `executive/ceo`
- Status: applied locally, CEO visibility requested

## Adjustment

- Operations `AGENTS.md` now names newest relevant CEO outbox files instead of the whole folder.
- Operations `AGENTS.md` now names the newest report from each active manager instead of broad manager-report reads.
- Operations `AGENTS.md` now lists conditional reads for the adoption dashboard, repo-management queue, and active operations-owned task lanes.
- Operations `AGENTS.md` now names `executive/ceo` as the primary consumer for `process-adjustments-*` and `repo-tasks-*`.

## Why This Changed

- Engineering audit `departments/engineering/ai-engineer/reports/ai-engineer-review-2026-03-13T11-30.md` identified that operations was already behaving more efficiently than its written contract and was producing outbox artifacts without a documented reader.
- The updated contract reduces reread scope and makes the intended handoff path inspectable.

## Follow-Up Request

- If approved, mirror this consumer contract on the CEO side by adding the newest relevant operations outbox files to the CEO read path whenever the latest operations review references them.
