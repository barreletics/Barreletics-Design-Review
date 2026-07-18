# Canonical Design System Diff

**Date:** 2026-07-13
**Purpose:** Compare matured implementation values against knowledge base documentation
**Method:** Extract every design token from matured HTML/CSS, compare against docs/03, docs/04, docs/05, docs/06

---

## COLORS

### Primary Palette

| Token / Purpose | PDP v36 HTML | DS v1.0 HTML | Homepage :root (docs/06) | pdp-styles.css | docs/03 | docs/04 | Drift Type | Recommended Canonical |
|-----------------|-------------|--------------|--------------------------|----------------|---------|---------|------------|----------------------|
| Page background | `#fff` | `#faf9f7` (page bg) | `#ffffff` (--br-bg) | `#ffffff` | `#ffffff` (--br-bg) | `#ffffff` | **Documentation drift** — DS v1.0 uses #faf9f7 for page bg while all others use #fff | `#ffffff` for PDP; `#faf9f7` for DS chrome only |
| Primary text | `#1c1916` | `#1c1916` (Warm Charcoal) | `#050505` (--br-text) | inherits `var(--br-text)` = `#050505` | `#050505` | `#050505` | **PDP-specific** — PDP v36 + DS v1.0 use warm charcoal #1c1916; Homepage/matured uses near-black #050505 | **Architect decision required.** PDP direction = #1c1916; Homepage direction = #050505 |
| Secondary text | `#4a4a4a` | `#4a4a4a` | `#4a4a4a` (--br-text-soft) | `var(--br-text-soft)` = `#4a4a4a` | `#4a4a4a` | `#6a6a6a` | **Documentation drift** — docs/04 says #6a6a6a but every implementation uses #4a4a4a | `#4a4a4a` |
| Muted text | `#8a8a8a` | `#9a9182` (warm muted) | `#8a8a8a` (--br-text-mute) | `var(--br-text-mute)` = `#8a8a8a` | `#8a8a8a` | `#999999` | **PDP-specific** — PDP v36 uses both: #8a8a8a (cool muted) + #9a9182 (warm muted). DS v1.0 defines #9a9182 as the warm muted. docs/04 = #999999 | PDP v36: #8a8a8a (inline), #9a9182 (DS v1.0 warm context). docs/04 #999999 is stale |
| Supporting text | `#5a5248` (desc), `#6b645a` (FAQ body) | `#6b6459` | — | — | — | — | **Undocumented** — #5a5248 used in PDP desc inline style; #6b645a in FAQ body. DS v1.0 defines #6b6459 | `#6b6459` per DS v1.0; PDP #5a5248 is a warm variant |
| Title text (H1 SEO) | `#2d2926` | `#2d2926` | — | — | — | — | **Consistent** (PDP-specific token) | `#2d2926` for SEO H1 label |
| Ultra-muted text | — | `#b0a898` | — | — | — | — | **Undocumented** in docs/ | `#b0a898` per DS v1.0 |
| Accent / CTA hover | `#c45c3f` (terracotta) | `#c45c3f` (terracotta) | `#f97250` (--br-accent, coral) | inherits `var(--br-accent)` = `#f97250` | `#f97250` | `#f97250` | **PDP-specific** — PDP v36 + DS v1.0 use terracotta #c45c3f; Homepage uses coral #f97250 | **Architect decision required.** Two parallel accent colors: terracotta (PDP/DS v1.0) vs coral (Homepage/matured) |
| Accent hover | — | — | `#e85e3c` (--br-accent-hover) | — | `#e85e3c` | — | **Consistent** (Homepage only) | `#e85e3c` for coral hover |
| Star rating | `#d4af37` (gold) | `#d4af37` (gold) | `#fbc02d` (--br-star) | `var(--br-accent)` = `#f97250` | `#fbc02d` | `#fbc02d` | **Implementation drift** — PDP v36/DS v1.0 use antique gold #d4af37; Homepage + docs use bright gold #fbc02d; pdp-styles.css wrongly uses accent coral for stars | **Architect decision required.** PDP = #d4af37 (antique gold); Homepage = #fbc02d (bright gold) |
| LE badge (in-swatch) | `#2563eb` (blue) | — | `#3a8de8` (--br-le) | `var(--br-le)` = `#3a8de8` | `#3a8de8` | — | **Implementation drift** — PDP v36 inline uses #2563eb; pdp-styles.css/docs use #3a8de8 | `#3a8de8` (docs are correct; PDP v36 inline is approximate) |
| LE badge bg | — | — | `#eaf3fc` (--br-le-bg) | — | `#eaf3fc` | — | **Consistent** | `#eaf3fc` |
| Info / sale banner | — | — | `#3a8de8` (--br-info) | — | `#3a8de8` | — | **Consistent** | `#3a8de8` |
| Button fill | `#1c1916` | `#1c1916` | `#050505` (--br-button) | `var(--br-text)` = `#050505` | `#050505` | `#050505` | **PDP-specific** — same drift as primary text | Match primary text decision |

### Structural / UI Colors

