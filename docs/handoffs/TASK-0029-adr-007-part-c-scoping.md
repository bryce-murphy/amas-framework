---
task_id: TASK-0029
title: ADR-007 Part C materialization scoping decision (amends ADR-006 D2)
pr: PR-39
branch: adr/task-0029-adr-007-part-c-scoping
linked_predecessor: TASK-0028 (PR-37 squash f677532 substantive: bundled lightweight absorption Items 4+10+11+12+14 + M-A7 14th + Class A v2.24 → v2.25 patch v-bump; PR-38 squash 3b722d6 chore-fix-up per PMN-001 (k))
linked_successor: TBD
linked_pr: PR-39 (Builder fills with squash SHA post-merge per PMN-001 (k))
framework_version_dogfooded: AMAS v2.25 → v2.26
production_target: AMAS v3.0
spec_source: .claude/session-handoffs/TASK-0029-spec.md (gitignored per ADR-001 D15)
date_authored: 2026-05-07
status: drafted
---

# HANDOFF: TASK-0029

## Metadata

- Task ID: TASK-0029 (matches PR-39 anticipated; first cycle executing ADR-007 ship — architectural-class direction-decision per ADR-005 substantive-direction-decision precedent + ADR-006 partial-supersession pattern)
- Linked Issue: none
- Linked PR: PR-39 — URL TBD at PR-open (substituted at step-13 per PMN-001 (k) deferred-substitution discipline)
- Linked ADR(s): **ADR-007** (this cycle ships); **ADR-006** (Decision 2 further-partially-superseded by ADR-007 Decision 2 inserting Part C.1 + Part C.2; D1 + D3 + D4 preserved; §Status amendment landed); ADR-003 (preserved through ADR-006 + ADR-007); ADR-001 D9/D11/D15; ADR-002 / ADR-004 / ADR-005 cited at ADR-007 §Cross-references.
- Linked Feature Brief: none (ADR-class direction-decision cycle; no FEAT)
- Linked review-context file: docs/reviews/PR-39-codex-pre-commit.md
- Linked PMN(s): PMN-001 (k) (chore-fix-up substitution discipline; canonical regex empirical pre-application at pre-flight); PMN-002 (a) (verbatim-output convention); PMN-002 (d) (code-fenced kickoff prompt); PMN-007 HEAD canonical 12-field handoff frontmatter form (applied here); PMN-008 §3.1 (k.1) self-instantiation framework (cycle surfaces a NEGATIVE (k.1) instance — see §1.1 Honesty record); PMN-009 / `core.md` §23.6.3 (sub-shape A verify-at-authoring batch + canonical-impact-surface-completeness check applied at this Builder pre-flight); PMN-010 §2 sub-shape 1 (forward-ref §-citation correctness applied across ADR-007 §Cross-references + handoff + review-context).
- Owner role: Builder (Claude Sonnet 4.6, Claude Code, owner's local session)
- Previous role: Architect (Claude Opus 4.7, Claude.ai Project)
- Timestamp (UTC): cycle execution in progress
- Last synced commit SHA: `3b722d6897f580e1f14a8ffe6a9fc2ca59331856` (PR-38 chore-fix-up squash for TASK-0028 linked-PR substitution per PMN-001 (k); auto-fired by linked-pr-fix-up Action; verified at pre-flight 2026-05-07 against `git rev-parse origin/main` after `git fetch origin && git pull --ff-only origin main` returned `Already up to date`).
- Branch: `adr/task-0029-adr-007-part-c-scoping` (Option B canonical form per ADR-005; adr-type per architectural cycle class; matches `^(feat|fix|chore|adr|shadow|spike)/task-[0-9]{4}-([a-z0-9]|[a-z0-9][a-z0-9.-]*[a-z0-9])$` regex).
- Status: drafted
- Direction: Architect → Builder (universal handoff schema, v2.14.1 §14.1 substrate; forthcoming at Part C+ in v3 core.md)
- Framework version: AMAS v2.25 → v2.26 (Class A minor v-bump at this cycle per `core.md` §18.4 minor tier — substantive new canonical text in feature-class cluster: ADR-007 canonicalizing architectural decision)
- Recursive-self-instantiation salience: **MEDIUM** (escalated from spec-anticipated LOW-MEDIUM per (k.1) NEGATIVE self-instantiation event surfaced at step 4.1 — see §1.1 Honesty record). Justification: spec §4.1 byte-exact prescription contained drift-asserted ADR-006 D2 batch labels; Builder caught at cross-surface verify-before-assert pre-commit, Architect adjudicated path-(a) with structural refinement (Corrections 1-3) at step 4.1 stop-and-show. Direct empirical evidence for §23.6.3 sub-shape A canonical-impact-surface-completeness extension candidate (TASK-0030+).

## Objective

Five coupled substantive content edits + 2 co-shipped artifacts in single PR. Cycle-class architectural (ADR-class direction-decision):

1. **ADR-007 new file** at `docs/adr/ADR-007-part-c-materialization-scoping.md` — canonicalizes Part C materialization scoping decision; amends ADR-006 D2 by inserting Part C.1 + Part C.2 batches into the canonical batch sequence; ADR-006 D1 + D3 + D4 preserved.
2. **ADR-006 §Status amendment** — single-line append per ADR-002 amendment-pattern precedent recording further partial-supersession of D2 by ADR-007.
3. **README "Roadmap" paragraph rewrite** — acknowledges ADR-007 Part C.1 / Part C.2 schedule per Decision 3; preserves ADR-003 + ADR-006 cross-references; adds ADR-007 cross-reference.
4. **Class A v-bump v2.25 → v2.26 minor tier** per §18.4 — 4 byte-exact substitutions across 3 sites: README:9 (×2), AGENTS.md:9 (×1), CLAUDE.md:9 (×1).
5. **core.md §18.3 M-A7 15th-instance amendment** — in-place v2.25 cumulative-instances paragraph refinement extending enumeration to `... + PR-35 + PR-37 = 15`; preamble updates to v2.26 / PR-39 / TASK-0029 per Item 13 inclusive M-A7 read ratification at TASK-0028.

Co-shipped: TASK-0029 handoff (this file) + PR-39 Codex desktop pre-commit review-context.

## Last completed step

Step 13 post-PR Codex pass-1 path-(a) absorption fix-up commit (this edit) — Codex post-PR pass-1 P2 line-comment on this very `## Last completed step` field flagged delivery-artifact self-consistency drift (within-cycle 2nd instance of same defect class as pre-commit pass-1 Minor at §Current state L55); Architect ratified path-(a) revise across 6 surfaces (this field + §3 step-record + §6 + §8 verbatim absorption + §10 ledger Item carry-forward + review-context append). Prior completed: Step 12 commit `cc99bfe` + push to `origin/adr/task-0029-adr-007-part-c-scoping` + `gh pr create` → PR-39 OPEN at https://github.com/bryce-murphy/amas-framework/pull/39. Awaiting fix-up commit + push (gated by `core.md` §8.3 stop-and-show); owner re-invokes `@codex review` for pass-2 verification post-push (Codex auto-trigger only on PR-open / draft-ready / explicit `@codex review`; fix-up push does not auto-fire). Anticipated pass-2 shape per Item 13 anti-binary-routing: most likely clean APPROVE/COMMENT with no findings; possible incidental refinements at adjacent surfaces (sub-class diagnostic refinement); admissible new-defect-class surface routes new path-(a)/(β) per `core.md` §8.1.1.3 evidence-bar at adjudication time. Post pass-2 clean-absorb → step 17 hand-back to Architect with §24.3.1 five-point check.

## Current state

**Summary**: 8 files staged on branch `adr/task-0029-adr-007-part-c-scoping` (5 modified + 3 added). Substantive content edits applied per spec §4 byte-exact prescriptions with Architect-adjudicated path-(a) Corrections 1-3 absorbed at step 4.1 stop-and-show. Codex desktop pre-commit pass-1 absorbed (verdict COMMENT; 1 Minor delivery-artifact self-consistency finding; path-(a) revise applied — this edit).

**Files authored / modified by Builder**:
1. NEW `docs/adr/ADR-007-part-c-materialization-scoping.md` — full ADR per spec §4.1 with Corrections 1+2 absorbed (§Decision 1 first-paragraph batch enumeration uses ADR-006 D2 actual labels; §Consequences placement diagram uses actual labels with C.1-within-P1 + C.2-between-P3-P4 framing); §Context refinement included (acknowledges dual qualifier-marked + unmarked forward-reference forms per Builder pre-flight empirical sweep — 37 instances / 30 lines on canonical surfaces).
2. MODIFIED `docs/adr/ADR-006-product-delivery-pivot-pr-plan-amendment.md` §Status — single-line amendment append per ADR-002 amendment-pattern precedent.
3. MODIFIED `README.md` line 30 (Roadmap paragraph rewrite per Correction 3) + line 9 (×2 v2.25 → v2.26 Class A v-bump).
4. MODIFIED `AGENTS.md` line 9 — Class A v-bump (×1 inline mention).
5. MODIFIED `CLAUDE.md` line 9 — Class A v-bump (×1 inline mention).
6. MODIFIED `core.md` §18.3 lines 238 + 240 + 242 — M-A7 15th-instance in-place paragraph refinement (4 byte-exact substitutions: preamble v2.25 → v2.26 / PR-37 → PR-39 / TASK-0028 → TASK-0029; enumeration `... + PR-35 = 14` → `... + PR-35 + PR-37 = 15`; span-text `v2.16 through v2.24` → `v2.16 through v2.25`; count `14 consecutive` → `15 consecutive`).
7. NEW `docs/handoffs/TASK-0029-adr-007-part-c-scoping.md` — this file.
8. NEW `docs/reviews/PR-39-codex-pre-commit.md` — co-shipped review-context per templates/review-template.md canonical form.

**Cumulative-diff-stats** (per `core.md` §23.6.1.1 (e.1) staged-tree convention): re-derived at step 9.5 pre-commit per (e.1) sub-rule. Anticipation: ~360-500 ins / ~10-20 del across ~7-8 files (default-cycle ±20% MC-A tolerance per Item 10 calibration; architectural-class cycle).

## Decisions made

- **§0.1 standing scope ratifications** (locked pre-Builder execution per spec §0.1; three-cycle plan ratified by owner 2026-05-07): TASK-0028 = bundled lightweight absorption + M-A7 chore (closed); TASK-0029 = ADR-007 Part C scoping decision (this cycle); TASK-0030 = Part C.1 substantive content materialization per ADR-007 D3 schedule (next).

- **Step-1 stop-and-show 5 Phase 1 owner adjudications** (all 5 ratified 2026-05-07):
  - **Adjudication 1 (PRIMARY) — Decision 2 split structure boundaries**: ratified Architect-recommended split. Part C.1 = `core.md` §14 + §14.1-§14.7 + §17.5 + §17.7 (cycle-execution canonical surfaces); Part C.2 = `core.md` §8.2 + §8.3 + §13 (+§13.1/§13.2) + §10.5 + §23.6.5 (operating-discipline canonical surfaces). Other forward-referenced sections fold per topic at substantive-content cycles.
  - **Adjudication 2 — Class A v-bump tier**: ratified minor v2.25 → v2.26 per §18.4 (substantive new canonical text in feature-class cluster — ADR canonicalizing architectural decision).
  - **Adjudication 3 — M-A7 inclusion of PR-37 as 15th-instance**: ratified inclusive read per TASK-0028 ledger Item 13 ratification; PR-37 = M-A7-eligible 15th-instance enumeration this cycle; PR-39 candidate 16th-instance at TASK-0030+ post-merge maintenance authoring.
  - **Adjudication 4 — README Roadmap rewrite scope**: ratified single-paragraph update preserving ADR-003 + ADR-006 cross-references + adding ADR-007 cross-reference.
  - **Adjudication 5 — ADR-007 §Decision content refinements**: ratified spec §4.1 byte-exact prescription (subsequently amended at step 4.1 stop-and-show — see §1.1 Honesty record).

- **Step 4.1 stop-and-show — substantive cross-surface verify-before-assert finding** (Builder caught; Architect path-(a) adjudication ratified 2026-05-07): Spec §4.1 ADR-007 §Decision 1 enumeration of ADR-006 D2 batch labels + §Consequences placement diagram + spec §4.3 Roadmap rewrite text contained drifted batch labels (P2 = "canonical-law-Part-A" instead of actual "GitHub-artifact templates"; P3 = "canonical-law-Part-B" instead of actual "prompts"; P6 = "tool-inventory" instead of actual "project-type appendices" — tool-inventory is in P1; P7 = "surfaces-manifest" instead of actual "receiving-surface adapter packs" — surfaces-manifest is in P1). Architect adjudicated path-(a) absorption with structural refinement: Correction 1 (§Decision 1 first-paragraph rewrite using actual ADR-006 D2 labels with explicit framing "canonical-law-Part-A/B shipped at earlier substantive cycles + Part C is INTERNAL to core.md"); Correction 2 (§Consequences placement-diagram rewrite with C.1-within-P1 + C.2-between-P3-P4 framing); Correction 3 (README Roadmap rewrite using actual ADR-006 D2 labels). All three corrections applied at substantive-content authoring time before any commit.

- **§Context empirical refinement** (Builder authoring discretion ratified at step-1 stop-and-show): ADR-007 §Context includes empirical observation from Builder pre-flight — 37 explicit `(forthcoming at Part C+)` qualifier instances on 30 distinct lines across 4 canonical surfaces (usage-guide.md 27/20; templates/handoff-template.md 7/7; CLAUDE.md 2/2; AGENTS.md 1/1) + acknowledgment of secondary unmarked forward-reference form (§13.2 / §17.7 / §23.6.5 cited without qualifier marker). Strengthens §Context evidence base; marginal text addition (~3 lines).

## Assumptions

- Repo-state at pre-flight: clean working tree on main; local HEAD at `3b722d6` (PR-38) was already up to date with remote (no fast-forward needed).
- Branch protection per ADR-001 D9 admin-bypass posture (Posture 2 Rulesets); owner squash-merge bypass authorized at step-17.
- `gh` CLI authenticated with bryce-murphy/amas-framework repo scope.
- Codex desktop pre-commit Reviewer (GPT-5.5) operational per ADR-001 D11 owner-invokes convention; owner pastes kickoff prompt at step 11.
- linked-pr-fix-up Action shipped at PR-21 (per ADR-004) operational; canonical regex at `.github/scripts/linked-pr-fix-up.py:35` matches `linked_pr: PR-39 (Builder fills with squash SHA post-merge per PMN-001 (k))` (verified empirically at pre-flight via Python re.match).

## §1. Cycle scope

Five substantive content edits per spec §1 (parallel above) + 2 co-shipped artifacts (handoff + review-context). All five substantive edits applied byte-exactly per spec §4.1-§4.5 prescriptions with Architect-adjudicated path-(a) Corrections 1-3 absorbed at step 4.1.

### §1.1 Honesty record per `core.md` §23.6.3 + carry-forward to §10 ledger

**(k.1) NEGATIVE self-instantiation event at step 4.1 — substantive cross-surface verify-before-assert defect at Architect spec authoring** (MAXIMUM-salience signal):

At step 4.1 substantive-content authoring of ADR-007, Builder identified that spec §4.1 ADR-007 §Decision 1 enumeration of ADR-006 D2 batch labels was factually wrong against actual ADR-006 §Decision 2 content. The drifted labels propagated into §Consequences placement diagram + spec §4.3 Roadmap rewrite text. Specifically:

| Batch | Spec §4.1 (drifted) | ADR-006 D2 actual |
|---|---|---|
| P2 | canonical-law-Part-A | GitHub-artifact templates |
| P3 | canonical-law-Part-B | prompts |
| P6 | tool-inventory | project-type appendices (tool-inventory is in P1) |
| P7 | surfaces-manifest | receiving-surface adapter packs (surfaces-manifest is in P1) |
| P8 | final adoption | release tag + final README polish |

Builder caught at cross-surface verify-before-assert per `core.md` §24 (locating ADR-006 §Decision 2 for Roadmap rewrite step; sub-shape A canonical-impact-surface-completeness check extended to "claims about repo state of OTHER referenced canonical surfaces" beyond edit-target surfaces). Stop-and-show surfaced finding pre-commit. Architect adjudicated path-(a) absorption with structural refinement (Corrections 1-3) 2026-05-07; all three corrections applied before commit.

**MAXIMUM-salience signal**: this defect occurred at the very next cycle's Architect spec authoring AFTER `core.md` §24 cross-surface verify-before-assert canonicalization at TASK-0028 + §23.6.3 sub-shape A extensions (canonical-impact-surface-completeness check + template-content authoring meta-pattern) + Item 14 within-surface sub-component-enumeration sub-discipline canonicalization. Even with extensive forward calibration applied (Items 6+9+14 from inception), the underlying drift-assertion defect class recurred at Architect-side spec authoring. This is direct empirical evidence for a §23.6.3 sub-shape A extension candidate at TASK-0030+: extend canonical-impact-surface-completeness check to include "claims about repo state of OTHER referenced canonical surfaces" (not just edit-target surfaces), via `project_knowledge_search` verification at spec authoring time.

**Verified at Builder pre-flight (i.5) batch** (sub-shape B verify-at-authoring complete):
- `git fetch origin && git pull --ff-only origin main` → `Already up to date`; HEAD = `3b722d6` ✓ matches anticipated PR-38 squash.
- `git status` → clean working tree pre-branch-creation.
- `gh pr list --state merged --limit 4` → PR-38 + PR-37 + PR-36 + PR-35 ✓ matches spec enumeration.
- `gh pr list --state open` → zero open PRs ✓.
- Part C qualifier empirical enumeration `grep -rnE "forthcoming at Part C" --include="*.md" .` → 37 instances on 30 distinct lines across 4 canonical-tracked surfaces (usage-guide.md 27/20; templates/handoff-template.md 7/7; CLAUDE.md 2/2; AGENTS.md 1/1) + 2 instances on 2 lines in templates/handoff-template.md cross-references; aggregate matches spec §Context anticipation "~30+ qualifier instances".
- Class A v-bump byte-exact target line numbers identified before any edits (Item 6+9 MAXIMAL surface-enumeration + Item 14 within-surface sub-component-enumeration applied from inception): README:9 (2 v2.25 instances on same line), AGENTS:9 (1 inline mention), CLAUDE:9 (1 inline mention).
- core.md §18.3 in-place refinement target lines identified before any edits: line 238 (preamble), line 240 (enumeration + span-text), line 242 (count).

**Authored from**: TASK-0029 spec at `.claude/session-handoffs/TASK-0029-spec.md` (gitignored per ADR-001 D15) + Architect-to-Architect handoff §"Strategic three-cycle plan" + ADR-006 D2 batch sequence (verified empirically at step-4.1 finding) + TASK-0028 cycle-close ledger Items 6+9+10+13+14 forward calibration.

## §2. Cycle gates

Standard cycle gates per established convention (TASK-0021 / TASK-0023 / TASK-0025 / TASK-0027 architectural priors); see spec §2.

## §3. Step-by-step execution record

Steps 1-13.1 complete per spec §3.1-§3.7: pre-flight + branch + authoring (4.1-4.5) + co-shipped (5-6) + self-review (9) + pre-commit stop-and-show (10) + Codex desktop pre-commit pass-1 absorption (11) + commit + push + PR-39 OPEN (12) + post-PR Codex pass-1 absorption with path-(a) fix-up (13.1). Step 4.1 stop-and-show event detailed at §1.1 Honesty record. Codex pre-commit pass-1 verdict: COMMENT (1 Minor delivery-artifact self-consistency finding at handoff §Current state line 55 "7 files" undercount; path-(a) revise to "8 files staged ... (5 modified + 3 added)" applied; one-iteration convergence). Step 12 commit `cc99bfe` + push `adr/task-0029-adr-007-part-c-scoping` → `origin` + `gh pr create` → PR-39 OPEN. Step 13.1 post-PR Codex pass-1 (UTC 2026-05-08T10:51:26Z formal-review submitted_at; reviewed commit `cc99bfed62`; substantive landing endpoint A line-comment per `pulls/39/comments`): verdict COMMENTED / 1 P2 line-comment at handoff line 51 `## Last completed step` field stale state — same defect class as pre-commit pass-1 Minor (delivery-artifact self-consistency drift in handoff state-snapshot fields; within-cycle 2nd instance); Architect ratified path-(a) revise across 6 surfaces (this absorption fix-up). Step 13.2 fix-up commit + push pending stop-and-show ratification; step 13.3 owner re-invokes `@codex review` for pass-2 verification; step 17 hand-back to Architect with §24.3.1 five-point check pending post pass-2 clean-absorb.

## §4. Substantive-content evidence

Per-deliverable evidence per spec §6 acceptance criteria — verifiable at pre-commit per claim block in `docs/reviews/PR-39-codex-pre-commit.md`.

## §5. Self-review record

Populated at step 9 per `core.md` §23.6.2 iterative-to-fixed-point with Item 14 within-surface sub-component-enumeration sweep applied.

## §6. Pre-commit absorption

Codex desktop pre-commit pass-1 verbatim absorbed at `docs/reviews/PR-39-codex-pre-commit.md` ## Codex desktop pre-commit output absorption section per PMN-002 (a) verbatim-output convention. Verdict: COMMENT. Findings: 1 Minor (delivery-artifact self-consistency drift at handoff §Current state line 55: "7 files in working tree" undercount vs actual 8 staged; same handoff §Files authored/modified lists 8). Adjudication: path-(a) revise per `core.md` §8.1.1.3 pure-token-swap class one-iteration cost; `7 files in working tree` → `8 files staged ... (5 modified + 3 added)`. Resolution applied at handoff §Current state line 55 + §3 step-record + this section pre-commit (single-iteration convergence; PMN-007 §9.3 (n) cycle-trailing-clean Approve candidate routing pending step-13+ post-PR Codex pass-1).

## §7. Commit + push + PR-open record

Populated at step 12+ post commit/push.

## §8. Post-PR Codex review state

### Codex post-PR pass-1 (UTC 2026-05-08T10:51:26Z formal-review submitted_at; reviewed commit `cc99bfed62`)

**Three-endpoint poll** per `core.md` §8.1.1.1:
- `pulls/39/reviews`: 1 formal review (ID 4251668342, state COMMENTED; boilerplate "💡 Codex Review" header — substantive landing endpoint A line-level)
- `issues/39/comments`: 1 owner kickoff `@codex review` (no Codex issue-comment summary)
- `pulls/39/comments`: 1 line-comment from `chatgpt-codex-connector[bot]` at `docs/handoffs/TASK-0029-adr-007-part-c-scoping.md` line 51 (P2 severity)

**Verdict**: COMMENTED (substantive landing endpoint A line-level)

**Findings** (verbatim per PMN-002 (a)):

> **P2  Update the stale last-completed-step state**
>
> This handoff is the durable resume point for TASK-0029, but it still says execution is only at Step 8 and is awaiting self-review/pre-commit. Later in the same new handoff it records that steps 1–11 and Codex pre-commit absorption are complete, and the current-state summary says the pre-commit finding was already absorbed, so anyone resuming from the required `Last completed step` field would be sent back to already-completed work instead of the actual next step.

**Adjudication** (per `core.md` §8.1.1.3 + ADR-006 D3 evidence-bar + Item 13 sub-class diagnostic refinement framing):

- **Severity**: P2 (Codex yellow tier ≈ Major in three-level taxonomy). Substantive defect at durable resume anchor (`## Last completed step` field) — misstates state vs same-document §3 + §Current state + §6 records.
- **Class**: Delivery-artifact self-consistency drift in handoff state-snapshot fields. **Same defect class as pre-commit pass-1 Minor** (handoff §Current state L55 "7 files" undercount); within-cycle 2nd instance.
- **Generative-gap diagnosis**: Item 14 within-surface sub-component-enumeration sub-discipline applied at substantive-content authoring time (core.md §18.3 M-A7 coupled-shape sub-components clean) but NOT extended to absorption-time updates of structurally-parallel state-snapshot fields. At step-11 pre-commit absorption time, §Current state + §3 + §6 were updated but `## Last completed step` was not — same generative gap.
- **Routing**: path-(a) revise. Pure-token-swap class on a single field (~3 lines original; ~3 lines replacement). One-iteration cost. Clear quality improvement to durable resume anchor.
- Item 13 anti-binary-routing applied: anticipate sub-class diagnostic refinement at pass-2 if emerges (don't pre-commit to "definitely converges" or "definitely needs more iterations"; pass-2 outcome-shape budget per Item 13).

**Resolution applied** (path-(a)):

- Edit 13.1.1: handoff line 51 `## Last completed step` field rewritten — pre-state "Step 8 substantive-content authoring complete..." → post-state "Step 13 post-PR Codex pass-1 path-(a) absorption fix-up commit (this edit)..." with full state-snapshot reflecting Step 12 commit `cc99bfe` + push + PR-39 OPEN landed; awaiting fix-up commit + push gated by §8.3 stop-and-show; pass-2 anticipation per Item 13. Verifiable at next-iteration: `grep -nE "Step 13 post-PR Codex pass-1 path-\(a\) absorption fix-up commit" docs/handoffs/TASK-0029-adr-007-part-c-scoping.md` returns 1 line at line 51.
- Edit 13.1.2: handoff §3 step-record extended — Steps 1-11 → Steps 1-13.1; added Step 12 commit `cc99bfe` + push + PR-39 OPEN; added Step 13.1 post-PR Codex pass-1 with verdict + finding + path-(a) routing; added Step 13.2 fix-up commit + push pending; Step 13.3 pass-2 invocation; Step 17 hand-back post pass-2 clean-absorb.
- Edit 13.1.3: handoff §6 unchanged (already adequate; pre-commit absorption record stands; post-PR absorption record at §8 per body-section convention).
- Edit 13.1.4: handoff §8 (this section) populated verbatim per PMN-002 (a) + TASK-0028 §8 pattern.
- Edit 13.1.5: handoff §10 ledger — within-cycle defect-class recurrence Item carry-forward added with Architect-ratified wording.
- Edit 13.1.6: review-context `docs/reviews/PR-39-codex-pre-commit.md` — Codex post-PR pass-1 absorption section appended per PMN-002 (a) verbatim convention; status field continues `drafted` until post-merge linked-pr-fix-up Action substitutes to `recorded` per PMN-001 (k).

**Pass-2 anticipation per Item 13 anti-binary-routing**:
- Most likely: clean APPROVE/COMMENT with no findings (path-(a) absorption converges; same-class recurrence resolved at all 6 enumerated surfaces).
- Possible: incidental refinements at adjacent surfaces (sub-class diagnostic refinement; e.g., review-context post-PR section formatting nuance, §10 ledger Item wording).
- Less likely but admissible: NEW defect class surfaces (would route new path-(a) or path-(β) per `core.md` §8.1.1.3 evidence-bar at adjudication time).
- Bandwidth budget: ~1 path-(a) iteration at most.

## §9. Sign-off

Populated at step 17 by Architect (§24.3.1 five-point post-handback check).

## §10. Cycle-close ledger

Populated at cycle close. Pre-population candidate carry-forward observations:

- **Item carry-forward (k.1) NEGATIVE self-instantiation event at TASK-0029 spec authoring** (per §1.1 Honesty record): MAXIMUM-salience signal. Architect asserted ADR-006 D2 batch labels (P2 / P3 / P6 / P7 / P8) from drifted mental model rather than verifying against actual ADR-006 §Decision 2 content via `project_knowledge_search`. Builder caught at step 4.1 cross-surface verify-before-assert pre-commit; path-(a) absorption with structural refinement (Corrections 1-3) ratified by Architect 2026-05-07. Refinement candidate at TASK-0030+: §23.6.3 sub-shape A canonical-impact-surface-completeness extension to include "claims about repo state of OTHER referenced canonical surfaces" (not just edit-target surfaces), via `project_knowledge_search` verification at spec authoring time. Pattern: even with extensive forward calibration applied (Items 6+9+14 from inception), the underlying drift-assertion defect class recurs at Architect-side spec authoring.

- **Forward-calibration positive observation**: Item 6+9 MAXIMAL surface-enumeration + Item 14 within-surface sub-component-enumeration applied from inception at Builder pre-flight enabled step 4.1 cross-surface verify-before-assert catch. Without MAXIMAL-enumeration directive, Builder would not have located ADR-006 §Decision 2 content for Roadmap rewrite step until Roadmap authoring; defect would have propagated further (into Roadmap rewrite + downstream artifacts). (k.1) POSITIVE for Builder-side application of forward calibration.

- **MC-A 6th-cycle data point candidate**: cumulative-diff-stats vs anticipation re-derived at step 9.5; default-cycle ±20% MC-A tolerance per Item 10 calibration applies (architectural-class; no MAXIMUM-salience bias).

- **Item carry-forward — Within-cycle defect-class recurrence (delivery-artifact self-consistency drift in handoff state-snapshot fields)** (Architect-ratified wording 2026-05-08): Pre-commit pass-1 Minor caught §Current state L55 "7 files" instance; post-PR pass-1 P2 caught `## Last completed step` field instance. Same defect class; both within TASK-0029. Item 14 sub-discipline applied at substantive-content authoring time (core.md §18.3 coupled-shape sub-components clean) but NOT extended to absorption-time updates of structurally-parallel state-snapshot fields. Refinement candidate at TASK-0030+: extend Item 14 within-surface sub-component-enumeration sub-discipline to apply at absorption-time as well as authoring-time, with state-snapshot field enumeration sweep when any one state-snapshot field is updated per absorption pass. (k.1) self-instantiation evidence at MAXIMUM salience: defect class recurs within single cycle at structurally-parallel handoff fields despite Item 14 forward-calibration directive being load-bearing this cycle.

## §11. Session log archive

(Most recent session in PR body per AMAS v2.14.1 §13.1 substrate; forthcoming at Part C+ in v3 core.md. Prior sessions migrate here at next cycle iteration.)

### Builder session record — 2026-05-07 (Claude Sonnet 4.6, Claude Code, Windows + Bash)

Pre-flight (i.5) batch executed per spec §3.1: HEAD verified at `3b722d6`; 4 merged PRs enumerated; zero open PRs; Part C qualifier empirical sweep returned 37 instances / 30 lines; byte-exact target line numbers identified upfront across 7 surfaces. Step-1 stop-and-show surfaced 5 Phase 1 adjudications + Builder discretion offer at §Context refinement; Architect ratified all 5 + ratified §Context refinement inclusion 2026-05-07. Step 2 branch creation: `git checkout -b adr/task-0029-adr-007-part-c-scoping` from `3b722d6`. Steps 4.1-4.5 substantive content authoring per spec §4 byte-exact prescriptions. Step 4.1 stop-and-show: cross-surface verify-before-assert finding surfaced re ADR-006 D2 batch label drift in spec §4.1 + §4.3; Architect adjudicated path-(a) Corrections 1-3 ratified 2026-05-07; corrections applied to in-flight ADR-007 + README pre-commit. Steps 5-6 co-shipped authoring (this handoff + PR-39 review-context) per templates/handoff-template.md + templates/review-template.md canonical forms. Awaiting step 9 self-review.
