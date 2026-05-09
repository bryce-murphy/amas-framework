---
template_version: 3.0.0
status: filled
filled_by: PR-43 (TASK-0031)
---

# ADR template

This template canonicalizes the form for Architectural Decision Record (ADR) files per ADR-001 through ADR-007 observable patterns + usage-guide.md "ADR edit discipline" bullet + §10.10 / §10.11 friction-pattern conventions. ADR files document substantive direction-decisions warranting durable rationale capture per ADR-005 substantive-direction-decision precedent.

## Frontmatter (canonical 7-field form per ADR-006 + ADR-007)

```yaml
---
adr_id: ADR-NNN
title: <title; may include partial-supersession ref if amending predecessor (e.g., "Part C materialization scoping decision — amends ADR-006 D2 batch sequence")>
status: Accepted | Proposed | Superseded | Deprecated
date: YYYY-MM-DD
amends: <predecessor ADR partial-supersession ref> | none
supersedes: <predecessor ADR full-supersession ref> | none
superseded_by: <successor ADR ref> | none
---
```

Status field values + partial-supersession qualifier:
- `Proposed`: under deliberation; not yet ratified.
- `Accepted`: ratified; in force.
- `Superseded`: fully superseded by successor ADR; `superseded_by` field populated.
- `Deprecated`: no longer in force without successor.
- Partial-supersession qualifier: `Status: Accepted; partially superseded by ADR-NNN (<scope>)` per usage-guide §10.11 convention. Use when a successor ADR invalidates one section of the older ADR while leaving the rest in effect.

## Body section structure

Canonical body section sequence per ADR-001 through ADR-007 observable patterns:

- **`## Status`** (between H1 and Context): `Accepted — YYYY-MM-DD` (or other status) plus framing of amendment scope, partial-supersession scope, and historical amendment record (e.g., "Amended YYYY-MM-DD by ADR-NNN (<scope>)").
- **`## Context`**: substantive framing of the situation motivating the decision — empirical state of the system at decision authoring; problem definition; constraint enumeration; alternatives explored; precedent cycles or precedent ADRs.
- **`## Decision N`** (numbered Decisions; usually multiple — D1 through DN): each Decision states one canonical claim; numbered to support cross-ADR partial-supersession reference (e.g., "ADR-006 D2 partial-supersession" cites Decision 2 specifically).
- **`## Alternatives considered`**: explicit enumeration of rejected alternatives with rationale for rejection — preserves the fact that the decision was deliberate (vs default by omission); supports future-cycle revisitation if context changes.
- **`## Consequences`**: forward-projected effects of the decision on subsequent cycles + adopter-side implications + distributed-update discipline activations (e.g., ADR-003 §Consequences + ADR-006 D4 + Item 14 retroactive-supersession-marking sub-rule).
- **`## Cross-references`**: explicit listing of cross-referenced ADRs (predecessor, sibling, successor), PMNs, core.md §-citations, transition plan v0.2 references, FEAT references.

H1 heading: `# ADR-NNN — <title>` matching `title` frontmatter field.

## ADR edit discipline

Accepted ADRs are not edited in place per usage-guide.md "ADR edit discipline" bullet + §10.10 friction-pattern. Supersede with a new ADR; update the old ADR's `Status` field to `Superseded` (or partial-supersession qualifier) and leave Context / Decision / Alternatives sections unchanged. The narrow exception is typographical corrections — broken links, misspelled names, formatting — anything that doesn't change the decision content.

For partial supersession: `Status: Accepted; partially superseded by ADR-NNN (<scope>)` per §10.11 convention. The new ADR's `amends` frontmatter field references the partially-superseded predecessor.

## Path conventions

`docs/adr/ADR-NNN-<kebab-slug>.md`. `<kebab-slug>` is concise descriptive slug capturing the ADR's primary decision (e.g., `ADR-006-product-delivery-pivot-pr-plan-amendment.md`, `ADR-007-part-c-materialization-scoping.md`). ADR-NNN counter is monotonically incremented across cycles; the highest existing ADR-NNN across any artifact in the repo is authoritative for the next-cycle counter assignment.

## Authoring surface

Substantive direction-decisions warrant ADR adjudication per ADR-005 precedent (substantive direction-decisions of this scope warrant ADR per partial-supersession-via-deliberate-divergence precedent). Informal direction would not durably document the rationale or amendment scope; future-cycle Architects (or external adopters) reading the repo would encounter the predecessor ADR as canonical without amendment marker.

## Cross-references

ADR-001 D11 (owner-invokes Codex review convention; ADR convention surface); ADR-002 amendment pattern (ADR-002 Decision 3 anticipation pattern → ADR-003 amendment precedent); ADR-005 (substantive-direction-decision precedent); ADR-006 D4 (distributed-update discipline + Item 14 retroactive-supersession-marking sub-rule); usage-guide.md "ADR edit discipline" bullet + §10.10 / §10.11 friction-pattern; `core.md` §17 (Templates parent frame; mechanism-not-policy framing); `core.md` §17.5 (template lifecycle).
