# AMAS Framework

GitHub-native framework for AI-assisted projects: role separation (Architect / Builder / Reviewer), universal handoff schema, surface-file synchronization, claimed-action verification, and deterministic enforcement via Actions.

## Status

This repository is under active development. **AMAS v3.0 is in production** via a multi-phase PR sequence locked in [docs/adr/ADR-003-full-package-pr-plan.md](docs/adr/ADR-003-full-package-pr-plan.md). See [docs/adr/ADR-001-initial-repo-setup.md](docs/adr/ADR-001-initial-repo-setup.md) for the standalone-repo decision and [docs/adr/ADR-003-full-package-pr-plan.md](docs/adr/ADR-003-full-package-pr-plan.md) for the current PR plan.

The current canonical AMAS framework version is **v2.14.1**, materialized in the UPCDS reference project. Until v3 publishes from this repository, adopters should reference v2.14.1.

## What is AMAS?

AMAS (AI Multi-Agent System) is an operating-system framework for projects that combine human and AI work. It defines:

- **Roles**: Architect, Builder, Reviewer (required) plus optional Researcher, Release Manager, Tooling/Automation Agent, and Adjudicator
- **Universal handoff schema** with seven direction-specific variants (Architect→Builder, Builder→Reviewer, Reviewer→Builder, Reviewer→Architect, Builder→Architect, Human→AI, AI→Human)
- **GitHub-as-canonical-memory** discipline: durable artifacts (ADRs, handoffs, post-merge notes) live in version control, not in chat history
- **Deterministic enforcement** via GitHub Actions for branch naming, PR templates, linked records, surface-file synchronization, and claimed-action verification
- **Surface-file synchronization** to keep AGENTS.md, CLAUDE.md, PR templates, and workflows aligned with the framework version
- **Phantom-action verification**: catching AI claims about actions that did not actually occur

## Reading order

1. This README
2. [AGENTS.md](AGENTS.md) (Codex-targeted) or [CLAUDE.md](CLAUDE.md) (Claude-targeted) for AI agent operating expectations on this repository
3. Once v3 ships: `core.md`, `github-reference.md`, `usage-guide.md`, plus the templates, Actions, and appendices

## Roadmap

v3 production is sequenced across thirteen substantive content PRs (PR-7 ADR-003 + PR-8 through PR-19 content + PR-19 release tag), with PMN insertion budget through TASK-0026. The UPCDS reference project will adopt v3.0.0 in a separate PR sequence in the UPCDS repo after v3.0.0 ships. See [ADR-003](docs/adr/ADR-003-full-package-pr-plan.md) for the current PR plan and [ADR-001](docs/adr/ADR-001-initial-repo-setup.md) for the standalone-repo decision.

## Package layout

The v3 framework package is organized into seven layers. Each stub or template declares its `framework_version` or `template_version` in YAML frontmatter (or YAML comment for `.yml` files); archived prompts preserve their original structure and carry only a provenance HTML comment. The `filled_by` field on every stub points at [ADR-003](docs/adr/ADR-003-full-package-pr-plan.md) until the stub is filled; each substantive content PR updates its filled stub's `filled_by` field to the actual PR/TASK number at content-fill time.

### Canonical law (3 files)

| Path | Description | Filled by |
|---|---|---|
| `core.md` | Platform-agnostic framework canonical | PR-8 (TASK-0008) §1–§17 Part A; PR-9 (TASK-0009) §18–§24 Part B |
| `github-reference.md` | GitHub-specific implementation of core | PR-10 (TASK-0010) |
| `usage-guide.md` | Practical operating guidance + three-tier framing | PR-11 (TASK-0011) |

### Prompts (5 files)

| Path | Description | Filled by |
|---|---|---|
| `prompts/greenfield.md` | Project kickoff (project-type-aware) | PR-14 (TASK-0014) |
| `prompts/retrofit.md` | Existing-project adoption | PR-14 (TASK-0014) |
| `prompts/upgrade.md` | Inter-version upgrade | PR-14 (TASK-0014) |
| `prompts/deep-research-design-brief.md` | Original Design Brief, archived | PR-2 (this PR) |
| `prompts/research-deliverable.md` | Research Deliverable, archived | PR-2 (this PR) |

### Templates (16 files)

| Path | Description | Filled by |
|---|---|---|
| `templates/AGENTS.md` | Distributed AGENTS template | PR-13 (TASK-0013) |
| `templates/CLAUDE.md` | Distributed CLAUDE template | PR-13 (TASK-0013) |
| `templates/PULL_REQUEST_TEMPLATE.md` | Distributed PR template | PR-13 (TASK-0013) |
| `templates/ADR-template.md` | ADR template | PR-12 (TASK-0012) |
| `templates/handoff-template.md` | Universal handoff schema with Direction field | PR-12 (TASK-0012) |
| `templates/review-template.md` | §17.7 review template | PR-12 (TASK-0012) |
| `templates/post-merge-note-template.md` | PMN template | PR-12 (TASK-0012) |
| `templates/role-scorecard-template.md` | Role scorecard template | PR-12 (TASK-0012) |
| `templates/feature-brief-template.md` | Feature Brief template | PR-12 (TASK-0012) |
| `templates/project-brief-template.md` | Project Brief template (incl. doc-MCP mechanism field) | PR-12 (TASK-0012) |
| `templates/tool-inventory-template.md` | Tool Inventory with expanded MCP fields | PR-12 (TASK-0012) |
| `templates/surfaces-manifest-template.yml` | `.amas/surfaces.yml` schema | PR-12 (TASK-0012) |
| `templates/ISSUE_TEMPLATE/project-initiation.md` | Issue 0 template | PR-13 (TASK-0013) |
| `templates/ISSUE_TEMPLATE/feature.md` | Feature Issue template | PR-13 (TASK-0013) |
| `templates/ISSUE_TEMPLATE/chore.md` | Chore Issue template | PR-13 (TASK-0013) |
| `templates/ISSUE_TEMPLATE/retrospective.md` | PMN companion Issue template | PR-13 (TASK-0013) |

