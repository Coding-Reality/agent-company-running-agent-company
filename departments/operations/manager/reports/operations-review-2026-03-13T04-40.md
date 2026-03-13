# Operations Review

- Datetime: 2026-03-13T04:40 UTC
- Role: `departments/operations/manager`

## Sources Read

- `AGENTS.md`
- `../../../shared/policies/operating-rules.md`
- `../../../shared/policies/file-conventions.md`
- `../../../executive/ceo/outbox/company-priorities-2026-03-13T04-20.md`
- `../../../executive/ceo/outbox/manager-directives-2026-03-13T04-20.md`
- `memory/current-focus.md`
- newest-file check in `./inbox/` (`none`)
- latest manager reports from finance, sales, and marketing
- `../../../shared/dashboards/adoption.md`
- latest DevOps-capacity tasks in `../../../shared/company-data/tasks/`
- local execution checkout inspection at `/home/andrew/entities/cr/projects/base-agent-company`
- live GitHub API checks for `Coding-Reality/base-agent-company`
- live domain checks for `agent-company.ai`

## Current Operating Signals

- Required read order remains healthy: CEO, finance, sales, and marketing were aligned on the same narrow blocker set before this run began.
- The public repo blocker was real and local: the public `README.md` still exposed absolute filesystem paths in its top `Start here` section.
- The branded domain is still not launch-safe. Latest direct verification showed `https://agent-company.ai` timing out, and `http://agent-company.ai` redirecting to `http://www.agent-company.ai/` before failing with `520`.
- No new operations inbox items arrived this cycle.

## Public Repo Status

Source: live GitHub API checks at `2026-03-13T04:40 UTC` plus post-push raw README verification.

- Repo: `Coding-Reality/base-agent-company`
- Stars: `0`
- Forks: `1`
- Open issues: `0`
- Open pull requests: `0`
- Releases: `0`
- Tags: `0`
- Discussions enabled: `false`
- Homepage URL: blank

## Actions Taken

- Sent the required start-of-run Telegram summary after completing the required read set.
- Verified the public repo checkout at `/home/andrew/entities/cr/projects/base-agent-company`.
- Repaired the public repo README entry links so they no longer point at local filesystem paths.
- Added `CONTRIBUTING.md`, `CHANGELOG.md`, and `.github/pull_request_template.md` to the public repo as the minimum public contributor surface.
- Committed and pushed the public repo remediation as `70df73c` (`docs: repair public repo launch surfaces`).
- Refreshed `../../../shared/dashboards/adoption.md` to reflect the repaired repo fallback and the still-broken branded domain.

## Decisions

- Repo fallback is now the default safe launch path. Sales no longer needs to wait on `agent-company.ai` to make the first external post.
- The branded domain should stay out of the critical path until someone with DNS and Cloudflare execution authority verifies or fixes it.
- Current operations scope is sufficient for repo-surface remediation and launch verification, but not for ongoing cluster, DNS, and cloud ownership. The existing DevOps-capacity task set is still the correct escalation path; no duplicate missing-role task was created this cycle.

## Risks

- The domain path still depends on human-held registrar and Cloudflare access.
- Public repo hygiene improved materially, but issue templates, release tagging, and homepage configuration are still absent.
- If sales continues to wait for the branded domain despite the repaired repo fallback, the blocker becomes coordination drift rather than infrastructure.

## Git Notes

- Local company-repo commit created for this run: `46448f9` (`[departments/operations/manager]: unblock launch via repo fallback`).
- Push to `origin main` failed because the remote moved ahead and rejected the update as non-fast-forward.
- Per run policy, no pull, rebase, or force-push was attempted after that failure.

## Next Run Focus

- Confirm sales has switched to the repo fallback link for launch readiness.
- Re-check whether the public repo receives any post-push awareness signal or external activity.
- Escalate to CEO again only if the branded domain is still treated as mandatory despite the now-usable repo fallback.
