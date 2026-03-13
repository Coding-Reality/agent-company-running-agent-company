# Runtime Playbook

## Goal
Launch each role with a compact prompt and let the agent execute primarily against Redmine.

## Default Run Flow
1. Read local `AGENTS.md`.
2. Check the Redmine wiki page `Company` and the relevant Redmine issues before acting.
3. Read repository-local policy or product files only if they are needed for the current decision.
4. Read role-local historical files only if migration context requires them.
5. Make decisions and record execution in Redmine.
6. Update repository-local shared documents only when the source of truth for that document still lives in the repo.
7. If changes were made, commit with the required agent prefix and push when safe.

## Token-Efficient Discovery
- Use Redmine issue filters and the wiki before repo-wide file scans.
- Use `rg --files` to map candidate repository files quickly when local docs are still needed.
- Prefer current shared source files over historical role-local directories.
- If migration context is needed, inspect only the newest relevant historical files before expanding further.

## Hiring And Activation
If a required role is missing or dormant:
- create or update a Redmine issue for activation or hiring
- note the dependency in Redmine
- update local task files only if the migration still requires a mirrored record

Do not pretend a missing role has acted unless files exist showing that action.

## Git Output Rule
- Use the runtime agent name as the commit prefix: `[agent-name]: summary`.
- Keep commits small and role-scoped.
- Push only after confirming the current branch state is safe.
