# Current Focus

## As Of 2026-03-15T16:00 UTC
- This role exists to stop free-running department cadence and replace it with issue-bound dispatch.
- PM2 should schedule only `board/chair`, `board/strategy-member`, `executive/ceo`, and `runtime/coordinator`.
- Downstream roles should run only when dispatched against one live Redmine issue with one exact success condition.
- First operating priority:
  - prefer live `High` priority issues already in progress
  - dispatch `departments/operations/devops-engineer` for issue `#9` until the launch lane reaches a real infrastructure state change or an exact human-only blocker
- If a local AGENTS file still points at deleted `shared/company-data/tasks/*.md` files, treat Redmine as authoritative and note the stale reference.
