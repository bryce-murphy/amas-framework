# PR-15 Codex desktop pre-commit review context

## Metadata

- PR ID: PR-15
- TASK ID: TASK-0015
- Branch: feat/task-0015-pmn-007
- Base SHA: e6a592be8769a25987fb03e33559026924075727 (squash-merge of PR-14 chore on main, 2026-05-03)
- Builder: Claude Code (Claude Opus 4.7)
- Reviewer: Codex (GPT-5.5) — desktop, pre-commit, untracked working tree
- Architect (this PR's): Claude Opus 4.7 (Claude.ai Project)
- Owner: Bryce Murphy (`@bryce-murphy`)
- Framework version: AMAS v2.16 (dogfooded per CLAUDE.md active framework version; PMN-007 cycle does not bump framework_version per spec §2 out-of-scope; v2.16 bump landed at PR-13)
- Severity taxonomy: Blocking / Major / Minor (three-level; per repo discipline; standing per PMN-004 §5 (a))
- Disciplines applied (PMN-004 §5 (a)-(f) + PMN-005 sub-rule (e.1) + PMN-006 (g)/(h)/(i) + PMN-006 §5.3 bounded-continuation rule generalized + PMN-006 §3.4 frontmatter-vs-body sub-clause + PMN-007 §2.4 cost-class refinement with genuinely-asymptotic-vs-pure-token-swap distinction (canonicalized this cycle) + PMN-007 §3.1 four-surface iterative-pre-flight + iterative-post-PR-review pattern + PMN-007 §9.1 (i) extended pre-authoring verification batch): severity taxonomy three-level (a); verification-command portability (b); no future-tense pre-commit claims (c); pre-commit cross-surface scope clarity (d); §23.6 prose-arithmetic decomposition (e) with sub-rule (e.1) cumulative-diff-stats re-derivation; section-citation correctness sweep (f); verification-artifact internal consistency (g) with sub-shapes (g.1)/(g.2); verification-command operational correctness (h) with sub-shapes (h.1)/(h.2)/(h.3); cross-document state verification (i) with sub-shapes (i.1)/(i.2)/(i.3)/(i.4); §23.6.2 iterative-to-fixed-point self-review; §8.1.1.3 bounded-continuation rule with cost-class refinement (genuinely-asymptotic-vs-pure-token-swap distinction canonicalized this cycle).
- Recursive-self-instantiation: PR-15 canonicalizes (in core.md) the cost-class refinement extension at §8.1.1.3 distinguishing genuinely-asymptotic from pure-token-swap cascades — the rule is then applied at its own canonicalization moment within this same cycle. Builder pre-flight surfaced 2 spec-baseline-drift defects (Mismatch 1 docs/post-merge-notes/ count; Mismatch 2 docs/reviews/ count), both pure-token-swap class, both routed path-(a) per the very refinement this cycle canonicalizes; (k.1) positive self-instantiation. Architect iter-4 "correction" introducing Mismatch 1 is (k.2) failure-mode self-instantiation absorbed into spec §10 defect log.

## Builder claims to verify

The Builder asserts the following at hand-off to Codex desktop pre-commit review. Each claim is verifiable from the working tree at pre-commit time (no future-tense claims per PMN-004 §5 (c)). PR-15 is a substantive PMN-cycle authoring PMN-007 (PR-13 cycle learnings) + companion artifacts plus a surgical addition to core.md §8.1.1.3 cost-class refinement clause.

1. **Tracked-file count on feature branch post-Builder-commit** = 96 (93 base + 3 new files: PMN-007 + TASK-0015 handoff + PR-15 review-context; core.md modification does not change count). Pre-commit-verifiable per (c) discipline; post-merge value tracked under post-PR claims below.
   - bash: `git ls-files | wc -l` returns `96` on feature branch post-staging
   - PowerShell: `(git ls-files | Measure-Object -Line).Lines` returns `96`

2. **PMN-007 §-header count** = 11 top-level §-sections (§1-§11). Verifiable at pre-commit:
   - bash: `grep -cE "^## §[0-9]+\." docs/post-merge-notes/PMN-007-pr-13-cycle-learnings.md` returns `11`
   - PowerShell: `(Select-String -Path docs/post-merge-notes/PMN-007-pr-13-cycle-learnings.md -Pattern '^## §[0-9]+\.').Count` returns `11`

3. **PMN-007 §1.1 honesty record enumerates ≥9 distinct defect items** (architect-side iter-2 batch + iter-3 batch + Builder pre-flight P1/P2/P3 + Codex pre-commit Claim 1/Claim 14 + Codex post-PR pass 1 P2 + Codex post-PR pass 2 cycle-trailing-clean = 9 enumerated items aggregating 23 defects). Verifiable at pre-commit:
   - bash: `awk '/^### §1\.1/,/^### §1\.2/' docs/post-merge-notes/PMN-007-pr-13-cycle-learnings.md | grep -cE "^[0-9]+\. \*\*"` returns ≥`9`
   - PowerShell: equivalent regex via `Select-String`

4. **PMN-007 §-numbering matches PMN-007 §1.4 framing** = 11 §-headers (§1 cycle context; §2-§9 substantive umbrellas; §10 refined disciplines summary; §11 anticipated forward integration + cross-references). Verifiable at pre-commit:
   - bash: `grep -cE "^## §[0-9]+\." docs/post-merge-notes/PMN-007-pr-13-cycle-learnings.md` returns `11` (claim 2 above) AND `grep -cE "^## §(1|2|3|4|5|6|7|8|9|10|11)\." docs/post-merge-notes/PMN-007-pr-13-cycle-learnings.md` returns `11` (specific §-numbers all present)
   - PowerShell: equivalent

5. **core.md §-header count unchanged post-modification** = 21 §-headers. Verifiable at pre-commit:
   - bash: `grep -nE "^#{1,6} §[0-9]" core.md | wc -l` returns `21`
   - PowerShell: `(Select-String -Path core.md -Pattern '^#{1,6} §[0-9]').Count` returns `21`

6. **core.md §8.1.1.3 contains "Cost-class sub-distinction" exactly once**. Verifiable at pre-commit:
   - bash: `grep -c "Cost-class sub-distinction" core.md` returns `1`
   - PowerShell: `(Select-String -Path core.md -Pattern 'Cost-class sub-distinction' -AllMatches).Matches.Count` returns `1`

7. **core.md §8.1.1.3 contains "genuinely-asymptotic" ≥3 times** (per byte-exact text in spec §3.4: bold-marker title + (i) clause + "(genuinely-asymptotic class)" clause). Verifiable at pre-commit:
   - bash: `grep -o "genuinely-asymptotic" core.md | wc -l` returns ≥`3`
   - PowerShell: `(Select-String -Path core.md -Pattern 'genuinely-asymptotic' -AllMatches).Matches.Count` returns ≥`3`
   - Note: `grep -c` counts MATCHING LINES not occurrences; since the byte-exact text is one paragraph (one source line in the spec block), `grep -c` returns `1`. Use `grep -o ... | wc -l` for occurrence count per (h.2) verification-command operational correctness sub-shape.

8. **core.md §8.1.1.3 contains "pure-token-swap" ≥3 times case-insensitive** (per byte-exact text in spec §3.4: bold-marker title + (ii) clause + "Pure-token-swap cascades" sentence — the third instance is capitalized `Pure-token-swap` so case-insensitive matching is required per (h.2) verification-command operational correctness sub-shape). Verifiable at pre-commit:
   - bash: `grep -oi "pure-token-swap" core.md | wc -l` returns ≥`3` (case-insensitive `-i` flag)
   - PowerShell: `(Select-String -Path core.md -Pattern 'pure-token-swap' -AllMatches).Matches.Count` returns ≥`3` (PowerShell `Select-String` is case-insensitive by default)
   - Note: `grep -o "pure-token-swap"` (without `-i` flag) is case-sensitive and returns `2` (matching only the lowercase instances); the case-insensitive form is canonical.

9. **README.md unchanged this cycle** (per spec §2 deliverables out-of-scope). Verifiable at pre-commit (working-tree state compared to main, covering both staged and unstaged changes — ref-to-ref comparison `main..feat/task-0015-pmn-007` is operationally insufficient at pre-commit time because the feature branch has no commits yet, so the ref comparison always returns empty regardless of staged content; the canonical pre-commit verification compares the working tree against main per (h.2) verification-command operational correctness sub-shape):
   - bash: `git diff main -- README.md` returns empty (compares working tree including staged + unstaged against main)
   - bash adjunct: `git diff --staged -- README.md` returns empty (compares staged tree against HEAD; redundant cross-check)
   - PowerShell: `git diff main -- README.md` returns empty (shell-agnostic)

10. **TASK-0015 handoff frontmatter task_id is TASK-0015**. Verifiable at pre-commit:
    - bash: `grep -c "^task_id: TASK-0015$" docs/handoffs/TASK-0015-pmn-007-pr-13-cycle-learnings.md` returns `1`
    - PowerShell: `(Select-String -Path docs/handoffs/TASK-0015-pmn-007-pr-13-cycle-learnings.md -Pattern '^task_id: TASK-0015$').Count` returns `1`

11. **TASK-0015 handoff frontmatter framework_version_dogfooded is AMAS v2.16**. Verifiable at pre-commit:
    - bash: `grep -c "^framework_version_dogfooded: AMAS v2\.16$" docs/handoffs/TASK-0015-pmn-007-pr-13-cycle-learnings.md` returns `1`
    - PowerShell: equivalent regex

12. **PMN-007 frontmatter status is "drafted"** at file creation. Verifiable at pre-commit:
    - bash: `grep -c "^status: drafted$" docs/post-merge-notes/PMN-007-pr-13-cycle-learnings.md` returns `1`
    - PowerShell: equivalent
    - Status flips to `recorded` post-merge per PMN-001 (k) Linked PR fix-up substitution + status flip convention (small-chore-PR mechanism per spec §4 mechanism-vs-discipline distinction).

13. **PMN-007 cross-references PMN-001 through PMN-006 + ADR-001 + ADR-002 + ADR-003**. Verifiable at pre-commit:
    - bash: `grep -cE "^- \*\*(PMN-00[1-6]|ADR-00[1-3])" docs/post-merge-notes/PMN-007-pr-13-cycle-learnings.md` returns ≥`9` (six PMNs + three ADRs)
    - PowerShell: equivalent

14. **PMN-007 cross-references PR-13 + PR-14 + PR-15 squash SHAs or placeholders**. Verifiable at pre-commit:
    - bash: `grep -cE "(PR-1[3-5]|squash-merge \`[0-9a-f]{7,}\`)" docs/post-merge-notes/PMN-007-pr-13-cycle-learnings.md` returns ≥`3`
    - PowerShell: equivalent

15. **Cumulative-diff-stats consistency per (e.1) sub-rule**: Σ per-file insertions = total insertions in `git diff --stat`. Verifiable at pre-commit (post-staging, pre-commit):
    - bash: `git diff --staged --stat` shows insertions / deletions across staged files; total insertions field = sum of per-file insertions field
    - cmd: `git diff --staged --stat` (shell-agnostic)
    - PowerShell: `git diff --staged --stat` (shell-agnostic)
    - Expected: 4 files changed (PMN-007 new; TASK-0015 handoff new; PR-15 review-context new; core.md modified). PMN-007 + handoff + review-context per their own line counts; core.md addition is one paragraph (the byte-exact sub-distinction clause). Evidence section populated at step-10 self-verification per (e.1) sub-rule.
    - (e.1) cumulative-diff-stats re-derivation per PMN-005 §4.4: if any path-(a) revision occurs during step-10 self-verification or Codex pre-commit, re-derive cumulative diff stats and re-verify all dependent claims.

## Reviewer focus (Codex desktop)

For each Builder claim above, verify the verification command produces the asserted result. Specific focus areas (only pre-commit-existing surfaces enumerated per PMN-004 §5 (d)):

- **PMN-007 canonical text byte-exact compliance against spec §4** (claims 2-4): PMN-007 body matches spec §4 fenced markdown block byte-exact (frontmatter from spec §3.1; body from spec §4 lines between the `markdown` fences). Any byte-divergence (whitespace, punctuation, word substitution, paragraph reordering) is a Blocking finding regardless of substantive equivalence.

- **core.md §8.1.1.3 byte-exact addition against spec §3.4** (claims 5-8): the addition matches spec §3.4 fenced text byte-exact. Verify by comparing the modified §8.1.1.3 cost-class refinement region against spec §3.4's fenced block. Any whitespace, punctuation, or paragraph-reordering divergence is a Blocking finding.

- **§-numbering insertion ordering** (claim 5): core.md §-header sequence preserved at 21; the surgical addition does not introduce a new §-header. Any new §-header (e.g., §8.1.1.4) is a Blocking scope-leakage finding.

- **(g) Verification-artifact internal consistency** (canonicalized in PMN-006 §3.1): for each Builder claim, verify (g.1) timing-correctness across surfaces and (g.2) within-block label-vs-example consistency. Recursive-self-instantiation surface — bounded-continuation rule §8.1.1.3 cost-class refinement extension this cycle includes byte-exact text that itself follows the discipline. Any sub-shape failure is a Blocking finding.

- **(h) Verification-command operational correctness** (canonicalized in PMN-006 §3.2): PMN-007 + spec §3.4 addition do not author new verification commands; (h.1) pagination, (h.2) command-achieves-claim, (h.3) filter-boundary trivially satisfied at the canonical-text surface. (h) discipline applies to this review-context's own verification commands (claims 1-15 above) — verify each grep / awk / PowerShell command's output domain covers the claim's verification need. Specifically: claim 7 + claim 8 use `grep -o ... | wc -l` for occurrence count not `grep -c`; (h.2) sub-shape applied correctly per the explicit Note in claim 7.

- **(i) Cross-document state verification** (canonicalized in PMN-006 §7): for each Builder claim asserting a fact about another file's content, path, or structure, verify the assertion against actual file state via the supplied `grep` / `findstr` / `Select-String` form. The (i) discipline already surfaced 2 defects on the TASK-0015 spec at the Builder pre-flight surface (Mismatch 1 docs/post-merge-notes/ count = 7 not 6; Mismatch 2 docs/reviews/ count = 11 not ≥12) — both path-(a) per §8.1.1.3 cost-class refinement (pure-token-swap class); spec corrected at Architect path-(a) revision before Builder resumed step 2.

- **Pre-commit cross-surface count claim consistency** (per PMN-004 §5 (e) + sub-rule (e.1)): the number `21` (core.md cumulative §-header count) appears in (a) handoff Assumptions; (b) this file's claim 5; (c) spec §5.6 verification expectation. All pre-commit-existing surfaces must agree on `21`. The number `11` (PMN-007 §-header count) appears in (a) handoff Decisions made (Phase 1 decision 1); (b) this file's claim 2 + claim 4; (c) spec §5.3 verification expectation; (d) PMN-007 §1.4 framing. All must agree on `11`. The number `96` (tracked-file count post-staging) appears in (a) handoff Current state; (b) this file's claim 1; (c) spec §6.1 claim 1. All must agree on `96`.

- **Cumulative-diff-stats re-derivation** (sub-rule (e.1)): per-file insertion/deletion counts in handoff Validation run (if filled at hand-back) must match `git diff --staged --stat` exactly. No approximate counts; no `~`-prefixed numbers. If the section is empty pending step-10 fill, that is acceptable per PMN-004 §5 (c). If the section contains any number, that number must be exact.

- **Section-citation correctness across modified core.md + new PMN-007 + new TASK-0015 handoff + new PR-15 review-context** (claim 13 + sweep): every `§N` citation resolves to existing canonical text or explicitly-named forward-reference; no defect citations. Codex sweeps all four documents for `§[0-9]+(\.[0-9]+)*` patterns; each must land at an actual heading in the cited document. Forward-reference set explicitly excluded (§13.1, §13.2, §14.1, §2.3.4, §7.1, §17.6 — out-of-tree per spec convention). Report all dangling references (other than the enumerated forward-reference set) as Blocking findings. Iterative-to-convergence per PMN-005 §4.3.

- **Severity-taxonomy compliance** (PMN-004 §5 (a)): this file enumerates three levels (Blocking / Major / Minor) per repo discipline. Two-level framing in any artifact is a Blocking finding.

- **Scope-leakage check on `core.md` modifications**: only insertion of one paragraph (the byte-exact sub-distinction clause per spec §3.4) within §8.1.1.3 cost-class refinement region (lines 115-146) is in scope. Any modification outside §8.1.1.3 cost-class refinement region (existing §8 / §17 / §18 / §23 / §24 leaves) is a Blocking finding (spec §3.4 + §7 surgical-or-defer guard for PMN-cycle scope).

- **Phantom-action claim verification** (per §8.1.1.2 / PMN-005 §2.5 / PMN-007 §9.2 (m) Reviewer-side citation correctness sub-shape B): each Builder claim's verification command is itself directly verifiable. Codex runs the command; reports result verbatim; flags any divergence from the Builder's asserted result. Any Codex-emitted comment claiming a commit SHA, file addition, or file modification is verifiable against repository state via `gh api repos/.../commits/<sha>` and `gh api repos/.../contents/<path>`; unreachable claims are informational-only. Sub-shape B (correct-content-fabricated-citation) applies symmetrically across Reviewer-side and Builder-side claimed-action surfaces per PMN-007 §9.2.

- **No future-tense claims at pre-commit time** (PMN-004 §5 (c)): Sweep all 15 Builder claims for "will be" / "shall" / "to be filled" language. Any future-tense claim that does not have a pre-commit-verifiable counterpart is a Blocking finding. Note: phrases of the form "filled at step-10" or "filled at hand-back" referring to handoff Last-completed-step / Current-state subsections are acceptable per discipline (c) because step-10 self-verification populates these subsections before commit and step-15 hand-back populates the final state.

- **§8.1.1.3 cost-class refinement self-application** (per PMN-007 §2.3 (l) failure-mode self-instantiation guard): verify any path-(β) routing decision Codex applies in this review-context against the genuinely-asymptotic-vs-pure-token-swap distinction canonicalized in core.md §8.1.1.3 (the very text this cycle adds). Pure-token-swap cascades route path-(a); only genuinely-asymptotic cascades warrant path-(β). The cycle that canonicalizes the rule must apply the rule correctly to its own routing decisions.

## Reviewer-direction shape (claim-verification-only, imperative `Action:` per PMN-002 (a))

Codex's output structure:

For each claim 1 through 15 above, output one of:
- `Claim N: Verified clean.`
- `Claim N: <Severity> finding — <description>; verification command output: <verbatim>; recommended action: <path (a) revise / path (β) record-and-proceed>.`

After per-claim verdict, output an overall summary:
- Total claims: 15
- Verified clean: <count>
- Blocking findings: <count>
- Major findings: <count>
- Minor findings: <count>
- Recommended disposition: clean / revise (path (a)) / record-and-proceed (path (β))

Severity definitions for this review:

- **Blocking** — finding that prevents merge until addressed (e.g., spec-prescribed canonical text byte-divergence in PMN-007 or core.md §8.1.1.3 addition; section-citation slip producing dangling reference; severity-taxonomy non-compliance; cumulative-diff-stats drift on pre-commit-existing surface; future-tense pre-commit claim without verifiable counterpart; (g)/(h) defect within this review-context's own claim blocks; (i) cross-document state assertion mismatched against actual repo state; scope-leakage outside §8.1.1.3 cost-class refinement region in core.md; modification to README.md). Cannot ship without revision.
- **Major** — finding that should be addressed pre-merge but does not block merge in the absence of address (e.g., minor prose-arithmetic drift caught post-step-10; clarifying language improvement; clustering-pressure-vs-full-enumeration scope question warranting Architect adjudication). Default disposition path (a) revise.
- **Minor** — finding noted for record but not requiring address (e.g., stylistic preference; future-section forward-reference noted as such; cosmetic issue not propagated to downstream artifact). Default disposition path (β) record-and-proceed.

Action phrasing examples in the Reviewer-direction shape:

```
Action: For each enumerated claim above, verify the verification command produces the asserted result. Report any divergence as a Blocking finding regardless of magnitude. Report verification commands' outputs verbatim.

Action: For PMN-007 canonical text claims 2-4, compare PMN-007 body content against spec §4 fenced markdown block byte-exact. Report any whitespace, punctuation, word substitution, or paragraph reordering as a Blocking finding regardless of substantive equivalence.

Action: For core.md §8.1.1.3 addition claims 5-8, compare the modified §8.1.1.3 cost-class refinement region against spec §3.4 fenced text byte-exact. Report any divergence as a Blocking finding.

Action: Sweep core.md, this review-context, TASK-0015 handoff, and PMN-007 for §-citations matching the pattern §[0-9]+(\.[0-9]+)*. For each citation, verify the cited §-number resolves to an actual heading in the cited document. Forward-reference set excluded: §13.1, §13.2, §14.1, §2.3.4, §7.1, §17.6 (out-of-tree per spec convention). Report all dangling references as Blocking findings.

Action: Verify the README.md diff against main is empty. Any modification to README.md is a Blocking finding (per claim 9 + spec §2 out-of-scope).

Action: Run the cumulative-diff-stats re-derivation per (e.1). Compare any Evidence section in TASK-0015 handoff against `git diff --staged --stat` output. Any discrepancy is a Blocking finding. Any `~`-prefixed number in the Evidence section is a Blocking finding.

Action: Verify scope-leakage on core.md modifications. Only one-paragraph insertion within §8.1.1.3 cost-class refinement region (lines 115-146) is in scope. Any modification outside this region is a Blocking finding.

Action: Apply (g)/(h)/(i) sweep to this review-context's own claim blocks. Each claim's verification command must (g.1) declare timing matching what it proves; (g.2) match label-vs-example; (h.1) include `--paginate` where reachable (n/a for grep-only commands); (h.2) prove what's claimed (specifically: claim 7 + claim 8 use `grep -o ... | wc -l` not `grep -c` per the explicit Note in claim 7); (h.3) use lexicographic OR form for any timestamp filter (n/a for this review-context's grep-only commands). Cross-document assertions verified against actual repo state per (i.1)-(i.4). Any sub-shape failure is a Blocking finding.

Action: Apply §8.1.1.3 cost-class refinement (canonicalized this cycle) to any path-(β) routing decision Codex applies in this review-context. Pure-token-swap cascades (single-iteration fixed-point; no new propagation surfaces) route path-(a); only genuinely-asymptotic cascades (structural shifts introducing new propagation surfaces) warrant path-(β). The cycle that canonicalizes the rule must apply the rule correctly to its own routing decisions.
```

## Adjudication / fix-up

**Codex desktop pre-commit review pass 1 (2026-05-03)**: 14 claims verified clean; 1 Blocking finding on Claim 9 (verification command operationally insufficient — `git diff main..feat/task-0015-pmn-007 -- README.md` is a ref-to-ref comparison that always returns empty on a feature branch with no commits yet, regardless of staged content; supplemental staged check confirmed README.md substantively unchanged). Builder reports Codex output verbatim per PMN-002 (a) (no Builder reframing); routing adjudicated per §8.1.1.3 (now-refined per spec §3.4) bounded-continuation rule + cost-class refinement extension.

**Claim 9 — path-(a) revise**:
- Class: (h.2) verification-command operational correctness sub-shape (third cycle instance after claim 7's grep-line-vs-occurrence Note at authoring + claim 8 Builder step-6 self-review case-sensitivity).
- Codex finding: supplied bash command `git diff main..feat/task-0015-pmn-007 -- README.md` does not cover staged pre-commit changes; verification command output: `<empty>` from both ref-comparison and supplemental staged check.
- Cost-class assessment: **pure-token-swap** — single-iteration fix (replace ref-comparison with working-tree-vs-main comparison); no new propagation surfaces beyond the command swap. Substantive content (README unchanged) is correct per Codex's supplemental staged check.
- Routing: path-(a) per §8.1.1.3 cost-class refinement extension (canonicalized this cycle). The cycle that canonicalizes the genuinely-asymptotic-vs-pure-token-swap distinction applies the distinction correctly to its own routing decision; (k.1) positive self-instantiation. Applied: Claim 9 bash command updated to `git diff main -- README.md` (working tree against main; covers both staged and unstaged) plus adjunct `git diff --staged -- README.md` for redundant cross-check.
- Re-stage post-fix verification: both forms return empty; cumulative-diff-stats re-derived per (e.1) sub-rule post-fix.

**Same-class (h.2) sweep per (j) propagation residual discipline**: third cycle instance of (h.2) class after claim 7 explicit Note (caught grep-line-vs-occurrence at authoring) + claim 8 Builder step-6 self-review (caught case-sensitivity). Swept other claims for same-class residuals: claim 1 uses `git ls-files` (tracked-files index, includes staged tree) ✅; claim 15 uses `git diff --staged` ✅; claims 2-8 + 10-14 grep file content on disk ✅. No additional same-class residuals.

**Pre-commit Builder pre-flight findings already absorbed at spec correction time** (Architect path-(a) revision per spec §10 defect log Builder pre-flight entries):

- **Mismatch 1** docs/post-merge-notes/ count: spec §5.1 expected `6` corrected to `7 (.gitkeep + PMN-001..006)`. Class: (i.2) filesystem-path / (k.2) failure-mode self-instantiation (Architect iter-4 "correction" introduced the defect; iter-1/2/3 baseline was correct). Routing: path-(a) per §8.1.1.3 cost-class refinement (pure-token-swap class — single-iteration fixed-point; no downstream propagation surfaces). Architect applied path-(a) before Builder resumed step 2.
- **Mismatch 2** docs/reviews/ count: spec §5.1 expected `≥12` corrected to `11 (PR-2..PR-11 + PR-13)`. Class: (i.4) recap-consistency / (i.5) sub-shape candidate emerging — convention-inference verification gap not caught by extended pre-authoring batch which scopes to direct-text grep verification not convention-inference. ADR-001 decision 11 owner-invokes-Codex convention applies at substantive-cycle PRs only; chore-fix-up PRs (PR-12/PR-14) did not generate separate review-context files. Routing: path-(a) per §8.1.1.3 cost-class refinement (pure-token-swap class). Architect applied path-(a) before Builder resumed step 2.

**Pre-flight defect tally** (carried to PMN-008 cycle's PMN-007 §1.1 honesty record):
- 7 Architect §23.6 iteration defects across iter-2/iter-3/iter-4 (per spec §10 defect log Iteration 1→2 / 2→3 / 3→4 entries)
- +1 (k.2) failure-mode self-instantiation: iter-4 Defect H "correction" introduced Mismatch 1 (overlap with Mismatch 1 surfacing — counted once)
- +2 Builder pre-flight defects: Mismatch 1 (overlap; iter-4 self-introduced); Mismatch 2 baseline-knowledge gap

Net distinct defects: 9 (7 iteration + Mismatch 2 net-new; Mismatch 1 is the iter-4 self-introduced defect surfaced at Builder pre-flight, counted once). Vs PR-13 cycle baseline: 17 Architect-side + 3 Builder pre-flight = 20 spec-time. **(i) refinement candidate** (extended pre-authoring batch) preliminary verdict: helping at §-header enumeration surface (claim 5: 21 baseline matched at Builder pre-flight); not catching convention-inference gaps. (i.5) sub-shape candidate emerges from this cycle: when asserting expected counts of files-per-PR-class, verify against actual git history not convention inference.

**(j) same-class propagation residuals** gains third in-cycle data point: iteration-4 path-(a) "correction" introduced new defect at the surface being corrected. Strong corroboration for the canonicalization candidate (already at preliminary two-instance single-cycle from PMN-007 §3.3); now three-instance single-cycle.

[Codex pre-commit findings populated at step 8 — pending owner invocation per ADR-001 decision 11.]

**Codex post-PR review pass 1 + pass 2 (2026-05-03, post-PR-15-open)**: owner invoked `@codex review` per ADR-001 decision 11. Two-endpoint poll per core.md §8.1.1.1 (corrected canonical form per PMN-006 §1.1 defect 2: `gh api ... --paginate` + lexicographic tie-break per (h.3) + author filter for `chatgpt-codex-connector[bot]`) confirmed Codex actually fired (verify-before-assert per §24; phantom-review check per §8.1.1.2). Endpoint 1 (PR reviews) empty; Endpoint 2 (PR comments) returned **2 Codex comments**:

1. **Pass 1** (id 4366725804, 2026-05-03 17:17:22Z) — verbose "Review outcome (post-PR follow-up)" comment with explicit "Blocking: None identified", "Major: None identified", "Minor: None identified". Codex cited canonical line ranges in `core.md §8.1.1.3` (lines 115-147), TASK-0015 handoff (lines 4-6, 97-99), and PR-15 review-context (lines 15-17, 119-120) confirming cycle narrative consistency. Repository checks run: `git status`, `git log --oneline -10`, `nl -ba core.md | rg -n "8\.1\.1\.3|Cost-class sub-distinction|bounded-continuation"`, `nl -ba docs/reviews/PR-15-codex-pre-commit.md | sed -n '1,120p'`, `nl -ba docs/handoffs/TASK-0015-pmn-007-pr-13-cycle-learnings.md | sed -n '1,140p'`.

2. **Pass 2** (id 4366731614, 2026-05-03 17:20:27Z) — standard auto-review template: "Codex Review: Didn't find any major issues. Delightful!"

**Substantive findings across both passes**: 0 Blocking / 0 Major / 0 Minor. Recommended disposition: clean.

**Pass-shape analysis per PMN-007 §9.3 (n) cycle-trailing-clean-Approve**: this is **NOT** a cycle-trailing-clean shape (which requires "prior pass with findings + path-(a) absorption + subsequent clean pass" per PMN-007 §9.3 + PR-10 pass 5 + PR-11 close + PR-13 close precedents). This is a **clean-first-pass** shape — empirically novel relative to PR-10/PR-11/PR-13 cycle data. **Single-data-point empirical evidence** of pre-commit-pipeline-sufficient state: the four-surface pipeline (Architect §23.6 4-iter to fixed-point + Builder pre-flight + Builder step-6 self-review + Codex desktop pre-commit) reached defect-free state without requiring post-PR iteration.

**Routing**: NO path-(a) revisions needed (zero findings). Step 14 N/A.

**PMN-008 candidate observation entries** (Architect-adjudicated framing per architect surface):

- **Clean-first-pass post-PR Codex pass sub-shape** (provisional naming (n.2) or similar numbering at PMN-008 spec authoring): empirically distinct from (n) cycle-trailing-clean-Approve canonicalized at PMN-007 §9.3. The (n) shape requires "prior pass with findings + path-(a) absorption + subsequent clean pass" per PR-10 pass 5 + PR-11 close + PR-13 close precedents. PR-15 close = clean-first-pass (no prior post-PR findings → clean on first run). Preliminary single-data-point sub-shape candidate at PMN-007 §9.3 application surface; cross-cycle confirmation ~2-3 cycles before canonical refinement to §8.1.1.1 explicitly noting both shapes.

- **(j) same-class propagation residual sweep adequacy positive empirical evidence**: Builder's step 8 same-class sweep claim ("No additional same-class residuals" after the third (h.2) cycle instance at claim 9) was empirically tested by post-PR Codex pass returning zero findings. Validates the discipline that correction at surface-of-finding + same-class sweep at adjacent surfaces prevents residual propagation. (j) cluster strengthens toward canonicalization threshold; carried to PMN-008 cycle as adequacy-confirmation evidence.

- **Pre-commit pipeline sufficiency hypothesis** preliminary single-data-point: four-surface pipeline (Architect §23.6 4-iter + Builder pre-flight + Builder step-6 self-review + Codex desktop pre-commit) reached defect-free state pre-merge. Corroborates PMN-007 §3.1 four-surface refinement; the maturation interpretation is that pre-commit-pipeline can collapse the cycle-trailing-clean multi-pass pattern when applied iteratively-to-fixed-point at each surface. Carried to PMN-008 cycle as preliminary single-data-point.

- **Pre-merge record-updates-as-fix-up sub-shape** (Architect framing precision per PMN-008 §1.1 honesty record entry): the discipline being self-instantiated by Option 1 (fix-up commit on feature branch BEFORE squash-merge capturing post-PR Codex absorption + handoff body fill) is the PR-13 cycle pattern of pre-merge record-updates-as-fix-up — a sub-shape of PMN-001 (h.2) file-based Builder direction operationalized as cycle-record discipline. NOT §18.3 M-A7 self-instantiation (which is about the merge-commit-body itself); the precision matters for cross-discipline cross-reference correctness.

- **Cycle defect tally final**: 11 net distinct cycle defects vs PR-13 baseline 20 ≈ **0.55x defect density**. Zero post-PR findings → final tally unchanged from step 11 stop-and-show. (i) refinement candidate empirical verdict at cycle close: helping at surfaces it scopes to (direct-text grep verification for §-header enumeration / grep semantics); not catching what it doesn't scope to (convention-inference gaps; iter-N self-introduced defects). Multi-surface mitigation per PMN-006 §3 framing remains structurally load-bearing.

## Builder hand-back attestation

After Codex desktop pre-commit review completes, Builder reports:
- Codex review outcome (per the summary structure above)
- Path (a) revisions made, if any
- Path (β) acceptances recorded, if any per §8.1.1.3 bounded-continuation rule (refined this cycle with genuinely-asymptotic-vs-pure-token-swap distinction)
- §23.6 recapitulation-consistency re-check result after any path (a) revisions (per PMN-003 (a) refined; extended scope per PMN-004 §2.3 to include verification-command surfaces; further extended per PMN-005 §4.4 sub-rule (e.1) to include cumulative-diff-stats re-derivation; further extended per PMN-006 §3.4 to include frontmatter-vs-body sub-clause)
- Section-citation correctness sweep result after any path (a) revisions, applied iteratively to convergence per PMN-005 §4.3 / §23.6.2
- Cumulative-diff-stats Evidence subsection populated with landed exact counts from `git diff --staged --stat` immediately before commit, per PMN-005 §4.4 sub-rule (e.1)
- (g)/(h)/(i) self-application sweep result on this review-context's own claim blocks; iteration count to convergence
- Cost-class routing adjudication (per spec §3.4 / PMN-007 §2.4 / §8.1.1.3 refinement): for any path-(β) routing applied during pre-commit absorption, document the genuinely-asymptotic justification explicitly — pure-token-swap cascades terminate at one-iteration fixed-point and route path-(a) by default.

## Post-PR / post-merge claims (segregated per (c)/(d) discipline)

Post-PR-merge claims that cannot be verified at pre-commit (per spec §6.2):

- PR-15 squash SHA exists at expected location (verified post-merge by Builder + Architect five-point check).
- linked_pr field substituted in TASK-0015 handoff frontmatter post-merge (per PMN-001 (k) discipline; small-chore-PR mechanism applies if branch protection requires per spec §4 mechanism-vs-discipline distinction).
- PMN-007 status flipped from `drafted` to `recorded` post-merge.
- M-A6 post-merge calculation = 7/13 = 54% (verified by counting PMN files + counting substantive merged PRs).
- core.md framework_version unchanged at v2.16 (PMN-007 cycle does not bump per spec §2 out-of-scope).

## Notes

- Codex desktop reviews the untracked working tree before commit (read-only git inspection only; no `.git/index.lock` writes).
- Post-PR `@codex review` is owner-invoked per ADR-001 decision 11; this pre-commit review is separate and is the substantive verification before commit.
- PR-15 is a substantive PMN-cycle authoring PMN-007 (PR-13 cycle learnings; ~600+ source lines per PMN-007 §-header structure per spec §1.4 framing) plus a surgical addition to core.md §8.1.1.3 (one paragraph per spec §3.4 byte-exact text). Recursive-self-instantiation: the discipline being canonicalized (cost-class refinement extension distinguishing genuinely-asymptotic from pure-token-swap cascades) is applied at its own canonicalization moment within this same cycle — Builder pre-flight Mismatch 1 + Mismatch 2 routing applied path-(a) per the very refinement this cycle canonicalizes.
- Builder pre-flight Mismatch 1 + Mismatch 2 (Builder pre-flight surface; (i.2) / (i.4) / (i.5) cluster): both path-(a) per §8.1.1.3 cost-class refinement extension (pure-token-swap class); spec corrected at Architect path-(a) revision before Builder resumed step 2.
- Builder step-6 self-review surface caught one additional (h.2) sub-shape defect in this review-context's own claim 8 (case-sensitivity mismatch on `grep -o "pure-token-swap"` — byte-exact spec §3.4 text contains `Pure-token-swap cascades` with capital P; case-sensitive bash returns 2 not 3). Routing path-(a) per §8.1.1.3 cost-class refinement extension (pure-token-swap class — single-iteration fix; no new propagation surfaces beyond the case-sensitivity flag update). Self-application of the very refinement this cycle canonicalizes; (k.1) positive self-instantiation. Architect-side spec §6.1 claim 8 + spec §5.6 verification commands carry the same (h.2) defect (gitignored per ADR-001 decision 15; Architect can correct in their copy independently).
- Spec-origination + execution defect count this cycle: 11 net distinct (7 Architect iteration + Mismatch 2 net-new; Mismatch 1 overlaps with iter-4 self-introduced; +1 Builder step-6 self-review surface (h.2) on PR-15 review-context claim 8 case-sensitivity; +1 Codex pre-commit pass 1 Blocking on PR-15 review-context claim 9 (h.2) ref-vs-tree-comparison) vs PR-13 cycle baseline of 20 = ~0.55x. Pre-authoring verification batch + iterative §23.6 sweep + Builder pre-flight surface + Builder step-6 self-review surface + Codex pre-commit surface composition: helping at direct-text-verification surfaces; not catching convention-inference gaps; catching Builder-authored (h.2) sub-shape defects at Builder step-6 self-review + Codex pre-commit surfaces. (h.2) sub-shape three-instance single-cycle evidence (claim 7 Note authoring + claim 8 Builder step-6 + claim 9 Codex pre-commit) — same-class three-instance pattern within single cycle confirms (j) same-class propagation residual canonicalization candidate at three-data-point single-cycle evidence (PMN-007 §3.3 was at two-data-point; promoted to three-data-point this cycle). Carried to PMN-008 cycle as substantive empirical material on (i) refinement candidate verdict + (i.5) sub-shape candidate + (j) same-class propagation residual three-instance single-cycle evidence + Builder step-6 self-review surface as fifth iterative-multi-surface stage extending PMN-007 §3.1 four-surface refinement.
