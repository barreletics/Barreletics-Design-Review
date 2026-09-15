# Frozen Spec — Juicer Instagram

---
status: FROZEN · LOCKED 2026-07-31
surface: Reusable library section (`sections/home-juicer.liquid`)
authority: PDP Definitive-v19 `#instagram` · Andrew letter 2026-07-31 (“lock it for all pages to be used on or not”)
theme: repo master — deploy only when Andrew names a draft ID
updated: 2026-07-31
---

> **Reusable on any page.** Add or omit in Theme Editor.  
> Filename `home-juicer` kept for template type stability; display name **Juicer Instagram**.  
> Do **not** force onto every product/page JSON — availability ≠ auto-include.

## Composition

1. Eyebrow — Follow the movement  
2. Heading — @barreletics  
3. Body — Real practitioners. Real studios. Real grip.  
4. Live Juicer feed (`barreletics`) — bigger tiles, page scroll only  
5. See more (on-page load more)  
6. Follow on Instagram → (secondary)

## Locked TE defaults

| Control | Default |
|---------|---------|
| posts_per_page | 12 |
| max_pages | 1 |
| enable_see_more | true |
| max_height | **0** (no clamp / no inner scroll) |
| feed_id | barreletics |
| bg | #ffffff |

Per-page instances (e.g. PDP) may override settings when the section is added.

## Forbidden without Andrew letter

- Homepage-only coupling / remove presets
- Default max-height > 0 (inner sidebar scroll)
- Auto-wiring into every template JSON
- Overwriting locked PDP v16 mock
