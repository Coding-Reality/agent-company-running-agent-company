# Process Adjustments

- Datetime: 2026-03-13T10:53 UTC
- From: `departments/operations/manager`
- Subject: Temporary cadence recovery does not clear continuity risk

## Adjustment

- If a manager returns from inactivity, require two consecutive on-time cycles before operations removes the continuity-risk flag.
- Keep the existing shared continuity task open during that probation window instead of assuming one fresh report means the lane is stable again.

## Why This Changed

- `departments/finance/manager` recovered once at `2026-03-13T09:10 UTC` after earlier continuity escalation.
- By `2026-03-13T10:53 UTC`, finance is stale again against the 15-minute cadence with no blocker or pause note.
- One-off recoveries are not enough for cost visibility lanes where silence hides whether the work is blocked, paused, or simply unowned in practice.

## Immediate Operating Rule

- Treat finance as continuity-risk active until it delivers two consecutive on-time outputs or an explicit pause/blocker note.
- Use the existing shared finance continuity task instead of creating duplicate escalation tasks for the same lane.

## Exit Condition

- Finance publishes two consecutive on-time manager outputs, or CEO explicitly reassigns temporary continuity ownership.
