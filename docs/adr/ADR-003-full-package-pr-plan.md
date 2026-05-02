# ADR-003 — Full v3.0 package PR plan and TASK reservation extension through TASK-0026

## Status

Accepted — 2026-05-01

Amends ADR-002 (further reservation extension, consistent with ADR-002 Decision 3 anticipation pattern). Partially supersedes ADR-001 decision 8 (PR sequence portion only; other ADR-001 decisions unchanged).

## Context

ADR-001 decision 8 named a PR-0 through PR-9 sequence with PR-9 = UPCDS adoption (a separate-repo cycle). ADR-002 extended the in-repo TASK reservation to TASK-0012 to accommodate PMN insertions and explicitly anticipated further extensions: "subsequent ADR amendments will document such extensions following the same pattern as ADR-002" (ADR-002 Decision 3).

The realized PR sequence has accumulated four post-merge-learning insertions in the TASK-0001 through TASK-0006 range — PMN-001 (TASK-0003), PMN-002 (TASK-0004), ADR-002 amendment (TASK-0005), PMN-003 (TASK-0006) — before any substantive v3 framework content has been authored. The original ADR-001 decision 8 PR sequence is structurally obsolete in two respects:

1. **TASK numbering**: ADR-001 decision 8 mapped substantive content PRs to TASK-0003 through TASK-0008. Reality maps them to TASK-0008 onward.
2. **Scope**: ADR-001 decision 8 named six substantive content PRs (PR-3 through PR-8) implicitly covering core, github-reference, usage-guide, prompts, templates, actions, and appendices in some unspecified grouping. The v3 transition plan v0.2 §10 named a 9-PR sequence for UPCDS but did not specify the standalone-repo grouping. The four-PR decomposition decided in the PR-6-close-to-PR-7-authoring session covers only the canonical-law trio (3 of 50 scaffold stubs); the remaining 47 stubs (templates, prompts, actions, appendices, adapter packs) have no resolved PR plan.

The README "Package layout" tables (authored at PR-2 against the original ADR-001 decision 8 plan) currently misrepresent the repo's PR sequence to anyone reading the repo: every stub's `filled_by` claim references a PR/TASK number that reality has falsified. The 47-uncovered-stubs question is a real architectural-level open question with material consequences for v3.0 ship scope.

PR-6's P1 finding (severity-taxonomy omission in TASK-0006 handoff step 4 — Architect-side authoring against repo discipline from memory rather than verification) and PMN-003 (a)'s in-cycle path-(a) revision propagation gap are evidence that authoring against stale-from-memory reference data is a recurrent defect class. Authoring four canonical-law PRs against a repo whose README and ADR set visibly misrepresent the PR plan would compound this defect class. Resolving the staleness now, before further canonical-content authoring, mitigates the defect class at structural level.

## Decision

Three substantive decisions plus one consequence-administration item.

**Decision 1: v3.0 ship scope is complete.** v3.0.0 ships when all 50 PR-2 scaffold stubs are filled with substantive content. No staged-v3.0 / v3.1+ deferral path. Adopters of v3.0 receive a fully usable framework: canonical law, materialized templates, working Actions, and complete appendices. A v3.0 that ships with stub templates and unenforced Actions provides minimal adopter value and would force every adopter to materialize their own templates from canonical text — defeating the purpose of distributed templates.

**Decision 2: PR plan is tight-coupling dependency order, twelve substantive content PRs.** Each PR cites only previously-merged canonical text. The plan:

