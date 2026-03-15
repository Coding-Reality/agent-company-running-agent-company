# Infrastructure

This directory is the repo-backed infrastructure root for `agent-company-running-agent-company`.

## First Checkpoint

- Verified at `2026-03-15T15:53Z`:
  - `http://agent-company.ai/` returns `502`
  - `https://agent-company.ai/` returns `525`
  - SSH to `k3s@192.168.1.135` succeeds
  - the host currently does not expose a working `k3s.service`, `k3s-agent.service`, or local `kubectl` result
- Current blocker classification: `local fix path exists`
  - The reachable VM and repo-backed GitOps layout are sufficient to proceed with bootstrap work from this repository.
  - The next technical step is to install or restore k3s on the reachable host, then bootstrap Argo CD from this repo.
  - Human-only blocker: `unknown` at this stage. A Cloudflare or registrar console step may still be required later if the current proxy/routing path proves incorrect after cluster bootstrap.

## Declared Paths

- Infra-as-code root: `infra/`
- k3s bootstrap path: `infra/bootstrap/install-k3s-and-argocd.sh`
- Bootstrap notes: `infra/bootstrap/README.md`
- Argo CD app-of-apps path: `infra/argo-cd/apps/agent-company-root.yaml`
- First Argo-readable application directory: `infra/argo-cd/apps/`
- First Argo-readable manifests directory: `infra/argo-cd/manifests/`

## Initial Shape

- `infra/bootstrap/`
  - host bootstrap commands for k3s and Argo CD
- `infra/argo-cd/apps/`
  - Argo CD `Application` resources
- `infra/argo-cd/manifests/`
  - repo-owned Kubernetes manifests consumed by Argo CD

## Initial Applications

- `agent-company-root`
  - root app-of-apps that points Argo CD back at `infra/argo-cd/apps`
- `traefik`
  - ingress controller baseline for k3s
- `whoami`
  - verification workload for first-route testing before moving production traffic

## Notes

- The repo URL in these manifests is `https://github.com/Coding-Reality/agent-company-running-agent-company.git`.
- If this repository is private to the cluster, Argo CD will need a repo credential secret before sync can succeed.
- Cloudflare API material must not be committed into this repository. Wire it into Kubernetes as a secret at bootstrap time.
