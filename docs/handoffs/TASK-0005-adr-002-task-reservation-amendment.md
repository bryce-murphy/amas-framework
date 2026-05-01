# HANDOFF: TASK-0005

## Metadata
- Task ID: TASK-0005
- Linked Issue: not opened (single-contributor convention observed on PR-1, PR-2, PR-3, PR-4)
- Linked PR: #5 (assigned at `gh pr create` time)
- Linked ADR(s): ADR-002 (this PR authors); amends ADR-001 decision 8
- Linked Feature Brief: not required per §7.2.1 (documentation-only, single-session, no user-visible behavior change)
- Linked PMN: PMN-001 (deferred follow-up flagged), PMN-002 (escalated ADR-002 as overdue), PMN-003 (forthcoming as TASK-0006)
- Owner role: Architect (Claude Opus 4.7, Claude.ai Project) authored content; Builder (Claude Code, Claude Opus 4.7, Windows) placing
- Previous role: N/A (new task this session)
- Handoff timestamp (Builder local): 2026-05-01 15:56:55 EDT
- Handoff timestamp (UTC): 2026-05-01 19:56:55 UTC
- Last synced commit SHA: `5337b30621188c9337c296ea3d4dc65a32628b25` (PR-4 squash-merge SHA on `main`)
- Branch: `chore/task-0005-adr-002-task-reservation-amendment`
- Trigger basis: architecture change (ADR amendment to ADR-001 decision 8)
- Status: active

## Objective

Single-purpose amendment PR. Authors three files on a new branch and opens PR #5 against `main`:

1. `docs/adr/ADR-002-task-reservation-amendment.md` — ADR-002 substantive content amending ADR-001 decision 8: reservation extends from TASK-0001-through-0008 to TASK-0001-through-0012; PMN-insertion pattern recognized as a regular reservation feature.
2. `docs/handoffs/TASK-0005-adr-002-task-reservation-amendment.md` — this handoff.
3. `docs/reviews/PR-5-codex-pre-commit.md` — pre-commit Codex review-context, claim-verification-only direction shape with imperative `Action:` phrasing per PMN-002 (a).

Documentation-only — three new files, zero modifications.

## Last completed step

Architect authored ADR-002 file content + this TASK-0005 handoff content + PR-5 review-context placeholder content. Architect ran §23.6 pre-handoff self-review (acceptance-criteria, internal-consistency, ADR-conflict, recapitulation-consistency — all passed). Builder prompt delivered as markdown file at `.claude/architect-prompts/task-0005-adr-002-prompt.md`.

## Current state

- Summary: Pre-flight complete; branch created; three files authored on branch; staging next; expected sequence is stage → stop-and-show staged content → owner triggers pre-commit Codex → adjudication → placeholder-substitution audit → commit → push → PR open → post-PR Codex review absorption (two-endpoint) → hand back
- Files changed: 3 created on branch (uncommitted at handoff authoring time; staged before commit)

## Decisions made

- ADR-002 authored as standalone amendment ahead of PMN-003 (TASK-0006) per Architect-recommended robustness option: decouples reservation administration from PMN substantive content. Each TASK slot maps to one canonical artifact class.
- Reservation extension (TASK-0001 through TASK-0012) accommodates two existing PMN PRs in the range plus the present ADR-002 amendment plus PMN-003 anticipated next, with six remaining slots for substantive v3 content PRs (TASK-0007 through TASK-0012).
- PMN-insertion pattern recognized in ADR-002 Decision 3 as a framework feature, not an exception; future PMN-driven reservation extensions follow the ADR-002 pattern.
- Form adaptation to existing in-repo conventions: ADR-002 status block normalized to ADR-001's `## Status\n\nAccepted — DATE` layout (not the architect-spec `**Status**:` bold-key layout); related-records section named `## Evidence / references` to match ADR-001; "Amends" annotation placed under Status as a single line. ADR-002 omits an "Alternatives considered" section because the small-amendment scope did not surface deliberated alternatives.
- Form adaptation for handoff: TASK-0003 / TASK-0004 schema (Metadata / Objective / Last completed step / Current state / Decisions made / Assumptions / Risks / Blocking questions / Validation run / Exact next step / Reassessment / expiry / Session log archive) preserved as the spine; architect-spec sections (Architect §23.6 pre-handoff self-review / Pre-commit Codex review state / Post-PR Codex review state / Sign-off) appended as additional sections at the end where the existing schema has no slot.
- Form adaptation for review-context: PR-3 / PR-4 schema (status block / Direction shape / Codex desktop request / Codex output / Findings / Adjudication / Final state at commit) preserved as the spine; architect-spec content (Source-of-truth context / Claims / Reviewer output expected) folded into the `## Codex desktop request` code fence with imperative `Action:` directives per PMN-002 (a).
- Pre-commit Codex desktop review framed as claim-verification-only (six claims) with imperative phrasing per PMN-002 (a) field evidence.
- Single-contributor Issue-skipping convention preserved (matches PR-1 through PR-4 pattern).
- File-based Builder direction (h.2) used for this Builder prompt.

