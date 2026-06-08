---
task_id: TASK-0052
title: three-endpoint canonical reconciliation (github-reference.md §6.3 fix + 3.0.2 -> 3.0.3 patch)
pr: PR-98
branch: fix/task-0052-three-endpoint-canonical-reconciliation
linked_predecessor: TASK-0051 (PR-95 squash b72bf45 feat(actions): materialize surface-version-sync-check (TASK-0051))
linked_successor: TBD
linked_pr: PR-98 (Builder fills with squash SHA post-merge per PMN-001 (k))
framework_version_dogfooded: AMAS v3.0.3
production_target: AMAS v3.1
spec_source: .claude/session-handoffs/TASK-0052-directive.md
date_authored: 2026-06-08
status: drafted
---

# HANDOFF: TASK-0052 — three-endpoint canonical reconciliation

## Metadata

- Task ID: TASK-0052 (matches PR-98 anticipated)
- Linked Issue: none
- Linked PR: PR-98 — URL TBD at PR-open (substituted post-merge per PMN-001 (k))
- Linked ADR(s): ADR-008 (D6 release-track bump posture — this cycle bumps patch v3.0.2 -> v3.0.3 intra-v3.1-track)
- Linked Feature Brief: none (defect-fix patch cycle)
- Linked review-context file: docs/reviews/PR-98-codex-pre-commit.md
- Owner role: Builder (Claude Code, Windows)
- Previous role: Architect (handoff direction Architect -> Builder)
- Timestamp (UTC): 2026-06-08
- Last synced commit SHA: d596cd3 (main HEAD at pre-flight; PR-97 TASK-0051 close-reconciliation)
- Branch: fix/task-0052-three-endpoint-canonical-reconciliation
- Status: drafted
- Direction: Architect -> Builder (universal handoff schema, core.md §14.1)
- Framework version: AMAS v3.0.3 (patch bump; intra-v3.1-track per ADR-008 D6)
- Recursive-self-instantiation salience: LOW (this cycle patches the description of review polling; the Builder-discipline polling clauses in core.md §8.1.1.1 and usage-guide.md §7.4 are unchanged; the patch governs what future cycles will read about §6.3, not the current cycle's own polling behavior)

## Objective

Patch `github-reference.md §6.3` from two-endpoint to three-endpoint review-polling operationalization, aligning it with the canonical three-endpoint mandate at `core.md §8.1.1.1` and `usage-guide.md §7.4`. De-churn the `§7.1` example version pins to placeholders. Bump framework version 3.0.2 -> 3.0.3. Append a one-line adopter migration note to `README.md ## Status`. Author cycle artifacts (this handoff + pre-commit review context).

Deliverable classes (D1-D5):
- D1: `github-reference.md §6.3` full rewrite — three-endpoint preamble, three GET paths, three endpoint-specific step-4 freshness rows, three-endpoint tie-break clause, legacy-label clause inline at the §8.1.1.1 citation.
- D2: `github-reference.md §7.1` example pins -> placeholders (`framework_version: <version>`, `canonical_version: <version>` x2).
- D3: Targeted version bump 3.0.2 -> 3.0.3 at 11 sites across 7 files (trio frontmatter x3, in-dev markers x3, surfaces.yml framework_version + canonical_version x4 = x5).
- D4: One-line adopter migration note appended to `README.md ## Status` (no new section).
- D5: This handoff + `docs/reviews/PR-98-codex-pre-commit.md`.

## Last completed step

All seven files modified + two new cycle artifacts authored. Branch `fix/task-0052-three-endpoint-canonical-reconciliation` created from `main` at `d596cd3`. **Next: Gate A pre-commit stop-and-show — presenting staged-tree diff to owner for ratification before commit. §23.6.2 self-review to fixed-point complete (see §5).**

## Current state

**Summary**: Branch at `fix/task-0052-three-endpoint-canonical-reconciliation`. Seven files modified (github-reference.md, core.md, usage-guide.md, README.md, AGENTS.md, CLAUDE.md, .amas/surfaces.yml), two new files authored (docs/handoffs/TASK-0052-three-endpoint-canonical-reconciliation.md, docs/reviews/PR-98-codex-pre-commit.md). All deliverables complete; pending Gate A owner ratification before staging + commit.

**Files authored / modified by Builder**:
1. MODIFIED `github-reference.md` — D1 §6.3 full rewrite (two- -> three-endpoint; step-4 freshness rows; legacy-label clause) + D2 §7.1 example pins -> placeholders + D3 frontmatter bump 3.0.2 -> 3.0.3
2. MODIFIED `core.md` — D3 frontmatter bump only (§18.3 untouched)
3. MODIFIED `usage-guide.md` — D3 frontmatter bump only
4. MODIFIED `README.md` — D3 line-9 in-dev marker bump + D4 adopter migration note
5. MODIFIED `AGENTS.md` — D3 line-9 in-dev marker bump
6. MODIFIED `CLAUDE.md` — D3 line-9 in-dev marker bump
7. MODIFIED `.amas/surfaces.yml` — D3 framework_version + canonical_version x4 bump
8. NEW `docs/handoffs/TASK-0052-three-endpoint-canonical-reconciliation.md` — D5 this handoff
9. NEW `docs/reviews/PR-98-codex-pre-commit.md` — D5 pre-commit review context

**Cumulative-diff-stats** (per `core.md` §23.6.1.1 (e.1) staged-tree convention):
- Derived at Gate A pre-commit stop-and-show from `git diff --staged --shortstat origin/main` + per-file numstat. (Populated at Gate A after staging.)

## Decisions made

Per Phase-1 Gate-A report and Phase-2 Architect adjudication:

- **FIX (D1):** `github-reference.md §6.3` — section title, "both endpoints" phrase, "either...or" binary preamble, two-path GET block, and step-4 validation logic all two-endpoint; rewritten to three-endpoint in full.
- **HOLD (legacy label):** `dual-signal` label at `core.md §8.1.1` preamble + `core.md §8.1.1.1` title + `github-reference.md §6.3` back-reference + `github-reference.md §8` cross-ref — not renamed this cycle; D1 adds a one-line legacy-label clause inline at the §6.3 consumer surface only.
- **Ratification ask 1 settled:** Per-surface `canonical_version` tracks framework version (3.0.2 confirmed at Phase-1 read); D3 bumps all four per-surface canonical_version fields with the framework_version.
- **Ratification ask 2 settled:** `README.md ## Status` section receives the adopter migration note (D4); no new section needed.
- **§18.3 protected:** M-A7 stays 38; "v3.0.2 canonicalization" historical strings in §18.3 preserved verbatim; defect-fix patch excluded from M-A7 count per inclusion criterion.
- **ADR-008 D6 confirmed** as the governing decision for intra-release-track patch tier (verified in Phase-1 ADR-008 structure read).

**Follow-up candidate register** (do not act; monitor for future cycles):
1. `dual-signal` rename — naming-consistency improvement; `core.md §8.1.1.1` title and §8.1 preamble use "dual-signal" as a legacy label while the body enumerates three endpoints. A dedicated naming-consistency patch cycle would update the label. Held.
2. `core.md §18.4` ADR-008 D6 citation specificity — §18.4 says "(ADR-008 D4)" for the roadmap-concept parenthetical and "ADR-008" generically for the bump-posture pointer. A follow-up could add "D6" by letter for precision. Held.

## Assumptions

- Base branch: `main` at `d596cd3` (PR-97 squash; 6/6 PASS pre-flight confirmed)
- Branch pattern `fix/task-####-<kebab-slug>` per `github-reference.md §2.2` + ADR-005 verified
- TASK-0052 is the free counter (highest observed TASK: TASK-0051) confirmed
- Anticipated PR-98 (highest PR at pre-flight: PR-97) confirmed; verified at `gh pr create`
- Predecessor SHA `b72bf45` (TASK-0051 / PR-95 full SHA: `b72bf455510be594e4986ec929b463b9a2b37356`) verified via `git log`
- Codex Reviewer operational for post-PR three-endpoint poll per §8.1.1.1

## §1. Cycle scope deliverables

Enumerated under Objective above (D1-D5).

## §2. Cycle gates

- **Gate A (pre-commit stop-and-show):** Builder presents staged-tree diff summary + cumulative-diff-stats + §6.3 rewrite + D3 target/exclusion confirmation + N/N self-review. Owner ratifies before commit.
- **Gate B (post-push five-point check):** After `git push` + `gh pr create`, Builder runs §24.3.1 five-point check (three-endpoint poll, branch SHA, file audit, phantom-action audit, comment-content claims) and hands back PR-98 URL + clean post-PR Codex three-endpoint poll result before owner squash-merge.

## §3. Execution record

1. Phase-1 diagnostic sweep on `main` at `d596cd3` — 5/5 pre-flight PASS; 2 FIX hits (github-reference.md:287, :289) + 4 HOLD hits (core.md:21, :23, github-reference.md:289 label, :396); Gate-A report assembled.
2. Phase-2 Architect adjudication — FIX/HOLD split ratified; ratification asks 1+2 settled; scope locked.
3. Branch `fix/task-0052-three-endpoint-canonical-reconciliation` created from `main` at `d596cd3`. Pre-flight 6/6 PASS.
4. D3 frontmatter bumps applied: trio frontmatter x3 (core.md, github-reference.md, usage-guide.md), in-dev markers x3 (README.md, AGENTS.md, CLAUDE.md), surfaces.yml framework_version + canonical_version x4.
5. D1 §6.3 rewrite applied to `github-reference.md`.
6. D2 §7.1 de-churn applied to `github-reference.md` (3 pins -> placeholders).
7. D4 adopter migration note appended to `README.md ## Status`.
8. D5 cycle artifacts authored: this handoff + `docs/reviews/PR-98-codex-pre-commit.md`.
9. §23.6.2 iterative self-review to fixed-point (see §5). **Next: Gate A stop-and-show; then stage + commit on owner approval; then push + PR-open.**

## §4. Substantive content evidence

**D1 — §6.3 rewrite anchor-verification** (byte-exact against `core.md §8.1.1.1`):
- Three endpoint names mirrored: formal Pull Request Review objects, top-level issue-comment summaries, line-level review comments
- Three GET paths byte-exact:
  - `GET /repos/{owner}/{repo}/pulls/{pull_number}/reviews`
  - `GET /repos/{owner}/{repo}/issues/{issue_number}/comments`
  - `GET /repos/{owner}/{repo}/pulls/{pull_number}/comments`
- "all three endpoints" (not "both") in the preamble and step-4 context
- Legacy-label clause: "`dual-signal` is retained as a legacy label for the established §8.1.1.1 discipline, which operationally spans three endpoint surfaces"
- Step-4 endpoint-specific freshness rows (M1 fix): three rows for reviews/commit_id, issues/created_at, pulls/commit_id+fallback
- Tie-break clause: "symmetrically across all three endpoints" + staleness-vs-tie-break distinction sentence
- `§8.1.1.1 (h.3)` citation preserved verbatim

**D2 — §7.1 de-churn**:
- `framework_version: <version>` (was 3.0.1)
- `canonical_version: <version>     # framework anchor (optional)` (AGENTS.md entry; was 3.0.1)
- `canonical_version: <version>` (CLAUDE.md entry; was 3.0.1)
- `template_version: 3.0.0` entries: unchanged

**D3 — version bump 9 sites**:
- core.md:2 `framework_version: 3.0.3`
- github-reference.md:2 `framework_version: 3.0.3`
- usage-guide.md:2 `framework_version: 3.0.3`
- README.md:9 `v3.0.3 (in development)`
- AGENTS.md:9 `v3.0.3 (in development)`
- CLAUDE.md:9 `v3.0.3 (in development)`
- .amas/surfaces.yml: `framework_version: 3.0.3` + `canonical_version: 3.0.3` x4
- §18.3 historical strings "v3.0.2 canonicalization" (core.md:584, :586): preserved
- v3.0.0 published markers (README.md, AGENTS.md, CLAUDE.md): preserved

**D4 — adopter migration note** (verbatim):
> Adopter migration note (v3.0.3): adopters who implemented review-freshness automation from `github-reference.md` §6.3 against two endpoints should add the line-level review-comments endpoint (`pulls/{pr}/comments`) before relying on "no findings" assertions, per the three-endpoint discipline at `core.md` §8.1.1.1.

## §5. Self-review record

**Iteration 1:**
- (j) all-instances sweep: no residual "two-endpoint"/"both endpoints" in §6.3; "dual-signal" at 4 HOLD sites (core.md:21, :23; github-reference.md:289 back-reference, :400 cross-ref); confirmed via grep.
- D3 target sweep: `grep -rn '3.0.2' core.md github-reference.md usage-guide.md README.md AGENTS.md CLAUDE.md .amas/surfaces.yml` — returns only core.md §18.3 historical strings (2 hits); correct.
- D3 count sweep: `grep -rn '3.0.3' ...` — returns 12 hits; expected 12 (11 D3 + 1 D4).
- §-citation sweep: `§8.1.1.1 (h.3)` — filter-boundary sub-shape label at core.md:133 (defined); §8.1.1.1 heading at core.md:23 (resolves); §6.3 title updated at github-reference.md:287.
- Scope protection: no .github/workflows/ file; no dual-signal rename; no template_version change; no §18.3 touch; no v3.0.0 marker change.
- **1 defect found:** D3 site count written as "9 sites" in handoff Objective + review context claim 19; correct value is 11 D3 sites (12 grep hits include D4). Corrected both files.

**Iteration 2 (post-correction):**
- Full sweeps repeated. All results same. "11 sites" and "12 hits" confirmed correct in both files.
- Zero defects found.

**Iteration 3 (confirming):**
- Spot-checks: §6.3 title, 3 GET paths, 3 step-4 validate rows, 3 §7.1 placeholders, 5 surfaces.yml 3.0.3 values, linked_pr form, review-context status frontmatter. All correct.
- Zero defects found. Two consecutive zero-defect iterations (iter 2 + iter 3): **fixed-point confirmed.**

**Gate A owner five-point check — path-(a) correction:**
- Finding: `issues/{pull_number}/comments` in §6.3 (GET block + step-4 row) diverges from `core.md §8.1.1.1` canonical form `issues/{issue_number}/comments`. Class fix (not instance fix) — both occurrences replaced.
- Fix applied: `replace_all` on `github-reference.md` `issues/{pull_number}/comments` → `issues/{issue_number}/comments` (2 hits: GET block line + step-4 row label).
- Cascaded to cycle artifacts: `docs/handoffs/…:120` §4 GET path listing + `docs/reviews/…:35` claim 4 description — both updated to `issues/{issue_number}/comments`.
- (j) sweep post-fix: `grep -n 'issues/{pull_number}/comments'` → zero hits in operational surfaces ✓.

## §6. Pre-commit absorption

(Populated post-Codex-desktop-pre-commit pass.)

## §7. Commit + push + PR-open record

- Commit: TBD (pending Gate A owner ratification)
- Push: TBD (§8.3 stop-and-show before push)
- PR-98: TBD (URL substituted here post-open; §8.3 stop-and-show before `gh pr create`)
- linked_pr squash SHA: TBD (substituted by linked-pr-fix-up Action post-merge per PMN-001 (k))

## §8. Post-PR Codex review state

(Populated at three-endpoint poll after `@codex review` trigger per §8.1.1.1.)

## §9. Sign-off

(Architect §24.3.1 five-point check post-merge; Architect populates.)

## §10. Cycle-close ledger

**Follow-up monitoring candidates** (do not act; Architect review):
1. `dual-signal` rename — `core.md §8.1.1.1` title + §8.1 preamble use "dual-signal" as a legacy label while the body enumerates three endpoints. A dedicated naming-consistency patch cycle would update all four HOLD sites consistently. Estimated scope: small (4 label-use sites, no operational content change).
2. `core.md §18.4` ADR-008 D6 citation specificity — §18.4 text says "(ADR-008 D4)" for the roadmap concept but does not specify "D6" by letter for the bump-posture pointer ("See ADR-008 for the decision"). Adding "D6" by letter would improve traversal precision. Estimated scope: minimal (one parenthetical addition).

**No new PMN candidate** — defect-fix patch; operational friction was pre-existing gap (two-endpoint description vs. three-endpoint canon), not a novel cycle-learning event. The three-endpoint discipline itself was canonicalized at TASK-0021 / PMN-008 §5.8 (h.4); this patch reconciles the description surface that lagged.

**No M-A7 close-reconciliation chore** — §18.3 intentionally not touched; defect-fix patch excluded from M-A7 count per established inclusion criterion; no PR-NN placeholder authored in §18.3.

**§24.6 Stop-Iteration pre-commitment:** reach-4 applies (post-PR pass-4 canonical boundary). At reach-4, halt, route residuals per condition B (documentary/operationally-hazardous classification), and hand back without extension.

## §11. Session log archive

(Architect + Builder session records per cycle iteration; populated per §13.1/§13.2 conventions.)
