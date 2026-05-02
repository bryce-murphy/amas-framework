# HANDOFF: TASK-0008 — PMN-004 PR-7 cycle learnings

## Metadata

- Task ID: TASK-0008
- Linked Issue: n/a (PMN-tracked; PMN-004 is the deliverable)
- Linked PR: <FILL AT PR-OPEN — substitute actual PR URL after `gh pr create` returns; per PMN-001 (k) handling>
- Linked ADR(s): ADR-003 (PMN-004 inserts under Decision 3 contingency budget; consumes one of seven slots)
- Linked PMN(s): PMN-001, PMN-002, PMN-003 (PMN-004 builds on the lineage; specifically refines PMN-003 (a) and confirms PMN-003 (e) empirically)
- Linked Feature Brief: n/a (PMNs do not have associated Feature Briefs)
- Linked review-context file: `docs/reviews/PR-8-codex-pre-commit.md`
- Owner role: Architect (Claude.ai) → Builder (Claude Code)
- Previous role: Architect produced this handoff and the PMN-004 spec from the Builder's PR-7 close hand-back observations
- Timestamp (UTC): 2026-05-02T02:33:28Z
- Last synced commit SHA: 4ac4640 (squash-merge of PR-7 on main, 2026-05-02T01:55:11Z)
- Branch: chore/task-0008-pmn-004-pr-7-cycle-learnings
- Status: active
- Direction: Architect → Builder (universal handoff schema, AMAS v2.14.1 §14.1)
- Framework version: AMAS v2.14.1 (dogfooded)

## Objective

Author PMN-004 documenting the PR-7 cycle learnings: claim-text drift across multiple authored surfaces as a recurrent defect class with refined mitigations, empirical case for keeping the pre-commit Codex desktop review gate, empirical confirmation of PMN-003 (e) refined two-endpoint discipline. Six refined disciplines articulated for application to all subsequent cycles. The PMN-004 PR is small (3 files: PMN + handoff + review-context); no README sweep, no ADR amendment, no scaffold-stub modification. The README "Canonical law" row staying briefly stale (forecasting PR-8 = core Part A; reality PR-8 = PMN-004) is the explicit first test of the per-PR-row-update discipline ADR-003 §Consequences established. PR-9 (next substantive cycle, core Part A authoring) Builder will reconcile the row at content-fill time.

## Last completed step

Architect verified repo state at SHA 4ac4640, received Builder PR-7 close hand-back (8 sections covering cycle outcome, verification chain, 5 candidate observations, path A vs path B framing for PMN-004 timing, README durability test framing, 6 carryforward disciplines, repo-state ground truth, reassessment), confirmed all seven strategic decisions plus three open-question recommendations ("ship it" 2026-05-02), authored this handoff and the PMN-004 spec.

## Current state

- Summary: `main` is at 4ac4640 with 80 tracked files. Local clone clean. Branch protection on `main` per ADR-001 decision 9 + posture-2 admin bypass via Rulesets.
- Files changed: none yet at handoff hand-off.

## Decisions made

- PMN-004 timing: path A (PMN-004 first, before TASK-0009 core Part A authoring). Three reasons: established PMN-after-cycle cadence; quality dependency on canonical-content authoring (canonical disciplines must be canonical before being applied to canonical content); observation freshness.
- PMN-004 scope: consolidated single PMN with five sub-findings synthesized into three substantive sections plus refined disciplines summary plus cross-references. Splitting into multiple PMNs dilutes the lesson; consolidated PMNs are established norm (PMN-001/002/003 all consolidated).
- PR-8 file count: exactly 3 (3 new + 0 modified). Same shape as PMN-003 / PR-6. No README sweep; ADR-003 §Consequences explicitly establishes per-PR-row-update discipline.
- Branch slug: `chore/task-0008-pmn-004-pr-7-cycle-learnings` (parallels PMN-003 precedent `chore/task-0006-pmn-003-pr-3-pr-4-pr-5-review-discipline-refinements`).
- Renumbering: ADR-003's anticipated PR-8-through-PR-19 substantive content sequence shifts +1; canonical content authoring now starts at PR-9 (TASK-0009 core Part A). Already budgeted by ADR-003 Decision 3.
- M-A6 monitoring item: added now (not deferred). PMN-rate-vs-budget tracking; current rate 3 PMNs in 7 cycles = 43% within ADR-003 forecast range (23-54%). Promotion trigger at TASK-0023 (3 contingency slots remaining).
- All six §5 disciplines from Builder hand-back: applied to this deliverable's authoring; carried forward to all subsequent specs.

## Assumptions

- TASK-0008 is the next available TASK number (verified in step 1 pre-flight: `ls docs/handoffs` returns 7 files TASK-0001 through TASK-0007).
- PMN-004 is the next available PMN number (verified in step 1: `ls docs/post-merge-notes` returns 3 files PMN-001 through PMN-003).
- Base SHA `4ac4640` is current `main` (verified in step 1).
- Branch protection on `main` is live and configured per ADR-001 decision 9.
- `gh` CLI authenticated with `repo` scope minimum.
- Codex desktop is available to the owner for step 7 pre-commit review.

