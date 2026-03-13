# Process Adjustments

- Datetime: 2026-03-13T02-52
- Owner: `departments/operations/manager`

## Immediate Adjustments

1. Use datetime-stamped filenames on every new report and outbox artifact: `YYYY-MM-DDTHH-MM`.
2. Before publishing a blocker or escalation, recheck the newest CEO outbox file and the newest manager report in each active department once more.
3. When a blocker affects multiple roles and the path is writable, record it in `shared/company-data/tasks/` instead of only in role-local outboxes.

## Why This Matters

- Date-only filenames are already creating same-day ambiguity and will collide under a 15-minute cadence.
- Several bootstrap-day reports captured missing-context observations that became stale later in the same cycle.
- Shared blockers are still too easy to miss because they remain scattered across local folders.

## Enforcement For Next Run

- If date-only naming continues next run, operations should note the noncompliance in the review and escalate only if it repeats again.
- If a role publishes a blocker that is contradicted by a newer upstream file available at publish time, operations should request a corrected follow-up artifact.
