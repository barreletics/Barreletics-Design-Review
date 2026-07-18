# ADR Change Matrix

**Generated:** 2026-07-13  
**Purpose:** Complete cross-reference of every conflicting token across all source documents

---

## Token Occurrence Matrix

| ADR | Token/Value | docs/03 | docs/04 | docs/05 | docs/06 | docs/07 | docs/09 | docs/10 | Lines (key) | Risk |
|-----|-------------|---------|---------|---------|---------|---------|---------|---------|-------------|------|
| 01 | `#f9f7f2` (warm alt-bg) | — | 23, 130 | — | 3897, 9452 | 3898+ (80× in HTML) | — | — | docs/04: 23, 130; docs/06: 3897, 9452; docs/07: 3898+ | High |
| 01 | `#f9f9f9` (neutral alt-bg) | 120 | — | 36, 76, 161–164, 231, 289, 502, 536 | 40, 2751, 4253, 5595, 8306 | — | — | 63 | docs/03: 120; docs/06: 40; docs/10: 63 | High |
| 01 | `#6a6a6a` (warm text-soft) | — | 24 | — | — | — | — | — | docs/04: 24 only | High |
| 01 | `#4a4a4a` (neutral text-soft) | 123 | — | 43, 61, 72, 77, 82, 174, 250, 257, 264, 268, 307–322, 350, 539 | 43, 5598 | — | — | 63 | docs/03: 123; docs/05: 43+; docs/06: 43; docs/10: 63 | High |
| 01 | `#999999` (warm text-mute) | — | 25 | — | — | — | — | — | docs/04: 25 only | High |
| 01 | `#8a8a8a` (neutral text-mute) | 124 | — | 45, 55, 76, 176, 195, 202, 230–231, 239, 352, 354, 493, 495, 542, 562 | 44, 5599 | — | — | 63 | docs/03: 124; docs/05: 45+; docs/06: 44; docs/10: 63 | High |
| 01 | `#e5e2db` (warm line) | — | 26, 29 | — | — | — | — | — | docs/04: 26, 29 only | High |
| 01 | `#e6e6e6` (neutral line) | 125 | — | 67, 92, 162–164, 193, 199, 224, 230, 239, 247–266, 276, 287, 341, 541, 554, 561 | 45, 5600 | — | — | 63 | docs/03: 125; docs/05: 67+; docs/06: 45; docs/10: 63 | High |
| 02 | `$75` (stale threshold) | 239 (historical note) | — | 264, 2197, 2295, 2360 | — | — | — | 585 (superseded) | docs/05: 264, 2197, 2295, 2360 | Medium |
| 02 | `$150` (current threshold) | 239, 402–404 | — | 195, 2212 | 4294 | — | 24, 965–966 | 577, 585, 1085 | docs/05: 195, 2212; docs/09: 24, 965 | Medium |
| 03 | `border-radius: 0px` (buttons) | 372 | 37 | — | — | — | — | 30 | docs/04: 37; docs/03: 372; docs/10: 30 | High |
| 03 | `border-radius: 6px` (PDP CTA) | — | — | 46, 230–231 | — | — | — | — | docs/05: 46, 230–231 | High |
| 04 | `0.14em` letter-spacing | 371, 396 | 12 | 763, 1029, 1315, 1358, 1628, 2015, 2502 | 872, 1078, 1344, 1630, 1673, 1943, 2487, 2813, 3010, 3129, 3207, 3320, 3359, 3419, 3592, 3862, 3908, 4016 | — | — | 1077 | docs/04: 12; docs/03: 371 | High |
| 04 | `0.08em` letter-spacing (eyebrow) | 149, 395 | — | 40, 55, 59, 81, 754, 1148, 1563, 1824 | 76 (token), 1069, 1463, 1878, 2139, 3742, 3883, 3902, 3991, 4001 | — | — | — | docs/06: 76; docs/05: 40, 55 | High |
| 04 | `0.18em` letter-spacing | — | 576 | 1297, 1794, 2077 | 156, 220, 501, 557, 910, 978, 3783, 3834, 3998 (30+) | — | — | — | docs/04: 576; docs/06: 30+ | Medium |
| 04 | `0.06em` letter-spacing | — | 668 | 126, 858, 1230, 1257, 1853, 2396, 2573 | 1173, 1545, 1572, 3271, 3701, 3965 (16+) | — | — | — | docs/04: 668; docs/05: 126+ | Medium |
| 05 | `#050505` (primary text) | 122, 374 | 20 | — | 42, 60, 2645+ (20+) | — | — | 63 | docs/04: 20; docs/03: 122, 374; docs/06: 42 | High |
| 05 | `#1c1916` (warm text) | — | — | 24, 25, 31, 42, 44, 46, 51, 56, 60, 73, 83, 88, 94, 97, 99, 161, 227, 231, 240–243 | 4210 | — | — | — | docs/05: 24+ (20+); docs/06: 4210 | High |
| 06 | `border-radius: 0/2–4px max` | 372 | 30–33 | — | — | — | — | — | docs/04: 30–33; docs/03: 372 | High |
| 06 | `border-radius: 12px` (cards) | — | — | 67, 80, 541, 561 | — | — | — | 287 | docs/05: 67, 80; docs/10: 287 | High |
| 06 | `border-radius: 8px` (gallery/video) | — | — | 36, 76 | — | — | — | 293 | docs/05: 36, 76; docs/10: 293 | Medium |
| 07 | `#fbc02d` (system gold) | 130, 374 | 22 | — | 55, 5610 | — | — | 63 | docs/04: 22; docs/03: 130, 374; docs/06: 55 | High |
| 07 | `#d4af37` (PDP gold) | — | — | 41, 71, 552 | — | — | — | — | docs/05: 41, 71 | High |

