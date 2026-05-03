---
task_id: TASK-0015
title: PMN-007 PR-13 cycle learnings + core.md §8.1.1.3 cost-class refinement extension
pr: PR-15
branch: feat/task-0015-pmn-007
linked_predecessor: TASK-0012 / PR-13 (squash SHA 6086a16); TASK-0012 PMN-001 (k) chore-fix-up / PR-14 (squash SHA e6a592b)
linked_successor: TBD (next substantive cycle)
linked_pr: PR-15 (Builder fills with squash SHA post-merge per PMN-001 (k))
framework_version_dogfooded: AMAS v2.16
production_target: AMAS v3.0
spec_source: .claude/session-handoffs/TASK-0015-spec.md (gitignored per ADR-001 decision 15)
date_authored: 2026-05-03
status: active
---

# TASK-0015 — PMN-007 PR-13 cycle learnings + core.md §8.1.1.3 cost-class refinement extension

## Metadata

- TASK ID: TASK-0015
- PR: PR-15
- Branch: `feat/task-0015-pmn-007`
- Author surface: Builder (Claude Code, Claude Opus 4.7, Windows 11 + Git Bash)
- Date authored: 2026-05-03
- Linked records: PMN-001 (h.2)/(k); PMN-002 (a)/(d); PMN-003 (a)-refined/(e)-refined; PMN-004 §5 (a)-(f) + §1 4-iteration self-review; PMN-005 §2.5/§4.4 (e.1); PMN-006 §3 (g)/(h)/(i) + §5.3 bounded-continuation generalized + §3.4 frontmatter-vs-body sub-clause; ADR-001 decisions 9/11/15; ADR-003 Decision 3 (this PMN consumes a fourth contingency slot from TASK-0023-onward operational accounting; reservation ceiling at TASK-0026 preserved)
- Framework version dogfooded: AMAS v2.16
- Production target: AMAS v3.0
- Spec source: `.claude/session-handoffs/TASK-0015-spec.md` (gitignored per ADR-001 decision 15)

## Last completed step

[Filled at hand-back per Builder execution. Currently in-flight at step 4 — TASK-0015 handoff creation.]

## Current state

[Filled at hand-back. Tracked-file count post-staging expected: `96` (93 base + 3 new files: PMN-007 + TASK-0015 handoff + PR-15 review-context; core.md modification does not change count). Files changed: 4 (PMN-007 new; TASK-0015 handoff new; PR-15 review-context new; core.md modified for §8.1.1.3 cost-class sub-distinction byte-exact addition per spec §3.4).]

## Decisions made

The handoff records inherited Architect-decided scope decisions per spec §1-§4 plus in-cycle Builder-pre-flight-surfaced adjudications:

- **Phase 1 decision 1: aggressive cluster consolidation** — 16 candidate clusters (8 inherited (a)-(h) + 8 new (i)-(p)) consolidated to 8 substantive umbrellas + 3 standard structure §-sections = 11 §-headers in PMN-007. Adjudicated by Architect at TASK-0015 spec authoring per spec §1.4.
- **Phase 1 decision 4: joint canonicalization of (a) cost-class refinement + (l) bounded-iteration family composition refinement** — both refinements land at core.md §8.1.1.3 cost-class clause level via the byte-exact sub-distinction addition per spec §3.4. (g) cross-surface generalization saturation recorded in PMN text without core.md modification.
- **Phase 1 D2 (inherited from PMN-006 cycle): chore-PR denominator counting** — chore-PRs that materialize PMN-001 (k) substitution mechanism (PR-12, PR-14) are NOT separate denominator entries in M-A6; they belong to their substantive cycle's denominator entry. Pre-PMN-007: 6 PMNs / 12 substantive cycles = 50%; post-PMN-007: 7/13 = 54% within ADR-003 forecast upper bound. Per spec §1.3.
- **Phase 1 (k.3) cleanup-phase-coordination scope decision**: PMN-001 (k) execution form refinement canonicalized at PMN-007 §4 by-reference; PMN-001 text amendment deferred to PMN-008 cycle if reference-impl-level documentation needed. Light-touch canonicalization avoiding cross-document-state-verification complexity. Per spec §3.4 / §4.3 + spec §4.3 NOTE.
- **Cluster consolidation absorbing canonicalization-adjacency**: (a)/(g)/(l)/(f) → §2; (b)/(c)/(j) → §3; (e) → §4; (k) → §5; (d) → §6; (h)/M-A7/M-A8/M-A6 → §7; (o)/(p) → §8; (i)/(m)/(n) → §9. Per spec §1.4.
- **(h) candidate retirement** with explicit changelog reasoning at PMN-007: three-data-point pattern reached + canonical text at core.md §18.4 covers the discipline; further candidate-status tracking redundant with canonical text. Per spec §7.1.
- **M-A7 monitoring item retirement** — canonicalized at core.md §18.3 last cycle (PR-13). Memory-hygiene observation: monitoring memory `project_m_a7_monitoring_candidate.md` removed post-canonicalization at PR-13 cycle close. Per spec §7.2.
- **Builder pre-flight surfacing 2 spec-baseline-drift defects** — Mismatch 1 docs/post-merge-notes/ count (iter-4 self-introduced defect; (k.2) failure-mode self-instantiation); Mismatch 2 docs/reviews/ count (convention-inference gap not caught by extended pre-authoring batch). Both routed path-(a) per §8.1.1.3 cost-class refinement (pure-token-swap class). Architect applied path-(a) corrections to spec §5.1 + §10. Per spec §10 defect log + Builder pre-flight notes this session.
- **Surgical-or-defer guard on core.md §8.1.1.3 modification** (per spec §3.4 + §7): Builder reads §8.1.1.3 body (lines 115-146) to identify insertion location; if surrounding-prose restructuring would be required, defer to PMN-008 and surface stop-and-show. Adjudication at step 6.
- **No ADR amendments this cycle**. M-A6 within forecast upper bound; no ADR-004 reservation extension warranted.
- **No README modifications** this cycle. PMN cycles do not bump framework_version (the v2.16 bump landed at PR-13 not PMN-007); per ADR-003 §Consequences distributed-update discipline.

