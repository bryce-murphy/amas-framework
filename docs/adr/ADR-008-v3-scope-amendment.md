---
adr_id: ADR-008
title: v3.0 scope amendment — minimum-viable canonical framework + v3.1+ phased roadmap
status: Accepted
date: 2026-05-20
amends: ADR-003 (Decision 1 partial-supersession; v3.0 ship scope revised) + ADR-006 (Decisions 1 + 2 partial-supersession; v3.0 ship criteria + remaining-work batch sequence revised)
supersedes: none
superseded_by: none
---

# ADR-008 — v3.0 scope amendment: minimum-viable canonical framework + v3.1+ phased roadmap

## Status

Accepted — 2026-05-20.

Amends ADR-003 (Decision 1 partial-supersession; v3.0 ship scope revised from "50 stubs filled = complete package" to "canonical-law trio + Part C.1 + Part C.2 + Batches P1-P3 + release polish = minimum viable canonical framework"). Amends ADR-006 (Decisions 1 + 2 partial-supersession; v3.0 ship criteria + remaining-work batch sequence revised consistent with ADR-003 D1 partial-supersession scope). ADR-007 Decisions 1 + 2 + 3 + 4 preserved unchanged — Part C scoping + Part C.2-before-P4 Actions ordering canonical at amended scope. ADR-003 Decisions 2 + 3 preserved (D2 PR plan portion already partially superseded at ADR-006 D2; D3 TASK reservation + PMN insertion budget preserved). ADR-006 Decisions 3 + 4 preserved (D3 lightweight-absorption framework; D4 distributed-update discipline + Item 14 retroactive-supersession-marking sub-rule). Precedent: ADR-006 partial-supersession of ADR-003 D2; ADR-007 further partial-supersession of ADR-006 D2; ADR-008 follows same partial-supersession-via-amendment pattern at orthogonal scope axis (ship-criteria + remaining-batch-deferral rather than batch-sequence-insertion).

Effective: immediately for v3 in-repo cycle direction; remaining cycles to v3.0.0 ship execute per ADR-008 Decision 2 amended sequence.

## Context

ADR-003 Decision 1 (2026-05-01) named v3.0 ship scope as "50 scaffold stubs filled = complete package" — the canonical framing for v3.0.0 release completion criteria. ADR-006 Decision 1 (2026-05-06) acknowledged the plan-vs-reality gap at the PR plan portion (Decision 2 partial-supersession) but PRESERVED ADR-003 Decision 1 ship-scope-criterion unchanged: "ADR-003 Decision 1 (v3.0 ship scope = 50 stubs filled) and Decision 3 (TASK reservation extension pattern + PMN insertion budget pattern) preserved unchanged." ADR-007 Decision 1 (2026-05-07) amended ADR-006 Decision 2 at batch-sequence-insertion scope (Part C.1 + Part C.2 inserted) without touching Decision 1 ship-scope-criterion.

**Predecessor decisions context**:

- **ADR-003 D1 reasoning**: 50 scaffold stubs filled = full adopter value. No staged-v3.0 / v3.1+ deferral. Justification: comprehensive reference package at first release; adopters get complete framework rather than incremental layers.
- **ADR-006 D1/D2**: empirical PR-plan falsification at 26-cycle horizon; revised remaining-work batch sequence (Batches P1-P8) preserving 50-stubs-filled scope.
- **ADR-007 D1-D4**: Part C materialization scoping decision; Part C.1 cycle-execution canonical (§14 / §17.5 / §17.7) before remaining P1 templates; Part C.2 operating-discipline canonical (§8.2 / §8.3 / §13 / §10.5 / §23.6.5) before Batch P4 Actions; per-cycle distributed-update sweeps drop `(forthcoming at Part C+)` qualifier.

**Operational evidence postdating predecessor decisions**:

