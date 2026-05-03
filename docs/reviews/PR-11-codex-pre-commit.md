# PR-11 Codex desktop pre-commit review context

## Metadata

- PR ID: PR-11
- TASK ID: TASK-0011
- Branch: feat/task-0011-pmn-006
- Base SHA: 80f5a4a (squash-merge of PR-10 on main, 2026-05-02)
- Builder: Claude Code (Claude Opus 4.7)
- Reviewer: Codex (GPT-5.5) — desktop, pre-commit, untracked working tree
- Architect (this PR's): Claude Opus 4.7 (Claude.ai Project)
- Owner: Bryce Murphy (`@bryce-murphy`)
- Framework version: AMAS v2.15 (dogfooded post-PR-10); production target AMAS v3.0
- Severity taxonomy: Blocking / Major / Minor (three-level; per repo discipline; standing per PMN-004 §5 (a))
- Disciplines applied (PMN-004 §5 (a)-(f) + PMN-005 sub-rule (e.1) + PMN-006 new disciplines (g), (h), (i) + PMN-003 (a) refined extended with frontmatter-vs-body sub-clause): severity taxonomy three-level (a); verification-command portability (b); no future-tense pre-commit claims (c); pre-commit cross-surface scope clarity (d); §23.6 prose-arithmetic decomposition (e) with sub-rule (e.1) cumulative-diff-stats re-derivation; section-citation correctness sweep (f); verification-artifact internal consistency (g) with sub-shapes (g.1)/(g.2); verification-command operational correctness (h) with sub-shapes (h.1)/(h.2)/(h.3); cross-document state verification (i) with sub-shapes (i.1)/(i.2)/(i.3)/(i.4); §23.6.2 iterative-to-fixed-point self-review.
- PMN-006 self-application: PR-11 is the first cycle to apply (g)/(h)/(i) at PR review-context authoring time; recursive-self-instantiation case (the claim block authoring discipline this PR canonicalizes is the discipline applied to this PR's claim blocks).

## Builder claims to verify

The Builder asserts the following at hand-off to Codex desktop pre-commit review. Each claim is verifiable from the working tree at pre-commit time (no future-tense claims per PMN-004 §5 (c)). PR-11 is a small-scope PMN-insertion cycle authoring PMN-006 + applying two surgical corrections to `core.md` Part A canonical text + four companion artifacts.

1. **`docs/post-merge-notes/PMN-006-pr-10-cycle-learnings.md` exists and follows §18 PMN canonical form.** Verifiable at pre-commit:
   - bash: `[ -f docs/post-merge-notes/PMN-006-pr-10-cycle-learnings.md ] && head -1 docs/post-merge-notes/PMN-006-pr-10-cycle-learnings.md`
   - cmd: `if exist docs\post-merge-notes\PMN-006-pr-10-cycle-learnings.md type docs\post-merge-notes\PMN-006-pr-10-cycle-learnings.md`
   - PowerShell: `Test-Path docs/post-merge-notes/PMN-006-pr-10-cycle-learnings.md` returns `True`; `Get-Content docs/post-merge-notes/PMN-006-pr-10-cycle-learnings.md -Head 1`
   - Expected first line: `# PMN-006 — PR-10 cycle learnings: verification-artifact-validity discipline split (g)/(h) + cross-document state verification (i) + bounded-continuation rule + four preliminary observations`

2. **PMN-006 §-header count is 9** (one §-header per observation cluster + cycle context section). Verifiable at pre-commit:
   - bash: `grep -cE "^## §[0-9]" docs/post-merge-notes/PMN-006-pr-10-cycle-learnings.md` returns `9`
   - PowerShell: `(Select-String -Path docs/post-merge-notes/PMN-006-pr-10-cycle-learnings.md -Pattern '^## §[0-9]').Count` returns `9`
   - cmd-side: PowerShell form supplied (per PMN-004 §5 (b) findstr codepage caveat for `§` byte sequence)
   - Decomposition: §1 cycle context; §2 (a) §23.6.2 convergence-count role-axis-dependence; §3 (b)→(g)+(h) split; §4 (c) pass-shape Reviewer-specificity; §5 (d) iterative-fix-up + bounded-continuation; §6 (e)/(f)/(g)/(h) refinement and convention items grouped; §7 (i) cross-document state verification; §8 refined disciplines summary; §9 anticipated forward integration + cross-references.

3. **PMN-006 §1.1 honesty record enumerates 10 defects with attribution** (defects 1-7 per spec §1.1; defect 8 per owner adjudication on Builder pre-flight pass 3 — three iteration-7/iteration-8 propagation residuals routed to path-(β) per bounded-continuation rule §5.3; defect 9 surfaced at step-8 execution time — spec deliverable 5 asserted a non-existent README "PMN file table"; same path-(β) routing per same-class (i) bounded-continuation; defect 10 surfaced by Codex cloud post-PR pass 2 on PR-11 commit `421fda1` — (h.3) canonical-form articulation defect: naive `>= AND id >` form drops valid emissions when ids do not strictly track timestamps; path-(a) revised to lexicographic OR form within this same cycle). Verifiable at pre-commit:
   - bash: `awk '/^### §1\.1/,/^### §1\.2/' docs/post-merge-notes/PMN-006-pr-10-cycle-learnings.md | grep -cE "^[0-9]+\. \*\*"` returns `10`
   - PowerShell: `(Get-Content docs/post-merge-notes/PMN-006-pr-10-cycle-learnings.md | Select-String -Pattern '^[0-9]+\. \*\*').Count` returns `10` for the §1.1 block (manually scope to §1.1 region)

4. **PMN-006 (g) and (h) discipline split structure with sub-shapes enumerated** in §3. Verifiable at pre-commit:
   - bash: `grep -nE "\(g\.[12]\)|\(h\.[123]\)" docs/post-merge-notes/PMN-006-pr-10-cycle-learnings.md | head -10` returns lines naming sub-shapes (g.1), (g.2), (h.1), (h.2), (h.3) — at least 5 distinct sub-shape labels present
   - PowerShell: `Select-String -Path docs/post-merge-notes/PMN-006-pr-10-cycle-learnings.md -Pattern '\(g\.[12]\)|\(h\.[123]\)' | Select-Object -First 10`
   - Expected: 5 distinct sub-shape labels — (g.1), (g.2), (h.1), (h.2), (h.3) — each defined in §3.1 / §3.2.

5. **PMN-006 (i) discipline canonicalization with four sub-shapes** in §7. Verifiable at pre-commit:
   - bash: `grep -nE "\(i\.[1234]\)" docs/post-merge-notes/PMN-006-pr-10-cycle-learnings.md` returns lines naming sub-shapes (i.1), (i.2), (i.3), (i.4) — 4 distinct sub-shape labels
   - PowerShell: `Select-String -Path docs/post-merge-notes/PMN-006-pr-10-cycle-learnings.md -Pattern '\(i\.[1234]\)'`
   - Expected: 4 distinct sub-shape labels — (i.1) tracked-file presence, (i.2) filesystem path assertions, (i.3) content-pattern assertions, (i.4) surrounding-context-preservation — each defined in §7.3.

6. **PMN-006 (b.3) reclassification to PMN-003 (a) refined extension recorded in §3.4 and §8.** Verifiable at pre-commit:
   - bash: `grep -n "(b\.3)" docs/post-merge-notes/PMN-006-pr-10-cycle-learnings.md` returns at least 2 lines (one in §3.4 reclassification statement; one in §8 refinement summary)
   - bash: `grep -n "frontmatter-vs-body" docs/post-merge-notes/PMN-006-pr-10-cycle-learnings.md` returns at least 2 lines
   - PowerShell: `Select-String -Path docs/post-merge-notes/PMN-006-pr-10-cycle-learnings.md -Pattern '\(b\.3\)|frontmatter-vs-body'`

7. **`core.md` §8.1.1.1 polling-commands corrected per (h.3) symmetric application — lexicographic tie-break form**: strict `>` removed for both `submitted_at` and `created_at` filters; lexicographic `(timestamp > last-known) OR (timestamp == last-known AND id > last-seen-id)` form present on both endpoints; naive `>= AND id >` form NOT present (per defect 10 — Codex post-PR pass 2 surfaced that the naive form drops valid emissions when ids do not strictly track timestamps); `select(.user.login==...)` author filter preserved on both endpoints. Verifiable at pre-commit:
   - bash:
     - `grep -c "submitted_at >= " core.md` returns `0` (naive form removed per defect 10)
     - `grep -c "created_at >= " core.md` returns `0` (naive form removed per defect 10)
     - `grep -c "submitted_at == " core.md` returns at least `1` (lexicographic same-timestamp tie clause for endpoint a)
     - `grep -c "created_at == " core.md` returns at least `1` (lexicographic same-timestamp tie clause for endpoint b)
     - `grep -cE "submitted_at > \"<last-known>\" or" core.md` returns at least `1` (endpoint a lexicographic OR clause)
     - `grep -cE "created_at > \"<last-known>\" or" core.md` returns at least `1` (endpoint b lexicographic OR clause)
     - `grep -c "select(.user.login" core.md` returns at least `2` (one per endpoint, preserved through substitution)
   - cmd: `findstr /n /c:"submitted_at >= " core.md` returns 0 lines; `findstr /n /c:"submitted_at == " core.md` returns at least 1 line; `findstr /n /c:"select(.user.login" core.md` returns at least 2 lines
   - PowerShell: `Select-String -Path core.md -Pattern 'submitted_at >= '` returns 0 matches; `Select-String -Path core.md -Pattern 'submitted_at == '` returns at least 1 match; `(Select-String -Path core.md -Pattern 'select\(\.user\.login').Count` returns at least 2

8. **`core.md` §24.3.1 point 2 corrected per (h.2)**: `git fetch && git status` removed; `git rev-parse HEAD` plus expected-SHA comparison present; `git status --porcelain` clean-tree adjunct check named. Verifiable at pre-commit:
   - bash:
     - `grep -c "git fetch && git status" core.md` returns `0` (defect 2 removed)
     - `grep -nE "git rev-parse HEAD.*expected" core.md` returns at least `1` line in §24.3.1 context
     - `grep -c "git status --porcelain" core.md` returns at least `1` (clean-tree adjunct present)
   - cmd: `findstr /c:"git fetch && git status" core.md` returns 0; `findstr /c:"git rev-parse HEAD" core.md` returns at least 1; `findstr /c:"git status --porcelain" core.md` returns at least 1
   - PowerShell: `Select-String -Path core.md -Pattern 'git fetch && git status'` returns 0; `Select-String -Path core.md -Pattern 'git rev-parse HEAD.*expected'` returns at least 1; `Select-String -Path core.md -Pattern 'git status --porcelain'` returns at least 1

9. **Section-citation correctness sweep clean per (f) iterative-to-convergence** across PMN-006, PR-11 review-context (this file), TASK-0011 handoff. Verifiable at pre-commit:
   - bash: `grep -nE "§[0-9]+(\.[0-9]+)*" docs/post-merge-notes/PMN-006-pr-10-cycle-learnings.md docs/reviews/PR-11-codex-pre-commit.md docs/handoffs/TASK-0011-pmn-006-pr-10-cycle-learnings.md` lists every line containing a §-citation; visually verify each citation's target document and section number resolves to an actual heading.
   - PowerShell: `Select-String -Path docs/post-merge-notes/PMN-006-pr-10-cycle-learnings.md,docs/reviews/PR-11-codex-pre-commit.md,docs/handoffs/TASK-0011-pmn-006-pr-10-cycle-learnings.md -Pattern '§[0-9]+(\.[0-9]+)*' | Format-Table LineNumber,Line`
   - Citation-range expectations: PMN-006-internal `§N` citations land in 1-9 range; PMN-005-internal in 1-7 range; PMN-004-internal in 1-8 range; PMN-001/PMN-002/PMN-003 use observation-letter citations (e.g. PMN-003 (a)) not §N. core.md §-citations land at actual headings (verify via `grep -nE "^#+ §" core.md`). Iterative application: this sweep is run multiple times until two consecutive zero-defect iterations are reached (fixed-point convergence per PMN-005 §4.3 / §23.6.2). Iteration count recorded in handoff §"Validation run" Evidence section.

10. **Frontmatter-vs-body reconciliation clean per (b.3) extended PMN-003 (a) refined.** PMN-006 has no YAML frontmatter (PMN bodies use markdown title + Status block per §18 canonical form), so frontmatter-vs-body reconciliation primarily applies to TASK-0011 handoff (which has frontmatter `task_id`, `linked_predecessor`, `linked_pr`, etc.). Verifiable at pre-commit:
    - PMN-006: title line + first ## §1 reference internal consistency — title says "PR-10 cycle learnings" (line 1); §1 prose says "PR-10 (TASK-0010) authored core.md Part A" (line 11). Verify: `head -15 docs/post-merge-notes/PMN-006-pr-10-cycle-learnings.md | grep -c "PR-10"` returns at least 2 (head depth 15 covers title at line 1 + §1 prose at line 11; head -3 was insufficient — would return 1 — and was the (g.1) timing-correctness defect surfaced by Codex pre-commit on this very claim).
    - TASK-0011 handoff frontmatter: `task_id: TASK-0011` present; body `# TASK-0011 — ...` opening line present; `linked_pr: (filled at step-18 fix-up per PMN-001 (k))` pending-form acceptable pre-merge.
    - PR-11 review-context (this file): metadata block PR ID = PR-11 + TASK ID = TASK-0011 + branch = feat/task-0011-pmn-006; body claim 1 references PMN-006; body claim 11 references TASK-0011 handoff Evidence section. Verify: `head -10 docs/reviews/PR-11-codex-pre-commit.md | grep -c "PR-11"` returns at least 2.

11. **Cumulative diff stats re-derivation per (e.1)** — exact counts in TASK-0011 handoff Evidence section. Per PMN-005 §4.4 sub-rule (e.1): no `~`-prefixed numbers; Evidence section populated immediately before commit at step-10. Verifiable at pre-commit (post-step-10 fill):
    - bash: `git diff --stat $(git merge-base HEAD origin/main)..HEAD` (post-staging-and-commit; or `git diff --stat --cached` at staged-pre-commit state)
    - cmd / PowerShell: same command
    - Expected shape: 4 changed files (PMN-006 new, PR-11 review-context new, TASK-0011 handoff new, core.md modified) with exact insertion/deletion counts; counts populated in handoff §"Validation run" Evidence section as exact landed values, no `~` prefixes. README.md is NOT modified in this cycle (path-(β) record-and-proceed per PMN-006 §1.1 defect 9 — spec deliverable 5 asserted a non-existent "PMN file table"; bounded-continuation rule §5.3 routes same-class (i) findings to PMN evidence rather than path-(a) micro-fix).

12. **Severity-taxonomy three-level enumeration**: this review-context file enumerates Blocking / Major / Minor with explicit definitions in `## Reviewer-direction shape` per PMN-004 §5 (a). No two-level framing in any committed artifact in this PR. Verifiable at pre-commit:
    - bash: `grep -c "Blocking / Major / Minor" docs/reviews/PR-11-codex-pre-commit.md` returns `2` or more
    - cmd: `findstr /c:"Blocking / Major / Minor" docs\reviews\PR-11-codex-pre-commit.md`
    - PowerShell: `(Select-String -Path docs/reviews/PR-11-codex-pre-commit.md -Pattern 'Blocking / Major / Minor').Count` returns `2` or more

13. **(g)/(h)/(i) self-application — every claim's verification command in this review-context passes Builder self-check at step-10**: each verification command's declared timing matches its runnable timing (g.1); the example output (where named) matches the claim's label (g.2); pagination supplied where reachable (h.1); the named command's output domain covers the claim's verification need (h.2); strict-comparator filters use `>=`-plus-tie-breaker form (h.3, n/a for grep-based claims; applies to gh api polling commands which are out-of-scope for this review-context); cross-document state assertions verified against actual repo state (i.1-i.4). Verifiable at pre-commit:
    - Builder attestation: each of claims 1-12 above has had its verification command run against the pre-commit working tree and produced the asserted result. Iteration count to (g)/(h)/(i) self-application convergence recorded in handoff §"Validation run" Evidence section.

## Reviewer focus (Codex desktop)

For each Builder claim above, verify the verification command produces the asserted result. Specific focus areas (only pre-commit-existing surfaces enumerated per PMN-004 §5 (d)):

- **(g) Verification-artifact internal consistency** (NEW this PMN, applied here): for each claim block, verify the command's declared timing matches what the command actually proves at that timing (g.1); verify the example output (where shown) matches the label (g.2). Mismatched timing or example/label divergence is a Blocking finding.

- **(h) Verification-command operational correctness** (NEW this PMN, applied here): for each claim block, verify `--paginate` is present where reachable (h.1); verify the named command's output domain covers the claim's verification need (h.2); verify strict-comparator timestamp filters are `>=`-plus-tie-breaker form (h.3). The (h.2) and (h.3) sub-shapes are the primary motivators for this PR's `core.md` corrections (claims 7 and 8 above).

- **(i) Cross-document state verification** (NEW this PMN, applied here): for each Builder claim asserting a fact about another file's content, path, or structure, verify the assertion against actual file state via the supplied `grep` / `findstr` / `Select-String` form. The (i) discipline is what surfaced 9 defects on the TASK-0011 spec across three Builder pre-flight passes plus one step-8-execution-time surfacing; defect 8 (three iteration-7/iteration-8 propagation residuals) and defect 9 (non-existent README "PMN file table") are documented in PMN-006 §1.1 as path-(β) record-and-proceed evidence.

- **Pre-commit cross-surface count claim consistency** (per PMN-004 §5 (e) + sub-rule (e.1)): the number `9` (PMN-006 §-header count) appears in (a) `docs/post-merge-notes/PMN-006-pr-10-cycle-learnings.md` §3 (cluster enumeration); (b) this file's claim 2; (c) TASK-0011 handoff §"Validation run" Evidence section. All pre-commit-existing surfaces must agree on `9`. The number `9` (PMN-006 §1.1 honesty record defect count) appears in (a) PMN-006 §1.1 prose ("Nine defects originated"); (b) this file's claim 3 expected value `9`; (c) TASK-0011 handoff §"Validation run" Evidence section. All pre-commit-existing surfaces must agree on `9`. The number `4` (files changed) appears in (a) TASK-0011 handoff §Current state ("Files changed: 4"); (b) this file's claim 11 expected shape ("4 changed files"). All must agree on `4`.

- **Cumulative-diff-stats re-derivation** (sub-rule (e.1)): per-file insertion/deletion counts in TASK-0011 handoff §"Validation run" Evidence section must match `git diff --stat <merge-base>..HEAD` exactly. No approximate counts; no `~`-prefixed numbers. If the Evidence section is empty pending step-10 fill, that is acceptable per PMN-004 §5 (c). If the Evidence section contains any number, that number must be exact.

- **Section-citation correctness in PMN-006**: every `§N` cross-reference in PMN-006 resolves. Codex sweeps PMN-006 for `§[0-9]+(\.[0-9]+)*` patterns; each must land at an actual heading in the cited document. PMN-006-internal citations land in 1-9 range. core.md citations land at actual `^#+ §` headings in core.md HEAD. PMN-005-internal citations land in 1-7 range; PMN-004-internal in 1-8 range; PMN-001/PMN-002/PMN-003 observation-letter citations land in their respective letter ranges. Report all dangling references as Blocking findings. Iterative-to-convergence per PMN-005 §4.3.

- **Severity-taxonomy compliance** (PMN-004 §5 (a)): this file enumerates three levels (Blocking / Major / Minor) per repo discipline. Two-level framing in any artifact is a Blocking finding.

- **Scope-leakage check on `core.md` corrections**: only the §8.1.1.1 polling-block timestamp filters (both endpoints) and §24.3.1 point 2 are modified per spec §4. Any modification outside these two locations is a Blocking finding. The corrections are surgical (small, isolated, do not require restructuring surrounding prose) per spec §4 surgical-or-defer guard.

- **Phantom-action claim verification** (per §8.1.1.2 / PMN-005 §2.5): each Builder claim's verification command is itself directly verifiable. Codex runs the command; reports result verbatim; flags any divergence from the Builder's asserted result. Additionally per PMN-005 §2.5, any Codex-emitted comment claiming a commit SHA, file addition, or file modification is verifiable against repository state via `gh api repos/.../commits/<sha>` and `gh api repos/.../contents/<path>`; unreachable claims are informational-only.

- **README.md modification scope**: README.md is NOT modified in this cycle per PMN-006 §1.1 defect 9 (spec deliverable 5 asserted a non-existent "PMN file table"; path-(β) record-and-proceed per bounded-continuation rule §5.3). The Package layout table is explicitly out of scope per spec §2 deliverable 5 + ADR-003 §Consequences (substantive PRs update their own package-layout row at content-fill time; PMN-006 is not a substantive content PR; the visible drift on the `usage-guide.md` row is forecast-vs-actual by ADR-003 design and stays until usage-guide actually ships). Codex diffs README.md against `main` to confirm zero modifications. Any modification to README.md is a Blocking finding (spec defect 9 routes to path-(β); README stays unchanged this cycle).

- **No future-tense claims at pre-commit time** (PMN-004 §5 (c)): Sweep all 13 Builder claims for "will be" / "shall" / "to be filled" language. Any future-tense claim that does not have a pre-commit-verifiable counterpart is a Blocking finding. Note: phrases of the form "filled at step-10" referring to the Validation run Evidence section are acceptable per discipline (c) because step-10 self-verification populates this subsection before commit.

## Reviewer-direction shape (claim-verification-only, imperative `Action:` per PMN-002 (a))

Codex's output structure:

For each claim 1 through 13 above, output one of:
- `Claim N: Verified clean.`
- `Claim N: <Severity> finding — <description>; verification command output: <verbatim>; recommended action: <path (a) revise / path (b) record-and-proceed>.`

After per-claim verdict, output an overall summary:
- Total claims: 13
- Verified clean: <count>
- Blocking findings: <count>
- Major findings: <count>
- Minor findings: <count>
- Recommended disposition: clean / revise (path (a)) / record-and-proceed (path (b))

Severity definitions for this review:

- **Blocking** — finding that prevents merge until addressed (e.g., spec-prescribed canonical correction missing from `core.md`; section-citation slip producing dangling reference; severity-taxonomy non-compliance; cumulative-diff-stats drift on pre-commit-existing surface; future-tense pre-commit claim without verifiable counterpart; (g)/(h) defect within this review-context's own claim blocks; (i) cross-document state assertion mismatched against actual repo state). Cannot ship without revision.
- **Major** — finding that should be addressed pre-merge but does not block merge in the absence of address (e.g., minor prose-arithmetic drift caught post-step-10; clarifying language improvement; cross-reference forward-pointing where backward-pointing would be clearer). Default disposition path (a) revise.
- **Minor** — finding noted for record but not requiring address (e.g., stylistic preference; future-section forward-reference noted as such; cosmetic issue not propagated to downstream artifact). Default disposition path (b) record-and-proceed.

Action phrasing examples in the Reviewer-direction shape:

```
Action: For each enumerated claim above, verify the verification command produces the asserted result. Report any divergence as a Blocking finding regardless of magnitude. Report verification commands' outputs verbatim.

Action: Sweep PMN-006, this review-context, and TASK-0011 handoff for §-citations matching the pattern §[0-9]+(\.[0-9]+)*. For each citation, verify the cited §-number resolves to an actual heading in the cited document. Report all dangling references as Blocking findings.

Action: Verify the README.md diff against main is empty (zero modifications): `git diff --name-only 80f5a4a..HEAD -- README.md` produces no output. Any modification to README.md is a Blocking finding per PMN-006 §1.1 defect 9 path-(β) record-and-proceed (spec deliverable 5 asserted a non-existent "PMN file table"; bounded-continuation rule §5.3 routes to path-(β) rather than path-(a) micro-fix; README stays unchanged this cycle).

Action: Run the cumulative-diff-stats re-derivation per (e.1). Compare the Evidence section in TASK-0011 handoff against `git diff --stat` output. Any discrepancy is a Blocking finding. Any `~`-prefixed number in the Evidence section is a Blocking finding.

Action: Verify scope-leakage on `core.md` corrections. Only §8.1.1.1 polling-block timestamp filters (both endpoints, preserving author filter) and §24.3.1 point 2 are modified. Any modification outside these locations is a Blocking finding.

Action: Apply (g)/(h)/(i) sweep to this review-context's own claim blocks. Each claim's verification command must (g.1) declare timing matching what it proves; (g.2) match label-vs-example; (h.1) include `--paginate` where reachable; (h.2) prove what's claimed; (h.3) use `>=`-plus-tie-breaker for any timestamp filter (n/a for this review-context's grep-only commands). Cross-document assertions verified against actual repo state per (i.1)-(i.4). Any sub-shape failure is a Blocking finding.
```

## Builder hand-back attestation

After Codex desktop pre-commit review completes, Builder reports:
- Codex review outcome (per the summary structure above)
- Path (a) revisions made, if any
- Path (b) acceptances recorded, if any
- §23.6 recapitulation-consistency re-check result after any path (a) revisions (per PMN-003 (a) refined; extended scope per PMN-004 §2.3 to include verification-command surfaces; further extended per PMN-005 §4.4 sub-rule (e.1) to include cumulative-diff-stats re-derivation; further extended per PMN-006 §3.4 to include frontmatter-vs-body sub-clause)
- Section-citation correctness sweep result after any path (a) revisions, applied iteratively to convergence per PMN-005 §4.3 / §23.6.2
- Cumulative-diff-stats Evidence subsection populated with landed exact counts from `git diff --stat <merge-base>..HEAD` immediately before commit, per PMN-005 §4.4 sub-rule (e.1)
- (g)/(h)/(i) self-application sweep result on this review-context's own claim blocks; iteration count to convergence

## Notes

- Codex desktop reviews the untracked working tree before commit (read-only git inspection only; no `.git/index.lock` writes).
- Post-PR `@codex review` is owner-invoked per ADR-001 decision 11; this pre-commit review is separate and is the substantive verification before commit.
- PR-11 is the first cycle to apply the (g)/(h)/(i) discipline split that PMN-006 canonicalizes. Recursive-self-instantiation: the disciplines being canonicalized are the disciplines applied to this PR's claim blocks.
- PMN-006 §1.1 defect 8 records three iteration-7/iteration-8 spec propagation residuals routed to path-(b) record-and-proceed per bounded-continuation rule §5.3 (§5 step 2 stale ADR reference in spec preamble; §6 sweep-set intro missing (i); §12.1 sweep-set self-application list missing (i)). These residuals exist in the gitignored `.claude/session-handoffs/TASK-0011-spec.md` and are out of scope for this review (the spec is gitignored per ADR-001 decision 15). They are documented in PMN-006 §1.1 defect 8 for empirical record.
- PMN-006 cycle: third Builder pre-flight pass surfaced 3 same-class residuals; bounded-continuation rule §5.3 applied at adjudication time to route to path-(b) rather than iteration-9 spec micro-fix. The decision NOT to iterate on the spec is itself empirical material for §7 iterative-pre-flight pattern preliminary refinement.
- TASK-0011 reservation per ADR-003 Decision 3 PMN-insertion discipline: PMN PRs consume the next available TASK slot at authoring time; the TASK-0011 handoff file IS the reservation; no separate registry. PMN-006 consumes the third contingency slot in the ADR-003 Decision 3 contingency budget (TASK-0020 through TASK-0026, seven slots): PMN-004 ate the first, PMN-005 ate the second, PMN-006 eats the third by virtue of shifting downstream substantive content forward by one TASK number. Four contingency slots remaining: TASK-0023 through TASK-0026.
