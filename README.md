# AMAS Framework

GitHub-native framework for AI-assisted projects: role separation (Architect / Builder / Reviewer), universal handoff schema, surface-file synchronization, claimed-action verification, and deterministic enforcement via Actions.

## Status

This repository is under active development. **AMAS v3.0 is in production** via a multi-phase PR sequence locked in [docs/adr/ADR-003-full-package-pr-plan.md](docs/adr/ADR-003-full-package-pr-plan.md). See [docs/adr/ADR-001-initial-repo-setup.md](docs/adr/ADR-001-initial-repo-setup.md) for the standalone-repo decision and [docs/adr/ADR-003-full-package-pr-plan.md](docs/adr/ADR-003-full-package-pr-plan.md) for the current PR plan.

The current canonical AMAS framework version is **v2.26**, materialized in the UPCDS reference project. Until v3 publishes from this repository, adopters should reference v2.26.

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

The current canonical PR plan reference is the combined [ADR-003](docs/adr/ADR-003-full-package-pr-plan.md) + [ADR-006](docs/adr/ADR-006-product-delivery-pivot-pr-plan-amendment.md) + [ADR-007](docs/adr/ADR-007-part-c-materialization-scoping.md) sequence: ADR-003 establishes v3.0.0 ship scope (50 stubs); ADR-006 amends the canonical framework-package batch sequence (Batch P1-P8); ADR-007 inserts Part C.1 + Part C.2 as canonical-law-Part-C materialization batches internal to `core.md`. Part C.1 lands within P1 (after first 2 of 9 process templates filled at PR-35; before remaining 7 templates that reference §14 / §17.5 / §17.7); Part C.2 lands between P3 (prompts) and P4 (Actions; grounds operating-instruction surface disciplines that Actions enforce). Effective batch sequence: P1 (process templates) → C.1 → P1[continuation] → P2 (GitHub-artifact templates) → P3 (prompts) → C.2 → P4 (Actions) → P5 (flat appendices) → P6 (project-type appendices) → P7 (receiving-surface adapter packs) → P8 (release + README polish). Per-batch progress tracked via the Package layout tables. ADR-003 Decision 1 (v3.0 ship scope = 50 stubs filled) and Decision 3 (TASK reservation + PMN insertion budget pattern) remain in force. The UPCDS reference project will adopt v3.0.0 in a separate PR sequence in the UPCDS repo after v3.0.0 ships. See [ADR-001](docs/adr/ADR-001-initial-repo-setup.md) for the standalone-repo decision.

## Package layout

The v3 framework package is organized into seven layers. Each stub or template declares its `framework_version` or `template_version` in YAML frontmatter (or YAML comment for `.yml` files); archived prompts preserve their original structure and carry only a provenance HTML comment. The `filled_by` field on every stub points at [ADR-003](docs/adr/ADR-003-full-package-pr-plan.md) until the stub is filled; each substantive content PR updates its filled stub's `filled_by` field to the actual PR/TASK number at content-fill time.

### Canonical law (3 files)

| Path | Description | Filled by |
|---|---|---|
| `core.md` | Platform-agnostic framework canonical | PR-10 (TASK-0010) Part A — verify-before-assert cluster (§8.1.1, §23.6, §24.3); PR-13 (TASK-0012) Part B — §17/§18 baseline + M-A7 (§18.3) + bump-trigger criteria (§18.4) + bounded-continuation rule (§8.1.1.3) |
| `github-reference.md` | GitHub-specific implementation of core | PR-17 (TASK-0017) |
| `usage-guide.md` | Practical operating guidance + three-tier framing | PR-29 (TASK-0024) |

### Prompts (5 files)

| Path | Description | Filled by |
|---|---|---|
| `prompts/greenfield.md` | Project kickoff (project-type-aware) | Batch P3 (ADR-006); pending content-fill cycle |
| `prompts/retrofit.md` | Existing-project adoption | Batch P3 (ADR-006); pending content-fill cycle |
| `prompts/upgrade.md` | Inter-version upgrade | Batch P3 (ADR-006); pending content-fill cycle |
| `prompts/deep-research-design-brief.md` | Original Design Brief, archived | PR-2 (this PR) |
| `prompts/research-deliverable.md` | Research Deliverable, archived | PR-2 (this PR) |

### Templates (16 files)

| Path | Description | Filled by |
|---|---|---|
| `templates/AGENTS.md` | Distributed AGENTS template | Batch P2 (ADR-006); pending content-fill cycle |
| `templates/CLAUDE.md` | Distributed CLAUDE template | Batch P2 (ADR-006); pending content-fill cycle |
| `templates/PULL_REQUEST_TEMPLATE.md` | Distributed PR template | Batch P2 (ADR-006); pending content-fill cycle |
| `templates/ADR-template.md` | ADR template | Batch P1 (ADR-006); pending content-fill cycle |
| `templates/handoff-template.md` | Universal handoff schema with Direction field | PR-35 (TASK-0027) |
| `templates/review-template.md` | §17.7 review template | PR-35 (TASK-0027) |
| `templates/post-merge-note-template.md` | PMN template | Batch P1 (ADR-006); pending content-fill cycle |
| `templates/role-scorecard-template.md` | Role scorecard template | Batch P1 (ADR-006); pending content-fill cycle |
| `templates/feature-brief-template.md` | Feature Brief template | Batch P1 (ADR-006); pending content-fill cycle |
| `templates/project-brief-template.md` | Project Brief template (incl. doc-MCP mechanism field) | Batch P1 (ADR-006); pending content-fill cycle |
| `templates/tool-inventory-template.md` | Tool Inventory with expanded MCP fields | Batch P1 (ADR-006); pending content-fill cycle |
| `templates/surfaces-manifest-template.yml` | `.amas/surfaces.yml` schema | Batch P1 (ADR-006); pending content-fill cycle |
| `templates/ISSUE_TEMPLATE/project-initiation.md` | Issue 0 template | Batch P2 (ADR-006); pending content-fill cycle |
| `templates/ISSUE_TEMPLATE/feature.md` | Feature Issue template | Batch P2 (ADR-006); pending content-fill cycle |
| `templates/ISSUE_TEMPLATE/chore.md` | Chore Issue template | Batch P2 (ADR-006); pending content-fill cycle |
| `templates/ISSUE_TEMPLATE/retrospective.md` | PMN companion Issue template | Batch P2 (ADR-006); pending content-fill cycle |

