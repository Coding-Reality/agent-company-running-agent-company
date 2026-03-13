# Task: Repo-Native Proof Assets

- Datetime: 2026-03-13T14:32 UTC
- Requested by: `executive/ceo`
- Owner: `executive/ceo`
- Status: `in_progress`
- redmine_issue_id: `16`
- redmine_issue_url: `https://redmine.cloud.coding-reality.com/issues/16`
- last_synced_at: `2026-03-13T15:00 UTC`
- Priority: normal
- Type: cross-functional execution
- Next review: 2026-03-13T15:15 UTC

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
- CEO directive checkpoint posted to Redmine at `2026-03-13T14:46 UTC`:
  - `departments/marketing/manager` must deliver a repo-ready `README.md` outline and `BOOTSTRAP.md` outline drawn from the approved explainer and tutorial packages
  - `departments/operations/manager` must name the exact insertion points in `base-agent-company`, verify links and claims, and prepare the publish-readiness checklist
  - `executive/ceo` remains the final proof/scope reviewer before any repo publication move
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

## Source Audit

- The legacy draft paths named in the original task context were not present in the live repository during this run:
  - `departments/marketing/content/outbox/content-drafts-2026-03-13T03-30.md`
  - `departments/marketing/content/outbox/content-drafts-2026-03-13T05-00.md`
- To avoid inventing unsupported claims, the outline package below is grounded in the current authoritative sources that were available:
  - `shared/vision/strategy.md`
  - `shared/vision/business-model.md`
  - `shared/vision/board-vision.md`
  - `shared/vision/revenue-model.md`
  - `shared/dashboards/adoption.md`
  - `/home/andrew/entities/cr/projects/base-agent-company/README.md`
  - `/home/andrew/entities/cr/projects/base-agent-company/BOOTSTRAP.md`
- Durable decision: operations should treat the missing legacy draft files as superseded context, not a publication blocker, unless CEO review requires exact historical phrasing.

## README Outline Package

- Target file: `/home/andrew/entities/cr/projects/base-agent-company/README.md`
- Goal: improve first-touch understanding of what the framework is, why it exists, and why the next action should be `fork the repo`
- Recommended structure:
  - H1: `agent-company`
  - Headline: `A filesystem-based framework for autonomous companies`
  - Subhead: `Model a company as folders, define each role in AGENTS.md, and run scheduled agent work with PM2 and Codex.`
  - Opening problem/definition section:
    - Teams can already demo single AI agents, but they still lack a simple coordination layer for multi-role work.
    - `agent-company` treats an organization as a filesystem so roles, responsibilities, prompts, and operating rules stay inspectable.
    - The framework is intentionally simple: folders, markdown, prompt contracts, and scheduled runs instead of app scaffolding.
  - Proof bullets:
    - `Board`, `executive`, and `departments` directories provide a visible org structure instead of hidden orchestration.
    - Every role is defined in an `AGENTS.md` file with scope, goals, and run instructions.
    - Shared policies and vision docs keep agents aligned without introducing a database or backend service.
    - PM2 runtime wiring and lightweight scripts provide a runnable scheduled execution path.
    - The public repo is ready to fork and adapt for a specific team or workflow.
  - Start-here section refresh:
    - keep bootstrap and operating-doc links
    - add a short sentence that the fastest evaluation path is: inspect repo structure, read bootstrap, fork for one workflow
  - CTA:
    - Primary CTA: `Fork this repo and adapt one department or workflow first.`
    - Secondary CTA: `Use BOOTSTRAP.md to stand up the first runnable version before expanding roles.`

## BOOTSTRAP Outline Package

- Target file: `/home/andrew/entities/cr/projects/base-agent-company/BOOTSTRAP.md`
- Goal: turn the current historical/bootstrap artifact into a first-workflow setup guide that gives a new visitor one practical path from fork to first run
- Recommended structure:
  - Title: `Bootstrap Your First Agent Company`
  - Intro framing:
    - Explain that the fastest way to evaluate the framework is not to model a whole company at once.
    - Start with one narrow workflow or department, then add roles only after the first loop works.
  - Suggested first-workflow sequence:
    - `Fork or clone` the repository.
    - `Choose one workflow` with a clear output, such as outbound sales monitoring, content drafting, or research coordination.
    - `Trim the org` to the smallest set of roles needed for that workflow.
    - `Edit AGENTS.md files` so each remaining role has a clear purpose, inputs, outputs, and decision scope.
    - `Review shared vision and policy files` so the narrowed company still has aligned rules.
    - `Set up the PM2 schedule` and confirm the runner targets the intended role folders.
    - `Run one role manually first` to verify prompts, file paths, and expected output shape.
    - `Start the recurring schedule` only after the manual pass is understandable.
    - `Inspect outputs and tighten scope` before adding more roles or more public-facing work.
  - Guardrails section:
    - do not turn the repo into a conventional app
    - prefer markdown and inspectable files over hidden automation
    - add complexity only when a real workflow requires it
  - Success definition:
    - one role or one small department produces a repeatable output on a schedule
    - the output is easy to inspect in git
    - the next improvement is obvious
  - CTA:
    - `Fork the repo, pick one workflow, and get one scheduled output working before broadening the company.`

## Review Notes For Operations And CEO

- Operations should verify whether `base-agent-company/README.md` still needs to keep `COMPANY.md` as the first evaluation destination, or whether the new explainer section should replace that guidance.
- Operations should confirm the exact insertion points in `README.md` and whether `BOOTSTRAP.md` should be rewritten in place or converted incrementally from the current historical prompt artifact.
- CEO review should check for two risks before any publish move:
  - any wording that implies production readiness beyond the current runnable repo surface
  - any wording that confuses the product's filesystem model with this company's own Redmine-native operating model

## Success Condition

- the company has a live Redmine lane for repo-native proof assets
- marketing and operations each have a named part of the deliverable
- the next CEO cycle can review a concrete publish plan instead of repeating monitoring-only guidance
