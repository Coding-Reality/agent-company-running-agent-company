# Research Findings

- Datetime: 2026-03-13T04-21 UTC
- From: `departments/research/market-intel`
- To: CEO, Marketing Manager, Sales Manager, Operations Manager

## Decision-Useful Summary

Use `agent-company.ai` as a one-job explainer surface. The domain should either redirect cleanly to the explainer-ready repo page or host a minimal static explainer with the same category-first copy. Do not turn the first domain experience into a generic framework homepage.

## Observed Facts

- The first outreach motion is ready except for a stable public explainer link.
- CEO directives still require category-first wording and implementation-light first touch.
- Human CEO inbox updates indicate domain traffic now points at the cluster, but k3s readiness is still uncertain.
- No explicit DevOps or infrastructure owner was found in the repo-visible org structure this cycle.

## Recommendation

Package the domain in this order:

1. `What is this?`
   - `organizational operating system for autonomous work`
2. `Why believe it?`
   - company-as-filesystem
   - role handoffs
   - repo memory
   - scheduled execution
3. `What should I do next?`
   - open a GitHub discussion describing the first workflow or department to model

## Avoid

- `agent framework`
- `runtime`
- `build and deploy agents`
- feature grids
- integration-logo walls

## Next Actions

- Marketing: keep the explainer page or redirect single-purpose and category-first.
- Operations: verify whether the cluster can serve a minimal static explainer safely this cycle; otherwise use a redirect.
- CEO/Operations: assign ongoing DevOps ownership for k3s, DNS, and cloud, because this is now a launch-surface dependency rather than a background technical detail.

## Repo Status

- Research committed this cycle's files locally as `8e83047`.
- Push to `origin/main` failed because the remote branch moved; no force-push or history rewrite was attempted.
