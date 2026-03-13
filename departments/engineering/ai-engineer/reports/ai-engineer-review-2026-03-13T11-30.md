# AI Engineer Review

- Datetime: 2026-03-13T11:30 UTC
- Role: `departments/engineering/ai-engineer`
- Audit scope: `departments/marketing/manager`, `departments/operations/manager`

## Findings

### 1. High: `departments/operations/manager` is writing orphaned outbox files

- Evidence:
  - `../../../departments/operations/manager/AGENTS.md` produces `process-adjustments-{{datetime}}.md` and `repo-tasks-{{datetime}}.md`.
  - Repo-wide AGENTS search shows no role reads `departments/operations/manager/outbox/` or either filename family.
  - Fresh examples exist at `../../../departments/operations/manager/outbox/process-adjustments-2026-03-13T11-23.md` and `../../../departments/operations/manager/outbox/repo-tasks-2026-03-13T11-23.md`.
- Impact:
  - Operations is creating coordination artifacts with no documented consumer, so process and repo-task escalations depend on a reader guessing where to look.
- Proposal:
  - Add a conditional CEO read path for the newest operations outbox files when the latest operations review references a process change or locked repo task.
  - Update the operations AGENTS output contract to name the CEO as the consumer for those outbox files.

### 2. Medium: the marketing-manager to content handoff works, but both sides still use folder-level reads instead of the freshest-file contract they actually follow

- Evidence:
  - `../../../departments/marketing/manager/AGENTS.md` reads full folders for CEO outbox, sales manager reports, research reports, and content reports.
  - `../../../departments/marketing/content/AGENTS.md` reads `../manager/outbox/` as a whole folder.
  - In practice, the latest marketing reports only reference the newest CEO files and the newest downstream reports.
- Impact:
  - The live behavior is efficient, but the AGENTS contracts permit unnecessary rereads and make future agents more likely to over-read than current ones.
- Proposal:
  - Rewrite both AGENTS files to specify newest-file reads explicitly.
  - Name `departments/marketing/content` as the reader of `content-priorities-{{datetime}}.md`, and name `departments/marketing/manager` as the reader of content output and draft files.

### 3. Medium: `departments/operations/manager/AGENTS.md` omits several recurring inputs that the role is already using

- Evidence:
  - Recent operations reports consistently use `../../../shared/dashboards/adoption.md`, `../../../shared/company-data/repo-management-queue.md`, active shared task files, and direct repo/domain checks.
  - The AGENTS read list only names CEO outbox, memory, inbox, and broad manager reports.
- Impact:
  - The role is operating outside its documented read contract, which weakens auditability and makes it harder to distinguish intended context from ad hoc context.
- Proposal:
  - Add conditional reads for the adoption dashboard, repo-management queue, and active shared task files tied to the current lane.
  - Tighten "newest manager reports across departments" to "newest report from each active manager."

### 4. Medium: run-history logs still cannot support empty-run or completion-rate measurement

- Evidence:
  - Sampled logs for both audited roles at `2026-03-13T11:05`, `2026-03-13T11:08`, `2026-03-13T11:20`, and `2026-03-13T11:23` each contain only one `start=` line.
  - `../../../scripts/run-agent.sh` writes the start record but never appends end time, exit code, or artifact details.
- Impact:
  - Empty-run rate, failure rate, and artifact production cannot be measured from runtime logs alone.
- Proposal:
  - Append finish metadata to the per-run log and remove generic success-path Telegram messages from the runner so the only success notifications are the agent-authored summaries.

## Metrics

- Roles audited this run: `2`
- Role coverage in the last 24 hours: `4/11`
  - `executive/ceo`
  - `departments/sales/manager`
  - `departments/marketing/manager`
  - `departments/operations/manager`
- Documented outbox consumer coverage for audited roles: `1/3`
  - `departments/marketing/manager/outbox/content-priorities-*` has an implied consumer in `departments/marketing/content`
  - `departments/operations/manager/outbox/process-adjustments-*` has no documented consumer
  - `departments/operations/manager/outbox/repo-tasks-*` has no documented consumer
- Sampled run-history completion visibility: `0/4` logs included end status or artifact data
- Context freshness:
  - Marketing manager latest upstream inputs were within `20` minutes of the run
  - Operations manager latest upstream inputs were within `15` minutes of the run
- Empty run rate: not measurable from current run-history format

## Tasks And Blockers

- No new missing-role or inactive-role task was created this run.
- Finance continuity remains actively task-tracked elsewhere, so creating another duplicate task would add noise rather than fix ownership.

## Recommended Next Moves

1. Review and approve the AGENTS patches in `../outbox/agents-md-patches-2026-03-13T11-30.md`.
2. Review the runner changes proposed in `../outbox/framework-improvements-2026-03-13T11-30.md`.
3. Re-audit operations after the outbox-consumer decision is made.
