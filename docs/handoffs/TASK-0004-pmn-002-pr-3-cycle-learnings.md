# HANDOFF: TASK-0004

## Metadata
- Task ID: TASK-0004
- Linked Issue: not opened (single-contributor convention observed on PR-1, PR-2, PR-3)
- Linked PR: #4 (assigned at `gh pr create` time)
- Linked ADR(s): ADR-001 (decision 8 reservation flex compounds; ADR-002 amendment now overdue per PMN-002 action items)
- Linked Feature Brief: not required per §7.2.1 (documentation-only, single-session, no user-visible behavior change)
- Linked PMN: PMN-002 (this PR authors)
- Owner role: Architect (Claude Opus 4.7, Claude.ai Project) authored content; Builder (Claude Code, Claude Opus 4.7, Windows) placing
- Previous role: N/A (new task this session)
- Timestamp (UTC): 2026-05-01 19:08 UTC
- Last synced commit SHA: `467768c5100a375f8b73ae5d6c8990f3db8aedc9` (PR-3 squash-merge SHA on `main`)
- Branch: `chore/task-0004-pmn-002-pr-3-cycle-learnings`
- Status: active

## Objective

Place PMN-002 (PR-3 cycle learnings) per AMAS v2.14.1 §18 form on a new branch, accompanied by this TASK-0004 handoff and the PR-4 pre-commit Codex review-context file. Open PR #4 against `main`. Documentation-only — three new files, zero modifications.

## Last completed step

Architect authored PMN-002 file content + this TASK-0004 handoff content + PR-4 review-context placeholder content. Architect ran §23.6 pre-handoff self-review (acceptance-criteria, internal-consistency, ADR-conflict — all passed). Builder prompt delivered as markdown file at `.claude/architect-prompts/TASK-0004-builder-prompt.md`.

## Current state

- Summary: Pre-flight not yet started; expected sequence is verify state → branch → author files → pre-commit review → stop-and-show → commit → push → PR open → hand back
- Files changed: 0 yet; expected 3 created

## Decisions made

- PMN-002 numbering per §18 per-project sequential (next after PMN-001).
- TASK-0004 assignment to PMN-002 PR per §7.7.1 (PMN-002 crosses six artifact types).
- ADR-001 decision 8 reservation flex compounds: PR-1 = TASK-0001, PR-2 = TASK-0002, PMN-001 = TASK-0003, PMN-002 = TASK-0004, v3 content sequence shifts to TASK-0005-through-TASK-0010. PMN-002 surfaces this as overdue ADR-002 work rather than further deferral.
- Pre-commit Codex desktop review included for this PR, framed as claim-verification-only direction shape with imperative `Action:` phrasing per PMN-002 observation (a) — meta-application of the discipline PMN-002 documents.
- Single-contributor Issue-skipping convention preserved (matches PR-1, PR-2, PR-3 pattern).
- File-based Builder direction (h.2) used for this Builder prompt.

## Assumptions

- HEAD on `main` is the PR-3 squash-merge SHA (Builder verifies at step 1)
- `docs/post-merge-notes/` contains `.gitkeep` and `PMN-001-pr-0-pr-2-production-learnings.md` only
- No existing TASK-0004 or PR-4 artifacts
- No other PRs open between PR-3 and this work (`gh pr list --state open` returns empty)
- Builder has `gh` CLI configured with push/PR-create permissions
- Codex desktop available for pre-commit review at step 6
- Owner available for §8.3 stop-and-show approval before commit

## Risks

- Pre-flight reveals state mismatch (e.g., open PR present that would shift the next PR number from #4) → stop and surface to Architect.
- Codex desktop pre-commit review surfaces substantive findings exceeding line-anchored prescribed scope → escalate per PMN-001 observation (k); do not self-assess.
- Codex desktop returns clarification request even with imperative phrasing → surface as a finding-shaped escalation; observation (a) discipline may need further refinement.
- Codex line-anchored evidence cites rendered-line-numbers diverging from as-written (anticipated per observation (b)); surface divergence cleanly rather than treat anchors as authoritative.

## Blocking questions

None at handoff creation.

## Validation run

- Commands: pre-flight (step 1) verifies repo state; no automated tests apply (documentation-only PR)
- Results: TBD (pre-flight execution at Builder time)
- Evidence: pre-flight output captured in this PR's session log; PR-4 review-context file documents pre-commit Codex review

## Exact next step

1. Run pre-flight verification per Architect-to-Builder prompt step 1; record PR-3 merge SHA
2. If pre-flight passes, create branch per step 2
3. Author three files per steps 3, 4, 5; substitute `<PR-3 merge SHA>` placeholders with the recorded value
4. Run pre-commit Codex desktop review per step 6 (claim-verification-only, imperative phrasing)
5. Update PR-4 review-context file with Codex output and adjudication per step 7
6. Substitute all `(Builder fills with X)` placeholders in PR body before `gh pr create` per observation (e) discipline
7. Stop-and-show per §8.3 before commit (step 8)
8. After owner approval: commit, push, gh pr create per steps 9, 10, 11
9. Hand back per step 12

## Reassessment / expiry

Handoff status flips to `resolved` after PR #4 is merged. If pre-commit Codex review exceeds scope or owner declines stop-and-show, status flips to `blocked` pending Architect direction.

## Session log archive

(not yet populated; new task, single session expected)
