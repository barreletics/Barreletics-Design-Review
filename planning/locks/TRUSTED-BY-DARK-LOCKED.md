# Trusted by strip — DARK LOCKED (sitewide)

**Confirmed:** Andrew 2026-09-14 — “wicked cool” / lock it.  
**Surface:** Footer group · every page  
**File:** `shopify-build/sections/footer-group.json` → `sections.footer.settings`

## Locked values

```
show_studio_trust: true
trust_theme: dark
```

Renders black band + white type (`.footer-studio-trust--dark` in `assets/chrome.css`).

## Why

Breaks cream → white → cream sandwiches. One global footer setting — not per-template.

## Never

- Flip back to `light` / cream without Andrew letter
- Hide the strip sitewide without letter
- Invent a third trust theme

## Guardrails

| Layer | Path |
| --- | --- |
| Letter | `planning/locks/TRUSTED-BY-DARK-LOCKED.md` |
| Machine | `planning/locks/sitewide.lock.json` → `trusted_by_footer` |
| Scanner | `scripts/lock-scan.py` |
| CSS | `assets/chrome.css` → `.footer-studio-trust--dark` |

## Before push

`python3 scripts/lock-scan.py .` — must not FAIL trusted_by_footer.
