---
status: drafted
---

# PR-80 Codex review

## Metadata

- PR: PR-80 (draft) — https://github.com/bryce-murphy/amas-framework/pull/80
- Branch: `feat/task-0047-batch-p3-retrofit-upgrade-prompts` per ADR-005 Option B + `github-reference.md` §2.2
- Cycle: TASK-0047 — Batch P3 retrofit kickoff prompt + adopter-runnability remediation (split cycle 2 of 2; PR-A). `prompts/upgrade.md` ships as PR-B.
- Linked handoff: `docs/handoffs/TASK-0047-batch-p3-retrofit-upgrade-prompts.md`
- Status: `drafted` | `recorded` — `drafted` pre-merge; flips to `recorded` post-merge per the PMN-018 path-scoped linked-pr-fix-up Action transition on `docs/reviews/`.
- Review model: draft-PR Codex GitHub-App **branch** reviews (post-push) + a Codex desktop comprehensive **red-team**. This was NOT a Codex desktop pre-commit pass, hence the artifact name `PR-80-codex-review` (the "-pre-commit" suffix would be a misnomer for this cycle).

## Review trail

### Codex GitHub-App branch review — pass 1 (reviewed commit `9fd363a`)
- **P2** `templates/handoff-template.md:69` — "Require the real PR number before fix-up". The TASK-0000 bootstrap-case note framed the `PR-0` sentinel as "works unchanged" because the linked-pr-fix-up Action substitutes the squash SHA. **Verified true** (§8.1.1.2) against `.github/scripts/linked-pr-fix-up.py`: the Action preserves the matched numeric token (`PR-{m.group(1)}`) and substitutes only the squash SHA; it never uses `PR_NUMBER` to rewrite `0`. A bootstrap handoff left at `PR-0` would merge to `linked_pr: PR-0 (squash SHA ...)` and permanently lose the real bootstrap PR link.
  - **Resolution — path-a, commit `2b5ec16`**: the handoff-template note now states `PR-0` is the pre-PR-open authoring sentinel and must be replaced with the actual bootstrap PR number once the PR is opened, before merge. Teaching the Action to rewrite the sentinel from the event PR number is noted as a v3.1 / Batch P4 candidate.

### Codex GitHub-App branch review — pass 2 (reviewed commit `2b5ec16`)
- **P2** `prompts/retrofit.md:223` — same finding-class re-raised on the prompt surface: the TASK-0000 bullet allowed `PR-0` as a committable default without the replace-before-merge caveat.
  - **Resolution — path-a, commit `66831ca`**: parallel correction to both prompts' TASK-0000 bullet (byte-identical) + a convergence sweep so every in-diff `PR-0` mention (both prompts, `handoff-template.md:69`, the ADR-009 worked-instance) carries or points to the replace-before-merge caveat. The PR-0-sentinel finding-class did not re-raise on the subsequent pass (closed).

### Codex desktop comprehensive red-team (reviewed commit `66831ca`)
3 P1 + 3 P2, all verified path-a; resolved in one batch (this commit):

- **P1-a** — review-context artifact missing though the handoff claimed it co-shipped. → This file created; handoff Objective + file-list references reconciled to the real artifact name/path.
- **P1-b** — handoff gate-current stale ("uncommitted; no PR") vs the committed + pushed branch (3 commits; PR-80 draft open). → All gate-current surfaces refreshed (Last-completed-step, Current-state, Cumulative-diff-stats, Exact-next-step).
- **P1-c** — `usage-guide.md` §2.3 lite-kickoff said "produces a smaller set," contradicting the prompts (run FULL at v3.0; lite forthcoming). → §2.3 reconciled.
- **P2-a** — upgrade routing points (greenfield preamble, retrofit preamble, usage-guide §2.2) routed to `prompts/upgrade.md` (a stub) without a forthcoming caveat. → "forthcoming; ships at PR-B" added at the routing points.
- **P2-b** — README retrofit Prompts-row used a cite-the-cycle form. → `PR-80 (TASK-0047)` filled-by convention (PR-80 verified at draft-open).
- **P2-c** — qualifier-sweep completion: `templates/project-brief-template.md` "forthcoming Batch P3"; `templates/ISSUE_TEMPLATE/project-initiation.md` prompt-set "ship-pending"; `usage-guide.md` §0 stale `TASK-0025+` / `TASK-0026+` appendix refs → v3.2-planned wording.
- A repo-wide convergence completion-sweep was run to force closure of each stale-reference class (see the handoff cycle-close ledger / this PR's batch commit).

## Cross-references

- `core.md` §17.7 review template; §8.1.1.1 three-endpoint poll; §8.1.1.2 phantom-action verification (which caught the phantom review-context claim, P1-a — a self-instantiation worth a cycle-close ledger note).
- ADR-009 (kickoff-artifact defaulting); PMN-018 (path-scoped Action transitions; `docs/reviews/` → `recorded`).
