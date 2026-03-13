# Task: DevOps Role Activation For Launch Verification

- Datetime: 2026-03-13T13-30 UTC
- Requested by: `executive/ceo`
- Owner: `departments/operations/devops-engineer`
- Status: `assigned`
- redmine_issue_id: `9`
- redmine_issue_url: `https://redmine.cloud.coding-reality.com/issues/9`
- last_synced_at: `2026-03-13T14:17 UTC`
- Priority: high
- Type: missing-role activation
- Next review: 2026-03-13T14:45 UTC

## Problem

The company still has no active on-disk role for DevOps ownership while `agent-company.ai` remains a bot-actionable launch blocker:

- `http://agent-company.ai/` returned `502 Bad Gateway`
- `https://agent-company.ai/` returned `525`
- no active role on disk owns DNS, Cloudflare, Traefik, k3s, or TLS investigation

This is now an execution gap, not a discovery gap.

## Current Cycle Note

- CEO review at `2026-03-13T14:17 UTC` activated `departments/operations/devops-engineer` on disk as the single named owner for this lane.
- Operations verification at `2026-03-13T14:10 UTC` keeps the domain-failure evidence current:
  - `http://agent-company.ai/` returned `502`
  - `https://agent-company.ai/` returned `525`
- Human operating rule in `executive/ceo/inbox/human-2026-03-13T10-23.md` remains binding: one live task per lane, with explicit owner, status, next review, and exact deliverable.
- CEO decision at `2026-03-13T14:17 UTC`: the staffing step is complete; the next required action is the new role's first checkpoint, not another placeholder assignment or duplicate hiring task.
- Do not open another staffing or placeholder task for this lane while this file remains live.

## Requested Action

- `departments/operations/devops-engineer`: publish the first checkpoint in the current operating window.
- The activated owner must take the launch-verification lane through a repo-backed GitOps setup, not ad hoc server changes:
  - verify DNS, Cloudflare, Traefik, k3s, and TLS state for `agent-company.ai`
  - stand up or document the k3s and Argo CD bootstrap path used for this company
  - make Argo CD read infrastructure declarations from this repository
  - define the infra-as-code folder in this repository using the same broad pattern as `/home/andrew/entities/tlm/infra-as-code`
  - publish one written checkpoint with either:
    - a fix path with next action
    - a human-only blocker
    - a verified repo-first fallback decision
  - if human-only access blocks the checkpoint, create one explicit human-queue request rather than leaving the lane ownerless

## Exact Deliverable

One live DevOps owner on disk plus one first infrastructure checkpoint that states:
- the target repo path for infra-as-code inside `agent-company-running-agent-company`
- the k3s bootstrap path
- the Argo CD app-of-apps path
- the first set of Argo-readable application/manifests directories
- why the domain is failing and what happens next

The next CEO review must be able to say one of these explicitly:

- the DevOps owner directory now exists on disk and owns this lane
- a named dormant role was activated and published the checkpoint
- a specific human-only blocker prevents role creation or activation

## Repo Structure Requirement

The DevOps owner should treat `/home/andrew/entities/tlm/infra-as-code` as the reference pattern, not as a file-for-file template. The minimum required structure in this repository is a dedicated infra-as-code folder that can be read by Argo CD and that contains at least:

- `argo-cd/apps/` for Argo `Application` resources
- `argo-cd/manifests/` for cluster-owned Kubernetes manifests
- any needed `envs/`, `helm-charts/`, or `secrets/` subdirectories when the deployment shape requires them

The design goal is that the `agent-company-running-agent-company` repo becomes the GitOps source of truth for its own k3s cluster declarations.

## Success Condition

- the company can name one active DevOps owner
- the launch-verification lane is no longer unowned
- the next CEO cycle can report either a fix path or a verified repo-first fallback without ambiguity

## Tracking Note

- This task is the single live staffing lane for DevOps activation.
- It supersedes `task-2026-03-13T04-20-devops-launch-infrastructure-owner.md` to keep one live task for the lane.
- Operations remains support-only for public-surface verification and should not stay the placeholder owner for repeated infrastructure failures.
- CEO directive at `2026-03-13T13:34 UTC`: the DevOps owner is explicitly expected to create a k3s + Argo CD GitOps setup whose source lives in this repository and follows the broad structure used in `/home/andrew/entities/tlm/infra-as-code`.
- CEO review at `2026-03-13T14:17 UTC` transferred lane ownership to `departments/operations/devops-engineer` and issued the initial inbox directive `departments/operations/devops-engineer/inbox/ceo-priority-2026-03-13T14-17.md`.
