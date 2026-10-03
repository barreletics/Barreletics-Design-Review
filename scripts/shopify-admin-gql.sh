#!/usr/bin/env bash
# Read-only Admin GraphQL. Shopify no longer shows a copyable shpat_ token.
# Use Dev Dashboard Client ID + secret (client_credentials grant).
# Secrets: SHOPIFY_STORE, SHOPIFY_CLIENT_ID, SHOPIFY_CLIENT_SECRET
# Optional: SHOPIFY_ADMIN_ACCESS_TOKEN if you still have a legacy shpat_.
set -euo pipefail

if [[ -z "${SHOPIFY_STORE:-}" ]]; then
  echo "Missing SHOPIFY_STORE (barreletics.myshopify.com)." >&2
  exit 1
fi

QUERY="${1:-}"
if [[ -z "$QUERY" ]]; then
  echo "Usage: shopify-admin-gql.sh '<graphql query>'" >&2
  exit 1
fi

if echo "$QUERY" | grep -qiE '\bmutation\b'; then
  echo "Blocked: read-only script (no mutations)." >&2
  exit 2
fi

export SHOPIFY_API_VERSION="${SHOPIFY_API_VERSION:-2025-10}"

python3 - "$QUERY" <<'PY'
import json, os, sys, urllib.parse, urllib.request

query = sys.argv[1]
store = os.environ["SHOPIFY_STORE"].replace("https://", "").rstrip("/")
token = os.environ.get("SHOPIFY_ADMIN_ACCESS_TOKEN", "").strip()
client_id = os.environ.get("SHOPIFY_CLIENT_ID", "").strip()
client_secret = os.environ.get("SHOPIFY_CLIENT_SECRET", "").strip()

if not token:
    if not client_id or not client_secret:
        print("Missing SHOPIFY_CLIENT_ID and SHOPIFY_CLIENT_SECRET (or a legacy SHOPIFY_ADMIN_ACCESS_TOKEN).", file=sys.stderr)
        sys.exit(1)
    body = urllib.parse.urlencode({
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
    }).encode()
    req = urllib.request.Request(
        f"https://{store}/admin/oauth/access_token",
        data=body,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        token = json.loads(resp.read().decode())["access_token"]

version = os.environ["SHOPIFY_API_VERSION"]
gql_body = json.dumps({"query": query}).encode()
req = urllib.request.Request(
    f"https://{store}/admin/api/{version}/graphql.json",
    data=gql_body,
    headers={
        "Content-Type": "application/json",
        "X-Shopify-Access-Token": token,
    },
    method="POST",
)
with urllib.request.urlopen(req, timeout=60) as resp:
    print(resp.read().decode())
PY
