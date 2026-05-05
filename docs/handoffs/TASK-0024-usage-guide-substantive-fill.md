---
task_id: TASK-0024
title: usage-guide.md substantive content fill (v2.14.1 substrate restructured into v3 split-package form + framework evolution since v2.14.1)
pr: PR-29
branch: feat/task-0024-usage-guide-substantive-fill
linked_predecessor: TASK-0023 (PR-27 squash 6bd66c2; PMN-009 §5 absorption + §23.6.3 + §24.3 enumeration update + Class A v2.19→v2.20)
linked_successor: TBD
linked_pr: PR-29 (squash SHA TBD at PR-open; substituted post-merge per PMN-001 (k))
framework_version_dogfooded: AMAS v2.20
production_target: AMAS v3.0
spec_source: .claude/session-handoffs/TASK-0024-spec.md (gitignored per ADR-001 decision 15)
date_authored: 2026-05-05
status: active
---

# HANDOFF: TASK-0024

## Metadata

- Task ID: TASK-0024 (matches PR-29 anticipated; first non-self-instantiating canonical-application of §23.6.3 reference-verification discipline shipped at TASK-0023; Path B `(forthcoming at Part C+)` qualifier convention introduced this cycle for forward-referenced core.md §-citations)
- Linked Issue: none
- Linked PR: PR-29 — URL TBD at PR-open (substituted at step-13 per PMN-001 (k) deferred-substitution discipline)
- Linked ADR(s): ADR-001 decision 11 (owner-invokes Codex); ADR-001 decision 15 (.claude/session-handoffs/ gitignored region); ADR-003 (decision 2 canonical sequencing — usage-guide.md fill at this cycle per ADR-003 D2 plan; decision 3 contingency-slot ledger reconciliation deferred per cycle-close ledger Item 1); ADR-004 (Actions-batch insertion precedent, not amended this cycle)
- Linked PMN(s): PMN-002/PMN-003 (Reviewer-output absorption refinements); PMN-004 §5 (review-discipline baseline); PMN-005 sub-rule (e.1) (cumulative-diff-stats re-derivation); PMN-006 (g)/(h)/(i) sweep set; PMN-007 §2.4 (cost-class refinement) + HEAD canonical 12-field handoff frontmatter; PMN-008 §3.2 (five-surface review pipeline) + §4.2 (i.5) convention-inference; PMN-009 / core.md §23.6.3 (reference-verification before spec authoring — first non-self-instantiating canonical-application this cycle)
- Owner role: Builder (Claude Opus 4.7, Claude Code, owner's local session)
- Previous role: Architect (Claude Opus 4.7, Claude.ai Project)
- Timestamp (UTC): 12:30 (approximate; cycle execution in progress)
- Last synced commit SHA: `9365b4b` (PR-28 chore-fix-up squash for TASK-0023 linked-PR substitution per PMN-001 (k); auto-fired by linked-pr-fix-up Action shipped at PR-21; verified at pre-flight 2026-05-05 against `git rev-parse origin/main`).
- Branch: `feat/task-0024-usage-guide-substantive-fill` (`feat/` prefix verified at pre-flight (i.5) batch — TASK-0019/TASK-0020/TASK-0021/TASK-0023 substantive-cycle priors all use `feat/<task-####-slug>`; owner ratified at step-1 stop-and-show).
- Status: active

## Objective

Three coupled deliverables:

1. **usage-guide.md substantive content fill** — scaffold-stub → substantive per spec §4 content prescription. v3 §0–§13 structure parallel to v2.14.1 substrate; substantive-content preserved with v3 framing adaptation and framework-evolution incorporation. Materialized at 388 source lines (below pre-cycle estimate of 600-700; no defect, surfaced at step-10 stop-and-show for awareness).

2. **README.md updates** — per-PR-row update at "Canonical law" table for usage-guide.md `filled_by` attribution (forecast `PR-11 (TASK-0011)` → actual `PR-29 (TASK-0024)`) per ADR-003 §Consequences distributed-update discipline; Class A canonical-version-of-record bump v2.20 → v2.21 at line 9 per §18.4 substantive-reading minor criterion.

3. **stub frontmatter update** — usage-guide.md frontmatter `status: stub` → `status: drafted`; `filled_by: per ADR-003` → `filled_by: PR-29 (TASK-0024)` per ADR-003 §Consequences per-PR-row update discipline (subsumed by deliverable 1; same file).

Co-shipped: TASK-0024 handoff (this file's body, Builder-filled at step-9 self-review + step-10 pre-commit + step-17 hand-back) + PR-29 Codex pre-commit review-context.

Cycle scope is the largest single-document substantive-content cycle in project history. No PMN authoring this cycle (PMN-010 deferred to TASK-0025+ per Architect Phase 1 scoping at TASK-0023 cycle close; one-artifact-class-per-PR convention preserved).

## Last completed step

Architect Phase 1 scoping completed (prior session, 2026-05-05):

1. v2.14.1 substrate read in full (uploaded to Architect context, 441 lines, §0–§13 structure) before authoring per §23.6.3 standing applied pre-emptively at this cycle.
2. v3 framing adaptation drafted per transition plan v0.2 Decision A (restructure-only at v3.0; substantive guidance preserved from v2.14.1; structural reorganization adapts to v3 split-package framing).
3. v3 expansion absorbing framework evolution since v2.14.1: PMN-002/003/004/005/006/007/008/009 + ADR-003/004 absorbed per spec §1 enumeration.
4. v3 expansion adding new content: three-tier solo-operator framing (Decision E + R-12); converging-lines-of-evidence multi-surface review pipeline framing (R-10); forward-references to project-type / documentation-MCP / amas-vs-other / regulated-tier appendices.
5. v3 reduction dropping v2.14.1 §11.3–§11.6.3 version-specific changelog and §10.22–§10.27 v2.12–v2.14 patch-era patterns.
6. M-A7 instance count: PR-29 = 11th empirical instance per `PR-9 + PR-10 + PR-11 + PR-13 + PR-15 + PR-17 + PR-19 + PR-21 + PR-25 + PR-27 + PR-29 = 11`.
7. Spec §1.1 honesty record per §23.6.3: substrate read in full + §-references claimed verified against current core.md / github-reference.md state + line-number / structural-element references deferred to Builder pre-flight (i.5) batch + externally-determined-at-consumption values (PR-29; squash SHA TBD) marked for Builder pre-flight verification per sub-shape E provisional handling.

Builder pre-flight + step-1 stop-and-show completed (this session, 2026-05-05):

8. Pre-flight clean; HEAD at `9365b4b` (PR-28 chore-fix-up squash) confirmed; PR-28 merge state owner-merged (auto-fired by linked-pr-fix-up Action). Working tree clean.
9. (i.5) batch surfaced 1 MAJOR finding + 6 routine items at step-1 stop-and-show:
   - (i.5)(c) **MAJOR**: 12 forward-referenced core.md §-citations in spec §4 content prescription (§2.2.2, §2.3.4, §2.3.6, §2.3.7, §3.1, §3.4.1, §3.4.2, §5.4, §8.2, §8.3, §10.5, §17.5) do not resolve in current core.md (status: partial; only §8/§17/§18/§23/§24 materialized to date). Architect adjudication: Path B with refined qualifier `(forthcoming at Part C+)` applied at every occurrence; path-(a) in-cycle correction. Owner approved.
   - (i.5)(a)/(b)/(d): handoff frontmatter shape (12-field PMN-007 HEAD canonical), review-context shape, github-reference.md §-citations (§2.2 + §6.2) all clean.
   - (i.5)(e)/(f): README line 9 = v2.20 × 2; "Canonical law" table row 42 = `PR-11 (TASK-0011)` forecast text; Class A v-bump scope = README line 9 only.
   - (i.5)(g)/(h)/(i): all forward-referenced files (prompts/{greenfield,retrofit,upgrade}.md, appendices/project-types/{5 files}, appendices/{documentation-mcp-options,amas-vs-other-frameworks,regulated-tier-extension}.md) exist as scaffold-stubs.
   - PR-28 review-context absence: per chore-fix-up convention (PR-22/24/26 priors); not defect.
10. **(i.5)(c) MAJOR finding classified as 14th cumulative-empirical-record confirmation** of §23.6.3 / PMN-009 / TASK-0023 self-instantiation pattern (13 → 14). Volume of single-cycle catch (12 distinct §-citations across ~25-35 occurrence-sites) is itself notable. Carry to cycle-close ledger as primary substantive evidence for PMN-010 authoring at TASK-0025+.

## Current state

**Summary**: 4 files staged (2 modified + 2 added): usage-guide.md substantive content fill + README.md Class A v-bump + table-row update + TASK-0024 handoff (this file) + PR-29 review-context. Path B `(forthcoming at Part C+)` qualifier convention introduced and applied across 27 instance-occurrences (on 20 distinct lines) covering 9 distinct forward-referenced core.md §-sections actually cited in §4 body content; step-1 finding's 12-section enumeration refined at step-9 self-review (3 of 12 — §2.3.6, §3.4.1, §3.4.2 — were spec §7 anticipated but not landed in §4 body; over-anticipation, not defect).

**Files authored / modified by Builder**:

(Builder fills at step-10 pre-commit stop-and-show — landed exact counts post-staging, per (e.1) sub-rule staged-tree convention.)

1. MODIFIED `usage-guide.md` — scaffold-stub (9 lines) → substantive content fill (388 lines). Frontmatter `status: stub` → `drafted`; `filled_by: per ADR-003` → `filled_by: PR-29 (TASK-0024)`. Body fully replaced with §0–§13 structure (14 top-level §-sections) per spec §4 verbatim materialization. Path B qualifier `(forthcoming at Part C+)` applied at 27 instance-occurrences covering 9 distinct forward-referenced core.md §-sections. Numstat: 382/3.

2. MODIFIED `README.md` — Class A canonical-version-of-record bump line 9 (`v2.20` × 2 → `v2.21` × 2). "Canonical law" table row 42 `Filled by` cell text `PR-11 (TASK-0011)` → `PR-29 (TASK-0024)`. Scope: 2-line modification. Numstat: 2/2.

3. NEW `docs/handoffs/TASK-0024-usage-guide-substantive-fill.md` — this handoff. Numstat: TBD (final landed at step-12 commit; see Cumulative diff stats below).

4. NEW `docs/reviews/PR-29-codex-pre-commit.md` — Codex pre-commit review-context with claim list + Codex output absorption section. Numstat: TBD (final landed at step-12 commit; see Cumulative diff stats below).

**Cumulative diff stats** (per (e.1) sub-rule staged-tree convention per TASK-0023 cycle-close N4 observation; final landed values committed to git ledger at step-12; values below reflect step-11 Codex absorption iteration; Builder re-derives at step-12 final pre-commit if any post-step-11 fix-ups land):

- Step-9 self-review iteration: `4 files changed, 661 insertions(+), 5 deletions(-)` (numstat: README 2/2 + handoff 171/0 + review-context 106/0 + usage-guide 382/3).
- Step-11 Codex absorption iteration delta: handoff 171 → 195 (+24 lines: cycle-close-ledger entries N1-N11 + Validation run rewrite + Risks N16-confirmation update + N4/N11 meta-(i.5) refinement post-Architect verification-question); review-context 106 → 181 (+75 lines: Codex output absorption section). Step-16 fix-up commit `7cb557d` extended handoff 195 → 200 (+5 lines: N12-N16 cycle-close-ledger); step-16 re-iteration extends handoff 200 → 201 (+1 line: N17 phantom-SHA observation). Final landed at step-16-bis: `4 files changed, 766 insertions(+), 5 deletions(-)` (numstat: README 2/2 + handoff 201/0 + review-context 181/0 + usage-guide 382/3; sum-stability check 2+201+181+382=766 ✓; deletions 2+0+0+3=5 ✓).
- Counts re-derived at each iteration; no `~`-prefixed approximate counts. Definitive values committed to git ledger at step-12 commit.

## Decisions made

**Architect Phase 1 scoping (TASK-0023 cycle close + this cycle's spec authoring)**:

- **Cycle scope**: usage-guide.md substantive content fill as single-document large-cycle. PMN-010 deferred to TASK-0025+ per one-artifact-class-per-PR convention (Q2 split decision).
- **v3 framing**: restructure-only per transition plan v0.2 Decision A; substantive guidance preserved from v2.14.1 substrate; structural reorganization adapts to v3 split-package framing.
- **Three-tier solo-operator framing**: integrated into v3 expansion per Decision E + research finding R-12.
- **Multi-surface review pipeline framing**: "converging lines of evidence" per research finding R-10.
- **Forward-reference convention**: `(forthcoming at TASK-####+)` for files; Path B `(forthcoming at Part C+)` for core.md §-citations not yet materialized (introduced this cycle per Architect adjudication at step-1 stop-and-show).
- **v3 reduction**: drop v2.14.1 §11.3–§11.6.3 version-specific changelog + §10.22–§10.27 v2.12–v2.14 patch-era patterns.

**Builder in-cycle decisions (this cycle's step-1 stop-and-show + execution)**:

- **(i.5)(c) MAJOR finding adjudication**: Path B refined qualifier form `(forthcoming at Part C+)` adopted (refinement from Architect's initial recommendation `(forthcoming at core.md Part C+)` — redundant `core.md` dropped since citation's leading `core.md §X.Y` already names the document); semantically equivalent, reads cleaner; pure-token-swap class per §8.1.1.3.
- **Qualifier-application scope**: every-occurrence application across all 20 forward-referenced §-citation sites covering 12 distinct sections, symmetric to §0 `(forthcoming at TASK-####+)` qualifier convention for forward-referenced files.
- **Branch type prefix**: `feat/` confirmed per substantive-content-cycle convention; matches TASK-0019/0020/0021/0023 priors.
- **Class A v-bump scope**: README.md line 9 only (2 instances); v2.20 → v2.21 minor per §18.4 substantive-reading minor criterion (substantive content addition: 388 lines + canonical-law trio third document materialized).
- **Spec §1.1 honesty record**: stands as authored — pre-flight catch documented at cycle-close (this handoff + future PMN-010 evidence) per Architect direction; not by retroactive spec edit; matches §23.6 self-review fixed-point handling.

## Assumptions

- core.md §-citations to forward-referenced (i.e., not yet materialized) sections will materialize in future Part C+ cycles per ADR-003 D2 plan; Path B qualifier becomes drop-target at materialization time (mechanical removal as part of materialization-cycle's already-implicit cross-ref update cost).
- Reader of v3.0-shipped usage-guide.md will eventually have access to full core.md when v3 ship completes; in the meantime, Path B qualifier signals partial-canonical state honestly.
- §-numbering for forward-referenced core.md sections mirrors v2.14.1 substrate §-numbering (per Decision A restructure-only framing); future Part C+ materialization preserves §-numbers.
- 388-source-line materialized usage-guide is below pre-cycle estimate (600-700) but matches §4 prescription verbatim — variance is in pre-cycle estimation, not materialization fidelity.
- Codex desktop pre-commit anticipated to surface 3-7 findings per substantive-content-cycle priors (TASK-0010/TASK-0012/TASK-0017); pure-token-swap class anticipated for most; path-(a) routing per §8.1.1.3 cost-class refinement.
- (w) fourth data point may surface at PR-29 emission (autonomous post-PR Codex emission before owner trigger); contributes to PMN-010 evidence base if observed.

## Risks

- **Risk: cycle scope is largest single-document in project history** — mitigated: 388 lines materialized verbatim from spec prescription; Builder-side authoring discretion zero.
- **Risk: §-citation correctness across large content surface** — Path B qualifier coverage verified at step-9 (j) all-instances grep sweep; 0 unqualified forward-ref citations residuals.
- **Risk: forward-reference correctness for forthcoming files** — verified at pre-flight (i.5)(g)/(h)/(i); all forward-referenced files exist as scaffold-stubs; anticipation-language qualifiers match TASK-numbering convention.
- **Risk: Codex pre-commit pass surfaces findings on Path B qualifier convention itself** — novel convention introduced this cycle; Reviewer may flag as defect (path-(a) in-cycle correction or path-(β) record-and-proceed adjudication via Architect at step-11).
- **Risk: §23.6.3 self-application catches new in-cycle (i.5) instances at step-9 self-review or Codex pre-commit** — likely per project's empirical pattern (large-content-cycle = surface area for drift catches); carry to cycle-close ledger; future PMN absorbs.
- **Risk: 14th confirmation classification on Path B catch may need refinement** — surface count advanced 13 → 14 → 15 → 16 across this cycle (step-1 + step-9 + Codex pre-commit Finding 1); pattern strength claim deferred to PMN-010 authoring at TASK-0025+.
- **No PMN authoring this cycle** — PMN-010 deferred per Q2 split decision; primary substantive evidence accumulates here for next-cycle authoring.

## Blocking questions

None at handoff-authoring time. Step-1 stop-and-show resolved all surfaced items via Architect adjudication + owner approval.

## Validation run

Landed at step-9 self-review + step-10 pre-commit + step-11 Codex pre-commit absorption:

- `wc -l usage-guide.md` returns `388` source lines.
- `grep -cE "^## §" usage-guide.md` returns `14` (14 top-level §-sections per spec §7 Claim 1).
- `head -5 usage-guide.md` shows frontmatter `framework_version: 3.0.0`, `status: drafted`, `filled_by: PR-29 (TASK-0024)`.
- `grep -oE "forthcoming at Part C\+" usage-guide.md | wc -l` returns `27` qualifier instances on 20 distinct lines covering 9 actually-cited forward-referenced core.md §-sections (§2.2.2, §2.3.4, §2.3.7, §3.1, §5.4, §8.2, §8.3, §10.5, §17.5).
- `sed -n '9p' README.md` returns post-bump line `v2.21` × 2; `grep -nE "\bv2\.20\b" README.md` returns 0 lines.
- `grep -nE "PR-29.*TASK-0024" README.md` returns line 42 (`Canonical law` table row for usage-guide.md). `grep -E "PR-11.*TASK-0011" README.md` returns 0 lines (forecast text replaced).
- `git diff --shortstat origin/main` returns `4 files changed, 766 insertions(+), 5 deletions(-)` (final landed post step-16 re-iteration; per (e.1) sub-rule re-derived from current branch state, not propagated from prior iterations).
- (j) all-instances grep sweep landed counts: usage-guide=`157`, handoff=`67`, review-context=`60` (canonical spec §3 step 9 regex; Codex regex variant reported 1-line systematic delta on handoff/review-context — see cycle-close ledger Item N6).
- Codex desktop pre-commit: 2 Major + 1 Minor findings; all adjudicated (see review-context Codex absorption section + cycle-close ledger items N7-N9).

## §8. Post-PR Codex review state

(Builder fills at step-15 three-endpoint poll + step-17 hand-back.)

- Endpoint 1: `gh pr view 29 --json reviews` — TBD.
- Endpoint 2: `gh api repos/bryce-murphy/amas-framework/issues/29/comments` — TBD.
- Endpoint 3: `gh api repos/bryce-murphy/amas-framework/pulls/29/comments` — TBD.
- Settling-period state: TBD.
- (w) data point classification: TBD (autonomous emission before owner trigger = data point 4 toward PMN-010; triggered emission = (w) carries forward at 3 confirmations).

## §9. Sign-off

(Architect fills post-handback per §24.3.1 five-point check.)

- Three-endpoint poll reconciliation: TBD.
- Branch tip-SHA verification: TBD.
- File content audit against prescription: TBD.
- Phantom-action audit: TBD.
- Comment-content claim verification (per §8.1.1.2): TBD.

## §10. Cycle-close ledger

Carry-forward state from TASK-0023 + new monitoring observations from this cycle:

**Carried forward from TASK-0023 (resurfaces at next cycle authoring time)**:
- **Item 1**: ADR-003 D3 contingency-slot ledger reconciliation — still tabled; needs structural surface. Carry; no TASK-0024 action.
- **Item 6 (w)**: at 3 cross-cycle data points; threshold met; PMN-010 deferred to TASK-0025+ per Architect Phase 1 scoping. Carry as primary substantive content for next-cycle PMN authoring. Possible 4th data point from PR-29 emission monitoring at step-15 — see §8 Post-PR Codex review state.
- **Items 7, 11**: stays at monitoring (carry).
- **Items 13, 15, 16**: deferred operational items (carry).
- **§23.6.1 sweep-set canonical enumeration gap** — sweep-set categories (g)/(h)/(i) referenced at §8.1.1.3 line ~133 as "§23.6.1 sweep set categories" but enumerated only at PMN-006 §3+§7. Pre-existing from PR-13 era; carry.
- **README §Package layout 16-file undercount** vs actual 19 files in `templates/`; **README ADR-003 D2 plan stale** relative to actual PR sequence — TASK-0022 monitoring observations; not in TASK-0024 scope.

**New monitoring observations from TASK-0024**:

- **N1**: TASK-0024 in-cycle (i.5) catches: 2 instances (1 MAJOR at step-1 stop-and-show + 1 step-9 self-review refinement); cumulative empirical pattern advances **13 → 16 confirmations** (+3 this cycle: step-1 + step-9 + Codex pre-commit Finding 1).
- **N2**: First non-self-instantiating canonical-application of §23.6.3 reference-verification discipline (TASK-0023 was self-instantiating). Discipline operating effectively: pre-flight (i.5)(c) catch + step-9 self-review refinement + Codex pre-commit catch on distinct drift class (cross-doc-shape-drift, not forward-ref-§-citation).
- **N3**: Path B `(forthcoming at Part C+)` qualifier convention introduced this cycle (Architect-adjudicated path-(a) in-cycle correction at step-1 stop-and-show; refined form per Builder execution-mechanics note). 27 qualifier instances on 20 lines × 9 distinct sections. Convention symmetric to §0 `(forthcoming at TASK-####+)` for forward-referenced files. Future Part C+ materialization cycles drop qualifier as part of materialization-cycle's already-implicit cross-ref update cost.
- **N4**: Single-cycle catch volume: 12 anticipated forward-ref §-sections (step-1 finding) refined to 9 actually-cited sections (step-9 (j) sweep refinement). Largest single-cycle (i.5) finding-volume in project history. Source of 12→9 delta: §2.3.6 + §3.4.1 + §3.4.2 were spec-context references (§2.3.6 "implied by spec §1"; §3.4.1/§3.4.2 "anticipated per spec §7 claim 2") not §4 prescription body materialization citations; Builder step-1 finding conservatively unioned anticipated + body-cited; canonical step-9 (j) sweep correctly narrowed to actually-cited. Strengthens PMN-010 evidence base.
- **N5**: Spec wording-line estimate (600-700) vs actual landed (388): 45% under-estimate. Spec §10 cycle-scope Risk under-anticipated; not a defect — content matches §4 prescription verbatim. Future-cycle estimation discipline observation.
- **N6**: 1-line systematic delta between canonical (j) sweep regex (Builder; spec §3 step 9) and Codex regex variant on handoff (67 vs 68) and review-context (60 vs 61). Pattern is systematic, not random — likely regex-clause difference (e.g., extra anchor or unanchored boundary). Future-cycle PMN-eligible if pattern recurs across multiple cycles.
- **N7**: Codex pre-commit Finding 1 — branch convention drift in usage-guide.md §3.3 + §5.3 — adjudicated Path α (record-and-proceed). PMN-008 watch carry-forward: status remains active. AGENTS.md/CLAUDE.md → v3 migration cycle is the natural ADR-warranted surface for branch-shape direction-decision. Substantive direction-observation (out of scope this cycle, surfaced for future-ADR awareness): lived practice `<type>/task-####-<kebab-slug>` threads TASK-#### into branch names reinforcing AMAS's TASK-#### centrality; v3 trio's `<type>/<id>-<summary>` form may be inadvertent generic-git-flow drift from TASK-0017 github-reference.md authoring. Future ADR cycle's likely conclusion (medium-high confidence): v3 trio adopts the lived form.
- **N8**: Spec internal-consistency observation — `.claude/session-handoffs/TASK-0024-spec.md` line 119 says "13 top-level §-sections" while actual is 14 (spec §7 Claim 1 correctly says 14). Within-spec drift class — distinct from §23.6.3 cross-document drift class. Refinement-eligible at future PMN; could fold into PMN-010 as co-class observation or stand alone (framing decision deferred to TASK-0025 PMN-010 authoring time).
- **N9**: (i.5) catch-surface segmentation refinement: previously {Builder pre-flight, Codex pre-commit, GitHub PR-open API} for forward-ref-§-citation class. Now segmented by drift class: {Builder pre-flight (forward-ref-§-citation class), Codex pre-commit (cross-doc-shape-drift class)}. Surface-class segmentation detail preserved for PMN-010 authoring-time reconciliation.
- **N10**: §23.6.2 self-review fixed-point convergence: 2 iterations (anticipated 3-5; converged faster due to small fix-up surface and no cascading defects). Below cycle-bandwidth budget.
- **N11**: Meta-(i.5) class observation per N4 12→9 refinement: spec-context-vs-body-citation conflation is a refinement-eligible class for §23.6.3 sub-shape enumeration (distinct from sub-shapes A/B/C/D/E currently canonicalized). Builder pre-flight finding scope can over-enumerate when conservatively unioning spec-text anticipated citations with body-prescription actually-cited citations; step-9 (j) sweep narrows to actually-cited. Surface-class refinement candidate for PMN-010 authoring at TASK-0025+.
- **N12**: Meta-(i.5) class observation from Codex post-PR Finding 1 (Feature Brief path drift): cross-doc artifact-path verification is a refinement-eligible class for §23.6.3 sub-shape enumeration (sibling to N11; distinct from forward-ref-§-citation class). Step-1 (i.5)(c) verification scope was forward-ref-§-citation focused; artifact-path conventions (Feature Brief paths, handoff paths, review-context paths, PMN paths, ADR paths) weren't part of pre-flight verification scope. usage-guide.md introduced `docs/features/FEAT-####/brief.md` directory-style form against 3-surface-consistent lived practice (`docs/features/FEAT-####-<slug>.md` flat-file form: actual file + FEAT-0001 self-reference + TASK-0002 handoff cross-ref + PR-2 review-context cross-ref) with zero v3 trio canonicalization (github-reference.md has no Feature Brief path content). Path-(a) in-cycle correction applied at step-16. Two refinement-eligible sub-classes surfaced this cycle (N11 + N12) — pattern strength is signal, not noise; PMN-010 sub-shape enumeration should expand to cover both at TASK-0025 authoring. Surface-class refinement candidate for PMN-010.
- **N13**: Codex post-PR §8.1.1.2 phantom-action observation: Codex bot summary on endpoint 2 (`issues/29/comments`) at 2026-05-05T18:34:51Z claimed concrete actions — "Committed the follow-up change as `e234894 docs(usage-guide): align feature brief path examples`" + "recorded a PR via the `make_pr` tool" + four ✅ test-step claims (`git diff --check`, `rg`, `git status`, `git log`). §8.1.1.2 four-category verification all-fail-confirmed: (i) commit `e234894` does not exist in any branch/ref (`git rev-parse --verify e234894` → `fatal: Needed a single revision`); (ii) no commit on any branch matches "align feature brief" message; (iii) no follow-up PR exists post-PR-29 (`gh pr list --state all` returns only PR-29/28/27/26/25); (iv) n/a. Branch tip `d12852f` unchanged from Builder push; working tree clean; phantom-action operationally zero-impact. **Substantive concern beyond this cycle**: concrete fabrication with specific identifiers (named SHA `e234894`, named tool `make_pr`, ✅-formatted test claims) is a meaningful failure mode distinct from vague hallucination. PMN-008 (h.4) accumulation: this is a fourth-class data point (claimed-action fabrication with specific identifiers); pattern recurrence at TASK-0025/26+ may warrant Codex-replacement evaluation OR discipline shift to "ignore Codex action-claims by default; credit only observable repo state via independent verification." Carry as PMN-010-relevant pattern for owner awareness.
- **N14**: (i.5) cumulative empirical record advances 13 → 14 (step-1) → 15 (step-9) → 16 (Codex pre-commit Finding 1) → **17** (Codex post-PR Finding 1 Feature Brief path = cross-doc-state-verification at new Codex post-PR surface). (i.5) catch-surface segmentation refined: was {Builder pre-flight, Codex pre-commit, GitHub PR-open API} for forward-ref-§-citation class; now {Builder pre-flight (forward-ref-§-citation), Codex pre-commit (cross-doc-shape-drift on branch convention), Codex post-PR (cross-doc-artifact-path-drift on Feature Brief path)} — three distinct catch-surfaces × three distinct drift sub-classes mapped at this cycle. PMN-010 evidence base substantially enriched.
- **N15**: Forward-cycle observation: github-reference.md has zero Feature Brief path canonicalization. After step-16 path-(a) fix-up, usage-guide.md is the only v3 doc with this content. Surgical-or-defer guard rules out scope-expansion this cycle; carry forward as TASK-0025+ v3 canonical-law-trio artifact-path-convention review (parallel to AGENTS.md/CLAUDE.md → v3 migration cycle scope).
- **N16**: (w) data point classification at PR-29 emission: Codex emission timestamps endpoint 1 `pulls/29/reviews` 18:34:36Z + endpoint 2 issue-comment 18:34:51Z; owner trigger on issue-comment 18:32:05Z. Codex emission ~2.5 minutes after owner trigger. **Triggered emission**, not autonomous. (w) carries forward at 3 confirmations; no fourth data point at PR-29.
- **N17**: §8.1.1.2 phantom-SHA observation second-instance this cycle (post-fix-up Codex re-review at `7cb557d`): Codex re-review line-comment body referenced fabricated SHA `ad8af2a` in shell example (`git diff --shortstat ad8af2a^ ad8af2a`); `git rev-parse --verify ad8af2a` returns `fatal: Needed a single revision`. Distinct sub-class from N13 first-instance (action-claim fabrication: claimed commit `e234894` + `make_pr` tool action) — N17 is reference-fabrication-within-finding-body (Codex's substantive diff-stats claim 765/5 matched reality at re-review time `7cb557d`; only the SHA in shell example was fabricated). Two distinct §8.1.1.2 phantom-SHA sub-classes within single PR-29 review cycle: action-claim fabrication (N13) + body-reference fabrication (N17). PMN-008 (h.4) phantom-action namespace accumulates fast within single cycle — meaningful pattern for PMN-010 evidence base; case strengthens at TASK-0025/26+ for either Codex-replacement evaluation OR discipline shift to "verify all Codex-cited SHAs against git before crediting." Carry as PMN-010-relevant pattern; flag for owner awareness.

## §11. Session log archive

(Empty at handoff-authoring time; populated at session-boundary write-back per core.md §6.5.)
