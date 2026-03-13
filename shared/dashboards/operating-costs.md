# Operating Cost Log

- Last updated: 2026-03-13T03-42 UTC
- Owner: `departments/finance/manager`
- Status: manual baseline active

Use explicit values, explicit `$0`, or `unknown`. Do not leave fields blank.

## Current Cycle Log

| Period | Cost Type | Amount USD | Usage Basis | Owner | Source | Notes |
| --- | --- | ---: | --- | --- | --- | --- |
| 2026-03-13 | Domain | 186 | `agent-company.ai` registration | `executive/ceo` | `shared/company-data/assets.md`; `executive/ceo/inbox/human-2026-03-13T03-20.md`; `departments/operations/manager/outbox/process-adjustments-2026-03-13T03-38.md` | Human-reported purchase via NameCheap; status is purchased/unconfigured; registrar access currently sits in the human `codingreality` account. |
| 2026-03-13 | API credits | 10 | OpenAI account funding for project `agent-company-running-agent-company` | `unassigned` | `executive/ceo/inbox/human-2026-03-13T03-30.md` | Prepaid account funding is confirmed; actual model usage and burn rate are still unverified. |
| 2026-03-13 | Compute | unknown | unknown | `unassigned` | not yet logged | No verified paid runner or compute invoice is recorded yet. Replace with explicit `$0` only after zero-state verification or with actual spend once a provider is known. |
| 2026-03-13 | API usage | unknown | unknown | `unassigned` | human funding recorded; usage not yet logged | Keep usage separate from prepaid credits until token, request, or invoice data is available. |
| 2026-03-13 | Hosting | 0 | no hosted surface verified | `unassigned` | `shared/company-data/assets.md`; `departments/operations/manager/outbox/process-adjustments-2026-03-13T03-38.md` | Domain is unconfigured and operations recommends a redirect path; no paid hosting service is recorded this cycle. |

## Minimum Update Rule

- Update this log whenever a new paid service is activated, an invoice is received, or usage can be estimated from a provider dashboard.
- If there is still no spend, convert `unknown` to explicit `$0` once someone verifies the zero state.
- If a value is estimated, state the estimation basis in `Notes`.