## Assumptions

- HEAD on `main` is `5337b30621188c9337c296ea3d4dc65a32628b25` (PR-4 squash-merge SHA); verified at pre-flight.
- `docs/post-merge-notes/` contains `.gitkeep`, `PMN-001-pr-0-pr-2-production-learnings.md`, `PMN-002-pr-3-cycle-learnings.md`; verified at pre-flight.
- No existing TASK-0005, PR-5, or ADR-002 artifacts; verified at pre-flight (`docs/adr/` contains only ADR-001).
- No other PRs open between PR-4 and this work (`gh pr list --state open` returned empty); verified at pre-flight.
- 71 tracked files in repo at branch point; verified at pre-flight.
- Builder has `gh` CLI configured with push/PR-create permissions to `bryce-murphy/amas-framework`.
- Codex desktop available for pre-commit review at §4.
- Owner available for §8.3 stop-and-show approval before commit and at hand-back.

## Risks

- Pre-commit Codex review surfaces a Major or Blocking finding → escalate per PMN-001 (k); do not self-assess.
- Codex line-anchored evidence cites rendered-line-numbers diverging from as-written (anticipated per PMN-002 (b)); surface divergence cleanly rather than treat anchors as authoritative.
- Post-PR `@codex review` auto-fire on PR-open produces phantom-action narrative (claimed commits / claimed files) before any explicit trigger per PMN-003 (b) anticipated co-occurrence of §8.1.1.1 + §8.1.1.2; Builder runs four-claim-category phantom-action verification BEFORE treating auto-fire as substantive.
- Single-endpoint review-state check is §24.2(a) external-system-behavior assertion failure per PMN-003 (e); Builder runs both `gh pr view --json reviews` AND `gh api repos/bryce-murphy/amas-framework/pulls/5/comments` before any "no findings" assertion.
- Placeholder-substitution audit must enumerate placeholders across all three committed artifacts, not just the PR body, per PMN-003 (d); audit step (§5) is the structural fix.
- Heading-preservation discipline per PMN-003 (f) on any in-cycle Edit operation that touches `##`-or-higher structural headings.

## Blocking questions

None at handoff creation. Form-adaptation deviations enumerated under "Decisions made" above and surfaced to owner at the §4 staged-content stop-and-show.

## Validation run

- Commands: pre-flight (§2) verified repo state; no automated tests apply (documentation-only PR; no code changes).
- Results: pre-flight passed — HEAD `5337b30...`, working tree clean, 71 tracked files, four PRs merged, none open, expected directory contents present.
- Evidence: pre-flight output captured in this PR's Builder session log; PR-5 review-context file documents pre-commit Codex review.

## Exact next step

