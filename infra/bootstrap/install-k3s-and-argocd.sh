#!/usr/bin/env bash
set -euo pipefail

if [[ "${EUID}" -ne 0 ]]; then
  echo "Run as root on the target host." >&2
  exit 1
fi

export INSTALL_K3S_EXEC="${INSTALL_K3S_EXEC:-server --write-kubeconfig-mode 644}"
curl -sfL https://get.k3s.io | sh -

kubectl get nodes -o wide

kubectl create namespace argocd --dry-run=client -o yaml | kubectl apply -f -
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

cat <<'EOF'

Next:
1. Wait for Argo CD pods:
   kubectl get pods -n argocd
2. Apply the root app from this repository:
   kubectl apply -f infra/argo-cd/apps/agent-company-root.yaml
3. If the repo is private, create the Argo CD repository credential first.

EOF
