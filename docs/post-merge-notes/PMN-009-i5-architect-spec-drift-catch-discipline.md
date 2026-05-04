---
post_merge_note_id: PMN-009
title: (i.5) Architect-spec-drift catch discipline canonicalization-candidate
linked_pr: PR-25 (Builder fills with squash SHA post-merge per PMN-001 (k))
framework_version_dogfooded: AMAS v2.18.1
status: drafted
---

# PMN-009 — (i.5) Architect-spec-drift catch discipline canonicalization-candidate

## Status

Drafted — 2026-05-04

PMN-009 inserts under ADR-003 Decision 3 contingency budget (slot accounting reconciliation deferred per cycle-close ledger Item 1; spec accounting consumes one slot in TASK-0021 scoping). Status flips to Recorded post-merge per PMN-001 (k) Linked PR fix-up substitution + status flip convention.

## §1. Cycle context

PMN-009 documents an Architect-spec-authoring-drift catch discipline that has empirically operated at the Builder pre-flight (i.5) batch surface across the TASK-0019 + TASK-0020 cycles. The (i.5) sub-shape was canonicalized at PMN-008 §4.2 with the PMN-file-shape sub-extension; PMN-007 originated the (i.5) registration as part of the cross-document state verification (i) discipline cluster. Across the two cycles since (i.5) canonicalization, the discipline has caught Architect-spec-authoring drift at four distinct sub-shapes — frontmatter convention, structural-element count, line-number references, and form/section structure — at the Builder pre-flight surface before Builder execution.

This PMN documents the field evidence + proposes canonical refinement for absorption at a subsequent cycle (TASK-0022+) per PMN-005 propose-then-absorb cadence. The proposed refinement adds a §23.6 sub-rule for Architect-side reference-verification before spec authoring, distributing some of the catch surface forward into Architect-side discipline rather than relying solely on the reactive Builder pre-flight catch.

Authoring task: TASK-0021 / PR-25. Framework version dogfooded: AMAS v2.18.1 → v2.19 minor-bump at this cycle's ship per §18.4 substantive-reading minor criterion (new canonical text at core.md §8.1.1.1 + new PMN; clear minor tier).

### §1.1. Honesty record

Four cross-cycle field-evidence data points across the TASK-0019 + TASK-0020 cycles. The same root-cause class — Architect spec-authoring references specific values without verifying against actual canonical sources at authoring time — manifests at four distinct sub-shapes. All four caught operationally before they corrupted Builder execution; the discipline operated as designed.

1. **TASK-0019 frontmatter expansion catch (Builder pre-flight (i.5) batch)** — Architect-side spec authoring of TASK-0019 spec frontmatter used a 2-field form (older convention). Canonical PMN-007 HEAD form is 12-field (`task_id`, `title`, `pr`, `branch`, `linked_predecessor`, `linked_successor`, `linked_pr`, `framework_version_dogfooded`, `production_target`, `spec_source`, `date_authored`, `status`). Caught by Builder pre-flight (i.5) batch sample-read of prior TASK handoff frontmatter (TASK-0017 / TASK-0018); surfaced at step-1 stop-and-show; Architect adjudicated path-(a) revise; canonical 12-field form restored. Sub-shape A (frontmatter convention divergence).

2. **TASK-0020 step-1 ADR-004 §Consequences point-count off-by-one (Builder pre-flight (i.5) batch)** — TASK-0020 spec §3 step 6 instructed Builder to append the (h.4)-related decision as ADR-004 §Consequences point 7. Actual ADR-004 at HEAD had 7 existing points (post-TASK-0019 ship state); the correct append was point 8, not point 7. Caught by Builder pre-flight (i.5) batch sample-read of `docs/adr/ADR-004-pre-actions-batch-action-insertion.md` current state; surfaced at step-1 stop-and-show; Architect adjudicated path-(a) revise; spec amended to "append as point 8". Sub-shape B (structural-element count off-by-one).

