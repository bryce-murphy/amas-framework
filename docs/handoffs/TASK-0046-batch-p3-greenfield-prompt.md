---
task_id: TASK-0046
title: Batch P3 greenfield kickoff prompt (split cycle 1 of 2)
pr: PR-75
branch: feat/task-0046-batch-p3-greenfield-prompt
linked_predecessor: TASK-0045 (PR-73 substantive squash 583e12e + PR-74 chore-fix-up squash a030554)
linked_successor: TASK-0047 (anticipated; Batch P3 retrofit + upgrade prompts — split cycle 2 of 2)
linked_pr: PR-75 (squash SHA 32c4afa)
framework_version_dogfooded: v2.42
production_target: v3.0.0
spec_source: .claude/session-handoffs/task-0046-spec.md
date_authored: 2026-05-30
status: resolved
---

# HANDOFF: TASK-0046 — Batch P3 greenfield kickoff prompt (split cycle 1 of 2)

## Metadata

- **Cycle class**: Batch P3 substantive content-fill (prompt scaffold) — split cycle 1 of 2 (greenfield solo; retrofit + upgrade deferred to TASK-0047)
- **§0 salience**: HIGH (first prompt-class cycle establishing the canonical kickoff-prompt scaffold; §23.6.5 behavioral empirical test #1; recursive self-application — a kickoff prompt authored under AMAS cycle discipline)
- **Branch**: feat/task-0046-batch-p3-greenfield-prompt
- **HEAD anchor**: main HEAD at post-PR-74-merge state (`a030554`)
- Linked PR: PR-75 (Builder fills with squash SHA post-merge per PMN-001 (k))
- **Spec source**: `.claude/session-handoffs/task-0046-spec.md` (gitignored per ADR-001 D15)
- **Cycle-protocol baseline**: standard per `core.md` §23.6.x + §24.5 + §24.6
- **§23.6.5 behavioral taxonomy (empirical test #1; applied this cycle BEFORE Part C.2 canonicalization)**: this handoff's body surfaces are classified into two tiers. **Gate-current** (refreshed ONLY at gates — Gate A initial + each Gate A re-application after absorption + Gate B + Gate B re-applications; inter-gate staleness ACCEPTED by-design): §Last completed step, §Current state Summary, §Cumulative-diff-stats. **Append-only historical** (never back-refreshed; only appended; reference volatile state BY POINTER, e.g. "see §Cumulative-diff-stats", NOT by pinned value): §3 step-by-step execution record, §6 pre-commit absorption, §8 post-PR review state, §10 cycle-close ledger. The **sole canonical cycle-close marker** is action-filled frontmatter (`linked_pr` squash SHA + `status: resolved` + review-context `status: recorded`); NO body surface is a close marker.

## Objective

Fill `prompts/greenfield.md` (was stub: `status: stub`, `filled_by: per ADR-003`) with the canonical greenfield project-kickoff prompt — a paste-ready operator-facing artifact that runs one greenfield kickoff session producing the bootstrap artifact set. Frontmatter transition `status: stub → drafted` + `filled_by: per ADR-003 → PR-75 (TASK-0046)`. Co-shipped distributed-update surfaces: `core.md` §18.3 M-A7 32nd-instance amendment per Adj 8 ((XXI) line-shared) + Class A v-bump v2.41 → v2.42 minor at 4 sites (README L9 ×2 + AGENTS L9 + CLAUDE L9) + README roadmap L30 four-anchor post-split shift (Finding A) + README Prompts table greenfield row + `usage-guide.md` forthcoming-qualifier sweep at L22 + L370 (Finding B; greenfield-only drop, retrofit/upgrade retained at TASK-0047) + this handoff + PR-75 pre-commit review-context. Single prompt this cycle; retrofit + upgrade deferred to TASK-0047 per Batch P3 split.

## Last completed step

*[GATE-CURRENT surface — refreshed at gates only.]*

Step-13 Codex post-PR pass-1 absorbed at Gate B: P2 (handoff §Current-state status-descriptor staleness) → path-(a) gate-current refresh; Step-4 hardening (project-profile elicitation) → path-(a); phantom delivery-layer claims (commit `2b5cfd1` + follow-up PR via `make_pr`) verified non-existent → §8.1.1.2 ledger (IX); usage-guide §2.1 alignment → path-(β) decline/carry-forward → ledger (X). All gate-current surfaces refreshed to final pre-merge state. Cumulative-diff-stats: see §Cumulative-diff-stats (gate-current).

Exact next step: owner squash-merge per ADR-001 D9 → PMN-001 (k) Action (linked_pr squash SHA + handoff `status: active → resolved` + review-context `drafted → recorded`; auto-fires chore-fix-up PR per ADR-004) → branch cleanup → cycle-close — pending Gate B ratification.

## Current state

*[GATE-CURRENT surface — refreshed at gates only.]*

**Summary**: Cycle progression through step-13 (final pre-merge state): pre-flight 11/11 (Findings A + B adjudicated; §2/§4 confirmed) → step-2 branch → step-3 greenfield.md authored (ratified) → step-4 §18.3 M-A7 32nd-instance → step-5 Class A v-bump v2.41 → v2.42 → step-6 README roadmap 4-anchor shift + Prompts row + usage-guide L22/L370 sweep → step-7 handoff (this file) + step-8 PR-75 review-context authoring → step-9 self-review to fixed-point → Gate A ratified → step-9.X path-(α') token-swap (greenfield.md `drafted → active`) → step-10 Codex pre-commit pass-1 (2 substantive, 0 blocking) absorbed at step-11 Gate A re-application → step-12 commit (`a63b272`) + push + PR #75 open → step-13 Codex post-PR pass-1 absorbed (P2 → path-(a) gate-current refresh; Step-4 hardening → path-(a); phantom delivery-layer claims → §8.1.1.2 ledger (IX); §2.1 alignment → path-(β) ledger (X)). `prompts/greenfield.md` is `status: active`, Step 4 hardened with project-profile elicitation. (XVII) bidirectional sum-stability PASS at all 3 axes. Awaiting Gate B ratification before owner squash-merge.

**Files authored / modified by Builder**:
1. MODIFIED `prompts/greenfield.md` — stub → active; frontmatter `status: stub → active` + `filled_by: per ADR-003 → PR-75 (TASK-0046)`; body = paste-ready greenfield kickoff prompt (Step 0 context + Steps 1-6 mapping the 7 content obligations per spec §2 to usage-guide anchors; Step 4 hardened at step-13 with project-profile elicitation per Codex post-PR path-(a)). Ratified at step-3 + step-13 Gate B.
2. MODIFIED `core.md` — §18.3 M-A7 32nd-instance amendment at the (XXI) line-shared cluster (preamble + count+span line + steady-state line); 3 substitution lines.
3. MODIFIED `README.md` — L9 Class A v-bump v2.41 → v2.42 (×2 same-line); L30 roadmap four-anchor post-split shift (greenfield 0046 / retrofit+upgrade 0047 / Part C.2 0048 / release 0049; both end-sequence + mid-paragraph anchors per Finding A); Prompts table greenfield row → `PR-75 (TASK-0046)`.
4. MODIFIED `AGENTS.md` — L9 Class A v-bump v2.41 → v2.42.
5. MODIFIED `CLAUDE.md` — L9 Class A v-bump v2.41 → v2.42.
6. MODIFIED `usage-guide.md` — forthcoming-qualifier sweep at L22 + L370 (Finding B): greenfield qualifier dropped (now live); retrofit + upgrade retained forthcoming, qualifier currentness updated `TASK-0025+ → TASK-0047`. §11.3 + L24 untouched (anti-scope).
7. NEW `docs/handoffs/TASK-0046-batch-p3-greenfield-prompt.md` — this file; PMN-007 HEAD canonical 12-field frontmatter + §23.6.5 behavioral taxonomy applied; Adj 11 canonical regex placeholder at L8 `linked_pr`.
8. NEW `docs/reviews/PR-75-codex-pre-commit.md` — PR-75 pre-commit review-context; `core.md` §17.7 1-field frontmatter (`status: drafted`); Builder-claims list + §23.6.5 Codex taxonomy block.

**Cumulative-diff-stats** *(gate-current; refreshed at Gate B — final pre-merge state)*: 8 files / 513 insertions(+) / 13 deletions(-) vs `main` (whole-PR cumulative; the step-13 absorption added a +23/−6 increment over the step-12 commit `a63b272`). (XVII) bidirectional sum-stability PASS at all 3 axes (per-file ins sum 513 = shortstat; del sum 13 = shortstat; row count 8 = shortstat file-count). Within spec §6 envelope (~380-600 ins / ~12-18 del / 6-8 files). Substantive-scope-creep trigger NOT met: greenfield prompt body = 159 lines (well under ~260 ins trigger; no retrofit/upgrade mode-logic added).

## Decisions made

Per spec adjudications + step-1 Architect adjudication of pre-flight Findings A + B:

1. **Cycle class**: Batch P3 substantive content-fill, split cycle 1 of 2 (greenfield solo). RATIFIED per ADR-008 D2 + Batch P3 split (no new ADR — split within a batch is per-cycle defect-surface-narrowing discretion, parallel to Batch P2 TASK-0043/0044 split).
2. **Greenfield prompt structure**: 7 content obligations per spec §2, authored as paste-ready operator prose (not a checklist), mode-neutral scaffold so retrofit/upgrade (TASK-0047) inherit Steps 0-6 with mode-specific deltas.
3. **§3.1 reference form**: `core.md §3.1 (forthcoming at Part C+)` — UNMATERIALIZED confirmed at pre-flight (first substantive § = §8); prompt references the bootstrap set as operational guidance sourced through usage-guide §2.3, NOT as materialized canonical law; does NOT materialize §3.1.
4. **Finding A (README L30 two-anchor shift)**: RATIFIED — L30 carries TWO Part C.2 → TASK-0048 anchors (mid-paragraph "anticipated at" + end-sequence) plus release → TASK-0049; both shifted. AGENTS/CLAUDE L12 are task-number-free (untouched).
5. **Finding B (usage-guide shared-line sweep)**: RATIFIED — L22 + L370 are the two real greenfield-forthcoming targets, both shared-line; greenfield split out as live, retrofit/upgrade retain forthcoming with qualifier updated to TASK-0047 (disposition (a)). §1.2 + §2.1 carry no qualifier (untouched); §11.3 report-only this cycle (see §10 ledger).
6. **M-A7 32nd-instance**: count 31 → 32 at v2.42 per (XXI) line-shared; verified at pre-flight (count was 31 at v2.41).
7. **Class A v-bump tier**: minor v2.41 → v2.42 per `core.md` §18.4 substantive-reading minor criterion (new operator-facing prompt content).
8. **§23.6.5 behavioral discipline (empirical test #1)**: applied BEHAVIORALLY this cycle (handoff gate-current/append-only surface taxonomy + review-context pre-commit claims as append-only "snapshot at pre-commit Gate A"); NOT canonicalized as text (Part C.2 / TASK-0048 territory per anti-scope).
9. **No PMN co-ship** per Adj 12 trigger-based posture (cycle-close ledger carries observations forward).
10. **Handoff authoring-time status**: `status: active` per step-7 direction (PMN-001(k) Action flips `active → resolved` post-merge); greenfield.md stays `drafted` until post-Gate-A path-(α'); review-context `drafted`. (Surfaced at Gate A for Architect confirmation.)

## Assumptions

- Repo state at pre-flight: main HEAD `a030554`, parity with origin/main, working tree clean (verified at step-1 pre-flight; 11/11).
- PR-75 next available PR number (PR-73 substantive + PR-74 chore-fix-up consumed). Phantom-corrected at PR-open if actual diverges (appears in 5 surfaces: greenfield.md `filled_by`, README Prompts row, M-A7 enumeration, this handoff `linked_pr`, review-context filename).
- Codex Reviewer operational at desktop session per ADR-001 D11; owner invokes Codex pre-commit at step-10 + `@codex review` post-PR per ADR-001 D11.
- linked-pr-fix-up Action operational at PR-75 squash-merge per PMN-001 (k) regex strict-match form.
- substrate v2.14.1 §2.3.6 unreachable (URL 404 confirmed at pre-flight item 10; non-blocking); usage-guide §1-§3 + filled templates are the authoritative structural source. `amas-v3-transition-plan-v0_2.md` absent from repo (pre-flight item 9; not git-tracked) — no authority conflict.

## Risks

- **(R1) First prompt-class scaffold propagation**: scaffold defects propagate to retrofit + upgrade (TASK-0047). Mitigated by mode-neutral scaffold design (Decision 2) + 2-iteration self-review fixed-point + operator-usability review priority at Codex pre-commit (spec §9).
- **(R2) §23.6.5 behavioral empirical test**: this cycle dogfoods the gate-current/append-only refresh discipline before canonicalization. If the discipline reduces churn vs TASK-0045 (claim-7/8/12 rewrite churn), it strengthens the TASK-0048 canonicalization case (see §10 ledger; carry-forward to TASK-0048 per spec §11).
- **(R3) PR-number anticipation**: PR-75 anticipated across 5 surfaces; verify at step-11 against actual GitHub assignment; phantom-correct together at PR-open if divergent.
- **(R4) Recursive self-application**: a kickoff prompt orchestrating AMAS bootstrap is authored under AMAS cycle discipline; the prompt's own canonical-section references must be currency-correct. Verified at step-9 reference-resolution sweep.

## Blocking questions

None. Step-1 pre-flight 11/11 with Findings A + B adjudicated by Architect at step-1 stop-and-show; step-3 greenfield.md ratified at step-3 stop-and-show. Architect Gate A applies at this step-9 stop-and-show + Gate B at step-12+ post-PR-open per `core.md` §24.3.1 (XXVI).

## §1. Cycle scope deliverables enumeration

Parallel to spec §4 (8 files: 6 modified + 2 new):

1. MODIFIED `prompts/greenfield.md` — stub → filled (spec §4.1)
2. MODIFIED `core.md` — §18.3 M-A7 32nd-instance (spec §4.2)
3. MODIFIED `README.md` — Class A v-bump (spec §4.3) + roadmap L30 4-anchor shift (spec §4.4) + Prompts row (spec §4.5)
4. MODIFIED `AGENTS.md` — Class A v-bump (spec §4.3)
5. MODIFIED `CLAUDE.md` — Class A v-bump (spec §4.3)
6. MODIFIED `usage-guide.md` — forthcoming-qualifier sweep L22 + L370 (spec §4.6)
7. NEW `docs/handoffs/TASK-0046-batch-p3-greenfield-prompt.md` (this file; spec §4.7)
8. NEW `docs/reviews/PR-75-codex-pre-commit.md` (spec §4.8)

Total: 8 unique files (anticipated 6-8 per spec §6).

## §2. Cycle gates

Per `core.md` §24.3.1 (XXVI) two-gate Gate A + Gate B:

- **Gate A** at step-9 pre-commit stop-and-show: cumulative-diff-stats + (XVII) bidirectional sum-stability + spec §10 verification baseline + (XIV) sweep + (XXIV.a-n) catalog at staged-tree state per `core.md` §23.6.1.1 (e.1). §23.6.5 behavioral: refresh gate-current body surfaces here.
- **Gate B** at step-12+ post-PR-open: cycle-close completeness; gate-current surfaces refreshed; append-only surfaces appended (never back-edited).
- **§24.6 Stop-Iteration framework** at reach 4+ canonical boundary: HIGH §0 salience; (B-3) HYBRID closure mechanism available per spec §8 step-12.

## §3. Step-by-step execution record

*[APPEND-ONLY HISTORICAL surface — never back-refreshed; references volatile state BY POINTER.]*

- Step-1 pre-flight: 11/11 verification items run read-only against main HEAD `a030554`. §2/§4 spec assumptions substantively confirmed (M-A7 count 31 at v2.41; Class A v2.41 ×4; §3.1 unmaterialized — first substantive § = §8; greenfield stub confirmed; retrofit/upgrade stubs). Two anchor-completeness findings surfaced + Architect-adjudicated: Finding A (README L30 has TWO Part C.2 → TASK-0048 anchors, not one) + Finding B (usage-guide L22 + L370 shared-line; §1.2/§2.1 non-targets; §11.3 report-only). substrate §2.3.6 404 (non-blocking); transition-plan absent from repo. Hand-back → Architect adjudication + step-2/step-3 authorization.
- Step-2 branch: `feat/task-0046-batch-p3-greenfield-prompt` created from main HEAD `a030554`; `git pull` clean; ADR-005 Option B + `github-reference.md` §2.2 regex compliant; working tree clean post-checkout.
- Step-3 greenfield.md authoring: frontmatter transition + paste-ready body (Step 0 + Steps 1-6 mapping 7 content obligations to usage-guide anchors). Self-review 2 iterations to fixed-point (iteration 1 residual: Step 6 cross-references omitted the canonical-law trio per spec obligation 7; fixed iteration 2). Body 155 lines (envelope 120-220; substantive-scope-creep trigger ~260 NOT hit; no retrofit/upgrade mode-logic). Ratified at step-3 stop-and-show; body LOCKED.
- Step-4 §18.3 M-A7 32nd-instance: 3 byte-exact substitutions at the (XXI) line-shared cluster (preamble `v2.41/PR-73/TASK-0045 → v2.42/PR-75/TASK-0046`; count+span line `+ PR-73 = 31 → + PR-73 + PR-75 = 32` AND `through v2.41 → through v2.42`; steady-state `31 → 32 consecutive`). `= 31` residual count = 0 in core.md; other M-A7 doctrine/evidence mentions untouched.
- Step-5 Class A v-bump v2.41 → v2.42 at 4 sites: README L9 ×2 (same-line replace_all) + AGENTS L9 + CLAUDE L9. v2.42 count = 4 (2/1/1); v2.41/v2.40 residuals = 0. AGENTS/CLAUDE L12 task-number-free (untouched).
- Step-6 README roadmap + Prompts row + usage-guide sweep: (6a) L30 four-anchor post-split shift — end-sequence `Batch P3 greenfield (TASK-0046) → Batch P3 retrofit + upgrade (TASK-0047) → Part C.2 (...; TASK-0048) → release polish + v3.0.0 tag (TASK-0049...)` + mid-paragraph `anticipated at TASK-0048`; no 5th anchor (L7 task-number-free). (6b) Prompts greenfield row → `PR-75 (TASK-0046)`; retrofit/upgrade rows unchanged. (6c) usage-guide L22 + L370 greenfield-forthcoming drop, retrofit/upgrade retained at TASK-0047; §1.2/§2.1/§11.3 untouched.
- Step-7 handoff (this file) + step-8 PR-75 review-context authoring (THIS step): NEW handoff + NEW review-context authored; frontmatter canonical forms (12-field PMN-007 HEAD + 1-field §17.7); Adj 11 regex placeholder at L8; §23.6.5 behavioral taxonomy labels applied (this handoff) + pre-commit claims labeled "snapshot at pre-commit Gate A" (review-context).
- Step-9 self-review to fixed-point: see §5 (gate-current iteration log). Cumulative state: see §Cumulative-diff-stats.

## §4. Substantive-content evidence per deliverable

- greenfield.md: frontmatter `status: active` + `filled_by: PR-75 (TASK-0046)`; 7-obligation coverage (preamble/attach-then-paste §2.1; operating-environment §2.4; three-tier §2.5; scorecard + ecosystem-fallback guard §2.5/§2.6; bootstrap set §2.3 verbatim 11-item + both trip-ups + §3.1 forthcoming + lite-kickoff one-way caveat; follow-ups + handoff §2.7/§2.9 + Issue-0 closure → project-initiation §7; cross-references incl. canonical-law trio); all citations resolve against current main.
- core.md §18.3: M-A7 32nd-instance at (XXI) line-shared cluster; `= 31` residual = 0.
- Class A: v2.42 ×4 (README L9 ×2 + AGENTS L9 + CLAUDE L9); zero v2.41/v2.40 residuals.
- README roadmap: 4-anchor post-split shift; Prompts greenfield row `PR-75 (TASK-0046)`; retrofit/upgrade rows preserved.
- usage-guide sweep: L22 + L370 greenfield live / retrofit+upgrade forthcoming at TASK-0047; anti-scope (§1.2/§2.1/§11.3 untouched).
- Frontmatter: handoff 12-field PMN-007 HEAD + Adj 11 regex placeholder at L8; review-context 1-field §17.7 (`status: drafted`).
- Branch regex: `feat/task-0046-batch-p3-greenfield-prompt` per ADR-005 Option B + `github-reference.md` §2.2.
- (XVII) bidirectional sum-stability: see Gate A stop-and-show.

## §5. Self-review record (step-9 §23.6.2 iteration log)

*[GATE-CURRENT for the convergence result; iteration log itself stable post-fixed-point.]*

Step-3 greenfield.md self-review: 2 iterations to fixed-point (iteration 1 residual: trio omitted from cross-references; iteration 2 clean). Step-9 whole-cycle self-review: iteration count + residuals reported at Gate A stop-and-show per `core.md` §23.6.2 + Adj 8 (XXIV.a-n) catalog + (XIV) 4-dimension sweep.

## §6. Pre-commit absorption (step-10 Codex desktop output absorption)

*[APPEND-ONLY HISTORICAL surface — populated post Codex pre-commit pass; never back-refreshed at later absorption.]*

Populated post Codex desktop pre-commit pass-1 (step-10) per `core.md` §8.1.1.2 phantom-action verification discipline. Pre-merge absorptions appended here (path-(a)/(β) per Architect routing); volatile state referenced BY POINTER (see §Cumulative-diff-stats gate-current).

## §7. Commit + push + PR-open record

Commit SHA: filled post-merge with squash SHA per PMN-001 (k) Action (pre-merge feature-branch HEAD transient — squashed at merge; no pre-merge amend SHA pinned, eliminating SHA-recursion source per TASK-0045 (XVII) lesson). Branch pushed at step-11; PR-75 opened (number verified vs anticipated at step-11; phantom-correct if divergent). Status `drafted → active` token-swap (greenfield.md) at step-9.X path-(α'). Linked-pr-fix-up Action at PR-75 squash-merge per PMN-001 (k): `linked_pr` SHA substitution + handoff `active → resolved` + review-context `drafted → recorded`.

## §8. Post-PR Codex review state

*[APPEND-ONLY HISTORICAL surface — populated post each Codex post-PR pass; never back-refreshed.]*

Populated post Codex desktop post-PR pass-1+ (step-12) per `core.md` §24.5 + §24.6. §24.6 Stop-Iteration framework + (B-3) HYBRID closure available. Findings + absorptions appended; volatile state by pointer.

## §9. Sign-off (§24.3.1 five-point check; Architect populates)

Populated by Architect at Gate B clearance per `core.md` §24.3.1 (XXVI).

## §10. Cycle-close ledger

*[APPEND-ONLY HISTORICAL surface — observations appended at cycle close; references volatile state BY POINTER.]*

- **(I)** First prompt-class cycle: greenfield establishes the canonical kickoff-prompt scaffold (mode-neutral Steps 0-6) that retrofit + upgrade (TASK-0047) inherit. Documentary observation; scaffold-correctness empirical record feeds TASK-0047.
- **(II)** §23.6.5 behavioral empirical test #1: gate-current/append-only surface taxonomy applied to this handoff + pre-commit-claims-as-frozen-snapshot to the review-context. Cycle-close captures whether the discipline reduced churn vs TASK-0045 (claim-7/8/12 rewrite churn) — input to §23.6.5 canonicalization at TASK-0048 (spec §11 carry-forward). (Populated at cycle close.)
- **(III)** Pre-flight Findings A + B: anchor-completeness refinements caught at step-1 verify-before-assert BEFORE authoring (Finding A README L30 two-anchor; Finding B usage-guide shared-line). Cross-cycle reach of (XXIV.k) parallel-form completeness sub-surface; verify-before-assert empirical positive (parallel to TASK-0045 step-1 catching 2 Architect-side spec defects).
- **(IV)** §18.3 M-A7 32nd-instance landed at v2.42 per (XXI) line-shared: 32 consecutive substantive cycles spanning v2.16 through v2.42.
- **(V)** §11.3 upgrade-forthcoming qualifier currentness: §11.3 retains `prompts/upgrade.md` (forthcoming at TASK-0025+)` — report-only this cycle (left untouched per step-6c direction). Parallel-form-consistency carry-forward candidate: Architect to adjudicate at TASK-0047 whether §11.3 (+ L24 appendices) warrant the same TASK-number currentness update the L22/L370 sweep applied.
- **(VI)** PR-number anticipation verification at step-11 — PR-75 anticipated across 5 surfaces; phantom-correct if divergent. (Populated at step-11.)
- **(VII)** §24.5 multi-surface review pipeline empirical record at first prompt-class cycle (populated at step-10+ / step-12+).
- **(VIII)** Codex pre-commit pass-1 F-2 root gap (append-only): `usage-guide.md` §2.7 + `prompts/greenfield.md` Step 5 reference a Project Brief **"Kickoff follow-ups"** section that `templates/project-brief-template.md` does not materialize. Hardened greenfield this cycle with a graceful-degradation parenthetical (path-(a)); root reconciliation left anti-scope. Preferred fix: add the "Kickoff follow-ups" section to `project-brief-template.md` so §2.7 + greenfield both resolve against a materialized template section. Candidate PMN; reconcile in a future template/canonical cycle (TASK-0047 template-adjacent or post-v3.0.0). Surfaced by Codex pre-commit pass-1 (F-2).
- **(IX)** Codex post-PR pass-1 §8.1.1.2 phantom-action instance (append-only): the post-PR review comment claimed it committed `2b5cfd1 fix(prompts): TASK-0046 absorb greenfield follow-up findings` on the branch and "Created a PR via `make_pr`". Both verified non-existent against repo state — `git cat-file -t 2b5cfd1` → not a valid object; no follow-up branch/PR in the all-state PR list; PR #75 branch tip remained `a63b272`; working tree clean. Codex narrated step-11's already-authored work (gate-current diff-stats refresh + review-context absorption section) as its own commits. Caught by §8.1.1.2 phantom-action verification; no action propagated; no delivery-layer artifact created. Empirical §8.1.1.2 instance — strengthens the verify-before-assert discipline at the post-PR receiving surface.
- **(X)** Codex post-PR pass-1 suggested aligning `usage-guide.md` §2.1 (attach-then-paste) to require the full canonical-law trio before pasting, matching greenfield Step 0 (append-only). Anti-scope this cycle: usage-guide §-body edits beyond the L22/L370 sweep are out per spec §5. Disposition path-(β) decline/carry-forward to a future usage-guide-touch cycle (bundle with the ledger-(VIII) §2.7 root-gap); verify then whether §2.1 under-specifies the trio vs greenfield Step 0. `usage-guide.md` left untouched this cycle.

PMN co-shipping NOT default at this cycle per ADR-006 D3 + Adj 12 trigger-based posture; carry-forward PMN candidacy to TASK-0048 release-polish or post-v3.0.0 retrospective.

**Architect post-merge maintenance**: linked-pr-fix-up Action operational at PR-75 squash-merge per PMN-001 (k) regex; handoff `active → resolved` + review-context `drafted → recorded` + `linked_pr` SHA substitution per Action script. Owner squash-merge authority per ADR-001 D9 admin-bypass. Auto-fire chore-fix-up PR anticipated per ADR-004 linked-pr-fix-up.yml Action.

## §11. Session log archive

Architect session record + Builder session record per AMAS v2.14.1 §13.1 substrate (`forthcoming at Part C+` in v3 `core.md`). Most recent session at PR body per substrate convention; prior sessions migrated here at cycle close.
