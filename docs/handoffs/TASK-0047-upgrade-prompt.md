---
task_id: TASK-0047
title: Batch P3 upgrade kickoff prompt (PR-B; split cycle 2 of 2, second PR)
pr: PR-83
branch: feat/task-0047-upgrade-prompt
linked_predecessor: TASK-0047 PR-A (PR #80 squash a166d1a; chore-fix-up #81 squash 8c7317e; close-reconciliation #82 squash 5506c92)
linked_successor: TASK-0048 (anticipated; Part C.2 operating-discipline canonical surfaces)
linked_pr: PR-83 (Builder fills with squash SHA post-merge per PMN-001 (k))
framework_version_dogfooded: v2.44
production_target: v3.0.0
spec_source: .claude/session-handoffs/task-0047-spec.md
date_authored: 2026-06-03
status: drafted
---

# HANDOFF: TASK-0047 PR-B — Batch P3 upgrade kickoff prompt

## Metadata

- **Cycle class**: Batch P3 substantive content-fill (prompt scaffold) — **PR-B**, the second PR of TASK-0047's split cycle 2 of 2 (PR-A landed retrofit + the adopter-runnability remediation at PR-80; this PR fills the last prompt, `prompts/upgrade.md`, on the proven merged baseline).
- **§0 salience**: MEDIUM (third prompt-class cycle; inherits the proven retrofit scaffold; upgrade-specific deltas only; far below PR-A's remediation load).
- **Branch**: feat/task-0047-upgrade-prompt
- **HEAD anchor**: main HEAD at PR-A close-reconciliation state (`5506c92`).
- Linked PR: PR-83 (Builder fills with squash SHA post-merge per PMN-001 (k))
- **Spec source**: `.claude/session-handoffs/task-0047-spec.md` (gitignored per ADR-001 D15); this PR-B kickoff is the operative spec.
- **§23.6.5 behavioral taxonomy**: gate-current (§Last completed step, §Current state Summary, §Cumulative-diff-stats) refreshed at gates; append-only-historical (§3 / §6 / §8 / §10) appended, volatile state by pointer. Sole close marker = action-filled frontmatter.

## Objective

Fill `prompts/upgrade.md` (stub → active) with its canonical project-kickoff prompt, reusing the **proven** greenfield/retrofit scaffold (context pack + missing-template fallback, Step-1 environment, §2.6.2 role-assignment + fallbacks, version-of-record, v3.0 defaults, Kickoff-follow-ups, cross-refs) and applying the two **upgrade-specific deltas**: (1) **current-version-proof** — prove the project's current adopted AMAS version from its trio `framework_version` before migrating; (2) **version-delta migration** — guide the operator across the current→target delta with ADR-009 plan-vs-instantiate (the canonical migration mechanism is forthcoming; `core.md §18.4` gives only the delta-**severity** signal, not the mechanism). Ratified **upgrade-vs-bootstrap reframe**: an upgrade is a project-scope-shift **amendment**, not a fresh bootstrap — Step 5 re-validates/amends the *existing* artifact set, Step 6 records an **ADR** + resumes (no Issue-0 / TASK-0000). Co-shipped: **upgrade-now-live qualifier sweep** (greenfield + retrofit preambles/cross-refs, usage-guide §0/§2.2/§11.3/one-page, README upgrade Prompts-row → `PR-83 (TASK-0047)`) + **Class A dogfood v-bump v2.43 → v2.44** (README L9 ×2 + AGENTS L9 + CLAUDE L9) + this handoff. `core.md §18.3 M-A7 34th-instance` increment **deferred to PR-B close-reconciliation** (with verified PR-83 + v2.44).

## Last completed step

*[GATE-CURRENT surface — refreshed at gates only.]*

PR-B Codex absorption (path-a). Substantive content committed at `95913fb` + pushed to `origin/feat/task-0047-upgrade-prompt`; **draft PR-83 open** (not merged). Codex's proportionate post-push review returned **2 P2** (no P1; `prompts/upgrade.md` itself clean): **F1** usage-guide §2 bootstrap-vs-upgrade leak (class-swept §2.1 + §2.3) + **F2** this gate-current staleness — both absorbed in a **trailing remediation commit** that sits on top of `95913fb` (do not treat `95913fb` as the branch tip). `status: drafted` holds until ready-for-review; `linked_pr` stays the canonical PMN-001(k) placeholder (Action substitutes the squash SHA at merge). Cumulative state: see §Cumulative-diff-stats (gate-current).

## Current state

*[GATE-CURRENT surface — refreshed at gates only.]*

**Summary**: PR-B content complete, committed (`95913fb`), and pushed; **draft PR-83 open** (not merged). `prompts/upgrade.md` filled on the proven baseline (PR-A merged: scaffold + ADR-009 + §2.6.2 + defaults all live on `main`). Adjudicated refinements applied: **R1** (Step 0/2 target-vs-current-trio clarity note), **R2** (Step 5 delta-source — no phantom changelog; v3.0 proxies [README positioning + ADR/PMN history + §18.4 severity] + canonical changelog/migration-notes marked forthcoming); **R3** already satisfied (Step 4 reads re-validate); **R4** already clean (retrofit cross-ref). Co-shipped: upgrade-now-live sweep (all surfaces) + dogfood v-bump v2.43 → v2.44. `core.md` untouched (M-A7 34th deferred to close-reconciliation). Codex post-push review (2 P2, path-a) absorbed in a trailing remediation commit: **F1** usage-guide §2 bootstrap-vs-upgrade class-sweep (§2.1 + §2.3) + **F2** this gate-current refresh.

**Files modified/authored by Builder** (PR-B):
1. MODIFIED `prompts/upgrade.md` — stub → active; proven scaffold + current-version-proof (Step 2) + version-delta migration (Step 5, ADR-009 forthcoming markers) + upgrade-vs-bootstrap reframe (Steps 5/6).
2. MODIFIED `prompts/greenfield.md` + `prompts/retrofit.md` — upgrade-now-live sweep (preamble + cross-ref markers dropped).
3. MODIFIED `usage-guide.md` — upgrade-now-live sweep (§0 + §2.2 + §11.3 + one-page).
4. MODIFIED `README.md` — upgrade Prompts-row → `PR-83 (TASK-0047)`; dogfood v-bump v2.43 → v2.44 (L9 ×2).
5. MODIFIED `AGENTS.md` + `CLAUDE.md` — dogfood v-bump v2.43 → v2.44 (L9).
6. NEW `docs/handoffs/TASK-0047-upgrade-prompt.md` — this file.

**Cumulative-diff-stats** *(gate-current; staged-tree vs `origin/main` per `core.md` §23.6.1.1 (e.1))*: **8 files changed, +380 insertions / −20 deletions**. (XVII) PASS — per-file numstat sums files=8 / ins=380 / del=20, matching the shortstat. `core.md` NOT in the set (M-A7 34th deferred to close-reconciliation).

## Decisions made

1. **Reuse the proven scaffold**: PR-B inherits the merged greenfield/retrofit scaffold verbatim where shared; do not re-derive (TASK-0046/PR-A precedent).
2. **Upgrade-vs-bootstrap reframe (Architect-ratified)**: an AMAS version upgrade is a project-scope-shift amendment per `templates/project-brief-template.md`, not a bootstrap — no Issue-0 / TASK-0000 / fresh bootstrap-set; Step 5 re-validates/amends the existing set, Step 6 records an ADR + resumes. `lite→full` omitted (bootstrap-specific).
3. **Two upgrade deltas**: current-version-proof (Step 2); version-delta migration (Step 5).
4. **ADR-009 plan-vs-instantiate for the forthcoming migration mechanism + changelog/migration-notes surface**: non-blocking forthcoming markers + v3.0-available proxies; no bare-forthcoming in a required position; do not fabricate a migration step from a deferred spec.
5. **Dogfood v-bump v2.43 → v2.44 (per-substantive-PR cadence)**: consistent with the M-A7 per-PR enumeration (v2.41/PR-73 → v2.42/PR-75 → v2.43/PR-80 → v2.44/PR-83). **Surfaced for Architect §18.4 confirmation** (revert to v2.43 if per-TASK intended). M-A7 34th-instance §18.3 increment deferred to close-reconciliation.

## Assumptions

- Fresh `main` = `5506c92` (PR-A close-reconciliation #82 merged); parity with origin/main.
- PR-83 next available PR number (highest existing = #82). Anticipated across surfaces (upgrade.md `filled_by`, README row, this handoff `pr`/`linked_pr`); phantom-correct at PR-open if divergent.
- linked-pr-fix-up Action operational + path-scoped (PMN-018) — confirmed clean at PR-A's PR-81 first substitution-bearing run.

## Risks

- **(R1) Upgrade-vs-bootstrap reframe** is a design judgment (Architect-ratified); the smoke confirmed it reads coherently. If a future adopter expects a bootstrap-shaped upgrade, the intro + Steps 5/6 explicitly state the amendment framing.
- **(R2) Forthcoming migration mechanism + changelog**: the upgrade leans on v3.0 proxies until the canonical migration discipline + changelog/migration-notes surface materialize (post-v3.0). Carried forward (see §10).
- **(R3) Dogfood-bump determination** (v2.44 per-substantive-PR): surfaced for §18.4 confirmation.

## Exact next step

Targeted Codex re-pass on the two fixed surfaces only (usage-guide §2 reframe completeness + handoff gate-current currency — a focused confirm, not a full re-review), with Gate A in parallel. On clean: Gate A + Gate B closure → resolve any Codex threads → owner squash-merge → chore-fix-up watch → PR-B close-reconciliation (M-A7 34th-instance + PR-83 + **final TASK-0047 cycle-close** + formally register the monitoring candidates at TASK-0048). Completes Batch P3 + TASK-0047 → Part C.2 (TASK-0048) → v3.0.0 (TASK-0049).

## §1. Cycle scope deliverables enumeration

PR-B: MODIFIED `prompts/upgrade.md` (stub→active) + upgrade-now-live sweep (`prompts/greenfield.md`, `prompts/retrofit.md`, `usage-guide.md`, `README.md`) + dogfood v-bump v2.43→v2.44 (`README.md`, `AGENTS.md`, `CLAUDE.md`) + NEW this handoff. NOT in PR-B: `core.md §18.3` M-A7 34th (close-reconciliation); a PR-B review-context (authored at Gate A if the review warrants one).

## §2. Cycle gates

Gate A (review-context, at draft-PR Codex review) + Gate B (post-PR-open completeness) per `core.md` §24.3.1 (XXVI). PR-B is below the comprehensive-red-team trigger — a proportionate post-push Codex pass is expected.

## §3. Step-by-step execution record

*[APPEND-ONLY HISTORICAL — references volatile state BY POINTER.]*

- Branch `feat/task-0047-upgrade-prompt` off `5506c92`; verified version cadence + handoff convention + upgrade.md stub at pre-flight.
- Authored `prompts/upgrade.md` from the proven retrofit scaffold + 2 upgrade deltas + reframe.
- Mode-1 push-through smoke: no hard walls; 2 stall points (target/current-trio clarity; delta-source/changelog) → adjudicated → R1 + R2.
- Applied R1/R2 + upgrade-now-live sweep + dogfood v-bump v2.43→v2.44; this handoff born drafted.
- *[Commit/push/PR-open append here.]*

## §4. Substantive-content evidence per deliverable

*[Populated at gates.]* upgrade.md: 7-step scaffold parallel to retrofit + current-version-proof (Step 2) + version-delta migration (Step 5) + ADR + resume (Step 6); ADR-009 forthcoming markers for the migration mechanism + changelog surface.

## §5. Self-review record (§23.6.2)

*[GATE-CURRENT for the convergence result.]* Fixed-point at authoring; parallel-form with retrofit on the shared scaffold; citations resolve (§18.4, §11.3, §2.6.2, §2.8, §8, §9, §2.1).

## §6. Pre-commit / review absorption

*[APPEND-ONLY HISTORICAL — populated post Codex review; volatile state by pointer.]*

## §7. Commit + push + PR-open record

Substantive content committed at `95913fb`; pushed to `origin/feat/task-0047-upgrade-prompt`; **draft PR-83 opened** against `main` (number verified = anticipated PR-83; no reconciliation needed). The F1 §2 sweep + F2 this gate-current refresh are a trailing path-a remediation commit on top of `95913fb` — the branch tip advances past it, so no transient HEAD SHA is pinned here. Squash SHA filled post-merge per PMN-001 (k) Action; `status: drafted → active` token-swap at the pre-merge ready gate.

## §8. Post-PR Codex review state

*[APPEND-ONLY HISTORICAL — populated post each Codex pass; volatile state by pointer.]*

## §9. Sign-off (§24.3.1 five-point check; Architect populates)

*[Cleared at cycle-close hand-back.]*

## §10. Cycle-close ledger

*[APPEND-ONLY HISTORICAL — observations appended at cycle close; volatile state BY POINTER.]*

- **(I)** **Monitoring-register candidates carried in from PR-A §10 (VIII)** — flagged for **formal registration at the next PMN-authoring cycle (TASK-0048)**: the **comprehensive pre-merge red-team** (triggered on large/multi-surface/sweep cycles) + the three upstream drift-prevention disciplines (**class-sweep-not-instance-fix**; **gate-current-refresh-at-each-state-transition**; **claim-artifact-parity**). PR-B is below the red-team trigger, so it neither re-tests nor registers them; they ride to TASK-0048.
- **(II)** **Stall-2 carry-forward**: a canonical **changelog / migration-notes surface** is forthcoming — a companion to the forthcoming canonical migration mechanism (post-v3.0). upgrade.md Step 5 leans on the v3.0 proxies (README positioning + ADR/PMN history + §18.4 severity) until both materialize.
- **(III)** **Dogfood v-bump determination** (v2.43 → v2.44, per-substantive-PR) surfaced for §18.4 Architect confirmation; M-A7 34th-instance §18.3 increment deferred to PR-B close-reconciliation.
- *[PR-B cycle-close observations append here.]*

## §11. Session log archive

*[Architect + Builder session records per AMAS v2.14.1 §13.1 substrate; most recent in PR body, prior migrated here at close.]*
