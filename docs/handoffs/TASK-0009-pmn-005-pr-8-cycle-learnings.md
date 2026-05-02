# HANDOFF: TASK-0009 — PMN-005 PR-8 cycle learnings

## Metadata

- Task ID: TASK-0009
- Linked Issue: n/a (PMN-tracked; PMN-005 is the deliverable)
- Linked PR: <FILL AT PR-OPEN — substitute actual PR URL after gh pr create returns; per PMN-001 (k) handling>
- Linked ADR(s): ADR-003 (PMN-005 inserts under Decision 3 contingency budget; consumes second slot of seven; five remaining)
- Linked PMN(s): PMN-001, PMN-002, PMN-003, PMN-004 (PMN-005 builds on the lineage; specifically refines PMN-003 (e) and PMN-004 §5 (e); recursively self-instances PMN-004 §2 claim-text drift defect class via PMN-005 §4)
- Linked Feature Brief: n/a (PMNs do not have associated Feature Briefs)
- Linked review-context file: `docs/reviews/PR-9-codex-pre-commit.md`
- Owner role: Architect (Claude.ai) → Builder (Claude Code)
- Previous role: Architect produced this handoff and the PMN-005 spec from the Builder's PR-8 close hand-back observations (3 candidate observations consolidated into a single PMN per owner-confirmed decision)
- Timestamp (UTC): 2026-05-02T12:19:42Z
- Last synced commit SHA: 56256ea (squash-merge of PR-8 on main, 2026-05-02T11:35:24Z)
- Branch: chore/task-0009-pmn-005-pr-8-cycle-learnings
- Status: active
- Direction: Architect → Builder (universal handoff schema, AMAS v2.14.1 §14.1)
- Framework version: AMAS v2.14.1 (dogfooded)

## Objective

Author PMN-005 documenting the PR-8 cycle learnings: reviewer-claimed-effects-don't-land defect class (high confidence; two sub-shapes) + pass-shape correlation hypothesis (preliminary; 3 data points across 2 cycles) + path-(a)-revision-propagation gap on Validation run Evidence / cumulative diff stats sub-rule refinement of PMN-004 §5 (e). Two refinements articulated: PMN-003 (e) refined extended to include comment-content verification against repo state (five-point Architect-side post-handback check pattern); PMN-004 §5 (e) prose-arithmetic decomposition extended with sub-rule (e.1) cumulative-diff-stats re-derivation. The PMN-005 PR is small (3 files: PMN + handoff + review-context); no README sweep, no ADR amendment, no scaffold-stub modification.

The README "Canonical law" row staying briefly stale across PR-8 and PR-9 cycles (forecasting PR-8 = core Part A; reality PR-8 = PMN-004 and PR-9 = PMN-005) is the second test of the per-PR-row-update discipline ADR-003 §Consequences established. PR-10 (next substantive cycle, core Part A authoring) Builder will reconcile the row at content-fill time per ADR-003 §Consequences distributed-update discipline.

## Last completed step

Architect verified repo state at SHA 56256ea, received Builder PR-8 close hand-back (three candidate observations; cycle summary; observation density 3 from 3-file cycle), confirmed all seven strategic decisions ("ship it" 2026-05-02), authored this handoff and the PMN-005 spec.

## Current state

- Summary: `main` is at 56256ea with 83 tracked files. Local clone clean. Branch protection on `main` per ADR-001 decision 9 + posture-2 admin bypass via Rulesets.
- Files changed: none yet at handoff hand-off.

## Decisions made

