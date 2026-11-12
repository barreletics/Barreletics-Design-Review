#!/usr/bin/env bash
# Minimal revision payload vs parent baseline commit (default 52efdab).
set -euo pipefail
BASE_COMMIT="${REV_BASE_COMMIT:-52efdab}"
SRC="${1:-/workspace/shopify-build}"
OUT="${2:-/opt/cursor/artifacts/cart-bundles-crosssell-revision}"
ALLOWLIST=(
  assets/cart-bundle-promo.js
  assets/cart-bundle-promo.css
  snippets/cart-bundle-promo-config.liquid
  config/settings_schema.json
)
rm -rf "$OUT"
mkdir -p "$OUT/payload"
for rel in "${ALLOWLIST[@]}"; do
  mkdir -p "$OUT/payload/$(dirname "$rel")"
  cp "$SRC/$rel" "$OUT/payload/$rel"
done
(
  cd /workspace
  for rel in "${ALLOWLIST[@]}"; do
    git show "${BASE_COMMIT}:shopify-build/${rel}" >"$OUT/baseline-${rel//\//_}" 2>/dev/null || echo "MISSING" >"$OUT/baseline-${rel//\//_}"
    cp "$SRC/$rel" "$OUT/after-${rel//\//_}"
  done
)
REV_BASE_COMMIT="$BASE_COMMIT" SRC="$SRC" OUT="$OUT" ALLOWLIST_JSON="$(printf '%s\n' "${ALLOWLIST[@]}" | node -e "const fs=require('fs');process.stdout.write(JSON.stringify(fs.readFileSync(0,'utf8').trim().split(/\n/).filter(Boolean)))")" node <<'NODE'
const fs = require('fs');
const crypto = require('crypto');
const path = require('path');
const { execSync } = require('child_process');
const base = process.env.REV_BASE_COMMIT;
const src = process.env.SRC;
const out = process.env.OUT;
const allowlist = JSON.parse(process.env.ALLOWLIST_JSON);
function shaBuffer(buf) {
  return crypto.createHash('sha256').update(buf).digest('hex');
}
const files = allowlist.map((rel) => {
  let before = null;
  try {
    before = execSync(`git -C /workspace show ${base}:shopify-build/${rel}`, { encoding: 'buffer' });
  } catch (e) {
    before = null;
  }
  const afterPath = path.join(src, rel);
  const afterBuf = fs.readFileSync(afterPath);
  return {
    path: rel,
    sha256_before: before ? shaBuffer(before) : null,
    sha256_after: shaBuffer(afterBuf),
    status: before ? 'modified' : 'added'
  };
});
const manifest = {
  generatedAt: new Date().toISOString(),
  baselineGitCommit: base,
  allowlist,
  files,
  pushOnly: allowlist.map((p) => `  --only ${p}`)
};
fs.writeFileSync(path.join(out, 'MANIFEST-REVISION.json'), JSON.stringify(manifest, null, 2) + '\n');
fs.writeFileSync(
  path.join(out, 'PUSH-ONLY-REVISION.txt'),
  '# Re-push only changed cross-sell revision files\n' +
    allowlist.map((p) => `shopify theme push ... --only ${p}`).join('\n') +
    '\n'
);
const tar = path.join(path.dirname(out), path.basename(out) + '.tar.gz');
execSync(`tar -czf "${tar}" -C "${path.dirname(out)}" "${path.basename(out)}"`);
console.log('Wrote', path.join(out, 'MANIFEST-REVISION.json'), tar);
NODE
ruby "$SRC/scripts/validate-snippet-liquid.rb" "$OUT/payload/snippets/cart-bundle-promo-config.liquid" | tee "$OUT/LIQUID-PARSE-RUBY.log"
