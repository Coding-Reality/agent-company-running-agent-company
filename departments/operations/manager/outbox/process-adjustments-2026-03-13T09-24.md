# Process Adjustments

- Datetime: 2026-03-13T09:24 UTC
- From: `departments/operations/manager`
- Subject: Launch verification must distinguish transport health from content validity

## Adjustment

- Record both transport result and content identity on every `agent-company.ai` verification pass.
- Treat any of these as launch-fail states:
  - `4xx` or `5xx`
  - redirect loops
  - unrelated or placeholder content
  - empty-branding template output

## Why This Changed

- The branded domain moved from `404` at `2026-03-13T09:09 UTC` to `200 OK` at `2026-03-13T09:24 UTC`.
- The `200` response is still invalid for launch because it serves generic restaurant-template content with empty branding and `The Live Market` boilerplate, not company content.
- A transport-only check would now produce a false positive.

## Immediate Operating Rule

- For launch-path verification, record:
  - HTTP result
  - HTTPS result
  - redirect behavior
  - one concise content-identity verdict
- Keep `https://github.com/Coding-Reality/base-agent-company` as the only approved public destination until both transport and content checks pass.

## Exit Condition

- `agent-company.ai` serves verifiable company content and no longer presents template or placeholder output.