- **PMN-012 adoption-pilot empirical record** (`docs/post-merge-notes/PMN-012-pr-50-cycle-learnings.md`): first AMAS adoption pilot at bryce-murphy/employee-churn completed end-to-end in retrofit mode using canonical-law trio + Batch P1 process templates. Pilot encountered F1 packaging-qualifier-instance ambiguity friction at canonical-law trio + just-shipped Batch P1 templates (validates ADR-007 adopter-readability concern at substrate-qualifier sites). Pilot did NOT use Batches P4 (Actions) through P8 (release polish) in pilot scope; these batches were not blocking for pilot completion. PMN-012 documented the absence — pilot was retrofit-mode through canonical-text + Batch P1 form alone.
- **TASK-0040 + TASK-0041 cycle empirical load**: TASK-0041 §24.6 reach 4+ canonical boundary engagement at LOW-recursive-self-instantiation-classified substantive-content cycle (anticipation broken at empirical engagement); 14 in-cycle Architect adjudication-surface defects across cycle (strongest single-cycle observation in cycle history); first cross-cycle HYBRID closure precedent at §24.6 condition (B-3) refined application. Cycle empirical load materially higher than ADR-007 Decision 4 cycle-bandwidth expectation framing — cycle bandwidth absorbed by multi-surface review pipeline iteration + Stop-Iteration framework engagement rather than substantive-content shipping.
- **Cross-Architect critique pilot empirical positive** at TASK-0041 + TASK-0042 scoping cycles: cross-cycle reach 3 of distinct primary-Architect framing-gap catches at Phase 1 scoping (TASK-0040 scoping; TASK-0041 scoping; TASK-0042 scoping). Pattern empirically robust at three independent cycles; canonicalization-promotion candidate at Phase 1 scoping if pattern persists at TASK-0043+ cycles per ADR-008 cycle-close ledger forward-reference (deferred to post-v3.0.0 per PMN-013 §6.x carry-forward framework).

**Operational evidence vs theoretical evidence asymmetry**:

ADR-003 D1 + ADR-006 D1/D2 + ADR-007 reasoning was theoretically-derived: forward-reference analysis (50-stubs-filled = adopter-comprehensive package); adopter-readability anticipation (Part C materialization before adopter-readable v3.0.0); cycle-count anticipation at substantive-content batch level. PMN-012 + TASK-0040/0041 + cross-Architect pilot is operationally-derived: actual adoption pilot completion at retrofit mode; actual cycle empirical load at MEDIUM-to-MAXIMUM substantive engagement; actual cross-Architect framing-gap detection at three Phase 1 scoping cycles. Operational evidence postdating theoretical reasoning is the canonical condition for ADR amendment per ADR-006 D3 evidence-bar discipline + ADR-007 Decision 1 architectural-gap-acknowledgment precedent.

**Honest acknowledgment of remaining uncertainty**:

PMN-012 evidence supports amendment but is narrowly bounded. The pilot was retrofit, not greenfield: an existing project adopting AMAS canonical-law trio + Batch P1 templates without Batches P4-P8. The pilot did not validate P4-P8 unnecessity — it demonstrated P4-P8 were not blocking for this specific retrofit pilot. A greenfield project pilot, or a different project-class retrofit, might surface different blocking-vs-non-blocking signal. Amendment is justified by the affirmative framing: "highest-value ship blocker is canonical/readability/packaging clarity at the canonical-law-trio + Part C + Batches P1-P3 surface; P4-P8 remain unvalidated inferred needs whose pilot evidence is not yet available." Amendment is NOT justified by the negative framing: "P4-P8 are unnecessary." Decision 4 phased-v3.1+ roadmap preserves P4-P8 ship commitment at named release boundaries; deferral is bounded, not abandonment.

**Current state at ADR-008 ship**:

Package-layout enumeration at README package-layout tables (52 rows distributed across 7 sub-tables): canonical-law (3 filled) + prompts (5 rows; 2 archived filled + 3 pending) + templates (16 rows; 12 filled + 4 ISSUE_TEMPLATE pending) + Actions (9 rows; 0 filled) + flat appendices (7 rows; 0 filled) + project-type appendices (5 rows; 0 filled) + receiving-surface adapters (7 rows; 0 filled). The "50 scaffold stubs" framing at ADR-003 D1 enumerated the unfilled scaffold set at PR-2 baseline (excluding canonical-law trio mid-cycle fills + 2 archived prompts); current 52-row enumeration includes filled-mid-cycle canonical-law + archived prompts. Both framings refer to the same FEAT-0001 PR-2 v3 framework package scaffold; counting-convention difference is non-substantive.

