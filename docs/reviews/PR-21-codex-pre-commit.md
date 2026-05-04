---
status: drafted
---

# PR-21 Codex desktop pre-commit review context

## Metadata

- PR ID: PR-21
- TASK ID: TASK-0019
- Branch: `feat/task-0019-linked-pr-fix-up-action`
- Base SHA: `809b9ca004bbb7fabb8145ede94529352703e75e` (squash-merge of PR-20 chore on main, 2026-05-03 23:32:33Z)
- Builder: Claude Code (Claude Opus 4.7, Windows 11 + Git Bash)
- Reviewer: Codex (GPT-5.5) — desktop, pre-commit, untracked working tree
- Architect (this PR's): Claude Opus 4.7 (Claude.ai Project)
- Owner: Bryce Murphy (`@bryce-murphy`)
- Framework version: AMAS v2.18 (dogfooded post-§18.4 substantive-reading bump from v2.17; third canonical-document version bump applying §18.4 criteria; first was PR-13 self-instantiation, second was PR-17 v2.16 → v2.17, this is third PR-21 v2.17 → v2.18)
- Severity taxonomy: Blocking / Major / Minor (three-level; per repo discipline; standing per PMN-004 §5 (a))
- Disciplines applied (PMN-004 §5 (a)-(f) + PMN-005 sub-rule (e.1) + PMN-006 (g)/(h)/(i) + PMN-006 §5.3 bounded-continuation rule generalized + PMN-006 §3.4 frontmatter-vs-body sub-clause + PMN-007 §2.4 cost-class refinement + PMN-007 §3.1 four-surface iterative-pre-flight + iterative-post-PR-review pattern + PMN-007 §9.1 (i) extended pre-authoring verification batch + PMN-007 §4 PMN-001 (k) mechanism-vs-discipline canonicalization + PMN-008 §3.2 five-surface review pipeline + PMN-008 §4.2 (i.5) convention-inference verification with PMN-file-shape sub-extension + PMN-008 §5.8 (h.4) three-endpoint Codex poll discipline OPERATIONAL this cycle pending core.md §8.1.1.1 canonical-text correction at separate cycle): severity taxonomy three-level (a); verification-command portability (b); no future-tense pre-commit claims (c); pre-commit cross-surface scope clarity (d); §23.6 prose-arithmetic decomposition (e) with sub-rule (e.1) cumulative-diff-stats re-derivation; section-citation correctness sweep (f); verification-artifact internal consistency (g); verification-command operational correctness (h) with sub-shapes (h.1)/(h.2)/(h.3)/(h.4); cross-document state verification (i) with sub-shapes (i.1)/(i.2)/(i.3)/(i.4)/(i.5); §23.6.2 iterative-to-fixed-point self-review; §8.1.1.3 bounded-continuation rule with cost-class refinement.
- Recursive-self-instantiation: PR-21 is the first cycle to ship a deterministic-enforcement Action ahead of the canonical Actions batch per ADR-003 D3 contingency-slot consumption; the Action this cycle ships automates the PMN-001 (k) chore-fix-up discipline that has run manually across 10 substantive-cycle instances through PR-19. Builder pre-flight surfaced 2 MAJOR convention-divergence findings (a-frontmatter + a-ADR-004 form) + 3 minor surface defects at step-1 stop-and-show; Architect adjudicated path-(a) on both MAJOR findings (Items 1 + 2) + path-(b) on minor wording defects (Item 5). Builder step-6 self-review at ADR-004 (j) sweep surfaced 2 §-citation correctness defects (anticipation-language attribution + slot-enumeration arithmetic) caught at authoring surface; both pure-token-swap path-(a) applied byte-exactly. (k.1) positive self-instantiation of bounded-continuation rule cost-class refinement at this cycle's third-instance application.

## Builder claims to verify

The Builder asserts the following at hand-off to Codex desktop pre-commit review. Each claim is verifiable from the working tree at pre-commit time (no future-tense claims per PMN-004 §5 (c)). PR-21 ships the linked-pr-fix-up GitHub Action (.github/workflows/.yml + .github/scripts/.py) + ADR-004 + TASK-0019 handoff + PR-21 review-context + README.md Class A v-bump on line 9.

1. **Tracked-file count on feature branch post-Builder-commit** = base + 5 new files. Pre-commit-verifiable per (c) discipline.
   - bash: `git ls-files | wc -l` returns base count + 5 new files (5 NEW: `.github/workflows/linked-pr-fix-up.yml` + `.github/scripts/linked-pr-fix-up.py` + `docs/handoffs/TASK-0019-linked-pr-fix-up-action.md` + `docs/reviews/PR-21-codex-pre-commit.md` + `docs/adr/ADR-004-pre-actions-batch-action-insertion.md`); README.md modified does not change count.
   - PowerShell: `(git ls-files | Measure-Object).Count` returns same.

2. **`.github/scripts/linked-pr-fix-up.py` byte-exact match against Architect-attached upload** at `C:/Users/BryceMurphy/Downloads/linked-pr-fix-up.py`. Verifiable at pre-commit:
   - bash: `git hash-object .github/scripts/linked-pr-fix-up.py` returns `b8c694fb9df1d45ae43cb086431341797cf2fd9f` AND `git hash-object /c/Users/BryceMurphy/Downloads/linked-pr-fix-up.py` returns same hash.
   - bash: `wc -l .github/scripts/linked-pr-fix-up.py` returns `158`.

3. **`.github/workflows/linked-pr-fix-up.yml` §E1 single-line substitution applied byte-exactly** modulo the recursion-guard line. Verifiable at pre-commit:
   - bash: pre-§E1 hash from upload `git hash-object /c/Users/BryceMurphy/Downloads/linked-pr-fix-up.yml` returns `b554854df1c888996cbe6b58f025b01c448498e5`; post-§E1 placed-file hash `git hash-object .github/workflows/linked-pr-fix-up.yml` returns `e5d787e18334361b48f27ce069ef3b39deecb5df`.
   - bash: `diff /c/Users/BryceMurphy/Downloads/linked-pr-fix-up.yml .github/workflows/linked-pr-fix-up.yml` returns single-line diff at line 35 only (ORIGINAL `if [[ "$SOURCE_BRANCH" == *"linked-pr-fix-up"* ]] || [[ "$SOURCE_BRANCH" == *"pmn-001-k"* ]]; then` → REPLACE `if [[ "$SOURCE_BRANCH" =~ ^chore/task-[0-9]+-(linked-pr-fix-up|pmn-001-k)$ ]]; then`); 10-space leading indent + bash conditional structure preserved.
   - bash: `wc -l .github/workflows/linked-pr-fix-up.yml` returns `144`.

4. **(a) §E1 recursion-guard regex correctness**: anchored regex `^chore/task-[0-9]+-(linked-pr-fix-up|pmn-001-k)$` correctly matches the auto-generated chore-fix-up branch shape (`chore/task-NNNN-linked-pr-fix-up`) AND the manual fallback shape (`chore/task-NNNN-pmn-001-k`), and DOES NOT match the parent feature branch shape (e.g., `feat/task-0019-linked-pr-fix-up-action`).
   - bash test: `echo "chore/task-0019-linked-pr-fix-up" | grep -E "^chore/task-[0-9]+-(linked-pr-fix-up|pmn-001-k)$"` returns the input (matches ✓).
   - bash test: `echo "chore/task-0019-pmn-001-k" | grep -E "^chore/task-[0-9]+-(linked-pr-fix-up|pmn-001-k)$"` returns the input (matches ✓).
   - bash test: `echo "feat/task-0019-linked-pr-fix-up-action" | grep -E "^chore/task-[0-9]+-(linked-pr-fix-up|pmn-001-k)$"` returns empty (does NOT match ✓; `feat/` ≠ `^chore/`; trailing `-action` breaks `$` anchor).

5. **(b) `apply_substitutions` idempotency**: re-running the Python script's `apply_substitutions` function on already-substituted content is a no-op (placeholder pattern absent → regex doesn't match → no edit applied; status target values not source-side → no re-edit).
   - Verification by code reading: `PLACEHOLDER_PATTERN` regex (`linked-pr-fix-up.py` lines 34-37) requires literal `(Builder fills with squash SHA post-merge per PMN-001 (k))` parenthetical → re-run on substituted form `linked_pr: PR-N (squash SHA <sha>)` doesn't match.
   - Verification by code reading: `STATUS_TRANSITIONS` dict (lines 41-44) maps `drafted → recorded` and `active → resolved`; the regex `^status: {old}\s*$` only matches source-side values → re-run on target-side values doesn't match.

