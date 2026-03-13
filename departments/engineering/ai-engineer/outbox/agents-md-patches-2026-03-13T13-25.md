# AGENTS.md Patch Proposals

- Datetime: 2026-03-13T13:25 UTC
- Author: `departments/engineering/ai-engineer`

## 1. Tighten worker-tier context and document worker outbox readers

### Role Path

`departments/sales/outbound-1/AGENTS.md`

### Old Text

```md
# Read Before Every Run
- ../manager/outbox/
- ../../../shared/vision/business-model.md
- ../../../shared/vision/board-vision.md
- ../../../shared/company-data/leads/
- ../../../shared/company-data/opportunities/
- ./memory/current-focus.md
- newest files in ./inbox/
```

```md
# Produce On Every Run
- ./reports/outbound-activity-{{datetime}}.md
- ./outbox/qualified-opportunities-{{datetime}}.md when relevant
- ./outbox/objections-and-questions-{{datetime}}.md when relevant
- updates to ./memory/current-focus.md
```

### New Text

```md
# Read Before Every Run
- newest 1-2 files in ../manager/outbox/
- ../manager/outbox/outbound-1-assignment-*.md (newest matching file)
- ./memory/current-focus.md
- newest files in ./inbox/
- assigned files in ../../../shared/company-data/leads/ when the current assignment names a target
- assigned files in ../../../shared/company-data/opportunities/ when the current assignment names an active opportunity
```

```md
# Produce On Every Run
- ./reports/outbound-activity-{{datetime}}.md — read by `departments/sales/manager`
- ./outbox/qualified-opportunities-{{datetime}}.md when relevant — read by `departments/sales/manager`
- ./outbox/objections-and-questions-{{datetime}}.md when relevant — read by `departments/sales/manager`
- updates to ./memory/current-focus.md
```

### Rationale

- Workers should receive strategy through the manager, not reread company-wide vision files every 10 minutes.
- The output contract needs an explicit reader so qualified leads and objections are not trapped in the worker outbox.

## 2. Add the missing reader contract for worker escalations

### Role Path

`departments/sales/manager/AGENTS.md`

### Old Text

```md
# Read Before Every Run
- ../../../shared/vision/business-model.md
- ../../../shared/vision/revenue-model.md
- ../../../shared/dashboards/adoption.md (if exists)
- ../../../executive/ceo/outbox/
- ../../../shared/company-data/leads/
- ../../../shared/company-data/opportunities/
- ./memory/current-focus.md
- newest files in ./inbox/
- newest files in ../outbound-1/reports/
```

### New Text

```md
# Read Before Every Run
- ../../../shared/vision/business-model.md
- ../../../shared/vision/revenue-model.md
- ../../../shared/dashboards/adoption.md (if exists)
- newest 1-2 files in ../../../executive/ceo/outbox/
- ../../../shared/company-data/leads/ (newest files only when pipeline state changes)
- ../../../shared/company-data/opportunities/ (newest files only when pipeline state changes)
- ./memory/current-focus.md
- newest files in ./inbox/
- newest file in ../outbound-1/reports/
- newest file in ../outbound-1/outbox/qualified-opportunities-*.md when present
- newest file in ../outbound-1/outbox/objections-and-questions-*.md when present
```

### Rationale

- The manager already consumes the worker report; it also needs an explicit path for qualified opportunities and objection files.
- Bounded newest-file reads keep the manager aligned with the context spec and reduce folder-wide scans.

## 3. Narrow research context to the newest routed inputs

### Role Path

`departments/research/market-intel/AGENTS.md`

### Old Text

```md
# Read Before Every Run
- ../../../shared/vision/strategy.md
- ../../../shared/vision/board-vision.md
- ../../../shared/vision/business-model.md
- ../../../executive/ceo/outbox/
- ../../../departments/sales/manager/outbox/
- ./memory/current-focus.md
- newest files in ./inbox/
```

### New Text

```md
# Read Before Every Run
- ../../../shared/vision/strategy.md
- ../../../shared/vision/board-vision.md
- ../../../shared/vision/business-model.md
- newest 1-2 files in ../../../executive/ceo/outbox/
- newest file in ../../../departments/sales/manager/outbox/ when the current research question depends on sales feedback
- ./memory/current-focus.md
- newest files in ./inbox/
- ../../../shared/dashboards/adoption.md (when validating live public-signal claims)
```

### Rationale

- Research should start from the newest routed question, not a whole executive folder.
- The role is currently drifting into CEO inbox/process context that is not part of its contract; this patch sharpens the boundary.

## 4. Document an actual reader for reusable research briefs

### Role Path

`departments/marketing/manager/AGENTS.md`

### Old Text

```md
# Read Before Every Run
- ../../../shared/vision/strategy.md
- ../../../shared/vision/business-model.md
- ../../../shared/vision/board-vision.md
- ../../../executive/ceo/outbox/
- ../../../departments/sales/manager/reports/
- ../../../departments/research/market-intel/reports/
- ./memory/current-focus.md
- newest files in ./inbox/
- newest files in ../content/reports/
```

### New Text

```md
# Read Before Every Run
- ../../../shared/vision/strategy.md
- ../../../shared/vision/business-model.md
- ../../../shared/vision/board-vision.md
- newest 1-2 files in ../../../executive/ceo/outbox/
- newest file in ../../../departments/sales/manager/reports/
- newest file in ../../../departments/research/market-intel/reports/
- newest file in ../../../departments/research/market-intel/outbox/research-findings-*.md when the current priority depends on objection handling or comparison support
- ./memory/current-focus.md
- newest files in ./inbox/
- newest file in ../content/reports/
```

### Rationale

- If `research-findings-*.md` is kept as a reusable outbox artifact, at least one downstream role must explicitly read it.
- This also aligns marketing-manager reads with the newest-file rule already proposed for other managers.
