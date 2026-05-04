---
status: drafted
---

# PR-23 Codex desktop pre-commit review context

## Metadata

- PR ID: PR-23
- TASK ID: TASK-0020
- Branch: `feat/task-0020-linked-pr-fix-up-defect-fix`
- Base SHA: `42132c296ee64638ba30aab16ceb0d20a9fe7f8d` (squash-merge of PR-22 chore on main, 2026-05-04 15:44:04Z)
- Builder: Claude Code (Claude Opus 4.7, Windows 11 + Git Bash)
- Reviewer: Codex (GPT-5.5) — desktop, pre-commit, untracked working tree
- Architect (this PR's): Claude Opus 4.7 (Claude.ai Project)
- Owner: Bryce Murphy (`@bryce-murphy`)
- Framework version: AMAS v2.18.1 (dogfooded post-§18.4 substantive-reading patch bump from v2.18; first patch-tier version bump applying §18.4 patch criterion — correctness fix to existing Action code + operational-dependency documentation; no new framework content)
- Severity taxonomy: Blocking / Major / Minor (three-level; per repo discipline; standing per PMN-004 §5 (a))
- Disciplines applied (PMN-004 §5 (a)-(f) + PMN-005 sub-rule (e.1) + PMN-006 (g)/(h)/(i) + PMN-006 §5.3 bounded-continuation rule generalized + PMN-006 §3.4 frontmatter-vs-body sub-clause + PMN-007 §2.4 cost-class refinement + PMN-007 §3.1 four-surface iterative-pre-flight + iterative-post-PR-review pattern + PMN-007 §9.1 (i) extended pre-authoring verification batch + PMN-007 §4 PMN-001 (k) mechanism-vs-discipline canonicalization + PMN-008 §3.2 five-surface review pipeline + PMN-008 §4.2 (i.5) convention-inference verification with PMN-file-shape sub-extension + PMN-008 §5.8 (h.4) three-endpoint Codex poll discipline OPERATIONAL this cycle pending core.md §8.1.1.1 canonical-text correction at separate cycle): severity taxonomy three-level (a); verification-command portability (b); no future-tense pre-commit claims (c); pre-commit cross-surface scope clarity (d); §23.6 prose-arithmetic decomposition (e) with sub-rule (e.1) cumulative-diff-stats re-derivation; section-citation correctness sweep (f); verification-artifact internal consistency (g); verification-command operational correctness (h) with sub-shapes (h.1)/(h.2)/(h.3)/(h.4); cross-document state verification (i) with sub-shapes (i.1)/(i.2)/(i.3)/(i.4)/(i.5); §23.6.2 iterative-to-fixed-point self-review; §8.1.1.3 bounded-continuation rule with cost-class refinement.
- Defect-fix-cycle context: PR-23 is the first defect-fix cycle for the linked-pr-fix-up Action shipped at PR-21. Two defects empirically validated at PR-22 first-auto-fire event: (1) regex newline-consumption corrupting frontmatter when status field is the last fm_body line; (2) workflow `gh pr create` step blocked by repo-setting "Allow GitHub Actions to create and approve pull requests" being OFF. PR-23 fixes defect 2 at code level (pure-token-swap regex correction) and defect 1 at documentation level (ADR-004 §Consequences point 8 amendment per Architect path-α adjudication). Builder pre-flight surfaced 2 (i.5) convention-divergence findings against spec body at step-1 stop-and-show (lines 36+93 → 35+93; existing §Consequences point count 6 → 7, new point 7 → 8); both adjudicated path-(a) by owner.

## Builder claims to verify

The Builder asserts the following at hand-off to Codex desktop pre-commit review. Each claim is verifiable from the working tree at pre-commit time (no future-tense claims per PMN-004 §5 (c)). PR-23 ships the linked-pr-fix-up Action defect-fix (regex newline-consumption fix at lines 35 + 93) + ADR-004 §Consequences point 8 amendment (path-α default wording) + TASK-0020 handoff + PR-23 review-context + README.md Class A v-bump v2.18 → v2.18.1.

1. **Working-tree state: 2 new files + 3 modified files**. Verifiable at pre-commit per (c) + (h.2) discipline (working-tree-aware forms; no future-tense commit-time semantics).
   - bash (pre-commit, untracked-aware): `git status --porcelain | grep -c "^??"` returns `2` (2 NEW: `docs/handoffs/TASK-0020-linked-pr-fix-up-defect-fix.md` + `docs/reviews/PR-23-codex-pre-commit.md`).
   - bash (pre-commit, modified-aware): `git status --porcelain | grep -c "^ M"` returns `3` (3 modified: `.github/scripts/linked-pr-fix-up.py`, `docs/adr/ADR-004-pre-actions-batch-action-insertion.md`, `README.md`).
   - bash (pre-commit baseline): `git ls-files | wc -l` returns `106` (untracked files not counted). Post-stage (after `git add` of the 2 new files): `git ls-files | wc -l` returns `108`.

2. **Defect 2 regex fix at `.github/scripts/linked-pr-fix-up.py` lines 35 + 93 — pure-token-swap `\s*$` → `[ \t]*$` applied byte-exactly** modulo those two locations.
   - bash: pre-fix hash from base SHA `42132c2`: `git show 42132c2:.github/scripts/linked-pr-fix-up.py | git hash-object --stdin` returns `b8c694fb9df1d45ae43cb086431341797cf2fd9f`; post-fix placed-file hash `git hash-object .github/scripts/linked-pr-fix-up.py` returns `500779a2f4054170f09e83e9c0db26e8090daa8e`.
   - bash (working-tree-vs-main; works at pre-commit AND clean post-edits): `git diff origin/main -- .github/scripts/linked-pr-fix-up.py` shows exactly 2 line replacements at lines 35 + 93 (both `\s*$` → `[ \t]*$`); no other line in the file modified.
   - bash: `wc -l .github/scripts/linked-pr-fix-up.py` returns `158` (unchanged from pre-fix line count; both substitutions are token-swap, no line addition/deletion).

3. **Defect 2 regex fix correctness — `[ \t]*$` matches horizontal whitespace only without consuming line-terminator `\n`**. Verifiable at pre-commit by Python interpreter (Codex desktop expected to have python; local Builder environment lacks it):
   ```bash
   python3 -c "
   import re
   test = '---\nstatus: active\n---\n'
   fm = test[3:test.rindex('---')]
   pat = re.compile(r'^status: active[ \t]*\$', re.MULTILINE)
   result = test[:3] + pat.sub('status: resolved', fm) + test[test.rindex('---'):]
   print(repr(result))
   "
   ```
   Expected output: `'---\nstatus: resolved\n---\n'` (trailing newline between `resolved` and closing `---` preserved).
   Architect-side empirical verification performed at TASK-0020 spec authoring per spec §"Last completed step" item 7. Local Builder environment lacks python interpreter; by-inspection verification: `[ \t]*` is the standard Python regex character-class for `[space, tab]` matching, and `$` in `re.MULTILINE` mode anchors to end-of-line position before `\n`, not the `\n` itself. The replacement preserves all newlines.

4. **Defect 2 fix idempotency preserved**: re-running `apply_substitutions` on already-substituted content is a no-op. Same idempotency property as pre-fix.
   - Verification by code reading: `PLACEHOLDER_PATTERN` (post-fix line 35) requires literal `(Builder fills with squash SHA post-merge per PMN-001 (k))` parenthetical → re-run on substituted form `linked_pr: PR-N (squash SHA <sha>)` doesn't match.
   - Verification by code reading: `STATUS_TRANSITIONS` dict still maps `drafted → recorded` and `active → resolved`; the regex `^status: {old}[ \t]*$` only matches source-side values → re-run on target-side values doesn't match.

5. **Edge case verification — file ending exactly at closing `---` with no trailing file-level newline**: substitution preserves the newline between `status: <new>` and closing `---`. Verifiable by Python interpreter (Codex desktop):
   ```bash
   python3 -c "
   import re
   test = '---\nstatus: drafted\n---'  # no trailing \n
   fm = test[3:test.rindex('---')]
   pat = re.compile(r'^status: drafted[ \t]*\$', re.MULTILINE)
   result = test[:3] + pat.sub('status: recorded', fm) + test[test.rindex('---'):]
   print(repr(result))
   "
   ```
   Expected output: `'---\nstatus: recorded\n---'` (newline between `recorded` and closing `---` preserved; no trailing file-level newline added by substitution).

6. **ADR-004 amendment additive — new §Consequences point 8 added; existing points 1-7 retained (with §Context line 15 wording revised per Codex pre-commit Major 1 path-(a)); Status field updated per ADR-002 amendment-pattern precedent**.
   - bash (working-tree-vs-main; works at pre-commit AND clean post-edits): `git diff origin/main -- docs/adr/ADR-004-pre-actions-batch-action-insertion.md` shows: (a) Status line substitution ("Accepted — 2026-05-03" → "Accepted — 2026-05-03; Amended 2026-05-04 (...)"); (b) §Context line 15 wording revision (Codex Major 1 path-(a): replaces "does NOT auto-fire on its own ship cycle's close — it auto-fires on PR-22 (the next substantive-content PR's close) at earliest" with reconciled language naming the anchored recursion-guard regex permitting first auto-fire at PR-21 own merge-close + repo-setting precondition for chore-fix-up PR auto-open); (c) new §Consequences point 8 line; (d) two new §Evidence/references entries (TASK-0020 handoff + PR-23 review-context). No modification to existing §Decision, §Alternatives considered, §Consequences points 1-7 body, or §Evidence pre-existing entries.
   - Pre-existing §Consequences point count (per pre-flight (i.5) (c)): 7. Post-amendment count: 8.
   - bash: post-amendment hash `git hash-object docs/adr/ADR-004-pre-actions-batch-action-insertion.md` returns `5aab01044b1064857d8fb7ff6e157028afb468e5` (post-Codex-Major-1 fix-up).

7. **Class A v-bump applied — README.md line 9 `v2.18` × 2 → `v2.18.1` × 2**; no `v2.18` remaining at Class A canonical-version-of-record surface.
   - bash (working-tree-vs-main; works at pre-commit AND clean post-edits): `git diff origin/main -- README.md` returns single-line change at line 9 (TWO `v2.18` → `v2.18.1` substitution; no other modification).
   - bash: `grep -E "v2\.18[^.]" README.md | grep -v "v2\.18\.1"` returns empty (no `v2.18` remaining without a `.1` suffix).
   - bash: post-bump hash `git hash-object README.md` returns `600cb291b51fbbb29f574b1815d96b17bc0f346f`.

8. **(j) all-instances grep sweep on ADR-004 amendment §-cites verified clean**. New citations introduced by this amendment:
   - Status line: `PR-22`, `TASK-0020` cycle reference.
   - §Consequences point 8 body: `PR-22`, `PR-21`, `TASK-0019`, `TASK-0020`, `PR-24` (anticipation language for empirical-validation event).
   - §Context line 15 path-(a) revision: `PR-21`, `PR-22` (Codex Major 1 fix-up — chronology reconciliation).
   - §Evidence/references new lines: `TASK-0020`, `PR-23`.

   All citations verified well-formed against canonical sources:
   - `PR-22` = TASK-0019 manual chore-fix-up squash `42132c2` (`gh pr view 22` confirms).
   - `PR-21` = TASK-0019 substantive ship squash `db3c9b0` (`gh pr view 21` confirms).
   - `TASK-0019` handoff at `docs/handoffs/TASK-0019-linked-pr-fix-up-action.md` (verified at pre-flight).
   - `TASK-0020` = current cycle (this handoff at `docs/handoffs/TASK-0020-linked-pr-fix-up-defect-fix.md`).
   - `PR-23` = current PR (anticipation language at pre-PR-open form; settles at PR-open per (h.2) sub-shape).
   - `PR-24` = anticipated future PR (TASK-0020 first-auto-fire event; anticipation language acceptable per established cycle-close convention).
   - bash: `grep -nE "(core\.md|github-reference\.md|ADR-00[0-9]+|PMN-00[0-9]+|TASK-[0-9]+|PR-[0-9]+)" docs/adr/ADR-004-pre-actions-batch-action-insertion.md` enumerated; 0 unverifiable citations.

9. **Workflow-level `permissions: pull-requests: write` declaration unchanged** at `.github/workflows/linked-pr-fix-up.yml` line 24 (`permissions:` declared at line 22; `contents: write` at line 23; `pull-requests: write` at line 24). Defect 1 fix is operational-only (repo-setting toggle by owner per path-α); no workflow file modification this cycle.
   - bash (working-tree-vs-main; works at pre-commit AND clean post-edits): `git diff origin/main -- .github/workflows/linked-pr-fix-up.yml` returns empty (workflow file unchanged).

10. **TASK-0020 handoff structural-headings count + section ordering matches TASK-0019 prior** per PMN-007 HEAD canonical 12-field frontmatter convention.
    - **Structural `##` heading count: 16** (matches TASK-0019 = 16). Sections in order: Metadata, Objective, Last completed step, Current state, Decisions made, Assumptions, Risks, Blocking questions, Validation run, Exact next step, §4. ADR-004 amendment content prescription, §5. Placeholder-substitution discipline (PMN-003 (d)), §6. Reassessment / expiry, §7. Post-PR Codex review state, §8. Sign-off, §9. Session log archive.
    - **Literal grep count: 18** — `grep -cE "^## " docs/handoffs/TASK-0020-linked-pr-fix-up-defect-fix.md` returns 18 because §"Exact next step" step 6 contains 2 fenced ` ## Status` example lines inside a `markdown` code-block (the ADR-002 amendment-pattern prescription). Structural count derived by excluding fenced content; the 2-count divergence is fence-internal and does not affect structural section ordering.
    - Frontmatter field count: 12 (task_id, title, pr, branch, linked_predecessor, linked_successor, linked_pr, framework_version_dogfooded, production_target, spec_source, date_authored, status).
    - bash: post-author hash `git hash-object docs/handoffs/TASK-0020-linked-pr-fix-up-defect-fix.md` returns `30893969944b731b617cd9ce90f05d17beac4eee` (post-Validation-run hash-fill + cross-document chicken-and-egg resolution at step-9 self-review re-run; review-context hash claim omitted from handoff Validation run per one-pass resolution).

11. **Cumulative-diff-stats self-stability** per (e.1) sub-rule: per-file numstat sums match cumulative total exactly. Pre-commit verification requires intent-to-add for the 2 untracked files (`git add -N <new-files>`) so they appear in `git diff` output (working-tree-aware form per (h.2)); `git reset` afterwards preserves un-staged state. Builder fills final values post-fix-up at step-9 self-review re-run; values updated here reflect the path-(a) revisions applied this turn.
    - `.github/scripts/linked-pr-fix-up.py`: +2 / -2 (2 token-swap line replacements at lines 35 + 93).
    - `README.md`: +1 / -1 (single-line v-bump at line 9).
    - `docs/adr/ADR-004-pre-actions-batch-action-insertion.md`: +5 / -2 (Status line replacement + §Context line 15 path-(a) revision + new §Consequences point 8 line + 2 new §Evidence/references lines). [Updated post-Codex-Major-1 fix-up; pre-fix-up state was +4 / -1.]
    - `docs/handoffs/TASK-0020-linked-pr-fix-up-defect-fix.md`: +344 / -0 (new file).
    - `docs/reviews/PR-23-codex-pre-commit.md`: +125 / -0 (new file; post-fix-up final size).
    - Per-file numstat sums: 2+1+5+344+125 = **477 insertions** ✓; 2+1+2+0+0 = **5 deletions** ✓. Verified: `git diff --shortstat HEAD` (after `git add -N` of the 2 untracked files) reports `5 files changed, 477 insertions(+), 5 deletions(-)`.

12. **No core.md or github-reference.md modification this cycle** — defect-fix scope tight per §"Decisions made". Three-endpoint Codex poll discipline canonicalization at core.md §8.1.1.1 (cycle-close ledger Item 8) deferred to TASK-0021.
    - bash (working-tree-vs-main; works at pre-commit AND clean post-edits): `git diff origin/main -- core.md github-reference.md` returns empty (both stub files unchanged this cycle).

## Severity adjudication

Per ADR-001 decision 11 owner-invokes convention with Architect direction:
- **Blocking** → hand back to Architect per PMN-001 (k); do not proceed past pre-commit gate.
- **Major** → surface to Architect for path-(a) revise / path-(β) record-and-proceed adjudication.
- **Minor** → surface to Architect; default path-(b) unless direction otherwise.

## Codex review output (verbatim)

Codex desktop pre-commit pass 1 returned 5 findings (0 Blocking + 2 Major + 3 Minor) per established severity taxonomy:

- **[Major] ADR retains stale auto-fire chronology** (`docs/adr/ADR-004-pre-actions-batch-action-insertion.md` line 15): "ADR-004 now documents the empirical first-auto-fire failure, but the existing context still says the Action does not auto-fire on its own ship-cycle close and only fires on PR-22 earliest. That now conflicts with the PR-22 squash commit body and the new amendment text, so the ADR is internally inconsistent unless this older sentence is amended or qualified." Confidence 0.88.
- **[Major] Pre-commit diff/count claims are not literally true** (`docs/reviews/PR-23-codex-pre-commit.md` claims 1, 2, 6, 7, 9, 11, 12): "The current tree is pre-commit: HEAD and origin/main both resolve to 42132c2, and the two new files are still untracked. Literal verification gives git ls-files = 106, git diff origin/main..HEAD empty, and git diff --shortstat HEAD = 3 files changed, 7 insertions, 4 deletions, not the claimed 108 tracked files / 5 files / 472 insertions. The review artifact should either use working-tree-aware commands that include untracked files or clearly mark these as post-stage/post-commit projections." Confidence 0.96.
- **[Minor] Malformed TASK IDs in citation sweep claim** (`docs/reviews/PR-23-codex-pre-commit.md` claim 8): "The ADR itself uses TASK-0019 and TASK-0020, but this claim lists TASK-2019 and TASK-2020 as introduced citations. That makes the all-instances citation sweep internally false even though the underlying ADR citations are well-formed." Confidence 0.98.
- **[Minor] Handoff heading-count command counts fenced examples** (`docs/reviews/PR-23-codex-pre-commit.md` claim 10): "The stated grep-style heading check returns 18 for TASK-0020 versus 16 for TASK-0019 because it counts the two fenced markdown example lines `## Status`. Structurally the extra headings are inside code fences, so the claim should use a fence-aware check or state the structural count separately from the literal grep result." Confidence 0.91.
- **[Minor] Correct workflow permission line reference** (`docs/adr/ADR-004-pre-actions-batch-action-insertion.md` §Consequences point 8): "The ADR says `pull-requests: write` is declared at line 23, but the workflow has `permissions:` at line 22, `contents: write` at line 23, and `pull-requests: write` at line 24. Use line 24 or avoid the exact line number." Confidence 0.99.

Codex review summary: Blocking none; Major 2; Minor 3; recommendation "Request changes before commit, mostly to clean up the verification artifact and the ADR consistency issue." Codex verified-as-passing: regex edits exactly at lines 35 + 93 with hash `500779a2f4054170f09e83e9c0db26e8090daa8e`; bundled Python confirmed newline preservation + idempotency; README hash `600cb291b51fbbb29f574b1815d96b17bc0f346f`; ADR hash (pre-Codex-Major-1 fix-up) `3b967cd1b52cac64120ee968a652b5185c909bcd`; workflow / core / github-reference diffs empty. No file edits applied by Codex.

## Adjudication trace

Architect adjudicated all 5 findings as **path-(a) revise** per cycle convention (Major findings always path-(a); Minor typically path-(a) for clean review-context). All findings classified as pure-token-swap or content-rewrite-at-pure-token-swap class per §8.1.1.3.

Builder applied path-(a) revisions in-place at the substantive commit (pre-push, pre-PR-open):
- **Major 1** — ADR-004 §Context line 15 reworded per Codex's proposed text: replaced "does NOT auto-fire on its own ship cycle's close — it auto-fires on PR-22 (the next substantive-content PR's close) at earliest" with reconciled language naming first auto-fire at PR-21 own merge-close + repo-setting precondition for chore-fix-up PR auto-open.
- **Major 2** — PR-23 review-context claims 1, 2, 6, 7, 9, 11, 12 revised: `git diff origin/main..HEAD` → `git diff origin/main` (working-tree-aware); claim 1 reworked to use `git status --porcelain`; claim 11 clarified `git add -N` requirement for untracked files; pre-commit-vs-post-stage semantics explicit per (h.2) sub-shape.
- **Minor 1** — PR-23 review-context claim 8: 3 token-swap fixes (TASK-2020 ×2 → TASK-0020; TASK-2019 ×1 → TASK-0019).
- **Minor 2** — PR-23 review-context claim 10: reworded to distinguish structural `##` count (16, matches TASK-0019) vs literal grep count (18, includes 2 fenced ` ## Status` example lines inside §3 step 6 code-block).
- **Minor 3** — ADR-004 §Consequences point 8: "line 23" → "line 24" per actual workflow line position (`permissions:` line 22; `contents: write` line 23; `pull-requests: write` line 24).

Cycle-defect-tally cumulative for TASK-0020: 8 (3 pre-flight (i.5) + 5 Codex pre-commit). All path-(a). Lower than TASK-0019's 13. Convergence at one-iteration fixed-point per §8.1.1.3 bounded-continuation rule; Codex pass 2 declined per Builder discretion.

## Codex post-PR pass 1 absorption

Owner posted `@codex review` on PR-23 at 2026-05-04T17:03:54Z (issue-comment `4372907253`). Three-endpoint poll per PMN-008 §5.8 (h.4) OPERATIONAL discipline:

**Endpoint 1 — `gh pr view 23 --json reviews`**: `{"reviews":[]}` (empty; consistent with prior six-cycle pattern for empty endpoint 1).

**Endpoint 2 — `gh api repos/bryce-murphy/amas-framework/issues/23/comments`**: 3 comments verbatim:

1. **Codex bot autonomous pre-trigger comment** (`4372889326`, 2026-05-04T17:01:34Z, **~2m 20s before owner `@codex review`**):
   > "Thanks — I interpreted this trigger as a **review-context/status update** for PR-23 rather than a request to modify code right now.
   >
   > ## Decision
   >
   > Based on the trigger + PR metadata, there is **no explicit follow-up action requested from me yet** (e.g., no new `@codex` instruction like "review now," "apply fix," or "open follow-up PR"). So I'm not generating code changes or a new PR in this turn.
   >
   > ## What I validated from the provided blocks
   >
   > - PR-23 scope is coherent: defect fix for regex newline handling plus ADR operational dependency documentation.
   > - The described code fix (`\\s*$` → `[ \\t]*$`) is technically plausible for preserving terminal newline under `re.MULTILINE`.
   > - The repo-setting dependency note is operationally important and correctly framed as "permissions in workflow are necessary but not sufficient."
   > - The expected empirical validation event is clearly defined as **post-merge auto-fire** behavior (PR-24 creation path).
   >
   > ## Suggested next trigger (if you want action now)
   >
   > If you want me to proceed immediately, post one of these explicit instructions:
   >
   > 1. `@codex review` → I'll produce a formal review summary (Blocking/Major/Minor + recommendation).
   > 2. `@codex fix <issue>` → I'll implement changes in a new branch/PR on top of PR-23 context.
   > 3. `@codex verify claims` → I'll perform claim-by-claim phantom-action verification against repo state/logs.
   >
   > No repository changes were made in this turn."

2. **Owner `@codex review` invocation** (`4372907253`, 2026-05-04T17:03:54Z, by `bryce-murphy`):
   > "@codex review"

3. **Codex bot formal review verdict** (`4372917992`, 2026-05-04T17:05:18Z):
   > "Codex Review: Didn't find any major issues. What shall we delve into next?"

**Endpoint 3 — `gh api repos/bryce-murphy/amas-framework/pulls/23/comments`**: `[]` (empty; no line-level review comments).

### Verdict

**No findings.** Substantive verdict at endpoint 2 verdict comment `4372917992`. No fix-up applied (nothing to address).

### (w) sub-shape this cycle — anti-claim variant

Comment `4372889326` from Codex bot at 17:01:34Z is a **(w) sub-shape A second-instance** evidence point per cycle-close ledger Item 6 (single-data-point at TASK-0019; PR-23 provides second instance):

- **Sub-shape**: autonomous emission without explicit `@codex review` trigger from owner.
- **Variant this cycle**: anti-claims ("I'm not generating code changes or a new PR in this turn", "No repository changes were made in this turn") rather than TASK-0019 sub-shape A's positive-action claims that didn't land.
- **§8.1.1.2 phantom-action verification on anti-claims**: PR-23 diff state at the time of the autonomous comment was exactly `ffb0054` (substantive) + `fad0bae` (URL fill); no Codex-bot-introduced commits, branches, content changes, or new PRs. **Anti-claims verified TRUE** — no phantom-action this instance.
- The two cross-cycle instances share the parent class (autonomous emission without explicit trigger) but diverge in sub-shape (positive-action claims at TASK-0019 vs. anti-claims at TASK-0020). Per Architect ledger update: parent class confirmed; sub-shape variants strengthen the (w) candidate framing without yet meeting promotion threshold.

### (h.4) empirical-pattern refinement note

TASK-0020 is the **first cycle in 7** where the substantive Codex post-PR review verdict landed at **endpoint 2** (`issues/{pr}/comments`) rather than **endpoint 3** (`pulls/{pr}/comments`). Prior six cycles (PR-11/13/15/17/19/21) had substantive content at endpoint 3 (line-level review comments). This cycle's verdict is a single issue-level comment.

Refines cycle-close ledger Item 8 from "substantive findings always at endpoint 3" → **"substantive findings can land at any of the three endpoints; three-endpoint poll required by empirical necessity, not just (h.4) discipline"**. The TASK-0021 canonical-text correction at `core.md` §8.1.1.1 should reflect this refined empirical pattern (verdict landing endpoint is variable; poll all three regardless).

Strengthens the canonical-text-correction case for TASK-0021 (now empirically overdetermined across seven cycles).
