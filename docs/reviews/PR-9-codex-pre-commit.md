# PR-9 Codex desktop pre-commit review context

## Metadata

- PR ID: PR-9
- TASK ID: TASK-0009
- Branch: chore/task-0009-pmn-005-pr-8-cycle-learnings
- Base SHA: 56256ea (squash-merge of PR-8 on main, 2026-05-02T11:35:24Z)
- Builder: Claude Code (Claude Opus 4.7)
- Reviewer: Codex (GPT-5.5) — desktop, pre-commit, untracked working tree
- Architect (this PR's): Claude Opus 4.7 (Claude.ai Project)
- Owner: Bryce Murphy (`@bryce-murphy`)
- Framework version: AMAS v2.14.1 (dogfooded)
- Severity taxonomy: Blocking / Major / Minor (three-level; per repo discipline; standing per PMN-004 §5 (a))
- Disciplines applied (PMN-004 §5 (a)-(f) + PMN-005 refinements): severity taxonomy three-level (a); verification-command portability (b); no future-tense pre-commit claims (c); pre-commit cross-surface scope clarity (d); §23.6 prose-arithmetic decomposition (e) with PMN-005 sub-rule (e.1) cumulative-diff-stats re-derivation; spec source citation correctness sweep (f)
- PMN-005 refinements applied: PMN-003 (e) refined extended to comment-content verification against repo state; PMN-004 §5 (e) extended with sub-rule (e.1) cumulative-diff-stats re-derivation

## Builder claims to verify

The Builder asserts the following at hand-off to Codex desktop pre-commit review. Each claim is verifiable from the working tree at pre-commit time (no future-tense claims per PMN-004 §5 (c)).

1. **PMN-005 file authored at `docs/post-merge-notes/PMN-005-pr-8-cycle-learnings.md`** with the verbatim content from §2 of the TASK-0009 spec. Verifiable at pre-commit:
   - bash: `[ -f docs/post-merge-notes/PMN-005-pr-8-cycle-learnings.md ] && head -1 docs/post-merge-notes/PMN-005-pr-8-cycle-learnings.md`
   - cmd: `if exist docs\post-merge-notes\PMN-005-pr-8-cycle-learnings.md type docs\post-merge-notes\PMN-005-pr-8-cycle-learnings.md`
   - Expected first line: `# PMN-005 — PR-8 cycle learnings: reviewer-claimed-effects-don't-land defect class + pass-shape correlation hypothesis + cumulative-diff-stats sub-rule refinement`

2. **TASK-0009 handoff authored at `docs/handoffs/TASK-0009-pmn-005-pr-8-cycle-learnings.md`** with the verbatim content from §3 of the spec. Verifiable at pre-commit:
   - bash: `[ -f docs/handoffs/TASK-0009-pmn-005-pr-8-cycle-learnings.md ] && head -1 docs/handoffs/TASK-0009-pmn-005-pr-8-cycle-learnings.md`
   - cmd: `if exist docs\handoffs\TASK-0009-pmn-005-pr-8-cycle-learnings.md type docs\handoffs\TASK-0009-pmn-005-pr-8-cycle-learnings.md`
   - Expected first line: `# HANDOFF: TASK-0009 — PMN-005 PR-8 cycle learnings`

3. **PR-9 review-context file authored at `docs/reviews/PR-9-codex-pre-commit.md`** (this file). Verifiable at pre-commit:
   - bash: `[ -f docs/reviews/PR-9-codex-pre-commit.md ] && head -1 docs/reviews/PR-9-codex-pre-commit.md`
   - cmd: `if exist docs\reviews\PR-9-codex-pre-commit.md type docs\reviews\PR-9-codex-pre-commit.md`
   - Expected first line: `# PR-9 Codex desktop pre-commit review context`

4. **Total file count change at branch tip is exactly 3** (3 new + 0 modified). Verifiable at pre-commit:
   - bash: `git status --porcelain | wc -l` returns `3`
   - cmd: `git status --porcelain | find /c /v ""` returns `3`
   - Each of the three files is in `?? docs/...` form (untracked-new); no `M` (modified) entries.

5. **No file outside the three new artifacts is touched**. Verifiable at pre-commit:
   - bash: `git status --porcelain | grep -v "^?? docs/" | wc -l` returns `0`
   - cmd: `git status --porcelain | findstr /v /c:"?? docs/" | find /c /v ""` returns `0`

6. **Tracked-file count delta**: branch tip would be 86 tracked files post-commit-and-push (83 baseline + 3 new). Verifiable at pre-commit (read-only; no `git add -A` invoked):
   - bash: `git ls-files | wc -l` returns `83` (baseline tracked, unchanged from base SHA `56256ea`)
   - bash: `git status --porcelain | grep -c "^?? "` returns `3` (new untracked)
   - Arithmetic sum: `83 + 3 = 86` would-be-tracked-post-merge
   - cmd: `git ls-files | find /c /v ""` returns `83`; `git status --porcelain | findstr /b "?? " | find /c /v ""` returns `3`
   - PowerShell: `(git ls-files).Count` returns `83`; `(git status --porcelain | Select-String -Pattern '^\?\? ').Count` returns `3`
   - Note: this claim is read-only and does not require `git add -A`; `.git/index.lock` is not touched at any point during step-10 or Codex pre-commit verification.

7. **Cross-surface count claim consistency**: file count claim "3" appears in (a) PR body draft (§6.3 of spec; post-commit surface, not pre-commit-verifiable per discipline (d)), (b) TASK-0009 handoff §"Validation run" Evidence section (filled at step-10 per discipline (c)), (c) this review-context file claim 4. All pre-commit-existing surfaces ((b) and (c)) agree on 3 (decomposition: 3 = PMN-005 + handoff + review-context = 1 + 1 + 1). No fourth pre-commit surface contains a competing count. Verifiable at pre-commit:
   - bash: `grep -c "3 files\|3 new\|count: 3\|exactly 3" docs/handoffs/TASK-0009-pmn-005-pr-8-cycle-learnings.md docs/reviews/PR-9-codex-pre-commit.md` returns `4` or more total matches across both files
   - cmd: `findstr /c:"3 files" /c:"3 new" /c:"count: 3" /c:"exactly 3" docs\handoffs\TASK-0009-pmn-005-pr-8-cycle-learnings.md docs\reviews\PR-9-codex-pre-commit.md | find /c /v ""` returns `4` or more
   - PowerShell: `(Select-String -Path docs/handoffs/TASK-0009-pmn-005-pr-8-cycle-learnings.md,docs/reviews/PR-9-codex-pre-commit.md -Pattern '3 files|3 new|count: 3|exactly 3').Count` returns `4` or more

8. **Severity taxonomy three-level enumeration**: this review-context file enumerates Blocking / Major / Minor with explicit definitions in `## Reviewer-direction shape` below. No two-level framing in any committed artifact in this PR. Verifiable at pre-commit:
   - bash: `grep -c "Blocking / Major / Minor" docs/reviews/PR-9-codex-pre-commit.md` returns `2` or more
   - cmd: `findstr /c:"Blocking / Major / Minor" docs\reviews\PR-9-codex-pre-commit.md`

9. **PMN-005 substantive content references the three candidate observations from PR-8 close hand-back synthesized into §1 (cycle context), §2 (reviewer-claimed-effects-don't-land defect class with two sub-shapes), §3 (pass-shape correlation hypothesis preliminary), §4 (path-(a)-revision-propagation gap on Validation run Evidence / cumulative diff stats sub-rule), §5 (refined disciplines summary), §6 (anticipated forward integration), §7 (cross-references)**. Verifiable at pre-commit:
   - bash: `grep -cE "^## §[0-9]" docs/post-merge-notes/PMN-005-pr-8-cycle-learnings.md` returns `7` (level-2 §-section headers only; `^## ` excludes `### §2.1/§3.1/etc.` subheaders)
   - PowerShell: `(Select-String -Path docs/post-merge-notes/PMN-005-pr-8-cycle-learnings.md -Pattern '^## §[0-9]').Count` returns `7`
   - cmd note: native `findstr /r "^## §[0-9]"` is unreliable on Windows due to OEM/UTF-8 codepage mismatch on the `§` byte sequence; use the PowerShell form above as the cmd-side equivalent. The PowerShell form is in scope per PMN-004 §5 (b) "PowerShell (alternative Windows environment)".

10. **Section-citation correctness in committed pre-commit artifacts**: every `§N` citation in `docs/handoffs/TASK-0009-pmn-005-pr-8-cycle-learnings.md` and `docs/reviews/PR-9-codex-pre-commit.md` (this file) refers to a section that exists in the source spec at the cited number. For citations to PMN-004's own sections, each §N citation must land in the 1-8 range (PMN-004 has 8 level-2 §-headers). For citations to PMN-005's own sections, each §N citation must land in the 1-7 range (PMN-005 has 7 level-2 §-headers). The spec source itself (`.claude/session-handoffs/TASK-0009-pmn-005-spec.md`) is gitignored per ADR-001 decision 15. Verifiable at pre-commit:
    - bash: `grep -nE "§[0-9]+(\.[0-9]+)?" docs/handoffs/TASK-0009-pmn-005-pr-8-cycle-learnings.md docs/reviews/PR-9-codex-pre-commit.md` lists every line containing a §-citation; visually verify each citation's target document and section number
    - cmd: `findstr /n /r "§[0-9]" docs\handoffs\TASK-0009-pmn-005-pr-8-cycle-learnings.md docs\reviews\PR-9-codex-pre-commit.md` produces the same listing
    - PowerShell: `Select-String -Path docs/handoffs/TASK-0009-pmn-005-pr-8-cycle-learnings.md,docs/reviews/PR-9-codex-pre-commit.md -Pattern '§[0-9]+(\.[0-9]+)?' | Format-Table LineNumber,Line` produces the same listing
    - Cross-document verification PMN-004: for citations to PMN-004's own sections, confirm each cited `§N` lands within `1`-`8` range (PMN-004 has 8 level-2 §-headers per PR-8 review-context claim 9 attestation)
    - Cross-document verification PMN-005: for citations to PMN-005's own sections, run `grep -E "^## §[0-9]" docs/post-merge-notes/PMN-005-pr-8-cycle-learnings.md` (returns 7 PMN-005 level-2 headers `§1` through `§7`); confirm each PMN-005-internal `§N` citation lands within that 1-7 range
    - Per PMN-004 §5 (f) and PMN-005 §4.5, citations to the source spec (`§N` references in handoff "Exact next step" pointing to spec sections) are out-of-tree by design (gitignored spec); their resolution is verified against the source spec's `## §N` headings at the time the spec is read by Builder. Builder attests at hand-back §10 that the spec-source-citation sweep was clean.
    - Iterative-to-convergence application: per PMN-005 §4.3 empirical evidence that section-citation slips can survive a single iteration of self-review, this sweep is run multiple times until no slip is detected (fixed-point convergence). PR-8 review-context claim 10 articulates the same convergence requirement.

## Reviewer focus (Codex desktop)

For each Builder claim above, verify the verification command produces the asserted result. Specific focus areas (only pre-commit-existing surfaces enumerated per PMN-004 §5 (d)):

- **Pre-commit cross-surface count claim consistency (PMN-004 §5 (e) + PMN-005 sub-rule (e.1))**: The number 3 appears in (a) PR-9 review-context claim 4 + claim 7 (this file), (b) TASK-0009 handoff §"Validation run" Evidence section. PR body is not a pre-commit surface; deferred to post-PR verification scope (per PMN-004 §5 (d) pre-commit cross-surface scope clarity). All pre-commit surfaces must agree on 3.

- **Cumulative-diff-stats re-derivation (PMN-005 §4.4 sub-rule (e.1))**: any per-file insertion / deletion counts in TASK-0009 handoff §"Validation run" Evidence section must match `git diff --stat HEAD` exactly (no approximate counts; no `~`-prefixed numbers). If the Evidence section is empty pending step-10 fill, that is acceptable per PMN-004 §5 (c) — the Evidence is filled at step-10, not pre-step-10. If the Evidence section contains any number, that number must be exact.

- **PMN-005 content fidelity**: Verify the `docs/post-merge-notes/PMN-005-pr-8-cycle-learnings.md` content matches §2 of the spec byte-for-byte. Em-dash (`—`, U+2014) verification: scan the file for byte sequence `E2 80 94`; should appear in §-headers and inline contexts as authored. Smart-quote substitution check: ensure no `'`/`'`/`"`/`"` (U+2018, U+2019, U+201C, U+201D) appear in PMN-005; ASCII single-quote `'` and double-quote `"` only.

- **TASK-0009 handoff metadata**: Confirm Linked PR field reads `<FILL AT PR-OPEN — substitute actual PR URL after gh pr create returns; per PMN-001 (k) handling>` at pre-commit. Confirm Timestamp field reads `<FILL AT BRANCH-CREATION — substitute current ISO-8601 UTC>` or has been substituted to a current ISO-8601 timestamp. Per PMN-004 §5 (c), the Validation run section Results subsection must be filled at step-10 with actual results, not left as placeholder template at pre-commit. Per PMN-005 §4.4 sub-rule (e.1), the Evidence subsection's cumulative-diff-stats line must be populated only with landed exact counts from `git diff --stat HEAD` immediately before commit.

- **Review-context completeness**: Verify all 10 Builder claims are present in this file with verification commands in both bash and cmd forms (per PMN-004 §5 (b) verification-command portability).

- **Severity taxonomy consistency (PMN-004 §5 (a))**: Confirm this review-context file enumerates Blocking / Major / Minor (three levels) with definitions, and no other taxonomy variant appears in any committed artifact in this PR. Two-level (Blocking / Minor) framing is a Blocking finding.

- **Section-citation correctness (PMN-004 §5 (f) + PMN-005 §4.3 iterative convergence)**: Sweep the spec source for `§N` references; verify each cited section exists at the cited number. PMN-004-internal `§N` citations must land in 1-8 range. PMN-005-internal `§N` citations must land in 1-7 range. Iterative-to-convergence application is required (PMN-005 §4.3 empirical evidence): rerun the sweep after any path-(a) revision until no slip is detected.

- **Phantom-action claim verification (PMN-005 §2.5 five-point pattern)**: Each Builder claim's verification command is itself directly verifiable. Codex desktop runs the command in whichever shell is available; reports result verbatim; flags any divergence from the Builder's asserted result. Additionally per PMN-005 §2.5, any reviewer comment (including pre-commit Codex's own findings) claiming a commit SHA, file addition, or file modification is verifiable against repository state via `gh api repos/.../commits/<sha>` and `gh api repos/.../contents/<path>`; unreachable claims are informational-only.

- **No future-tense claims at pre-commit time (PMN-004 §5 (c))**: Sweep all 10 Builder claims for "will be" / "shall" / "to be filled" language. Any future-tense claim that does not have a pre-commit-verifiable counterpart is a Blocking finding. Note: phrases of the form "will be filled at step-10" referring to the Validation run Results / Evidence subsections are acceptable per discipline (c) because step-10 self-verification populates these subsections before commit.

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
- **Blocking**: defect that falsifies a Builder claim, contradicts PMN-005 substantive content, contradicts PMN-004 §5 disciplines, introduces cross-surface count drift on pre-commit-existing surfaces, breaks PMN-005 sub-rule (e.1) cumulative-diff-stats re-derivation, surfaces a section-citation slip on PMN-004 (out-of-range 1-8) or PMN-005 (out-of-range 1-7) §-citations, or surfaces future-tense claims at pre-commit time without pre-commit-verifiable counterparts. Cannot ship without revision.
- **Major**: defect that does not falsify a Builder claim but degrades artifact quality (e.g., minor wording inconsistency, suboptimal cross-reference path, section-citation slip propagated to downstream artifact, prose-arithmetic decomposition imprecision). Can ship with documented exception via path (b); preferred path (a) revise.
- **Minor**: cosmetic or stylistic defect (e.g., trailing whitespace, ordering preference, section-citation slip not propagated to downstream artifact). Default path (b) record-and-proceed.

Action phrasing: each finding must use imperative `Action: <verb> <object>.` form (e.g., `Action: Update PMN-005 §2.2 paragraph 3 to match spec §2.2 byte-for-byte.`). Per PMN-002 (a) refined.

## Builder hand-back attestation

After Codex desktop pre-commit review completes, Builder reports:
- Codex review outcome (per the summary structure above)
- Path (a) revisions made, if any
- Path (b) acceptances recorded, if any
- §23.6 recapitulation-consistency re-check result after any path (a) revisions (per PMN-003 (a) refined; extended scope per PMN-004 §2.3 to include verification-command surfaces; further extended scope per PMN-005 §4.4 sub-rule (e.1) to include cumulative-diff-stats re-derivation)
- Section-citation correctness sweep result after any path (a) revisions, applied iteratively to convergence per PMN-005 §4.3
- Cumulative-diff-stats Evidence subsection populated with landed exact counts from `git diff --stat HEAD` immediately before commit, per PMN-005 §4.4 sub-rule (e.1)

## Notes

- Codex desktop reviews the untracked working tree before commit (read-only git inspection only; no `.git/index.lock` writes).
- Post-PR `@codex review` is owner-invoked per ADR-001 decision 11; this pre-commit review is separate and is the substantive verification before commit.
- PMN-005 introduces the five-point Architect-side post-handback check pattern (extension of PMN-003 (g) four-point pattern). The fifth point (comment-content claim verification against repository state) applies to post-PR Codex review findings as well as to any other reviewer-emitted commit-SHA or file-addition claim. The fifth point is operationally cheap (one `gh api` call per claim); the benefit is structural (Architect adjudicates against verified repo state, not against asserted repo state).
- PMN-005 §3 articulates a preliminary pass-shape correlation hypothesis. This review-context does not test the hypothesis; the hypothesis is for future-cycle data collection. The two-endpoint polling discipline (PMN-003 (e) refined) remains the canonical operational discipline regardless of hypothesis confirmation status.
