# Context Specification

Maintained by: `departments/engineering/ai-engineer`

This document defines the strict context-loading rules every role must follow. It is the authoritative reference for what agents read, in what order, and why.

---

## Context-Loading Tiers

Every role follows a tiered read pattern. Higher tiers are read first.

### Tier 1 — Identity
- Own `AGENTS.md`

### Tier 2 — Redmine Doctrine And Work Queue
- Redmine wiki page `Company`
- Redmine issues relevant to the role's assigned work, blockers, and recent updates

### Tier 3 — Shared Repo Sources
- `shared/vision/`, `shared/dashboards/`, `shared/company-data/`, and policy files that are still authoritative in the repository

### Tier 4 — Legacy Filesystem Context
- Role-local `inbox/`, `outbox/`, `reports/`, and `memory/` files only when migration or historical context requires them

### Tier 5 — Historical
- Older run artifacts and archived decisions only when Tiers 1-4 leave an unanswered question

---

## Discovery Before Reading

Before opening any repository file, agents should use discovery commands:
```
rg --files <path> | head -20              # discover files in a subtree
find <path> -maxdepth 2 -type f | sort    # structured discovery
wc -l <file>                              # gauge file size before reading
```

**Rule:** Never `cat` an entire directory of files. Discover, sort by recency, read newest 1-3.

---

## Output Contracts

Every role's AGENTS.md must specify:
1. **What Redmine updates it produces** — issue updates, comments, new issues, or wiki edits
2. **What repository-local artifacts still exist** — only if shared docs or migration records are still required
3. **Who consumes them** — which role or human depends on this output
4. **Whether high-cadence execution is logged in Redmine notes** — recurring monitoring loops should not default to new role-local reports or memory files

If an outbox file has no documented reader, it's a dead handoff — flag and fix.

---

## Handoff Integrity Rules

1. If Role A creates or updates a Redmine issue for Role B, Role B's AGENTS.md must make that Redmine surface explicit in its read section.
2. Repository-local artifacts should not be used as hidden handoff channels.
3. A role must never assume context from a source it doesn't list in its read section.
4. If a manager hands work to a worker, the handoff surface should be a Redmine issue or issue note unless a shared repo artifact is explicitly authoritative.

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
- **Stale Redmine state** — issue status, ownership, or blockers not updated after a run.
- **Hidden filesystem handoffs** — writing new role-local directives or reports that nobody is expected to read.
- **Recurring zero-state report loops** — high-frequency roles creating repetitive local reports when a Redmine note would preserve the same signal with lower token cost.
- **Skipping discovery** — opening repo files without checking whether Redmine or a shared source already has the answer.
- **Recreating company doctrine in repo markdown** — the authoritative company doctrine lives on the Redmine wiki page `Company`.
- **Circular reads** — Role A reads Role B, Role B reads Role A on the same data. Break the cycle with clear upstream/downstream.
