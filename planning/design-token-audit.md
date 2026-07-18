# Design Token Audit

**Status:** INVENTORY — requires Architect decisions on all flagged items  
**Sources audited:**
1. `docs/06-HOMEPAGE-ARCHITECTURE.md` lines 38–112 (CSS `:root` tokens)
2. `docs/04-COMPONENT-LIBRARY.md` lines 8–55 (Core Design System)
3. `docs/03-DESIGN-SYSTEM.md` lines 364–385 (Research Bible rules)
4. `docs/05-PDP-ARCHITECTURE.md` lines 20–100 (PDP CSS)

**Legend:**  
🔴 = Inconsistency (same purpose, different values across sources)  
🟡 = Duplicate (same value, different name)  
✅ = Consistent across all sources

---

## COLORS

### Brand / UI Colors

| Token / Name | Hex Value | Source(s) | Consistent? |
|---|---|---|---|
| `--br-bg` | `#ffffff` | Homepage :root | ✅ All sources agree |
| Background | `#ffffff` | Component Library, Research Bible | ✅ |
| `--br-alt-bg` | `#f9f9f9` | Homepage :root | 🔴 See below |
| Alt background | `#f9f7f2` | Component Library | 🔴 **Conflict:** cool grey vs warm grey |
| `--br-alt-bg-2` | `#f3f3f3` | Homepage :root | No equivalent elsewhere |
| `--br-text` | `#050505` | Homepage :root | 🔴 See below |
| Text (primary) | `#050505` | Component Library, Research Bible | ✅ (these three agree) |
| body color | `#1c1916` | PDP CSS | 🔴 **Conflict:** PDP uses warm black `#1c1916` instead of `#050505` |
| `--br-text-soft` | `#4a4a4a` | Homepage :root | 🔴 See below |
| Text (soft) | `#6a6a6a` | Component Library | 🔴 **Conflict:** `#4a4a4a` vs `#6a6a6a` |
| PDP soft text | `#6b645a` | PDP CSS | 🔴 **Third value** — warm-tinted soft |
| `--br-text-mute` | `#8a8a8a` | Homepage :root | 🔴 See below |
| Text (muted) | `#999999` | Component Library | 🔴 **Conflict:** `#8a8a8a` vs `#999999` |
| `--br-line` | `#e6e6e6` | Homepage :root | 🔴 See below |
| `--br-line-soft` | `#efefef` | Homepage :root | No equivalent elsewhere |
| Line (border) | `#e5e2db` | Component Library | 🔴 **Conflict:** cool `#e6e6e6` vs warm `#e5e2db` |
| PDP border | `#d6cfc0` | PDP CSS | 🔴 **Third border value** — darker warm |
| `--br-accent` | `#f97250` | Homepage :root | 🔴 See below |
| Accent (coral) | `#f97250` | Component Library, Research Bible | ✅ (these three agree) |
| PDP badge/accent | `#c45c3f` | PDP CSS | 🔴 **Conflict:** PDP uses darker `#c45c3f` instead of `#f97250` |
| `--br-accent-hover` | `#e85e3c` | Homepage :root | Only defined in :root |
| `--br-coral` | `var(--br-accent)` | Homepage :root | 🟡 Alias of `--br-accent` |
| `--br-sale` | `var(--br-text)` | Homepage :root | 🟡 Alias of `--br-text` |
| `--br-star` | `#fbc02d` | Homepage :root | 🔴 See below |
| Star (rating) | `#fbc02d` | Component Library, Research Bible | ✅ (these three agree) |
| PDP stars | `#d4af37` | PDP CSS | 🔴 **Conflict:** `#fbc02d` vs `#d4af37` |
| `--br-info` | `#3a8de8` | Homepage :root | Only in :root |
| `--br-le` | `#3a8de8` | Homepage :root | 🟡 Duplicate of `--br-info` |
| `--br-le-bg` | `#eaf3fc` | Homepage :root | Only in :root |
| `--br-button` | `#050505` | Homepage :root | ✅ Matches primary text |
| `--br-button-text` | `#ffffff` | Homepage :root | ✅ |
| PDP CTA bg | `#1c1916` | PDP CSS | 🔴 Uses PDP text color, not `--br-button` |
| PDP CTA hover | `#c45c3f` | PDP CSS | 🔴 PDP buttons change to coral on hover; no hover color change in design system |
| PDP FAQ bg | `#f5f2ec` | PDP CSS | Unique — warm-tinted section bg |
| PDP swatch border | `#9a9182` | PDP CSS | Unique — warm grey |
| PDP placeholder | `#9a9182` | PDP CSS | 🟡 Same as swatch border |

