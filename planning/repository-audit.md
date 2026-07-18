# Repository Audit — Barreletics-Design-Review

**Date:** 2026-07-13  
**Status:** PLANNING — do not commit  
**Scope:** 551 files across 47 directories (excluding `.git/`)

---

## Summary

This repository suffers from **massive duplication** caused by the same design files being copied across 4+ parallel directory trees that mirror each other. Of 551 total files, an estimated **~350 are exact duplicates**. The `barreletics-design-review/` subtree alone contains 4 near-identical copies of the same project (`Barreletics Design Review/`, `project/`, `design_handoff_barreletics 2/`, and their `versions/` subdirectories). Additionally, the `files/` and `Barreletics_All_Versions/` directories duplicate the full homepage version history.

---

## 1. Duplicate Files (Exact Match — Same MD5)

### 1A. Full Directory Mirrors (Biggest Problem)

The following directories contain **byte-identical** copies of the same files:

| Canonical (keep) | Duplicate 1 | Duplicate 2 |
|---|---|---|
| `barreletics-design-review/Barreletics Design Review/` | `barreletics-design-review/project/` | `barreletics-design-review/design_handoff_barreletics 2/pages/` |

**Evidence:** Every text file in `project/` has the same MD5 as its counterpart in `Barreletics Design Review/`. The `design_handoff_barreletics 2/pages/` directory is also identical for all shared files. The `project/uploads/` directory is a byte-for-byte clone of `Barreletics Design Review/uploads/`.

**Scale:** ~150 files duplicated across these 3 trees = **~300 redundant copies**.

**Recommended action:** Designate `barreletics-design-review/Barreletics Design Review/` as canonical. Delete `project/` and `design_handoff_barreletics 2/pages/` after verifying no unique files exist.

### 1B. Homepage Version History Duplicated

| Location 1 | Location 2 |
|---|---|
| `files/Barreletics_Home_v10.html` through `v24.html` | `barreletics-design-review/Barreletics_All_Versions/Barreletics_Home_v10.html` through `v24.html` |

**Evidence:** All 15 version files (v10–v24) have identical MD5 hashes between the two locations.

**Additional:** `Barreletics_Home_v22.html` and `Barreletics_Home_v23.html` are **byte-identical** (MD5: `fc1f8ffbf4b3a81aff3106d564b22407`, size: 151,784 bytes). Either v23 wasn't actually updated from v22, or the wrong file was saved.

**Recommended action:** Keep `files/` as the canonical homepage archive. Delete `Barreletics_All_Versions/`.

### 1C. Version Snapshot Directories (Internal Duplication)

Each `versions/` subdirectory is duplicated between `Barreletics Design Review/versions/` and `project/versions/`:

- `versions/2026-05-24/` — 13 files × 2 copies
- `versions/2026-05-25/` — 15 files × 2 copies  
- `versions/2026-05-25-batch/` — 13 files × 2 copies
- `versions/2026-05-25-v4-prebuild/` — 11 files × 2 copies
- `versions/2026-05-25-v4-video/` — 1 file × 2 copies
- `versions/2026-05-25-v5/` — 18 files × 2 copies
- `versions/2026-05-25-coperni-vid/` — 1 file × 2 copies
- `versions/2026-05-26-v6/` — 5 files × 2 copies
- `versions/2026-05-26-v7v8/` — 2 files × 2 copies
- `versions/2026-05-26-v9/` — 1 file × 2 copies
- `versions/2026-05-31/` — 3 files (only in `Barreletics Design Review/`)

**Recommended action:** All version snapshots should live in one `versions/` tree only.

### 1D. CSS Files Duplicated 8–11 Times

| File | Duplicate Count |
|---|---|
| `audit-styles.css` | 11 identical copies |
| `pdp-styles.css` | 9 identical copies (current version) + 2 older versions |
| `pages-extras.css` | 3 identical copies (current) + 4 older versions |
| `section-mocks.css` | 3 identical copies |
| `wireframes-styles.css` | 3 identical copies |
| `maturation-styles.css` | 3 identical copies |
| `home-matured.css` | 2 identical copies |

### 1E. Upload Screenshots Duplicated with Hash Suffixes

Every screenshot in `uploads/` exists twice — once with the original name and once with a hash suffix (e.g., `Screenshot...PM.png` and `Screenshot...PM-5d7af6f0.png`). These are then duplicated again in `project/uploads/`.

**Result:** Each screenshot has **4 identical copies** in the repo.

**Recommended action:** Remove hash-suffixed duplicates and the `project/uploads/` mirror.

### 1F. Research Bible — 5 Copies

