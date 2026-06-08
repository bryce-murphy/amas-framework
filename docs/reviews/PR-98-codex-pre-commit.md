---
status: drafted
---

# PR-98 Codex desktop pre-commit review

## Metadata

- PR: PR-98 (anticipated)
- Branch: fix/task-0052-three-endpoint-canonical-reconciliation
- Cycle: TASK-0052
- Linked handoff: docs/handoffs/TASK-0052-three-endpoint-canonical-reconciliation.md
- Status: drafted
- Codex desktop session timestamp (UTC): TBD

## Builder claims to verify

1. **§6.3 section title changed from "Two-endpoint" to "Three-endpoint".**
   - bash: `grep -n '### §6\.3' github-reference.md` returns `287:### §6.3. Three-endpoint review polling operationalization`
   - PowerShell: `Select-String -Pattern '### §6\.3' github-reference.md`
   - Class: token-swap + structural expansion per D1 spec

2. **§6.3 preamble enumerates three endpoint shapes (no "either…or" binary; "all three endpoints" present).**
   - bash: `sed -n '/### §6\.3/,/### §6\.4/p' github-reference.md | grep 'three distinct'` returns the preamble sentence containing "three distinct GitHub API endpoints with distinct content shapes"
   - bash: `sed -n '/### §6\.3/,/### §6\.4/p' github-reference.md | grep -c 'either.*or\|both endpoints'` returns `0`

3. **§6.3 GET-path block contains exactly three paths (third path `pulls/{pull_number}/comments` present).**
   - bash: `sed -n '/### §6\.3/,/### §6\.4/p' github-reference.md | grep 'GET '` returns three lines
   - Third path present: `GET /repos/{owner}/{repo}/pulls/{pull_number}/comments`
   - Class: structural expansion (new endpoint added)

4. **§6.3 step 4 has three endpoint-specific freshness rows (M1 fix — the load-bearing change).**
   - bash: `sed -n '/### §6\.3/,/### §6\.4/p' github-reference.md | grep -cE '^\s+-\s+\x60pulls/'` returns `2` (pulls/reviews and pulls/comments rows)
   - bash: `sed -n '/### §6\.3/,/### §6\.4/p' github-reference.md | grep -c 'issues/'` returns `1` (issues/comments row)
   - All three endpoint-specific bullet rows present: `pulls/{pull_number}/reviews` (commit_id rule), `issues/{issue_number}/comments` (created_at rule), `pulls/{pull_number}/comments` (commit_id + created_at fallback rule)

5. **§6.3 legacy-label clause present inline in the §8.1.1.1 citation.**
   - bash: `grep 'dual-signal.*retained as a legacy label' github-reference.md` returns the §6.3 preamble sentence
   - PowerShell: `Select-String -Pattern 'dual-signal.*retained as a legacy label' github-reference.md`

6. **§6.3 tie-break clause: "symmetrically across all three endpoints" + staleness-vs-tie-break distinction sentence present.**
   - bash: `grep 'symmetrically across all three endpoints' github-reference.md` returns the tie-break sentence in §6.3
   - bash: `grep 'distinct from the per-endpoint' github-reference.md` returns the staleness-vs-tie-break distinction sentence

7. **§6.3 retains the `core.md §8.1.1.1 (h.3)` canonical citation verbatim.**
   - bash: `grep '§8\.1\.1\.1 (h\.3)' github-reference.md` returns the tie-break sentence in §6.3
   - The `(h.3)` sub-shape label resolves: `grep '(h\.3)' core.md` returns the filter-boundary sub-shape definition at core.md:133; §8.1.1.1 heading present at core.md:23.

8. **§7.1 example pins are placeholders (not 3.0.1, not 3.0.3; `template_version` unchanged).**
   - bash: `grep -n '3\.0\.1' github-reference.md` returns no hits (confirming no residual 3.0.1 pins in §7.1)
   - bash: `grep 'framework_version: <version>' github-reference.md` returns the §7.1 example YAML line
   - bash: `grep -c 'canonical_version: <version>' github-reference.md` returns `2` (AGENTS.md + CLAUDE.md entries in the example block)
   - bash: `grep 'template_version: 3\.0\.0' github-reference.md` returns the `template_version: 3.0.0` lines in §7.1 example block (unchanged)

