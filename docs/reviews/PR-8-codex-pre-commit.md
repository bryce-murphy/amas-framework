# PR-8 Codex desktop pre-commit review context

## Metadata

- PR ID: PR-8
- TASK ID: TASK-0008
- Branch: chore/task-0008-pmn-004-pr-7-cycle-learnings
- Base SHA: 4ac4640 (squash-merge of PR-7 on main, 2026-05-02T01:55:11Z)
- Builder: Claude Code (Claude Opus 4.7)
- Reviewer: Codex (GPT-5.5) — desktop, pre-commit, untracked working tree
- Architect (this PR's): Claude Opus 4.7 (Claude.ai Project)
- Owner: Bryce Murphy (`@bryce-murphy`)
- Framework version: AMAS v2.14.1 (dogfooded)
- Severity taxonomy: Blocking / Major / Minor (three-level; per repo discipline; standing per PMN-004 §5 (a))
- Disciplines applied (PMN-004 §5): severity taxonomy three-level (a); verification-command portability (b); no future-tense pre-commit claims (c); pre-commit cross-surface scope clarity (d); §23.6 prose-arithmetic decomposition (e); spec source citation correctness sweep (f)

## Builder claims to verify

The Builder asserts the following at hand-off to Codex desktop pre-commit review. Each claim is verifiable from the working tree at pre-commit time (no future-tense claims per PMN-004 §5 (c)).

1. **PMN-004 file authored at `docs/post-merge-notes/PMN-004-pr-7-cycle-learnings.md`** with the verbatim content from §4 of the TASK-0008 spec. Verifiable at pre-commit:
   - bash: `[ -f docs/post-merge-notes/PMN-004-pr-7-cycle-learnings.md ] && head -1 docs/post-merge-notes/PMN-004-pr-7-cycle-learnings.md`
   - cmd: `if exist docs\post-merge-notes\PMN-004-pr-7-cycle-learnings.md type docs\post-merge-notes\PMN-004-pr-7-cycle-learnings.md`
   - Expected first line: `# PMN-004 — PR-7 cycle learnings: claim-text drift defect class + pre-commit discipline confirmation + two-endpoint empirical validation`

2. **TASK-0008 handoff authored at `docs/handoffs/TASK-0008-pmn-004-pr-7-cycle-learnings.md`** with the verbatim content from §3.2 of the spec. Verifiable at pre-commit:
   - bash: `[ -f docs/handoffs/TASK-0008-pmn-004-pr-7-cycle-learnings.md ] && head -1 docs/handoffs/TASK-0008-pmn-004-pr-7-cycle-learnings.md`
   - cmd: `if exist docs\handoffs\TASK-0008-pmn-004-pr-7-cycle-learnings.md type docs\handoffs\TASK-0008-pmn-004-pr-7-cycle-learnings.md`
   - Expected first line: `# HANDOFF: TASK-0008 — PMN-004 PR-7 cycle learnings`

3. **PR-8 review-context file authored at `docs/reviews/PR-8-codex-pre-commit.md`** (this file). Verifiable at pre-commit:
   - bash: `[ -f docs/reviews/PR-8-codex-pre-commit.md ] && head -1 docs/reviews/PR-8-codex-pre-commit.md`
   - cmd: `if exist docs\reviews\PR-8-codex-pre-commit.md type docs\reviews\PR-8-codex-pre-commit.md`
   - Expected first line: `# PR-8 Codex desktop pre-commit review context`

4. **Total file count change at branch tip is exactly 3** (3 new + 0 modified). Verifiable at pre-commit:
   - bash: `git status --porcelain | wc -l` returns `3`; or `git diff --stat HEAD` shows `3 files changed`
   - cmd: `git status --porcelain | find /c /v ""` returns `3`
   - Each of the three files is in `??` (untracked) state pre-stage, or `A` (added) state post-stage

5. **No file outside the three new artifacts is modified**. Verifiable at pre-commit:
   - bash: `git status --porcelain | grep -v "^?? docs/" | wc -l` returns `0`
   - cmd: `git status --porcelain | findstr /v "^?? docs/" | find /c /v ""` returns `0`
   - No README change; no ADR change; no scaffold-stub change; no other repository file affected

6. **Tracked-file count would be 83 post-merge** (80 baseline + 3 new). Verifiable read-only at pre-commit (no `git add -A` or any index writes required; `.git/index.lock` is not touched):
   - bash: tracked baseline = `git ls-files | wc -l` returns `80`; new untracked = `git status --porcelain | grep -c "^?? "` returns `3`; arithmetic sum = `80 + 3 = 83`
   - cmd: tracked baseline = `git ls-files | find /c /v ""` returns `80`; new untracked = `git status --porcelain | findstr /b "??" | find /c /v ""` returns `3`; arithmetic sum = `80 + 3 = 83`
   - PowerShell: `(git ls-files | Measure-Object).Count + (git status --porcelain | Where-Object { $_ -match '^\?\? ' } | Measure-Object).Count` returns `83`
   - The baseline count of `80` matches `main` at base SHA `4ac4640`; the new-untracked count of `3` matches Claim 4 above; the sum `83` is the tracked count that would obtain after this PR's eventual squash-merge.

7. **Cross-surface count claim consistency**: file count claim "3" appears in (a) PR body draft (§6.3 of spec; post-commit surface, not pre-commit-verifiable per discipline (d)), (b) TASK-0008 handoff §"Validation run" Evidence section (filled at step-10 per discipline (c)), (c) this review-context file claim 4. All pre-commit-existing surfaces ((b) and (c)) agree on 3 (decomposition: 3 = PMN-004 + handoff + review-context = 1 + 1 + 1). No fourth pre-commit surface contains a competing count. Verifiable at pre-commit:
   - bash: `grep -c "3 files\|3 new\|count: 3\|exactly 3" docs/handoffs/TASK-0008-pmn-004-pr-7-cycle-learnings.md docs/reviews/PR-8-codex-pre-commit.md` returns `4` or more total matches across both files
   - cmd: `findstr /c:"3 files" /c:"3 new" /c:"count: 3" /c:"exactly 3" docs\handoffs\TASK-0008-pmn-004-pr-7-cycle-learnings.md docs\reviews\PR-8-codex-pre-commit.md | find /c /v ""` returns `4` or more
   - PowerShell: `(Select-String -Path docs/handoffs/TASK-0008-pmn-004-pr-7-cycle-learnings.md,docs/reviews/PR-8-codex-pre-commit.md -Pattern '3 files|3 new|count: 3|exactly 3').Count` returns `4` or more

8. **Severity taxonomy three-level enumeration**: this review-context file enumerates Blocking / Major / Minor with explicit definitions in `## Reviewer-direction shape` below. No two-level framing in any committed artifact in this PR. Verifiable at pre-commit:
   - bash: `grep -c "Blocking / Major / Minor" docs/reviews/PR-8-codex-pre-commit.md` returns `2` or more
   - cmd: `findstr /c:"Blocking / Major / Minor" docs\reviews\PR-8-codex-pre-commit.md`

9. **PMN-004 substantive content references the five candidate observations from PR-7 close hand-back synthesized into §2 (defect class), §3 (pre-commit gate), §4 (two-endpoint empirical confirmation), §5 (refined disciplines), §6 (§23.6 enhancements), §7 (forward integration), §8 (cross-references)**. Verifiable at pre-commit:
   - bash: `grep -cE "^## §[0-9]" docs/post-merge-notes/PMN-004-pr-7-cycle-learnings.md` returns `8` (level-2 §-section headers only; `^## ` excludes `### §2.1/2.2/2.3` subheaders)
   - PowerShell: `(Select-String -Path docs/post-merge-notes/PMN-004-pr-7-cycle-learnings.md -Pattern '^## §[0-9]').Count` returns `8`
   - cmd note: native `findstr /r "^## §[0-9]"` is unreliable on Windows due to OEM/UTF-8 codepage mismatch on the `§` byte sequence (returns spurious matches against `## Status` and `### §2.x` headers); use the PowerShell form above as the cmd-side equivalent. The PowerShell form is in scope per PMN-004 §5 (b) "PowerShell (alternative Windows environment)".

10. **Section-citation correctness in committed pre-commit artifacts**: every `§N` citation in `docs/handoffs/TASK-0008-pmn-004-pr-7-cycle-learnings.md` and `docs/reviews/PR-8-codex-pre-commit.md` (this file) refers to a section that exists in the source spec at the cited number, and where citations refer to sections internal to the committed artifacts themselves (e.g., handoff Exact next step references §7 / §11 of the spec; review-context references PMN-004 §5 (a)-(f), PMN-003 (a)/(e), ADR-001/ADR-003), each cited section resolves to an actual heading in the cited document. The spec source itself (`.claude/session-handoffs/TASK-0008-pmn-004-spec.md`) is gitignored per ADR-001 decision 15 and is not a committed pre-commit artifact; spec §-citations in committed artifacts therefore cannot be mechanically verified from the working tree alone. Verifiable at pre-commit:
   - bash: `grep -nE "§[0-9]+(\.[0-9]+)?" docs/handoffs/TASK-0008-pmn-004-pr-7-cycle-learnings.md docs/reviews/PR-8-codex-pre-commit.md` lists every line containing a §-citation across the two committed artifacts; visually verify each citation's target document and section number
   - cmd: `findstr /n /r "§[0-9]" docs\handoffs\TASK-0008-pmn-004-pr-7-cycle-learnings.md docs\reviews\PR-8-codex-pre-commit.md` produces the same listing
   - PowerShell: `Select-String -Path docs/handoffs/TASK-0008-pmn-004-pr-7-cycle-learnings.md,docs/reviews/PR-8-codex-pre-commit.md -Pattern '§[0-9]+(\.[0-9]+)?' | Format-Table LineNumber,Line` produces the same listing
   - Cross-document verification: for citations to PMN-004's own sections, run `grep -E "^## §[0-9]" docs/post-merge-notes/PMN-004-pr-7-cycle-learnings.md` (returns the 8 PMN-004 level-2 headers `§1` through `§8`); confirm each PMN-004-internal `§N` citation lands within that 1-8 range
   - Per PMN-004 §5 (f), citations to the source spec (`§3` step sequence, `§3.2`, `§4`, `§5`, `§6`, `§7`, `§8`, `§9`, `§11`) are out-of-tree by design (gitignored spec); their resolution is verified against the source spec's `## §N` headings at the time the spec is read by Builder. Builder attests at hand-back §11 that the spec-source-citation sweep was clean.

## Reviewer focus (Codex desktop)

For each Builder claim above, verify the verification command produces the asserted result. Specific focus areas (only pre-commit-existing surfaces enumerated per PMN-004 §5 (d)):

- **Pre-commit cross-surface count claim consistency (PMN-004 §5 (e))**: The number 3 appears in (a) PR-8 review-context claim 4 + claim 7 (this file), (b) TASK-0008 handoff §"Validation run" Evidence section. PR body is not a pre-commit surface; deferred to post-PR verification scope (per PMN-004 §5 (d) pre-commit cross-surface scope clarity). All pre-commit surfaces must agree on 3.

- **PMN-004 content fidelity**: Verify the `docs/post-merge-notes/PMN-004-pr-7-cycle-learnings.md` content matches §4 of the spec byte-for-byte. Em-dash (`—`, U+2014) verification: scan the file for byte sequence `E2 80 94`; should appear in §-headers and inline contexts as authored. Smart-quote substitution check: ensure no `'`/`'`/`"`/`"` (U+2018, U+2019, U+201C, U+201D) appear in PMN-004; ASCII single-quote `'` and double-quote `"` only.

- **TASK-0008 handoff metadata**: Confirm Linked PR field reads `<FILL AT PR-OPEN — substitute actual PR URL after gh pr create returns; per PMN-001 (k) handling>` at pre-commit. Confirm Timestamp field reads `<FILL AT BRANCH-CREATION — substitute current ISO-8601 UTC>` or has been substituted to a current ISO-8601 timestamp. Per PMN-004 §5 (c), the Validation run section must be filled at step-10 with actual results, not left as placeholder template at pre-commit.

- **Review-context completeness**: Verify all 10 Builder claims are present in this file with verification commands in both bash and cmd forms (per PMN-004 §5 (b) verification-command portability).

- **Severity taxonomy consistency (PMN-004 §5 (a))**: Confirm this review-context file enumerates Blocking / Major / Minor (three levels) with definitions, and no other taxonomy variant appears in any committed artifact in this PR. Two-level (Blocking / Minor) framing is a Blocking finding.

- **Section-citation correctness (PMN-004 §5 (f))**: Sweep the spec source for `§N` references; verify each cited section exists at the cited number. Defects are Minor unless the citation slip propagates to a downstream artifact (handoff Exact next step, review-context Reviewer focus, etc.), in which case Major.

- **Phantom-action claim verification**: Each Builder claim's verification command is itself directly verifiable. Codex desktop runs the command in whichever shell is available; reports result verbatim; flags any divergence from the Builder's asserted result.

- **No future-tense claims at pre-commit time (PMN-004 §5 (c))**: Sweep all 10 Builder claims for "will be" / "shall" / "to be filled" language. Any future-tense claim that does not have a pre-commit-verifiable counterpart is a Blocking finding.

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
- **Blocking**: defect that falsifies a Builder claim, contradicts PMN-004 substantive content, introduces cross-surface count drift on pre-commit-existing surfaces, breaks PMN-004 §5 disciplines (a)-(f), or surfaces future-tense claims at pre-commit time without pre-commit-verifiable counterparts. Cannot ship without revision.
- **Major**: defect that does not falsify a Builder claim but degrades artifact quality (e.g., minor wording inconsistency, suboptimal cross-reference path, section-citation slip propagated to downstream artifact). Can ship with documented exception via path (b); preferred path (a) revise.
- **Minor**: cosmetic or stylistic defect (e.g., trailing whitespace, ordering preference, section-citation slip not propagated to downstream artifact). Default path (b) record-and-proceed.

Action phrasing: each finding must use imperative `Action: <verb> <object>.` form (e.g., `Action: Update PMN-004 §2.2 paragraph 3 to match spec §4 byte-for-byte.`). Per PMN-002 (a) refined.

## Builder hand-back attestation

After Codex desktop pre-commit review completes, Builder reports:
- Codex review outcome (per the summary structure above)
- Path (a) revisions made, if any
- Path (b) acceptances recorded, if any
- §23.6 recapitulation-consistency re-check result after any path (a) revisions (per PMN-003 (a) refined; extended scope per PMN-004 §2.3 to include verification-command surfaces)

## Notes

- Codex desktop reviews the untracked working tree before commit (read-only git inspection only; no `.git/index.lock` writes).
- Post-PR `@codex review` is owner-invoked per ADR-001 decision 11; this pre-commit review is separate and is the substantive verification before commit.
- Per PMN-003 (e) refined empirically confirmed in PMN-004 §4, two-endpoint + re-poll review-state check applies to post-PR review only; this pre-commit review is single-channel (Codex desktop output) by definition. Pre-commit cross-surface scope clarity per PMN-004 §5 (d) excludes post-PR surfaces from this pre-commit review's focus areas.