## Assumptions

- TASK-0015 is the next available TASK number per ADR-003 Decision 3 (verified at step 1 pre-flight: `git ls-files docs/handoffs/` returns 12 files TASK-0001 through TASK-0012; this handoff IS the reservation per ADR-001 decision 15 gitignored-spec convention).
- PR-15 is the next available PR number (verified at step 1: `gh pr list --state open --search "TASK-0015"` returns no results; `git log --oneline --all | grep TASK-0015` returns no merged commits).
- Base SHA `e6a592be8769a25987fb03e33559026924075727` is current `main` HEAD (squash-merge SHA of PR-14, the TASK-0012 PMN-001 (k) chore-fix-up).
- Branch protection on `main` is live and configured per ADR-001 decision 9.
- `gh` CLI authenticated with `repo` scope minimum.
- Codex desktop is available to the owner for step 8 pre-commit review per ADR-001 decision 11 owner-invokes convention.
- `core.md` exists at repo root with 21 §-header structure per spec §5.1 verification (verified at step 1 pre-flight: `grep -nE "^#{1,6} §[0-9]" core.md | wc -l` returns 21).
- `core.md` §8.1.1.3 body lines 115-146 (per spec §3.4 cited line range) are accessible for surgical addition; Builder reads body before applying byte-exact paste.
- v2.14.1 reference text unavailable at Builder surface (`amas-v2.14.1.md` absent); spec §4 canonical text for PMN-007 + §3.4 byte-exact text for core.md §8.1.1.3 are authoritative.
- Phase 1 / Phase 1.5 owner adjudications recorded in spec §1-§4 inherited; no re-litigation at session start (except Builder pre-flight defect surfacing per §8 stop-and-show pattern, which has been adjudicated path-(a) by Architect via spec corrections).
- Pre-flight per spec §5.1 confirms: 93 tracked files; clean working tree; main only branch; 21 §-headers in core.md; 7 in docs/post-merge-notes/ (corrected baseline); 12 in docs/handoffs/; 11 in docs/reviews/ (corrected baseline); 3 in docs/adr/; README "PMN file" absent; no merged TASK-0015 commit.

## Risks

- **Surgical-or-defer guard on core.md §8.1.1.3 modification** (per spec §3.4 + §7): if §8.1.1.3 cost-class refinement clause structural read reveals surrounding-prose restructuring would be required to fit the byte-exact sub-distinction clause, defer modification to PMN-008 cycle and surface stop-and-show. Mitigation at step 6: Builder reads lines 115-146 and adjudicates structural fit before applying paste.
- **PMN-007 §4.3 PMN-001 mechanism-vs-discipline canonical placement scope**: spec §4.3 records the distinction as canonicalized at PMN-007 §4 by-reference; PMN-001 text amendment deferred. If subsequent review (Codex pre-commit or post-PR) surfaces this scope decision as defective (e.g., PMN-001 text amendment is load-bearing for canonical correctness), route per §8.1.1.3 bounded-continuation rule (refined this cycle).
- **Recursive-self-instantiation in cluster recording** (per spec §7 + §5 of PMN-007 body): the cycle that records (k) cluster as preliminary observations may itself instantiate (k) cluster shapes during execution. (k.1) positive: Builder pre-flight Mismatch 1 routing applied path-(a) under (l) refinement self-instantiating the canonicalizing pattern correctly. (k.2) failure-mode: Architect iter-4 "correction" introducing Mismatch 1 is a within-spec-authoring (k.2) failure-mode self-instantiation event already absorbed into spec §10 defect log.
- **Pre-authoring verification batch (extended per (i)) as testable hypothesis** (per spec §7 risk + §9.1 PMN-007 body): if PMN-007 cycle defect count materially exceeds PR-13 cycle's 17 Architect-side baseline, the discipline composition with extended batch is empirically insufficient — PMN-008 records definitive negative evidence. Currently tracking via §1.1 honesty record material to be carried to PMN-008 cycle.
- **Bounded-continuation cost-class refinement self-application** (per spec §7 + (l) failure-mode self-instantiation): the PMN-007 cycle that canonicalizes the genuinely-asymptotic-vs-pure-token-swap distinction must apply the distinction correctly when adjudicating routing for any pre-commit / post-PR findings. Pure-token-swap cascades route path-(a); only genuinely-asymptotic cascades warrant path-(β). Mitigation: explicit cost-class adjudication framing at any path-(β) routing decision; surface adjudication reasoning in PR-15 review-context.
- **Cluster consolidation pressure vs full enumeration discipline**: 16 candidate clusters at full enumeration vs 11 §-headers at canonicalization-adjacency consolidation. If §23.6 self-review or Builder pre-flight surfaces that consolidation lost substantive material, route per §8.1.1.3 bounded-continuation rule first finding path-(a) revise cluster decomposition.
- **README PMN file table verification** (per spec §5.1 + PMN-006 §1.1 defect 9 path-(β) discipline): verified at pre-flight (`grep -in "PMN file" README.md` returns no matches); no discrepancy.

