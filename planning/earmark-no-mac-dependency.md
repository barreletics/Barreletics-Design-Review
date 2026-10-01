# Earmark — no Mac dependency (2026-09-10)

**Andrew:** Keep all Design System work **in the Design Review repo**. After the current stretch, do **not** require Andrew’s Mac to stay connected for day-to-day draft QA.

## Source of truth

- **Repo:** `Barreletics-Design-Review` / `shopify-build/`
- **QA runtime:** draft theme `187144929571` only
- **Live** `185687998755`: never touch

## Target workflow (post-stretch)

1. Edit / PR via **Cursor cloud agent** against GitHub (not Mac-local only)
2. Theme pull/push from an always-on agent environment (Grok box Shopify CLI or CI), not Andrew’s laptop uptime
3. Mac = optional for rare local visual checks

## Status

Earmarked. Coperni specialty strip applied on draft while Mac was connected; migrate push path off Mac next.
