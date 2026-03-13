# Human Protocol

Humans hold ultimate authority over this company. Any human input overrides agent-generated direction when there is a conflict. Agents must treat human inputs as the highest-priority items in their read queue.

## Identifying Human Inputs

Human-authored files must begin with a frontmatter block:

```
---
source: human
author: <name or handle>
datetime: YYYY-MM-DDTHH-MM UTC
---
```

When agents encounter a file with `source: human`, they must:
- read it immediately, before any agent-generated content in the same folder
- treat its directives as binding unless they contradict a newer human input
- acknowledge the human input explicitly in their next report

## Entry Points

Humans should interact with this company through Redmine first.

### Strategic Direction
**Surface:** Redmine wiki page `Company` or project wiki pages linked from it
**Use when:** Changing company direction, operating model, audience, positioning, or role doctrine.

### Tasking, Blockers, And Follow-Up
**Surface:** Redmine issues in project `agent-company-running-agent-company`
**Use when:** Assigning work, changing status, escalating blockers, or requesting execution.

### Repository Data Updates
**Surface:** `shared/dashboards/*.md`, `shared/company-data/**`, or other shared repo documents
**Use when:** You have product data or repo-owned facts that still belong in version control.

### Structural Role Changes
**Surface:** `{role-path}/AGENTS.md`
**Use when:** A role needs expanded or restricted scope.

### Legacy Filesystem Inputs
Role-local `inbox/`, `outbox/`, `reports/`, and `memory/` files are legacy interfaces only. Do not use them as the normal command path for this company.

## Company Assets & Real-World Facts

Agents cannot observe the real world. When humans acquire assets, close deals, have conversations, or make purchases, they must record these as files so the company can act on them.

**File:** `shared/company-data/assets.md` (create if missing)
**Format:**
```markdown
# Company Assets

## Domains
- agent-company.ai — purchased YYYY-MM-DD, registrar: <name>, status: <active/parked/configured>

## Accounts
- GitHub: Coding-Reality/base-agent-company
- <platform>: <handle/url>

## Subscriptions
- <service>: <tier>, <cost/mo>, <renewal date>

## Other
- <description>
```

Agents should check this file when making decisions about branding, distribution, URLs, or external presence.

## Work Tracking Requirement

All substantive company work should be tracked in Redmine.

Repository-local markdown may still exist for shared product data or migration records, but it is not the primary execution surface. If a human drops work into a legacy local role folder, agents should migrate it into Redmine during triage.

## Requesting Human Action (Agent → Human)

Agents cannot interact with the outside world. When the company needs something only a human can do, agents must formally request it.

### When to Request Human Action

- Purchasing a domain, service, or subscription
- Creating or configuring external accounts (hosting, analytics, social media)
- Signing contracts, legal decisions, or spending approvals
- Real-world conversations (partnerships, sales calls, interviews)
- Providing credentials or API keys
- DNS configuration, deployment, or infrastructure that requires console access
- Any decision that involves money, legal risk, or external identity

### How to Request

Create or update a Redmine issue first. Use `shared/company-data/human-queue/` only when a repository-local audit trail is still required by migration.

**Filename:** `request-YYYY-MM-DDTHH-MM-<slug>.md`

**Format:**
```markdown
---
source: agent
requesting-role: <role-path>
datetime: YYYY-MM-DDTHH-MM UTC
urgency: low | medium | high | blocking
status: open
---

# Human Action Requested: <short title>

## What We Need
<specific, actionable description of what the human must do>

## Why
<business reason — what is blocked or enabled by this action>

## Context
<links to relevant files, decisions, or reports that led to this request>

## When
<deadline or "next convenient opportunity" or "blocking — nothing can proceed until this is done">

## Once Done
<what the human should update — e.g., "add domain to shared/company-data/assets.md" or "drop credentials in executive/ceo/inbox/">
```

### Telegram Notification

When creating a human-queue request with urgency `high` or `blocking`, the agent must also send a Telegram message:

```bash
bash scripts/send-telegram.sh "[HUMAN ACTION NEEDED] <title> — urgency: <level>. See shared/company-data/human-queue/<filename>"
```

For `low` and `medium` urgency, Telegram notification is optional.

### Tracking & Follow-Up

- Agents should check `shared/company-data/human-queue/` for open requests on every run.
- If a `blocking` request is older than 4 hours with no response, the board chair or CEO should re-send the Telegram notification.
- If a `high` request is older than 24 hours, escalate it in the next board report.
- Agents must not assume a request has been fulfilled unless the status is changed to `done` or the expected output file exists.

### How Humans Respond

When a human completes a request:
1. Update the Redmine issue status and result
2. Update any relevant company data files (assets.md, dashboards, etc.)
3. Only touch local role folders if legacy migration context still requires it

### Request Statuses

- `open` — waiting for human action
- `acknowledged` — human has seen it and will act
- `done` — completed, result recorded
- `wont-do` — human declined with reason in `## Result`

## Priority Rules

1. A human input always outranks an agent-generated directive at the same level.
2. A human updating the relevant Redmine issue or doctrine wiki outranks older agent-generated execution state.
3. A human editing `board-vision.md` or the company wiki outranks all existing CEO priorities.
4. If two human inputs conflict, the newer datetime wins.
5. Agents must never silently discard or deprioritize a human input — if they cannot act on it, they must escalate it in their report.

## Acknowledging Human Inputs

Every agent that reads a human input must:
- reference it by filename in their next report
- state what action they took or why they could not act
- propagate relevant information downstream if it affects other roles

## Examples

### "I just bought a domain"
1. Add the domain to `shared/company-data/assets.md`
2. Create or update the relevant Redmine issue with instructions to incorporate the domain into launch strategy
3. CEO cascades through Redmine to marketing (brand/website), operations (DNS/hosting), and sales (outreach URLs)

### "Change the target audience"
1. Edit `shared/vision/board-vision.md` — update the "Who It's For" section
2. Board chair picks it up → rewrites CEO priorities → entire org pivots

### "Stop all outreach until the blog is ready"
1. Update or create the relevant Redmine issue with a hold directive
2. CEO reads it → tells sales manager to pause → outbound agent stops

### "This agent is doing the wrong thing"
1. Update the relevant Redmine issue or doctrine wiki entry with corrected priorities
2. Or edit `{role}/AGENTS.md` if the problem is structural

### Agent needs a domain configured (agent → human)
1. Operations agent creates `shared/company-data/human-queue/request-2026-03-13T14-30-configure-dns.md` with urgency `high`
2. Agent sends Telegram: `[HUMAN ACTION NEEDED] Configure DNS for agent-company.ai — urgency: high`
3. Human sees notification, configures DNS, edits request status to `done`, updates `shared/company-data/assets.md`
4. Operations agent sees status change on next run and proceeds with deployment

### Agent needs spending approved (agent → human)
1. Finance manager creates `shared/company-data/human-queue/request-2026-03-13T16-00-approve-hosting.md` with urgency `medium`
2. Human reviews at next convenience, approves or declines, updates status
3. Finance agent reads result and updates operating-costs dashboard
