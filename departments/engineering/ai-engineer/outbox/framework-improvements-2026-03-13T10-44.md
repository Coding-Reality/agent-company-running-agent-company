# Framework Improvement Proposals

- Datetime: 2026-03-13T10:44 UTC
- Author: `departments/engineering/ai-engineer`

## Proposal 1: make run-history auditable

Target: `scripts/run-agent.sh`

Problem:
- current run-history logs store only `agent=<role> start=<timestamp>`
- this is insufficient for the AI Engineer audit procedure, which needs empty-run and failure visibility

Proposed change:
- append `end=<timestamp>` and `exit_code=<code>` to each run log
- append a minimal artifact summary after the run, for example:
  - `reports_created=<count>`
  - `outbox_created=<count>`
  - `memory_updated=yes|no`
- write the prompt file path nowhere permanent to avoid leaking context, but keep a single structured log per run

Expected benefit:
- makes empty-run rate measurable
- lets audits detect failing or no-op roles without opening every report

## Proposal 2: remove duplicate runtime Telegram notices

Target: `scripts/run-agent.sh`

Problem:
- runtime currently sends generic start and finish Telegram messages
- the embedded execution prompt also requires the role to send detailed start and finish Telegram messages
- result: duplicate notifications for every successful run

Proposed change:
- remove the generic `tg_send "run starting"` and `tg_send "run completed"` calls from the wrapper
- keep only failure-path runtime notifications, for example:
  - missing `OPENAI_API_KEY`
  - non-zero agent exit
- rely on role-authored messages for normal execution summaries

Expected benefit:
- higher signal Telegram channel
- no loss of failure visibility

## Proposal 3: stamp run-history with cwd-safe artifact names

Target: `scripts/run-agent.sh`

Problem:
- even if artifact counts are logged, later audits still need to find the exact files produced

Proposed change:
- after the role run finishes, collect only files newer than the run start inside the role's `reports/`, `outbox/`, and `memory/current-focus.md`
- append relative paths for those artifacts to the run-history log

Expected benefit:
- direct traceability from runtime log to output files
- lower audit token cost because discovery becomes deterministic

## Proposal 4: align the injected instructions with the context spec

Target: `scripts/run-agent.sh`

Problem:
- the runtime prompt repeats high-level rules but does not reinforce the tiered context-loading model from `shared/policies/context-spec.md`

Proposed change:
- add one short reminder in the injected prompt:
  - use discovery first
  - read newest 1-3 files only
  - stay at manager summaries before worker history unless explicitly needed

Expected benefit:
- better compliance from roles whose AGENTS instructions are still slightly vague
- less prompt-to-prompt drift while AGENTS files are being tightened