| Token / Purpose | PDP v36 HTML | DS v1.0 HTML | Homepage :root | pdp-styles.css | docs/03 | docs/04 | Drift Type | Recommended Canonical |
|-----------------|-------------|--------------|----------------|----------------|---------|---------|------------|----------------------|
| Divider / border | `#e6e6e6` | `#e6e6e6` | `#e6e6e6` (--br-line) | `var(--br-line)` = `#e6e6e6` | `#e6e6e6` | `#e5e2db` | **Documentation drift** — docs/04 says #e5e2db; all implementations use #e6e6e6 | `#e6e6e6` |
| Soft line | — | — | `#efefef` (--br-line-soft) | — | `#efefef` | — | **Consistent** | `#efefef` |
| Warm divider | `#d6cfc0` | `#e8e4de` | — | — | — | — | **PDP-specific** — PDP v36 uses #d6cfc0 for FAQ/warm borders; DS v1.0 defines #e8e4de as warm divider | #d6cfc0 (PDP) and #e8e4de (DS v1.0) are both valid warm variants |
| Alt background (warm) | `#f5f2ec` (brand section) | `#f5f2ec` (Warm Linen) | `#f9f9f9` (--br-alt-bg) | `var(--br-alt-bg)` = `#f9f9f9` | `#f9f9f9` | `#f9f7f2` | **PDP-specific** — PDP v36 uses #f5f2ec for warm sections; Homepage uses #f9f9f9 (neutral grey); docs/04 says #f9f7f2 (yet another value) | PDP warm = `#f5f2ec`; Homepage neutral = `#f9f9f9`; docs/04 #f9f7f2 is stale |
| Alt background 2 | — | — | `#f3f3f3` (--br-alt-bg-2) | — | `#f3f3f3` | — | **Consistent** | `#f3f3f9` |
| Gallery/image bg | `#f9f9f9` | `#f5f2ec` (card bg) | — | — | — | — | **PDP-specific** — PDP hero gallery uses #f9f9f9; DS v1.0 collection cards use #f5f2ec | PDP gallery = `#f9f9f9`; product cards = `#f5f2ec` |
| Card border | `#e6e6e6` (review card) | — (no border on product cards) | — | — | — | — | **Consistent** — only review cards get border | Review cards: `1px solid #e6e6e6`; product cards: none |
| Inactive button bg | — | `#f0efec` | — | — | — | — | **Undocumented** in docs/ | `#f0efec` per DS v1.0 |
| Size badge bg | — | `#ece9e3` | — | — | — | — | **Undocumented** in docs/ | `#ece9e3` per DS v1.0 |
| Tab inactive text | `#7a7268` | `#7a7268` | — | — | — | — | **Undocumented** in docs/ | `#7a7268` |
| Tab disabled text | `#b0a898` | `#b0a898` | — | — | — | — | **Undocumented** in docs/ | `#b0a898` |

### Product Swatch Colors (PDP v36 only — undocumented)

| Swatch Name | Hex | Status |
|-------------|-----|--------|
| Onyx | `#050505` | Undocumented |
| Dusty Rose | `#e9d3cb` | Undocumented |
| Stone | `#c9c5b8` | Undocumented |
| Sage | `#7b8c84` | Undocumented |
| White | `#fff` | Undocumented |
| Terracotta | `#d4a78a` | Undocumented |
| Espresso | `#3d3530` | Undocumented |
| Mist | `#b8c4c0` | Undocumented |
| Cream | `#e8e0d0` | Undocumented |
| Mocha | `#8b7355` | Undocumented |
| Forest | `#5c6b5e` | Undocumented |
| Coperni | `#c8b99a` | Undocumented |

---

## TYPOGRAPHY

