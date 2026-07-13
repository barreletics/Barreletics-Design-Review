# Barreletics Knowledge Base — Operating Model

**Status:** APPROVED  
**Effective:** 2026-07-13  
**Authority:** This document is the permanent operating system for this repository.

---

## Roles

- **CEO (Andrew):** Assigns work, approves deliverables, breaks ties, owns the repository
- **Lead Architect (ChatGPT):** Designs specs, reviews content accuracy, grants APPROVED status
- **Build Engineer (Cursor):** Executes builds, commits, pushes, runs audits, implements code

---

## Document Status System

Every document in this repository carries exactly one status:

| Status | Meaning |
|--------|---------|
| STUB | Document has not been built |
| BUILDING | Work in progress |
| PENDING REVIEW | Build complete, awaiting ChatGPT review |
| APPROVED | ChatGPT has explicitly approved the content |
| SUPERSEDED | Replaced by a newer document |

No document becomes APPROVED without explicit ChatGPT approval.

---

## Assignment Format: Sprint Ticket

Every assignment is a single-prompt sprint ticket:

```
ASSIGNMENT: [short name]
DELIVERABLE: [exact file path or output]
STATUS ON COMPLETION: [PENDING REVIEW or BUILDING]
SCOPE: [what's in / what's out]
DEPENDENCIES: [prior docs, data sources, URLs]
ACCEPTANCE CRITERIA: [what "done" looks like]
APPROVAL ROUTE: [ChatGPT review required? or auto-approve?]
```

One ticket per message. Build Engineer executes and reports. No multi-turn negotiation.

---

## Completion Rules

### Rule 1: Acceptance Criteria Are Law

A task is NEVER complete because the Build Engineer believes it is complete.

A task is complete ONLY when every Acceptance Criterion in the Sprint Ticket has been satisfied.

If even one Acceptance Criterion is not satisfied, the task remains BUILDING.

### Rule 2: No Unsupported Metrics

Never report counts, metrics, percentages, or statistics unless they are measured directly from the repository or source material.

- No estimates.
- No inferred counts.
- No approximations.

### Rule 3: Correct, Don't Defend

If the Build Engineer discovers during self-audit that an earlier report was incorrect, immediately correct it before reporting completion.

- Do not defend the earlier report.
- Do not justify it.
- Simply correct the work.

### Rule 4: No Invention

The Build Engineer builds from source material provided or independently verifiable. Never fabricate content.

### Rule 5: Self-Audit Before Reporting

Every deliverable is self-audited against its Acceptance Criteria before reporting done.

---

## Commit Rules

- **One commit per deliverable.** The deliverable is the atomic unit, not the conversation.
- Every deliverable ends with a commit + push.
- No orphaned work.

---

## Approval Flow

```
BUILDING ──(build complete)──> PENDING REVIEW ──(ChatGPT approves)──> APPROVED
                                      |
                                      v (ChatGPT returns with fixes)
                                   BUILDING
```

- **Auto-approve (no ChatGPT review):** Status changes, structural edits, Shopify code, git operations, tooling, workflow docs
- **ChatGPT review required:** Any document containing brand claims, product copy, strategy, or customer-facing content
- **CEO approval required:** Changes to the operating model, repository structure, or status system

---

## Parallel Work

| Can run in parallel | Cannot overlap |
|---|---|
| Doc build + Shopify theme edit | Two docs that reference each other |
| Copy audit + analytics pull | Doc build + doc restructure |
| Blog content + product data | Any two tasks editing the same file |
| MCP queries + file creation | Schema migration + code that uses schema |

---

## Workflow for Batched Tasks

```
CEO (batch planning)
  → ChatGPT (specs + acceptance criteria for next 3-5 tasks)
    → CEO (pastes one sprint ticket to Cursor)
      → Cursor (builds, self-audits, commits, pushes, reports)
        → ChatGPT (reviews if PENDING REVIEW, grants APPROVED)
          → CEO (pastes next ticket)
```

While Cursor builds task N, ChatGPT specs tasks N+1 through N+3. No one waits.

---

## Interrupts

If the CEO changes direction mid-build: say "stop" and issue a new ticket. No penalty. No justification needed.

---

## Context Between Sessions

Each session starts fresh from repository state. Git history, file contents, and this workflow persist. Prior conversation memory does not carry over unless transcripts are explicitly consulted.
