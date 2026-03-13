# Company-Wide Agent Rules

- Optimize for revenue, useful execution, and measurable progress.
- Stay inside your role boundary and authority.
- Read the smallest set of Redmine and repository context needed to make a sound decision.
- Label assumptions clearly instead of presenting them as facts.
- Prefer concrete next actions over general commentary.
- Write outputs that another role can use without reinterpretation.
- Record durable decisions in Redmine so they are inspectable later.
- Use Redmine on every execution. Start in Redmine, work in Redmine, and finish by syncing any status, owner, blocker, or scope changes back to Redmine.
- Do not use role-local `inbox/`, `outbox/`, `reports/`, or `memory/` directories as the primary workflow for this company.
- Escalate blockers explicitly instead of silently stalling.
- Reuse existing context before creating new plans.
- Avoid duplicating work already assigned or completed.
- Every run should produce at least one useful artifact unless genuinely blocked.

## Redmine Tracking Policy

- Redmine is the required system of record for every execution and for all company work that has an owner, status, deliverable, blocker, dependency, or durable decision.
- The Redmine wiki page `Company` is the authoritative company doctrine for this project.
- Redmine issues, notes, status changes, and wiki pages are the primary execution surface for this company.
- Role-local `inbox/`, `outbox/`, `reports/`, and `memory/` trees are legacy artifacts. Read them only for migration or historical context, and do not create new role-local workflow files unless a migration step explicitly requires it.
- Repository-local markdown should be limited to shared product documents, repo-owned assets, and historical records that do not belong in Redmine.
- Before starting new work, agents should check whether a Redmine issue already exists for it.
- If a qualifying task does not have a Redmine issue, the agent responsible for triage must create one or escalate if credentials/access are unavailable.
- Work is not considered fully documented unless Redmine is updated.
- Shared Redmine workflow details live in `shared/skills.md`.
