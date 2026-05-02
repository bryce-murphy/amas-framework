# HANDOFF: TASK-0007 — ADR-003 full-package PR plan + structural staleness sweep

## Metadata

- Task ID: TASK-0007
- Linked Issue: n/a (ADR-tracked; ADR-003 is the spec)
- Linked PR: https://github.com/bryce-murphy/amas-framework/pull/7
- Linked ADR(s): ADR-003 (this PR's substantive output); ADR-001 decision 8 (partially superseded); ADR-002 (amended)
- Linked Feature Brief: n/a (no new FEAT for an architectural-decision PR)
- Linked review-context file: `docs/reviews/PR-7-codex-pre-commit.md`
- Owner role: Architect (Claude.ai) → Builder (Claude Code)
- Previous role: Architect produced this handoff and the ADR-003 spec
- Timestamp (UTC): 2026-05-02T00:31:32Z
- Last synced commit SHA: 0f93eada37c1d5563946ee911b6016d72dc75803
- Branch: chore/task-0007-adr-003-full-package-pr-plan
- Status: active
- Direction: Architect → Builder (universal handoff schema, AMAS v2.14.1 §14.1)
- Framework version: AMAS v2.14.1 (dogfooded)

## Objective

Author ADR-003 to lock the full v3.0 package PR plan (12 substantive content PRs in tight-coupling dependency order through TASK-0019; reservation extended through TASK-0026 with PMN-insertion budget). Update README "Package layout" tables, Status, and Roadmap sections to reflect the ADR-003 plan. Sweep `filled_by` frontmatter across the 50 PR-2 scaffold stubs to point at ADR-003 as the canonical plan reference rather than specific PR numbers, eliminating the staleness recurrence pattern. Update ADR-001 Status field to mark decision 8 PR sequence as partially superseded by ADR-003.

ADR-003 amends ADR-002 (further reservation extension, consistent with ADR-002 Decision 3's anticipation that subsequent ADR amendments would follow ADR-002's pattern). ADR-003 partially supersedes ADR-001 decision 8 (the original PR-0 through PR-9 sequence is replaced by the full-package plan).

## Last completed step

Architect verified repo state at SHA 0f93eada37c1d5563946ee911b6016d72dc75803, confirmed ADR-002 / FEAT-0001 / README staleness against current PR sequence reality, surfaced strategic question to owner, received owner confirmation on all 8 strategic decisions ("ship it" 2026-05-01), authored this handoff and the ADR-003 spec.

## Current state

- Summary: `main` is at 0f93eada37c1d5563946ee911b6016d72dc75803 with 77 tracked files. Local clone clean. Branch protection on `main` per ADR-001 decision 9 + posture-2 admin bypass via Rulesets.
- Files changed: none yet at handoff hand-off.

## Decisions made

- Full v3.0 package ship scope: all 50 scaffold stubs filled before v3.0.0 tag. No staged-v3.0 / v3.1+ deferral path.
- PR ordering: tight-coupling dependency order (canonical-law trio first, derived artifacts in dependency-respecting batches; see ADR-003 Decision 2 PR plan table for full sequence).
- PMN insertion budget: empirical median rate plus margin; reservation extends to TASK-0026 (14 additional slots beyond TASK-0012 / ADR-002 cap).
- README sweep scope: full sweep (all "Filled by" cells, Status text, Roadmap text, all 50 stub `filled_by` frontmatter lines). Not deferred to per-substantive-PR row updates — that pattern produced the current staleness empirically.
- ADR-001 decision 8 disposition: partially superseded by ADR-003 (decision 8 PR sequence portion only; other ADR-001 decisions unchanged). Status field updated to reflect partial supersession scope.
- ADR-002 disposition: amended (not superseded). ADR-002 Decision 3's anticipation language explicitly authorizes this pattern. ADR-002 Status field unchanged (amendment convention preserves Status).
- Stub `filled_by` frontmatter: sweep all 50 stubs to `filled_by: per ADR-003`. Generic reference rather than per-PR specific value, preventing per-PR staleness recurrence. Each substantive content PR will update its own stub's `filled_by` to its actual PR/TASK number at content-fill time as part of normal PR scope.
- Stub `framework_version` and `status` fields: untouched by ADR-003 PR. Those fields remain as PR-2 set them; substantive content PRs will update `status: stub` → `status: drafted` (or similar) as part of content-fill.

## Assumptions

- TASK-0007 is the next available TASK number (verified in step 1 pre-flight).
- ADR-003 is the next available ADR number (verified in step 1 pre-flight).
- Base SHA `0f93eada37c1d5563946ee911b6016d72dc75803` is current `main` (verified in step 1).
- Branch protection on `main` is live and configured per ADR-001 decision 9.
- `gh` CLI authenticated with `repo` scope minimum.
- Codex desktop is available to the owner for step 11 pre-commit review.
- The 50 stubs identified by `git ls-tree HEAD` minus the canonical `core.md` / `github-reference.md` / `usage-guide.md` plus the 47 other PR-2 scaffold stubs match the FEAT-0001 §"In scope" enumeration of 50 stubs (3 Class A canonical-framework + 30 Class B template-markdown + 1 Class B' YAML-comment + 7 Class C adapter-pack + 9 Class D action-yaml). Step-7 sweep verifies the count.

## Risks

- **Stub sweep count mismatch**: 50 stubs is the FEAT-0001 expected count. If the regex sweep matches more or fewer than 50 files, halt at step 7 and surface — indicates either uncovered stubs (bug) or unexpected matches in non-stub files (false positive). Mitigation: explicit count verification at step 7; stop condition on mismatch.
- **README diff drift**: README modification at step 5 changes ~70 lines across 6 H2 sections. Per-section spot-check at step 9 step-10 self-verification.
- **Status field defect class**: ADR-001 Status update is a single-line modification of an existing accepted ADR. §7.1.1 explicitly permits Status field updates for supersession/amendment marker addition. Mitigation: spot-check that no other line in ADR-001 changes; `git diff docs/adr/ADR-001-initial-repo-setup.md` should show exactly 1 line changed.
- **ADR-003 verbatim transcription**: ADR-003 file is authored verbatim from §4 of this spec. Risk of transcription typos (em-dash mojibake, smart-quote substitution, etc.). Mitigation: byte-level encoding check at step 9; Codex desktop verification at step 10.
- **Cross-surface count claim drift**: file count claims appear in PR body, this handoff, ADR-003 itself (in Consequences section), and review-context file. All four must agree on the number of files changed. Mitigation: §24 cross-surface sweep at Codex pre-commit review step 10.
- **Severity-taxonomy compliance per Meta-observation 1**: review-context file enumerates severity levels for Codex's output structure. Levels MUST match repo's three-level taxonomy (Blocking / Major / Minor). Verified at §13 §23.6 self-review of this spec.
- **Phantom-action surface in Builder hand-back**: claims about file existence, content, and counts must be directly verifiable from working-tree filesystem and `git diff` output. Mitigation: Builder's hand-back lists each claim with the verification command that produced it (per AMAS v2.14.1 §8.1.1.2 Reviewer claimed-action verification).

## Blocking questions

None at handoff time. If any surface during execution, stop and surface to owner via stop-and-show §12.

## Validation run

Step-10 self-verification completed 2026-05-02 UTC. All checks PASS.

**Commands run**: artifact first-line checks (ADR-003, handoff, review-context); README diff line-pair count; ADR-001 single-line diff; stub sweep regex matches across .md and .yml targets; tracked-file count delta; em-dash / § / smart-quote byte verification across new artifacts; total file count via `git diff --stat HEAD`.

**Results**:
- ADR-003 first line matches §4 ✓
- TASK-0007 handoff first line matches §3.2 ✓
- PR-7 review-context first line matches §8 ✓
- README diff: 50 stub-row `+` lines + 50 stub-row `-` lines + 3 prose changes (Status, Roadmap, Package layout intro) — matches §5.11 ✓
- ADR-001 diff: 1 line changed at line 5 (1 deletion + 1 insertion) — matches §6 ✓
- Stub sweep: 40 .md matches `^filled_by: per ADR-003$` + 10 .yml matches `^# filled_by: per ADR-003$` = 50 total — matches §7.1 ✓
- 0 false negatives (no remaining old `PR-N (TASK-NNNN)` patterns) ✓
- 0 false positives (no files outside §7.1 carry the new pattern) ✓
- Total file count: 55 files changed (3 added + 52 modified) — matches §9 commit-message arithmetic ✓
- Tracked files post-add: 80 = 77 baseline + 3 new ✓
- ADR-003: 19 em-dashes, 10 § characters, 0 smart quotes ✓
- TASK-0007 handoff: 0 smart quotes ✓
- PR-7 review-context: 4 smart quotes (one each U+2018/2019/201C/201D), all spec-mandated literal examples in §8 "ADR-003 content fidelity" focus-area enumeration; transcribed verbatim per §8 instruction ✓

**Evidence**: 55-file tree-state delta: `git status --short` returns 55 lines (52 modified + 3 untracked); `git diff --stat HEAD` reports 52 (tracked-only); after `git add -A`, `git diff --cached --stat HEAD` reports 55. Tracked-files post-add: `git ls-files` returns 80 lines (77 baseline + 3 new artifacts; `git ls-tree -r --name-only HEAD` continues to return 77 because HEAD doesn't reflect staging until commit). Commit SHA at branch tip will be filled at PR-open.

## Exact next step

Run the v2 Builder prompt for TASK-0007 from §3.1 pre-flight forward.
- Codex desktop pre-commit review at step 10 (using prompt block embedded in `docs/reviews/PR-7-codex-pre-commit.md`).
- Stop-and-show at step 11.
- Linked-PR fix-up at step 14 if `gh pr create` returns a URL that needs substituting back into the handoff's Linked PR field.
- Hand back at step 14 with PR URL, file count, handoff metadata confirmation, Codex pre-commit review outcome, severity-taxonomy verification attestation, and explicit no-`@codex review`-from-Builder note.

## Reassessment / expiry

This handoff is stale 7 days after PR opens or immediately on any ADR-003 amendment, ADR-002 amendment, or owner-confirmed scope change. Re-read this spec and ADR-003 before resuming if delayed.

## Session log archive (prior logs migrated from PR body per §13.1)

<!-- Empty at PR-7 open. Builder appends per §13.2 if PR has multiple sessions. -->
