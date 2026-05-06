# CLAUDE.md — amas-framework

Operating instructions for Claude (Claude Code, Claude.ai Projects) working on the `amas-framework` repository.

## Operating context

This repository **is** the AMAS framework. Work in this repo follows AMAS itself ("dogfooding"): the framework operates under its own rules.

- **Active framework version**: AMAS v3.0 (in development; current canonical materialization at v2.23 — see README)
- **Substrate canonical reference**: AMAS v2.14.1 lives at https://github.com/recruiting-tech/upcds/blob/main/docs/ai-operating-system.md and is the substrate from which the v3 canonical-law trio is being authored per ADR-003
- **Repository status**: AMAS v3.0 trio is in active production in this repository (canonical-law trio: `core.md`, `github-reference.md`, `usage-guide.md` — all materialized; full v3.0 package per ADR-003 D2 thirteen-substantive-PR sequence in progress).

## Mandatory read order (before any meaningful work)

1. **AMAS v3 canonical-law trio** (read in order; per `github-reference.md` §4.1):
   - `core.md` — role model, Reviewer disciplines (§8.1.1.1 / §8.1.1.2 / §8.1.1.3), PMN/ADR discipline (§17 / §18), Architect-side prompt construction including self-review (§23 / §23.6 / §23.6.1 / §23.6.2 / §23.6.3), cross-surface verify-before-assert (§24 / §24.2 / §24.3 / §24.3.1)
   - `github-reference.md` — GitHub-specific implementation (branch convention §2.2 per ADR-005, branch protection §3, templates §4, AI agent identity §5, deterministic Actions §6)
   - `usage-guide.md` — practical operating guidance (kickoff, first-task pattern, handoff/log lifecycle, ID conventions, Reviewer-output absorption, Architect-side disciplines)
2. **AMAS v2.14.1 canonical** (URL above) — substrate reference for sections not yet materialized in v3 trio. Especially relevant for Architect work: v2.14.1 §2.3.6 (agent-role prompt shapes; v3 substrate). For Builder work: v2.14.1 §8.2 (pre-flight; `(forthcoming at Part C+)` in v3 core.md), §8.3 (stop-and-show; same), §13 (AI Session Log; v3 substrate), §14 (handoff templates; v3 substrate).
3. **The active task handoff** at `docs/handoffs/TASK-####-<slug>.md`
4. **The PR description** if a PR already exists
5. **Relevant ADRs** in `docs/adr/`
6. **This file (CLAUDE.md)** on first session

## Validation commands

- `git status` — confirm clean working tree
- `git log --oneline -10` — verify commit history
- For markdown: spot-check rendering
- For ADR/handoff/PMN paths: confirm naming matches `core.md` §17 conventions (`docs/adr/ADR-###-<slug>.md`, `docs/handoffs/TASK-####-<slug>.md`, `docs/post-merge-notes/PMN-###-<slug>.md`)

## Branch and PR expectations

- Branch naming per `github-reference.md` §2.2 (canonical at v3; deliberately diverges from v2.14.1 §6.1 substrate per ADR-005): `<type>/task-####-<kebab-slug>`
- PR template at `.github/PULL_REQUEST_TEMPLATE.md` is required reading; populate every section
- Conventional commit messages
- v2.14.1 §8.2 pre-flight before remote-visible actions (substrate; `(forthcoming at Part C+)` in v3 core.md)
- v2.14.1 §8.3 stop-and-show with the owner before `git push`, `gh pr create`, or any destructive operation (substrate; same)

## Scope and escalation rules

- **Architect surface (Claude.ai Projects)**: authors Builder prompts per v2.14.1 §23.2 elements (substrate); runs `core.md` §23.6 self-review before tagging Reviewer (Codex). Does not write to the repo directly.
- **Builder surface (Claude Code)**: executes Architect handoffs; honors v2.14.1 §8.2 and §8.3 disciplines (substrate); hands back at named hand-back points; never merges.
- **Both**: escalate to owner on scope drift, blocking questions, or any condition the handoff did not anticipate.
- **Both**: claimed actions must be true. Do not narrate actions not actually performed. If a `core.md` §23.6 sweep cannot complete within session budget, hand back per v2.14.1 §23.6.5 (substrate) rather than handing partial work to the next surface.

## Repo-specific notes

- Solo-contributor repo, MIT-licensed, public.
- Codex (GPT-5.5) is the configured Reviewer. Cross-ecosystem from Builder (Claude Code) per v2.14.1 §2.3.1 (substrate).
- Reviewer invocation: the project owner posts `@codex review` after the PR opens. Builder does not invoke from its side.

## Meta-recursive caution

This repo's own work modifies the framework that governs the repo. When authoring v3 content, watch for cases where a proposed change to v3 implies a change to how this repo currently operates under v2.14.1. Surface those as decision-required for the owner; do not silently apply v3-shaped behavior to v2.14.1 work.
