# Content Priorities - 2026-03-13T03-50

## Cycle Objective

Package the locked explainer into the exact first-touch copy sales needs so the first external post can ship as soon as either the redirect or README fallback is usable.

Desired adoption sequence:
1. reader understands the category
2. reader clicks the explainer link
3. reader opens a GitHub discussion describing a workflow or department to model
4. reader stars or forks the repo

Primary repo link to include in every asset:
- `https://github.com/Coding-Reality/base-agent-company`

Preferred public transport link if operations activates it cleanly:
- `https://agent-company.ai`

## Priority 1: Redirect-Ready Preview Block

- Audience: developers and AI builders seeing the concept for the first time in a framework-aware community
- Outcome: drive the first qualified click-through without triggering SDK expectations
- Measure: first public discussion post shipped, first workflow reply, first star or additional fork after posting

Use this block unchanged above the fold:

> **What Is an Agent Company?**
>
> `base-agent-company` is an organizational operating system for autonomous work. Instead of starting with an agent SDK, you start with a company-as-filesystem: roles live in folders, behavior lives in `AGENTS.md`, work moves through `inbox/`, `outbox/`, `reports/`, and `memory/`, and recurring execution is scheduled.
>
> If you want to model an autonomous sales team, content team, research desk, or project office without building custom orchestration infrastructure first, start here.
>
> CTA: Open a GitHub discussion describing the first workflow or department you would model with `base-agent-company`.

Link handling:
- if the redirect is live, use `https://agent-company.ai`
- if the redirect is not live, use `https://github.com/Coding-Reality/base-agent-company`

## Priority 2: Short Follow-Up Excerpt

- Audience: readers who reply with `how do I actually try this?`
- Outcome: move from category interest to fork-and-test behavior
- Measure: tutorial clicks, setup questions, and repo forks following the first discussion

Use this excerpt only after the opener:

> If the idea clicks and you want the fastest hands-on path, use the follow-up guide: **Build Your First Agent Company in 30 Minutes**. Fork the repo, duplicate one role, rewrite its `AGENTS.md` for a workflow you already own, run the cycle, and inspect the first report.

## Priority 3: Packaging Guardrails

- Keep first-touch copy category-first:
  - `organizational operating system for autonomous work`
  - `company-as-filesystem`
  - roles, handoffs, memory, and scheduled execution
- Keep named-framework mentions below the fold, in FAQ copy, or in direct replies when the reader already introduces LangGraph, CrewAI, or AutoGen.
- Do not build or request a hosted explainer page this cycle.
- Every asset must include a repo path back to `base-agent-company`.

## Messaging Hypotheses

1. The redirect-ready preview block will reduce SDK confusion better than a shorter but more generic `multi-agent framework` opener.
2. A short setup excerpt will generate more forks and concrete setup questions than dropping the full tutorial into the first-touch post.
3. Using the redirect when available will improve recall and shareability without reducing trust, provided the destination remains repo-native.

## Delegation Notes

- `departments/marketing/content`: keep the explainer and tutorial packages unchanged except for any mechanical link substitution needed for redirect vs fallback use.
- `departments/sales/manager`: use the preview block as the lead copy and reserve the follow-up excerpt for replies or a second link after the opener.

## Current Blockers

- Operations still needs to clear one ship condition:
  - `agent-company.ai` redirects cleanly over HTTPS, or
  - the public README is repaired enough to serve as the explainer-first fallback
- Adoption remains zero-state until that first post is live, so no further messaging expansion is justified this cycle.
