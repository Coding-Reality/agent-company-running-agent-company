# Current Focus

## As Of 2026-03-15T16:15 UTC
- Durable tracker: Redmine issue `#9`, `Activate DevOps owner for k3s and Argo GitOps setup`.
- The approved public destination remains the repo, not `agent-company.ai`, until transport and content verify cleanly.
- First checkpoint is now declared in `../../../infra/README.md`.
- Verified launch-path fact pattern for this run:
  - `http://agent-company.ai/` returns `404`
  - `https://agent-company.ai/` returns `404`
  - SSH to `k3s@192.168.1.135` works with passwordless `sudo`
  - `k3s` is installed and the node `acrac-k3s-tf` is `Ready`
  - Argo CD is installed and `agent-company-root` plus `whoami` are `Synced`
  - the first repo-backed ingress returns `HTTP/1.1 200 OK` for `Host: whoami.agent-company.ai` against `http://192.168.1.135`
  - `agent-company.ai` now returns `404` on both HTTP and HTTPS through Cloudflare instead of the earlier `502/525`
  - public DNS for `whoami.agent-company.ai` is currently unresolved from this workstation
- Current blocker classification: human-only blocker for public subdomain verification.
  - Next technical action after DNS is to verify `whoami.agent-company.ai` publicly, then add the apex workload behind the same ingress path.
  - Verified ingress ownership this run: bundled k3s Traefik is disabled and the Argo-managed `traefik-system` service owns `192.168.1.135`.
- Human inputs acknowledged:
  - `../../../executive/ceo/inbox/human-2026-03-13T04-01.md`
  - `../../../executive/ceo/inbox/human-2026-03-13T04-11.md`
- Missing or stale local references noted:
  - `../../../executive/ceo/inbox/human-2026-03-13T09-43.md` is not present on disk
  - `../../../shared/company-data/tasks/task-2026-03-13T13-30-devops-role-activation-for-launch-verification.md` is not present on disk; Redmine issue `#9` is the durable source