9. **D3 trio frontmatter all bumped to 3.0.3.**
   - bash: `grep -E '^framework_version:' core.md github-reference.md usage-guide.md` returns `framework_version: 3.0.3` x3
   - PowerShell: `Select-String -Pattern '^framework_version:' core.md, github-reference.md, usage-guide.md`

10. **D3 in-dev markers bumped to v3.0.3 (README.md, AGENTS.md, CLAUDE.md).**
    - bash: `grep -n 'Active framework version.*v3\.0\.3\|v3\.0\.3.*in development' README.md AGENTS.md CLAUDE.md` returns three hits
    - bash: `grep 'v3\.0\.2' README.md AGENTS.md CLAUDE.md` returns no hits at the in-dev marker lines (only §18.3 historical strings in core.md, which is not in this list)

11. **D3 surfaces.yml: framework_version + canonical_version x4 bumped to 3.0.3; template_version values unchanged (3.0.0 and 3.0.1 only).**
    - bash: `grep -E 'framework_version:|canonical_version:|template_version:' .amas/surfaces.yml`
      - Returns: `framework_version: 3.0.3`; `template_version: 3.0.0` x3; `template_version: 3.0.1` x1; `canonical_version: 3.0.3` x4
    - No `3.0.2` in `.amas/surfaces.yml`: `grep '3\.0\.2' .amas/surfaces.yml` returns no output

12. **§18.3 historical strings preserved verbatim (not bumped).**
    - bash: `grep 'v3\.0\.2 canonicalization' core.md` returns two lines: "as of v3.0.2 canonicalization at PR-95 / TASK-0051" (Status line) and "spanning v2.16 through v3.0.2 canonicalization" (enumeration line)
    - Both strings unchanged — historical milestone, not version-of-record

13. **v3.0.0 published markers preserved (no accidental bump to v3.0.3).**
    - bash: `grep -c 'v3\.0\.0' README.md AGENTS.md CLAUDE.md` returns counts > 0 (preserved)
    - bash: `grep 'v3\.0\.0.*v3\.0\.3\|v3\.0\.3.*v3\.0\.0' README.md AGENTS.md CLAUDE.md` returns no hits (no garbled dual-version line)

14. **No `template_version` field changed anywhere (all stay 3.0.0 or 3.0.1).**
    - bash: `grep -rn 'template_version' .amas/surfaces.yml` returns only `3.0.0` or `3.0.1` values
    - bash: `grep -n 'template_version' github-reference.md` returns only `3.0.0` values in the §7.1 example block

15. **No `.github/workflows/review-freshness-check.yml` file created.**
    - bash: `ls .github/workflows/ | grep review-freshness` returns no output
    - bash: `test -f .github/workflows/review-freshness-check.yml && echo EXISTS || echo ABSENT` returns `ABSENT`

16. **Handoff frontmatter conforms to PMN-007 12-field canonical form; `linked_pr` matches MC-C regex.**
    - bash: `head -14 docs/handoffs/TASK-0052-three-endpoint-canonical-reconciliation.md` shows all 12 fields present in correct order
    - `linked_pr: PR-98 (Builder fills with squash SHA post-merge per PMN-001 (k))` — matches canonical regex `^linked_pr: PR-(\d+) \(Builder fills with squash SHA post-merge per PMN-001 \(k\)\)[ \t]*$`
    - python verification: `python -c "import re; print(re.match(r'^linked_pr: PR-(\d+) \(Builder fills with squash SHA post-merge per PMN-001 \(k\)\)[ \t]*$', 'linked_pr: PR-98 (Builder fills with squash SHA post-merge per PMN-001 (k))'))"` returns a Match object (not None)

17. **Review-context frontmatter is 1-field canonical (`status: drafted`).**
    - bash: `head -4 docs/reviews/PR-98-codex-pre-commit.md` returns `---\nstatus: drafted\n---\n`

