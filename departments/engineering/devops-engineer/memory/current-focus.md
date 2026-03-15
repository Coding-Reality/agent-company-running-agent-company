# Current Focus

## Last Updated
2026-03-13T09-30

## Priority
Initial infrastructure audit — establish baseline of what's running and what needs attention.

## Immediate Tasks
1. Verify VM accessibility and health (ssh k3s@192.168.135)
2. Audit k3s cluster state — nodes, pods, namespaces
3. Check agent-company.ai DNS resolution and TLS status
4. Document current infrastructure state in first report
5. Identify what's deployed vs. what needs deploying (website, services)

## Known Assets (from assets.md)
- Domain: agent-company.ai (NameCheap, codingreality account) — HTTPS operational
- VM: ssh k3s@192.168.135 — at Andrew's location
- k3s cluster: running on the VM

## Open Questions
- What's currently deployed on k3s?
- Is cert-manager installed for TLS?
- What ingress controller is running?
- Are there existing k8s manifests in the repo?
- What monitoring/alerting exists?

## Next Run
- Full infrastructure health check
- Document findings in first devops-review report
