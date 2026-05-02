# PR-7 Codex desktop pre-commit review context

## Metadata

- PR ID: PR-7
- TASK ID: TASK-0007
- Branch: chore/task-0007-adr-003-full-package-pr-plan
- Base SHA: 0f93eada37c1d5563946ee911b6016d72dc75803
- Builder: Claude Code (Claude Opus 4.7)
- Reviewer: Codex (GPT-5.5) — desktop, pre-commit, untracked working tree
- Architect (this PR's): Claude Opus 4.7 (Claude.ai Project)
- Owner: Bryce Murphy (`@bryce-murphy`)
- Framework version: AMAS v2.14.1 (dogfooded)
- Severity taxonomy: Blocking / Major / Minor (three-level; per repo discipline)

## Builder claims to verify

The Builder asserts the following at hand-off to Codex desktop pre-commit review. Each claim is verifiable from the working tree.

1. **ADR-003 file authored at `docs/adr/ADR-003-full-package-pr-plan.md`** with the verbatim content from §4 of the TASK-0007 spec. Verifiable: `Test-Path docs/adr/ADR-003-full-package-pr-plan.md` returns True; first line is `# ADR-003 — Full v3.0 package PR plan and TASK reservation extension through TASK-0026`; total file matches §4 byte-for-byte.

2. **TASK-0007 handoff authored at `docs/handoffs/TASK-0007-adr-003-full-package-pr-plan.md`** with content from §3.2 of the spec, with placeholder substitutions per §3.2's inline directives (Timestamp filled at branch-creation; Validation run filled at step-10; Linked PR to be filled at PR-open). Verifiable: `Test-Path` returns True; first line is `# HANDOFF: TASK-0007 — ADR-003 full-package PR plan + structural staleness sweep`; non-placeholder content matches §3.2.

3. **PR-7 review-context file authored at `docs/reviews/PR-7-codex-pre-commit.md`** (this file). Verifiable: `Test-Path` returns True.

4. **README.md modified per spec §5.1 through §5.10**. Verifiable: `git diff README.md` shows the changes specified in §5; no other README lines changed. `git diff --stat README.md` reports `1 file changed, 53 insertions(+), 53 deletions(-)` (50 stub rows + 3 prose changes per §5.11). The 50 stub-row pairs are visible in `git diff README.md` as 50 lines beginning with `+|` and 50 lines beginning with `-|`; reviewers may count via shell-native idiom (PowerShell: `(git diff README.md | Select-String "^\+\|").Count`; bash: `git diff README.md | grep -c "^+|"`). Status section change verifiable per §5.1; Roadmap section change verifiable per §5.2; Package layout intro change verifiable per §5.3.

5. **ADR-001 Status line modified per spec §6**. Verifiable: `git diff docs/adr/ADR-001-initial-repo-setup.md` shows exactly 1 line changed (1 deletion, 1 insertion); the changed line is line 5; before/after match §6 specification.

6. **50 stub `filled_by` frontmatter lines swept to `filled_by: per ADR-003`** per §7. Verifiable: `Select-String -Pattern "^filled_by: per ADR-003$"` across all 40 .md stubs returns 40 matches; `Select-String -Pattern "^# filled_by: per ADR-003$"` across all 10 .yml stubs returns 10 matches; total 50. No file outside the §7.1 target list is modified.

7. **Total file count change**: 55 files = 3 new (ADR-003, TASK-0007 handoff, PR-7 review-context) + 52 modified (50 swept stubs + README + ADR-001). Verifiable pre-stage via shell-agnostic git output: `git diff --stat HEAD` ends with `52 files changed, 104 insertions(+), 104 deletions(-)` (tracked-only); `git status --short` returns 55 lines (52 modified + 3 untracked); `git ls-files --others --exclude-standard` returns 3 lines (the new artifacts). Reviewers may count lines via shell-native idiom (PowerShell: `(git status --short | Measure-Object -Line).Lines`; bash: `git status --short | wc -l`). Verifiable post-stage: after `git add -A`, `git diff --cached --stat HEAD` ends with `55 files changed, 395 insertions(+), 104 deletions(-)`. Halt if outside 54–56 range.

8. **No substantive content authored in any of the 50 swept stubs beyond the `filled_by` frontmatter line**. Verifiable: `git diff` on each swept stub shows exactly 1 line changed (the `filled_by` line). Body text (e.g., the `*Stub. To be authored ...*` line currently in each Class A stub) is unchanged.

9. **Severity taxonomy verification**: This review-context file enumerates Blocking / Major / Minor — the repo's three-level taxonomy. Verified at Architect §23.6 self-review of the spec (Meta-observation 1 of incoming session handoff). No two-level (Blocking / Minor) framing present in any committed artifact in this PR.

10. **No `@codex review` invocation from Builder side**. Owner invokes per ADR-001 decision 11. Verifiable pre-commit: working-tree state contains no `gh pr comment` or `@codex review` invocation other than this file's references and ADR-001 decision 11; the `## Notes` section of this review-context file explicitly defers post-PR `@codex review` to owner-invoked. The hand-back-time attestation is recorded in PR body §AI Session Log at PR-open per §14.

## Reviewer focus (Codex desktop)

For each Builder claim above, verify the verification command produces the asserted result. Specific focus areas:

- **§24 cross-surface count claim consistency (pre-commit scope)**: The number "55" appears at pre-commit time in (a) this review-context file (claim 7) and (b) the TASK-0007 handoff §"Validation run" Evidence section. Both must agree on the resolved count. Codex desktop sweeps both surfaces and reports the actual values verbatim. ADR-003 §Consequences references "50 scaffold stubs" semantically (not a file-count claim by design); PR body cross-surface verification happens post-`gh pr create` per §15 Point 1 (out of pre-commit scope).

- **§5 README diff completeness**: Verify each before/after pair from §5.1 through §5.10 matches the actual diff. Read the diff against the spec directly. Any "Filled by" cell still showing a pre-ADR-003 value (`PR-3 (TASK-0003)`, `PR-4 (TASK-0004)`, `PR-5 (TASK-0005)`, `PR-7 (TASK-0007)`, `PR-8 (TASK-0008)`) is a Blocking finding.

- **§7.1 stub sweep completeness**: Verify the 50 expected stubs all show `filled_by: per ADR-003` (or YAML-comment equivalent for .yml files). Any stub from §7.1 still showing a pre-ADR-003 `filled_by` value is a Blocking finding. Any file NOT in §7.1 showing a `filled_by: per ADR-003` change is a Blocking finding (false positive in sweep).

- **ADR-003 content fidelity**: Verify the `docs/adr/ADR-003-full-package-pr-plan.md` content matches §4 of the spec byte-for-byte. Em-dash (`—`, U+2014) verification: scan the file for byte sequence `E2 80 94`; should appear in the locations §4 specifies. Smart-quote substitution check: ensure no `‘`/`’`/`“`/`”` (U+2018, U+2019, U+201C, U+201D) appear; ASCII single-quote `'` and double-quote `"` only.

- **ADR-001 Status line scope**: Confirm exactly 1 line of ADR-001 changed. Any change beyond line 5 is a Blocking finding.

- **Severity taxonomy consistency**: Confirm this review-context file enumerates Blocking / Major / Minor (three levels) and no other taxonomy variant appears in any committed artifact in this PR. Two-level (Blocking / Minor) framing in any artifact is a Blocking finding.

- **Phantom-action claim verification**: Each Builder claim's verification command is itself directly verifiable. Codex desktop runs the command; reports result verbatim; flags any divergence from the Builder's asserted result.

## Reviewer-direction shape

Codex's output structure:

For each claim 1 through 10 above, output one of:
- `Claim N: Verified clean.`
- `Claim N: <Severity> finding — <description>; verification command output: <verbatim>; recommended action: <path (a) revise / path (b) record-and-proceed>.`

After per-claim verdict, output an overall summary:
- Total claims: 10
- Verified clean: <count>
- Blocking findings: <count>
- Major findings: <count>
- Minor findings: <count>
- Recommended disposition: clean / revise (path (a)) / record-and-proceed (path (b))

Severity definitions for this review:
- **Blocking**: defect that falsifies a Builder claim, contradicts ADR-003 substantive content, or introduces cross-surface count drift. Cannot ship without revision.
- **Major**: defect that does not falsify a Builder claim but degrades artifact quality (e.g., minor wording inconsistency, suboptimal cross-reference path). Can ship with documented exception via path (b); preferred path (a) revise.
- **Minor**: cosmetic or stylistic defect (e.g., trailing whitespace, ordering preference). Default path (b) record-and-proceed.

Action phrasing: each finding must use imperative `Action: <verb> <object>.` form (e.g., `Action: Update README.md line 137 to match spec §5.4.`). Per PMN-002 (a) refined.

## Builder hand-back attestation

After Codex desktop pre-commit review completes, Builder reports:
- Codex review outcome (per the summary structure above)
- Path (a) revisions made, if any
- Path (b) acceptances recorded, if any
- §23.6 recapitulation-consistency re-check result after any path (a) revisions per PMN-003 (a) refined

## Notes

- Codex desktop reviews the untracked working tree before commit (read-only git inspection only; no `.git/index.lock` writes).
- Post-PR `@codex review` is owner-invoked per ADR-001 decision 11; this pre-commit review is separate and is the substantive verification before commit.
- Per PMN-003 (e) refined, two-endpoint + re-poll review-state check applies to post-PR review only; this pre-commit review is single-channel (Codex desktop output) by definition.
