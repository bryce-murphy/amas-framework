---
status: drafted
---

# PR-39 Codex desktop pre-commit review

## Metadata

- PR ID: PR-39 (anticipated; pre-PR-open authoring per spec sub-shape E provisional handling; verified at pre-flight via `gh pr list --state open` returning zero)
- TASK ID: TASK-0029
- Branch: `adr/task-0029-adr-007-part-c-scoping` (Option B canonical form per ADR-005; adr-type per architectural cycle class; matches `^(feat|fix|chore|adr|shadow|spike)/task-[0-9]{4}-([a-z0-9]|[a-z0-9][a-z0-9.-]*[a-z0-9])$` regex)
- Linked handoff: docs/handoffs/TASK-0029-adr-007-part-c-scoping.md
- Base SHA: `3b722d6897f580e1f14a8ffe6a9fc2ca59331856` (squash-merge of PR-38 chore on main, 2026-05-07T20:10:14Z; PR-38 = TASK-0028 linked-PR substitution chore-fix-up auto-fired by linked-pr-fix-up Action)
- Builder: Claude Sonnet 4.6 (Claude Code, Windows + Git Bash)
- Reviewer: Codex (GPT-5.5) — desktop, pre-commit, staged working tree per TASK-0025 cycle-close Item 4 lesson (claims align to staged-tree state at pre-commit time)
- Architect (this PR's): Claude Opus 4.7 (Claude.ai Project)
- Owner: Bryce Murphy (`@bryce-murphy`)
- Status: drafted (pre-stage; transitions to recorded post-merge per linked-pr-fix-up Action substitution per PMN-001 (k))
- Codex desktop session timestamp (UTC): TBD at owner kickoff
- Framework version: AMAS v2.25 → v2.26 (Class A v-bump at this cycle per `core.md` §18.4 minor tier — substantive new canonical text in feature-class cluster: ADR-007 canonicalizing architectural decision). Architectural-class direction-decision cycle (ADR-007 ship). Recursive-self-instantiation salience escalated to **MEDIUM** from spec-anticipated LOW-MEDIUM per (k.1) NEGATIVE self-instantiation event surfaced at step 4.1 substantive content authoring (see handoff §1.1 Honesty record).
- Severity taxonomy: Blocking / Major / Minor (three-level; per repo discipline; standing per PMN-004 §5 (a)).
- Disciplines applied: PMN-001 (k) (linked-pr-fix-up substitution discipline; canonical regex empirical pre-application via Python re.match returning Match at pre-flight) + PMN-002 (a) (verbatim-output convention) + PMN-002 (d) (code-fenced kickoff prompt) + PMN-004 §5 (a)-(f) + PMN-007 §3.3 (j) all-instances + PMN-007 §9.1 (i) anticipation-prose-vs-verify-at-authoring (per TASK-0028 amendment) + PMN-007 HEAD canonical 12-field handoff frontmatter form + PMN-008 §3.1 (k.1) self-instantiation framework + PMN-008 §4.2 (i.5) convention-inference verification + PMN-009 / `core.md` §23.6.3 sub-shape A verify-at-authoring batch + canonical-impact-surface-completeness check (extended at step 4.1 to include "claims about repo state of OTHER referenced canonical surfaces") + PMN-010 §2 sub-shape 1 forward-ref §-citation correctness + `core.md` §8.1.1.3 bounded-continuation rule + `core.md` §24 cross-surface verify-before-assert (catch event at step 4.1 surfaced spec §4.1 + §4.3 ADR-006 D2 batch label drift; Architect path-(a) Corrections 1-3 absorbed) + ADR-006 Decision 3 evidence-bar (this cycle architectural-class, NOT lightweight-absorption).
- Substantive-content-cycle context: PR-39 ships 5 substantive content edits in a single PR per single-PR-with-split-trigger discipline (TASK-0012 Part B precedent extended through TASK-0028). ADR-007 new file (~128 lines) + ADR-006 §Status amendment (single-line append) + README Roadmap rewrite (Correction 3 form per step 4.1 absorption) + Class A v-bump v2.25 → v2.26 minor tier (4 byte-exact substitutions across 3 sites) + core.md §18.3 M-A7 15th-instance amendment (in-place paragraph refinement). Step-1 pre-flight stop-and-show ratified all 5 Phase 1 adjudications + Builder §Context refinement discretion. Step 4.1 stop-and-show absorbed Architect path-(a) Corrections 1-3 for spec §4.1 + §4.3 ADR-006 D2 batch label drift. ADR-007 ships canonical architectural decision; cycle's content empirically validates ADR-007 D2 split structure + D3 schedule + D4 cycle-bandwidth expectation. TASK-0030 = Part C.1 substantive content materialization per ADR-007 D3 schedule (next cycle).

## Builder claims to verify

The Builder asserts the following at hand-off to Codex desktop pre-commit review. Each claim is verifiable from the working tree at staged-tree state per (e.1) sub-rule + TASK-0025 cycle-close Item 4 lesson; verify-at-authoring shape per PMN-007 §9.1 amendment at TASK-0028 (no anticipated-prose claims). PR-39 ships ADR-007 new file + ADR-006 §Status amendment + README Roadmap rewrite + Class A v-bump + core.md §18.3 M-A7 15th-instance amendment + TASK-0029 handoff + PR-39 review-context.

1. **Working-tree state at pre-commit (staged): 5 staged-modified + 3 staged-added**. Per TASK-0025 cycle-close Item 4 lesson, this cycle stages all changes before Codex pre-commit pass. Verifiable at pre-commit:
   - bash (staged-modified): `git status --porcelain | grep -c "^M "` returns `5` (staged-modified: `AGENTS.md` + `CLAUDE.md` + `README.md` + `core.md` + `docs/adr/ADR-006-product-delivery-pivot-pr-plan-amendment.md`).
   - bash (staged-added): `git status --porcelain | grep -c "^A "` returns `3` (staged-added: `docs/adr/ADR-007-part-c-materialization-scoping.md` + `docs/handoffs/TASK-0029-adr-007-part-c-scoping.md` + `docs/reviews/PR-39-codex-pre-commit.md`).

2. **ADR-007 new file at canonical path with §-section structure per spec §4.1 + Corrections 1-2 absorbed**. Verifiable at pre-commit:
   - bash: `ls docs/adr/ADR-007-part-c-materialization-scoping.md` returns 1 line (file exists).
   - bash: `wc -l docs/adr/ADR-007-part-c-materialization-scoping.md` returns ~128 lines (slight overshoot of spec §4.1 ~80-120 anticipation due to Corrections 1+2 expanding §Decision 1 + §Consequences enumerations to use ADR-006 D2 actual labels; within default-cycle ±20% MC-A tolerance).
   - bash: `grep -nE "^## " docs/adr/ADR-007-part-c-materialization-scoping.md` returns Status / Context / Decision / Alternatives / Consequences / Cross-references headers.
   - bash: `grep -cE "^### Decision [1-4]" docs/adr/ADR-007-part-c-materialization-scoping.md` returns `4`.
   - bash: `grep -cE "^### \([A-E]\)" docs/adr/ADR-007-part-c-materialization-scoping.md` returns `5` (Alternatives A-E).
   - bash: `grep -nE "GitHub-artifact templates \(P2\)" docs/adr/ADR-007-part-c-materialization-scoping.md` returns 1 line in §Decision 1 (Correction 1 absorption: actual ADR-006 D2 labels used).
   - bash: `grep -nE "P1\[remaining 7 templates\] → P2 \(GitHub-artifact templates\)" docs/adr/ADR-007-part-c-materialization-scoping.md` returns 1 line in §Consequences (Correction 2 absorption: corrected placement diagram).
   - bash: `grep -nE "37 explicit" docs/adr/ADR-007-part-c-materialization-scoping.md` returns 1 line in §Context (Builder pre-flight empirical refinement: 37 qualifier instances / 30 distinct lines).
   - Class: PMN-009 (i.5) sub-shape A verify-at-authoring + PMN-010 sub-shape 1 forward-ref §-citation correctness.

3. **ADR-006 §Status amendment — single-line append per ADR-002 amendment-pattern precedent**. Verifiable at pre-commit:
   - bash: `grep -nE "Amended 2026-05-07 by ADR-007" docs/adr/ADR-006-product-delivery-pivot-pr-plan-amendment.md` returns 1 line at line 11 (within §Status field, between "Effective:" line at 9 and `## Context` at 13).
   - bash: `grep -nE "further partial-supersession of Decision 2 batch sequence; D1 \+ D3 \+ D4 preserved unchanged" docs/adr/ADR-006-product-delivery-pivot-pr-plan-amendment.md` returns 1 line.
   - Class: PMN-009 (i.5) sub-shape A verify-at-authoring + amendment-pattern precedent compliance (ADR-002 → ADR-003 → ADR-005 → ADR-006 self-precedent).

4. **README "Roadmap" paragraph rewrite per Correction 3 (step 4.1 stop-and-show absorption)**. Verifiable at pre-commit:
   - bash: `grep -nE "ADR-003.*ADR-006.*ADR-007 sequence" README.md` returns 1 line in Roadmap paragraph.
   - bash: `grep -nE "P1 \(process templates\) → C\.1 → P1\[continuation\] → P2 \(GitHub-artifact templates\)" README.md` returns 1 line (Correction 3 effective batch sequence with actual ADR-006 D2 labels).
   - bash: `grep -nE "between P3 \(prompts\) and P4 \(Actions" README.md` returns 1 line (Part C.2 placement framing).
   - bash: `grep -nE "ADR-007" README.md` returns ≥1 line (Roadmap adds ADR-007 cross-reference).
   - bash: `grep -nE "P2 GitHub-artifact templates, P3 prompts" README.md` returns `0` lines (pre-cycle Roadmap text replaced).
   - Class: PMN-009 (i.5) sub-shape A verify-at-authoring + PMN-010 sub-shape 1 forward-ref §-citation correctness + Item 14 retroactive-supersession-marking sub-rule application.

5. **Class A v-bump applied at 3 sites (4 byte-exact substitutions: README:9 ×2 + AGENTS:9 ×1 + CLAUDE:9 ×1; v2.25 → v2.26 minor tier per §18.4)**. Verifiable at pre-commit:
   - bash: `grep -nE "v2\.25" README.md AGENTS.md CLAUDE.md` returns `0` lines (Class A surgical edit complete; no residual v2.25 at any of 3 Class A sites).
   - bash: `grep -oE "v2\.26" README.md AGENTS.md CLAUDE.md | wc -l` returns `4` (4 match-occurrences: README:9 ×2 + AGENTS:9 + CLAUDE:9).
   - bash: `grep -nE "current canonical materialization at v2\.26 — see README" AGENTS.md` returns 1 line at line 9.
   - bash: `grep -nE "current canonical materialization at v2\.26 — see README" CLAUDE.md` returns 1 line at line 9.
   - bash: `awk 'NR==9' README.md | grep -oE "v2\.26" | wc -l` returns `2` (both v2.26 instances on README line 9).
   - Class: PMN-007 §3.3 (j) all-instances propagation-residual sweep + Class A canonical-version-of-record (per TASK-0027 step-2 §6 ratification extending through this cycle) + canonical-impact-surface-completeness check.

6. **core.md §18.3 M-A7 15th-instance amendment — in-place v2.25 cumulative-instances paragraph refinement to 15-instance enumeration**. Verifiable at pre-commit:
   - bash: `grep -nE "as of v2\.26 canonicalization at PR-39 / TASK-0029" core.md` returns 1 line at line 238.
   - bash: `grep -nE "PR-9 \+ PR-10 \+ PR-11 \+ PR-13 \+ PR-15 \+ PR-17 \+ PR-19 \+ PR-21 \+ PR-25 \+ PR-27 \+ PR-29 \+ PR-31 \+ PR-33 \+ PR-35 \+ PR-37 = 15" core.md` returns 1 line at line 240.
   - bash: `grep -nE "spanning v2\.16 through v2\.25 canonicalization" core.md` returns 1 line.
   - bash: `grep -nE "15 consecutive substantive cycles" core.md` returns 1 line at line 242.
   - bash: `grep -nE "= 14" core.md` returns `0` lines (no residual 14-count enumeration).
   - bash: `grep -nE "spanning v2\.16 through v2\.24 canonicalization" core.md` returns `0` lines (replaced).
   - bash: `grep -nE "Four-instance evidence \(PMN-005" core.md` returns 1 line (original 4-instance grounding paragraph preserved post-amendment).
   - Class: PMN-009 (i.5) sub-shape A verify-at-authoring + PMN-010 sub-shape 1 + arithmetic-by-enumeration verification (count by enumeration: 15 PRs in chain) + Item 14 within-surface sub-component-enumeration (3 coupled-shape constructs at L238/L240/L242 updated coupled).

7. **Frontmatter shape conformance — TASK-0029 handoff PMN-007 HEAD canonical 12-field + PR-39 review-context 1-field**. Verifiable at pre-commit:
   - bash: `head -14 docs/handoffs/TASK-0029-adr-007-part-c-scoping.md` shows 12-field frontmatter with `task_id: TASK-0029` + `framework_version_dogfooded: AMAS v2.25 → v2.26` + `status: drafted`.
   - bash: `grep -cE "^(task_id|title|pr|branch|linked_predecessor|linked_successor|linked_pr|framework_version_dogfooded|production_target|spec_source|date_authored|status):" docs/handoffs/TASK-0029-adr-007-part-c-scoping.md` returns `12`.
   - bash: `grep -cE "^linked_pr: PR-39 \(Builder fills with squash SHA post-merge per PMN-001 \(k\)\)$" docs/handoffs/TASK-0029-adr-007-part-c-scoping.md` returns `1` (canonical placeholder regex form per `.github/scripts/linked-pr-fix-up.py:35`; pre-applied at MC-C empirical pre-application step (j) at pre-flight).
   - bash: `head -3 docs/reviews/PR-39-codex-pre-commit.md` shows `status: drafted` 1-field frontmatter.
   - Class: MC-C empirical pre-application + PMN-007 HEAD canonical form compliance + PMN-009 (i.5) sub-shape A verify-at-authoring.

8. **(j) all-instances grep sweep on cycle-introduced references — clean propagation**. Verifiable at pre-commit:
   - bash: `grep -nE "ADR-007" docs/adr/ADR-007-part-c-materialization-scoping.md docs/adr/ADR-006-product-delivery-pivot-pr-plan-amendment.md README.md docs/handoffs/TASK-0029-adr-007-part-c-scoping.md docs/reviews/PR-39-codex-pre-commit.md` returns ≥1 line on each of the 5 surfaces (cycle-coupled cross-references resolve).
   - bash: `grep -nE "TASK-0029" docs/handoffs/TASK-0029-adr-007-part-c-scoping.md docs/reviews/PR-39-codex-pre-commit.md` returns ≥1 line each (cycle ID resolves on co-shipped artifacts).
   - bash: `grep -nE "PR-39" docs/handoffs/TASK-0029-adr-007-part-c-scoping.md docs/reviews/PR-39-codex-pre-commit.md` returns ≥1 line each.
   - Class: PMN-007 §3.3 (j) all-instances propagation-residual sweep + canonical-impact-surface-completeness check.

## Reviewer focus

- **Substantive content shape**: ADR-007 §Decision 1 + §Consequences placement diagram + README Roadmap rewrite all use ADR-006 D2 actual batch labels per Architect step 4.1 stop-and-show Corrections 1-3 absorption. Verify no residual drifted labels (e.g., "canonical-law-Part-A (P2)", "canonical-law-Part-B (P3)", "tool-inventory (P6)", "surfaces-manifest (P7)") outside the historical context discussion in handoff §1.1 Honesty record.
- **§-citation resolution against current canonical state**: forward-references in ADR-007 + handoff + review-context resolve in current canonical state per PMN-010 sub-shape 1 (with `(forthcoming at Part C+)` qualifier on substrate-only sections; ADR-007 §Cross-references resolve against ADR-001 through ADR-006 + PMN-001/007/010 + transition plan v0.2 + FEAT-0001).
- **Cumulative-diff-stats matches review-context claims**: re-derived per (e.1) at pre-commit; anticipation ~360-500 ins / ~10-20 del across ~7-8 files (default-cycle ±20% MC-A tolerance).
- **Frontmatter shape conformance**: PMN-007 HEAD canonical 12-field handoff + 1-field review-context.
- **(j)/(g)/(h)/(i) sweeps on review-context's own claim blocks** (per PMN-008 §5.8): verify claim-block self-consistency.
- **Recursive-self-instantiation salience MEDIUM** (per PMN-008 §3.1): handoff §1.1 Honesty record documents (k.1) NEGATIVE self-instantiation event at step 4.1 — Architect drift-asserted ADR-006 D2 batch labels in spec §4.1 + §4.3; Builder cross-surface verify-before-assert catch; Architect path-(a) Corrections 1-3 ratified. MAXIMUM-salience signal: defect class recurred at very next cycle's Architect spec authoring AFTER §24 + §23.6.3 sub-shape A canonicalization at TASK-0028. Refinement candidate at TASK-0030+: extend canonical-impact-surface-completeness check to "claims about repo state of OTHER referenced canonical surfaces" via `project_knowledge_search` verification at spec authoring time.

## Codex desktop pre-commit kickoff

```
Please review the pending changes on the current branch (adr/task-0029-adr-007-part-c-scoping) per the review-context at docs/reviews/PR-39-codex-pre-commit.md. Working tree at staged-tree state per TASK-0025 cycle-close Item 4 lesson.

Cycle scope: 5 substantive content edits + 2 co-shipped artifacts. ADR-007 new file canonicalizes Part C materialization scoping decision (amends ADR-006 D2 by inserting Part C.1 + Part C.2 batches into canonical batch sequence; D1 + D3 + D4 preserved). ADR-006 §Status amendment records further partial-supersession. README Roadmap rewrite acknowledges ADR-007 schedule (Correction 3 form per step 4.1 absorption with actual ADR-006 D2 labels). Class A v-bump v2.25 → v2.26 minor tier per §18.4 (4 byte-exact substitutions across 3 sites). core.md §18.3 M-A7 15th-instance amendment (in-place v2.25 paragraph refinement; PR-37 = 15th per Item 13 inclusive read ratification at TASK-0028). Co-shipped: TASK-0029 handoff (PMN-007 HEAD canonical 12-field) + PR-39 review-context (1-field).

Pre-flight + step-1 stop-and-show: 5 Phase 1 adjudications all ratified (Decision 2 split structure / Class A minor tier / M-A7 PR-37 inclusive read / Roadmap single-paragraph scope / spec §4.1 byte-exact prescription) + Builder §Context refinement discretion ratified. Step 4.1 stop-and-show absorbed Architect path-(a) Corrections 1-3 for spec §4.1 + §4.3 ADR-006 D2 batch label drift (cross-surface verify-before-assert finding caught by Builder pre-commit; MAXIMUM-salience (k.1) NEGATIVE self-instantiation event documented at handoff §1.1 Honesty record).

Per ADR-001 D11 owner-invokes convention: please run pre-commit review, surface findings per severity (Blocking → handback; Major → path-(a)/(β); Minor → default path-(b)). Substantive verdict via formal review (`gh pr view` reviews endpoint) preferred; issue-comment summary acceptable; line-level review-comments acceptable.

Verbatim-output convention: capture review verbatim into the review-context file ## Codex desktop pre-commit output absorption section.
```

## Codex desktop pre-commit output absorption

Initial state: placeholder — populated post-Codex-pass per PMN-002 (a) verbatim-output convention.

### Codex pass 1 (UTC 2026-05-08T10:33:01Z)

**Verdict**: COMMENT — no Blocking or Major findings; one Minor delivery-artifact consistency finding. Substantive ADR-007 / ADR-006 / README / Class A v-bump / core.md M-A7 content checks passed against the staged tree.

**Findings** (verbatim):

> **Minor**
>
> 1. `docs/handoffs/TASK-0029-adr-007-part-c-scoping.md:55` says the current state has "7 files in working tree", but the staged tree has 8 files (`git diff --staged --name-only` returns 8; `git status --porcelain` shows 5 staged-modified + 3 staged-added), and the same handoff immediately lists 8 authored/modified files at lines 58-65. This is a delivery-layer self-consistency/count drift only; it does not affect the substantive ADR-007 scoping decision, README roadmap rewrite, Class A v-bump, or core.md M-A7 amendment.
>
> **Validation notes**
>
> - Staged shape verified: branch `adr/task-0029-adr-007-part-c-scoping`; 5 modified + 3 added files; `git diff --staged --stat` reports 8 files changed, 439 insertions, 7 deletions.
> - ADR-006 D2 batch labels checked against ADR-006 actual rows: P1 process templates; P2 GitHub-artifact templates; P3 prompts; P4 Actions; P5 flat appendices; P6 project-type appendices; P7 receiving-surface adapter packs; P8 release/final README polish. ADR-007 Decision 1, ADR-007 Consequences, and README Roadmap use the corrected label set in staged files.
> - Class A v-bump verified on scoped surfaces: README / AGENTS / CLAUDE contain 4 total `v2.26` occurrences and no residual `v2.25` on those three files.
> - core.md M-A7 amendment verified: enumeration includes `PR-37 = 15`, span is `v2.16 through v2.25`, and the amended paragraph no longer carries the prior `= 14` / `v2.24` wording.
> - Frontmatter shape verified: TASK-0029 handoff has the 12 expected frontmatter fields; PR-39 review-context has the 1-field `status: drafted` frontmatter.
> - GitHub PR lookup verified with network-enabled `gh pr list --head adr/task-0029-adr-007-part-c-scoping --json number,title,state,url`: no PR exists yet (`[]`), so no formal PR review endpoint is available at pre-PR-open time.
> - Mandatory v2.14.1 substrate URL from AGENTS.md was attempted via GitHub page and raw URL; both returned unavailable/404 in this environment. Review proceeded against the local v3 canonical trio and current staged artifacts.

**Adjudication** (per ADR-001 D11):

- Reviewer recommendation: Minor defaults to path-(b) record-and-proceed unless the Builder/Architect elects a surgical path-(a) wording fix before commit.

**Resolution applied** (if path-(a)):

- Builder applied path-(a) revise post-Codex-pass-1 absorption per `core.md` §8.1.1.3 pure-token-swap class one-iteration cost: handoff §Current state line 55 `7 files in working tree` → `8 files staged on branch adr/task-0029-adr-007-part-c-scoping (5 modified + 3 added)`; handoff §3 step-record + §6 absorption record updated coupled. Rationale: cycle's MAXIMAL surface-enumeration directive + within-surface sub-component-enumeration sub-discipline applied from inception this cycle make path-(a) one-line revise the canonical-correct routing for delivery-artifact self-consistency drift even at Minor severity (improves durable resume anchor + signals discipline application at within-cycle granularity). One-iteration convergence verified by re-derived staged-tree state: 8 files / 451 ins / 7 del (matches Codex final-staged report exactly).

### Codex post-PR pass 1 (UTC 2026-05-08T10:51:26Z formal-review submitted_at; reviewed commit `cc99bfed62`)

**Three-endpoint poll** per `core.md` §8.1.1.1:
- `pulls/39/reviews`: 1 formal review (ID 4251668342, state COMMENTED; boilerplate "💡 Codex Review" header — substantive landing endpoint A line-level)
- `issues/39/comments`: 1 owner kickoff `@codex review` from `bryce-murphy` 2026-05-08T10:48:38Z (no Codex issue-comment summary)
- `pulls/39/comments`: 1 line-comment from `chatgpt-codex-connector[bot]` at `docs/handoffs/TASK-0029-adr-007-part-c-scoping.md` line 51 (P2 severity)

**Verdict**: COMMENTED (substantive landing endpoint A line-level)

**Findings** (verbatim per PMN-002 (a)):

> **P2  Update the stale last-completed-step state**
>
> This handoff is the durable resume point for TASK-0029, but it still says execution is only at Step 8 and is awaiting self-review/pre-commit. Later in the same new handoff it records that steps 1–11 and Codex pre-commit absorption are complete, and the current-state summary says the pre-commit finding was already absorbed, so anyone resuming from the required `Last completed step` field would be sent back to already-completed work instead of the actual next step.

**Adjudication** (per `core.md` §8.1.1.3 + ADR-006 D3 evidence-bar + Item 13 sub-class diagnostic refinement framing):

- **Severity**: P2 (Codex yellow tier ≈ Major in three-level taxonomy). Substantive defect at durable resume anchor.
- **Class**: Delivery-artifact self-consistency drift in handoff state-snapshot fields. **Same defect class as pre-commit pass-1 Minor** (handoff §Current state L55 "7 files" undercount); within-cycle 2nd instance.
- **Generative-gap diagnosis**: Item 14 sub-discipline applied at substantive-content authoring time but NOT extended to absorption-time updates of structurally-parallel state-snapshot fields. At step-11 pre-commit absorption time, §Current state + §3 + §6 were updated coupled but `## Last completed step` was missed — same generative gap. (k.1) self-instantiation evidence at MAXIMUM salience for Item 14 absorption-time-extension candidacy.
- **Routing**: path-(a) revise. Pure-token-swap class on a single field. One-iteration cost. Architect ratified path-(a) per Builder enumeration of 6 surfaces 2026-05-08.

**Resolution applied** (path-(a) Architect-ratified 2026-05-08):

- Edit 13.1.1: handoff `## Last completed step` field rewritten to reflect actual state (Step 12 commit `cc99bfe` + push + PR-39 OPEN; Step 13 post-PR Codex pass-1 absorption fix-up commit in progress). Verifiable: `grep -nE "Step 13 post-PR Codex pass-1 path-\(a\) absorption fix-up commit" docs/handoffs/TASK-0029-adr-007-part-c-scoping.md` returns 1 line at line 51.
- Edit 13.1.2: handoff §3 step-record extended to Steps 1-13.1 with full execution detail.
- Edit 13.1.3: handoff §6 unchanged (already adequate; post-PR record at §8 per body-section convention).
- Edit 13.1.4: handoff §8 populated verbatim per PMN-002 (a) + TASK-0028 §8 pattern (parallel to this section).
- Edit 13.1.5: handoff §10 ledger Item carry-forward added with Architect-ratified wording (within-cycle defect-class recurrence; Item 14 absorption-time-extension refinement candidate at TASK-0030+).
- Edit 13.1.6: this section appended to review-context per PMN-002 (a) verbatim convention.

**Pass-2 anticipation per Item 13 anti-binary-routing**:
- Most likely: clean APPROVE/COMMENT with no findings (path-(a) absorption converges; same-class recurrence resolved at all 6 enumerated surfaces).
- Possible: incidental refinements at adjacent surfaces (sub-class diagnostic refinement; e.g., review-context post-PR section formatting nuance, §10 ledger Item wording).
- Less likely but admissible: NEW defect class surfaces (would route new path-(a)/(β) per `core.md` §8.1.1.3 evidence-bar at adjudication time).
- Bandwidth budget: ~1 path-(a) iteration at most.

### Codex post-PR pass 2 (UTC 2026-05-08T11:07:25Z formal-review submitted_at; reviewed commit `7f45785e528cf01225d092deabce6ef569c3fbf0`)

**Three-endpoint poll** per `core.md` §8.1.1.1:
- `pulls/39/reviews`: pass-2 formal review (ID 4251749913, state COMMENTED; boilerplate "💡 Codex Review" header — substantive landing endpoint A line-level)
- `issues/39/comments`: pass-2 owner kickoff `@codex review` from `bryce-murphy` 2026-05-08T11:05:07Z
- `pulls/39/comments`: 1 NEW line-comment from `chatgpt-codex-connector[bot]` at `docs/adr/ADR-007-part-c-materialization-scoping.md` line 23 (P2 severity)

**Verdict**: COMMENTED (substantive landing endpoint A line-level)

**Findings** (verbatim per PMN-002 (a)):

> **P2  Correct the Part C qualifier count**
>
> The empirical qualifier population in this ADR is overstated: rerunning `rg -o --fixed-strings '(forthcoming at Part C+)' usage-guide.md templates/handoff-template.md templates/review-template.md AGENTS.md CLAUDE.md core.md github-reference.md` on the reviewed tree gives 35 instances across 28 lines, with `templates/handoff-template.md` contributing 5 instances rather than 7. Because this count is used here to justify and scope the Part C.1/C.2 materialization batches and future cleanup sweeps, leaving the ADR with the wrong baseline will make those follow-up cycles verify against a stale target.

**Adjudication** (per `core.md` §8.1.1.3 + ADR-006 D3 evidence-bar + Item 13 anti-binary-routing framing):

- **Severity**: P2 (Codex yellow tier ≈ Major). Substantive defect at ADR-007 §Context empirical evidence base — count is load-bearing for ADR scoping rationale and downstream cleanup-sweep cycles will verify against a stale target if uncorrected.
- **Class**: **NEW defect class** — Methodological calibration in empirical-evidence enumeration. Distinct from prior 2 within-cycle instances (delivery-artifact self-consistency drift). Pre-flight qualifier sweep used loose regex `forthcoming at Part C` rather than strict literal `(forthcoming at Part C+)`.
- **Routing**: path-(a) revise. Substantive content correctness gating ADR scoping rationale; not record-and-proceed candidate. Architect ratified path-(a) per Builder enumeration of 7 surfaces with §Context two-form/sub-variant framing + §10 ledger Items N+1/N+2/N+3 wording refinements 2026-05-08.
- **Item 13 empirical positive**: pass-2 surfaced the "less likely but admissible: NEW defect class" outcome explicitly admitted in pass-1 absorption pass-2 anticipation framing. Direct empirical positive for Item 13 anti-binary-routing sub-discipline (1st explicit empirical-positive instance).

**Empirical verification** (Builder re-ran strict-literal pattern at adjudication time):
- `grep -oF "(forthcoming at Part C+)"` per surface: usage-guide.md 27/20; templates/handoff-template.md 5/5; templates/review-template.md 0/0; AGENTS.md 1/1; CLAUDE.md 2/2; core.md 0/0; github-reference.md 0/0. Sum: **35 instances / 28 distinct lines** ✓ (matches Codex exactly).
- Diagnostic on Builder pre-flight loose-regex over-count: 2 lines at templates/handoff-template.md L142 (`...substrate (forthcoming at Part C+ in v3 core.md)`) + L150 (`(handoff schema; forthcoming at Part C+)`) match loose pattern but not strict literal — Form (a) syntactic sub-variant per ADR-007 §Context corrected wording.

**Resolution applied** (path-(a) Architect-ratified 2026-05-08; 7 surfaces per Architect refinements):

- Edit 13.2.1: ADR-007 §Context — count corrected from 37/30 to 35/28 strict-literal canonical with two-form/sub-variant framing (Form (a) canonical sub-variant 35/28 + Form (a) syntactic sub-variant 2 instances at templates/handoff-template.md L142+L150 + Form (b) unmarked forward-references at §13.2/§17.7/§23.6.5).
- Edit 13.2.2: handoff §1.1 Honesty record — methodological calibration acknowledgment.
- Edit 13.2.3: handoff `## Last completed step` — Step 13.2 absorption in progress.
- Edit 13.2.4: handoff §3 step-record extended Steps 1-13.1 → Steps 1-13.2.
- Edit 13.2.5: handoff §8 populated verbatim per PMN-002 (a) + TASK-0028 §8 pattern.
- Edit 13.2.6: handoff §10 ledger — Items N+1/N+2/N+3 added with Architect-refined wording (NEW defect class multi-surface chain + Item 13 empirical positive + Item 14 absorption-time extension durable).
- Edit 13.2.7: this section appended to review-context per PMN-002 (a).

**Pass-3 anticipation per Item 13 anti-binary-routing**:
- Most likely: clean APPROVE/COMMENT (path-(a) absorption converges; corrected count + acknowledged calibration; multi-surface defect chain absorbed at all 7 enumerated surfaces).
- Possible: incidental refinements at adjacent surfaces (e.g., §Context wording, §10 ledger wording, sub-variant labeling).
- Less likely but admissible: ANOTHER new defect class would extend bounded-continuation rule iteration count per `core.md` §8.1.1.3 cost-class refinement (3 iteration ceiling at default-cycle; can extend to 4-5 at architectural-class with owner ratification).
- Bandwidth budget: ~1 path-(a) iteration at most.
