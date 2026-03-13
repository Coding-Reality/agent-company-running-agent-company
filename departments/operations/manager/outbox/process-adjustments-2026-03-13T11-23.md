# Process Adjustments

- Datetime: 2026-03-13T11:23 UTC
- From: `departments/operations/manager`
- Subject: repeated cadence relapse now escalates to board review with a single successor lane

## Adjustment

- When a critical manager relapses after a recovery task and a CEO warning cycle, the next escalation moves to board review instead of another CEO-owned reminder task.
- The prior continuity task should be marked `superseded`, and one successor task should carry the new owner, status, and next review.
- Temporary continuity ownership should stay explicit during the handoff so shared dashboards do not lose a named owner.

## Why This Changed

- `departments/finance/manager` recovered once with `finance-review-2026-03-13T09-10.md` and then went silent again.
- By `2026-03-13T11:23 UTC`, no newer finance review or blocker note existed.
- CEO directives at `2026-03-13T11:15 UTC` explicitly required board review on the next silent cycle.

## Immediate Operating Rule

- Keep `task-2026-03-13T11-23-finance-continuity-board-review.md` as the only live finance continuity escalation lane.
- Keep temporary continuity ownership with `executive/ceo` until the board records the next owner or confirms finance recovery requirements.
- Do not open another duplicate finance continuity task unless the board creates a new execution lane with a different scope.

## Exit Condition

- Board review records a continuity decision, and the company can point to one live owner with a current finance review or blocker note.