| PR | TASK | Content | Files modified |
|---|---|---|---|
| PR-7 (this PR) | TASK-0007 | ADR-003 + README full sweep + ADR-001 Status update + 50-stub frontmatter sweep | ADR-003 (new), TASK-0007 handoff (new), PR-7 review-context (new), README.md, ADR-001, 50 scaffold stubs |
| PR-8 | TASK-0008 | `core.md` Part A (§1–§17 — foundations, role model, capability scoring, MCP transport security, role definitions, handoff schema, claimed-action verification principle, surface-file synchronization principle, PMN/ADR discipline) | core.md, TASK-0008 handoff, PR-8 review-context |
| PR-9 | TASK-0009 | `core.md` Part B (§18–§24 — workflow phase, PMN form, write-back, AI Session Log, handoff templates, deterministic enforcement, project instruction files, Architect-side prompt construction, cross-surface verify-before-assert) | core.md, TASK-0009 handoff, PR-9 review-context |
| PR-10 | TASK-0010 | `github-reference.md` (GitHub-specific implementation of core: branch naming, PR template, CODEOWNERS, AI agent identity, deterministic Actions reference) | github-reference.md, TASK-0010 handoff, PR-10 review-context |
| PR-11 | TASK-0011 | `usage-guide.md` (practical operating guidance, three-tier solo-operator framing, converging-lines-of-evidence framing, worked-example PMN absorption) | usage-guide.md, TASK-0011 handoff, PR-11 review-context |
| PR-12 | TASK-0012 | Process templates batch (9 files): handoff-template, review-template, post-merge-note-template, ADR-template, role-scorecard-template, feature-brief-template, project-brief-template, tool-inventory-template, surfaces-manifest-template.yml | 9 templates, TASK-0012 handoff, PR-12 review-context |
| PR-13 | TASK-0013 | GitHub-artifact templates batch (7 files): templates/AGENTS.md, templates/CLAUDE.md, templates/PULL_REQUEST_TEMPLATE.md, 4 ISSUE_TEMPLATE files | 7 templates, TASK-0013 handoff, PR-13 review-context |
| PR-14 | TASK-0014 | Prompts (3 files): greenfield, retrofit, upgrade | 3 prompts, TASK-0014 handoff, PR-14 review-context |
| PR-15 | TASK-0015 | Actions (9 workflows): branch-name-check, pr-template-check, linked-records-check, ai-session-log-check, review-freshness-check, surface-version-sync-check, artifact-path-check, claimed-action-verification, mcp-config-validation | 9 workflows, TASK-0015 handoff, PR-15 review-context |
| PR-16 | TASK-0016 | Flat appendices (7 files): mcp-integration, documentation-mcp-options, tool-capability-model, vendor-surface-guidance, github-review-automation, amas-vs-other-frameworks, regulated-tier-extension | 7 appendices, TASK-0016 handoff, PR-16 review-context |
| PR-17 | TASK-0017 | Project-type appendices (5 files): api-app, research-methodology, code-reports-data-analysis, documents-only, mixed | 5 appendices, TASK-0017 handoff, PR-17 review-context |
| PR-18 | TASK-0018 | Receiving-surface adapter packs (7 files): claude-code, codex, chatgpt, cursor, gemini, copilot, human-maintainer | 7 adapter packs, TASK-0018 handoff, PR-18 review-context |
| PR-19 | TASK-0019 | v3.0.0 release tag + final README polish (status update from "in production" to "released"; remove Roadmap progress markers) | README.md, git tag v3.0.0, TASK-0019 handoff, PR-19 review-context |

**Decision 3: TASK reservation extended through TASK-0026.** Thirteen substantive PR slots (PR-7 through PR-19, TASK-0007 through TASK-0019) are named in Decision 2. Seven contingency slots (TASK-0020 through TASK-0026) absorb anticipated PMN insertions during the substantive sequence. Empirical PMN rate at this project from PR-3 through PR-6 was three PMNs in four cycles; extrapolating across thirteen substantive cycles suggests three to seven PMN PRs likely. Seven contingency slots accommodate the high end with margin.

PMN insertions follow the established TASK-numbering discipline: PMN PRs consume the next available TASK slot at authoring time, not a pre-reserved slot. As PMN PRs land, subsequent substantive PR/TASK numbers shift. The Decision 2 table is an anticipated PR sequence; merge order is the authoritative final mapping. Each substantive PR updates its own README "Package layout" row and stub `filled_by` frontmatter at content-fill time to reflect its actual PR/TASK number — preventing recurrence of the README/stub staleness this ADR's full sweep resolves.