## Decision

### Decision 1 — Acknowledge plan-vs-evidence gap; ADR-003 D1 + ADR-006 D1/D2 partial supersession at v3.0 ship scope

ADR-003 D1 v3.0 ship scope ("50 stubs filled = complete package") is empirically falsified at the operational-evidence-vs-theoretical-reasoning axis per PMN-012 + TASK-0040/0041 + cross-Architect pilot record above. Operational evidence postdating theoretical reasoning supports revision; ADR-003 Decision 1 partially superseded at v3.0 ship-scope-criterion portion only. ADR-006 Decisions 1 + 2 partially superseded consistent with ADR-003 D1 partial-supersession (D1 ship-criterion + D2 remaining-batch-sequence both touched). ADR-007 Decisions 1 + 2 + 3 + 4 preserved unchanged — Part C scoping + Part C.2-before-P4 Actions ordering canonical at amended scope per ADR-007 D2 adopter-readability rationale (Part C.2 operating-discipline canonical surfaces materially advance adopter-readiness; ADR-008 D2 retains Part C.2 in v3.0 minimum scope).

Other predecessor ADR decisions preserved: ADR-001 D1-D7 + D9-D15 unchanged (D8 PR sequence portion previously superseded by ADR-003); ADR-002 amendment pattern preserved; ADR-003 D2 PR plan portion (previously partially superseded at ADR-006 D2) further-partially-superseded by ADR-008 D2 at remaining-batch portion; ADR-003 D3 TASK reservation + PMN insertion budget preserved; ADR-004 linked-pr-fix-up Action operational + preserved; ADR-005 branch convention preserved; ADR-006 D3 lightweight-absorption framework + D4 distributed-update discipline preserved.

### Decision 2 — Revised v3.0 minimum scope and amended remaining-work batch sequence

v3.0 ship scope at ADR-008:

- **canonical-law trio** (DONE; `core.md` + `github-reference.md` + `usage-guide.md` shipped at PR-10 + PR-13 + PR-17 + PR-29 prior cycles)
- **Part C.1** (DONE; cycle-execution canonical surfaces — §14 + §14.1-§14.7 + §17.5 + §17.7 shipped at PR-41 / TASK-0030 per ADR-007 D3 schedule)
- **Part C.2** (PENDING; operating-discipline canonical surfaces — §8.2 + §8.3 + §13 + §10.5 + §23.6.5 per ADR-007 Decision 2 enumeration; per ADR-007 D3 schedule lands BEFORE Batch P4 Actions; preserved in v3.0 minimum scope per ADR-007 adopter-readability rationale)
- **Batch P1** (DONE; 9/9 process templates filled — handoff-template + review-template + post-merge-note-template + ADR-template + role-scorecard + feature-brief + project-brief + tool-inventory + surfaces-manifest)
- **Batch P2** (IN PROGRESS; 3/7 GitHub-artifact templates filled at TASK-0041 — templates/AGENTS.md + templates/CLAUDE.md + templates/PULL_REQUEST_TEMPLATE.md filled; 4 ISSUE_TEMPLATE files remaining)
- **Batch P3** (PENDING; 3 prompts — greenfield + retrofit + upgrade)
- **Release polish + v3.0.0 tag** (PENDING; final README polish + v3.0.0 git tag)

**Amended remaining-work batch sequence** (effective post-ADR-008):

1. Batch P2 ISSUE_TEMPLATEs split across two cycles (TASK-0043 + TASK-0044) per per-cycle defect surface narrowing — choice between project-initiation + feature vs alternative pairings deferred to TASK-0043 scoping
2. Batch P3 prompts (TASK-0045)
3. Part C.2 operating-discipline canonical surfaces (TASK-0046)
4. Release polish + v3.0.0 tag (TASK-0047 or per actual cycle-count)

