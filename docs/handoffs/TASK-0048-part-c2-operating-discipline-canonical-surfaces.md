---
task_id: TASK-0048
title: Part C.2 operating-discipline canonical surfaces materialization + class-bound qualifier sweep
pr: PR-86
branch: feat/task-0048-part-c2-operating-discipline-canonical-surfaces
linked_predecessor: TASK-0047 (PR-83 squash 3606278; Batch P3 upgrade prompt)
linked_successor: TASK-0049 (release polish + v3.0.0 tag)
linked_pr: PR-86 (squash SHA 0eb51f7)
framework_version_dogfooded: v2.45
production_target: v3.0.0
spec_source: .claude/session-handoffs/task-0048-spec.md
date_authored: 2026-06-03
status: resolved
---

# HANDOFF: TASK-0048 — Part C.2 operating-discipline canonical surfaces

> **§23.6.5 surface taxonomy legend (self-instantiation).** GATE-CURRENT surfaces (§Last completed step, §Current state Summary, §Cumulative-diff-stats) refresh only at gates; this handoff's gate-current surfaces reflect the **post-PR / Gate-B-approach** state (refreshed at the post-PR absorption commits). APPEND-ONLY HISTORICAL surfaces (the handoff's §3 step-by-step execution record, the §10 cycle-close ledger, and the post-PR/absorption sections once they exist) are never back-refreshed and reference volatile state by pointer. The §23.6.5 **suppression clause** applies to this handoff's own append-only surfaces. Sole canonical cycle-close marker = action-filled frontmatter (`linked_pr` squash SHA + `status: resolved`); no body surface asserts close.

## Metadata

