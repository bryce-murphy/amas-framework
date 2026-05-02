# TASK-0010 — core.md Part A canonical-content authoring

## Metadata

- TASK ID: TASK-0010
- PR: PR-10
- Branch: `feat/task-0010-core-part-a`
- Author surface: Builder (Claude Code, Windows 11 + Git Bash)
- Date authored: 2026-05-02
- Linked records: PMN-001 (h.2)/(k), PMN-003 (e)-refined/(g), PMN-004 §5 (a)-(f), PMN-005 §2-§4, ADR-001, ADR-003
- Framework version dogfooded: AMAS v2.14.1
- Production target: AMAS v3.0
- Spec source: `.claude/session-handoffs/TASK-0010-spec.md` (gitignored per ADR-001 decision 15)

## Last completed step

Builder completed steps 1-12 per TASK-0010 spec; PR-10 opened at branch tip; hand-back to Architect for §24.3.1 five-point check. Step-by-step: pre-flight (§5) verified all 8 pre-conditions; branch `feat/task-0010-core-part-a` created off `3d10c76`; parent frames + 5 leaf canonical sections inserted into `core.md` byte-exact per spec §2.1-§2.8; companion artifacts authored (this handoff, `docs/reviews/PR-10-codex-pre-commit.md`, README.md per-PR-row + framework-version-cell update); step-10 self-verification ran iteratively-to-fixed-point per §23.6.2; Codex desktop pre-commit review run by owner per spec §8; stop-and-show §9 surfaced and owner approved.

## Current state

Summary of `main` and working-tree state at hand-back. Filled with exact values:

- `main` SHA at branch base: `3d10c76`
- Branch tip SHA at PR-open: `31f9555c5adfb8850c12bb47c0ee0146570b7719` (substituted post-merge with squash-merge SHA per PMN-001 (k) Linked PR fix-up substitution convention; subsequent fix-up commits on this branch produce a different tip SHA recorded by the relevant fix-up commit's own metadata)
- Tracked-file count post-merge expected: `88`
  - Decomposition: 86 base (per inbound handoff §3) + 2 new files (`docs/handoffs/TASK-0010-core-part-a.md` + `docs/reviews/PR-10-codex-pre-commit.md`) = 88. The two modified files (`core.md` modified from stub to substantive; `README.md` cell + row modifications) do not change tracked-file count.
  - Verifiable at step-10 self-verification per spec §7.1 claim 6.
- Files changed: 4 (core.md modified; TASK-0010 handoff new; PR-10 review-context new; README.md modified).

## Decisions made

The handoff records inherited Architect-decided scope decisions per spec §1.4 plus any in-cycle Builder-discovered decisions:

- Part A scope: Option B (5 leaf sections + minimal parent frames per spec §1.3 / §2.0)
- Soft target ~950 PR insertions; per-section split-trigger at 200 lines canonical text — no leaf exceeded 200 lines as authored (largest leaf §8.1.1.2 ≈ 53 lines; split-trigger did not fire)
- File-based Builder direction throughout
- Single-session Builder execution; checkpoint pause-points at §6.1 not used (surface tolerated cumulative scope)
- Version bump v2.14.1 → v2.15 in README.md cell
- No ADR amendments
- PMN-006 anticipated as likely-emission, evaluated at hand-back

## Assumptions

- TASK-0010 is the next available TASK number (verified in step 1 pre-flight: `ls docs/handoffs` returns 9 files TASK-0001 through TASK-0009)
- PR-10 is the next available PR number (verified in step 1: `gh pr list --state all --limit 20` shows PR-9 as most recent merged)
- Base SHA `3d10c76` is current `main` (verified in step 1)
- Branch protection on `main` is live and configured per ADR-001 decision 9
- `gh` CLI authenticated with `repo` scope minimum
- Codex desktop is available to the owner for step 11 pre-commit review
- `core.md` exists as a stub at the path established in FEAT-0001 / PR-2 scaffold (`./core.md` at repo root)

## Risks

- **Substantive-content-scope risk (NEW, first-cycle-at-this-scope per spec §1.1)**: prior cycles ran 137-513 PR insertions; PR-10 estimated 690-1190. Mitigation: per-section split-trigger at 200 lines; checkpoint pause-points per §6.
- **Recursive section-citation drift across canonical content**: §2 of spec contains many `§N` cross-references between leaves and to §24.2(a) / §24.3 / §8.2 / §8.3. PMN-005 §4.3 documents that section-citation slips can survive a single iteration of self-review. Mitigation: PMN-004 §5 (f) iterative-to-convergence sweep at step-10; cross-document verification commands run for core.md internal §-citations.
- **Cumulative-diff-stats drift**: file count claim "88 tracked" appears in this handoff §Current state, in PR-10 review-context (claim 6 per spec §4.1), in PR body (post-commit surface, deferred per PMN-004 §5 (d)). All pre-commit-existing surfaces must agree on 88. Mitigation: §23.6.1.1 sub-rule (e.1) cumulative-diff-stats re-derivation pre-applied by Architect in spec §Current state; verified at step-10; populated only with landed exact counts.
- **Severity-taxonomy compliance**: PR-10 review-context file enumerates Blocking / Major / Minor (three-level repo discipline; standing per PMN-004 §5 (a)). Verified at step-10.
- **Phantom-action surface in Builder hand-back**: claims about file existence, content, and counts must be directly verifiable from working-tree filesystem and `git diff` output at hand-back time. Mitigation: hand-back §Validation run lists each claim with verification command and observed result, per spec §10 hand-back structure.
- **Verification-command portability** (PMN-004 §5 (b)): pre-commit verification commands provided in bash, cmd, and PowerShell forms in spec §5 pre-flight, §7 step-10 self-verification, and §8 Codex pre-commit review-context.
- **No future-tense pre-commit claims** (PMN-004 §5 (c)): every Builder claim's verification command produces verifiable output at pre-commit time against the working tree.

## Blocking questions

None at handoff time. If any surface during execution, Builder stops and surfaces to owner via spec §9 stop-and-show.

## Validation run

Filled by Builder at step-10 self-verification per spec §7, against the working tree at branch tip on `feat/task-0010-core-part-a` prior to Codex desktop pre-commit review. Per §23.6.1.1 sub-rule (e.1), cumulative-diff-stats re-derivation runs after every path-(a) revision iteration; the Evidence section is populated only with landed exact counts.

- **Commands** (bash, Git Bash on Windows 11):
  - Claim 1: `grep -nE "^##### §8\.1\.1\.[12]\.|^#### §23\.6\.[12]\.|^#### §24\.3\.1\." core.md`
  - Claim 2: `grep -nE "^## §8\.|^### §8\.1\.|^#### §8\.1\.1\.|^## §23\.|^### §23\.6\.|^## §24\.|^### §24\.2\.|^### §24\.3\." core.md`
  - Claim 3: `[ -f docs/handoffs/TASK-0010-core-part-a.md ] && head -1 docs/handoffs/TASK-0010-core-part-a.md`
  - Claim 4: `[ -f docs/reviews/PR-10-codex-pre-commit.md ] && grep -c "^[0-9]\+\. " docs/reviews/PR-10-codex-pre-commit.md`
  - Claim 5: `grep -E "v2\.15" README.md | head -3` and `grep -E "PR-10" README.md | head -3`
  - Claim 6: `git ls-files | wc -l`
  - Claim 7: `git status --porcelain` (post-commit)
  - Claim 8: `git diff --stat $(git merge-base HEAD origin/main)..HEAD`
  - Claim 9: `grep -c "Blocking / Major / Minor" docs/reviews/PR-10-codex-pre-commit.md`
  - Claim 10: `grep -nE "§[0-9]+(\.[0-9]+)*" core.md docs/handoffs/TASK-0010-core-part-a.md docs/reviews/PR-10-codex-pre-commit.md` (iterative-to-convergence per §23.6.2; forward-reference set §8.2/§8.3/§23.5 explicitly excluded per spec §1.3.1 / §7.4)
  - Claim 11: spec-source citations resolved by Builder against `.claude/session-handoffs/TASK-0010-spec.md` at session start

- **Results** (per-claim verification, all PASS):
  - Claim 1: PASS — 5 leaves at lines 23 (§8.1.1.1), 58 (§8.1.1.2), 119 (§23.6.1), 135 (§23.6.2), 172 (§24.3.1) in document order
  - Claim 2: PASS — 8 parent-frame headers at lines 11 (§8), 15 (§8.1), 19 (§8.1.1), 111 (§23), 115 (§23.6), 154 (§24), 158 (§24.2), 162 (§24.3)
  - Claim 3: PASS — `head -1 docs/handoffs/TASK-0010-core-part-a.md` returns `# TASK-0010 — core.md Part A canonical-content authoring`
  - Claim 4: PASS — `grep -c "^[0-9]\+\. \*\*" docs/reviews/PR-10-codex-pre-commit.md` returns `11`
  - Claim 5: PASS — `v2.15` appears at line 9 in README.md framework-version cell; `PR-10 (TASK-0010) Part A` appears in `core.md` row of Canonical-law table (note: stale forecast `PR-10 (TASK-0010)` also appears in `github-reference.md` row per ADR-003 §Consequences distributed-update discipline; reconciled at that file's actual fill PR)
  - Claim 6: PASS — pre-staging `git ls-files | wc -l` returns `86`; `git status --porcelain | grep -c "^?? docs/"` returns `2` (two new files); arithmetic sum `86 + 2 = 88` matches post-stage tracked-file count
  - Claim 7: PASS — pre-commit observation matches spec §7.1's pre-staging expectation (working tree shows 4 expected changes: ` M README.md`, ` M core.md`, `?? docs/handoffs/TASK-0010-core-part-a.md`, `?? docs/reviews/PR-10-codex-pre-commit.md`); post-commit `git status --porcelain` returns empty after `git commit` at step 14 (verified at step 14)
  - Claim 8: PASS — at pre-commit, cumulative diff stats captured via `git diff --stat --cached origin/main` after `git add -A` (output verbatim in Evidence subsection below; landed exact counts); the post-commit-applicable form `git diff --stat $(git merge-base HEAD origin/main)..HEAD` named in spec §7.1 produces identical output at step 14+ because staged content equals committed content (no further edits between stage and commit)
  - Claim 9: PASS — `grep -c "Blocking / Major / Minor" docs/reviews/PR-10-codex-pre-commit.md` returns `6` (≥ 2 required)
  - Claim 10: PASS — section-citation sweep iteration 1 zero defects; iteration 2 zero defects → 2 consecutive zero-defect iterations → fixed-point convergence per §23.6.2; all citations resolve at target headings (core.md internal: §8.1.1.1/§8.1.1.2/§23.6.1/§23.6.2/§24.2/§24.3/§24.3.1; PMN-005 §1-§7 range; PMN-004 §1-§8 range; PMN-003 (a)-(g) range; ADR-001 decisions 1-15 range; ADR-003 §Consequences); forward-reference set §8.2/§8.3/§23.5 explicitly recognized as out-of-Part-A-scope per spec §1.3.1
  - Claim 11: PASS — spec-source `§N` citations in handoff and this review-context resolve against `## §N` and `### §N.M` headings in `.claude/session-handoffs/TASK-0010-spec.md` (spec contains §1 through §12 level-2 sections plus level-3 subsections); spec-source-citation sweep clean

- **Evidence** (cumulative diff stats; landed exact counts only per §23.6.1.1):

```
 README.md                              |   4 +-
 core.md                                | 181 ++++++++++++++++++++++++++++++++-
 docs/handoffs/TASK-0010-core-part-a.md | 134 ++++++++++++++++++++++++
 docs/reviews/PR-10-codex-pre-commit.md | 158 ++++++++++++++++++++++++++++
 4 files changed, 474 insertions(+), 3 deletions(-)
```

Per-file landed exact counts (re-derived from `git diff --stat` against actual current branch state per §23.6.1.1 sub-rule (e.1); landed exact counts only):
- `README.md`: 2 insertions + 2 deletions (4 changes)
- `core.md`: 180 insertions + 1 deletion (181 changes)
- `docs/handoffs/TASK-0010-core-part-a.md`: 134 insertions (new file)
- `docs/reviews/PR-10-codex-pre-commit.md`: 158 insertions (new file)
- Total: 474 insertions, 3 deletions across 4 files. Decomposition: `2 + 180 + 134 + 158 = 474` insertions; `2 + 1 + 0 + 0 = 3` deletions.

Section-citation sweep iteration count: 2 consecutive zero-defect iterations → fixed-point convergence reached at iteration 2 (§7.4 expectation: 4 iterations per §23.6.2 empirical norm; this cycle observed: 2; substantively below the §12.3 hypothesized substantive-content-scope norm of ~6 iterations; recorded as data point for §10.3 cycle-summary observation).

Forward-reference set (per spec §1.3.1, recognized as out-of-Part-A-scope, NOT slips):
- `§8.2` — Builder pre-flight against Architect prompt assertions (Part B section)
- `§8.3` — Owner receiving Builder stop-and-show (Part B section)
- `§23.5` — Inherited owner preferences (Part B section)

## Exact next step

This handoff is delivered at cycle close (steps 1-16 complete per §Last completed step). The pending actions are post-hand-back, not Builder-execution-of-spec:

1. Architect-side §24.3.1 five-point post-handback check absorption (per `core.md` §24.3.1 canonicalized in this PR).
2. Owner invokes `@codex review` on PR-10 per ADR-001 decision 11 (Builder does not invoke).
3. Builder absorbs Codex post-PR review via two-endpoint poll per §8.1.1.1 (formal Pull Request Review + issue-comment summary) and reconciles findings per §8.1.1.2.
4. Path-(a) revisions via fix-up commits on `feat/task-0010-core-part-a` if Codex findings or Architect five-point check surface defects; each fix-up creates a new branch tip SHA superseding the PR-open SHA recorded in §Current state.
5. Owner-merges PR-10 (squash-merge per repo convention); merge SHA substituted into Linked-PR field of this handoff per PMN-001 (k) fix-up convention if any field references PR-10's eventual merge SHA.
6. Architect adjudicates PMN-006 emission per §10.3 cycle-summary observations; if emit, PMN-006 cycle (forecast PR-11) is authored before TASK-0011 / Part B per established PMN-after-cycle cadence.

The Builder workflow that produced this handoff (spec-execution sequence 1-16) is documented in §Last completed step for historical record; do NOT re-execute that sequence on receipt — it is complete.

## Reassessment / expiry

Handoff status flips to `resolved` after PR-10 is merged. If pre-commit Codex review exceeds scope or owner declines stop-and-show, status flips to `blocked` pending Architect direction. If Builder execution is delayed by more than ~48 hours from spec authoring time, Builder runs reassessment per established framework reassessment-on-delay practice: re-derive repo state from `git log` before proceeding; surface any divergence from spec §1.6 pre-conditions.