`Barreletics_Research_Bible.md` (17,538 bytes) exists at:
1. `barreletics-design-review/Barreletics_Research_Bible.md`
2. `barreletics-design-review/Barreletics_All_Versions/Barreletics_Research_Bible.md`
3. `barreletics-design-review/Barreletics Design Review/uploads/Barreletics_Research_Bible.md`
4. `barreletics-design-review/Barreletics Design Review/uploads/Claude Design Files/Barreletics_Research_Bible.md`
5. `barreletics-design-review/Barreletics Design Review/uploads/Claude Design Files/Barreletics_Research_Bible-4a33764a.md`

### 1G. Claude Handoff Doc — 3 Copies

`Barreletics_Complete_Handoff_for_ClaudeDesign.md` (11,739 bytes):
1. `uploads/Barreletics_Complete_Handoff_for_ClaudeDesign.md`
2. `uploads/Claude Design Files/Barreletics_Complete_Handoff_for_ClaudeDesign.md`
3. `uploads/Claude Design Files/Barreletics_Complete_Handoff_for_ClaudeDesign-26231250.md`

### 1H. Barreletics_v28_1_BASE.html — 3 Copies

1. `uploads/Barreletics_v28_1_BASE.html`
2. `uploads/Claude Design Files/Barreletics_v28_1_BASE.html`
3. `uploads/Claude Design Files/Barreletics_v28_1_BASE-054a51d3.html`

---

## 2. Obsolete Versions

### 2A. Homepage Design Exploration (v1–v10)

The `barreletics-design-review/Barreletics Design Review/` directory contains:
- `Barreletics Home.html` (v1 implicit)
- `Barreletics Home v2.html` through `Barreletics Home v10.html`
- `Barreletics Home - Matured.html` (matured/final variant)

**These are superseded** by the `files/` directory versions (v10–v24), which themselves are superseded by the current homepage at `index.html` and the section-based architecture in `sections/`.

### 2B. Homepage Full-Page Versions (v10–v24)

Located in `files/` (and duplicated in `Barreletics_All_Versions/`):
- v10 through v24, with v24 being the latest monolithic build
- **v22 and v23 are identical** (same MD5 hash), suggesting a version numbering error

**Current canonical:** The `sections/` directory + `index.html` represent the decomposed, section-based approach that supersedes all monolithic homepage versions.

### 2C. PDP Versions

- `Barreletics PDP.html` → `Barreletics PDP v2.html` → `Barreletics PDP - Matured.html`
- All superseded by **`Barreletics-PDP-v36-Jul2026.html`** (52 KB, root level)

### 2D. Version Snapshot Directories

10 date-stamped snapshot directories under `versions/` (2026-05-24 through 2026-05-31) preserve intermediate states. These are historical archives but are not referenced by any current document.

**Recommended action:** Archive all version snapshots to a single `archive/` directory or Git tag. The current live files don't need 10 snapshot copies alongside them.

---

## 3. Orphaned Assets

### 3A. Empty Directories

| Directory | Contents |
|---|---|
| `barreletics-design-review/Barreletics Design Review 2/` | Empty (0 files) |
| `barreletics-design-review/Barreletics_All_Versions 2/` | Empty (0 files) |
| `barreletics-design-review/design_handoff_barreletics 3/` | Empty (0 files) |
| `Manychat Content/` | Only `.DS_Store` |

**Recommended action:** Delete all 4 empty directories.

### 3B. Orphaned ZIP Files

- `manychat-kb/manychat-kb-all-16.zip` — The individual markdown files are already extracted alongside it
- `Manychat Content.zip` — Same content, root-level duplicate of the zip

**Recommended action:** Delete both ZIPs since content is extracted.

### 3C. Unreferenced Standalone HTML Files

| File | Status |
|---|---|
| `matrix-20260707.html` | Superseded by `Barreletics-SectionDecisionMatrix-v1_0-Jul2026.html` |
| `Section-26-NotesFromStudio.html` | Not referenced by index.html or any doc |
| `Section-27-FAQ.html` | Not referenced by index.html or any doc |
| `Section-28-Newsletter.html` | Not referenced by index.html or any doc |
| `Barreletics-DesignSystem-v1_0-Jul2026.html` | Standalone, not referenced in docs/ |
| `Barreletics-Everything-Index.html` (406 KB) | Standalone omnibus file, possibly orphaned |

### 3D. Orphaned Screenshots

The `screenshots/` directory (19 PNG files) contains review artifacts (e.g., `v10-sockmath.png`, `01-teal-sections.png`) not referenced by any HTML or markdown file.

### 3E. `.DS_Store` Files

At least 4 `.DS_Store` files scattered across the repo. Should be in `.gitignore`.

---

## 4. Conflicting Specifications

### 4A. `tweaks-panel.jsx` — Two Different Versions