### Audit-Only Colors (not in components — ignore for production)

| Token | Hex Value | Source |
|---|---|---|
| `--au-bg` | `#fafaf7` | Homepage :root |
| `--au-card` | `#ffffff` | Homepage :root |
| `--au-flag` | `#c43d2a` | Homepage :root |
| `--au-flag-bg` | `#fdf0ec` | Homepage :root |
| `--au-ok` | `#1f6f4a` | Homepage :root |
| `--au-ok-bg` | `#ecf6f0` | Homepage :root |
| `--au-note` | `#6b5b3a` | Homepage :root |
| `--au-note-bg` | `#fbf5e6` | Homepage :root |

### Dark Section Colors (from Component Library component specs)

| Value | Where Used | Notes |
|---|---|---|
| `#1a1a1a` | Sock Math dark bg | Documented in component spec |
| `var(--m-dark)` | Manifesto, Founder Letter, Closing Statement, Credibility | CSS variable referenced but not defined in :root |
| `var(--m-bg)` | Product Grid bg | Referenced but not defined in :root |
| `var(--m-accent)` | Problem Section strikethrough | Referenced but not defined in :root |

### Color Inconsistency Summary

| Purpose | Homepage :root | Component Library | Research Bible | PDP CSS | Values |
|---|---|---|---|---|---|
| Primary text | `#050505` | `#050505` | `#050505` | `#1c1916` | **2 values** |
| Soft text | `#4a4a4a` | `#6a6a6a` | — | `#4a4a4a` / `#6b645a` | **3 values** |
| Muted text | `#8a8a8a` | `#999999` | — | `#8a8a8a` | **2 values** |
| Accent | `#f97250` | `#f97250` | `#f97250` | `#c45c3f` | **2 values** |
| Star/gold | `#fbc02d` | `#fbc02d` | `#fbc02d` | `#d4af37` | **2 values** |
| Alt bg | `#f9f9f9` | `#f9f7f2` | — | `#f5f2ec` / `#f9f9f9` | **3 values** |
| Border | `#e6e6e6` | `#e5e2db` | — | `#d6cfc0` | **3 values** |

> **Recommendation (requires Architect decision):** The Homepage :root tokens and Research Bible agree on a cool-neutral palette. The Component Library leans warm. The PDP is fully warm-tinted and uses a completely different primary black (`#1c1916`). The Architect must decide: adopt the :root cool palette everywhere, or shift to the warm PDP palette, or standardize a middle-ground.

---

## SPACING

### Spacing Scale (from :root)

| Token | Value | Source |
|---|---|---|
| `--sp-1` | `4px` | Homepage :root |
| `--sp-2` | `8px` | Homepage :root |
| `--sp-3` | `12px` | Homepage :root |
| `--sp-4` | `16px` | Homepage :root |
| `--sp-5` | `24px` | Homepage :root |
| `--sp-6` | `32px` | Homepage :root |
| `--sp-7` | `48px` | Homepage :root |
| `--sp-8` | `64px` | Homepage :root |
| `--sp-9` | `96px` | Homepage :root |
| `--sp-10` | `128px` | Homepage :root |

### Ad-hoc Spacing Values (not using tokens)

| Value | Where Used | Closest Token |
|---|---|---|
| `14px` | Button padding-y | Between `--sp-3` (12px) and `--sp-4` (16px) — **off-scale** |
| `18px` | PDP FAQ item padding, PDP CTA padding-y | **Off-scale** |
| `20px` | PDP card gap, product grid internal padding, footer column gap | Between `--sp-4` (16px) and `--sp-5` (24px) — **off-scale** |
| `22px` | Variants button margin-top, assoc strip mark spacing | **Off-scale** |
| `28px` | Button padding-x, card gap, review card padding, section spacing | Between `--sp-5` (24px) and `--sp-6` (32px) — **off-scale** |
| `40px` | PDP section side padding, PDP grid gap, justifier gap | Between `--sp-6` (32px) and `--sp-7` (48px) — **off-scale** |
| `56px` | PDP newsletter padding, footer padding, credibility padding, assoc padding | Between `--sp-7` (48px) and `--sp-8` (64px) — **off-scale** |
| `72px` | 50/50 split copy side padding | Between `--sp-7` (48px) and `--sp-9` (96px) — **off-scale** |
| `76px` | Founder Letter vertical padding | **Off-scale** |
| `80px` | 50/50 split copy side padding, PDP FAQ padding | Between `--sp-8` (64px) and `--sp-9` (96px) — **off-scale** |
| `88px` | Closing Statement vertical padding | **Off-scale** |