| Token / Purpose | PDP v36 HTML | DS v1.0 HTML | Homepage :root (docs/06) | pdp-styles.css | docs/03 | docs/04 | Drift Type | Recommended Canonical |
|-----------------|-------------|--------------|--------------------------|----------------|---------|---------|------------|----------------------|
| Font family (primary) | `'Roboto', -apple-system, BlinkMacSystemFont, sans-serif` | `'Roboto', -apple-system, sans-serif` | `'Roboto', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif` | inherits via var(--t-font) | Roboto | Roboto only (300–700) | **Consistent** — all use Roboto; fallback stack varies slightly | `'Roboto', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif` (fullest fallback) |
| Font family (mono/code) | — | `'SF Mono', 'Fira Code', monospace` | — | `ui-monospace, Menlo, monospace` | JetBrains Mono (matured direction only) | — | **Documentation drift** — docs/03 says JetBrains Mono; DS v1.0 says SF Mono/Fira Code; pdp-styles uses ui-monospace | `'SF Mono', 'Fira Code', monospace` for DS specs; `ui-monospace, Menlo, monospace` for product labels |
| Hero display headline | 44px / 700 / 1.08 lh | 44px / 300+700 mixed / 1.08 lh | 72px (--t-display) | `clamp(28px, 3vw, 40px)` / 400 | 44px (--t-h2) | — | **PDP-specific** — PDP hero = 44px; Homepage display = 72px. pdp-styles uses clamp(28-40px) which is the older design | PDP: `44px`; Homepage: `72px` |
| H1 (SEO product title) | 18px / 600 / #2d2926 | 18px / 600 / #2d2926 | 56px (--t-h1) | `clamp(28px, 3vw, 40px)` (buy__name) | 56px | — | **PDP-specific** — PDP uses 18px for H1 (styled as secondary for SEO); homepage H1 = 56px | PDP H1: `18px/600/#2d2926`; Homepage H1: `56px` |
| H2 section title | 42px / 700 / 1.2 lh (class) | 38px / 300+700 mixed / 1.08 lh | 44px (--t-h2) | `clamp(28px, 3.2vw, 44px)` / 500 | 44px | — | **Implementation drift** — PDP section__title = 42px; DS v1.0 = 38px; Homepage token = 44px; pdp-styles clamp to 44px | PDP sections: `42px/700`; editorial H2: `38px/300+700`; Homepage: `44px` |
| H2 (PDP brand section) | 40px / 300+700 / 1.1 lh | 38px / 300+700 / 1.08 lh | — | — | — | — | **PDP-specific** — inline 40px vs DS v1.0 spec of 38px | `38px` per DS v1.0 (PDP inline 40px is approximate) |
| H3 value block | 18px / 700 / 1.2 lh (inline) | 18px / 700 / 1.2 lh | 36px (--t-h3) | 17px / 600 (benefit__title) | 36px | — | **PDP-specific** — PDP H3 = 18px; Homepage system H3 = 36px; pdp-styles uses 17px | PDP H3: `18px/700`; Homepage H3: `36px` |
| Benefit title | 20px / 700 (class) | — | — | 17px / 600 (pdp-benefit__title) | — | — | **Implementation drift** — PDP v36 stylesheet says 20px; pdp-styles.css says 17px | `20px/700` (PDP v36 wins as newest matured) |
| Eyebrow / section label | 11px / 700 / uppercase / 0.08em / #8a8a8a | 11px / 600 / uppercase / 0.1em / #9a9182 | 12px (--t-eyebrow) / 0.08em / 600 | 12px / 700 / 0.14em | 12px / 0.08em / 600 | 12px / 700 / 0.14em | **Implementation drift** — 3 different eyebrow specs: PDP v36=11px/0.08em; DS v1.0=11px/0.1em; Homepage/pdp-styles=12px/0.14em | **Architect decision required.** PDP direction: `11px/700/0.08em`; Homepage direction: `12px/700/0.14em` |
| Body primary | 16px / 400 / 1.6 lh (desc class) | 16px / 400 / 1.65 lh | 16px (--t-body) | — | 16px | 16px | **Consistent** — minor line-height variance (1.6 vs 1.65) | `16px/400/1.65` |
| Body supporting | 15px / 400 / 1.6 lh | 15px / 400 / 1.7 lh | — | 15px / 1.55 lh | — | — | **Consistent** — minor lh variance | `15px/400/1.7` per DS v1.0 |
| Product card name | 24px / 700 / 1.1 lh (inline) | 22px / 700 / 1.1 lh | — | 14px / 500 (vcard__title) | — | — | **Implementation drift** — PDP v36 inline = 24px; DS v1.0 = 22px; pdp-styles vcard = 14px | `22px/700` per DS v1.0 (pdp-styles 14px is the older matured direction) |
| Product type label | 11px / 300 / 0.01em / #9a9182 (inline) | 11px / 300 / 0.01em / #9a9182 | — | 12px / soft (vcard__meta) | — | — | **Consistent** between PDP v36 and DS v1.0 | `11px/300/0.01em/#9a9182` |
| Price (grid card) | 13px / 700 / #1c1916 (inline) | 13px / 700 / #1c1916 | — | 13px / 500 (vcard__price) | — | — | **Implementation drift** — weight differs: PDP v36 = 700; pdp-styles = 500 | `13px/700` (PDP v36 wins) |
| Price (hero) | 36px / 700 / #1c1916 (class) | — | — | 22px / 500 (buy__price-now) | — | — | **Implementation drift** — PDP v36 = 36px/700; pdp-styles = 22px/500 | `36px/700` (PDP v36 wins as newest) |
| Review text | 15px / italic / 1.7 lh / #4a4a4a | — | — | 14px / 1.6 lh (review__body) | — | — | **PDP-specific** — PDP v36 review = 15px italic; pdp-styles = 14px regular | `15px/italic/1.7/#4a4a4a` (PDP v36 wins) |
| Review author | 13px / 700 / #1c1916 | — | — | 11.5px / 0.06em (review__attr) | — | — | **Implementation drift** — PDP v36 = 13px/700; pdp-styles = 11.5px | `13px/700` (PDP v36 wins) |
| FAQ trigger | 16px / 500 / #1c1916 | — | — | 17px / 500 (faq__item summary) | — | — | **Implementation drift** — PDP v36 = 16px; pdp-styles = 17px | `16px/500` (PDP v36 wins) |
| FAQ body | 14px / 400 / 1.6 lh / #6b645a | — | — | 15px / 1.65 lh (faq__body) | — | — | **Implementation drift** — PDP v36 = 14px; pdp-styles = 15px | `14px/400/1.6/#6b645a` (PDP v36 wins) |
| Newsletter title | 36px / 500 / #1c1916 | — | — | — | — | — | **Undocumented** | `36px/500/#1c1916` |
| Newsletter desc | 15px / 400 / #6b645a / 1.6 lh | — | — | — | — | — | **Undocumented** | `15px/400/#6b645a` |
| Trust row | 12px / 400 / #8a8a8a | — | — | 11.5px / 0.06em (shipnote) | — | — | **Implementation drift** — PDP v36 = 12px; pdp-styles = 11.5px | `12px/400/#8a8a8a` (PDP v36 wins) |
| Accordion summary | 14px / 600 | — | — | 13px / 500 / 0.06em (buy__tab summary) | — | — | **Implementation drift** — PDP v36 = 14px/600; pdp-styles = 13px/500 | `14px/600` (PDP v36 wins) |
| Accordion body | 14px / 400 / #4a4a4a / 1.7 lh | — | — | 14px / 1.65 / soft (tab-body) | — | — | **Consistent** | `14px/400/#4a4a4a/1.7` |

---

## SPACING

| Token / Purpose | PDP v36 HTML | DS v1.0 HTML | Homepage :root (docs/06) | pdp-styles.css | docs/03 | docs/04 | Drift Type | Recommended Canonical |
|-----------------|-------------|--------------|--------------------------|----------------|---------|---------|------------|----------------------|
| sp-1 | — | 4px (space-1) | 4px (--sp-1) | — | 4px | — | **Consistent** | `4px` |
| sp-2 | — | 8px (space-2) | 8px (--sp-2) | — | 8px | — | **Consistent** | `8px` |
| sp-3 | — | 12px (space-3) | 12px (--sp-3) | — | 12px | — | **Consistent** | `12px` |
| sp-4 | — | 16px (space-4) | 16px (--sp-4) | — | 16px | — | **Consistent** | `16px` |
| sp-5 | — | 20px (space-5) | 24px (--sp-5) | — | 24px | — | **Implementation drift** — DS v1.0 defines space-5 as 20px; Homepage :root --sp-5 = 24px | **Architect decision.** DS v1.0: 20px; :root: 24px (different scale systems) |
| sp-6 | — | 24px (space-6) | 32px (--sp-6) | — | 32px | — | **Implementation drift** — DS v1.0 space-6=24px; :root --sp-6=32px | Different naming systems; document both |
| sp-7 | — | — | 48px (--sp-7) | — | 48px | — | **Consistent** | `48px` |
| sp-8 | — | 32px (space-8) | 64px (--sp-8) | — | 64px | — | **Implementation drift** — DS v1.0 space-8=32px; :root --sp-8=64px | Different naming systems |
| sp-9 | — | — | 96px (--sp-9) | — | 96px | — | **Consistent** | `96px` |
| sp-10 | — | 40px (space-10) | 128px (--sp-10) | — | 128px | — | **Implementation drift** — DS v1.0 space-10=40px; :root --sp-10=128px | Different naming systems; DS v1.0 has more granular 4px-based scale |
| Hero padding (desktop) | 64px 40px | — | — | 32px 32px 80px | — | — | **Implementation drift** — PDP v36 = 64px vert 40px horiz; pdp-styles = 32px sides | `64px 40px` (PDP v36 wins) |
| Hero gap (gallery/buy) | 64px | — | — | 64px | — | — | **Consistent** | `64px` |
| Section padding (desktop) | 64px 40px (standard); 80px 40px (FAQ); 56px 40px (newsletter) | 72px 80px | — | 96px 32px | — | — | **Implementation drift** — multiple values across sources | PDP standard: `64px 40px`; PDP FAQ: `80px 40px` |
| Section padding (mobile) | 48px 16px; 32px 16px (hero) | 48px 24px | — | — | — | — | **Consistent** pattern | PDP mobile: `48px 16px` |
| Product card image margin-bottom | 26px (inline) | 26px | — | 14px (vcard__media) | — | — | **Implementation drift** — PDP v36 = 26px; pdp-styles = 14px | `26px` (PDP v36 wins) |
| Product card name mb | 3px (inline) | 3px | — | 2px (vcard__title) | — | — | **Consistent** (near-identical) | `3px` |
| Product card type mb | 8px (inline) | 8px | — | — | — | — | **Consistent** | `8px` |
| Product card size badge mb | 10px (inline) | 10px | — | — | — | — | **Consistent** | `10px` |
| Product card price mb | 12px (inline) | 12px | — | — | — | — | **Consistent** | `12px` |
| Max-width content | 1200px (section__inner) | — | 1320px (au-doc) | 1440px | — | — | **PDP-specific** — PDP v36 section content = 1200px; pdp-styles container = 1440px | PDP content: `1200px`; PDP full-width container: `1440px` |
| Max-width hero | 1400px | — | — | 1440px | — | — | **Implementation drift** — PDP v36 = 1400px; pdp-styles = 1440px | `1400px` (PDP v36 wins) |