### Actions (9 workflows)

| Path | Description | Filled by |
|---|---|---|
| `actions/branch-name-check.yml` | Enforce `github-reference.md` §2.2 branch regex per ADR-005 | Batch P4 (ADR-006); pending content-fill cycle |
| `actions/pr-template-check.yml` | Enforce §17.6 PR template sections | Batch P4 (ADR-006); pending content-fill cycle |
| `actions/linked-records-check.yml` | Verify TASK/ADR/FEAT references resolve | Batch P4 (ADR-006); pending content-fill cycle |
| `actions/ai-session-log-check.yml` | Verify AI Session Log section present | Batch P4 (ADR-006); pending content-fill cycle |
| `actions/review-freshness-check.yml` | Detect stale review approvals | Batch P4 (ADR-006); pending content-fill cycle |
| `actions/surface-version-sync-check.yml` | Verify `.amas/surfaces.yml` matches surface frontmatter | Batch P4 (ADR-006); pending content-fill cycle |
| `actions/artifact-path-check.yml` | Enforce ADR/handoff/PMN/review/Feature filename patterns | Batch P4 (ADR-006); pending content-fill cycle |
| `actions/claimed-action-verification.yml` | Phantom-action verification (advisory; expanded scope) | Batch P4 (ADR-006); pending content-fill cycle |
| `actions/mcp-config-validation.yml` | Validate `.mcp.json` against transport-security defaults | Batch P4 (ADR-006); pending content-fill cycle |

### Appendices — flat (7 files)

| Path | Description | Filled by |
|---|---|---|
| `appendices/mcp-integration.md` | Tool Inventory schema, OAuth 2.1, STDIO advisory, transport security | Batch P5 (ADR-006); pending content-fill cycle |
| `appendices/documentation-mcp-options.md` | Context7 + alternatives + selection criteria | Batch P5 (ADR-006); pending content-fill cycle |
| `appendices/tool-capability-model.md` | Capability-class taxonomy + industry-taxonomy alignment | Batch P5 (ADR-006); pending content-fill cycle |
| `appendices/vendor-surface-guidance.md` | Generic per-surface guidance (not adapters) | Batch P5 (ADR-006); pending content-fill cycle |
| `appendices/github-review-automation.md` | GitHub-specific review patterns | Batch P5 (ADR-006); pending content-fill cycle |
| `appendices/amas-vs-other-frameworks.md` | Distinctive contributions claim | Batch P5 (ADR-006); pending content-fill cycle |
| `appendices/regulated-tier-extension.md` | Additive layer for regulated projects | Batch P5 (ADR-006); pending content-fill cycle |

### Appendices — project types (5 files)

| Path | Description | Filled by |
|---|---|---|
| `appendices/project-types/api-app.md` | API/app project type | Batch P6 (ADR-006); pending content-fill cycle |
| `appendices/project-types/research-methodology.md` | Research methodology project type | Batch P6 (ADR-006); pending content-fill cycle |
| `appendices/project-types/code-reports-data-analysis.md` | Code/reports/data analysis project type | Batch P6 (ADR-006); pending content-fill cycle |
| `appendices/project-types/documents-only.md` | Documents-only project type | Batch P6 (ADR-006); pending content-fill cycle |
| `appendices/project-types/mixed.md` | Mixed project type | Batch P6 (ADR-006); pending content-fill cycle |

### Appendices — receiving-surface adapters (7 files)

Each adapter pack carries an extended frontmatter with `last_validated_on`, `vendor_doc_urls`, `last_breaking_change_observed` per AMAS v3 transition plan v0.2 §6.

| Path | Description | Filled by |
|---|---|---|
| `appendices/receiving-surface-adapters/claude-code.md` | Claude Code adapter pack | Batch P7 (ADR-006); pending content-fill cycle |
| `appendices/receiving-surface-adapters/codex.md` | Codex (cloud) adapter pack — phantom-action surface | Batch P7 (ADR-006); pending content-fill cycle |
| `appendices/receiving-surface-adapters/chatgpt.md` | ChatGPT adapter pack | Batch P7 (ADR-006); pending content-fill cycle |
| `appendices/receiving-surface-adapters/cursor.md` | Cursor adapter pack — phantom-action surface | Batch P7 (ADR-006); pending content-fill cycle |
| `appendices/receiving-surface-adapters/gemini.md` | Gemini adapter pack | Batch P7 (ADR-006); pending content-fill cycle |
| `appendices/receiving-surface-adapters/copilot.md` | GitHub Copilot adapter pack | Batch P7 (ADR-006); pending content-fill cycle |
| `appendices/receiving-surface-adapters/human-maintainer.md` | Human Maintainer adapter pack | Batch P7 (ADR-006); pending content-fill cycle |

## License

MIT. See [LICENSE](LICENSE).

## Contributing

Contribution guidelines will land alongside v3.0 publication. Until then, framework changes are coordinated through the project owner via the PR sequence.
