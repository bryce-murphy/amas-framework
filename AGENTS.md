# AGENTS.md — amas-framework

Operating instructions for AI agents (Codex, GitHub Copilot, etc.) working on the `amas-framework` repository.

## Operating context

This repository **is** the AMAS framework. Work in this repo follows AMAS itself ("dogfooding"): the framework operates under its own rules.

- **Active framework version**: AMAS v2.14.1
- **Canonical reference**: AMAS v2.14.1 lives at https://github.com/recruiting-tech/upcds/blob/main/docs/ai-operating-system.md
- **Repository status**: AMAS v3.0 is in production in this repository via PR-2 through PR-8. PR-9 (a separate PR sequence in the UPCDS reference project) will adopt v3.0 there.

## Mandatory read order before acting as Builder

1. **AMAS v2.14.1 canonical** at the URL above. Sections especially relevant:
   - §2 (role assignment + capability scoring)
   - §8 (role definitions, Reviewer disciplines, especially §8.1.1.2 phantom-action verification)
   - §13 (AI Session Log) and §14 (handoff templates)
   - §17 (template canonical forms)
   - §23 (Architect-side prompt construction)
2. **The active task handoff** at `docs/handoffs/TASK-####-<slug>.md` for the work you are being asked to do
3. **The PR description** if a PR already exists for the task
4. **Any ADR referenced by the handoff**
5. **This file (AGENTS.md)** if this is your first session on this repo

## Validation commands

For PRs that touch repository content:

- `git status` — confirm clean working tree post-edits
- `git log --oneline -10` — confirm commit history matches expectations
- For markdown files: spot-check rendering (GitHub-flavored Markdown)
- Future: deterministic checks via `.github/workflows/` will run automatically on PR open (workflows ship in PR-7 of the v3 production sequence)

## Branch and PR expectations

- **Branch naming** per AMAS v2.14.1 §6.1: `<type>/task-####-<kebab-slug>`. Allowed types: `feat`, `fix`, `chore`, `docs`, `adr`, `refactor`, `test`, `ci`
- **PR template**: every PR uses `.github/PULL_REQUEST_TEMPLATE.md`. Required sections: Linked records, Summary, Decisions in this PR, Validation, Reviewer focus, Ready for review, AI Session Log
- **Conventional commit messages**: `<type>(<scope>): <subject>` — e.g., `feat(amas): TASK-0002 v3 package scaffold`
- **Per AMAS v2.14.1 §8.2**: Pre-flight verification before any destructive or remote-visible action
- **Per AMAS v2.14.1 §8.3**: Stop-and-show before `git push`, `gh pr create`, branch deletion, or force push

## Review guidelines

When invoked as Reviewer (`@codex review`), produce a Review Summary per AMAS v2.14.1 §17.7 with:

- **Findings classified by severity**: Blocking, Major, Minor (per template)
- **Validation of claims**: verify the Builder's claimed actions per §8.1.1.2 — claimed commits exist at claimed SHAs, claimed files exist at claimed paths, claimed follow-up artifacts (PRs, Issues, branches) exist, identifier patterns conform to project convention
- **Recommendation**: Approve / Request changes / Comment

If verification surfaces a phantom claim, name it explicitly and separate substantive review evidence from phantom-affected delivery layer per §8.1.1.2 adjudication discipline.

## Scope and escalation

- **Stay within the task's named scope**. Adjacent in-scope edits (one corresponding test, one corresponding doc, one helper file) are acceptable per §8.3; broader edits require explicit approval.
- **Escalate to the project owner via stop-and-show** for: scope drift, blocking questions, ambiguous acceptance criteria, ADR-conflict candidates, or any condition the handoff did not anticipate.
- **Do not merge**. The project owner runs all merges (currently solo-contributor bypass per AMAS v2.14.1 §10.5).

## Repo-specific notes

- Solo-contributor repo. Single CODEOWNER. Codex review runs in substantive-only mode per §8.1; the owner clicks merge after substantive findings are addressed.
- This is a meta-recursive context: framework changes affect the repo's own operating discipline. Cross-surface verify-before-assert per AMAS v2.14.1 §24 is especially load-bearing.
