# 03 — Design System

---
document: 03 – Design System
version: 1.0
status: 🔵 Ready for Review
approved_by: —
approval_date: —
last_modified: 2026-07-18
depends_on: [01, 02]
supersedes: [QA-03-DESIGN-SYSTEM.md]
---

## Canonical Source

The full design system is maintained as a Cursor skill:
`~/.cursor/skills/barreletics-design-system/SKILL.md`

That skill is auto-invoked on any Barreletics HTML/CSS work and contains all tokens, component CSS, and build rules. This document provides system-level context and resolved design decisions that supplement the skill.

## Design System Version

**v49** — Confirmed approved. All new work builds around v49; never rewrite existing v49 sections.

## Hard Rules

1. **v49 is the base.** Never rewrite existing v49 sections — only add around them.
2. **No black and orange.** The brand palette is warm neutrals + rust accent. Pure black (#000) and bright orange are banned.
3. **No external CSS for mockups.** New sections use inline styles or a `<style>` block appended to v49's existing styles.
4. **Rust accent (#c45c3f) is limited.** Badges, benefit numbers, CTA hovers, justifier card borders, eyebrow labels. Never as a background fill.
5. **Coral (#e8927c) for cart badge only.** Do not use elsewhere.
6. **"Blog" → "Journal"** in all navigation, URLs, and references.

## Resolved Design Tokens

These values are canonical. All ADR conflicts from the prior planning phase are resolved per the v49 approved design and recency rule.

### Color Palette

| Token | Hex | Use |
|-------|-----|-----|
| Charcoal (primary text) | `#1c1916` | Body text, headings, CTA background, dark sections |
| Rust (accent) | `#c45c3f` | Badges, numbers, hover states, card borders |
| Gold (stars) | `#d4af37` | Star ratings only |
| Body text | `#4a4a4a` | Paragraph copy |
| Muted text | `#8a8a8a` | Labels, meta text, fine print |
| Warm muted | `#6b645a` | Secondary body text |
| Warm border | `#d6cfc0` | Dividers, input borders |
| Warm cream bg | `#f5f2ec` | Alternating section backgrounds |
| Light bg | `#f9f9f9` | Card/gallery backgrounds |
| White | `#ffffff` | Primary background |

**Resolution notes:**
- Primary text is `#1c1916` (warm charcoal), not `#050505`. The v49 PDP and matured homepage both use the warmer value. (Resolves ADR-01, ADR-05)
- Star/rating color is `#d4af37` (antique gold), not `#fbc02d`. Matches v49 PDP. (Resolves ADR-07)

### Typography

- **Font family:** `'Roboto', -apple-system, BlinkMacSystemFont, sans-serif`
- **Headings:** 42px / 700 / 1.2 → 32px mobile
- **H1:** 44px / 700 / 1.08 → 32px mobile
- **Body:** 15–16px / 400 / 1.6–1.7
- **Eyebrow labels:** 11px / 700 / uppercase / letter-spacing `0.08em` / color `#8a8a8a`
- **Benefit numbers:** 11px / 700 / uppercase / letter-spacing `0.08em` / color `#c45c3f`
- **Badge:** 10px / 700 / uppercase / letter-spacing `0.08em` / bg `#c45c3f` / color `#fff` / border-radius `3px`

**Resolution notes:**
- Eyebrow letter-spacing is `0.08em`, not `0.14em`. Matches v49 PDP and matured homepage CSS tokens. Component-specific overrides (manifesto `0.18em`, closing CTA `0.06em`) are documented exceptions. (Resolves ADR-04)

### Border Radius

| Element | Radius |
|---------|--------|
| CTA buttons | `6px` |
| Size selector pills | `6px` |
| Gallery/video containers | `8px` |
| Review cards | `12px` |
| Justifier cards | `12px` |
| Badges | `3px` |
| Color swatches | `50%` (circle) |

**Resolution notes:**
- The system-level "0px default, never 12px" rule is superseded by v49 approved values. v49 uses contextual radius: square for structural elements, rounded for content/interaction elements. (Resolves ADR-03, ADR-06)

### Spacing

- **Section padding:** 64px vertical / 40px horizontal → 48px/16px mobile
- **Max content width:** 1200px (centered)
- **Hero max width:** 1400px
- **Grid gaps:** 20–40px depending on density
- **50/50 Split:** `height: 420px` fixed, `overflow: hidden`, `padding: 80px 72px` copy side. Mobile: `height: auto`.

### Breakpoints

| Breakpoint | Changes |
|------------|---------|
| ≤1024px | Benefits → 2-col, variants → 2-col, reviews → 2-col, motion → 2-col |
| ≤768px | Hero → single column, gallery unsticks, H1 → 32px, sections → 16px padding |

### Eyebrow Color Rule
- **White** `rgba(255,255,255,0.7)` on dark sections
- **Coral** `var(--br-accent)` / `#c45c3f` only on white/light backgrounds

## Section Inventory (v49 approved order — PDP)

1. Hero (gallery + buy box with rust badge)
2. Brand pillars strip (warm cream bg)
3. Variant grid — "The Studio Collection"
4. Reviews — "Real people. Real results."
5. Sock math — "One pair replaces eight."
6. Motion — "See how it works."
7. Justifier testimonials — "Real feedback from the floor."
8. FAQ — "Everything you need to know."
9. Newsletter — "Join the list"

---

**Cross-references:**
- Full token details → Barreletics Design System skill
- Component specs → `04-component-library.md`
- Page architectures → `05-pdp-architecture.md`, `06-homepage-architecture.md`
- Decision history → `10-decision-log.md`
