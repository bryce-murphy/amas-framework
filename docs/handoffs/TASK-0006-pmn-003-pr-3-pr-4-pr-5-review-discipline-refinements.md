# HANDOFF: TASK-0006

## Metadata

- Task ID: TASK-0006 (matches Issue, PR, PMN-003 per §7.7.1)
- Linked Issue: none — chore-style PR per ADR-001 single-contributor convention
- Linked PR: PR-6 (https://github.com/bryce-murphy/amas-framework/pull/6)
- Linked ADR(s): ADR-001, ADR-002
- Linked Feature Brief: none — PMN authoring is not feature work
- Owner role: Builder (Claude Opus 4.7, Claude Code, owner's local session)
- Previous role: Architect (Claude Opus 4.7, Claude.ai Project)
- Timestamp (UTC): 21:15
- Last synced commit SHA: c1fd8d5 (PR-5 squash-merge SHA on main; Builder verifies at pre-flight via `git rev-parse origin/main` and updates if main has advanced)
- Branch: `chore/task-0006-pmn-003-pr-3-pr-4-pr-5-review-discipline-refinements`
- Status: proposed

## Objective

Place the Architect-authored PMN-003 content at `docs/post-merge-notes/PMN-003-pr-3-pr-4-pr-5-review-discipline-refinements.md`, place this handoff at `docs/handoffs/TASK-0006-pmn-003-pr-3-pr-4-pr-5-review-discipline-refinements.md`, place pre-commit Codex review evidence at `docs/reviews/PR-6-codex-pre-commit.md`, open PR-6 with placeholder substitutions complete, and hand back to Architect for §24.2(a) verification before merge.

## Last completed step

Architect completed authoring of PMN-003 content, this handoff, and the Builder prompt at the Architect surface (Claude.ai Project). §23.6 self-review pass completed before handoff. Three cycle's worth of field evidence (PR-3, PR-4, PR-5) consolidated into 7 observations across 3 clusters with 3 structural-fix recommendations. PMN-003 (a) discipline carryover (recapitulation re-check after in-cycle revisions) folded into (a)'s structural-fix wording per implicit refinement candidate from TASK-0005 cycle defect log.

## Current state

**Summary:** Three Architect-authored artifacts ready for placement-only by Builder. PMN-003 content is final-form; this handoff is final-form; the Builder prompt is final-form. Builder cycle is mechanical placement plus PR-open with the two deferred substitutions (timestamp, post-PR review state) handled at the appropriate cycle steps.

**Files to be authored by Builder:**

- `docs/post-merge-notes/PMN-003-pr-3-pr-4-pr-5-review-discipline-refinements.md` — content provided in Builder prompt; Builder saves verbatim except for the metadata `Date authored` field which the Builder fills with the YYYY-MM-DD at handoff creation.
- `docs/handoffs/TASK-0006-pmn-003-pr-3-pr-4-pr-5-review-discipline-refinements.md` — this handoff itself; Builder saves verbatim except for: (i) `Linked Issue` field (issue number or "none"), (ii) `Linked PR` field (filled post-PR-open with PR-6 number), (iii) `Timestamp (UTC)` field (HH:MM at handoff creation), (iv) `Last synced commit SHA` (verify against `origin/main` HEAD; update if main has advanced past `c1fd8d5`), (v) `Validation run` block (filled post-author with actual commands run and outputs), (vi) `Post-PR Codex review state` deferred until Codex review settles, (vii) `Sign-off` deferred until Architect §24.2(a) verification completes.
- `docs/reviews/PR-6-codex-pre-commit.md` — pre-commit Codex review-context file; Builder authors per PR-5 precedent at `docs/reviews/PR-5-codex-pre-commit.md`. Six claims to verify per Builder prompt §4 pre-commit Codex review block.

**Files changed (summary):**

- 3 files added under `docs/post-merge-notes/`, `docs/handoffs/`, `docs/reviews/`.
- No existing files modified.

## Decisions made

- **PMN-003 covers PR-3 + PR-4 + PR-5 cycles as a unified cluster** rather than splitting across multiple PMNs. Three-cycle evidence base; refinements update wording within observations rather than spawning new categories. Slug reflects three-cycle scope.
- **Implicit (a) refinement candidate from TASK-0005 cycle defect log absorbed** into (a)'s structural-fix wording. Adds a second §23.6 self-review checklist item (re-run recapitulation-consistency check after in-cycle path-(a) revisions touching multiple artifacts). Direct field-evidence basis from TASK-0005 cycle.
- **(g) open placement question not resolved at PMN-003.** Whether v3 `core.md` adds a fifth surface-specific section parallel to §8.2 for Architect-receiving-Builder-hand-back is deferred to v3 authoring time (PR-7 / PR-8). PMN-003 records the question informationally.
- **PMN-001 observation count standardized to 15** in this handoff and PMN-003 references. Prior session-handoff text contained inconsistent count (15/15/14); 15 is authoritative per project knowledge cross-reference.
- **PMN-001 slug reference deferred to Builder filesystem verification.** Architect cannot determine canonical slug from chat context; Builder verifies actual filename at pre-flight (`Get-ChildItem docs/post-merge-notes/PMN-001*` or `ls docs/post-merge-notes/PMN-001*`) and uses verbatim in any cross-references.

## Assumptions

- Repo state matches the snapshot in the Architect-to-Architect session-handoff: HEAD of main at `c1fd8d5`, no open PRs, branches clean. Builder pre-flight verifies.
- Codex Reviewer is operational (no §2.3.7 failover episode in flight). If Codex unavailable at pre-commit step, Builder hands back per §2.3.7 pause-and-preserve-state discipline.
- Branch protection on main is unchanged from the snapshot (Posture 2 — pull-request-only admin bypass via Rulesets; PRs required, 1 approval, code-owner review, conversation resolution, squash-only merge).
- Owner is available at the stop-and-show gate (after pre-commit Codex review and Architect adjudication, before commit) and at the post-PR `@codex review` invocation gate.

## Risks

- **Codex auto-fire on PR open may or may not occur** per PMN-003 (b) refined framing. Three-cycle evidence base is split (present in PR-3, PR-4; absent in PR-5). Builder discipline does not depend on auto-fire occurring; if it occurs, treat as standard sentinel signal and apply §8.1.1.2 phantom-action verification per AMAS v2.14.1.
- **Single-poll across both endpoints when timed too early is a §24.2(a) failure mode** per PMN-003 (e) refinement. Builder must re-poll, not single-poll, after `@codex review` trigger before asserting "no findings."
- **Path-(a) in-cycle revisions may surface during the pre-commit Codex review adjudication step.** Per PMN-003 (a) refinement, if path-(a) revision touches asserted facts in multiple artifacts (PMN body and review-context, or handoff and PMN body), Architect re-runs recapitulation-consistency check before stop-and-show. This is Architect-side discipline at adjudication time, not Builder-side.
- **PMN-001 slug filesystem-verification at pre-flight** has a small risk of mismatch with Architect-asserted reference. If mismatch surfaces, Builder applies §24.2(a) caveat-discipline ("the prompt says X; my actual finding is Y; here is the divergence") and hands back rather than silently working around.

## Blocking questions

None at handoff time. Builder cycle is placement-only with mechanical sequence in the prompt.

## Validation run

- Commands (pre-flight, §1):
  - `git fetch origin` → already up to date.
  - `git checkout main` → "Already on 'main'".
  - `git pull --ff-only origin main` → "Already up to date."
  - `git rev-parse HEAD` → `c1fd8d5d77ef346682b7742223a00ec35347e3cc` (matches Architect-asserted `c1fd8d5`).
  - `git rev-parse origin/main` → `c1fd8d5d77ef346682b7742223a00ec35347e3cc` (main has not advanced; Last synced commit SHA recorded as `c1fd8d5`).
  - `git status` → "On branch main … nothing to commit, working tree clean".
  - `gh pr list --state merged --limit 6` → PR #1, #2, #3, #4, #5 listed merged; PR #6 not present (matches assertion).
  - `gh pr list --state open` → empty (matches assertion).
  - `ls -la docs/post-merge-notes` → `.gitkeep`, `PMN-001-pr-0-pr-2-production-learnings.md`, `PMN-002-pr-3-cycle-learnings.md` (matches assertion; PMN-001 canonical filename `PMN-001-pr-0-pr-2-production-learnings.md`).
  - `ls docs/handoffs` → TASK-0001 through TASK-0005 (matches assertion; no TASK-0006 yet).
  - `ls docs/reviews` → PR-2, PR-3, PR-4, PR-5 codex-pre-commit files (matches assertion; no PR-6 yet).
  - `ls docs/adr` → ADR-001, ADR-002 (matches assertion).
- Results: pre-flight clean across all legs; no divergence from Architect-asserted state. Branch `chore/task-0006-pmn-003-pr-3-pr-4-pr-5-review-discipline-refinements` created via `git checkout -b` and verified via `git branch --show-current`.
- Evidence (placed-file blob hashes via `git hash-object`):
  - `docs/post-merge-notes/PMN-003-pr-3-pr-4-pr-5-review-discipline-refinements.md` — blob `ca05c38bf6606087f2fdf42e2d9faadc60626fc1`, 196 lines.
  - `docs/handoffs/TASK-0006-pmn-003-pr-3-pr-4-pr-5-review-discipline-refinements.md` — blob recomputes after this Validation-run substitution; pre-substitution blob `3a6c915deb96a5383f2ce4783f09bd4ed7bcc6c1`, 157 lines.
  - `docs/reviews/PR-6-codex-pre-commit.md` — blob `8d8428df63d31452237c1cf6465f7ec88a274f22`, 48 lines.
  - PR-6 URL: https://github.com/bryce-murphy/amas-framework/pull/6
- Post-edit Read-verify (PMN-003 (f)): structural headings (`#`, `##`, `###`) for all three placed files extracted via grep and confirmed matching Architect-prepared content (PMN-003 14 headings, TASK-0006 handoff 15 headings, PR-6 review-context 6 headings).

## Exact next step

Execute the following mechanical sequence. Hand-back point is **after PR-6 is open with placeholders substituted, after `@codex review` trigger, after both formal Codex endpoints settle non-empty OR a 5–10 minute settling period elapses with both endpoints stable empty**, before merge. Architect then performs §24.2(a) four-point verification per PMN-003 (g) before signing off for §10.5 single-contributor bypass merge.

1. **Pre-flight verification.** Run the verification block from the Architect-to-Architect session-handoff. Specifically:
   - `cd C:\Users\BryceMurphy\repos\amas-framework`
   - `git fetch origin`
   - `git checkout main`
   - `git pull --ff-only origin main`
   - `git rev-parse HEAD` — expect `c1fd8d5` or descendant; record actual SHA.
   - `git status` — expect clean.
   - `gh pr list --state merged --limit 6` — expect PR #1, #2, #3, #4, #5 listed merged; PR #6 not yet open.
   - `gh pr list --state open` — expect empty.
   - `Get-ChildItem docs/post-merge-notes` — expect `.gitkeep`, `PMN-001-*`, `PMN-002-*` (no PMN-003 yet); record actual PMN-001 filename.
   - `Get-ChildItem docs/handoffs` — expect TASK-0001 through TASK-0005 (no TASK-0006 yet).
   - `Get-ChildItem docs/reviews` — expect PR-2, PR-3, PR-4, PR-5 codex-pre-commit files (no PR-6 yet).
   - `Get-ChildItem docs/adr` — expect ADR-001, ADR-002.
   - **If verification fails on any leg, hand back to Architect with the divergence stated explicitly per §24.2(a) caveat-discipline.** Do not proceed.

2. **Branch creation.**
   - `git checkout -b chore/task-0006-pmn-003-pr-3-pr-4-pr-5-review-discipline-refinements`

3. **Author files.** Save the three Architect-prepared file contents from the Builder prompt to their target paths verbatim except for the explicitly-named substitutions:
   - PMN-003 file: substitute `Date authored` field with YYYY-MM-DD at handoff creation.
   - TASK-0006 handoff file: substitute `Linked Issue`, `Timestamp (UTC)`, `Last synced commit SHA` (verify against `origin/main` HEAD), and leave `Linked PR`, `Validation run`, `Post-PR Codex review state`, `Sign-off` as placeholder-deferred sections per the prompt's §5 substitution discipline.
   - PR-6 review-context file: author per the structure in the Builder prompt's §4.

4. **Pre-commit Codex review** (claim-verification-only, imperative phrasing per PMN-002 (a)). Use the prompt template provided in Builder prompt §4. Six claims to verify. Wait for Codex output. Record output verbatim into `docs/reviews/PR-6-codex-pre-commit.md`. If any finding is Blocking, hand back to Architect per PMN-001 (k); if Minor, surface to Architect for adjudication path (a) (revise) or (b) (record-and-proceed).

5. **§5 stop-and-show with placeholder-substitution audit (PMN-003 (d) discipline).** Enumerate ALL `(Builder fills with X)` and `(Builder updates with X)` patterns across ALL three files plus the prepared PR body. For each, name the substitution timing (now / at-PR-open / deferred-to-handback). Wait for owner approval before commit.

6. **Commit.** Single commit with message:
   ```
   chore(amas): TASK-0006 PMN-003 — PR-3 + PR-4 + PR-5 review-discipline refinements
   
   Adds PMN-003 capturing 7 observations across 3 clusters from
   PR-3, PR-4, and PR-5 review cycles, with 3 structural-fix
   recommendations to land in v3 canonical content authoring.
   
   Refs ADR-001, ADR-002, PMN-001, PMN-002,
        TASK-0003, TASK-0004, TASK-0005.
   ```

7. **Push.**
   - `git push -u origin chore/task-0006-pmn-003-pr-3-pr-4-pr-5-review-discipline-refinements`

8. **PR-open with placeholder substitutions complete.** Use the PR body template from the Builder prompt §6. Audit ALL placeholders in the PR body before submitting `gh pr create`.

9. **Owner invokes `@codex review`.** Anticipate per PMN-003 (b) refined: auto-fire may or may not occur on PR open; do not depend on it. Per PMN-003 (c) refined: substantive verdict comes via formal Pull Request Review + line-level comment endpoints; fast-response issue-level "Approve" stub is anti-channel and non-authoritative.

10. **Two-endpoint review-state check + re-poll discipline per PMN-003 (e) refined.** After `@codex review` trigger, do not assert "no findings" until either (i) at least one formal endpoint returns non-empty content, OR (ii) 5–10 minute settling period has elapsed with both endpoints stable empty. Single-poll OR single-endpoint check is §24.2(a) failure.
    - `gh pr view <N> --json reviews`
    - `gh api repos/bryce-murphy/amas-framework/pulls/<N>/comments`

11. **Address findings if any.** Path (a) revise / path (b) record-and-proceed adjudication runs through Architect. Maybe none, maybe Minor; treat any Blocking as escalation per PMN-001 (k).

12. **Hand back to Architect** with: PR-6 URL, Codex review state via both formal endpoints (verbatim outputs), branch state (`git status`, `git log -1`), and explicit assertion of "no findings" or "findings addressed at SHA X" with both-endpoints-verified evidence. Do not assert merge-readiness; that is the Architect's call after §24.2(a) verification per PMN-003 (g).

## Reassessment / expiry

- Hand-back gate at step 12 is the natural reassessment point. If the cycle stalls (Codex unresponsive, ambiguous review output, unexpected pre-commit findings requiring substantial revision), Builder hands back to Architect with state explicit; do not extend autonomous execution past the named hand-back point.
- TASK status flips to `resolved` only after Architect §24.2(a) verification clean, owner merge via §10.5, and Architect confirmation of merged state.

## Post-PR Codex review state

(Builder fills after step 12 hand-back with verbatim outputs from both formal endpoints. Section deferred-to-handback per §5 placeholder-substitution audit.)

- `gh pr view <N> --json reviews` output: 
- `gh api repos/bryce-murphy/amas-framework/pulls/<N>/comments` output: 
- Settling period observation: 
- Findings adjudication summary: 

## Sign-off

(Architect fills after §24.2(a) four-point verification per PMN-003 (g). Section deferred-to-handback per §5 placeholder-substitution audit.)

- §24.2(a) four-point verification:
  - PR comments via both endpoints checked verbatim against artifact:
  - Branch state checked:
  - File content against prescription (PMN-003 body, TASK-0006 handoff, PR-6 review-context):
  - Phantom-action audit:
- Architect sign-off for §10.5 single-contributor bypass merge:

## Session log archive (prior logs migrated from PR body per §13.1)

<!-- Append prior AI Session Logs here as new sessions happen, oldest at top, newest at bottom. Most recent log stays in the PR body, not here. -->
