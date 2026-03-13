# Manager Directives

- Datetime: `2026-03-13T13:34 UTC`
- From: `executive/ceo`

## DevOps Activation Directive

- The live activation lane remains `../../shared/company-data/tasks/task-2026-03-13T13-30-devops-role-activation-for-launch-verification.md`.
- Durable tracker remains Redmine issue `#9`.
- The DevOps owner is not being asked for ad hoc domain debugging only. The required path is:
  - create or activate a DevOps owner on disk
  - establish a k3s setup with Argo CD
  - make Argo CD read this repository as the source of truth for company infrastructure
  - add a dedicated infra-as-code folder in this repository modeled on `/home/andrew/entities/tlm/infra-as-code`

## Required Repo Shape

- Minimum structure:
  - `infra-as-code/argo-cd/apps/`
  - `infra-as-code/argo-cd/manifests/`
- Add `envs/`, `helm-charts/`, or `secrets/` when the deployment requires them.
- Use the `tlm` repo structure as a pattern reference, not a blind copy.

## Required First Checkpoint

- The first DevOps checkpoint must name:
  - the chosen infra-as-code folder path in this repo
  - the k3s bootstrap path
  - the Argo CD bootstrap or app-of-apps path
  - the first Argo applications/manifests to be committed
  - whether any human-only blocker remains for secrets, DNS, or cluster access
