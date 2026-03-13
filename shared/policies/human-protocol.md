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

Humans interact with the company through files. Choose the entry point that matches the scope of your input.

### Strategic Direction
**File:** `shared/vision/board-vision.md` or `shared/vision/strategy.md`
**Effect:** Board chair reads these every 4 hours → issues new CEO priorities → cascades to all departments.
**Use when:** Changing company direction, audience, positioning, product scope, or success criteria.

### Direct Order to CEO
**File:** `board/chair/outbox/ceo-priorities-YYYY-MM-DDTHH-MM.md`
**Effect:** CEO reads within 15 minutes → cascades to managers within one cycle.
**Use when:** You want something executed immediately without waiting for the board cycle.

### Cross-Role Task
**File:** `shared/company-data/tasks/task-YYYY-MM-DDTHH-MM.md`
**Effect:** CEO and assigned roles pick it up on their next run.
**Use when:** A specific deliverable needs one or more departments to act.

### Direct Message to a Role
**File:** `{role-path}/inbox/human-YYYY-MM-DDTHH-MM.md`
**Effect:** That agent reads it on its next run.
**Use when:** You need a specific role to do something without involving the chain of command.

### Override Role Context
**File:** `{role-path}/memory/current-focus.md`
**Effect:** Immediately changes what that agent prioritizes on its next run.
**Use when:** An agent is stuck in a loop or focused on the wrong thing.

### Update Company Data
**Files:** `shared/dashboards/*.md`, `shared/company-data/**`
**Effect:** Agents read these as ground truth for metrics, leads, pipeline, etc.
**Use when:** You have real-world data that agents cannot observe (domain purchases, revenue, partnerships, external conversations).

### Change Role Authority
**File:** `{role-path}/AGENTS.md`
**Effect:** Permanently changes what the role can do, reads, and produces.
**Use when:** A role needs expanded or restricted scope.

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

Create a file in `shared/company-data/human-queue/`:

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
1. Edit the request file: change `status: open` to `status: done`
2. Add a `## Result` section at the bottom with what was done
3. Update any relevant company data files (assets.md, dashboards, etc.)
4. Optionally drop a file in the requesting role's inbox if further agent action is needed

### Request Statuses

- `open` — waiting for human action
- `acknowledged` — human has seen it and will act
- `done` — completed, result recorded
- `wont-do` — human declined with reason in `## Result`

## Priority Rules

1. A human input always outranks an agent-generated directive at the same level.
2. A human writing directly to a role's inbox outranks that role's current focus.
3. A human editing `board-vision.md` outranks all existing CEO priorities.
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
2. Create `board/chair/outbox/ceo-priorities-YYYY-MM-DDTHH-MM.md` with frontmatter and instructions to incorporate the domain into launch strategy
3. CEO cascades to marketing (brand/website), operations (DNS/hosting), sales (outreach URLs)

### "Change the target audience"
1. Edit `shared/vision/board-vision.md` — update the "Who It's For" section
2. Board chair picks it up → rewrites CEO priorities → entire org pivots

### "Stop all outreach until the blog is ready"
1. Write to `board/chair/outbox/ceo-priorities-YYYY-MM-DDTHH-MM.md` with a hold directive
2. CEO reads it → tells sales manager to pause → outbound agent stops

### "This agent is doing the wrong thing"
1. Edit `{role}/memory/current-focus.md` with corrected priorities
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
