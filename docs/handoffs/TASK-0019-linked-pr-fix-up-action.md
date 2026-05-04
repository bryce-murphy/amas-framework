---
task_id: TASK-0019
title: Ship linked-pr-fix-up GitHub Action — automate PMN-001 (k) chore-fix-up; ADR-004 records pre-canonical-Actions-batch insertion
pr: PR-21
branch: feat/task-0019-linked-pr-fix-up-action
linked_predecessor: TASK-0018 / PR-19 (squash SHA ddc54a4); TASK-0018 PMN-001 (k) chore-fix-up / PR-20 (squash SHA 809b9ca)
linked_successor: TBD (anticipated usage-guide.md authoring per ADR-003 D2; branch-regex reconciliation cycle deferred from PR-17 path-(β); first Action auto-fire empirical event at PR-22)
linked_pr: PR-21 (Builder fills with squash SHA post-merge per PMN-001 (k))
framework_version_dogfooded: AMAS v2.18
production_target: AMAS v3.0
spec_source: .claude/session-handoffs/TASK-0019-linked-pr-fix-up-action.md (gitignored per ADR-001 decision 15)
date_authored: 2026-05-03
status: active
---

# HANDOFF: TASK-0019

## Metadata

- Task ID: TASK-0019 (matches PR-21 anticipated; ADR-004 authored this cycle)
- Linked Issue: none — pre-canonical-Actions-batch ADR-class substantive cycle per ADR-004 (authored this cycle); ADR-001 single-contributor convention
- Linked PR: PR-21 — https://github.com/bryce-murphy/amas-framework/pull/21
- Linked ADR(s): ADR-001 (decision 11 owner-invokes Codex), ADR-003 (decision 2 canonical Actions batch sequencing; decision 3 contingency slot consumption — 5 → 4), ADR-004 (this cycle — pre-batch insertion decision)
- Linked PMN(s): PMN-001 (k) (chore-fix-up substitution discipline being automated); PMN-008 §5.8 (h.4) (three-endpoint Codex poll discipline)
- Linked Feature Brief: none
- Owner role: Builder (Claude Opus 4.7, Claude Code, owner's local session)
- Previous role: Architect (Claude Opus 4.7, Claude.ai Project)
- Timestamp (UTC): 01:25
- Last synced commit SHA: `809b9ca` (PR-20 squash; TASK-0018 PMN-001 (k) manual chore-fix-up of PR-19; verified at pre-flight 2026-05-03 against `git rev-parse origin/main`)
- Branch: `feat/task-0019-linked-pr-fix-up-action` (`feat/` prefix verified at pre-flight (i.5) (b) — TASK-0017 substantive-cycle prior used `feat/task-0017-github-reference`; TASK-0018 PMN-only prior used `chore/` per chore-class scope; TASK-0019 substantive-cycle alignment with TASK-0017 confirmed at step-1 stop-and-show; Architect adjudication confirmed)
- Status: active

## Objective

Ship the linked-pr-fix-up GitHub Action — a workflow that automates the manual PMN-001 (k) chore-fix-up substitution cycle (linked_pr placeholder + status drafted/active flips) — as a discrete pre-canonical-Actions-batch insertion documented by ADR-004. Place the two ingestion files (`.github/workflows/linked-pr-fix-up.yml` with §E1 recursion-guard refinement + `.github/scripts/linked-pr-fix-up.py` verbatim) at canonical paths; author ADR-004 (~50–100 source lines); author this TASK handoff and PR-21 review-context per established form; optionally add README.md Action-enumeration row pending deliverable-6 step-1 decision.

Architect-level review of the two ingestion files completed at light-ratification depth at TASK-0019 Phase 1 scoping. The §E1 recursion-guard refinement is the single design defect surfaced and resolved at scoping time; otherwise files are authored verbatim. Deeper review surfaces at Codex pre-commit (step-7) per ADR-001 decision 11 owner-invokes convention.

## Last completed step

Architect Phase 1 scoping completed (this session, 2026-05-03):
1. PR-19 (PMN-008) merge state ratified at `ddc54a4`.
2. Two ingestion files (`linked-pr-fix-up.yml` + `linked-pr-fix-up.py`) reviewed at light-ratification depth.
3. Three handoff §4 decisions ratified by owner: Path X (ship as TASK-0019), ADR-004 yes, (u) deferred.
4. §E1 recursion-guard tightening ratified by owner (anchored regex `^chore/task-[0-9]+-(linked-pr-fix-up|pmn-001-k)$` replaces substring match `*linked-pr-fix-up*` || `*pmn-001-k*`).
5. Architect §23.6 self-review of this handoff iterated to fixed-point prior to placement.

## Current state

**Summary**: Five required deliverables + one optional sixth (README modification, deliverable-6 decided at Builder step-1 stop-and-show per §3 below). The two largest deliverables (`.yml` + `.py`) are Architect-prepared content for verbatim ingestion modulo the §E1 recursion-guard line modification. ADR-004 content shape is fully prescribed in §4 below; Builder authors per the prescription. This handoff itself is final-form modulo the named placeholder substitutions per §5 below. PR-21 review-context Builder authors per PR-17 / PR-19 review-context priors at pre-flight per (i.5).

**Files to be authored / modified by Builder** (counted at PR diff-shape):

1. NEW `.github/workflows/linked-pr-fix-up.yml` — verbatim from Architect-attached source modulo the §E1 recursion-guard substitution (3-line modification — see §3 step 4).
2. NEW `.github/scripts/linked-pr-fix-up.py` — verbatim from Architect-attached source.
3. NEW `docs/handoffs/TASK-0019-linked-pr-fix-up-action.md` — this handoff; Builder saves verbatim except for the placeholder substitutions per §5.
4. NEW `docs/reviews/PR-21-codex-pre-commit.md` — Builder authors per PR-17 / PR-19 review-context priors at pre-flight per (i.5); claim list per §3 step 7.
5. NEW `docs/adr/ADR-004-pre-actions-batch-action-insertion.md` — Builder authors per content prescription in §4; conforms to ADR-001 / ADR-002 / ADR-003 form per pre-flight sample.
6. MODIFIED `README.md` — Class A canonical-version-of-record v-bump on line 9 (TWO `v2.17` instances → `v2.18`) applied per Architect Item 4 step-2 stop-and-show + §18.4 substantive-reading minor criterion. Action-enumeration row NOT added (deliverable-6 deferred per Architect Item 3; rationale documented in ADR-004 §Consequences point 5).

**Files changed (final diff shape)**: 5 files added + 1 file modified (README.md line 9 Class A v-bump per Architect Item 4). Cumulative insertions / deletions per (e.1) sub-rule re-derivation filled at step 10 pre-commit stop-and-show.

## Decisions made

- **Path X ratified at handoff §4.1.** TASK-0019 ships the Action as substantive cycle; consumes one ADR-003 D3 contingency slot (5 → 4). Usage-guide.md authoring slips to TASK-0020.
- **ADR-004 yes.** Pre-canonical-Actions-batch insertion is documented by a small ADR. Content shape prescribed in §4 below.
- **(u) deferral.** v2.14.1-canonical-vs-repo-convention branch-regex divergence reconciliation gets its own cycle (TASK-0020 or following). TASK-0019 scope tight to Action authoring + ADR-004.
- **§E1 recursion-guard tightening.** Substring match (`*linked-pr-fix-up*` || `*pmn-001-k*`) replaced by anchored regex (`^chore/task-[0-9]+-(linked-pr-fix-up|pmn-001-k)$`). Defect surfaced: PR-21's natural feature branch `feat/task-0019-linked-pr-fix-up-action` contains the substring `linked-pr-fix-up` and would have triggered the substring guard, suppressing the Action's first auto-fire on its own ship cycle. Anchored regex restricts the guard to `chore/`-prefixed branches matching the auto-generated chore-fix-up shape and the manual fallback shape — both of which are the actual recursive cases.
- **Branch type prefix `feat/`.** Default selection — feature-shipping work. Builder verifies against PR-17 + PR-19 parent feature branch types at pre-flight per (i.5); surfaces at step-1 stop-and-show if priors used different prefix (e.g., `adr/` or other).
- **No core.md §8.1.1.1 (h.4) canonical-text correction this cycle.** Routed path-(β); separate cycle anticipated TASK-0021 or following. Three-endpoint poll is OPERATIONAL discipline this cycle regardless of canonical-text current state, per PMN-008 §5.8 authoritative direction.
- **No github-reference.md §6.2 enumeration update this cycle.** Action insertion is documented by ADR-004 consequences; §6.2 enumeration update deferred to canonical Actions batch cycle.
- **M-A7 merge-commit-body amendment anticipated post-merge.** PR-21 = eighth empirical instance per enumeration: PR-9 + PR-10 + PR-11 + PR-13 + PR-15 + PR-17 + PR-19 + PR-21 = 8. **Verify by explicit enumeration before authoring** per the PR-17 cycle close lesson. Architect performs amendment post-merge per core.md §18.3.

## Assumptions

- Repo state at TASK-0019 execution time matches the handoff snapshot, advanced by PR-20: HEAD of main at PR-20 squash SHA, no open PRs, branches clean. Builder pre-flight verifies; if PR-20 has not yet merged, Builder hands back per caveat-discipline (state divergence stated explicitly: "the prompt says X; my actual finding is Y; here is the divergence") — TASK-0019 execution depends on PR-20 close to keep the cycle ordering canonical.
- Codex Reviewer is operational (no §2.3.7 failover episode in flight). If Codex unavailable at pre-commit step, Builder hands back per §2.3.7 pause-and-preserve-state discipline.
- Branch protection on main is unchanged from established posture (Posture 2 — pull-request-only admin bypass via Rulesets; PRs required, 1 approval, code-owner review, conversation resolution, squash-only merge).
- Owner is available at the §3 step-1 stop-and-show gate (deliverable-6 README decision + branch type prefix confirmation), at the step-6 §5 placeholder-substitution audit gate, and at the post-PR `@codex review` invocation gate per ADR-001 decision 11.
- The two ingestion files (`linked-pr-fix-up.yml` + `linked-pr-fix-up.py`) are made available to Builder at execution time (re-attached to the chat or saved to a local working directory accessible to Claude Code per handoff §2.3 owner workflow).
- Framework version bump from v2.17 → v2.18 anticipated for ADR-class substantive cycle per §18.4 substantive-reading discipline. Builder verifies at step-6 self-review per Class A/B/C version-marker classification (PMN-008 §4 / §5.3 of handoff).

## Risks

- **Action's own first auto-fire (PR-22) is the first production-validation event.** If the Action fails on its own first auto-fire, manual fallback works — owner runs the manual PMN-001 (k) chore-fix-up cycle as today. Architect-recorded design philosophy: additive, not load-bearing. PR-22 cycle will be empirical evidence; cycle close should produce a small note (informal, not necessarily a PMN) on first-auto-fire outcome regardless of pass/fail.
- **§E1 recursion-guard regex correctness.** The anchored regex `^chore/task-[0-9]+-(linked-pr-fix-up|pmn-001-k)$` was Architect-derived at scoping; Codex pre-commit treatment at step 7 will scrutinize it. If Codex surfaces an issue with the anchoring (e.g., trailing whitespace, alternate branch shapes for chore-fix-up not yet seen in the repo), Builder applies path-(a) revise / path-(b) record-and-proceed adjudication via Architect.
- **(j) all-instances grep sweep on ADR-004 §-cites.** ADR-004 references core.md / github-reference.md / ADR-001 / ADR-003 / PMN-001 / PMN-008 by §-citation. (j) discipline: enumerate all `(core\.md|github-reference\.md|ADR-00[1-3]|PMN-00[1-8])\b` instances and verify each citation against the canonical source. Defect class: stale or invented §-numbers.
- **Three-endpoint Codex poll discipline must be applied at PR-21 absorption** regardless of core.md §8.1.1.1 canonical-text current state, per PMN-008 §5.8 (h.4). The third endpoint `pulls/{pr}/comments` exposes line-level review comments that the canonical-text two-endpoint poll misses. Five-data-point empirical evidence per handoff §5.1.
- **README.md modification (deliverable 6) decision risk.** If README has no coherent Actions placement, deliverable-6 inclusion forces an ad-hoc placement decision during this cycle. Architect direction: defer if no clear placement; record deferral rationale in ADR-004 §Consequences.
- **M-A7 instance count error risk.** Pre-merge commit message authoring of "eighth empirical instance" must be verified by explicit enumeration of the prior-instance set (PR-9, PR-10, PR-11, PR-13, PR-15, PR-17, PR-19), not by trusting prior count + 1 reasoning. PR-17 cycle had a count error this discipline addresses.
- **(t) pre-merge feature-branch fix-up commit two-data-point preliminary status.** PMN-008 §5.6 monitoring; promotion trigger is third substantive-content-cycle confirmation. This cycle's outcome may produce the third data point depending on whether pre-merge fix-ups happen on the feature branch.

## Blocking questions

None at handoff time. Owner adjudication on §4 decisions + §E1 ratified at Phase 1 scoping. Builder cycle proceeds mechanically modulo the named stop-and-show gates.

## Validation run

Builder fills this section progressively across pre-flight (§3 step 1), placement (§3 step 4-6, 8), self-review (§3 step 9), and post-commit (§3 step 11+). Sub-sections below populated to current step; later-step fields explicitly named with their fill timing.

### Commands run (pre-flight, §3 step 1)

- `git fetch origin` → `From https://github.com/bryce-murphy/amas-framework / * branch main -> FETCH_HEAD`
- `git checkout main` → `Already on 'main'`
- `git pull --ff-only origin main` → `Already up to date.`
- `git rev-parse HEAD` → `809b9ca004bbb7fabb8145ede94529352703e75e`
- `git rev-parse origin/main` → `809b9ca004bbb7fabb8145ede94529352703e75e` (reconciles with metadata `Last synced commit SHA: 809b9ca` ✓; advanced from spec metadata's anticipated `ddc54a4` to PR-20 squash post-PMN-008-manual-chore-fix-up)
- `git status` → clean working tree (`On branch main / Your branch is up to date with 'origin/main'. / nothing to commit, working tree clean`)
- `gh pr list --state merged --limit 6` → PR-20 (chore/task-0018-pmn-001-k, MERGED 2026-05-03T23:32:33Z) most-recent ✓; PR-19 / PR-18 / PR-17 / PR-16 / PR-15 in expected positions
- `gh pr list --state open` → empty ✓
- Path-existence checks: `.github/workflows/` did NOT exist (state divergence vs spec §3 step 1 line 112; surfaced as defect (e.3) at step-2 stop-and-show; Architect Item 5 cycle-close-amend); `.github/scripts/` did NOT exist (consistent with spec); both created at step 4 via `mkdir -p`. `docs/adr/`: ADR-001/002/003 ✓ no ADR-004. `docs/post-merge-notes/`: PMN-001..008 ✓ no PMN-009. `docs/handoffs/`: TASK-0001..0018 with reserved-task gaps (TASK-0013/0014/0016 absent — reservation slots per ADR-002/003 not consumed by realized cycles); no TASK-0019 yet ✓. `docs/reviews/`: PR-2..PR-19 with chore-cycle gaps (PR-12/14/16/18/20 absent — chore cycles don't author review-contexts per convention); no PR-21 yet ✓.

### Convention sample reads (i.5 batch)

- **(a) TASK-0017 + TASK-0018 handoff form** — `docs/handoffs/TASK-0017-github-reference.md` + `docs/handoffs/TASK-0018-pmn-008-pr-17-cycle-learnings.md`. Frontmatter convention (PMN-007 HEAD canonical ~13 fields: `task_id` / `title` / `pr` / `branch` / `linked_predecessor` / `linked_successor` / `linked_pr` / `framework_version_dogfooded` / `production_target` / `spec_source` / `date_authored` / `status`). Section ordering: H1 + ## Metadata + ## Last completed step + ## Current state + ## Decisions made (+ ## Assumptions / ## Risks / ## Decision points / ## Exact next step / ## Reassessment / expiry for substantive cycles per TASK-0017; or ## Hand-back points + ## Notes carried forward to next cycle for chore-class cycles per TASK-0018). **Spec frontmatter divergence (2 fields vs canonical ~13) surfaced at step-2 stop-and-show as MAJOR finding (a-frontmatter); Architect Item 1 path-(a) ratified canonical-precedent expansion. Spec section-structure additions (## Objective / ## Blocking questions / ## Validation run / ## §4..§9) accepted per Architect Item 6 as substantive-cycle-shape evolution.**
- **(b) PR-17 + PR-19 review-context form** — `docs/reviews/PR-17-codex-pre-commit.md` + `docs/reviews/PR-19-codex-pre-commit.md`. PR-17 form selected as PR-21 analog (substantive-content cycle); PR-19 form not applicable (PMN-only chore-class scope).
- **(c) ADR-001 + ADR-002 + ADR-003 form** — `docs/adr/ADR-001-initial-repo-setup.md` + `docs/adr/ADR-002-task-reservation-amendment.md` + `docs/adr/ADR-003-full-package-pr-plan.md`. Canonical ADR section-form (## Status / ## Context / ## Decision / ## Alternatives considered / ## Consequences / ## Evidence / references). ADR-002 minor anomaly (Consequences-before-Alternatives) is one-off authoring artifact per PR-5 path-(a) insertion-time correction, not canonical signal (Architect Item 2 nuance). **Spec §4 ADR-004 prescription divergence (added separate Rationale section, reordered Consequences-before-Alternatives, renamed Evidence/references to References) surfaced at step-2 stop-and-show as MAJOR finding (a-ADR-004 form); Architect Item 2 path-(a) ratified alignment to canonical priors: Rationale folds into Decision, References renames to Evidence / references, Alternatives-before-Consequences ordering preserved.**
- **(d) README.md "Package layout"** — current structure: Canonical law (3) / Prompts (5) / Templates (16) / Actions (9) / Appendices flat (7) / Appendices project types (5) / Appendices receiving-surface adapters (7). "Actions (9 workflows)" entries all `actions/<name>.yml` template-distribution paths shipped at PR-15. Linked-pr-fix-up Action's `.github/workflows/` operational path is structurally distinct from template-distribution layer; deliverable-6 deferred per Architect Item 3 step-2 stop-and-show adjudication (deliverable count = 5).
- **(e) Class A/B/C version-marker classification** — Class A canonical-version-of-record: README.md line 9 (TWO `v2.17` instances). Class B historical/dated cross-document state (preserve verbatim): core.md lines ~223 (M-A7 promotion event at PR-13), ~236 (v2.13.x examples), ~238 (v2.14/v2.15 examples), ~240 (v3.0.0 anticipated reference). Class C sequence enumeration (preserve verbatim): core.md line ~234 (`v2.14.1, v2.15, v2.16, v3.0.0, ...`). CLAUDE.md `v2.14.1` operating-framework reference: NOT updated (Class B-like; preserved until v3.0 self-adoption per ADR-001 decision 8 amended). **Bump v2.17 → v2.18 ratified per Architect Item 4 + §18.4 substantive-reading minor criterion (substantive new functional content + new architectural decision).**

### Step-2 stop-and-show + Architect adjudication

Step-1 pre-flight surfaced 2 MAJOR convention-divergence findings (a-frontmatter + a-ADR-004-form) + 3 minor surface defects (e.2 spec wording inconsistency + e.3 spec wording gap + e.4 intellectual-trace verification triple-validated). All adjudicated at step-2 stop-and-show by Architect:

- Item 1 path-(a) — frontmatter expansion to PMN-007 HEAD canonical ~13 fields (this handoff applies)
- Item 2 path-(a) — ADR-004 alignment to ADR-001/003 canonical form (Status / Context / Decision / Alternatives considered / Consequences / Evidence / references; Rationale folded into Decision)
- Item 3 — README modification deferred (deliverable-6 = 5 not 6 deliverables); ADR-004 §Consequences point 5 documents deferral
- Item 4 — v2.17 → v2.18 minor bump confirmed; Class A/B/C update set per (e) above
- Item 5 — (e.2) + (e.3) spec wording defects pure-token-swap, no functional effect; Architect cycle-close item; Builder behavior unchanged
- Item 6 — section-structure additions / `## Decision points` drop / PR-17 review-context analog / M-A7 enumeration (count = 8) all confirmed
- Item 7 — Codex pre-commit claim (g) wording adjusted to make PMN-007 HEAD canonical-priors-aligned verification target explicit; claim (e) extended to assert ADR-004 canonical-form match

Architect cleared Builder past step-1 gate.

### Evidence (placed-file blob hashes via `git hash-object`)

- `.github/scripts/linked-pr-fix-up.py`: **`b8c694fb9df1d45ae43cb086431341797cf2fd9f`** (158 lines; verbatim from upload `C:/Users/BryceMurphy/Downloads/linked-pr-fix-up.py` via `cp`)
- `.github/workflows/linked-pr-fix-up.yml`: pre-§E1 `b554854df1c888996cbe6b58f025b01c448498e5` → **post-§E1 `e5d787e18334361b48f27ce069ef3b39deecb5df`** (144 lines; single-line bash conditional substitution at line 35: `[[ "$SOURCE_BRANCH" == *"linked-pr-fix-up"* ]] || [[ "$SOURCE_BRANCH" == *"pmn-001-k"* ]]` → `[[ "$SOURCE_BRANCH" =~ ^chore/task-[0-9]+-(linked-pr-fix-up|pmn-001-k)$ ]]`; 10-space leading indent + bash conditional structure preserved verbatim; surrounding `echo` lines + `$GITHUB_OUTPUT` writes unchanged)
- `docs/handoffs/TASK-0019-linked-pr-fix-up-action.md`: hash filled at final pre-commit state per (e.1) sub-rule re-derivation (step 9 / step 10)
- `docs/adr/ADR-004-pre-actions-batch-action-insertion.md`: hash filled at final pre-commit state (step 9 / step 10)
- `docs/reviews/PR-21-codex-pre-commit.md`: hash filled at final pre-commit state (step 9 / step 10)
- README.md: modified for Class A v-bump only (line 9 TWO `v2.17` → `v2.18` per Architect Item 4); Action-enumeration row NOT added (deliverable-6 deferred per Architect Item 3). Hash filled at final pre-commit state per (e.1) sub-rule.
- PR-21 URL: filled at PR-open (step 13)

### Post-edit Read-verify (PMN-003 (f))

Structural-headings extraction + cross-check filled at step 9 Builder step-6 self-review per spec §3 step 9.

### (j) sweep evidence (ADR-004 §-citations)

`grep -nE "(core\.md|github-reference\.md|ADR-00[0-9]+|PMN-00[0-9]+)" docs/adr/ADR-004-*.md` enumeration + canonical-source verification filled at step 7 Codex pre-commit + step 9 Builder step-6 self-review per spec §3 step 7 (e) + §3 step 9.

### Cumulative diff stats per (e.1) sub-rule

**Initial commit `5222c2d`** (step 11): 6 files / 1025 insertions / 1 deletion. Σ per-file = 158 (`.github/scripts/linked-pr-fix-up.py`) + 144 (`.github/workflows/linked-pr-fix-up.yml`) + 1 (`README.md` +1/-1) + 55 (`docs/adr/ADR-004-pre-actions-batch-action-insertion.md`) + 426 (`docs/handoffs/TASK-0019-linked-pr-fix-up-action.md`) + 241 (`docs/reviews/PR-21-codex-pre-commit.md`) = **1025 ✓ self-stable**.

**Fix-up commit 1 `de71e52`** (step 13 URL substitution at PR-open per §5 + (t) sub-shape pre-merge fix-up convention): 1 file / 1 insertion / 1 deletion. Σ per-file = 1 (`docs/handoffs/TASK-0019-linked-pr-fix-up-action.md` Linked PR URL substitution) = **1 ✓ self-stable**.

**Fix-up commit 2** (Codex pre-commit pass 1 absorption — 3 Blocking findings path-(a) per spec §3 step 7 adjudication): re-derived per (e.1) at fix-up commit time + recorded in commit message + this Validation run section. Cumulative-diff-stats span: ADR-004 line 48 path-(a) (anticipation-slot arithmetic harmonization) + PR-21 review-context claims 8 + 15 (h.2) verification-command updates + PR-21 review-context Adjudication / fix-up section Codex pass 1 absorption record (per PMN-002 (a)) + this handoff Validation run Evidence + Cumulative diff stats subsection populates. Verification at fix-up commit: `git diff main..HEAD --shortstat` post-fix-up-commit reports cumulative-diff-stats across all three commits since base SHA `809b9ca`.

**Verification commands** (temporally-robust per (h.2) sub-shape):
- bash (post-commit canonical): `git diff main..HEAD --stat` shows per-file insertions / deletions across all three commits on feature branch.
- bash (post-commit aggregate): `git diff main..HEAD --shortstat` returns aggregate.
- (e.1) cumulative-diff-stats re-derivation per PMN-005 §4.4: any path-(a) revision at any surface triggers re-derivation across all dependent claims; cycle's iterative-to-fixed-point convergence per §23.6.2.

### Class A v-bump applied this cycle

README.md line 9 TWO `v2.17` instances → `v2.18` applied per Architect Item 4 (Class A canonical-version-of-record; §18.4 substantive-reading minor criterion). Class A-adjacent fields applied at handoff frontmatter (`framework_version_dogfooded: AMAS v2.18`) and PR-21 review-context Metadata (`Framework version: AMAS v2.18`). CLAUDE.md `v2.14.1` operating-framework reference NOT updated (Class B-like). Diff shape revised: 5 NEW + 1 MODIFIED = 6 file changes.

### Anticipated post-merge update set (recorded for reference)

- PMN-001 (k) Action's first auto-fire at PR-22 (post-PR-21-merge): substitutes `linked_pr: PR-21 (Builder fills with squash SHA post-merge per PMN-001 (k))` → `linked_pr: PR-21 (squash SHA <sha>)` + `status: active` → `status: resolved` in this handoff; substitutes `status: drafted` → `status: recorded` in PR-21 review-context. If Action fails first auto-fire, fallback is manual chore-fix-up cycle as today.
- This cycle's commit + PR open is the first production-validation event for the Action. Action does not auto-fire on its own ship cycle (PR-21 close); it auto-fires on the NEXT substantive-content PR's close (PR-22).

## Exact next step

Execute the following sequence. Hand-back point is **after PR-21 is open with placeholders substituted per §5, after `@codex review` trigger, after all three Codex endpoints (`pulls/{pr}/reviews` + `issues/{pr}/comments` + `pulls/{pr}/comments`) settle non-empty OR a 5–10 minute settling period elapses with all three endpoints stable empty**, before merge. Architect performs §24.3.1 five-point post-handback check before signing off for §10.5 single-contributor bypass merge.

### 1. Pre-flight verification (extended (i.5) batch)

- `cd <repo-root>` (Windows: `C:\Users\BryceMurphy\repos\amas-framework`; adjust if owner's repo path has changed)
- `git fetch origin`
- `git checkout main`
- `git pull --ff-only origin main`
- `git rev-parse HEAD` — expect PR-20 squash SHA (PMN-008 manual chore-fix-up); record actual.
- `git rev-parse origin/main` — same; reconcile against metadata Last synced commit SHA.
- `git status` — expect clean.
- `gh pr list --state merged --limit 6` — expect PR-20 most-recent merged; PR-21 not yet open.
- `gh pr list --state open` — expect empty.
- `Get-ChildItem .github` (or `ls .github`) — verify `.github/workflows/` exists; confirm `.github/scripts/` does NOT exist (will be created this cycle as first script-bearing Action).
- `Get-ChildItem docs/adr` (or `ls docs/adr`) — expect ADR-001, ADR-002, ADR-003; no ADR-004 yet.
- `Get-ChildItem docs/post-merge-notes` (or `ls docs/post-merge-notes`) — expect PMN-001 through PMN-008 (8 PMNs). PR-20 chore-fix-up is anticipated to have updated PMN-008 frontmatter (status: drafted → recorded + linked_pr substitution); confirm.
- `Get-ChildItem docs/handoffs` — expect TASK-0001 through TASK-0018 with PR-20 chore-fix-up updates landed; no TASK-0019 yet.
- `Get-ChildItem docs/reviews` — expect through PR-19; no PR-21 yet (no PR-20 review-context expected — chore-fix-up cycles do not author review-contexts per established convention).
- **(i.5) convention-inference samples** (read-only):
  - (a) Sample TASK-0017 + TASK-0018 handoffs for frontmatter shape + section ordering. Compare against this handoff. Surface divergence at step-1 stop-and-show.
  - (b) Sample PR-17 + PR-19 review-contexts for frontmatter + section ordering. Inform PR-21 review-context authoring at step 8.
  - (c) Sample ADR-001 + ADR-002 + ADR-003 for ADR convention. Inform ADR-004 authoring at step 6. Particular attention to ADR-001 as form-establisher.
  - (d) Read README.md (entire file or "Package layout" / "Repo structure" / equivalent section if section-scoped). Decide deliverable-6 inclusion: if README has coherent Actions placement, include; else defer.
  - (e) Convention inference for current canonical version-of-record marker per Class A/B/C scheme (PMN-008 §4 / handoff §5.3): sample core.md / canonical-doc / latest substantive PR for current marker form. Identify framework-version-bump-from string for Class A markers (anticipated `v2.17` → `v2.18` for ADR-class substantive cycle per §18.4).
- **If verification fails on any leg, hand back to Architect with the divergence stated explicitly per caveat-discipline ("the prompt says X; my actual finding is Y; here is the divergence").** Do not proceed.

### 2. Step-1 stop-and-show

Surface to owner before branch creation:
- (a) Convention divergence findings from (i.5) (a)/(b)/(c) — any structural form divergence between this handoff and TASK-0017/TASK-0018, or between anticipated PR-21 review-context and PR-17/PR-19, or between anticipated ADR-004 and ADR-001/002/003.
- (b) Branch type prefix decision: spec defaults `feat/`; report what PR-17 / PR-19 parent branches actually used and confirm `feat/` or surface alternative.
- (c) Deliverable-6 README decision: report findings from step 1 (i.5) (d) with clear recommendation (include with row text drafted, or defer with rationale).
- (d) Class A/B/C version-marker findings from (i.5) (e): name each marker found, classify per scheme, propose update set for substantive-content cycle (anticipated v2.17 → v2.18).
- (e) Any other surface defects observed during pre-flight.

Wait for owner approval / direction before proceeding.

### 3. Branch creation

- `git checkout -b feat/task-0019-linked-pr-fix-up-action` (or owner-directed alternate per step-2 stop-and-show).

### 4. Place ingestion files

(a) **`.github/scripts/linked-pr-fix-up.py`**: write Architect-attached file content verbatim. Create directory `.github/scripts/` if not present. Verify post-write blob hash.

(b) **`.github/workflows/linked-pr-fix-up.yml`**: write Architect-attached file content with the §E1 recursion-guard substitution applied. Specifically, locate the recursion-guard step's bash conditional (lines around the comment `Recursion guard — skip if source branch is itself a fix-up`):

ORIGINAL:
```bash
if [[ "$SOURCE_BRANCH" == *"linked-pr-fix-up"* ]] || [[ "$SOURCE_BRANCH" == *"pmn-001-k"* ]]; then
```

REPLACE WITH:
```bash
if [[ "$SOURCE_BRANCH" =~ ^chore/task-[0-9]+-(linked-pr-fix-up|pmn-001-k)$ ]]; then
```

The surrounding bash structure (echo lines + `$GITHUB_OUTPUT` write) is unchanged. Verify post-write blob hash. The substitution is the ONLY modification to the .yml; if any other content needs changing, hand back.

### 5. Author this handoff (TASK-0019)

Write Architect-prepared content to `docs/handoffs/TASK-0019-linked-pr-fix-up-action.md` verbatim except for the named substitutions:

- YAML frontmatter `linked_pr` placeholder — leave as-is until post-merge (the linked-pr-fix-up Action will substitute on its own first auto-fire at PR-22, OR if Action fails the manual chore-fix-up cycle substitutes).
- YAML frontmatter `status: active` — leave as-is until post-merge (same).
- Metadata `Linked PR: PR-21 (Builder fills URL post-PR-open per §5)` — Builder substitutes the actual `https://github.com/bryce-murphy/amas-framework/pull/21` URL at PR-open time (step 13).
- Metadata `Timestamp (UTC)` — Builder fills HH:MM at handoff creation.
- Metadata `Last synced commit SHA` — Builder updates to actual `origin/main` HEAD per pre-flight if main has advanced past `ddc54a4`.
- Validation run section — Builder fills post-pre-flight + post-author per template in §"Validation run" above.
- Post-PR Codex review state section — Builder fills post-Codex-review-settling per template (existing TASK handoffs as reference).
- Sign-off section — Architect fills post-§24.3.1-five-point-check.

### 6. Author ADR-004

Write `docs/adr/ADR-004-pre-actions-batch-action-insertion.md` per the content prescription in §4 below. Conform to ADR-001 / ADR-002 / ADR-003 form sampled at pre-flight (i.5) (c). Target length: 50–100 source lines.

### 7. Pre-commit Codex review (claim-verification)

Use the prompt template established in prior cycles' Codex pre-commit review-contexts. Claims to verify (Builder-authored as PR-21-codex-pre-commit.md content; the claim list itself is Builder responsibility but should cover):

- (a) The §E1 recursion-guard regex `^chore/task-[0-9]+-(linked-pr-fix-up|pmn-001-k)$` correctly matches the auto-generated chore-fix-up branch shape (`chore/task-NNNN-linked-pr-fix-up`) AND the manual fallback shape (`chore/task-NNNN-pmn-001-k`), and DOES NOT match the parent feature branch shape (e.g., `feat/task-0019-linked-pr-fix-up-action`).
- (b) The Python script's `apply_substitutions` logic is idempotent: re-running on already-substituted content is a no-op (placeholder pattern absent → regex doesn't match → no edit applied).
- (c) The script's frontmatter-bounds parser (`parse_frontmatter_bounds`) handles markdown bodies that contain `---` horizontal-rule sequences correctly (the second `---` at file-level is the closing fence, regardless of subsequent body `---` occurrences).
- (d) The workflow's `permissions: contents: write + pull-requests: write` is the minimum permission set required for the operations performed (commit + push + `gh pr create`).
- (e) ADR-004 §-citations all resolve to canonical sources per (j) all-instances grep sweep — `grep -nE "(core\.md|github-reference\.md|ADR-00[0-9]+|PMN-00[0-9]+)" docs/adr/ADR-004-*.md` enumerated and verified.
- (f) Class A/B/C version-marker updates applied per step-1 stop-and-show direction (anticipated v2.17 → v2.18 for ADR-class substantive cycle).
- (g) This handoff structural-headings count + section ordering matches TASK-0017 / TASK-0018 priors.

Wait for Codex output. Record output verbatim into `docs/reviews/PR-21-codex-pre-commit.md`. Adjudicate per ADR-001 decision 11 owner-invokes convention with Architect direction:
- Blocking → hand back to Architect per PMN-001 (k); do not proceed past pre-commit gate.
- Major → surface to Architect for path-(a) revise / path-(b) record-and-proceed adjudication; do not proceed past pre-commit gate without direction.
- Minor → surface to Architect; default path-(b) unless direction otherwise.

### 8. Author PR-21 review-context

Write `docs/reviews/PR-21-codex-pre-commit.md` per PR-17 / PR-19 priors at pre-flight (i.5) (b). YAML frontmatter `status: drafted` (post-merge transition to `recorded` is Action / chore-fix-up cycle responsibility).

### 9. Builder step-6 self-review

Per PMN-008 §3 / handoff §5.2 canonical fifth surface promotion. Re-read all five placed/modified files end-to-end against the spec; check for:
- Placeholder-substitution audit (PMN-003 (d) discipline) — enumerate ALL `(Builder fills with X)` patterns across ALL files and the prepared PR body; for each, name substitution timing (now / at-PR-open / deferred-to-handback).
- Class A/B/C version-marker updates applied per step-1 direction.
- (j) all-instances grep sweep on ADR-004 §-cites verified.
- §-citation correctness across all artifacts.
- Hash-evidence in Validation run matches actual committed blobs (PMN-002 / PMN-003 lessons).

Surface findings to Architect via the pre-commit stop-and-show in step 10 below.

### 10. Pre-commit stop-and-show

Surface to owner before commit:
- Step-6 self-review findings (any defects + how addressed).
- Placeholder-substitution audit per §5 + Builder-prep PR body.
- Codex pre-commit review-context state + adjudication outcomes.
- Final diff shape (`git diff --stat`).

Wait for owner approval before commit.

### 11. Commit

Single commit with message:

```
feat(amas): TASK-0019 ship linked-pr-fix-up Action — automate PMN-001 (k) chore-fix-up

Adds .github/workflows/linked-pr-fix-up.yml + .github/scripts/linked-pr-fix-up.py
implementing the automated PMN-001 (k) substitution cycle. ADR-004 records the
pre-canonical-Actions-batch insertion decision per ADR-003 D3 contingency-slot
consumption (5 → 4). §E1 recursion-guard regex anchored to chore/task-NNNN-
shape per Architect Phase 1 scoping defect catch.

Refs ADR-001, ADR-003, ADR-004, PMN-001, PMN-008,
     TASK-0017, TASK-0018.
```

(Owner adjusts conventional-commits prefix per repo convention if `feat(amas):` differs from established form per pre-flight (i.5) sample.)

### 12. Push

- `git push -u origin feat/task-0019-linked-pr-fix-up-action`

### 13. PR-open with placeholder substitutions complete

Use a PR body template per PR-17 / PR-19 priors. Audit ALL placeholders in the PR body before submitting `gh pr create`. Fill the Linked PR field in the metadata of THIS handoff (step 5 deferred substitution) with `https://github.com/bryce-murphy/amas-framework/pull/21` once PR number assigned.

### 14. Owner invokes `@codex review`

Per ADR-001 decision 11. Substantive verdict comes via formal endpoints (Pull Request Review + line-level comments at `pulls/{pr}/comments`). Anti-channel signal (fast-response issue-level "Approve" stub from `chatgpt-codex-connector`) is non-authoritative per PMN-003 (c) refined.

### 15. Three-endpoint review-state poll + re-poll discipline per PMN-008 §5.8 (h.4)

After `@codex review` trigger, do not assert "no findings" until either (i) at least one formal endpoint returns non-empty content, OR (ii) 5–10 minute settling period has elapsed with all three endpoints stable empty. Single-poll OR two-endpoint check is a verification failure (the third endpoint omission is the canonical-text gap per PMN-008 §5.8 (h.4)).

Three endpoints to poll:
- `gh pr view <N> --json reviews` — formal Pull Request Reviews
- `gh api repos/<owner>/<repo>/issues/<N>/comments` — issue-level comments
- `gh api repos/<owner>/<repo>/pulls/<N>/comments` — line-level review comments (the third endpoint per PMN-008 §5.8 (h.4) — the canonical-text gap; OPERATIONAL discipline this cycle pending TASK-0021 canonical-text correction)

### 16. Address findings if any

Path (a) revise / path (b) record-and-proceed adjudication runs through Architect. Treat any Blocking as escalation per PMN-001 (k).

### 17. Hand back to Architect

Provide:
- PR-21 URL
- Codex review state via all three formal endpoints (verbatim outputs)
- Branch state (`git status`, `git log -1`, `git diff --stat origin/main..HEAD`)
- Explicit assertion of "no findings" or "findings addressed at SHA X" with all-three-endpoints-verified evidence
- Builder step-6 self-review attestation

Do not assert merge-readiness; that is the Architect's call after §24.3.1 five-point post-handback check.

## §4. ADR-004 content prescription

Builder authors `docs/adr/ADR-004-pre-actions-batch-action-insertion.md` with the following content shape, conformed to ADR-001 / ADR-002 / ADR-003 form (sampled at pre-flight (i.5) (c)). Target 50–100 source lines.

### Required sections + content

**Title**: `ADR-004: Pre-canonical-Actions-batch insertion of linked-pr-fix-up Action`

**Status**: Accepted (2026-05-03) — verify date convention against ADR-001/002/003 priors.

**Context**:
- PMN-001 (k) chore-fix-up cycle runs after every substantive-content PR merge, performing mechanical YAML-frontmatter substitutions: linked_pr placeholder + status drafted/active flips.
- Cycle is mechanical, repetitive, and high-volume: 10 instances through PR-19 (PR-1, PR-3, PR-5, PR-7, PR-9, PR-11, PR-13, PR-15, PR-17, PR-19 — Builder verifies enumeration at authoring time per PR-17 lesson). Projected 25–30 instances through canonical Actions batch ship.
- Original ADR-003 Decision 2 sequencing put all Actions into a canonical batch (anticipated TASK-0023 or following). Per ADR-003 Decision 3, contingency slots exist for substantive cycles inserted ahead of the canonical sequence.
- Owner directive at TASK-0018 cycle close: ship the linked-pr-fix-up Action now rather than wait for canonical batch.

**Decision**: Insert the linked-pr-fix-up GitHub Action ahead of the canonical Actions batch as TASK-0019 substantive cycle. Consumes one ADR-003 Decision 3 contingency slot (5 remaining → 4 remaining). Source-of-truth lives at `.github/workflows/linked-pr-fix-up.yml` + `.github/scripts/linked-pr-fix-up.py` operationally.

**Rationale**:
1. Eliminates manual PMN-001 (k) chore-fix-up burden 3–5 cycles earlier than canonical-batch shipment, with cumulative savings of approximately 15–25 manual cycles depending on canonical-batch landing time.
2. Action's operational track record between TASK-0019 ship and canonical-batch ship serves as design input for the batch — particularly around recursion-guard patterns, idempotency, and frontmatter-substitution generalization.
3. Owner directive ratified at handoff §4.1 Path X (versus Path Y bundle-into-PMN-008 chore-fix-up rejected; Path Z further-deferral rejected).

**Consequences**:
1. github-reference.md §6.2 Actions enumeration grows from 9 to 10 entries. Enumeration update deferred to canonical Actions batch cycle (this ADR records the deferral; not a §6.2 edit this cycle).
2. Canonical-source-of-truth lives at `.github/workflows/linked-pr-fix-up.yml` + `.github/scripts/linked-pr-fix-up.py` operationally until canonical Actions batch creates `actions/<action-name>/` source layout. Migration to canonical layout happens at canonical batch cycle.
3. Canonical Actions batch authoring (anticipated TASK-0023+) inherits this Action's empirical operational track record as input — design conventions, defect patterns, recursion-guard patterns.
4. ADR-003 Decision 3 contingency slots: 5 → 4 remaining post-this-decision.
5. README.md Action enumeration: see deliverable-6 step-1 decision (include if coherent placement, defer otherwise).
6. Pre-canonical-batch insertion sets a precedent that future Actions MAY ship pre-batch under similar conditions (Owner directive + clear high-volume mechanical cycle being automated). Future similar decisions reference this ADR as precedent.

**Alternatives considered**:
1. **Path Y — bundle into PMN-008 chore-fix-up (PR-20)**. Rejected: mixes mechanical and substantive scope, breaks chore-fix-up's mechanical-only invariant, complicates §24.3.1 five-point post-handback check.
2. **Path Z — defer to canonical Actions batch (TASK-0023+)**. Rejected: owner has indicated readiness to ship; deferral wastes a directive and accumulates 3–5 more manual cycles unnecessarily.

**References**: ADR-001 (decision 11 owner-invokes Codex), ADR-003 (decision 2 canonical Actions batch sequencing; decision 3 contingency slots), PMN-001 (k) chore-fix-up substitution discipline, PMN-008 §5.8 (h.4) three-endpoint poll discipline, TASK-0019 handoff (this cycle).

## §5. Placeholder-substitution discipline (PMN-003 (d))

Enumerate ALL `(Builder fills with X)` and `(Builder updates with X)` patterns. Substitution timing classification:

| File | Field | Pattern | Timing |
|---|---|---|---|
| THIS handoff (frontmatter) | `linked_pr` | `PR-21 (Builder fills with squash SHA post-merge per PMN-001 (k))` | post-merge (Action auto-fire OR manual chore-fix-up) |
| THIS handoff (frontmatter) | `status` | `active` | post-merge (`active` → `resolved`) |
| THIS handoff (Metadata) | Linked PR | `PR-21 (Builder fills URL post-PR-open per §5)` | at PR-open (step 13) |
| THIS handoff (Metadata) | Timestamp (UTC) | `Builder fills HH:MM at handoff creation` | at handoff creation (step 5) |
| THIS handoff (Metadata) | Last synced commit SHA | `ddc54a4 ... Builder verifies at pre-flight; ... Update field to actual origin/main HEAD` | at pre-flight (step 1) |
| THIS handoff (Validation run) | entire section | template-only | post-pre-flight + post-author + post-Codex (steps 1, 5, 7) |
| THIS handoff (Post-PR Codex review state) | entire section | template-only | post-Codex-settling (step 15) |
| THIS handoff (Sign-off) | entire section | Architect-deferred | post-§24.3.1 five-point check |
| PR-21 review-context (frontmatter) | `status` | `drafted` | post-merge (`drafted` → `recorded`) |
| PR-21 review-context | Codex output | per template | post-Codex-output (step 7) |

Builder audits this enumeration at step 9 (step-6 self-review) before commit.

## §6. Reassessment / expiry

- Hand-back gate at step 17 is the natural reassessment point. If the cycle stalls (Codex unresponsive, ambiguous review output, unexpected pre-commit findings requiring substantial revision, §E1 regex anomaly surfaced by Codex, ADR-004 §-cite divergence requiring path-(a) revise across multiple sources), Builder hands back to Architect with state explicit; do not extend autonomous execution past the named hand-back point.
- TASK status flips to `resolved` only after Architect §24.3.1 five-point post-handback check clean, owner merge via §10.5, Architect M-A7 merge-commit-body amendment, and Architect confirmation of merged state.
- If PR-22 (TASK-0019's own PMN-001 (k) chore-fix-up; the Action's first auto-fire opportunity) fails to fire OR fires with incorrect substitutions, fallback is the manual chore-fix-up cycle as today. Cycle close should produce informal note on first-auto-fire outcome regardless of pass/fail.

## §7. Post-PR Codex review state

Builder fills post-Codex-review-settling per PR-17 / PR-19 review-context priors.

## §8. Sign-off

Architect §24.3.1 five-point post-handback check completed [Architect fills date]. Each of the five canonical-text-named verification points performed; record results below per established Sign-off template (TASK-0017 / TASK-0018 priors as form reference).

Anticipated check coverage at minimum:
- PR comments via all three endpoints (`pulls/{pr}/reviews` + `issues/{pr}/comments` + `pulls/{pr}/comments`) — verbatim transcription against PR-21 review-context state.
- Branch state — three-endpoint poll evidence + commit sequence verification.
- File content against prescription — diff against this handoff's deliverable specifications, especially §E1 recursion-guard exact text.
- Phantom-action audit — Builder self-audit table verified against actual diff.
- (j) all-instances grep sweep verification on ADR-004 §-cites — re-run sweep + verify each citation against canonical source.

Architect verifies the canonical §24.3.1 fifth-point at sign-off and adjusts as needed.

Authorized for §10.5 single-contributor bypass merge per ADR-001 decision 11 admin-bypass posture.

— Architect, [Architect fills date]

## §9. Session log archive (prior logs migrated from PR body per §13.1)

<!-- Append prior AI Session Logs here as new sessions happen, oldest at top, newest at bottom. Most recent log stays in the PR body, not here. -->
