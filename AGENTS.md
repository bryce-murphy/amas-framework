# AGENTS.md — amas-framework

Operating instructions for AI agents (Codex, GitHub Copilot, etc.) working on the `amas-framework` repository.

## Operating context

This repository **is** the AMAS framework. Work in this repo follows AMAS itself ("dogfooding"): the framework operates under its own rules.

- **Active framework version**: AMAS v3.0 (in development; current canonical materialization at v2.43 — see README)
- **Substrate canonical reference**: AMAS v2.14.1 lives at https://github.com/recruiting-tech/upcds/blob/main/docs/ai-operating-system.md and is the substrate from which the v3 canonical-law trio is being authored per ADR-003
- **Repository status**: AMAS v3.0 trio is in active production in this repository (canonical-law trio: `core.md`, `github-reference.md`, `usage-guide.md` — all materialized; full v3.0 package per ADR-003 D2 thirteen-substantive-PR sequence in progress). UPCDS reference project will adopt v3.0.0 in a separate PR sequence after v3.0.0 ships.
- **v3.0 scope framing**: per [ADR-008](docs/adr/ADR-008-v3-scope-amendment.md) (2026-05-20), v3.0 ships canonical disciplines + materialized templates + project-kickoff prompts as the minimum-viable framework (canonical-law trio + Part C.1 + Part C.2 + Batches P1-P3 + release polish). Deterministic-enforcement automation (Batch P4 Actions) lands at v3.1 minor release; comprehensive reference + adapter packs (Batches P5-P7) at v3.2.

## Mandatory read order before acting as Builder

1. **AMAS v3 canonical-law trio** (read in order; per `github-reference.md` §4.1 reading order):
   - `core.md` (canonical law foundations: roles, handoff schema, phantom-action verification §8.1.1.2, PMN/ADR discipline §17 / §18, Architect prompt construction §23, cross-surface verify-before-assert §24)
   - `github-reference.md` (GitHub-specific implementation: branch convention §2.2, branch protection §3, templates §4, AI agent identity §5, deterministic Actions §6)
   - `usage-guide.md` (practical operating guidance: kickoff, first-task pattern, handoff/log lifecycle, ID conventions, Reviewer-output absorption, Architect-side disciplines)
2. **AMAS v2.14.1 canonical** at the URL above — substrate reference for sections not yet materialized in v3 trio (forthcoming v3 content noted in trio with `(forthcoming at Part C+)` qualifier per TASK-0019 cycle convention). Sections especially relevant as v3 substrate:
   - v2.14.1 §2 (role assignment + capability scoring; v3 substrate for forthcoming role-model content)
   - v2.14.1 §13 / §14 (AI Session Log + handoff templates; v3 substrate for forthcoming workflow-phase content)
   - v2.14.1 §17 (template canonical forms; v3 substrate for forthcoming template-set content)
3. **The active task handoff** at `docs/handoffs/TASK-####-<slug>.md` for the work you are being asked to do
4. **The PR description** if a PR already exists for the task
5. **Any ADR referenced by the handoff**
6. **This file (AGENTS.md)** if this is your first session on this repo

## Validation commands

For PRs that touch repository content:

- `git status` — confirm clean working tree post-edits
- `git log --oneline -10` — confirm commit history matches expectations
- For markdown files: spot-check rendering (GitHub-flavored Markdown)
- Future: deterministic checks via `.github/workflows/` will run automatically on PR open (Actions batch ships per ADR-003 D2 sequence; partial-deployment in progress — `linked-pr-fix-up.yml` shipped at PR-21 per ADR-004 + ADR-001 D9 single-contributor governance flow)

## Branch and PR expectations

- **Branch naming** per `github-reference.md` §2.2 (canonical at v3; deliberately diverges from v2.14.1 §6.1 substrate per ADR-005 to align with AMAS TASK-#### centrality + lived practice): `<type>/task-####-<kebab-slug>`. Allowed types: `feat`, `fix`, `chore`, `adr`, `shadow`, `spike` (per v3 canonical types; conventional-commit-extension types `docs`, `refactor`, `test`, `ci` retired this cycle per ADR-005 reconciliation)
- **PR template**: every PR uses `.github/PULL_REQUEST_TEMPLATE.md`. Required sections: Linked records, Summary, Decisions in this PR, Validation, Reviewer focus, Ready for review, AI Session Log
- **Conventional commit messages**: `<type>(<scope>): <subject>` — e.g., `feat(amas): TASK-0002 v3 package scaffold`
- **Per AMAS v2.14.1 §8.2**: Pre-flight verification before any destructive or remote-visible action
- **Per AMAS v2.14.1 §8.3**: Stop-and-show before `git push`, `gh pr create`, branch deletion, or force push

## Review guidelines

When invoked as Reviewer (`@codex review`), produce a Review Summary per AMAS v2.14.1 §17.7 with:

- **Findings classified by severity**: Blocking, Major, Minor (per template)
- **Validation of claims**: verify the Builder's claimed actions per `core.md` §8.1.1.2 — claimed commits exist at claimed SHAs, claimed files exist at claimed paths, claimed follow-up artifacts (PRs, Issues, branches) exist, identifier patterns conform to project convention
- **Recommendation**: Approve / Request changes / Comment

If verification surfaces a phantom claim, name it explicitly and separate substantive review evidence from phantom-affected delivery layer per `core.md` §8.1.1.2 adjudication discipline.

## Scope and escalation

- **Stay within the task's named scope**. Adjacent in-scope edits (one corresponding test, one corresponding doc, one helper file) are acceptable per §8.3; broader edits require explicit approval.
- **Escalate to the project owner via stop-and-show** for: scope drift, blocking questions, ambiguous acceptance criteria, ADR-conflict candidates, or any condition the handoff did not anticipate.
- **Do not merge**. The project owner runs all merges (currently solo-contributor bypass per AMAS v2.14.1 §10.5).

## Repo-specific notes

- Solo-contributor repo. Single CODEOWNER. Codex review runs in substantive-only mode per §8.1; the owner clicks merge after substantive findings are addressed.
- This is a meta-recursive context: framework changes affect the repo's own operating discipline. Cross-surface verify-before-assert per `core.md` §24 is especially load-bearing.
