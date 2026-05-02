---
task_id: TASK-0011
title: PMN-006 PR-10 cycle learnings + core.md surgical corrections
pr: PR-11
branch: feat/task-0011-pmn-006
linked_predecessor: TASK-0010 / PR-10 (squash SHA 80f5a4aab532bc89cd14fb752b5fc07fbf42fc7f)
linked_successor: TASK-0012 (Part B authoring; pending)
linked_pr: (filled at step-18 fix-up per PMN-001 (k))
framework_version_dogfooded: AMAS v2.15
production_target: AMAS v3.0
spec_source: .claude/session-handoffs/TASK-0011-spec.md (gitignored per ADR-001 decision 15; spec at iteration 8 per §12.2; three known residuals routed to path-(b) per PMN-006 §1.1 defect 8)
date_authored: 2026-05-02
status: in_progress
---

# TASK-0011 — PMN-006 PR-10 cycle learnings + core.md surgical corrections

## Metadata

- TASK ID: TASK-0011
- PR: PR-11
- Branch: `feat/task-0011-pmn-006`
- Author surface: Builder (Claude Code, Windows 11 + Git Bash)
- Date authored: 2026-05-02
- Linked records: PMN-001 (h.2)/(k), PMN-003 (a)-refined/(e)-refined, PMN-004 §5 (a)-(f), PMN-005 §2.5/§4.4, PMN-006 §3 (g)/(h), PMN-006 §7 (i), PMN-006 §5.3 bounded-continuation rule, ADR-001, ADR-003
- Framework version dogfooded: AMAS v2.15
- Production target: AMAS v3.0
- Spec source: `.claude/session-handoffs/TASK-0011-spec.md` (gitignored per ADR-001 decision 15)

## Last completed step

Builder completed steps 1-13 per TASK-0011 spec; PR-11 opened at branch tip; hand-back to Architect for §24.3.1 five-point check (now corrected per (h.2) — `git rev-parse HEAD` + expected SHA + `git status --porcelain` clean-tree adjunct). Step-by-step: pre-flight (§5 step 1) verified all repo-state pre-conditions; pre-flight pass 1 surfaced 4 substantive spec defects (PMN-006 §1.1 defects 4, 6 incorporating sub-defects); pre-flight pass 2 surfaced defect 7 (§5 step 2 reservation-mechanism error); owner adjudicated (i) cluster adoption + path-(β) record-and-proceed for pre-flight pass 3 residuals (PMN-006 §1.1 defect 8). Branch `feat/task-0011-pmn-006` created off `80f5a4a`; PMN-006 authored at 9 §-headers with §1.1 honesty record enumerating 8 defects; core.md §8.1.1.1 polling-commands corrected per (h.3) symmetric application across both `submitted_at` and `created_at` endpoints with author filter preserved; core.md §24.3.1 point 2 corrected per (h.2) `git rev-parse HEAD` + expected-SHA form; companion artifacts authored (this handoff, `docs/reviews/PR-11-codex-pre-commit.md`, README.md PMN file table per-PR-row update); step-10 self-verification ran iteratively-to-fixed-point per §23.6.2; Codex desktop pre-commit review run by owner per spec §14; stop-and-show §14 surfaced and owner approved.

## Current state

Summary of `main` and working-tree state at hand-back. Filled with exact values:

- `main` SHA at branch base: `80f5a4a` (squash-merge SHA of PR-10)
- Branch tip SHA at PR-open: (filled at step-12 push per PMN-001 (k) Linked PR fix-up substitution convention; subsequent fix-up commits on this branch produce a different tip SHA recorded by the relevant fix-up commit's own metadata)
- Tracked-file count post-merge expected: `91`
  - Decomposition: 88 base (verified at step 1 via `git ls-files | wc -l`) + 3 new files (`docs/post-merge-notes/PMN-006-pr-10-cycle-learnings.md` + `docs/reviews/PR-11-codex-pre-commit.md` + `docs/handoffs/TASK-0011-pmn-006-pr-10-cycle-learnings.md`) = 91. The single modified file (`core.md` modified for §8.1.1.1 + §24.3.1 surgical corrections) does not change tracked-file count.
  - Verifiable at step-10 self-verification per spec §7.1.
- Files changed: 4 (PMN-006 new; PR-11 review-context new; TASK-0011 handoff new; core.md modified). README.md is NOT modified in this cycle per PMN-006 §1.1 defect 9 (spec deliverable 5 asserted a non-existent "PMN file table"; routed to path-(β) record-and-proceed per bounded-continuation rule §5.3 generalized cross-surface).

## Decisions made

The handoff records inherited Architect-decided scope decisions per spec §2 plus in-cycle owner-adjudicated decisions:

- PMN-006 scope: 9 observation clusters per spec §3 (8 originally scoped (a)-(h) + (i) cross-document state verification adopted in iteration 7 at owner adjudication post-Builder pre-flight pass 1).
- core.md surgical corrections: both §8.1.1.1 (h.3) symmetric across both endpoints + §24.3.1 (h.2). Surgical-or-defer guard not triggered (both corrections fit cleanly without surrounding-prose restructuring).
- README scope: PMN file table only — Package layout table updates explicitly out-of-scope per spec §2 deliverable 5 + ADR-003 §Consequences (substantive content PRs update their own package-layout row at content-fill time; PMN-006 is not a substantive content PR).
- Bounded-continuation rule generalized cross-surface: rule originally articulated at Reviewer post-PR review surface (PMN-005 §2 / PR-10 pass 5 adjudication); PMN-006 generalizes to Architect-side spec-revision surface in response to Builder pre-flight findings. Iteration 8 was path-(a) revision; defect 8 (three iteration-7/iteration-8 propagation residuals) is path-(β) record-and-proceed material per owner adjudication.
- No ADR amendment in this cycle. M-A7 §-section text in core.md deferred to Part B (TASK-0012). Bounded-continuation rule §-section text in core.md deferred to Part B.
- No new monitoring item this cycle. M-A8 (PMN-cadence step-up) preliminary observation only; promotion deferred to ~3 cycles of evidence.

## Assumptions

- TASK-0011 is the next available TASK number per ADR-003 Decision 3 PMN-insertion discipline (verified in step 1 pre-flight: `gh pr list --state open --search "TASK-0011"` returned no results; `git log --oneline --all | grep TASK-0011` returned no merged commit). Reservation mechanism is handoff-file-presence (this file IS the reservation; no separate registry).
- PR-11 is the next available PR number (verified in step 1 via `gh pr list --state all` showing PR-10 as most recent merged at squash-SHA `80f5a4a`).
- Base SHA `80f5a4a` is current `main` (verified in step 1).
- Branch protection on `main` is live and configured per ADR-001 decision 9.
- `gh` CLI authenticated with `repo` scope minimum.
- Codex desktop is available to the owner for step 14 pre-commit review.
- `core.md` exists at repo root (verified in step 1; `Glob **/core.md` returns single path `core.md`; spec's initial `docs/spec/core.md` assumption was a defect surfaced in pre-flight pass 1).
- `.gitkeep` is tracked in `docs/post-merge-notes/` (verified in step 1; `git ls-files docs/post-merge-notes/` returns 6 entries including `.gitkeep`; spec session-2's initial inversion claim that `.gitkeep` was untracked was a defect surfaced in pre-flight pass 1).

## Risks

- **Surgical-or-defer guard on core.md corrections** (per spec §2 / §4): if either §8.1.1.1 or §24.3.1 correction reveals surrounding-prose restructuring, defer to Part B. **Outcome**: not triggered. Both corrections fit surgically; one explanatory sentence added adjacent to §8.1.1.1 polling block describing same-second tie-break mechanism; one expanded prose at §24.3.1 point 2 describing necessary-but-not-sufficient relationship between `git rev-parse HEAD` and `git status --porcelain` clean-tree check. Surrounding prose unchanged elsewhere in either §-section.
- **Codex pre-commit produces same-class findings (g) or (h) or (i) on this cycle's review-context** (per spec §10): Builder applies bounded-continuation rule per PMN-006 §5.3 generalized cross-surface. First finding in any (g)/(h)/(i) sub-shape: path-(a) revise. Second-pass finding in same sub-shape: path-(β) record-and-proceed; carry to PMN-007 if substantive. Recursive-self-instantiation: PR-11 review-context is the first claim-block surface where (g)/(h)/(i) self-application is canonicalized; pre-flight pass 3 already surfaced one (g) defect within PR-11 review-context's own final note (mid-prose self-correction; cleaned at authoring time, not Codex finding).
- **§23.6 self-review iteration step-up if substantive-content scope persists** (per spec §10 / §3.1 preliminary hypothesis): PMN-006 has 9 observation clusters. Builder convergence target was 2-3 iterations per role-axis-dependence preliminary hypothesis. Actual: see §"Validation run" Evidence section below for landed iteration count.
- **PMN-006 §-count drift** (per spec §10): spec-time count 9 (§3 spec). Frontmatter-vs-body reconciliation per (b.3) extended catches this. **Outcome**: §-count = 9 verified at step-10 (`grep -cE "^## §[0-9]" docs/post-merge-notes/PMN-006-pr-10-cycle-learnings.md` returns `9`).
- **Cross-document citation drift** (per spec §10): PMN-006 cross-references PMN-001 through PMN-005 + core.md §-sections + AMAS v2.14.1 §-sections + ADR-001/002/003. PMN-004 / PMN-005 / PMN-006 use §N numbering and require range-checks per (f). PMN-001 / PMN-002 / PMN-003 use observation-letter citations and require letter-existence verification. core.md citations require §-existence verification at HEAD (post-correction state). Mitigation: §23.6 (f) iterative-to-convergence sweep at step 9; cross-document state verification per (i) at step 9.
- **(i) iterative-pre-flight pattern** (per PMN-006 §7.6): Builder pre-flight is itself iterative; pre-flight passes 1, 2, 3 each surfaced new defects from prior iteration's propagation gaps. Bounded-continuation rule §5.3 applied as structural stop condition: iteration 8 was path-(a) revision; defect 8 (residuals 1-3) is path-(β) record-and-proceed material. Without bounded-continuation, iteration count has no convergence guarantee in finite spec-revision iterations. Owner adjudicated path-(β); residuals stay in spec for empirical record.
- **Severity-taxonomy compliance** (PMN-004 §5 (a)): PR-11 review-context file enumerates Blocking / Major / Minor (three-level repo discipline; standing). Verified at step-10.
- **Phantom-action surface in Builder hand-back** (PMN-005 §2.5): claims about file existence, content, and counts must be directly verifiable from working-tree filesystem and `git diff` output at hand-back time. Mitigation: §"Validation run" lists each claim with verification command and observed result.
- **Verification-command portability** (PMN-004 §5 (b)): pre-commit verification commands provided in bash, cmd, and PowerShell forms in spec §5 pre-flight, §7 step-10 self-verification, and §6 + §8 PR-11 review-context.
- **No future-tense pre-commit claims** (PMN-004 §5 (c)): every Builder claim's verification command produces verifiable output at pre-commit time against the working tree. The "filled at step-10" Evidence section pattern is acceptable per discipline (c).

## Blocking questions

None at handoff time. If any surface during execution, Builder stops and surfaces to owner via spec §14 stop-and-show.

## Validation run

Filled by Builder at step-10 self-verification per spec §7, against the working tree at branch tip on `feat/task-0011-pmn-006` prior to Codex desktop pre-commit review. Per PMN-005 §4.4 sub-rule (e.1), cumulative-diff-stats re-derivation runs after every path-(a) revision iteration; the Evidence section is populated only with landed exact counts.

- **Commands** (bash, Git Bash on Windows 11):
  - Claim 1: `[ -f docs/post-merge-notes/PMN-006-pr-10-cycle-learnings.md ] && head -1 docs/post-merge-notes/PMN-006-pr-10-cycle-learnings.md`
  - Claim 2: `grep -cE "^## §[0-9]" docs/post-merge-notes/PMN-006-pr-10-cycle-learnings.md`
  - Claim 3: `awk '/^### §1\.1/,/^### §1\.2/' docs/post-merge-notes/PMN-006-pr-10-cycle-learnings.md | grep -cE "^[0-9]+\. \*\*"`
  - Claim 4: `grep -cE "\(g\.[12]\)|\(h\.[123]\)" docs/post-merge-notes/PMN-006-pr-10-cycle-learnings.md`
  - Claim 5: `grep -cE "\(i\.[1234]\)" docs/post-merge-notes/PMN-006-pr-10-cycle-learnings.md`
  - Claim 6: `grep -cE "(b\.3)|frontmatter-vs-body" docs/post-merge-notes/PMN-006-pr-10-cycle-learnings.md`
  - Claim 7: `grep -c "submitted_at > " core.md` and `grep -c "created_at > " core.md` and `grep -c "submitted_at >=" core.md` and `grep -c "created_at >=" core.md` and `grep -c "select(.user.login" core.md`
  - Claim 8: `grep -c "git fetch && git status" core.md` and `grep -nE "git rev-parse HEAD.*expected" core.md` and `grep -c "git status --porcelain" core.md`
  - Claim 9: `grep -nE "§[0-9]+(\.[0-9]+)*" docs/post-merge-notes/PMN-006-pr-10-cycle-learnings.md docs/reviews/PR-11-codex-pre-commit.md docs/handoffs/TASK-0011-pmn-006-pr-10-cycle-learnings.md` (iterative-to-convergence per §23.6.2)
  - Claim 10: visual frontmatter-vs-body reconciliation on PMN-006 + PR-11 review-context + TASK-0011 handoff
  - Claim 11: `git diff --stat $(git merge-base HEAD origin/main)..HEAD` (post-staging-and-commit)
  - Claim 12: `grep -c "Blocking / Major / Minor" docs/reviews/PR-11-codex-pre-commit.md`
  - Claim 13: Builder attestation that each of claims 1-12's verification command was run against pre-commit working tree and produced asserted result; (g)/(h)/(i) self-application sweep iteration count recorded in Evidence section

- **Results** (per-claim verification, all PASS):
  - Claim 1: PASS — `head -1 docs/post-merge-notes/PMN-006-pr-10-cycle-learnings.md` returns `# PMN-006 — PR-10 cycle learnings: verification-artifact-validity discipline split (g)/(h) + cross-document state verification (i) + bounded-continuation rule + four preliminary observations`
  - Claim 2: PASS — `grep -cE "^## §[0-9]" docs/post-merge-notes/PMN-006-pr-10-cycle-learnings.md` returns `9`
  - Claim 3: PASS — `awk '/^### §1\.1/,/^### §1\.2/' docs/post-merge-notes/PMN-006-pr-10-cycle-learnings.md | grep -cE "^[0-9]+\. \*\*"` returns `9` (defect count was originally 8 per spec; defect 9 added at step-8 execution time per path-(β) record-and-proceed; cross-surface count claim consistency verified at iteration 2 of §23.6 self-review)
  - Claim 4: PASS — `grep -cE "\(g\.[12]\)|\(h\.[123]\)" docs/post-merge-notes/PMN-006-pr-10-cycle-learnings.md` returns `16` (each sub-shape label appears multiple times across §3.1 / §3.2 / §3.3 prose; ≥5 distinct labels required, all 5 present)
  - Claim 5: PASS — `grep -cE "\(i\.[1234]\)" docs/post-merge-notes/PMN-006-pr-10-cycle-learnings.md` returns `9` (4 distinct sub-shapes (i.1)/(i.2)/(i.3)/(i.4) across §7.3 + cross-references)
  - Claim 6: PASS — `(b\.3)` and `frontmatter-vs-body` both present in §3.4 reclassification statement and §8 refinement summary
  - Claim 7: PASS — `submitted_at > ` returns 0; `created_at > ` returns 0; `submitted_at >=` returns 1; `created_at >=` returns 1; `select(.user.login` returns 2 (one per endpoint, preserved through substitution)
  - Claim 8: PASS — `git fetch && git status` returns 0; `git rev-parse HEAD.*expected` returns ≥1 in §24.3.1 context (line 185); `git status --porcelain` returns ≥1 (clean-tree adjunct present)
  - Claim 9: PASS — section-citation sweep iteration 1 surfaced count drift on cross-surface "8 defects" → "9 defects" propagation across PR-11 review-context claim 3 (fixed at iteration 1); iteration 2 zero defects → fixed-point convergence per §23.6.2; PMN-006 internal §N citations land in 1-9 range; PMN-005 citations land in 1-7 range; PMN-004 citations land in 1-8 range; core.md citations resolve at HEAD (post-correction state); AMAS v2.14.1 §17/§18 references are out-of-tree (acceptable per spec convention)
  - Claim 10: PASS — frontmatter-vs-body reconciliation clean: PMN-006 title and §1 both reference PR-10 cycle; TASK-0011 handoff frontmatter `task_id: TASK-0011` matches body `# TASK-0011 — ...` opening; `linked_pr: (filled at step-18 fix-up...)` pending-form acceptable pre-merge per PMN-001 (k); PR-11 review-context metadata block PR ID = PR-11, TASK ID = TASK-0011, branch = feat/task-0011-pmn-006 — all consistent with body claims
  - Claim 11: PASS — cumulative diff stats per `git diff --numstat HEAD` (post-`git add -N` of three new files): see Evidence subsection below; all counts are landed exact values (no `~` prefixes)
  - Claim 12: PASS — `grep -c "Blocking / Major / Minor" docs/reviews/PR-11-codex-pre-commit.md` returns `6` (≥2 required)
  - Claim 13: PASS — (g)/(h)/(i) self-application sweep on PR-11 review-context's own claim blocks: each claim's verification command timing labels match what the command produces (g.1); example outputs match labels (g.2); pagination is n/a (no `gh api` calls in this review-context's claims; (h.1) trivially satisfied); commands prove what they claim (h.2); no timestamp filters in the review-context's own commands ((h.3) trivially satisfied for these claims; (h.3) IS the load-bearing discipline applied to core.md §8.1.1.1 corrections per claim 7); cross-document state assertions verified against actual repo state (i.1-i.4) — all PMN-006 / TASK-0011 handoff / core.md path / content references verified during step 9 §23.6 self-review iteration 1+2. Iteration count to convergence: 2 iterations (iteration 1 surfaced count drift on defect-9 propagation; iteration 2 verified fixed-point).

- **Evidence** (cumulative diff stats; landed exact counts only per (e.1)):

```
core.md                                                                  | 5 insertions, 3 deletions
docs/handoffs/TASK-0011-pmn-006-pr-10-cycle-learnings.md                 | 161 insertions, 0 deletions (new file)
docs/post-merge-notes/PMN-006-pr-10-cycle-learnings.md                   | 329 insertions, 0 deletions (new file)
docs/reviews/PR-11-codex-pre-commit.md                                   | 176 insertions, 0 deletions (new file)
4 files changed, 671 insertions(+), 3 deletions(-)
```

Per-file landed exact counts (re-derived from `git diff --numstat HEAD~1..HEAD` against actual landed commit state per (e.1); landed exact counts only):
- `core.md`: 5 insertions + 3 deletions (8 changes; §8.1.1.1 polling-block timestamp filters changed for both endpoints with surrounding prose addition; §24.3.1 point 2 replacement)
- `docs/handoffs/TASK-0011-pmn-006-pr-10-cycle-learnings.md`: 161 insertions (new file; this handoff including this Evidence section as filled at step 10; landed-after-Evidence-section-fill count, re-derived post-commit per (e.1) sub-rule iterative application — initial pre-fill estimate was 127, post-fill landed exact is 161)
- `docs/post-merge-notes/PMN-006-pr-10-cycle-learnings.md`: 329 insertions (new file; PMN-006 with 9 §-headers and 9 honesty record defects)
- `docs/reviews/PR-11-codex-pre-commit.md`: 176 insertions (new file; PR-11 Codex desktop pre-commit review-context with 13 claims)
- Total: 671 insertions, 3 deletions across 4 files. Decomposition: `5 + 161 + 329 + 176 = 671` insertions; `3 + 0 + 0 + 0 = 3` deletions.

Note: `README.md` is NOT modified in this cycle per PMN-006 §1.1 defect 9 (spec deliverable 5 asserted a non-existent "PMN file table"; routed to path-(β) record-and-proceed per bounded-continuation rule §5.3 generalized cross-surface). Spec §7.1 expectation `git status --porcelain | grep -c "^ M README.md"` should return `1` per spec; actual returns `0`. The spec expectation is the defect-9-bearing assertion; actual repo state is the corrected ground truth.

Section-citation sweep iteration count: 2 iterations to fixed-point convergence (iteration 1 surfaced cross-surface count drift on defect-9 propagation across PR-11 review-context claim 3 expected value `8` vs actual `9`; iteration 2 zero defects after the count fix). Builder convergence at 2 iterations matches §3.1 role-axis-dependence preliminary hypothesis target (2-3 iterations expected for Builder mechanical-application scope; this cycle observed 2; first data point post-PMN-006 canonicalization of (i) discipline).

(g)/(h)/(i) self-application sweep iteration count: integrated with §23.6 self-review at iteration 2; no separate iteration count.

Forward-reference set (per spec convention, recognized as out-of-tree per spec §13 — gitignored or AMAS v2.14.1 legacy doc — NOT slips):
- PR-10 spec §1.4 — gitignored per ADR-001 decision 15
- AMAS v2.14.1 §17 / §18 — legacy doc not yet migrated to core.md; deferred to Part B (TASK-0012)

## Exact next step

This handoff is delivered at cycle close (steps 1-13 complete per §Last completed step). The pending actions are post-hand-back, not Builder-execution-of-spec:

1. Architect-side §24.3.1 five-point post-handback check absorption (now per the corrected canonical form: `git rev-parse HEAD` + expected-SHA + `git status --porcelain` clean-tree per (h.2) corrected text).
2. Owner invokes `@codex review` on PR-11 per ADR-001 decision 11 (Builder does not invoke).
3. Builder absorbs Codex post-PR review via two-endpoint poll per §8.1.1.1 corrected canonical form (per (h.3) — `>=` plus last-seen-ID tie-breaker on both `submitted_at` and `created_at` endpoints; author filter preserved); reconciles findings per §8.1.1.2.
4. Path-(a) revisions via fix-up commits on `feat/task-0011-pmn-006` if Codex findings or Architect five-point check surface defects; bounded-continuation rule per PMN-006 §5.3 applies if same-class findings recur (first finding path-(a); subsequent same-class path-(β) record-and-proceed; carry to PMN-007 if substantive).
5. Owner-merges PR-11 (squash-merge per ADR-001 decision 9); merge SHA substituted into Linked-PR field of this handoff per PMN-001 (k) fix-up convention.
6. Architect updates merge commit body with post-PR-window content per M-A7 operationally canonical pattern (PMN-006 §6.2). M-A7 §-section text in core.md deferred to Part B (TASK-0012).
7. Architect adjudicates PMN-007 emission per cycle-summary observations; if emit, PMN-007 cycle is authored before TASK-0012 / Part B per established PMN-after-cycle cadence.

The Builder workflow that produced this handoff (spec-execution sequence 1-13) is documented in §Last completed step for historical record; do NOT re-execute that sequence on receipt — it is complete.

## Reassessment / expiry

Handoff status flips to `resolved` after PR-11 is merged. If pre-commit Codex review exceeds scope or owner declines stop-and-show, status flips to `blocked` pending Architect direction. If Builder execution is delayed by more than ~48 hours from spec authoring time (2026-05-02), Builder runs reassessment per established framework reassessment-on-delay practice: re-derive repo state from `git log` before proceeding; surface any divergence from spec §10 reassessment triggers (7-day staleness; interim merge to main; ADR-004+ adoption).