Total ~5 substantive cycles to v3.0.0 ship post-ADR-008. Cycle-count expectation is not pre-committed (anti-fragile to PMN/discipline insertion drift per ADR-006 Decision 3 framework + ADR-007 D4 sub-shape A discipline).

**Amended at v2.41 per TASK-0045**: pre-Batch-P3 canonical-stabilization mini-cycle insertions at position 0 of the remaining-work batch sequence are authorized when cross-cycle empirical evidence at ADR-006 D3 3+ threshold supports targeted canonical-discipline-prevention-text canonicalization. Such mini-cycles must have strict scope (single canonical-law amendment class), explicit anti-scope (no substantive batch work; no full PMN-triage), and bounded envelope per `core.md` §23.6.1.1 (e.1) anticipation. Cumulative ADR-008 D2 batch sequence integrity preserved post-mini-cycle.

### Decision 3 — Release-surface semantics for deferred stubs

Stub files at canonical-package locations remain at v3.0.0 release (not excluded from distribution). Semantic distinction at canonical level introduced via stub YAML frontmatter:

- `roadmap_status: v3.0-required` — default for v3.0-required stubs (filled stubs + unfilled stubs in v3.0 minimum scope). Field absence indicates `v3.0-required` default; explicit field optional. Adopters reading frontmatter without `roadmap_status` interpret as v3.0-required-default.
- `roadmap_status: v3.1-planned` — deferred to v3.1 minor release post-v3.0.0 ship (Batch P4 Actions; 9 canonical scaffold workflows).
- `roadmap_status: v3.2-planned` — deferred to v3.2 minor release post-v3.1 ship (Batches P5 + P6 + P7; 7 flat appendices + 5 project-type appendices + 7 receiving-surface adapter packs = 19 stubs).

Stub frontmatter gains optional `roadmap_status` field with values `v3.1-planned` and `v3.2-planned` for deferred stubs. Field absence indicates `v3.0-required` default (applied to all v3.0-required stubs, whether filled or unfilled). Adopters reading v3.0.0 see explicit `roadmap_status: v3.1-planned` / `v3.2-planned` annotation at 28 deferred-stub frontmatter surfaces + 28 corresponding README package-layout row annotations. Field-absence-default semantic documented at this Decision body language; avoids retrofitting filled + v3.0-required-unfilled stubs (24 stubs) with redundant `roadmap_status: v3.0-required` field while preserving canonical-form interpretability.

`filled_by` field semantics at deferred stubs revised: deferred-stub `filled_by` points at ADR-008 + roadmap planning reference (e.g., `Batch P4 (ADR-008); v3.1 release`) rather than the prior `Batch P[X] (ADR-006); pending content-fill cycle` form. Update applied per Decision 5 distributed-update discipline.

### Decision 4 — v3.1+ phased roadmap

- **v3.1 = Batch P4 Actions** (deterministic-enforcement automation layer). 9 canonical scaffold workflows materialize at v3.1 minor release post-v3.0.0 ship: `branch-name-check.yml` + `pr-template-check.yml` + `linked-records-check.yml` + `ai-session-log-check.yml` + `review-freshness-check.yml` + `surface-version-sync-check.yml` + `artifact-path-check.yml` + `claimed-action-verification.yml` + `mcp-config-validation.yml`. Adopter benefit: opt-in automated discipline enforcement via CI/CD; v3.0 adopters operate canonical disciplines at human + AI-receiving-surface level without deterministic-enforcement gate.

- **v3.2 = Batches P5 + P6 + P7** (documentation / reference / adapter layer). 19 stubs materialize at v3.2 minor release post-v3.1 ship: 7 flat appendices (mcp-integration + documentation-mcp-options + tool-capability-model + vendor-surface-guidance + github-review-automation + amas-vs-other-frameworks + regulated-tier-extension) + 5 project-type appendices (api-app + research-methodology + code-reports-data-analysis + documents-only + mixed) + 7 receiving-surface adapter packs (claude-code + codex + chatgpt + cursor + gemini + copilot + human-maintainer). Adopter benefit: comprehensive reference documentation + project-type-specific adoption guides + role-specific receiving-surface configurations.