18. **Cumulative-diff-stats bidirectionally sum-stable per `core.md` §23.6.1.1 (e.1).**
    - bash: `git diff --staged --shortstat origin/main` returns `9 files changed, X insertions(+), Y deletions(-)`
    - bash: `git diff --staged --numstat origin/main` — per-file insertion sum equals shortstat X exactly; per-file deletion sum equals shortstat Y exactly
    - (Values populated at Gate A staging; bidirectional sum-stability confirmed at that point)

19. **(j) All-instances sweep.**
    - No residual "two-endpoint"/"both endpoints" in §6.3: `sed -n '/### §6\.3/,/### §6\.4/p' github-reference.md | grep -iE 'two.endpoint|both endpoints'` returns no output
    - "dual-signal" at exactly 4 HOLD sites unchanged: `grep -n 'dual.signal' core.md github-reference.md` returns core.md:21, core.md:23, github-reference.md:289 (back-reference), github-reference.md:396 (cross-ref) — 4 hits, none renamed
    - No residual 3.0.2 at bump targets: `grep -rn '3\.0\.2' core.md github-reference.md usage-guide.md README.md AGENTS.md CLAUDE.md .amas/surfaces.yml` returns only core.md §18.3 historical strings
    - D3 bump sites at 3.0.3: `grep -rn '3\.0\.3' core.md github-reference.md usage-guide.md README.md AGENTS.md CLAUDE.md .amas/surfaces.yml` returns 12 hits (11 D3 bump sites + 1 D4 adopter migration note at README.md:11)

## Reviewer focus

- **D1 shape verification (primary)**: does `github-reference.md §6.3` mirror `core.md §8.1.1.1` three-endpoint enumeration for endpoint names and GET paths? Does step 4 have three endpoint-specific freshness rows covering all three endpoint shapes? Is the "either…or" binary absent? Is the legacy-label clause syntactically well-formed?
- **D2 verification**: do the §7.1 example pins use `<version>` placeholders? Is `template_version: 3.0.0` unchanged in the example block?
- **D3 precision**: exactly 9 enumerated sites bumped; §18.3 historical strings ("v3.0.2 canonicalization" x2) untouched; v3.0.0 published markers untouched; template_version values untouched (3.0.0 and 3.0.1 only).
- **§-citation resolution**: `§8.1.1.1 (h.3)` in §6.3 tie-break clause resolves — heading §8.1.1.1 present in core.md; (h.3) sub-shape label defined at core.md:133. No other §-citations introduced.
- **Scope protection**: no `.github/workflows/review-freshness-check.yml` file created; no `roadmap_status` / `[v3.1-planned]` marker flipped; no `dual-signal` renamed; no `template_version` changed; no §18.3 content touched.
- **Cumulative-diff-stats bidirectional sum-stability** per claim 18.
- **Recursive-self-instantiation salience**: LOW — this cycle patches the description of review polling (github-reference.md §6.3); the Builder-discipline polling clauses in core.md §8.1.1.1 and usage-guide.md §7.4 are unchanged; the patch governs what future cycles read about §6.3, not the current cycle's own polling behavior.

## Codex desktop pre-commit kickoff

```
Please review the pending changes on the current branch (fix/task-0052-three-endpoint-canonical-reconciliation) per the review-context at docs/reviews/PR-98-codex-pre-commit.md. Working tree at staged-tree state.

Cycle scope: TASK-0052 — v3.0.3 three-endpoint canonical reconciliation. Patch fixes github-reference.md §6.3 (two-endpoint -> three-endpoint; three endpoint-specific step-4 freshness rows; inline legacy-label clause for `dual-signal`). Also de-churns the §7.1 example version pins to `<version>` placeholders (D2), bumps framework version 3.0.2 -> 3.0.3 across 7 files at 9 targeted sites (D3), and appends a one-line adopter migration note to README.md ## Status (D4).

Pre-flight: 6/6 PASS on main at d596cd3 (PR-97 squash merged). Branch: fix/task-0052-three-endpoint-canonical-reconciliation. Anticipated PR: PR-98. Defect-fix patch class; M-A7 stays 38; §18.3 untouched.

Per ADR-001 D11 owner-invokes convention: please run pre-commit review, surface findings per severity (Blocking -> handback; Major -> path-(a)/(beta); Minor -> default path-(b)). Substantive verdict via formal review (`gh pr view` reviews endpoint) preferred; issue-comment summary acceptable; line-level review-comments acceptable.

Verbatim-output convention: capture review verbatim into the review-context file ## Codex desktop pre-commit output absorption section.
```

