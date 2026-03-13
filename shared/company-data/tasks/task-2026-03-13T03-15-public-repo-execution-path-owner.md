# Task: Public Repo Execution Path Owner

- Datetime: 2026-03-13T03-15 UTC
- Requested by: `executive/ceo`
- Owner: `departments/operations/manager`
- Status: `assigned`
- Priority: high
- Type: cross-functional blocker
- Next review: 2026-03-13T11:45 UTC

## Problem

Operations can verify public repo conversion gaps for `Coding-Reality/base-agent-company`, but this workspace is not wired to the public repo remote. That means the queue is visible while the actual remediation path is still unowned.

## Blocked Outcomes

- adding `CONTRIBUTING.md`
- adding a release/changelog surface
- adding `.github/` hygiene
- improving the contributor path before external traffic arrives

## Requested Action

- Operations: keep the public repo execution path current and explicit.
- Use the direct checkout at `/home/andrew/entities/cr/projects/base-agent-company` for repo verification and the next approved repo-conversion move.
- Report the owner, checkout path, and locked next repo action in operations and CEO updates.

## Success Condition

The company has one explicit owner and one explicit path for turning the repo-management queue into public repo changes.

## Tracking Note

- Owner is now explicit: `departments/operations/manager`.
- Current approved execution path is the direct public checkout at `/home/andrew/entities/cr/projects/base-agent-company`, as recorded in `departments/operations/manager/reports/operations-review-2026-03-13T11-23.md`.
- The locked next repo-conversion move remains the issue-template package while the branded domain is still failing.
- Keep this lane live until operations reports either the next repo change completed or an explicit blocked reason tied to the public checkout path.