- `barreletics-design-review/Barreletics Design Review/tweaks-panel.jsx` (24,572 bytes, MD5: `5cdc2a46...`)
- `barreletics-design-review/project/tweaks-panel.jsx` (23,873 bytes, MD5: `7551642a...`)
- `barreletics-design-review/design_handoff_barreletics 2/pages/tweaks-panel.jsx` (24,572 bytes, matches `Barreletics Design Review/`)

The `project/` copy differs from the others by ~700 bytes. **This is the only non-identical file between the "mirror" directories**, suggesting an unsaved or divergent edit.

### 4B. `Barreletics Wireframes.html` — Two Versions

- `Barreletics Design Review/Barreletics Wireframes.html` (63,879 bytes, MD5: `5374da6f...`)
- `design_handoff_barreletics 2/pages/Barreletics Wireframes.html` (64,198 bytes, MD5: `f72aba56...`)

The handoff copy is 319 bytes larger, indicating modifications were made to one copy but not synced back.

### 4C. `Barreletics Maturation Study.html` — Three Versions

1. `Barreletics Design Review/Barreletics Maturation Study.html` (102,454 bytes)
2. `Barreletics Design Review/versions/2026-05-31/Barreletics Maturation Study.html` (73,899 bytes)
3. `design_handoff_barreletics 2/pages/Barreletics Maturation Study.html` (125,749 bytes)

Three different sizes = three different versions. Unclear which is canonical.

### 4D. `docs/08-LIVE-SITE-COPY-AUDIT.md` Not in INDEX.md

This 118 KB document exists in `docs/` but is **not listed in `docs/INDEX.md`**. It is referenced by `docs/09-PRODUCT-KNOWLEDGE.md` but invisible to anyone navigating via the index.

Meanwhile, `docs/08-CREATIVE-PLAYBOOK.md` (109 bytes, STUB) occupies the `08` slot in the index. Two files share the `08-` prefix with different names and purposes.

---

## 5. Missing Documentation

### 5A. Stub Documents (Created but Empty)

| File | Status | Size |
|---|---|---|
| `docs/00-README.md` | STUB | 71 bytes |
| `docs/01-BRAND-NORTH-STAR.md` | PENDING REVIEW | 101 bytes |
| `docs/08-CREATIVE-PLAYBOOK.md` | STUB | 109 bytes |
| `docs/10-DECISIONS.md` | STUB | 95 bytes |

These files are listed in the index but contain only a title and status line — no actual content.

### 5B. No Top-Level README.md

The repository root has no `README.md`. The only README is inside `barreletics-design-review/README.md` (1,538 bytes) and `barreletics-design-review/design_handoff_barreletics 2/README.md` (16,581 bytes).

### 5C. Missing `.gitignore`

No `.gitignore` exists. This is why `.DS_Store` files and potentially large binary assets are tracked.

### 5D. No Collection Page Architecture Doc

`docs/05-PDP-ARCHITECTURE.md` (123 KB) and `docs/06-HOMEPAGE-ARCHITECTURE.md` (320 KB) exist, but there is no collection page architecture document despite collection page HTML files existing in the design review.

### 5E. `manychat-kb/01-*.md` Missing

The manychat-kb directory has files numbered `02` through `16`, but **no `01-` file**. Either it was never created or was deleted.

---

## 6. Naming Inconsistencies

### 6A. File Name Casing & Separator Conventions

| Convention | Examples | Count |
|---|---|---|
| `kebab-case` with underscores | `Barreletics_Home_v19.html` | ~15 files |
| Title Case with spaces | `Barreletics Home v8.html` | ~50 files |
| Kebab-case with dashes | `barreletics-decisions-2026-07-09.json` | ~5 files |
| PascalCase-Kebab hybrid | `Barreletics-PDP-v36-Jul2026.html` | ~4 files |
| Numbered prefix | `01-section.html`, `02-open-vs-closed-sole.md` | ~45 files |
| ALL-CAPS with numbers | `09-PRODUCT-KNOWLEDGE.md` | ~10 files |

**At least 6 different naming conventions** are used across the repo.

### 6B. `Section-XX-Name.html` vs `XX-section.html`

Root-level standalone sections use `Section-26-NotesFromStudio.html` format, while the `sections/` directory uses `01-section.html` format. Some section files in `sections/` use descriptive names (`hero.html`, `problem.html`, `manifesto.html`) while others use number-only names (`01-section.html` through `29-section.html`).

### 6C. Directory Names with Spaces and Numbering

- `Barreletics Design Review` (spaces, Title Case)
- `Barreletics_All_Versions` (underscores, Title_Case)
- `design_handoff_barreletics 2` (mixed underscores + spaces + number suffix)
- `Manychat Content` (spaces)
- `manychat-kb` (kebab-case)

### 6D. Version Numbering Inconsistency

- Homepage uses `v2`–`v10` (simple), then `v10`–`v24` (monolithic), then section-based
- PDP uses `PDP`, `PDP v2`, `PDP - Matured`, then `PDP-v36` (jumped to v36)
- Design system uses `v1_0` in filename

