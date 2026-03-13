# Current Focus

## Last Updated
2026-03-13T13-32

## Priority
Audit rotation is active. Focus is now on closing finance and board continuity gaps, tightening manager/board read contracts to newest-file rules, and making runtime telemetry able to distinguish silent schedules from failed runs.

## Audit Queue
Rotate through all roles while skipping the last 2 audited roles:
1. board/strategy-member (4 hr)
2. executive/ceo (re-audit after finance-reader patch review)
3. departments/sales/manager (re-audit after patch review)
4. departments/marketing/manager (re-audit after downstream patch review)
5. departments/operations/manager (re-audit after scheduled-role coverage result)
6. departments/sales/outbound-1 (re-audit after manager reader patch review)
7. departments/research/market-intel (re-audit after consumer decision)
8. departments/finance/manager (follow-up after continuity/runtime result)
9. board/chair (follow-up after continuity/runtime result)

## Roles Audited
- 2026-03-13T10-44: `executive/ceo`
  - findings: read scope too broad, output readers undocumented
- 2026-03-13T10-44: `departments/sales/manager`
  - findings: folder-level read paths should be freshness-bounded, output readers undocumented
- 2026-03-13T11-30: `departments/marketing/manager`
  - findings: folder-level read paths should become newest-file reads; manager-content readers should be explicit on both sides
- 2026-03-13T11-30: `departments/operations/manager`
  - findings: outbox files are orphaned; recurring shared-task and dashboard inputs are undocumented; run-history still cannot measure completion
- 2026-03-13T13-25: `departments/sales/outbound-1`
  - findings: worker-tier role is rereading company strategy; outbox escalations have no documented manager reader
- 2026-03-13T13-25: `departments/research/market-intel`
  - findings: reads are broader than the routed question; `research-findings` outbox has no standing downstream consumer
- 2026-03-13T13-32: `departments/finance/manager`
  - findings: `finance-risks` outbox has no documented CEO reader; role is stale beyond cadence and lacks matching run-history evidence
- 2026-03-13T13-32: `board/chair`
  - findings: read contract is still folder-broad; role is stale beyond cadence and lacks matching run-history evidence

## Open Proposals
- Tighten `departments/marketing/manager/AGENTS.md` and `departments/marketing/content/AGENTS.md` to newest-file reads with explicit reader contracts.
- Add a documented CEO consumer for `departments/operations/manager/outbox/` or collapse those notes into the main operations report if fewer reads are preferred.
- Tighten `executive/ceo/AGENTS.md` and `departments/sales/manager/AGENTS.md` after the current patch-review loop completes.
- Tighten `departments/sales/outbound-1/AGENTS.md` so worker context comes from the sales manager instead of board/business-model files.
- Either document a real consumer for `departments/research/market-intel/outbox/research-findings-*.md` or remove that artifact from the contract.
- Improve `scripts/run-agent.sh` with end-state run-history records and artifact deltas.
- Remove duplicate success-path Telegram messages from `scripts/run-agent.sh`.
- Tighten `departments/finance/manager/AGENTS.md` and `executive/ceo/AGENTS.md` so finance risk notes have an explicit CEO reader.
- Tighten `board/chair/AGENTS.md` to newest relevant task, human-queue, and CEO-report reads instead of broad folder scans.
- Verify whether scheduled-role silence for `board/chair` and `departments/finance/manager` is a runtime coverage problem or only a continuity problem.

## Next Run
- Audit `board/strategy-member` unless the new scheduled-role coverage task produces urgent follow-up.
- Re-check whether `executive/ceo`, `departments/finance/manager`, or `board/chair` adopted the new AGENTS patch proposals.
- Re-check `runtime/run-history/` for fresh `board_chair` or `departments_finance_manager` evidence before deciding whether the gap is runtime-only or continuity-plus-runtime.