---

## RADIUS

| Token / Purpose | PDP v36 HTML | DS v1.0 HTML | Homepage :root (docs/06) | pdp-styles.css | docs/03 | docs/04 | Drift Type | Recommended Canonical |
|-----------------|-------------|--------------|--------------------------|----------------|---------|---------|------------|----------------------|
| Primary CTA button | 6px | — | 0px (--btn-radius) | 0px (no radius) | 0px | 0px | **PDP-specific** — PDP v36 uses 6px radius on CTA; all other sources specify 0px (square) | **Architect decision required.** PDP v36 evolved to 6px; docs/Homepage mandate 0px |
| Gallery hero image | 8px | — | — | — | — | — | **Undocumented** | `8px` (PDP v36-specific) |
| Review card | 12px | 6px (color swatch card) | — | — | — | 2-4px max (matured) | **PDP-specific** — PDP v36 review cards = 12px radius | `12px` for review cards (PDP v36 specific) |
| Justifier card | 12px | — | — | — | — | — | **Undocumented** | `12px` |
| Value comparison card | 12px (inline) | — | — | — | — | — | **Undocumented** | `12px` |
| Motion video | 8px | — | — | — | — | — | **Undocumented** | `8px` |
| Badge (product type) | 3px | — | — | — | — | — | **Undocumented** | `3px` |
| Size badge pill | 20px | — | — | — | — | — | **Undocumented** | `20px` |
| Newsletter input/button | 4px | — | — | — | — | — | **Undocumented** | `4px` |
| Size selector button | 6px (inline) | — | 0px (--btn-radius) | 0px | 0px | 0px | **PDP-specific** — PDP v36 = 6px; all docs = 0px | **Architect decision required.** Same as CTA radius decision |
| LE badge (swatch overlay) | 2px | — | — | 2px | — | — | **Consistent** | `2px` |
| LE badge (card overlay) | 1px | — | — | 0px | — | — | **Implementation drift** — PDP v36 = 1px; pdp-styles = 0px | `1px` (PDP v36 wins) |

---

## BUTTONS

| Token / Purpose | PDP v36 HTML | DS v1.0 HTML | Homepage :root (docs/06) | pdp-styles.css | docs/03 | docs/04 | Drift Type | Recommended Canonical |
|-----------------|-------------|--------------|--------------------------|----------------|---------|---------|------------|----------------------|
| Primary CTA bg | `#1c1916` | `#1c1916` | `#050505` (--br-button) | `var(--br-text)` = `#050505` | `#050505` | `#050505` | **PDP-specific** — matches primary text divergence | Match text color decision |
| Primary CTA text | `#fff` | `#fff` | `#ffffff` (--br-button-text) | `#fff` | `#ffffff` | white | **Consistent** | `#ffffff` |
| Primary CTA hover bg | `#c45c3f` | `#c45c3f` | — | opacity 0.88 (no color change) | — | — | **PDP-specific** — PDP v36 changes to terracotta on hover; pdp-styles just reduces opacity | `#c45c3f` hover (PDP v36 wins) |
| Primary CTA padding | 18px (all sides) | 18px (all sides) | 14px y / 28px x | 18px | 14px y / 28px x | 14px y / 28px x | **PDP-specific** — PDP CTA is full-width with 18px padding; docs specify 14px/28px for standard buttons | PDP hero CTA: `18px` (full-width); standard buttons: `14px y / 28px x` |
| Primary CTA font-size | 16px | 16px | 14px (--btn-text-size) | 14px / 0.12em / uppercase | 14px | 14px | **PDP-specific** — PDP v36 hero CTA = 16px/600; standard system = 14px/600 | PDP hero CTA: `16px/600`; standard: `14px/600/uppercase` |
| Primary CTA font-weight | 600 | 600 | 600 (--btn-weight) | 700 / 0.12em / uppercase | 600 | 600 | **Implementation drift** — pdp-styles uses 700 weight + uppercase; PDP v36/DS = 600 sentence | PDP hero: `600`; pdp-styles CTA (older): `700/uppercase` |
| Primary CTA letter-spacing | — (none) | 0.02em | 0.06em (--btn-letter) | 0.12em | 0.06em | 0.06em | **PDP-specific** — PDP v36 has no letter-spacing; DS v1.0 = 0.02em; docs/Homepage = 0.06em | PDP hero CTA: none; standard buttons: `0.06em` |
| Primary CTA text-transform | none (sentence case) | none | uppercase | uppercase | — | — | **PDP-specific** — PDP v36 CTA = sentence ("Add to cart · $74"); other contexts = uppercase | PDP hero: sentence case; standard buttons: uppercase |
| Primary CTA border-radius | 6px | 6px | 0px | 0px | 0px | 0px | **PDP-specific** — see RADIUS section | **Architect decision required** |
| Primary CTA width | 100% | 100% (max-width 360px in demo) | — | — | — | — | **Consistent** for hero CTA | `width: 100%` (hero context) |
| Text CTA (Add to Cart →) | 15px / 600 / #1c1916 / border-bottom 1.5px solid #9a9182 | 15px / 600 / #1c1916 / border-bottom 1.5px solid #9a9182 | — | — | — | — | **Consistent** | `15px/600/#1c1916/underline 1.5px #9a9182` |
| Text CTA (Notify Me →) | 13px / 500 / #9a9182 / border-bottom 1px solid #d0c8be | 13px / 500 / #9a9182 / border-bottom 1px solid #d0c8be | — | — | — | — | **Consistent** | `13px/500/#9a9182/underline 1px #d0c8be` |
| Newsletter button | 14px / 600 / #1c1916 bg / uppercase / 0.05em / radius 4px | — | — | 11.5px / 700 / 0.12em / uppercase / no radius | — | — | **Implementation drift** | `14px/600/uppercase/0.05em/radius 4px` (PDP v36 wins) |