## Codex desktop pre-commit output absorption

### Codex desktop pre-commit review — 2026-06-08

**Findings**

Blocking: none.

Major: none.

Minor:

- [m1] `docs/reviews/PR-98-codex-pre-commit.md:107` / `docs/reviews/PR-98-codex-pre-commit.md:118` / `docs/handoffs/TASK-0052-three-endpoint-canonical-reconciliation.md:134` still describe D3 as "9 sites" even though the corrected cycle scope and handoff deliverable line say 11 D3 sites across 7 files. The branch content verifies the 11-site model (trio frontmatter x3, in-dev markers x3, `.amas/surfaces.yml` framework_version + canonical_version x4 = x5). Default path-(b) is acceptable if this is left as review-context/handoff noise, but the stale labels are worth fixing if another handoff refresh happens.

- [m2] Several review-context verification commands have stated outputs that do not match the current branch, even though the underlying content is correct. Examples: claim 4's `grep -c 'issues/'` over the whole §6.3 range returns `2` (GET path + bullet row), not `1`; claim 9's `grep -E '^framework_version:' core.md github-reference.md usage-guide.md` returns 4 lines because the §7.1 example now intentionally has `framework_version: <version>` at column 1; claim 13's dual-version grep returns the three valid version-positioning lines that contain current `v3.0.3` and latest published `v3.0.0`; claim 14's broad `grep -n 'template_version' github-reference.md` also returns field-model and §7.2 prose, not only the §7.1 example block. These are battery-shape defects, not substantive patch defects.

- [m3] `docs/handoffs/TASK-0052-three-endpoint-canonical-reconciliation.md:22`, `:31`, `:49`, `:53`, and `:112` still describe the cycle as pre-commit / pre-PR / drafted, while the same handoff later records commit `6f146f3`, push, and PR-98 URL at §7 and the frontmatter status is `active`. The most recent record is recoverable, but the handoff's "current state" is internally contradictory for the next reader.

**Verification Summary**

- Review target note: local `git diff --cached` is empty and `git status` is clean at `HEAD=3407344`; I reviewed the branch delta via `origin/main...HEAD` / `git diff --staged origin/main`, because the index currently matches the branch head rather than an uncommitted staged tree.
- PR metadata verified read-only: PR-98 is OPEN at `https://github.com/bryce-murphy/amas-framework/pull/98`, head branch `fix/task-0052-three-endpoint-canonical-reconciliation`, head SHA `34073444065ca7691b729f52ad94de1f976b932c`; `reviews=[]`, `comments=[]` at check time.
- D1 confirmed: §6.3 title is `Three-endpoint review polling operationalization`; the preamble names three distinct endpoint/content shapes; no `either...or` / `both endpoints` binary remains in §6.3; the GET block has exactly three paths including `pulls/{pull_number}/comments`; step 4 has rows for `pulls/{pull_number}/reviews`, `issues/{issue_number}/comments`, and `pulls/{pull_number}/comments`; the legacy-label and tie-break distinction clauses are present.
- §-citation confirmed: `core.md §8.1.1.1 (h.3)` citation appears once in §6.3; `core.md` has the §8.1.1.1 heading and `(h.3)` label at the filter-boundary definition.
- D2 confirmed: §7.1 example uses `framework_version: <version>` and `canonical_version: <version>` x2; no `3.0.1` remains in `github-reference.md`; `template_version: 3.0.0` values are unchanged in the example.
- D3 confirmed: trio frontmatter is `3.0.3`; README/AGENTS/CLAUDE in-development markers are `v3.0.3`; `.amas/surfaces.yml` has `framework_version: 3.0.3`, four `canonical_version: 3.0.3`, and only `template_version` values `3.0.0` / `3.0.1`; no residual `3.0.2` remains at bump targets.
- D4 confirmed: README status note is present. I did not classify `pulls/{pr}/comments` vs `pulls/{pull_number}/comments` in the human-facing migration note as a finding because the canonical endpoint spelling is present in §6.3 and the README note is informal, but aligning the placeholder would reduce friction.
- §18.3 protection confirmed: only the two intended historical `v3.0.2 canonicalization` strings remain; M-A7 count stays 38 and §18.3 was not substantively changed.
- Scope protection confirmed: no `.github/workflows/review-freshness-check.yml`; no `roadmap_status` / `[v3.1-planned]` marker flips detected in the branch delta; `dual-signal` remains at exactly four HOLD sites; no `template_version` field was bumped.
- Diff-stat check confirmed: `git diff --staged --shortstat origin/main` reports `9 files changed, 359 insertions(+), 19 deletions(-)`; numstat sums to `adds=359 dels=19`; `git diff --check origin/main...HEAD` is clean.

