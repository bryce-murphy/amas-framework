# CLAUDE.md — amas-framework

Operating instructions for Claude (Claude Code, Claude.ai Projects) working on the `amas-framework` repository.

## Operating context

This repository **is** the AMAS framework. Work in this repo follows AMAS itself ("dogfooding"): the framework operates under its own rules.

- **Active framework version**: AMAS v2.14.1
- **Canonical reference**: AMAS v2.14.1 lives at https://github.com/recruiting-tech/upcds/blob/main/docs/ai-operating-system.md
- **Repository status**: AMAS v3.0 is in production in this repository via PR-2 through PR-8.

## Mandatory read order (before any meaningful work)

1. **AMAS v2.14.1 canonical** (URL above). Sections especially relevant for Architect work: §2.3.6 (agent-role prompt shapes), §23 (Architect-side prompt construction including §23.6 self-review), §24 (cross-surface verify-before-assert). For Builder work: §8.2 (pre-flight), §8.3 (stop-and-show), §13 (AI Session Log), §14 (handoff templates).
2. **The active task handoff** at `docs/handoffs/TASK-####-<slug>.md`
3. **The PR description** if a PR already exists
4. **Relevant ADRs** in `docs/adr/`
5. **This file (CLAUDE.md)** on first session

## Validation commands

- `git status` — confirm clean working tree
- `git log --oneline -10` — verify commit history
- For markdown: spot-check rendering
- For ADR/handoff/PMN paths: confirm naming matches §17 conventions (`docs/adr/ADR-###-<slug>.md`, `docs/handoffs/TASK-####-<slug>.md`, `docs/post-merge-notes/PMN-###-<slug>.md`)

## Branch and PR expectations

- Branch naming per §6.1: `<type>/task-####-<kebab-slug>`
- PR template at `.github/PULL_REQUEST_TEMPLATE.md` is required reading; populate every section
- Conventional commit messages
- §8.2 pre-flight before remote-visible actions
- §8.3 stop-and-show with the owner before `git push`, `gh pr create`, or any destructive operation

## Scope and escalation rules

- **Architect surface (Claude.ai Projects)**: authors Builder prompts per §23.2 elements; runs §23.6 self-review before tagging Reviewer (Codex). Does not write to the repo directly.
- **Builder surface (Claude Code)**: executes Architect handoffs; honors §8.2 and §8.3 disciplines; hands back at named hand-back points; never merges.
- **Both**: escalate to owner on scope drift, blocking questions, or any condition the handoff did not anticipate.
- **Both**: claimed actions must be true. Do not narrate actions not actually performed. If a §23.6 sweep cannot complete within session budget, hand back per §23.6.5 rather than handing partial work to the next surface.

## Repo-specific notes

- Solo-contributor repo, MIT-licensed, public.
- Codex (GPT-5.5) is the configured Reviewer. Cross-ecosystem from Builder (Claude Code) per §2.3.1.
- Reviewer invocation: the project owner posts `@codex review` after the PR opens. Builder does not invoke from its side.

## Meta-recursive caution

This repo's own work modifies the framework that governs the repo. When authoring v3 content, watch for cases where a proposed change to v3 implies a change to how this repo currently operates under v2.14.1. Surface those as decision-required for the owner; do not silently apply v3-shaped behavior to v2.14.1 work.