1. Stage three files; surface raw `git status` and full file content to owner per §4 step 2 stop-and-show.
2. Owner reviews staged content and triggers pre-commit Codex review per ADR-001 decision 11. Direction shape: claim-verification-only per the §3.3 review-context file with imperative `Action:` phrasing per PMN-002 (a).
3. Builder receives Codex output; reports per-claim severity verbatim (no Builder reframing).
4. Architect adjudicates each finding; Architect adjudication recorded in `## Adjudication / fix-up` of the review-context file.
5. If any path-(a) revision: revise, re-stage, re-run pre-commit. At most one revision cycle anticipated.
6. Stop-and-show with placeholder-substitution audit per §5 + PMN-003 (d).
7. After owner approves: commit (single squash commit), push, `gh pr create` per §6.
8. Post-PR Codex review absorption: anticipate §8.1.1.1 + §8.1.1.2 co-occurrence per PMN-003 (b); run two-endpoint review-state check per PMN-003 (e); report substantive verdict per PMN-003 (c) channel observed.
9. Hand-back to Architect per §9 with two-endpoint review-state evidence; Architect runs §24.2(a) caveat-discipline verification per PMN-003 (g) before merge sign-off.

## Reassessment / expiry

Handoff status flips to `resolved` after PR #5 is merged. If pre-commit Codex review exceeds scope or owner declines stop-and-show, status flips to `blocked` pending Architect direction.

## Session log archive

(not yet populated; new task, single session expected)

## Architect §23.6 pre-handoff self-review

Architect ran the §23.6 pre-handoff self-review before issuing the Builder prompt at `.claude/architect-prompts/task-0005-adr-002-prompt.md`:

- **Acceptance-criteria sweep**: ADR-002 substantive content covers reservation extension (TASK-0001 through TASK-0012), reservation accounting table, PMN-insertion pattern recognition, consequences, related records. All four ADR canonical sections (Context / Decision / Consequences / Related records) present.
- **Internal-consistency check**: TASK reservation table consistent with ADR-001 decision 8 baseline; PR/TASK numbering consistent across ADR-002 body, this handoff, the pre-commit review-context, and the PR body. PMN-001 / PMN-002 / PMN-003 cross-references resolve to repo paths.
- **ADR-conflict check**: ADR-002 explicitly amends ADR-001 decision 8; no other ADR-001 decisions modified; no other ADRs in scope.
- **Recapitulation-consistency check** (PMN-003 (a) preview discipline): factual content recapitulated across ADR-002 body, this handoff, and the pre-commit review-context — TASK reservation accounting, PMN cross-references, branch/PR identifiers — verified consistent at Architect-prompt authoring time.

## Pre-commit Codex review state

- Claim 1 (ADR-001 decision 8 baseline reservation): None
- Claim 2 (TASK-0003 / TASK-0004 artifact-class mapping): None
- Claim 3 (PMN-001 deferred-follow-up language): None
- Claim 4 (PMN-002 escalation language): None
- Claim 5 (ADR-002 internal cross-reference resolution): None
- Claim 6 (Reservation accounting table internal consistency): None

6× None, "Verified clean." No Architect adjudication required (no findings Minor or above). One Codex Claim-5 directory-vs-filename observation classified as None severity by Codex and disposed without fix-up; ADR-002's directory-scope reference for the five-handoff range is intentional. See `docs/reviews/PR-5-codex-pre-commit.md` `## Adjudication / fix-up` for full disposition.

## Post-PR Codex review state

(Builder fills this section at handoff finalization, after post-PR Codex review completes. Format: substantive verdict text from COMMENTED body OR confirmation of boilerplate-only-body equivalent verdict per PMN-003 (c) channel (i) or (ii); §8.1.1.2 phantom-action verification result against any auto-fire output per PMN-003 (b); two-endpoint review-state evidence per PMN-003 (e) — both `gh pr view --json reviews` rollup and `gh api repos/bryce-murphy/amas-framework/pulls/5/comments` line-level comments check.)

## Sign-off

(Architect fills this line after §24.2(a) caveat-discipline verification of Builder hand-back claims per PMN-003 (g): cross-references PR comments via both API endpoints, branch state via `git log` / `git ls-tree`, and ADR-002 / handoff / review-context content against actual committed file content. Sign-off is conditional on verification matching Builder's hand-back claims.)
