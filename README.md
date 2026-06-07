# AMAS Framework

GitHub-native framework for AI-assisted projects: role separation (Architect / Builder / Reviewer), universal handoff schema, surface-file synchronization, and claimed-action verification. v3.0 ships canonical disciplines + materialized templates + project-kickoff prompts as the minimum-viable framework; deterministic-enforcement automation lands at v3.1 + comprehensive reference + adapter packs at v3.2 per [ADR-008](docs/adr/ADR-008-v3-scope-amendment.md).

## Status

**AMAS v3.0.0 is published from this repository** — the minimum-viable canonical framework canonicalized through the [ADR-003](docs/adr/ADR-003-full-package-pr-plan.md) + [ADR-006](docs/adr/ADR-006-product-delivery-pivot-pr-plan-amendment.md) + [ADR-007](docs/adr/ADR-007-part-c-materialization-scoping.md) + [ADR-008](docs/adr/ADR-008-v3-scope-amendment.md) chain. ADR-008 sets v3.0 ship scope to the minimum-viable canonical framework (canonical-law trio + Part C.1 + Part C.2 + Batches P1-P3 + release polish); v3.1 ships Batch P4 Actions (deterministic-enforcement automation); v3.2 ships Batches P5-P7 (flat appendices + project-type appendices + receiving-surface adapter packs). See [ADR-001](docs/adr/ADR-001-initial-repo-setup.md) for the standalone-repo decision.

The current canonical AMAS framework version is **v3.0.2** (in development in this repository). The latest published release is **v3.0.0** — the adopter-facing version of record: adopters should reference the v3.0.0 release, governed by this version-positioning note together with the v3.0.0 release tag once the owner publishes it, until the v3.1 release.

## What is AMAS?

AMAS (AI Multi-Agent System) is an operating-system framework for projects that combine human and AI work. It defines:

- **Roles**: Architect, Builder, Reviewer (required) plus optional Researcher, Release Manager, Tooling/Automation Agent, and Adjudicator
- **Universal handoff schema** with seven direction-specific variants (Architect→Builder, Builder→Reviewer, Reviewer→Builder, Reviewer→Architect, Builder→Architect, Human→AI, AI→Human)
- **GitHub-as-canonical-memory** discipline: durable artifacts (ADRs, handoffs, post-merge notes) live in version control, not in chat history
- **Deterministic enforcement** via GitHub Actions for branch naming, PR templates, linked records, surface-file synchronization, and claimed-action verification (v3.1 roadmap per [ADR-008](docs/adr/ADR-008-v3-scope-amendment.md))
- **Surface-file synchronization** to keep AGENTS.md, CLAUDE.md, PR templates, and workflows aligned with the framework version
- **Phantom-action verification**: catching AI claims about actions that did not actually occur

## Reading order

1. This README
2. [AGENTS.md](AGENTS.md) (Codex-targeted) or [CLAUDE.md](CLAUDE.md) (Claude-targeted) for AI agent operating expectations on this repository
3. `core.md`, `github-reference.md`, `usage-guide.md`, plus the templates (with the Actions and appendices arriving at v3.1 / v3.2)

## Roadmap