**Recommendation**

Comment / proceed. No blocking or major substantive findings against the TASK-0052 code/content patch. The minor findings are artifact and verification-battery consistency issues suitable for default path-(b), or for a small cleanup if the owner wants the review-context/handoff to be pristine before merge.

### Adjudication — fix-up path-(a) (TASK-0052 Architect directive 2026-06-08)

**F1 — stale "9 sites" site-count label (path-(a), class-sweep):**
- `docs/handoffs/TASK-0052-three-endpoint-canonical-reconciliation.md:134` — "**D3 — version bump 9 sites**" → "**D3 — version bump 11 sites across 7 files**". This is the surviving current-claim instance; the iter-1 §23.6.2 correction fixed the Objective section + claim 19 but missed the §4 deliverable label.
- `docs/reviews/PR-98-codex-pre-commit.md:107` (Reviewer focus: "exactly 9 enumerated sites bumped") — append-only pre-commit historical snapshot; §23.6.5 suppression applied. Correction recorded here only; no back-edit.
- `docs/reviews/PR-98-codex-pre-commit.md:118` (kickoff block: "at 9 targeted sites (D3)") — verbatim text sent to Codex desktop; append-only historical snapshot; §23.6.5 suppression applied. Correction recorded here only; no back-edit.

**F2 — false stated outputs in review-context Builder-claims (all append-only; recorded here, not back-edited):**
- **Claim 4b** (`grep -c 'issues/'` stated `1`; actual `2`): The `issues/` pattern matches both the GET block line (`GET /repos/{owner}/{repo}/issues/{issue_number}/comments`) and the step-4 freshness row bullet. A correct command: `grep -cE '^\s+-\s+\x60issues/'` returns `1` (step-4 bullet row only). Underlying content is correct — one issues endpoint-specific freshness row is present.
- **Claim 9** (`grep -E '^framework_version:' core.md github-reference.md usage-guide.md` stated `framework_version: 3.0.3` x3; actual x4): The §7.1 example block contains `framework_version: <version>` starting at column 0, which matches the `^framework_version:` pattern. A correct command: `grep -E '^framework_version: [0-9]' core.md github-reference.md usage-guide.md` returns exactly 3 lines (frontmatter only). Underlying content is correct — trio frontmatter is `3.0.3` x3.
- **Claim 13** (dual-version grep stated `no hits`; actual 3 hits): The version-positioning sentences in README.md, AGENTS.md, CLAUDE.md correctly contain both `v3.0.3` and `v3.0.0` on the same line (current in-dev vs latest published). The command false-positives on valid content; no garbled dual-version concatenation is present. Underlying content is correct.
- **Claim 14** (`grep -n 'template_version' github-reference.md` stated "only `3.0.0` values in the §7.1 example block"; actual includes §7.2 prose occurrences): The broad pattern matches `template_version` in §7.2 explanatory prose (lines 364, 370, 374, 381, 385, 387). A correct command to scope to example-block values: `grep -n 'template_version: 3\.' github-reference.md` returns only the `3.0.0` value lines in the §7.1 example block. Underlying content is correct — no `template_version` field was bumped.