- **Task**: TASK-0048 — materialize the five Part C.2 operating-discipline canonical surfaces + class-bound DROP/REWRITE/STAY sweep + D2 operational migration + standard cycle distributed-update.
- **PR**: PR-86 (anticipated; verified against live `gh pr list` — highest merged = #85; phantom-correct at PR-open per PMN-001 (k)).
- **Branch**: `feat/task-0048-part-c2-operating-discipline-canonical-surfaces` (per `github-reference.md` §2.2 + ADR-005).
- **Spec**: `.claude/session-handoffs/task-0048-spec.md` (gitignored per ADR-001 D15).
- **Primary ADRs**: ADR-007 (Part C scope/schedule), ADR-008 (P4→v3.1; Part C.2 in v3.0), ADR-006 D3, ADR-001 D9.

## Objective

Materialize §8.2, §8.3, §13/§13.1/§13.2, §10.5, §23.6.5 to enforcement-grade (schema elements + checkable predicate + Cross-references each); execute the 68-occurrence class-bound DROP (41) / REWRITE (14) / STAY (13) sweep + D2 root-file migration + the L546 fix + the +1 bare-ref; standard surfaces (Class A v2.44→v2.45, M-A7 35th, README roadmap). Last substantive-content cycle of v3.0.0; Batch P4 Actions DEFERRED to v3.1 (ADR-008).

## Last completed step  *(GATE-CURRENT — post-PR / Gate-B-approach state)*

Authoring + sweep + standard surfaces + artifacts done; §5 battery 10/10 PASS; Gate A cleared (twice — initial + post pre-commit-absorption). Codex pre-commit/red-team absorbed (3 path-(a): F1/F2/F3); committed `9098bd2`, pushed, PR #86 opened (PR-open re-verification: actual #86 = anticipated). Codex post-PR passes 1–8 absorbed and pushed: P1 §13.1 ratifications; P2 gate-current refresh; pass-3/4 self-volatile-pinned-total class (gate-current pointers, then de-pin); **pass-5 P2 = §23.6.5 by-pointer clarification; pass-6 = stale-head path-(β); pass-7 P2 = §13.1 parallel by-pointer clarification (by-pointer class then exhausted, 2 members); pass-8 P2 = §8.2 item-(4) pre-branch-timing fix.** Pushed through `0e77e00` (passes 9–10). Pass-11 (expanded) ratified + pushed through `bbb466e`. **Pass-12 (3 path-(a) §8.2-timing fixes: usage-guide quick-ref L404 + handoff-template pre-flight note L149 + core.md:161 §8.2 principle-intro fold-in; §8.2-timing class fully exhausted — principle + evidence-set + item-4 + predicate + all 6 mirror surfaces, grep-confirmed zero laggard) absorbed, Gate A re-cleared, ratified, and pushed.** Canonical+operational delta by-pointer (no pinned current total; L161 in-place, no line-count change).

## Current state Summary  *(GATE-CURRENT — post-PR / Gate-B-approach state)*

Five Part C.2 members materialized in `core.md` in document order (§8.2 → §8.3 → §10.5 → §13/§13.1/§13.2 → §23.6.5), each schema-grade. Class-bound sweep complete: in-scope qualifier residue = 0; STAY-13 byte-unchanged; D2 migration materialized-only (§2.3.6 retained as substrate); PR-template canonical converged to live attestation form with `.github` mirror byte-unchanged; §10.5 → `github-reference.md` §3.2 cross-ref present with provenance (:148/:379) untouched; L546 + the two ruled Item-14 migrations applied. Class A v2.45 across 4 sites (zero v2.44/v2.43 residual); §18.3 M-A7 35th internally consistent across 5 sub-claims; README roadmap rotated (Part C.2 shipped). Zero open same-cycle forward-refs. PR #86 open; Codex pre-commit (3) + post-PR passes 1–12 absorbed + pushed; **pass-12 (3 §8.2-timing fixes + core.md:161 principle-intro fold-in; §8.2-timing class fully exhausted, grep-enumerated) Gate-A-re-cleared, ratified, and pushed.** Canonical+operational delta by-pointer; no surface pins a current total. Awaiting binding Codex re-review → Gate B.

## Cumulative-diff-stats  *(GATE-CURRENT — post-PR / Gate-B-approach state; re-derive (e.1) at each staged-tree mutation)*

- **Canonical + operational surfaces (10 files: core.md, usage-guide, AGENTS, CLAUDE, README, templates/{AGENTS, CLAUDE, handoff-template, PULL_REQUEST_TEMPLATE, role-scorecard})**: current delta **by pointer** — `git diff main --numstat` (restrict to those paths). **Not pinned here**, per §23.6.5 reference-volatile-by-pointer: the figure moves whenever a canonical surface changes (e.g. the post-PR §8.3 `gh pr edit` bullet + the §10.5/usage-guide bypass rewording), so no surface pins a current total — this closes the self-volatile-pinned-total class completely. *(Historical snapshot, correct-by-design: clusters C1–C4 contributed +128 pure-add to core.md.)*
- **Cycle artifacts (this pass)**: + PMN-019, + this handoff, + review-context `PR-86-codex-pre-commit.md` (3 new files).
- **Full staged total (incl. the 3 self-volatile cycle artifacts)**: **by pointer** — `git diff main --shortstat`; **not pinned here**, per §23.6.5 reference-volatile-by-pointer (the full total moves on every docs-only fix-up). With L42 also by-pointer, **no surface in this cycle pins a current total** — the self-volatile-pinned-total class is fully closed. github-reference.md + `.github/PULL_REQUEST_TEMPLATE.md` byte-unchanged (0/0).
- **(XVII) two-axis**: occurrence DROP 41 + REWRITE 14 + STAY 13 = 68 (STAY held at 13); line-edit 37 DROP + 14 REWRITE + 1 bare-ref + 1 L546 = 53.

## Decisions made

1. §0 D1 class-bound residual sweep + D2 materialized-only migration executed exactly per spec ledger.
2. §10.5 hosted under a **minimal §10 parent** (heading + one-sentence intro; §10.1–§10.4 noted substrate/forthcoming) per doc convention (no orphan §X.Y).
3. L546 ruled option-(a) (current/most-recent → §13.2; prior/migrated → §13.1); both ruled Item-14 migrations (handoff-template:143; templates L68/L69) applied in Pass B STEP 0.
4. Templates L45 DROP required a **coherent rewrite** to a `core.md` citation (token-removal would break the sentence) — 1 line-edit in the ledger.
5. M-A7 35th term written as `PR-NN` **manual-substitution placeholder** in `core.md` (L583 + L585) — NOT Action-governed (see Blocking questions / Cycle-close ledger).

## Assumptions

- Anticipated PR number = **PR-86**, verified against live `gh pr list --state all` (highest merged = **#85**, TASK-0047 PR-B close-reconciliation). NB: the entry-state handoff's "highest = 84" was stale — F1 (Codex BLOCKING) caught the resulting PR-85 mis-anticipation; corrected here. Phantom-correct again at PR-open per PMN-001 (k) across handoff `pr`/`linked_pr`, PMN-019 `linked_pr`, review-context, and the M-A7 `PR-NN` term.
- Entry anchor verified empirically: `main` HEAD `b46e46e`, v2.44, M-A7=34, TASK-0047 closed, tree clean (step-1 16/16 PASS).

## Risks

- **M-A7 `PR-NN` placeholder** is non-Action-governed canonical-body text; if the post-merge manual reconciliation is skipped, `core.md` ships with `PR-NN` at L583 + L585. Mitigated by the explicit Cycle-close ledger item + the inline note. (Approved approach, Pass B.)
- Anticipated PR-86 divergence at PR-open → phantom-correct the numeric across all artifacts (frontmatter, body, review-context filename, M-A7 term) before the post-PR pass and merge.

## Blocking questions

None open. Two Item-14 finds were ruled (option-(a)) and applied. The M-A7 Action-vs-manual scope is recorded as a confirmed finding (Cycle-close ledger), not a blocker.

## Validation run

§5 battery (10/10 PASS) — see §Sub-phase execution record + the review-context Builder-claims block. Key greps: in-scope residue = 0; STAY-13 = 13; 5 headings document-ordered; Class A v2.45 ×4; M-A7 5-claim consistency; github-reference.md + `.github` byte-unchanged.

## Exact next step  *(GATE-CURRENT — post-PR / Gate-B-approach state)*

Owner re-invokes the binding Codex re-review (`usage-guide.md` §7.1/§7.3) against the **latest pushed HEAD** (pass-agnostic — sequenced AFTER this fix-up push; re-invoking against an un-pushed fix re-flags the stale head, per the pass-2 desync) → on convergence, **Gate B** (§24.3.1 + (XXVI) two-gate; origin/<branch> post-push state). Then owner squash-merge (ADR-001 D9, step 10) → PMN-001 (k) chore (squash SHA + `status: active→resolved` / `drafted→recorded`) → **manual M-A7 35th `PR-NN` → PR-86 substitution at core.md L583 + L585** (out of Action scope) → cycle-close ledger + TASK-0049 successor handoff. *(F1 hardening, already exercised at PR-open: actual #86 = anticipated; no correction needed. Retain the live-`gh pr list` re-verify discipline for any future PR-number-bearing push.)*

## §3. Step-by-step execution record  *(APPEND-ONLY HISTORICAL — never back-refreshed; volatile state by pointer; the sub-phase/cluster records below ARE the §3 step-by-step content per §23.6.5)*

1. **Step-1 pre-flight** — 16/16 PASS, zero drift; entry anchor + 68-occurrence ledger re-confirmed on `main`. Stop-and-show (no branch). Ratified.
2. **Branch created** — `feat/task-0048-part-c2-operating-discipline-canonical-surfaces` from `b46e46e`.
3. **Cluster 1** (§8.2 + §8.3) — +46; stop-and-show; approved (+ 2 C1 touch-ups ruled at C2).
4. **Cluster 2** (§13 + §13.1 + §13.2 + 2 C1 touch-ups: §24.2(a)/Gate B §24.3.1 + reciprocal §13.1 cross-refs) — C2 delta +35; surfaced L546 attribution tension. Stop-and-show; approved; L546 ruled option-(a).
5. **Cluster 3** (§10 minimal host + §10.5 + §10.5→§3.2 cross-ref) — +24; §8.3→§10.5 forward-ref resolved. Stop-and-show; approved.
6. **Cluster 4** (§23.6.5 in-place at §23.6) — +23; last open forward-ref (§13.1/§13.2→§23.6.5) resolved → ZERO open forward-refs. Stop-and-show; approved.
7. **§4.6 sweep + migration** — DROP 41 / REWRITE 14 / STAY 13 + bare-ref + L546; 9 edit-files, +180/−61... (see §Cumulative-diff-stats gate-current for current figures). 2 Item-14 finds surfaced. Stop-and-show; approved.
8. **Pass B** (§4.6 Item-14 migrations STEP 0 + §4.7 standard surfaces) — Class A v2.45 ×4 + M-A7 35th (5-claim consistency; caught L583 snapshot header) + README rotation. Stop-and-show; approved (PR-NN approach approved).
9. **Pass C** (this pass) — PMN-019 + handoff + review-context + §5 battery → Gate A.

*(Per the §23.6.5 suppression clause: the +46/+35/+24/+23 and +180 figures above are the per-step records at the step they were taken; they are NOT back-refreshed to the current staged total — see §Cumulative-diff-stats gate-current for the authoritative current figure.)*

## §10. Cycle-close ledger  *(APPEND-ONLY HISTORICAL — populated at cycle close)*

Post-merge close-out (2026-06-04):
- **(a)** ✅ `linked_pr` squash-SHA substitution fired via PMN-001 (k) linked-pr-fix-up Action (PR-87 `32c6a07`): `linked_pr → PR-86 (squash SHA 0eb51f7)`; handoff `status: resolved`; PMN-019 `status: recorded`; review-context `status: recorded`.
- **(b)** ✅ M-A7 35th `PR-NN` → `PR-86` manually substituted at core.md L584 (snapshot header: "PR-86 / TASK-0048") + L586 (enumeration tail: "PR-83 + PR-86 = 35"), confirmed Architect-side post-merge maintenance per PMN-018 path-scoping (Action does not touch core.md body text).
- **(c)** ✅ 18 open Codex review conversations resolved.
- **(d)** TASK-0049 successor handoff (release polish + v3.0.0 tag) — in progress this close-reconciliation commit.

## Session log archive  *(§13.1 in-cycle records; current set per §13.2 in PR body)*

### Builder session — Claude Code (Sonnet) — 2026-06-03

- **Surface**: Builder.
- **Steps executed**: step-1 pre-flight; branch; clusters C1–C4; §4.6 sweep; Pass B (§4.6 Item-14 + §4.7); Pass C (PMN-019 + handoff + review-context + §5 battery).
- **Stop-and-show points reached (§8.3) — payload + owner ratification pairs** (per §13.1, each record carries the §8.3 payload AND the owner ratification that followed):
  - step-1 pre-flight: payload = 16/16 PASS pre-flight + ledger re-confirm → **owner ratified** (branch authorized).
  - C1 (§8.2+§8.3): payload = authored text + diff-stats (+46) → **approved** (+ 2 touch-ups ruled at C2).
  - C2 (§13/§13.1/§13.2 + touch-ups): payload = authored text + diff-stats (+35) + L546 tension surfaced → **approved** (L546 ruled option-(a)).
  - C3 (§10.5 + §3.2 cross-ref): payload = authored text + diff-stats (+24) → **approved**.
  - C4 (§23.6.5): payload = authored text + diff-stats (+23) → **approved**.
  - §4.6 sweep: payload = DROP/REWRITE/STAY ledger execution + diff-stats + 2 Item-14 finds → **approved** (finds ruled option-(a)).
  - Pass B (§4.6 Item-14 migrations + §4.7 standard surfaces): payload = Class A v2.45 + M-A7 35th + README rotation → **approved** (PR-NN approach approved).
  - Pass C / Gate A: payload = PMN-019 + handoff + review-context + §5 battery → **owner ratified** (Gate A cleared).
  - Codex pre-commit absorption: payload = 3 path-(a) fixes (F1/F2/F3) re-staged → **owner ratified** (Gate A re-cleared).
  - Commit + push + PR-open (step 9): payload = commit `9098bd2` + branch push + PR #86 open + PR-open live re-verification (actual #86 = anticipated PR-86) → **owner authorized**.
  - Codex post-PR absorption (passes 1–2): payload = post-PR P1 fix (§13.1 ratification records) + pass-2 stale-commit-desync absorption (P1 re-stated + P2 gate-current, both pre-resolved) → **owner ratified** (fix-up push granted; pushed `e7513a9`).
  - Codex post-PR pass-3 absorption: payload = P2 gate-current pointer class-sweep (L18 legend + L44 diff-stats; reviewed against the fixed HEAD `e7513a9`) → **owner ratified** (fix-up push granted; pushed `aa309fe`).
  - Codex post-PR pass-4 absorption: payload = P2 self-volatile-pinned-total de-pin (review-context resolution → by-pointer per §23.6.5; L44 de-pinned, ruling (a)) → **owner ratified** (fix-up push granted; pushed `7daa361`).
  - Codex post-PR pass-5 absorption: payload = P2 **canonical-law** fix — narrowed core.md §23.6.5 append-only by-pointer rule to current/live state (carving out historical snapshots), resolving internal contradiction with the suppression clause; Gate A re-cleared on the canonical change → **owner ratified** (fix-up push granted).
  - Codex post-PR pass-6: stale-head re-flag (relay-ordering desync, path-(β)) — re-reviewed unpushed `7daa361` and re-flagged pass-5's P2; pre-resolved by this fix-up; no content change. Recorded.
  - Codex post-PR pass-7 absorption: payload = P2 **canonical-law** fix — narrowed core.md §13.1 by-pointer rule to current/live state (parallel to §23.6.5 pass-5 fix; historical §8.3 payload snapshots carved out) → **owner ratified** (fix-up push granted; pushed `d8f9d9b`).
  - Codex post-PR pass-8 absorption: payload = P2 **canonical-law** fix — §8.2 item (4) pre-branch-timing: validate the *proposed* branch name at pre-branch pre-flight (working branch is still `main`), verify the actual working branch only once it exists → **owner ratified** (fix-up push granted; pushed `173484e`).
  - Codex post-PR pass-9 absorption: payload = 3 path-(a) **canonical-law** cross-surface-consistency fixes (P1 §8.2 predicate pre-flight-before-branch/repo-write; P1 §10.5 acknowledgment reconciled to "no additional artifact required" per github-reference §3.2 + usage-guide §3.9; P2 §8.3 trigger list adds `gh pr edit`); Gate A re-cleared → **owner ratified** (fix-up push granted; pushed `eb09645`).
  - Codex post-PR pass-10 absorption: payload = P2 **canonical-law** reverse-direction completion of the §10.5 reconciliation — usage-guide §3.9 (L118) + one-page bypass rule (L402) reworded to the canonical "optional" posture; bypass-ack class swept clean; Gate A re-cleared → **owner ratified** (fix-up push granted; pushed `0e77e00`).
  - Codex post-PR pass-11 absorption (expanded): payload = (P2) class-sweep propagating the §8.2 pre-flight-timing + §8.3 `gh pr edit` canonical fixes to the **receiving-surface summaries** (root AGENTS.md/CLAUDE.md + templates/AGENTS.md/CLAUDE.md, 8 lines) + a **five-topic receiving-surface consistency sweep** (§8.2/§8.3/§10.5/§13.x/§23.6.5 across AGENTS/CLAUDE/README/templates/.github — §10.5/§13/§23.6.5 confirmed already-current); (P2) **structural close of the self-volatile-pinned-total class** — de-pinned ALL current-claiming totals (handoff L42/L34/L44) → by-pointer (`git diff main --numstat`); historical snapshots (the §4.6-step +180/−61, the +128 authoring) retained as correct-by-design per the §23.6.5 carve-out; Gate A re-cleared → **owner ratified** (fix-up push granted; pushed `bbb466e`).
  - Codex post-PR pass-12 absorption: payload = 3 path-(a) **canonical-law** §8.2-timing fixes — the 2 propagation laggards the pass-11 sweep missed (usage-guide §8.2 quick-ref L404 + templates/handoff-template §8.2 pre-flight note L149) + the owner-ruled fold-in of core.md:161 (§8.2 principle intro) surfaced by the documented exhaustive sweep; §8.2-timing class now fully exhausted (principle + evidence-set + item-4 + predicate + all 6 mirror surfaces); Gate A re-cleared → **owner ratified** (fix-up push granted).
  - *Genuinely-pending (truthful `awaiting`, not a missing field)*: the binding Codex re-review of the **latest pushed HEAD** (pass-agnostic) → **Gate B** → owner squash-merge (step 10). These are the cycle's next steps, not completed §8.3 payloads.
- **Pre-flight reports (§8.2)**: step-1 = 16/16 PASS; per-cluster (j)-sweeps + (e.1) diff-stat re-derivations at each staged-tree mutation. (Per §13.1 enforcement-coupling, these pre-flight reports + the ratifications above are the durable §8.2/§8.3 record for this cycle.)
- **Hand-back point**: Gate B (post-PR convergence; §24.3.1 + (XXVI) two-gate).

*(Architect Phase-1 spec-authoring session is recorded in the PR-description current-set per §13.2; the Reviewer Codex pre-commit + post-PR passes are recorded verbatim in `docs/reviews/PR-86-codex-pre-commit.md` per §8.1.1.1/§8.1.1.2.)*
