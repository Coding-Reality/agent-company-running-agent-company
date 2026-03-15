# Shared Skills

## Redmine Project Operations

Use Redmine as the primary execution and tracking system for this company. This company's Redmine project is:

- name: `agent-company-running-agent-company`
- identifier: `agent-company-running-agent-company`
- parent project: `coding-reality`
- homepage: `https://agent-company.ai/`

### Company Doctrine Wiki

- wiki page title: `Company`
- purpose: the baseline company doctrine, including the role-folder contract (`AGENTS.md`, `inbox/`, `outbox/`, `reports/`, `memory/`)
- rule: this wiki page is authoritative; do not keep a duplicate `COMPANY.md` in the repository
- project-specific override: this company itself operates in Redmine, not through role-local filesystem handoffs

### Validated Baseline

Validated on `2026-03-13`:

- `REDMINE_BASE_URL` resolves and accepts API requests.
- `REDMINE_API_KEY` authenticates successfully for the `ai-agent` user.
- project creation permission is available to that credential.
- the Redmine project `agent-company-running-agent-company` exists and is reachable.
- enabled trackers: `Bug`, `Feature`, `Support`
- issue statuses available: `New`, `In Progress`, `Resolved`, `Feedback`, `Closed`, `Rejected`

### Credential Rules

- Use `REDMINE_BASE_URL` and `REDMINE_API_KEY`.
- Treat the credential source as managed infrastructure. Do not paste secrets into reports, task files, or new docs.
- Before creating or updating issues, validate credentials with:

```bash
curl -sS -H "X-Redmine-API-Key: $REDMINE_API_KEY" \
  "$REDMINE_BASE_URL/users/current.json"
```

- Validate project access with:

```bash
curl -sS -H "X-Redmine-API-Key: $REDMINE_API_KEY" \
  "$REDMINE_BASE_URL/projects/agent-company-running-agent-company.json"
```

If either call fails, stop Redmine writes and escalate through the human queue.

### Project Bootstrap Rule

If the Redmine project does not exist, create it before creating issues:

```bash
curl -sS -H "X-Redmine-API-Key: $REDMINE_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST "$REDMINE_BASE_URL/projects.json" \
  -d '{
    "project": {
      "name": "agent-company-running-agent-company",
      "identifier": "agent-company-running-agent-company",
      "description": "Operational Redmine project for the filesystem-based company that markets and improves base-agent-company.",
      "homepage": "https://agent-company.ai/",
      "is_public": false,
      "parent_id": 1
    }
  }'
```

After creation, re-run the project access validation and continue only if it succeeds.

### Operating Workflow

1. Start every run by checking the relevant Redmine issue set and the wiki page `Company`.
2. Check whether the local work item already has a Redmine issue id or URL.
3. If not, create a Redmine issue in `agent-company-running-agent-company`.
4. Mirror into a local file only when a shared repo document or migration record explicitly requires it.
5. Update Redmine whenever ownership, status, due date, estimate, blocking context, or durable decisions change.
6. Do not create new role-local `inbox/`, `outbox/`, `reports/`, or `memory/` workflow artifacts unless a migration step explicitly requires them.
7. Close both the Redmine issue and any required mirrored record only when the work is actually complete.

### Tracker Selection

- Use `Feature` for roadmap, content, process, infra, and growth work.
- Use `Bug` for broken automation, regressions, missing outputs, or incorrect behavior.
- Use `Support` for unblockers, access requests, or human-assisted operational tasks.

### Minimum Issue Shape

Every new issue should include:

- subject with a specific action and owner-facing outcome
- description with background, expected result, and any blocker details
- tracker
- status
- assignee when known
- due date when work is time-sensitive
- link back to the filesystem task file path

### Suggested Create Call

```bash
curl -sS -H "X-Redmine-API-Key: $REDMINE_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST "$REDMINE_BASE_URL/issues.json" \
  -d '{
    "issue": {
      "project_id": "agent-company-running-agent-company",
      "tracker_id": 2,
      "status_id": 1,
      "priority_id": 2,
      "subject": "Assign owner and status to shared task backlog",
      "description": "Source file: shared/company-data/tasks/task-2026-03-13T04-21-devops-capability-for-domain-and-cluster.md"
    }
  }'
```

### Required Local Mirror

For any task tracked in Redmine, keep these fields in the local markdown file frontmatter or top section:

- `owner`
- `status`
- `redmine_issue_id`
- `redmine_issue_url`
- `last_synced_at`

Redmine is the durable tracker. Local files remain the execution workspace.

### Preferred Tooling

- Preferred: direct Redmine REST API calls with `curl`
