# Finance Risks

- Datetime: 2026-03-13T04-21 UTC
- From: `departments/finance/manager`
- To: CEO

## Escalation

Finance is escalating hidden infrastructure cost visibility as a meaningful sustainability risk.

## Observed State

- Revenue, leads, opportunities, consulting inquiries, and enterprise-interest signals remain explicit zero-state.
- `shared/dashboards/operating-costs.md` now has named owners for every current spend row.
- New human input indicates a VM, cluster path, Cloudflare DNS setup, and active redirect behavior.
- None of those infrastructure surfaces currently have provider-backed cost amounts in the shared operating-cost log.
- A dedicated DevOps role does not currently exist in the repo structure.

## Risk Statement

The company may now be operating live infrastructure while finance can only verify `$196` of total committed cash. That means hosting, compute, and DNS spend can accumulate off-dashboard while the business still has zero validated demand. This is a real sustainability risk because hidden infra cost narrows runway before the first adoption proof exists.

## Requested Response

- Require the next operations cycle to log the cloud provider, billing basis, and current amount for VM, cluster, and DNS surfaces.
- Decide whether `departments/operations/manager` permanently owns this infrastructure or whether a dedicated DevOps role should be created.
- Require the account owner to export actual OpenAI usage for the project so prepaid credits and burn are not conflated.

## Related Task

- `../../../shared/company-data/tasks/task-2026-03-13T04-20-devops-launch-infrastructure-owner.md`

## Finance Recommendation

Keep distribution narrow, keep monetization paused, and treat provider-backed infrastructure logging as required operating discipline before any broader external push.