### Section Padding Patterns

| Section | Desktop Padding | Mobile Padding | Source |
|---|---|---|---|
| PDP sections | `64px 40px` | — | PDP CSS |
| PDP FAQ | `80px 40px` | — | PDP CSS |
| PDP Newsletter | `56px 40px` | — | PDP CSS |
| 50/50 Split (copy) | `80px 72px` | height: auto | Research Bible |
| Manifesto | `96px` | `60px` | Component Library |
| Closing Statement | `88px` | `48px` | Component Library |
| Credibility | `56px` | — | Component Library |
| Founder Letter | `76px` | `48px` | Component Library |
| Problem Section | `64px` | — | Component Library |
| Product Grid | `64px` | — | Component Library |
| Footer | `56px` | — | Component Library |

> **Recommendation (requires Architect decision):** Many spacing values bypass the `--sp-*` scale. Either expand the token scale to include common breakpoints (14, 20, 28, 40, 56, 72, 76, 80, 88) or constrain component specs to use only existing tokens.

---

## RADIUS

| Value | Where Used | Source | Consistent with System? |
|---|---|---|---|
| `0px` | Buttons, product cards (default) | Homepage :root (`--btn-radius`), Component Library, Research Bible | ✅ **Canonical** |
| `2px` | "Where matured direction uses radius" | Component Library | ✅ Allowed |
| `4px` | "Where matured direction uses radius", PDP newsletter input/button | Component Library, PDP CSS | ✅ Allowed |
| `3px` | PDP badge | PDP CSS | 🔴 Not in allowed set (0/2/4) |
| `6px` | PDP CTA button | PDP CSS | 🔴 **Violates system** — buttons must be 0px |
| `8px` | PDP gallery hero, PDP motion video | PDP CSS | 🔴 Not in allowed set |
| `12px` | PDP review cards, PDP justifier cards | PDP CSS | 🔴 Not in allowed set |
| `50%` | PDP color swatches (circle) | PDP CSS | Special case — functional |

### Inconsistency Summary

The design system mandates `0px` default with `2px` or `4px` max. The PDP CSS uses `3px`, `6px`, `8px`, and `12px` extensively, violating the system in every section.

> **Recommendation (requires Architect decision):** Either update the design system to include a full radius scale (0, 2, 4, 8, 12) or strip all PDP radii back to 0/2/4. The `6px` CTA button radius directly contradicts the "buttons are square" rule in three separate source docs.

---

## TYPOGRAPHY

### Font Family

| Token / Property | Value | Source | Consistent? |
|---|---|---|---|
| `--t-font` | `'Roboto', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif` | Homepage :root | ✅ |
| Font | Roboto only (300–700) | Component Library | ✅ |
| Font | Roboto only (300–700), no Josefin Sans | Research Bible | ✅ |
| body font-family | `'Roboto', -apple-system, BlinkMacSystemFont, sans-serif` | PDP CSS | ✅ (shorter fallback) |

### Font Size Scale

| Token | Value | Source | PDP Equivalent |
|---|---|---|---|
| `--t-eyebrow` | `12px` | Homepage :root | — |
| `--t-body-sm` | `14px` | Homepage :root | — |
| `--t-body` | `16px` | Homepage :root | — |
| `--t-body-lg` / `--t-h6` | `18px` | Homepage :root | — |
| `--t-h5` | `22px` | Homepage :root | — |
| `--t-h4` | `28px` | Homepage :root | — |
| `--t-h3` | `36px` | Homepage :root | PDP newsletter title: `36px` ✅ |
| `--t-h2` | `44px` | Homepage :root | PDP buy name: `44px` ✅, PDP section title: `42px` 🔴 |
| `--t-h1` | `56px` | Homepage :root | — |
| `--t-display` | `72px` | Homepage :root | — |
| `--t-h1-mobile` | `36px` | Homepage :root | — |
| `--t-display-mobile` | `44px` | Homepage :root | — |

### Ad-hoc Font Sizes (not in token scale)

