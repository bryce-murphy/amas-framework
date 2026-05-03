---
task_id: TASK-0018
title: PMN-008 PR-15 + PR-17 cycle learnings — (r) fifth review surface, (i.5) convention-inference verification, (t) two-data-point preliminary
pr: PR-19
branch: chore/task-0018-pmn-008-pr-17-cycle-learnings
linked_predecessor: TASK-0017 / PR-17 (squash SHA ce44836); TASK-0017 PMN-001 (k) chore-fix-up / PR-18 (squash SHA 52ee07e)
linked_successor: TBD (next substantive cycle, anticipated usage-guide.md / canonical-law trio third member)
linked_pr: PR-19 (Builder fills with squash SHA post-merge per PMN-001 (k))
framework_version_dogfooded: AMAS v2.17
production_target: AMAS v3.0
spec_source: .claude/session-handoffs/PMN-008-pr-17-cycle-learnings.md (gitignored per ADR-001 decision 15)
date_authored: 2026-05-03
status: drafted
---

# TASK-0018 — PMN-008 PR-15 + PR-17 cycle learnings

## Metadata

- TASK ID: TASK-0018
- PR: PR-19
- Branch: `chore/task-0018-pmn-008-pr-17-cycle-learnings`
- Author surface: Builder (Claude Code, Claude Opus 4.7, Windows 11 + Git Bash)
- Date authored: 2026-05-03
- Linked records: PMN-001 (h.2)/(k); PMN-004 §1 4-iteration self-review + §5 (a)-(f); PMN-005 §2/§2.5/§4.4 (e.1); PMN-006 §1.1/§3.1/§3.2 (g)/(h)/(i) + §5 bounded-continuation generalized + §3.4 frontmatter-vs-body sub-clause; PMN-007 §2.4 cost-class refinement + §3.1 four-surface pipeline + §8.2 (p) M-A7 amend-on-main framing; ADR-001 decisions 9/11/15; ADR-003 Decision 2 PR plan + Decision 3 TASK reservation (this PMN consumes one of four remaining contingency slots; three remaining post-PMN-008 — TASK-0025 through TASK-0027 unconsumed)
- Framework version dogfooded: AMAS v2.17
- Production target: AMAS v3.0
- Spec source: `.claude/session-handoffs/PMN-008-pr-17-cycle-learnings.md` (gitignored per ADR-001 decision 15)

## Last completed step

To be filled in pre-merge fix-up commit per (t) sub-shape (PMN-008 §2 demoted but pattern operationally applied this cycle as third data point — anticipated promotion of (t) to canonical-refinement-threshold-reached at TASK-0019 cycle if shape repeats).

## Current state

To be filled in pre-merge fix-up commit per (t) sub-shape.

Summary of `main` and feature-branch state at hand-back will record:
- `main` SHA at branch base (PR-18 squash-merge SHA `52ee07e84628a2d8e5a8ffbf5d1dc6e22b2b35b0`).
- Feature branch tip SHA at PR-open (filled at hand-back).
- Tracked-file count post-staging at first-commit (98 base + 3 new = 101).
- Files changed at first-commit (3 new: PMN-008 + TASK-0018 handoff + PR-19 review-context).
- Cumulative-diff-stats first-commit per (e.1) sub-rule (filled at hand-back).
- Hand-back fix-up commit additions to PR-19 review-context (post-PR Codex absorption section) + this handoff body (Last completed step + Current state fill) per (t) pre-merge feature-branch fix-up shape.
- PR-19 state.
- Codex post-PR review state.

## Decisions made

This cycle's adjudications, recorded for cross-cycle reference:

- **(t) demotion adjudicated at PMN-008 spec drafting**: Architect-Builder roundtrip at TASK-0018 / PR-19 step-1 surfaced that the TASK-0017-cycle-close framing of (t) as three-data-point canonical-refinement-threshold-reached had collapsed the (t)-vs-§18.3-M-A7 distinction TASK-0015 handoff explicitly preserved. Owner adjudicated path-(a) revision: PMN-008 ships with two canonical refinements ((r) + (i.5)) NOT three; (t) demotes to monitoring item §5.6 with verified two-data-point empirical evidence. Demotion record absorbed into PMN-008 §2.
- **Frontmatter convention adjudicated as PMN-007 HEAD canonical precedent** (NOT new convention): owner confirmed Architect spec authoring drifted from canonical pattern out of inattention, not design intent. Builder applied four corrections inline (frontmatter shape; linked_predecessor TASK-0013→TASK-0015; add `## Status` section; align H1 to title field) per Path 1 adjudication.
- **(v) candidate observation registered**: pattern of "self-instantiation-via-failure-and-correction at the surface canonicalizing the discipline" recorded as monitoring item §5.7. Single-cycle observation at PMN-008 authoring; promotion threshold = 2-3 cross-cycle confirmations (anticipated TASK-0019 usage-guide.md authoring as next test case).
- **Recursive empirical confirmation framing**: PMN-008's own authoring cycle becomes the strongest possible empirical evidence for (r) and (i.5) load-bearing role. The disciplines PMN-008 canonicalizes self-applied at the very next PR cycle (PR-19 PMN-008 authoring) to catch defects that escaped Architect §23.6 single-iteration sweep on PMN-008 itself. Pattern recorded in PMN-008 §1.1 and (v) candidate §5.7.
- **No core.md / [github-reference.md](github-reference.md) / README.md modification this cycle**: PMN-008 is pure post-merge note authoring (PMN file + handoff + review-context). No canonical-text changes. Branch type `chore` (not `feat`) per cycle scope.
- **Class A/B/C version-marker classification scheme placement deferred to TASK-0019**: PMN-008 §4.2 carries the verbatim scheme text forward as canonical refinement; placement within usage-guide.md vs github-reference.md adjudicated at TASK-0019 Phase 1 scoping.

## Hand-back points

Cycle hand-back to Architect at the following named points (per spec convention; populated by Builder at execution):

1. **Step-1 stop-and-show after pre-flight pre-authoring batch** — surfaced 3 §-content defects + 4 frontmatter/structure defects in Architect-drafted PMN-008 spec content; Architect revised spec inline (path-(a) for all seven); owner adjudicated each defect; Builder green-light to resume per corrected shape. ✅ Complete.
2. **Step-N stop-and-show before commit/push** (this stop-and-show; pre-§8.3 owner approval gate per CLAUDE.md): cumulative-diff-stats summary + verification claim summary + branch state + staged content review.
3. **Step-N+1 hand-back to Architect at PR-19 open** for §24.3.1 five-point post-handback check + Codex desktop pre-commit invocation per ADR-001 decision 11.
4. **Step-N+2 hand-back at post-PR Codex absorption + pre-merge fix-up commit** per (t) sub-shape — body fill of `## Last completed step` + `## Current state` + PR-19 review-context post-PR Codex absorption section. Builder pushes fix-up to feature branch; owner squash-merges per ADR-001 decision 9.
5. **Step-N+3 hand-back at PMN-001 (k) chore-fix-up cycle** post-PR-19-merge — substitute squash SHA into PMN-008 `linked_pr` field + flip PMN-008 `status: drafted` → `status: recorded` + flip TASK-0018 handoff `status: drafted` → `status: resolved`. Anticipated PR-20 chore-fix-up.

## Notes carried forward to next cycle

- (t) two-data-point preliminary (PR-15 + PR-17); third data point at TASK-0019 cycle would reach canonical-refinement-threshold-reached; PMN at that cycle proposes Builder execution steps template canonical addition.
- (u) v2.14.1-canonical-vs-repo-convention divergence watch — usage-guide.md migration sources.
- (v) self-instantiation-via-failure-and-correction watch — usage-guide.md canonicalizes operating-guidance disciplines.
- Class A/B/C version-marker classification scheme placement adjudication at TASK-0019 Phase 1 scoping.
- Branch regex reconciliation cycle deferred from PR-17 path-(β) — anticipated at TASK-0019 Phase 1 scoping or following.
- M-A6 contingency budget: 3 slots remaining post-PMN-008 (TASK-0025 through TASK-0027). Trigger event remains TASK-0023.
