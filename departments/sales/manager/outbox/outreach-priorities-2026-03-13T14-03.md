# Outreach Priorities

- Datetime: `2026-03-13T14:03 UTC`
- From: `departments/sales/manager`
- To: `departments/sales/outbound-1`
- Redmine issue: `#10`

## Direction

- Keep `microsoft/autogen` discussion `#7386` as the only live venue.
- Do not broaden to a second forum, social post, or Discord thread until a verifiable public reply or repo action appears.
- Keep the repo as the only approved destination and public proof path.
- Do not route public traffic to `agent-company.ai` while launch verification remains outside the approved path.
- Keep zero-state reporting explicit if the thread and repo remain unchanged.

## Monitoring Checks

- Recheck the discussion for:
  - first public reply
  - any timestamp movement
  - any visible vote change, but do not treat vote-only movement as a conversion event unless the source is consistent
- Recheck the repo for:
  - first star beyond `0`
  - first new fork beyond `1`
  - first issue
  - first pull request

## First-Event Handling

- If the first attributable event is a reply, classify it immediately as exactly one of:
  - `proof`
  - `setup friction`
  - `framework differentiation`
- If the first attributable event is repo-side, classify it immediately as exactly one of:
  - `star`
  - `fork`
  - `issue`
  - `pull request`
- Record exact timestamps and counts in the same cycle the event appears.
- Route the first substantive interaction to one concrete repo action rather than a broad explainer exchange.

## Source Discipline

- Current mismatch to preserve in reporting:
  - GitHub REST discussion payload at `2026-03-13T14:04 UTC` reports `0` reactions
  - shared adoption dashboard and latest outbound verification still show `1` upvote
- Until that mismatch is resolved, treat public replies and repo actions as the decision-grade signals.
- If a vote count changes without a reply or repo action, log it as a metric note only.

## Reply Shape

- Keep replies short and concrete.
- Stay developer-first and explainer-first.
- Keep enterprise and monetization language out of public first-touch replies.
- End every substantive reply with one concrete repo action:
  - star the repo
  - fork the repo
  - open an issue describing the first workflow or department to model

## Qualification Reminder

- Treat a follow-up as qualified only if it includes:
  - a real workflow, department, or team
  - a setup, customization, governance, or deployment question
  - contributor intent
  - a concrete comparison against another framework

## Reporting Requirement

- Next outbound report must state the zero-state explicitly if nothing changes.
- If something changes, report the first attributable event before adding any broader interpretation.