- PMN-005 timing: now (before TASK-0010 core Part A authoring). Three reasons: established PMN-after-cycle cadence; quality dependency on canonical-content authoring (PMN-005 reviewer-claimed-effects-don't-land defect class has direct implications for TASK-0010's §8.1.1.2 canonical text on Reviewer claimed-action verification; PMN-005 refinements must be canonical before being applied to canonical content); observation freshness.
- PMN-005 scope: consolidated single PMN with three observations. Splitting dilutes the lesson; consolidated PMNs are established norm (PMN-001/002/003/004 all consolidated).
- Pass-shape-correlation confidence framing: preliminary hypothesis with explicit qualifier ("3 data points across 2 cycles; consistent with hypothesis; ~3 more cycles needed for higher confidence"). Don't suppress; don't overclaim. Future cycles test against named hypothesis.
- Claimed-effects-don't-land mitigations: extend PMN-003 (e) refined two-endpoint discipline to include comment-content verification vs repo state. Same verification surface; adding content-verification to existing discipline is cleaner than adding a new top-level discipline.
- §5 discipline (e) sub-rule addition: explicitly add (e.1) "after path-(a) revisions to any artifact, re-derive cumulative diff stats and any approximate counts to landed exact counts." Not a new discipline; sub-rule within existing (e).
- PR-9 file count: exactly 3 (3 new + 0 modified). Same shape as PMN-003 / PMN-004 (PR-6, PR-8). No README sweep; ADR-003 §Consequences explicitly establishes per-PR-row-update discipline.
- Branch slug: `chore/task-0009-pmn-005-pr-8-cycle-learnings` (parallels PMN-003 / PMN-004 precedent).
- M-A6 monitoring item update: PMN-rate post-PMN-005-merge will be 5/9 = 56%; exceeds ADR-003 forecast upper bound (54%) by 2 percentage points. Does NOT trigger M-A6 promotion (trigger remains at TASK-0023, three contingency slots remaining). Surface as evidence at TASK-0023 evaluation point.
- Renumbering: ADR-003's anticipated PR-9-through-PR-20 substantive content sequence shifts +1; canonical content authoring now starts at PR-10 (TASK-0010 core Part A). Already budgeted by ADR-003 Decision 3.
- All six §5 disciplines from PMN-004 plus PMN-005 two refinements: applied to this deliverable's authoring; carried forward to all subsequent specs.

## Assumptions

- TASK-0009 is the next available TASK number (verified in step 1 pre-flight: `ls docs/handoffs` returns 8 files TASK-0001 through TASK-0008).
- PMN-005 is the next available PMN number (verified in step 1: `ls docs/post-merge-notes` returns 4 files PMN-001 through PMN-004).
- Base SHA `56256ea` is current `main` (verified in step 1).
- Branch protection on `main` is live and configured per ADR-001 decision 9.
- `gh` CLI authenticated with `repo` scope minimum.
- Codex desktop is available to the owner for step 7 pre-commit review.

## Risks

- **Recursive section-citation drift**: PMN-005 §4.3 documents the prior-session handoff's "PMN-004 §10" citation slip (PMN-004 has §1-§8 only). PMN-005 itself contains many `§N` citations to PMN-003, PMN-004, ADR-003, AMAS v2.14.1 sections. Mitigation: PMN-004 §5 (f) section-citation correctness sweep applied iteratively to convergence per PMN-005 §4.5 step-10 self-verification; cross-document verification commands run for PMN-004 internal §-citations (must land in 1-8 range), PMN-005 internal §-citations (must land in 1-7 range), ADR-003 internal references, and AMAS v2.14.1 reference §-numbers.
- **Cumulative-diff-stats drift**: file count claim "3" appears in PR body (§6.3 of this spec; post-commit surface, not pre-commit-verifiable per discipline (d)), this handoff §"Validation run" Evidence section (filled at step-10 per discipline (c)), PR-9 review-context (claim 7). Three pre-commit-existing surfaces total. All pre-commit-existing surfaces must agree on 3. Mitigation: §23.6 prose-arithmetic decomposition with sub-rule (e.1) cumulative-diff-stats re-derivation (PMN-005 §4.4) is pre-applied by Architect in this spec; verified at §10 step-10 self-verification; the Evidence section is populated only with landed exact counts, never with approximate or `~`-prefixed numbers.
- **Severity-taxonomy compliance**: PR-9 review-context file enumerates Blocking / Major / Minor (three-level repo discipline; standing per PMN-004 §5 discipline (a)). Verified at step-10 self-review of this spec.
- **Phantom-action surface in Builder hand-back**: claims about file existence, content, and counts must be directly verifiable from working-tree filesystem and `git diff` output at hand-back time. Mitigation: Builder's hand-back lists each claim with its verification command and observed result, per PMN-005 §2.5 five-point post-handback check pattern (extended from PMN-003 (g) four-point pattern).
- **Verification-command portability (PMN-004 §5 discipline (b))**: pre-commit verification commands provided in both bash and Windows cmd forms in §5 pre-flight, §7 step-10 self-verification, and §4 PR-9 review-context (Codex pre-commit prompt embedded). Builder runs whichever shell is available; Codex desktop runs the cmd/PowerShell form if executing on Windows.
- **No future-tense pre-commit claims (PMN-004 §5 discipline (c))**: every Builder claim's verification command produces verifiable output at pre-commit time against the working tree. No claim of the form "will be substituted at PR-open" is acceptable in pre-commit Builder claims; the substitution itself happens post-PR-open via fix-up commit per PMN-001 (k). Mitigation: §7 step-10 self-verification explicitly checks each claim's verification command runs successfully against the working tree before pre-commit.

