---
status: recorded
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
   - bash: `grep -F '^linked_pr: PR-(\d+) \(Builder fills with squash SHA post-merge per PMN-001 \(k\)\)' templates/handoff-template.md` returns 3 lines (the canonical regex anchor code-block + positive `PR-1` python verification example + counter-example `PR-XX` python verification, all referencing the same canonical regex literal; fixed-string match avoids ERE escaping pitfalls per Codex post-PR pass-1 P2 finding R.5 absorption).

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
    - bash: `grep -rln "PR-35" --include="*.md" .` returns 7 committed-tree files containing `PR-35` references — TASK-0027 handoff (frontmatter `pr` + `linked_pr` + body Metadata) + PR-35 review-context (filename + body Metadata) + README (Templates table 2 cells) + handoff-template.md (`filled_by: PR-35 (TASK-0027)`) + review-template.md (`filled_by: PR-35 (TASK-0027)`) + core.md (§18.3 amendment "at PR-35 / TASK-0027") + ADR-006 (§Consequences distributed-update text "PR-35 (TASK-0027)" × 2 occurrences at line ~84). All 7 sites consistent with Builder step-10 stop-and-show §4 (j)-sweep enumeration (intra-document Claim-16-vs-step-10-table consistency restored at Edit R.8 per Codex post-PR pass-3 P2 finding absorption).

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

### Codex post-PR pass 1 (UTC 2026-05-07T00:57:20Z)

Three-endpoint poll evidence per `core.md` §8.1.1.1:
- **Endpoint A** (`gh pr view 35 --json reviews`): 1 formal review submitted UTC 2026-05-07T00:57:20Z by `chatgpt-codex-connector`; state `COMMENTED`; body is generic Codex header (substantive content not at endpoint A).
- **Endpoint B** (`gh api repos/.../issues/35/comments`): only owner's `@codex review` invocation at UTC 2026-05-07T00:53:12Z. No Codex-side substantive content.
- **Endpoint C** (`gh api repos/.../pulls/35/comments`): 1 line-level review-comment, P2 (Major-tier) priority badge — substantive landing (consistent with PMN-008 §5.8 (h.4) cross-cycle pattern; TASK-0027 = data point 8 in (h.4) distribution).

Settling-period rule satisfied: formal review submitted +4 minutes from `@codex review` invocation; both endpoints stable.

**Verdict**: Major findings × 1 (P2 priority badge).

**Findings** (verbatim per `core.md` §8.1.1.2):

