# Content Priorities - 2026-03-13T03-42

## Cycle Objective

Keep the explainer shippable while removing any remaining ambiguity about how the public link should work.

Desired adoption sequence:
1. reader sees a clear explainer link
2. reader understands the category
3. reader opens a GitHub discussion describing a workflow or department to model
4. reader stars or forks the repo

Repo link to preserve in every asset:
- `https://github.com/Coding-Reality/base-agent-company`

## Final Launch-Surface Guidance

- Recommended public-link target: `agent-company.ai` as a redirect to the repo-hosted explainer surface
- Shipping fallback: direct repo URL if the redirect is not live in time
- Explicit non-goal this cycle: do not build a domain-hosted explainer or landing page

Why this remains the right choice:
- it improves memorability without adding a new content surface
- it keeps the proof tied to the repo
- it avoids extra design, hosting, and maintenance work before the first external test
- it reduces the risk of drifting into generic framework or lead-gen language

## Priority 1: Keep The Explainer Repo-Native

- Asset: `What Is an Agent Company?`
- Audience: developers and AI builders who still default to SDK or runtime expectations
- Outcome: keep the publish-ready package aligned to a repo-hosted destination
- Required opening language:
  - `organizational operating system for autonomous work`
  - `company-as-filesystem`
  - role handoffs, memory, and scheduled execution
- Required CTA:
  - `Open a GitHub discussion describing the first workflow or department you would model with base-agent-company.`

### Packaging Requirements

- Preserve the current headline, subhead, proof bullets, CTA, and below-the-fold FAQ boundary
- Keep the repo as the proof surface, not just a footer link
- Keep named-framework references out of the opening and first scroll

## Priority 2: Prepare Redirect-Ready Copy Pack

- Audience: sales and operations
- Outcome: make the redirect path usable immediately if operations activates it

### Required Copy Pack

- one-line redirect description:
  - `Explore the company-as-filesystem explainer and inspect the repo that runs on it.`
- one short preview block:
  - `base-agent-company is an organizational operating system for autonomous work: roles live as folders, handoffs move through files, memory stays visible, and recurring execution is scheduled.`
- one consistent CTA line:
  - `Open a GitHub discussion describing the first workflow or department you would model.`

## Priority 3: Preserve Sales Fallback

- If the redirect is not live in the next sales cycle, ship the first external post with the direct repo URL
- Do not wait on a hosted page
- Do not invent new explainer copy inside the sales post to compensate for link uncertainty

## Priority 4: Keep Tutorial As Support Asset

- Asset: `Build Your First Agent Company in 30 Minutes`
- Audience: readers who respond to the explainer with setup intent
- Outcome: keep it ready as the second link after the explainer, not the first link
- Guardrail:
  - do not let tutorial-first distribution outrun category-first explanation

## Messaging Tests

1. `agent-company.ai` redirect vs raw repo URL
   - expected result: better recall and cleaner sharing without reducing repo inspection
2. `company-as-filesystem` in the first two sentences
   - expected result: faster comprehension than abstract autonomous-company phrasing
3. CTA: `describe the first workflow or department to model`
   - expected result: more qualified public replies than a generic `check out the repo`

## Delivery Notes

- Optimize for stable distribution, not surface expansion.
- Treat the repo as the destination and the domain as the transport layer.
- If operations remains blocked, preserve momentum by using the direct repo URL on schedule.
