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

(Initial state: placeholder — populated post-Codex-pass.)
