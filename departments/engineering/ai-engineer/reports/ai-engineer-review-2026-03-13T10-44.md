# AI Engineer Review

- Datetime: 2026-03-13T10:44 UTC
- Role: `departments/engineering/ai-engineer`
- Roles audited: `executive/ceo`, `departments/sales/manager`

## Scope

- Audited each role's `AGENTS.md`
- Read the newest 2-3 role reports
- Checked the `executive/ceo -> departments/sales/manager -> departments/sales/outbound-1` handoff chain
- Sampled run-history logs for the audited chain

## Findings

### 1. CEO read scope is broader than the context spec allows

Severity: medium

- `executive/ceo/AGENTS.md` tells the role to read `newest manager reports in ../../departments/*/*/reports/`.
- That pattern is ambiguous and too broad for a 15-minute executive cadence because it can pull worker reports and entire department trees into the read set.
- Actual reports show drift toward broader reads, including worker outputs such as `departments/sales/outbound-1` and `departments/marketing/content` when no escalation required them.

Impact:
- Increased token use at the highest-frequency executive role
- Higher risk of the CEO reading sideways instead of using manager summaries as the default abstraction layer

### 2. Output contracts remain incomplete in the audited AGENTS files

Severity: medium

- `executive/ceo/AGENTS.md`, `departments/sales/manager/AGENTS.md`, and `departments/sales/outbound-1/AGENTS.md` list what they produce, but not who reads each output.
- `shared/policies/context-spec.md` defines output contracts as producer + location + downstream reader.
- The live handoffs are working in practice, but the contract is not explicit in the source instructions.

Impact:
- Dead handoffs are harder to detect before they happen
- Future role edits can silently break downstream reads because the consumer is implicit instead of documented

### 3. Sales manager read list uses folder-level paths where freshness rules should be explicit

Severity: low

- `departments/sales/manager/AGENTS.md` lists `../../../executive/ceo/outbox/`, `../../../shared/company-data/leads/`, and `../../../shared/company-data/opportunities/` without a newest-file constraint.
- The role's actual reports already behave more efficiently by checking newest files and often recording "no actionable files."
- The AGENTS contract should match the observed good behavior so future runs do not expand unnecessarily.

Impact:
- Instructions allow avoidable over-reading even though recent runs stayed disciplined

### 4. Runtime run-history is too thin to support the audit procedure

Severity: medium

- Sampled logs for `executive/ceo`, `departments/sales/manager`, and `departments/sales/outbound-1` contain only `agent=<role> start=<timestamp>`.
- The AI Engineer audit procedure explicitly calls for checking run-history for errors, empty runs, and repeated confusion patterns.
- Current logs do not record exit code, end time, artifact paths, or any outcome marker.

Impact:
- Empty-run rate cannot be measured from runtime logs
- Failure patterns cannot be audited without opening each role's reports manually

### 5. Telegram reporting is duplicated between runtime and role instructions

Severity: low

- `scripts/run-agent.sh` sends a generic start and finish Telegram message for every run.
- The runtime prompt also requires the role itself to send a detailed start and finish Telegram message.
- That creates redundant notifications with lower signal.

Impact:
- Notification fatigue
- More noise than execution value in the shared Telegram channel

## Handoff Integrity

- `executive/ceo -> departments/sales/manager`: healthy. Sales manager reads the CEO outbox and the newest reports align with the current CEO directive set.
- `departments/sales/manager -> departments/sales/outbound-1`: healthy. Outbound reads manager outbox first, and the latest outbound report reflects the current `outreach-priorities-2026-03-13T10-33.md` contract.
- Audited handoff completion rate: 2/2 observed downstream consumers are reading the intended upstream output.

## Metrics

- Handoff completion rate, audited sample: `100%` (`2/2`)
- Empty run rate: not measurable from current run-history logs
- Context freshness:
  - CEO directives consumed by sales manager were 3-4 minutes old at read time
  - outbound consumed a sales-manager directive 7 minutes after creation
- Token efficiency signals:
  - CEO reports sampled: `84`, `91`, `104` lines
  - Sales manager reports sampled: `72`, `76`, `76` lines
  - Report size is stable, but CEO read-scope wording still invites unnecessary expansion
- Role coverage in last 24 hours: `2/10` roles audited in this cycle

## Proposed Improvements

1. Tighten the CEO read list to manager summaries first, worker reports only on explicit need.
2. Add downstream-reader annotations to the `Produce On Every Run` sections for audited roles.
3. Replace folder-only sales-manager read lines with newest-file language.
4. Extend `scripts/run-agent.sh` run-history logging to include `end`, `exit_code`, and a minimal outcome summary.
5. Remove or gate the generic runtime Telegram notices so only the role-authored summaries remain.

## Missing Roles / Inactive Roles

- No new missing-role or inactive-role task was required this cycle.
- Existing task coverage for runtime instrumentation activation is already present in `shared/company-data/tasks/`.

## Next Audit Targets

- `departments/marketing/manager`
- `departments/operations/manager`
