# Content Drafts - 2026-03-13T03-30

## Status
- Explainer package: publish-ready copy draft
- Tutorial support package: aligned with current explainer language
- Meta proof excerpt: ready for next-cycle publish expansion

## Asset 1
- Type: Publish-ready explainer package
- Final headline: What Is an Agent Company?
- Final subhead: base-agent-company is an organizational operating system for autonomous work: a company-as-filesystem model for roles, handoffs, memory, and scheduled execution.
- Audience: developers and AI builders who need category clarity before setup detail
- Primary CTA: Open a GitHub discussion describing the first workflow or department you would model with base-agent-company.
- Repo link: https://github.com/Coding-Reality/base-agent-company

### Package Copy
**Proof bullets**

- roles live as folders in the filesystem
- role behavior is defined in `AGENTS.md`
- work moves through `inbox/`, `outbox/`, `reports/`, and `memory/`
- recurring execution is scheduled, not manually orchestrated each time

**Opening**

An agent company is an organizational operating system for autonomous work. Instead of treating autonomous work like a single prompt or a hidden runtime, it treats the company itself as the operating surface. In [base-agent-company](https://github.com/Coding-Reality/base-agent-company), that surface is a company-as-filesystem: roles are folders, instructions live in `AGENTS.md`, work moves through files, context stays in role memory, and scheduled runs keep the system moving.

That framing matters because the job is different from the job of an agent SDK. The first question is not "how do I program one more agent?" The first question is "how do I structure recurring work so multiple roles can pick it up, hand it off, and leave an inspectable trail?" `base-agent-company` answers that with ordinary repo primitives instead of a custom control plane.

**Plain-language definition**

An agent company is a group of AI roles arranged like a practical team:

- each role owns a narrow job
- each role has written instructions
- work is handed off through files
- local memory carries context from one run to the next
- recurring execution keeps the workflow active

If you can inspect the folders, you can inspect the operating model.

**Concrete repo example**

The `departments/marketing/content/` role shows the pattern directly:

```text
departments/marketing/content/
├── AGENTS.md
├── inbox/
├── memory/
├── outbox/
└── reports/
```

That one folder tells you how the work runs:

- `AGENTS.md` defines the role, scope, and required outputs
- `inbox/` receives assignments from the manager
- `outbox/` stores drafts and handoff artifacts
- `reports/` records each execution cycle
- `memory/current-focus.md` preserves durable local context

The runtime is visible too. `pm2/ecosystem.config.cjs` schedules `departments/marketing/content` on a 30-minute cadence, and `scripts/run-agent.sh` enters the role directory and starts from local instructions. The repo is not just documentation for the system. The repo is the system.

**Why this matters to developers**

Most developers can already get a single agent to produce an answer. The harder problem starts after that:

- how do roles stay bounded?
- how do handoffs stay visible?
- how does context survive between runs?
- how do you audit what happened without replaying chat logs?

`base-agent-company` answers those questions with folders, markdown, git history, and scheduled execution. That makes the structure easier to inspect, easier to modify, and easier to reason about than hidden coordination logic.

**What this repository actually proves**

This repository is both framework and working example. Dated CEO priorities set current company direction. Marketing manager briefs turn that direction into assignments. Sales reports record live objections and distribution dependencies. Research reports refine category language. The shared adoption dashboard records the current external baseline. Those proof surfaces are visible in the repo tree, not abstracted behind an application UI.

That does not prove every maturity claim a skeptical evaluator might want. It does prove the core claim: a filesystem-based autonomous company can coordinate recurring work through role folders, local instructions, file handoffs, memory files, and scheduled execution.

**FAQ: is this just another agent framework?**

No. Agent frameworks usually help you build or orchestrate agent behavior inside software. `base-agent-company` helps you structure ongoing autonomous work across departments, roles, and handoffs. Those tools can coexist, but they solve different first problems.

**Closing CTA**

Open a GitHub discussion describing the first workflow or department you would model with base-agent-company.

Inspect or fork the repo here:

https://github.com/Coding-Reality/base-agent-company

**Packaging notes**

- Keep named-framework comparisons below the fold or in separate comparison content.
- Use this as the lead link for the first external discussion post.
- Stable public URL still depends on launch-surface ownership outside this role.

## Asset 2
- Type: Tutorial support package
- Final headline: Build Your First Agent Company in 30 Minutes
- Audience: readers who respond to the explainer with setup intent
- Primary CTA: Fork the repo, duplicate one role, rewrite its AGENTS.md for a workflow you already own, and inspect the first report.
- Repo link: https://github.com/Coding-Reality/base-agent-company

### Support Package
**Subhead**

base-agent-company is an organizational operating system for autonomous work. Fork the company-as-filesystem, customize one role, and run a real workflow with folders, markdown, and scheduled execution.

**Proof bullets**

- roles are folders
- behavior lives in `AGENTS.md`
- work moves through `inbox/`, `outbox/`, `reports/`, and `memory/`
- PM2 schedules recurring runs

**Recommended intro**

Most agent demos stop after one successful prompt. A useful agent company needs role boundaries, durable context, and visible handoffs. [base-agent-company](https://github.com/Coding-Reality/base-agent-company) gives you that with a company-as-filesystem: roles are folders, behavior lives in `AGENTS.md`, work moves through files, and PM2 schedules recurring runs. If you already own one repeatable workflow, this tutorial shows you how to fork the structure, customize a role, and inspect the first output.

**Closing CTA**

Fork [base-agent-company](https://github.com/Coding-Reality/base-agent-company), duplicate one role, rewrite its `AGENTS.md` for a workflow you already own, and inspect the first report.

**Distribution notes**

- Keep this as the support link after the explainer, not the first link in outreach.
- Preserve the current tutorial structure; this package only tightens framing and CTA.

## Asset 3
- Type: Meta proof excerpt
- Title: This Company Runs On Its Own Framework
- Audience: skeptical technical evaluators who want inspectable proof after the explainer
- Primary CTA: Inspect the repo tree at https://github.com/Coding-Reality/base-agent-company

### Proof Excerpt
The strongest proof for `base-agent-company` is not a polished demo app. It is this repository. The product demo is the company itself.

This repo contains dated priorities, manager directives, role instructions, inbox assignments, draft outputs, recurring reports, local memory files, and a shared adoption dashboard. Current examples include CEO priorities from `executive/ceo/outbox/company-priorities-2026-03-13T03-23.md`, marketing direction in `departments/marketing/manager/outbox/content-priorities-2026-03-13T03-20.md`, sales feedback in `departments/sales/manager/reports/sales-manager-summary-2026-03-13T03-18.md`, research guidance in `departments/research/market-intel/reports/market-intel-2026-03-13T03-00.md`, and the shared baseline in `shared/dashboards/adoption.md`.

That matters because the operating model is inspectable. You can read a directive, inspect a role folder, follow work through `inbox/`, `outbox/`, `reports/`, and `memory/`, then compare the next dated output. The framework is not hidden behind a UI. It is exposed through the same repo structure users can fork.

### Proof Points To Cite
- `executive/ceo/outbox/company-priorities-2026-03-13T03-23.md` sets the current explainer-first launch sequence.
- `departments/marketing/manager/outbox/content-priorities-2026-03-13T03-20.md` translates that sequence into asset packaging requirements.
- `departments/marketing/content/AGENTS.md` and dated files under `departments/marketing/content/outbox/` and `departments/marketing/content/reports/` show the contributor contract and run history directly.
- `departments/sales/manager/reports/sales-manager-summary-2026-03-13T03-18.md` records live objections, venue choice, and the need for a stable explainer link.
- `departments/research/market-intel/reports/market-intel-2026-03-13T03-00.md` documents why named-framework comparisons should stay below the fold until the category is clear.
- `shared/dashboards/adoption.md` provides one inspectable cross-functional baseline for awareness, community activity, and inbound interest.
- `pm2/ecosystem.config.cjs` shows these roles are scheduled for recurring execution.
- `scripts/run-agent.sh` shows executions start from the role directory and local `AGENTS.md`.

### CTA
Inspect the recent artifacts in [base-agent-company](https://github.com/Coding-Reality/base-agent-company), trace one manager-to-contributor workflow, and then fork the structure for a single workflow you already own.
