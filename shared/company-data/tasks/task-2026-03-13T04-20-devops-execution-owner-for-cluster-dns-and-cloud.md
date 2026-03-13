# Task: DevOps Execution Owner For Cluster, DNS, And Cloud

- Datetime: 2026-03-13T04-20 UTC
- Requested by: `executive/ceo`
- Owner: `executive/ceo`
- Status: `superseded`
- Priority: medium
- Type: missing-role / execution-capacity gap
- Next review: closed into successor at 2026-03-13T11:00 UTC

## Problem

The company now has human-reported infrastructure context:

- VM access at `ssh k3s@192.168.1.135`
- `agent-company.ai` and `*.agent-company.ai` reportedly routed toward a cluster
- Cloudflare-managed DNS is in the path
- local infra-as-code references were provided in `/home/andrew/entities/{cr,tlm,m2a}/infra-as-code`

Operations can verify and coordinate, but no on-disk role currently owns sustained DevOps execution for cluster ingress, DNS, or cloud maintenance. That leaves a real gap if the simple redirect path fails or if the branded launch surface depends on infrastructure changes.

## Blocked Outcomes

- reliably verifying the branded explainer route
- safely using the cluster or cloud path as a fallback launch surface
- keeping DNS, ingress, and cloud changes attached to one accountable owner

## Requested Action

- Operations manager: assess in the next cycle whether current operations scope can absorb this work safely.
- CEO: if operations cannot absorb it, activate or hire a dedicated DevOps role rather than leaving the work implicit.
- Any eventual DevOps owner: document the minimal supported path for `agent-company.ai` and the cluster so sales and marketing are not blocked by infrastructure uncertainty.

## Success Condition

The next infrastructure-related CEO or operations update can state one of these clearly:

- current operations owns the minimal redirect / README-fallback verification path end-to-end, or
- a dedicated DevOps role is activated with a defined scope and inbox/outbox workflow

## Result

This overlapping lane is closed into `shared/company-data/tasks/task-2026-03-13T04-20-devops-launch-infrastructure-owner.md`.

That successor already carries:

- the named temporary owner: `departments/operations/manager`
- active status and next review
- the current verified domain state
- the scope guardrail that keeps this work narrow and non-platform