> **<sub><sub>![P2 Badge](https://img.shields.io/badge/P2-yellow?style=flat)</sub></sub>  Fix the invalid grep verification command**
>
> When a reviewer runs this verification claim exactly, GNU `grep -E` errors with `Unmatched ( or \(` rather than proving that the `linked_pr` regex anchor is documented, so the review-context now contains a false Builder-verification claim. In the pre-commit review workflow this line is intended to be copy-runnable evidence; use a literal match (`grep -F`) or a corrected ERE so claim 5 can actually be verified.
>
> Useful? React with 👍 / 👎.

**Adjudication** (per ADR-001 D11 + `core.md` §8.1.1.3 cost-class refinement; ratified at Architect step-13 §3):

- **Finding (P2)**: ratified path-(a) revise. Class: pure-token-swap (verification-command operational correctness; (h.2) sub-shape per PMN-009 canonical sub-shape framework). One-iteration convergence anticipated.

Bounded-continuation rule per `core.md` §8.1.1.3: one resolution iteration; if hypothetical Codex pass-2 surfaces 4th-instance (h.2) recurrence within TASK-0027, escalate per §8.1.1.3 cost-class refinement (genuinely-asymptotic distinction). Three-instance intra-cycle is at the bounded-continuation tolerance edge.

**Resolution applied** (path-(a)):

- **Edit R.5** (Codex post-PR Finding, review-context Claim 5 fourth bullet line 51): replaced invalid ERE-escaped command `grep -nE "^\\^linked_pr: PR-\\\\\\(d\\+\\\\\\) \\\\\\(Builder fills" templates/handoff-template.md` (which errored `Unmatched ( or \(` under GNU `grep -E`) with `grep -F '^linked_pr: PR-(\d+) \(Builder fills with squash SHA post-merge per PMN-001 \(k\)\)' templates/handoff-template.md` (Builder Option (i) fixed-string match form ratified at Architect §3). Empirical: returns 3 lines covering (a) canonical regex anchor code-block + (b) positive `PR-1` python verification example + (c) counter-example `PR-XX` python verification — all three lines reference the same canonical regex literal. Verifiable at next-iteration: command runs without ERE-parse errors and returns exactly 3 lines. Verified via Bash inline at Edit application.

**Pass-2 self-review iteration-1** per `core.md` §23.6.2 + bounded-continuation per §8.1.1.3: focused on R.5 edit site + Codex finding scope; no new defects surfaced; convergence at iteration 1; pure-token-swap class; no same-class recurrence.

**Cycle-close ledger entry queued** (lightweight per ADR-006 D3 + Architect §4 ratification):
- **Item 9 — (h.2) intra-cycle recurrence empirical observation**: 3-instance (h.2) cluster within TASK-0027 (Codex pre-commit R.1.1+R.1.2 + Codex pre-commit R.3 + Codex post-PR R.5). (h.2) is already canonical at PMN-009 sub-shape framework; intra-cycle recurrence is empirical confirmation of existing canonical, not new defect class. Builder-side authoring discipline observation: verification-claim authoring against template-content-with-embedded-regex-patterns surfaces (h.2) at higher intra-cycle rate when templates with regex content are the authoring substrate. Single-cycle observation; carry-forward for monitoring at future template-content cycles (Batch P1 continuing TASK-0028+). Empirically strengthens (k.1) MEDIUM-HIGH framing (multi-surface review pipeline catches (h.2) drift at distinct surfaces, individually one-iteration-resolved). [Amended at pass-2: 4th-instance recurrence observed at templates/handoff-template.md:21 inline YAML annotation; recursive defect at R.1.1 → R.6 chain; see ledger Item 1 + Item 9 amendments + new Item 10 in handoff §10.]

### Codex post-PR pass 2 (UTC 2026-05-07T01:52:59Z)

Three-endpoint poll evidence per `core.md` §8.1.1.1 (cumulative across passes):
- **Endpoint A** (`gh pr view 35 --json reviews`): 2 formal reviews — pass-1 @ T00:57:20Z (reviewed `5cb5ba8`) + pass-2 @ T01:52:59Z (reviewed `602a0de`); both `COMMENTED` state with generic Codex headers.
- **Endpoint B** (`gh api repos/.../issues/35/comments`): 2 owner `@codex review` invocations.
- **Endpoint C** (`gh api repos/.../pulls/35/comments`): 3 cumulative line-level review-comments — pass-1 R.5 absorbed + 2 NEW pass-2 findings (1 P2 + 1 P3). Substantive landing endpoint C confirmed across both passes (TASK-0027 = data point 8 in PMN-008 §5.8 (h.4) cross-cycle distribution; both passes reinforce (h.4) empirical pattern).

**Verdict**: Major findings × 1 (P2) + Minor findings × 1 (P3).

**Findings** (verbatim per `core.md` §8.1.1.2):

> **<sub><sub>![P2 Badge](https://img.shields.io/badge/P2-yellow?style=flat)</sub></sub>  Remove the non-matching inline linked_pr comment**
>
> When a Builder copies this frontmatter block and replaces `PR-N` with a real number, the appended YAML comment still makes the `linked_pr` line fail the exact regex used by `.github/scripts/linked-pr-fix-up.py` (`$` only permits trailing whitespace). In that scenario the post-merge fix-up Action silently leaves the durable handoff's `linked_pr` placeholder unsubstituted, even though this template is meant to be the canonical copy source; move the guidance out of the field line so the sample itself matches the required form.
>
> Useful? React with 👍 / 👎.

> **<sub><sub>![P3 Badge](https://img.shields.io/badge/P3-lightgrey?style=flat)</sub></sub>  Keep linked-pr-fix-up outside the nine-action count**
>
> This cross-reference contradicts ADR-006's own Batch P4 definition, which lists nine canonical action stubs and says `linked-pr-fix-up.yml` was shipped separately as additive, not subtractive. If future builders plan Batch P4 from this summary, it understates the remaining canonical action work as eight instead of nine and can leave one scaffold action unfilled; describe ADR-004 as separately shipped/additive rather than `1-of-9`.
>
> Useful? React with 👍 / 👎.

**Adjudication** (per ADR-001 D11 + `core.md` §8.1.1.3 cost-class refinement; ratified at Architect step-13-pass-2 §3):

- **Finding 1 (P2)** at templates/handoff-template.md:21: ratified path-(a) revise. Class: pure-token-swap (h.2) verification-command operational correctness — recursive instance introduced by Edit R.1.1 inline annotation. **4th-instance (h.2) intra-cycle recurrence**; Architect step-back diagnosis closed-the-loop in-cycle (per §2 step-back analysis): R.6 structural reframe (strip annotation entirely) eliminates recurrence at root; bounded-continuation rule + cost-class refinement validates itself empirically per (k.1) MAXIMUM tier framework.
- **Finding 2 (P3)** at docs/adr/ADR-006-...md:95: ratified path-(a) revise. Class: pure-token-swap; same defect-class cluster as R.2.1+R.2.2 (substantive content correctness — ADR-004 framing additive vs subtractive). Finishes (j)-sweep on R.2 defect class at §Cross-references surface that R.2.1+R.2.2 didn't cover.

**Bounded-continuation budget reset** post-R.6+R.7 per Architect §7: pass-3 hypothetical within budget; R.6 structural reframe eliminates recurrence root (no annotation to fail-regex post-R.6); future findings would be net-new defect classes, not (h.2) at same location. If pass-3 surfaces 5th-instance (h.2) at different location, re-assess; otherwise proceed to step-17 hand-back.

**Resolution applied** (path-(a)):

- **Edit R.6** (Finding 1, P2; templates/handoff-template.md:21): stripped inline `# N MUST be numeric digits per .github/scripts/linked-pr-fix-up.py:35 regex (\d+); literal "N" / "XX" / "####" cause Action to silently skip substitution` annotation from `linked_pr:` line. Post-edit form: `linked_pr: PR-N (Builder fills with squash SHA post-merge per PMN-001 (k))` (byte-exact regex-matching when adopters substitute `PR-N` with `PR-<digits>`). MC-C "Frontmatter conformance discipline" prose subsection IMMEDIATELY BELOW the YAML block preserves all explanatory discipline (regex form documented; drift consequences enumerated; positive `PR-1` Match + counter-example `PR-XX` None verification commands present). Other inline comments on non-regex-constrained fields (`pr:` / `branch:` / `linked_successor:` / `framework_version_dogfooded:` / `production_target:` / `spec_source:`) preserved verbatim — no defect at those sites; their fields don't have canonical-regex constraints. Verifiable at next-iteration: substituting `PR-N` with concrete digits in the template's `linked_pr:` line and applying `.github/scripts/linked-pr-fix-up.py:35` regex returns Match (no annotation tail to fail `[ \t]*$` tolerance).
- **Edit R.7** (Finding 2, P3; docs/adr/ADR-006-product-delivery-pivot-pr-plan-amendment.md:95): replaced `**ADR-004** linked-pr-fix-up Action ship; counted in Batch P4 as 1-of-9 already shipped.` with `**ADR-004** linked-pr-fix-up.yml shipped via ADR-004 operational insertion ahead of canonical Actions batch (additive to the 9-Action scaffold, not subtractive); see Decision 2 Batch P4 row for canonical framing.`. Verifiable at next-iteration: `grep -nE "1-of-9 already shipped" docs/adr/ADR-006-product-delivery-pivot-pr-plan-amendment.md` returns 0 lines (defective framing fully removed); `grep -nE "additive to the 9-Action scaffold, not subtractive" docs/adr/ADR-006-product-delivery-pivot-pr-plan-amendment.md` returns ≥1 line (R.2.1 + R.2.2 + R.7 (j)-sweep complete across 3 sites: §Context bullet + Batch P4 row + §Cross-references).

**Pass-2 self-review iteration-1** per `core.md` §23.6.2 + bounded-continuation per §8.1.1.3: focused on R.6 + R.7 edit sites + Codex finding scope; no new defects surfaced; convergence at iteration 1; pure-token-swap class × 2; no same-class recurrence post-R.6 structural reframe.

**Cycle-close ledger amendments** queued (per Architect step-13-pass-2 §6):
- **Item 1 amendment**: (k.1) salience MEDIUM → MEDIUM-HIGH (step-10-resolution) → MAXIMUM (step-13 pass-2). Recursive R.1.1 → R.6 chain at line 21 documented; ADR-006 D3 cadence-relaxation discipline empirically self-validating at MAXIMUM tier per PMN-008 §3.1 framework.
- **Item 9 amendment**: (h.2) intra-cycle recurrence framing strengthened: "single-cycle observation, 3-instance count" → "4-instance count + recursive (k.1) MAXIMUM at R.1.1 → R.6". (h.2) sub-shape canonical at PMN-009 already; cycle's empirical record strengthens existing canonical, not new sub-shape.
- **Item 10 NEW (template-content authoring meta-pattern)**: structural tension between byte-exact-canonical-form-as-copy-source vs explanatory-annotation-needs. Resolution pattern: byte-exact regions byte-exact ONLY; discipline at adjacent prose surfaces. Single-cycle observation; multi-cycle confirmation at Batch P1 continuation. Lightweight canonical absorption candidate at TASK-0028+ (`core.md` §23.6.3 sub-shape A 2-3 line enumeration addition codifying: "When prescribing edits for templates that are copy-sources for canonical-regex-bound content, byte-exact regions must remain byte-exact. Explanatory discipline belongs at adjacent prose surfaces, NOT inline within regex-bound regions. The regex's tolerance window (e.g., `[ \t]*$`) governs what may follow the canonical content on the same line.").
- **Item 11 NEW (R.7 (j)-sweep continuation)**: R.2 defect class (ADR-004 framing additive vs subtractive) had third surface at ADR-006:95 §Cross-references not covered by R.2.1+R.2.2 (j)-sweep at Codex pre-commit. Pre-(j)-sweep enumeration completeness candidate observation; carry-forward.

### Codex post-PR pass 3 (UTC 2026-05-07T11:07:28Z)

Three-endpoint poll evidence per `core.md` §8.1.1.1 (cumulative across passes):
- **Endpoint A**: 3 formal reviews — pass-1 @ T00:57:20Z (`5cb5ba8`) + pass-2 @ T01:52:59Z (`602a0de`) + pass-3 @ T11:07:28Z (`6d6f3b76c2`); all `COMMENTED` state with generic Codex headers.
- **Endpoint B**: 3 owner `@codex review` invocations.
- **Endpoint C**: 4 cumulative line-level review-comments — pass-1 R.5 (absorbed) + pass-2 R.6 + R.7 (absorbed) + 1 NEW pass-3 P2 finding. Substantive landing endpoint C confirmed across all 3 passes; reinforces PMN-008 §5.8 (h.4) cross-cycle pattern at empirical-pattern data point 8 with three intra-cycle confirmations.

Settling-period: ~4 minutes per pass (pass-1, pass-2, pass-3 all ~4 min from invocation to formal review). Stable empirical cadence.

**Verdict**: Major findings × 1 (P2).

**Findings** (verbatim per `core.md` §8.1.1.2):

> **<sub><sub>![P2 Badge](https://img.shields.io/badge/P2-yellow?style=flat)</sub></sub>  Correct the PR-35 sweep claim for ADR-006**
>
> When claim 16 is checked, `docs/adr/ADR-006-product-delivery-pivot-pr-plan-amendment.md` is actually in the result set because ADR-006 line 84 mentions `PR-35 (TASK-0027)`, so the parenthetical `ADR-006 not present` is a false Builder-verification claim. In this review-context workflow, readers use these sweep records to prove which surfaces were checked; leaving ADR-006 documented as absent can cause that ADR surface to be skipped in later claim verification.
>
> Useful? React with 👍 / 👎.

**Adjudication** (per ADR-001 D11 + `core.md` §8.1.1.3 cost-class refinement; ratified at Architect step-13-pass-3 §1):

- **Finding (P2)** at docs/reviews/PR-35-codex-pre-commit.md:101: ratified path-(a) revise. Class: pure-token-swap (h.2) verification-command operational correctness — 5th-instance (h.2) at different location (NOT recursive R.1.1 → R.6 cycle). One-iteration convergence anticipated.

**Re-assessment per Architect step-13-pass-2 §7 trigger** (5th-instance (h.2) at different location): completed at Architect step-13-pass-3 §2 + §3 — bounded-continuation rule continues to apply per `core.md` §8.1.1.3 cost-class refinement (per-pass rate trajectory 2 → 1 → 1 → 1 = decreasing, NOT genuinely-asymptotic; high-density-of-claim-surfaces cycle is the driver, not asymptotic loop). Each individual finding remains pure-token-swap one-iteration; no cascade at fix-location.

**Sub-cluster diagnosis**: 3 of 5 (h.2) instances cluster at "Builder-claims-to-verify forward-looking claims" sub-shape (R.3 + R.5 + R.8) — common authoring mechanism: claims authored as anticipated-prose rather than verify-at-authoring-output. Builder writes prose enumerating expected output without running the verification command at authoring time AND incorporating actual output verbatim. PMN-009 (h.2) sub-shape canonical mechanism applies recursively to claim-authoring surface. **Lightweight canonical absorption candidate at TASK-0028+** per Architect §3 ratification (Item 12 NEW in cycle-close ledger): 1-2 line addition to PMN-007 §2.4 (j)-sweep discipline OR `core.md` §23.6.3 sub-shape A enumeration codifying Builder-side verification-claim authoring sub-rule.

**Resolution applied** (path-(a)):

- **Edit R.8** (Pass-3 P2 finding, review-context Claim 16 line 101): replaced false `ADR-006 not present per Decision 4 forward-reference convention` parenthetical with empirically-correct 7-site enumeration restoring intra-document consistency between Claim 16 and Builder's own step-10 stop-and-show §4 (j)-sweep table. Verifiable at next-iteration: `grep -rln "PR-35" --include="*.md" .` returns 7 committed-tree files matching the enumeration (TASK-0027 handoff + PR-35 review-context + README + handoff-template + review-template + core.md + ADR-006); `grep -nE "ADR-006 not present" docs/reviews/PR-35-codex-pre-commit.md` returns 0 lines (false-claim parenthetical fully removed).

**Pass-3 self-review iteration-1** per `core.md` §23.6.2 + bounded-continuation per §8.1.1.3: focused on R.8 edit site + Codex pass-3 finding scope; no new defects surfaced; convergence at iteration 1; pure-token-swap class; no same-class recurrence at R.8 site.

**Cycle-close ledger amendments** queued (per Architect step-13-pass-3 §4):
- **Item 9 amendment** (4-instance → 5-instance): "(h.2) intra-cycle recurrence count = 5 with sub-cluster decomposition: Builder-claims-to-verify (3 instances: R.3 + R.5 + R.8) + template-byte-exact-regex (2 instances: R.1.1 + R.6 recursive chain). Per-pass rate 2→1→1→1 (decreasing); not genuinely-asymptotic per `core.md` §8.1.1.3. Lightweight canonical absorption candidate at TASK-0028+ for Builder-claims-to-verify sub-cluster sub-rule."
- **Item 12 NEW (Builder-claims-to-verify authoring discipline lightweight canonical absorption candidate)**: 1-2 line addition to PMN-007 §2.4 (j)-sweep discipline OR `core.md` §23.6.3 sub-shape A enumeration codifying: "Builder-side verification-claim authoring sub-rule: When authoring review-context Claims-to-verify with bash/PowerShell verification commands, run the command at authoring time against the staged-tree state and incorporate actual output verbatim into claim prose. Anticipated-prose claims (authored without running the command) systematically produce (h.2) operational-correctness drift; PMN-009 (h.2) sub-shape canonical mechanism applies recursively to claim-authoring surface itself." Carry-forward to TASK-0028+ adjudication; could ride along with Item 10 template-content authoring sub-rule + Item 11 (j)-sweep enumeration completeness sub-rule as bundled lightweight canonical amendment cycle.

### Codex post-PR pass 4 (UTC 2026-05-07T13:04:41Z)

Three-endpoint poll evidence per `core.md` §8.1.1.1 (cumulative across passes):
- **Endpoint A**: 4 formal reviews — pass-1 @ T00:57:20Z (`5cb5ba8`) + pass-2 @ T01:52:59Z (`602a0de`) + pass-3 @ T11:07:28Z (`6d6f3b76c2`) + **pass-4 @ T13:04:41Z (`76c650d`)**; all `COMMENTED` state with generic Codex headers.
- **Endpoint B**: 3 owner `@codex review` invocations recorded (4th may be in flight).
- **Endpoint C**: 6 cumulative line-level review-comments — pass-1 R.5 (absorbed) + pass-2 R.6 + R.7 (absorbed) + pass-3 R.8 (absorbed) + 2 NEW pass-4 findings (1 P2 + 1 P3). Substantive landing endpoint C confirmed across all 4 passes.

**Verdict**: Major findings × 1 (P2) + Minor findings × 1 (P3).

**Findings** (verbatim per `core.md` §8.1.1.2):

> **<sub><sub>![P2 Badge](https://img.shields.io/badge/P2-yellow?style=flat)</sub></sub>  Update stale package-plan rows with the pivot**
>
> After this new roadmap makes ADR-006 the governing plan, the Package layout table still advertises the superseded ADR-003 PR slots for unfilled work (for example prompts at PR-14, actions at PR-15, appendices at PR-16/17/18). In the context where an adopter or future Builder uses README as the package-status index, this contradicts the batch plan introduced here and preserves the exact stale-forecast defect ADR-006 says it is correcting; either point those rows at ADR-006/batches or otherwise mark them as superseded until filled.
>
> Useful? React with 👍 / 👎.

> **<sub><sub>![P3 Badge](https://img.shields.io/badge/P3-lightgrey?style=flat)</sub></sub>  Keep ADR-004 out of the nine-action count**
>
> In this handoff metadata, ADR-004 is still described as `counted in Batch P4 as 1-of-9 already shipped`, but ADR-006 now defines `linked-pr-fix-up.yml` as shipped separately and additive to the nine canonical action stubs. When someone resumes TASK-0027 or plans Batch P4 from the handoff rather than the ADR, this understates the remaining action work by one and reintroduces the same count drift fixed elsewhere in ADR-006.
>
> Useful? React with 👍 / 👎.

**Adjudication** (per ADR-001 D11 + `core.md` §8.1.1.3 cost-class refinement; ratified at owner-direction 2026-05-07):

- **Finding 1 (P2)** at README.md:30 area (Package layout): substantive scope question — ADR-006 D2 falsified the ADR-003 forecast for Batch P3-P7 PR slots (PR-14 through PR-18) but README rows still advertised them. Owner ratified **Option (10.ii) supersession marking** on all stale-forecast rows (~38 sweep-2 estimate; 45 empirical post-PR-12-Batch-P1-remaining inclusion). Class: substantive content correctness — distributed-update discipline coverage of unfilled rows post-partial-supersession event. NEW class this cycle. Owner reasoning: shipping ADR-006 alongside README rows that advertise the falsified forecast is the same defect class ADR-006 was authored to prevent.
- **Finding 2 (P3)** at handoff:23 (Linked ADR(s) Metadata): R.2-family 4th site (ADR-004 framing additive vs subtractive). Class: substantive content correctness; pre-(j)-sweep enumeration completeness candidate observation strengthening per Item 11 NEW. Owner ratified path-(a) revise.

**Defect-class classification**: Pass-4 findings are NOT (h.2) verification-command operational correctness. (h.2) cumulative count remains at 5 from pass-3 (no new (h.2) at pass-4). Per-pass (h.2) rate trajectory: 2 → 1 → 1 → 1 → **0**. Pass-4 0-(h.2) count empirically confirms Architect step-13-pass-3 §2 cost-class analysis (decreasing per-pass rate; not genuinely-asymptotic).

**Resolution applied** (path-(a)):

- **Edit R.9** (Pass-4 Finding 2 P3, handoff:23 Linked ADR(s) Metadata): replaced `ADR-004 (linked-pr-fix-up Action; counted in Batch P4 as 1-of-9 already shipped)` with `ADR-004 (linked-pr-fix-up.yml shipped via ADR-004 operational insertion ahead of canonical Actions batch; additive to the 9-Action scaffold, not subtractive; see ADR-006 Decision 2 Batch P4 row for canonical framing)`. R.2-family (j)-sweep continuation closes 4th site (R.2.1 + R.2.2 ADR-006 §Context + Batch P4 row at Codex pre-commit pass-1; R.7 ADR-006:95 §Cross-references at Codex post-PR pass-2; R.9 handoff:23 at Codex post-PR pass-4). Verifiable at next-iteration: `grep -nE "1-of-9 already shipped" docs/handoffs/TASK-0027-product-delivery-pivot.md` returns 0 lines.
- **Edit R.10** (Pass-4 Finding 1 P2, README Package layout supersession marking sweep): applied Option (10.ii) supersession marking on all stale-forecast rows. **Empirical count: 45 rows** (Builder pre-edit sweep 2 estimated 38 with regex `PR-1[3-8]`; the 7 Batch P1 remaining rows at PR-12 were missed by the regex; total empirical = 38 + 7 = 45). Per-batch breakdown: Batch P1 (7 rows) + Batch P2 (7 rows) + Batch P3 (3 rows) + Batch P4 (9 rows) + Batch P5 (7 rows) + Batch P6 (5 rows) + Batch P7 (7 rows) = 45. Cell form replacement: `PR-N (TASK-NNNN)` → `Batch P[X] (ADR-006); pending content-fill cycle`. Disambiguation handled at PR-17 (TASK-0017): line 41 `github-reference.md` row preserved as historical fill record (NOT stale forecast); only the 5 project-type appendices rows at lines 105-109 updated. Verifiable at next-iteration: `grep -cF "(ADR-006); pending content-fill cycle" README.md` returns 45; `grep -nF "PR-17 (TASK-0017)" README.md` returns exactly 1 line at line 41 (github-reference.md historical fill preserved); `grep -cE "PR-1[2-8] \(TASK-001[2-8]\)" README.md` returns 1 (only the line-41 historical fill remaining).

**Pass-4 self-review iteration-1** per `core.md` §23.6.2 + bounded-continuation per §8.1.1.3: focused on R.9 + R.10 edit sites + Codex pass-4 finding scope; no new defects surfaced; convergence at iteration 1; pure-token-swap class × 1 (R.9) + bulk-substitution class × 1 (R.10 supersession marking sweep with disambiguation); no same-class recurrence.

**Cycle-close ledger amendments** queued (per owner 2026-05-07 ratification + Architect step-13-pass-3 prior amendments):
- **Item 11 amendment**: pre-(j)-sweep enumeration completeness candidate observation strengthened to **4-instance R.2-family count** (R.2.1 + R.2.2 caught at pre-commit pass-1; R.7 caught at post-PR pass-2; R.9 caught at post-PR pass-4) confirming the multi-document distinct-section enumeration discipline gap empirically.
- **Item 14 NEW (Distributed-update discipline coverage of unfilled rows post-partial-supersession event)**: ADR-003 §Consequences distributed-update discipline ("filled at content-fill time") interacted with ADR-006 partial-supersession event to leave ~45 README rows advertising the falsified forecast post-amendment; Codex pass-4 P2 surfaced this as substantive scope question; owner ratified Option (10.ii) supersession marking sweep within-cycle. Pattern: when a partial-supersession ADR amends a forecast that was previously documented in distributed surfaces, the distributed-update discipline must be applied retroactively to the rows whose forecasts the partial-supersession falsified — NOT just at "content-fill time" of each individual row. Lightweight canonical absorption candidate at TASK-0028+: 1-2 line addition to ADR-006 §Consequences distributed-update discipline OR PMN-007 §2.4 enumeration codifying the retroactive-supersession-marking sub-rule. Single-cycle observation; carry-forward.

**Bounded-continuation budget post-R.9+R.10** per owner 2026-05-07 direction §3: **no pass-5**. Pass-4 zero-(h.2) trajectory + ADR-006 D3 ship-product framing + Architect §24.3.1 five-point check at step-17 as next pipeline surface. Anything missed surfaces at next-cycle review (TASK-0028+ Batch P1 continuation) and absorbs incrementally per framework design.
