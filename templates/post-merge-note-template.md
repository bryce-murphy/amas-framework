---
template_version: 3.0.0
status: filled
filled_by: PR-43 (TASK-0031)
---

# Post-merge note template

This template canonicalizes the form for post-merge note (PMN) files per `core.md` §18 cycle-close discipline cluster + ADR-006 D3 evidence-bar discipline. PMN files document cycle-close empirical observations meeting promotion threshold per §18.1 PMN-trigger criteria; lightweight observations (single-cycle / refinement / state-correction) absorb at handoff cycle-close ledger per ADR-006 D3 lightweight-absorption-preferred-default framing.

## Frontmatter (canonical 5-field form per PMN-007 HEAD)

```yaml
---
post_merge_note_id: PMN-NNN
title: <title matches H1 heading content after "PMN-NNN — " prefix per (i.5) title↔H1 alignment discipline>
linked_pr: PR-NN (squash SHA <sha>)
framework_version_dogfooded: AMAS vX.YZ [→ vX.YZ+1 if v-bump triggered at originating cycle]
status: drafted | recorded
---
```

Status field lifecycle (per `.github/scripts/linked-pr-fix-up.py` canonical transitions):
- `drafted` (pre-stage; pre-merge) → `recorded` (post-merge per PMN-001 (k) Action substitution).
- Drift from these exact values breaks the linked-pr-fix-up Action's status transition.

`linked_pr` MC-C canonical-regex form: `^PR-(\d+) \(squash SHA [a-f0-9]+\)$` post-substitution; `^PR-(\d+) \(Builder fills with squash SHA post-merge per PMN-001 \(k\)\)$` pre-merge placeholder. Per PMN-007 §3.3 frontmatter-conformance MC-C absorption discipline.

## Body section structure

Canonical body section sequence per PMN-004/005/006/007/008/009/010 observable patterns:

- **`## Status`** (between H1 and §1): `Drafted at TASK-####` (pre-merge) or `Recorded — YYYY-MM-DD` (post-merge), plus framing of canonicalization scope and any cross-cycle deferral notes.
- **`## §1. Cycle context`**: empirical record framing — what cycle(s) this PMN documents, cumulative empirical instance count if applicable, sourcing material enumeration.
  - **`### §1.1. Honesty record`** (sub-section): authoring-time self-application notes, verification batch results, any (i.5) sub-shape A self-instantiation observations, cross-cycle precedent references.
- **`## §2.` through `## §N`**: substantive sections per cycle scope — taxonomy enumeration with lettered sub-classes (a)/(b)/(c)/... per PMN-001/PMN-002/PMN-007/PMN-008 precedent, or sub-shape enumeration per PMN-009/PMN-010 precedent. Each substantive section presents empirical evidence + canonical-text-or-discipline-proposal + cross-cycle pattern observations.
- **`## §N. Cross-references`** (final numbered §): explicit listing of cross-referenced PMNs + ADRs + core.md §-citations + cycle-execution patterns at predecessor cycles.

H1 heading: `# PMN-NNN — <title>` matching `title` frontmatter field per (i.5) title↔H1 alignment discipline.

## Path conventions

`docs/post-merge-notes/PMN-NNN-<kebab-slug>.md`. `<kebab-slug>` is concise descriptive slug capturing the PMN's primary content; convention varies but typically follows the PR's substantive content theme (e.g., `PMN-008-pr-17-cycle-learnings.md`, `PMN-010-reference-verification-sub-shape-enumeration.md`). PMN-NNN counter is monotonically incremented across cycles; the highest existing PMN-NNN across any artifact in the repo is authoritative for the next-cycle counter assignment.

## Authoring surface

Substantive PMN content authors at cycle-close cycles where empirical evidence accumulates to 3+ cross-cycle confirmations within same defect class per ADR-006 D3 evidence-bar discipline AND canonicalization-cost (200-260 source lines + cycle bandwidth) is materially smaller than projected adopter-cost-of-discipline-absent. Lightweight-absorption-preferred-default per ADR-006 D3: cycle-close ledger entries (informational), discipline-anchor 1-3 line additions (canonical text), template body documentation (when authoring a template that formalizes the discipline) all carry candidate observations until evidence-bar reach.

## Cross-references

`core.md` §18 (cycle-close discipline cluster); §18.1 (PMN-trigger criteria — five categories: architecture / workflow / tool-assignment / validation-strategy / unexpected-review-friction); §18.2 (PMN form specification); §18.3 (M-A7 cumulative-instance enumeration); ADR-006 D3 (evidence-bar discipline); ADR-003 D3 (PMN insertion budget reservation extension pattern); PMN-001 (k) (chore-fix-up Action substitution discipline); PMN-007 §3.3 (frontmatter-conformance MC-C absorption discipline); PMN-007 HEAD canonical 5-field frontmatter form (this template's primary precedent).