## Decision points

- **Cluster consolidation surface vs full enumeration** (per Phase 1 decision 1): 16 candidates absorbed to 11 §-headers. If Codex pre-commit or post-PR surfaces lost substantive material, path-(a) revise cluster decomposition first finding; bounded-continuation rule §8.1.1.3 (refined this cycle) applies subsequent same-class findings.
- **PMN-001 text amendment scope** (per Phase 1 (k.3) cleanup-phase-coordination scope): canonicalized at PMN-007 §4 by-reference; PMN-001 text amendment deferred. If Codex review adjudicates this as defective, path-(a) revise scope to include PMN-001 amendment per §8.1.1.3 bounded-continuation rule.
- **Surgical-or-defer guard on core.md §8.1.1.3** (per spec §3.4 + §7): Builder reads lines 115-146 at step 6; if surrounding-prose restructuring required, defer modification to PMN-008 and surface stop-and-show; deliverable count adjusts from 4 to 3.
- **Cost-class routing application in-cycle** (per spec §7 self-application risk): pure-token-swap → path-(a); genuinely-asymptotic → path-(β). Self-instantiation discipline applies (the cycle that canonicalizes the rule applies the rule correctly to its own routing).

## Exact next step

Builder continues §5 step sequence:

1. **Step 5** — Create `docs/reviews/PR-15-codex-pre-commit.md` per spec §3.3 + §6.1 verifiable claims enumeration.
2. **Step 6** — Read core.md §8.1.1.3 body (lines 115-146) to identify insertion location; apply byte-exact sub-distinction text per spec §3.4 (or defer per surgical-or-defer guard).
3. **Step 7** — Stop-and-show to owner: list staged files + diff stat + cumulative-diff-stats per (e.1) sub-rule + verification claim summary per spec §6.1.
4. **Step 8** — Owner invokes Codex desktop pre-commit review per ADR-001 decision 11; Builder absorbs findings + routes per §8.1.1.3 cost-class refinement.
5. **Step 9** — Path-(a) revisions if pre-commit findings; bounded-continuation rule §8.1.1.3 (refined) applies.
6. **Step 10** — Self-verification iterative-to-fixed-point per §23.6.2 + extended (i) pre-authoring batch.
7. **Step 11** — Commit per spec §5.11.
8. **Step 12** — Push + open PR-15.
9. **Step 13** — Owner invokes `@codex review` post-PR; Builder absorbs Codex post-PR review via two-endpoint poll per core.md §8.1.1.1.
10. **Step 14** — Path-(a) revisions if post-PR findings; bounded-continuation rule applies.
11. **Step 15** — Hand-back: Builder fills `## Last completed step` + `## Current state`; Architect §24.3.1 five-point post-handback check; owner squash-merges; merge SHA substituted into linked_pr field per PMN-001 (k); Architect updates merge-commit-body per core.md §18.3 with (k.1) positive self-instantiation surface; Architect adjudicates PMN-008 emission per cycle-summary observations.

## Reassessment / expiry

Handoff status flips to `resolved` after PR-15 is merged + linked_pr substitution + status flip per PMN-001 (k) Linked PR fix-up convention (small-chore-PR mechanism applies if branch protection requires; per spec §4 mechanism-vs-discipline distinction). If pre-commit Codex review or post-PR Codex review exceeds scope or owner declines stop-and-show, status flips to `blocked` pending Architect direction. Bounded-continuation rule applies if same-class findings recur per §8.1.1.3 (refined this cycle).

Spec source diverges from main per PMN-006 §6.1 (e) sub-rule once any path-(a) revision lands on feature branch (Architect already applied path-(a) corrections to spec §5.1 + §10 absorbing Builder pre-flight Mismatch 1 + Mismatch 2 surfacing); future cycles paste from main, not spec, per PMN-006 §6.1.
