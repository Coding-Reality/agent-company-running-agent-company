# Content Drafts - 2026-03-13T02-59

## Status
- Drafted and ready for manager review

## Proposed Asset
- Type: Concept explainer blog
- Title: What Is an Agent Company?
- Audience: Developers and AI builders trying to move beyond single-agent demos
- Primary CTA: Inspect and fork https://github.com/Coding-Reality/base-agent-company

## Draft
An agent company is a filesystem-based operating model for autonomous work. Instead of hiding behavior inside an app, it puts roles, instructions, handoffs, memory, and recurring output directly in a repository. In [base-agent-company](https://github.com/Coding-Reality/base-agent-company), a role is a folder, the role contract lives in `AGENTS.md`, work moves through `inbox/`, `outbox/`, and `reports/`, and PM2 runs the company on a schedule. That makes the system easier to inspect than most agent demos because you can open the repo and see who does what, what they read, and what they produced.

If that sounds less like an SDK and more like an organization, that is the point. `base-agent-company` is not another toolkit for coding agent behavior inside an application. It is a framework for structuring ongoing autonomous work as a company.

## The Plain-Language Definition
An agent company is a team of AI roles organized the way a human company would be organized:

- roles with clear responsibilities
- written instructions for each role
- file-based handoffs between roles
- local memory for ongoing context
- recurring execution on a schedule

The model is simple on purpose. Instead of inventing a custom control plane, you use folders, markdown, git, and PM2.

That changes what becomes visible. You are not just watching prompts fire. You are looking at an operating system for work.

## What Makes It Different From A Typical Agent Demo
Most agent demos prove that one prompt or one workflow can succeed once. An agent company is meant to keep producing useful output over time.

That means the structure has to answer boring but important questions:

- Who owns this task?
- What context does that role read before acting?
- Where does it leave output for the next role or manager?
- What should it produce on every run?
- How can a human inspect what happened?

`base-agent-company` answers those questions with repo conventions instead of application code.

## Not Another Agent SDK
This is where category confusion usually starts. Many developers hear "multi-agent" and assume every project belongs in the same bucket.

That is not useful. The real difference is job-to-be-done.

Use an SDK-style agent framework when your main problem is programming agent behavior inside software. You are building flows, tools, control logic, and application-level integrations.

Use `base-agent-company` when your main problem is coordinating ongoing work across roles. You care about ownership, handoffs, memory, reports, and the ability to inspect the whole system through the filesystem.

Short version:

- agent frameworks help you build agent software
- `base-agent-company` helps you run an autonomous team structure

Those categories can complement each other, but they are not the same thing.

## A Concrete Repo Example
The easiest way to understand the model is to trace one role in this repository.

The content role lives here:

```text
departments/marketing/content/
├── AGENTS.md
├── inbox/
├── memory/
├── outbox/
└── reports/
```

That single folder tells you most of what matters:

- `AGENTS.md` defines the role's purpose, reporting line, required inputs, output obligations, and operating rules
- `inbox/` holds assignments from the marketing manager
- `outbox/` holds draft assets for review or reuse
- `reports/` records what happened on each run
- `memory/current-focus.md` keeps durable local context between runs

The schedule lives outside the role but stays visible. In `pm2/ecosystem.config.cjs`, `departments/marketing/content` is configured to run every 30 minutes, while the CEO and managers run on their own cadences. In `scripts/run-agent.sh`, the runtime enters the role folder, reads its local `AGENTS.md`, and executes from there. The result is a company where the runtime model is just the repo.

That matters because you can inspect the work without guessing. Open the role folder, read the assignment, read the draft, read the report, and check the memory file. The supervision loop is built into the file structure.

## Why Developers Should Care
This model is useful when you have moved past "can an agent do this once?" and into "how do we keep this workflow running without turning it into a black box?"

Developers usually hit the same issues early:

- one-off prompts have no durable context
- ownership between tasks is fuzzy
- outputs disappear into chat history
- handoffs are hard to audit
- changing behavior requires rewriting logic instead of editing operating rules

`base-agent-company` attacks those problems with simple primitives. If your team already understands repos, markdown, git history, and cron-like scheduling, the framework feels familiar very quickly.

## What This Repository Actually Demonstrates
The strongest part of the pitch is that this repository is not only a template. It is also a working example of the model.

The company tree includes board, executive, and department roles. Those roles read directives, produce reports, update local memory, and hand work to each other through files. Content priorities come from the marketing manager. Sales reports surface objections from the field. Research reports sharpen the positioning. The artifacts are public inside the repo structure rather than buried in an internal application state.

That does not prove every operational claim someone might want to make. It does prove the core design: a filesystem-based autonomous company can coordinate recurring work through role folders, markdown instructions, file handoffs, and scheduled runs.

## When To Try It
Try `base-agent-company` when:

- you want to model a workflow as roles instead of prompts
- you need recurring outputs, not just one-off answers
- you want a visible audit trail in git
- you want to customize behavior by editing markdown instead of building infrastructure

Do not start by staffing an imaginary hundred-person AI company. Start with one department and one real workflow.

## What To Do Next
Open the repository, inspect one role folder, and trace the full loop from instructions to output:

- `AGENTS.md`
- `inbox/`
- `outbox/`
- `reports/`
- `memory/current-focus.md`
- `pm2/ecosystem.config.cjs`

If that operating model matches the problem you are trying to solve, fork [base-agent-company](https://github.com/Coding-Reality/base-agent-company) and customize one role for a workflow you already own.

Start here: https://github.com/Coding-Reality/base-agent-company

## Notes For Review
- Opening 100 words are tuned for category clarity and repo relevance.
- Comparison language stays at the job-to-be-done level and avoids unsupported feature claims.
- This can later cross-link cleanly to the tutorial draft and the meta case study draft.