### Actions (9 workflows)

| Path | Description | Filled by |
|---|---|---|
| `actions/branch-name-check.yml` | Enforce §6.1 branch regex | PR-15 (TASK-0015) |
| `actions/pr-template-check.yml` | Enforce §17.6 PR template sections | PR-15 (TASK-0015) |
| `actions/linked-records-check.yml` | Verify TASK/ADR/FEAT references resolve | PR-15 (TASK-0015) |
| `actions/ai-session-log-check.yml` | Verify AI Session Log section present | PR-15 (TASK-0015) |
| `actions/review-freshness-check.yml` | Detect stale review approvals | PR-15 (TASK-0015) |
| `actions/surface-version-sync-check.yml` | Verify `.amas/surfaces.yml` matches surface frontmatter | PR-15 (TASK-0015) |
| `actions/artifact-path-check.yml` | Enforce ADR/handoff/PMN/review/Feature filename patterns | PR-15 (TASK-0015) |
| `actions/claimed-action-verification.yml` | Phantom-action verification (advisory; expanded scope) | PR-15 (TASK-0015) |
| `actions/mcp-config-validation.yml` | Validate `.mcp.json` against transport-security defaults | PR-15 (TASK-0015) |

### Appendices — flat (7 files)

| Path | Description | Filled by |
|---|---|---|
| `appendices/mcp-integration.md` | Tool Inventory schema, OAuth 2.1, STDIO advisory, transport security | PR-16 (TASK-0016) |
| `appendices/documentation-mcp-options.md` | Context7 + alternatives + selection criteria | PR-16 (TASK-0016) |
| `appendices/tool-capability-model.md` | Capability-class taxonomy + industry-taxonomy alignment | PR-16 (TASK-0016) |
| `appendices/vendor-surface-guidance.md` | Generic per-surface guidance (not adapters) | PR-16 (TASK-0016) |
| `appendices/github-review-automation.md` | GitHub-specific review patterns | PR-16 (TASK-0016) |
| `appendices/amas-vs-other-frameworks.md` | Distinctive contributions claim | PR-16 (TASK-0016) |
| `appendices/regulated-tier-extension.md` | Additive layer for regulated projects | PR-16 (TASK-0016) |

### Appendices — project types (5 files)

| Path | Description | Filled by |
|---|---|---|
| `appendices/project-types/api-app.md` | API/app project type | PR-17 (TASK-0017) |
| `appendices/project-types/research-methodology.md` | Research methodology project type | PR-17 (TASK-0017) |
| `appendices/project-types/code-reports-data-analysis.md` | Code/reports/data analysis project type | PR-17 (TASK-0017) |
| `appendices/project-types/documents-only.md` | Documents-only project type | PR-17 (TASK-0017) |
| `appendices/project-types/mixed.md` | Mixed project type | PR-17 (TASK-0017) |

### Appendices — receiving-surface adapters (7 files)

Each adapter pack carries an extended frontmatter with `last_validated_on`, `vendor_doc_urls`, `last_breaking_change_observed` per AMAS v3 transition plan v0.2 §6.

| Path | Description | Filled by |
|---|---|---|
| `appendices/receiving-surface-adapters/claude-code.md` | Claude Code adapter pack | PR-18 (TASK-0018) |
| `appendices/receiving-surface-adapters/codex.md` | Codex (cloud) adapter pack — phantom-action surface | PR-18 (TASK-0018) |
| `appendices/receiving-surface-adapters/chatgpt.md` | ChatGPT adapter pack | PR-18 (TASK-0018) |
| `appendices/receiving-surface-adapters/cursor.md` | Cursor adapter pack — phantom-action surface | PR-18 (TASK-0018) |
| `appendices/receiving-surface-adapters/gemini.md` | Gemini adapter pack | PR-18 (TASK-0018) |
| `appendices/receiving-surface-adapters/copilot.md` | GitHub Copilot adapter pack | PR-18 (TASK-0018) |
| `appendices/receiving-surface-adapters/human-maintainer.md` | Human Maintainer adapter pack | PR-18 (TASK-0018) |

## License

MIT. See [LICENSE](LICENSE).

## Contributing

Contribution guidelines will land alongside v3.0 publication. Until then, framework changes are coordinated through the project owner via the PR sequence.