**Consequence administration**: ADR-002 reservation table (Decision 2) is wholly absorbed and extended by ADR-003 Decision 3. ADR-002 Decision 3 (PMN-insertion pattern recognition as framework feature) is preserved by reference and built upon by ADR-003 Decision 3's reservation extension. ADR-002 Status field unchanged per amendment convention.

ADR-001 decision 8 PR sequence portion is replaced by ADR-003 Decision 2. Other ADR-001 decisions (1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15) are unchanged. ADR-001 Status field updated to reflect partial supersession scope: "Accepted — 2026-04-30; decision 8 PR sequence portion superseded by ADR-003 (2026-05-01)."

UPCDS adoption (originally ADR-001 decision 8 PR-9 = UPCDS adoption in a separate repo) is unaffected by ADR-003. The UPCDS-side adoption sequence is governed by a separate ADR in the UPCDS repo when UPCDS adopts amas-framework v3.0.0; ADR-003 governs only amas-framework's in-repo PR plan.

## Alternatives considered

**(A) Staged v3.0**: ship canonical-law trio as v3.0 (TASK-0008 through TASK-0011 only); defer templates / prompts / actions / appendices / adapter packs to v3.1+. Rejected because shipping a framework without materialized templates and working Actions provides minimal adopter value. Adopters would receive principles without the operational machinery the principles describe — forcing each adopter to re-author templates from canonical text. The v3.0 transition plan v0.2 §3 explicitly enumerates the full package as the v3 deliverable; partial-ship contradicts that intent.

**(B) Continue per-PR ADR-002 amendment pattern**: each future PMN insertion extends reservation by one slot via a small standalone ADR amendment. Rejected because (1) cumulative drift makes the ADR-002 lineage difficult to read at any single point in time; (2) the substantive PR plan question (what content fills which PR) is unresolved by reservation extension alone — that question requires a substantive ADR regardless; (3) authoring multiple small amendments accumulates ceremony cost without resolving the underlying staleness defect class.

**(C) Loose-order PR sequence**: substantive PRs author in opportunistic order without strict cumulative-dependency constraint. Rejected because cross-references benefit from strict cumulative dependency. Each PR citing only previously-merged canonical text is the discipline aid that prevents cross-reference drift across the sequence — a 13-PR sequence is the longest the project has attempted, and the largest body of cross-reference work in the project's history. Loose ordering compounds reference-drift risk.

**(D) Skip stub frontmatter sweep**: leave 50 stubs with their current PR-N (TASK-NNNN) `filled_by` values; rely on each substantive PR to update its own stub at content-fill time. Rejected because that discipline failed empirically — PR-2 authored 50 stubs with `filled_by` values that reality falsified across PR-3 through PR-6, and the README "Package layout" tables compound the same defect class. Sweeping all 50 stubs to `filled_by: per ADR-003` (a generic reference rather than a specific PR number) breaks the staleness recurrence pattern: the reference points at the canonical plan rather than at a specific PR slot, so reservation drift no longer falsifies the stub.

**(E) Defer ADR-003 to PR-10 close (or later)**: monitor the four-PR canonical-law sequence; let field evidence inform whether the remaining 47 stubs need a single ADR-003 plan or some other shape. Rejected because the staleness is already actionable and visible to anyone reading the repo today; deferring resolution while authoring four more PRs against the stale state compounds the defect. Field evidence from PR-8 through PR-11 will inform Decision 2's PR plan in the sense that PMN insertions may shift specific PR numbers, but the structural decisions (complete v3.0 vs staged; tight-coupling order vs loose; reservation extent) are answerable now without the canonical-law-sequence empirical input.

## Consequences

