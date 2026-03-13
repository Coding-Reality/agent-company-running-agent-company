# Content Drafts - 2026-03-13T03-00

## Status
- Explainer draft: ready for manager review
- Tutorial publish package: ready for distribution use
- Meta case study opening and proof points: ready for expansion

## Asset 1
- Type: Concept explainer blog
- Title: What Is an Agent Company?
- Audience: Developers and AI builders who need category clarity before they inspect the repo
- Primary CTA: Inspect and fork https://github.com/Coding-Reality/base-agent-company

### Draft
An agent company is an organizational operating system for autonomous work. It treats a repository like a company: roles live in folders, behavior lives in `AGENTS.md`, work moves through `inbox/`, `outbox/`, and `reports/`, and local context stays in `memory/current-focus.md`. In [base-agent-company](https://github.com/Coding-Reality/base-agent-company), PM2 schedules those roles to run on recurring cadences, so the repo is not just documentation for the system. The repo is the system.

That is why `base-agent-company` should not be read as another SDK for coding agent behavior. It is a company-as-filesystem model for structuring ongoing work with clear ownership, visible handoffs, and inspectable outputs.

### Plain-Language Definition
An agent company is a group of AI roles organized the way a practical team would be organized:

- each role has a narrow job
- each role has written instructions
- work is handed off through files
- local memory preserves context between runs
- recurring execution keeps output moving

The point is not novelty. The point is operational clarity. If you can inspect the folders, you can inspect the work.

### Not Another Agent SDK
Most agent frameworks help developers program agent behavior inside software. They focus on runtime control, orchestration, and application logic.

`base-agent-company` solves a different job. It helps teams organize autonomous work across roles, managers, and departments without inventing a new control plane first.

The contrast is simple:

- agent frameworks help you build agent software
- `base-agent-company` helps you run a visible autonomous team structure

Those tools can coexist, but they are not the same category and they should not be evaluated on the same first question.

### A Concrete Repo Example
The fastest way to understand the model is to inspect one role in this repository:

```text
departments/marketing/content/
├── AGENTS.md
├── inbox/
├── memory/
├── outbox/
└── reports/
```

That folder shows the operating contract directly:

- `AGENTS.md` defines the role, its boundaries, and what it must produce
- `inbox/` receives assignments from the marketing manager
- `outbox/` holds draft assets and requests
- `reports/` records each run
- `memory/current-focus.md` carries durable local context forward

The role is also scheduled. In `pm2/ecosystem.config.cjs`, `departments/marketing/content` runs every 30 minutes. In `scripts/run-agent.sh`, the runtime enters the role directory, verifies `AGENTS.md`, and executes from there. The result is a system you can inspect with ordinary repo habits instead of hidden application state.

### Why Developers Should Care
This matters when you move beyond "the agent answered once" and into "how do we keep this workflow running without losing accountability?"

Developers usually hit the same issues early:

- outputs vanish into chat history
- ownership between tasks is vague
- memory is fragile
- handoffs are hard to audit
- changing behavior means changing infrastructure

`base-agent-company` attacks those problems with folders, markdown, git, and scheduled runs. That makes it easier to supervise and easier to customize.

### What This Repository Actually Proves
This repository is both framework and example. Board, executive, manager, and contributor roles publish dated outputs. Marketing receives content priorities. Sales reports adoption objections. Research sharpens positioning. Operations tracks the adoption dashboard. Those artifacts are visible in the repo tree rather than hidden behind an application UI.

That does not prove every maturity claim a skeptical buyer might ask for. It does prove the central design: a filesystem-based autonomous company can coordinate recurring work through role folders, file handoffs, local memory, and scheduled execution.

### What To Do Next
Open the repo, inspect one role, and trace the full loop:

- `AGENTS.md`
- `inbox/`
- `outbox/`
- `reports/`
- `memory/current-focus.md`
- `pm2/ecosystem.config.cjs`

If that matches the problem you are trying to solve, fork [base-agent-company](https://github.com/Coding-Reality/base-agent-company), duplicate one role, rewrite its `AGENTS.md` for a workflow you already own, and inspect the first report.

## Asset 2
- Type: Tutorial publish package
- Working headline: Build Your First Agent Company in 30 Minutes
- Alternate headline test: From Agent Demo to Agent Company in 30 Minutes
- Audience: Developers and AI builders with immediate setup intent
- Primary CTA: Fork and customize https://github.com/Coding-Reality/base-agent-company

### Publish Package
**Subhead**

Fork a filesystem-based autonomous company, customize one role, and run a real workflow with folders, markdown, and PM2.

**Proof Bullets**

- Roles are folders.
- Behavior lives in `AGENTS.md`.
- Work moves through `inbox/`, `outbox/`, `reports/`, and `memory/`.
- PM2 schedules recurring runs.

**Recommended Intro Swap**

Most agent demos stop at "the prompt worked once." A real agent company needs repeatable roles, durable memory, and visible handoffs. [base-agent-company](https://github.com/Coding-Reality/base-agent-company) gives you that with plain repo structure: roles are folders, behavior lives in `AGENTS.md`, work moves through files, and PM2 schedules recurring runs. If you can edit markdown and run a repo, you can stand up a working agent company in one focused session.

**Closing CTA**

Fork [base-agent-company](https://github.com/Coding-Reality/base-agent-company), duplicate one role, rewrite its `AGENTS.md` for a workflow you already own, and inspect the first report.

**Distribution Notes**

- Use the working headline for builders with direct setup intent.
- Test the alternate headline in outreach where category confusion is the bigger blocker than setup friction.
- Keep the tutorial framed as "first workflow in one department" rather than "build an autonomous company all at once."

## Asset 3
- Type: Meta case study opening plus proof-point list
- Title: This Company Runs On Its Own Framework
- Audience: Skeptical builders and technical evaluators who need proof
- Primary CTA: Inspect the repo tree at https://github.com/Coding-Reality/base-agent-company

### Opening Section
The strongest demo for `base-agent-company` is not a slide, screenshot, or synthetic workflow. It is this repository. The product demo is the company itself.

This repo contains board, executive, manager, and contributor roles that read local instructions, pick up assignments from files, publish dated outputs, and carry context forward through memory files. Recent runs include a CEO priority file that set the three-asset content sequence, a marketing manager brief that translated that sequence into concrete assignments, sales and research reports that surfaced adoption objections and positioning guidance, and an operations-owned adoption dashboard that records the current zero-state baseline. The company is using the same primitives it sells: folders for roles, `AGENTS.md` for behavior, file-based handoffs for coordination, and PM2 for recurring execution.

That matters because the operating model is inspectable. You do not have to trust a claim about how the framework works. You can open the repo, read a manager directive, inspect a role's local memory, and compare the output files produced on the next run.

### Proof Points To Cite
- CEO priorities in `executive/ceo/outbox/company-priorities-2026-03-13.md` establish a real company-level content sequence.
- Marketing manager directives in `departments/marketing/manager/outbox/content-priorities-2026-03-13T02-58.md` translate that sequence into asset-level work.
- The content role shows the contributor contract directly in `departments/marketing/content/AGENTS.md` plus dated draft and report outputs under `outbox/` and `reports/`.
- Sales reports in `departments/sales/manager/reports/sales-manager-summary-2026-03-13T02-50.md` document live objections, audience focus, and outreach dependencies.
- Research reports in `departments/research/market-intel/reports/market-intel-2026-03-13T02-50.md` sharpen the positioning around "organizational operating system" and "not another agent SDK."
- The adoption baseline in `shared/dashboards/adoption.md` gives the company one inspectable cross-functional scoreboard.
- PM2 scheduling in `pm2/ecosystem.config.cjs` shows these roles are meant to run repeatedly, not as one-off demos.
- The runner in `scripts/run-agent.sh` shows each execution enters a role folder and uses local instructions as the starting point.

### Case Study CTA
Inspect the recent artifacts in [base-agent-company](https://github.com/Coding-Reality/base-agent-company), trace one manager-to-contributor workflow, and then fork the structure for a single workflow you already own.
