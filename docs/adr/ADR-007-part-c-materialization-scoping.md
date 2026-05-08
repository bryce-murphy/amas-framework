---
adr_id: ADR-007
title: Part C materialization scoping decision — amends ADR-006 D2 batch sequence
status: Accepted
date: 2026-05-07
amends: ADR-006 (Decision 2 partial-supersession; further partial-supersession after ADR-003 Decision 2 partial-supersession at ADR-006)
supersedes: none
superseded_by: none
---

# ADR-007 — Part C materialization scoping decision

## Status

Accepted — 2026-05-07. Amends ADR-006 Decision 2 (further partial-supersession; ADR-007 inserts Part C.1 + Part C.2 batches into the canonical batch sequence). ADR-006 Decisions 1, 3, 4 preserved unchanged.

## Context

ADR-006 Decision 2 canonicalized the v3.0.0 ship batch sequence as Batch P1 (process templates) through Batch P8 (final adoption preparation), with each batch landing in 1-N substantive cycles. ADR-006 D2 did not address Part C materialization — the canonical-law-Part-C sections of `core.md` that are forward-referenced from canonical-law-Part-A + Part-B + just-shipped templates with `(forthcoming at Part C+)` qualifier convention introduced at TASK-0024 (PR-29).

Empirical state of substrate-fallback debt at TASK-0028 close (post-PR-37 ship), confirmed by TASK-0029 Builder pre-flight enumeration (2026-05-07) with strict-literal canonical pattern correction at Codex post-PR pass-2 (2026-05-08):

- **Form (a) — explicit `(forthcoming at Part C+)` qualifier markers**:
  - **Canonical sub-variant**: 35 strict-literal `(forthcoming at Part C+)` matches across 28 distinct lines on canonical-tracked surfaces (`usage-guide.md` 27 instances / 20 lines; `templates/handoff-template.md` 5 instances / 5 lines; `CLAUDE.md` 2 instances / 2 lines; `AGENTS.md` 1 instance / 1 line). The canonical-law trio (`core.md` + `github-reference.md` + `usage-guide.md`) + operating-instruction surfaces (`AGENTS.md` + `CLAUDE.md`) + just-shipped Batch P1 templates (`templates/handoff-template.md` + `templates/review-template.md`) contain the canonical-tracked qualifier population. **This is the canonical baseline that downstream Part C.1 / Part C.2 cleanup-sweep cycles will verify against** (strict-literal `(forthcoming at Part C+)` pattern).
  - **Syntactic sub-variant**: 2 additional instances at `templates/handoff-template.md` L142 (`...substrate (forthcoming at Part C+ in v3 core.md)`) and L150 (`(handoff schema; forthcoming at Part C+)`) carry the qualifier inside extra-context parenthetical groupings; semantically equivalent substrate-fallback debt; require extended pattern at cleanup-sweep cycles (separate handling beyond strict-literal sweep).
- **Form (b) — unmarked forward-references**: forward-references to Part C sections that cite §X.Y without the explicit qualifier marker (e.g., §13.2 + §17.7 + §23.6.5 in spec / handoff / review-context cycle artifacts). These are similarly resolved at Part C ship cycles.
- 9 distinct Part C sections forward-referenced: §8.2 pre-flight + §8.3 stop-and-show + §13 AI Session Log (with §13.1 in-cycle session records / §13.2 post-handoff cycle-close content) + §14 universal handoff schema (with §14.1-§14.7 direction variants) + §17.5 template lifecycle + §17.7 review template canonical + §10.5 single-contributor bypass + §23.6.5 session-budget hand-back + scattered §2.X / §3.X / §5.4 references.

Without architectural decision on Part C materialization, Part C decisions happen by ad-hoc accretion: each cycle that touches a §X.Y reference adjudicates whether to materialize. This reproduces the exact anti-pattern ADR-006 was authored against (§Context "the same defect class ADR-003 was authored to mitigate in PR-7 — recurrence in the same project after 26 cycles is itself evidence of cadence drift").

ADR-006 D2 batch sequence does not include Part C cycles. Future Batch P1+ continuation cycles (post-merge-note-template + ADR-template + role-scorecard + feature-brief + project-brief + tool-inventory + surfaces-manifest = 7 remaining Batch P1 stubs) reference Part C sections via `(forthcoming at Part C+)` qualifier; substrate-fallback debt compounds with each unfilled-template-cycle until Part C ships.

ADR-007 addresses the gap by inserting Part C.1 + Part C.2 batches into the canonical batch sequence between Batch P1 (process templates; in flight) and Batch P4 (Actions; downstream).

## Decision

### Decision 1 — Acknowledge Part C as architectural gap not addressed by ADR-006 Decision 2

