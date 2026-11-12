#!/usr/bin/env bash
# Parse sealed artifact bytes (copy) with logged SHA256 before/after Ruby Liquid parse.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SRC="${1:-$ROOT/snippets/cart-bundle-promo-config.liquid}"
ARTIFACT="${TMPDIR:-/tmp}/cart-bundle-promo-config-artifact.liquid"
EXPECTED_HASH="${2:-}"

cp "$SRC" "$ARTIFACT"
HASH_BEFORE=$(sha256sum "$ARTIFACT" | awk '{print $1}')
echo "liquid_sealed_hash_before=$HASH_BEFORE path=$ARTIFACT"

ruby "$ROOT/scripts/validate-snippet-liquid.rb" "$ARTIFACT"
HASH_AFTER=$(sha256sum "$ARTIFACT" | awk '{print $1}')
echo "liquid_sealed_hash_after=$HASH_AFTER"

if [[ "$HASH_BEFORE" != "$HASH_AFTER" ]]; then
  echo "liquid_sealed_hash_mismatch" >&2
  exit 1
fi

if [[ -n "$EXPECTED_HASH" && "$HASH_BEFORE" != "$EXPECTED_HASH" ]]; then
  echo "liquid_sealed_expected_hash_mismatch expected=$EXPECTED_HASH actual=$HASH_BEFORE" >&2
  exit 1
fi

echo "liquid_sealed_parse_ok path=$ARTIFACT sha256=$HASH_BEFORE"