Rationale for phasing across v3.1 vs v3.2 rather than single v3.1 layer:

- P4 Actions are operationally distinct from P5-P7 documentation surfaces (enforcement-automation layer vs documentation/reference/adapter layer). Phased shipping allows adopters to opt-in to enforcement automation independently of comprehensive reference docs.
- P5-P7 benefit from pilot-feedback informing content. Greenfield + retrofit pilot evidence accumulating post-v3.0.0 ship + v3.1 ship informs P5-P7 content depth at v3.2 authoring (e.g., adapter pack canonical surfaces at receiving-surface adapter packs benefit from observed pre-canonical adapter behavior).
- Owner-side cycle bandwidth: v3.1 + v3.2 phased ship reduces single-release-cycle authoring load.

### Decision 5 — Framework positioning rewording at distributed surfaces

Distributed-update discipline per ADR-006 D4 + Item 14 retroactive-supersession-marking sub-rule applies at ADR-008 ship. README + AGENTS.md + CLAUDE.md primary-positioning text updated to reflect v3.0 minimum-viable + v3.1+ phased roadmap framing.

- **README primary positioning** (top-of-file framing + Roadmap paragraph): v3.0 ships canonical disciplines + materialized templates + project-kickoff prompts; deterministic-enforcement automation at v3.1; comprehensive reference + adapter packs at v3.2. Remove "9 deterministic enforcement Actions" from primary positioning (move to v3.1 roadmap section). README L30 Roadmap paragraph amended per ADR-006 D4 distributed-update discipline + ADR-007 §Consequences single-paragraph-update precedent: new sequence reflects amended batch ordering at v3.0 + v3.1 + v3.2 phased boundaries.
- **README package-layout tables**: row-level `[v3.1-planned]` / `[v3.2-planned]` annotation in existing `filled_by` column at 28 deferred-stub rows. Annotation form preserves table structural shape (no new column added) while making v3.0-vs-v3.1-vs-v3.2 distinction visible at adopter-readable scan.
- **AGENTS.md + CLAUDE.md positioning addition**: brief positioning addition near top of file referencing v3.0 minimum-viable framework + v3.1+ enhancement roadmap. Preserves existing operational content per Adj 5 ratification — positioning is supplemental framing, not operational-content rewrite.

## Alternatives considered

### (A) ADR-003 Decision 1 reaffirmation (no amendment)

Rejected. Honors prior theoretical reasoning at ADR-003 D1 but contradicts operational evidence at PMN-012 empirical pilot + TASK-0040/0041 cycle empirical load + cross-Architect pilot record. Reaffirmation would commit to ~17-24 additional substantive cycles at empirically-observed load (P2 ISSUE_TEMPLATEs split + P3 + P4 Actions + P5-P7 documentation/reference/adapter + Part C.2 + release polish), whereas amendment ships v3.0 in ~5 cycles + defers v3.1+ to post-ship pilot-validation cycle. Reaffirmation also continues the staleness-defect-class pattern ADR-006 was authored to mitigate (ADR-003 D2 PR plan falsified at 26-cycle horizon; ADR-003 D1 ship-scope-criterion approaches similar falsification trajectory at sustained empirical load).

### (B) Exclude P4-P8 stub files from v3.0 release distribution

Rejected. Operationally complex — release-tag scope-narrowing requires git-level surgery (separate branch / cherry-pick or release-tooling configuration) at every v3.0.x patch release. Loses canonical reference at v3.0 ship — adopters cloning v3.0.0 tagged release would not see P4-P8 file canonical locations, weakening forward-reference traversal at v3.1 + v3.2 upgrade cycles. Decision 3 `roadmap_status` semantic distinction achieves same adopter-clarity benefit (explicit "roadmap, not incomplete" framing) at lower operational cost — single frontmatter field at 28 stubs + README annotation rather than release-tooling reconfiguration.

