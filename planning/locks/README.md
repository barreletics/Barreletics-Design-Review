# Barreletics lock catalog

**Sitewide (every page):** `sitewide.lock.json` — Type OS roles, pad ladder tokens, 50/50 mobile, media QC, guarantee band, cream, sock-math editorial.

**Page spines / feature sets:** `<page>.lock.json` (e.g. `shop-all.lock.json`).

**Scan:** from Design Review root:
```bash
python3 scripts/lock-scan.py
# optional: one template
python3 scripts/lock-scan.py . templates/collection.json
```

**Rule:** never weaken a lock to pass. Update the lock only when Andrew re-locks.

**Add a page lock:** copy `shop-all.lock.json` shape (visible_spine, section_titles, features_required, pads, cream_bg).
