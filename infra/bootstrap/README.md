# k3s Bootstrap

This bootstrap path is the first repo-backed install path for the launch lane.

## Target Host

- SSH target: `k3s@192.168.1.135`
- Verified reachable at `2026-03-15T15:53Z`
- Current observed state:
  - `k3s.service`: absent
  - `k3s-agent.service`: absent
  - `kubectl`: absent or not usable from the current account

## Intended Sequence

1. Run `infra/bootstrap/install-k3s-and-argocd.sh` on the target Ubuntu host.
2. Verify `kubectl get nodes` succeeds.
3. Verify Argo CD pods are healthy in `argocd`.
4. Apply the root app at `infra/argo-cd/apps/agent-company-root.yaml`.
5. Let Argo CD reconcile `traefik` and `whoami`.
6. Verify `whoami.agent-company.ai` or a temporary host before routing the apex domain.

## Required Secrets

- Argo CD repo access secret if the GitHub repository is not public
- Cloudflare DNS token secret if DNS-01 ACME is used with Traefik

## Explicit Unknowns

- Whether the current Cloudflare proxy path already points directly at this host or at an intermediate redirector
- Whether the target host should terminate traffic directly or sit behind another edge service
- Whether the repo is public enough for unauthenticated Argo CD sync
