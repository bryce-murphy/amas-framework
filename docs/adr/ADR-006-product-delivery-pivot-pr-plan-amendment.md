# ADR-006 — Product-delivery pivot: ADR-003 D2 PR plan amendment + PMN-after-cycle cadence relaxation

## Status

Accepted — 2026-05-06.

Amends ADR-003 (further partial-supersession of D2 PR plan portion only; D1 ship scope + D3 reservation extension preserved). Precedent: ADR-002 amendment of ADR-001 D8; ADR-003 partial-supersession of ADR-001 D8; ADR-005 partial-supersession of v2.14.1 §6.1 substrate.

Effective: immediately for v3 in-repo cycle direction; remaining 47 unfilled stubs filled per revised dependency order documented below.

## Context

ADR-003 D2 (2026-05-01) named a 12-PR substantive content sequence (PR-7 through PR-19) to ship v3.0.0 + a PMN insertion budget of 7 contingency slots (TASK-0020 through TASK-0026; "extrapolating across thirteen substantive cycles suggests three to seven PMN PRs likely") with an empirical PMN rate of 3 PMNs per 4 cycles (75%) measured through PR-6.

Empirical reality at the close of TASK-0026 / PR-33 (2026-05-06):

- **PR sequence**: 33 PRs merged. ADR-003 D2 forecast PR-19 = v3.0.0 release; reality is PR-33 with most stubs unfilled.
- **Stubs filled**: ~3 of 50 (canonical-law trio: `core.md`, `github-reference.md`, `usage-guide.md`) plus 1 Action shipped via ADR-004 (`linked-pr-fix-up.yml`) plus AGENTS.md / CLAUDE.md migrations (operating-instruction surfaces, not scaffold-stubs proper).
- **Stubs unfilled**: 47 — 9 process templates (handoff, review, post-merge-note, ADR, role-scorecard, feature-brief, project-brief, tool-inventory, surfaces-manifest) + 7 GitHub-artifact templates (templates/AGENTS.md, templates/CLAUDE.md, templates/PULL_REQUEST_TEMPLATE.md, 4 ISSUE_TEMPLATE files) + 3 prompts (greenfield, retrofit, upgrade) + 9 canonical Actions (branch-name-check, pr-template-check, linked-records-check, ai-session-log-check, review-freshness-check, surface-version-sync-check, artifact-path-check, claimed-action-verification, mcp-config-validation; linked-pr-fix-up.yml shipped separately via ADR-004 operational insertion ahead of canonical Actions batch — additive to the 9-Action scaffold, not subtractive) + 7 flat appendices + 5 project-type appendices + 7 receiving-surface adapter packs.
- **PMN-after-cycle cadence**: 10 PMNs authored (PMN-001 through PMN-010); ~30+ cycles total when including chore-fix-up PRs (PR-22, PR-24, PR-26, PR-28, PR-30, PR-32, PR-34) + ADR insertions (ADR-002 / ADR-003 / ADR-004 / ADR-005 = 4 ADRs across 27 cycles); PMN rate ~31% of substantive cycles; meta-discipline cadence dominates.
- **Cycle outcomes**: meta-disciplines mature (verification batches, sub-shape taxonomies, multi-surface review pipeline, branch-convention canonicalization). Adopter-facing deliverables (templates, prompts, actions, appendices, adapter packs) substantially unstarted.

The ADR-003 D2 PR plan is empirically falsified at scope and timeline. The README "Package layout" tables (last swept at PR-7 to point at `per ADR-003`) currently misrepresent the repo's plan to anyone reading the repo: every unfilled stub's `filled_by` claim references a PR/TASK number ADR-003 forecast that reality has falsified for the second time (PR-2 forecast falsified at PR-7 sweep; PR-7 forecast falsified at PR-33 with most stubs unfilled).