3. **TASK-0020 line-number off-by-one in code references (Builder pre-flight + Codex pre-commit catches; two sub-instances)** — Sub-shape C surfaced at TASK-0020 across two distinct file references, both line-number off-by-one. **(3a)** `.github/scripts/linked-pr-fix-up.py` regex newline-consumption fix: TASK-0020 spec §3 step 4 named lines 36 + 93 for the regex fix; actual file at HEAD had the regex pattern at line 35 + line 93 (line 36 is the `re.MULTILINE,` argument continuation on the next physical line of the pattern function call, not the regex literal itself). Caught by Builder pre-flight (i.5) batch sample-read of `linked-pr-fix-up.py` current state; surfaced at step-1 stop-and-show; Architect adjudicated path-(a) revise; spec amended to "lines 35 + 93". **(3b)** `.github/workflows/linked-pr-fix-up.yml` permission-line reference embedded in ADR-004 amendment text: ADR-004 amendment point 8 referenced workflow `permissions: pull-requests: write` at line 23; actual file had `permissions: pull-requests: write` at line 24 (line 23 is `contents: write`). Caught by Codex pre-commit pass on the TASK-0020 working tree, NOT by Builder pre-flight (i.5) batch (which sampled the .py file directly but not the .yml line-number reference embedded inside the ADR-004 amendment text); routed path-(a) revise. Sub-shape C (line-number off-by-one in code references; two distinct file targets across two distinct catch surfaces — Builder pre-flight for (3a), Codex pre-commit for (3b)).

4. **TASK-0019 ADR-004 form / section-structure divergence catch (Builder pre-flight (i.5) batch)** — TASK-0019 spec prescribed ADR-004 with section structure Status / Context / Decision / Rationale / Consequences / References. Canonical priors form across ADR-001 + ADR-002 + ADR-003 was Status / Context / Decision / Alternatives considered / Consequences / Evidence / References (different section ordering and section-name form). Caught by Builder pre-flight (i.5) batch sample-read of canonical priors form across the ADR-001/002/003 cluster at step-1 stop-and-show; Architect adjudicated path-(a) revise; spec amended to canonical priors form. Sub-shape D (section-structure / form divergence).

The framework operated as designed across all four data points: each defect was caught at a Builder-side or Codex-side surface before it corrupted execution. The Architect failure mode was consistent: spec authoring referenced specific values (line numbers, structural-element counts, convention shapes, form structures) without verifying those values against the actual canonical sources at authoring time.

## §2. Sub-shape characterization

The four field-evidence data points decompose into four distinct sub-shapes of the same root-cause class. Each sub-shape is characterized by what kind of value the spec references, where the canonical source lives, and which catch surface is structurally aligned to detect the drift.

- **Sub-shape A — frontmatter convention divergence.** Architect references frontmatter shape (field set, field ordering, field naming) in the spec; the canonical convention has evolved across cycles; the spec-authored shape diverges from current canonical. Catch surface: Builder pre-flight (i.5) batch sample-read of prior cycle's handoff or PMN frontmatter against the spec's frontmatter prescription.

- **Sub-shape B — structural-element count off-by-one.** Architect references a count of structural elements (sections, points, items, table rows) in the spec; the actual count in the canonical source differs from the spec-authored count, typically off by one. Catch surface: Builder pre-flight (i.5) batch sample-read of canonical source current state; structurally guaranteed catch when the source exists at HEAD and the Builder reads it before executing the count-dependent step.

- **Sub-shape C — line-number off-by-one in code references.** Architect references specific line numbers for code modifications, regex fixes, or workflow edits; the actual file structure at HEAD differs from the spec-authored line reference, typically off by one (multi-line continuations, blank lines, comment lines confound the count). Catch surface: Builder pre-flight (i.5) batch sample-read of source file OR Codex pre-commit verification (Codex catches the residual when the Builder pre-flight skips the specific file).

- **Sub-shape D — section-structure / form divergence.** Architect prescribes section structure or form for a new artifact (ADR, PMN, handoff, review-context); the spec-prescribed form differs from the canonical priors form established across multiple prior artifacts in the same artifact class. Catch surface: Builder pre-flight (i.5) batch sample-read of canonical priors form. Empirical evidence at §1.1 data point 4 (TASK-0019 ADR-004 form catch).