ADR-006 D2 batch sequence Batch P1-P8 covers framework-package-level batches authored AFTER `core.md` Parts A and B were shipped at earlier substantive cycles: process templates (P1; 9 files including tool-inventory + surfaces-manifest) + GitHub-artifact templates (P2; templates/AGENTS.md + templates/CLAUDE.md + PR_TEMPLATE + 4 ISSUE_TEMPLATEs) + prompts (P3; greenfield + retrofit + upgrade) + Actions (P4; 9 canonical scaffold workflows) + flat appendices (P5; mcp-integration + others, 7 files) + project-type appendices (P6; 5 files) + receiving-surface adapter packs (P7; 7 files) + v3.0.0 release tag + final README polish (P8). canonical-law-Part-A and canonical-law-Part-B (substantive `core.md` content) shipped at earlier substantive cycles (PR-13 Part B, prior PRs Part A) and are not enumerated in ADR-006 D2. Part C (canonical-law-Part-C; `core.md` §X.Y sections forward-referenced from Parts A+B and from templates) is INTERNAL to `core.md`, not a separate framework-package batch, and is NOT enumerated in ADR-006 D2.

This ADR records that omission as architectural gap. Without explicit Part C scoping, Part C materialization happens by ad-hoc accretion at each Batch cycle that touches a §X.Y reference — exact anti-pattern ADR-006 was authored against.

### Decision 2 — Split structure for Part C content

Part C content splits into two batches per dependency-grounding analysis:

**Part C.1 — Cycle-execution canonical surfaces** (referenced by templates + cycle artifacts):

- `core.md` §14 universal handoff schema
- `core.md` §14.1-§14.7 direction-specific variants (Architect → Builder, Builder → Reviewer, Reviewer → Builder, Reviewer → Architect, Builder → Architect, Human → AI, AI → Human)
- `core.md` §17.5 template lifecycle canonical
- `core.md` §17.7 review template canonical

**Part C.2 — Operating-discipline canonical surfaces** (referenced by operating-instruction surfaces + Actions):

- `core.md` §8.2 pre-flight discipline
- `core.md` §8.3 stop-and-show discipline
- `core.md` §13 AI Session Log discipline (with §13.1 in-cycle session records / §13.2 post-handoff cycle-close content)
- `core.md` §10.5 single-contributor bypass posture
- `core.md` §23.6.5 session-budget hand-back discipline

Other forward-referenced sections (`core.md` §2.2.2, §2.3.4, §2.3.6, §2.3.7, §3.1, §5.4) fold into appropriate Part C member per topic; folding adjudicated at Part C.1 / Part C.2 substantive-content cycle authoring per discipline coupling.

### Decision 3 — Schedule

- **Part C.1 lands BEFORE remaining Batch P1 templates** — grounds cycle-execution canonical surfaces being authored at Batch P1 continuation cycles. Remaining Batch P1 templates (post-merge-note-template + ADR-template + role-scorecard + feature-brief + project-brief + tool-inventory + surfaces-manifest = 7 templates) reference §14 / §17.5 / §17.7 via `(forthcoming at Part C+)` qualifier; Part C.1 ship drops qualifier across just-relevant surfaces.

- **Part C.2 lands BEFORE Batch P4 Actions** — grounds Actions enforcement of operating-instruction surface disciplines. Actions (§8.1 / §8.2 / §13 / §10.5 referenced) require canonical-text grounding before deterministic-enforcement layer materializes.

- **Per-cycle distributed-update sweeps** drop `(forthcoming at Part C+)` qualifier across just-relevant surfaces at each Part C ship cycle (smaller per-cycle sweeps than single late sweep).

### Decision 4 — Cycle-bandwidth expectation

- **Part C.1 expected cycle-bandwidth**: ~1 substantive cycle (~250-350 source lines new canonical text; comparable to PR-13 Part B scope at MAXIMUM-salience cycle precedent).
- **Part C.2 expected cycle-bandwidth**: ~1 substantive cycle (~150-250 source lines new canonical text).

Anticipation per established §23.6.3 sub-shape A discipline; actual bandwidth tracked at MC-A monitoring item per cycle.

## Alternatives considered

### (A) Substrate-fallback-acceptable-through-v3.0.0-ship

Rejected. Adopter-readability concern (qualifier instances confuse adopters reading canonical-law trio + templates) + qualifier-sweep debt accumulation pattern (each cycle adds qualifiers; deferred sweep cost compounds).

### (B) Ad-hoc accretion at each Batch cycle

Rejected. Anti-pattern reproduction (each cycle adjudicates Part C materialization fragment without architectural framing). Exact pattern ADR-006 was authored against.

### (C) Defer Part C entirely to post-v3.0.0 patch versions

Rejected. Adopter-readability at ship requires Part C materialized + qualifier-cleanup before v3.0.0 release. Patch versions for Part C ship would require v3.0.0 to ship with substantial qualifier residue, weakening adopter readiness.

### (D) Full Part C in single substantive cycle

