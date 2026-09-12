# M4 Store Portability Rules

**Principle:** The theme adapts to the store. The store must never change to accommodate the theme.

## Navigation (hard rule)

- **Do not** invent or require new Admin → Navigation handles (`footer-shop`, `footer-support`, `footer-company`, `help-menu`, etc.).
- Menus are **global to the store**, not theme-specific. Development must not alter live Navigation.
- Header/footer use Theme Editor **`link_list` pickers** only.
- Unassigned menus → render nothing for that slot (no errors, no hardcoded link fallbacks to Barreletics URLs).
- Footer fallback: optional column pickers → else **primary footer menu** (`footer` on this store today if assigned in Theme Editor). Nested items → columns; flat → one list.

## Allowed soft defaults in theme JSON

| Setting | OK? | Why |
|---------|-----|-----|
| `menu: main-menu` in header-group | OK if that handle already exists on the store | Shopify default; Theme Editor can reassign |
| `menu: footer` in footer-group | OK if that handle already exists | Existing store menu; not a new handle |
| Invented handles | **Forbidden** | Requires store Navigation changes |

## Other assumptions to eliminate (tracked)

| Assumption | Status | Fix |
|------------|--------|-----|
| Hardcoded `/collections/grippy-shoes` etc. in sections/snippets | **Open** | Prefer Theme Editor URL settings / collection pickers; empty if unset |
| Hardcoded logo wordmark “BARRELETICS” | **Fixed** in `header.liquid` → `shop.name` |
| Hardcoded social URLs in footer-group | **Fixed** → blank; merchant sets in Theme Editor |
| Required Help Scout / Tidio / Meta snippets in layout | **Open (2.0)** | App embeds XOR theme snippets; layout must not error if absent |
| Required metafield definitions for theme to boot | Theme may enhance with metafields but must not crash if missing | Guard with `blank` checks (br-variants already does for many) |
| App-specific sections (Shogun/PageFly) | Keep optional; never required for chrome boot | |

## Before continuing Phase 2.0 restorations

1. Push portable header/footer to draft `187143618851` only.
2. In Theme Editor, assign existing `main-menu` + `footer` (no Admin Navigation edits).
3. Then clear Liquid errors / cart — still no new Navigation handles.