| Value | Where Used | Closest Token |
|---|---|---|
| `10px` | PDP badge, Credibility small caps | Below `--t-eyebrow` (12px) |
| `11px` | Section labels, benefit numbers, manifesto eyebrow, variant labels | Below `--t-eyebrow` (12px) |
| `11.5px` | Variant grid button | Below `--t-eyebrow` (12px) |
| `13px` | Nav text, price meta, color name, review author, footer links | Between `--t-eyebrow` (12px) and `--t-body-sm` (14px) |
| `15px` | PDP benefit sub, review text, newsletter desc, founder body, problem body | Between `--t-body-sm` (14px) and `--t-body` (16px) |
| `20px` | PDP benefit title, testimonial quote | Between `--t-body-lg` (18px) and `--t-h5` (22px) |
| `21px` | Product name, article headline | Between `--t-body-lg` (18px) and `--t-h5` (22px) |
| `24px` | Variant grid price | Between `--t-h5` (22px) and `--t-h4` (28px) |
| `26px` | Credibility logo bar, Founder opening quote min | Between `--t-h5` (22px) and `--t-h4` (28px) |
| `30px` | Problem headline min, Credibility headline min | Between `--t-h4` (28px) and `--t-h3` (36px) |
| `34px` | Closing Statement headline min | Between `--t-h6` (32px*) and `--t-h3` (36px) |
| `38px` | Manifesto headline min | Between `--t-h3` (36px) and `--t-h2` (44px) |
| `42px` | PDP section title | Between `--t-h3` (36px) and `--t-h2` (44px) 🔴 |
| `52px` | Credibility headline max | Between `--t-h2` (44px) and `--t-h1` (56px) |
| `60px` | Closing Statement headline max | Between `--t-h1` (56px) and `--t-display` (72px) |
| `92px` | Manifesto headline max | Above `--t-display` (72px) |

### Font Weight

| Value | Where Used | Source |
|---|---|---|
| `300` | Founder opening quote, Closing headline, Manifesto | Component Library |
| `400` | Product name, logo text, body text | Component Library, PDP CSS |
| `500` | PDP newsletter title, FAQ trigger, motion cap, price | PDP CSS |
| `600` | Eyebrows (:root), buttons, nav text, CTA | Homepage :root, Component Library |
| `700` | Eyebrows (Component Library), section labels, headings, buy name, price | Component Library, PDP CSS |

#### Eyebrow Font Weight Conflict

| Source | Weight |
|---|---|
| Homepage :root (comment) | `600` |
| Component Library | `700` |
| Research Bible | `700` |
| PDP section labels | `700` |

> 🔴 Homepage :root says eyebrows are `600`; all other sources say `700`.

### Letter Spacing

| Value | Where Used | Source | Consistent? |
|---|---|---|---|
| `0.05em` | PDP toggle buttons, PDP newsletter button | PDP CSS | 🔴 Not in any token |
| `0.06em` | Buttons | Homepage :root (`--btn-letter`), Component Library | ✅ |
| `0.08em` | Homepage :root eyebrow (comment), PDP section labels, PDP badge | Homepage :root, PDP CSS | 🔴 Conflicts with 0.14em |
| `0.14em` | Eyebrows | Component Library, Research Bible | 🔴 Conflicts with 0.08em |
| `0.18em` | Manifesto eyebrow | Component Library | 🔴 Third eyebrow value |

#### Eyebrow Letter-Spacing Conflict (Critical)

| Source | Letter-Spacing |
|---|---|
| Homepage :root (comment on `--t-eyebrow`) | `0.08em` |
| Component Library (Core Design System) | `0.14em` |
| Research Bible | `0.14em` |
| Manifesto component spec | `0.18em` |
| PDP section labels | `0.08em` |

> 🔴 **Three different eyebrow letter-spacing values.** Component Library and Research Bible agree on `0.14em`. Homepage :root and PDP use `0.08em`. Manifesto uses `0.18em`.

### Line Height

| Value | Where Used | Source |
|---|---|---|
| `1.08` | PDP buy name | PDP CSS |
| `1.15` | — | — |
| `1.2` | PDP section title | PDP CSS |
| `1.5` | Body (default) | PDP CSS (body rule) |
| `1.6` | PDP buy desc, benefit sub, FAQ body, newsletter desc | PDP CSS |
| `1.65` | Founder body text | Component Library |
| `1.7` | Review text, justifier quote | PDP CSS |

> **Recommendation (requires Architect decision):** Standardize on 2–3 line-height values (e.g., tight: 1.1, normal: 1.5, relaxed: 1.65) and apply consistently.

---

## ANIMATION / TRANSITION