Rejected. Density concern per TASK-0027 / PR-13 dense-cycle precedent (130 lines new canonical text + 23 cycle defects = empirical density ceiling). Full Part C ~400-600 source lines exceeds single-cycle density tolerance.

### (E) Different Part C split structure

Architect-adjudicated at this ADR per Decision 2 split. Alternative splits (e.g., template-grounding-vs-action-grounding split + standalone §13 AI Session Log batch) considered but rejected for grouping coherence at substantive-content batch level. Owner override at TASK-0030+ scoping if alternative emerges as preferable.

## Consequences

- **ADR-006 Decision 2 batch sequence amended** to insert Part C.1 within P1 (after handoff-template + review-template ship at PR-35; before remaining 7 P1 templates that reference §14 / §17.5 / §17.7 via `(forthcoming at Part C+)` qualifier) and to insert Part C.2 between P3 (prompts) and P4 (Actions). Effective batch sequence: P1 (process templates; 2 of 9 filled at PR-35) → C.1 (cycle-execution canonical surfaces) → P1[remaining 7 templates] → P2 (GitHub-artifact templates) → P3 (prompts) → C.2 (operating-discipline canonical surfaces) → P4 (Actions) → P5 (flat appendices) → P6 (project-type appendices) → P7 (receiving-surface adapter packs) → P8 (release tag + final README polish).

- **README "Roadmap" paragraph updated** to reflect Part C.1 + Part C.2 schedule; preserves ADR-003 + ADR-006 cross-references; adds ADR-007 cross-reference. Single-paragraph update per ADR-006 Decision 4 distributed-update discipline + Item 14 retroactive-supersession-marking sub-rule.

- **Expected v3.0.0 ship cycle-count revised** — Part C.1 + Part C.2 add ~2 substantive cycles vs ADR-006 D2 implicit count; adopter-readiness-at-ship preserved.

- **TASK-0030 begins Part C.1 substantive content materialization** per Decision 3 schedule. Part C.1 cycle = first execution of Decision 4 cycle-bandwidth expectation (~1 substantive cycle ~250-350 lines).

- **Per-cycle distributed-update sweeps** at Part C.1 + Part C.2 ship cycles drop `(forthcoming at Part C+)` qualifier across just-relevant surfaces. Smaller per-cycle sweeps than single late sweep.

- **`templates/handoff-template.md` + `templates/review-template.md`** (PR-35 ship) reference §14 / §17.5 / §17.7 via `(forthcoming at Part C+)` qualifier; Part C.1 ship cycle distributed-update drops qualifier at template surfaces.

- **Adopters of pre-v3.0.0 amas-framework** see ADR-007 alongside ADR-006 as the current canonical batch sequence reference; ADR-006 D2 partially superseded for batch sequence portion only (D1 + D3 + D4 preserved).

- **UPCDS adoption** of amas-framework v3.0.0 unaffected by this ADR per ADR-003 §Consequences UPCDS-side-ADR convention (preserved through ADR-006).

## Cross-references

- **ADR-001** decisions 1-7, 9-15 unchanged; decision 8 PR sequence portion superseded by ADR-003 (preserved); ADR-001 §Status field unchanged.
- **ADR-002** Decision 3 anticipation pattern; ADR-002 Status field unchanged per amendment convention.
- **ADR-003** Decision 1 (v3.0 ship scope) preserved; Decision 2 (PR plan) partially superseded by ADR-006; Decision 3 (TASK reservation + PMN insertion budget) preserved; §Consequences distributed-update discipline preserved.
- **ADR-004** linked-pr-fix-up Action; preserved through ADR-006 + ADR-007.
- **ADR-005** branch convention canonicalization + partial-supersession-via-deliberate-divergence precedent; ADR-007 follows same partial-supersession pattern.
- **ADR-006** Decision 1 (gap diagnosis) preserved; Decision 2 (batch sequence) further-partially-superseded by this ADR's Decision 2 (inserts Part C.1 + Part C.2); Decision 3 (lightweight-absorption framework) preserved (this ADR is architectural-class, NOT lightweight-absorption); Decision 4 (distributed-update discipline + Item 14 retroactive-supersession-marking sub-rule) preserved (this ADR's §Consequences applies it).
- **PMN-001** through **PMN-010** post-merge learning evidence; no PMN canonicalized at ADR-007 ship.
- **Transition plan v0.2** §3 / §10 package structure + UPCDS-relative PR sequence (preserved through ADR-006 + ADR-007).
- **FEAT-0001** PR-2 v3 framework package scaffold — the 50-stub enumeration whose `filled_by` values continue to point at canonical plan reference (now ADR-006 + ADR-007 for unfilled stubs at content-fill time per Decision 4 distributed-update discipline + Item 14 retroactive-supersession-marking sub-rule).
- **TASK-0029 (this PR)** — first cycle executing ADR-007 ship; Part C.1 / Part C.2 schedule effective at TASK-0030+.
