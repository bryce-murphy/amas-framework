---
task_id: TASK-0021
title: three-endpoint poll canonicalization (core.md §8.1.1.1) + PMN-009 (i.5) discipline canonicalization-candidate
pr: PR-25
branch: feat/task-0021-three-endpoint-poll-canonicalization
linked_predecessor: TASK-0020 (PR-23 substantive defect-fix + PR-24 auto-generated chore-fix-up)
linked_successor: TBD
linked_pr: PR-25 (Builder fills with squash SHA post-merge per PMN-001 (k))
framework_version_dogfooded: AMAS v2.18.1
production_target: AMAS v3.0
spec_source: .claude/session-handoffs/TASK-0021-spec.md (gitignored per ADR-001 decision 15)
date_authored: 2026-05-04
status: active
---

# HANDOFF: TASK-0021

## Metadata

- Task ID: TASK-0021 (matches PR-25 anticipated; absorbs PMN-008 §5.8 (h.4) recommendation; ships PMN-009)
- Linked Issue: none
- Linked PR: PR-25 — https://github.com/bryce-murphy/amas-framework/pull/25
- Linked ADR(s): ADR-001 decision 11 (owner-invokes Codex); ADR-003 (decision 2 canonical sequencing; decision 3 contingency slots — slot consumption deferred per ledger Item 1 reconciliation)
- Linked PMN(s): PMN-006 (§8.1.1.1 (h.3) lexicographic OR form precedent); PMN-008 §5.8 (h.4) (recommendation absorbed by this cycle); PMN-009 (this cycle ships)
- Owner role: Builder (Claude Opus 4.7, Claude Code, owner's local session)
- Previous role: Architect (Claude Opus 4.7, Claude.ai Project)
- Timestamp (UTC): 18:53
- Last synced commit SHA: `a88b410` (PR-24 squash; TASK-0020 auto-generated chore-fix-up). Verified at pre-flight 2026-05-04 against `git rev-parse origin/main`; main HEAD has not advanced past PR-24 squash.
- Branch: `feat/task-0021-three-endpoint-poll-canonicalization` (Builder verifies type-prefix conformance against TASK-0019 + TASK-0020 priors at pre-flight per (i.5) batch)
- Status: active

## Objective

Ship a substantive-content cycle with three coupled deliverables:

1. **core.md §8.1.1.1 amendment** — canonical-text correction absorbing PMN-008 §5.8 (h.4) recommendation matured across 8 cycles' empirical evidence (PR-11/13/15/17/19/21/23/24). Surgical addition of `pulls/{pr}/comments` as third polling endpoint to the existing two-endpoint canonical text; refinement of (h.4) pattern note (substantive verdict can land at any of the three endpoints, not always endpoint 3); update settling-period rule to cover all three endpoints. Surgical-or-defer guard per PMN-006 precedent: if amendment requires surrounding prose restructuring, defer to follow-up cycle.

2. **PMN-009 authoring** — (i.5) Architect-spec-drift catch discipline canonicalization-candidate documentation. Field evidence: 4 cross-cycle confirmations of the (i.5) Builder pre-flight batch catching Architect-spec-authoring drift across distinct sub-shapes (frontmatter convention, structural-element count, line-number references, ADR form). Proposed canonical refinement: §23.6 sub-rule addition for Architect-side reference-verification discipline; canonical absorption deferred to TASK-0022+ per PMN-evidence-then-absorption cadence (PMN-005 precedent).

3. **Operational hygiene + version bump** — `.gitignore` `__pycache__/` addition (cycle-close ledger Item 14); README.md Class A canonical-version-of-record bump v2.18.1 → v2.19 per §18.4 substantive-reading minor criterion (new canonical text + new PMN; clear minor tier).

Architect-level review of this scope completed at TASK-0020 cycle close. Both substantive contents have empirically-overdetermined evidence threshold (h.4 at 8 cycles; (i.5) at 4 confirmations). Surgical-or-defer guard on §8.1.1.1 amendment is the primary risk; PMN-009 authoring-only discipline (no canonical absorption this cycle) is the primary scope-discipline guard.

## Last completed step

Architect Phase 1 scoping completed (this session, 2026-05-04):
1. PR-23 (TASK-0020 defect-fix) merge state at `39b700e`; PR-24 (TASK-0020 chore-fix-up) at `a88b410` (current main HEAD).
2. Cycle-close ledger 16 items absorbed; items 4 + 8 + 14 promoted to TASK-0021 scope; items 13 + 15 + 16 deferred.
3. Q1 bundling adjudication: bundled — PMN-009 + core.md §8.1.1.1 amendment co-ship in single PR per cross-reference structure (the (i.5) discipline at Builder pre-flight surface is structurally adjacent to (h.4) discipline at Reviewer-output absorption surface; both sit in Builder receiving-side verification cluster).
4. Q2 operational hygiene adjudication: item 14 (`__pycache__/` gitignore) included; items 15 (Action title-template refinement) + 16 (`prompts/cycle-close.md`) deferred.
5. PMN-009 absorption discipline: documents field evidence + proposes canonical refinement; canonical absorption deferred to TASK-0022+ per PMN-005 precedent.
6. Surgical-or-defer guard on §8.1.1.1 amendment: surgical addition of third endpoint should not require surrounding prose restructuring; if it does, Builder defers to follow-up cycle and surfaces at handback.
7. Version bump tier: v2.18.1 → v2.19 minor per §18.4 (new canonical text + new PMN).
8. M-A7 instance count: PR-25 = 9th empirical instance per `PR-9 + PR-10 + PR-11 + PR-13 + PR-15 + PR-17 + PR-19 + PR-21 + PR-25 = 9`. Verified by explicit enumeration before authoring per PR-17 cycle lesson. Architect performs M-A7 amendment post-merge per spec §Decisions made bullet.

## Current state

**Summary**: 6 deliverables (4 new + 2 modified). Substantive-content cycle scope (canonical-text correction + new PMN); larger than TASK-0020 defect-fix cycle. Estimated cumulative diff ~600-900 substantive lines.

**Files to be authored / modified by Builder**:

1. MODIFIED `core.md` — §8.1.1.1 amendment (third endpoint addition + (h.4) pattern refinement + settling-period rule update). Surgical scope ~10-25 lines added; surgical-or-defer guard active per spec §3 step 4.
2. NEW `docs/post-merge-notes/PMN-009-i5-architect-spec-drift-catch-discipline.md` — (i.5) discipline canonicalization-candidate documentation with 4 cross-cycle field evidence + recommended §23.6 sub-rule addition. Estimated 150-220 lines.
3. NEW `docs/handoffs/TASK-0021-three-endpoint-poll-canonicalization.md` — this handoff. ~300-380 lines.
4. NEW `docs/reviews/PR-25-codex-pre-commit.md` — Codex pre-commit review-context with claim list per §3 step 7. ~180-250 lines.
5. MODIFIED `README.md` — Class A canonical-version-of-record bump line 9 (`v2.18.1` → `v2.19`; both instances). 1-line modification.
6. MODIFIED `.gitignore` — append `__pycache__/` exclusion (item 14). 1-2 line addition.

**Files changed (anticipated diff shape)**: 4 new + 2 modified. Estimated 600-900 insertions, 4-8 deletions across modifications.

## Decisions made

- **Bundled scope**: PMN-009 + core.md §8.1.1.1 amendment co-ship in single PR per Q1 default. Two-artifact-class-per-PR exception justified by cross-reference structure: PMN-009 ((i.5) discipline at Builder pre-flight surface) and §8.1.1.1 amendment ((h.4) discipline at Reviewer-output absorption surface) are structurally adjacent (both sit in Builder receiving-side verification cluster); coupling preserves cross-reference clarity.
- **Surgical-or-defer guard on §8.1.1.1 amendment** per PMN-006 §1.1 precedent: surgical addition of third endpoint should not require surrounding prose restructuring. If amendment requires substantive restructuring (e.g., third endpoint creates ambiguity that requires prose-structure change), Builder defers and surfaces at handback. Architect cycle-close adjudication on deferred amendments.
- **PMN-009 absorption discipline**: PMN-009 documents field evidence + proposes canonical refinement (§23.6 sub-rule addition). Canonical absorption of the proposed refinement deferred to TASK-0022+ per PMN-005 precedent (PMNs propose; subsequent cycle absorbs after additional cross-cycle field evidence matures).
- **Operational hygiene scope**: item 14 (`__pycache__/` gitignore) included as trivial mechanical addition. Items 15 (Action title-template refinement) + 16 (`prompts/cycle-close.md`) deferred per Architect Q2 default.
- **Framework version bump v2.18.1 → v2.19**: minor tier per §18.4 substantive-reading minor criterion (new canonical text at core.md §8.1.1.1 + new PMN-009 ship). Class A canonical-version-of-record at README.md line 9.
- **No ADR amendments this cycle**: §8.1.1.1 amendment is canonical-text correction at core.md scope; PMN-009 authoring is observation-record at PMN scope. Neither warrants ADR amendment.
- **M-A7 increment**: TASK-0021 IS M-A7-eligible (substantive-content cycle). PR-25 = 9th empirical instance per `PR-9 + PR-10 + PR-11 + PR-13 + PR-15 + PR-17 + PR-19 + PR-21 + PR-25 = 9`. **Verify by explicit enumeration before authoring** per the PR-17 cycle close lesson. Architect performs amendment post-merge per core.md §18.3.
- **ADR-003 D3 contingency-slot accounting**: spec accounting consumes one slot (5 → 4 remaining); actual ledger reconciliation deferred per cycle-close ledger Item 1.
- **Branch type prefix `feat/`**: substantive-cycle-shape continuity from TASK-0019 + TASK-0020 priors. Confirmed default.

## Assumptions

- Repo state at TASK-0021 execution time matches handoff snapshot: HEAD of main at `a88b410` (PR-24 squash); no open PRs; branches clean. If interleaving cycle has shipped, Builder hands back per caveat-discipline ("the prompt says X; my actual finding is Y; here is the divergence").
- Codex Reviewer is operational; no §2.3.7 failover episode in flight.
- Branch protection on main is unchanged (Posture 2 — pull-request-only admin bypass via Rulesets).
- linked-pr-fix-up Action at full automation (post-TASK-0020 path-α + defect 2 fix); TASK-0021's first auto-fire on PR-25 close anticipated to fire correctly per TASK-0020 first-auto-fire empirical evidence. **Architect cycle-close note material**: TASK-0021 = second cycle of full-automation Action operation; further empirical evidence on Action's reliability at scale.
- core.md §8.1.1.1 current canonical text is two-endpoint poll form per PMN-006 (h.3) lexicographic OR form correction landed at PR-11 squash. Builder verifies at pre-flight (i.5) (c) sample-read of core.md §8.1.1.1 current state; surfaces divergence if found.
- Owner is available at step-1 stop-and-show + step-10 pre-commit stop-and-show + post-PR `@codex review` invocation gate per ADR-001 decision 11.

## Risks

- **§8.1.1.1 amendment surgical-or-defer trigger**: third endpoint addition may reveal surrounding prose ambiguity requiring restructuring. **Outcome**: Builder applies surgical-or-defer guard at step 4 authoring; if triggered, defers and surfaces at handback. Mitigation: spec §4 amendment prescription is precise (line-level prose changes named explicitly); Builder reads §8.1.1.1 current state at pre-flight before authoring.
- **PMN-009 substantive scope**: 4 cross-cycle field evidence data points + sub-shape characterization across 4 distinct sub-shapes (frontmatter convention, structural-element count, line-number references, ADR form). Substantive PMN authoring; Architect §23.6 self-review iteration count expected at 2-3 per role-axis-dependence preliminary hypothesis.
- **Two-artifact-class-per-PR exception**: bundling PMN-009 + §8.1.1.1 amendment in single PR creates cross-class coupling (Codex finding on either blocks the other; mixed scope at Codex pre-commit + post-PR review surfaces). Mitigation: clear scope separation in PR body; PMN-009 vs canonical-text-correction sections in PR-25 review-context Builder claims to verify.
- **(j) all-instances grep sweep on PMN-009 + §8.1.1.1 amendment §-cites**: substantial sweep scope (PMN-009 has cross-cycle data point references + canonical-text refinement recommendations; §8.1.1.1 amendment cross-references PMN-006 + PMN-008 + cycle-evidence). (j) discipline applies; expect 30-50 §-citations sweep total.
- **TASK-0021 first-auto-fire empirical-validation event** (PR-26 anticipated post-merge): second cycle of full-automation Action operation post-TASK-0020. Empirical evidence on Action reliability at scale. Cycle-close note material regardless of pass/fail.
- **(w) cycle-close ledger Item 6 monitoring**: TASK-0019 + TASK-0020 cycles show two sub-shapes of Codex post-PR autonomous-action emissions. PR-25 absorption may produce third-instance evidence (would cross small-PMN promotion threshold) or settle the candidate. Builder applies §8.1.1.2 verification discipline regardless.
- **Three-endpoint Codex poll discipline self-instantiation**: TASK-0021 ships canonical text for the very discipline being applied at PR-25 absorption. **Recursive self-instantiation** — PR-25 review-context absorption of Codex post-PR review IS the canonical-text-being-shipped's first canonical-application. Architect monitoring for any (h.4)-class anomalies at PR-25 absorption surface.

## Blocking questions

None at handoff time. Owner adjudication on Q1 (bundling) + Q2 (operational hygiene) absorbed at Architect Phase 1 scoping per defaults. Builder cycle proceeds mechanically modulo named stop-and-show gates.

## Validation run

- **Commands run** (pre-flight, §3 step 1):
  - `git fetch origin` ✓
  - `git checkout main` ✓ (already on main)
  - `git pull --ff-only origin main` ✓ (already up to date)
  - `git rev-parse HEAD` → `a88b410e5e70bdef043278f22253dd19ff364616` ✓ (matches metadata `a88b410`)
  - `git rev-parse origin/main` → `a88b410e5e70bdef043278f22253dd19ff364616` ✓ (reconciled)
  - `git status` → clean apart from pre-existing local-only `.github/scripts/__pycache__/` ✓ (this cycle adds to `.gitignore`)
  - `gh pr list --state merged --limit 4` → PR-24, PR-23, PR-22, PR-21 ✓ (PR-24 most-recent merged 2026-05-04T17:15:54Z)
  - `gh pr list --state open` → empty ✓
  - `core.md` exists, 331 lines pre-amendment ✓; §8.1.1.1 located at lines 23–60 of pre-amendment file ✓
  - `docs/post-merge-notes/` enumerated through PMN-008 ✓ (no PMN-009 yet)
  - `docs/handoffs/` enumerated through TASK-0020 ✓ (no TASK-0021 yet)
  - `docs/reviews/` enumerated through PR-23 ✓ (no PR-25 yet)
  - `.gitignore` exists, 15 lines pre-modification ✓
- **(i.5) convention-inference samples**:
  - (a) TASK-0019 + TASK-0020 handoff frontmatter shape = 12-field PMN-007 HEAD canonical; this handoff matches.
  - (b) PR-21 + PR-23 review-context structure = `status: drafted`/`recorded` frontmatter + Metadata section + numbered Builder claims to verify list + post-Codex output section; PR-25 review-context follows.
  - (c) core.md §8.1.1.1 current state: 38 source lines (lines 23–60); structural shape = heading + intro paragraph + endpoint enumeration + pass-shape paragraph + Builder discipline + bash block + lexicographic-explanation + --paginate + reconciliation + Anti-channel + Cross-reference. Surgical-or-defer assessment: all three §4 amendments (third endpoint addition + (h.4) refinement + PMN-008 absorption cross-reference) fit within existing structural shape with localized edits; no subsection insertion or paragraph reorder required.
  - (d) PMN-006 + PMN-008 form = frontmatter (`post_merge_note_id`, `title`, `linked_pr`, `framework_version_dogfooded`, `status`) + `# PMN-N — title` heading + `## Status` block + numbered §-sections + `## §N. Cross-references` closer; PMN-009 follows.
  - (e) README.md current state: line 9 has TWO `v2.18.1` instances (`**v2.18.1**` + `v2.18.1`); update set for v2.18.1 → v2.19.
  - (f) Class A/B/C version-marker classification: Class A scope = README.md line 9 (2 instances); Class B (operating-framework anchor at AGENTS.md / CLAUDE.md / ADR-001 — `v2.14.1`) preserved verbatim; Class C (historical / dated cross-document state in core.md / github-reference.md / ADRs / PMNs / handoffs / review-contexts / FEAT / prompts) preserved verbatim.
- **Evidence (post-edit blob hashes via `git hash-object`)**:
  - `core.md` (post-amendment + post-Codex-Blocking-fix-up at L17/L21/L72/L331): `eaab3a70caef81c044588311cae6deb7cfd8ca58`
  - `README.md` (post-v-bump): `602f010952f0e2027a00692a7bc16050dfc03801`
  - `.gitignore` (post-`__pycache__/` addition): `2ae485fb974352bf70f123bd106d30ae7404228a`
  - `docs/handoffs/TASK-0021-three-endpoint-poll-canonicalization.md`: self-hash not claimed (avoids self-referential edit-cycle); Builder enumerates structural evidence via PR-25 review-context claim 13 instead.
  - `docs/post-merge-notes/PMN-009-i5-architect-spec-drift-catch-discipline.md` (post-Codex-Major-1 §1.1 renumbering fix-up): `e9796ec44416c7e11e032264d97433ada9cb6e47`
  - `docs/reviews/PR-25-codex-pre-commit.md`: hash recorded post-Codex-output-fill at step 7; pre-Codex-fill hash captured at step 9 self-review.
  - PR-25 URL: filled at step 13 (PR-open).
- **Cumulative-diff-stats (modified-only, post-Codex-pre-commit + post-Codex-post-PR-fix-up pre-stage)**: `git diff --numstat origin/main` returns `3	0	.gitignore` + `1	1	README.md` + `25	17	core.md`; modified-only sum 29 insertions / 18 deletions. core.md decomposition: §8.1.1.1 hunk 19+/11- + Codex-pre-commit-Blocking cross-reference cluster fix-up at L17/L21/L72/L331 4+/4- + Codex-post-PR-Major Option A pass-shape rewrite 2+/2- = 25+/17- (net +8 lines; still 339 total). New-file source-line counts: PMN-009 96 + TASK-0021 handoff 430 + PR-25 review-context 269 (post-Codex-post-PR-absorption section fill) = 795 source lines. Cumulative pre-stage net: 824 insertions / 18 deletions. Snapshot at third-pre-commit-stop-and-show post-Codex-post-PR-absorption.
- **Post-edit Read-verify** (PMN-003 (f)): structural-headings counts via `grep -cE "^#"` — TASK-0021 handoff: 38; PMN-009: 10; PR-25 review-context: 8 (post-Codex-output-fill will rise modestly). All match prescription.
- **(j) sweep evidence**: per-artifact §-citation counts via `grep -nE "(core\.md|github-reference\.md|ADR-00[0-9]+|PMN-00[0-9]+|TASK-[0-9]+|PR-[0-9]+)"` — PMN-009: 28; TASK-0021 handoff: 127 (most are Architect-pre-authored spec content); PR-25 review-context: 55; core.md amendment additions: 2 (PMN-008 §5.8 reference + 8-cycle PR enumeration). Total ~212 citations across new content; each citation in newly-authored content (PMN-009 + review-context + core.md amendment) manually verified at step 9 self-review.
- **§8.1.1.1 amendment surgical-or-defer attestation**: Builder explicitly attests that the §8.1.1.1 amendment did NOT require surrounding prose restructuring. Surgical scope honored. The amendment is confined to lines 23–60 (pre-amendment) / 23–67 (post-amendment) of core.md; no subsection inserted; no paragraph reordered; structural shape preserved (heading → endpoint enumeration → pass-shape → empirical-pattern note [new paragraph; additive within existing structural shape] → Builder discipline → bash block → lexicographic explanation → --paginate → reconciliation → Anti-channel → Cross-reference). Surgical-or-defer guard NOT triggered.
- **M-A7 enumeration verification**: PR-25 = 9th empirical instance per `PR-9 + PR-10 + PR-11 + PR-13 + PR-15 + PR-17 + PR-19 + PR-21 + PR-25 = 9` (substantive-cycle PR enumeration; PR-22/PR-23/PR-24 M-A7-ineligible per defect-fix + chore-fix-up class distinction). Verified by explicit enumeration before authoring per PR-17 cycle close lesson. Architect performs the M-A7 amendment post-merge per core.md §18.3.

## Exact next step

Execute the following sequence. Hand-back point is **after PR-25 is open with placeholders substituted per §6, after `@codex review` trigger, after all three Codex endpoints settle**, before merge. Architect performs §24.3.1 five-point post-handback check before signing off for §10.5 single-contributor bypass merge.

### 1. Pre-flight verification (extended (i.5) batch)

- `cd <repo-root>`
- `git fetch origin`
- `git checkout main`
- `git pull --ff-only origin main`
- `git rev-parse HEAD` — expect `a88b410` (PR-24 squash); record actual.
- `git rev-parse origin/main` — same; reconcile against metadata Last synced commit SHA.
- `git status` — expect clean (apart from pre-existing local-only `__pycache__/` directory which this cycle adds to `.gitignore`).
- `gh pr list --state merged --limit 4` — expect PR-24 most-recent merged; PR-25 not yet open.
- `gh pr list --state open` — expect empty.
- Verify `core.md` exists; record current §8.1.1.1 line range for diff baseline.
- Verify `docs/post-merge-notes/` contains PMN-001 through PMN-008; no PMN-009 yet.
- Verify `docs/handoffs/` contains TASK-0001 through TASK-0020; no TASK-0021 yet.
- Verify `docs/reviews/` contains PR-N priors through PR-23; no PR-25 yet.
- Verify `.gitignore` exists; record current content for diff baseline.
- **(i.5) convention-inference samples** (read-only):
  - (a) Sample TASK-0019 + TASK-0020 handoffs for frontmatter shape (PMN-007 HEAD canonical 12-field) + section ordering. Compare against this handoff. Surface divergence at step-1 stop-and-show.
  - (b) Sample PR-21 + PR-23 review-contexts for frontmatter (`status: drafted`) + section ordering. Inform PR-25 review-context authoring at step 8.
  - (c) Sample core.md §8.1.1.1 current state — record exact prose + verification commands form (timestamp filter form, settling-period prose, endpoint enumeration). Inform §8.1.1.1 amendment authoring at step 4. **Particular attention to the surgical-or-defer guard**: identify exact insertion points for third endpoint addition + (h.4) refinement; surface ambiguity at step-1 stop-and-show if surrounding prose restructuring appears required.
  - (d) Sample PMN-006 + PMN-008 for PMN form (Status block, §-section structure, Honesty record + observation cluster shape). Inform PMN-009 authoring at step 5.
  - (e) Read README.md current state. Verify Class A canonical-version-of-record markers (line 9 should have `v2.18.1` × 2 instances per TASK-0020 cycle ship).
  - (f) Convention inference for current canonical version-of-record marker per Class A/B/C scheme: identify all `v2.18.1` instances; classify per scheme; propose update set for v2.18.1 → v2.19 minor bump.
- **If verification fails on any leg, hand back to Architect with the divergence stated explicitly per caveat-discipline.** Do not proceed.

### 2. Step-1 stop-and-show

Surface to owner before branch creation:

- (a) **§8.1.1.1 amendment surgical-or-defer assessment** per (i.5) (c) — does the third endpoint addition + (h.4) refinement fit cleanly without surrounding prose restructuring? Surface specific insertion points or restructuring ambiguity if found.
- (b) Convention divergence findings from (i.5) (a)/(b)/(d) — any structural form divergence between this handoff and TASK-0019 + TASK-0020, or between anticipated PR-25 review-context and PR-21 + PR-23, or between anticipated PMN-009 and PMN-006 + PMN-008.
- (c) Branch type prefix decision: spec defaults `feat/`; report TASK-0019 + TASK-0020 priors + confirm `feat/`.
- (d) Class A/B/C version-marker findings from (i.5) (f): name each marker found, classify per scheme, propose update set for v2.18.1 → v2.19 minor bump.
- (e) `.gitignore` `__pycache__/` placement decision: append at end-of-file vs. logical-section placement; surface convention.
- (f) Any other surface defects observed during pre-flight.

Wait for owner approval / direction before proceeding.

### 3. Branch creation

- `git checkout -b feat/task-0021-three-endpoint-poll-canonicalization` (or owner-directed alternate per step-2 stop-and-show).

### 4. core.md §8.1.1.1 amendment

Apply surgical amendment per §4 content prescription below. **Surgical-or-defer guard active**: if amendment requires surrounding prose restructuring beyond the named insertion points, Builder defers and surfaces at handback. Verify post-edit blob hash + structural-headings extraction.

### 5. Author PMN-009

Write `docs/post-merge-notes/PMN-009-i5-architect-spec-drift-catch-discipline.md` per §5 content prescription below. Conform to PMN-006 + PMN-008 form sampled at pre-flight (i.5) (d).

### 6. Author this handoff (TASK-0021)

Write Architect-prepared content to `docs/handoffs/TASK-0021-three-endpoint-poll-canonicalization.md` verbatim except for the named substitutions per §6 below.

### 7. Pre-commit Codex review (claim-verification)

Use the prompt template established in prior cycles' Codex pre-commit review-contexts. Builder authors PR-25-codex-pre-commit.md content with claim list:

- (a) **§8.1.1.1 amendment surgical scope honored**: third endpoint addition + (h.4) refinement applied per §4 prescription; no surrounding prose restructuring; `git diff origin/main -- core.md` shows additions confined to named insertion points.
- (b) **§8.1.1.1 third endpoint canonical form**: `pulls/{pr}/comments` polling endpoint added with parallel timestamp filter form to existing two endpoints; (h.3) lexicographic OR form preserved per PMN-006 precedent.
- (c) **§8.1.1.1 (h.4) pattern refinement**: settling-period rule covers all three endpoints; empirical-pattern note records that substantive verdict can land at any of the three endpoints (not always endpoint 3) per 8-cycle empirical record.
- (d) **PMN-009 form conformance** per PMN-006 + PMN-008 precedent: Status block + §-section structure + Honesty record + observation cluster shape match.
- (e) **PMN-009 sub-shape characterization correctness**: 4 sub-shapes (frontmatter convention, structural-element count, line-number references, ADR form) traceable to specific cycle-evidence data points; cross-cycle confirmations enumerated.
- (f) **PMN-009 canonical refinement recommendation**: §23.6 sub-rule addition for Architect-side reference-verification discipline; absorption deferred to TASK-0022+ per PMN-005 precedent (recommendation, not amendment).
- (g) **(j) all-instances grep sweep** across all artifacts: each citation verified clean against canonical source; output of `grep -nE "(core\.md|github-reference\.md|ADR-00[0-9]+|PMN-00[0-9]+|TASK-[0-9]+|PR-[0-9]+)"` for each artifact.
- (h) **Class A v-bump applied**: README.md line 9 `v2.18.1` × 2 → `v2.19` × 2; no `v2.18.1` remaining at Class A canonical-version-of-record surface.
- (i) **`.gitignore` `__pycache__/` addition**: pure-token-swap add; pre-existing entries unchanged.
- (j) **TASK-0021 handoff structural-headings count + section ordering matches TASK-0019 + TASK-0020 priors** per PMN-007 HEAD canonical 12-field frontmatter convention.
- (k) **Cumulative-diff-stats self-stability** per (e.1) sub-rule: per-file numstat sums match `git diff --staged --shortstat` total exactly; no `~`-prefixed approximate counts in any artifact.
- (l) **M-A7 enumeration verification**: PR-25 = 9th empirical instance per `PR-9 + PR-10 + PR-11 + PR-13 + PR-15 + PR-17 + PR-19 + PR-21 + PR-25 = 9`; verified by explicit enumeration per PR-17 cycle lesson.

Wait for Codex output. Record output verbatim into `docs/reviews/PR-25-codex-pre-commit.md`. Adjudicate per ADR-001 decision 11 owner-invokes convention with Architect direction:
- Blocking → hand back to Architect per PMN-001 (k); do not proceed past pre-commit gate.
- Major → surface to Architect for path-(a) revise / path-(β) record-and-proceed adjudication.
- Minor → surface to Architect; default path-(b) unless direction otherwise.

### 8. Author PR-25 review-context

Write `docs/reviews/PR-25-codex-pre-commit.md` per PR-21 + PR-23 priors at pre-flight (i.5) (b). YAML frontmatter `status: drafted`.

### 9. Builder step-6 self-review

Per PMN-008 §3 / handoff §5.2 canonical fifth surface promotion. Re-read all six placed/modified files end-to-end against the spec; check for:
- Placeholder-substitution audit (PMN-003 (d) discipline) — enumerate ALL `(Builder fills with X)` patterns across ALL files and the prepared PR body.
- Class A v-bump applied per step-1 direction.
- (j) all-instances grep sweep on all artifacts verified.
- §-citation correctness across all artifacts.
- Hash-evidence in Validation run matches actual committed blobs (PMN-002 / PMN-003 lessons).
- §8.1.1.1 amendment surgical-or-defer attestation recorded.
- M-A7 enumeration verification recorded.

Surface findings to Architect via the pre-commit stop-and-show in step 10 below.

### 10. Pre-commit stop-and-show

Surface to owner before commit:
- Step-9 self-review findings (any defects + how addressed).
- Placeholder-substitution audit per §6 + Builder-prep PR body.
- Codex pre-commit review-context state + adjudication outcomes.
- §8.1.1.1 amendment surgical-or-defer attestation.
- M-A7 enumeration verification.
- Final diff shape (`git diff --stat`).

Wait for owner approval before commit.

### 11. Commit

Single commit with message:

```
feat(amas): TASK-0021 three-endpoint poll canonicalization (core.md §8.1.1.1) + PMN-009 (i.5) discipline

Amends core.md §8.1.1.1 absorbing PMN-008 §5.8 (h.4) recommendation matured
across 8 cycles. Adds `pulls/{pr}/comments` as third polling endpoint;
refines (h.4) pattern (verdict can land at any of three endpoints, not
always endpoint 3); updates settling-period rule. Surgical scope honored.

Ships PMN-009 documenting (i.5) Architect-spec-drift catch discipline with
4 cross-cycle field evidence + recommended §23.6 sub-rule addition for
Architect-side reference-verification. Canonical absorption deferred to
TASK-0022+ per PMN-005 precedent. README.md Class A v-bump v2.18.1 →
v2.19 per §18.4 minor criterion. `.gitignore` `__pycache__/` addition
per cycle-close ledger Item 14.

PR-25 = 9th M-A7 empirical instance per explicit enumeration.

Refs ADR-001, ADR-003, PMN-005, PMN-006, PMN-008, PMN-009,
     TASK-0019, TASK-0020.
```

(Owner adjusts conventional-commits prefix per repo convention if `feat(amas):` differs from established form per pre-flight (i.5) sample.)

### 12. Push

- `git push -u origin feat/task-0021-three-endpoint-poll-canonicalization`

### 13. PR-open with placeholder substitutions complete

Use a PR body template per PR-21 + PR-23 priors. Audit ALL placeholders in the PR body before submitting `gh pr create`. Fill the Linked PR field in metadata of THIS handoff (step 6 deferred substitution) with `https://github.com/bryce-murphy/amas-framework/pull/25` once PR number assigned.

### 14. Owner invokes `@codex review`

Per ADR-001 decision 11. Substantive verdict comes via formal endpoints (Pull Request Review + line-level comments at `pulls/{pr}/comments` + issue-level comments at `issues/{pr}/comments` per §8.1.1.1 amendment-being-shipped's three-endpoint discipline). **Self-instantiation note**: PR-25 review-context absorption of Codex post-PR review IS the canonical-text-being-shipped's first canonical-application.

### 15. Three-endpoint review-state poll + re-poll discipline per amended §8.1.1.1

After `@codex review` trigger, do not assert "no findings" until either (i) at least one formal endpoint returns non-empty content, OR (ii) 5–10 minute settling period has elapsed with all three endpoints stable empty.

Three endpoints to poll (now canonical per this cycle's amendment):
- `gh pr view 25 --json reviews`
- `gh api repos/bryce-murphy/amas-framework/issues/25/comments`
- `gh api repos/bryce-murphy/amas-framework/pulls/25/comments`

### 16. Address findings if any

Path (a) revise / path (β) record-and-proceed adjudication via Architect. Treat any Blocking as escalation per PMN-001 (k). §8.1.1.2 phantom-action verification applied to any endpoint 2 issue-comment claims (cycle-close ledger Item 6 (w) monitoring continues — third-instance evidence may surface).

### 17. Hand back to Architect

Provide:
- PR-25 URL
- Codex review state via all three formal endpoints (verbatim outputs)
- Branch state (`git status`, `git log -1`, `git diff --stat origin/main..HEAD`)
- Explicit assertion of "no findings" or "findings addressed at SHA X" with all-three-endpoints-verified evidence
- Builder step-6 self-review attestation
- §8.1.1.1 amendment surgical-or-defer attestation
- M-A7 enumeration verification

Do not assert merge-readiness; that is the Architect's call after §24.3.1 five-point post-handback check.

## §4. core.md §8.1.1.1 amendment content prescription

Builder applies surgical amendment to `core.md` §8.1.1.1 per the following prescription. Conform to current canonical text form (line-level prose changes named explicitly; surgical-or-defer guard active per §3 step 4).

### Required amendments

**Amendment 1 — Add third endpoint to polling block.** Locate the existing two-endpoint polling block (per PMN-006 (h.3) lexicographic OR form correction landed at PR-11 squash). Add `pulls/{pr}/comments` as third endpoint with parallel timestamp filter form:

```
gh api --paginate repos/<owner>/<repo>/pulls/<N>/comments
```

with same lexicographic OR timestamp filter form as the existing two endpoints (per (h.3) discipline; preserved verbatim).

**Amendment 2 — (h.4) pattern refinement prose.** Update settling-period rule prose to cover all three endpoints (current canonical text covers two). Add empirical-pattern note: substantive verdict can land at any of the three endpoints, not always endpoint 3 (per 8-cycle empirical record across PR-11/13/15/17/19/21/23/24).

**Amendment 3 — Reference PMN-008 §5.8 (h.4) absorption**: cross-reference note that this amendment absorbs the PMN-008 §5.8 (h.4) recommendation matured across 8 cycles' empirical evidence.

### Surgical-or-defer guard

If any of the above amendments requires restructuring of surrounding §8.1.1.1 prose (e.g., third endpoint creates ambiguity that requires prose-structure change; (h.4) refinement requires expanding a subsection that currently doesn't exist), Builder defers the affected amendment and surfaces at handback. Architect cycle-close adjudication on deferred amendments.

Target amendment length: 10-25 lines added net (additive third endpoint + minor prose updates + cross-reference note).

## §5. PMN-009 content prescription

Builder authors `docs/post-merge-notes/PMN-009-i5-architect-spec-drift-catch-discipline.md` with the following content shape, conformed to PMN-006 + PMN-008 form (sampled at pre-flight (i.5) (d)).

### Required sections + content

**Title**: `PMN-009 — (i.5) Architect-spec-drift catch discipline canonicalization-candidate`

**Status**: Recorded — 2026-05-04. PMN-009 inserts under ADR-003 D3 contingency budget (slot accounting per cycle-close ledger Item 1 reconciliation).

**§1 Cycle context**: brief reference to TASK-0019 + TASK-0020 cycles where (i.5) discipline first surfaced as monitoring-candidate at cycle-close ledger Item 4. (i.5) discipline per PMN-007 HEAD canonical sub-extension.

**§1.1 Honesty record**: 4 distinct field-evidence data points across TASK-0019 + TASK-0020 cycles:
1. **TASK-0019 frontmatter expansion catch (cycle close evidence)** — Architect-side spec authoring of TASK-0019 spec frontmatter used 2-field form when canonical PMN-007 HEAD form is 12-field. Caught by Builder pre-flight (i.5) batch sample-read of prior TASK handoff frontmatter; Architect Item 1 path-(a) adjudication restored canonical form.
2. **TASK-0020 step-1 ADR-004 §Consequences point-count off-by-one (Builder pre-flight catch)** — Spec §3 step 6 instructed Builder to append §Consequences as point 7; actual ADR-004 had 7 points; correct append was point 8. Caught by Builder pre-flight (i.5) batch sample-read of ADR-004 current state.
3. **TASK-0020 step-1 linked-pr-fix-up.py line-number off-by-one (Builder pre-flight catch)** — Spec §3 step 4 named lines 36 + 93 for regex fix; actual file has line 35 + line 93 (line 36 is `re.MULTILINE,` argument continuation). Caught by Builder pre-flight (i.5) batch sample-read of `linked-pr-fix-up.py` current state.
4. **TASK-0020 Codex pre-commit linked-pr-fix-up.yml line-23/24 reference (Codex pre-commit catch)** — ADR-004 amendment point 8 referenced workflow `permissions: pull-requests: write` at line 23; actual file has it at line 24 (line 23 is `contents: write`). Caught by Codex pre-commit pass.

**§2 Sub-shape characterization**: 4 sub-shapes of the same root-cause class:
- **Sub-shape A (frontmatter convention divergence)**: Architect references frontmatter shape in spec; canonical convention has evolved; spec-authored shape diverges. Catch surface: (i.5) sample-read of prior cycle's handoff frontmatter.
- **Sub-shape B (structural-element count off-by-one)**: Architect references count of structural elements (sections, points, items) in spec; actual count differs from spec-authored count. Catch surface: (i.5) sample-read of canonical source current state.
- **Sub-shape C (line-number off-by-one in code references)**: Architect references specific line numbers for code modifications; actual file structure differs from spec-authored line reference. Catch surface: (i.5) sample-read of source file OR Codex pre-commit verification.
- **Sub-shape D (section-structure / form divergence)**: Architect prescribes section structure / form for new artifact; canonical priors form differs from spec-authored prescription. Catch surface: (i.5) sample-read of canonical priors form. (Empirical evidence at TASK-0019 ADR-004 form catch — spec prescribed Status / Context / Decision / Rationale / Consequences / References; canonical priors form is Status / Context / Decision / Alternatives considered / Consequences / Evidence / references.)

**§3 Common root cause**: Architect spec authoring references specific values (line numbers, structural-element counts, convention shapes, form structures) without verifying against actual canonical sources at authoring time. Architect operates from memory or partial-context at spec authoring; specific values drift.

**§4 Catch-surface analysis**: (i.5) Builder pre-flight batch is the structural catch-surface. Builder samples canonical priors + current state at pre-flight; surfaces Architect-spec-authoring drift before Builder execution. Working as designed across 4 cross-cycle confirmations. Codex pre-commit is secondary catch-surface (one of the 4 sub-shape catches).

**§5 Recommended canonical refinement**: §23.6 sub-rule addition for Architect-side reference-verification discipline. Recommendation text:

> **§23.6 sub-rule (g) — Architect-side reference-verification before spec authoring.** Before authoring spec content that references specific values (line numbers, structural-element counts, convention shapes, form structures), Architect either: (i) samples actual canonical sources to verify the referenced value, OR (ii) explicitly defers verification to Builder pre-flight (i.5) batch by marking the value as "Builder verifies at pre-flight" rather than committing to a specific value. The latter is the recommended default for line-number references and structural-element counts; the former is the recommended default for convention shapes and form structures.

Canonical absorption of this recommendation deferred to TASK-0022+ per PMN-005 precedent (PMNs propose; subsequent cycle absorbs after additional cross-cycle field evidence matures).

**§6 Anticipated forward integration**: TASK-0022+ specs apply (i.5) reference-verification discipline pre-emptively at Architect-side spec authoring. Empirical evidence on whether the canonical absorption reduces (i.5) catch surface findings (positive direction = discipline working preventively, not just reactively).

**§7 Cross-references**: PMN-005 (proposes-then-absorbs precedent), PMN-006 (§23.6 self-review canonical text), PMN-007 ((i.5) PMN-file-shape sub-extension origin), PMN-008 (§5.8 (h.4) discipline; analog cross-cycle empirical pattern), TASK-0019 + TASK-0020 (field evidence cycles).

Target length: 150-220 source lines.

## §6. Placeholder-substitution discipline (PMN-003 (d))

Enumerate ALL `(Builder fills with X)` and `(Builder updates with X)` patterns. Substitution timing classification:

| File | Field | Pattern | Timing |
|---|---|---|---|
| THIS handoff (frontmatter) | `linked_pr` | `PR-25 (Builder fills with squash SHA post-merge per PMN-001 (k))` | post-merge (Action auto-fire per TASK-0020 ship state) |
| THIS handoff (frontmatter) | `status` | `active` | post-merge (`active` → `resolved`) |
| THIS handoff (Metadata) | Linked PR | `PR-25 (Builder fills URL post-PR-open per §6)` | at PR-open (step 13) |
| THIS handoff (Metadata) | Timestamp (UTC) | `Builder fills HH:MM at handoff creation` | at handoff creation (step 6) |
| THIS handoff (Metadata) | Last synced commit SHA | `a88b410 ... Builder verifies at pre-flight` | at pre-flight (step 1) |
| THIS handoff (Validation run) | entire section | template-only | post-pre-flight + post-author + post-Codex (steps 1, 6, 7) |
| THIS handoff (Post-PR Codex review state) | entire section | template-only | post-Codex-settling (step 15) |
| THIS handoff (Sign-off) | entire section | Architect-deferred | post-§24.3.1 five-point check |
| PR-25 review-context (frontmatter) | `status` | `drafted` | post-merge (`drafted` → `recorded`) |
| PR-25 review-context | Codex output | per template | post-Codex-output (step 7) |
| PMN-009 | (no Builder-fill placeholders) | n/a | n/a (PMN authored complete at step 5) |

Builder audits this enumeration at step 9 (step-6 self-review) before commit.

## §7. Reassessment / expiry

- Hand-back gate at step 17 is the natural reassessment point. If the cycle stalls (Codex unresponsive, ambiguous review output, unexpected pre-commit findings requiring substantial revision, §8.1.1.1 amendment surgical-or-defer triggered, PMN-009 substantive scope expansion required), Builder hands back to Architect with state explicit; do not extend autonomous execution past the named hand-back point.
- TASK status flips to `resolved` only after Architect §24.3.1 five-point post-handback check clean, owner merge via §10.5, Architect M-A7 merge-commit-body amendment, and Architect confirmation of merged state.
- If TASK-0021 first-auto-fire (PR-26 anticipated) fails OR fires with incorrect substitutions, fallback is the manual chore-fix-up cycle. Cycle-close note (informal) records first-auto-fire outcome regardless of pass/fail (second cycle of full-automation Action operation post-TASK-0020 path-α + defect 2 fix).

## §8. Post-PR Codex review state

Builder fills post-Codex-review-settling per PR-21 + PR-23 review-context priors.

## §9. Sign-off

Architect §24.3.1 five-point post-handback check completed [Architect fills date]. Each of the five canonical-text-named verification points performed; record results below per established Sign-off template (TASK-0019 + TASK-0020 priors as form reference).

Anticipated check coverage at minimum:
- PR comments via all three endpoints (`pulls/{pr}/reviews` + `issues/{pr}/comments` + `pulls/{pr}/comments`) — verbatim transcription against PR-25 review-context state. **Self-instantiation**: this is the canonical-text-being-shipped's first canonical-application at the §24.3.1 verification surface.
- Branch state — three-endpoint poll evidence + commit sequence verification.
- File content against prescription — diff against this handoff's deliverable specifications, especially §8.1.1.1 amendment exact text + PMN-009 exact text.
- Phantom-action audit — Builder self-audit table verified against actual diff. (w) cycle-close ledger Item 6 monitoring continues at this surface.
- (j) all-instances grep sweep verification on PMN-009 + §8.1.1.1 amendment §-cites — re-run sweep + verify each citation against canonical source.

Architect verifies the canonical §24.3.1 fifth-point at sign-off and adjusts as needed.

Authorized for §10.5 single-contributor bypass merge per ADR-001 decision 11 admin-bypass posture.

— Architect, [Architect fills date]

## §10. Session log archive

(empty at handoff-authoring time; new task, single session expected)