### (C) All P4-P8 at v3.1 (no v3.1 vs v3.2 phased split)

Considered. Defensible: single post-v3.0.0 release ships full deferred-stub set; adopters at v3.1 gain both automation + comprehensive docs simultaneously. Rejected at Decision 4 in favor of phased split for two reasons:

- **Domain distinction**: P4 Actions are enforcement-automation layer (CI/CD scaffold); P5-P7 are documentation/reference/adapter layer (markdown content). Phased shipping allows adopters to opt-in to enforcement-automation independently of documentation; an adopter wanting Actions-deterministic-enforcement at v3.1 ship doesn't need to wait for documentation/reference completion.
- **Pilot-feedback informing content**: P5-P7 content (especially receiving-surface adapter packs + project-type appendices) benefits materially from observed adoption pilots post-v3.0.0 + v3.1 ship. Phased timing allows pilot evidence to inform v3.2 content depth rather than v3.2 content being authored from purely-theoretical reasoning.

Owner override at TASK-0042+ scoping if alternative (C) preferred. Recommendation at this ADR: phased split per Decision 4.

### (D) Further re-scoping (e.g., defer Part C.2 + Batch P3 to v3.1)

Rejected. PMN-012 pilot evidence validates Part C.2 (substrate qualifier cleanup = adopter-readability) + Batch P3 prompts (project-kickoff surfaces) as adopter-readiness-relevant at v3.0 ship. Further re-scoping below current Decision 2 minimum scope would weaken adopter-readiness justification — adopters at v3.0.0 ship would encounter substrate-fallback qualifier residue at canonical-law trio + Batch P1 templates without Part C.2 ship (validates PMN-012 F1 friction class) + lack project-kickoff prompts at greenfield/retrofit/upgrade adoption (validates ADR-007 D2 dependency-grounding reasoning). Current Decision 2 minimum scope represents the empirically-grounded floor at PMN-012 + TASK-0040/0041 evidence.

## Consequences

