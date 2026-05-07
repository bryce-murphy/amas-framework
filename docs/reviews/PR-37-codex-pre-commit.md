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
- Status: drafted (pre-stage; pre-Codex-pass; transitions to recorded post-merge per linked-pr-fix-up Action substitution per PMN-001 (k))
- Codex desktop session timestamp (UTC): pending step-11
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
    - bash: `head -14 docs/handoffs/TASK-0028-bundled-lightweight-absorption-m-a7.md` shows 12-field frontmatter with `task_id: TASK-0028` + `framework_version_dogfooded: AMAS v2.24` + `status: drafted`.
    - bash: `grep -cE "^(task_id|title|pr|branch|linked_predecessor|linked_successor|linked_pr|framework_version_dogfooded|production_target|spec_source|date_authored|status):" docs/handoffs/TASK-0028-bundled-lightweight-absorption-m-a7.md` returns `12`.
    - bash: `grep -cE "^linked_pr: PR-37 \(Builder fills with squash SHA post-merge per PMN-001 \(k\)\)$" docs/handoffs/TASK-0028-bundled-lightweight-absorption-m-a7.md` returns `1` (canonical placeholder regex form per `.github/scripts/linked-pr-fix-up.py:35` empirically pre-applied via PowerShell match returning `MATCH: PR-37`).
    - bash: `head -3 docs/reviews/PR-37-codex-pre-commit.md` shows `status: drafted` 1-field frontmatter.
    - Class: PMN-009 (i.5) sub-shape D convention-inference + MC-C frontmatter conformance discipline per templates/handoff-template.md substantive content.

11. **Cumulative-diff-stats per `core.md` §23.6.1.1 (e.1) staged-tree convention** — landed-exact at step-11.1 post-Codex-pre-commit-pass-1 R.1/R.2/R.3 absorption staging. Spec §1.1 anticipation ~261-369 ins / ~3 del across ~8 files; landed ins within range; landed del 6 vs anticipated ~3 attributable to §18.3 in-place line-replacement refinement (3 del + 3 ins not foreseen in spec del-anticipation). Order of magnitude smaller than TASK-0027 (1038/58/10) per ADR-006 D3 lightweight-absorption efficiency. Verifiable at pre-commit:
    - bash: `git diff --staged --shortstat origin/main` returns `8 files changed, 397 insertions(+), 6 deletions(-)` post-step-11.1 staging per `core.md` §23.6.1.1 (e.1) cumulative-diff-stats re-derivation discipline (Codex pre-commit pass-1 Major 1 R.1 absorption: landed-exact value re-derived rather than anticipated-prose placeholder).
    - Class: PMN-005 (e.1) cumulative-diff-stats re-derivation + PMN-007 §9.1 verify-at-authoring discipline absorbed this cycle (landed-exact value re-derived per Codex Major-1 Recommendation rather than anticipated-prose placeholder shape).

12. **M-A7 enumeration arithmetic verification** — count by enumeration, not by claim per spec §3.5: `PR-9 + PR-10 + PR-11 + PR-13 + PR-15 + PR-17 + PR-19 + PR-21 + PR-25 + PR-27 + PR-29 + PR-31 + PR-33 + PR-35 = 14 PRs`. Builder enumeration: 1-PR-9, 2-PR-10, 3-PR-11, 4-PR-13, 5-PR-15, 6-PR-17, 7-PR-19, 8-PR-21, 9-PR-25, 10-PR-27, 11-PR-29, 12-PR-31, 13-PR-33, 14-PR-35. Arithmetic-by-enumeration confirmed = 14. Verifiable at pre-commit:
    - bash: `grep -oE "PR-[0-9]+" core.md | sort -u | wc -l` (within §18.3 enumeration line span) — count of unique PRs in enumeration matches stated count.
    - Class: PMN-005 prose-arithmetic decomposition discipline (per `core.md` §23.6.1) + canonical-impact-surface-completeness check (per Items 4+10 amendment this cycle).

## Reviewer focus

- **Substantive content shape verification**: do all 6 byte-exact canonical-text edits match spec §4.1-§4.6 prescriptions byte-exactly? Particular attention to:
  - ADR-006 §Consequences new bullet position (between distributed-update bullet and PMN insertion budget bullet — preserves cluster-coherence framing).
  - PMN-007 §3.3 + §9.1 append-paragraph positions (after each section's existing close, before next §-heading).
  - core.md §23.6.3 bold-header + 2 enumerated bullets at line 321-325 (between Default-path-guidance pair end and Architect adjudication-framework arithmetic start per Architect step-1 (3a) ratification).
  - core.md §18.3 in-place v2.24 paragraph refinement (4 byte-exact substitutions: preamble + enumeration + span + count); original 4-instance grounding paragraph preserved per spec §4.5 Note on append-vs-replace.
  - Class A v-bump (4 byte-exact substitutions across 3 sites; zero residual v2.24).

- **§-citation correctness**: all §-citations resolve against current canonical state (post-edit core.md §-numbering preserved; PMN-007 §3.3 + §9.1 preserved as targets; ADR-006 §Consequences preserved as target).

- **Cumulative-diff-stats matches review-context claims**: `git diff --staged --shortstat origin/main` returns `8 files changed, 397 insertions(+), 6 deletions(-)` landed-exact at step-11.1 post-Codex-pass-1 R.1/R.2/R.3 staging; ins within spec §1.1 anticipation range (~261-369); del overage 6 vs anticipated ~3 documented at Builder-claim 11 with attribution to §18.3 in-place line-replacement refinement.

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