6. **(c) `parse_frontmatter_bounds` handles markdown bodies with `---` horizontal-rule sequences correctly**: the function uses `matches[0].end()` and `matches[1].start()` from `FRONTMATTER_DELIM.finditer(content)`; subsequent body `---` HR sequences (matches 3+) are correctly ignored.
   - Verification by code reading: `linked-pr-fix-up.py` lines 51-62 — `parse_frontmatter_bounds` requires content to start with `---`, then uses only the first two `^---\s*$` matches as frontmatter bounds.
   - Optional bash test: `printf -- '---\nstatus: drafted\n---\n\nbody\n\n---\n\nmore\n' | python3 -c "import sys, re; from pathlib import Path; sys.path.insert(0, '.github/scripts'); ...` — exercise on synthetic input.

7. **(d) Workflow's minimum permissions: `contents: write` + `pull-requests: write`** is the minimum permission set required for operations performed (commit + push + `gh pr create`).
   - bash: `grep -A 2 "^permissions:" .github/workflows/linked-pr-fix-up.yml` returns `permissions: / contents: write / pull-requests: write` (3 lines verbatim per workflow lines 22-24).
   - Verification by operational decomposition: `Path.write_text` mutations (Python script) require `contents: write` ✓; `git add/commit/push` (chore-PR step) require `contents: write` ✓; `gh pr create` (chore-PR step) requires `pull-requests: write` ✓; no issue / release / actions-runs API calls beyond automatic event payload reading; no further scopes needed.
   - Per ADR-001 decision 14: `GITHUB_TOKEN` workflow permissions are read-only by default; the explicit `permissions:` block is canonical override pattern.

