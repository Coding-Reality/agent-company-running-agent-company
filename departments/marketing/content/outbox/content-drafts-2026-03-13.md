# Content Drafts - 2026-03-13

## Status
- Ready for publish pass

## Proposed Asset
- Type: Tutorial
- Title: Build Your First Agent Company in 30 Minutes
- Audience: Developers experimenting with multi-agent workflows
- Primary CTA: Fork or study https://github.com/Coding-Reality/base-agent-company

## Draft
Most agent demos stop at "the prompt worked once." A real agent company needs repeatable roles, durable memory, and visible handoffs. [base-agent-company](https://github.com/Coding-Reality/base-agent-company) gives you that with plain repo structure: roles are folders, instructions live in `AGENTS.md`, work moves through files, and PM2 triggers scheduled runs. If you can edit markdown and run a repo, you can build a working agent company in one focused session.

This matters because most multi-agent setups fail in boring places: no durable memory, no clear ownership, no simple audit trail, and no easy way to see what changed. A filesystem-based company solves that with primitives developers already understand: folders, markdown, git, and cron-style scheduling.

## What You Need
- A fork or local copy of https://github.com/Coding-Reality/base-agent-company
- The `codex` CLI installed and authenticated
- PM2 installed for scheduled runs
- One workflow you can describe as inputs, outputs, and handoffs

## What You Are Building
Your first agent company is not a chatbot swarm. It is a small operating system for work:

- A company tree that defines who exists and where they work
- Role instructions in `AGENTS.md`
- Shared policies and vision files that keep decisions aligned
- Local state in `memory/current-focus.md`
- File-based handoffs through `inbox/`, `outbox/`, and `reports/`
- Scheduled execution through PM2

The goal is not to make agents feel magical. The goal is to make their work inspectable.

## Step 1: Start From The Template
Begin with the framework repository:

- https://github.com/Coding-Reality/base-agent-company

Fork it or copy its structure into a new repository. Keep the default layout intact on your first pass. The structure is part of the operating model:

```text
board/
executive/
departments/
shared/
pm2/
scripts/
```

That layout gives you a company with top-down direction, department-level execution, and shared operating rules.

In the example company, a role looks like this:

```text
departments/marketing/content/
├── AGENTS.md
├── inbox/
├── memory/
├── outbox/
└── reports/
```

That pattern matters more than the department name. It gives every role the same contract: instructions, incoming work, durable context, outgoing requests, and dated outputs.

## Step 2: Pick One Real Workflow
Do not start by staffing a whole fake enterprise. Pick one workflow that already exists in your team and has obvious inputs and outputs.

Good first examples:

- Marketing content production
- Research monitoring
- Sales prospecting
- Internal operations reporting

Bad first examples:

- "Run my whole startup"
- "Autonomously do growth"
- Anything without a clear owner, handoff, or definition of done

If you can describe the workflow as a sequence of files being read and written, it is a good fit.

## Step 3: Define Roles Narrowly
Each role should have a constrained job. That means one area of responsibility, a clear reporting line, and explicit read/write expectations.

A strong role definition usually includes:

- Purpose
- What the role can decide
- What it must escalate
- Which files to read before acting
- Which files it must produce on each run
- Practical operating rules

In this model, `AGENTS.md` is the contract. Keep it specific enough that another agent run tomorrow would behave similarly.

An effective first role is "content writer for one tutorial" or "research analyst for one report," not "head of growth."

## Step 4: Use File Conventions As Your Coordination Layer
The core directories are simple, but they do real work:

- `inbox/` holds incoming work
- `outbox/` holds delegations and requests
- `reports/` holds recurring outputs
- `memory/` holds durable local context

This is the difference between an isolated prompt and an operating role. A role that writes reports, updates memory, and leaves a file trail can be reviewed, retried, or replaced without mystery.

Git becomes part of the runtime model. You can inspect decisions, compare runs, and see exactly which agent changed what.

## Step 5: Add The Minimum Shared Context
Your agents need enough shared context to avoid drifting apart. In practice, that means a few documents that define:

- What the company is trying to achieve
- How decisions should be made
- How files are named and used
- How git changes should be handled

Do not overbuild this. If the shared layer becomes a novel, agents stop using it and humans stop trusting it.

## Step 6: Wire Up Execution
The framework uses PM2 to schedule role runs. In this company instance, each role is registered in `pm2/ecosystem.config.cjs`, and each run routes through `scripts/run-agent.sh`.

That design is worth copying:

- PM2 handles recurring execution
- A single runner script gives you one place to define runtime behavior
- The role folder remains the source of truth for local context

The repository's bootstrap script keeps the first start simple:

```bash
pm2 start /path/to/your/repo/pm2/ecosystem.config.cjs
pm2 logs board-chair
```

You do not need a complex orchestration platform to get useful behavior. You need predictable schedules and disciplined file I/O.

## Step 7: Run One Department Before You Scale
Resist the urge to activate every role immediately. Start with one department and confirm that:

- The role reads the right files
- It produces useful output every run
- It updates memory cleanly
- It does not invent authority it does not have
- Its reports are good enough that a human could supervise it quickly

Once that works, add the manager above it. Then add adjacent roles. The company structure should grow only when the current structure is actually doing work.

## Step 8: Measure Output Quality, Not Agent Vibes
A successful run is not "the agent sounded smart." A successful run leaves artifacts that are useful.

Look for:

- Better drafts
- Faster research summaries
- Cleaner handoffs
- More consistent status reporting
- Less manual coordination overhead

If a role cannot produce a useful file, it is not operational yet.

## Common Failure Modes
Most early agent companies break in a few predictable ways:

- Roles are too broad, so outputs become vague
- Shared context is too thin, so roles drift
- Shared context is too large, so runs waste tokens
- Managers do not issue concrete priorities
- Teams automate schedules before they validate output quality

The fix is usually not more intelligence. It is tighter scope and cleaner operating rules.

## Why This Model Is Different
Many agent frameworks optimize for developer APIs. This one optimizes for operational clarity.

That tradeoff matters if you want to:

- Audit what happened
- Hand off work between roles
- Keep memory in the repo
- Let non-specialists edit role behavior
- Run the system with tools your team already knows

A folder tree is not flashy. It is durable.

## What To Do Next
If you want to test the model, fork [base-agent-company](https://github.com/Coding-Reality/base-agent-company), activate one workflow, and force yourself to keep the first version small.

Do not try to build an autonomous corporation in one pass. Build one reliable department, then one reliable manager, then the reporting loop around them.

That is how an agent company becomes real work instead of a demo.

Specific next action:
- Fork https://github.com/Coding-Reality/base-agent-company
- Duplicate one existing role
- Rewrite that role's `AGENTS.md` for a real workflow you already own
- Start PM2 and inspect the first report it produces

Start here: https://github.com/Coding-Reality/base-agent-company

## Notes For Publish Pass
- Add screenshots or repo tree snippets from `base-agent-company` if available.
- Consider a follow-up guide: "How to customize `AGENTS.md` without breaking role boundaries."
