# AI Operations Manual — Barreletics Design Review Repository

**Date:** 2026-07-13  
**Status:** PLANNING — do not commit  
**Purpose:** Everything another AI agent needs to immediately become productive on this repository.  
**Read this file first, then WORKFLOW.md.**

---

## ROLES

| Role | Actor | Responsibilities |
|------|-------|-----------------|
| CEO | Andrew | Assigns work via sprint tickets, approves deliverables, breaks ties, owns the repository |
| Lead Architect | ChatGPT | Designs specifications, reviews content accuracy, grants APPROVED status, makes ADR decisions |
| Build Engineer | Cursor | Executes builds, commits, pushes, runs audits, implements Shopify code |

**Chain of command:** CEO assigns → Build Engineer executes → Architect reviews (when required) → CEO approves or reassigns.

No agent self-assigns work. No agent changes another agent's role. No agent modifies WORKFLOW.md without CEO approval.

---

## WORKFLOW

### Sprint Ticket Format

Every assignment arrives as a single-prompt sprint ticket:

```
ASSIGNMENT: [short name]
DELIVERABLE: [exact file path or output]
STATUS ON COMPLETION: [PENDING REVIEW or BUILDING]
SCOPE: [what's in / what's out]
DEPENDENCIES: [prior docs, data sources, URLs]
ACCEPTANCE CRITERIA: [what "done" looks like]
APPROVAL ROUTE: [ChatGPT review required? or auto-approve?]
```

One ticket per message. Execute and report. No multi-turn negotiation.

### Acceptance Criteria Rules

1. A task is complete ONLY when every acceptance criterion is satisfied
2. If even one criterion is not met, the task remains BUILDING
3. Never report a task complete based on belief — verify against each criterion
4. Acceptance criteria are literal — do not interpret loosely

### Self-Audit Requirement

Before reporting any deliverable as done:

1. Re-read every acceptance criterion
2. Verify each one is met (with evidence if measurable)
3. If a measured count was reported earlier and turns out wrong, correct immediately — do not defend
4. Report the self-audit result alongside the deliverable

### Commit Discipline

- **One commit per deliverable** — the deliverable is the atomic unit
- Every deliverable ends with a commit + push
- No orphaned work (uncommitted changes)
- Descriptive commit messages that name the deliverable
- Verify the push succeeded (check git status after push)

---

## STATUS SYSTEM

Every document in docs/ carries exactly one status:

| Status | Meaning | Who Sets It |
|--------|---------|-------------|
| STUB | Document has not been built — contains only title and status | Build Engineer (initial creation) |
| BUILDING | Work in progress | Build Engineer |
| PENDING REVIEW | Build complete, awaiting ChatGPT review | Build Engineer (on completion) |
| APPROVED | ChatGPT has explicitly approved the content | Architect only |
| SUPERSEDED | Replaced by a newer document | CEO or Architect |

**Rules:**
- No document becomes APPROVED without explicit ChatGPT approval
- STUB documents have ≤10 lines (title + status + placeholder)
- Status must appear in the document header as `**Status:** VALUE`
- Status transitions are one-way: STUB → BUILDING → PENDING REVIEW → APPROVED (or → SUPERSEDED)

---

## SPRINT PROCESS

```
1. CEO assigns sprint ticket (in chat)
2. Build Engineer reads ticket, gathers sources
3. Build Engineer executes the build
4. Build Engineer self-audits against acceptance criteria
5. Build Engineer commits and pushes (one commit per deliverable)
6. Build Engineer reports completion with self-audit summary
7. ChatGPT reviews (if PENDING REVIEW and review required)
8. CEO approves, requests changes, or assigns next ticket
```

**While Build Engineer works on task N, Architect specs tasks N+1 through N+3. No one waits.**

---

## REPOSITORY CONVENTIONS

### Directory Structure

```
/
├── docs/                    ← Production knowledge base (numbered 00–10)
├── planning/                ← Working documents (NEVER committed to production)
├── WORKFLOW.md              ← Operating manual (APPROVED, permanent)
├── barreletics-design-review/  ← Design source files (HTML mockups, CSS, uploads)
├── files/                   ← Homepage version archive (v10–v24)
├── sections/                ← Decomposed homepage sections (01–29)
├── manychat-kb/             ← ManyChat knowledge base articles (02–16)
└── screenshots/             ← Review artifact screenshots
```

### docs/ Numbering

