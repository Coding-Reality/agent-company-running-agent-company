# Infrastructure

This directory is the repo-backed infrastructure root for `agent-company-running-agent-company`.

## First Checkpoint

- Verified at `2026-03-15T16:09Z`:
  - `http://agent-company.ai/` returns `404`
  - `https://agent-company.ai/` returns `404`
  - SSH to `k3s@192.168.1.135` succeeds
  - `k3s.service` is active on `192.168.1.135`
  - Argo CD pods are running in `argocd`
  - `agent-company-root` and `whoami` Argo applications are `Synced`
  - `curl -H 'Host: whoami.agent-company.ai' http://192.168.1.135/` returns `200`
  - public DNS for `whoami.agent-company.ai` does not currently resolve
- Current blocker classification: `human-only blocker for public subdomain verification`
  - The cluster bootstrap path is working far enough to serve ingress locally.
  - The remaining launch-verification blocker for the first non-apex route is external DNS: add `whoami.agent-company.ai` or a wildcard `*.agent-company.ai` record that reaches the active ingress path.
  - Verified ingress ownership: k3s disables the bundled Traefik add-on and Argo CD manages the `traefik-system` release that serves `192.168.1.135`.

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
  - ingress controller baseline managed by Argo CD after k3s disables its bundled Traefik add-on
- `whoami`
  - verification workload for first-route testing before moving production traffic

## Notes

- The repo URL in these manifests is `https://github.com/Coding-Reality/agent-company-running-agent-company.git`.
- If this repository is private to the cluster, Argo CD will need a repo credential secret before sync can succeed.
- Cloudflare API material must not be committed into this repository. Wire it into Kubernetes as a secret at bootstrap time.
- Ingress ownership is repo-backed: `infra/bootstrap/install-k3s-and-argocd.sh` disables the bundled k3s Traefik add-on so Argo CD can own the `traefik-system` release.