---

## CARDS

| Token / Purpose | PDP v36 HTML | DS v1.0 HTML | Homepage :root (docs/06) | pdp-styles.css | docs/03 | docs/04 | Drift Type | Recommended Canonical |
|-----------------|-------------|--------------|--------------------------|----------------|---------|---------|------------|----------------------|
| Product card border | none | none | — | none (default); 1px solid line (bordered variant) | — | — | **Consistent** | No border (default) |
| Product card shadow | none | none | — | none | — | — | **Consistent** | None |
| Product card image bg | `#f5f2ec` (inline) | `#f5f2ec` | — | repeating gradient pattern | — | — | **PDP-specific** — PDP v36 uses solid #f5f2ec; pdp-styles uses hatched placeholder | `#f5f2ec` solid |
| Product card image ratio | 1:1 | 1:1 | — | 1:1 | — | — | **Consistent** | `1:1` |
| Product card hover | scale(1.04) / 0.45s ease (inline) | — | — | — | — | scale 1.02 / 320ms | **Implementation drift** — PDP v36 = 1.04/0.45s; docs/04 = 1.02/320ms | `scale(1.04) / 0.45s ease` (PDP v36 wins) |
| Review card border | 1px solid #e6e6e6 | — | — | 1px solid var(--br-line) | — | — | **Consistent** | `1px solid #e6e6e6` |
| Review card radius | 12px | — | — | 0px (grid, no radius) | — | — | **PDP-specific** — PDP v36 review cards have 12px radius; pdp-styles reviews have 0 | `12px` (PDP v36 wins) |
| Review content padding | 28px | — | — | 24px 32px | — | — | **Implementation drift** | `28px` (PDP v36 wins) |
| Justifier card | padding 32px / radius 12px / border-left 5px solid #c45c3f | — | — | — | — | — | **Undocumented** | `padding:32px; radius:12px; border-left:5px solid #c45c3f` |
| Value comparison card | padding 32px / radius 12px / border 1px solid #e6e6e6 | — | — | — | — | — | **Undocumented** | `padding:32px; radius:12px; border:1px solid #e6e6e6` |

---

## INPUTS

| Token / Purpose | PDP v36 HTML | DS v1.0 HTML | Homepage :root (docs/06) | pdp-styles.css | docs/03 | docs/04 | Drift Type | Recommended Canonical |
|-----------------|-------------|--------------|--------------------------|----------------|---------|---------|------------|----------------------|
| Newsletter input padding | 12px 16px | — | — | 12px 14px (footer) | — | — | **Consistent** (near-identical) | `12px 16px` |
| Newsletter input border | 1px solid #d6cfc0 | — | — | 1px solid var(--br-text) (footer) | — | — | **PDP-specific** — PDP v36 uses warm border; pdp-styles footer uses ink border | PDP: `1px solid #d6cfc0` |
| Newsletter input radius | 4px | — | — | 0px (footer) | — | — | **PDP-specific** | `4px` (PDP v36 wins) |
| Newsletter input font | 14px / #1c1916 | — | — | 13px / var(--br-text) | — | — | **Implementation drift** | `14px/#1c1916` (PDP v36 wins) |
| Newsletter placeholder | #9a9182 | — | — | var(--br-text-mute) = #8a8a8a | — | — | **PDP-specific** | `#9a9182` |
| Size selector padding | 14px | — | — | 12px 4px (standard); 16px 12px (wide) | — | — | **Implementation drift** | `14px` (PDP v36 wins) |
| Size selector border | 1px solid #e6e6e6 (inactive); 2px solid #1c1916 (active) | — | — | 1px solid var(--br-text) (all) | — | — | **PDP-specific** — PDP v36 uses light border inactive; pdp-styles uses ink border all | PDP v36 pattern: inactive = `1px #e6e6e6`; active = `2px #1c1916` |
| Size selector radius | 6px | — | — | 0px | — | — | **PDP-specific** | See radius decision above |
| Size selector active bg | #f9f9f9 | — | — | var(--br-text) = #050505 (filled) | — | — | **Implementation drift** — PDP v36 uses subtle grey active; pdp-styles fills with ink | `#f9f9f9` subtle active (PDP v36 wins) |

---

## ICONS

