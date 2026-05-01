# FEAT-0001: AMAS v3 framework package scaffold

## Metadata

- Feature ID: FEAT-0001
- Status: Active
- Author: Architect (Claude Opus 4.7, Claude.ai Project)
- Date: 2026-05-01
- Framework version: AMAS v2.14.1 (production); AMAS v3.0 (in production via PR-2 through PR-8)
- Related TASK: TASK-0002
- Related ADR: ADR-001 (decisions 7-8 cover this PR's scope)
- Related PR: PR-2

## Project documentation-MCP mechanism

Per AMAS v3 framework canonical (to be authored in PR-3, anticipated rule): every project at initiation declares its documentation-MCP mechanism for current-tool-knowledge retrieval.

For `amas-framework`: web-search via native Claude/Codex tools + explicit owner verification. Context7 not configured. If/when needed, owner adds and updates this declaration.

Citation pattern when surfaces retrieve current docs: `Source: <library>@<version> — retrieved <YYYY-MM-DD> via <tool-name>`.

## Objective

Author the v3 framework package scaffold per AMAS v3 transition plan v0.2 §3 and ADR-001 decisions 7-8. Create 50 stub files plus 2 archive prompts plus 1 root README modification, organized into a six-class package layout (canonical-framework, template-markdown, YAML-comment template, adapter-pack, action-yaml, archive-prompt, README-modification).

PR-2 is intentionally minimal-scope: stubs and structural artifacts only. No substantive framework content is authored. Substantive content lands in PR-3 (TASK-0003) onward.

## In scope

- 3 canonical-framework stubs (Class A): `core.md`, `github-reference.md`, `usage-guide.md`
- 30 template-markdown stubs (Class B): 11 flat templates + 4 ISSUE_TEMPLATE + 3 prompt stubs + 7 flat appendices + 5 project-type appendices
- 1 YAML-comment template stub (Class B'): `templates/surfaces-manifest-template.yml`
- 7 receiving-surface adapter pack stubs (Class C): `appendices/receiving-surface-adapters/*`
- 9 action workflow YAML stubs (Class D): `actions/*`
- 2 archive prompts (Class E): `prompts/deep-research-design-brief.md`, `prompts/research-deliverable.md`
- 1 root README modification (Class F): append `## Package layout` section
- 1 Feature Brief (this file): `docs/features/FEAT-0001-v3-package-scaffold.md`
- 1 Codex desktop pre-commit review-context file: `docs/reviews/PR-2-codex-pre-commit.md`
- 1 handoff: `docs/handoffs/TASK-0002-v3-package-scaffold.md`

Total: 50 stubs + 2 archives = 52 §5-table-driven files; plus Feature Brief, review-context, handoff, README modification = 56 total file authoring operations = 55 new files + 1 modified README = 56 changed files.

## Out of scope

- Authoring substantive framework canonical content (`core.md` body, etc.) — PR-3 (TASK-0003)
- Authoring template content (`templates/AGENTS.md` body, etc.) — PR-4 (TASK-0004)
- Authoring kickoff prompts (`prompts/greenfield.md` body, etc.) — PR-5 (TASK-0005)
- Authoring action workflows — PR-7 (TASK-0007)
- Authoring appendices — PR-8 (TASK-0008)
- Authoring receiving-surface adapter packs — PR-8 (TASK-0008)
- Authoring ADR-002 (substantive v3 architectural decision) — PR-3 (TASK-0003)
- Modifying any of the 9 unchanged PR-0 files
- Enabling or modifying GitHub Actions workflows in `.github/workflows/` — `actions/` directory contains framework reference, not GitHub-active workflows

## Acceptance criteria

1. **File count**: 65 tracked / 56 changed / 55 new / 1 modified / 9 unchanged at branch tip
2. **Frontmatter conformance**: every stub matches its §4 class template:
   - Class A: `framework_version: 3.0.0`, `status: stub`, `filled_by: PR-3 (TASK-0003)`
   - Class B: `template_version: 3.0.0`, `status: stub`, `filled_by: PR-N (TASK-NNNN)`
   - Class B': YAML comment frontmatter analogous to Class D
   - Class C: `adapter_pack`, `amas_version: 3.0`, `last_validated_on: 2026-04-30`, `vendor_doc_urls: []`, `last_breaking_change_observed: 2026-04-30`, `status: stub`, `filled_by: PR-8 (TASK-0008)`
   - Class D: YAML-comment template_version + minimal valid `name`/`on`/`jobs` skeleton
3. **Archive integrity**: archive prompts match source content verbatim plus single-line provenance HTML comment
4. **README modification**: only the new `## Package layout` section added; existing sections unchanged byte-for-byte
5. **No scope leakage**: no substantive framework content authored in any stub body; placeholder text only
6. **Cross-surface consistency**: framework_version 3.0.0 in all Class A files agrees; PR sequence referenced consistently across all metadata
7. **§8.2 pre-flight pass**: all preconditions report PASS
8. **Codex desktop pre-commit review**: completed (clean / minor accepted / material addressed) and outcome captured in review-context file

## Risks

- **Count drift**: §3 count table claims must reconcile to actual tree state at step 10 verification. Mitigation: explicit count table in §3, reconciliation in step 10, stop condition on mismatch.
- **Frontmatter typos**: 50 stubs with structured frontmatter creates many opportunities for typos. Mitigation: §4 Class templates are precise; spot-checks in step 10; Codex desktop pre-commit review at step 11.
- **Archive corruption**: copy-from-project-knowledge for 2 large archive files creates risk of truncation or encoding loss. Mitigation: byte-level encoding check in step 10; Codex desktop verification in step 11.
- **Accidental substantive content**: Builder may interpret "stub" broadly. Mitigation: explicit `*Stub.*` body in §4 templates; Codex desktop scope-leakage check at step 11.
- **`.claude/` leak**: harness directory may slip into staged commit. Mitigation: explicit check in step 12 staging verification.
- **Linked-PR fix-up commit drift**: fix-up should change exactly 1 file. Mitigation: stop condition on `git diff --stat HEAD~1` showing more than 1 file.

## Validation strategy

Three layers:

1. **Builder self-verification (step 10)**: tree enumeration, count check, frontmatter spot-check per class, byte-level UTF-8 encoding check on archives.
2. **Codex desktop pre-commit review (step 11)**: untracked-tree review against §17.7 Review Summary template; claimed-action verification against Builder claims listed in `docs/reviews/PR-2-codex-pre-commit.md`.
3. **Post-PR `@codex review` (owner-handled)**: PR-level review against AGENTS.md `## Review guidelines`; Codex bot has access to PR metadata, full diff, and AGENTS.md auto-discovery.

## Dependencies

- PR-1 (TASK-0001) merged: provides `main` baseline at SHA c1ec54f
- Branch protection on `main` enabled per ADR-001 decision 9
- ADR-001 in place: decisions 7 (root content) and 8 (PR sequence) are the authoritative spec for PR-2 scope
- v0.2 transition plan: §3 file tree and §10 PR-2 row are the source of truth for what stubs to author
- Project knowledge accessibility: `deep-research-report.md` and `amas-v3-research-deliverable.md` must be readable for archive authoring

## Reviewer focus

For Codex desktop pre-commit review (step 11) and `@codex review` post-PR:

- Per-class frontmatter conformance to §4 templates (especially Class C extended frontmatter and Class D YAML-comment frontmatter)
- Cross-surface §24 consistency: file count claims (65/56/55/1/9) appear in PR body, FEAT-0001, TASK-0002 handoff, and review-context file — all four must agree
- Archive provenance comment correctness on the 2 archive prompts
- README modification scope: only the `## Package layout` section added
- Phantom-action surface: claims about file existence, frontmatter content, and counts are directly verifiable from working-tree filesystem
- No substantive framework content in any stub