| Number | Document | Purpose |
|--------|----------|---------|
| 00 | README | Getting started (STUB) |
| 01 | BRAND-NORTH-STAR | Brand vision, mission, positioning |
| 02 | BRAND-SYSTEM | Voice, tone, messaging |
| 03 | DESIGN-SYSTEM | Tokens, principles, architecture |
| 04 | COMPONENT-LIBRARY | Reusable components and patterns |
| 05 | PDP-ARCHITECTURE | Complete PDP HTML/CSS specification |
| 06 | HOMEPAGE-ARCHITECTURE | Complete homepage HTML/CSS specification |
| 07 | COPY-GUIDE | Lossless copy archive (217K lines of HTML) |
| 08 | CREATIVE-PLAYBOOK | Creative direction (STUB) |
| 08 | LIVE-SITE-COPY-AUDIT | Evidence-based audit of 46 live URLs |
| 09 | PRODUCT-KNOWLEDGE | Product facts, specs, variants |
| 10 | DECISIONS | Complete decision log with conflicts register |

**Note:** Two files share the 08- prefix (CREATIVE-PLAYBOOK and LIVE-SITE-COPY-AUDIT). INDEX.md only lists CREATIVE-PLAYBOOK. This is a known issue.

### planning/ File Types

| Prefix/Pattern | Type | Count |
|----------------|------|-------|
| ADR-NN-* | Architecture Decision Record | 7 |
| review-NN-* | Review packet for ChatGPT | 6 |
| QA-NN-* | QA checklist | 5 |
| *-inventory.md | Source material inventory | 4 |
| Other | Audits, plans, maps | 5 |

### Source Rules

- All content must be cited with `Source:` lines
- No invention — everything comes from source material (Research Bible, design handoff, live site, Shopify data)
- No unsupported metrics — measure directly or don't report
- Lossless migration only — when extracting from HTML sources, preserve every detail

### What NOT To Do

- Never modify APPROVED documents without explicit Architect approval
- Never report estimated counts (measure directly)
- Never summarize when lossless extraction is required
- Never commit planning/ files to production
- Never invent content not in sources
- Never fabricate citations

---

## APPROVAL RULES

### Auto-Approve (no ChatGPT review needed)

- Status changes (BUILDING → PENDING REVIEW)
- Structural edits (adding cross-references, fixing formatting)
- Shopify theme code
- Git operations
- Tooling and workflow documentation
- Planning documents

### Requires ChatGPT Review

- Brand content (docs/01, docs/02)
- Design decisions (docs/03, docs/04)
- Product copy and claims (docs/09)
- Architecture specifications (docs/05, docs/06)
- Any document containing customer-facing content
- ADR resolutions

### Requires CEO Approval

- Changes to WORKFLOW.md
- Repository structure changes
- Status system modifications
- Role definitions

---

## GIT WORKFLOW

### Branch Strategy

- Single branch: `main`
- All work committed directly to main
- No feature branches (unless CEO directs otherwise)

### Commit Protocol

```bash
git add [specific file(s)]
git commit -m "descriptive message naming the deliverable"
git push
git status   # verify push succeeded
```

- One commit per deliverable
- Never batch unrelated changes in one commit
- Descriptive messages: "Build docs/09-PRODUCT-KNOWLEDGE.md from sprint ticket" not "update files"
- Push after every commit — no local-only commits
- Verify after push — check git status shows clean state

### Common Commands

```bash
# Check current state
git status
git log --oneline -5

# Standard commit flow
git add docs/09-PRODUCT-KNOWLEDGE.md
git commit -m "Build docs/09-PRODUCT-KNOWLEDGE.md — product facts and variant data"
git push

# Verify
git status
git log --oneline -1
```

---

## ARCHITECT WORKFLOW (ChatGPT)

When operating as the Architect:

1. Review PENDING REVIEW documents against their review packet (planning/review-NN-*.md)
2. Check content against source material citations
3. Verify no invented content
4. Make ADR decisions when presented with options
5. Grant APPROVED status or return with specific feedback
6. Update docs/10-DECISIONS.md conflicts register when resolving conflicts

**Architect does not:** build documents, commit code, assign tasks, modify planning files.

---

## BUILDER WORKFLOW (Cursor)

When operating as the Build Engineer:

1. Read the sprint ticket completely
2. Identify all source dependencies (prior docs, URLs, data)
3. Gather sources — read the files, don't assume contents
4. Build the deliverable following acceptance criteria exactly
5. Self-audit: re-read every criterion and verify
6. Commit with descriptive message
7. Push
8. Report completion with:
   - What was built
   - Self-audit result (PASS / CONDITIONAL / FAIL per criterion)
   - Any issues discovered during build

**Builder does not:** approve documents, make design decisions, change the workflow, skip self-audit.

---

## QA WORKFLOW

When performing quality assurance on any deliverable:

### QA Checklist

1. **Acceptance criteria:** Compare deliverable against every criterion in the sprint ticket
2. **Source verification:** Verify all `Source:` lines point to real, accessible sources
3. **Omission check:** Look for content in sources that should be in the deliverable but isn't
4. **Contradiction check:** Compare claims against other docs/ files for conflicts
5. **Cross-reference check:** Verify all references to other documents are correct (file exists, section exists)
6. **Format check:** Status line present, header structure matches convention, citations formatted correctly

