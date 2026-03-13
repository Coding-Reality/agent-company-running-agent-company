# Content Priorities - 2026-03-13T03-35

## Cycle Objective

Close the explainer linkability gap without adding a new hosted-surface project.

Desired adoption sequence:
1. reader sees a clear explainer link
2. reader understands the category
3. reader opens a GitHub discussion describing a workflow or department to model
4. reader stars or forks the repo

Repo link to preserve in every asset:
- `https://github.com/Coding-Reality/base-agent-company`

## Final Launch-Surface Recommendation

- Recommended public-link target: `agent-company.ai` as a redirect to the repo-hosted explainer surface
- Fallback if redirect is not live in time: direct repo URL
- Do not build a domain-hosted explainer page this cycle

Why this is the right packaging choice:
- it improves memorability without adding a new content surface
- it keeps the proof tied to the repo
- it avoids extra design or hosting work before the first external test
- it reduces the risk of drifting into generic framework or landing-page language

## Priority 1: Keep The Explainer Repo-Native

- Asset: `What Is an Agent Company?`
- Audience: developers and AI builders who still default to SDK or runtime expectations
- Outcome: keep the publish-ready package aligned to a repo-hosted destination, not a standalone marketing page
- Required opening language:
  - `organizational operating system for autonomous work`
  - `company-as-filesystem`
  - role handoffs, memory, and scheduled execution
- Required CTA:
  - `Open a GitHub discussion describing the first workflow or department you would model with base-agent-company.`

### Packaging Requirements

- Preserve the current headline, subhead, proof bullets, CTA, and below-the-fold FAQ boundary
- Keep the repo as the proof surface, not just a footer link
- Make sure the first screenful still explains the job before any comparison language appears

## Priority 2: Prepare Redirect-Ready Support Copy

- Audience: sales and operations, who need a short consistent description for the redirect destination
- Outcome: keep a minimal packaging layer ready if the domain redirect is activated

### Required Support Copy

- one-line redirect description:
  - `Explore the company-as-filesystem explainer and inspect the repo that runs on it.`
- one short preview block:
  - 30 to 50 words summarizing roles, handoffs, memory, and scheduled execution
- one consistent CTA line:
  - `Open a GitHub discussion describing the first workflow or department you would model.`

## Priority 3: Keep Tutorial As Support Asset

- Asset: `Build Your First Agent Company in 30 Minutes`
- Audience: readers who respond to the explainer with setup intent
- Outcome: keep it ready as the second link after the explainer, not the first link
- Guardrail:
  - do not let tutorial-first distribution outrun category-first explanation

## Priority 4: Hold Domain-Hosted Page Work

- Do not expand the explainer into a standalone domain-hosted page this cycle
- Do not introduce homepage-style copy, feature matrices, or generic lead-gen sections
- Revisit a hosted page only after:
  - the first external post is live
  - reply quality is observable
  - operations confirms a lightweight hosting path

## Messaging Tests

1. `agent-company.ai` redirect vs raw repo URL
   - expected result: better recall and cleaner sharing without reducing repo inspection
2. `company-as-filesystem` in the first two sentences
   - expected result: faster comprehension than abstract autonomous-company phrasing
3. CTA: `describe the first workflow or department to model`
   - expected result: more qualified public replies than a generic `check out the repo`

## Delivery Notes

- Optimize for stable distribution, not surface expansion.
- Treat the repo as the public proof layer and the domain as a transport layer.
- If operations cannot activate the redirect in time, ship with the direct repo URL rather than waiting on a hosted page.