The diagnosis is not that meta-discipline cycles produced no value — they produced 10 PMNs, 5 ADRs, and a battle-tested cycle protocol. The diagnosis is that the marginal value curve has flattened: each additional meta-discipline cycle does less than the prior one because the high-value taxonomic / governance observations have been canonicalized. Meanwhile, the framework's stated v3.0.0 ship goal (50 stubs filled per ADR-003 D1) remains substantially unstarted.

## Decision

Four substantive decisions.

**Decision 1: Acknowledge plan-vs-reality gap; ADR-003 D2 PR plan empirically falsified at scope.** ADR-003 D2 named PR-7 through PR-19 to ship v3.0.0; PR-33 reality has most stubs unfilled. Decision 2 PR plan portion partially superseded by this ADR. ADR-003 Decision 1 (v3.0 ship scope = 50 stubs filled) and Decision 3 (TASK reservation extension pattern + PMN insertion budget pattern) preserved unchanged.

**Decision 2: Revised remaining-work scope per dependency order.** 47 unfilled stubs filled per the following batch sequence. Each batch ships in one or more substantive content cycles (cycle count not pre-committed; anti-fragile to PMN/discipline insertion drift):

| Batch | Files | Dependency rationale |
|---|---|---|
| **Batch P1**: process templates (9 files) | handoff-template, review-template, post-merge-note-template, ADR-template, role-scorecard, feature-brief, project-brief, tool-inventory, surfaces-manifest | Cycle-execution canonical surface; most-used per cycle; cited by canonical-law trio. **TASK-0027 begins this batch with handoff-template + review-template (highest-leverage starting pair).** |
| **Batch P2**: GitHub-artifact templates (7 files) | templates/AGENTS.md, templates/CLAUDE.md, templates/PULL_REQUEST_TEMPLATE.md, 4 ISSUE_TEMPLATE files | Distributed surfaces consumed by adopters; depend on Batch P1 form alignment (process templates establish canonical lifecycle shapes). |
| **Batch P3**: prompts (3 files) | greenfield, retrofit, upgrade | Project-kickoff surfaces; depend on Batch P1 + P2 (templates referenced from kickoff prompts). |
| **Batch P4**: Actions (9 canonical scaffold files; linked-pr-fix-up.yml already shipped via ADR-004 operational insertion ahead of this batch — additive, not subtractive) | branch-name-check, pr-template-check, linked-records-check, ai-session-log-check, review-freshness-check, surface-version-sync-check, artifact-path-check, claimed-action-verification, mcp-config-validation | Deterministic enforcement layer; depend on Batch P1-P2 templates as enforcement targets. |
| **Batch P5**: flat appendices (7 files) | mcp-integration, documentation-mcp-options, tool-capability-model, vendor-surface-guidance, github-review-automation, amas-vs-other-frameworks, regulated-tier-extension | Reference content; minimally cross-dependent with prior batches; can ship in parallel with later P-batches. |
| **Batch P6**: project-type appendices (5 files) | api-app, research-methodology, code-reports-data-analysis, documents-only, mixed | Project-type-specific guidance; minimally cross-dependent with prior batches. |
| **Batch P7**: receiving-surface adapter packs (7 files) | claude-code, codex, chatgpt, cursor, gemini, copilot, human-maintainer | Vendor-specific receiving-surface translation; minimally cross-dependent with prior batches. |
| **Batch P8**: v3.0.0 release tag + final README polish | README.md, git tag v3.0.0 | Capstone PR; depends on all 47 stubs filled. |

Cycle-count expectation: not pre-committed. Each batch may ship in 1-N cycles depending on per-template content scope. PMN/discipline insertions remain expected at the lower per-cycle rate per Decision 4 below.

**Decision 3: PMN-after-cycle cadence relaxation.** PMN authoring threshold raised from "default after every cycle" to "evidence is strong AND discipline cost-benefit favorable." Specifically:

- **Promote candidate observation to PMN** when: (a) cross-cycle empirical evidence accumulates to 3+ confirmations within the same defect class, AND (b) the canonicalization-cost (200-260 source lines + cycle bandwidth) is materially smaller than the projected adopter-cost-of-discipline-absent.
- **Lightweight observation absorption is preferred default** when: (a) single-cycle observation, OR (b) refinement of existing canonical text by 1-3 lines, OR (c) state correction without novel taxonomic content.
- **Lightweight absorption venues**: cycle-close ledger entries (informational); discipline-anchor 1-3 line additions (canonical text); template body documentation (when authoring a template that formalizes the discipline).

Most cycles become content-production cycles. Meta-discipline cycles continue when warranted by evidence-bar discipline.

**Decision 4: README distributed-update discipline applies to ADR-006 amendment.** README "Package layout" tables continue per-PR `Filled by` cell update at content-fill time (ADR-003 §Consequences pattern). Additionally, README "Roadmap" text updated at this PR to reflect Decision 2 batch sequence rather than ADR-003 D2 12-PR forecast (single-paragraph update; preserves ADR-003 cross-reference + adds ADR-006 cross-reference).

## Alternatives considered

**(A) Continue meta-discipline cadence; defer ADR-006 indefinitely.** Rejected because the plan-vs-reality gap is empirically actionable today; deferring further compounds the staleness defect class (the same defect class ADR-003 was authored to mitigate in PR-7 — recurrence in the same project after 26 cycles is itself evidence of cadence drift). PMN-008 / PMN-010 + ADR-005 mature the meta-discipline framework sufficiently; further refinement does not advance the v3.0.0 ship goal.

**(B) Author ADR-006 as full-rewrite of ADR-003 (not partial-supersession).** Rejected because ADR-003 D1 (v3.0 ship scope = 50 stubs) and D3 (TASK reservation extension pattern + PMN insertion budget framing) are still load-bearing canonical decisions. D1 frames v3.0 completion criteria; D3 establishes the PMN-as-regular-feature pattern that this ADR's Decision 3 refines (does not replace). Partial-supersession preserves intentful framework structure.

**(C) Pivot product-delivery via informal direction (not ADR-class adjudication).** Rejected because direction-decisions of this scope warrant ADR per ADR-005 substantive-direction-decision precedent. Informal direction would not durably document the plan-vs-reality gap or the cadence relaxation; future-cycle Architects (or external adopters) reading the repo would encounter ADR-003 D2 as canonical without amendment marker.

**(D) Delay ADR-006 until first templates batch ships (ship templates, then document plan).** Rejected because authoring templates against an empirically-falsified plan is the same defect class ADR-003 mitigated at PR-7. Resolving the staleness now, before further substantive content cycles, mitigates the defect class at structural level. Concurrent ADR-006 + first templates batch (this cycle) ships both in the same PR per single-PR-with-split-trigger discipline (TASK-0012 Part B precedent).

**(E) Defer cadence relaxation to subsequent ADR; Decision 3 scope reduced to plan amendment only.** Rejected because the plan-vs-reality gap and the cadence reflexivity are coupled phenomena: the plan was falsified partly because PMN-after-cycle cadence absorbed cycle bandwidth that would have advanced the plan. Resolving them separately produces inconsistent direction (revised plan with unrevised cadence reproduces the same defect class).

## Consequences

- **ADR-003 Decision 2 PR plan portion partially superseded** by this ADR Decision 2. ADR-003 Decision 1 (v3.0 ship scope) and Decision 3 (reservation extension + PMN insertion budget) preserved unchanged. ADR-003 §Status field updated to reflect partial-supersession of D2 by ADR-006 (consistent with ADR-002 amendment / ADR-003 partial-supersession of ADR-001 D8 pattern).

- **TASK-0027 begins Batch P1 (process templates)** with `templates/handoff-template.md` + `templates/review-template.md` substantive content fill (highest-leverage starting pair: most-cited in canonical-law trio + most-used in cycle execution + paired set forming canonical cycle-execution surface).

- **Each batch's PR(s) update README "Package layout" rows** at content-fill time per ADR-003 §Consequences distributed-update discipline (preserved). Each filled stub's `filled_by` frontmatter updated from `per ADR-003` to `PR-N (TASK-NNNN)`.

