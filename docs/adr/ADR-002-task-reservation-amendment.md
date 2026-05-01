# ADR-002 — Task Reservation Amendment for PMN-Insertion Pattern

## Status

Accepted — 2026-05-01

Amends ADR-001 decision 8 (initial TASK-0001 through TASK-0008 reservation).

## Context

ADR-001 decision 8 reserved TASK-0001 through TASK-0008 for the v3 PR sequence under the implicit assumption that the reservation would map one-to-one against substantive v3 content PRs. The actual PR sequence has accumulated two §18 post-merge-note PRs in the reservation range:

- TASK-0003 = PR-3 = PMN-001 (covering PR-1 + PR-2 production learnings)
- TASK-0004 = PR-4 = PMN-002 (covering PR-3 cycle learnings)

A third PMN PR is anticipated next (TASK-0006 = PMN-003), and the present PR (TASK-0005 = this ADR-002 amendment) consumes a fifth reservation slot before the first substantive v3 content PR is authored.

PMN-001 flagged "ADR-002 amendment" as a deferred follow-up at "PR-3 prompt time or first ADR-002 amendment." That deferral did not happen during PR-3 authoring. PMN-002 (PR-4) surfaced ADR-002 as overdue and recommended escalation. PMN-003 (PR-6, forthcoming as TASK-0006) escalates further; ADR-002 is authored as a standalone amendment ahead of PMN-003 to decouple reservation administration from PMN substantive content.

The reservation drift is itself evidence of a framework pattern: §18 post-merge-note PRs are not exceptional events; they insert into the substantive-content PR sequence as a regular feature of the project's operating cadence. The original ADR-001 reservation did not account for this insertion pattern.

## Decision

ADR-002 amends ADR-001 decision 8 as follows.

**1. Reservation extended.** TASK-0001 through TASK-0012 (was TASK-0001 through TASK-0008).

**2. Reservation accounting (as of this ADR's merge).**

| TASK | PR | Status | Type |
|---|---|---|---|
| TASK-0001 | PR-1 | merged | repo bootstrap |
| TASK-0002 | PR-2 | merged | v3 framework package scaffold |
| TASK-0003 | PR-3 | merged | PMN-001 (PR-1 + PR-2 production learnings) |
| TASK-0004 | PR-4 | merged | PMN-002 (PR-3 cycle learnings) |
| TASK-0005 | PR-5 | this PR | ADR-002 amendment (reservation extension) |
| TASK-0006 | PR-6 | anticipated next | PMN-003 (PR-3 + PR-4 review-discipline refinements) |
| TASK-0007 through TASK-0012 | PR-7 through PR-12 | future | substantive v3 content PRs (originally TASK-0003 through TASK-0008 in ADR-001 plan) |

**3. PMN-insertion pattern recognized.** §18 post-merge-note PRs are accommodated as regular reservation slots, not exceptional events. Future PMN insertions are expected and may further extend the reservation; subsequent ADR amendments will document such extensions following the same pattern as ADR-002.

## Consequences

- The six substantive v3 content PRs originally reserved as TASK-0003 through TASK-0008 (under ADR-001) are renumbered TASK-0007 through TASK-0012. PR-sequence numbering (PR-7 through PR-12) parallels.

- The PMN-#### identifier remains independent of TASK-#### per AMAS v2.14.1 §18 canonical form. ADR-002 does not alter the PMN numbering convention.

- The reservation extension does not change the substantive scope of any single PR. Each TASK slot maps to one PR with one canonical artifact class (bootstrap, scaffold, PMN, ADR amendment, or substantive v3 content).

- Future PMN-driven reservation extensions follow the ADR-002 pattern: a small standalone ADR amendment authored as a single TASK slot, ahead of the next PMN PR, decoupling reservation administration from PMN substantive content.

- ADR-001's other decisions (1–7, 9–15) are not modified by ADR-002.

## Alternatives considered

Three approaches to addressing the reservation drift were deliberated:

**Option (i) — Defer ADR-002 into the first substantive v3 content PR.** Author ADR-002 alongside the first substantive v3 content PR. Rejected because it continues the deferral pattern that PMN-001 and PMN-002 escalated — PMN-003 documents the deferral itself as the failure mode, and continuing the pattern while authoring the PMN that escalates it is structurally inconsistent.

**Option (ii) — Standalone ADR-002 PR (TASK-0005), then PMN-003 (TASK-0006).** Chosen. Ships a small standalone amendment ahead of the PMN that documents the drift. Decouples reservation administration from PMN substantive content; failure modes in either artifact do not block the other; ADR-002 ships first, allowing PMN-003 to reference ADR-002 as merged formalization rather than concurrent authoring. Cost: one extra PR cycle on a single-page amendment, judged proportionate to the robustness gain.

**Option (iii) — Combined PMN-003 + ADR-002 PR.** Single PR authoring both artifacts. Rejected because (1) it couples failure modes between two artifact classes — any Codex finding on either blocks the other; (2) it mixes artifact classes in a single PR, contrary to the project's one-artifact-class-per-PR convention; (3) the "minimum-friction" framing was the same reasoning that justified deferring ADR-002 across two prior cycles, and continuing that framing while documenting its failure mode is structurally inconsistent.

Option (ii) chosen for robustness: decoupled artifacts, single-purpose PRs, audit-trail clarity, reversal of the bundling pattern PMN-003 documents.

## Evidence / references

- **ADR-001** decision 8 (amended by this ADR)
- **PMN-001** (`docs/post-merge-notes/PMN-001-pr-0-pr-2-production-learnings.md`) — flagged ADR-002 as deferred follow-up
- **PMN-002** (`docs/post-merge-notes/PMN-002-pr-3-cycle-learnings.md`) — escalated ADR-002 as overdue
- **PMN-003** (forthcoming as TASK-0006 / PR-6) — documents PMN-insertion pattern as framework evidence; the cycle in which the reservation drift was finally formalized
- **TASK-0001 through TASK-0005** handoffs (`docs/handoffs/`)