| Property | Duration | Easing | Where Used | Source |
|---|---|---|---|---|
| Opacity crossfade | `320ms` | `ease` | General transitions | Component Library |
| Image scale hover | `320ms` | `ease-out` | Product cards, promo tiles | Component Library |
| Accordion height | `200ms` | — | PDP accordion | Component Library |
| Toggle cross-fade | `240ms` | `ease-out` | Sock ⇄ Skin toggle | Component Library |
| Hero eyebrow rotation | `3.5s` | cycle | Hero rotating eyebrow | Component Library |
| Ticker slide interval | `4s` | — | Ticker bar | Component Library |
| Ticker opacity crossfade | `320ms` | `ease` | Ticker slide transition | Component Library |
| Manifesto rotation | `0.7s` | `ease` | Manifesto headline rotation | Component Library |
| PDP toggle all | `0.2s` | (default) | PDP toggle buttons | PDP CSS |
| PDP swatch all | `0.2s` | (default) | PDP swatches | PDP CSS |
| Button hover opacity | — | — | Opacity shift to 0.9 | Component Library |

### Inconsistencies

| Context | Value | Source |
|---|---|---|
| General component transitions | `320ms` | Component Library |
| PDP transitions | `0.2s` (200ms) | PDP CSS |

> 🔴 PDP uses `200ms` for interactive transitions while the Component Library specifies `320ms` for the same type of interaction (hover/toggle).

> **Recommendation (requires Architect decision):** Define 2–3 duration tokens (fast: 200ms, normal: 320ms, slow: 700ms) and assign them by interaction type.

---

## BREAKPOINTS

| Breakpoint | Value | Source |
|---|---|---|
| Mobile → Desktop | `768px` | Component Library (Responsive Behavior Summary, Accessibility & Mobile) |

### Notes

- Only one breakpoint is documented across all sources.
- `clamp()` functions are used for fluid typography on hero/display, but intermediate breakpoints are not specified.
- Touch target minimum: `44×44px` at mobile.
- Font sizes "reduce via `clamp()`" on mobile but specific clamp ranges are only documented for a few elements (e.g., manifesto headline `38–92px`, credibility headline `30–52px`).

> **Recommendation (requires Architect decision):** Consider adding a tablet breakpoint (e.g., `1024px`) for sections that jump from 1-column to 4+ columns. Currently the only breakpoint creates very wide single-column layouts on tablets.

---

## CONTAINERS (max-width)

| Value | Where Used | Source |
|---|---|---|
| `600px` | PDP newsletter container | PDP CSS |
| `720px` | Association strip | Component Library |
| `760px` | PDP FAQ container | PDP CSS |
| `1200px` | PDP sections (general) | PDP CSS |
| `1400px` | PDP hero | PDP CSS |
| `48ch` | Founder Letter copy | Component Library |
| `26ch` | Product description, article excerpt | Component Library |
| (none specified) | Homepage sections | Homepage :root — **no max-width token** |

### Inconsistencies

- No container max-width token exists in the `:root` system.
- PDP uses 4 different max-widths (`600px`, `760px`, `1200px`, `1400px`).
- Homepage has no documented max-width constraint.

> **Recommendation (requires Architect decision):** Define container tokens, e.g., `--container-sm: 600px`, `--container-md: 760px`, `--container-lg: 1200px`, `--container-xl: 1400px`.

---

## GRID

| Spec | Columns | Gap | Where Used | Source |
|---|---|---|---|---|
| PDP hero | `1fr 1fr` | `64px` | PDP main layout | PDP CSS |
| PDP benefits | `repeat(3, 1fr)` | `40px` | Benefit grid (PDP) | PDP CSS |
| PDP variants | `repeat(4, 1fr)` | `20px` | Variant product grid | PDP CSS |
| PDP reviews | `repeat(3, 1fr)` | `32px` | Review cards | PDP CSS |
| PDP motion | `repeat(3, 1fr)` | `32px` | Motion/video grid | PDP CSS |
| PDP justifier | `repeat(2, 1fr)` | `40px` | Justifier cards | PDP CSS |
| Product Grid (home) | 3–4 columns | `28px` | Product card grid | Component Library |
| Product Card Grid | 4-column (desktop) | — | Home product cards | Component Library |
| Pillar Strip | 6-column | — | Pillar attributes | Component Library |
| Pillar Strip (mobile) | 2-column | — | Pillar attributes | Component Library |
| Disciplines | 3-column | — | Discipline cards | Component Library |
| Footer | `1fr 1fr 1fr 1fr` | `28px` | Footer columns | Component Library |
| 50/50 Split | 2-column (equal) | — | Editorial splits | Component Library |
| Founder Letter | `0.85fr : 1fr` | — | Image : copy | Component Library |
| Problem Section | `1.15fr : 0.85fr` | — | Copy : visual | Component Library |
| Variant Grid | `1fr : 1.1fr` | `56px` | Form : image | Component Library |
| Credibility | 2-column | `2px` | Logo cells | Component Library |
| Promo Tiles | `1fr 1fr` | `28px` | Promo images | Component Library |

