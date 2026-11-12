#!/usr/bin/env bash
set -euo pipefail
SRC="${1:-/workspace/shopify-build}"
OUT="${2:-/opt/cursor/artifacts/cart-bundles-hotfix-2file}"
if [[ "${SNIPPET_ONLY:-}" == "1" ]]; then
  ALLOWLIST=(snippets/cart-bundle-promo-config.liquid)
else
  ALLOWLIST=(
    snippets/cart-bundle-promo-config.liquid
    config/settings_schema.json
  )
fi
rm -rf "$OUT"
mkdir -p "$OUT/payload/snippets" "$OUT/payload/config"
for rel in "${ALLOWLIST[@]}"; do
  cp "$SRC/$rel" "$OUT/payload/$rel"
done
node -e "
const fs=require('fs');const crypto=require('crypto');const path=require('path');
const out=process.argv[1];const src=process.argv[2];
const list=JSON.parse(process.argv[3]);
const files=list.map(rel=>({path:rel,sha256:crypto.createHash('sha256').update(fs.readFileSync(path.join(src,rel))).digest('hex')}));
const m={generatedAt:new Date().toISOString(),hotfix:'shopify-cli-validation-rejections',allowlist:list,files,redeployNote:'Parent may re-run same 8-file push; only these 2 paths changed since last attempt.'};
fs.writeFileSync(path.join(out,'MANIFEST-HOTFIX.json'),JSON.stringify(m,null,2)+'\n');
" "$OUT" "$SRC" '["snippets/cart-bundle-promo-config.liquid","config/settings_schema.json"]'
TAR_NAME="$(basename "$OUT").tar.gz"
tar -czf "$(dirname "$OUT")/$TAR_NAME" -C "$(dirname "$OUT")" "$(basename "$OUT")"
echo "Wrote $OUT and $(dirname "$OUT")/$TAR_NAME"
