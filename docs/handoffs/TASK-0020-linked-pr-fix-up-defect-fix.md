---
task_id: TASK-0020
title: linked-pr-fix-up Action defect-fix cycle — regex newline-consumption + repo-setting dependency
pr: PR-23
branch: feat/task-0020-linked-pr-fix-up-defect-fix
linked_predecessor: TASK-0019 (PR-21 substantive ship + PR-22 manual chore-fix-up)
linked_successor: TBD
linked_pr: PR-23 (squash SHA 39b700e)
framework_version_dogfooded: AMAS v2.18
production_target: AMAS v3.0
spec_source: .claude/session-handoffs/TASK-0020-spec.md (gitignored per ADR-001 decision 15)
date_authored: 2026-05-04
status: resolved
---

# HANDOFF: TASK-0020

## Metadata

- Task ID: TASK-0020
- Linked Issue: none — defect-fix cycle for TASK-0019 ship; no separate issue tracker
- Linked PR: PR-23 — https://github.com/bryce-murphy/amas-framework/pull/23
- Linked ADR(s): ADR-004 (this cycle amends §Consequences); ADR-001 decision 11 (owner-invokes Codex)
- Linked PMN(s): PMN-001 (k) (chore-fix-up substitution discipline being defect-fixed); PMN-008 §5.8 (h.4) (three-endpoint Codex poll discipline)
- Owner role: Builder (Claude Opus 4.7, Claude Code, owner's local session)
- Previous role: Architect (Claude Opus 4.7, Claude.ai Project)
- Timestamp (UTC): 16:36
- Last synced commit SHA: `42132c2` (PR-22 squash; TASK-0019 manual chore-fix-up). Verified at pre-flight 2026-05-04 against `git rev-parse origin/main`; main HEAD has not advanced past PR-22 squash.
- Branch: `feat/task-0020-linked-pr-fix-up-defect-fix` (`feat/` prefix verified at pre-flight (i.5) — TASK-0019 substantive-cycle prior used `feat/task-0019-linked-pr-fix-up-action`; defect-fix cycle ships working code corrections per §Decisions made; owner ratified at step-1 stop-and-show).
- Status: active

## Objective

Ship a small defect-fix cycle for the linked-pr-fix-up GitHub Action shipped at TASK-0019 (PR-21). Two empirically-validated defects from PR-22 first-auto-fire empirical-validation event (TASK-0019 cycle close; cycle-close ledger items 9 + 10):

1. **Defect 2 — regex newline-consumption** (load-bearing, code-level): `\s*$` with `re.MULTILINE` in `linked-pr-fix-up.py` lines 35 + 93 consumes trailing `\n` when match is at end of fm_body, corrupting frontmatter when the `status` field is the last line (always the case per PMN-007 HEAD canonical). Pure-token-swap fix: replace `\s*$` with `[ \t]*$` in both `PLACEHOLDER_PATTERN` and the status-flip pattern.

2. **Defect 1 — workflow permission repo-setting dependency** (operational, configuration-level): GitHub repo setting "Allow GitHub Actions to create and approve pull requests" must be ON for the Action's `gh pr create` step to succeed. Workflow-level `permissions: pull-requests: write` is necessary but not sufficient. Owner-action: enable setting at repo level (not a code change). TASK-0020 documents the requirement via ADR-004 §Consequences amendment per Architect path-α adjudication.

Plus framework version bump v2.18 → v2.18.1 per §18.4 patch criterion (correctness fix to existing code + operational-dependency documentation; no new framework content).

Architect-level review of this defect-fix scope completed at TASK-0019 cycle-close adjudication. Both defects are pure-token-swap class per §8.1.1.3; ADR-004 amendment is additive (no existing decision content modified). Deeper review surfaces at Codex pre-commit (step 7) per ADR-001 decision 11 owner-invokes convention.

## Last completed step

Architect Phase 1 scoping completed (this session, 2026-05-04):
1. PR-21 (TASK-0019 substantive Action ship) merge state at `db3c9b0`; PR-22 (TASK-0019 manual chore-fix-up) at `42132c2` (current main HEAD).
2. Cycle-close ledger 11 items absorbed; items 2 + 9 + 10 promoted to TASK-0020 scope.
3. Path α/β/γ adjudication: path-α default (owner enables repo setting). Adjudication-pending gate at step-1 stop-and-show if owner unconfirmed.
4. ADR-004 amendment vs. new ADR-005 adjudication: amendment per ADR-002 amendment-pattern precedent (small additive amendment on existing decision; no full new ADR needed).
5. Version bump tier: v2.18 → v2.18.1 patch per §18.4 substantive-reading patch criterion.
6. Spec wording defects e.2 + e.3 (TASK-0019 spec lines 145 + 112) absorbed into TASK-0020 spec authoring discipline (not a deliverable; corrected wording applies from this spec forward).
7. Empirical verification of defect 2 fix correctness performed Architect-side via Python regex test (canonical fm_body shape + edge case of file ending exactly at closing `---`); fix preserves trailing newline; idempotency preserved.

Builder step-1 stop-and-show (2026-05-04) surfaced two (i.5) convention-divergence findings against spec body:
- Spec §3 step 4 named lines 36 + 93 for the `\s*$` → `[ \t]*$` substitution; actual `linked-pr-fix-up.py` has the `\s*$` token at line **35** + line 93 (line 36 is the `re.MULTILINE,` argument continuation). Pure-token-swap path-(a) revision adjudicated by owner; line numbers 35 + 93 used throughout this handoff and downstream artifacts.
- Spec §3 step 6 assumed existing ADR-004 §Consequences point count of 6 and instructed amendment as point 7; actual ADR-004 currently has 7 §Consequences points. Pure-token-swap path-(a) revision adjudicated by owner; new §Consequences point appended as point **8**.

Path-α confirmed by owner at step-1 stop-and-show; default amendment wording applies. Branch prefix `feat/` confirmed.

## Current state

**Summary**: 5 deliverables (3 new + 2 modified). Smaller scope than TASK-0019 (single-regex-fix + small ADR-004 amendment + standard cycle artifacts). Estimated cumulative diff ~250–380 substantive lines.

**Files to be authored / modified by Builder**:

1. MODIFIED `.github/scripts/linked-pr-fix-up.py` — regex fix at lines 35 + 93 (both `\s*$` → `[ \t]*$` for `PLACEHOLDER_PATTERN` + status-flip pattern). 2-line modification.
2. MODIFIED `docs/adr/ADR-004-pre-actions-batch-action-insertion.md` — §Consequences amendment adding new point recording repo-setting operational dependency (per path-α default); Status field amended per ADR-002 amendment-pattern precedent. New point appended as point 8 (existing point count = 7 per pre-flight (i.5) finding). ~10–20 line addition.
3. NEW `docs/handoffs/TASK-0020-linked-pr-fix-up-defect-fix.md` — this handoff. ~250–300 lines.
4. NEW `docs/reviews/PR-23-codex-pre-commit.md` — Codex pre-commit review-context with claim list per §3 step 7. ~150–200 lines.
5. MODIFIED `README.md` — Class A canonical-version-of-record bump line 9 (`v2.18` → `v2.18.1`; both instances). 1-line modification.

**Files changed (anticipated diff shape)**: 3 new + 2 modified. Estimated 250–380 insertions, 4–6 deletions across modifications.

## Decisions made

- **Path-α adjudicated at step-1 stop-and-show**: owner enabled repo setting "Allow GitHub Actions to create and approve pull requests" before TASK-0020 execution. TASK-0020 documents the requirement via ADR-004 §Consequences amendment with path-α default wording.
- **Defect 2 fix**: pure-token-swap regex fix at `linked-pr-fix-up.py` lines 35 + 93 — replace `\s*$` with `[ \t]*$` in both `PLACEHOLDER_PATTERN` and the status-flip pattern. Matches trailing whitespace on the same line without consuming the line-terminator newline. Standard Python regex idiom for line-end matching when newline preservation matters. **Empirically verified Architect-side** (see §3 step 7 claim (a) for reproducible test).
- **ADR-004 amendment vs. new ADR-005**: amendment per ADR-002 amendment-pattern precedent. The §Consequences point is purely additive within ADR-004's existing decision scope (does not modify or supersede the substantive pre-batch-insertion decision). Status field amendment notation per ADR-002 form.
- **ADR-004 §Consequences new point number = 8** (not 7 per spec). Pre-flight (i.5) found existing point count is 7; new point appended as point 8.
- **Defect 2 fix line numbers = 35 + 93** (not 36 + 93 per spec). Pre-flight (i.5) found line 36 is the `re.MULTILINE,` argument continuation; line 35 contains the `\s*$` token to be replaced.
- **Framework version bump v2.18 → v2.18.1**: patch tier per §18.4 substantive-reading patch criterion (correctness fix + operational-dependency documentation; no new framework content). Class A canonical-version-of-record at README.md line 9.
- **No core.md update this cycle**: §8.1.1.1 third-endpoint canonicalization (cycle-close ledger Item 8; six-cycle empirically-overdetermined) deferred to TASK-0021 — separate cycle scope.
- **No PMN-009 this cycle**: cycle-close ledger items 6 + 7 + 11 stay at single-/two-data-point monitoring; no candidate at small-PMN promotion threshold (2–3 cross-cycle confirmations). Bundling defect-fix cycle with PMN-authoring cycle would break one-artifact-class-per-PR convention.
- **M-A7 instance count**: TASK-0020 is **not** an M-A7-eligible cycle (M-A7 enumerates substantive-content cycles; defect-fix is a correction-class cycle). PR-23 does not increment M-A7. Architect performs no M-A7 amendment for this cycle. Next M-A7 increment is at the following substantive-content cycle.
- **Branch type prefix `feat/`**: substantive-cycle-shape inheritance from TASK-0019. Defect-fix cycles are substantive in the sense that they ship working code corrections; not chore-class. Owner ratified at step-1 stop-and-show.

## Assumptions

- Repo state at TASK-0020 execution time matches handoff snapshot: HEAD of main at `42132c2` (PR-22 squash); no open PRs; branches clean. Verified at pre-flight 2026-05-04.
- Owner has enabled repo setting "Allow GitHub Actions to create and approve pull requests" before PR-23 close (path-α default — confirmed at step-1 stop-and-show).
- Codex Reviewer is operational; no §2.3.7 failover episode in flight.
- Branch protection on main is unchanged (Posture 2 — pull-request-only admin bypass via Rulesets; PRs required, 1 approval, code-owner review, conversation resolution, squash-only merge).
- Owner is available at step-10 pre-commit stop-and-show + post-PR `@codex review` invocation gate per ADR-001 decision 11.
- The `linked-pr-fix-up.py` + `linked-pr-fix-up.yml` files are at canonical paths (`.github/scripts/` + `.github/workflows/`) post-PR-21 squash-merge; verified at pre-flight.

## Risks

- **TASK-0020 first-auto-fire empirical-validation event** (PR-24 anticipated post-merge): both defect fixes empirically tested at TASK-0020's own merge-close. (a) If regex fix correct, frontmatter substitutions on TASK-0020 handoff + PR-23 review-context preserve trailing newlines (validates defect 2 fix); if regex fix wrong, defect 2 recurs at empirical surface. (b) If owner enabled repo setting (path-α), Action successfully opens PR-24 as auto-generated chore-fix-up (validates defect 1 fix); if not enabled, defect 1 recurs and manual chore-fix-up needed. **First empirical-validation loop test for both defect-class fixes**. Cycle-close note material regardless of pass/fail.
- **(z) candidate strengthens or settles at empirical-validation surface**: this cycle is the first defect-fix cycle for the linked-pr-fix-up Action. PR-24 first-auto-fire event provides further evidence on whether mechanical/regex correctness defects systematically slip past static-review surfaces (cycle-close ledger Item 11). If TASK-0020 first-auto-fire passes cleanly, (z) doesn't strengthen; if a new defect surfaces at runtime that all pre-runtime surfaces missed, (z) gets second-instance evidence.
- **Path-α dependency on owner repo-setting**: setting confirmed enabled at step-1 stop-and-show. Reversible — manual fallback always works per spec §Risks framing on additive-not-load-bearing.
- **(j) all-instances grep sweep on ADR-004 amendment**: amendment introduces minor new §-citations + cross-references. (j) discipline applies; smaller sweep than TASK-0019 ADR-004 authoring (~3–7 new citations vs. ~27 for full ADR-004).
- **Three-endpoint Codex poll discipline**: OPERATIONAL discipline this cycle pending TASK-0021 canonical-text correction at core.md §8.1.1.1. Six-cycle confirmed empirical pattern at endpoint 3 per cycle-close ledger Item 8.
- **(w) Codex post-PR autonomous-action attempts** (cycle-close ledger Item 6): single-data-point at TASK-0019 cycle close. PR-23 absorption may produce second-instance evidence if Codex post-PR re-emits phantom-action sub-shape A claims. Builder applies §8.1.1.2 verification discipline regardless; outcome strengthens or settles the candidate.
- **Local Builder environment lacks python interpreter**: empirical-test for defect 2 fix correctness (claim (a) verification command) cannot run locally at Builder side. Test was performed Architect-side per §"Last completed step" item 7; will be re-run Codex-side at pre-commit (claim (a)). Surface defect captured at pre-commit stop-and-show.

## Blocking questions

(none at active execution time — all step-1 items adjudicated by owner)

## Validation run

- **Commands run** (pre-flight, §3 step 1):
  - `git fetch origin` ✓
  - `git checkout main` ✓ (already on main)
  - `git pull --ff-only origin main` ✓ (already up to date)
  - `git rev-parse HEAD` → `42132c296ee64638ba30aab16ceb0d20a9fe7f8d` ✓ (matches metadata `42132c2`)
  - `git rev-parse origin/main` → `42132c296ee64638ba30aab16ceb0d20a9fe7f8d` ✓ (reconciled)
  - `git status` → clean ✓
  - `gh pr list --state merged --limit 4` → PR-22, PR-21, PR-20, PR-19 ✓ (PR-22 most-recent)
  - `gh pr list --state open` → empty ✓
  - `.github/scripts/linked-pr-fix-up.py` exists, 158 lines ✓
  - `.github/workflows/linked-pr-fix-up.yml` exists ✓
  - `docs/adr/ADR-004-pre-actions-batch-action-insertion.md` exists, §Consequences point count = 7 ✓
  - `docs/handoffs/` enumerated through TASK-0019 ✓
  - `docs/reviews/` enumerated through PR-21 (no PR-22 review-context per chore-fix-up convention) ✓
- **(i.5) convention-inference samples**:
  - (a) TASK-0019 handoff frontmatter shape = 12-field PMN-007 HEAD canonical; this handoff matches.
  - (b) PR-21 review-context structure = `status: drafted` frontmatter + Metadata section + numbered Builder claims to verify list; PR-23 review-context follows.
  - (c) ADR-004 current state: Status field text `Accepted — 2026-05-03`; §Consequences point count = 7 (not 6 per spec); §Evidence/references format established.
  - (d) README.md current state: line 9 has TWO `v2.18` instances (`**v2.18**` + `v2.18`); update set for v2.18 → v2.18.1.
  - (e) Class A v-bump set: 2 instances on line 9; no other Class A markers at canonical-version-of-record surface.
- **Evidence (post-edit blob hashes via `git hash-object`)**:
  - `.github/scripts/linked-pr-fix-up.py` (post-fix): `500779a2f4054170f09e83e9c0db26e8090daa8e`
  - `docs/adr/ADR-004-pre-actions-batch-action-insertion.md` (post-amendment + post-Codex-Major-1 fix-up): `5aab01044b1064857d8fb7ff6e157028afb468e5`
  - `docs/handoffs/TASK-0020-linked-pr-fix-up-defect-fix.md`: self-hash not claimed (avoids self-referential edit-cycle); Builder enumerates structural evidence via PR-23 review-context claim 10 instead.
  - `docs/reviews/PR-23-codex-pre-commit.md`: cross-document hash claim omitted (avoids chicken-and-egg with review-context claim 10 of handoff hash; one-pass resolution per (g) cross-document state verification discipline). Final review-context hash recorded only at review-context-side step-9 self-review.
  - `README.md` (post-v-bump): `600cb291b51fbbb29f574b1815d96b17bc0f346f`
  - PR-23 URL: Builder fills post-step-13
- **Post-edit Read-verify** (PMN-003 (f)): structural headings extraction performed at step-9 self-review.
- **(j) sweep evidence**: `grep -nE "(core\.md|github-reference\.md|ADR-00[0-9]+|PMN-00[0-9]+|TASK-[0-9]+|PR-[0-9]+)" docs/adr/ADR-004-pre-actions-batch-action-insertion.md` recorded post-step-6.
- **Empirical-test for defect 2 fix correctness** (claim (a) per §3 step 7): local Builder environment lacks python interpreter (`python` / `python3` / `py` not on PATH). Architect-side empirical verification performed at handoff §"Last completed step" item 7; re-verification at Codex pre-commit (claim (a)). By-inspection verification: `[ \t]*$` matches horizontal whitespace (space + tab) only without consuming the line-terminator `\n` — standard Python regex idiom. Diff confirms both edits applied byte-exactly to the prescribed locations (lines 35 + 93). Codex desktop pre-commit (verified-as-passing) confirmed bundled-Python newline preservation + idempotency at desktop runtime per PR-23 review-context §"Codex review output (verbatim)".
- **Post-fix-up-5 absorption cumulative-diff-stats per (e.1)** (re-derived after Codex post-PR absorption edits to PR-23 review-context + this handoff §7): branch tip = absorption commit; per-file numstat sums (substantive-commit + fix-up-5):
  - `.github/scripts/linked-pr-fix-up.py`: +2 / -2
  - `README.md`: +1 / -1
  - `docs/adr/ADR-004-pre-actions-batch-action-insertion.md`: +5 / -2
  - `docs/handoffs/TASK-0020-linked-pr-fix-up-defect-fix.md`: +357 / -1 (post-absorption-edit total — handoff URL fill + §7 absorption + this Validation run entry)
  - `docs/reviews/PR-23-codex-pre-commit.md`: +205 / -2 (post-absorption-edit total — claim list path-(a) fix-ups + Codex review output (verbatim) + Adjudication trace + Codex post-PR pass 1 absorption)
  - Cumulative across all five files: ~570 insertions / ~8 deletions (Builder fills final exact values via `git diff --shortstat origin/main` post-fix-up-5 commit; per (h.2) discipline, working-tree-vs-main form).

## Exact next step

Execute the following sequence. Hand-back point is **after PR-23 is open with placeholders substituted per §5, after `@codex review` trigger, after all three Codex endpoints settle**, before merge. Architect performs §24.3.1 five-point post-handback check before signing off for §10.5 single-contributor bypass merge.

(Steps 1–4 already performed. Steps 5–17 ongoing per spec sequence; numbering preserved for cross-reference clarity with spec.)

### 1. Pre-flight verification (extended (i.5) batch)

[Performed; see §Validation run above.]

### 2. Step-1 stop-and-show

[Performed; owner adjudicated all four items: path-α confirmed, point 8 (not 7), lines 35+93 (not 36+93), branch prefix `feat/` confirmed.]

### 3. Branch creation

[Performed: `git checkout -b feat/task-0020-linked-pr-fix-up-defect-fix`.]

### 4. Apply regex fix to `.github/scripts/linked-pr-fix-up.py`

[Performed; both `\s*$` → `[ \t]*$` substitutions applied at lines 35 + 93. Post-edit hash `500779a2f4054170f09e83e9c0db26e8090daa8e`.]

### 5. Author this handoff (TASK-0020)

[Performing now.]

### 6. Author ADR-004 amendment

Modify `docs/adr/ADR-004-pre-actions-batch-action-insertion.md` per the path-α default amendment shape:

(a) **Status field amendment** per ADR-002 amendment-pattern precedent:

ORIGINAL:
```markdown
## Status

Accepted — 2026-05-03
```

REPLACE WITH:
```markdown
## Status

Accepted — 2026-05-03; Amended 2026-05-04 (this amendment adds §Consequences point on operational dependency surfaced at PR-22 first-auto-fire empirical-validation event per TASK-0020 cycle).
```

(b) **§Consequences new point 8** appended at end of §Consequences section (existing point count = 7 per pre-flight (i.5) finding; new point appended as point 8).

Path-α default wording:
```markdown
8. **Repo-setting operational dependency**: the linked-pr-fix-up Action's `gh pr create` step requires GitHub repo setting "Allow GitHub Actions to create and approve pull requests" (Settings → Actions → General → Workflow permissions) to be enabled. Workflow-level `permissions: pull-requests: write` declared at line 23 of `.github/workflows/linked-pr-fix-up.yml` is necessary but not sufficient; the repo-level setting is also required. Surfaced at PR-22 first-auto-fire empirical-validation event (TASK-0019 cycle close): repo setting was OFF at PR-21 ship time; Action's auto-fire on PR-21's own merge-close created the chore-fix-up branch and applied substitutions, but the `gh pr create` step failed with `pull request create failed: GraphQL: GitHub Actions is not permitted to create or approve pull requests (createPullRequest)`. Owner enabled the setting at TASK-0020 cycle execution per Architect path-α adjudication. TASK-0020's own first-auto-fire (PR-24 anticipated post-merge) is the empirical-validation event for this fix.
```

(c) **§Evidence / references update**: append references to TASK-0020 handoff + PR-23 review-context + this amendment context.

Target amendment length: 10–20 lines added net. Single-line Status field replacement; ~10–15 line §Consequences point addition; 1–3 line §Evidence/references append.

### 7. Pre-commit Codex review (claim-verification)

Builder authors `docs/reviews/PR-23-codex-pre-commit.md` content with claim list:

- (a) **Defect 2 regex fix correctness** at `linked-pr-fix-up.py` lines 35 + 93. Verification command:
  ```bash
  python3 -c "
  import re
  test = '---\nstatus: active\n---\n'
  fm = test[3:test.rindex('---')]
  pat = re.compile(r'^status: active[ \t]*\$', re.MULTILINE)
  result = test[:3] + pat.sub('status: resolved', fm) + test[test.rindex('---'):]
  print(repr(result))
  "
  ```
  Expected output: `'---\nstatus: resolved\n---\n'`.
- (b) **Defect 2 fix idempotency preserved**: re-running the substitution on already-substituted content is a no-op (placeholder pattern absent → regex doesn't match → no edit applied). Same idempotency property as pre-fix.
- (c) **Edge case verification**: file ending exactly at closing `---` with no trailing file-level newline. Substitution preserves the newline between `status: <new>` and closing `---`. Verification per Architect Phase 1 empirical test.
- (d) **ADR-004 amendment additive**: new §Consequences point 8 added; existing points 1-7 unchanged; Status field updated per ADR-002 amendment-pattern precedent. `git diff origin/main..HEAD -- docs/adr/ADR-004-pre-actions-batch-action-insertion.md` shows additions only at Status field + new §Consequences point + §Evidence/references append.
- (e) **Class A v-bump applied**: README.md line 9 `v2.18` × 2 → `v2.18.1` × 2; no `v2.18` remaining at Class A canonical-version-of-record surface.
- (f) **(j) all-instances grep sweep on ADR-004 amendment §-cites**: smaller sweep than TASK-0019 ADR-004 authoring. Each new citation in the amendment verified clean against canonical source.
- (g) **TASK-0020 handoff structural-headings count + section ordering matches TASK-0019 prior** per PMN-007 HEAD canonical 12-field frontmatter convention.
- (h) **Cumulative-diff-stats self-stability** per (e.1) sub-rule: per-file numstat sums match `git diff --staged --shortstat` total exactly; no `~`-prefixed approximate counts in any artifact.

Wait for Codex output. Record output verbatim into `docs/reviews/PR-23-codex-pre-commit.md`. Adjudicate per ADR-001 decision 11 owner-invokes convention with Architect direction:
- Blocking → hand back to Architect per PMN-001 (k); do not proceed past pre-commit gate.
- Major → surface to Architect for path-(a) revise / path-(β) record-and-proceed adjudication.
- Minor → surface to Architect; default path-(b) unless direction otherwise.

### 8. Author PR-23 review-context

Write `docs/reviews/PR-23-codex-pre-commit.md` per PR-21 prior at pre-flight (i.5) (b). YAML frontmatter `status: drafted` (post-merge transition to `recorded` is Action / chore-fix-up cycle responsibility per defect 2 fix).

### 9. Builder step-6 self-review

Per PMN-008 §3 / handoff §5.2 canonical fifth surface promotion. Re-read all five placed/modified files end-to-end against the spec.

### 10. Pre-commit stop-and-show

Surface to owner before commit:
- Step-9 self-review findings.
- Placeholder-substitution audit per §5 + Builder-prep PR body.
- Codex pre-commit review-context state + adjudication outcomes.
- Final diff shape (`git diff --stat`).
- Local Builder environment limitation (no python interpreter for empirical-test claim (a)).

### 11. Commit

Single commit with message:

```
fix(amas): TASK-0020 defect-fix cycle for linked-pr-fix-up Action — regex newline-consumption + repo-setting dependency

Fixes regex newline-consumption defect at .github/scripts/linked-pr-fix-up.py
lines 35 + 93 (\s*$ → [ \t]*$) preventing trailing-newline corruption when
the status field is the last fm_body line. Documents repo-setting operational
dependency at ADR-004 §Consequences amendment (point 8) per Architect path-α
adjudication. README.md Class A v-bump v2.18 → v2.18.1 per §18.4 patch
criterion. Both defects surfaced at PR-22 first-auto-fire empirical-
validation event (TASK-0019 cycle close).

Refs ADR-001, ADR-002, ADR-004, PMN-001, PMN-008, TASK-0019.
```

### 12. Push

`git push -u origin feat/task-0020-linked-pr-fix-up-defect-fix`

### 13. PR-open with placeholder substitutions complete

Use a PR body template per PR-21 prior. Audit ALL placeholders in the PR body before submitting `gh pr create`.

### 14. Owner invokes `@codex review`

Per ADR-001 decision 11.

### 15. Three-endpoint review-state poll + re-poll discipline per PMN-008 §5.8 (h.4)

Three endpoints to poll:
- `gh pr view 23 --json reviews`
- `gh api repos/bryce-murphy/amas-framework/issues/23/comments`
- `gh api repos/bryce-murphy/amas-framework/pulls/23/comments`

OPERATIONAL discipline this cycle pending TASK-0021 canonical-text correction per cycle-close ledger Item 8.

### 16. Address findings if any

Path (a) revise / path (β) record-and-proceed adjudication via Architect.

### 17. Hand back to Architect

Provide PR-23 URL, three-endpoint Codex outputs, branch state, "no findings" or "findings addressed" attestation, Builder step-6 self-review attestation, defect 2 empirical-test outcome.

## §4. ADR-004 amendment content prescription

(See §3 step 6 for full path-α default amendment text. Path-α confirmed at step-1 stop-and-show.)

## §5. Placeholder-substitution discipline (PMN-003 (d))

| File | Field | Pattern | Timing |
|---|---|---|---|
| THIS handoff (frontmatter) | `linked_pr` | `PR-23 (Builder fills with squash SHA post-merge per PMN-001 (k))` | post-merge (Action auto-fire OR manual chore-fix-up; defect 2 fix tested empirically here) |
| THIS handoff (frontmatter) | `status` | `active` | post-merge (`active` → `resolved`; defect 2 fix tested empirically here) |
| THIS handoff (Metadata) | Linked PR | `PR-23 (Builder fills URL post-PR-open per §5)` | at PR-open (step 13) |
| THIS handoff (Metadata) | Timestamp (UTC) | filled at handoff creation | at handoff creation (step 5) — `16:36` |
| THIS handoff (Metadata) | Last synced commit SHA | `42132c2` verified at pre-flight | at pre-flight (step 1) — verified |
| THIS handoff (Validation run) | hash + URL post-fills | template | post-step-{6,8,13} |
| THIS handoff (Post-PR Codex review state) | entire section | template-only | post-Codex-settling (step 15) |
| THIS handoff (Sign-off) | entire section | Architect-deferred | post-§24.3.1 five-point check |
| PR-23 review-context (frontmatter) | `status` | `drafted` | post-merge (`drafted` → `recorded`; defect 2 fix tested empirically here) |
| PR-23 review-context | Codex output | per template | post-Codex-output (step 7) |

Builder audits this enumeration at step 9 (step-6 self-review) before commit.

## §6. Reassessment / expiry

- Hand-back gate at step 17 is the natural reassessment point. If the cycle stalls (Codex unresponsive, ambiguous review output, unexpected pre-commit findings requiring substantial revision, ADR-004 amendment §-cite divergence requiring path-(a) revise across multiple sources), Builder hands back to Architect with state explicit; do not extend autonomous execution past the named hand-back point.
- TASK status flips to `resolved` only after Architect §24.3.1 five-point post-handback check clean, owner merge via §10.5, and Architect confirmation of merged state. (No M-A7 amendment for this cycle per §Decisions made.)
- If TASK-0020 first-auto-fire (PR-24) fails to fire OR fires with incorrect substitutions, fallback is the manual chore-fix-up cycle as today. **Cycle close should produce informal note on first-auto-fire outcome regardless of pass/fail** — this cycle's first-auto-fire is the empirical-validation event for both defect fixes.

## §7. Post-PR Codex review state

Owner posted `@codex review` on PR-23 at 2026-05-04T17:03:54Z (issue-comment `4372907253`). Three-endpoint poll per PMN-008 §5.8 (h.4) OPERATIONAL discipline returned:

- **Endpoint 1** (`pulls/23/reviews`): empty.
- **Endpoint 2** (`issues/23/comments`): 3 comments — autonomous Codex pre-trigger comment (`4372889326`, 17:01:34Z, ~2m 20s before owner trigger; (w) sub-shape A second-instance evidence with anti-claim variant; anti-claims verified TRUE per §8.1.1.2), owner `@codex review` invocation (`4372907253`, 17:03:54Z), Codex formal verdict (`4372917992`, 17:05:18Z): "Didn't find any major issues."
- **Endpoint 3** (`pulls/23/comments`): empty.

**Substantive verdict: no findings.** Verbatim outputs + (w) sub-shape framing + (h.4) empirical-pattern refinement (first instance in 7 cycles where substantive verdict lands at endpoint 2 rather than endpoint 3) recorded canonically at `docs/reviews/PR-23-codex-pre-commit.md` §"Codex post-PR pass 1 absorption". No fix-up applied (nothing to address).

Cycle-close ledger updates this turn (per Architect §24.3.1 hand-back):
- Item 5 ✓ now actually-settled (text-propagation residual surfaced at TASK-0020 Codex pre-commit Major 1; resolved at path-(a) revise during pre-commit fix-up).
- Item 6 (w) strengthens to two cross-cycle data points with refined sub-shape framing (sub-shape A ↔ anti-claim variant); below 3-confirm promotion threshold.
- Item 8 (h.4) — seventh-cycle evidence with empirical-pattern refinement; strengthens canonical-text-correction case for TASK-0021.
- (i.5) Architect-spec-drift catch discipline — 4 cross-cycle confirmations; PMN-009 promotion-overdetermined; targeted for TASK-0021 ship.

## §8. Sign-off

Architect §24.3.1 five-point post-handback check completed [Architect fills date]. Each of the five canonical-text-named verification points performed; record results below per established Sign-off template (TASK-0019 prior as form reference).

Anticipated check coverage at minimum:
- PR comments via all three endpoints — verbatim transcription against PR-23 review-context state.
- Branch state — three-endpoint poll evidence + commit sequence verification.
- File content against prescription — diff against this handoff's deliverable specifications, especially regex fix exact text + ADR-004 amendment exact text.
- Phantom-action audit — Builder self-audit table verified against actual diff (cycle-close ledger Item 6 (w) monitoring continues).
- (j) all-instances grep sweep verification on ADR-004 amendment §-cites.

Architect verifies the canonical §24.3.1 fifth-point at sign-off and adjusts as needed.

Authorized for §10.5 single-contributor bypass merge per ADR-001 decision 11 admin-bypass posture.

— Architect, [Architect fills date]

## §9. Session log archive

(empty at handoff-authoring time; new task, single session expected)
