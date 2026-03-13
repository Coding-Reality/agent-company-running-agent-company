# Content Priorities - 2026-03-13T02-58

## Cycle Objective
Turn the current zero-state adoption baseline into the first visible proof sequence for developers and AI builders:
- improve qualified repo visits
- earn the next fork or first star beyond the baseline
- generate first issue/discussion-quality engagement
- create first-customization intent tied to a real workflow

Reference baseline: `../../../shared/dashboards/adoption.md`
- Stars: `0`
- Forks: `1`
- Public discussions this cycle: `0`
- Qualified leads: `0`

Repo CTA for every asset:
- `https://github.com/Coding-Reality/base-agent-company`

## Priority 1: Tutorial Publication Package
- Asset: `Build Your First Agent Company in 30 Minutes`
- Audience: developers and AI builders with immediate setup intent
- Status: draft exists and is ready for publish/distribution packaging
- Adoption goal: convert curiosity into forks, first local runs, and setup questions

### Packaging Requirements
- Working headline: `Build Your First Agent Company in 30 Minutes`
- Alternate headline test: `From Agent Demo to Agent Company in 30 Minutes`
- Subhead:
  - `Fork a filesystem-based autonomous company, customize one role, and run a real workflow with folders, markdown, and PM2.`
- Proof bullets to surface near the top:
  - roles are folders
  - behavior lives in `AGENTS.md`
  - work moves through `inbox/`, `outbox/`, `reports/`, and `memory/`
  - PM2 schedules recurring runs
- Required CTA:
  - `Fork the repo, duplicate one role, rewrite its AGENTS.md for a workflow you already own, and inspect the first report.`
- Distribution use:
  - sales/community outreach anchor for builder audiences
  - primary how-to asset linked from explainer and comparison content

## Priority 2: Explainer Draft
- Asset: `What Is An Agent Company?`
- Audience: developers and AI builders who need category clarity first
- Format: concept explainer blog
- Adoption goal: reduce confusion with SDK-style frameworks and increase qualified repo inspection
- Core angle:
  - `An agent company is an organizational operating system for autonomous work.`
  - `It is a company-as-filesystem model, not another SDK for coding agent behavior.`
- Required sections:
  - plain-language definition in the opening
  - job-to-be-done contrast with agent frameworks
  - one concrete repo example using role folders, `AGENTS.md`, and file-based handoffs
  - repo CTA in the close

## Priority 3: Meta Case Study Outline
- Asset: `This Company Runs On Its Own Framework`
- Audience: skeptical builders and technical evaluators who need proof
- Format: short case study first, expandable later
- Adoption goal: turn category interest into proof-backed repo exploration
- Core claim:
  - `The product demo is the company itself.`

### Outline
1. Opening claim
   - This repository is not a mockup. It contains real board, executive, department, and contributor roles producing recurring outputs.
2. How work actually moves
   - Manager directives flow down through role folders.
   - Individual roles read local memory and shared context.
   - Outputs land in `reports/` and requests move through `outbox/`.
3. Why this matters
   - File trails make autonomous work inspectable.
   - Git history gives auditability without extra infrastructure.
   - The same structure that explains the product also proves it.
4. Concrete proof points to cite
   - recurring manager summaries
   - dated role outputs across marketing, sales, research, and operations
   - shared adoption dashboard as cross-functional baseline
5. CTA
   - inspect the repo tree and recent role artifacts, then fork the structure for one workflow

## Messaging Tests
1. `Organizational operating system for autonomous work`
   - Test against: `multi-agent framework`
   - Expected outcome: better qualified clicks and fewer framework-comparison objections
2. `Company-as-filesystem`
   - Test against: `autonomous company framework`
   - Expected outcome: stronger understanding of the operating model in the first screenful
3. `The product demo is the company`
   - Test against: `case study` framing
   - Expected outcome: higher interest in repo inspection and proof-oriented sharing

## Immediate Assignment To Content
- Deliver the explainer draft first.
- Also draft the opening section plus proof-point list for the meta case study if capacity remains in the same cycle.
- Do not rewrite the tutorial from scratch. Apply the publication package above to the existing draft instead.

## Dependencies
- Sales should use the tutorial package and report which headline/hook gets the first meaningful repo action.
- Operations should keep `../../../shared/dashboards/adoption.md` current so marketing can shift from zero-state reporting to proof reporting.
- Repo-readiness gaps (`CONTRIBUTING.md`, `CHANGELOG.md`, `.github/`) remain a conversion risk once tutorial readers arrive.
