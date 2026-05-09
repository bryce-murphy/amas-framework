---
template_version: 3.0.0
status: filled
filled_by: PR-45 (TASK-0032)
---

# Project brief template

Canonical template form for AMAS Project Briefs. A Project Brief captures project-level scope, role assignments, tool inventory pointer, documentation-MCP mechanism declaration, and receiving-surface posture at project initiation. The Project Brief is the durable project-initiation record; amendments at project-scope-shift cycles (AMAS major-version upgrade; major-tool-change).

## Frontmatter

Filled Project Briefs carry 7-field YAML frontmatter:

- `project_id`: canonical project slug (e.g., `amas-framework`, `upcds`, `employee-churn`); lowercase kebab-case
- `project_type`: AMAS project-type appendix reference (`api-app | research-methodology | code-reports-data-analysis | documents-only | mixed`)
- `status`: lifecycle state (`active | archived`)
- `author`: authoring role + surface
- `date`: authoring date (ISO `YYYY-MM-DD`)
- `framework_version`: AMAS canonical version at project initiation or last amendment
- `doc_mcp_mechanism`: declared documentation-MCP mechanism in short form (e.g., `web-search via native Claude/Codex tools + explicit owner verification`; or `Context7 + <library configurations>`); body §"Project documentation-MCP mechanism" carries full declaration

## Body section structure

Filled Project Briefs document the following canonical body sequence as actual H2 headings:

- **Metadata**: re-list frontmatter fields for human-readable narrative.
- **Project documentation-MCP mechanism** (REQUIRED): full declaration per FEAT-0001 §"Project documentation-MCP mechanism" precedent. Include: chosen mechanism + rationale + citation pattern for retrieved docs (`Source: <library>@<version> — retrieved <YYYY-MM-DD> via <tool-name>`).
- **Project type**: AMAS project-type appendix declaration + project-type-specific scope notes (forthcoming Batch P6 project-type appendices provide per-type guidance).
- **Roles**: enumerate assigned roles with surface affinity (Architect / Builder / Reviewer pairings to specific tools/surfaces). Reference per-role role scorecards at `docs/role-scorecards/<role_id>.md`.
- **Tools**: high-level tool inventory pointer to `docs/tool-inventory.md` (filled per Batch P1 tool-inventory template schema; forthcoming at TASK-0033+).
- **Receiving surfaces**: per-surface posture declaration (`AGENTS.md` / `CLAUDE.md` / `.cursorrules` / etc.) + receiving-surface adapter pack reference (forthcoming Batch P7).
- **Initial scope**: 1-3 paragraphs framing project-initiation scope; subsequent feature scoping happens via Feature Briefs.
- **Cross-references**: pointers to related canonical surfaces.

## Path conventions

Filled Project Briefs live at `docs/project-brief.md` (single canonical file per project; not enumerated). The template at `templates/project-brief-template.md` is the canonical form-of-record at framework-package level.

## Authoring surface

Project Briefs are authored at project initiation by the Architect, ratified by the owner. Project Briefs amend at project-scope-shift cycles. Project Brief authoring may pair with project-kickoff prompts (forthcoming Batch P3: `prompts/greenfield.md` / `prompts/retrofit.md` / `prompts/upgrade.md`).

## Cross-references

- `core.md §17` — templates parent frame
- `core.md §17.5` — template lifecycle
- `templates/role-scorecard-template.md` — role scorecard canonical form
- `templates/feature-brief-template.md` — feature brief canonical form (project scope materializes via feature briefs)
- FEAT-0001 §"Project documentation-MCP mechanism" — doc-MCP mechanism field precedent
- `appendices/mcp-integration.md` (forthcoming Batch P5) — MCP integration appendix
- `appendices/documentation-mcp-options.md` (forthcoming Batch P5) — doc-MCP options appendix
- AMAS project-type appendices (forthcoming Batch P6) — project-type-specific scope guidance
- ADR-006 D2 — Batch P1 process templates batch
- ADR-007 D3 — Part C materialization scoping