| Token / Purpose | PDP v36 HTML | DS v1.0 HTML | Homepage :root (docs/06) | pdp-styles.css | docs/03 | docs/04 | Drift Type | Recommended Canonical |
|-----------------|-------------|--------------|--------------------------|----------------|---------|---------|------------|----------------------|
| Accordion expand icon | `+` text character | `+` text character | — | `+` via ::after pseudo | — | Chevron/arrow | **Documentation drift** — docs/04 says "chevron/arrow"; all implementations use `+`/`−` text | `+` / `−` text characters |
| FAQ expand icon | `▼` / `▲` character | — | — | `+` / `−` via ::after | — | — | **Implementation drift** — PDP v36 FAQ uses ▼/▲; pdp-styles uses +/− | `+` / `−` (DS v1.0 and pdp-styles pattern) |
| Star rating | `★` (Unicode U+2605) | `★` (Unicode U+2605) | — | text characters | — | 5★ | **Consistent** | Unicode `★` characters |
| Trust checkmark | `✓` bold text | — | — | `✓` via ::before | — | — | **Consistent** | `✓` text character |
| CTA arrow | `→` (Unicode) | `→` (Unicode) | — | — | — | → | **Consistent** | `→` |

---

## CONTAINERS

| Token / Purpose | PDP v36 HTML | DS v1.0 HTML | Homepage :root (docs/06) | pdp-styles.css | docs/03 | docs/04 | Drift Type | Recommended Canonical |
|-----------------|-------------|--------------|--------------------------|----------------|---------|---------|------------|----------------------|
| Hero max-width | 1400px | — | 1320px (au-doc) | 1440px | — | — | **Implementation drift** — three different max-widths | PDP hero: `1400px`; pdp-styles: `1440px` (wider for full page) |
| Section inner max-width | 1200px | — | — | 1440px | — | — | **PDP-specific** — PDP v36 content = 1200px; pdp-styles full = 1440px | Content: `1200px`; Full container: `1440px` |
| FAQ container | 760px | — | — | 880px | — | — | **Implementation drift** — PDP v36 = 760px; pdp-styles = 880px | `760px` (PDP v36 wins) |
| Newsletter container | 600px | — | — | — | — | — | **Undocumented** | `600px` |
| Brand section | 1240px (inline) | — | — | — | — | — | **Undocumented** | `1240px` |
| DS v1.0 content width | — | 1200px (max-content) | — | — | — | 1200px centered | **Consistent** | `1200px` |
| Side margins (desktop) | 40px | 80px (DS chrome) | 32px (pdp-styles) | 32px | — | 40px | **Implementation drift** | PDP v36: `40px`; pdp-styles: `32px` |
| Side margins (mobile) | 16px | 24px | — | — | — | 16px | **Consistent** for PDP | PDP mobile: `16px` |

---

## GRID

| Token / Purpose | PDP v36 HTML | DS v1.0 HTML | Homepage :root (docs/06) | pdp-styles.css | docs/03 | docs/04 | Drift Type | Recommended Canonical |
|-----------------|-------------|--------------|--------------------------|----------------|---------|---------|------------|----------------------|
| Hero layout (desktop) | 1fr 1fr / gap 64px | — | — | 1fr 1fr / gap 64px | — | — | **Consistent** | `grid: 1fr 1fr / gap 64px` |
| Hero layout (mobile) | 1fr / gap 32px | — | — | 1fr / gap 32px | — | — | **Consistent** | `grid: 1fr / gap 32px` |
| Product grid (desktop) | repeat(4, 1fr) / col-gap 28px / row-gap 60px | repeat(4, 1fr) / gap 28px | — | repeat(4, 1fr) / gap 24px | — | 4 cols / 28px col, 60px row | **Implementation drift** — pdp-styles uses 24px gap; PDP v36 = 28px col + 60px row | `repeat(4, 1fr) / col-gap 28px / row-gap 60px` (PDP v36 wins) |
| Product grid (tablet) | repeat(2, 1fr) | — | — | repeat(2, 1fr) | — | 3 cols / 20px | **Implementation drift** — DS v1.0 tablet = 3 cols; PDP v36 = 2 cols at 1024px | PDP: 2 cols at ≤1024px |
| Product grid (mobile) | repeat(2, 1fr) / gap 16px | — | — | — | — | 2 cols / 16px | **Consistent** | `repeat(2, 1fr) / gap 16px` |
| Benefits grid (desktop) | repeat(3, 1fr) / gap 40px | — | — | repeat(3, 1fr) / gap 20px | — | — | **Implementation drift** — PDP v36 = 40px gap; pdp-styles = 20px | `repeat(3, 1fr) / gap 40px` (PDP v36 wins) |
| Review grid | repeat(3, 1fr) / gap 32px | — | — | repeat(2, 1fr) / gap 0 (bordered) | — | 2-3 col | **PDP-specific** — PDP v36 = 3-col card grid; pdp-styles = 2-col bordered list | `repeat(3, 1fr) / gap 32px` (PDP v36 card design) |
| Justifier grid | repeat(2, 1fr) / gap 40px | — | — | — | — | — | **Undocumented** | `repeat(2, 1fr) / gap 40px` |
| Motion grid | repeat(3, 1fr) / gap 32px | — | — | — | — | — | **Undocumented** | `repeat(3, 1fr) / gap 32px` |
| Value comparison | repeat(3, 1fr) / gap 40px | — | — | 1fr 1.1fr / gap 64px | — | 2 col (dark) | **Implementation drift** — PDP v36 = 3 column cards; pdp-styles = 2 col split | `repeat(3, 1fr) / gap 40px` (PDP v36 wins) |
| Brand section grid | 1fr 1fr / gap 64px 80px | — | — | — | — | — | **Undocumented** | `1fr 1fr / gap 64px 80px` |

---

## SHADOWS

| Token / Purpose | PDP v36 HTML | DS v1.0 HTML | Homepage :root (docs/06) | pdp-styles.css | docs/03 | docs/04 | Drift Type | Recommended Canonical |
|-----------------|-------------|--------------|--------------------------|----------------|---------|---------|------------|----------------------|
| All elements | None used | None used | None used | None used | None / no drop shadows | No shadows | **Consistent** | No shadows anywhere |

---

## ANIMATIONS

