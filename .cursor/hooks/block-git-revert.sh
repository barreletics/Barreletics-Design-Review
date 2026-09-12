#!/usr/bin/env bash
# FAIL-CLOSED: block git restore / checkout overwrites of guarded Barreletics paths
# unless ALLOW_BARRELETICS_RESTORE=1 (only after Andrew said "restore X" in CURRENT message).
set -euo pipefail

input=$(cat)
command=$(printf '%s' "$input" | python3 -c 'import json,sys; print(json.load(sys.stdin).get("command") or "")')

deny() {
  local msg="$1"
  python3 -c 'import json,sys; print(json.dumps({"permission":"deny","user_message":sys.argv[1],"agent_message":sys.argv[2]}))' \
    "$msg" \
    "ANTI-REVERT HOOK DENIED this command. Read barreletics-anti-revert skill + .cursor/rules/anti-revert-fail-closed.mdc. Only proceed if Andrew said restore X in the CURRENT message, then re-run with ALLOW_BARRELETICS_RESTORE=1."
  exit 0
}

# Fast allow: empty or clearly unrelated
if [[ -z "$command" ]]; then
  echo '{ "permission": "allow" }'
  exit 0
fi

# Escape hatch after explicit Andrew "restore X"
if [[ "${ALLOW_BARRELETICS_RESTORE:-}" == "1" ]]; then
  echo '{ "permission": "allow" }'
  exit 0
fi

# Normalize for matching
lc=$(printf '%s' "$command" | tr '[:upper:]' '[:lower:]')

guarded_hit=0
printf '%s' "$lc" | grep -Eq 'shopify-build/(sections|templates)|pdp-buy-box|home-juicer|proof-numbers|value-strip|footer\.liquid|product\.json|product\.open-sole|product\.outdoor|index\.json|definitive-v1[69]|m4-section-freeze' && guarded_hit=1

is_restore=0
# git restore …
printf '%s' "$lc" | grep -Eq '(^|[;&|]|&&|\|\|)[[:space:]]*git[[:space:]]+restore([[:space:]]|$)' && is_restore=1
# git checkout -- path / git checkout HEAD -- path (path restore form)
printf '%s' "$lc" | grep -Eq 'git[[:space:]]+checkout([[:space:]]+(-[bB]|--[[:alnum:]-]+|HEAD|@|origin/[^[:space:]]+|main|master|[0-9a-f]{7,40}))*[[:space:]]+--[[:space:]]+' && is_restore=1
# git show COMMIT:path > file  or  git show … | tee
printf '%s' "$lc" | grep -Eq 'git[[:space:]]+show[[:space:]]+[^|;]*:(shopify-build|docs/)' && is_restore=1
printf '%s' "$lc" | grep -Eq 'git[[:space:]]+show[[:space:]].*>([[:space:]]|.)*shopify-build' && is_restore=1
# checkout of a single file without -- also common
printf '%s' "$lc" | grep -Eq 'git[[:space:]]+checkout[[:space:]]+[^|;]*[[:space:]]+shopify-build/' && is_restore=1

if [[ "$is_restore" -eq 1 && "$guarded_hit" -eq 1 ]]; then
  deny "Blocked git restore/checkout of a guarded Barreletics path. Say restore X in chat, or set ALLOW_BARRELETICS_RESTORE=1 only after that letter."
fi

# Broader: any git restore touching shopify-build even if path match missed
if [[ "$is_restore" -eq 1 ]]; then
  if printf '%s' "$lc" | grep -Eq 'shopify-build|\.liquid|\.json|definitive-v'; then
    deny "Blocked likely restore of theme/mock files. Anti-revert fail-closed."
  fi
fi

echo '{ "permission": "allow" }'
exit 0