- **TASK-0007 is reassigned from canonical-law-Part-A authoring (the original four-PR-decomposition plan) to ADR-003 + README sweep + frontmatter sweep**. Canonical-law authoring shifts: PR-8 / TASK-0008 (core Part A), PR-9 / TASK-0009 (core Part B), PR-10 / TASK-0010 (github-reference), PR-11 / TASK-0011 (usage-guide).
- **The four-PR canonical-law decomposition is preserved** as Decision 2's first four substantive PRs (PR-8 through PR-11). The decomposition rationale (bounded blast radius, natural §17/§18 cleavage in core.md, defect-density concentration in Part B) is unchanged; only the PR/TASK numbering shifts.
- **Each substantive PR (PR-8 through PR-19) updates its own README "Package layout" row** at content-fill time to reflect actual PR/TASK number landed. The Decision 2 table is the anticipated plan; merge-order is the authoritative final mapping. This discipline distributes README maintenance across the sequence and prevents another full sweep from being needed.
- **Each substantive PR also updates its own stub `filled_by` frontmatter** at content-fill time, from `filled_by: per ADR-003` (set by this PR) to `filled_by: PR-N (TASK-NNNN)` (the actual filling PR's number). This is the per-PR discipline that pairs with the README row update — the stub frontmatter declares the actual PR that filled it, not a forecast.
- **PMN insertions during PR-8 through PR-19** consume the next available TASK number and shift downstream substantive PR numbers by one. The Decision 2 table assumes zero PMN insertions for clarity; actual numbering will reflect insertions.
- **ADR-002 Status field unchanged** per amendment convention. ADR-002 Decision 3's anticipation language — "subsequent ADR amendments will document such extensions following the same pattern as ADR-002" — explicitly authorizes ADR-003's amendment pattern.
- **ADR-001 Status field updated** to reflect partial supersession of decision 8 only. Other ADR-001 decisions remain unchanged in substance and unchanged in Status implication.
- **README "Package layout" tables, Status text, and Roadmap text** are updated by this PR to reflect the ADR-003 plan. All 50 stub `filled_by` frontmatter lines are updated to `filled_by: per ADR-003` by this PR. Future per-PR row updates and frontmatter updates are scoped to the single row + single frontmatter line each substantive PR fills.
- **v3.0.0 release tag lands at PR-19**, after all 50 scaffold stubs are filled with substantive content. PR-19 also performs final README polish (Status text shifts from "in production" to "released"; Roadmap shifts to released-version-history).
- **UPCDS adoption** of amas-framework v3.0.0 occurs in a separate UPCDS-repo PR sequence governed by a UPCDS-side ADR. ADR-003 does not govern UPCDS-side scheduling.
- **Adopters of pre-v3.0.0 amas-framework** see partial visibility into the package: stubs with `filled_by: per ADR-003` and a README "Package layout" referencing the ADR-003 plan. Adopters reading the repo at any HEAD see what's currently filled vs anticipated, with the same precision the original PR-2 README aimed for but with durable accuracy under reservation drift.

## Evidence / references

- **ADR-001** decisions 1–7, 9–15 unchanged; decision 8 PR sequence portion superseded
- **ADR-002** Decision 3 anticipation language explicitly authorizes the ADR-003 amendment pattern; ADR-002 Decision 1 reservation through TASK-0012 absorbed and extended by ADR-003 Decision 3 to TASK-0026; ADR-002 Decision 2 reservation accounting table absorbed and extended by ADR-003 Decision 2 PR plan table
- **PMN-001, PMN-002, PMN-003** post-merge learning evidence justifying the staleness-defect framing in Context and the PMN-insertion budget in Decision 3
- **Session handoff 2026-05-01** (PR-6 close → PR-7 authoring) which scoped the four-PR canonical-law decomposition that ADR-003 Decision 2 preserves
- **v3 transition plan v0.2 §3** package structure and §10 PR sequence (UPCDS-relative, distinct from amas-framework's in-repo sequence governed by ADR-003)
- **FEAT-0001 PR-2 v3 framework package scaffold** spec — the 50-stub enumeration whose `filled_by` values this PR sweeps to `per ADR-003`
- **TASK-0001 through TASK-0006 handoffs** for cycle-closure context
- **README.md "Package layout" tables** — modified by this PR to reflect ADR-003 plan