| Token / Purpose | PDP v36 HTML | DS v1.0 HTML | Homepage :root (docs/06) | pdp-styles.css | docs/03 | docs/04 | Drift Type | Recommended Canonical |
|-----------------|-------------|--------------|--------------------------|----------------|---------|---------|------------|----------------------|
| Card image hover | `transform: scale(1.04)` / `transition: transform 0.45s ease` | `transform: scale(1.04)` / `transition: 0.45s ease` | — | — | hover scale 1.02 / 320ms | scale 1.02 / 320ms ease-out | **PDP-specific** — PDP v36/DS v1.0 = 1.04/0.45s; docs = 1.02/320ms (older value) | `scale(1.04) / 0.45s ease` |
| CTA hover transition | `transition: all 0.2s` (toggle btn); bg change on CTA | `transition: background 0.2s` | — | `transition: opacity 0.15s` | — | — | **Implementation drift** — PDP v36 = bg color change; pdp-styles = opacity | `background: #c45c3f; transition: background 0.2s` (PDP v36 wins) |
| Swatch transition | `transition: all 0.2s` | — | — | `transition: border-color 0.12s, transform 0.12s` | — | — | **Implementation drift** | `transition: all 0.2s` (PDP v36 simpler) |
| Color swatch hover | `border-color: #9a9182` | — | — | `transform: scale(1.06)` | — | — | **Implementation drift** — PDP v36 shows border; pdp-styles scales up | PDP v36: `border-color: #9a9182`; pdp-styles adds scale |
| Ticker animation | — | — | — | `opacity 0.55s ease, transform 0.55s ease` (slide transition) | opacity crossfade 320ms | 320ms ease | **Implementation drift** — pdp-styles ticker = 0.55s; docs say 320ms | `opacity 0.55s ease, transform 0.55s ease` (pdp-styles is actual implementation) |
| Tab activation | instant (no transition) | instant | — | `transition: background 0.12s, color 0.12s` (variant-tab) | — | — | **PDP-specific** — PDP v36 tab switch is instant; pdp-styles has 0.12s | Instant for type tabs; 0.12s for variant tabs |
| Scroll behavior | `scroll-behavior: smooth` on html | `scroll-behavior: smooth` on html | — | — | — | — | **Consistent** | `scroll-behavior: smooth` |
| Entrance animations | None | None | — | — | None | — | **Consistent** — explicitly no entrance animations | None |
| Card CTA hover | `letter-spacing: 0.06em` on hover (card-cta) | — | — | — | — | caption underline draws in | **PDP-specific** | `letter-spacing: 0.06em` on hover |

---

## BREAKPOINTS

| Token / Purpose | PDP v36 HTML | DS v1.0 HTML | Homepage :root (docs/06) | pdp-styles.css | docs/03 | docs/04 | Drift Type | Recommended Canonical |
|-----------------|-------------|--------------|--------------------------|----------------|---------|---------|------------|----------------------|
| Mobile max | 768px | 900px (sidebar hides) | — | 700px (gallery reflow) | — | < 768px | **Implementation drift** — PDP v36 breaks at 768px; pdp-styles gallery at 700px; DS v1.0 sidebar at 900px | PDP mobile: `768px`; Gallery: `700px` |
| Tablet max | 1024px | — | — | 1000px (main grid reflow) | — | 768–1023px | **Implementation drift** — PDP v36 = 1024px; pdp-styles = 1000px | `1024px` (PDP v36 wins) |
| Laptop | — | — | — | — | — | 1024–1279px | **Docs-only (not implemented)** | Document for DS v1.0 reference |
| Desktop min | 1024px+ | 900px+ | — | 1000px+ | — | 1280px+ | **Implementation drift** | PDP desktop: `1024px+` |
| Wide | — | — | — | — | — | 1440px+ | **Docs-only** | Reference only |
| Mobile breakpoint (pdp-styles) | — | — | — | 520px (benefit 1-col); 600px (ticker); 700px (gallery); 800px (benefits 2-col, pillars) | — | — | **Undocumented** in main docs | Additional pdp-styles breakpoints at 520, 600, 700, 800px |

---

## COMPONENT BEHAVIORS

| Token / Purpose | PDP v36 HTML | DS v1.0 HTML | Homepage :root (docs/06) | pdp-styles.css | docs/03 | docs/04 | Drift Type | Recommended Canonical |
|-----------------|-------------|--------------|--------------------------|----------------|---------|---------|------------|----------------------|
| Gallery sticky | `position: sticky; top: 64px` | — | — | `position: sticky; top: 88px` | — | buy box sticky on scroll | **Implementation drift** — PDP v36 sticks at 64px; pdp-styles at 88px | `sticky; top: 64px` (PDP v36 wins) |
| Gallery mobile | `position: static` | — | — | `position: static` (≤700px) | — | — | **Consistent** | `position: static` on mobile |
| Swatch size | 23px content / 9px padding / content-box = 41px total tap | — | — | 36px / border-radius 50% | — | — | **Implementation drift** — PDP v36 = 23px+18px padding = ~41px; pdp-styles = 36px | PDP v36: `23px inner, 41px tap target`; pdp-styles: `36px` |
| Swatch selected | `border: 2px solid #1c1916` | — | — | `border-color: var(--br-text); box-shadow: inset 0 0 0 2px #fff` | — | — | **Implementation drift** — PDP v36 = border only; pdp-styles adds inset shadow | `border: 2px solid #1c1916` (PDP v36 simpler) |
| Thumbnail size | 72px × 72px | — | — | 88px column (grid) | — | — | **Implementation drift** — PDP v36 = 72px buttons below; pdp-styles = 88px sidebar | `72px` inline row (PDP v36 wins) |
| Thumbnail active | `border: 2px solid #1c1916` | — | — | `border-color: var(--br-text)` | — | — | **Consistent** | `2px solid #1c1916` |
| Thumbnail inactive | `border: 1px solid #e6e6e6` | — | — | `border: 1px solid transparent` | — | — | **Implementation drift** — PDP v36 shows light border; pdp-styles = transparent | `1px solid #e6e6e6` (PDP v36 visible border) |
| FAQ open behavior | toggle data-open attr | — | — | native `<details>` element | — | one open at a time / 200ms | **Implementation drift** — PDP v36 uses custom JS; pdp-styles uses native details; docs say one-at-a-time | PDP v36: custom toggle; pdp-styles: native `<details>` |
| Accordion behavior | native `<details>` (multiple open) | native `<details>` | — | native `<details>` | one open at a time / 200ms | one open at a time | **Documentation drift** — docs say one-at-a-time; all implementations allow multiple open | Native `<details>` (multiple open OK) — docs are aspirational |
| Header sticky | — | — | — | `position: sticky; top: 0; z-index: 30` | sticky on scroll | sticky | **Consistent** | `position: sticky; top: 0` |
| Product card hover effect | `transform: scale(1.04)` via JS onmouseenter | `scale(1.04)` via CSS | — | — | 1.02x | 1.02x / 320ms | **PDP-specific** — JS-driven 1.04x in PDP v36 vs CSS in DS v1.0 | CSS `transform: scale(1.04); transition: 0.45s ease` |

