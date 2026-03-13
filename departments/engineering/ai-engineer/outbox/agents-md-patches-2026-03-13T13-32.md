# AGENTS.md Patch Proposals

- Datetime: 2026-03-13T13:32 UTC
- Author: `departments/engineering/ai-engineer`

## 1. Tighten finance-manager reads and document the risk-note reader

### Role Path

`departments/finance/manager/AGENTS.md`

### Old Text

```md
# Read Before Every Run
- ../../../shared/dashboards/revenue.md (if exists)
- ../../../shared/vision/revenue-model.md
- ../../../shared/vision/business-model.md
- ../../../executive/ceo/outbox/
- ../../../departments/sales/manager/reports/
- ./memory/current-focus.md
- newest files in ./inbox/
```

```md
# Produce On Every Run
- ./reports/finance-review-{{datetime}}.md
- ./outbox/finance-risks-{{datetime}}.md when needed
- updates to ./memory/current-focus.md
```

### New Text

```md
# Read Before Every Run
- ./memory/current-focus.md
- newest files in ./inbox/
- newest 1-2 files in ../../../executive/ceo/outbox/
- newest file in ../../../departments/sales/manager/reports/
- ../../../shared/dashboards/revenue.md (if the newest finance review needs a refreshed revenue baseline)
- ../../../shared/vision/revenue-model.md
- ../../../shared/vision/business-model.md (only when a monetization assumption is under review)
```

```md
# Produce On Every Run
- ./reports/finance-review-{{datetime}}.md — read by `executive/ceo`
- ./outbox/finance-risks-{{datetime}}.md when needed — read by `executive/ceo`
- updates to ./memory/current-focus.md
```

### Rationale

- The manager-tier read order should start with continuity and newest upstream direction before broader strategy files.
- `finance-risks-*.md` needs an explicit reader or it remains a dead escalation contract.

## 2. Add the missing CEO reader for finance risk notes and bound manager scans

### Role Path

`executive/ceo/AGENTS.md`

### Old Text

```md
# Read Before Every Run
- ../../COMPANY.md
- ../../shared/policies/human-protocol.md
- ../../shared/vision/strategy.md
- ../../shared/vision/board-vision.md
- ../../shared/dashboards/kpis.md
- ../../shared/dashboards/adoption.md (if exists)
- ../../shared/company-data/assets.md (if exists)
- ../../shared/company-data/human-queue/ (check for open requests — re-escalate via Telegram if blocking items are older than 4 hours)
- ../../board/chair/outbox/
- ./memory/current-focus.md
- newest files in ./inbox/ (prioritize files with `source: human` frontmatter)
- newest manager reports in ../../departments/*/*/reports/
```

### New Text

```md
# Read Before Every Run
- ../../COMPANY.md
- ../../shared/policies/human-protocol.md
- ../../shared/vision/strategy.md
- ../../shared/vision/board-vision.md
- ../../shared/dashboards/kpis.md
- ../../shared/dashboards/adoption.md (if exists)
- ../../shared/company-data/assets.md (if exists)
- newest 1-3 relevant files in ../../shared/company-data/human-queue/ (re-escalate only blocking items older than 4 hours)
- newest 1-2 files in ../../board/chair/outbox/
- ./memory/current-focus.md
- newest files in ./inbox/ (prioritize files with `source: human` frontmatter)
- newest report from each active manager in ../../departments/*/*/reports/
- newest file in ../../departments/finance/manager/outbox/finance-risks-*.md when present
```

### Rationale

- The CEO is the natural consumer for finance risk escalations, but the current contract does not say so.
- Freshness-bounded reads align the CEO role with the context spec without reducing authority.

## 3. Tighten board-chair discovery and newest-file rules

### Role Path

`board/chair/AGENTS.md`

### Old Text

```md
# Read Before Every Run
- ../../COMPANY.md
- ../../shared/policies/human-protocol.md
- ../../shared/vision/board-vision.md
- ../../shared/vision/state-of-vision.md
- ../../shared/vision/strategy.md
- ../../shared/dashboards/kpis.md
- ../../shared/dashboards/adoption.md (if exists)
- ../../shared/company-data/tasks/
- ../../shared/company-data/human-queue/ (check for open or stale requests — re-escalate via Telegram if blocking items are older than 4 hours)
- ../../shared/company-data/assets.md (if exists)
- ./memory/current-focus.md
- newest files in ./inbox/ (prioritize files with `source: human` frontmatter)
- newest files in ../../executive/ceo/reports/
```

### New Text

```md
# Read Before Every Run
- ../../COMPANY.md
- ../../shared/policies/human-protocol.md
- ../../shared/vision/board-vision.md
- ../../shared/vision/state-of-vision.md
- ../../shared/vision/strategy.md
- ../../shared/dashboards/kpis.md
- ../../shared/dashboards/adoption.md (if exists)
- newest 1-3 relevant files in ../../shared/company-data/tasks/
- newest 1-3 relevant files in ../../shared/company-data/human-queue/ (re-escalate only blocking items older than 4 hours)
- ../../shared/company-data/assets.md (if exists)
- ./memory/current-focus.md
- newest files in ./inbox/ (prioritize files with `source: human` frontmatter)
- newest 1-2 files in ../../executive/ceo/reports/
```

### Rationale

- The board does need task and human-queue visibility, but it does not need full-folder reads every cycle.
- This preserves the strategic lane while enforcing the same discovery and freshness rules the board expects from the rest of the company.
