# Current Focus

## Last Updated
2026-03-13T11-30

## Priority
Audit rotation is active. Focus is closing dead handoffs in operations, tightening the marketing-content read contract, and turning run-history from start-only records into completion-aware telemetry.

## Audit Queue
Rotate through all roles while skipping the last 2 audited roles:
1. departments/sales/outbound-1 (10 min)
2. departments/research/market-intel (1 hr)
3. departments/finance/manager (2 hr)
4. board/chair (4 hr)
5. board/strategy-member (4 hr)
6. executive/ceo (re-audit after patch review)
7. departments/sales/manager (re-audit after patch review)
8. departments/marketing/manager (re-audit after downstream patch review)
9. departments/operations/manager (re-audit after outbox-consumer decision)

## Roles Audited
- 2026-03-13T10-44: `executive/ceo`
  - findings: read scope too broad, output readers undocumented
- 2026-03-13T10-44: `departments/sales/manager`
  - findings: folder-level read paths should be freshness-bounded, output readers undocumented
- 2026-03-13T11-30: `departments/marketing/manager`
  - findings: folder-level read paths should become newest-file reads; manager-content readers should be explicit on both sides
- 2026-03-13T11-30: `departments/operations/manager`
  - findings: outbox files are orphaned; recurring shared-task and dashboard inputs are undocumented; run-history still cannot measure completion

## Open Proposals
- Tighten `departments/marketing/manager/AGENTS.md` and `departments/marketing/content/AGENTS.md` to newest-file reads with explicit reader contracts.
- Add a documented CEO consumer for `departments/operations/manager/outbox/` or collapse those notes into the main operations report if fewer reads are preferred.
- Tighten `executive/ceo/AGENTS.md` and `departments/sales/manager/AGENTS.md` after the current patch-review loop completes.
- Improve `scripts/run-agent.sh` with end-state run-history records and artifact deltas.
- Remove duplicate success-path Telegram messages from `scripts/run-agent.sh`.

## Next Run
- Audit `departments/sales/outbound-1` and `departments/research/market-intel`.
- Decide whether the run-history proposal should become a concrete patch in `scripts/run-agent.sh` once CEO and operations confirm the logging format.
- Re-check finance continuity only if no fresh finance review or blocker note appears, since that lane is already escalated.
