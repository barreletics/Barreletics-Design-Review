#!/usr/bin/env bash
# Read-only Admin GraphQL for barreletics cloud agents. Requires dashboard secrets:
#   SHOPIFY_STORE=barreletics.myshopify.com
#   SHOPIFY_ADMIN_ACCESS_TOKEN=shpat_...
set -euo pipefail

if [[ -z "${SHOPIFY_STORE:-}" || -z "${SHOPIFY_ADMIN_ACCESS_TOKEN:-}" ]]; then
  echo "Missing SHOPIFY_STORE or SHOPIFY_ADMIN_ACCESS_TOKEN (set in Cloud environment secrets)." >&2
  exit 1
fi

QUERY="${1:-}"
if [[ -z "$QUERY" ]]; then
  echo "Usage: shopify-admin-gql.sh '<graphql query>'" >&2
  exit 1
fi

export SHOPIFY_API_VERSION="${SHOPIFY_API_VERSION:-2025-10}"

python3 - "$QUERY" <<'PY'
import json, os, sys, urllib.request

query = sys.argv[1]
store = os.environ["SHOPIFY_STORE"]
token = os.environ["SHOPIFY_ADMIN_ACCESS_TOKEN"]
version = os.environ["SHOPIFY_API_VERSION"]
url = f"https://{store}/admin/api/{version}/graphql.json"
body = json.dumps({"query": query}).encode()
req = urllib.request.Request(
    url,
    data=body,
    headers={
        "Content-Type": "application/json",
        "X-Shopify-Access-Token": token,
    },
    method="POST",
)
with urllib.request.urlopen(req, timeout=60) as resp:
    print(resp.read().decode())
PY
