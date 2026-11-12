#!/usr/bin/env bash
# COPY03 interactive cart module — baseline 5a01277 (3 files, no settings_*).
set -euo pipefail
BASE="${REV_BASE_COMMIT:-5a01277}"
SRC="${1:-/workspace/shopify-build}"
OUT="${2:-/opt/cursor/artifacts/cart-interactive-copy03-fixed}"
TAR_NAME="${TAR_NAME:-cart-interactive-copy03-fixed.tar.gz}"
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
TEST_LOG="$OUT/evidence/VERIFY-ALL-TESTS.log"
(cd "$SRC" && npm run test:cart-all >"$TEST_LOG" 2>&1) || true
sync
sleep 0.2
sha256sum "$OUT/payload/"*/* >"$OUT/evidence/PAYLOAD-SHA256.txt"
cp "$SRC/deploy/CART-OFFER-AB-GUIDE.md" "$OUT/"
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
const m={
  deliverable:'cart-interactive-copy03-fixed',
  baselineCommit:base,
  baselineFull:execSync('git -C /workspace rev-parse '+base,{encoding:'utf8'}).trim(),
  allowlist:list,
  files,
  stageNote:'URL A/B default control (5a01277); variant COPY03 inline cross-sell.',
  abParam:'br_cart_offer=control|variant',
  excludedFromPush:['config/settings_schema.json','config/settings_data.json','assets/cart.js','layout/theme.liquid','sections/main-cart.liquid']
};
fs.writeFileSync(path.join(out,'MANIFEST-COPY03.json'),JSON.stringify(m,null,2)+'\n');
fs.writeFileSync(path.join(out,'PUSH-ONLY.txt'),'# Parent-approved theme push only (not run by cloud agent)\n'+list.map(p=>'shopify theme push ... --only '+p).join('\n')+'\n');
fs.writeFileSync(path.join(out,'COPY03-HANDOFF.txt'),
['COPY03 progressive cart module + URL A/B (br_cart_offer=control|variant)',
 '- At 1 qualifying Performance Skin pair: exact headline + Add Open/Closed Sole flow.',
 '- At 2+ pairs: 15% preview line/savings then 35% one-pant photo/picker.',
 '- Preview notice on all stages; no unlock/discount codes/checkout intercept.',
 '- Source tests mock product JSON + add path; browser proof is parent-only.',
 ''].join('\n'));
"
tar --warning=no-file-changed -czf "$(dirname "$OUT")/$TAR_NAME" -C "$(dirname "$OUT")" "$(basename "$OUT")"
sha256sum "$(dirname "$OUT")/$TAR_NAME"
echo "Wrote $OUT and $(dirname "$OUT")/$TAR_NAME"