---

## SUMMARY OF CRITICAL ARCHITECT DECISIONS REQUIRED

| # | Decision | Option A (PDP v36 / DS v1.0) | Option B (Homepage / docs) | Impact |
|---|----------|-------------------------------|---------------------------|--------|
| 1 | Primary text color | `#1c1916` (warm charcoal) | `#050505` (near-black) | Affects all headings, nav, CTAs sitewide |
| 2 | Accent color | `#c45c3f` (terracotta) — used for hover, badges, accent | `#f97250` (coral) — restricted to cart badge only | Fundamentally different accent philosophy |
| 3 | Star rating color | `#d4af37` (antique gold) | `#fbc02d` (bright gold) | Visual weight of social proof |
| 4 | Button border-radius | `6px` (PDP v36 evolved value) | `0px` (square, per docs) | Feel: rounded-premium vs sharp-editorial |
| 5 | Eyebrow spec | `11px / 700 / 0.08em` (PDP v36) | `12px / 700 / 0.14em` (Homepage) | Type scale consistency |
| 6 | Spacing scale naming | DS v1.0 granular (space-1=4, space-5=20, space-8=32…) | :root compact (sp-5=24, sp-8=64…) | Token naming convention |

---

## UNDOCUMENTED TOKENS (exist in implementation, absent from all docs/)

| Token | Value | Source | Category |
|-------|-------|--------|----------|
| Tab inactive color | `#7a7268` | PDP v36, DS v1.0 | Typography |
| Tab disabled color | `#b0a898` | PDP v36, DS v1.0 | Typography |
| Warm divider | `#d6cfc0` | PDP v36 | Colors |
| Inactive button bg | `#f0efec` | DS v1.0 | Colors |
| Size badge bg | `#ece9e3` | DS v1.0, PDP v36 | Colors |
| Brand section max-width | `1240px` | PDP v36 | Containers |
| Newsletter container | `600px` | PDP v36 | Containers |
| Justifier card specs | `padding:32px; radius:12px; border-left:5px #c45c3f` | PDP v36 | Cards |
| Motion video radius | `8px` | PDP v36 | Radius |
| Gallery image radius | `8px` | PDP v36 | Radius |
| Product swatch colors (12) | See swatch table above | PDP v36 | Product data |
| Value comparison 3-col layout | `repeat(3,1fr) / gap 40px` | PDP v36 | Grid |
| Supporting text #5a5248 | `#5a5248` | PDP v36 inline | Colors |
| CTA hover letter-spacing | `0.06em` | PDP v36 | Animations |

---

## DOCS-ONLY VALUES (appear in docs but NOT in matured implementations)

| Token | Value | Source | Category | Notes |
|-------|-------|--------|----------|-------|
| docs/04 text-soft | `#6a6a6a` | docs/04 | Colors | All implementations use #4a4a4a |
| docs/04 text-mute | `#999999` | docs/04 | Colors | All implementations use #8a8a8a |
| docs/04 border | `#e5e2db` | docs/04 | Colors | All implementations use #e6e6e6 |
| docs/04 alt-bg | `#f9f7f2` | docs/04 | Colors | Homepage uses #f9f9f9; PDP uses #f5f2ec |
| docs/04 card hover 1.02x/320ms | scale 1.02 / 320ms | docs/04 | Animations | PDP v36 uses 1.04x / 0.45s |
| docs/03 JetBrains Mono | JetBrains Mono | docs/03 | Typography | Not used in any matured HTML |
| docs/04 accordion one-at-a-time | exclusive open | docs/04 | Behavior | All implementations allow multiple |
| DS v1.0 wide breakpoint 1440px+ | 1440px+ | DS v1.0 | Breakpoints | Not implemented in CSS |
| DS v1.0 laptop breakpoint 1024-1279px | specific range | DS v1.0 | Breakpoints | PDP uses simpler 768/1024 breaks |

---

## PARALLEL DESIGN SYSTEMS SUMMARY

The matured implementations reveal **two coexisting design directions** that have not been reconciled:

### Direction A: "PDP Editorial" (PDP v36 + DS v1.0 HTML)
- Primary: `#1c1916` (warm charcoal)
- Accent: `#c45c3f` (terracotta) — used freely for hover, badges, borders
- Stars: `#d4af37` (antique gold)
- Warm backgrounds: `#f5f2ec`
- Buttons: `6px radius`, sentence case, 16px
- Cards: 12px radius on review/justifier cards
- Gallery: 8px radius
- Feel: warm, rounded, editorial-magazine

### Direction B: "Homepage Matured" (Homepage :root + pdp-styles.css + docs/03-04)
- Primary: `#050505` (near-black ink)
- Accent: `#f97250` (coral) — **restricted to cart badge ONLY**
- Stars: `#fbc02d` (bright gold)
- Neutral backgrounds: `#f9f9f9`
- Buttons: `0px radius`, uppercase, 14px, high letter-spacing
- Cards: 0px radius
- Feel: sharp, minimal, Acne Studios / editorial-restrained

**The PDP v36 and DS v1.0 HTML are the newest matured artifacts and represent the evolved direction. The Homepage :root tokens and docs/ represent the earlier matured direction that preceded the PDP editorial evolution.**