8. **README.md scope-leakage check**: only Class A v-bump on line 9 (TWO `v2.17` instances → `v2.18`) modified per Architect Item 4 step-2 stop-and-show + §18.4 substantive-reading minor criterion. NO Action-enumeration row added (deliverable-6 deferred per Architect Item 3). NO other surface modifications. Verifiable at pre-commit:
   - bash: `git diff --staged -- README.md` returns 2 lines changed (line 9 only — TWO substitutions on same line constitute 1-line-changed in unified diff).
   - bash: `grep -c "v2\.18" README.md` returns 2 (TWO Class A instances on line 9; previously TWO `v2.17` on same line).
   - bash: `grep -c "v2\.17" README.md` returns 0 (no remaining canonical-version-of-record references; if other v2.17 occurrences existed elsewhere as historical/Class B, would be preserved — verify per below).
   - bash: scope-leakage Action-row check: `grep -c "linked-pr-fix-up" README.md` returns 0 (no Action-enumeration row added; deliverable-6 deferred).

9. **core.md unmodified this cycle**: per Class B/C preserve-verbatim discipline at step-1 stop-and-show + Architect Item 4. Verifiable at pre-commit:
   - bash: `git diff main -- core.md` returns empty.
   - bash: `git diff --staged -- core.md` returns empty.
   - bash: `grep -c "v2\.16" core.md` returns 2 (lines ~223 + ~234; Class B + Class C preserved verbatim per PR-17 cycle Architect adjudication).
   - Any modification to core.md is a Blocking finding (scope-leakage).

10. **CLAUDE.md unmodified this cycle** (operating-framework reference Class B-like; preserved until v3.0 self-adoption per ADR-001 decision 8 amended). Verifiable at pre-commit:
    - bash: `git diff main -- CLAUDE.md` returns empty.
    - bash: `git diff --staged -- CLAUDE.md` returns empty.
    - bash: `grep -c "v2\.14\.1" CLAUDE.md` returns ≥1 (preserved at original bootstrap value).