---

## CROSS-ADR DEPENDENCIES

### Direct Dependencies

| Dependency | Why |
|-----------|-----|
| **ADR-01 → ADR-05** | If ADR-01 resolves toward warm palette (Option B), the warm text `#1c1916` from ADR-05 is more coherent. If ADR-01 goes neutral (Option A), `#050505` is more coherent. |
| **ADR-05 → ADR-07** | Star color `#d4af37` was likely chosen to harmonize with `#1c1916` warm text. If ADR-05 resolves to `#050505`, the brighter `#fbc02d` may be more appropriate. |
| **ADR-01 → ADR-07** | The warm-vs-neutral palette direction affects which gold feels more cohesive. `#d4af37` suits warm; `#fbc02d` suits neutral. |
| **ADR-03 → ADR-06** | Both address border-radius exceptions. If ADR-03 allows PDP overrides (Option A/C), that precedent makes ADR-06 Option A/C more defensible. If system wins (Option B), both should be strict. |
| **ADR-04 → ADR-05** | Eyebrow color rendering depends on the text color baseline. Eyebrows using `--br-text-mute` color will differ depending on `#8a8a8a` vs `#999999`. |
| **ADR-06 → ADR-03** | Review card radius and button radius are philosophically linked — both test "are page-level overrides permitted?" |

### Dependency Chain

```
ADR-01 (palette direction)
  ├── ADR-05 (text color follows palette)
  │     └── ADR-07 (star color follows text warmth)
  └── ADR-04 (muted text color used in eyebrows)

ADR-03 (button radius precedent)
  └── ADR-06 (card radius follows same philosophy)
```

### Recommended Resolution Order for Dependencies

1. **ADR-01** first (sets warm-vs-neutral direction)
2. **ADR-05** second (follows from palette)
3. **ADR-07** third (follows from text color)
4. **ADR-03** fourth (sets override philosophy)
5. **ADR-06** fifth (follows override philosophy)
6. **ADR-04** sixth (benefits from all prior decisions)
7. **ADR-02** anytime (independent — only touches docs/05)

---

## VALIDATION REQUIRED AFTER IMPLEMENTATION

