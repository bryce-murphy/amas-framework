# HANDOFF: TASK-0003

## Metadata
- Task ID: TASK-0003
- Linked Issue: not opened (single-contributor convention observed on PR-1 and PR-2)
- Linked PR: #3 (assigned at `gh pr create` time)
- Linked ADR(s): ADR-001 (decision 8 reservation flex documented in PMN-001 action items; ADR-002 deferred)
- Linked Feature Brief: not required per §7.2.1 (documentation-only, single-session, no user-visible behavior change)
- Owner role: Architect (Claude Opus 4.7, Claude.ai Project) authored content; Builder (Claude Code, Claude Opus 4.7, Windows) placing
- Previous role: N/A (new task this session)
- Timestamp (UTC): 2026-05-01 17:40
- Last synced commit SHA: `0e7eef4` (PR-2 squash-merge SHA on `main`)
- Branch: `chore/task-0003-pmn-001-production-learnings`
- Status: active

## Objective

Place PMN-001 (PR-1 + PR-2 production learnings) per AMAS v2.14.1 §18 form on a new branch, accompanied by this TASK-0003 handoff and the PR-3 pre-commit Codex review-context file. Open PR #3 against `main`. Documentation-only — three new files, zero modifications.

## Last completed step

Architect authored PMN-001 file content + this TASK-0003 handoff content + PR-3 review-context placeholder content. Architect's first attempt used in-chat block delivery (h.1); chat-rendering distortion surfaced in dialogue with owner; Architect adopted file-based delivery (h.2) in-cycle and added (h.2) as a new PMN-001 observation. Architect ran §23.6 pre-handoff self-review (acceptance-criteria, internal-consistency, ADR-conflict — all passed against the 15-observation final form). Builder prompt delivered as markdown file at `.claude/architect-prompts/TASK-0003-builder-prompt.md`; owner saved file to that path before invoking Builder.

## Current state

- Summary: Pre-flight not yet started; expected sequence is verify state → branch → author files → pre-commit review → stop-and-show → commit → push → PR open → hand back
- Files changed: 0 yet; expected 3 created

## Decisions made

- PMN-001 numbering correction at session start: prior-session Architect proposed PMN-004; current Architect corrected to PMN-001 per §18 per-project numbering (verified against empty `docs/post-merge-notes/.gitkeep`).
- TASK-0003 assignment to PMN-001 PR per §7.7.1 (PMN-001 crosses six artifact types: branch, commits, PR, PMN file, handoff, review-context).
- ADR-001 decision 8 reservation flex from TASK-0001-through-0008 to TASK-0001-through-0009 with PMN-001 = TASK-0003 interleaved between bootstrap (TASK-0001) and v3 content sequence (now TASK-0004 through TASK-0009). Documentation of this flex deferred to PR-3 prompt time or to ADR-002 if owner prefers explicit ADR — per PMN-001 action items.
- Joint coverage of PR #1 + PR #2 in PMN-001 (rather than separate retrospective PMNs) per §18 mid-life adoption discretion.
- Pre-commit Codex desktop review included for this PR despite documentation-only nature, framed as claim-verification-only direction shape. Rationale: PMN-001 contains 15 observations whose factual fidelity benefits from external Reviewer perspective; cycle cost is low for one targeted invocation.
- File-based Builder direction (h.2) adopted for this Builder prompt per real-time discovery: in-chat block delivery (h.1) was attempted first and failed for ~6k words of content with embedded file bodies and nested code fences; chat-rendering distortion surfaced via owner feedback; file-based pattern adopted and codified as PMN-001 observation (h.2) in-cycle.
- Single-contributor Issue-skipping convention: no GitHub Issue opened for TASK-0003 (matches observed PR-1 and PR-2 pattern).

## Assumptions

- HEAD on `main` is `0e7eef4...` (PR-2 squash-merge SHA)
- `docs/post-merge-notes/` contains only `.gitkeep`
- No existing TASK-0003 or PR-3 artifacts
- Builder has `gh` CLI configured with push/PR-create permissions to `bryce-murphy/amas-framework`
- Codex desktop available for pre-commit review at step 6
- Owner available for §8.3 stop-and-show approval before commit

## Risks

- Pre-flight reveals state mismatch (e.g., new commits on `main` since handoff authored) → stop and surface to Architect.
- Codex desktop pre-commit review surfaces substantive findings exceeding line-anchored prescribed scope → escalate per observation (k) edge-case escalation pattern; do not self-assess.
- Encoding misdiagnosis recurrence on review-capture pipeline (per observations d/e/f) → use byte-safe diff capture if any review pipeline is engaged: `cmd /c "chcp 65001 >nul && git diff > <file>"` from PowerShell 5.1; native UTF-8 from PowerShell 7+ if available.

## Blocking questions

None at handoff creation. Builder surfaces any that arise via §8.3 stop-and-show.

## Validation run

- Commands: pre-flight (step 1) verifies repo state; no automated tests apply (documentation-only PR; no code changes)
- Results: TBD (pre-flight execution at Builder time)
- Evidence: pre-flight output captured in this PR's session log; PR-3 review-context file documents pre-commit Codex review

## Exact next step

1. Run pre-flight verification per Architect-to-Builder prompt step 1
2. If pre-flight passes, create branch per step 2
3. Author three files per steps 3, 4, 5
4. Run pre-commit Codex desktop review per step 6 (claim-verification-only direction)
5. Update PR-3 review-context file with Codex output and adjudication per step 7
6. Stop-and-show per §8.3 before commit (step 8)
7. After owner approval: commit, push, gh pr create per steps 9, 10, 11
8. Hand back per step 12 with PR URL + Codex review verbatim + pre-flight evidence

## Reassessment / expiry

Handoff status flips to `resolved` after PR #3 is merged. If pre-commit Codex review exceeds scope or owner declines stop-and-show, status flips to `blocked` pending Architect direction.

## Session log archive

(not yet populated; new task, single session expected)