## Blocking questions

None at handoff time. If any surface during execution, stop and surface to owner via stop-and-show §9 of the spec.

## Validation run

Filled by Builder at step-10 self-verification per §7 of the spec, against the working tree at branch tip on `chore/task-0009-pmn-005-pr-8-cycle-learnings` prior to Codex desktop pre-commit review (per PMN-004 §5 discipline (c) — no future-tense claims at pre-commit time). Per PMN-005 §4.4 sub-rule (e.1), cumulative-diff-stats re-derivation is run after every path-(a) revision iteration; the Evidence section below is populated only with landed exact counts.

- **Commands** (bash, Git Bash on Windows 11):
  - Claim 1: `[ -f docs/post-merge-notes/PMN-005-pr-8-cycle-learnings.md ] && head -1 docs/post-merge-notes/PMN-005-pr-8-cycle-learnings.md`
  - Claim 2: `[ -f docs/handoffs/TASK-0009-pmn-005-pr-8-cycle-learnings.md ] && head -1 docs/handoffs/TASK-0009-pmn-005-pr-8-cycle-learnings.md`
  - Claim 3: `[ -f docs/reviews/PR-9-codex-pre-commit.md ] && head -1 docs/reviews/PR-9-codex-pre-commit.md`
  - Claim 4: `git status --porcelain | wc -l`
  - Claim 5: `git status --porcelain | grep -v "^?? docs/" | wc -l`
  - Claim 6 (read-only): `git ls-files | wc -l` (returns `83`) + `git status --porcelain | grep -c "^?? "` (returns `3`) → arithmetic sum `86`
  - Claim 7: `grep -c "3 files\|3 new\|count: 3\|exactly 3" docs/handoffs/TASK-0009-pmn-005-pr-8-cycle-learnings.md docs/reviews/PR-9-codex-pre-commit.md`
  - Claim 8: `grep -c "Blocking / Major / Minor" docs/reviews/PR-9-codex-pre-commit.md`
  - Claim 9: `grep -E "^## §[0-9]" docs/post-merge-notes/PMN-005-pr-8-cycle-learnings.md | wc -l`
  - Claim 10: `grep -cE "§[0-9]+" docs/handoffs/TASK-0009-pmn-005-pr-8-cycle-learnings.md docs/reviews/PR-9-codex-pre-commit.md` (lists §-citation-bearing lines for visual sweep)
  - Cumulative diff stats (per PMN-005 §4.4 sub-rule (e.1)): `git diff --stat HEAD` against the actual working-tree state immediately before commit; per-file insertion / deletion counts populated below verbatim from this command's output (no approximate counts; no `~`-prefixed numbers)
  - Encoding: `grep -c "—" docs/post-merge-notes/PMN-005-pr-8-cycle-learnings.md` (lines) and `grep -o "—" docs/post-merge-notes/PMN-005-pr-8-cycle-learnings.md | wc -l` (occurrences); PowerShell smart-quote scan (U+2018/U+2019/U+201C/U+201D) across all three files

