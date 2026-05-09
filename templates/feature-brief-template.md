---
template_version: 3.0.0
status: filled
filled_by: PR-45 (TASK-0032)
---

# Feature brief template

Canonical template form for AMAS Feature Briefs. A Feature Brief captures feature-level scope, objective, in-scope/out-of-scope enumeration, acceptance criteria, and durable links for a Feature tracked at FEAT-#### level. Feature Briefs anchor TASK-#### cycles that materialize feature scope; a feature may span multiple TASKs.

## Frontmatter

Filled Feature Briefs carry 8-field YAML frontmatter:

- `feature_id`: canonical FEAT identifier (e.g., `FEAT-0001`); zero-padded 4-digit
- `title`: feature short title
- `status`: lifecycle state (`active | shipped | superseded`)
- `author`: authoring role + surface (e.g., `Architect (Claude Opus 4.7, Claude.ai Project)`)
- `date`: authoring date (ISO `YYYY-MM-DD`)
- `framework_version`: AMAS canonical version when authored
- `related_tasks`: comma-separated TASK-#### references materializing feature scope
- `related_pr`: PR-#### reference at ship; pre-ship may carry `pending` placeholder

## Body section structure

Filled Feature Briefs document the following canonical body sequence as actual H2 headings:

- **Metadata**: re-list frontmatter fields for human-readable narrative (Feature ID + Status + Author + Date + Framework version + Related TASK(s) + Related ADR(s) + Related PR).
- **Project documentation-MCP mechanism** (when applicable): if feature touches doc-retrieval surfaces, declare mechanism per FEAT-0001 §"Project documentation-MCP mechanism" precedent (mechanism + rationale + citation pattern).
- **Objective**: 1-3 paragraphs articulating feature scope and target outcome.
- **In scope**: enumerated items for inclusion in this feature.
- **Out of scope**: enumerated items deferred to other features or future cycles.
- **Acceptance criteria**: enumerated, verifiable criteria that determine ship-readiness.
- **Cross-references**: pointers to related canonical surfaces (ADRs / handoffs / PMNs / canonical-law sections).

## Path conventions

Filled Feature Briefs live at `docs/features/FEAT-####-<short-slug>.md`. Filename pattern: `FEAT-` prefix + zero-padded 4-digit FEAT ID + lowercase kebab-case slug + `.md`.

## Authoring surface

Feature Briefs are authored by the Architect at feature-scoping cycles, ratified by the owner. The Feature Brief is the durable scope record across the feature's TASK chain; updates to scope or status amend the brief in-place.

## Cross-references

- `core.md §17` — templates parent frame
- `core.md §17.5` — template lifecycle
- `templates/handoff-template.md` — universal handoff schema (Linked Feature Brief field per PMN-007 §3.3 12-field handoff frontmatter form)
- ADR-003 D3 — TASK reservation + PMN insertion budget pattern
- FEAT-0001 — canonical Feature Brief instance precedent
- ADR-006 D2 — Batch P1 process templates batch
