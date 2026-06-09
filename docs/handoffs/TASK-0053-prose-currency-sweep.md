---
task_id: TASK-0053
title: prose-currency sweep (README v3.0.0 tag language + archived design-brief schema pointer)
pr: PR-100
branch: chore/task-0053-prose-currency-sweep
linked_predecessor: TASK-0052 (PR-98 squash 63ac2d0 three-endpoint canonical reconciliation)
linked_successor: TBD
linked_pr: PR-100 (squash SHA 7502cb9)
framework_version_dogfooded: AMAS v3.0.3
production_target: AMAS v3.0
spec_source: .claude/session-handoffs/TASK-0053-spec.md
date_authored: 2026-06-08
status: resolved
---

# HANDOFF: TASK-0053

## Metadata

- Task ID: TASK-0053 (matches PR-100 anticipated)
- Linked Issue: none
- Linked PR: PR-100 — URL TBD at PR-open (substituted at step-13 per PMN-001 (k))
- Linked ADR(s): none (chore-class, no durable decision)
- Linked Feature Brief: none
- Linked review-context file: docs/reviews/PR-100-codex-pre-commit.md
- Owner role: Builder (Claude Code)
- Previous role: Architect (handoff direction Architect → Builder)
- Timestamp (UTC): 2026-06-08T00:00:00Z
- Last synced commit SHA: e5cfe9d5f8fba4e2ceb1b9adbe173f5a1293cb4c
- Branch: chore/task-0053-prose-currency-sweep
- Status: drafted
- Direction: Architect → Builder (universal handoff schema per `core.md` §14.1)
- Framework version: AMAS v3.0.3
- Recursive-self-instantiation salience: LOW (chore-class docs edit; no canonical-law amendment)

## Objective

Prose-currency sweep: three targeted edits across two files to close stale conditional language in `README.md` and add a dated schema-pointer note in `prompts/deep-research-design-brief.md`. Chore-class, docs-only cycle — no canonical-law amendment, no `framework_version` change (trio stays at v3.0.3), M-A7 stays at 38.

**Deliverables (3 edits across 2 files):**

1. **`README.md` Edit 1** (~L9, `## Status` region): Reframe stale conditional tag clause to past tense + disambiguate git-tag vs GitHub-release status. Replace "adopters should reference the v3.0.0 release, governed by this version-positioning note together with the v3.0.0 release tag once the owner publishes it, until the v3.1 release." with the published-tag / no-GitHub-release clarification per Phase-1.5 Gate C finding (git tag v3.0.0 exists; no GitHub release published).

2. **`README.md` Edit 2** (~L32, Roadmap paragraph): Reframe forward-looking tag clause to past tense. Replace "the v3.0.0 release tag is applied by the owner at merge time" with "the v3.0.0 git tag has been applied".

3. **`prompts/deep-research-design-brief.md` Edit 3** (~L67, before surface-sync schema region): Insert additive dated editorial pointer noting the superseded `templates:` map form and `framework_version: 3.0.0` pins; preserve the illustrative YAML and review-freshness-workflow block below it verbatim as archived design exploration.

## Last completed step

Codex post-PR pass 1 absorbed (2026-06-08T21:23:59Z); Minor P2 (handoff gate-current stale, lines 50-54) found; path-(a) correction committed. Next: push fix-up commit then post-PR re-review then Gate B then squash.

## Current state

**Summary**: Post-PR state: fix-up commit applied (path-(a) handoff gate-current correction + review-context post-PR absorption); ready to push for post-PR re-review.

**Files authored / modified:**
1. NEW `docs/handoffs/TASK-0053-prose-currency-sweep.md` — this handoff (status: `active`)
2. MODIFIED `README.md` — Edits 1 + 2 (tag-language currency) ✓
3. MODIFIED `prompts/deep-research-design-brief.md` — Edit 3 (additive schema pointer) ✓
4. NEW `docs/reviews/PR-100-codex-pre-commit.md` — review-context (Codex fix-up in progress)

**Cumulative-diff-stats**: TBD — re-derived after fix-up edits staged.

## Decisions made

