# Frozen Spec — Footer

---
status: FROZEN · SIGNED 2026-08-12 (Join the list A) · LOCKED 2026-07-31
surface: Sitewide footer (`sections/footer.liquid` via `footer-group.json`)
authority: Home WORKING layout · Andrew lock letter 2026-07-31
theme: `187144929571` (M4 Visual QA) — never live
updated: 2026-08-12
---

> Sitewide on every page via `{% sections 'footer-group' %}` in `layout/theme.liquid`.  
> Do **not** add page-level duplicate Join the list / newsletter sections.  
> Do **not** reintroduce 10% / discount claims.

## Stack (top → bottom)

1. **Trusted by** (optional TE toggle) — cream light or brand dark `#1c1916`
2. **Join the list** (optional TE toggle) — white light or brand dark; **split: headline left, form right**; checks **OFF**; **NO 10%** · body **"New colorways and studio stories."** (no cadence, no "never spam")
3. **Columns** — Shop · Learn · Support · Connect (+ Best Grippy Socks SEO under Learn)
4. **Bottom** — copyright · Made in USA

## TE locks (keep these controls)

| Control | Values |
|---------|--------|
| Show Trusted by strip | on/off |
| Trusted by theme | Light / Dark |
| Show Join the list band | on/off |
| Join the list theme | Light / Dark |
| Columns + bottom theme | Light / Dark |
| Title/body size overrides | Type OS size only (no font family) |
| Show value checkmarks | on/off — **default off** (Andrew 2026-08-12 option A) |

**Dark Join:** if checks are ever re-enabled, they match text color (no rust). Light Join rust ✓ is retired from the locked composition.

## Critical includes

- Join the list (not 10%)
- Independent Light/Dark per band (Trusted / Join / Columns)
- SEO Learn link: `/pages/best-barre-pilates-yoga-grippy-socks`
- Files: `footer.liquid`, `footer-group.json`, `assets/chrome.css`

**SIGNED 2026-08-12** — Andrew approved option A on M4. One global signup: footer-group only.

## Forbidden without Andrew letter

- Reintroduce 10%
- Split Trusted/Join into per-page sections that drift
- Overwrite locked mocks to change footer