## Risks

- **Future-tense claim defect (PMN-004 §5 discipline (c))**: Builder claims about action-execution at pre-commit time must be verifiable at pre-commit time. No claim of the form "will be substituted at PR-open" is acceptable in pre-commit Builder claims; the substitution itself happens post-PR-open via fix-up commit per PMN-001 (k). Mitigation: §7 step-10 self-verification explicitly checks each claim's verification command runs successfully against the working tree before pre-commit.
- **Cross-surface count claim drift**: file count claim "3" appears in PR body (§6.3), this handoff (Validation run Evidence), PMN-004 §1 cycle context (no), PR-8 review-context (claim 7). Three surfaces total. All three must agree on the number 3. Mitigation: §23.6 prose-arithmetic decomposition (PMN-004 §5 discipline (e)) is pre-applied by Architect in this spec; verified at §10 self-review.
- **Severity-taxonomy compliance**: PR-8 review-context file enumerates Blocking / Major / Minor (three-level repo discipline per Meta-observation 1 of PR-6→PR-7 incoming session handoff and confirmed standing per PMN-004 §5 discipline (a)). Verified at §10 self-review of this spec.
- **Phantom-action surface in Builder hand-back**: claims about file existence, content, and counts must be directly verifiable from working-tree filesystem and `git diff` output at hand-back time. Mitigation: Builder's hand-back lists each claim with its verification command and observed result.
- **Verification-command portability (PMN-004 §5 discipline (b))**: pre-commit verification commands provided in both bash and Windows cmd forms in §3.1 pre-flight, §7 step-10 self-verification, and §8 Codex pre-commit prompt. Builder runs whichever shell is available; Codex desktop runs the cmd/PowerShell form if executing on Windows.

## Blocking questions

None at handoff time. If any surface during execution, stop and surface to owner via stop-and-show §9.

## Validation run

Filled by Builder at step-10 self-verification per §7 of the spec, against the working tree at branch tip on `chore/task-0008-pmn-004-pr-7-cycle-learnings` prior to Codex desktop pre-commit review (per PMN-004 §5 discipline (c) — no future-tense claims at pre-commit time).

- **Commands** (bash, Git Bash on Windows 11):
  - Claim 1: `[ -f docs/post-merge-notes/PMN-004-pr-7-cycle-learnings.md ] && head -1 docs/post-merge-notes/PMN-004-pr-7-cycle-learnings.md`
  - Claim 2: `[ -f docs/handoffs/TASK-0008-pmn-004-pr-7-cycle-learnings.md ] && head -1 docs/handoffs/TASK-0008-pmn-004-pr-7-cycle-learnings.md`
  - Claim 3: `[ -f docs/reviews/PR-8-codex-pre-commit.md ] && head -1 docs/reviews/PR-8-codex-pre-commit.md`
  - Claim 4: `git status --porcelain | wc -l`
  - Claim 5: `git status --porcelain | grep -v "^?? docs/" | wc -l`
  - Claim 6 (read-only): `git ls-files | wc -l` (returns `80`) + `git status --porcelain | grep -c "^?? "` (returns `3`) → arithmetic sum `83`
  - Claim 7: `grep -c "3 files\|3 new\|count: 3\|exactly 3" docs/handoffs/TASK-0008-pmn-004-pr-7-cycle-learnings.md docs/reviews/PR-8-codex-pre-commit.md`
  - Claim 8: `grep -c "Blocking / Major / Minor" docs/reviews/PR-8-codex-pre-commit.md`
  - Claim 9: `grep -E "^## §[0-9]" docs/post-merge-notes/PMN-004-pr-7-cycle-learnings.md | wc -l`
  - Claim 10: `grep -cE "§[0-9]+" docs/handoffs/TASK-0008-pmn-004-pr-7-cycle-learnings.md docs/reviews/PR-8-codex-pre-commit.md` (lists §-citation-bearing lines for visual sweep)
  - Encoding: `grep -c "—" docs/post-merge-notes/PMN-004-pr-7-cycle-learnings.md` (lines) and `grep -o "—" docs/post-merge-notes/PMN-004-pr-7-cycle-learnings.md | wc -l` (occurrences); PowerShell smart-quote scan (U+2018/U+2019/U+201C/U+201D) across all three files
