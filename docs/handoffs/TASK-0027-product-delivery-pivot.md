---
task_id: TASK-0027
title: Option Y product-delivery pivot — ADR-006 (ADR-003 D2 partial-supersession) + handoff-template + review-template authoring + M-A7 amendment + README v2.23 → v2.24
pr: PR-35
branch: feat/task-0027-product-delivery-pivot
linked_predecessor: TASK-0026 (PR-33 squash fbe025b substantive: ADR-005 branch-convention canonicalization (Option B) + AGENTS.md/CLAUDE.md → v3 migration + v3 trio reconciliation + README v2.22→v2.23; PR-34 squash e71a4bd chore-fix-up per PMN-001 (k))
linked_successor: TBD
linked_pr: PR-35 (Builder fills with squash SHA post-merge per PMN-001 (k))
framework_version_dogfooded: AMAS v2.23
production_target: AMAS v3.0
spec_source: .claude/session-handoffs/TASK-0027-spec.md (gitignored per ADR-001 decision 15)
date_authored: 2026-05-06
status: active
---

# HANDOFF: TASK-0027

## Metadata

- Task ID: TASK-0027 (matches PR-35 anticipated; first cycle executing ADR-006 Decision 2 Batch P1 process-templates batch + Decision 3 cadence relaxation; product-delivery pivot per Option Y owner-ratification 2026-05-06).
- Linked Issue: none
- Linked PR: PR-35 — URL TBD at PR-open (substituted at step-13 per PMN-001 (k) deferred-substitution discipline)
- Linked ADR(s): **ADR-006 (this cycle's substantive direction-decision authoring)**; ADR-001 D9 (admin-bypass posture); ADR-001 D11 (owner-invokes Codex per `@codex review`); ADR-001 D15 (`.claude/session-handoffs/` gitignored region); ADR-002 Decision 3 anticipation pattern (precedent for ADR-006 partial-supersession amendment); ADR-003 (partially superseded by ADR-006 at D2; D1 ship scope + D3 reservation extension preserved); ADR-004 (linked-pr-fix-up Action; counted in Batch P4 as 1-of-9 already shipped); ADR-005 (branch-convention canonicalization; precedent for partial-supersession-via-deliberate-divergence; branch convention Option B applied this cycle).
- Linked Feature Brief: none (ADR-tracked direction-decision cycle; no FEAT)
- Linked review-context file: docs/reviews/PR-35-codex-pre-commit.md
- Linked PMN(s): PMN-001 (k) (chore-fix-up substitution discipline; this cycle's `linked_pr` field substitution post-merge); PMN-002 (d) (code-fenced kickoff prompt convention applied at review-template body-section template authoring); PMN-007 HEAD canonical 12-field handoff frontmatter form (canonicalized in this cycle's handoff-template.md substantive content fill); PMN-008 §3.1 (k.1 positive self-instantiation framework; AGENTS.md/CLAUDE.md inline-mention drift catch at step-2 step-2 stop-and-show is k.1 evidence at MEDIUM salience); PMN-009 (i.5) Architect-spec-drift-catch discipline applied at Builder pre-flight (i.5) batch; PMN-010 §2 sub-shape 1 (forward-ref §-citation correctness against named-source-state — applied at Class A v-bump scope expansion adjudication) + §2 sub-shape 4 sub-class (spec §1.1 Honesty record vs body prescription form drift on ADR-003 §Status) + §2 sub-shape 6 (stub-vs-operational artifact-path distinction applied at templates/handoff-template.md + templates/review-template.md fill — both have operational counterparts).
- Owner role: Builder (Claude Opus 4.7, Claude Code, owner's local session)
- Previous role: Architect (Claude Opus 4.7, Claude.ai Project)
- Timestamp (UTC): cycle execution in progress
- Last synced commit SHA: `e71a4bd` (PR-34 chore-fix-up squash for TASK-0026 linked-PR substitution per PMN-001 (k); auto-fired by linked-pr-fix-up Action shipped at PR-21; verified at pre-flight 2026-05-06 against `git rev-parse origin/main` after `git fetch origin main`; local was behind 2 squashes before fast-forward).
- Branch: `feat/task-0027-product-delivery-pivot` (Option B canonical form per ADR-005; matches `^(feat|fix|chore|adr|shadow|spike)/task-[0-9]{4}-([a-z0-9]|[a-z0-9][a-z0-9.-]*[a-z0-9])$` regex).
- Status: active
- Direction: Architect → Builder (universal handoff schema, v2.14.1 §14.1 substrate)
- Framework version: AMAS v2.23 → v2.24 (Class A v-bump at this cycle per `core.md` §18.4 substantive-reading minor criterion)
- Recursive-self-instantiation salience: MEDIUM-HIGH (updated from step-2 MEDIUM framing at step-10-resolution per Architect §6 ratification) — ADR-006 IS the cadence-relaxation document AND multi-surface review pipeline empirically validated AT the same cycle (3 distinct surfaces caught Architect-spec-authoring-discovery drift independently this cycle: Builder pre-flight (i.5)(e) + Codex desktop pre-commit Finding 2 + TASK-0026-prior Codex post-PR Finding 2); cycle-close discipline applied with evidence-bar restraint per ADR-006 Decision 3 (lightweight canonical absorption recommended for MC-D 3-instance evidence base per cycle-close ledger Item 4 amendment).

## Objective

Six coupled substantive deliverables + 2 co-shipped artifacts in a single PR per single-PR-with-split-trigger discipline (TASK-0012 Part B precedent extended through TASK-0026):

1. **ADR-006 authoring** at `docs/adr/ADR-006-product-delivery-pivot-pr-plan-amendment.md` — substantive direction-decision establishing product-delivery cycle cadence + amending ADR-003 D2 PR plan (empirically-falsified PR-7-through-PR-19 forecast) + revised remaining-work scope (47 unfilled stubs across Batches P1-P8) + PMN-after-cycle cadence relaxation (Decision 3). Partial-supersession of ADR-003 D2 only; D1 ship scope (50 stubs filled) + D3 reservation extension pattern preserved.

2. **`templates/handoff-template.md` substantive content fill** — 4-line stub → canonical handoff template per PMN-007 HEAD canonical 12-field frontmatter form + body section template per TASK-0023+ lived-practice canonical structure + usage notes including MC-C `linked_pr` canonical-regex form discipline subsection (template IS the discipline reference per Option Y D3 cadence relaxation).

3. **`templates/review-template.md` substantive content fill** — 4-line stub → canonical review-context template per TASK-0021+ lived-practice canonical 1-field frontmatter form + body section template (pre-commit + post-PR variants) + Codex desktop pre-commit kickoff fenced code block + Codex desktop pre-commit output absorption section template.

4. **`core.md` §18.3 M-A7 amendment** — append-only sub-paragraph after original 4-instance numbered list documenting cumulative 13-instance enumeration `PR-9 + PR-10 + PR-11 + PR-13 + PR-15 + PR-17 + PR-19 + PR-21 + PR-25 + PR-27 + PR-29 + PR-31 + PR-33 = 13`. Original 4-instance empirical grounding paragraph preserved (load-bearing for the M-A7 promotion event itself).

5. **ADR-003 §Status field amendment** — partial-supersession declaration per ADR-005 precedent (single-line append after existing partial-supersession line; preserves D1 + D3 load-bearing decisions).

6. **README.md Edits P.A-P.D + AGENTS.md/CLAUDE.md inline-mention bump** — Edit P.A.1 README line 9 (both `v2.23` → `v2.24`); Edit P.A.2 AGENTS.md:9 (`v2.23` → `v2.24`); Edit P.A.3 CLAUDE.md:9 (`v2.23` → `v2.24`); Edit P.B + P.C Templates table 2 rows (`PR-12 (TASK-0012)` → `PR-35 (TASK-0027)` for handoff-template + review-template); Edit P.D Roadmap paragraph (Batch P1-P8 sequence per ADR-006 Decision 2; ADR-003 + ADR-006 cross-references; UPCDS adoption note preserved).

Co-shipped: TASK-0027 handoff (this file's body) + PR-35 Codex desktop pre-commit review-context.

## Last completed step

Step 9 — `core.md` §23.6.2 iterative-to-fixed-point self-review pass complete; standing by at step-10 pre-commit stop-and-show.

## Current state

**Summary**: 10 files modified/created on branch `feat/task-0027-product-delivery-pivot` based on `e71a4bd` (post-PR-34 main HEAD, fast-forwarded from local `374ee6a`). Working tree pre-stage; cumulative-diff-stats computed at step 9 self-review per (e.1) staged-tree convention.

**Files authored / modified by Builder**:
1. NEW `docs/adr/ADR-006-product-delivery-pivot-pr-plan-amendment.md` — substantive direction-decision per spec §4.1 (Status / Context / Decision (4) / Alternatives (5) / Consequences / Cross-references).
2. MODIFIED `templates/handoff-template.md` — 4-line stub → substantive content fill per spec §4.2.
3. MODIFIED `templates/review-template.md` — 4-line stub → substantive content fill per spec §4.3.
4. MODIFIED `core.md` §18.3 — append-only sub-paragraph per spec §4.4.
5. MODIFIED `docs/adr/ADR-003-full-package-pr-plan.md` §Status — single-line append per spec §4.5.
6. MODIFIED `README.md` — Edits P.A.1 + P.B + P.C + P.D per spec §4.6 + Architect §6 path-(a) scope expansion.
7. MODIFIED `AGENTS.md` line 9 — Edit P.A.2 per Architect §6 scope expansion.
8. MODIFIED `CLAUDE.md` line 9 — Edit P.A.3 per Architect §6 scope expansion.
9. NEW `docs/handoffs/TASK-0027-product-delivery-pivot.md` — this file.
10. NEW `docs/reviews/PR-35-codex-pre-commit.md` — co-shipped review-context per TASK-0021+ canonical form.

**Cumulative-diff-stats** (per `core.md` §23.6.1.1 (e.1) staged-tree convention; surfaced at step-10 stop-and-show post-stage).

## Decisions made

- **§0 owner-pre-step-2 adjudications** (locked pre-Builder execution per spec §0): Option Y product-delivery pivot ratified; 2-template kickoff scope = handoff-template + review-template; ADR-006 partial-supersession of ADR-003 D2 only (D1 + D3 preserved); M-A7 amendment append-only form; MC-C absorption venue = handoff-template Frontmatter conformance discipline subsection (template IS the discipline); MC-D + MC-E carry-forward (no PMN this cycle); README v-bump v2.23 → v2.24 minor per `core.md` §18.4.
- **Architect step-2 §6 path-(a) scope expansion**: Edit P.A scope expanded to 3 sites (README:9 + AGENTS:9 + CLAUDE:9) — pure-token-swap class. AGENTS.md/CLAUDE.md inline-mention drift caught at Builder pre-flight (i.5) batch (e); reclassified as Class A canonical-version-of-record (not Class B substrate). Class A v-bump definition refinement documented in cycle-close ledger (in-cycle adjudication; canonical promotion deferred per ADR-006 D3).
- **(k.1) positive self-instantiation salience MEDIUM**: discipline-being-authored (ADR-006 D3 evidence-bar cadence relaxation) caught its own spec-authoring-discovery gap at the cycle authoring it. Single-cycle observation; carry-forward monitoring per ADR-006 D3 (NOT PMN-promoted this cycle — would violate D3 self-instantiation if promoted on single-cycle evidence).

## Assumptions

- Repo-state at pre-flight: clean working tree on previous cycle's merged branch `feat/task-0026-...`; local main at `374ee6a` (PR-32) behind remote at `e71a4bd` (PR-34); fast-forward at step 3 succeeded.
- Branch protection per ADR-001 D9 admin-bypass posture (Posture 2 Rulesets); owner squash-merge bypass authorized at step-17.
- `gh` CLI authenticated with bryce-murphy/amas-framework repo scope.
- Codex desktop pre-commit Reviewer (GPT-5.5) operational per ADR-001 D11 owner-invokes convention; owner pastes kickoff prompt at step 11.
- linked-pr-fix-up Action shipped at PR-21 (per ADR-004) operational; canonical regex at `.github/scripts/linked-pr-fix-up.py:35` matches `linked_pr: PR-35 (Builder fills with squash SHA post-merge per PMN-001 (k))` (verified empirically at pre-flight via PowerShell match).

## §1. Cycle scope deliverables enumeration

Per spec §1: 6 substantive deliverables + 2 co-shipped artifacts. Cumulative-diff-stats anticipation per Architect §6 update: ~757-962 ins / ~12-17 del across 10 files.

## §2. Cycle gates

Per spec §2: step-2 stop-and-show (Builder pre-flight findings) + step-10 pre-commit stop-and-show (Builder step-9 self-review surface) + step-17 hand-back (Architect §24.3.1 five-point post-handback check). Severity routing per ADR-001 D11 (Blocking handback / Major path-(a)/(β) / Minor path-(b) default).

## §3. Step-by-step execution record

- **Step 1 (i.5) pre-flight batch**: complete — all 8 sub-shapes (a)-(h) verified clean; PR-XX = PR-35 reconciled; canonical regex MC-C empirical pre-application verified via PowerShell match.
- **Step 2 stop-and-show**: surfaced per spec §3.2 + §9; Architect ratified with §6 path-(a) Edit P.A scope expansion (AGENTS.md/CLAUDE.md inline-mention drift reclassified as Class A surface, not Class B substrate).
- **Step 3 branch creation**: `git checkout main && git pull origin main` (fast-forward `374ee6a..e71a4bd`); `git checkout -b feat/task-0027-product-delivery-pivot`.
- **Steps 4.1-4.6 authoring sequence**: complete per spec §4.1-§4.6 + Architect §6 P.A scope expansion.
- **Step 5 stub frontmatter updates**: applied at Steps 4.2 + 4.3 (`status: stub` → `status: filled`; `filled_by: per ADR-003` → `filled_by: PR-35 (TASK-0027)`).
- **Step 6 (j) all-instances grep sweep**: surfaced at step-10 stop-and-show per spec §3.4 step 6.
- **Step 7 handoff body authoring**: this file.
- **Step 8 review-context authoring**: PR-35 review-context co-shipped.
- **Step 9 §23.6.2 iterative-to-fixed-point self-review pass-1**: complete; convergence at iteration 1 (pure-token-swap class).
- **Step 10 pre-commit stop-and-show (initial)**: surfaced; Architect ratified gate proceeding to Codex desktop pre-commit invocation.
- **Step 11 Codex desktop pre-commit pass-1**: complete; verdict Major findings × 4 (no Blocking; no Minor); review absorbed verbatim into review-context per `core.md` §8.1.1.2.
- **Step 11.1 path-(a) resolutions R.1.1 / R.1.2 / R.2.1 / R.2.2 / R.3 / R.4**: complete; pure-token-swap class one-iteration convergence per `core.md` §8.1.1.3 bounded-continuation rule.
- **Step 11.2 §23.6.2 self-review pass-2**: complete; convergence at iteration 1; no same-class recurrence.
- **Step 11.3 step-10-resolution stop-and-show**: surfaced; Architect ratified resolution gate authorizing commit + push + PR-open per Architect §7 direction.
- **Step 12 commit**: in progress (composite spec §4.7 commit message + R.1-R.4 absorption appendix per Architect §7 direction).
- **Step 13 push branch + open PR-35**: complete; PR-35 opened at https://github.com/bryce-murphy/amas-framework/pull/35 with full template populated.
- **Step 14 Codex post-PR pass-1 (UTC 2026-05-07T00:57:20Z)**: complete; verdict Major findings × 1 (P2); substantive landing endpoint C; consistent with PMN-008 §5.8 (h.4) cross-cycle pattern.
- **Step 14.1 Architect step-13 ratification + Edit R.5 application**: complete per Architect step-13 §3 + §4 ratification; pure-token-swap class one-iteration convergence per `core.md` §8.1.1.3.
- **Step 14.2 §23.6.2 self-review pass-3**: complete; convergence at iteration 1; no same-class recurrence.
- **Step 14.3 fix-up commit + push**: in progress.
- **Steps 15-16 Codex post-PR pass-2 (hypothetical)**: settling-period rule per `core.md` §8.1.1.1 — wait 5-10 min post-fix-up-push for any pass-2 trigger.
- **Step 17 Architect §24.3.1 five-point post-handback check**: pending post-step-14 absorption convergence.

## §4. Substantive-content evidence per deliverable

Per spec §4.1 / §4.2 / §4.3 / §4.4 / §4.5 / §4.6 byte-exact prescriptions; Architect ratifications recorded inline in spec. PR-35 substituted for PR-XX at content authoring per Architect step-2 ratification.

- **ADR-006**: 4-decision substantive direction-decision; partial-supersession of ADR-003 D2 only; Batch P1-P8 sequence; PMN-after-cycle cadence relaxation per Decision 3 + evidence-bar discipline per Decision 3 sub-rules.
- **handoff-template.md**: 12-field PMN-007 HEAD canonical frontmatter documentation + body section template + MC-C Frontmatter conformance discipline subsection + usage notes + cross-references.
- **review-template.md**: 1-field canonical frontmatter + body sections (Codex desktop pre-commit variant primary, post-PR variant differential) + Codex kickoff fenced block per PMN-002 (d) reliable-copy convention + output absorption template + usage notes.
- **core.md §18.3 M-A7 amendment**: append-only sub-paragraph documenting cumulative 13-instance enumeration; original 4-instance empirical grounding paragraph preserved (load-bearing for M-A7 promotion event).
- **ADR-003 §Status amendment**: single-line append documenting D2 partial-supersession by ADR-006 (2026-05-06); D1 + D3 preservation note.
- **README.md Edits P.A-P.D + AGENTS/CLAUDE P.A.2/P.A.3**: Class A v2.23 → v2.24 across 3 sites (per Architect §6 expansion); Templates table 2-row update; Roadmap paragraph rewrite per ADR-006 D2 batch sequence.

## §5. Self-review record (step-9 §23.6.2 iteration log)

Per `core.md` §23.6.2 iterative-to-fixed-point: pass 1 covered §-citation correctness + cross-document consistency + frontmatter conformance + Class A scope (3 sites) + M-A7 enumeration + stub frontmatter transitions + (j) sweep results + cumulative-diff-stats per (e.1). Convergence anticipated at iteration 1-2 (pure-token-swap class for any drift). Findings surfaced at step-10 stop-and-show.

## §6. Pre-commit absorption (step-11 Codex desktop output absorption)

Codex desktop pre-commit pass-1 complete (UTC 2026-05-07T00:23:23Z): verdict Major findings × 4 (no Blocking; no Minor). Review verbatim recorded into [docs/reviews/PR-35-codex-pre-commit.md:148](docs/reviews/PR-35-codex-pre-commit.md) per `core.md` §8.1.1.2 verbatim-output convention. All 4 findings adjudicated path-(a) revise per ADR-001 D11 + `core.md` §8.1.1.3 cost-class refinement; pure-token-swap class × 4; one-iteration convergence per bounded-continuation rule. Resolution edits R.1.1 + R.1.2 (handoff-template `linked_pr` exemplar regex correctness) + R.2.1 + R.2.2 (ADR-006 ADR-004 framing additive vs subtractive) + R.3 (review-context Claim 10 PR-12 count `2` → `7`) + R.4 (review-context Claim 20 cumulative-diff-stats durable-claim refactor to step-10-stop-and-show-referenced empirical recording). §23.6.2 self-review pass-2 converged at iteration 1; no same-class recurrence. Step-10-resolution stop-and-show surfaced; Architect §7 ratified resolution gate authorizing commit + push + PR-open.

## §7. Commit + push + PR-open record

Pending — populated post-step-12 + step-13.

## §8. Post-PR Codex review state (populated step-13+)

Codex post-PR pass-1 complete (UTC 2026-05-07T00:57:20Z): verdict Major findings × 1 (P2 priority badge); substantive landing endpoint C per `core.md` §8.1.1.1 (line-level review-comment on `docs/reviews/PR-35-codex-pre-commit.md:51`); consistent with PMN-008 §5.8 (h.4) cross-cycle empirical pattern (TASK-0027 = data point 8). Three-endpoint poll evidence + verbatim findings recorded in [docs/reviews/PR-35-codex-pre-commit.md](docs/reviews/PR-35-codex-pre-commit.md) Codex post-PR pass-1 absorption section per `core.md` §8.1.1.2. Finding adjudicated path-(a) revise (pure-token-swap class; (h.2) verification-command operational correctness sub-shape per PMN-009 canonical sub-shape framework); Architect step-13 §3 ratified Edit R.5 prescription (Builder Option (i) `grep -F` fixed-string match form); Resolution applied: Edit R.5 (review-context Claim 5 fourth bullet `grep -nE` invalid ERE escaping → `grep -F` fixed-string match; verified empirically returns 3 lines). §23.6.2 self-review pass-2 iteration-1 converged; no same-class recurrence. (h.2) intra-cycle recurrence count = 3 (within bounded-continuation tolerance edge; 4th-instance break-out condition per `core.md` §8.1.1.3). Step-13 absorption fix-up commit + push pending; step-17 hand-back to Architect anticipated post-fix-up if pass-2 stable empty (settling-period rule per §8.1.1.1).

## §9. Sign-off (step-17 §24.3.1 five-point check; Architect populates)

Pending — populated by Architect at step-17 hand-back per `core.md` §24.3.1 five-point post-handback check.

## §10. Cycle-close ledger

In-cycle observations + carry-forward monitoring + new PMN candidates. Per ADR-006 Decision 3 evidence-bar discipline, single-cycle observations absorb to lightweight cycle-close ledger entries (NOT PMN-promoted unless 3+ cross-cycle confirmations + canonicalization-cost favorable).

- **Item 1 — (k.1) positive self-instantiation at MEDIUM-HIGH salience** (updated from MEDIUM at step-2 §6 framing post-step-10-resolution per Architect §6 ratification): three distinct surfaces independently caught Architect-spec-authoring-discovery completeness drift this cycle — Builder pre-flight (i.5)(e) caught AGENTS.md/CLAUDE.md inline-mention drift; Codex desktop pre-commit Finding 2 caught ADR-006 ADR-004 framing additive-vs-subtractive drift; (TASK-0026 prior cycle) Codex post-PR Finding 2 caught Migration-mapping-table completeness gap. Multi-surface review pipeline empirically load-bearing AT the cycle authoring ADR-006 D3 cadence relaxation, which depends on multi-surface pipeline as the primary defect-prevention mechanism replacing per-cycle PMN authoring. Discipline-being-shipped successfully validates itself: ADR-006 D3 says "lightweight absorption preferred + multi-surface review pipeline catches drift"; this cycle's execution demonstrates both empirically. Salience MEDIUM-HIGH. Single-cycle observation amplified by intra-cycle recurrence pattern; carry-forward monitoring per ADR-006 D3 evidence-bar discipline. NOT PMN-promoted this cycle (would violate ADR-006 D3 self-instantiation if promoted on single-cycle evidence; lightweight canonical absorption recommended per Item 4 amendment).

- **Item 2 — Class A v-bump definition refinement (in-cycle adjudication)**: per Architect step-2 §6 ratification, Class A canonical-version-of-record = README.md line 9 (primary canonical-version anchor) + any inline current-version mentions in operating-instruction surfaces that explicitly cite the README version (post-TASK-0026 migration: AGENTS.md:9 + CLAUDE.md:9). Class B = substrate references (`v2.14.1` preserved verbatim). Class C = historical narrative references in PMNs / handoffs / review-contexts (preserved verbatim). Refinement documented in this ledger entry; canonical promotion to discipline anchor (e.g., `core.md` §18.4 substantive-reading paragraph or new §-section) deferred per ADR-006 D3 evidence-bar discipline.

- **Item 3 — Structural reframe candidate (deferred)**: future-cycle adjudication candidate — replace `current canonical materialization at vX.Y — see README` form with `current canonical materialization — see README` form (eliminates inline version mention; collapses Class A v-bump scope back to README-only). Not in TASK-0027 scope per §0 owner-adjudication preservation; defer to subsequent cycle owner adjudication or fold into next substantive-content cycle. Trade-off: adopters reading AGENTS.md/CLAUDE.md as entry-point lose at-a-glance version visibility vs eliminate recurring per-cycle staleness defect class. Owner discretion.

- **Item 4 — MC-D 3-instance evidence base + lightweight canonical absorption recommendation** (updated post-step-10-resolution per Architect §5 ratification): Architect-spec-authoring-discovery completeness gap evidence base materially strengthened to 3 instances across 2 cycles via multi-surface confirmation:
  - **Instance 1** (TASK-0026 Codex post-PR Finding 2): Migration-mapping-table completeness gap. Cycle-close Item 13 of TASK-0026 handoff.
  - **Instance 2** (TASK-0027 Builder pre-flight (i.5)(e)): AGENTS.md/CLAUDE.md inline-mention drift; Class B → Class A reclassification absorbed via Edit P.A scope expansion.
  - **Instance 3** (TASK-0027 Codex desktop pre-commit Finding 2): ADR-006 ADR-004 framing additive vs subtractive drift; absorbed via Edit R.2.1 + R.2.2 path-(a) resolutions.

  **Cost-benefit assessment per ADR-006 D3 evidence-bar discipline**: 3-instance confirmation threshold reached. Canonicalization cost: PMN-011 (~200 source lines) vs lightweight 2-3 line addition to `core.md` §23.6.3 sub-shape A enumeration codifying canonical-impact-surface-completeness check at spec-authoring time. Lightweight absorption wins on cost-benefit: codifies the discipline at the existing canonical-anchor surface; PMN-011 would document the same discipline at greater length without proportional benefit.

  **Architect direction for TASK-0028+**: lightweight canonical absorption recommended via small `core.md` §23.6.3 sub-shape A amendment (could ride along with next M-A7 amendment cycle as bundled chore). NOT PMN-011 this cycle nor next per ADR-006 D3 framework. Owner adjudicates at TASK-0028+ Phase 1 scoping.

- **Item 5 — MC-C absorption empirical confirmation**: `linked_pr` canonical-regex form discipline absorbed into handoff-template.md Frontmatter conformance discipline subsection per spec §0 + §4.2. Builder pre-empted MC-C empirically at pre-flight (i.5) batch (a) via PowerShell regex match — first cycle where MC-C is Builder-pre-applied (vs surfaced at Codex post-PR like TASK-0026). Discipline IS the template per Option Y D3 cadence relaxation. Cycle-close evidence FOR template-as-discipline-reference operating model.

- **Item 6 — M-A7 14th-instance cycle-close ledger entry**: PR-35 = 14th instance candidate per established M-A7 inclusion criterion (substantive-cycle PR; not defect-fix patch or chore-fix-up). Architect adjudicates at step-17 sign-off whether to include in next cycle's enumeration amendment. Anticipated next-cycle (TASK-0028+) M-A7 amendment: `... + PR-33 + PR-35 = 14`.

- **Item 7 — ADR-003 §Status descriptive-form drift (Class C, non-blocking)**: spec §1.1 Honesty record described §Status as single combined `/`-separated form; empirical state is two paragraphs. Prescription anchor in spec §4.5 actionable verbatim against empirical line 7. Class: PMN-010 sub-shape 4 (spec-context-vs-body-citation conflation) sub-class — descriptive form vs prescription form. Single-cycle observation; carry-forward monitoring per ADR-006 D3.

- **Item 8 — Cumulative-diff-stats anticipation update**: spec §1 anticipated ~755-960 ins / ~10-15 del across 8 files. Architect §6 path-(a) expansion adjusted to ~757-962 ins / ~12-17 del across 10 files (AGENTS.md + CLAUDE.md added). Empirical landed pre-Codex 730 ins (-3.6% under low bound; within MC-A tolerance); post-Codex-pre-commit-absorption 786 ins (+3.8% above low bound; within range non-blocking); post-Codex-post-PR-Edit-R.5 fix-up: surfaced at step-13-absorption stop-and-show.

- **Item 9 — (h.2) intra-cycle recurrence empirical observation** (added at Codex post-PR pass-1 absorption per Architect step-13 §4 ratification): 3-instance (h.2) verification-command operational correctness cluster within TASK-0027 cycle alone — Codex pre-commit Finding 1 (R.1.1 + R.1.2 handoff-template `linked_pr` exemplar) + Codex pre-commit Finding 3 (R.3 review-context Claim 10 PR-12 count) + Codex post-PR pass-1 (R.5 review-context Claim 5 fourth bullet ERE escaping). (h.2) is already canonical at PMN-009 sub-shape framework; intra-cycle recurrence is empirical confirmation of existing canonical, not new defect class. Builder-side authoring discipline observation: verification-claim authoring against template-content-with-embedded-regex-patterns surfaces (h.2) at higher intra-cycle rate when templates with regex content are the authoring substrate. Each instance individually under bounded-continuation rule (pure-token-swap one-iteration convergence × 3); no cascade. Three-instance count is at bounded-continuation tolerance edge per `core.md` §8.1.1.3; 4th-instance break-out condition would warrant Architect-side step-back to assess whether template-content authoring discipline needs refinement before Batch P1 continuation. Single-cycle observation; carry-forward for monitoring at future template-content cycles (Batch P1 continuing TASK-0028+). Empirically strengthens (k.1) MEDIUM-HIGH framing — multi-surface review pipeline catches (h.2) drift at distinct surfaces, individually one-iteration-resolved; no PMN-promotion needed for already-canonical sub-shape.

## §11. Session log archive

<Per AMAS v2.14.1 §13.1 (forthcoming at Part C+) most-recent-session storage rule: most recent session in PR body; prior sessions migrate here.>

### Architect session — Claude Opus 4.7 / Claude.ai Project — 2026-05-06

Authored TASK-0027-spec.md (gitignored per ADR-001 D15) per `core.md` §23.6.3 sub-shape A reference-verification batch + §23.6.2 iterative-to-fixed-point self-review. Spec scope: ADR-006 substantive direction-decision authoring + handoff-template.md + review-template.md substantive content fill + core.md §18.3 M-A7 amendment + ADR-003 §Status amendment + README v2.23 → v2.24 Class A v-bump. Owner pre-step-2 adjudications locked: Option Y ratified; 2-template kickoff scope; ADR-006 partial-supersession of ADR-003 D2 only; M-A7 append-only form; MC-C absorption via handoff-template; MC-D + MC-E carry-forward; README v-bump v2.23 → v2.24 minor per §18.4.

### Builder session — Claude Opus 4.7 / Claude Code — 2026-05-06

Pre-flight (i.5) batch executed per spec §3.1 (a)-(h); all 8 sub-shapes verified clean. PR-XX = PR-35 reconciled. MC-C empirical pre-application via PowerShell regex match. Class A/B/C version-marker survey surfaced AGENTS.md/CLAUDE.md inline-mention drift at (e) — Architect step-2 §6 ratified path-(a) scope expansion to include 3 Class A sites. Branch creation: fast-forward main + new branch `feat/task-0027-product-delivery-pivot`. Authoring sequence steps 4.1-4.6 + step 7 (this handoff) + step 8 (review-context). Self-review pass 1 at step 9. Standing by at step-10 pre-commit stop-and-show.
