---
template_version: 3.0.0
status: recorded
filled_by: PR-62 (TASK-0040)
---

# CLAUDE template

Canonical receiving-surface instruction file for Anthropic Claude AI products (Claude.ai Project, Claude Code CLI, Claude desktop, successor Claude products) operating at an AMAS-adopted repository. At an adopter project, this template is materialized as `CLAUDE.md` at repository root and declares receiving-surface identity, operational expectations, and project-specific overlay. AMAS canonical discipline applies identically across AI receiving surfaces; receiving-surface-specific operational depth lives in receiving-surface adapter packs at `appendices/receiving-surface-adapters/claude-code.md` per Batch P7 (ship-pending per ADR-006 D2 + ADR-007 batch sequence).

## §1. Receiving-surface identity

This file targets Anthropic Claude AI products at `<PROJECT NAME>`. Receiving-surface identity is fixed at this file; sibling receiving-surface canonical instruction files address other AI families:

- `AGENTS.md` — OpenAI Codex products (Codex desktop, Codex CLI, successor Codex products)
- `<OTHER>.md` — additional receiving surfaces per receiving-surface adapter packs (Batch P7; ship-pending)

Project-specific operational context that supplements canonical discipline lives at §8.

## §2. Reading order

Recommended reading order before any meaningful work at the receiving surface:

1. `README.md` — project-specific orientation
2. This file (`CLAUDE.md`) — receiving-surface identity + operational expectations
3. AMAS canonical-law trio: `core.md` + `github-reference.md` + `usage-guide.md`
4. Active TASK handoff at `docs/handoffs/TASK-####-<slug>.md`
5. PR description if a PR exists for the task
6. Linked ADRs referenced by the handoff (under `docs/adr/`)
7. Linked PMNs referenced by the handoff or ADRs (under `docs/post-merge-notes/`)

Reading order is adjustable by project per §8 overlay.

## §3. Operational expectations

Canonical-law §-sections governing receiving-surface AI agent operations:

- `core.md` §8.1 reviewer-output absorption + §8.1.1 channel handling + §8.1.1.3 cost-class refinement (bounded-continuation rule)
- `core.md` §10.5 single-contributor bypass
- `core.md` §14 + §14.1-§14.7 universal handoff schema + direction-specific variants
- `core.md` §17.5 template lifecycle + §17.7 review template
- `core.md` §18.1-§18.4 PMN trigger + form + version-bump criteria
- `core.md` §23.6 + §23.6.1.1 + §23.6.2 + §23.6.3 self-review disciplines (prose-arithmetic decomposition + iterative-to-fixed-point + reference-verification)
- `core.md` §24 + §24.3 + §24.3.1 + §24.5 + §24.6 cross-surface verify-before-assert + receiving-side caveat-discipline + Architect ← Builder hand-back symmetric-application + multi-surface review pipeline + Stop-Iteration framework
- `core.md` §8.2 pre-flight + §8.3 stop-and-show + §13 / §13.1 / §13.2 AI Session Log discipline

Receiving-surface-specific operational depth lives at `appendices/receiving-surface-adapters/claude-code.md` per Batch P7 (ship-pending).

## §4. Validation commands

Baseline validation commands at receiving surface:

- `git status` — confirm working tree state
- `git log --oneline -10` — confirm commit history matches expectations
- For markdown: spot-check GitHub-flavored Markdown rendering
- For canonical-law trio integrity: `grep -nE "^##+ §" <file>` enumerates §-section headings for spot verification
- Deterministic checks via `.github/workflows/` (Batch P4; ship-pending per ADR-006 D2 + ADR-007 batch sequence)

Project-specific validation commands (test runners, linters, type-checkers, deterministic format checks) live at §8.

## §5. Branch and PR expectations

Per `github-reference.md` §2.2 + ADR-005:

- Branch naming: `<type>/task-####-<kebab-slug>`; allowed types: `feat`, `fix`, `chore`, `adr`, `shadow`, `spike`
- PR template at `.github/PULL_REQUEST_TEMPLATE.md`; populate every section per `github-reference.md` §4.2
- Conventional commit messages: `<type>(<scope>): <subject>`
- Pre-flight verification before branch creation and before any repo-writing, destructive, or remote-visible action (`core.md` §8.2)
- Stop-and-show before `git push`, `gh pr create`, `gh pr edit`, branch deletion, or force push (`core.md` §8.3)

## §6. Review guidelines

When invoked as Reviewer per `core.md` §17.7:

- Findings classified by severity: Blocking / Major / Minor
- Validation of Builder claims per `core.md` §8.1.1.2 — claimed commits exist at claimed SHAs; claimed files exist at claimed paths; claimed follow-up artifacts (PRs, Issues, branches) exist; identifier patterns conform to project convention
- Recommendation: Approve / Request changes / Comment
- Phantom-claim handling per `core.md` §8.1.1.2 — if verification surfaces a phantom claim, name it explicitly and separate substantive review evidence from phantom-affected delivery layer

Claude products are most commonly engaged in Architect or Builder roles; Reviewer invocation is less common but supported per `core.md` §17.7. Receiving-surface-specific reviewer operational depth lives in the adapter pack at `appendices/receiving-surface-adapters/claude-code.md` (Batch P7; ship-pending).

## §7. Scope and escalation

- Stay within the named scope of the active task; out-of-scope work belongs at the handoff §Out-of-scope register or a follow-up cycle
- Escalate ambiguous conditions per `core.md` §10.5 + Architect-level adjudication
- Apply `core.md` §24.5 multi-surface review pipeline at canonical-text amendment cycles
- Honor `core.md` §24.6 Stop-Iteration framework at the reach 4+ canonical boundary

## §8. Project-specific overlay

<Adopter fills this section with project context that supplements AMAS canonical law.>

- Project name + repository URL
- Project-specific validation commands (test runners, linters, type-checkers, format checks)
- Project-specific branch protection rules + bypass policies
- Project-specific reviewer routing
- Project-specific MCP servers + tool inventory references
- Project-specific documentation-MCP mechanism per project-brief

<Project-specific overlay typically 10-30 lines at filled adopter surface.>

## §9. Cross-references

- AMAS canonical-law trio: `core.md`, `github-reference.md`, `usage-guide.md`
- Project ADRs at `docs/adr/`
- Project PMNs at `docs/post-merge-notes/`
- Project Feature Briefs at `docs/features/`
- Project handoffs at `docs/handoffs/`
- Receiving-surface adapter pack for Claude Code: `appendices/receiving-surface-adapters/claude-code.md` (Batch P7; ship-pending)
- Sibling receiving-surface canonical instruction file: `AGENTS.md` (OpenAI Codex products)
- Canonical artifact form references: `templates/handoff-template.md` + `templates/review-template.md` + `templates/post-merge-note-template.md`
