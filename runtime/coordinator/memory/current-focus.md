# Current Focus

## As Of 2026-03-15T16:00 UTC
- This role exists to stop free-running department cadence and replace it with issue-bound dispatch.
- PM2 should schedule only `board/chair`, `board/strategy-member`, `executive/ceo`, and `runtime/coordinator`.
- Downstream roles should run only when dispatched against one live Redmine issue with one exact success condition.
- First operating priority:
  - prefer live `High` priority issues already in progress
  - dispatch `departments/operations/devops-engineer` for issue `#9` until the launch lane reaches a real infrastructure state change or an exact human-only blocker
- If a local AGENTS file still points at deleted `shared/company-data/tasks/*.md` files, treat Redmine as authoritative and note the stale reference.

## As Of 2026-03-15T16:05 UTC
- Redmine Company wiki is restored and reachable again; Redmine remains the authoritative dispatch surface.
- Active queue review still points to issue `#9` as the highest-priority in-progress lane with a valid owner and concrete next deliverable.
- This cycle should dispatch `departments/operations/devops-engineer` with one narrow success condition:
  - either advance from repo-only GitOps scaffolding to a host bootstrap checkpoint on `192.168.1.135`
  - or record the exact human-only blocker that prevents k3s and Argo CD bootstrap
- Coordinator verification after the child run must confirm a fresh Redmine note or other material issue change on `#9`.
