# Context Specification

Maintained by: `departments/engineering/ai-engineer`

This document defines the strict context-loading rules every role must follow. It is the authoritative reference for what agents read, in what order, and why.

---

## Context-Loading Tiers

Every role follows a tiered read pattern. Higher tiers are read first. Agents MUST NOT skip tiers or read out of order.

### Tier 1 — Identity (always read first)
- Own `AGENTS.md` — role definition, scope, rules, read list, output contracts

### Tier 2 — Continuity
- Own `memory/current-focus.md` — what was I focused on? What did the last run decide?

### Tier 3 — Upstream Direction
- Immediate manager's `outbox/` (newest 1-2 files) — what am I being asked to do?
- Human inputs in own `inbox/` (files with `source: human` frontmatter take priority)

### Tier 4 — Strategic Context (role-appropriate subset)
- Board/Executive: `shared/vision/`, `shared/dashboards/`
- Managers: `shared/vision/strategy.md`, CEO outbox
- Workers: manager outbox only (not company-wide strategy)

### Tier 5 — Peer and Downstream Signals
- Reports from peer or downstream roles relevant to current decision
- Only read when current-focus or upstream directives indicate a need

### Tier 6 — Historical (read only when needed)
- Older reports, archived decisions, past run-history
- Only access when Tiers 1-5 leave an unanswered question

---

## Discovery Before Reading

Before opening any file, agents should use discovery commands:
```
ls -t inbox/ outbox/ reports/ memory/     # see what's newest
rg --files <path> | head -20              # discover files in a subtree
find <path> -maxdepth 2 -type f | sort    # structured discovery
wc -l <file>                              # gauge file size before reading
```

**Rule:** Never `cat` an entire directory of files. Discover, sort by recency, read newest 1-3.

---

## Output Contracts

Every role's AGENTS.md must specify:
1. **What files it produces** — exact filenames with `{{datetime}}` placeholder
2. **Where it writes them** — `reports/`, `outbox/`, or `memory/`
3. **Who reads them** — which downstream role(s) depend on this output

If an outbox file has no documented reader, it's a dead handoff — flag and fix.

---

## Handoff Integrity Rules

1. If Role A writes to `outbox/`, Role B's AGENTS.md must list Role A's outbox in its "Read Before Every Run" section.
2. Outbox file naming must be predictable so downstream roles can `ls -t` and find the newest directive.
3. A role must never assume context from a file it doesn't list in its read section.

---

## Per-Tier Context Budgets (Guidelines)

These are soft limits. The goal is to keep total context under control so agents have room to reason.

| Role Tier | Target Files Read | Max Files Read |
|-----------|------------------|----------------|
| Board     | 5-8              | 12             |
| Executive | 8-12             | 18             |
| Manager   | 6-10             | 15             |
| Worker    | 4-7              | 10             |

"Files read" means files whose content is loaded into the agent's context window. Discovery commands (`ls`, `find`, `rg --files`) don't count.

---

## Anti-Patterns

- **Reading everything "just in case"** — violates minimum viable context. Read what you need, nothing more.
- **Stale memory** — `current-focus.md` not updated after runs means the next run starts blind.
- **Orphaned outbox** — writing directives nobody reads. Every outbox file must have a documented consumer.
- **Skipping discovery** — opening files without checking timestamps or even knowing what exists.
- **Re-reading COMPANY.md every run** — board and executive tiers only. Workers get company context through their manager.
- **Circular reads** — Role A reads Role B, Role B reads Role A on the same data. Break the cycle with clear upstream/downstream.
