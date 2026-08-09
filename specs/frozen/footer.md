# Frozen Spec — Footer

---
status: FROZEN · LOCKED 2026-07-31
surface: Sitewide footer (`sections/footer.liquid` via `footer-group.json`)
authority: Home WORKING layout · Andrew lock letter 2026-07-31
theme: `187144929571` (M4 Visual QA) — never live
updated: 2026-07-31
---

> Sitewide on every page via `{% sections 'footer-group' %}` in `layout/theme.liquid`.  
> Do **not** add page-level duplicate Join the list / newsletter sections.  
> Do **not** reintroduce 10% / discount claims.

## Stack (top → bottom)

1. **Trusted by** (optional TE toggle) — cream light or brand dark `#1c1916`
2. **Join the list** (optional TE toggle) — white light or brand dark; form + checks; **NO 10%**
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
| Show value checkmarks | on/off |

**Dark Join:** checkmarks match text color (no rust). Light Join: rust ✓.

## Critical includes

- Join the list (not 10%)
- Independent Light/Dark per band (Trusted / Join / Columns)
- SEO Learn link: `/pages/best-barre-pilates-yoga-grippy-socks`
- Files: `footer.liquid`, `footer-group.json`, `assets/chrome.css`

## Forbidden without Andrew letter

- Reintroduce 10%
- Split Trusted/Join into per-page sections that drift
- Overwrite locked mocks to change footer