**F3a — handoff frontmatter `status: drafted -> active`:** Applied at commit `3407344` (prior to this fix-up). `linked_pr: PR-98 (Builder fills with squash SHA post-merge per PMN-001 (k))` confirmed matches MC-C canonical regex; no change needed.

**F3b — gate-current surface refresh:** In this fix-up commit: (1) Metadata `- Status: drafted` → `- Status: active`; (2) Metadata `- Linked PR` URL populated; (3) `## Last completed step` updated to post-PR/Codex-absorbed/fix-up state; (4) `## Current state` Summary updated; (5) cumulative-diff-stats sentence updated with fix-up stats.

**F3c — suppressed (§23.6.5, append-only history):** Codex m3 finding flagged `handoff:22`, `:31`, `:49`, `:53`, `:112` as internally contradictory. `:22` (Metadata Linked PR URL) and `:31` (Metadata Status) and `:49`/`:53` (Last-completed-step / Current-state) are gate-current surfaces — addressed by F3b. `:112` is the `## §3. Execution record` step-9 line ("Next: Gate A stop-and-show...") which is an append-only chronological execution record — §23.6.5 suppression applied; no back-edit. The Codex "false-staleness" flag on the step-by-step execution record is acknowledged and suppressed per §23.6.5.

## Post-PR Codex review — three-endpoint poll record

### Poll timestamp

Trigger: owner posted `@codex review` on PR-98 at 2026-06-08T15:37:34Z. Poll conducted 2026-06-08 after fix-up push (`3df4a4c`).

### Three-endpoint poll results

**Endpoint (a) — `pulls/98/reviews`:**
```
id: 4450692215
user: bryce-murphy
state: COMMENTED
submitted_at: 2026-06-08T14:56:51Z
commit_id: 34073444065ca7691b729f52ad94de1f976b932c  (= 3407344; pre-fix-up head; stale vs current 3df4a4c)
body: [Codex desktop pre-commit verbatim output — see ## Codex desktop pre-commit output absorption above]
```
Note: posted by owner (`bryce-murphy`) as a formal review object containing the Codex desktop pre-commit output. Stale relative to current head `3df4a4c` — expected; this is the pre-commit review, not the post-PR re-review.

**Endpoint (b) — `issues/98/comments`:**
```
id: 4650667689
user: bryce-murphy
created_at: 2026-06-08T15:37:34Z
body: "@codex review"

id: 4650695523
user: chatgpt-codex-connector[bot]
created_at: 2026-06-08T15:40:48Z
body: "Codex Review: Didn't find any major issues. Keep it up!"
```

**Endpoint (c) — `pulls/98/comments`:** empty

**PR head SHA at poll time:** `3df4a4c005e86fff13760c2dc8254ac3d85431af` (= `3df4a4c`) -- fix-up commit. ✓

### Verdict

`chatgpt-codex-connector[bot]` at endpoint (b): **"Didn't find any major issues."** Substantive verdict — no findings raised. Clean re-review pass. The retained append-only "9 sites" / false-output text (review-context `:107`/`:118`, claims 4b/9/13/14) was NOT re-flagged. Reach = 1 (below sec 24.6 Stop-Iteration threshold of 4).

### Thread engagement (sec 7.2 rule (b))

Reply posted on PR-98 at `https://github.com/bryce-murphy/amas-framework/pull/98#issuecomment-4650711517`:
- F1 (handoff sec 4 "9 sites"): corrected to 11 at current-claim surface in `3df4a4c`.
- F1 append-only instances (review-context :107/:118) + F2 (false stated outputs, claims 4b/9/13/14): left by design as append-only pre-commit review-invocation record per sec 13.1/sec 23.6.5; corrections recorded in adjudication.
- F3a/F3b: status active + gate-current surfaces refreshed in `3df4a4c`.
- F3c: sec 3 execution-record step-9 left per sec 23.6.5 suppression; acknowledged in adjudication.
