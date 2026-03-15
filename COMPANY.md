# Company

## Mission
Grow adoption and awareness of [base-agent-company](https://github.com/Coding-Reality/base-agent-company) — the open-source framework for building filesystem-based autonomous companies powered by AI agents. This company markets the idea, expands on it, writes content, manages the public repo, and builds community.

## Product
**base-agent-company** is a ready-to-fork template that lets anyone create an autonomous company as a folder structure. Roles are folders. Coordination is files. Execution is scheduled AI agents via PM2 cron jobs. No backend, no database, no API — just a filesystem and prompts.

GitHub: https://github.com/Coding-Reality/base-agent-company

## Why This Company Exists
The agent-company framework is a new paradigm. It needs:
- clear positioning so developers and teams understand the value
- content that shows how to use it (blogs, tutorials, use-case guides)
- community management around the public repo
- market intelligence on the AI agent landscape to sharpen messaging
- a roadmap driven by real adoption signals

This company is itself an agent-company instance — proving the framework works by using it.

## Operating Model
- Each role lives in its own folder.
- PM2 cron jobs launch only the board roles, the CEO, and the detached `runtime/coordinator`.
- The runtime coordinator dispatches downstream department and worker roles on demand against live Redmine issues.
- Every dispatched run should have one issue, one owner, one success condition, and one required Redmine write-back.
- Shared folders act as company infrastructure and secondary context for strategy, pipeline, policies, and reusable templates.
- Humans interact with the company by writing files. See `shared/policies/human-protocol.md` for entry points, format rules, and priority handling. Human inputs override agent-generated direction.

## Phase 1 Roles
- `board/chair`
- `board/strategy-member`
- `executive/ceo`
- `runtime/coordinator`
- `departments/sales/manager`
- `departments/sales/outbound-1`
- `departments/marketing/manager`
- `departments/marketing/content`
- `departments/operations/manager`
- `departments/research/market-intel`
- `departments/finance/manager`
- `departments/engineering/ai-engineer`
- `departments/engineering/repo-engineer`
- `departments/engineering/devops-engineer`

## What Each Layer Does (Product Context)

### Board
Sets the vision for how agent-company should be positioned, what audience to target, and what success looks like. Reviews strategic direction and community signals.

### Executive
Converts board vision into execution priorities. Coordinates content production, outreach, repo management, and community growth.

### Marketing
Writes blogs, tutorials, and thought-leadership pieces. Defines messaging and positioning. Produces content calendars tied to product milestones and community demand.

### Sales
Grows the user base through direct outreach to dev communities, AI teams, open-source enthusiasts, and enterprise prospects. Tracks adoption signals and conversion.

### Research
Monitors the AI agent landscape — competing frameworks, emerging patterns, community sentiment. Feeds intelligence back to strategy and content.

### Operations
Manages the public repo workflow — issues, PRs, release notes, documentation quality. Keeps the company's internal operating cadence healthy.

### Engineering
Owns context engineering, framework improvement, infrastructure, and base repo maintenance. The AI Engineer audits what each role reads, how prompts are structured, and whether the execution flow produces high-quality outputs. The Repo Engineer syncs proven improvements from this running instance back to the public base-agent-company template — scripts, policies, AGENTS.md patterns, and new roles. The DevOps Engineer manages the VM, k3s cluster, domain (agent-company.ai), deployments, and operational reliability.

### Finance
Tracks costs (compute, API usage), sponsorship and partnership revenue, and sustainability metrics. Challenges assumptions about monetization.

## Role Activation
Phase 1 folders and PM2 jobs are pre-created. The board chair and CEO should still behave as if they are staffing the company:

- activate dormant roles by issuing written priorities
- create hiring or expansion tasks for missing roles
- avoid inventing people or outputs that do not exist on disk

## Token Efficiency
Agents should not read the whole repo on every run.

Default read order:
1. local `AGENTS.md`
2. shared strategy and policy indexes
3. own `memory/current-focus.md`
4. newest files in `inbox/`, `outbox/`, and `reports/`
5. only the specific downstream or upstream folders needed for the current decision

Use file discovery before file reading:
- `rg --files`
- `find . -maxdepth 2 -type f | sort`
- `ls -t`

Prefer:
- current state files
- indexes
- latest dated reports

Avoid:
- rereading large historical archives
- loading every file in every department
- rewriting old reports

## Git Discipline
- Agents may commit and push their own work.
- Commit messages must use the prefix format `[agent-name]: summary`.
- Agents should commit only their intended changes and avoid unrelated churn from other roles.
- If the branch has moved and push is not clean, agents should report the issue and stop instead of force-pushing.

## Telegram Reporting
Every agent has access to a Telegram notification tool at `scripts/send-telegram.sh`.

### When to report

1. **After reading** — Once you have read your key files (AGENTS.md, current-focus, inbox, latest reports), send a concise Telegram message listing:
   - Your role name
   - The files you read and why
   - Your current focus or priority based on what you read

2. **After execution** — When your run is complete, send a final Telegram message summarizing:
   - Actions taken (files created, decisions made, delegations sent)
   - Blockers or escalations
   - What the next run should pick up

### How to call it
```bash
bash scripts/send-telegram.sh "Your message here"
```

### Rules
- Keep messages short — bullet points, not essays.
- If the tool fails (missing token, network error), continue your work. Notifications are best-effort.
- Do not send messages mid-run for every small action. Two messages per run: one after reading, one after execution.
