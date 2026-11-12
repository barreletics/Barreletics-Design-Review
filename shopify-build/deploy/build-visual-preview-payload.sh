#!/usr/bin/env bash
# Minimal visual overlay vs deployed 52efdab (3 files — no settings_schema/settings_data).
set -euo pipefail
BASE="${REV_BASE_COMMIT:-52efdab}"
SRC="${1:-/workspace/shopify-build}"
OUT="${2:-/opt/cursor/artifacts/cart-bundles-visual-preview-52efdab}"
ALLOWLIST=(
  assets/cart-bundle-promo.js
  assets/cart-bundle-promo.css
  snippets/cart-bundle-promo-config.liquid
)
rm -rf "$OUT"
mkdir -p "$OUT/payload" "$OUT/evidence"
for rel in "${ALLOWLIST[@]}"; do
  mkdir -p "$OUT/payload/$(dirname "$rel")"
  cp "$SRC/$rel" "$OUT/payload/$rel"
done
ruby "$SRC/scripts/validate-snippet-liquid.rb" "$OUT/payload/snippets/cart-bundle-promo-config.liquid" >"$OUT/evidence/LIQUID-PARSE-RUBY.log" 2>&1
echo "exit_code=$?" >>"$OUT/evidence/LIQUID-PARSE-RUBY.log"
(cd "$SRC" && npm run test:cart-all >"$OUT/evidence/VERIFY-ALL-TESTS.log" 2>&1) || true
sha256sum "$OUT/payload/"*/* >"$OUT/evidence/PAYLOAD-SHA256.txt"
REV_BASE_COMMIT="$BASE" SRC="$SRC" OUT="$OUT" node -e "
const fs=require('fs');const crypto=require('crypto');const path=require('path');const {execSync}=require('child_process');
const base=process.env.REV_BASE_COMMIT, src=process.env.SRC, out=process.env.OUT;
const list=['assets/cart-bundle-promo.js','assets/cart-bundle-promo.css','snippets/cart-bundle-promo-config.liquid'];
function shaBuf(b){return crypto.createHash('sha256').update(b).digest('hex')}
const files=list.map(rel=>{
  let before=null;
  try{before=execSync('git -C /workspace show '+base+':shopify-build/'+rel,{encoding:'buffer'})}catch(e){}
  const after=fs.readFileSync(path.join(out,'payload',rel));
  return {path:rel,sha256_before:before?shaBuf(before):null,sha256_after:shaBuf(after),status:before?'modified':'added'}
});
const m={baselineCommit:base,baselineFull:'52efdab9d6c8f51dc375283ad12a9f5806721d2a',allowlist:list,files,excludedFromPush:['config/settings_schema.json','config/settings_data.json','assets/cart.js','layout/theme.liquid','sections/main-cart.liquid']};
fs.writeFileSync(path.join(out,'MANIFEST-VISUAL.json'),JSON.stringify(m,null,2)+'\n');
fs.writeFileSync(path.join(out,'PUSH-ONLY.txt'),list.map(p=>'shopify theme push ... --only '+p).join('\n')+'\n');
"
cp "$SRC/deploy/VISUAL-PREVIEW-TEST-BRIEF.md" "$OUT/"
tar -czf "$(dirname "$OUT")/$(basename "$OUT").tar.gz" -C "$(dirname "$OUT")" "$(basename "$OUT")"
echo "Wrote $OUT"
