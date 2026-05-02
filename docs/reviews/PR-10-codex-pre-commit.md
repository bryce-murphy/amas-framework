# PR-10 Codex desktop pre-commit review context

## Metadata

- PR ID: PR-10
- TASK ID: TASK-0010
- Branch: feat/task-0010-core-part-a
- Base SHA: 3d10c76 (squash-merge of PR-9 on main, 2026-05-02)
- Builder: Claude Code (Claude Opus 4.7)
- Reviewer: Codex (GPT-5.5) — desktop, pre-commit, untracked working tree
- Architect (this PR's): Claude Opus 4.7 (Claude.ai Project)
- Owner: Bryce Murphy (`@bryce-murphy`)
- Framework version: AMAS v2.14.1 (dogfooded); production target AMAS v3.0
- Severity taxonomy: Blocking / Major / Minor (three-level; per repo discipline; standing per PMN-004 §5 (a))
- Disciplines applied (PMN-004 §5 (a)-(f) + PMN-005 refinements): severity taxonomy three-level (a); verification-command portability (b); no future-tense pre-commit claims (c); pre-commit cross-surface scope clarity (d); §23.6 prose-arithmetic decomposition (e) with PMN-005 sub-rule (e.1) cumulative-diff-stats re-derivation; spec source citation correctness sweep (f); §23.6.2 iterative-to-fixed-point self-review
- PMN-005 refinements applied: PMN-003 (e) refined extended to comment-content verification against repo state; PMN-004 §5 (e) extended with sub-rule (e.1) cumulative-diff-stats re-derivation; PMN-003 (g) four-point post-handback check extended to five-point per PMN-005 §2.5

## Builder claims to verify

The Builder asserts the following at hand-off to Codex desktop pre-commit review. Each claim is verifiable from the working tree at pre-commit time (no future-tense claims per PMN-004 §5 (c)). PR-10 is the first cycle authoring substantive canonical content into `core.md` (Part A); claims 1, 2, and 10 cover the canonical-content surface specifically.

1. **`core.md` contains the five canonical leaf sections (§8.1.1.1, §8.1.1.2, §23.6.1, §23.6.2, §24.3.1)** at the §-numbering positions specified in spec §2 (TASK-0010 spec; gitignored per ADR-001 decision 15). Verifiable at pre-commit:
   - bash: `grep -nE "^##### §8\.1\.1\.[12]\.|^#### §23\.6\.[12]\.|^#### §24\.3\.1\." core.md` returns exactly 5 lines, in document order
   - cmd note: native `findstr` is unreliable on Windows for the `§` (U+00A7) byte sequence due to OEM/UTF-8 codepage mismatch. Use the PowerShell form below as the cmd-side equivalent. The PowerShell form is in scope per PMN-004 §5 (b) "PowerShell (alternative Windows environment)".
   - PowerShell: `Select-String -Path core.md -Pattern '^##### §8\.1\.1\.[12]\.|^#### §23\.6\.[12]\.|^#### §24\.3\.1\.' | Format-Table LineNumber,Line` returns exactly 5 matches, in document order

2. **`core.md` contains parent frames (§8, §8.1, §8.1.1, §23, §23.6, §24, §24.2, §24.3)** per spec §2.0 minimal-frames approach. Verifiable at pre-commit:
   - bash: `grep -nE "^## §8\.|^### §8\.1\.|^#### §8\.1\.1\.|^## §23\.|^### §23\.6\.|^## §24\.|^### §24\.2\.|^### §24\.3\." core.md` returns exactly 8 lines matching parent-frame headers
   - PowerShell: `Select-String -Path core.md -Pattern '^(## §8\.|### §8\.1\.|#### §8\.1\.1\.|## §23\.|### §23\.6\.|## §24\.|### §24\.[23]\.)' | Format-Table LineNumber,Line` returns exactly 8 matches

3. **`docs/handoffs/TASK-0010-core-part-a.md` exists with metadata block** per spec §3.1. Verifiable at pre-commit:
   - bash: `[ -f docs/handoffs/TASK-0010-core-part-a.md ] && head -1 docs/handoffs/TASK-0010-core-part-a.md`
   - cmd: `if exist docs\handoffs\TASK-0010-core-part-a.md type docs\handoffs\TASK-0010-core-part-a.md`
   - Expected first line: `# TASK-0010 — core.md Part A canonical-content authoring`

4. **`docs/reviews/PR-10-codex-pre-commit.md` exists (this file)** with the 11 enumerated claims and Reviewer-direction shape per spec §4. Verifiable at pre-commit:
   - bash: `[ -f docs/reviews/PR-10-codex-pre-commit.md ] && grep -c "^[0-9]\+\. \*\*" docs/reviews/PR-10-codex-pre-commit.md` returns `11` (eleven enumerated claims with `**bold**` opening)
   - PowerShell: `(Select-String -Path docs/reviews/PR-10-codex-pre-commit.md -Pattern '^[0-9]+\. \*\*').Count` returns `11`

5. **`README.md` framework-version cell updated** from `v2.14.1` to `v2.15` per spec §2.9; per-PR-row added for PR-10. Verifiable at pre-commit:
   - bash: `grep -E "v2\.15" README.md | head -3` returns at least one match
   - bash: `grep -E "PR-10" README.md | head -3` returns at least one match (the PR-10 row)
   - PowerShell: `Select-String -Path README.md -Pattern 'v2\.15'` returns at least one match
   - cmd: `findstr /c:"v2.15" README.md` returns at least one line; `findstr /c:"PR-10" README.md` returns at least one line

6. **Tracked-file count is `88`** post-staging (`git ls-files | wc -l` returns `88` after `git add` of the 4 changed files; or `86 base + 2 new = 88` derivable read-only at pre-commit). Verifiable at pre-commit:
   - bash (read-only, pre-staging): `git ls-files | wc -l` returns `86`; `git status --porcelain | grep -c "^?? docs/"` returns `2` (handoff + review-context); arithmetic sum `86 + 2 = 88`
   - bash (post-staging): `git ls-files | wc -l` returns `88`
   - cmd: `git ls-files | find /c /v ""`
   - PowerShell: `(git ls-files | Measure-Object).Count`
   - Decomposition: 86 base + 2 new files (`docs/handoffs/TASK-0010-core-part-a.md` + `docs/reviews/PR-10-codex-pre-commit.md`) = 88. The two modified files (`core.md`, `README.md`) do not change tracked-file count.

7. **Working-tree status verification** (separate pre-commit and post-commit expectations per spec §7.1 timing notes). Verifiable at pre-commit and at post-commit (step 14+):
   - **Pre-commit, pre-stage state** (Codex review-window; per Notes below, Codex desktop reviews the working tree pre-stage — read-only inspection without `git add`): `git status --porcelain` returns the 4 expected changes in `XY <path>` porcelain v1 format (X = index status, Y = work-tree status) — ` M README.md` and ` M core.md` (Y=M, unstaged-modified-tracked); `?? docs/handoffs/TASK-0010-core-part-a.md` and `?? docs/reviews/PR-10-codex-pre-commit.md` (untracked-new). Non-empty output is the EXPECTED pre-commit pre-stage state — Reviewer should NOT flag this as a Blocking failure.
   - **Post-commit state** (step 14+): `git status --porcelain` returns empty.
   - cmd / PowerShell: same commands, same expected outputs per timing.

8. **Cumulative diff stats**: per `git diff --stat <merge-base>..HEAD` — exact insertions/deletions per file, populated at step-10 with landed exact counts only (no `~`-prefixed numbers per §23.6.1.1 sub-rule (e.1)). Verifiable at pre-commit:
   - bash: `git diff --stat $(git merge-base HEAD origin/main)..HEAD` (post-staging-and-commit; or `git diff --stat --cached` at staged-pre-commit state)
   - cmd / PowerShell: same command
   - Expected shape: 4 changed files (core.md modified, TASK-0010 new, PR-10-codex new, README.md modified) with exact insertion/deletion counts; counts populated in handoff §"Validation run" Evidence section.

9. **Severity-taxonomy three-level enumeration**: this review-context file enumerates Blocking / Major / Minor with explicit definitions in `## Reviewer-direction shape` per PMN-004 §5 (a). No two-level framing in any committed artifact in this PR. Verifiable at pre-commit:
   - bash: `grep -c "Blocking / Major / Minor" docs/reviews/PR-10-codex-pre-commit.md` returns `2` or more
   - cmd: `findstr /c:"Blocking / Major / Minor" docs\reviews\PR-10-codex-pre-commit.md`
   - PowerShell: `(Select-String -Path docs/reviews/PR-10-codex-pre-commit.md -Pattern 'Blocking / Major / Minor').Count` returns `2` or more

10. **Section-citation correctness in committed pre-commit artifacts**: every `§N` citation in `core.md`, `docs/handoffs/TASK-0010-core-part-a.md`, and this file lands within the corresponding source-document's §-range. Cross-document verification:
    - core.md internal cross-references (Part A scope): §8.1.1.1 ↔ §8.1.1.2 ↔ §23.6.1 ↔ §23.6.2 ↔ §24.2 ↔ §24.3 ↔ §24.3.1 — each referenced §-number resolves to an actual heading authored in this PR
    - core.md forward-references (per spec §1.3.1): §8.2, §8.3, §23.5 are forward references to Part B sections not authored in this PR; their resolution is deferred to Part B authoring (TASK-0011 onward) and is out of Part A scope per spec §1.3.1
    - PMN-005 internal §-citations: each lands in 1-7 range (PMN-005 has 7 level-2 §-headers `§1` through `§7`)
    - PMN-004 internal §-citations: each lands in 1-8 range (PMN-004 has 8 level-2 §-headers `§1` through `§8`)
    - PMN-003 observation-letter citations: each lands in (a)-(g) range
    - ADR-001 decision references: each lands in 1-15 range (ADR-001 has 15 enumerated decisions)
    - ADR-003 §-references: §Consequences, §Alternatives considered, Decisions 1-3
    - Verifiable at pre-commit:
      - bash: `grep -nE "§[0-9]+(\.[0-9]+)*" core.md docs/handoffs/TASK-0010-core-part-a.md docs/reviews/PR-10-codex-pre-commit.md` lists every line containing a §-citation; visually verify each citation's target document and section number
      - PowerShell: `Select-String -Path core.md,docs/handoffs/TASK-0010-core-part-a.md,docs/reviews/PR-10-codex-pre-commit.md -Pattern '§[0-9]+(\.[0-9]+)*' | Format-Table LineNumber,Line` produces the same listing
    - Iterative-to-convergence application: per PMN-005 §4.3 / §23.6.2 empirical evidence that section-citation slips can survive a single iteration of self-review, this sweep is run multiple times until two consecutive zero-defect iterations are reached (fixed-point convergence). Iteration count recorded in handoff §"Validation run" Evidence section.

11. **Spec-source citations**: out-of-tree by design (gitignored spec per ADR-001 decision 15); resolved against `.claude/session-handoffs/TASK-0010-spec.md` headings at the time the spec is read by Builder. Builder attests at hand-back §10 that the spec-source-citation sweep was clean. Verifiable at pre-commit:
    - bash: `[ -f .claude/session-handoffs/TASK-0010-spec.md ] && grep -cE "^## §[0-9]" .claude/session-handoffs/TASK-0010-spec.md` returns the count of level-2 §-headers in the spec
    - Builder attestation: spec-source `§N` references in handoff and this review-context resolve to actual `## §N` headings in the spec at session start

## Reviewer focus (Codex desktop)

For each Builder claim above, verify the verification command produces the asserted result. Specific focus areas (only pre-commit-existing surfaces enumerated per PMN-004 §5 (d)):

- **Pre-commit cross-surface count claim consistency** (per PMN-004 §5 (e) + §23.6.1.1 sub-rule (e.1)): The number `88` (tracked-file count) appears in (a) `docs/handoffs/TASK-0010-core-part-a.md` §Current state, (b) this file's claim 6, (c) PR body §3 file count narrative (PR body is post-commit surface, deferred to post-PR verification scope per PMN-004 §5 (d)). All pre-commit-existing surfaces ((a) and (b)) must agree on `88`.

- **Cumulative-diff-stats re-derivation** (§23.6.1.1 sub-rule (e.1)): per-file insertion/deletion counts in `docs/handoffs/TASK-0010-core-part-a.md` §"Validation run" Evidence section must match `git diff --stat <merge-base>..HEAD` exactly. No approximate counts; no `~`-prefixed numbers. If the Evidence section is empty pending step-10 fill, that is acceptable per PMN-004 §5 (c). If the Evidence section contains any number, that number must be exact.

- **Section-citation correctness in `core.md`**: every `§N` cross-reference between the five leaves and the parent frames resolves. Codex sweeps `core.md` for `§[0-9]+(\.[0-9]+)*` patterns; each must land at an actual heading. Known forward-reference set per spec §1.3.1 — `§8.2`, `§8.3`, `§23.5` — is out-of-Part-A-scope; do not flag these as Blocking findings. Report all other dangling references as Blocking findings.

- **Severity-taxonomy compliance** (PMN-004 §5 (a)): this file enumerates three levels (Blocking / Major / Minor) per repo discipline. Two-level framing in any artifact is a Blocking finding.

- **Scope-leakage check**: no substantive content in `core.md` outside the five leaves and minimal parent frames per spec §2. No content authored that would belong to Part B (TASK-0011 onward). No accidental modification to FEAT-0001 stub frontmatter on `core.md`.

- **Phantom-action claim verification** (per §8.1.1.2 / PMN-005 §2.5): each Builder claim's verification command is itself directly verifiable. Codex runs the command; reports result verbatim; flags any divergence from the Builder's asserted result. Additionally per PMN-005 §2.5, any Codex-emitted comment claiming a commit SHA, file addition, or file modification is verifiable against repository state via `gh api repos/.../commits/<sha>` and `gh api repos/.../contents/<path>`; unreachable claims are informational-only.

- **README.md modification scope**: only the framework-version cell and the PR-10 row are added/modified. All other content unchanged byte-for-byte. Codex diffs README.md against `main` to confirm.

- **Byte-exact prescription compliance** (per spec §2.0 / §6.2): the canonical text in `core.md` (the five leaves + parent frames) matches spec §2.1-§2.8 verbatim. No paraphrase; no rewording; no creative addition. Discrepancies in canonical text body are Blocking findings.

- **No future-tense claims at pre-commit time** (PMN-004 §5 (c)): Sweep all 11 Builder claims for "will be" / "shall" / "to be filled" language. Any future-tense claim that does not have a pre-commit-verifiable counterpart is a Blocking finding. Note: phrases of the form "filled at step-10" referring to the Validation run Results / Evidence subsections are acceptable per discipline (c) because step-10 self-verification populates these subsections before commit.

## Reviewer-direction shape (claim-verification-only, imperative `Action:` per PMN-002 (a))

Codex's output structure:

For each claim 1 through 11 above, output one of:
- `Claim N: Verified clean.`
- `Claim N: <Severity> finding — <description>; verification command output: <verbatim>; recommended action: <path (a) revise / path (b) record-and-proceed>.`

After per-claim verdict, output an overall summary:
- Total claims: 11
- Verified clean: <count>
- Blocking findings: <count>
- Major findings: <count>
- Minor findings: <count>
- Recommended disposition: clean / revise (path (a)) / record-and-proceed (path (b))

Severity definitions for this review:

- **Blocking** — finding that prevents merge until addressed (e.g., spec-prescribed canonical content missing from `core.md`; section-citation slip producing dangling reference outside the known forward-reference set §8.2/§8.3/§23.5; severity-taxonomy non-compliance; substantive content outside Part A scope; cumulative-diff-stats drift on pre-commit-existing surface; future-tense pre-commit claim without verifiable counterpart; byte-exact prescription violation in canonical text). Cannot ship without revision.
- **Major** — finding that should be addressed pre-merge but does not block merge in the absence of address (e.g., minor prose-arithmetic drift caught post-step-10; clarifying language improvement; cross-reference forward-pointing where backward-pointing would be clearer). Default disposition path (a) revise.
- **Minor** — finding noted for record but not requiring address (e.g., stylistic preference; future-section forward-reference noted as such; cosmetic issue not propagated to downstream artifact). Default disposition path (b) record-and-proceed.

Action phrasing examples in the Reviewer-direction shape:

```
Action: For each enumerated claim above, verify the verification command produces the asserted result. Report any divergence as a Blocking finding regardless of magnitude. Report verification commands' outputs verbatim.

Action: Sweep core.md for §-citations matching the pattern §[0-9]+(\.[0-9]+)*. For each citation, verify the cited §-number resolves to an actual heading in core.md. The known forward-reference set per spec §1.3.1 — §8.2, §8.3, §23.5 — is out-of-Part-A-scope; do not flag these as Blocking findings. Report all other dangling references as Blocking findings.

Action: Verify the README.md diff against main is limited to (a) the framework-version cell update from v2.14.1 to v2.15 and (b) one new PR-10 row. Any modification outside these two locations is a Blocking finding.

Action: Run the cumulative-diff-stats re-derivation per §23.6.1.1 sub-rule (e.1). Compare the Validation run Evidence section in the handoff against `git diff --stat` output. Any discrepancy is a Blocking finding. Any `~`-prefixed number in the Evidence section is a Blocking finding.

Action: Verify scope-leakage. The five leaf canonical sections plus minimal parent frames per spec §2.0 are in scope. Any substantive content in core.md outside this scope is a Blocking finding.
```

## Builder hand-back attestation

After Codex desktop pre-commit review completes, Builder reports:
- Codex review outcome (per the summary structure above)
- Path (a) revisions made, if any
- Path (b) acceptances recorded, if any
- §23.6 recapitulation-consistency re-check result after any path (a) revisions (per PMN-003 (a) refined; extended scope per PMN-004 §2.3 to include verification-command surfaces; further extended scope per PMN-005 §4.4 sub-rule (e.1) to include cumulative-diff-stats re-derivation)
- Section-citation correctness sweep result after any path (a) revisions, applied iteratively to convergence per PMN-005 §4.3 / §23.6.2
- Cumulative-diff-stats Evidence subsection populated with landed exact counts from `git diff --stat <merge-base>..HEAD` immediately before commit, per PMN-005 §4.4 sub-rule (e.1)

## Notes

- Codex desktop reviews the untracked working tree before commit (read-only git inspection only; no `.git/index.lock` writes).
- Post-PR `@codex review` is owner-invoked per ADR-001 decision 11; this pre-commit review is separate and is the substantive verification before commit.
- PR-10 is the first cycle authoring substantive canonical content into `core.md`. The five leaves canonicalized in this PR (§8.1.1.1, §8.1.1.2, §23.6.1, §23.6.2, §24.3.1) are themselves the framework disciplines applied to this cycle's authoring — meta-recursive application per spec §1.7. The discipline being canonicalized governs the cycle that canonicalizes it.
- Forward references to §8.2, §8.3, §23.5 in `core.md` Part A are intentional per spec §1.3.1. They resolve when Part B (TASK-0011 onward) lands. Reviewer recognizes them as out-of-Part-A-scope citations rather than dangling references.
- PMN-005 introduces the five-point Architect-side post-handback check pattern (extension of PMN-003 (g) four-point pattern). The fifth point (comment-content claim verification against repository state) applies to post-PR Codex review findings as well as to any other reviewer-emitted commit-SHA or file-addition claim. The fifth point is operationally cheap (one `gh api` call per claim); the benefit is structural (Architect adjudicates against verified repo state, not against asserted repo state). §24.3.1 of `core.md` (canonicalized in this PR) names this as the default check pattern.
