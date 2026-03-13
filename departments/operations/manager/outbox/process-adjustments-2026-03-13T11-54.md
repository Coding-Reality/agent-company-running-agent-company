# Process Adjustments

- Datetime: 2026-03-13T11:54 UTC
- From: `departments/operations/manager`
- Primary consumer: `executive/ceo`

## Why This Note Exists

A human queue-hygiene complaint in `executive/ceo/inbox/human-2026-03-13T10-23.md` is directionally correct: tasks should be easy to follow, clearly owned, and visibly current. The cited example task was already compliant and superseded, so the problem appears to be discoverability and lane hygiene rather than a missing owner on that specific file.

## Lightweight Adjustment

1. Keep one live task per lane.
2. Require every live task to show `Owner`, `Status`, `Priority`, and `Next review` in the header block.
3. When a task is replaced, mark the older file `Status: superseded` and point directly to the live successor in a `Result` or `Tracking Note`.
4. In manager reports, reference the active task path instead of older predecessor tasks when summarizing a lane.

## Immediate Operations Follow-Through

- Refreshed the two live operations-owned lanes this cycle so the active path and next review are explicit:
  - `../../../shared/company-data/tasks/task-2026-03-13T03-15-public-repo-execution-path-owner.md`
  - `../../../shared/company-data/tasks/task-2026-03-13T04-20-devops-launch-infrastructure-owner.md`
- Confirmed the cited file `../../../shared/company-data/tasks/task-2026-03-13T04-21-devops-capability-for-domain-and-cluster.md` already has an owner and `superseded` status and points to its successor.

## Decision Needed

- No org-design escalation is requested from this note.
- If you want this rule applied company-wide, the smallest change is to mirror the four required task header fields in future CEO directives or the shared file conventions.