The four sub-shapes are not mutually exclusive — a single spec may carry drift at multiple sub-shapes simultaneously — but each is characterized by a distinct catch-surface alignment. The pre-flight (i.5) batch is structurally aligned to all four; Codex pre-commit catches Sub-shape C residuals when (i.5) skips the specific file.

## §3. Common root cause

Architect spec authoring references specific values (line numbers, structural-element counts, convention shapes, form structures) without verifying those values against actual canonical sources at authoring time. Architect operates from memory or partial-context at spec authoring (the spec is authored in a Claude.ai Project surface that does not have direct repo read access at the level of granularity that the verification would require); specific values drift relative to the actual repo HEAD state at the moment the Builder receives the spec.

The drift is bounded — Architect's general framing of what the spec should do is correct; only specific reference values drift. The catch surfaces (Builder pre-flight + Codex pre-commit) are well-aligned to detect the drift. The framework's multi-surface mitigation per PMN-006 §1.1 / §3.2 framing applies cleanly: catch-surface-A (Builder pre-flight) catches what Architect-surface (spec authoring) misses; catch-surface-B (Codex pre-commit) catches what Builder pre-flight misses.

## §4. Catch-surface analysis

The Builder pre-flight (i.5) batch is the primary structural catch surface. The (i.5) sub-shape was canonicalized at PMN-008 §4.2 specifically to verify convention-inference + canonical-priors-form discipline at the Builder receiving-side surface. Across the two cycles since (i.5) canonicalization, the discipline has caught Architect-spec-authoring drift at all four §1.1 data points before Builder execution: data points 1, 2, and 4 caught entirely at Builder pre-flight; data point 3 caught at two surfaces (Builder pre-flight for sub-instance 3a; Codex pre-commit for sub-instance 3b — the Codex secondary catch addressed an embedded line-number reference inside spec-amendment text that the Builder (i.5) batch's file-targeted sample reads did not cover).

The discipline is working as designed across four cross-cycle confirmations. The catch surface is structurally aligned to the drift class; the Builder is operationally applying the (i.5) batch consistently; the Architect is consistently producing drift bounded to specific reference values. Multi-surface mitigation is load-bearing in the same shape PMN-006 §1.1 + §3.2 framed it for verification-command operational correctness.

The remaining question is whether to leave the discipline at its current reactive shape (Builder pre-flight catches Architect drift after-the-fact) or to extend the discipline forward into Architect-side reference-verification before spec authoring (Architect verifies specific values at authoring time, distributing the catch surface forward). §5 below proposes the latter as a §23.6 sub-rule addition.

## §5. Recommended canonical refinement

The proposed refinement is a §23.6 sub-rule addition for Architect-side reference-verification before spec authoring. The rule articulates two operational paths — verify specific values, OR explicitly defer verification to Builder pre-flight — without prescribing which path is preferred for which sub-shape. The default-path guidance below distributes the recommendation by sub-shape.

> **§23.6 sub-rule (g) — Architect-side reference-verification before spec authoring.** Before authoring spec content that references specific values (line numbers, structural-element counts, convention shapes, form structures), Architect either: (i) samples actual canonical sources to verify the referenced value, OR (ii) explicitly defers verification to Builder pre-flight (i.5) batch by marking the value as "Builder verifies at pre-flight" rather than committing to a specific value. The latter is the recommended default for line-number references and structural-element counts (sub-shapes B and C above; specific values that drift between authoring time and execution time even within a single cycle, particularly when intervening commits land on main between Architect spec authoring and Builder execution); the former is the recommended default for convention shapes and form structures (sub-shapes A and D above; values that the Architect should have direct access to via prior-artifact memory and that constrain the structural correctness of what the spec produces).

Canonical absorption of this proposed sub-rule is **deferred to TASK-0022+** per PMN-005 propose-then-absorb cadence. PMN-009 documents the field evidence and articulates the proposed refinement; the subsequent cycle absorbs the sub-rule into core.md §23.6 canonical text after additional cross-cycle field evidence has matured. This is consistent with PMN-005's empirical demonstration that PMN-proposed refinements benefit from one or more additional cycles of evidence before canonical absorption (gives the framework's multi-surface review pipeline a chance to surface refinements to the proposed wording itself before it canonicalizes).

