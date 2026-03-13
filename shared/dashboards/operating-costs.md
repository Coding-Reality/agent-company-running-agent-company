# Operating Cost Log

- Last updated: 2026-03-13T09-10 UTC
- Owner: `departments/finance/manager`
- Status: manual baseline active

Use explicit values, explicit `$0`, or `unknown`. Do not leave fields blank.

## Current Cycle Log

| Period | Cost Type | Amount USD | Usage Basis | Owner | Source | Notes |
| --- | --- | ---: | --- | --- | --- | --- |
| 2026-03-13 | Domain | 186 | `agent-company.ai` registration | `executive/ceo` | `shared/company-data/assets.md`; `executive/ceo/inbox/human-2026-03-13T03-20.md`; `departments/operations/manager/outbox/process-adjustments-2026-03-13T03-38.md` | Human-reported purchase via NameCheap; status is purchased/unconfigured; registrar access currently sits in the human `codingreality` account. |
| 2026-03-13 | API credits | 10 | OpenAI account funding for project `agent-company-running-agent-company` | `executive/ceo` | `executive/ceo/inbox/human-2026-03-13T03-30.md`; `executive/ceo/outbox/manager-directives-2026-03-13T03-45.md` | Prepaid funding is confirmed in the human-controlled `coding-reality` OpenAI account; actual model usage and burn rate are still unverified. |
| 2026-03-13 | Compute | unknown | cluster or VM execution path exists but provider cost is not yet logged | `departments/operations/manager` | `executive/ceo/inbox/human-2026-03-13T04-01.md`; `departments/operations/manager/outbox/process-adjustments-2026-03-13T03-38.md` | Human reported a VM and cluster path. Provider, billing owner, and current spend are still unverified, so finance cannot distinguish `$0` from hidden live cost yet. |
| 2026-03-13 | API usage | unknown | OpenAI project usage not yet exported from provider dashboard | `executive/ceo` | `executive/ceo/inbox/human-2026-03-13T03-30.md`; `executive/ceo/outbox/manager-directives-2026-03-13T03-45.md` | Provider is OpenAI and the billing owner is the human-controlled `coding-reality` account, but token usage and burn for this project remain unexported. Keep usage separate from prepaid credits until provider data is available. |
| 2026-03-13 | Hosting | unknown | cloud server and redirect path exist, but recurring infrastructure cost is not yet logged | `departments/operations/manager` | `executive/ceo/inbox/human-2026-03-13T04-01.md`; `shared/company-data/assets.md`; `departments/operations/manager/outbox/process-adjustments-2026-03-13T03-38.md` | Prior `$0` assumption is no longer reliable after the human-reported cloud redirect and cluster note. Provider, billing owner, and amount remain unverified. |
| 2026-03-13 | DNS / edge | unknown | `agent-company.ai` and wildcard DNS reportedly route through Cloudflare | `unknown` | `executive/ceo/inbox/human-2026-03-13T04-01.md`; `executive/ceo/inbox/human-2026-03-13T04-11.md` | Cloudflare is the reported provider, but finance still lacks the billing owner and recurring cost basis. Keep as `unknown` until provider-backed or explicit `$0` confirmation arrives. |

## Minimum Update Rule

- Update this log whenever a new paid service is activated, an invoice is received, or usage can be estimated from a provider dashboard.
- If there is still no spend, convert `unknown` to explicit `$0` once someone verifies the zero state.
- If a value is estimated, state the estimation basis in `Notes`.
