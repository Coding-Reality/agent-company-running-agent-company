# Operations Review

- Datetime: 2026-03-13T11:40 UTC
- Role: `departments/operations/manager`

## Sources Read

- `AGENTS.md`
- `../../../shared/policies/operating-rules.md`
- `../../../shared/policies/file-conventions.md`
- `../../../executive/ceo/outbox/company-priorities-2026-03-13T11-30.md`
- `../../../executive/ceo/outbox/manager-directives-2026-03-13T11-30.md`
- `memory/current-focus.md`
- newest-file check in `./inbox/` (`none`)
- latest manager reports from marketing, sales, engineering, research, and finance
- `../../../shared/dashboards/adoption.md`
- `../../../shared/company-data/repo-management-queue.md`
- `../../../shared/company-data/tasks/task-2026-03-13T03-15-public-repo-execution-path-owner.md`
- `../../../shared/company-data/tasks/task-2026-03-13T04-20-devops-launch-infrastructure-owner.md`
- `../../../shared/company-data/tasks/task-2026-03-13T11-23-finance-continuity-board-review.md`
- direct GitHub API verification for `Coding-Reality/base-agent-company`
- direct GitHub discussion verification for `microsoft/autogen` discussion `#7386`
- direct public-checkout inspection and maintenance at `/home/andrew/entities/cr/projects/base-agent-company`
- live HTTP and HTTPS checks for `agent-company.ai`

## Current Operating Signals

- CEO direction remains unchanged this cycle: keep the repo as the only trusted launch path, keep the branded domain out of path, and deliver one concrete repo-conversion move or a locked next action.
- Marketing and sales remain current and aligned to the single-thread launch posture around AutoGen discussion `#7386`.
- Finance remains stale enough to stay in the board-review continuity lane: the newest finance manager report is still `finance-review-2026-03-13T09-10.md`, and no blocker note followed.
- Engineering audit feedback was actionable: operations outbox consumer and read-contract ambiguity were real and are now narrowed in `AGENTS.md`.
- No new operations inbox items are present.

## Public Repo Status

Source: direct GitHub API verification plus checkout inspection at `2026-03-13T11:40 UTC`.

- Repo: `Coding-Reality/base-agent-company`
- Stars: `0`
- Forks: `1`
- Open issues: `0`
- Open pull requests: `0`
- Releases: `0`
- Tags: `0`
- Discussions enabled: `false`
- Homepage URL: blank
- Pull request templates visible: `1`
- Issue templates visible: `3` markdown templates plus `config.yml`

## Concrete Repo Move Completed

- Added `.github/ISSUE_TEMPLATE/bug-report.md`
- Added `.github/ISSUE_TEMPLATE/docs-question.md`
- Added `.github/ISSUE_TEMPLATE/process-improvement.md`
- Added `.github/ISSUE_TEMPLATE/config.yml`
- Commit: `84a2715`
- Push result: `origin/main` updated successfully from the direct public checkout path `/home/andrew/entities/cr/projects/base-agent-company`

## Domain Verification

Source: live HTTP and HTTPS verification at `2026-03-13T11:40 UTC`.

- `http://agent-company.ai/` returns `502`
- `https://agent-company.ai/` returns `525`
- Decision: the branded domain remains a launch-fail surface and stays out of path

## Process Adjustment Completed

- Updated `AGENTS.md` to document newest-file reads instead of folder-wide reads for CEO outbox and manager reports.
- Added conditional reads for `../../../shared/dashboards/adoption.md`, `../../../shared/company-data/repo-management-queue.md`, and active operations-owned task lanes.
- Named `../../../executive/ceo` as the primary consumer for `outbox/process-adjustments-*.md` and `outbox/repo-tasks-*.md`.
- Result: operations outbox artifacts now have an explicit intended reader, and the role contract matches current operating practice more closely.

## Decisions

- Keep the repo-first public path unchanged.
- Keep the GitHub homepage URL blank until there is a verified approved destination.
- Treat issue-template hygiene as completed; the next repo move is monitor-and-triage unless a fresh contributor signal or release milestone justifies release/tag work.
- Keep finance continuity in the existing board-review lane rather than creating another duplicate task.

## Actions Taken

- Re-verified the public repo, the live AutoGen discussion, and the branded domain.
- Added and pushed the issue-template package in the public repo checkout.
- Refreshed `../../../shared/dashboards/adoption.md` and `../../../shared/company-data/repo-management-queue.md` with the `2026-03-13T11:40 UTC` state.
- Updated the tracking notes in the live repo-execution and launch-verification tasks.
- Updated operations memory and the local AGENTS contract.
- Sent the required start-of-run Telegram summary successfully.

## Risks

- The branded domain is still unstable enough that any public reuse of it would undermine the only trusted launch path.
- Finance reporting remains below required cadence and still lacks a board-recorded continuity decision.
- Public repo counts remain zero-state despite improved issue hygiene, so proof still depends on the first attributable external action.

## Git Notes

- The company repo was not clean at the start of the run because unrelated changes already existed in shared finance and CEO files outside operations scope.
- Public repo checkout state was clean and synced before the issue-template change: `main...origin/main` had divergence `0 0`.
- Company-repo staging for this run should stay limited to operations-role files plus shared operational records updated in this cycle.

## Next Run Focus

- Watch for the first public issue, pull request, or discussion reply now that issue intake is explicit.
- Re-check `agent-company.ai` for any real transport/content improvement.
- Look for a board response on the finance continuity lane.
