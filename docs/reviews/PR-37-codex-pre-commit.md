---
status: drafted
---

# PR-37 Codex desktop pre-commit review

## Metadata

- PR ID: PR-37 (anticipated; pre-PR-open authoring per spec sub-shape E provisional handling; verified at pre-flight via `gh pr list --state open` returning zero)
- TASK ID: TASK-0028
- Branch: `chore/task-0028-bundled-lightweight-absorption-m-a7` (Option B canonical form per ADR-005; chore-type per cycle class; matches `^(feat|fix|chore|adr|shadow|spike)/task-[0-9]{4}-([a-z0-9]|[a-z0-9][a-z0-9.-]*[a-z0-9])$` regex)
- Linked handoff: docs/handoffs/TASK-0028-bundled-lightweight-absorption-m-a7.md
- Base SHA: `ac5d3b831ca124e2ae77adaecceabbfc9aeefc78` (squash-merge of PR-36 chore on main, 2026-05-07T13:28:24Z; PR-36 = TASK-0027 linked-PR substitution chore-fix-up auto-fired by linked-pr-fix-up Action shipped at PR-21)
- Builder: Claude Code (Claude Opus 4.7, Windows 11 + PowerShell + Git Bash)
- Reviewer: Codex (GPT-5.5) — desktop, pre-commit, staged working tree per TASK-0025 cycle-close Item 4 lesson (claims align to staged-tree state at pre-commit time)
- Architect (this PR's): Claude Opus 4.7 (Claude.ai Project)
- Owner: Bryce Murphy (`@bryce-murphy`)
- Status: drafted (post-stage / post-Codex-pre-commit-pass-1 / post-Codex-post-PR-pass-1 / post-Codex-post-PR-pass-2; transitions to recorded post-merge per linked-pr-fix-up Action substitution per PMN-001 (k); refreshed at step-14.5 R2 path-(a) per Codex post-PR pass-2 + Architect MAXIMAL-enumeration-directive 2026-05-07)
- Codex desktop session timestamps (UTC): pre-commit pass-1 absorbed at step-11.1 (R.1/R.2/R.3 path-(a) one-iteration convergence); post-PR pass-1 absorbed at step-14 (R.4/R.5 path-(a) one-iteration convergence; UTC 2026-05-07T18:26:30Z formal-review submitted_at; reviewed commit c72a727); post-PR pass-2 absorbed at step-14.4 (R.6-R.21 path-(a) MAXIMAL-enumeration-directive convergence target; UTC 2026-05-07T18:47:17Z formal-review submitted_at; reviewed commit eb7f7ed)
- Framework version: AMAS v2.24 → v2.25 (Class A v-bump at this cycle per `core.md` §18.4 patch tier — lightweight canonical-text refinement criterion). First execution of ADR-006 D3 lightweight-absorption framework. Recursive-self-instantiation salience MEDIUM this cycle: cycle's content provides direct empirical evidence for ADR-006 D3 lightweight-absorption framework adopter-experienced cost-benefit; (k.1) positive self-instantiation candidate at any successful lightweight Item absorption; cycle's edits include amending the very disciplines (§23.6.3 sub-shape A; PMN-007 (j); PMN-007 (i)) being applied to spec authoring + Builder execution.
- Severity taxonomy: Blocking / Major / Minor (three-level; per repo discipline; standing per PMN-004 §5 (a)).
- Disciplines applied: PMN-001 (k) (linked-pr-fix-up substitution discipline; canonical regex empirical pre-application via PowerShell match returning `MATCH: PR-37` at pre-flight) + PMN-002 (a) (verbatim-output convention for Codex absorption) + PMN-002 (d) (code-fenced kickoff prompt convention) + PMN-004 §5 (a)-(f) + PMN-007 §3.3 + §9.1 (amended this cycle with cross-cycle empirical strengthening + verify-at-authoring vs anticipated-prose distinction) + PMN-007 HEAD canonical 12-field handoff frontmatter form (applied at TASK-0028 handoff frontmatter) + PMN-008 §3.1 (k.1) positive self-instantiation framework + PMN-008 §4.2 (i.5) convention-inference verification + PMN-009 / `core.md` §23.6.3 (sub-shape A verify-at-authoring batch applied at Architect spec authoring; Items 4+10 amend §23.6.3 sub-shape A discipline this cycle) + PMN-010 §2 sub-shape 1 (forward-ref §-citation correctness applied at all 6 byte-exact prescription targets line-number identification) + `core.md` §8.1.1.3 bounded-continuation rule with cost-class refinement + ADR-006 Decision 3 evidence-bar PMN-after-cycle cadence relaxation (this cycle's first execution as substantive-content cycle in lightweight-absorption form).
- Substantive-content-cycle context: PR-37 ships 6 substantive canonical-text edits in a single PR per single-PR-with-split-trigger discipline (TASK-0012 Part B precedent extended through TASK-0027). All five absorption Items (4 + 10 + 11 + 12 + 14) absorbed lightweight per ADR-006 D3 evidence-bar discipline at existing canonical anchors plus M-A7 14th-instance amendment plus Class A v2.24 → v2.25 patch v-bump. Cycle-class chore: first execution of ADR-006 D3 lightweight-absorption framework. Anticipated cumulative-diff-stats: ~261-369 ins / ~3 del across ~8 files. Order of magnitude smaller than TASK-0027 (1038/58/10) — first concrete demonstration of ADR-006 D3 lightweight-absorption framework efficiency. Step-1 pre-flight stop-and-show surfaced 3 open adjudications (patch-vs-minor v-bump tier; PR-37 M-A7 inclusion eligibility; §23.6.3 sub-shape A insertion structural placement); Architect ratified all three Builder recommendations 2026-05-07.

## Builder claims to verify

The Builder asserts the following at hand-off to Codex desktop pre-commit review. Each claim is verifiable from the working tree at staged-tree state per (e.1) sub-rule + TASK-0025 cycle-close Item 4 lesson; verify-at-authoring shape per PMN-007 §9.1 amendment this cycle (no anticipated-prose claims). PR-37 ships ADR-006 §Consequences amendment + PMN-007 §3.3 amendment + PMN-007 §9.1 amendment + core.md §23.6.3 sub-shape A amendment + core.md §18.3 M-A7 14th-instance amendment + README/AGENTS/CLAUDE Class A v-bump + TASK-0028 handoff + PR-37 review-context.

1. **Working-tree state at pre-commit (staged): 6 staged-modified + 2 staged-added**. Convention note: per TASK-0025 cycle-close Item 4 lesson, this cycle stages all changes before Codex pre-commit pass to align review-context claim-state with actual staged-tree state. Verifiable at pre-commit:
   - bash (staged-modified): `git status --porcelain | grep -c "^M "` returns `6` (6 staged-modified: `AGENTS.md` + `CLAUDE.md` + `README.md` + `core.md` + `docs/adr/ADR-006-product-delivery-pivot-pr-plan-amendment.md` + `docs/post-merge-notes/PMN-007-pr-13-cycle-learnings.md`).
   - bash (staged-added): `git status --porcelain | grep -c "^A "` returns `2` (2 staged-added: `docs/handoffs/TASK-0028-bundled-lightweight-absorption-m-a7.md` + `docs/reviews/PR-37-codex-pre-commit.md`).

2. **ADR-006 §Consequences Item 14 amendment — new bullet between distributed-update bullet and PMN insertion budget bullet**. Verifiable at pre-commit:
   - bash: `grep -nE "Decision 4 distributed-update discipline applies retroactively to forecasts falsified by partial-supersession" docs/adr/ADR-006-product-delivery-pivot-pr-plan-amendment.md` returns 1 line (line 78).
   - bash: `grep -n "Edit R.10" docs/adr/ADR-006-product-delivery-pivot-pr-plan-amendment.md` returns 1 line within new bullet.
   - bash: `grep -cE "^- \*\*" docs/adr/ADR-006-product-delivery-pivot-pr-plan-amendment.md` returns `27` (pre-cycle 26 + 1 new bullet).
   - Class: PMN-009 (i.5) sub-shape A verify-at-authoring + PMN-010 sub-shape 1 forward-ref §-citation correctness.

3. **PMN-007 §3.3 (j) sub-cluster amendment — append-paragraph documenting cross-cycle empirical strengthening**. Verifiable at pre-commit:
   - bash: `grep -nE "Cross-cycle empirical strengthening \(post-canonicalization, as of TASK-0027 / PR-35\)" docs/post-merge-notes/PMN-007-pr-13-cycle-learnings.md` returns 1 line (line 135).
   - bash: `grep -nE "pre-\(j\)-sweep enumeration completeness check" docs/post-merge-notes/PMN-007-pr-13-cycle-learnings.md` returns 1 line within new paragraph.
   - bash: `grep -nE "Lightweight canonical absorption at TASK-0028" docs/post-merge-notes/PMN-007-pr-13-cycle-learnings.md` returns ≥1 line (Items 11 + 12 both reference TASK-0028 absorption).
   - Class: PMN-009 (i.5) sub-shape A verify-at-authoring + PMN-010 sub-shape 1 forward-ref §-citation correctness.

4. **PMN-007 §9.1 (i) sub-cluster amendment — append-paragraph documenting verify-at-authoring vs anticipated-prose distinction**. Verifiable at pre-commit:
   - bash: `grep -nE "Additional refinement candidate \(post-canonicalization, as of TASK-0027\)" docs/post-merge-notes/PMN-007-pr-13-cycle-learnings.md` returns 1 line (line 272).
   - bash: `grep -nE "verify-at-authoring vs anticipated-prose distinction" docs/post-merge-notes/PMN-007-pr-13-cycle-learnings.md` returns 1 line within new paragraph.
   - bash: `grep -nE "Builder-claims-to-verify sub-cluster \(3 instances\)" docs/post-merge-notes/PMN-007-pr-13-cycle-learnings.md` returns 1 line within new paragraph (TASK-0027 (h.2) intra-cycle 5-instance recurrence empirical evidence).
   - Class: PMN-009 (i.5) sub-shape A verify-at-authoring + PMN-010 sub-shape 1 forward-ref §-citation correctness.

5. **core.md §23.6.3 sub-shape A discipline extensions — bold-headed paragraph + 2 enumerated bullets between Default-path-guidance pair and Architect adjudication-framework arithmetic**. Verifiable at pre-commit:
   - bash: `grep -nE "Sub-shape A authoring-time discipline extensions" core.md` returns 1 line (line 321).
   - bash: `grep -nE "Canonical-impact-surface-completeness check" core.md` returns 1 line (line 323) within new bullet.
   - bash: `grep -nE "Template-content authoring meta-pattern" core.md` returns 1 line (line 325) within new bullet.
   - bash: `grep -nE "TASK-0028 / PR-37 absorbing TASK-0026 \+ TASK-0027" core.md` returns 1 line at provenance preamble.
   - Class: PMN-009 (i.5) sub-shape A verify-at-authoring + PMN-010 sub-shape 1 forward-ref §-citation correctness.

6. **core.md §18.3 M-A7 14th-instance amendment — in-place v2.24 cumulative-instances paragraph refinement to 14-instance enumeration**. Verifiable at pre-commit:
   - bash: `grep -nE "as of v2\.25 canonicalization at PR-37 / TASK-0028" core.md` returns 1 line (line 238).
   - bash: `grep -nE "PR-9 \+ PR-10 \+ PR-11 \+ PR-13 \+ PR-15 \+ PR-17 \+ PR-19 \+ PR-21 \+ PR-25 \+ PR-27 \+ PR-29 \+ PR-31 \+ PR-33 \+ PR-35 = 14" core.md` returns 1 line (line 240).
   - bash: `grep -nE "spanning v2\.16 through v2\.24 canonicalization" core.md` returns 1 line.
   - bash: `grep -nE "14 consecutive substantive cycles" core.md` returns 1 line (line 242).
   - bash: `grep -nE "= 13" core.md` returns `0` lines (no residual 13-count enumeration).
   - bash: `grep -nE "spanning v2\.16 through v2\.23 canonicalization" core.md` returns `0` lines (replaced).
   - bash: `grep -nE "Four-instance evidence \(PMN-005" core.md` returns 1 line (original 4-instance grounding paragraph preserved post-amendment per spec §4.5 Note on append-vs-replace).
   - Class: PMN-009 (i.5) sub-shape A verify-at-authoring + PMN-010 sub-shape 1 forward-ref §-citation correctness + arithmetic-by-enumeration verification (count by enumeration: 14 PRs in chain).

7. **README.md Class A v-bump applied at line 9 (both v2.24 → v2.25)**. Verifiable at pre-commit:
   - bash: `grep -nE "v2\.24" README.md` returns `0` lines.
   - bash: `grep -oE "v2\.25" README.md | wc -l` returns `2` (both instances on line 9).
   - bash: `awk 'NR==9' README.md | grep -oE "v2\.25" | wc -l` returns `2`.
   - Class: PMN-009 (i.5) sub-shape A verify-at-authoring + Class A canonical-version-of-record (per TASK-0027 step-2 §6 ratification extending through this cycle).

8. **AGENTS.md + CLAUDE.md Class A v-bump applied at line 9 (single v2.24 → v2.25 inline-mention each)**. Verifiable at pre-commit:
   - bash: `grep -nE "v2\.24" AGENTS.md` returns `0` lines.
   - bash: `grep -nE "v2\.24" CLAUDE.md` returns `0` lines.
   - bash: `grep -nE "current canonical materialization at v2\.25 — see README" AGENTS.md` returns 1 line at line 9.
   - bash: `grep -nE "current canonical materialization at v2\.25 — see README" CLAUDE.md` returns 1 line at line 9.
   - Class: PMN-009 (i.5) sub-shape A verify-at-authoring + Class A canonical-version-of-record extension.

9. **(j) all-instances grep sweep — zero residual v2.24 across 3 Class A sites**. Verifiable at pre-commit:
   - bash: `grep -nE "v2\.24" README.md AGENTS.md CLAUDE.md` returns `0` lines (Class A surgical edit complete; no residual v2.24 at any of 3 Class A sites).
   - bash: `grep -nE "v2\.25" README.md AGENTS.md CLAUDE.md` returns `3` lines (4 matches total — README:9 has 2 v2.25 instances on the same line counted as 1 grep -n line; AGENTS:9 + CLAUDE:9 each contribute 1 line / 1 match). Match-count verification: `grep -oE "v2\.25" README.md AGENTS.md CLAUDE.md | wc -l` returns `4` (4 match-occurrences). Per Codex pre-commit pass-1 Minor 1 absorption: `-n` returns matched-line addresses while `-o` returns match-occurrences; clarification preserves substantive correctness while disambiguating count semantic.
   - Class: PMN-007 §3.3 (j) all-instances propagation-residual sweep + canonical-impact-surface-completeness check per Items 4+10 amendment this cycle.

10. **Frontmatter shape conformance — TASK-0028 handoff PMN-007 HEAD canonical 12-field + PR-37 review-context 1-field**. Verifiable at pre-commit:
    - bash: `head -14 docs/handoffs/TASK-0028-bundled-lightweight-absorption-m-a7.md` shows 12-field frontmatter with `task_id: TASK-0028` + `framework_version_dogfooded: AMAS v2.24` + `status: active` (refreshed at step-14.5 R6 path-(a) per Codex post-PR pass-2 Finding 2 absorption: status flipped drafted→active at step-11.1 R.2 absorption per template lifecycle pre-stage→post-stage; verification claim now matches actual frontmatter state).
    - bash: `grep -cE "^(task_id|title|pr|branch|linked_predecessor|linked_successor|linked_pr|framework_version_dogfooded|production_target|spec_source|date_authored|status):" docs/handoffs/TASK-0028-bundled-lightweight-absorption-m-a7.md` returns `12`.
    - bash: `grep -cE "^linked_pr: PR-37 \(Builder fills with squash SHA post-merge per PMN-001 \(k\)\)$" docs/handoffs/TASK-0028-bundled-lightweight-absorption-m-a7.md` returns `1` (canonical placeholder regex form per `.github/scripts/linked-pr-fix-up.py:35` empirically pre-applied via PowerShell match returning `MATCH: PR-37`).
    - bash: `head -3 docs/reviews/PR-37-codex-pre-commit.md` shows `status: drafted` 1-field frontmatter.
    - Class: PMN-009 (i.5) sub-shape D convention-inference + MC-C frontmatter conformance discipline per templates/handoff-template.md substantive content.

11. **Cumulative-diff-stats per `core.md` §23.6.1.1 (e.1) staged-tree convention** — landed-exact cumulative-from-origin/main at HEAD post-step-14.7 R.6-R.21 MAXIMAL-enumeration-directive fix-up staging. Spec §1.1 anticipation ~261-369 ins / ~3 del across ~8 files; cumulative ins +23.1% above ±20% MC-A tolerance upper bound (442.8 ins) attributable to recursive absorption-iteration overhead at MAXIMUM-salience cycle; cumulative del 6 stable from step-11.1 — fix-up del-from-prior-commits targeted Builder-authored content cancelling at cumulative-from-origin/main level (structurally-distinct pattern from substantive-cycle del trajectory; informational MC-A 4th-cycle data point per cycle-close ledger Item 4). Order of magnitude smaller than TASK-0027 (1038/58/10) per ADR-006 D3 lightweight-absorption efficiency despite recursive overhead. Verifiable at staged-tree state:
    - bash: `git diff --shortstat ac5d3b8 HEAD` returns `8 files changed, 618 insertions(+), 6 deletions(-)` at HEAD 741005d post-step-14.7-fix-up-commit + R.18 within-surface sub-component-enumeration-directive staging per `core.md` §23.6.1.1 (e.1) cumulative-diff-stats re-derivation discipline (R.18 path-(a) absorption per Architect Option C ratification 2026-05-07 — Codex post-PR pass-3 sub-shape A finding refreshed coupled-shape sub-components SHA + timing-qualifier; original R.7 at step-14.5 staging populated value 545 anchored to pre-pass-4-staging which was internally inconsistent — pass-3 caught the within-surface absorption-completeness gap; R.18 corrects). Cumulative reflects R.6-R.17 fix-up delta landed at step-14.7 commit 741005d + R.18 sub-component-enumeration delta.
    - Class: PMN-005 (e.1) cumulative-diff-stats re-derivation + PMN-007 §9.1 verify-at-authoring discipline absorbed this cycle (cumulative-from-origin/main re-derived per Architect §24.3.1 Item 4 cross-check directive rather than fix-up-commit-relative shape) + Item 11 sweep-target enumeration completeness (this surface enumerated R7 in step-14.5 MAXIMAL-enumeration list) + within-surface sub-component-enumeration sub-discipline (cycle-close ledger Item 14; this surface enumerated R.18b in step-16 within-surface sub-component-enumeration list).

12. **M-A7 enumeration arithmetic verification** — count by enumeration, not by claim per spec §3.5: `PR-9 + PR-10 + PR-11 + PR-13 + PR-15 + PR-17 + PR-19 + PR-21 + PR-25 + PR-27 + PR-29 + PR-31 + PR-33 + PR-35 = 14 PRs`. Builder enumeration: 1-PR-9, 2-PR-10, 3-PR-11, 4-PR-13, 5-PR-15, 6-PR-17, 7-PR-19, 8-PR-21, 9-PR-25, 10-PR-27, 11-PR-29, 12-PR-31, 13-PR-33, 14-PR-35. Arithmetic-by-enumeration confirmed = 14. Verifiable at pre-commit:
    - bash: `grep -oE '`PR-9 \+ PR-10[^`]+`' core.md | grep -oE 'PR-[0-9]+' | wc -l` returns `14` (scoped to the backtick-fenced M-A7 enumeration block specifically per Codex post-PR pass-1 Finding 2 R.5 absorption; tighter scope than line-grep because the enumeration line also references "PR-13" once outside the enumeration as the "M-A7 promotion event at PR-13 / v2.16" anchor — line-grep would return 15, contaminated by the prose reference). Empirical: command returns exactly `14` matching M-A7 enumeration arithmetic by enumeration. Builder enumeration verification (count by enumeration: 14 PRs in chain) is the primary check; scoped backtick-extraction grep is secondary.
    - Class: PMN-005 prose-arithmetic decomposition discipline (per `core.md` §23.6.1) + canonical-impact-surface-completeness check (per Items 4+10 amendment this cycle).

## Reviewer focus

- **Substantive content shape verification**: do all 6 byte-exact canonical-text edits match spec §4.1-§4.6 prescriptions byte-exactly? Particular attention to:
  - ADR-006 §Consequences new bullet position (between distributed-update bullet and PMN insertion budget bullet — preserves cluster-coherence framing).
  - PMN-007 §3.3 + §9.1 append-paragraph positions (after each section's existing close, before next §-heading).
  - core.md §23.6.3 bold-header + 2 enumerated bullets at line 321-325 (between Default-path-guidance pair end and Architect adjudication-framework arithmetic start per Architect step-1 (3a) ratification).
  - core.md §18.3 in-place v2.24 paragraph refinement (4 byte-exact substitutions: preamble + enumeration + span + count); original 4-instance grounding paragraph preserved per spec §4.5 Note on append-vs-replace.
  - Class A v-bump (4 byte-exact substitutions across 3 sites; zero residual v2.24).

- **§-citation correctness**: all §-citations resolve against current canonical state (post-edit core.md §-numbering preserved; PMN-007 §3.3 + §9.1 preserved as targets; ADR-006 §Consequences preserved as target).

- **Cumulative-diff-stats matches review-context claims**: `git diff --shortstat ac5d3b8 HEAD` returns `8 files changed, 618 insertions(+), 6 deletions(-)` landed-exact cumulative-from-origin/main at HEAD 741005d post-step-14.7-fix-up-commit + R.18 within-surface sub-component-enumeration-directive staging per Architect §24.3.1 cross-check Item 4 + step-15 MAXIMAL-enumeration-directive Item R9 + step-16 Option C within-surface sub-component-enumeration directive; del 6 stable from step-11.1 (cycle-close ledger Item 4 informational MC-A 5th-cycle data point per ledger Item 10).

- **Frontmatter shape conformance**: handoff 12-field PMN-007 HEAD canonical form + review-context 1-field canonical form; `linked_pr` regex form match per `.github/scripts/linked-pr-fix-up.py:35`.

- **(j)/(g)/(h)/(i) sweeps on review-context's own claim blocks** (per PMN-008 §5.8): claim-block §-citation enumeration completeness check; claim-statement formatting consistency; line-number references match staged-tree state.

- **Recursive-self-instantiation salience check** (per PMN-008 §3.1): MEDIUM this cycle. Document any (h.2) recurrence at this cycle's own canonical-text edits — would be direct empirical refutation of the very sub-rule being canonicalized at Items 4+10 (canonical-impact-surface-completeness check + template-content authoring meta-pattern). MEDIUM-HIGH escalation candidate if Phase 1 verification surfaces additional drift per spec §1.1 recursive-self-instantiation-salience monitoring.

- **Patch-tier v-bump verification**: cycle's edits empirically confirm sub-rule-refinement-at-existing-canonical-anchors classification (no new feature-class clusters / mechanisms / monitoring items / disciplines introduced). §18.4 patch criterion fits cleanly.

## Codex desktop pre-commit kickoff

```
Please review the pending changes on the current branch (chore/task-0028-bundled-lightweight-absorption-m-a7) per the review-context at docs/reviews/PR-37-codex-pre-commit.md. Working tree at staged-tree state per TASK-0025 cycle-close Item 4 lesson.

Cycle scope: TASK-0028 ships 6 substantive canonical-text edits in single PR per single-PR-with-split-trigger discipline — ADR-006 §Consequences amendment (Item 14 retroactive-supersession-marking sub-rule) + PMN-007 §3.3 amendment (Item 11 cross-cycle empirical strengthening + pre-(j)-sweep enumeration completeness check) + PMN-007 §9.1 amendment (Item 12 verify-at-authoring vs anticipated-prose distinction) + core.md §23.6.3 sub-shape A amendment (Items 4+10 bundle: canonical-impact-surface-completeness check + template-content authoring meta-pattern) + core.md §18.3 M-A7 14th-instance amendment (in-place v2.24 paragraph refinement to PR-35 = 14) + README/AGENTS/CLAUDE Class A v-bump (v2.24 → v2.25 patch tier per §18.4 lightweight canonical-text refinement criterion). Cycle-class chore: first execution of ADR-006 D3 lightweight-absorption framework. Anticipated cumulative-diff-stats ~261-369 ins / ~3 del across ~8 files (order of magnitude smaller than TASK-0027's 1038/58/10).

Pre-flight + step-1 stop-and-show context: Builder pre-flight (i.5) batch (sub-shapes a-h) verified clean — local main HEAD `ac5d3b8` matches PR-36 squash anticipation; zero open PRs (PR-37 next available); MC-C linked_pr canonical-regex empirical pre-application via PowerShell returning `MATCH: PR-37`; 6 byte-exact prescription target line numbers identified. Architect ratified all 3 open adjudications 2026-05-07: (1) patch v-bump tier (sub-rule refinements at existing anchors fit §18.4 patch criterion; precedent established for ADR-006 D3 lightweight-absorption cycles); (2) PR-37 inclusive M-A7 read (chore-class lightweight-absorption is structurally distinct from defect-fix patches and chore-fix-up substitution PRs; PR-37 candidate 15th-instance at TASK-0029+); (3) §23.6.3 sub-shape A insertion structural placement (after line 319 / before line 321 between Default-path-guidance pair end and Architect adjudication-framework arithmetic start; bold-header + 2 enumerated bullets form per spec §4.4).

Per ADR-001 D11 owner-invokes convention: please run pre-commit review, surface findings per severity (Blocking → handback; Major → path-(a)/(β); Minor → default path-(b)). Substantive verdict via formal review (`gh pr view` reviews endpoint) preferred; issue-comment summary acceptable; line-level review-comments acceptable.

Verbatim-output convention: capture review verbatim into the review-context file ## Codex desktop pre-commit output absorption section.
```

## Codex desktop pre-commit output absorption

```text
Codex desktop pre-commit review output (2026-05-07)

Review Summary

Findings

Blocking

None.

Major

1. [Major] Landed exact staged diff stats are not populated in the durable review artifacts.

   Evidence: `git diff --staged --shortstat origin/main` at review time, before recording this absorption output, returned `8 files changed, 339 insertions(+), 6 deletions(-)`. The review-context still says the cumulative-diff-stat claim is an "anticipated range ~261-369 ins / ~3 del" and that the command returns landed-exact placeholder text `N files changed, X insertions(+), Y deletions(-)` at `docs/reviews/PR-37-codex-pre-commit.md:93-94`; the Reviewer focus also says the landed-exact values were populated at `docs/reviews/PR-37-codex-pre-commit.md:112`. The handoff carries the same unresolved anticipated/projection shape at `docs/handoffs/TASK-0028-bundled-lightweight-absorption-m-a7.md:73` and `docs/handoffs/TASK-0028-bundled-lightweight-absorption-m-a7.md:159`.

   Why it matters: this is the same verify-at-authoring vs anticipated-prose class this PR is absorbing into PMN-007 §9.1. At pre-commit time the staged-tree exact value exists, so keeping placeholders/ranges in the Builder-claims-to-verify and handoff validation surfaces makes the durable artifacts internally false even though the actual diff is within the anticipated range.

   Recommendation: path-(a) revise the review-context and handoff to include the exact staged shortstat for the final post-absorption/fix-up tree, re-derived after all review-output and finding-fix edits, and, if useful, the per-file numstat already verified during this pass.

2. [Major] TASK-0028 handoff current-state / last-completed-step text is stale relative to the staged pre-commit state.

   Evidence: `docs/handoffs/TASK-0028-bundled-lightweight-absorption-m-a7.md:55-61` says the last completed step is Step 4, that the Builder is standing by at step 5 handoff authoring, step 6 review-context authoring, step 9 self-review, and step 10 stop-and-show, and that the working tree is "pre-stage." But the staged tree already contains the handoff, the review-context, all six substantive edits, and the pre-commit review invocation state. The step log repeats the stale sequencing at `docs/handoffs/TASK-0028-bundled-lightweight-absorption-m-a7.md:111-115`.

   Why it matters: the handoff is the cycle's durable resume surface. If this lands as-is, a future reader resumes from "Step 4 complete / pre-stage" even though the actual cycle state had advanced through handoff authoring, review-context authoring, staging, and owner-invoked Codex pre-commit review.

   Recommendation: path-(a) revise the handoff's "Last completed step", "Current state", cumulative-diff-stat sentence, and step log so they describe the actual staged pre-commit / Codex-pass state.

Minor

1. [Minor] The Class A v-bump grep claim counts matches as lines.

   Evidence: `docs/reviews/PR-37-codex-pre-commit.md:83` says `grep -nE "v2\.25" README.md AGENTS.md CLAUDE.md` returns `4` lines. The command returns 3 matching lines because README has two `v2.25` matches on one line; the underlying content is correct at README:9, AGENTS:9, and CLAUDE:9.

   Recommendation: path-(b) record-and-proceed is acceptable; if touching the review-context for the Major findings, revise this to "3 lines / 4 matches" or use a match-count command such as `grep -oE "v2\.25" README.md AGENTS.md CLAUDE.md | wc -l`.

Validation Of Builder Claims

- Branch verified: `chore/task-0028-bundled-lightweight-absorption-m-a7`.
- Staged shape verified before absorption edit: 6 staged-modified + 2 staged-added; files match the Builder's file list.
- Staged diff stats before absorption edit verified: `8 files changed, 339 insertions(+), 6 deletions(-)`. After this review-output absorption is staged, the final exact stats must be re-derived again before commit.
- Canonical text edits verified by diff/read:
  - ADR-006 §Consequences new retroactive distributed-update bullet is present in the intended cluster.
  - PMN-007 §3.3 and §9.1 append-paragraphs are present at the intended anchors.
  - core.md §23.6.3 sub-shape A extension header + two bullets are present between default-path guidance and adjudication arithmetic.
  - core.md §18.3 M-A7 enumeration reads through PR-35 = 14 and no residual `= 13` / `v2.23` span remains in that amended paragraph.
  - README / AGENTS / CLAUDE Class A v2.24 -> v2.25 substitutions are substantively correct.
- v2.14.1 substrate URL named in AGENTS.md was attempted but returned GitHub 404 from this environment, so this pre-commit pass relies on the local v3 canonical-law trio plus repo-local task artifacts.

Recommendation

Request changes before PR open. No Blocking findings. Major 1 and Major 2 should route path-(a) because they affect durable verification/resume artifacts and directly touch the cycle's own verify-at-authoring discipline. Minor 1 can route path-(b) by default, or be fixed opportunistically while editing the review-context for Major 1.
```

### Codex post-PR pass 1 (UTC 2026-05-07T18:26:30Z)

Three-endpoint poll evidence per `core.md` §8.1.1.1:
- **Endpoint A** (`gh api repos/.../pulls/37/reviews`): 1 formal review submitted UTC 2026-05-07T18:26:30Z by `chatgpt-codex-connector[bot]`; state `COMMENTED`; `commit_id: c72a727a77c7b3b52e4f203ae3522e4513a9f81d`; body is generic Codex header (substantive content not at endpoint A).
- **Endpoint B** (`gh api repos/.../issues/37/comments`): only owner's `@codex review` invocation at UTC 2026-05-07T18:24:01Z. No Codex-side substantive content.
- **Endpoint C** (`gh api repos/.../pulls/37/comments`): 2 line-level review-comments, both P2 (Major-tier per repo three-level taxonomy) priority badges — substantive landing endpoint C (consistent with PMN-008 §5.8 (h.4) cross-cycle pattern; TASK-0028 = data point 9 in (h.4) distribution; reinforces (h.4) empirical cumulative rate).

Settling-period rule satisfied: formal review submitted +2 minutes 29 seconds from `@codex review` invocation; both endpoints stable.

**Verdict**: Major findings × 2 (both P2 priority badges).

**Findings** (verbatim per `core.md` §8.1.1.2):

> **<sub><sub>![P2 Badge](https://img.shields.io/badge/P2-yellow?style=flat)</sub></sub>  Update the review-context phase metadata**
>
> After this file records the Codex pre-commit output and absorbed findings later in the same document, the metadata still says the artifact is `pre-stage; pre-Codex-pass` with a pending step-11 timestamp. In the post-absorption state this becomes a stale resume surface: a future reader or metadata-driven check will conclude the pre-commit review has not happened even though the review output and resolutions are already present.
>
> Useful? React with 👍 / 👎.

> **<sub><sub>![P2 Badge](https://img.shields.io/badge/P2-yellow?style=flat)</sub></sub>  Constrain the M-A7 PR-count verification command**
>
> The literal command shown here scans all of `core.md`; in this commit it returns 26 unique `PR-*` tokens, not the 14-item M-A7 enumeration, because it is not actually limited to the §18.3 enumeration line. Anyone following this verification step will get a failing result even though the intended enumeration line is correct, so the command needs an explicit line/span filter or should be replaced with the exact enumeration grep already used above.
>
> Useful? React with 👍 / 👎.

**Adjudication** (per ADR-001 D11 + `core.md` §8.1.1.3 cost-class refinement):

- **Finding 1 (P2)**: ratified path-(a) revise. Class: stale-state recurrence at review-context Metadata surface. **DIRECT EMPIRICAL INSTANCE of Item 11 PMN-007 §3.3 (j) sub-rule canonicalized this cycle (pre-(j)-sweep enumeration completeness check)** — Codex pre-commit Major 2 corrected stale state at handoff surface; R.2 absorption did NOT sweep all stale-state-prone surfaces (review-context Metadata had same authoring conditions + same susceptibility). Recursive (h.2) at the canonicalizing surface for Item 11. Bidirectional (k.1) self-instantiation: Item 12 positive (k.1) at pre-commit Major 1 + Item 11 recursive (h.2) at post-PR Finding 1 — both within single cycle. (k.1) salience escalates MEDIUM-HIGH → **MAXIMUM** per PMN-008 §3.1 framework (multi-instance recursive bidirectional self-instantiation at canonicalizing cycle).
- **Finding 2 (P2)**: ratified path-(a) revise. Class: pure-token-swap (verification-command scope correctness; (h.2) sub-shape per PMN-009 canonical sub-shape framework). One-iteration convergence anticipated.

Bounded-continuation rule per `core.md` §8.1.1.3: Codex pre-commit pass-1 (3 findings) + post-PR pass-1 (2 findings) = 5 cumulative findings within TASK-0028; 1 recursive (h.2) at the canonicalizing surface. Within bounded-continuation tolerance for substantive cycles per priors (TASK-0027 had 5+ findings at intra-cycle); not at structural-meta-pattern threshold per spec §5 risk monitoring.

**Resolution applied** (path-(a)):

- **Edit R.4** (Codex post-PR Finding 1): review-context Metadata Status field + Codex desktop session timestamp lines refreshed to reflect post-pre-commit-pass + post-post-PR-pass-1 state. Pre-commit pass-1 absorbed at step-11.1 (R.1/R.2/R.3); post-PR pass-1 absorbed at step-14 (R.4/R.5). Sweep-target enumeration applied retroactively per Item 11 sub-rule: review-context Metadata Status + timestamp + handoff Status + Last-completed-step + Current-state — all stale-state-prone surfaces enumerated and verified post-this-fix-up.
- **Edit R.5** (Codex post-PR Finding 2, claim-12 verification command): replaced unscoped `grep -oE "PR-[0-9]+" core.md | sort -u | wc -l` (returns 26 — all unique PR-* tokens in entire core.md) with scoped form `grep -oE '`PR-9 \+ PR-10[^`]+`' core.md | grep -oE 'PR-[0-9]+' | wc -l` returns `14` (extracts the backtick-fenced M-A7 enumeration block specifically). Tighter scoping than line-grep was required: line-grep `grep -E "PR-9 \+ PR-10" core.md | grep -oE "PR-[0-9]+" | wc -l` would return 15 (contaminated by the prose reference "M-A7 promotion event at PR-13" appearing on the same line outside the enumeration); backtick-extraction returns exactly 14 = M-A7 enumeration arithmetic by enumeration. Self-review pass-3 (j) propagation residual catch — first-attempt scoped form (line-grep) was empirically tested via Bash tool returning 15, refined to backtick-extraction returning 14 within same Builder iteration before staging final R.5; documents that sweep-target enumeration completeness check (Item 11 sub-rule) plus empirical-verification-at-authoring (Item 12 sub-rule) compose at fix-up authoring surface. Builder enumeration verification preserved as primary check; scoped backtick-extraction grep is secondary.

**Pass-3 self-review iteration-1** per `core.md` §23.6.2 + bounded-continuation per §8.1.1.3: focused on R.4 + R.5 edit sites + recursive (h.2) cluster scope; sweep-target enumeration applied to all stale-state-prone surfaces this iteration; no new defects surfaced; convergence at iteration 1; pure-token-swap class for both fixes; no further same-class recurrence anticipated.

**Cycle-close ledger entry queued** (lightweight per ADR-006 D3 evidence-bar discipline):
- **Item C-1 — Recursive (h.2) at the canonicalizing surface for Item 11**: TASK-0028 absorbed PMN-007 §3.3 (j) sub-cluster cross-cycle empirical strengthening + sub-rule refinement (Item 11) — pre-(j)-sweep enumeration completeness check before applying (j)-sweep. R.2 absorption (handoff state refresh) did NOT apply this very sub-rule at the cycle authoring it; review-context Metadata stale-state surfaced as propagation residual at downstream gate (Codex post-PR pass-1). Direct empirical refutation of Builder application at the cycle authoring the sub-rule, AND direct empirical confirmation of multi-surface mitigation pipeline catching the drift at downstream gate (per PMN-008 §3.1 (k.1) framework + PMN-006 §3 multi-surface mitigation). Single-cycle observation; not PMN-eligible per ADR-006 D3 evidence-bar discipline (single-cycle (k.1) recursive instance at canonicalization cycle is expected pattern shape per PMN-008 §3.1; cumulative monitoring carry-forward).
- **Item C-2 — (k.1) salience MAXIMUM escalation**: bidirectional self-instantiation at single cycle — Item 12 positive (k.1) at pre-commit Major 1 + Item 11 recursive (h.2) at post-PR Finding 1. Per PMN-008 §3.1 framework: multi-instance recursive bidirectional self-instantiation at canonicalizing cycle is MAXIMUM-tier signature.

### Codex post-PR pass 2 (UTC 2026-05-07T18:47:17Z)

Three-endpoint poll evidence per `core.md` §8.1.1.1 (cumulative across passes):
- **Endpoint A** (`gh api repos/.../pulls/37/reviews`): 2 cumulative formal reviews — pass-1 @ T18:26:30Z (reviewed `c72a727`) + pass-2 @ T18:47:17Z (reviewed `eb7f7ed`); both `COMMENTED` state with generic Codex headers.
- **Endpoint B** (`gh api repos/.../issues/37/comments`): 2 owner `@codex review` invocations (T18:24:01Z + T18:44:58Z); no Codex-side substantive content.
- **Endpoint C** (`gh api repos/.../pulls/37/comments`): 4 cumulative line-level review-comments — pass-1 (2 P2 absorbed at R.4/R.5) + 2 NEW pass-2 findings (both P2). Substantive landing endpoint C confirmed across both passes (TASK-0028 = data points 9-10 in PMN-008 §5.8 (h.4) cross-cycle distribution; reinforces (h.4) empirical pattern at cumulative N+2 instances within single cycle).

Settling-period rule satisfied: pass-2 formal review submitted +2 minutes 19 seconds from pass-2 `@codex review` invocation; both endpoints stable.

**Verdict**: Major findings × 2 (both P2 priority badges); NOT cycle-trailing-clean Approve.

**Findings** (verbatim per `core.md` §8.1.1.2):

> **<sub><sub>![P2 Badge](https://img.shields.io/badge/P2-yellow?style=flat)</sub></sub>  Refresh the handoff state surfaces consistently**
>
> When this handoff is used after the post-PR R.4/R.5 absorption, this line says the stale-state-prone surfaces were enumerated and all refreshed, but the same file still records step 14.1 as `in progress` and step 14.2/14.3 as pending later in the step log. That leaves the task handoff with two contradictory lifecycle states, so a Builder or reviewer following the handoff cannot tell whether the post-PR fixes are complete or still awaiting self-review/commit.
>
> Useful? React with 👍 / 👎.

> **<sub><sub>![P2 Badge](https://img.shields.io/badge/P2-yellow?style=flat)</sub></sub>  Align the status claim with the actual handoff frontmatter**
>
> For the frontmatter-conformance check, `head -14 docs/handoffs/TASK-0028-bundled-lightweight-absorption-m-a7.md` at this commit shows `status: active`, not `status: drafted`. Because this review-context section is meant to be an executable verification record, the mismatch creates a false conformance claim and sends later reviewers toward a failing check even though the field count itself is valid.
>
> Useful? React with 👍 / 👎.

**Adjudication** (per ADR-001 D11 + `core.md` §8.1.1.3 cost-class refinement; ratified at Architect step-15 stop-and-show):

- **Pass-2 Finding 1 (P2)**: ratified path-(a) revise. Class: stale-state recurrence at handoff step-log surface — 3rd instance of Item 11 (j) propagation-residual cluster at canonicalizing surface (cumulative: pass-1 Finding 1 review-context Metadata + pass-3 self-review line 228 R.5 description + this pass-2 Finding 1 handoff step log internal contradiction). R.4 absorption applied Item 11 sub-rule reactively per-finding rather than enumerating ALL stale-state-prone surfaces upfront.
- **Pass-2 Finding 2 (P2)**: ratified path-(a) revise. Class: stale-state recurrence at review-context Builder-claim verification-output surface — 4th instance of Item 11 cluster. Builder-claim 10 head-14 assertion `status: drafted` not refreshed when R.2 flipped frontmatter status drafted→active.

Bounded-continuation rule per `core.md` §8.1.1.3: 4-instance recurrence at canonicalizing surface = bounded-continuation tolerance edge per TASK-0027 / PR-13 R.1.1→R.6 chain precedent. Architect step-15 stop-and-show diagnostic: pattern is non-asymptotic — last gate found MORE instances than prior, not fewer; pure-token-swap class typically converges at 1-iteration fixed-point per `core.md` §8.1.1.3, but recurring at adjacent verification surfaces. Per-instance correction IS pure-token-swap; meta-problem at sweep-target enumeration layer — Builder applied fix-ups reactively per-finding, never enumerating ALL stale-state-prone surfaces upfront. Item 11 sub-rule explicitly canonicalizes the discipline against this defect mode; Builder authored sub-rule but didn't maximally apply.

Both pass-2 findings load-bearing for cycle artifact integrity per Architect step-15 cross-check: Finding 1 = cycle execution evidence trail integrity (handoff step log records false progression states); Finding 2 = (h.2) class — review-context claim 10 has falsified expected output. Per `core.md` §8.1.1.3: when subsequent same-class findings ARE load-bearing, rule routes to path-(a) regardless of repetition count. **Path-(β) routing not justified.**

**MAXIMAL enumeration directive ratification** (Architect step-15 2026-05-07): Builder produces enumeration list at start of R.6 authoring; applies all fixes simultaneously; runs Pass-4 self-review against enumerated set. Convergence success → cycle ships; non-convergence → structural reframe carry-forward to TASK-0029. Non-convergence outcome itself MAXIMUM-tier empirical evidence — cycle that canonicalizes the sub-rule produces counter-example to sub-rule's adequacy under maximal application. That carry-forward is genuine TASK-0029 scope material.

**Resolution applied** (path-(a) under MAXIMAL enumeration directive):

- **MAXIMAL sweep-target enumeration produced at step-14.5 BEFORE applying any fix**: 16 stale-state-prone surfaces enumerated across handoff + review-context (10 refreshes + 2 additions + 4 verified-current); verbatim-protected regions excluded (this absorption block + pass-1 absorption block per PMN-002 (a)). Empirically verified at HEAD eb7f7ed: cumulative-from-origin/main 444/6/8; pass-1 timestamp 18:26:30Z; pass-2 timestamp 18:47:17Z; handoff frontmatter status:active; review-context frontmatter status:drafted.

- **Edit R.6** (Pass-2 Finding 1, handoff §"Last completed step" line 57 + §"Current state" Summary line 61): refreshed to step-14.4-14.5 state (pass-2 absorbed; R.6-R.21 MAXIMAL fix-up in progress; HEAD eb7f7ed; iteration toward step-14.6 pass-4 self-review with enumerated-set verification + step-14.7 fix-up commit + push + step-16 Codex pass-3 cycle-trailing-clean confirmation).

- **Edit R.7** (handoff §"Current state" cumulative-diff-stats line 73 + review-context Builder-claim 11 + Reviewer focus): originally applied at step-14.5 staging populating value `8 files changed, 545 insertions(+), 6 deletions(-)` anchored to "HEAD eb7f7ed pre-pass-4-staging" — value was correct as forecast for post-staging tree but qualifier was internally inconsistent (545/6 only true at post-pass-4-staging, not pre); within-surface absorption-completeness gap (value-vs-SHA-qualifier coupling) caught by Codex post-PR pass-3 finding; refreshed at step-14.10 R.18 path-(a) absorption per Architect Option C ratification to anchor at HEAD 741005d post-step-14.7-fix-up-commit (current HEAD post-pass-2 absorption fix-up commit); ins overage attribution + del stable attribution recorded.

- **Edits R.8 / R.9 / R.10 / R.11** (handoff §3 step log entries 11.1 / 14.1 / 14.2 / 14.3): refreshed all "in progress" / "pending" status markers to "complete" with terminal-state evidence (commit SHA eb7f7ed; convergence-iteration counts; absorption-state references). Internal contradiction at line 57 (Pass-2 Finding 1 specific target) resolved.

- **Edit R.12** (handoff §3 step log entry 15 outcome): refreshed Step 15 from "pending; cycle-trailing-clean Approve anticipated" to "complete; verdict 0 Blocking / 2 Major P2 / 0 Minor — NOT cycle-trailing-clean Approve" with full pass-2 findings summary + 4-instance recurrence note.

- **Edit R.13** (handoff §3 step log additions): added entries for steps 14.4 (pass-2 absorption) + 14.4.1 (path-(a) iterate adjudication stop-and-show) + 14.5 (R.6-R.21 MAXIMAL-enumeration-directive fix-up) + 14.6 (pass-4 self-review pending) + 14.7 (fix-up commit + push pending) + 16 (Codex pass-3 pending) per Item 11 sub-rule completion-tracking discipline.

- **Edit R.14** (handoff §10 Cycle-close ledger): populated from placeholder with Items 1-8 surfaced across cycle gates per Architect surfacings (Items 1-4 step-14.3 cross-check + Items 5-7 step-15 stop-and-show + Item 8 pass-4 outcome TBD).

- **Edit R.15** (review-context §Metadata Status line 18 + timestamps line 19): refreshed to include post-Codex-post-PR-pass-2 state + pass-2 timestamp UTC 2026-05-07T18:47:17Z reviewed commit eb7f7ed.

- **Edit R.16** (review-context Builder-claim 10 head-14 status assertion): refreshed `status: drafted` → `status: active` with absorption rationale (R.2 flipped frontmatter status pre-stage→post-stage at step-11.1).

- **Edit R.17** (this absorption section): authored verbatim per PMN-002 (a) + `core.md` §8.1.1.2 with three-endpoint poll evidence + verdict + findings verbatim + adjudication + resolution + pass-4 self-review record + cycle-close ledger entry.

**Pass-4 self-review iteration-1** per `core.md` §23.6.2 + bounded-continuation per §8.1.1.3 with **enumerated-set verification per Architect MAXIMAL enumeration directive**:

- Enumerated-set verification scope: 16 surfaces from step-14.5 enumeration list. Each surface re-verified against staged-tree state post-R.6+ application:
  - H4 / H5 / H6 (handoff §Last-completed-step / §Current state Summary / §Current state cumulative-diff-stats): refreshed to post-pass-2-absorption + post-MAXIMAL-fix-up state ✓
  - H7-H11 (handoff §3 Step 11.1 / 14.1 / 14.2 / 14.3 / 15): all step-status markers refreshed; line 57 internal contradiction resolved ✓
  - H12 (handoff §3 Step log additions for 14.4 / 14.4.1 / 14.5 / 14.6 / 14.7 / 16): added ✓
  - H13 (handoff §10 Cycle-close ledger): populated with Items 1-8 ✓
  - R2 / R3 (review-context §Metadata Status + timestamps): refreshed with pass-2 state + timestamp ✓
  - R6 (Builder-claim 10 head-14 status): refreshed drafted→active ✓
  - R7 / R9 (Builder-claim 11 cumulative-diff-stats + Reviewer focus): refreshed to 444/6 ✓
  - R10 (this §Codex post-PR pass 2 section): authored ✓
  - Verified-current (no action): H1 / H2 / H3 / R1 / R4 / R5 / R8 — re-verified current at HEAD eb7f7ed staged-tree

- New-stale-class scan: scanned for any verification-claim or state-summary surface NOT on enumeration list that could be stale post-R.6+ staging. Candidate scan: handoff §Metadata Linked PR (line 22) "URL TBD at PR-open" — historically anchored, not stale; review-context §Reviewer focus other bullets — anchored to substantive-content-shape verification, not stale; review-context kickoff prompt — verbatim past invocation, not stale. **Zero new-stale-class candidates surfaced.**

- Convergence: pure-token-swap / line-stable / additive class for all R.6-R.17 fixes; sweep-target enumeration applied maximally upfront per Architect directive; no in-iteration self-correction needed (contrast with pass-3 line-228 catch). Iteration-1 zero defects on enumerated set; no new classes detected.

**Cycle-close ledger entry queued** (lightweight per ADR-006 D3 evidence-bar discipline):
- **Item C-3 — Recursive (h.2) at canonicalizing surface, 4-instance trajectory**: cumulative across cycle (pass-1 Finding 1 + pass-3 line 228 + pass-2 Finding 1 + pass-2 Finding 2). Pattern: per-instance correction is pure-token-swap; meta-problem at sweep-target enumeration layer; Item 11 sub-rule canonicalized but Builder applied REACTIVELY per-finding rather than maximally upfront. Architect step-15 MAXIMAL-enumeration-directive ratified path-(a) iterate as Item 11 load-bearing-with-maximal-application property test. Pass-4 convergence-success outcome → property confirmed; non-convergence → structural reframe carry-forward.
- **Item C-4 — (k.1) salience confirmation MAXIMUM**: bidirectional self-instantiation across multiple surfaces + multiple sub-rules per Architect step-14.3 cross-check matrix. Strongest possible cycle-close empirical evidence FOR Items 11+12 load-bearing nature.

### Codex post-PR pass 3 (UTC 2026-05-07T19:17:03Z)

Three-endpoint poll evidence per `core.md` §8.1.1.1 (cumulative across passes):
- **Endpoint A** (`gh api repos/.../pulls/37/reviews`): 3 cumulative formal reviews — pass-1 @ T18:26:30Z (reviewed `c72a727`) + pass-2 @ T18:47:17Z (reviewed `eb7f7ed`) + pass-3 @ T19:17:03Z (reviewed `741005d`); all `COMMENTED` state with generic Codex headers.
- **Endpoint B** (`gh api repos/.../issues/37/comments`): 3 owner `@codex review` invocations (T18:24:01Z + T18:44:58Z + T19:14:14Z); no Codex-side substantive content.
- **Endpoint C** (`gh api repos/.../pulls/37/comments`): 5 cumulative line-level review-comments — pass-1 (2 P2 absorbed at R.4/R.5) + pass-2 (2 P2 absorbed at R.6-R.17) + 1 NEW pass-3 finding (P2 at within-surface absorption-completeness sub-class). Substantive landing endpoint C confirmed across 3 passes (TASK-0028 = data points 9-11 in PMN-008 §5.8 (h.4) cross-cycle distribution; reinforces (h.4) empirical pattern at cumulative N+3 instances within single cycle — TASK-0028 strongest single-cycle (h.4) data point on record).

Settling-period rule satisfied: pass-3 formal review submitted +2 minutes 49 seconds from pass-3 `@codex review` invocation; both endpoints stable.

**Verdict**: Major findings × 1 (P2 priority badge); NOT cycle-trailing-clean Approve.

**Findings** (verbatim per `core.md` §8.1.1.2):

> **<sub><sub>![P2 Badge](https://img.shields.io/badge/P2-yellow?style=flat)</sub></sub>  Correct the stale diff-stat source claim**
>
> This verification claim says the 545/6 shortstat is from `HEAD eb7f7ed pre-pass-4-staging`, but checking the reviewed commits shows `git diff --shortstat ac5d3b8 eb7f7ed` is `8 files changed, 444 insertions(+), 6 deletions(-)`, while 545/6 is only true for the final `ef361f2` tree. Because this review-context file is the durable evidence surface for the cycle and the surrounding text uses the value for MC-A overage attribution, leaving the wrong source commit/timepoint will mislead future verification and repeats the exact stale-state class this cycle is trying to eliminate.
>
> Useful? React with 👍 / 👎.

**Codex Sub-shape B observation** (per `core.md` §8.1.1.2): Codex cited fabricated SHA `ef361f2` as "the final tree." Actual final tree is `741005d705a445e8cccd3bd90ffb06755e80a5fd` per `git rev-parse HEAD`. Codex's substantive critique correct (545/6 is post-pass-4 not pre-pass-4); citation fabricated. 2nd cross-cycle instance per PMN-007 §9.2 (m) Reviewer-side citation correctness sub-shape B (1st was Codex pass-1 SHA fabrication at TASK-0014); strengthens canonicalization candidate at TASK-0029+ or `core.md` §8.1.1.2 cross-side symmetry note. Cycle-close ledger Item 12.

**Adjudication** (per ADR-001 D11 + `core.md` §8.1.1.3 cost-class refinement; ratified at Architect step-16.2 stop-and-show):

- **Pass-3 Finding (P2)**: ratified path-(a) revise per Architect Option C with override of step-15 directive. **Refined diagnostic** (Architect step-16.2): pass-4 self-review converged clean at MAXIMAL surface-enumeration scope (zero findings, zero new-class within enumeration); pass-3 finding is at NEW sub-class adjacent to surface-enumeration — within-surface absorption-completeness (coupled value + SHA/timing-qualifier shape NOT in enumeration scope). Item 11 sub-rule's load-bearing-with-maximal-application property is VALIDATED at surface-enumeration scope, not refuted. Pass-3 finding is discovery of ADJACENT discipline gap, not structural refutation. Step-15 binary-outcome routing language ("non-convergence at MAXIMAL → Option B") was insufficiently nuanced for sub-class diagnostic refinement; refined diagnostic warrants revised routing per Item 13.

**Architect Option C with bounded commitment** (step-16.2 ratification 2026-05-07): R.18 path-(a) within-surface sub-component-enumeration directive — for each numeric value updated, identify accompanying SHA / timing-qualifier / contextualizing prose; verify each empirically against current state; apply coupled fixes simultaneously. Builder produces sub-component enumeration list at R.18 authoring time BEFORE applying fix. Pass-5 self-review verifies within-surface sub-component-enumeration completeness. Bounded commitment: ANY pass-4 finding (regardless of class) → immediate Option B fallback per cycle-bandwidth tradeoff acceptance.

**Resolution applied** (path-(a) under within-surface sub-component-enumeration directive):

- **R.18 within-surface sub-component enumeration list produced at step-14.8 BEFORE applying any fix**: 10 within-surface sub-component coupled-shape constructs enumerated (4 primary cumulative-diff-stats SHA/qualifier coupling at handoff line 73 + review-context line 94 + line 112 + line 278 = R.18a/b/c/d; 4 step-log status-vs-event coupling at handoff line 130/131/57/61 = R.18f/g/h/e; 1 §10 ledger Items 8-14 absorption = R.18i; 1 review-context §Codex post-PR pass 3 absorption section addition = R.18j). Empirically verified at HEAD 741005d: cumulative-from-origin/main pre-R.18 staging = 545/6/8 → post-R.18 staging = TBD (populated at pass-5 verification with line-count-stable digit substitution).

- **Edits R.18a-d** (primary; Codex pass-3 finding target): handoff §"Current state" cumulative-diff-stats line 73 + review-context Builder-claim 11 line 94 + Reviewer focus line 112 + R.7 absorption-record description line 278 — refreshed coupled-shape SHA/qualifier from "HEAD eb7f7ed pre-pass-4-staging" / "pre-R.6+-staging" → "HEAD 741005d post-step-14.7-fix-up-commit + R.18 within-surface sub-component-enumeration-directive staging." R.7 absorption-record clarified historical action vs current anchor (R.7 originally applied at step-14.5 staging populating value 545 anchored to pre-pass-4-staging; original anchor was internally inconsistent with value; pass-3 caught the within-surface absorption-completeness gap; R.18 corrects).

- **Edits R.18e-h** (within-surface sweep parallel patterns): handoff §"Current state" Summary line 61 (added step-14.7 commit 741005d as current PR-37 head + Codex pass-3 outcome + R.18 in-progress); handoff §3 Step 14.7 line 130 (pending → complete with SHA 741005d + 118+/17− delta); handoff §3 Step 16 line 131 (pending → complete with pass-3 outcome 1 P2 finding); handoff §"Last completed step" line 57 (refreshed to step-16.1 absorbed / R.18 in-progress per Architect Option C ratification).

- **Edit R.18i** (handoff §10 ledger): refreshed Item 8 (was "Pass-4 convergence outcome TBD"; now "MAXIMAL enumeration directive empirical record at TASK-0028" per Architect step-14.6 surfacing); added Items 9-14 (Architect surfacings: Items 9-10 step-14.6; Items 11-14 step-16.2 Option C adjudication).

- **Edit R.18j** (this absorption section): authored verbatim per PMN-002 (a) + `core.md` §8.1.1.2 with three-endpoint poll evidence + verdict + finding verbatim + Codex Sub-shape B observation + adjudication + resolution + pass-5 self-review record + cycle-close ledger entry.

**Pass-5 self-review iteration-1** per `core.md` §23.6.2 + bounded-continuation per §8.1.1.3 with **within-surface sub-component-enumeration completeness verification per Architect Option C directive**:

- Sub-component enumeration verification scope: 10 sub-component coupled-shape constructs from step-14.8 enumeration list. Each construct re-verified against staged-tree state post-R.18 application:
  - R.18a-d (primary cumulative-diff-stats SHA/qualifier coupling): all 4 surfaces refreshed to "HEAD 741005d post-step-14.7-fix-up-commit + R.18 staging" anchor ✓
  - R.18e-h (step-log status-vs-event coupling): line 61 + 130 + 131 + 57 all refreshed; Step 14.7 + Step 16 status flipped pending → complete with terminal-state evidence ✓
  - R.18i (§10 ledger Items 8-14): Item 8 refreshed; Items 9-14 added; ledger now reflects current canonical numbering per Architect surfacings ✓
  - R.18j (this §Codex post-PR pass 3 absorption section): authored ✓

- New sub-class scan: scanned for any other coupled-shape construct (numeric-value + qualifier; status-marker + event; field + comment) that could exhibit same within-surface absorption-completeness gap. Candidates scanned: handoff §Metadata Last synced commit SHA / Branch / Status / Framework version (anchored to pre-flight historical events; not coupled to current HEAD); review-context §Metadata Base SHA / Reviewer / Architect (historical anchors); review-context §Codex desktop pre-commit kickoff (verbatim past invocation). **Zero new sub-class candidates surfaced.**

- Convergence: pure-token-swap / line-stable / additive class for all R.18 fixes; sub-component enumeration applied upfront per Architect Option C directive (contrast with R.6-R.17 surface-only enumeration that left sub-component coupling unchecked). Iteration-1 zero defects on sub-component enumeration list; no new sub-class detected.

**Cycle-close ledger entry queued** (lightweight per ADR-006 D3 evidence-bar discipline):
- **Item C-5 — Item 11 load-bearing-at-MAXIMAL-application property refined diagnostic**: VALIDATED at surface-enumeration scope (pass-4 clean) + ADJACENT sub-discipline gap at within-surface sub-component scope (pass-3 finding). Item 11 sub-rule + new within-surface sub-component-enumeration sub-discipline (Item 14) are separable disciplines; surface-enumeration alone insufficient when coupled-shape sub-components present. Significant empirical material for TASK-0029+ structural reframe + ADR-006 D3 framework calibration record.
- **Item C-6 — Bounded-commitment Option C empirical test in progress**: pass-4 outcome at step-17 determines: clean Approve → cycle ships + Items 11 + new within-surface sub-discipline empirically validated; ANY finding → Option B fallback per bounded commitment + cycle ships with carry-forward + TASK-0029 immediate structural reframe scope expansion (Items 7 + 14 bundled).