- **Decision 4 distributed-update discipline applies retroactively to forecasts falsified by partial-supersession.** When this ADR (or any future partial-supersession ADR) amends a previously-documented forecast in distributed surfaces (README "Package layout" rows, "Roadmap" text, stub `filled_by` frontmatter, etc.), the distributed-update sweep MUST be applied retroactively at the partial-supersession event — not deferred to per-row content-fill cycles. Otherwise the distributed surfaces continue advertising the falsified forecast post-amendment, reproducing the exact stale-forecast defect class the partial-supersession was authored to correct. Empirically grounded at TASK-0027 / PR-35 Edit R.10: 45-row supersession-marking sweep `PR-N (TASK-NNNN)` → `Batch P[X] (ADR-006); pending content-fill cycle` across Batches P1-P7 applied within-cycle per owner direction 2026-05-07 §1 ratification.

- **PMN insertion budget reset** for remaining cycles per Decision 3 cadence relaxation. Specific count not committed (anti-fragile to drift). Empirical PMN rate may fall to 5-15% of substantive cycles under cadence relaxation (vs ~31% historical observed rate).

- **Cycle-count forecast not committed.** Each batch ships in 1-N cycles depending on per-template/per-action/per-appendix content scope. Architect-side cycle-count anticipation per cycle remains in scope (per `core.md` §23.6.3 sub-shape A discipline).

- **README "Roadmap" text updated at this PR** to reflect Batch P1-P8 sequence rather than ADR-003 D2 12-PR forecast. Single-paragraph update preserving ADR-003 cross-reference + adding ADR-006 cross-reference.

- **README "Package layout" Templates table 2 rows updated at this PR** per Decision 4 distributed-update discipline: `templates/handoff-template.md` `Filled by: PR-12 (TASK-0012)` → `PR-35 (TASK-0027)`; `templates/review-template.md` `Filled by: PR-12 (TASK-0012)` → `PR-35 (TASK-0027)`.

- **Adopters of pre-v3.0.0 amas-framework** see ADR-006 as the current canonical PR plan reference; ADR-003 D2 marked partially-superseded. Adopters reading the repo at any HEAD see Batch P1-P8 sequence + per-batch progress.

- **UPCDS adoption** of amas-framework v3.0.0 unaffected by this ADR (per ADR-003 §Consequences UPCDS-side-ADR convention).

## Cross-references

- **ADR-001** decisions 1-7, 9-15 unchanged; decision 8 PR sequence portion superseded by ADR-003 (preserved); ADR-001 §Status field unchanged (already reflects ADR-003 partial-supersession).
- **ADR-002** Decision 3 anticipation pattern; ADR-002 Status field unchanged per amendment convention.
- **ADR-003** Decision 1 (v3.0 ship scope) preserved; Decision 2 (PR plan) partially superseded by this ADR Decision 2; Decision 3 (TASK reservation + PMN insertion budget) preserved; §Consequences distributed-update discipline preserved.
- **ADR-004** linked-pr-fix-up.yml shipped via ADR-004 operational insertion ahead of canonical Actions batch (additive to the 9-Action scaffold, not subtractive); see Decision 2 Batch P4 row for canonical framing.
- **ADR-005** branch convention canonicalization + partial-supersession-via-deliberate-divergence precedent; ADR-006 follows same partial-supersession pattern.
- **PMN-001 through PMN-010** post-merge learning evidence justifying the cadence reflexivity diagnosis in §Context.
- **Transition plan v0.2 §3 / §10** package structure + UPCDS-relative PR sequence (distinct from amas-framework's in-repo sequence governed by ADR-003 + this ADR).
- **FEAT-0001 PR-2 v3 framework package scaffold** — the 50-stub enumeration whose `filled_by` values continue to point at canonical plan reference (now ADR-006 for unfilled stubs at content-fill time per Decision 4 distributed-update discipline).
- **TASK-0027 (this PR)** — first cycle executing Decision 2 Batch P1 + Decision 3 cadence relaxation.
