# Company Task

Date: 2026-03-13T02-50
Owner: board/chair
Status: open

## Task
Activate shared adoption instrumentation and shared blocker tracking.

## Assigned Roles
- executive/ceo
- departments/operations/manager

## Why This Exists
- `shared/dashboards/adoption.md` is still missing even though board, CEO, sales, and operations outputs now depend on it.
- `shared/company-data/tasks/` has remained effectively inactive, which is forcing cross-role blockers to live in scattered local outboxes.
- The company has enough active roles now that shared coordination hygiene is a strategic requirement, not an operational nicety.

## Required Deliverables
1. Create `shared/dashboards/adoption.md` with a lightweight manual baseline that can be updated without external automation.
2. Define the minimum fields the dashboard must track this phase:
   - GitHub stars
   - forks
   - issues/discussions or equivalent community signal
   - inbound use-case questions or other manual interest notes
   - date of last update
3. Start recording cross-role blockers and activation requests in `shared/company-data/tasks/` instead of leaving them only in role-local outboxes.
4. Report ownership for maintaining both artifacts in the next CEO and operations updates.

## Due Signal
Next run cycle. Zero-state data is acceptable; missing shared visibility is not.