- **Results**:
  - Claim 1: PASS — first line `# PMN-004 — PR-7 cycle learnings: claim-text drift defect class + pre-commit discipline confirmation + two-endpoint empirical validation`
  - Claim 2: PASS — first line `# HANDOFF: TASK-0008 — PMN-004 PR-7 cycle learnings`
  - Claim 3: PASS — first line `# PR-8 Codex desktop pre-commit review context`
  - Claim 4: PASS — `git status --porcelain | wc -l` returns `3`; three `?? docs/...` entries (PMN-004, TASK-0008 handoff, PR-8 review-context)
  - Claim 5: PASS — `git status --porcelain | grep -v "^?? docs/" | wc -l` returns `0` (no file outside the three new artifacts is touched)
  - Claim 6: PASS (read-only) — `git ls-files | wc -l` returns `80` (baseline tracked, unchanged from base SHA `4ac4640`); `git status --porcelain | grep -c "^?? "` returns `3` (new untracked); arithmetic sum `80 + 3 = 83` would-be-tracked-post-merge. No `git add -A` invoked; `.git/index.lock` not touched at any point during step-10 or Codex pre-commit verification.
  - Claim 7: PASS — `grep -c` returns `6` matches in handoff and `6` in review-context; total `12 ≥ 4`. PowerShell `Select-String ... -Pattern '3 files|3 new|count: 3|exactly 3'` returns `12` total. Pre-commit-existing surfaces (handoff §"Validation run" Evidence + review-context claims 4, 5, 7) all agree on `3`.
  - Claim 8: PASS — `grep -c "Blocking / Major / Minor" docs/reviews/PR-8-codex-pre-commit.md` returns `5`; satisfies "2 or more"
  - Claim 9: PASS — `grep -cE "^## §[0-9]" docs/post-merge-notes/PMN-004-pr-7-cycle-learnings.md` returns `8`; PowerShell `(Select-String -Path ... -Pattern '^## §[0-9]').Count` returns `8`; PMN-004 has 8 §-section level-2 headers (§1 through §8). Native cmd `findstr /r` form was unreliable on Windows due to OEM/UTF-8 codepage mismatch on the `§` byte (returns 12 spurious matches against `## Status` and `### §2.x` subheaders); PowerShell form supplied as cmd-side equivalent per PMN-004 §5 (b).
  - Claim 10: PASS — `grep -cE "§[0-9]+" docs/handoffs/TASK-0008-pmn-004-pr-7-cycle-learnings.md docs/reviews/PR-8-codex-pre-commit.md` lists `13` lines in handoff and `24` lines in review-context containing §-citations; visual sweep of those lines confirms each PMN-004-internal citation lands in §1-§8 range, each cross-document citation (PMN-003 (a)/(e), ADR-003 Decision 3, PMN-001 (k), PMN-002 (a)/(d)) resolves to an actual heading in the cited document, and each spec-source citation (out-of-tree per ADR-001 decision 15 — spec is gitignored) resolves to a `## §N` heading in the deliverable spec at the cited number (manual verification at Builder spec-read time).
  - Encoding: PASS — em-dash `—` (U+2014) appears on `13` lines and `17` byte occurrences in PMN-004 (multiple em-dashes per line in §-section headers, parentheticals, and inline contexts; `grep -c` counts matching lines, `grep -o ... | wc -l` counts occurrences); PowerShell scan across all three files reports `TOTAL_SMART_QUOTES=0` (no U+2018/U+2019/U+201C/U+201D).
- **Evidence**:
  - File count: 3 files changed (3 new + 0 modified). `git status --porcelain` lists exactly three `??` (untracked) entries, all under `docs/`. `git diff --stat HEAD` (post-stage) confirms `3 files changed`, `0 deletions(-)`, additions reflecting substantive content lengths (PMN-004 ~155 lines + TASK-0008 handoff ~62 lines + PR-8 review-context ~95 lines).
  - Tracked-file delta: `git ls-files | wc -l` returns `83` post-stage; baseline at base SHA `4ac4640` is `80`; delta = `+3 = 83 - 80` ✓.
  - Encoding: em-dash present in all three files; no smart quotes in any of the three files (PowerShell U+2018/U+2019/U+201C/U+201D scan returns zero).

## Exact next step

Run the v2 Builder prompt for TASK-0008 from §3.1 pre-flight forward.
- Codex desktop pre-commit review at step 7 (using prompt block embedded in `docs/reviews/PR-8-codex-pre-commit.md`).
- Stop-and-show at step 8.
- Linked-PR fix-up at step 11 substituting actual PR URL after `gh pr create` returns it.
- Hand back at step 12 with PR URL, file count attestation (3), handoff metadata confirmation, Codex pre-commit review outcome, severity-taxonomy attestation, cross-surface count attestation, phantom-action attestation, and explicit no-`@codex review`-from-Builder note.

## Reassessment / expiry

This handoff is stale 7 days after PR opens or immediately on any of: PMN-004 amendment, ADR-003 amendment, owner-confirmed scope change. Re-read this spec and PMN-004 before resuming if delayed.

## Session log archive (prior logs migrated from PR body per §13.1)

<!-- Empty at PR-8 open. Builder appends per §13.2 if PR has multiple sessions. -->
