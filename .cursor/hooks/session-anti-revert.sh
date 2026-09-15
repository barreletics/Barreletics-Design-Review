#!/usr/bin/env bash
# Inject anti-revert context at session start for this repo.
set -euo pipefail
cat >/dev/null  # consume stdin JSON
python3 - <<'PY'
import json
print(json.dumps({
  "additional_context": (
    "ANTI-REVERT ACTIVE (Barreletics): NEVER git restore/checkout guarded "
    "shopify-build sections/templates or locked PDP mocks to fix drift. "
    "CURRENT MESSAGE WINS. Exact phrase required: restore X. "
    "Auto-invoke skill barreletics-anti-revert before editing pdp-buy-box, "
    "product*.json, footer, home-juicer, proof-numbers, value-strip, index.json. "
    "PDP trust line = Trusted by 1,000+ Instructors. H1 has NO sole dash. "
    "Badge charcoal. Do not invent review counts. Keep Open/Outdoor/reviews."
  )
}))
PY
exit 0