### ADR-01: Color Palette Values
- [ ] Search all docs/ for old value (`#f9f7f2` or `#f9f9f9` depending on decision) → must return 0 results in token definitions
- [ ] Verify docs/07-COPY-GUIDE.md HTML templates — if #f9f7f2 is retired, 80+ occurrences need updating or documented exception
- [ ] Confirm docs/10-DECISIONS.md D-007 matches the chosen values
- [ ] Check docs/04 line 29 (`var(--br-line)` reference) still matches the chosen line color

### ADR-02: Free Shipping Threshold
- [ ] Search docs/05 for `$75` → must return 0 results (if Option A)
- [ ] Verify meta description (line 2197) matches live site
- [ ] Confirm docs/09 and docs/10 still align
- [ ] Check docs/03 line 239 historical note is still accurate

### ADR-03: Button Border-Radius
- [ ] Search docs/05 for `border-radius: 6px` on buttons → verify expected state
- [ ] Check docs/10 D-003 reflects the final decision
- [ ] If PDP exception allowed: verify docs/04 documents the exception

### ADR-04: Eyebrow Letter-Spacing
- [ ] Search all docs/ for old default value → must not appear as a "system rule"
- [ ] Verify docs/03 token table (line 149) and core rules (line 371) agree
- [ ] Verify docs/04 line 12 system rule agrees
- [ ] Check docs/06 line 76 `--t-eyebrow` token comment agrees
- [ ] Verify 0.18em and 0.06em component overrides are documented as exceptions or eliminated

### ADR-05: PDP Text Color
- [ ] If Option A: search docs/ for `#050505` in token definitions → should be gone
- [ ] If Option B: search docs/05 for hardcoded `#1c1916` → should be replaced with `var(--br-text)`
- [ ] Verify docs/06 matured override block (line 4206–4219) state matches decision
- [ ] Check contrast ratios are documented in docs/10

### ADR-06: Review Card Radius
- [ ] If Option B: search docs/05 for `border-radius: 12px` → must return 0
- [ ] If Option A/C: verify docs/04 lines 30–33 updated to document exception
- [ ] Check docs/10 D-038 reflects final decision
- [ ] Verify related 8px values (lines 36, 76) are addressed

### ADR-07: Star/Rating Color
- [ ] Search docs/ for old star color → must return 0 results in token definitions
- [ ] Verify docs/06 `--br-star` token matches chosen value
- [ ] Verify docs/05 PDP star classes use chosen value or `var(--br-star)`
- [ ] Check line 552 usage of `#d4af37` (non-star context) — update if needed

---

## RISK ASSESSMENT

| ADR | Risk Level | Rationale |
|-----|-----------|-----------|
| ADR-01 | **HIGH** | Touches 4 source documents + 80+ occurrences in docs/07. Warm values only exist in docs/04 (isolated); neutral values used by docs/03, docs/05, docs/06, docs/10 (majority). High blast radius on Option B. |
| ADR-02 | **MEDIUM** | Only affects docs/05 (4 stale lines). Other docs already correct. Clear resolution (C-010 already declares $150). Low risk of breakage. |
| ADR-03 | **HIGH** | Sets philosophical precedent for all border-radius exceptions. Interacts with ADR-06. PDP has `6px` in only 1 CSS class + 2 inline styles. Contained but precedent-setting. |
| ADR-04 | **HIGH** | Four different values across 5 files. Hundreds of occurrences of `0.14em` and `0.08em` in CSS. Most complex token conflict. Both defaults (`0.14em` in header rules, `0.08em` in token/CSS) are used extensively in the matured markup. |
| ADR-05 | **HIGH** | `#1c1916` hardcoded in 20+ PDP declarations. If retired, requires extensive refactoring of docs/05. If adopted system-wide, requires updating 3 source docs + removing matured override mechanism. |
| ADR-06 | **HIGH** | Directly violates an explicit "Never" prohibition. Resolution affects brand identity perception. Also triggers cascade — must address 8px gallery, 6px CTA alongside. |
| ADR-07 | **MEDIUM** | Clean two-value conflict, contained to 2 files (docs/05 hardcoded, system token in docs/03+04+06). Only 2 PDP declarations plus 1 non-star usage to update. |
