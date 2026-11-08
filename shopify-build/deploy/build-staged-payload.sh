#!/usr/bin/env bash
# Builds minimal staged payload from fresh baseline + merged tree. No Shopify writes.
set -euo pipefail
BASELINE="${CART_BASELINE_ROOT:-/tmp/fresh-draft}"
MERGED="${CART_MERGED_ROOT:-/tmp/merge-out}"
OUT="${1:-/opt/cursor/artifacts/cart-bundles-deployment-payload}"
ROOT="$OUT/payload"

ALLOWLIST=(
  assets/cart.js
  assets/cart-bundle-promo.js
  assets/cart-bundle-promo.css
  snippets/cart-bundle-promo-config.liquid
  layout/theme.liquid
  sections/main-cart.liquid
  config/settings_schema.json
)

rm -rf "$OUT"
mkdir -p "$ROOT" "$OUT/deploy"

for rel in "${ALLOWLIST[@]}"; do
  mkdir -p "$ROOT/$(dirname "$rel")"
  cp "$MERGED/$rel" "$ROOT/$rel"
done

cp /workspace/shopify-build/deploy/PUSH-ONLY.txt "$OUT/"
cp /workspace/shopify-build/deploy/HOLD.txt "$OUT/"
cp /workspace/shopify-build/deploy/pants-product-resolution.json "$OUT/deploy/"
cp /workspace/shopify-build/deploy/settings_data.draft-keys.json "$OUT/deploy/" 2>/dev/null || true

BASELINE="$BASELINE" MERGED="$MERGED" OUT="$OUT" ALLOWLIST_JSON="$(printf '%s\n' "${ALLOWLIST[@]}" | node -e "const fs=require('fs');process.stdout.write(JSON.stringify(fs.readFileSync(0,'utf8').trim().split(/\n/).filter(Boolean)))")" node <<'NODE'
const fs = require('fs');
const crypto = require('crypto');
const path = require('path');
const baseline = process.env.BASELINE;
const merged = process.env.MERGED;
const out = process.env.OUT;
const allowlist = JSON.parse(process.env.ALLOWLIST_JSON);

function sha(p) {
  return crypto.createHash('sha256').update(fs.readFileSync(p)).digest('hex');
}

const files = allowlist.map((rel) => {
  const beforePath = path.join(baseline, rel);
  const afterPath = path.join(merged, rel);
  const entry = { path: rel, sha256_after: sha(afterPath) };
  if (fs.existsSync(beforePath)) {
    entry.sha256_before = sha(beforePath);
    entry.status = 'modified';
  } else {
    entry.status = 'added';
  }
  return entry;
});

const manifest = {
  generatedAt: new Date().toISOString(),
  baselineRoot: baseline,
  mergedRoot: merged,
  theme: 'Nov08 Cart + bundles (draft only — parent push)',
  allowlist,
  files,
  checkoutSafety: {
    staticRegressionTests: 'shopify-build: npm run test:cart-all',
    proven: [
      'cart-drawer footer byte-identical to fresh baseline',
      'main-cart summary aside byte-identical to fresh baseline',
      'no estimated-total footer IDs in merged cart files',
      'cart.js has no checkout link listeners'
    ],
    notProven: [
      'Live draft theme render after shopify theme push',
      'Desktop/mobile drawer QA before checkout (parent)',
      'SAVE2/2FOR15 at checkout with real discounts',
      'Pants AJAX add on production CDN/product.js'
    ]
  }
};

fs.writeFileSync(path.join(out, 'MANIFEST.json'), JSON.stringify(manifest, null, 2) + '\n');

const tarPath = path.join(path.dirname(out), 'cart-bundles-deployment-payload.tar.gz');
const { execSync } = require('child_process');
execSync(`tar -czf "${tarPath}" -C "${path.dirname(out)}" "${path.basename(out)}"`, {
  stdio: 'inherit'
});
console.log('Wrote', path.join(out, 'MANIFEST.json'));
console.log('Wrote', tarPath);
NODE