---

## 7. Broken References

### 7A. `docs/INDEX.md` Missing `08-LIVE-SITE-COPY-AUDIT.md`

The index references `08-CREATIVE-PLAYBOOK.md` at the `08` slot but does not mention `08-LIVE-SITE-COPY-AUDIT.md` (118 KB), which is the substantially more important document.

### 7B. `docs/05-PDP-ARCHITECTURE.md` References Relative HTML Files

Lines 2238–2246 contain relative links like `<a href="Barreletics Home v2.html">` that expect HTML files to be in the same directory as the markdown file. These files don't exist in `docs/` — they exist in `barreletics-design-review/Barreletics Design Review/`.

### 7C. Handoff Markdown Points to Non-Canonical Location

`barreletics-design-review/Barreletics_Handoff.md` references `Barreletics_Home_v24.html` but the file doesn't exist at the same directory level — it's in `Barreletics_All_Versions/` or `files/`.

---

## 8. Consolidation Opportunities

### 8A. Merge the 4 Parallel Directory Trees → 1

**Highest impact.** Eliminate the `project/`, `design_handoff_barreletics 2/`, and `Barreletics_All_Versions/` mirrors. Keep `barreletics-design-review/Barreletics Design Review/` as the single canonical design source.

**Savings:** ~300 duplicate files removed.

### 8B. Merge `files/` and `Barreletics_All_Versions/` → `archive/homepage-versions/`

Both directories contain the same v10–v24 homepage builds. Consolidate into one `archive/` directory.

### 8C. Merge Standalone Section HTML Files

`Section-26-NotesFromStudio.html`, `Section-27-FAQ.html`, and `Section-28-Newsletter.html` at the root could move into the `sections/` directory with consistent naming.

### 8D. Consolidate Upload Deduplication

The `uploads/` directory has every screenshot twice (original + hash suffix). Remove hash-suffix copies.

### 8E. Single ManyChat KB Location

The `manychat-kb/` directory (individual files) + `manychat-kb-all-16.zip` + `Manychat Content.zip` + `Barreletics Design Review/uploads/Barreletics_ManyChat_Knowledge.md` could be consolidated. Keep `manychat-kb/` as canonical, delete the zips and standalone markdown.

### 8F. `docs/07-COPY-GUIDE.md` is 7.3 MB

At 7,326,654 bytes, this is by far the largest text file in the repo. It may contain embedded content or very extensive copy that should be reviewed for whether it should be split or compressed.

### 8G. `docs/06-HOMEPAGE-ARCHITECTURE.md` is 320 KB

The second-largest markdown file. Both this and `07-COPY-GUIDE.md` may benefit from being split into sub-documents.

### 8H. Bundled Export File is 3.3 MB

`Barreletics Design Review/export/Barreletics Maturation Study - Bundled.html` (3.3 MB) is an embedded/bundled export of a study that exists in a lighter form elsewhere.

---

## Recommended Cleanup Priority

| Priority | Action | Files Affected |
|---|---|---|
| **P0** | Delete `project/` directory (exact mirror) | ~150 files |
| **P0** | Delete `Barreletics_All_Versions/` (mirror of `files/`) | ~17 files |
| **P0** | Delete empty directories (`Barreletics Design Review 2/`, `Barreletics_All_Versions 2/`, `design_handoff_barreletics 3/`, `Manychat Content/`) | 4 dirs |
| **P1** | Delete `design_handoff_barreletics 2/pages/` (near-mirror, 3 unique files to review first) | ~40 files |
| **P1** | Remove hash-suffix duplicate screenshots from `uploads/` | ~24 files |
| **P1** | Delete ZIP files (`manychat-kb-all-16.zip`, `Manychat Content.zip`) | 2 files |
| **P1** | Add `.gitignore` with `.DS_Store`, `*.zip`, `Thumbs.db` | 1 new file |
| **P2** | Move obsolete homepage versions to `archive/` | ~15 files moved |
| **P2** | Fix `docs/INDEX.md` to include `08-LIVE-SITE-COPY-AUDIT.md` | 1 file |
| **P2** | Resolve `tweaks-panel.jsx` divergence | 1 file |
| **P2** | Resolve `Barreletics Maturation Study.html` 3-version conflict | 3 files |
| **P3** | Fill stub docs (`00-README.md`, `01-BRAND-NORTH-STAR.md`, `08-CREATIVE-PLAYBOOK.md`, `10-DECISIONS.md`) | 4 files |
| **P3** | Standardize naming conventions (pick one) | Repo-wide |
| **P3** | Add root `README.md` | 1 new file |
| **P3** | Investigate missing `manychat-kb/01-*.md` | 1 file |
