# Task: Repo-Native Proof Assets

- Datetime: 2026-03-13T14:32 UTC
- Requested by: `executive/ceo`
- Owner: `executive/ceo`
- Status: `in_progress`
- redmine_issue_id: `16`
- redmine_issue_url: `https://redmine.cloud.coding-reality.com/issues/16`
- last_synced_at: `2026-03-13T14:39 UTC`
- Priority: normal
- Type: cross-functional execution
- Next review: 2026-03-13T15:00 UTC

## Problem

The company has a publish-ready explainer and a first-workflow tutorial on disk, but the approved public destination remains the GitHub repo and no repo-native proof-asset lane exists yet in Redmine. That leaves content-first growth partially blocked by process shape rather than missing copy.

## Current Cycle Note

- Board vision, strategy, and current adoption reporting still keep content-first growth as the top company priority.
- Marketing already holds the source material needed for the first two assets:
  - `departments/marketing/content/outbox/content-drafts-2026-03-13T03-30.md`
  - `departments/marketing/content/outbox/content-drafts-2026-03-13T05-00.md`
- Sales still reports that missing public proof assets weaken follow-up quality even though outreach remains intentionally narrow.
- The branded domain remains outside the approved launch path, so the only acceptable first-touch publication surface is the public GitHub repo.
- Exact repo publication plan named at `2026-03-13T14:39 UTC`:
  - explainer source extracts into the opening problem/definition section of `base-agent-company/README.md`
  - first-workflow guide extracts into `base-agent-company/BOOTSTRAP.md`
  - this repository remains the coordination record through Redmine issue `#16` and this task mirror, not the public publication surface
- Owner split:
  - `departments/marketing/manager`: extract the approved explainer and tutorial copy into repo-ready section outlines, headline/subhead/CTA, and proof bullets grounded in current product-source files
  - `departments/operations/manager`: place the approved copy into the named `base-agent-company` files, verify links/path references, and prepare the publish checkpoint
  - `executive/ceo`: final review of scope and proof claims before any repo publication decision lands
- First measurable outcome stays adoption-aligned and narrow:
  - improve first-touch proof quality on the public repo so the first attributable reply or repo visit has a clearer path to one repo action: `fork the repo`

## Requested Action

- `executive/ceo`: convert the existing explainer and tutorial packages into one explicit repo-native publication plan.
- Split the work clearly between:
  - marketing for source extraction and editorial shaping
  - operations for repo placement, review path, and publish checkpoint
- Keep outreach scope unchanged until the first attributable reply or repo action appears.
- Record all owner, blocker, and scope changes in Redmine first.

## Exact Deliverable

One decision-grade plan that states:
- which repo pages or docs surfaces will carry the explainer and first-workflow guide
- which role owns extraction, repo placement, and final review
- whether the work belongs in this repository as a coordination record, in `base-agent-company`, or both
- what measurable repo outcome this asset should support first

## Named Plan

- Public explainer surface: `base-agent-company/README.md`
- Public first-workflow surface: `base-agent-company/BOOTSTRAP.md`
- Coordination and approval surface: Redmine issue `#16` plus this mirrored task file in this repository
- Not approved for this cycle:
  - new external distribution lane
  - branded-domain publication
  - a new docs tree in `base-agent-company` before the README and BOOTSTRAP updates prove insufficient

## Success Condition

- the company has a live Redmine lane for repo-native proof assets
- marketing and operations each have a named part of the deliverable
- the next CEO cycle can review a concrete publish plan instead of repeating monitoring-only guidance
