#!/usr/bin/env bash
# Create the Cloudflare API token secret in the traefik-system namespace.
# Run this on the k3s host BEFORE Traefik can issue certificates.
#
# Usage:
#   export CF_DNS_API_TOKEN="your-cloudflare-api-token-here"
#   bash infra/bootstrap/create-cloudflare-secret.sh
#
set -euo pipefail

if [[ -z "${CF_DNS_API_TOKEN:-}" ]]; then
  echo "Error: CF_DNS_API_TOKEN environment variable is not set." >&2
  echo "Usage: CF_DNS_API_TOKEN=<token> bash $0" >&2
  exit 1
fi

kubectl create namespace traefik-system --dry-run=client -o yaml | kubectl apply -f -

kubectl create secret generic cloudflare-api-token \
  --namespace traefik-system \
  --from-literal=api-token="${CF_DNS_API_TOKEN}" \
  --dry-run=client -o yaml | kubectl apply -f -

echo "Secret 'cloudflare-api-token' created/updated in traefik-system namespace."
