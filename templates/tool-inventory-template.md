---
template_version: 3.0.0
status: filled
filled_by: PR-48 (TASK-0033)
---

# Tool inventory template

Canonical template form for AMAS project tool inventories. A tool inventory enumerates the tools available to each project role (Architect / Builder / Reviewer) with access mode + setup state + canonical-source reference, supporting role-bound tool discovery + project-onboarding + role-handoff verification.

## Frontmatter

Filled tool inventories carry 4-field YAML frontmatter:

- `project_id`: canonical project slug matching project-brief project_id (e.g., `amas-framework`); lowercase kebab-case
- `status`: lifecycle state (`active | archived`)
- `filled_by`: PR/TASK reference at content-fill time (`PR-NN (TASK-####)`)
- `framework_version`: AMAS canonical version when authored or last amended

## Body section structure

Filled tool inventories document the following canonical body sequence as actual H2 headings, organized by role-and-surface affinity:

- **Architect tools**: per-tool entries enumerating tools available to the Architect role. Each entry: tool name + access mode + setup state + canonical-source reference + project-specific notes.
- **Builder tools**: per-tool entries enumerating tools available to the Builder role.
- **Reviewer tools**: per-tool entries enumerating tools available to the Reviewer role.
- **Cross-cutting tools**: tools available to multiple roles (e.g., MCP servers; repository GitHub Actions; CI infrastructure). Each entry adds role-binding enumeration.
- **Cross-references**: pointers to related canonical surfaces.

## Per-tool entry form

Each per-tool entry within an H2 section above carries the following fields as bullet sub-list under the tool name (authored as H3 heading or bold):

- **Access mode**: `CLI | MCP | API | web | desktop-app | other`
- **Setup state**: `installed | configured | pending | deprecated`
- **Canonical-source reference**: URL or repo-relative doc-path (e.g., `https://docs.claude.com/...` for Claude products; `.github/workflows/...` for repo Actions; `docs/<path>` for repo-internal docs)
- **Role-binding** (cross-cutting only): enumerate role(s) with access (`Architect | Builder | Reviewer`)
- **Notes**: 1-2 lines for project-specific configuration or constraints

## Path conventions

Filled tool inventories live at `docs/tool-inventory.md` (single canonical file per project; not enumerated). The template at `templates/tool-inventory-template.md` is the canonical form-of-record at framework-package level.

## Authoring surface

Tool inventories are authored at project initiation by the Architect alongside the project brief, ratified by the owner. Tool inventories amend at major-tool-change cycles (e.g., MCP server addition; Codex configuration change; agent platform migration); minor configuration tweaks propagate via inline edits without amendment cycle.

## Cross-references

- `core.md` §17 — templates parent frame
- `core.md` §17.5 — template lifecycle
- `templates/project-brief-template.md` — project brief Tools section (references this template's `docs/tool-inventory.md` instance)
- `templates/role-scorecard-template.md` — role-tool affinity at Role identity body section
- `templates/surfaces-manifest-template.yml` — surfaces manifest schema (paired system-documentation template at Batch P1 sub-batch B.3)
- ADR-006 D2 — Batch P1 process templates batch
