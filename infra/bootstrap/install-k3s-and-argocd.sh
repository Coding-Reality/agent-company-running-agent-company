#!/usr/bin/env bash
set -euo pipefail

if [[ "${EUID}" -ne 0 ]]; then
  echo "Run as root on the target host." >&2
  exit 1
fi

mkdir -p /etc/rancher/k3s

# Keep ingress ownership repo-backed under Argo CD.
if [[ ! -f /etc/rancher/k3s/config.yaml ]]; then
  cat >/etc/rancher/k3s/config.yaml <<'EOF'
disable:
  - traefik
EOF
fi

export INSTALL_K3S_EXEC="${INSTALL_K3S_EXEC:-server --write-kubeconfig-mode 644 --disable traefik}"
curl -sfL https://get.k3s.io | sh -

kubectl get nodes -o wide

kubectl create namespace argocd --dry-run=client -o yaml | kubectl apply -f -
kubectl apply --server-side --force-conflicts -n argocd \
  -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

cat <<'EOF'

Next:
1. Wait for Argo CD pods:
   kubectl get pods -n argocd
2. Apply the root app from this repository:
   kubectl apply -f infra/argo-cd/apps/agent-company-root.yaml
3. Verify the Argo-managed Traefik service is serving ingress:
   kubectl get svc -n traefik-system traefik
4. If the repo is private, create the Argo CD repository credential first.

EOF