The current canonical scope-and-sequence reference is the combined [ADR-003](docs/adr/ADR-003-full-package-pr-plan.md) + [ADR-006](docs/adr/ADR-006-product-delivery-pivot-pr-plan-amendment.md) + [ADR-007](docs/adr/ADR-007-part-c-materialization-scoping.md) + [ADR-008](docs/adr/ADR-008-v3-scope-amendment.md) chain: ADR-003 established the original 50-scaffold-stub ship-scope framing (Decision 1 partially superseded by ADR-008); ADR-006 amends the canonical framework-package batch sequence (Batch P1-P8; Decisions 1 + 2 partially superseded by ADR-008); ADR-007 inserts Part C.1 + Part C.2 as canonical-law-Part-C materialization batches internal to `core.md` (preserved unchanged); ADR-008 revises v3.0 ship scope to minimum-viable canonical framework + defines v3.1 + v3.2 phased roadmap for deferred batches. Part C.1 (cycle-execution canonical surfaces: §14 universal handoff schema + §14.1-§14.7 direction variants + §17.5 template lifecycle + §17.7 review template) shipped at PR-41 (TASK-0030); Part C.2 (operating-discipline canonical surfaces: §8.2 + §8.3 + §13 + §10.5 + §23.6.5) shipped at TASK-0048 per ADR-007 D3 schedule + ADR-008 D2 amended scope; release polish shipped at TASK-0049, completing the v3.0.0 minimum-viable canonical framework (the v3.0.0 release tag is applied by the owner at merge time). v3.1 + v3.2 are the forward roadmap. Batch P1 process templates 9 of 9 filled (CLOSED at PR-48); first AMAS adoption pilot completed at bryce-murphy/employee-churn (TASK-0001 → PR-7 squash merge `8d4eb0d`); empirical findings canonicalized at PMN-012 (PR-50); canonical-text amendment bundle landed at PR-52 (TASK-0035; bidirectional sum-stability + sweep-scope completeness role-invariance + path-(α') discipline + four-surface paired-discipline + two-gate hand-back + cost-class one-iteration convergence + verification-first handoff form). Effective post-ADR-008 batch sequence to v3.0.0 ship: Batch P2 (GitHub-artifact templates; 7/7 filled) ISSUE_TEMPLATEs split (TASK-0043 + TASK-0044) → Batch P3 greenfield (TASK-0046) → Batch P3 retrofit + upgrade (TASK-0047) → Part C.2 (operating-discipline; TASK-0048) → release polish + v3.0.0 tag (TASK-0049). v3.1 roadmap: Batch P4 (Actions; 9 canonical scaffold workflows; deterministic-enforcement automation layer). v3.2 roadmap: Batches P5-P7 (7 flat appendices + 5 project-type appendices + 7 receiving-surface adapter packs; documentation/reference/adapter layer). Per-batch progress tracked via the Package layout tables; deferred-stub rows annotated `[v3.1-planned]` / `[v3.2-planned]` per ADR-008 Decision 3. ADR-003 Decision 3 (TASK reservation + PMN insertion budget pattern) preserved. The UPCDS reference project will adopt v3.0.0 in a separate PR sequence in the UPCDS repo after v3.0.0 ships. See [ADR-001](docs/adr/ADR-001-initial-repo-setup.md) for the standalone-repo decision.

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
| `prompts/greenfield.md` | Project kickoff (project-type-aware) | PR-75 (TASK-0046) |
| `prompts/retrofit.md` | Existing-project adoption | PR-80 (TASK-0047) |
| `prompts/upgrade.md` | Inter-version upgrade | PR-83 (TASK-0047) |
| `prompts/deep-research-design-brief.md` | Original Design Brief, archived | PR-2 (this PR) |
| `prompts/research-deliverable.md` | Research Deliverable, archived | PR-2 (this PR) |

### Templates (16 files)

| Path | Description | Filled by |
|---|---|---|
| `templates/AGENTS.md` | Distributed AGENTS template | PR-62 (TASK-0040) |
| `templates/CLAUDE.md` | Distributed CLAUDE template | PR-62 (TASK-0040) |
| `templates/PULL_REQUEST_TEMPLATE.md` | Distributed PR template | PR-64 (TASK-0041) |
| `templates/ADR-template.md` | ADR template | PR-43 (TASK-0031) |
| `templates/handoff-template.md` | Universal handoff schema with Direction field | PR-35 (TASK-0027) |
| `templates/review-template.md` | §17.7 review template | PR-35 (TASK-0027) |
| `templates/post-merge-note-template.md` | PMN template | PR-43 (TASK-0031) |
| `templates/role-scorecard-template.md` | Role scorecard template | PR-45 (TASK-0032) |
| `templates/feature-brief-template.md` | Feature Brief template | PR-45 (TASK-0032) |
| `templates/project-brief-template.md` | Project Brief template (incl. doc-MCP mechanism field) | PR-45 (TASK-0032) |
| `templates/tool-inventory-template.md` | Tool Inventory with expanded MCP fields | PR-48 (TASK-0033) |
| `templates/surfaces-manifest-template.yml` | `.amas/surfaces.yml` schema | PR-48 (TASK-0033) |
| `templates/ISSUE_TEMPLATE/project-initiation.md` | Issue 0 template | PR-68 (TASK-0043) |
| `templates/ISSUE_TEMPLATE/feature.md` | Feature Issue template | PR-68 (TASK-0043) |
| `templates/ISSUE_TEMPLATE/chore.md` | Chore Issue template | PR-71 (TASK-0044) |
| `templates/ISSUE_TEMPLATE/retrospective.md` | PMN companion Issue template | PR-71 (TASK-0044) |

### Actions (9 workflows)

| Path | Description | Filled by |
|---|---|---|
| `actions/branch-name-check.yml` | Enforce `github-reference.md` §2.2 branch regex per ADR-005 | Batch P4 (ADR-008); v3.1 release [v3.1-planned] |
| `actions/pr-template-check.yml` | Enforce §17.6 PR template sections | Batch P4 (ADR-008); v3.1 release [v3.1-planned] |
| `actions/linked-records-check.yml` | Verify TASK/ADR/FEAT references resolve | Batch P4 (ADR-008); v3.1 release [v3.1-planned] |
| `actions/ai-session-log-check.yml` | Verify AI Session Log section present | Batch P4 (ADR-008); v3.1 release [v3.1-planned] |
| `actions/review-freshness-check.yml` | Detect stale review approvals | Batch P4 (ADR-008); v3.1 release [v3.1-planned] |
| `actions/surface-version-sync-check.yml` | Verify `.amas/surfaces.yml` declared template-versions are current against the template-of-record | Batch P4 (ADR-008); v3.1 release [v3.1-planned] |
| `actions/artifact-path-check.yml` | Enforce ADR/handoff/PMN/review/Feature filename patterns | Batch P4 (ADR-008); v3.1 release [v3.1-planned] |
| `actions/claimed-action-verification.yml` | Phantom-action verification (advisory; expanded scope) | Batch P4 (ADR-008); v3.1 release [v3.1-planned] |
| `actions/mcp-config-validation.yml` | Validate `.mcp.json` against transport-security defaults | Batch P4 (ADR-008); v3.1 release [v3.1-planned] |

### Appendices — flat (7 files)

| Path | Description | Filled by |
|---|---|---|
| `appendices/mcp-integration.md` | Tool Inventory schema, OAuth 2.1, STDIO advisory, transport security | Batch P5 (ADR-008); v3.2 release [v3.2-planned] |
| `appendices/documentation-mcp-options.md` | Context7 + alternatives + selection criteria | Batch P5 (ADR-008); v3.2 release [v3.2-planned] |
| `appendices/tool-capability-model.md` | Capability-class taxonomy + industry-taxonomy alignment | Batch P5 (ADR-008); v3.2 release [v3.2-planned] |
| `appendices/vendor-surface-guidance.md` | Generic per-surface guidance (not adapters) | Batch P5 (ADR-008); v3.2 release [v3.2-planned] |
| `appendices/github-review-automation.md` | GitHub-specific review patterns | Batch P5 (ADR-008); v3.2 release [v3.2-planned] |
| `appendices/amas-vs-other-frameworks.md` | Distinctive contributions claim | Batch P5 (ADR-008); v3.2 release [v3.2-planned] |
| `appendices/regulated-tier-extension.md` | Additive layer for regulated projects | Batch P5 (ADR-008); v3.2 release [v3.2-planned] |

### Appendices — project types (5 files)

| Path | Description | Filled by |
|---|---|---|
| `appendices/project-types/api-app.md` | API/app project type | Batch P6 (ADR-008); v3.2 release [v3.2-planned] |
| `appendices/project-types/research-methodology.md` | Research methodology project type | Batch P6 (ADR-008); v3.2 release [v3.2-planned] |
| `appendices/project-types/code-reports-data-analysis.md` | Code/reports/data analysis project type | Batch P6 (ADR-008); v3.2 release [v3.2-planned] |
| `appendices/project-types/documents-only.md` | Documents-only project type | Batch P6 (ADR-008); v3.2 release [v3.2-planned] |
| `appendices/project-types/mixed.md` | Mixed project type | Batch P6 (ADR-008); v3.2 release [v3.2-planned] |

### Appendices — receiving-surface adapters (7 files)

Each adapter pack carries an extended frontmatter with `last_validated_on`, `vendor_doc_urls`, `last_breaking_change_observed` per AMAS v3 transition plan v0.2 §6.

| Path | Description | Filled by |
|---|---|---|
| `appendices/receiving-surface-adapters/claude-code.md` | Claude Code adapter pack | Batch P7 (ADR-008); v3.2 release [v3.2-planned] |
| `appendices/receiving-surface-adapters/codex.md` | Codex (cloud) adapter pack — phantom-action surface | Batch P7 (ADR-008); v3.2 release [v3.2-planned] |
| `appendices/receiving-surface-adapters/chatgpt.md` | ChatGPT adapter pack | Batch P7 (ADR-008); v3.2 release [v3.2-planned] |
| `appendices/receiving-surface-adapters/cursor.md` | Cursor adapter pack — phantom-action surface | Batch P7 (ADR-008); v3.2 release [v3.2-planned] |
| `appendices/receiving-surface-adapters/gemini.md` | Gemini adapter pack | Batch P7 (ADR-008); v3.2 release [v3.2-planned] |
| `appendices/receiving-surface-adapters/copilot.md` | GitHub Copilot adapter pack | Batch P7 (ADR-008); v3.2 release [v3.2-planned] |
| `appendices/receiving-surface-adapters/human-maintainer.md` | Human Maintainer adapter pack | Batch P7 (ADR-008); v3.2 release [v3.2-planned] |

## License

MIT. See [LICENSE](LICENSE).

## Contributing

Contribution guidelines will land in a future release. Until then, framework changes are coordinated through the project owner via the PR sequence.
