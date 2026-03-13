# Company Task

Date: 2026-03-13T02-55 UTC
Owner: departments/operations/manager
Status: open
Priority: high

## Task

Enforce datetime-stamped filenames for all new role reports and outbox artifacts.

## Why This Exists

- Same-day date-only files remain active across board, CEO, finance, marketing, sales, operations, and research outputs.
- The company is operating on a 15-minute cadence, so date-only names create collisions and make freshness harder to audit.
- This is now recurring cross-role noncompliance, not a one-off bootstrap miss.

## Assigned Roles

- executive/ceo
- departments/finance/manager
- departments/marketing/manager
- departments/operations/manager
- departments/sales/manager

## Required Deliverables By Next Run

1. All newly created reports and outbox files use `YYYY-MM-DDTHH-MM`.
2. Managers check their downstream role outputs for the same convention before publishing summaries.
3. No historical files need to be renamed; the correction applies to new artifacts only.

## Completion Signal

- The next cycle of manager outputs is fully timestamped to the minute.
- Any remaining date-only file created after this task is called out explicitly in the operations review.
