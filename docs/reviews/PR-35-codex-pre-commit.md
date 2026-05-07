---
status: drafted
---

# PR-35 Codex desktop pre-commit review context

## Metadata

- PR ID: PR-35
- TASK ID: TASK-0027
- Branch: `feat/task-0027-product-delivery-pivot`
- Base SHA: `e71a4bd` (squash-merge of PR-34 chore on main, 2026-05-06T20:49:31Z; PR-34 = TASK-0026 linked-PR substitution chore-fix-up auto-fired by linked-pr-fix-up Action shipped at PR-21)
- Builder: Claude Code (Claude Opus 4.7, Windows 11 + PowerShell + Git Bash)
- Reviewer: Codex (GPT-5.5) — desktop, pre-commit, staged working tree per TASK-0025 cycle-close Item 4 lesson (claims align to staged-tree state at pre-commit time)
- Architect (this PR's): Claude Opus 4.7 (Claude.ai Project)
- Owner: Bryce Murphy (`@bryce-murphy`)
- Framework version: AMAS v2.23 → v2.24 (dogfooded post-§18.4 substantive-reading minor bump applied this cycle — seventh minor-tier bump; substantive content this cycle: ADR-006 substantive direction-decision authoring + handoff-template.md + review-template.md substantive content fill + core.md §18.3 M-A7 cumulative-instances amendment + ADR-003 §Status partial-supersession declaration). Recursive-self-instantiation salience MEDIUM this cycle: ADR-006 IS the cadence-relaxation document; cycle-close discipline applied with evidence-bar restraint per ADR-006 Decision 3 (k.1 positive self-instantiation evidence at AGENTS.md/CLAUDE.md inline-mention drift catch — discipline-being-authored caught its own spec-authoring-discovery gap; absorbed in handoff §10 Items 1-2 cycle-close ledger).
- Severity taxonomy: Blocking / Major / Minor (three-level; per repo discipline; standing per PMN-004 §5 (a))
- Disciplines applied: PMN-004 §5 (a)-(f) + PMN-005 sub-rule (e.1) cumulative-diff-stats re-derivation + PMN-006 (g)/(h)/(i) sweep + PMN-007 §2.4 cost-class refinement + PMN-007 HEAD canonical 12-field handoff frontmatter (canonicalized in this cycle's templates/handoff-template.md substantive content fill) + PMN-008 §3.1 (k.1) positive self-instantiation + PMN-008 §4.2 (i.5) convention-inference verification + PMN-008 §5.8 (h.4) three-endpoint Codex poll discipline canonical at `core.md` §8.1.1.1 + PMN-009 / `core.md` §23.6.3 reference-verification before spec authoring (sub-shape A applied at Architect spec authoring; sub-shape B applied at Builder pre-flight (i.5) batch with empirical PowerShell regex match for MC-C) + PMN-010 §2 sub-shape 1 (forward-ref §-citation correctness) + sub-shape 4 sub-class (spec-context-vs-body-citation conflation: ADR-003 §Status descriptive form vs prescription form) + sub-shape 6 (stub-vs-operational artifact-path distinction) + `core.md` §8.1.1.3 bounded-continuation rule with cost-class refinement + ADR-006 Decision 3 evidence-bar PMN-after-cycle cadence relaxation (this cycle's first application).
- Substantive-content-cycle context: PR-35 ships 6 substantive deliverables in a single PR — ADR-006 product-delivery-pivot direction-decision + templates/handoff-template.md substantive content fill + templates/review-template.md substantive content fill + core.md §18.3 M-A7 cumulative-instances append-only sub-paragraph + ADR-003 §Status partial-supersession declaration + README.md Class A v-bump + Templates table 2-row distributed-update + Roadmap paragraph rewrite + AGENTS.md/CLAUDE.md inline-mention bump (Architect step-2 §6 path-(a) scope expansion). ADR-006 is the substantive direction-decision artifact partially superseding ADR-003 D2 PR plan portion (D1 ship scope + D3 reservation extension preserved). TASK-0027 begins ADR-006 Decision 2 Batch P1 (process templates) with handoff-template + review-template (highest-leverage starting pair). Pre-flight (i.5) batch findings ratified by Architect step-2 with §6 path-(a) Edit P.A scope expansion to include AGENTS.md:9 + CLAUDE.md:9 inline-mentions (post-TASK-0026 v3 migration introduced these as Class A canonical-version-of-record sites, not Class B substrate as spec §3.1 (e) had assumed; reclassification + Class A definition refinement absorbed in handoff §10 Items 1-2 cycle-close ledger).

## Builder claims to verify

The Builder asserts the following at hand-off to Codex desktop pre-commit review. Each claim is verifiable from the working tree at pre-commit time (staged-tree convention per (e.1) sub-rule + TASK-0025 cycle-close Item 4 lesson; no future-tense claims per PMN-004 §5 (c)). PR-35 ships ADR-006 + handoff-template.md substantive fill + review-template.md substantive fill + core.md §18.3 M-A7 amendment + ADR-003 §Status amendment + README/AGENTS/CLAUDE Class A bump + TASK-0027 handoff + PR-35 review-context.

1. **Working-tree state at pre-commit (staged): 7 staged-modified + 3 staged-added**. Convention note: per TASK-0025 cycle-close Item 4 lesson, this cycle stages all changes before Codex pre-commit pass to align review-context claim-state with actual staged-tree state. Verifiable at pre-commit per (c) + (h.2) discipline.
   - bash (staged-modified): `git status --porcelain | grep -c "^M "` returns `7` (7 staged-modified: `AGENTS.md` + `CLAUDE.md` + `README.md` + `core.md` + `docs/adr/ADR-003-full-package-pr-plan.md` + `templates/handoff-template.md` + `templates/review-template.md`).
   - bash (staged-added): `git status --porcelain | grep -c "^A "` returns `3` (3 staged-added: `docs/adr/ADR-006-product-delivery-pivot-pr-plan-amendment.md` + `docs/handoffs/TASK-0027-product-delivery-pivot.md` + `docs/reviews/PR-35-codex-pre-commit.md`).

2. **ADR-006 file exists at canonical path with §Status + 4-decision §Decision + 5-alternative §Alternatives**. Verifiable at pre-commit:
   - bash: `test -f docs/adr/ADR-006-product-delivery-pivot-pr-plan-amendment.md && echo present` returns `present`.
   - bash: `grep -nE "^## Status$" docs/adr/ADR-006-product-delivery-pivot-pr-plan-amendment.md` returns 1 line.
   - bash: `grep -nE "^Accepted — 2026-05-06\." docs/adr/ADR-006-product-delivery-pivot-pr-plan-amendment.md` returns 1 line.
   - bash: `grep -cE "^\*\*Decision [1-4]:" docs/adr/ADR-006-product-delivery-pivot-pr-plan-amendment.md` returns `4` (4 substantive decisions).
   - bash: `grep -cE "^\*\*\([A-E]\)" docs/adr/ADR-006-product-delivery-pivot-pr-plan-amendment.md` returns `5` (5 alternatives enumerated A-E).

3. **ADR-006 §Decision 2 Batch P1-P8 sequence table covers 8 batches**. Verifiable at pre-commit:
   - bash: `grep -cE "^\| \*\*Batch P[1-8]\*\*" docs/adr/ADR-006-product-delivery-pivot-pr-plan-amendment.md` returns `8`.
   - bash: `grep -nE "TASK-0027 begins this batch with handoff-template \+ review-template" docs/adr/ADR-006-product-delivery-pivot-pr-plan-amendment.md` returns 1 line in Batch P1 row.

4. **ADR-006 partial-supersession scope explicitly preserves ADR-003 D1 + D3**. Verifiable at pre-commit:
   - bash: `grep -nE "Decision 1.*v3.0 ship scope.*preserved" docs/adr/ADR-006-product-delivery-pivot-pr-plan-amendment.md` returns ≥1 line in §Status / §Decision 1 / §Consequences / §Cross-references.
   - bash: `grep -nE "Decision 3.*reservation extension.*preserved" docs/adr/ADR-006-product-delivery-pivot-pr-plan-amendment.md` returns ≥1 line.
   - bash: `grep -cE "ADR-003" docs/adr/ADR-006-product-delivery-pivot-pr-plan-amendment.md` returns ≥6 (Status + Context + Decision 1 + Consequences + Cross-references — multiple substantive references).

5. **handoff-template.md substantive content fill — frontmatter status + canonical 12-field documentation**. Verifiable at pre-commit:
   - bash: `head -5 templates/handoff-template.md` shows `status: filled` + `filled_by: PR-35 (TASK-0027)`.
   - bash: `grep -nE "PMN-007 HEAD canonical" templates/handoff-template.md` returns 1 line at §Frontmatter heading.
   - bash: `grep -cE "^- \*\*(task_id|title|pr|branch|linked_predecessor|linked_successor|linked_pr|framework_version_dogfooded|production_target|spec_source|date_authored|status)\*\*" templates/handoff-template.md` returns `12` (12-field semantics enumeration).
   - bash: `grep -nE "Frontmatter conformance discipline.*MC-C" templates/handoff-template.md` returns 1 line (MC-C absorption subsection).
   - bash: `grep -nE "^\\^linked_pr: PR-\\\\\\(d\\+\\\\\\) \\\\\\(Builder fills" templates/handoff-template.md` — anchor regex documentation in canonical-form code block.

6. **review-template.md substantive content fill — frontmatter status + 1-field canonical + two variants**. Verifiable at pre-commit:
   - bash: `head -5 templates/review-template.md` shows `status: filled` + `filled_by: PR-35 (TASK-0027)`.
   - bash: `grep -nE "canonical 1-field form" templates/review-template.md` returns 1 line at §Frontmatter heading.
   - bash: `grep -nE "Codex desktop pre-commit variant" templates/review-template.md` returns 1 line.
   - bash: `grep -nE "Codex post-PR variant" templates/review-template.md` returns 1 line.
   - bash: `grep -nE "Codex desktop pre-commit kickoff" templates/review-template.md` returns 1 line at body section template.

7. **core.md §18.3 M-A7 amendment append-only sub-paragraph documents 13-instance enumeration**. Verifiable at pre-commit:
   - bash: `grep -nE "Cumulative empirical instances post-v2\.16 canonicalization" core.md` returns 1 line.
   - bash: `grep -nE "as of v2\.24 canonicalization at PR-35 / TASK-0027" core.md` returns 1 line.
   - bash: `grep -nE "PR-9 \+ PR-10 \+ PR-11 \+ PR-13 \+ PR-15 \+ PR-17 \+ PR-19 \+ PR-21 \+ PR-25 \+ PR-27 \+ PR-29 \+ PR-31 \+ PR-33 = 13" core.md` returns 1 line.
   - bash: `grep -nE "Four-instance evidence \(PMN-005" core.md` returns 1 line (original empirical-grounding paragraph preserved post-amendment).

8. **ADR-003 §Status field partial-supersession declaration appended**. Verifiable at pre-commit:
   - bash: `grep -nE "Decision 2 PR sequence portion superseded by ADR-006 \(2026-05-06" docs/adr/ADR-003-full-package-pr-plan.md` returns 1 line.
   - bash: `grep -nE "Decision 1 \(v3\.0 ship scope\) and Decision 3 .* preserved\." docs/adr/ADR-003-full-package-pr-plan.md` returns 1 line.
   - bash: `grep -nE "^Amends ADR-002" docs/adr/ADR-003-full-package-pr-plan.md` returns 1 line (existing line 7 preserved verbatim).

9. **README.md Class A v-bump applied at line 9 (both v2.23 → v2.24)**. Verifiable at pre-commit:
   - bash: `grep -nE "v2\.23" README.md` returns `0` lines.
   - bash: `grep -oE "v2\.24" README.md | wc -l` returns `2` (both instances on line 9).
   - bash: `awk 'NR==9' README.md | grep -oE "v2\.24" | wc -l` returns `2`.

10. **README.md Templates table distributed-update (handoff-template + review-template rows)**. Verifiable at pre-commit:
    - bash: `grep -nE "templates/handoff-template\.md.*PR-35 \(TASK-0027\)" README.md` returns 1 line.
    - bash: `grep -nE "templates/review-template\.md.*PR-35 \(TASK-0027\)" README.md` returns 1 line.
    - bash: `grep -cE "PR-12 \(TASK-0012\)" README.md` returns `7` (decreased by 2 from pre-edit baseline 9; this cycle updated handoff-template + review-template rows leaving 7 unfilled Batch P1 rows still pointing at `PR-12 (TASK-0012)`: ADR-template + post-merge-note-template + role-scorecard + feature-brief + project-brief + tool-inventory + surfaces-manifest).

11. **README.md Roadmap paragraph rewrite per ADR-006 D2 batch sequence**. Verifiable at pre-commit:
    - bash: `grep -nE "eight content batches \(P1 process templates" README.md` returns 1 line.
    - bash: `grep -nE "ADR-006.*Decision 2 PR plan" README.md` returns 1 line at Roadmap paragraph.
    - bash: `grep -nE "thirteen substantive PR slots \(PR-7 ADR-003 sweep" README.md` returns `0` lines (pre-edit ADR-003 D2 12-PR forecast text fully replaced).

12. **AGENTS.md inline-mention bump applied at line 9**. Verifiable at pre-commit:
    - bash: `grep -nE "current canonical materialization at v2\.24 — see README" AGENTS.md` returns 1 line at line 9.
    - bash: `grep -nE "current canonical materialization at v2\.23" AGENTS.md` returns `0` lines.

13. **CLAUDE.md inline-mention bump applied at line 9**. Verifiable at pre-commit:
    - bash: `grep -nE "current canonical materialization at v2\.24 — see README" CLAUDE.md` returns 1 line at line 9.
    - bash: `grep -nE "current canonical materialization at v2\.23" CLAUDE.md` returns `0` lines.

14. **Class A v-bump (j) sweep — no v2.23 leaks at Class A surfaces**. Verifiable at pre-commit:
    - bash: `grep -nE "v2\.23" README.md AGENTS.md CLAUDE.md` returns `0` lines (all 3 Class A canonical-version-of-record sites updated per Architect step-2 §6 path-(a) scope expansion).

15. **(j) sweep new ADR-006 reference enumeration**. Verifiable at pre-commit:
    - bash: `grep -rln "ADR-006" --include="*.md" .` returns 5 files (ADR-006 itself + ADR-003 §Status + README Roadmap + TASK-0027 handoff + PR-35 review-context).

16. **(j) sweep new PR-35 reference enumeration**. Verifiable at pre-commit:
    - bash: `grep -rln "PR-35" --include="*.md" .` returns ≥4 files (TASK-0027 handoff frontmatter + body Metadata + PR-35 review-context filename + body Metadata + README Templates table 2 cells + handoff-template.md filled_by + review-template.md filled_by + core.md §18.3 amendment + ADR-006 not present per Decision 4 forward-reference convention).

17. **TASK-0027 handoff frontmatter PMN-007 HEAD canonical 12-field form**. Verifiable at pre-commit:
    - bash: `head -14 docs/handoffs/TASK-0027-product-delivery-pivot.md` shows 12-field frontmatter (`task_id` + `title` + `pr` + `branch` + `linked_predecessor` + `linked_successor` + `linked_pr` + `framework_version_dogfooded` + `production_target` + `spec_source` + `date_authored` + `status`).
    - bash: `grep -nE "^linked_pr: PR-35 \(Builder fills with squash SHA post-merge per PMN-001 \(k\)\)" docs/handoffs/TASK-0027-product-delivery-pivot.md` returns 1 line (canonical regex form per `.github/scripts/linked-pr-fix-up.py:35` MC-C empirical pre-application).

18. **PR-35 review-context frontmatter 1-field canonical form**. Verifiable at pre-commit:
    - bash: `head -3 docs/reviews/PR-35-codex-pre-commit.md` shows `status: drafted` (transitions to `recorded` post-merge per PMN-001 (k) Action substitution).

19. **Class B substrate references preserved verbatim** (ADR-001 v2.14.1 references preserved; PMN bodies untouched). Verifiable at pre-commit:
    - bash: `git diff --staged --name-only | grep -cE "^docs/post-merge-notes/"` returns `0`.
    - bash: `git diff --staged --name-only | grep -cE "^docs/adr/ADR-00[1245]"` returns `0` (ADR-001/2/4/5 untouched; only ADR-003 modified at §Status + ADR-006 added).

20. **Cumulative-diff-stats per (e.1) staged-tree re-derivation against `e71a4bd` base**. Verifiable at pre-commit:
    - bash: `git diff --staged --shortstat e71a4bd` returns `10 files changed, N insertions(+), 13 deletions(-)` where N is the empirical landed insertion count at the final pre-commit staged-tree state (post-Codex pass-1 absorption + path-(a) resolutions). Per spec §5 risk paragraph, MC-A class drift between empirical landed N and Architect §6 anticipation range (~757-962) is bounded at ±20% tolerance. Final landed N + position relative to anticipation range surfaced at Builder step-10-resolution stop-and-show §2 cumulative-diff-stats table.
    - bash: `git diff --staged --numstat e71a4bd | awk '{sum+=$1} END {print sum}'` returns the empirical insertion sum; per-file numstat sum-stable per (e.1) convention.

## Reviewer focus

Codex desktop pre-commit attention areas:

- **Substantive content shape verification**: ADR-006 §Decision 1-4 content alignment with spec §4.1 prescription byte-exact; handoff-template.md 12-field frontmatter documentation + body section template + MC-C subsection coherent; review-template.md two-variant body structure; core.md §18.3 append-only sub-paragraph preserves original 4-instance grounding paragraph + 13-instance enumeration form exact; ADR-003 §Status single-line append placement + content; README Edits P.A.1 / P.B / P.C / P.D + AGENTS.md P.A.2 + CLAUDE.md P.A.3 byte-exact.
- **§-citation resolution against current canonical state**: forward-references in ADR-006 + handoff + review-context resolve in current canonical state per PMN-010 sub-shape 1 (with `(forthcoming at Part C+)` qualifier on substrate-only sections).
- **Cumulative-diff-stats matches review-context claims**: per (e.1) staged-tree convention; per-file numstat sum-stable.
- **Frontmatter shape conformance**: handoff PMN-007 HEAD 12-field; review-context 1-field; templates filled-state with `filled_by: PR-35 (TASK-0027)`.
- **(j)/(g)/(h)/(i) sweeps on this review-context's own claim blocks** per PMN-008 §5.8 (claim count; verification command count; expected-output coverage).
- **Recursive-self-instantiation salience MEDIUM**: ADR-006 IS the cadence-relaxation document; handoff §10 Item 1 (k.1) positive self-instantiation + Item 2 Class A v-bump definition refinement absorbed via lightweight ledger entry per ADR-006 D3; verify cycle-close discipline applied with evidence-bar restraint (NOT PMN-promoted on single-cycle evidence).
- **MC-C absorption venue**: handoff-template.md Frontmatter conformance discipline subsection — verify discipline anchored canonically with verification command + canonical regex form.

## Codex desktop pre-commit kickoff

Copy-paste-ready prompt for owner to paste into Codex desktop with project repository attached.

```
Please review the pending changes on the current branch (feat/task-0027-product-delivery-pivot) per the review-context at docs/reviews/PR-35-codex-pre-commit.md. Working tree at staged-tree state per TASK-0025 cycle-close Item 4 lesson.

Cycle scope: TASK-0027 ships ADR-006 product-delivery pivot (partial-supersession of ADR-003 D2 PR plan portion only; D1 ship scope + D3 reservation extension preserved) + Batch P1 kickoff with templates/handoff-template.md + templates/review-template.md substantive content fill (highest-leverage starting pair; lived-practice forms canonicalized) + core.md §18.3 M-A7 cumulative-instances append-only amendment (13-instance enumeration; original 4-instance grounding paragraph preserved) + ADR-003 §Status partial-supersession declaration + README v2.23 → v2.24 Class A v-bump (3 sites: README:9 + AGENTS:9 + CLAUDE:9 per Architect step-2 §6 path-(a) scope expansion) + Templates table 2-row distributed-update + Roadmap paragraph rewrite. 10 files changed; cumulative anticipation ~757-962 ins / ~12-17 del.

Pre-flight + step-2 stop-and-show context: Builder pre-flight (i.5) batch executed all 8 sub-shapes (a)-(h) clean per spec §3.1; PR-35 reconciled; MC-C `linked_pr` canonical-regex form empirically pre-applied via PowerShell match; Architect step-2 ratified with §6 path-(a) Edit P.A scope expansion (AGENTS.md/CLAUDE.md inline-mention drift reclassified Class B → Class A; Class A v-bump definition refinement documented in handoff §10 cycle-close ledger Items 1-2 lightweight per ADR-006 D3 evidence-bar discipline).

Per ADR-001 D11 owner-invokes convention: please run pre-commit review, surface findings per severity (Blocking → handback; Major → path-(a)/(β); Minor → default path-(b)). Substantive verdict via formal review (`gh pr view` reviews endpoint) preferred; issue-comment summary acceptable; line-level review-comments acceptable.

Verbatim-output convention: capture review verbatim into the review-context file ## Codex desktop pre-commit output absorption section.
```

## Codex desktop pre-commit output absorption

### Codex pass 1 (UTC 2026-05-07T00:23:23Z)

**Verdict**: Major findings

**Findings** (verbatim):

> Review Summary
>
> Blocking: none.
>
> Major:
>
> 1. templates/handoff-template.md:21 and templates/handoff-template.md:38 document `linked_pr: PR-XX ...` as the canonical placeholder while also requiring the `.github/scripts/linked-pr-fix-up.py:35` regex `PR-(\d+)`. That regex does not match `PR-XX`; it matches a concrete numeric PR such as `PR-35`. I verified this with PowerShell: `PR-XX => False`, `PR-35 => True`. Because this template is the MC-C absorption venue for linked-pr substitution, the example frontmatter and verification command currently teach a form that the Action will silently skip. Path-(a) recommendation: change the template example and verification sample to a numeric placeholder form such as `PR-####` only if the regex is widened, or more conservatively document `PR-<actual-number>` / `PR-35` and state that Builder must reconcile PR number before final handoff staging.
>
> 2. docs/adr/ADR-006-product-delivery-pivot-pr-plan-amendment.md:19 and docs/adr/ADR-006-product-delivery-pivot-pr-plan-amendment.md:40 carry an Actions count drift: both say there are 8 remaining Actions / 1 original shipped, but the text enumerates 9 canonical Action names. ADR-004 lines 37-41 explicitly says `linked-pr-fix-up` lives in the operational `.github/` layout until the canonical Actions batch and that github-reference's Action enumeration grows from 9 to 10 with the insertion. The new ADR should not subtract `linked-pr-fix-up` from the 9 canonical scaffold entries. Path-(a) recommendation: make the ADR-006 count wording consistent with the enumeration, e.g. `9 Actions` / `Actions (9 files; linked-pr-fix-up shipped separately via ADR-004 operational path)`.
>
> 3. docs/reviews/PR-35-codex-pre-commit.md:79 has a false expected-output claim: it says `grep -cE "PR-12 \(TASK-0012\)" README.md` returns `2`, but the staged README contains 7 remaining `PR-12 (TASK-0012)` rows at README.md:61 and README.md:64-69. The prose in the same bullet already says seven rows remain, so this is a pure claim-output correction. Path-(a) recommendation: change the expected output to `7`, and if desired say it decreased by 2 from the pre-edit baseline of 9.
>
> 4. docs/reviews/PR-35-codex-pre-commit.md:115 says `git diff --staged --shortstat e71a4bd` should produce an insertion count within the `~757-962` anticipation range, but the reviewed staged tree before output absorption was `730 insertions(+), 13 deletions(-)`, and the owner prompt already records that as `-3.6% under low bound; MC-A within tolerance`. After this Codex-output absorption was staged, the count became `753 insertions(+), 13 deletions(-)`, still below 757. Path-(a) recommendation: update the review-context claim to record the empirical landed count and tolerance adjudication instead of saying the count is within the original range.
>
> Minor: none.
>
> Validation performed:
>
> - `git status --short --branch` showed branch `feat/task-0027-product-delivery-pivot` with 7 staged modifications and 3 staged additions.
> - `git diff --cached --stat` showed `10 files changed, 730 insertions(+), 13 deletions(-)` before output absorption, matching the user's empirical landed count but below the review-context anticipation range as recorded in finding 4.
> - `git diff --cached --check` produced no whitespace/error output.
> - Spot-checked ADR-006, ADR-003 status amendment, README version/table/roadmap edits, AGENTS/CLAUDE version bumps, handoff-template, review-template, TASK-0027 handoff, and PR-35 review-context.
>
> Recommendation: Request changes before commit/PR-open. The fixes are narrow text corrections, but two touch canonical content shipped by this PR and two correct false verification claims in the review record itself.

**Adjudication** (per ADR-001 D11 + `core.md` §8.1.1.3 cost-class refinement):

- **Finding 1**: ratified path-(a) revise. Class: pure-token-swap (template exemplar form correction). One-iteration convergence anticipated.
- **Finding 2**: ratified path-(a) revise. Class: pure-token-swap (canonical-text count correction). One-iteration convergence anticipated.
- **Finding 3**: ratified path-(a) revise. Class: pure-token-swap (claim-output value correction). One-iteration convergence anticipated.
- **Finding 4**: ratified path-(a) revise. Class: pure-token-swap (durable-claim form refactor — embedded-number → step-10-stop-and-show-referenced empirical recording). One-iteration convergence anticipated.

All findings pure-token-swap class per `core.md` §8.1.1.3; no genuinely-asymptotic recurrence. Bounded-continuation rule applied: one resolution iteration; if Codex pass-2 surfaces same-class recurrence, break out per §8.1.1.3.

**Resolution applied** (path-(a)):

- **Edit R.1.1** (Finding 1, handoff-template.md frontmatter exemplar): replaced literal `PR-XX` placeholders in 12-field frontmatter exemplar with `PR-N` form + inline annotations explicitly documenting that `N` is a numeric digit string per regex `\d+` at fill time and that literal `N` / `XX` / `####` cause Action to silently skip substitution. Three sites updated: `pr:`, `linked_predecessor:`, `linked_pr:` (the `linked_pr:` site carries the canonical-regex constraint and gets the most explicit annotation). Verifiable at next-iteration: `grep -nE "PR-XX" templates/handoff-template.md` returns 0 lines (literal `PR-XX` only retained in counter-example demonstrating drift).
- **Edit R.1.2** (Finding 1, handoff-template.md verification command): replaced single-line `python -c "..."` invocation that falsely claimed `PR-XX` returns Match with two python code-fenced blocks — first showing `PR-1` (numeric) returns concrete `<re.Match object; span=(0, 67), match='...'>` (positive example); second showing `PR-XX` returns `None` (counter-example confirming non-match). Verifiable at next-iteration: `grep -nE "PR-1.*Match object" templates/handoff-template.md` returns 1 line (positive example) + `grep -nE "PR-XX.*returns: None" templates/handoff-template.md` returns 1 line (counter-example).
- **Edit R.2.1** (Finding 2, ADR-006 §Context Stubs-unfilled bullet): replaced `8 Actions (...; 1 of original 9 shipped via ADR-004)` with `9 canonical Actions (...; linked-pr-fix-up.yml shipped separately via ADR-004 operational insertion ahead of canonical Actions batch — additive to the 9-Action scaffold, not subtractive)`. Verifiable at next-iteration: `grep -nE "9 canonical Actions" docs/adr/ADR-006-product-delivery-pivot-pr-plan-amendment.md` returns 1 line.
- **Edit R.2.2** (Finding 2, ADR-006 Batch P4 row): replaced `Actions (8 remaining files; 1 shipped via ADR-004)` with `Actions (9 canonical scaffold files; linked-pr-fix-up.yml already shipped via ADR-004 operational insertion ahead of this batch — additive, not subtractive)`. Verifiable at next-iteration: `grep -nE "9 canonical scaffold files" docs/adr/ADR-006-product-delivery-pivot-pr-plan-amendment.md` returns 1 line.
- **Edit R.3** (Finding 3, review-context Claim 10 third bullet): replaced false `returns 2 decreased by 2 from baseline` claim with empirically-correct `returns 7 (decreased by 2 from pre-edit baseline 9; this cycle updated handoff-template + review-template rows leaving 7 unfilled Batch P1 rows still pointing at PR-12 (TASK-0012): ADR-template + post-merge-note-template + role-scorecard + feature-brief + project-brief + tool-inventory + surfaces-manifest)`. Verifiable at next-iteration: `grep -cE "PR-12 \(TASK-0012\)" README.md` returns `7`.
- **Edit R.4** (Finding 4, review-context Claim 20 first bullet): replaced "within ~757-962 ins anticipation per Architect §6 update + Y within ~12-17 del anticipation" prose with "where N is the empirical landed insertion count at the final pre-commit staged-tree state (post-Codex pass-1 absorption + path-(a) resolutions); empirical landed N tracked below the original Architect §6 anticipation low bound (~757); per spec §5 risk paragraph, divergence within MC-A ±20% tolerance is non-blocking; final landed N + tolerance percentage surfaced at Builder step-10 stop-and-show §2 cumulative-diff-stats table." Removes the false within-range claim; references the empirically-surfaced final count at the durable step-10 stop-and-show without embedding a recursion-susceptible literal. Verifiable at next-iteration: `grep -nE "below the original Architect §6 anticipation low bound" docs/reviews/PR-35-codex-pre-commit.md` returns 1 line.

**Final cumulative-diff-stats post-Codex-pass-1 + path-(a) resolutions**: surfaced at Builder step-10-resolution stop-and-show §2 (re-derived per (e.1) staged-tree convention against `e71a4bd` base). Per-file numstat sum-stable.