## §6. Anticipated forward integration

TASK-0022+ specs apply the (i.5)-extended reference-verification discipline pre-emptively at Architect-side spec authoring per the proposed §5 sub-rule (assuming canonical absorption lands at the next subsequent cycle). Empirical evidence at TASK-0022 / TASK-0023 / TASK-0024 cycles informs:

- Whether the canonical absorption reduces (i.5) Builder pre-flight catch-surface findings (positive direction = Architect-side discipline working preventively, not just reactively at the Builder surface).
- Whether the "Builder verifies at pre-flight" deferral path is cleanly applied at sub-shapes B/C without producing ambiguity at the spec interpretation surface (negative direction = the deferral path itself produces a new sub-shape of Architect-spec-authoring drift, requiring further refinement).
- Whether sub-shape D (form/structure divergence) reduces specifically (positive direction = Architect prior-artifact-form sampling at authoring time addresses the structural-form drift class).

If the canonical absorption lands cleanly across 2-3 subsequent cycles with reduced (i.5) catch-surface findings, the discipline matures from preliminary canonical refinement to standing §23.6 sub-rule. If the catch-surface findings persist or shift sub-shape, PMN-N+1 (a subsequent PMN) records the observation and proposes further refinement.

## §7. Cross-references

- **PMN-008** (`docs/post-merge-notes/PMN-008-pr-17-cycle-learnings.md`): §4.2 (i.5) convention-inference verification with PMN-file-shape sub-extension canonicalization; analog cross-cycle empirical pattern at the (h.4) Codex-output-endpoint-coverage discipline (which this cycle absorbs into core.md §8.1.1.1 canonical text).
- **PMN-007** (`docs/post-merge-notes/PMN-007-pr-13-cycle-learnings.md`): originated the (i.5) registration as part of the cross-document state verification (i) discipline cluster; HEAD canonical 12-field frontmatter convention.
- **PMN-006** (`docs/post-merge-notes/PMN-006-pr-10-cycle-learnings.md`): §1.1 honesty record + §3.2 (h)/(i) discipline canonicalization for multi-surface-mitigation load-bearing framing; §3.2 (h.2)/(h.3) sub-shapes; §23.6 self-review canonical text origin.
- **PMN-005** (`docs/post-merge-notes/PMN-005-pr-8-cycle-learnings.md`): propose-then-absorb cadence precedent — PMN proposes canonical refinement; subsequent cycle absorbs after additional cross-cycle field evidence matures.
- **TASK-0019 handoff** (`docs/handoffs/TASK-0019-linked-pr-fix-up-action.md`): field evidence cycle for sub-shape A (frontmatter expansion) + sub-shape D (ADR-004 form divergence); pre-flight (i.5) catches at step-1 stop-and-show.
- **TASK-0020 handoff** (`docs/handoffs/TASK-0020-linked-pr-fix-up-defect-fix.md`): field evidence cycle for sub-shapes B (ADR-004 §Consequences point-count) + C (linked-pr-fix-up.py line-number); pre-flight (i.5) catches at step-1 stop-and-show + Codex pre-commit secondary catch for sub-shape C variant (workflow line-number).
- **core.md §23.6 / §23.6.1 / §23.6.2**: target canonical surface for the proposed sub-rule (g) addition; absorption deferred to TASK-0022+.
- **core.md §8.1.1.3**: bounded-continuation rule cost-class refinement; (i.5) operates at single-defect-class catch surface across cycles.
- **PR-21 (TASK-0019 / squash SHA `db3c9b0`)**: data points 1 + 4 — sub-shape A (frontmatter expansion) + sub-shape D (ADR-004 form) catches.
- **PR-23 (TASK-0020 / squash SHA `39b700e`)**: data points 2 + 3 — sub-shape B (ADR-004 §Consequences point-count) + sub-shape C (line-number off-by-one; two sub-instances 3a + 3b) catches.
