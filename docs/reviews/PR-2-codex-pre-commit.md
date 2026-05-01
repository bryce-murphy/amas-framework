# PR-2 — Codex desktop pre-commit review context

## Metadata

- PR: #2 (will be assigned by `gh pr create` at step 15)
- TASK: TASK-0002
- FEAT: FEAT-0001
- Branch: `feat/task-0002-v3-package-scaffold`
- Base SHA: c1ec54f0015415329143a989e392b09005877f12
- Reviewer surface: Codex desktop (sandboxed `workspace-write` mode)
- Review timing: pre-stage (untracked working tree)
- Builder session: 2026-05-01

## Scope

Pre-commit review of v3 framework package scaffold per ADR-001 decisions 7-8 and AMAS v3 transition plan v0.2 §3.

PR-2 authors stubs only — no substantive framework content. 55 new files plus 1 modified README. Substantive content lands in PR-3 (TASK-0003) onward.

## Builder claims for Codex verification

- **File count**: 65 tracked / 56 changed / 55 new / 1 modified / 9 unchanged
- **Stub-class conformance**: every stub matches its §4 class template (Class A canonical-framework: 3 files; Class B template-markdown: 30 files; Class B' YAML-comment: 1 file; Class C adapter-pack: 7 files; Class D action-yaml: 9 files; Class E archive: 2 files; Class F README modification: 1 file)
- **No substantive framework content** authored in any stub — only frontmatter + placeholder body per §4
- **Archive integrity**: `prompts/deep-research-design-brief.md` matches `deep-research-report.md` source verbatim plus provenance comment; `prompts/research-deliverable.md` matches `amas-v3-research-deliverable.md` source verbatim plus provenance comment
- **README modification**: only the new `## Package layout` section added; rest of README unchanged
- **Cross-surface consistency**: framework_version 3.0.0 referenced consistently in all Class A files; PR sequence (PR-2 through PR-8) referenced consistently in all metadata
- **No `.claude/` content tracked** (gitignored locally)

## BEGIN CODEX DESKTOP PRE-COMMIT REVIEW PROMPT

You are Codex desktop in the `amas-framework` repository. Act as an AMAS pre-commit Reviewer.

State before review:
- The Builder has completed authoring.
- No commit has been created yet.
- All authored files are present in the working tree but UNTRACKED (no `git add` has run yet).
- Do not modify files, stage files, commit, push, or create PRs.

Please:
1. Read `AGENTS.md` from the repo root.
2. Read `docs/features/FEAT-0001-v3-package-scaffold.md` for the Feature Brief.
3. Read `docs/handoffs/TASK-0002-v3-package-scaffold.md` for the active handoff.
4. Read this file (`docs/reviews/PR-2-codex-pre-commit.md`) for Builder claims.
5. Inspect untracked working-tree state with `git status --short --untracked-files=all`.
6. Spot-check at least one file from each stub class:
   - Class A: `core.md` or `github-reference.md` or `usage-guide.md`
   - Class B: any file in `templates/` or `appendices/` (markdown)
   - Class B': `templates/surfaces-manifest-template.yml`
   - Class C: any file in `appendices/receiving-surface-adapters/`
   - Class D: any file in `actions/`
   - Class E: `prompts/deep-research-design-brief.md` or `prompts/research-deliverable.md`
   - Class F: `README.md` (verify only the `## Package layout` section was added)
7. Verify Builder claims listed above against actual working-tree state.
8. Review for substantive defects, missing files, frontmatter errors, AMAS scope violations (substantive content authored in stubs), and phantom-action risks.

Output an AMAS §17.7-style Review Summary with these sections:
- **Blocking findings** (defects that must be addressed before commit)
- **Major findings** (defects that should be addressed but could be deferred)
- **Minor findings** (improvements; nits)
- **Claimed-action verification** (one line per Builder claim above: verified / mismatch / unable-to-verify)
- **Recommendation**: Approve / Request changes / Comment
- **Residual risks or limits**: anything Codex desktop cannot authoritatively review (e.g., GitHub PR metadata which doesn't yet exist)

Caveats:
- If you cannot read a file or run a command, say so explicitly.
- Treat untracked files as the proposed commit content. Treat the modified-but-not-staged `README.md` as also part of the proposed commit.

## END CODEX DESKTOP PRE-COMMIT REVIEW PROMPT

## Codex review outcome

- **Outcome**: minor finding addressed (Codex's recommendation was `Comment`, not `Request changes`; owner elected to fix before commit; full re-run waived given one-word scope of the fix).
- **Codex findings**: one minor finding — `[README.md](../../README.md)` line 36 said the v3 package was "organized into six layers" while the section listed seven peer H3 sections (Canonical law, Prompts, Templates, Actions, Appendices — flat, Appendices — project types, Appendices — receiving-surface adapters). Priority 3, confidence 0.88.
- **Codex claimed-action verification** (verbatim summary):
  - File count: verified — 65 tracked / 56 changed / 55 new / 1 modified / 9 unchanged at branch tip.
  - Stub-class conformance: verified — A=3, B=30, B'=1, C=7, D=9, E=2.
  - No substantive framework content in stubs: verified for stubs; archive prompts hold archived source content (in scope for Class E).
  - Archive integrity: partially verified — both archives present with provenance comments and UTF-8-no-BOM; original sources not in repo, so byte-for-byte source equality not verified by Codex.
  - README modification: verified — `git diff -- README.md` shows only the new `## Package layout` section.
  - Cross-surface consistency: verified — FEAT, handoff, review-context all agree on `65/56/55/1/9`.
  - No `.claude/` content tracked: verified — `.claude/settings.local.json` exists locally but is git-ignored.
  - Recommendation: `Comment` (no blocking or major issues).
  - Residual limits: GitHub PR metadata not yet present (PR #2 not opened); archive sources unavailable in repo.
- **Owner decision**: fix the wording (option b), waive Codex re-run given one-word scope.
- **Builder actions**: changed `README.md` line 36 from "organized into six layers" to "organized into seven layers". Re-verified counts unchanged at 65/56/55/1/9; `git diff --stat HEAD` shows `56 files changed, 1844 insertions(+)`; H2 heading order preserved.
- **Iteration**: single pass (one Codex review; one minor finding addressed; re-run waived).