11. **(e) ADR-004 §-citations all resolve to canonical sources per (j) all-instances grep sweep**: enumeration via `grep -nE "(core\.md|github-reference\.md|ADR-00[0-9]+|PMN-00[0-9]+)" docs/adr/ADR-004-*.md` and each citation manually verified against canonical source. **ADR-004 section structure matches ADR-001 / ADR-003 canonical form** (## Status / ## Context / ## Decision / ## Alternatives considered / ## Consequences / ## Evidence / references) per Architect adjudication of step-1 stop-and-show (Item 2). Verifiable at pre-commit:
    - bash: `grep -nE "(core\.md|github-reference\.md|ADR-00[0-9]+|PMN-00[0-9]+)" docs/adr/ADR-004-pre-actions-batch-action-insertion.md` returns the (j) sweep enumeration. Each cited §-anchor is verifiable: ADR-001 decisions 9 / 11 / 14 (verified vs `docs/adr/ADR-001-initial-repo-setup.md` per PR-17 review-context §C.1 enumeration); ADR-002 D3 anticipation language (verified vs `docs/adr/ADR-002-task-reservation-amendment.md`); ADR-003 D2 + D3 (verified vs `docs/adr/ADR-003-full-package-pr-plan.md`); core.md §18.3 + §8.1.1.3 + §18.4 (verified vs core.md HEAD §-header set per PR-17 review-context's 21-§ verified set; §8.1.1.3 / §18.3 / §18.4 all present in HEAD).
    - bash: `grep -cE "^## " docs/adr/ADR-004-pre-actions-batch-action-insertion.md` returns 6 (## Status / ## Context / ## Decision / ## Alternatives considered / ## Consequences / ## Evidence / references — note the slash inside "Evidence / references" produces ONE `## ` heading).
    - bash: section-ordering check: `grep -nE "^## " docs/adr/ADR-004-pre-actions-batch-action-insertion.md` returns line numbers in canonical order (Status before Context before Decision before Alternatives before Consequences before Evidence/references).
    - **Builder step-6 self-review fix-up applied** (caught at ADR-004 (j) sweep at authoring surface): line 13 anticipation-language attribution corrected from "ADR-003 Decision 3" to "ADR-002 Decision 3 ... preserved by reference at ADR-003 Status field" (verified vs ADR-002 D3 + ADR-003 Status field text). Pure-token-swap path-(a) applied; (j) full-pattern sweep on contingency-slot enumeration revealed arithmetic inconsistency in Consequences point 3 (count "5 → 4" + enumerated "Six remaining slots") → trimmed to count claim only per spec accounting; specific TASK-slot enumeration deferred to Architect cycle-close ledger reconciliation.

12. **(f) Class A canonical-version-of-record v-bump applied per step-1 stop-and-show direction (Architect Item 4)**: README.md line 9 TWO `v2.17` instances → `v2.18`. Verifiable at pre-commit:
    - bash: `sed -n '9p' README.md` returns the post-bump line containing TWO `v2.18` instances and ZERO `v2.17` instances (Class A canonical-version-of-record).
    - bash: `grep -c "^framework_version_dogfooded: AMAS v2\.18$" docs/handoffs/TASK-0019-linked-pr-fix-up-action.md` returns 1 (Class A-adjacent per-cycle dogfooding declaration in handoff frontmatter).
    - bash: `grep -c "AMAS v2\.18" docs/reviews/PR-21-codex-pre-commit.md` returns ≥1 (Class A-adjacent in PR-21 review-context Metadata).
    - bash: Class B/C preservation check: `grep -c "v2\.16" core.md` returns 2 (preserved verbatim); `grep -c "v2\.14\.1" core.md` returns ≥1 (preserved verbatim per Class B); `grep -c "v2\.14\.1" CLAUDE.md` returns ≥1 (preserved verbatim per Class B-like operating-framework reference).

13. **TASK-0019 handoff frontmatter convention** = PMN-007 HEAD canonical ~13 fields per Architect Item 1 step-1 stop-and-show adjudication (path-(a) on a-frontmatter MAJOR finding):
    - bash: `head -13 docs/handoffs/TASK-0019-linked-pr-fix-up-action.md | grep -cE "^(task_id|title|pr|branch|linked_predecessor|linked_successor|linked_pr|framework_version_dogfooded|production_target|spec_source|date_authored|status):"` returns 12 (12 fields named; matches PMN-007 HEAD canonical per TASK-0017 + TASK-0018 priors).
    - bash: `grep -c "^task_id: TASK-0019$" docs/handoffs/TASK-0019-linked-pr-fix-up-action.md` returns 1.
    - bash: `grep -c "^pr: PR-21$" docs/handoffs/TASK-0019-linked-pr-fix-up-action.md` returns 1.
    - bash: `grep -c "^branch: feat/task-0019-linked-pr-fix-up-action$" docs/handoffs/TASK-0019-linked-pr-fix-up-action.md` returns 1.
    - bash: `grep -c "^status: active$" docs/handoffs/TASK-0019-linked-pr-fix-up-action.md` returns 1 (post-merge transition to `resolved` is Action / chore-fix-up cycle responsibility; (e.1) Action substitution targets `active → resolved`).
    - bash: `grep -c "^linked_pr: PR-21" docs/handoffs/TASK-0019-linked-pr-fix-up-action.md` returns 1 (placeholder pattern preserved exactly per Architect Item 1 placeholder-substitution timing table).

14. **(g) TASK-0019 handoff structural-headings count + section ordering matches TASK-0017 / TASK-0018 priors per PMN-007 HEAD canonical frontmatter convention** (Architect Item 7 wording extension): per step-1 stop-and-show Architect adjudication, spec frontmatter expanded from 2 fields to canonical ~13 fields; spec §5 placeholder-substitution table covers post-merge-substituted `linked_pr` + `status` only; remaining fields are Builder-fill-now from pre-flight data. Verification target is canonical priors-aligned form as written, not spec's sub-canonical 2-field form. Verifiable at pre-commit:
    - bash: `grep -cE "^## " docs/handoffs/TASK-0019-linked-pr-fix-up-action.md` returns 16 top-level §-sections. Decomposition: prior-aligned core (10 sections) `## Metadata` + `## Objective` + `## Last completed step` + `## Current state` + `## Decisions made` + `## Assumptions` + `## Risks` + `## Blocking questions` + `## Validation run` + `## Exact next step` PLUS spec-content additions (6 sections) `## §4. ADR-004 content prescription` + `## §5. Placeholder-substitution discipline (PMN-003 (d))` + `## §6. Reassessment / expiry` + `## §7. Post-PR Codex review state` + `## §8. Sign-off` + `## §9. Session log archive`. The first 10 align with TASK-0017 substantive-cycle prior structure; the 6 §-suffixed additions are substantive-cycle-shape evolution per Architect Item 6 (spec-content-shape requirements for this cycle's scope: ADR-004 embed + placeholder-substitution table + post-PR-Codex absorption + Architect sign-off + AI Session Log archive). 10 + 6 = 16 ✓.
    - bash: section-ordering check: `grep -nE "^## " docs/handoffs/TASK-0019-linked-pr-fix-up-action.md` returns line numbers in canonical order matching spec §-sequence.

15. **Cumulative-diff-stats consistency per (e.1) sub-rule**: Σ per-file insertions = total insertions in `git diff --staged --stat`. Verifiable at pre-commit (post-staging, pre-commit):
    - bash: `git diff --staged --stat` shows insertions / deletions across staged files; total insertions field = sum of per-file insertions field.
    - bash: `git diff --staged --shortstat` returns aggregate `<N> files changed, <X> insertions(+), <Y> deletions(-)`.
    - Expected: 6 files (5 new + 1 modified README.md). Insertion count fills at step 10 pre-commit stop-and-show per (e.1) sub-rule re-derivation.
    - (e.1) cumulative-diff-stats re-derivation per PMN-005 §4.4: if any path-(a) revision occurs during Codex pre-commit absorption, re-derive cumulative diff stats and re-verify all dependent claims.

## Reviewer focus (Codex desktop)

For each Builder claim above, verify the verification command produces the asserted result. Specific focus areas (only pre-commit-existing surfaces enumerated per PMN-004 §5 (d)):

- **Ingestion-file byte-exact compliance against upload** (claims 2-3): `.github/scripts/linked-pr-fix-up.py` is verbatim from `C:/Users/BryceMurphy/Downloads/linked-pr-fix-up.py` (no modifications); `.github/workflows/linked-pr-fix-up.yml` is verbatim from `C:/Users/BryceMurphy/Downloads/linked-pr-fix-up.yml` modulo the §E1 single-line substitution at line 35. Any byte-divergence beyond that line is a Blocking finding regardless of substantive equivalence.
- **§E1 recursion-guard regex correctness** (claim 4): the anchored regex correctly matches the two recursive cases AND does NOT match the parent feature branch shape. Empirical regex tests via `grep -E` on synthetic branch-name strings.
- **Python script logic correctness** (claims 5-6): code-reading verification of `apply_substitutions` idempotency and `parse_frontmatter_bounds` correctness against body `---` HR sequences.
- **Workflow permissions minimum** (claim 7): `contents: write + pull-requests: write` is exactly the minimum scope for the Action's operations.
- **README.md scope** (claim 8): only Class A v-bump on line 9; NO Action-enumeration row addition; NO other surface modifications. Any modification outside Class A v-bump scope is a Blocking finding (scope-leakage).
- **core.md + CLAUDE.md unmodified** (claims 9-10): Class B/C preservation discipline; any modification is a Blocking finding (scope-leakage).
- **ADR-004 §-citation correctness + canonical form** (claim 11): each §-citation resolves to actual heading in cited document; section structure matches ADR-001 / ADR-003 canonical form per Architect Item 2 adjudication. Any dangling citation is a Blocking finding; any section-form divergence is a Major finding.
- **Class A v-bump applied** (claim 12): README.md line 9 TWO `v2.17` → `v2.18`; handoff frontmatter `framework_version_dogfooded: AMAS v2.18`; PR-21 review-context Metadata `Framework version: AMAS v2.18`. Class B/C preservation across core.md + CLAUDE.md.
- **Handoff frontmatter convention** (claim 13): PMN-007 HEAD canonical ~13 fields per Architect Item 1; verifiable via field enumeration grep + spot-checks.
- **Handoff structural-headings + section ordering** (claim 14): matches TASK-0017 / TASK-0018 priors per PMN-007 HEAD canonical convention; verification target is canonical priors-aligned form, not spec's sub-canonical 2-field form per Architect Item 7.
- **Cumulative-diff-stats re-derivation** (claim 15): per-file insertion/deletion counts in handoff Validation run section must match `git diff --staged --stat` exactly. No approximate counts; no `~`-prefixed numbers.

- **(g) Verification-artifact internal consistency** (canonicalized in PMN-006 §3.1): for each Builder claim, verify (g.1) timing-correctness across surfaces and (g.2) within-block label-vs-example consistency.
- **(h) Verification-command operational correctness** (canonicalized in PMN-006 §3.2 with sub-shapes (h.1)/(h.2)/(h.3)/(h.4)): claim verification commands as authored should produce asserted results. (h.4) three-endpoint Codex poll discipline applies at PR-21 post-PR absorption regardless of core.md §8.1.1.1 canonical-text current state per PMN-008 §5.8 OPERATIONAL framing.
- **(i) Cross-document state verification** (canonicalized in PMN-006 §7): for each Builder claim asserting a fact about another file's content, verify the assertion against actual file state via supplied `grep` / `git hash-object` / file-read commands. (i.5) PMN-file-shape sub-extension applies at handoff frontmatter convention check (claim 13).

- **Phantom-action claim verification** (per §8.1.1.2 / PMN-005 §2.5 / PMN-007 §9.2 (m)): each Builder claim's verification command is itself directly verifiable. Codex runs the command; reports result verbatim; flags any divergence from the Builder's asserted result.

- **No future-tense claims at pre-commit time** (PMN-004 §5 (c)): Sweep all 15 Builder claims for "will be" / "shall" / "to be filled" language. Acceptable: "filled at step 10 pre-commit stop-and-show" referencing the cumulative-diff-stats Evidence subsection (claim 15) per discipline (c).

- **§8.1.1.3 cost-class refinement self-application**: verify any path-(β) routing decision Codex applies in this review-context against the genuinely-asymptotic-vs-pure-token-swap distinction. Builder step-6 self-review surfaced 2 path-(a) candidates at ADR-004 (j) sweep (anticipation-language attribution + slot-enumeration arithmetic), both routed pure-token-swap class — exemplary positive self-instantiation per (k.1) discipline.

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

- **Blocking** — finding that prevents merge until addressed (e.g., ingestion-file byte-divergence beyond the explicit §E1 substitution; §-citation slip producing dangling reference; cumulative-diff-stats drift on pre-commit-existing surface; future-tense pre-commit claim without verifiable counterpart; (g)/(h) defect within this review-context's own claim blocks; (i) cross-document state assertion mismatched against actual repo state; scope-leakage outside 6-file scope; modification to core.md or CLAUDE.md). Cannot ship without revision.
- **Major** — finding that should be addressed pre-merge but does not block merge in the absence of address. Default disposition path (a) revise.
- **Minor** — finding noted for record but not requiring address. Default disposition path (β) record-and-proceed per §8.1.1.3 bounded-continuation rule with cost-class refinement.

```
Action: For each enumerated claim 1-15, verify the verification command produces the asserted result. Report any divergence as a Blocking finding regardless of magnitude. Report verification commands' outputs verbatim.

Action: For ingestion-file byte-exact claims 2-3, compute git hash-object for the placed files AND for the upload sources at C:/Users/BryceMurphy/Downloads/. Verify (i) .py file hashes match exactly (verbatim copy); (ii) .yml file post-§E1 hash differs from upload pre-§E1 hash by exactly the single-line substitution at line 35. `diff /c/Users/BryceMurphy/Downloads/linked-pr-fix-up.yml .github/workflows/linked-pr-fix-up.yml` should show exactly one line-pair divergence at line 35.

Action: Verify the §E1 anchored regex against three branch-shape inputs: `chore/task-0019-linked-pr-fix-up` (must match), `chore/task-0019-pmn-001-k` (must match), `feat/task-0019-linked-pr-fix-up-action` (must NOT match). Use `echo "<input>" | grep -E "^chore/task-[0-9]+-(linked-pr-fix-up|pmn-001-k)$"` for each.

Action: Code-read .github/scripts/linked-pr-fix-up.py for `apply_substitutions` idempotency (claim 5) and `parse_frontmatter_bounds` correctness against body `---` HR sequences (claim 6). Report any defect as Blocking.

Action: Verify .github/workflows/linked-pr-fix-up.yml `permissions:` block (claim 7). Confirm exactly `contents: write` + `pull-requests: write` (no more, no less). Verify the operations performed by the workflow against the declared permissions: read events, write commits, write PR.

Action: Sweep README.md for v-marker state (claim 12). Confirm line 9 has TWO `v2.18` instances and ZERO `v2.17` instances. Confirm no other lines in README.md modified beyond line 9. Confirm no Action-enumeration row added (search for `linked-pr-fix-up` in README.md returns 0).

Action: Verify core.md + CLAUDE.md unmodified (claims 9-10). `git diff main -- core.md CLAUDE.md` returns empty. `git diff --staged -- core.md CLAUDE.md` returns empty.

Action: Sweep ADR-004 + TASK-0019 handoff + PR-21 review-context for §-citations matching the pattern `(core\.md|github-reference\.md|ADR-00[0-9]+|PMN-00[0-9]+|TASK-[0-9]+|PR-[0-9]+)`. For each citation, verify the cited §-number resolves to an actual heading in the cited document or the explicit forward-reference set. Report all dangling references as Blocking findings (claim 11 (j) sweep).

Action: Verify ADR-004 section structure matches ADR-001 / ADR-003 canonical form (Status / Context / Decision / Alternatives considered / Consequences / Evidence / references). Per Architect Item 2 adjudication of step-1 stop-and-show, ADR-004 conforms to canonical priors NOT to spec §4 prescription; spec §4 Rationale section folds into Decision body, References renames to Evidence / references, Alternatives-before-Consequences ordering preserved.

Action: Verify TASK-0019 handoff frontmatter convention against PMN-007 HEAD canonical (claim 13). Per Architect Item 1 adjudication of step-1 stop-and-show, handoff frontmatter expanded from spec's 2-field form to canonical ~13-field form; verification target is canonical priors-aligned form, not spec's sub-canonical 2-field form. Sample TASK-0017 + TASK-0018 priors for canonical reference.

Action: Run cumulative-diff-stats re-derivation per (e.1) (claim 15). Compare any Evidence section in TASK-0019 handoff against `git diff --staged --stat` output. Any discrepancy is a Blocking finding. Any `~`-prefixed number is a Blocking finding.

Action: Verify scope-leakage on the 6-file scope. Only .github/workflows/linked-pr-fix-up.yml (new), .github/scripts/linked-pr-fix-up.py (new), docs/handoffs/TASK-0019-linked-pr-fix-up-action.md (new), docs/reviews/PR-21-codex-pre-commit.md (new), docs/adr/ADR-004-pre-actions-batch-action-insertion.md (new), README.md (modified — Class A v-bump only) are in scope. Any modification to other files (core.md, CLAUDE.md, AGENTS.md, github-reference.md, templates, prompts, ADRs 1-3, other handoffs, other PMNs) is a Blocking finding.

Action: Apply (g)/(h)/(i) sweep to this review-context's own claim blocks. Each claim's verification command must (g.1) declare timing matching what it proves; (g.2) match label-vs-example; (h.2) prove what's claimed; (i.5) verify cross-document state assertions against actual file state. Any sub-shape failure is a Blocking finding.
```

## Adjudication / fix-up

**Step 1 stop-and-show — convention-divergence findings + minor wording defects** (resolved by Architect adjudication 2026-05-03):

Builder pre-flight surfaced:
- (a-frontmatter) MAJOR — spec frontmatter (2 fields) vs PMN-007 HEAD canonical (~13 fields) — Architect Item 1 path-(a): expand to canonical ~13 fields; spec §5 substitution timing table extends to cover added fields; Action's substitution targets unchanged (linked_pr + status only).
- (a-ADR-004 form) MAJOR — spec §4 ADR-004 prescription (Rationale separate; reordered; renamed References) vs canonical ADR-001/003 form — Architect Item 2 path-(a): align ADR-004 to canonical priors (Status / Context / Decision / Alternatives considered / Consequences / Evidence / references); Rationale folds into Decision; References renames; Alternatives-before-Consequences order preserved per ADR-001 / ADR-003 majority + ADR-002 one-off authoring artifact.
- (c) deliverable-6 — Architect Item 3 DEFER (5 deliverables for substantive content; README modification scope = Class A v-bump only per Item 4).
- (d) v2.17 → v2.18 minor bump — Architect Item 4 confirmed; Class A markers enumerated; Class B/C preserved.
- (e.2) spec §3 step 4 line 145 wording inconsistency ("3-line modification" vs single-line) — Architect Item 5 cycle-close item; Builder behavior unchanged; recorded in Validation run.
- (e.3) spec §3 step 1 line 112 + step 4 (b) gap — Architect Item 5 cycle-close item; Builder behavior unchanged; both `.github/workflows/` and `.github/scripts/` directories created at step 4.

**Step 6 ADR-004 (j) sweep at authoring surface** (Builder step-6 self-review at ADR-004 §-citation sweep; PMN-008 §3.1 fifth-surface (r) candidate operating at canonical step-6 surface):

1. **ADR-004 line 13 anticipation-language attribution defect**: original draft attributed "subsequent ADR amendments will document such extensions following the same pattern" to ADR-003 D3; canonical attribution is **ADR-002 D3** (verified vs `docs/adr/ADR-002-task-reservation-amendment.md` D3 verbatim text). ADR-003 preserves the pattern by reference at its Status field ("consistent with ADR-002 Decision 3 anticipation pattern"), but the anticipation language itself is ADR-002 D3. Class: §-citation correctness (i.5) sub-shape. Cost-class: pure-token-swap (paragraph-level wording correction). Routing: path-(a) per §8.1.1.3 cost-class refinement. Applied byte-exactly.

2. **ADR-004 Consequences point 3 arithmetic inconsistency**: original draft claimed contingency slots "5 → 4 remaining" then enumerated "Six remaining contingency slots (TASK-0020/21/22/24/25/26)" — count claim (4) inconsistent with enumeration count (6). Cause: contingency-slot-accounting carried via cycle handoffs not centrally summarized; TASK-0018 frontmatter records "3 remaining post-PMN-008 — TASK-0025 through TASK-0027 unconsumed" while spec accounting frames "5 → 4". Without centralized ledger, specific TASK-slot enumeration is unverifiable from this surface. Class: prose-arithmetic decomposition defect per §23.6.1; (j)-extension cumulative-diff-stats re-derivation discipline applied. Cost-class: pure-token-swap (drop unverifiable enumeration; preserve count claim per spec). Routing: path-(a). Applied byte-exactly. **Surfacing as step-10 stop-and-show item for Architect**: contingency-slot-accounting reconciliation between TASK-0018 frontmatter ("3 remaining") and TASK-0019 spec ("5 → 4") is a real divergence that warrants Architect cycle-close clarification.

**(j) full-pattern sweep at Builder step-6 self-review** (per spec §3 step 9 + PMN-008 §3.1 (r) discipline): grep `(core\.md|github-reference\.md|ADR-00[0-9]+|PMN-00[0-9]+|TASK-[0-9]+|PR-[0-9]+)` across all five new files + README.md modified; each citation manually verified against canonical source; **2 fix-up applications recorded above** (anticipation-language + slot-enumeration); zero remaining (j)-sweep residuals at fix-up convergence per iteration-2 zero-defect verification.

**Same-class (j) propagation residual sweep result**: 2 ADR-004 (j) sweep findings + 0 propagation residuals to TASK-0019 handoff / PR-21 review-context. The handoff + review-context were authored after ADR-004 with both fixes already applied; no propagation residuals introduced.

**(r) candidate fifth-surface empirical strength**: Builder step-6 self-review at ADR-004 (j) sweep caught 2 distinct §-citation correctness defects in spec-prescribed §-citation framing that the Architect Phase 1 scoping + spec authoring missed. Third cross-cycle confirmation (PR-15 step-6 → PR-17 step-6 → PR-19 step-6 → this cycle's step-6); strong empirical evidence for (r) canonical-refinement candidate per PMN-008 §3.1.

[Codex pre-commit findings absorbed below; awaiting any subsequent passes if applicable.]

[Codex post-PR review absorbed below post-`@codex review` invocation per ADR-001 decision 11; three-endpoint poll per PMN-008 §5.8 (h.4) OPERATIONAL discipline pending core.md §8.1.1.1 canonical-text correction.]

## Builder hand-back attestation

After Codex desktop pre-commit review completes, Builder reports:
- Codex review outcome (per the summary structure above)
- Path (a) revisions made, if any
- Path (β) acceptances recorded, if any per §8.1.1.3 bounded-continuation rule with cost-class refinement
- §23.6 recapitulation-consistency re-check result after any path (a) revisions
- Section-citation correctness sweep result after any path (a) revisions, applied iteratively to convergence per PMN-005 §4.3 / §23.6.2
- Cumulative-diff-stats Evidence subsection populated with landed exact counts from `git diff --staged --stat` immediately before commit, per PMN-005 §4.4 sub-rule (e.1)
- (g)/(h)/(i) self-application sweep result on this review-context's own claim blocks; iteration count to convergence
- Cost-class routing adjudication (per PMN-007 §2.4 / §8.1.1.3 refinement): for any path-(β) routing applied during pre-commit absorption, document the genuinely-asymptotic justification explicitly — pure-token-swap cascades terminate at one-iteration fixed-point and route path-(a) by default
- Three-endpoint Codex post-PR poll evidence per PMN-008 §5.8 (h.4) OPERATIONAL discipline: `pulls/{pr}/reviews` + `issues/{pr}/comments` + `pulls/{pr}/comments` outputs verbatim with empty/non-empty determinations + 5-10 minute settling-period evidence

## Post-PR / post-merge claims (segregated per (c)/(d) discipline)

Post-PR-merge claims that cannot be verified at pre-commit:

- PR-21 squash SHA exists at expected location (verified post-merge by Builder + Architect five-point check).
- linked_pr field substituted in TASK-0019 handoff frontmatter post-merge: by linked-pr-fix-up Action's first auto-fire (PR-22 = the chore-fix-up the Action creates) OR by manual chore-fix-up cycle if Action fails first auto-fire (per spec §Risks line 75).
- TASK-0019 handoff status flipped from `active` → `resolved` post-merge (Action substitution target).
- PR-21 review-context status flipped from `drafted` → `recorded` post-merge (Action substitution target).
- ADR-004 has no `status` field requiring substitution (Status section text-only).
- README.md framework_version_dogfooded reconciles to v2.18 across all canonical-version-of-record placements post-merge (line 9 only; core.md + CLAUDE.md preserve verbatim per Class B/C).
- M-A7 advances to eighth empirical instance per enumeration `PR-9 + PR-10 + PR-11 + PR-13 + PR-15 + PR-17 + PR-19 + PR-21`; Architect performs merge-commit-body amendment post-merge per core.md §18.3.

## Notes

- Codex desktop reviews the untracked working tree before commit (read-only git inspection only).
- Post-PR `@codex review` is owner-invoked per ADR-001 decision 11; this pre-commit review is the substantive verification before commit.
- PR-21 is a substantive cycle: ships the linked-pr-fix-up Action ahead of canonical Actions batch per ADR-003 D3 contingency-slot consumption + ADR-004 documents the architectural insertion decision. Recursive-self-instantiation: this cycle is the third-instance application of canonical text §18.4 substantive-reading minor-bump criterion (PR-13 first; PR-17 second; this cycle third).
- Builder pre-flight Step 1 stop-and-show on convention-divergence findings (a-frontmatter + a-ADR-004 form MAJOR; e.2/e.3 minor) + deliverable-6 + v-bump confirmation; Architect Items 1-7 adjudicated path-(a) on MAJOR findings + path-(b) cycle-close on minor wording defects.
- Builder step-6 self-review at ADR-004 (j) sweep caught 2 distinct §-citation defects (anticipation-language attribution + slot-enumeration arithmetic) at canonical step-6 authoring surface; both pure-token-swap path-(a) applied byte-exactly. Third-cross-cycle confirmation strengthening (r) canonical-refinement candidate per PMN-008 §3.1.
- (h.4) three-endpoint Codex post-PR poll discipline OPERATIONAL this cycle pending core.md §8.1.1.1 canonical-text correction at separate cycle per PMN-008 §5.8 path-(β) framing.
- Cycle defect tally projected at pre-commit: ≥5 net distinct (Builder pre-flight surface 5 — 2 MAJOR convention divergence + 3 minor surface defects) + 2 Builder step-6 ADR-004 (j) sweep (anticipation-language + slot-enumeration) = ≥7 net distinct pre-Codex. Actual cycle defect total finalized at hand-back per (i)/(i.5) discipline application empirical verdict.
