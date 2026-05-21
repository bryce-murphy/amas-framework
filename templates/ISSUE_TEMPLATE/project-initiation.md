---
template_version: 3.0.0
status: drafted
filled_by: PR-68 (TASK-0043)
---

# Project initiation Issue template

Canonical-source project-initiation Issue template for AMAS-adopted repositories. At an adopter project, this template materializes as `.github/ISSUE_TEMPLATE/project-initiation.md` (the operational instantiation) — GitHub recognizes templates at `.github/ISSUE_TEMPLATE/` and uses them at Issue-creation surfaces. The canonical-source-vs-operational distinction lives at `github-reference.md` §4.3: operators copy the body sections from this canonical-source form to the operational `.github/ISSUE_TEMPLATE/` instantiation; canonical-source amendments propagate via the same mirror discipline. The 7-section canonical body below is the authoritative form. At operational instantiation, the canonical-source AMAS 3-field frontmatter (template_version + status + filled_by) is replaced by GitHub's legacy-markdown ISSUE_TEMPLATE frontmatter (name + about + labels + assignees per GitHub Docs canonical); opening framing + closing Cross-references may also be stripped per GitHub-recognition hygiene.

## §1. Linked records

- **Project Brief**: <link to ratified Project Brief at `docs/project-brief.md` or equivalent project policy path> (REQUIRED for Issue 0)
- **FEAT**: <FEAT-### if the kickoff has an associated Feature Brief; usually N/A at Issue 0>
- **Prior PR**: <link to prior PR if retrofit/upgrade adoption; N/A at greenfield adoption>
- **AMAS framework version targeted**: <vX.Y.Z; current canonical version per `README.md`>
- **Receiving-surface assignments**:
  - Architect: <surface name, e.g., Claude.ai Project / Codex desktop>
  - Builder: <surface name, e.g., Claude Code / Codex CLI>
  - Reviewer: <surface name; per ADR-005-equivalent project decision>

## §2. Project context

<1-2 paragraph framing of the project being initiated.>

- What the project is (domain, scope, intended user/operator set).
- AMAS framework version being adopted (and rationale for that version selection).
- Adoption shape: greenfield (new project starting under AMAS) / retrofit (existing project adopting AMAS over prior workflow) / upgrade (existing AMAS project moving to a new framework version) per Batch P3 project-kickoff prompts.
- Project documentation-MCP mechanism (REQUIRED field per `templates/project-brief-template.md`): the surface where canonical project documents and references are persistently accessible to receiving-surface AI agents.

## §3. Project goal

<1-paragraph multi-sentence objective.>

- Durable outcome the project pursues (the load-bearing "why" of project existence).
- Alignment with AMAS adoption rationale: what AMAS discipline brings to this project that a pre-AMAS workflow did not.

## §4. Initial cycle scope

What ships at PR-0 / PR-1 (project bootstrap cycle). Adjust per project policy:

- [ ] Project Brief authored at `docs/project-brief.md` (or project-policy equivalent path)
- [ ] AMAS canonical-law trio (`core.md` + `github-reference.md` + `usage-guide.md`) referenced or mirrored at project root per project policy
- [ ] Receiving-surface AI-agent instruction files instantiated at project root (`AGENTS.md` for OpenAI Codex products + `CLAUDE.md` for Anthropic Claude products + others per project receiving-surface set)
- [ ] Branch protection configured per `github-reference.md` §3 (or project-policy equivalent)
- [ ] CODEOWNERS authored at canonical layout per `github-reference.md` §2.1 (or project-policy equivalent)
- [ ] PR template instantiated at `.github/PULL_REQUEST_TEMPLATE.md` per `github-reference.md` §4.2
- [ ] Initial Architect / Builder / Reviewer role assignments recorded at `AGENTS.md` / `CLAUDE.md` §8 project-specific overlay (or project-policy equivalent)
- [ ] Tool Inventory authored at `docs/tool-inventory.md` per `templates/tool-inventory-template.md` (or project-policy equivalent)

## §5. Out of scope

Explicit deferrals to future cycles:

- Substantive feature work (deferred to first feature-cycle Issue after bootstrap closure)
- Deterministic-enforcement Actions instantiation (deferred per project AMAS Actions adoption posture; Batch P4 v3.1-planned at canonical scope per ADR-008)
- Appendix references and adapter-pack adoption (deferred to project-maturity inflection per project-policy decision)
- Performance, hardening, or optimization work beyond bootstrap closure

## §6. Roles + tools

Structured enumeration of role assignments + tool inventory at project bootstrap:

- **Architect**: <role-holder identity (human + AI surface pair)> at <receiving surface, e.g., Claude.ai Project>
- **Builder**: <role-holder identity> at <receiving surface, e.g., Claude Code CLI on platform>
- **Reviewer**: <role-holder identity> at <receiving surface, e.g., Codex desktop>
- **Documentation-MCP mechanism**: <name + path; canonical reference surface for AI-agent context loading>
- **Other project-specific tools**: <enumerate per `templates/tool-inventory-template.md` reference; e.g., test runner, linter, type-checker, format check, deploy target, observability dashboards>

## §7. Acceptance criteria

Issue 0 closure conditions (project transitions from bootstrap to active operation when ALL boxes checked):

- [ ] Project Brief authored + ratified by owner
- [ ] Canonical-law trio files referenced at project root (or mirrored per project policy)
- [ ] `AGENTS.md` / `CLAUDE.md` / receiving-surface adapter pack(s) instantiated at project root
- [ ] Branch protection configured per ADR-001 D9 substrate or project equivalent
- [ ] PR-0 bootstrap cycle complete and merged
- [ ] First feature-cycle Issue opened (transitions project from bootstrap to active operation)

## Cross-references

- Canonical-source-vs-operational distinction: `github-reference.md` §4.3
- Operational instantiation path: `.github/ISSUE_TEMPLATE/project-initiation.md`
- Branch convention: `github-reference.md` §2.2 + ADR-005
- Project Brief canonical form: `templates/project-brief-template.md`
- Tool Inventory canonical form: `templates/tool-inventory-template.md`
- Project-kickoff prompt set: `prompts/greenfield.md` + `prompts/retrofit.md` + `prompts/upgrade.md` (Batch P3; ship-pending per ADR-008 D2)
- Sibling canonical-source templates: `templates/ISSUE_TEMPLATE/feature.md` + `templates/ISSUE_TEMPLATE/chore.md` + `templates/ISSUE_TEMPLATE/retrospective.md`