### QA Verdicts

| Verdict | Meaning |
|---------|---------|
| PASS | All criteria met, no issues found |
| CONDITIONAL | All criteria met but minor issues noted (formatting, missing cross-refs) |
| FAIL | One or more acceptance criteria not met — list which ones |

---

## KEY FILES

Read these to understand current repository state:

| File | Purpose | Read When |
|------|---------|-----------|
| WORKFLOW.md | Operating manual — rules, roles, processes | First session action |
| planning/architecture-governance-summary.md | Current state: what's approved, what's blocked, what's next | Starting any new work |
| planning/consistency-remediation-plan.md | 30 known issues with implementation tickets | Before editing any docs/ file |
| planning/knowledge-base-consistency-audit.md | Audit findings — what's wrong and why | Before editing any docs/ file |
| planning/repository-audit.md | File-level audit — duplicates, orphans, naming issues | Before any repo cleanup |
| planning/repository-source-map.md | Where source material lives | When building new documents |
| planning/engineering-backlog.md | 128 implementation tasks for Shopify build | When starting Shopify development |
| planning/repository-health-report.md | Measured repository metrics | For status reporting |
| docs/INDEX.md | Navigation guide to docs/ | Quick reference |
| docs/10-DECISIONS.md | Decision log + conflicts register | Before any design implementation |

---

## CURRENT STATE (as of 2026-07-13)

### What's Done
- 4 documents APPROVED (04, 05, 06, 08-LIVE-SITE-COPY-AUDIT)
- 6 documents PENDING REVIEW (01, 02, 03, 07, 09, 10)
- 7 ADRs prepared and awaiting Architect decision
- 30 consistency findings documented with remediation tickets
- 6 remediation batches defined with execution order
- Repository audit complete (578 files, ~350 duplicates identified)

### What's Blocked
- 7 ADR decisions needed from ChatGPT (ADR-01 through ADR-07)
- Shopify OS 2.0 confirmation needed
- Photography assets needed from brand team
- 5 homepage sections undecided (04, 15, 24, 25, 29)

### What's Next (recommended sprint order)
1. Submit ADR-01–07 to ChatGPT → get decisions
2. Execute Batch 6 (10 standalone fixes, no blockers)
3. Execute Batch 2 ($75→$150 fix, needs one approval)
4. Execute Batches 3–5 (cross-refs, dedup, formatting)
5. Execute Batch 1 (token reconciliation, after ADR decisions)
6. Begin Shopify theme development (per engineering backlog)

---

## PITFALLS TO AVOID

### Content Rules
- **Never modify APPROVED documents** without explicit Architect approval — even "minor" fixes
- **Never report estimated counts** — measure directly from the repository or don't report
- **Never summarize when lossless is required** — if the source has 50 items, the output has 50 items
- **Never commit planning/ files** — they are working documents, not production content
- **Never invent content not in sources** — if it's not in a cited source, it doesn't go in the document

### Process Rules
- **Never skip self-audit** — verify every acceptance criterion before reporting done
- **Never batch unrelated changes** in one commit — one deliverable, one commit
- **Never assume file contents** — read the file before editing it
- **Never change WORKFLOW.md** without CEO approval
- **Never approve your own work** — only the Architect grants APPROVED status

### Technical Rules
- **Never hardcode values** that should come from design tokens
- **Never use $75** for free shipping — it's $150 (resolved per C-010)
- **Never reference docs/07 for structured data** — it's a raw HTML archive, not structured content
- **docs/08 collision** — two files share the 08- prefix; always use the full filename
- **planning/ files are ephemeral** — they support the process but are not the product

### Common Mistakes from Prior Sessions
- Reporting counts without measuring (e.g., "approximately 30 findings" when the audit has exactly 30)
- Editing an APPROVED document to fix a "typo" without realizing it requires Architect approval
- Building a document from memory of a prior session instead of reading the actual source files
- Committing planning/ files alongside docs/ files
- Using the warm color palette (#f9f7f2) instead of the production tokens (#f9f9f9) — this is the subject of ADR-01

---

## QUICK START FOR A NEW AI AGENT

```
1. Read WORKFLOW.md (the operating manual)
2. Read planning/AI-OPERATIONS-MANUAL.md (this file)
3. Read planning/architecture-governance-summary.md (current state)
4. Read the sprint ticket assigned by the CEO
5. Gather all source files listed in ticket dependencies
6. Execute the build
7. Self-audit against acceptance criteria
8. Commit + push
9. Report completion
```

If no sprint ticket is assigned, ask the CEO: "What's my next ticket?"

Do not explore, reorganize, or improve the repository without a ticket. Every action traces to an assignment.

---

**END OF AI OPERATIONS MANUAL**
