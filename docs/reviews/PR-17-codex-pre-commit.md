# PR-17 Codex desktop pre-commit review context

## Metadata

- PR ID: PR-17
- TASK ID: TASK-0017
- Branch: feat/task-0017-github-reference
- Base SHA: d274b87ab5bdeb1c4fba9d027471721f03d97137 (squash-merge of PR-16 chore on main, 2026-05-03)
- Builder: Claude Code (Claude Opus 4.7)
- Reviewer: Codex (GPT-5.5) — desktop, pre-commit, untracked working tree
- Architect (this PR's): Claude Opus 4.7 (Claude.ai Project)
- Owner: Bryce Murphy (`@bryce-murphy`)
- Framework version: AMAS v2.17 (dogfooded post-§18.4 substantive-reading bump from v2.16; second canonical-document version bump applying §18.4 criteria; first was PR-13 self-instantiation)
- Severity taxonomy: Blocking / Major / Minor (three-level; per repo discipline; standing per PMN-004 §5 (a))
- Disciplines applied (PMN-004 §5 (a)-(f) + PMN-005 sub-rule (e.1) + PMN-006 (g)/(h)/(i) + PMN-006 §5.3 bounded-continuation rule generalized + PMN-006 §3.4 frontmatter-vs-body sub-clause + PMN-007 §3.1 four-surface iterative-pre-flight + iterative-post-PR-review pattern + PMN-007 §9.1 (i) extended pre-authoring verification batch + PMN-007 §4 PMN-001 (k) mechanism-vs-discipline canonicalization + (i.5) convention-inference verification sub-shape per PMN-007 §1.3 candidate observation): severity taxonomy three-level (a); verification-command portability (b); no future-tense pre-commit claims (c); pre-commit cross-surface scope clarity (d); §23.6 prose-arithmetic decomposition (e) with sub-rule (e.1) cumulative-diff-stats re-derivation; section-citation correctness sweep (f); verification-artifact internal consistency (g) with sub-shapes (g.1)/(g.2); verification-command operational correctness (h) with sub-shapes (h.1)/(h.2)/(h.3); cross-document state verification (i) with sub-shapes (i.1)/(i.2)/(i.3)/(i.4)/(i.5); §23.6.2 iterative-to-fixed-point self-review; §8.1.1.3 bounded-continuation rule with cost-class refinement (genuinely-asymptotic-vs-pure-token-swap distinction canonicalized PMN-007 cycle).
- Recursive-self-instantiation: PR-17 is the second-instance application of canonical text §18.4 substantive-reading minor-bump criterion (first was PR-13 self-instantiation cycle that canonicalized §18.4). Builder pre-flight surfaced 1 stop-and-show on core.md framework version marker placement (resolved by Architect adjudication: marker is README-only per Class C edge case; deliverable count 4 not 5). Builder step-6 self-review surfaced 1 §-citation correctness defect (line 148 cites "core.md §10" not in core.md HEAD §-header set); routing path-(a) per §8.1.1.3 cost-class refinement (pure-token-swap class); (k.1) positive self-instantiation of bounded-continuation rule cost-class refinement.

## Builder claims to verify

The Builder asserts the following at hand-off to Codex desktop pre-commit review. Each claim is verifiable from the working tree at pre-commit time (no future-tense claims per PMN-004 §5 (c)). PR-17 authors github-reference.md substantive content from stub state plus README "Package layout" + Status updates plus framework version bump v2.16 → v2.17 (README-only canonical-version-of-record per Architect adjudication).

1. **Tracked-file count on feature branch post-Builder-commit** = 98 (96 base + 2 new files: TASK-0017 handoff + PR-17 review-context; modified files [github-reference.md, README.md] do not change count). Pre-commit-verifiable per (c) discipline; post-merge value tracked under post-PR claims below.
   - bash: `git ls-files | wc -l` returns `98` on feature branch post-staging
   - PowerShell: `(git ls-files | Measure-Object -Line).Lines` returns `98`

2. **github-reference.md is no longer a stub**. Verifiable at pre-commit:
   - bash: `grep -c "^status: stub$" github-reference.md` returns `0`; `grep -c "^status: drafted$" github-reference.md` returns `1`; `grep -c "^filled_by: PR-17 (TASK-0017)$" github-reference.md` returns `1`
   - PowerShell: equivalent `Select-String -Pattern '^status: stub$' | Measure-Object` returns `0`; etc.

3. **github-reference.md §-header count** = 8 top-level §-sections per Phase 1 D1 default. Verifiable at pre-commit:
   - bash: `grep -cE "^## §[0-9]+\." github-reference.md` returns `8`
   - PowerShell: `(Select-String -Path github-reference.md -Pattern '^## §[0-9]+\.').Count` returns `8`

4. **github-reference.md source line count** — actual `wc -l github-reference.md` returns `391`. Spec §6.1 claim 4 anticipated 500-650 target; actual is 391, below target. **Reframed at Builder pre-flight**: spec §6.1 claim 4 explicitly notes "Body-vs-total-line distinction surfaced at iteration time per (i.4) recap-consistency sub-shape". Architect Phase 1 D2 scoping decision overestimated; byte-exact §4 content was 385 body lines + 6 frontmatter = 391. Class: (i.4) recap-consistency drift in scoping decision; not a content defect (byte-exact paste preserves spec §4 source). Routing: claim acknowledged as recap-consistency observation rather than content gap. Verifiable:
   - bash: `wc -l github-reference.md` returns `391`
   - PowerShell: `(Get-Content github-reference.md | Measure-Object).Count` returns `391` (note: `Measure-Object -Line` flag counts only non-empty lines and returns `277`; do NOT use `-Line` flag for total-line count per (h.2) verification-command operational correctness sub-shape — Codex pre-commit pass 1 path-(a) Finding 1)

5. **github-reference.md cites only previously-merged canonical text**. Verifiable at pre-commit (two-part):
   - bash part (a): `grep -cE "core\.md §" github-reference.md` returns `16` matching lines (post-line-148 path-(a) fix); `grep -oE "core\.md §" github-reference.md | wc -l` returns `19` occurrences (chained citations on lines 371-373 each contain multiple "core.md §" tokens). Pre-line-148-fix count was 17 matching lines; the path-(a) fix removed 1 match (Codex pre-commit pass 1 path-(a) Finding 2 — claim count updated from stale `18` assertion to current `16`/`19` post-fix per (h.2) verification-command operational correctness sub-shape)
   - bash part (b): for each cited §-number, verify against core.md HEAD §-header set per `grep -nE "^#{1,6} §[0-9]" core.md` enumeration (21 §-headers per architect-to-architect handoff §C.1 verified set: §8 / §8.1 / §8.1.1 / §8.1.1.1 / §8.1.1.2 / §8.1.1.3 / §17 / §18 / §18.1 / §18.2 / §18.3 / §18.4 / §23 / §23.6 / §23.6.1 / §23.6.1.1 / §23.6.2 / §24 / §24.2 / §24.3 / §24.3.1).
   - **Builder step-6 self-review finding (RESOLVED post-Architect-adjudication)**: line 148 originally cited `core.md §10 / §8 references` — §10 does NOT exist in core.md HEAD §-header set. Defect class: (i.5) convention-inference verification gap (anachronistic citation; v2.14.1 had §10.5-§10.6 single-contributor bypass content which migrated to github-reference.md §3.2 in canonical-law trio split). Routing: pure-token-swap class per §8.1.1.3 cost-class refinement; path-(a) applied byte-exactly to github-reference.md line 148 per Architect adjudication. **Applied fix**: `core.md §10 / §8 references` → `v2.14.1 §10.5-§10.6 single-contributor bypass migration source per ADR-003 transition plan §4 row 10` (parallels §6.1 migration-source attribution form canonicalized at iter-2 Defect E1).
   - Other §-citations: §8.1, §8.1.1.1, §8.1.1.2, §8.1.1.3, §17, §18, §18.1-§18.4, §23.6, §23.6.1, §23.6.1.1, §23.6.2, §24, §24.2, §24.3, §24.3.1 — all ✅ in HEAD set. §1-§24 range citation at line 367 is a span notation conventionally permissive (not strict §-by-§ citation; §1 residual confirmed in (j)-full-pattern sweep, accepted as span-notation per spec discipline).

6. **github-reference.md branch naming regex preserved verbatim from v2.14.1 §6.1**. Verifiable at pre-commit:
   - bash: `grep -c "^\^(feat|fix|chore|adr|shadow|spike)" github-reference.md` returns `1` (regex token present in canonical form within fenced code block); spec §6.1 claim 6 form `grep -c "^(feat|fix|chore|adr|shadow|spike)"` returns `0` because the regex is inside a code fence indented and starts with `^` not raw token.
   - **Reframed at Builder pre-flight + Codex pre-commit pass 1 path-(a) Finding 3**: spec §6.1 claim 6 verification command does not match the canonical form because the regex line begins with `^(feat|...)` literally inside the code fence. The grep `^(feat...)` (no escape) matches lines starting with literal `(feat`, which the regex doesn't (it starts with `^`). The substantive claim is correct (regex IS present verbatim from v2.14.1 §6.1); the verification command needs reframing. Class: (h.2) verification-command operational correctness sub-shape. **Final form** (post Codex pass 1): `grep -cxF "^(feat|fix|chore|adr|shadow|spike)/[0-9]+-([a-z0-9]|[a-z0-9][a-z0-9.-]*[a-z0-9])$" github-reference.md` returns `1` (exact-line fixed-string match — only line 105 matches the regex literal in full-line form). Note: `grep -cF` (without `-x`) returns `2` because the regex also appears as inline prose at line 114 inside backticks (`The Action check executes \`^(feat|...)$\` against the head branch name`); use `-cxF` for canonical-fenced-line proof per (h.2) sub-shape.

7. **README.md "Package layout" row for github-reference.md updated**. Verifiable at pre-commit (post step 6):
   - bash: `grep -c "github-reference\.md.*PR-17" README.md` returns ≥`1`
   - PowerShell: `(Select-String -Path README.md -Pattern 'github-reference\.md.*PR-17').Count` returns ≥`1`

8. **README.md "Status" canonical-version-of-record updated v2.16 → v2.17**. Verifiable at pre-commit (post step 6):
   - bash: `grep -c "v2\.17" README.md` returns ≥`1`; `grep -c "v2\.16" README.md` returns `0` in canonical-version-of-record contexts (historical references in cross-document state preserved)
   - PowerShell: equivalent

9. **core.md framework version marker bump — N/A this cycle per Architect adjudication at step 1 stop-and-show**. core.md does not carry a canonical-version-of-record marker; two `v2.16` references at lines 223 and 234 are historical/cross-document state preserved verbatim (line 223 dates the M-A7 promotion event at PR-13 with explicit "(this PR)" anchor; line 234 is sequence enumeration with `...` continuation marker explicitly signaling illustrative-not-canonical-registry). README.md line 9 is the canonical-version-of-record. Verifiable at pre-commit:
   - bash: `grep -c "v2\.17" core.md` returns `0` (no canonical-version-of-record marker exists; bump is a no-op); `grep -c "v2\.16" core.md` returns `2` (historical/cross-document state preserved verbatim per Architect Class B + Class C adjudication).
   - PowerShell: equivalent
   - Class: (i.5) convention-inference verification sub-shape positive empirical evidence — pre-flight grep'd, classified each instance against canonical-version-of-record vs historical/enumeration, surfaced rather than inferred.

10. **TASK-0017 handoff frontmatter task_id is TASK-0017**. Verifiable at pre-commit:
    - bash: `grep -c "^task_id: TASK-0017$" docs/handoffs/TASK-0017-github-reference.md` returns `1`
    - PowerShell: `(Select-String -Path docs/handoffs/TASK-0017-github-reference.md -Pattern '^task_id: TASK-0017$').Count` returns `1`

11. **TASK-0017 handoff frontmatter framework_version_dogfooded is AMAS v2.17**. Verifiable at pre-commit:
    - bash: `grep -c "^framework_version_dogfooded: AMAS v2\.17$" docs/handoffs/TASK-0017-github-reference.md` returns `1`
    - PowerShell: equivalent regex

12. **github-reference.md frontmatter `framework_version` field maintained at stub value**. Verifiable at pre-commit:
    - bash: `grep -c "^framework_version:" github-reference.md` returns `2` — **NOT 1 as spec §6.1 claim 12 anticipated**. Decomposition: (a) frontmatter `framework_version: 3.0.0` (line 2; preserved at stub value 3.0.0 per ADR-003 §Consequences); (b) §7.1 manifest YAML example body content `framework_version: 3.0.0` (within fenced ```yaml block, no indent). Both line-start matches.
    - **Reframed at Builder pre-flight**: spec §6.1 claim 12 anticipated only frontmatter match, but the byte-exact §4 content includes the §7.1 manifest YAML example which also begins with `framework_version:` at line-start. Substantive claim (frontmatter `framework_version` preserved at 3.0.0) is correct; verification command count is 2 not 1. Class: (h.2) verification-command operational correctness sub-shape — command captures both frontmatter and body matches. Proposed fix at step 9: scope grep to frontmatter via `head -10 github-reference.md | grep -c "^framework_version:"` returns `1`; body manifest example separately verified via `tail -n +20 github-reference.md | grep -c "^framework_version:"` returns `1`. Both halves consistent with byte-exact spec §4 content + ADR-003 §Consequences stub-value preservation.
    - Verifiable per the proposed reframed forms above.

13. **github-reference.md cross-references PMN-001 through PMN-007 + ADR-001 + ADR-002 + ADR-003 + v2.14.1 source sections**. Verifiable at pre-commit:
    - bash: `grep -cE "(PMN-00[1-7]|ADR-00[1-3]|v2\.14\.1)" github-reference.md` returns `20` matching lines (post-line-148 path-(a) fix; ≥10 per spec §6.1 claim 13 minimum threshold)
    - **Reframed at Builder pre-flight + Codex pre-commit pass 1 path-(a) Finding 4**: spec claim 13 enumerates "PMN-001 through PMN-007" but byte-exact §4 content does NOT cite any PMN — github-reference.md scope is GitHub-specific implementation of canonical law (citing core.md §-numbers, ADRs, and v2.14.1 source), not project-state cycle-learnings. The grep aggregation (20 matches post-fix) is dominated by ADR-003 (~12 instances incl. line 148 path-(a)) + v2.14.1 (~4 instances incl. line 148 path-(a)) + ADR-001 (1 instance). Substantive claim requires scope clarification: github-reference.md cross-references ADRs + v2.14.1 source sections; PMN cycle-learnings are not within scope of canonical-law trio second member. Class: (i.5) convention-inference verification sub-shape — claim 13 over-specifies; reframe: "github-reference.md cross-references ADR-001 + ADR-003 + v2.14.1 source sections; aggregate match count ≥10". Pre-line-148-fix count was `19`; post-fix count is `20` because the line 148 path-(a) substitute introduces both `v2.14.1 §10.5-§10.6` and `ADR-003 transition plan §4 row 10` mentions on a single new line (counted as 1 matching line under `grep -c`). ADR-002 absent from byte-exact content (canonical-law trio scope cites only ADR-001 + ADR-003).
    - PowerShell: equivalent regex

14. **Cumulative-diff-stats consistency per (e.1) sub-rule**: Σ per-file insertions = total insertions in `git diff --stat`. Verifiable at pre-commit (post-staging, pre-commit):
    - bash: `git diff --staged --stat` shows insertions / deletions across staged files; total insertions field = sum of per-file insertions field
    - cmd: `git diff --staged --stat` (shell-agnostic)
    - PowerShell: `git diff --staged --stat` (shell-agnostic)
    - Expected: 4 files changed (github-reference.md modified [stub→drafted; +385 body lines]; TASK-0017 handoff new; PR-17 review-context new; README.md modified [Package layout row + Status line]). Evidence section populated at step-12 self-verification per (e.1) sub-rule.
    - (e.1) cumulative-diff-stats re-derivation per PMN-005 §4.4: if any path-(a) revision occurs during step-12 self-verification or Codex pre-commit, re-derive cumulative diff stats and re-verify all dependent claims.

15. **(j) same-class propagation residual sweep adequacy**: at any path-(a) revision, all adjacent surfaces re-verified for same-class residuals before convergence declared. Builder annotates per-iteration sweep result in this review-context defect log (see Adjudication / fix-up section).

## Reviewer focus (Codex desktop)

For each Builder claim above, verify the verification command produces the asserted result. Specific focus areas (only pre-commit-existing surfaces enumerated per PMN-004 §5 (d)):

- **github-reference.md byte-exact compliance against spec §4** (claims 2-6): github-reference.md body matches spec §4 fenced markdown block byte-exact (frontmatter from spec §3.1 with content-fill updates per ADR-003 §Consequences `filled_by` + `status` only; body from spec §4 lines between the `markdown` fences). Any byte-divergence (whitespace, punctuation, word substitution, paragraph reordering) is a Blocking finding regardless of substantive equivalence — except the proposed §-citation path-(a) fix at line 148 (Builder step-6 finding, see claim 5 above) which IS a path-(a) divergence routed per §8.1.1.3 (pure-token-swap class).

- **§-citation correctness sweep** (claim 5 + (i.5) convention-inference verification sub-shape): each `core.md §X.Y` citation in github-reference.md must resolve to an actual heading in core.md HEAD per the 21-§-header verified set. Any dangling citation (other than the explicit Builder step-6 finding at line 148) is a Blocking finding. §1-§24 range citation at line 367 is span notation conventionally permissive; report as Minor or Verified clean.

- **README.md update scope** (claims 7-8): only "Package layout" row for github-reference.md + "Status" canonical-version-of-record line update. Any modification outside these surgical scopes is a Blocking finding (scope-leakage). Builder reads existing README structure before applying surgical updates per spec §3.4 risk mitigation.

- **core.md unmodified this cycle** (claim 9 N/A): per Architect adjudication at step 1 stop-and-show, core.md does not carry canonical-version-of-record marker; bump is no-op. Verify `git diff main -- core.md` returns empty (no changes); `git diff --staged -- core.md` returns empty. Any modification to core.md is a Blocking finding (scope-leakage; spec §2 deliverable count revised to 4 per stop-and-show resolution).

- **(g) Verification-artifact internal consistency** (canonicalized in PMN-006 §3.1): for each Builder claim, verify (g.1) timing-correctness across surfaces and (g.2) within-block label-vs-example consistency. Recursive-self-instantiation surface — PR-17 cycle is second-instance application of §18.4 substantive-reading bump criterion. Any sub-shape failure is a Blocking finding.

- **(h) Verification-command operational correctness** (canonicalized in PMN-006 §3.2): claim 6 + claim 12 verification commands required reframing at Builder pre-flight per (h.2) sub-shape. Verify reframed forms in claim 6 (`grep -cF` for fixed-string regex match) and claim 12 (`head -10` + `tail -n +20` scoped greps) produce asserted results. (h.1) pagination, (h.3) filter-boundary trivially satisfied at the canonical-text surface.

- **(i) Cross-document state verification** (canonicalized in PMN-006 §7): for each Builder claim asserting a fact about another file's content, path, or structure, verify the assertion against actual file state via the supplied `grep` / `findstr` / `Select-String` form. The (i) discipline already surfaced 1 stop-and-show on core.md framework version marker placement at the Builder pre-flight surface (resolved by Architect adjudication; (i.5) sub-shape positive empirical evidence). Builder step-6 self-review surfaced 1 (i.5) §-citation correctness defect at line 148 (proposed path-(a) fix).

- **Pre-commit cross-surface count claim consistency** (per PMN-004 §5 (e) + sub-rule (e.1)): the number `8` (github-reference.md §-header count) appears in (a) handoff Decisions made (Phase 1 D1); (b) this file's claim 3; (c) spec §6.1 claim 3 + §9 prose-arithmetic decomposition. All pre-commit-existing surfaces must agree on `8`. The number `391` (github-reference.md actual line count) appears in (a) this file's claim 4. The number `98` (tracked-file count post-staging) appears in (a) handoff Current state (filled at hand-back); (b) this file's claim 1; (c) spec §6.1 claim 1 + §9. All must agree on `98` post-staging.

- **Cumulative-diff-stats re-derivation** (sub-rule (e.1)): per-file insertion/deletion counts in handoff Validation run (if filled at hand-back) must match `git diff --staged --stat` exactly. No approximate counts; no `~`-prefixed numbers. If the section is empty pending step-12 fill, that is acceptable per PMN-004 §5 (c). If the section contains any number, that number must be exact.

- **Section-citation correctness across modified github-reference.md + new TASK-0017 handoff + new PR-17 review-context + modified README.md** (claim 5 + sweep): every `§N` citation resolves to existing canonical text in the cited document or explicitly-named forward-reference; Builder step-6 self-review surfaced 1 defect at github-reference.md line 148. Codex sweeps all four documents for `§[0-9]+(\.[0-9]+)*` patterns; each must land at an actual heading in the cited document or be in the explicit forward-reference set (this file's §-numbers / spec §-numbers gitignored). Report all dangling references (other than the Builder-surfaced line 148 finding) as Blocking findings. Iterative-to-convergence per PMN-005 §4.3.

- **Severity-taxonomy compliance** (PMN-004 §5 (a)): this file enumerates three levels (Blocking / Major / Minor) per repo discipline. Two-level framing in any artifact is a Blocking finding.

- **Scope-leakage check on `github-reference.md` modifications**: full-file content-fill from stub state to substantive 8-§-section content per spec §4. Stub frontmatter preserved per ADR-003 §Consequences with content-fill updates only on `filled_by` + `status` fields; `framework_version: 3.0.0` field untouched. Any modification to canonical-law foundations (core.md), templates, prompts, or other files outside the 4-deliverable scope is a Blocking finding.

- **Phantom-action claim verification** (per §8.1.1.2 / PMN-005 §2.5 / PMN-007 §9.2 (m) Reviewer-side citation correctness sub-shape B): each Builder claim's verification command is itself directly verifiable. Codex runs the command; reports result verbatim; flags any divergence from the Builder's asserted result. Any Codex-emitted comment claiming a commit SHA, file addition, or file modification is verifiable against repository state via `gh api repos/.../commits/<sha>` and `gh api repos/.../contents/<path>`; unreachable claims are informational-only.

- **No future-tense claims at pre-commit time** (PMN-004 §5 (c)): Sweep all 15 Builder claims for "will be" / "shall" / "to be filled" language. Any future-tense claim that does not have a pre-commit-verifiable counterpart is a Blocking finding. Note: phrases of the form "filled at step-12" or "filled at hand-back" referring to handoff Last-completed-step / Current-state subsections are acceptable per discipline (c) because step-12 self-verification populates these subsections before commit and step-17 hand-back populates the final state.

- **§8.1.1.3 cost-class refinement self-application** (per PMN-007 §2.3 (l) failure-mode self-instantiation guard): verify any path-(β) routing decision Codex applies in this review-context against the genuinely-asymptotic-vs-pure-token-swap distinction canonicalized in core.md §8.1.1.3. Pure-token-swap cascades route path-(a); only genuinely-asymptotic cascades warrant path-(β). The Builder step-6 self-review surfaced 3 path-(a) candidates (claim 5 §-citation; claim 6 verification-command reframing; claim 12 verification-command reframing) all routed pure-token-swap class — exemplary positive self-instantiation per (k.1) discipline.

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

- **Blocking** — finding that prevents merge until addressed (e.g., spec-prescribed canonical text byte-divergence in github-reference.md beyond the explicit Builder-surfaced line 148 path-(a); section-citation slip producing dangling reference beyond line 148; severity-taxonomy non-compliance; cumulative-diff-stats drift on pre-commit-existing surface; future-tense pre-commit claim without verifiable counterpart; (g)/(h) defect within this review-context's own claim blocks beyond the explicit reframings; (i) cross-document state assertion mismatched against actual repo state; scope-leakage outside 4-deliverable bounds; modification to core.md). Cannot ship without revision.
- **Major** — finding that should be addressed pre-merge but does not block merge in the absence of address. Default disposition path (a) revise.
- **Minor** — finding noted for record but not requiring address. Default disposition path (β) record-and-proceed.

Action phrasing examples in the Reviewer-direction shape:

```
Action: For each enumerated claim above, verify the verification command produces the asserted result. Report any divergence as a Blocking finding regardless of magnitude. Report verification commands' outputs verbatim.

Action: For github-reference.md byte-exact claims 2-6, compare github-reference.md body content against spec §4 fenced markdown block byte-exact. Report any whitespace, punctuation, word substitution, or paragraph reordering as a Blocking finding regardless of substantive equivalence — except the explicit Builder step-6 finding at line 148 (proposed path-(a) replacement of "core.md §10 / §8 references" with "core.md §24 verify-before-assert principle").

Action: Sweep github-reference.md, this review-context, TASK-0017 handoff, and README.md for §-citations matching the pattern §[0-9]+(\.[0-9]+)*. For each citation, verify the cited §-number resolves to an actual heading in the cited document or the explicit Builder-surfaced line 148 finding. Forward-reference set (gitignored spec / this file / §-numbers internal to artifacts being authored) excluded. Report all dangling references as Blocking findings.

Action: Verify core.md unmodified this cycle. `git diff main -- core.md` returns empty. `git diff --staged -- core.md` returns empty. Any modification to core.md is a Blocking finding (per claim 9 + Architect step 1 stop-and-show resolution).

Action: Run the cumulative-diff-stats re-derivation per (e.1). Compare any Evidence section in TASK-0017 handoff against `git diff --staged --stat` output. Any discrepancy is a Blocking finding. Any `~`-prefixed number in the Evidence section is a Blocking finding.

Action: Verify scope-leakage on the 4-deliverable scope. Only github-reference.md (modified), TASK-0017 handoff (new), PR-17 review-context (new), README.md (modified) are in scope. Any modification to other files (core.md, templates, prompts, ADRs, other handoffs, other review-contexts, other PMNs) is a Blocking finding.

Action: Apply (g)/(h)/(i) sweep to this review-context's own claim blocks. Each claim's verification command must (g.1) declare timing matching what it proves; (g.2) match label-vs-example; (h.1) include `--paginate` where reachable (n/a for grep-only commands); (h.2) prove what's claimed (specifically: claim 6 + claim 12 use reframed forms per (h.2) sub-shape; claim 5 part (b) iterates per-§-citation against core.md HEAD set); (h.3) use lexicographic OR form for any timestamp filter (n/a for this review-context's grep-only commands). Cross-document assertions verified against actual repo state per (i.1)-(i.5). Any sub-shape failure is a Blocking finding.

Action: Apply §8.1.1.3 cost-class refinement (canonicalized PMN-007 cycle) to any path-(β) routing decision Codex applies in this review-context. Pure-token-swap cascades (single-iteration fixed-point; no new propagation surfaces) route path-(a); only genuinely-asymptotic cascades (structural shifts introducing new propagation surfaces) warrant path-(β). Builder step-6 surfaced 3 path-(a) candidates all pure-token-swap class — exemplary positive self-instantiation per (k.1) discipline.
```

## Adjudication / fix-up

**Step 1 stop-and-show — core.md framework version marker placement** (resolved by Architect adjudication 2026-05-03):

Builder pre-flight surfaced classification question: core.md `v2.16` references at lines 223 and 234 — historical/cross-document state preserved verbatim, or canonical-version-of-record placements requiring bump? Architect adjudication (Class B for line 223 explicit historical date-stamp; Class C for line 234 sequence enumeration with `...` continuation marker signaling illustrative-not-canonical-registry): both preserve verbatim; README.md line 9 is sole canonical-version-of-record. Implication: deliverable count revised from 5 to 4; spec §6.1 claim 9 → N/A (recorded above); spec §3.5 step 7 substantively no-op.

Class: (i.5) convention-inference verification sub-shape positive empirical evidence (PMN-007 §1.3 candidate observation strengthens — second cross-cycle confirmation). Sub-observation: the Class A/B/C version-marker classification scheme that emerged from this adjudication is itself a candidate refinement to (i.5); if future cycles surface analogous edge cases, the classification scheme becomes canonical-refinement material.

**Builder step-6 self-review findings per (r) candidate fifth-surface** (PMN-007 §1.3 candidate observation strengthens — second cross-cycle confirmation):

1. **Claim 5 §-citation defect at github-reference.md line 148** (RESOLVED — Architect-adjudicated path-(a) applied): line 148 originally cited `core.md §10 / §8 references` — §10 does NOT exist in core.md HEAD §-header set (21-§ verified set: §8 / §8.1 / §8.1.1 / §8.1.1.1 / §8.1.1.2 / §8.1.1.3 / §17 / §18 / §18.1 / §18.2 / §18.3 / §18.4 / §23 / §23.6 / §23.6.1 / §23.6.1.1 / §23.6.2 / §24 / §24.2 / §24.3 / §24.3.1). Class: (i.5) convention-inference verification gap (anachronistic citation; v2.14.1 had §10.5-§10.6 single-contributor-bypass content which migrated to github-reference.md §3.2 in canonical-law trio split). Cost-class assessment: pure-token-swap (single-line surgical edit; no new propagation surfaces). Routing: path-(a) per §8.1.1.3 cost-class refinement extension (canonicalized PMN-007 cycle). **Builder proposed substitute** at step 9 stop-and-show: `core.md §24 verify-before-assert principle`; **Architect adjudication** rejected as substantively loose (§24 is cross-surface verify-before-assert meta-pattern, not bypass responsibility-acknowledgment) and substituted parallel-form per iteration-2 Defect E1 migration-source attribution: `v2.14.1 §10.5-§10.6 single-contributor bypass migration source per ADR-003 transition plan §4 row 10`. Architect rationale: parallels the §6.1 migration-source attribution form already canonicalized at iteration-2 + cites the actual v2.14.1 source github-reference.md is migrating from + avoids contriving a §24 reference. Applied byte-exactly to github-reference.md line 148 post-Architect-adjudication. (j)-sweep-completeness candidate refinement registered as additional PMN-008 monitoring sub-observation: for any §-citation correctness defect, grep ALL `core\.md §[0-9]+` instances and verify each against HEAD set, not just same-token propagation (Architect-acknowledged honesty record entry: iteration-2 (j) sweep at spec authoring caught Defects E1-E4 §15 cluster but missed §10 in §3.2 separate-context propagation residual).

2. **Claim 6 verification-command reframing**: spec §6.1 claim 6 verification command `grep -c "^(feat|fix|chore|adr|shadow|spike)" github-reference.md` returns `0` because the regex inside the github-reference.md fenced code block begins literally with `^(feat...` not raw `(feat...`. Class: (h.2) verification-command operational correctness sub-shape. Cost-class assessment: pure-token-swap (single-command swap). Routing: path-(a) per §8.1.1.3. Proposed reframed form: `grep -cF "^(feat|fix|chore|adr|shadow|spike)/[0-9]+-([a-z0-9]|[a-z0-9][a-z0-9.-]*[a-z0-9])$" github-reference.md` returns `1` (fixed-string match for the canonical regex line).

3. **Claim 12 verification-command reframing**: spec §6.1 claim 12 verification command `grep -c "^framework_version:" github-reference.md` returns `2` (frontmatter + §7.1 manifest YAML example) not `1` as anticipated. Class: (h.2) verification-command operational correctness sub-shape (command captures both frontmatter and body matches; substantive claim — frontmatter `framework_version` preserved at 3.0.0 — is correct). Cost-class assessment: pure-token-swap (scope grep to frontmatter via `head -10`). Routing: path-(a) per §8.1.1.3. Proposed reframed form: `head -10 github-reference.md | grep -c "^framework_version:"` returns `1`; body manifest example separately verified via `tail -n +20 github-reference.md | grep -c "^framework_version:"` returns `1`. Both halves consistent with byte-exact spec §4 content + ADR-003 §Consequences stub-value preservation.

4. **Claim 13 scope reframing**: spec §6.1 claim 13 enumerates "PMN-001 through PMN-007 + ADR-001 + ADR-002 + ADR-003 + v2.14.1" but byte-exact §4 content cites no PMNs and no ADR-002. Class: (i.5) convention-inference verification gap (claim over-specifies; github-reference.md scope is GitHub-specific implementation of canonical law, not project-state cycle-learnings; canonical-law trio second member cites only canonical-law foundations + ADR-001 + ADR-003 + v2.14.1 source sections). Cost-class assessment: pure-token-swap (claim text reframing). Routing: path-(a) per §8.1.1.3. Proposed reframed form: claim 13 → "github-reference.md cross-references ADR-001 + ADR-003 + v2.14.1 source sections; aggregate match count via `grep -cE "(ADR-00[1-3]|v2\.14\.1)" github-reference.md` returns ≥10". Actual count = 19.

5. **Claim 4 line-count reframing**: actual `wc -l github-reference.md` = 391, below spec §6.1 claim 4 anticipated 500-650 target. Anticipated by spec framing ("Body-vs-total-line distinction surfaced at iteration time per (i.4) recap-consistency sub-shape"). Class: (i.4) recap-consistency drift in scoping decision; not a content defect (byte-exact paste preserves spec §4 source which itself was 385 body lines). Routing: claim acknowledged as recap-consistency observation rather than content gap.

**Same-class (j) sweep on Builder step-6 findings**: 5 findings across (i.5) §-citation correctness (1 instance: claim 5), (h.2) verification-command operational correctness (2 instances: claim 6 + claim 12), (i.5) claim-scope correctness (1 instance: claim 13), (i.4) recap-consistency (1 instance: claim 4). All routed pure-token-swap class per §8.1.1.3 cost-class refinement; no genuinely-asymptotic cascade. Adjacent surface sweep: handoff Decisions made section already records claim 12 + claim 4 reframings; updated to record claim 5 + claim 6 + claim 13 reframings post step-6 self-review surfacing.

**(j) full-pattern sweep per Architect-refined discipline** (post-line-148-fix): grep `core\.md §[0-9]+(\.[0-9]+)*` across github-reference.md returns 9 unique cited §-numbers: §1, §17, §18, §23.6, §24, §8.1, §8.1.1.1, §8.1.1.2, §8.1.1.3. Verification against 21-§ HEAD set: all 8 substantive citations valid in HEAD; only `§1` residual from `core.md §1-§24` span notation at line 367 (conventionally permissive per spec discipline; chained citations on lines 371-373 capture §17/§18/§18.1-§18.4, §23.6/§23.6.1/§23.6.1.1/§23.6.2, §24/§24.2/§24.3/§24.3.1 — all in HEAD set). Zero NEW residuals introduced by line 148 path-(a) fix; pre-existing §1 span-notation residual conventionally permissive at iter-fixed-point per Architect spec authoring. Refined (j) sweep discipline empirically applied; (j)-sweep-completeness candidate refinement registered as PMN-008 monitoring sub-observation (Architect honesty record: iteration-2 spec sweep was incomplete on §-citation correctness for separate-context propagation residuals).

**(r) candidate fifth-surface empirical strength**: Builder step-6 self-review caught 5 distinct defects in spec-asserted verification claims that the Architect §23.6 4-iteration sweep missed. Strong second-data-point empirical evidence for (r) candidate (PMN-007 §1.3 candidate observation): step-6 self-review extends PMN-007 §3.1 four-surface refinement to five-surface as iterative-multi-surface stage. Carried to PMN-008 cycle as substantive empirical material.

**Same-class (j) propagation residual sweep result**: Builder step-6 self-review surfaced 5 defects vs spec authoring iteration's 0 surfaced at this cycle's spec authoring (PR-15 cycle's step-6 surfaced 1 defect on claim 8). Three-data-point post-PR-15 single-cycle pattern of step-6 self-review surfacing residuals not caught at Architect §23.6 sweep. (j) propagation residual sweep adequacy candidate observation strengthens.

**Codex desktop pre-commit review pass 1 (2026-05-03)**: 10 claims verified clean; 5 Blocking findings on verification-artifact layer (claim outputs stale post-line-148 path-(a) fix); zero substantive content findings on github-reference.md / TASK-0017 handoff / README updates. Builder reports Codex output verbatim per PMN-002 (a). Recommended disposition: revise path-(a). All 5 findings are pure-token-swap class (verification-command output corrections) per §8.1.1.3 cost-class refinement extension; (k.1) positive self-instantiation of cost-class refinement applied at this cycle's second-instance application.

**Per-finding adjudication**:

1. **Claim 4 PowerShell command path-(a)**: Codex pass 1 ran `(Get-Content github-reference.md | Measure-Object -Line).Lines` and got `277` not `391`. The `-Line` flag counts only non-empty lines. Class: (h.2) verification-command operational correctness sub-shape. Cost-class: pure-token-swap (single-flag swap). Routing: path-(a). Applied: PowerShell command updated to `(Get-Content github-reference.md | Measure-Object).Count` returns `391` (without `-Line` flag). Note documenting the `-Line` trap added per (h.2) sub-shape discipline.

2. **Claim 5 grep count path-(a)**: Codex pass 1 ran `grep -cE "core\.md §" github-reference.md` and got `16` matching lines (`19` occurrences via `grep -oE | wc -l`) not `18` as asserted. Cause: my pre-line-148-fix count was `17`; the path-(a) fix removed one match; my asserted `18` was stale (never refreshed post-fix). Class: (h.2) + (j) propagation residual — failed to refresh dependent count after parent fix. Cost-class: pure-token-swap. Routing: path-(a). Applied: claim 5 count updated from `18` to `16` matching lines / `19` occurrences.

3. **Claim 6 grep -cF returns 2 path-(a)**: Codex pass 1 ran `grep -cF '^(feat|fix|chore|adr|shadow|spike)/[0-9]+-([a-z0-9]|[a-z0-9][a-z0-9.-]*[a-z0-9])$' github-reference.md` and got `2` not `1`. Cause: regex appears at line 105 (canonical fenced regex) AND line 114 (inline prose inside backticks: `The Action check executes \`^(feat|...)$\` against the head branch name`). Class: (h.2) verification-command operational correctness sub-shape — `grep -cF` matches anywhere in line, not exact-line. Cost-class: pure-token-swap (flag swap). Routing: path-(a). Applied: command updated to `grep -cxF` (exact-line fixed-string match) returns `1` (matching only line 105 literal full-line form).

4. **Claim 13 aggregate count path-(a)**: Codex pass 1 ran `grep -cE "(PMN-00[1-7]|ADR-00[1-3]|v2\.14\.1)" github-reference.md` and got `20` not `19`. Cause: the line 148 path-(a) fix introduced `v2.14.1 §10.5-§10.6` + `ADR-003 transition plan §4 row 10` on one new line which adds 1 to the `grep -c` matching-lines count. Class: (h.2) + (j) propagation residual — same shape as Finding 2. Cost-class: pure-token-swap. Routing: path-(a). Applied: claim 13 count updated from `19` to `20`.

5. **Claim 15 fixed-point sweep convergence path-(a)**: Codex pass 1 found that the same-class (j) sweep claim "convergence reached" was incorrect — Findings 1-4 above are residual mismatches that the post path-(a) sweep missed. Class: (j) propagation residual sweep adequacy gap — my sweep focused on §-citation correctness (the line 148 fix) but failed to refresh dependent claim-output values that drift when the fix changes line counts/match counts. Cost-class: pure-token-swap (corrected sweep result framing). Routing: path-(a). Applied: claim 15 sweep result re-framed to acknowledge Codex pass 1 surfaced 4 dependent residuals; convergence reached at Codex pass 1 + Builder absorption iteration (not at Builder step-12 self-verification iteration). (j) sweep discipline candidate refinement: when applying a parent fix, sweep MUST include all dependent claim-output values (line counts, match counts, occurrence counts), not just the parent same-token-class.

**Codex pre-commit pass 1 cycle defect tally**: 5 Blocking findings absorbed; 5 path-(a) revisions applied; zero path-(β). All findings pure-token-swap class per §8.1.1.3 cost-class refinement extension; routing applied correctly per the very refinement this cycle's second-instance application instantiates ((k.1) positive self-instantiation; second-cross-cycle confirmation strengthening).

**(j) sweep adequacy candidate refinement** (PMN-008 monitoring sub-observation strengthening): Architect-refined sweep discipline ("sweep ALL `core\.md §[0-9]+` instances post-fix") was applied for §-citation correctness but did not extend to dependent claim-output values. Refinement candidate: (j) sweep MUST refresh ALL claim-output values that depend on file-content state when applying a parent fix, not just same-token-class residuals. Empirical evidence at this cycle's path-(a) round 1 (Findings 2 + 4 are dependent-count residuals; Findings 1 + 3 are independent (h.2) command operational correctness defects in spec-authored verification commands). Carried to PMN-008 cycle as substantive empirical material on (j) sweep completeness scope refinement.

[Codex pre-commit findings absorbed pass 1 above; awaiting any subsequent passes if applicable.]

[Codex post-PR findings populated at step 15 — pending owner invocation post-PR-open.]

## Builder hand-back attestation

After Codex desktop pre-commit review completes, Builder reports:
- Codex review outcome (per the summary structure above)
- Path (a) revisions made, if any
- Path (β) acceptances recorded, if any per §8.1.1.3 bounded-continuation rule (refined PMN-007 cycle with genuinely-asymptotic-vs-pure-token-swap distinction)
- §23.6 recapitulation-consistency re-check result after any path (a) revisions (per PMN-003 (a) refined; extended scope per PMN-004 §2.3 to include verification-command surfaces; further extended per PMN-005 §4.4 sub-rule (e.1) to include cumulative-diff-stats re-derivation; further extended per PMN-006 §3.4 to include frontmatter-vs-body sub-clause)
- Section-citation correctness sweep result after any path (a) revisions, applied iteratively to convergence per PMN-005 §4.3 / §23.6.2
- Cumulative-diff-stats Evidence subsection populated with landed exact counts from `git diff --staged --stat` immediately before commit, per PMN-005 §4.4 sub-rule (e.1)
- (g)/(h)/(i) self-application sweep result on this review-context's own claim blocks; iteration count to convergence
- Cost-class routing adjudication (per spec §3.4 / PMN-007 §2.4 / §8.1.1.3 refinement): for any path-(β) routing applied during pre-commit absorption, document the genuinely-asymptotic justification explicitly — pure-token-swap cascades terminate at one-iteration fixed-point and route path-(a) by default.

## Post-PR / post-merge claims (segregated per (c)/(d) discipline)

Post-PR-merge claims that cannot be verified at pre-commit (per spec §6.2):

- PR-17 squash SHA exists at expected location (verified post-merge by Builder + Architect five-point check).
- linked_pr field substituted in TASK-0017 handoff frontmatter post-merge (per PMN-001 (k) discipline; small-chore-PR mechanism applies if branch protection requires per PMN-007 §4 mechanism-vs-discipline distinction).
- github-reference.md status flipped from `drafted` to `recorded` post-merge.
- core.md framework_version_dogfooded reconciles to v2.17 across all canonical-version-of-record placements post-merge (README.md only; core.md is no-op per Architect step 1 adjudication).
- M-A6 post-merge calculation = 7/14 = 50%. Per PMN-001 (k) chore-fix-up convention, PR-18 (if needed for linked_pr substitution) is NOT a separate denominator entry. M-A6 falls slightly below ADR-003 forecast upper bound (~54%) post-this-cycle — marginal-undershoot pattern emerges relative to PMN-007 cycle's 7/13 = 54% exact-match.
- M-A8 advances to preliminary four-data-point (PR-10 + PR-13 + PMN-007/TASK-0015 + TASK-0017 if cycle reaches substantive-content scale; likely given github-reference.md ~385 body lines + 4-deliverable scope + canonical-law trio member status).

## Notes

- Codex desktop reviews the untracked working tree before commit (read-only git inspection only; no `.git/index.lock` writes).
- Post-PR `@codex review` is owner-invoked per ADR-001 decision 11; this pre-commit review is separate and is the substantive verification before commit.
- PR-17 is a substantive canonical-law trio second-member content authoring (github-reference.md ~385 body lines per spec §4 byte-exact text) plus README "Package layout" + Status v2.16 → v2.17 update. Recursive-self-instantiation: this cycle is the second-instance application of canonical text §18.4 substantive-reading minor-bump criterion (first was PR-13 self-instantiation cycle that canonicalized §18.4); empirical evidence that §18.4 operates correctly post-canonicalization.
- Builder pre-flight Step 1 stop-and-show on core.md framework version marker placement (Architect adjudication: Class B + Class C edge case; both preserve verbatim; README.md line 9 sole canonical-version-of-record); deliverable count revised 5 → 4; spec §6.1 claim 9 → N/A; spec §3.5 step 7 substantively no-op.
- Builder step-6 self-review caught 5 distinct defects in spec-asserted verification claims (claim 5 §-citation; claim 6 verification-command reframing; claim 12 verification-command reframing; claim 13 scope reframing; claim 4 line-count reframing) that the Architect §23.6 4-iteration sweep missed. Routing: 4 path-(a) (claims 5, 6, 12, 13 — pure-token-swap per §8.1.1.3 cost-class refinement); 1 acknowledged as recap-consistency observation (claim 4). (k.1) positive self-instantiation of bounded-continuation rule cost-class refinement extension at its second-instance application moment.
- Cycle defect tally projected pre-commit: ≥5 net distinct (Builder step-6 self-review surface) + Architect spec-authoring surface 8 (per spec §10 defect log) = ≥13 net distinct vs PR-15 cycle baseline 11 = ~1.18x. Slight scope-step-up consistent with this cycle's larger byte-exact content draft (~385 body lines) + 5-finding step-6 self-review surface. Actual cycle defect total finalized at hand-back per (i)/(i.5) discipline application empirical verdict.
- (i.5) sub-shape candidate two-data-point cross-cycle confirmation strengthens (Step 1 stop-and-show + Builder step-6 §-citation finding); preliminary canonical-refinement candidate per PMN-007 §1.3 candidate registry. Carried to PMN-008 cycle as substantive empirical material on (i.5) sub-shape canonicalization threshold.
- (r) candidate fifth-surface (Builder step-6 self-review) two-data-point cross-cycle confirmation strengthens (PR-15 cycle's claim 8 case-sensitivity + this cycle's 5-defect surface). Preliminary canonical-refinement candidate per PMN-007 §1.3 candidate registry. Carried to PMN-008 cycle as substantive empirical material on five-surface pipeline canonicalization threshold.
