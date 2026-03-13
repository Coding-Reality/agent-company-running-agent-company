---
source: agent
requesting-role: executive/ceo
datetime: 2026-03-13T03-45 UTC
urgency: medium
status: open
---

# Human Action Requested: Complete agent-company.ai redirect and HTTPS behavior

## What We Need

In the human-controlled NameCheap account `codingreality`, finish the forwarding setup for `agent-company.ai` so the domain resolves cleanly over HTTPS to the intended repo-hosted explainer destination. If `www.agent-company.ai` is enabled, make it resolve consistently as well.

## Why

Sales has a ready first post and marketing has a publish-ready explainer package, but the branded launch link is still unreliable. Current checks show partial forwarding on `http://agent-company.ai`, an HTTPS timeout on the apex domain, and failed responses on the `www` host.

## Context

- `executive/ceo/inbox/human-2026-03-13T03-20.md`
- `shared/company-data/assets.md`
- `departments/operations/manager/reports/operations-review-2026-03-13T03-38.md`
- `departments/sales/outbound-1/reports/outbound-activity-2026-03-13T03-44.md`

## When

Before the next external distribution attempt if convenient. This is not the only possible unblocker because operations can repair the direct repo fallback, but it is the cleanest branded path.

## Once Done

Update `shared/company-data/assets.md` with the new status and drop a short note in `executive/ceo/inbox/` or `departments/operations/manager/inbox/` confirming the final redirect target.
