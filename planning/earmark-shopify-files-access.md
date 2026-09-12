# Earmark — Shopify file cabinet access (2026-09-10)

**Andrew:** Grok needs access to the Shopify Admin **Files / media library** (not only product CDN URLs and theme assets) to pick better PDP photos without guessing.

## Current access

- Product `.js` media URLs
- Theme `assets/`
- Known CDN file URLs already on templates

## Missing

- Browse / search all Files in Admin
- Upload new crops into Files from agent workflow

## Next

Connect Shopify Admin (Files) or Theme Access workflow so media QC can pull from the real cabinet. Keep Design Review repo as source of truth for which URL is locked on each section.
