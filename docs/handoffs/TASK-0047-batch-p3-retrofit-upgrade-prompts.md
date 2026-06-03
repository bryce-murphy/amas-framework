---
task_id: TASK-0047
title: Batch P3 retrofit + upgrade kickoff prompts (split cycle 2 of 2)
pr: PR-80
branch: feat/task-0047-batch-p3-retrofit-upgrade-prompts
linked_predecessor: TASK-0046 (PR #75 squash 32c4afa; fix-chore #77/#78; reconciliation #79 squash 83916ca)
linked_successor: TASK-0048 (anticipated; Part C.2 operating-discipline canonical surfaces)
linked_pr: PR-80 (squash SHA a166d1a)
framework_version_dogfooded: v2.43
production_target: v3.0.0
spec_source: .claude/session-handoffs/task-0047-spec.md
date_authored: 2026-06-02
status: resolved
---

# HANDOFF: TASK-0047 — Batch P3 retrofit + upgrade kickoff prompts (split cycle 2 of 2)

## Metadata

- **Cycle class**: Batch P3 substantive content-fill (prompt scaffold) — split cycle 2 of 2 (greenfield landed at TASK-0046 / PR-75). Executed across 7 sub-phases + an assembly pass and split into **PR-A** (this PR: `prompts/retrofit.md` + substrate + adopter-runnability remediation + co-shipped surfaces) and **PR-B** (follow-on: `prompts/upgrade.md` on the merged baseline). The original single-PR "retrofit + upgrade together" plan was superseded mid-cycle when the adopter-runnability smoke gate surfaced a multi-sub-phase remediation; upgrade was split to PR-B to land it on the proven baseline.
- **§0 salience**: HIGH (second prompt-class cycle; inherits the mode-neutral greenfield scaffold per TASK-0046 ledger (I); recursive self-application — kickoff prompts authored under AMAS cycle discipline; §23.6.5 behavioral empirical test #2).
- **Branch**: feat/task-0047-batch-p3-retrofit-upgrade-prompts
- **HEAD anchor**: main HEAD at TASK-0046 reconciliation state (`83916ca`).
- Linked PR: PR-80 (Builder fills with squash SHA post-merge per PMN-001 (k))
- **Spec source**: `.claude/session-handoffs/task-0047-spec.md` (gitignored per ADR-001 D15)
- **Cycle-protocol baseline**: standard per `core.md` §23.6.x + §24.5 + §24.6.
- **§23.6.5 behavioral taxonomy (empirical test #2; applied this cycle BEFORE Part C.2 canonicalization)**: this handoff's body surfaces are classified into two tiers. **Gate-current** (refreshed ONLY at gates — Gate A initial + each Gate A re-application after absorption + Gate B + Gate B re-applications; inter-gate staleness ACCEPTED by-design): §Last completed step, §Current state Summary, §Cumulative-diff-stats. **Append-only historical** (never back-refreshed; only appended; reference volatile state BY POINTER, e.g. "see §Cumulative-diff-stats", NOT by pinned value): §3 step-by-step execution record, §6 pre-commit absorption, §8 post-PR review state, §10 cycle-close ledger. The **sole canonical cycle-close marker** is action-filled frontmatter (`linked_pr` squash SHA + `status: resolved` + review-context `status: recorded`); NO body surface is a close marker.

## Objective

Fill `prompts/retrofit.md` (stub → active) with its canonical project-kickoff prompt, inheriting the mode-neutral greenfield Steps 0-6 scaffold (TASK-0046) with retrofit deltas (existing-project inventory + map-vs-create + reframe-pending flagging per `usage-guide.md` §2.8). Land the substrate that grounds correct kickoff prompts — VIII (project-brief-template "Kickoff follow-ups" body section) + X (usage-guide §2.1 trio) — and the **adopter-runnability remediation** the smoke gate surfaced across sub-phases 3-7: two-tier kickoff context pack + missing-template fallback; degraded operator-relay mode (§2.6.1) + v3.0 role-assignment heuristic (§2.6.2); the plan-vs-instantiate defaulting discipline (schema-valid defaults + non-blocking forthcoming markers) canonicalized at **ADR-009**; explicit Issue-0 open/close; version-of-record, lite→full, project-type-picker, no-bot-Reviewer-fallback, and GitHub-legacy-frontmatter clarifications. Co-shipped distributed surfaces: Class A v-bump v2.42 → v2.43 (README L9 ×2 + AGENTS L9 + CLAUDE L9) + README retrofit Prompts-row + `usage-guide.md` forthcoming-qualifier sweep (retrofit now live; upgrade → PR-B) + this handoff + the PR-80 Codex review-context (`docs/reviews/PR-80-codex-review.md`). **`prompts/upgrade.md` is NOT in PR-A — it stays a stub and ships as PR-B** on the merged baseline. The `core.md` §18.3 M-A7 33rd-instance increment is deferred to Architect-side post-merge maintenance with the verified PR number.

## Last completed step

*[GATE-CURRENT surface — refreshed at gates only.]*

PR-80 final handoff close-out — committed + pushed; **PR-80 draft OPEN** (not merged). Branch history: `9fd363a` (content + co-shipped) → `2b5ec16` (Codex P2: handoff-template PR-0 sentinel) → `66831ca` (Codex P2 re-raise: prompts/ADR PR-0 convergence) → `0cf4930` (Codex desktop red-team, 3 P1 + 3 P2 + repo-wide convergence sweep) → `78fcff4` (handoff reconciliation: 2 P1 self-description fixes + whole-handoff class-sweep) → this final §Exact-next-step close-out commit. Frontmatter is `pr: PR-80` / `status: active`. The handoff-focused re-verify returned NOT CONVERGED with 1 P1 — `§Exact next step` lagged one review pass (still pointed at a further re-verify); fixed here by rewriting it to the **stable terminal close-out sequence** (treating that re-verify as the final review input), which breaks the lag-by-one-pass property. This is the **last handoff edit**; the Builder claim-by-claim self-verification (this pass) replaces a further external re-verify — the Architect clears Gate A on it. The only non-handoff deferred item is the `core.md` §18.3 M-A7 33rd-instance increment (post-merge maintenance, verified PR-80). Cumulative state: see §Cumulative-diff-stats (gate-current).

## Current state

*[GATE-CURRENT surface — refreshed at gates only.]*

**Summary**: PR-A content complete, committed, and pushed; **PR-80 draft open** (not merged). The cycle ran 7 sub-phases + an assembly pass, then split into **PR-A / PR-B**: PR-A ships retrofit + substrate + remediation; `prompts/upgrade.md` ships PR-B. §Metadata, §Objective, and §1 all reflect this split (the original 3-sub-phase single-PR enumeration is superseded). Arc from `main` tip `83916ca`: **SP1** VIII (project-brief-template "Kickoff follow-ups" bold-bullet) + X (usage-guide §2.1 trio) + born-drafted handoff → **SP2** `prompts/retrofit.md` authored (stub→active, mode-neutral greenfield scaffold + retrofit deltas) → **SP3/3b** class-wide smoke remediation (kickoff context pack two-tier + missing-template fallback; degraded operator-relay §2.6.1; SF-2/6 forthcoming-citation rewording; explicit Issue-0 open/close) → **SP4** role-assignment heuristic (usage-guide §2.6.2 + compact inline) + SF-3 @codex + SF-10/11 → **SP5** plan-vs-instantiate remediation (project-brief `doc_mcp_mechanism` v3.0 default; handoff-template TASK-0000 bootstrap-case; PR-template §8.2/§8.3 non-blocking) → **SP6** ADR-009 created + ADR-008 in-place addendum reverted; doc-MCP example alignment; version-of-record clarification; lite→full; Step-0 partial-trio/forthcoming clarifications; inline-heuristic trim → **SP7** cross-Architect changes (ADR-009 scope clause; project-type `mixed` picker; no-bot-Reviewer fallback mini-template; GitHub-legacy-frontmatter note; refined version-of-record wording; upgrade-as-PR-B cross-refs) → **assembly** v2.43 dogfood bump ×3 surfaces + qualifier sweep + README retrofit row + gate-current reconciliation → **commit/push** (`9fd363a`) + draft PR-80 opened → **Codex GitHub-App passes 1-2** absorbed (PR-0-sentinel finding-class, commits `2b5ec16` + `66831ca`) → **Codex desktop red-team** (3 P1 + 3 P2) resolved at `0cf4930` (review-context artifact + gate-current refresh + lite/upgrade/qualifier-sweep completion + README filled-by + repo-wide convergence sweep) → **targeted re-verification** returned 2 P1 handoff-drift items (content clean) → **this handoff-reconciliation pass** (the 2 P1s + a whole-handoff class-sweep). `prompts/upgrade.md` untouched (stub); `core.md` untouched (M-A7 deferred). Branch committed + pushed; **PR-80 draft open, NOT merged.** Terminal sequence (the handoff-focused re-verify was the final review input): Gate A/B closure → resolve the 2 Codex threads → owner squash-merge → Action watch → cycle-close ledger + M-A7 increment → PR-B (upgrade). See §Exact next step.

**Files authored / modified by Builder** (PR-A; 13 files = 10 modified + 3 new):
1. MODIFIED `prompts/retrofit.md` — stub→active; mode-neutral greenfield scaffold + retrofit deltas (Step-2 inventory, Step-5 map-vs-create, reframe-pending) + the full SP3–SP7 remediation. 283 lines.
2. MODIFIED `prompts/greenfield.md` — SP3–SP7 remediation applied in parallel (context pack, role heuristic, SF-2/6/10/11, version-of-record, lite→full, Step-0 clarifications, picker/fallback/frontmatter reducers). 241 lines.
3. MODIFIED `usage-guide.md` — X §2.1 trio + two-tier context pack; §2.6.1 degraded operator-relay; §2.6.2 v3.0 role-assignment heuristic; forthcoming-qualifier sweep (L22 + §11.3 + one-page ref: retrofit now live, upgrade→PR-B).
4. MODIFIED `templates/project-brief-template.md` — VIII "Kickoff follow-ups" body-section bullet; `doc_mcp_mechanism` v3.0 default + example alignment.
5. MODIFIED `templates/handoff-template.md` — TASK-0000 bootstrap-case frontmatter note (PR-0 sentinel / none / ADR-000).
6. MODIFIED `templates/PULL_REQUEST_TEMPLATE.md` — §8.2/§8.3 non-blocking markers (N/A until Part C.2 / TASK-0048).
7. MODIFIED `README.md` — v2.43 dogfood bump (L9 ×2); retrofit Prompts-row → `PR-80 (TASK-0047)`.
8. MODIFIED `AGENTS.md` — v2.43 dogfood bump (L9).
9. MODIFIED `CLAUDE.md` — v2.43 dogfood bump (L9).
10. MODIFIED `templates/ISSUE_TEMPLATE/project-initiation.md` — qualifier-sweep: §Cross-references prompt-set entry (greenfield + retrofit live; `prompts/upgrade.md` forthcoming → PR-B).
11. NEW `docs/adr/ADR-009-kickoff-artifact-defaulting.md` — kickoff-artifact defaulting principle (amends ADR-008 D3) + scope clause. 73 lines.
12. NEW `docs/handoffs/TASK-0047-batch-p3-retrofit-upgrade-prompts.md` — this file; PMN-007 HEAD 12-field frontmatter + §23.6.5 taxonomy + Adj-11 `linked_pr` placeholder.
13. NEW `docs/reviews/PR-80-codex-review.md` — PR-80 review-context (§17.7 1-field `status: drafted`); records the two Codex GitHub-App branch passes + the Codex desktop red-team trail + resolutions. Born `drafted`; flips to `recorded` post-merge per the PMN-018 path-scoped Action on `docs/reviews/`.

*[NOT in PR-A — deferred to PR-B: `prompts/upgrade.md` (stays stub). Deferred to Architect-side post-merge maintenance: the `core.md` §18.3 M-A7 33rd-instance increment (verified PR-80).]*

**Cumulative-diff-stats** *(gate-current; PR-80 final close-out, staged-tree vs `origin/main` per `core.md` §23.6.1.1 (e.1))*: **13 files changed, +743 insertions / −64 deletions** (`git diff --staged --shortstat origin/main`). 10 modified + 3 new (`docs/adr/ADR-009-kickoff-artifact-defaulting.md`, this handoff, `docs/reviews/PR-80-codex-review.md`). (XVII) bidirectional sum-stability PASS — per-file numstat sums to files=13 / ins=743 / del=64, matching the shortstat on all three axes. `prompts/upgrade.md` (stub) and `core.md` (M-A7 deferred) are NOT in the set.

## Decisions made

Per spec adjudications + TASK-0046 cross-Architect ledger-(XIII) carry-forwards:

1. **Cycle class**: Batch P3 substantive content-fill, split cycle 2 of 2 (retrofit + upgrade), planned at SP1 as a sub-phased single PR (later split into PR-A/PR-B — see Decision 9). No new ADR *for the split itself* — split within a batch is per-cycle defect-surface-narrowing discretion (parallel to TASK-0046 Decision 1 + Batch P2 TASK-0043/0044 split); ADR-009 was created separately for the kickoff-artifact defaulting principle (Decision 9).
2. **VIII + X are prompt-correctness dependencies, not deferred carry-forwards**: per TASK-0046 ledger-(XIII)(b), the project-brief "Kickoff follow-ups" template gap (VIII) and usage-guide §2.1 trio under-spec (X) are pulled INTO this cycle as substrate that grounds correct retrofit/upgrade prompts (retrofit surfaces more follow-ups than greenfield). Landed first, at sub-phase 1, before any prompt authoring.
3. **Sub-phase 1 scope discipline**: substrate + born-drafted handoff ONLY; no prompt authoring, no commit, no PR-open this sub-phase. Stop-and-show + hand-back to Architect at sub-phase boundary.
4. **Scaffold inheritance**: retrofit + upgrade inherit the mode-neutral greenfield Steps 0-6 (TASK-0046 Decision 2 + ledger (I)) with mode-specific deltas; do NOT re-derive the scaffold.
5. **VIII heading string**: EXACTLY "Kickoff follow-ups" to match `usage-guide.md` §2.7 + greenfield Step 5 (no variant); inserted in the existing bold-bullet body-sequence syntax (the file enumerates body sections as bold-bullets that render as H2 in a filled brief), not as a standalone `##` heading.
6. **X scope bound**: only the §2.1 prompt enumeration + two-files→three-files trio change; §2.2 / §2.7 / §2.8 / §0 / one-page reference untouched.
7. **M-A7 33rd-instance + Class A v2.43 v-bump**: anticipated at a later sub-phase per spec; NOT edited at sub-phase 1 (M-A7 confirmed at 32 / v2.42 at pre-flight; do-not-edit-this-sub-phase per kickoff).
8. **§23.6.5 behavioral discipline (empirical test #2)**: applied BEHAVIORALLY (handoff gate-current/append-only taxonomy + by-pointer volatile-state references); NOT canonicalized as text (Part C.2 / TASK-0048 territory per anti-scope).
9. **PR-A/PR-B split + ADR-009 (post-SP1 decisions)**: the original sub-phased single-PR plan (Decision 1) was superseded mid-cycle (SP6/assembly) when the adopter-runnability smoke gate surfaced a multi-sub-phase remediation — retrofit + substrate + remediation ship as **PR-A**; `prompts/upgrade.md` ships as **PR-B** on the merged baseline. The plan-vs-instantiate defaulting discipline was canonicalized at **ADR-009** (amends ADR-008 D3) during SP6, superseding (via revert) the SP5 in-place ADR-008 addendum per the ADR-edit discipline.

*[Born-drafted scaffold: Decisions 1-8 reflect the settled spec at sub-phase 1; later-sub-phase scope decisions (the PR-A/PR-B split, ADR-009) are appended (Decision 9) per this note's gate-append convention.]*

## Assumptions

- Repo state at pre-flight (sub-phase 1): main HEAD `83916ca`, parity with origin/main, working tree clean (verified 8/8 at pre-flight).
- Version parity v2.42 across README L9 (×2) + AGENTS L9 + CLAUDE L9; zero v2.41/v2.43 residuals (verified).
- `prompts/retrofit.md` + `prompts/upgrade.md` both `status: stub`, `template_version: 3.0.0`, `filled_by: per ADR-003` (verified).
- PR-80 next available PR number (highest existing = PR-79 per `gh pr list`). Anticipated across surfaces; phantom-correct at PR-open if actual diverges (appears at later sub-phases in retrofit/upgrade `filled_by`, README Prompts rows, §18.3 M-A7 enumeration, this handoff `pr`/`linked_pr`, review-context filename).
- Codex Reviewer operational at desktop session per ADR-001 D11; owner invokes Codex pre-commit + `@codex review` post-PR at later sub-phases.
- linked-pr-fix-up Action operational at PR-80 squash-merge per PMN-001 (k) regex strict-match form; PR-80 is the first live run of the path-scoped Action (PR #77 scoping, guard-skipped at #76 per TASK-0046 ledger-(XI)(a)) — TASK-0046 ledger-(XIII)(c) flagged adding minimal script-level regression tests before this first live run (carry-in to verify at a later sub-phase).

## Risks

- **(R1) Scaffold-defect inheritance**: defects in the greenfield scaffold (TASK-0046) propagate to retrofit + upgrade. Mitigated by mode-neutral scaffold design + the VIII/X substrate landing first (sub-phase 1) so prompt citations resolve against materialized surfaces.
- **(R2) First live path-scoped Action run**: PR-80 squash-merge is the first non-guard-skipped run of the path-scoped linked-pr-fix-up Action (per TASK-0046 ledger-(XI)). Verify regression-test coverage + correct scoping (handoffs→resolved; prompts/templates untouched; reviews/PMNs→recorded) before merge.
- **(R3) PR-number anticipation**: PR-80 anticipated across multiple later-sub-phase surfaces; verify at PR-open against actual GitHub assignment; phantom-correct together if divergent.
- **(R4) Recursive self-application**: kickoff prompts orchestrating AMAS bootstrap are authored under AMAS cycle discipline; their canonical-section references must be currency-correct. Verify at the self-review reference-resolution sweep (later sub-phase).
- **(R5) Adopter-usability-under-first-contact** (TASK-0046 ledger-(XIII)(e)): make retrofit/upgrade prompts runnable by a first-time operator cold from README + canonical trio; adopt the adopter-mode smoke test as a standing prompt-cycle acceptance gate.

## Blocking questions

None at sub-phase 1. Pre-flight 8/8 clean. One surfaced divergence reported at stop-and-show (non-blocking): the project-brief-template body sequence is a **bold-bullet list** under `## Body section structure`, not standalone `##` headings — VIII inserted in matching bold-bullet form (Decision 5). Architect authorizes sub-phase 2 (author `prompts/retrofit.md`) at this hand-back.

## Validation run

*[Sub-phase 1 — read-only + post-edit verification.]*

- `git log -1 --oneline` → `83916ca`; `git status` → clean (pre-flight).
- Version-residual grep: README/AGENTS/CLAUDE L9 = v2.42; zero v2.41/v2.43 residuals.
- Prompt-stub `head -5`: retrofit.md + upgrade.md both `template_version: 3.0.0` / `status: stub` / `filled_by: per ADR-003`.
- Post-edit Read-verify VIII: "Kickoff follow-ups" bold-bullet present between "Initial scope" / "Cross-references" (project-brief-template L34).
- Post-edit Read-verify X: §2.1 names three prompts + full trio; fallback preserved (usage-guide L47).
- `linked_pr` regex pre-validation: `PR-80 (Builder fills with squash SHA post-merge per PMN-001 (k))` matches `^linked_pr: PR-(\d+) \(Builder fills with squash SHA post-merge per PMN-001 \(k\)\)[ \t]*$`.
- Full cycle validation (commit-time stats, self-review fixed-point, (XVII) sum-stability, branch-name regex CI) runs at later sub-phases.

## Exact next step

Gate A + Gate B closure (§24.3.1 XXVI two-gate; the handoff-focused re-verify is the final review input — no further external re-verify) → resolve the 2 open Codex PR threads (hygiene) → owner squash-merge → linked-pr-fix-up Action watch: first substitution-bearing run on `docs/handoffs/` (`linked_pr` → squash SHA; `status: active → resolved`) and `docs/reviews/` (`status: drafted → recorded`) → cycle-close ledger + deferred `core.md` §18.3 M-A7 33rd-instance post-merge increment (verified PR-80) + log the comprehensive red-team and the three upstream disciplines (class-sweep-not-instance-fix; gate-current-refresh-each-transition; claim-artifact-parity) as monitoring-register candidates → `prompts/upgrade.md` in PR-B.

## §1. Cycle scope deliverables enumeration

Actual landed scope (the cycle ran 7 sub-phases + an assembly pass, then split into PR-A / PR-B; the original 3-sub-phase single-PR enumeration was superseded — see §Metadata cycle-class + §Decisions Decision 9):

**PR-A (this PR — LANDED; 13 files = 10 modified + 3 new):**
- MODIFIED `prompts/retrofit.md` (stub → active; mode-neutral greenfield scaffold + retrofit deltas + the SP3–SP7 remediation).
- MODIFIED `prompts/greenfield.md` (parallel SP3–SP7 remediation).
- MODIFIED `usage-guide.md` (X §2.1 trio + §2.6.1 operator-relay + §2.6.2 role heuristic + lite/upgrade/appendix qualifier sweep).
- MODIFIED `templates/project-brief-template.md` (VIII "Kickoff follow-ups" + `doc_mcp_mechanism` v3.0 default).
- MODIFIED `templates/handoff-template.md` (TASK-0000 bootstrap-case frontmatter note).
- MODIFIED `templates/PULL_REQUEST_TEMPLATE.md` (§8.2/§8.3 non-blocking markers).
- MODIFIED `templates/ISSUE_TEMPLATE/project-initiation.md` (prompt-set qualifier sweep).
- MODIFIED `README.md` + `AGENTS.md` + `CLAUDE.md` (Class A v-bump v2.42 → v2.43; README retrofit Prompts-row).
- NEW `docs/adr/ADR-009-kickoff-artifact-defaulting.md` + `docs/handoffs/TASK-0047-batch-p3-retrofit-upgrade-prompts.md` (this file) + `docs/reviews/PR-80-codex-review.md`.

**NOT in PR-A:**
- `prompts/upgrade.md` — stays a stub; ships as **PR-B** on the merged baseline.
- `core.md` §18.3 M-A7 33rd-instance increment — deferred to Architect-side post-merge maintenance (verified PR-80).

*[Authoritative file list with descriptions: §Current state Files-list (13). Cumulative-diff-stats: §Cumulative-diff-stats.]*

## §2. Cycle gates

Per `core.md` §24.3.1 (XXVI) two-gate Gate A + Gate B:

- **Sub-phase hand-backs** (this cycle's split discipline): stop-and-show at each sub-phase boundary. The cycle actually ran 7 sub-phases + an assembly pass (substrate → retrofit → SP3-SP7 remediation → assembly), then split `prompts/upgrade.md` to PR-B (not a sub-phase here).
- **Gate A** at the assembly/commit pass: cumulative-diff-stats + (XVII) bidirectional sum-stability + spec verification baseline + (XIV) sweep + (XXIV.a-n) catalog at staged-tree state per `core.md` §23.6.1.1 (e.1). §23.6.5 behavioral: refresh gate-current body surfaces here.
- **Gate B** at post-PR-open: cycle-close completeness; gate-current surfaces refreshed; append-only surfaces appended (never back-edited).
- **§24.6 Stop-Iteration framework** at reach 4+ canonical boundary: HIGH §0 salience.

## §3. Step-by-step execution record

*[APPEND-ONLY HISTORICAL surface — never back-refreshed; references volatile state BY POINTER.]*

- Sub-phase 1 pre-flight: 8/8 verification items run read-only against main HEAD `83916ca` (clean tree; v2.42 parity; both prompt stubs; greenfield scaffold Steps 0-6 + Step-4 project-profile elicitation; §2.1/§2.7/§2.8 exact text captured; project-brief-template body-sequence = bold-bullets ending Initial scope → Cross-references; M-A7 = 32 / v2.16–v2.42; PR-80 anticipated). One non-blocking divergence surfaced: body sequence is bold-bullets not `##` headings.
- Sub-phase 1 branch: `feat/task-0047-batch-p3-retrofit-upgrade-prompts` created from main HEAD `83916ca`; ADR-005 Option B + `github-reference.md` §2.2 regex compliant; working tree clean post-checkout.
- Sub-phase 1 VIII: `templates/project-brief-template.md` — new "Kickoff follow-ups" bold-bullet inserted between "Initial scope" and "Cross-references"; post-edit Read-verified.
- Sub-phase 1 X: `usage-guide.md` §2.1 — three-prompt enumeration + full-trio reference; fallback preserved; post-edit Read-verified.
- Sub-phase 1 handoff: this file born drafted with 12-field frontmatter + §23.6.5 taxonomy labels + Adj-11 regex placeholder.
- *[Sub-phase 2+ execution records append here.]*

## §4. Substantive-content evidence per deliverable

*[Populated as deliverables land across sub-phases.]*

- Sub-phase 1: VIII = project-brief-template "Kickoff follow-ups" bold-bullet (resolves TASK-0046 ledger-(VIII)). X = usage-guide §2.1 three-prompt + full-trio alignment (resolves TASK-0046 ledger-(X)). Handoff = 12-field PMN-007 HEAD frontmatter + Adj-11 regex placeholder + §23.6.5 taxonomy.
- *[retrofit.md / upgrade.md / co-shipped-surface evidence appends at sub-phases 2-3.]*

## §5. Self-review record (§23.6.2 iteration log)

*[GATE-CURRENT for the convergence result; iteration log itself stable post-fixed-point. Populated at sub-phase 2-3 prompt authoring + the whole-cycle Gate A self-review.]*

## §6. Pre-commit absorption (Codex desktop output absorption)

*[APPEND-ONLY HISTORICAL surface — populated post Codex pre-commit pass (sub-phase 3); never back-refreshed. Volatile state by pointer (see §Cumulative-diff-stats).]*

## §7. Commit + push + PR-open record

*[Populated at sub-phase 3. Commit SHA filled post-merge with squash SHA per PMN-001 (k) Action; no pre-merge amend SHA pinned. PR-80 number verified vs anticipated at PR-open; phantom-correct if divergent. Status `drafted → active` token-swap at the pre-merge path-(α') gate.]*

## §8. Post-PR Codex review state

*[APPEND-ONLY HISTORICAL surface — populated post each Codex post-PR pass; never back-refreshed. Volatile state by pointer.]*

## §9. Sign-off (§24.3.1 five-point check; Architect populates)

*[Cleared at cycle-close hand-back per `core.md` §24.3.1 (XXVI) two-gate five-point check.]*

## §10. Cycle-close ledger

*[APPEND-ONLY HISTORICAL surface — observations appended at cycle close; references volatile state BY POINTER.]*

- **(I)** Sub-phase 1 landed the VIII + X substrate as prompt-correctness dependencies (TASK-0046 ledger-(XIII)(b)) BEFORE any prompt authoring — VIII closes the project-brief-template "Kickoff follow-ups" root gap (TASK-0046 ledger-(VIII)); X closes the usage-guide §2.1 trio under-spec (TASK-0046 ledger-(X)).
- **(II)** Carry-in monitors for later sub-phases: TASK-0046 ledger-(V) §11.3 + L24 upgrade-forthcoming qualifier currentness (adjudicate whether the L22/L370-style TASK-number update applies); ledger-(XIII)(c) linked-pr-fix-up regression tests before PR-80 first live run; ledger-(XIII)(e) adopter-mode smoke test as standing acceptance gate.
- **(III)** Convergence trail — the multi-surface review pipeline drove **monotonic 6 → 2 → 1 → 0**: iterative self-review to fixed-point → two Codex GitHub-App branch passes (2 P2s, the PR-0-sentinel finding-class; `2b5ec16` + `66831ca`) → comprehensive Codex desktop red-team (3 P1 + 3 P2; `0cf4930`) + repo-wide convergence completion-sweep → two handoff re-verify rounds (`78fcff4` reconciliation + `1fb52a9` §Exact-next-step close-out). Empirical positive for the §24.5 multi-surface pipeline at a prompt-class cycle; the residual defects were documentation / self-description class, not artifact content.
- **(IV)** Recursive self-instantiation (empirical confirmation per §18.3 (d)): (a) the §8.1.1.2 phantom-claim discipline caught a **phantom in this cycle's own handoff** — a claimed-but-missing PR-A review-context (red-team P1-a) — the discipline self-instantiating at the artifact that documents it; (b) the gate-current-refresh discipline's own handoff repeatedly exhibited the very state-drift it documents (file-inventory count, §1 enumeration, §Exact-next-step lag), needing three reconciliation passes — evidence that gate-current surfaces need refresh at *every* state transition, not just named gates.
- **(V)** Central finding — the **plan-vs-instantiate adopter-runnability arc**: the greenfield/retrofit smoke gate (Mode-1 naive-comprehension + push-through) surfaced that v3.0 kickoff artifacts depended on not-yet-materialized canonical surfaces (`core.md §3.1`, Part C.2, v3.2 appendices) in ways that read as hard walls; resolved by the defaulting discipline (schema-valid defaults + non-blocking forthcoming markers) **canonicalized at ADR-009** (amends ADR-008 D3). The cycle's durable contribution beyond the retrofit prompt itself.
- **(VI)** §18.3 M-A7 **33rd-instance** increment landed at this close-reconciliation chore (count 32 → 33; span v2.16 → v2.43; `+ PR-80` appended; preamble + steady-state bumped to v2.43 / PR-80 / TASK-0047). PR-81 (chore-fix-up) excluded per the substantive-cycle-only inclusion criterion.
- **(VII)** First **substitution-bearing** live run of the path-scoped linked-pr-fix-up Action (PR-81): substituted the squash SHA into the handoff `linked_pr` (`PR-80 (squash SHA a166d1a)`) + flipped handoff `status: active → resolved` and review-context `status: drafted → recorded`, while leaving `prompts/` + `templates/` **untouched** — first clean live confirmation that the PMN-018 path-scoping does the right thing *with* real substitution (prior runs were guard-skipped / no-op). Resolves the (II) first-live-run concern; the PMN-018 residual (no script-level regression tests) remains a deferred enhancement.
- **(VIII)** **Monitoring-register candidates** (logged per the ADR-006 evidence-bar — observe-then-canonicalize; v3.0 is minimum-viable, these canonicalize post-v3.0). **Register-placement is ambiguous this cycle**: monitoring items conventionally live in PMN "Monitoring items" sections (PMN-006 §9.2 pattern), but this cycle authors no PMN — recorded here pending the Architect's placement decision (author a PMN, or carry to the next PMN / TASK-0048). Candidates:
  - **Comprehensive pre-merge red-team** — a full adversarial review pass triggered on large / multi-surface / sweep-deliverable cycles. First evidence = this cycle (caught 5 of 6 findings preventable pre-merge). Promote after ~3 such cycles.
  - **Class-sweep-not-instance-fix** — when a reviewer flags one instance of a defect class, sweep the whole class across all surfaces rather than fixing only the flagged instance. Evidence: the PR-0-sentinel instance-fix → sibling re-raise → convergence sweep closed it.
  - **Gate-current-refresh-at-each-state-transition** — refresh gate-current handoff surfaces at every commit / push / merge transition, not only at named gates. Evidence: the three handoff-drift reconciliation passes ((IV)(b)).
  - **Claim-artifact-parity** — every "co-shipped / created" claim in a durable record must correspond to an artifact actually in the commit. Evidence: the phantom review-context ((IV)(a)).
- **(IX)** **§10 scope / PR-B**: this records the **PR-A** cycle-close; **TASK-0047 is not fully closed** — `prompts/upgrade.md` ships as **PR-B** (its own kickoff on the merged baseline). This handoff is PR-A's resolved record (frontmatter `status: resolved`, Action-set at PR-80 merge); PR-B proceeds on its own handoff. Carry-in (II) dispositions: the adopter-mode smoke gate was exercised + validated as a standing prompt-cycle acceptance gate; the §11.3 / §0 / §8.5 upgrade + appendix qualifier currentness was swept in PR-A.

## §11. Session log archive

*[Architect session record(s) + Builder session record(s) per AMAS v2.14.1 §13.1 substrate (`forthcoming at Part C+` in v3 `core.md`). Most recent session in PR body; prior sessions migrated here at cycle close.]*
