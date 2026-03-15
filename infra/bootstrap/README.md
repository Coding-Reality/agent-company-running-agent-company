# k3s Bootstrap

This bootstrap path is the first repo-backed install path for the launch lane.

## Target Host

- SSH target: `k3s@192.168.1.135`
- Verified reachable at `2026-03-15T16:09Z`
- Current observed state:
  - `k3s.service`: active
  - `kubectl`: usable with `sudo`
  - `argocd` namespace and control-plane pods: running
  - `whoami` namespace and ingress: running
  - public DNS for `whoami.agent-company.ai`: unresolved

## Intended Sequence

1. Run `infra/bootstrap/install-k3s-and-argocd.sh` on the target Ubuntu host.
2. Verify `kubectl get nodes` succeeds.
3. Verify Argo CD pods are healthy in `argocd`.
4. Apply the root app at `infra/argo-cd/apps/agent-company-root.yaml`.
5. Let Argo CD reconcile `traefik` and `whoami`.
6. Verify `kubectl get svc -n traefik-system traefik` shows `192.168.1.135` as the external IP.
7. Verify `whoami.agent-company.ai` or a temporary host before routing the apex domain.

## Required Secrets

- Argo CD repo access secret if the GitHub repository is not public
- Cloudflare DNS token secret if DNS-01 ACME is used later for certificate automation

## Explicit Unknowns

- Whether the current Cloudflare proxy path already points directly at this host or at an intermediate redirector
- Whether the target host should terminate traffic directly or sit behind another edge service
- Whether the repo is public enough for unauthenticated Argo CD sync

## Verified Bootstrap Notes

- `k3s` must disable the bundled Traefik add-on so ingress ownership stays repo-backed under `infra/argo-cd/apps/traefik.yaml`.
- Argo CD install must use server-side apply against `https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml`; client-side apply hit the `applicationsets.argoproj.io` annotation-size limit during the live bootstrap on `2026-03-15`.

## Verified Checkpoint

- `agent-company.ai` resolves publicly and returns `404` on both HTTP and HTTPS as of `2026-03-15T16:08Z`.
- `whoami.agent-company.ai` does not currently resolve in public DNS.
- `curl -H 'Host: whoami.agent-company.ai' http://192.168.1.135/` returns `200`, which verifies the cluster ingress path locally.
- The host now disables the bundled k3s Traefik add-on so the Argo-managed Traefik service owns ingress on `192.168.1.135`.
