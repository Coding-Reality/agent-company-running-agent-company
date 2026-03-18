#!/usr/bin/env bash
# Create GHCR image pull credentials in the agent-company-site namespace.
# Run this on the k3s host so the Deployment can pull from ghcr.io.
#
# Usage:
#   export GHCR_TOKEN="your-github-pat-or-token"
#   export GHCR_USER="your-github-username"
#   bash infra/bootstrap/create-ghcr-secret.sh
#
set -euo pipefail

if [[ -z "${GHCR_TOKEN:-}" ]] || [[ -z "${GHCR_USER:-}" ]]; then
  echo "Error: GHCR_TOKEN and GHCR_USER environment variables must be set." >&2
  echo "Usage: GHCR_TOKEN=<token> GHCR_USER=<user> bash $0" >&2
  exit 1
fi

kubectl create namespace agent-company-site --dry-run=client -o yaml | kubectl apply -f -

kubectl create secret docker-registry ghcr-creds \
  --namespace agent-company-site \
  --docker-server=ghcr.io \
  --docker-username="${GHCR_USER}" \
  --docker-password="${GHCR_TOKEN}" \
  --dry-run=client -o yaml | kubectl apply -f -

echo "Secret 'ghcr-creds' created/updated in agent-company-site namespace."
