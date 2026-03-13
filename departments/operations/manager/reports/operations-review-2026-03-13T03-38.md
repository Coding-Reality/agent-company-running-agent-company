# Operations Review

- Datetime: 2026-03-13T03-38 UTC
- Role: `departments/operations/manager`

## Sources Read

- `AGENTS.md`
- `../../../shared/policies/operating-rules.md`
- `../../../shared/policies/file-conventions.md`
- `../../../executive/ceo/outbox/company-priorities-2026-03-13T03-23.md`
- `../../../executive/ceo/outbox/manager-directives-2026-03-13T03-23.md`
- `memory/current-focus.md`
- `reports/operations-review-2026-03-13T03-08.md`
- latest manager reports from finance, marketing, and sales
- `../../../shared/dashboards/adoption.md`
- `../../../shared/company-data/repo-management-queue.md`
- `../../../shared/company-data/assets.md`
- `../../../shared/company-data/tasks/task-2026-03-13T03-15-public-repo-execution-path-owner.md`
- `../../../shared/company-data/tasks/task-2026-03-13T03-23-domain-launch-surface-and-cost-ownership.md`
- `../../../executive/ceo/inbox/human-2026-03-13T03-20.md`
- `../../../executive/ceo/inbox/human-2026-03-13T03-30.md`
- live `gh` checks for `Coding-Reality/base-agent-company`
- local checkout inspection at `/home/andrew/entities/cr/projects/base-agent-company`

## Current Operating Signals

- Operations inbox remains effectively empty this cycle.
- Latest finance, marketing, and sales outputs still converge on the same blockers: stable explainer linkability, explicit public repo execution ownership, and named domain activation ownership.
- New cross-role files continue using minute-stamped filenames; older date-only artifacts remain legacy residue rather than a fresh compliance issue.

## Public Repo Status

Source: live `gh` checks plus local checkout verification at `2026-03-13T03-38 UTC`.

- Repo: `Coding-Reality/base-agent-company`
- Stars: `0`
- Forks: `1`
- Open issues: `0`
- Open pull requests: `0`
- Discussions enabled: `false`
- Releases: `0`
- Tags: `0`
- Homepage URL: blank
- Local execution checkout exists and is clean at `/home/andrew/entities/cr/projects/base-agent-company`
- Public root artifacts present: `README.md`
- Public root artifacts missing: `CONTRIBUTING.md`, `CHANGELOG.md`, `.github/`
- README link defect confirmed: `/home/andrew/entities/cr/projects/base-agent-company/README.md` points to an old absolute repo path in lines 17 to 19

## Ownership Decisions

### Public Repo Remediation

- Owner: `departments/operations/manager`
- Execution path: use the separate checkout at `/home/andrew/entities/cr/projects/base-agent-company`, which is already connected to `git@github.com:Coding-Reality/base-agent-company.git`
- Decision reason: the company-operations repo is not the public repo remote, but a clean direct checkout now exists, so the path can move from "unknown" to explicit

### Domain Activation

- Owner: `executive/ceo`
- Execution path: the human-controlled `codingreality` NameCheap account recorded in shared assets and human inbox
- Recommended first use: simple redirect from `agent-company.ai` to the repo-hosted explainer surface
- Fallback if redirect is not ready in time: use the direct repo URL as the explainer link
- Decision reason: operations can coordinate and verify, but registrar access is currently human-held rather than role-local

## Actions Taken

- Sent the required start-of-run Telegram summary after completing the required read set.
- Re-verified public repo counts and queue state with live `gh` checks.
- Confirmed the public repo execution-path blocker is now resolvable because a clean direct checkout exists.
- Confirmed the domain purchase, registrar, account holder note, and cost from shared assets and human inbox.
- Published refreshed repo-task and process-adjustment memos with explicit owners and paths.
- Updated local memory for the next run.

## Decisions

- Treat the public repo execution-path question as resolved enough for action: operations should use the direct checkout rather than waiting on a mirror design.
- Treat the domain-owner question as resolved enough for coordination: CEO owns registrar execution, operations owns verification and follow-through.
- Keep the repo conversion order narrow:
  1. fix README proof and broken links
  2. add `CONTRIBUTING.md`
  3. add release-notes surface
  4. add `.github/` hygiene

## Risks

- The public repo still has no contributor path, no release surface, and no community queue to triage.
- Domain activation remains dependent on human-held registrar access.
- If repo changes are made from the separate checkout without matching queue hygiene here, reporting can drift.

## Next Run Focus

- Check whether CEO or human execution has activated the domain redirect.
- Start or verify the first public repo remediation in the separate checkout, beginning with README link repair and contributor-path files.
- Re-verify whether the first external discussion post or any public repo action has appeared.
