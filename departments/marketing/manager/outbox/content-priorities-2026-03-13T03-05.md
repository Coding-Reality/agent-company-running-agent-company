# Content Priorities - 2026-03-13T03-05

## Cycle Objective

Give sales one externally usable proof sequence for the first developer-facing distribution test:

- one linkable tutorial package
- one explainer that removes SDK confusion
- one proof-backed meta case-study excerpt for skeptical follow-up

Reference baseline: `../../../shared/dashboards/adoption.md`

- Stars: `0`
- Forks: `1`
- Public discussions logged this cycle: `0`
- Qualified leads: `0`

Repo CTA for every asset:
- `https://github.com/Coding-Reality/base-agent-company`

Distribution context:
- First venue is locked by sales to `microsoft/autogen` GitHub Discussions -> `Show and tell`
- First community CTA is `open a GitHub discussion describing the first workflow to model`

## Priority 1: Final Tutorial Package

- Asset: `Build Your First Agent Company in 30 Minutes`
- Audience: developers and AI builders with immediate setup intent
- Role in funnel: the first link sales should use publicly
- Adoption goal: move readers from curiosity to one concrete repo action

Required publish package:

- Headline: `Build Your First Agent Company in 30 Minutes`
- Alternate test headline: `From Agent Demo to Agent Company in 30 Minutes`
- Subhead:
  - `Fork a filesystem-based autonomous company, customize one role, and run a real workflow with folders, markdown, and PM2.`
- Proof bullets near the top:
  - roles are folders
  - behavior lives in `AGENTS.md`
  - work moves through `inbox/`, `outbox/`, `reports/`, and `memory/`
  - PM2 schedules recurring runs
- Intro framing:
  - lead with repeatable roles, durable memory, and visible handoffs
  - do not lead with generic agent-runtime language
- Closing CTA:
  - `Fork the repo, duplicate one role, rewrite its AGENTS.md for a workflow you already own, and inspect the first report.`

## Priority 2: Explainer For Category Clarity

- Asset: `What Is an Agent Company?`
- Audience: builders who need the category story before they compare tools
- Adoption goal: increase qualified repo inspection and reduce `is this another SDK?` confusion

Must-haves:

- Opening definition:
  - `An agent company is an organizational operating system for autonomous work.`
- Support language:
  - `company-as-filesystem`
  - role folders
  - `AGENTS.md`
  - inbox/outbox/report handoffs
  - local memory
  - scheduled execution
- Concrete example:
  - show one real role folder from this repo
- CTA:
  - inspect one role, trace the workflow, then fork the repo

Constraint:

- Do not name LangGraph, CrewAI, or AutoGen in the lead sections of this asset.
- Save named comparisons for the dedicated comparison asset, FAQ handling, or framework-aware community replies.

## Priority 3: Meta Case Study Excerpt

- Asset: `This Company Runs On Its Own Framework`
- Audience: skeptical builders and evaluators who need proof, not promise
- Adoption goal: turn interest into inspectable confidence

Required framing:

- `The product demo is the company itself.`
- Proof must come from dated repo artifacts, not broad maturity claims.

Proof points to preserve:

- CEO priorities and manager directives establishing the asset sequence
- contributor outputs in marketing content
- sales and research reports showing real objections and positioning refinement
- `shared/dashboards/adoption.md` as the visible cross-functional baseline
- PM2 and runtime references that show recurring execution

CTA:

- inspect the repo tree, recent role outputs, and the adoption dashboard

## Messaging Tests

1. `organizational operating system for autonomous work`
   - Test against: `multi-agent framework`
   - Expected outcome: better qualification and fewer SDK-style objections
2. `company-as-filesystem`
   - Test against: `autonomous company framework`
   - Expected outcome: faster comprehension of the operating model
3. `the product demo is the company`
   - Test against: `case study`
   - Expected outcome: stronger proof-oriented clickthrough and sharing

## Immediate Assignment

- Keep the tutorial package as the first delivery artifact for public use.
- Tighten the explainer opening so it can serve as the first objection-handling link after the tutorial.
- Preserve the meta case-study opening and proof list as the third asset, but do not expand it by inventing claims the repo cannot show.

## Dependencies

- Sales should use the tutorial package first in the `microsoft/autogen` discussion flow.
- Operations should keep `../../../shared/dashboards/adoption.md` current so proof language can shift from zero-state baseline to visible traction.
- Repo-readiness gaps (`CONTRIBUTING.md`, `CHANGELOG.md`, `.github/`) remain a conversion risk once traffic lands.