- **Phase-1 diagnostic**: buckets A–D enumerated; fix-scope set by Architect + owner ratification.
- **Bucket B (25 handoff body `- Status:` mismatches) — OUT OF SCOPE**: Phase-1.5 Gate B confirmed body `- Status:` is a last-Builder-gate snapshot; the linked-pr-fix-up Action only updates frontmatter `status:`. Core.md §13.2:259 + §14:718 confirm no body surface is a cycle-close marker. Body `- Status:` values are correct-by-design; not touched this cycle.
- **FEAT-0001 (`docs/features/FEAT-0001-v3-package-scaffold.md`) — OUT OF SCOPE**: authoring-time-scoped feature brief; `framework_version: 3.0.0` reference describes original scaffold state. Owner ratified out of scope.
- **`template_version: 3.0.0` values — OUT OF SCOPE**: intentional per core.md §17.5 separate template-version axis; do not change with framework patch bumps.
- **core.md §18.3 M-A7 historical strings — OUT OF SCOPE**: explicitly excluded per spec (M-A7 exclusion).
- **`actions/fixtures/surface-version-sync-check/stale-manifest.yml` `framework_version: 3.0.2` — OUT OF SCOPE**: intentional negative fixture; explicitly excluded.
- **No `framework_version` bump**: chore-class docs-only; trio stays v3.0.3. M-A7 stays 38.
- **No GitHub release**: Phase-1.5 Gate C confirmed no GitHub release exists for v3.0.0; Edit 1 disambiguates. Creation of a GitHub release is out of scope.
- **Anticipated PR-100**: ratified at step-1 stop-and-show; "verify at PR-open" per §23.6.3 sub-shape E.

## Assumptions

- Working tree clean at branch creation (verified at pre-flight: HEAD `e5cfe9d`, clean).
- `README.md` and `prompts/deep-research-design-brief.md` edit targets confirmed present as literal strings (all 3 verified at step-1 pre-flight item 7).
- Codex Reviewer operational (ADR-001 D11 owner-invokes).
- No branch-protection conflicts for `chore/` type branches.

## §1. Cycle scope deliverables

Three edits across two files:

| # | File | Edit | Scope |
|---|------|------|-------|
| 1 | `README.md` ~L9 | Tag clause → past tense + tag-vs-release disambiguation | IN SCOPE |
| 2 | `README.md` ~L32 | Forward-looking tag clause → past tense | IN SCOPE |
| 3 | `prompts/deep-research-design-brief.md` ~L67 | Additive dated editorial pointer (YAML preserved) | IN SCOPE |

**Explicit out-of-scope register:**
- Bucket B: 25 handoff body `- Status: active/drafted` mismatches — last-gate snapshots, not residuals (per core.md §13.2 + §14; Phase-1.5 Gate B confirmed)
- `docs/features/FEAT-0001-v3-package-scaffold.md` — authoring-time-scoped; out of scope per owner ratification
- All `template_version: 3.0.0` values — intentional per §17.5
- `core.md` §18.3 M-A7 historical strings — explicitly excluded per spec
- `actions/fixtures/surface-version-sync-check/stale-manifest.yml` — intentional negative fixture
- `framework_version` bump — not triggered (chore-class)
- GitHub release creation — out of scope

## §2. Cycle gates

- **Gate A (pre-commit)**: staged-tree diff-stats + per-file numstat; only `README.md`, `prompts/deep-research-design-brief.md`, new handoff touched; Architect §24.3.1 five-point check before commit authorization.
- **Gate B (pre-push)**: post-commit SHA verification + `git status --porcelain` clean.

## §3. Step-by-step execution record

- **Step 1** (pre-flight): 7/7 PASS. HEAD `e5cfe9d`, clean tree, `main` current with origin, TASK counter confirmed (max `TASK-0052`), anticipated PR-100, predecessor `63ac2d0` resolvable, all 3 edit targets literal-confirmed.
- **Step 2** (branch + handoff): branch `chore/task-0053-prose-currency-sweep` created from `e5cfe9d`; handoff authored at `docs/handoffs/TASK-0053-prose-currency-sweep.md` (status: `drafted`).
- **Step 3** (three edits): pending — to be applied next.
- **Step 4** (stage + Gate A): pending.

## §10. Cycle-close ledger

*(Populated at cycle close.)*

## §11. Session log archive

*(Builder session record appended at Gate B / PR-open.)*