### Inconsistencies

- No standard column-gap token. Gaps vary: `2px`, `8px`, `16px`, `20px`, `28px`, `32px`, `40px`, `56px`, `64px`.
- Asymmetric grids (`0.85fr : 1fr`, `1.15fr : 0.85fr`, `1fr : 1.1fr`) are all slightly different ratios for conceptually similar 2-column layouts.

> **Recommendation (requires Architect decision):** Standardize asymmetric splits to one or two ratios (e.g., `0.85fr : 1fr` and `1fr : 1fr`). Define gap tokens tied to the spacing scale.

---

## CROSS-CUTTING ISSUES

### 1. PDP is a Parallel Design System
The PDP CSS defines its own colors (`#1c1916`, `#c45c3f`, `#d4af37`, `#d6cfc0`), radii (`6px`, `8px`, `12px`), and transition durations (`0.2s`) that contradict the `:root` token system and the Component Library/Research Bible rules. This is the single largest consistency issue.

### 2. Undefined CSS Variables
The Component Library references `var(--m-dark)`, `var(--m-bg)`, `var(--m-accent)`, and `var(--alt-bg)` which are **not defined** in the `:root` token block. These likely come from a separate `maturation-styles.css` file referenced in the Design System doc but not inventoried.

### 3. Eyebrow Specification Disagrees with Itself
Three sources define eyebrow styling with three different letter-spacing values (`0.08em`, `0.14em`, `0.18em`) and two different font weights (`600`, `700`).

### 4. Token Scale Has Gaps
The `--sp-*` scale jumps from `32px` to `48px` and from `64px` to `96px`. Many component specs use values in those gaps (40px, 56px, 72px, 76px, 80px, 88px). Either the scale needs expanding or the specs need constraining.

### 5. No Semantic Tokens
All tokens are primitive (raw values). There are no semantic aliases like `--color-surface`, `--color-on-surface`, `--spacing-section`, `--spacing-component`. This makes it harder to maintain consistency and support dark/light themes.

---

## DECISION LOG (empty — awaiting Architect)

| ID | Question | Options | Decision | Date |
|---|---|---|---|---|
| DT-01 | Primary text color | `#050505` (cool) vs `#1c1916` (warm) | — | — |
| DT-02 | Accent/coral color | `#f97250` vs `#c45c3f` | — | — |
| DT-03 | Star/gold color | `#fbc02d` vs `#d4af37` | — | — |
| DT-04 | Alt background | `#f9f9f9` (cool) vs `#f9f7f2` (warm) vs `#f5f2ec` (warmer) | — | — |
| DT-05 | Soft text | `#4a4a4a` vs `#6a6a6a` vs `#6b645a` | — | — |
| DT-06 | Muted text | `#8a8a8a` vs `#999999` | — | — |
| DT-07 | Border/line | `#e6e6e6` vs `#e5e2db` vs `#d6cfc0` | — | — |
| DT-08 | Eyebrow letter-spacing | `0.08em` vs `0.14em` vs `0.18em` | — | — |
| DT-09 | Eyebrow font-weight | `600` vs `700` | — | — |
| DT-10 | Border radius policy | Strict 0/2/4 vs expanded 0/2/4/8/12 | — | — |
| DT-11 | PDP button radius | `0px` (system) vs `6px` (PDP current) | — | — |
| DT-12 | Spacing scale gaps | Expand scale vs constrain specs | — | — |
| DT-13 | Container max-widths | Define tokens? What values? | — | — |
| DT-14 | Transition duration | `200ms` vs `320ms` as default interactive | — | — |
| DT-15 | Tablet breakpoint | Add `1024px` or stay single-breakpoint? | — | — |

---

**Last Updated:** 2026-07-13  
**Next Step:** Architect reviews each DT-* item and records decisions. Then a remediation pass updates all source docs and CSS to match.
