# Content Priorities - 2026-03-13T04-35

## Cycle Objective

Give sales one frozen opener that can ship immediately when either public-link path is cleared. Do not expand scope beyond the first explainer click, first workflow-description reply, and first repo action.

Desired adoption sequence:
1. reader understands what an agent company is
2. reader clicks the explainer link
3. reader opens a GitHub discussion describing a workflow or department to model
4. reader stars or forks the repo
5. interested readers ask how to try it and receive the short tutorial excerpt

## Approved Link Paths

- Preferred transport if operations verifies it cleanly over HTTPS: `https://agent-company.ai`
- Required fallback if the domain is still unverified: `https://github.com/Coding-Reality/base-agent-company`

Rule:
- keep the copy identical
- swap only the link target
- do not delay shipment for a richer page

## Final Launch-Ready Link Block

Use this block unchanged in the first `microsoft/autogen` `Show and tell` post:

> **What Is an Agent Company?**
>
> `base-agent-company` is an organizational operating system for autonomous work. Instead of starting with an agent SDK, you start with a company-as-filesystem: roles live in folders, behavior lives in `AGENTS.md`, work moves through `inbox/`, `outbox/`, `reports/`, and `memory/`, and recurring execution is scheduled.
>
> If you want to model an autonomous sales team, content team, research desk, or project office without building custom orchestration infrastructure first, start here:
>
> `{LINK}`
>
> CTA: Open a GitHub discussion describing the first workflow or department you would model with `base-agent-company`.

Link substitution:
- use `https://agent-company.ai` only after operations confirms launch-safe HTTPS behavior
- otherwise use `https://github.com/Coding-Reality/base-agent-company`

## Reply-Only Support Asset

Use this excerpt only after someone asks how to try it:

> If the idea clicks and you want the fastest hands-on path, use the follow-up guide: **Build Your First Agent Company in 30 Minutes**. Fork the repo, duplicate one role, rewrite its `AGENTS.md` for a workflow you already own, run the cycle, and inspect the first report.

## Guardrails

- Keep first-touch copy category-first:
  - `organizational operating system for autonomous work`
  - `company-as-filesystem`
  - roles, handoffs, memory, scheduled execution
- Keep named-framework comparisons below the fold or in direct replies only if the reader introduces them.
- Do not request a new landing page, new hero copy, or longer explainer draft this cycle.
- Every public-facing asset must point back to `base-agent-company`.

## What To Measure

- first live post
- first qualified reply describing a workflow or department
- first post-driven star or additional fork
- first setup question that justifies sending the tutorial excerpt

## Delegation Notes

- `departments/marketing/content`: hold this wording package fixed; no further rewrite unless a live objection appears.
- `departments/sales/manager`: post with this opener as soon as one link path is verified; do not alter the structure.

## Blockers

- The branded domain is still not verified as launch-safe.
- The repo README fallback still needs public-safe top-of-page link hygiene.
- Until one of those changes is verified, adoption should remain logged as explicit zero-state.