- **ADR-003 Decision 1 partially superseded** at v3.0 ship-scope-criterion portion only. Decision 2 PR plan portion (already partially superseded at ADR-006 D2 + ADR-007 D2) further-partially-superseded at remaining-batch portion per ADR-008 D2. Decision 3 (TASK reservation extension + PMN insertion budget pattern) preserved unchanged. ADR-003 §Status field unchanged per amendment convention (predecessor ADR status fields preserved at amendment ship per `templates/ADR-template.md` ADR edit discipline + usage-guide §10.11 partial-supersession-marker convention applied at the new ADR's `amends` frontmatter field rather than predecessor §Status field).

- **ADR-006 Decisions 1 + 2 partially superseded** at v3.0 ship-scope-criterion portion + remaining-work batch sequence portion only. Decisions 3 (lightweight-absorption framework) + 4 (distributed-update discipline + Item 14 retroactive-supersession-marking sub-rule) preserved unchanged. ADR-006 §Status field unchanged per amendment convention.

- **ADR-007 Decisions 1 + 2 + 3 + 4 preserved unchanged**. Part C.2-before-P4 Actions ordering canonical at amended scope; Part C.2 stays in v3.0 scope per ADR-007 D3 adopter-readability rationale; P4 Actions move to v3.1 per ADR-008 D2 + D4. ADR-007 §Status field unchanged.

- **README package-layout tables updated** per Decision 3 + Decision 5 implementation form: row-level `[v3.1-planned]` / `[v3.2-planned]` annotation in existing `filled_by` column at 28 deferred-stub rows (9 Actions + 7 flat appendices + 5 project-type appendices + 7 receiving-surface adapters). `filled_by` semantics revised at deferred-stub rows to reference ADR-008 + roadmap planning boundary (e.g., `Batch P4 (ADR-008); v3.1 release` replacing prior `Batch P4 (ADR-006); pending content-fill cycle`).

- **Stub YAML frontmatter updated** per Decision 3 implementation form at 28 deferred stubs: `roadmap_status: v3.1-planned` at 9 Actions stubs; `roadmap_status: v3.2-planned` at 7 flat appendices + 5 project-type appendices + 7 receiving-surface adapter packs. Field addition consistent with existing `template_version` / `status` / `filled_by` frontmatter form per `templates/ADR-template.md` ADR-style canonical-form extension precedent. Actions stubs use YAML-comment-form frontmatter per `.yml` workflow file canonical (`# roadmap_status: v3.1-planned`); markdown stubs use standard YAML-delimiter form. Receiving-surface adapter packs use extended-frontmatter form (`adapter_pack` + `amas_version` + `last_validated_on` + `vendor_doc_urls` + `last_breaking_change_observed` + `status` + `filled_by` + new `roadmap_status`); field placement after `status` per canonical-form ordering.

- **AGENTS.md + CLAUDE.md positioning** updated per Decision 5: brief addition near top of file referencing v3.0 minimum-viable + v3.1 + v3.2 phased roadmap. Existing operational content preserved.

- **README primary positioning + L30 Roadmap paragraph updated** per Decision 5: top-of-file framing reflects v3.0 minimum-viable framework + v3.1 enforcement-automation + v3.2 documentation/reference/adapter roadmap. L30 Roadmap paragraph amended to enumerate amended remaining-work batch sequence (Batch P2 ISSUE_TEMPLATEs split → P3 prompts → Part C.2 → v3.0.0 release) + v3.1 + v3.2 roadmap announcement.

- **Effective post-ADR-008 batch sequence to v3.0.0 ship**: Batch P2 ISSUE_TEMPLATEs split (TASK-0043 + TASK-0044 per per-cycle defect surface narrowing rationale at cross-Architect critique pilot Adj at TASK-0042 scoping) → Batch P3 prompts (TASK-0045) → Part C.2 operating-discipline canonical (TASK-0046) → release polish + v3.0.0 tag (TASK-0047 or per actual cycle-count). Total ~5 cycles to v3.0.0 ship post-ADR-008.

- **Cross-Architect critique pilot empirical record**: TASK-0042 ADR-008 cycle is pilot empirical reach extension (third Phase 1 scoping cycle with cross-Architect critique applied; cross-cycle reach 3 of distinct primary-Architect framing-gap catches). Canonicalization-promotion candidacy at `core.md` §24.5 Surface 0 extension if pattern persists at TASK-0043+ Phase 1 scoping cycles per ADR-006 D3 evidence-bar discipline (3+ confirmations within same class). Promotion adjudication deferred to post-v3.0.0 per PMN-013 §6.x carry-forward framework.

- **Adopters of pre-v3.0.0 amas-framework** see ADR-008 alongside ADR-003 + ADR-006 + ADR-007 as current canonical scope reference. ADR-003 + ADR-006 §Status fields unchanged per amendment convention; ADR-007 §Status field unchanged. ADR-008 §Status field carries authoritative amendment scope per `amends` frontmatter field + §Status body framing. Adopters reading the repo at any HEAD post-ADR-008 see the four-ADR chain (ADR-003 / ADR-006 / ADR-007 / ADR-008) as canonical scope-and-sequence reference.

- **UPCDS adoption of amas-framework v3.0.0** unaffected by this ADR per ADR-003 §Consequences UPCDS-side-ADR convention (preserved through ADR-006 + ADR-007 + ADR-008). UPCDS-side adoption ADR will reference ADR-008 alongside ADR-003 + ADR-006 + ADR-007 at UPCDS-repo authoring cycle.

- **v3.1 + v3.2 roadmap forward-reference**: ADR-008 is the canonical scope-and-sequence reference for v3.1 + v3.2 phased ship at post-v3.0.0 horizon. Future v3.1-shipping ADR (anticipated post-v3.0.0 release ship cycle) will reference ADR-008 D4 v3.1 = Batch P4 Actions framing; future v3.2-shipping ADR will reference ADR-008 D4 v3.2 = Batches P5 + P6 + P7 framing. Each future ship-cycle ADR adopts the partial-supersession-via-amendment pattern at orthogonal scope axis (release-version-boundary rather than batch-sequence-insertion) consistent with ADR-008 precedent.

## Cross-references

- **ADR-001** decisions 1-7, 9-15 unchanged; decision 8 PR sequence portion previously superseded by ADR-003 D2 portion (preserved). ADR-001 §Status field unchanged per amendment convention.
- **ADR-002** Decision 3 anticipation pattern; ADR-002 §Status field unchanged per amendment convention.
- **ADR-003** Decision 1 partially superseded by this ADR at v3.0 ship-scope-criterion portion; Decision 2 PR plan portion (already partially superseded at ADR-006 + ADR-007) further-partially-superseded at remaining-batch portion; Decision 3 preserved.
- **ADR-004** linked-pr-fix-up Action operational + preserved through ADR-006 + ADR-007 + ADR-008.
- **ADR-005** branch convention canonicalization + partial-supersession-via-deliberate-divergence precedent; ADR-008 follows same partial-supersession-via-amendment pattern.
- **ADR-006** Decisions 1 + 2 partially superseded by this ADR; Decisions 3 (lightweight-absorption framework) + 4 (distributed-update discipline + Item 14 retroactive-supersession-marking sub-rule) preserved.
- **ADR-007** Decisions 1 + 2 + 3 + 4 preserved unchanged; Part C scoping + Part C.2-before-P4 Actions ordering canonical at amended scope.
- **PMN-012** at `docs/post-merge-notes/PMN-012-pr-50-cycle-learnings.md` — first AMAS adoption pilot empirical evidence (retrofit mode; canonical-law trio + Batch P1 surface; F1 packaging-qualifier-instance ambiguity friction observation).
- **PMN-017** at `docs/post-merge-notes/PMN-017-pr-64-task-0040-cycle-close-pass-4-clean-documentary.md` — TASK-0041 cycle-close pass-4 CLEAN documentary + (XXIV.d) cycle-close completeness narrowness observation; informs cycle-load empirical evidence at ADR-008 §Context.
- **TASK-0040 handoff** at `docs/handoffs/TASK-0040-batch-p2-agents-claude-templates.md` — Batch P2 first cycle empirical record.
- **TASK-0041 handoff** at `docs/handoffs/TASK-0041-batch-p2-pull-request-template.md` — predecessor cycle empirical load record + cross-Architect critique pilot record at TASK-0041 scoping + §24.6 reach 4+ canonical boundary engagement empirical record.
- **TASK-0042 (this PR)** — first cycle executing ADR-008 ship; ADR-008 substantive authoring co-shipped with §18.3 M-A7 28th-instance amendment + Class A v-bump v2.37 → v2.38 minor + multi-surface positioning rewording + 28 deferred-stub `roadmap_status` field addition + README package-layout row annotation distributed-update.
- **`templates/ADR-template.md`** canonical 7-field frontmatter form + 6-section body structure; ADR-008 follows post-canonicalization vintage form parallel to ADR-007.
- **`core.md` §17 / §17.5** ADR templates + lifecycle conventions; §18.3 M-A7 promotion pattern; §18.4 Class A v-bump tier criteria; §23.6 Architect-side self-review disciplines applied at ADR-008 authoring; §24.5 multi-surface review pipeline + §24.6 Stop-Iteration framework applied at ADR-008 cycle.
- **`github-reference.md` §2.2** branch convention per ADR-005 (Option B `<type>/task-####-<kebab-slug>`); ADR-008 cycle branch `feat/task-0042-adr-008-v3-scope-amendment` conformant.
- **AMAS v2.14.1 substrate** — operational-discipline substrate referenced by ADR-007 Decision 2 Part C.2 forward-references (§8.2 + §8.3 + §13 + §10.5); ADR-008 D2 preserves Part C.2 ship in v3.0 scope per ADR-007 dependency-grounding rationale.