- **Results**:
  - Claim 1: PASS — `# PMN-005 — PR-8 cycle learnings: reviewer-claimed-effects-don't-land defect class + pass-shape correlation hypothesis + cumulative-diff-stats sub-rule refinement`
  - Claim 2: PASS — `# HANDOFF: TASK-0009 — PMN-005 PR-8 cycle learnings`
  - Claim 3: PASS — `# PR-9 Codex desktop pre-commit review context`
  - Claim 4: PASS — `git status --porcelain | wc -l` → `3`
  - Claim 5: PASS — `git status --porcelain | grep -v "^?? docs/" | wc -l` → `0`
  - Claim 6: PASS — `git ls-files | wc -l` → `83`; `git status --porcelain | grep -c "^?? "` → `3`; arithmetic sum `83 + 3 = 86`
  - Claim 7: PASS — `grep -c "3 files\|3 new\|count: 3\|exactly 3" docs/handoffs/TASK-0009-pmn-005-pr-8-cycle-learnings.md docs/reviews/PR-9-codex-pre-commit.md` → handoff `6`, review-context `5`; total `11` (≥ 4 required). Re-derived after Evidence-population per sub-rule (e.1) (Evidence text added further mentions of the 3-file count in the diff-stat block); pre-Evidence-population intermediate count was `3 + 5 = 8`.
  - Claim 8: PASS — `grep -c "Blocking / Major / Minor" docs/reviews/PR-9-codex-pre-commit.md` → `5` (≥ 2 required)
  - Claim 9: PASS — `grep -E "^## §[0-9]" docs/post-merge-notes/PMN-005-pr-8-cycle-learnings.md | wc -l` → `7`
  - Claim 10: PASS — section-citation sweep iteration 1 + iteration 2: PMN-005-internal citations (§2.2, §2.5, §3, §4, §4.3, §4.4, §4.5) all land in 1-7 range; PMN-004-internal citations (§2, §2.3, §5) all land in 1-8 range; the single `PMN-004 §10` token at handoff `## Risks` is slip-describing narrative ("(PMN-004 has §1-§8 only)" follows immediately), legitimate per spec §12.3 carryforward; out-of-tree citations (AMAS v2.14.1 §14.1, §23.6, §8.1.1.2; spec-source §4/§5/§7/§9/§10) verified against their source documents at spec-read time. Iteration 2 re-sweep clean (fixed-point convergence reached).
  - Encoding: PASS — em-dash (`—`, U+2014) count in PMN-005: `grep -c "—" ...` → `27` lines; `grep -o "—" ... | wc -l` → `27` occurrences. Smart-quote scan (U+2018/U+2019/U+201C/U+201D) across all three files → `0`.

- **Evidence**: Verbatim `git diff --stat HEAD` output captured against the working tree immediately before commit (files staged with `git add` at commit time; `git add -N` used at step-10 to surface insertion counts and reset post-capture so untracked-form claims 4-5-6 hold; counts identical to the post-`git add` state because no content changes between):

```
 docs/handoffs/TASK-0009-pmn-005-pr-8-cycle-learnings.md | 127 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 docs/post-merge-notes/PMN-005-pr-8-cycle-learnings.md   | 249 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 docs/reviews/PR-9-codex-pre-commit.md                   | 137 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 3 files changed, 513 insertions(+)
```

Per-file landed exact insertion counts: `docs/handoffs/TASK-0009-pmn-005-pr-8-cycle-learnings.md` = 127; `docs/post-merge-notes/PMN-005-pr-8-cycle-learnings.md` = 249; `docs/reviews/PR-9-codex-pre-commit.md` = 137. Total: `127 + 249 + 137 = 513` insertions across 3 files. Decomposition per (e): 127 + 249 + 137 = 513. No approximate counts; no `~`-prefixed numbers. Per PMN-005 §4.4 sub-rule (e.1), the Evidence-population edit at step-10 was itself a path-(a)-class revision touching this artifact; cumulative diff stats were re-derived after that edit from a fresh `git diff --stat HEAD` invocation, and the numbers above match the post-edit state. The number-only edits used to land the post-edit counts in this Evidence block (107 → 127 in the diff stripe; 493 → 513 in the totals; 107 → 127 in the prose decomposition) change the count of `+` characters in the diff-stat stripe but do not change the line count of this artifact, so `wc -l` of the handoff is invariant under the number-only edit; iteration is therefore at fixed-point at 127 lines.

## Exact next step

Run the Builder prompt for TASK-0009 from §5 pre-flight forward.
- Codex desktop pre-commit review at step 8 (using prompt block embedded in `docs/reviews/PR-9-codex-pre-commit.md`).
- Stop-and-show at §9 of the spec.
- Linked-PR fix-up at §10 if `gh pr create` returns a URL that needs substituting back into the handoff's Linked PR field.
- Hand back at §10 with PR URL, file count, handoff metadata confirmation, Codex pre-commit review outcome, severity-taxonomy verification attestation, cumulative-diff-stats re-derivation attestation per PMN-005 §4.4, and explicit no-`@codex review`-from-Builder note.

## Reassessment / expiry

This handoff is stale 7 days after PR opens or immediately on any ADR-003 amendment, ADR-002 amendment, PMN-004 amendment, or owner-confirmed scope change. Re-read this spec, ADR-003, and PMN-004 before resuming if delayed.

## Session log archive (prior logs migrated from PR body per §13.1)

<!-- Empty at PR-9 open. Builder appends per §13.2 if PR has multiple sessions. -->
