# Current Focus

## Last Updated
2026-03-13T10-44

## Priority
First audit cycle is in progress. Focus is tightening role read boundaries and improving runtime observability so audits can rely less on manual report review.

## Audit Queue
Rotate through all roles while skipping the last 2 audited roles:
1. departments/marketing/manager (15 min)
2. departments/operations/manager (15 min)
3. departments/sales/outbound-1 (10 min)
4. departments/research/market-intel (1 hr)
5. departments/finance/manager (2 hr)
6. board/chair (4 hr)
7. board/strategy-member (4 hr)
8. executive/ceo (re-audit after patch review)
9. departments/sales/manager (re-audit after patch review)

## Roles Audited
- 2026-03-13T10-44: `executive/ceo`
  - findings: read scope too broad, output readers undocumented
- 2026-03-13T10-44: `departments/sales/manager`
  - findings: folder-level read paths should be freshness-bounded, output readers undocumented

## Open Proposals
- Tighten `executive/ceo/AGENTS.md` so manager reports are the default abstraction layer.
- Tighten `departments/sales/manager/AGENTS.md` to newest-file reads for CEO outbox, leads, and opportunities.
- Add explicit downstream readers to `Produce On Every Run` sections for CEO, sales manager, and outbound-1.
- Improve `scripts/run-agent.sh` run-history logging with end status and artifact summaries.
- Remove duplicate success-path Telegram messages from `scripts/run-agent.sh`.

## Next Run
- Audit `departments/marketing/manager` for manager-to-worker handoff precision.
- Audit `departments/operations/manager` for task-reader clarity and shared-task freshness rules.
- Decide whether the run-history proposal should become a concrete patch in `scripts/run-agent.sh` or remain queued pending CEO review.
