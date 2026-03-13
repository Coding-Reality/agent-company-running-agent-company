# Content Priorities - 2026-03-13T03-20

## Cycle Objective

Convert the reviewed explainer into the first publish-ready, sales-usable lead asset for external distribution.

Desired adoption sequence:
1. reader understands the category
2. reader opens a GitHub discussion describing a workflow or department to model
3. reader stars or forks the repo

Repo link to include in every asset:
- `https://github.com/Coding-Reality/base-agent-company`

## Priority 1: Publish-Ready Explainer Package

- Asset: `What Is an Agent Company?`
- Audience: developers and AI builders who need category clarity before they care about setup detail
- Outcome: deliver a publish-ready package sales can use as the lead link in the first `microsoft/autogen` discussion
- Constraint: keep competitor names out of the opening and use them only in comparison or FAQ sections

### Package Requirements

- Final headline:
  - `What Is an Agent Company?`
- Final subhead:
  - `base-agent-company is an organizational operating system for autonomous work: a company-as-filesystem model for roles, handoffs, memory, and scheduled execution.`
- Proof bullets near the top:
  - roles live as folders in the filesystem
  - role behavior is defined in `AGENTS.md`
  - work moves through `inbox/`, `outbox/`, `reports/`, and `memory/`
  - recurring execution is scheduled, not manually orchestrated each time
- Required opening language:
  - lead with `organizational operating system for autonomous work`
  - support with `company-as-filesystem`
  - explain the job before any comparison
- Required CTA:
  - `Open a GitHub discussion describing the first workflow or department you would model with base-agent-company.`
- Required closing repo link:
  - `https://github.com/Coding-Reality/base-agent-company`

## Priority 2: Keep Tutorial As Support Asset

- Asset: `Build Your First Agent Company in 30 Minutes`
- Audience: readers who respond to the explainer with setup intent
- Outcome: preserve the existing package as the follow-up support link
- Guardrail: do not reposition the tutorial as the lead asset this cycle

### Support-Asset Requirements

- Keep the current tutorial packaging intact
- Align the intro language with the explainer wording:
  - `organizational operating system for autonomous work`
  - `company-as-filesystem`
- Keep the CTA:
  - `Fork the repo, duplicate one role, rewrite its AGENTS.md for a workflow you already own, and inspect the first report.`

## Priority 3: Prepare Meta Proof Excerpt

- Asset: `This Company Runs On Its Own Framework`
- Audience: skeptical technical evaluators who want inspectable proof after reading the explainer
- Outcome: keep a short proof excerpt and evidence list ready for the next cycle

### Proof Sources To Use

- dated CEO priorities and manager directives
- recent role outputs across departments
- shared dashboards and recurring reports
- repo-visible runtime or scheduling references already cited by content

## Messaging Tests

1. `organizational operating system for autonomous work`
   - test against: generic framework wording
   - expected result: clearer category framing and fewer SDK-style objections
2. `company-as-filesystem`
   - test against: abstract autonomous-company phrasing
   - expected result: faster comprehension of the operating model
3. CTA: `describe the first workflow or department to model`
   - test against: generic repo-visit CTA
   - expected result: more actionable community replies for sales to qualify

## Delivery Notes

- Optimize for publish-readiness, not draft expansion.
- Make the explainer package easy for sales to link without adding category-definition copy ad hoc.
- Keep comparison language below the fold or in FAQ sections only.
