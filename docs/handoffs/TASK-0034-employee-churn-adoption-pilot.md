---
task_id: TASK-0034
title: Adoption-pilot retroactive documentation cycle — employee-churn first AMAS adoption pilot
pr: PR-50
branch: feat/task-0034-employee-churn-adoption-pilot-documentation
linked_predecessor: TASK-0033 (PR-48 squash eb606f1 Batch P1 close — system documentation templates content fill + PMN-011 co-ship)
linked_successor: TASK-0035 (template-amendment candidate per PMN-012 recommendations)
linked_pr: PR-50 (Builder fills with squash SHA post-merge per PMN-001 (k))
framework_version_dogfooded: AMAS v2.30
production_target: AMAS v3.0
spec_source: .claude/session-handoffs/TASK-0034-spec.md (gitignored per ADR-001 D15)
date_authored: 2026-05-11
status: active
---

# HANDOFF: TASK-0034 — Adoption-pilot retroactive documentation cycle (employee-churn first AMAS adoption pilot)

## Metadata

- Linked PR: [PR-50](https://github.com/bryce-murphy/amas-framework/pull/50)
- Authored by: Architect (Claude Opus 4.7, Claude.ai Project) at `2026-05-11T09:59:27-04:00`
- Cycle class: **adoption-pilot-retroactive-documentation** (NEW class at AMAS framework per spec §0.1; first instance)
- Downstream repo cycle: [`bryce-murphy/employee-churn`](https://github.com/bryce-murphy/employee-churn) TASK-0001 (Issue #6, PR #7)
- Session context: cross-laptop coordination via owner relay; upstream Architect at work laptop, downstream Architect (ChatGPT 5.5 Thinking + GitHub connector) at personal laptop

## §1. Cycle objective + framing

TASK-0034 observed and documents the first downstream adoption pilot at `bryce-murphy/employee-churn`. Employee-churn TASK-0001 executed from a downstream-ratified issue body and Builder handoff, while upstream amas-framework captured empirical findings and retroactive cross-repo cycle artifacts. This cycle establishes the **adoption-pilot retroactive-documentation cycle class** for AMAS framework cycle taxonomy (spec §0.1; first instance).

Cycle-class semantic boundaries (spec §0.1 + §1.3): NO Class A v-bump; NO §18.3 M-A7 enumeration; NEW class distinct from substantive-content cycles (TASK-0030 through TASK-0033). Future canonicalization at TASK-0035+ §23.6.3 consolidation cycle if pattern recurs.

Cycle scope: 3 NEW files + 1 MODIFIED file at amas-framework (handoff + review-context + PMN-012 + README L30 Roadmap progression). PMN-012 co-shipped at this cycle per PMN-after-cycle cadence; canonicalizes 2 substantive empirical findings (F1 upstream v2.30/v3.0 packaging ambiguity + F2 handoff-currency recursion at template form) + 2 light-touch sub-findings (F3 per-role scorecard `source_of_truth_for_framework_anchors` recommendation + F4 cross-laptop coordination patterns).

## §2. Cross-repo cycle context

Empirically verified at pre-flight via `gh api` against `bryce-murphy/employee-churn` (per spec §8 step-1 (XXIV) extended batch):

- **Issue**: [employee-churn#6](https://github.com/bryce-murphy/employee-churn/issues/6) — state `closed`; title `TASK-0001: AMAS v2.10→v2.30 process-template retrofit`
- **PR**: [employee-churn#7](https://github.com/bryce-murphy/employee-churn/pull/7) — state `closed`; merged `2026-05-10T20:42:06Z`
- **Branch used at downstream**: `chore/6-amas-v2-30-upgrade` (empirical confirmation of `chore/<github-issue-#>-<kebab-summary>` convention at employee-churn — branch number is the GitHub issue number `6`, not the logical task number `0001`; see PMN-012 §5 observation 6)
- **Substantive PR-open commit**: `946bf12d68dd3f8e11fdcd59dc634f0dc47f52b3`
- **Squash merge commit**: `8d4eb0d042db4e7753eb3ca42db4ce8bf642ef72`
- **Absorption commits**: `0f94885ebf78f06afaccc5383b48754270a9128e` (C1/C2 absorption) + `ebbed880c90d1d373f334b0268cabcbb70f8fae5` (C3/C3-bis absorption)
- **Downstream handoff**: `docs/handoffs/TASK-0001-amas-v2-30-upgrade.md` (path verified at `@ref=8d4eb0d`)
- **ADR-003 actual filename at downstream**: `docs/adr/ADR-003-ai-operating-model-single-contributor-governance.md` (path verified at `@ref=8d4eb0d`; distinct from upstream's `ADR-003-full-package-pr-plan.md` because downstream's ADR-003 is the AI operating-model governance ADR, not the upstream's full-package PR plan)

Cross-laptop coordination: upstream Architect (Claude Opus 4.7) at work laptop where amas-framework local checkout lives + downstream Architect (ChatGPT 5.5 Thinking + GitHub connector) at personal laptop where employee-churn local clone lives. Bryce served as coordination relay between laptops.

## §3. Completed evidence enumeration

Downstream deliverables landed at employee-churn TASK-0001 (subject of this cycle's retroactive documentation; NOT pending instructions):

1. **AMAS v2.10 → v2.30-era process-template retrofit applied** at employee-churn governance surfaces
2. **Preserved local v2.10 operating-system core** at `docs/ai-operating-system.md` with upgrade notice (ChatGPT-recommended path; safer than stub-pointer given upstream v2.30/v3 packaging ambiguity — see PMN-012 §2 F1)
3. **Added `.amas/surfaces.yml`** per v2.30 surfaces-manifest template (canonical form-of-record from upstream PR-48)
4. **Added per-role scorecards** at `docs/role-scorecards/{architect,builder,reviewer}.md`
5. **Realigned `docs/project/project-brief.md` + `docs/project/tool-inventory.md`** content shape (v2.30 upstream canonical convention places these at root of `docs/` — `docs/project-brief.md` + `docs/tool-inventory.md`; `.amas/` is for surfaces-manifest only. Employee-churn preserved local `docs/project/` subdirectory paths per ChatGPT recommendation rather than relocating to canonical root-of-`docs/` form — adopter-local discretion preserved)
6. **Added artifact-only `docs/features/FEAT-0001-platform-baseline.md`**
7. **Added TASK-0001 handoff** at `docs/handoffs/TASK-0001-amas-v2-30-upgrade.md`
8. **Updated receiving surfaces** (`README.md` + `AGENTS.md` + `CLAUDE.md` + ADR-003) with v2.30 references

## §4. Codex review absorption record at downstream

Four Codex findings absorbed at employee-churn during PR-7 review iterations (verified via PR-7 GitHub history + ChatGPT employee-churn Architect hand-back synthesis):

- **C1**: frontmatter missing on TASK-0001 handoff → resolved in absorption commit `0f94885`
- **C2**: stale next-step state on TASK-0001 handoff → resolved in absorption commit `0f94885`
- **C3**: stale current-state wording on TASK-0001 handoff → resolved in absorption commit `ebbed88`
- **C3-bis**: duplicate of C3 from second `@codex review` trigger → resolved in absorption commit `ebbed88`

C3 + C3-bis surfaced the **handoff-currency recursion finding** canonicalized at PMN-012 §3 (this cycle). The defect class — committed-file present-tense live-state claims going stale at every absorption iteration — is the explanatory mechanism for (XVII)-class cumulative-diff-stats anticipation narrowness observed retrospectively at upstream TASK-0030 / TASK-0031 / TASK-0032 / TASK-0033 handoff state-snapshot fields.

## §5. Empirical findings summary (deferred to PMN-012 for canonical capture)

- **F1** (substantive): Upstream v2.30/v3.0 packaging ambiguity — `amas-framework@v2.30/core.md` declares partial v3 content (`framework_version: 3.0.0` + `status: partial` + heading "AMAS v3 Core") while adopter-facing surfaces (README + AGENTS.md + CLAUDE.md + ADR references) advertise canonical version as v2.30. Adopter impact at employee-churn: forced adapter pattern (preserve local v2.10 core; scope adoption to v2.30-era process-template layer only). Canonicalized at PMN-012 §2.
- **F2** (substantive): Handoff-currency recursion at handoff template form — current canonical at `templates/handoff-template.md` conflates durable handoff record + live workflow state tracker functions; latter is inherently volatile and goes stale at every absorption iteration. Retrospectively explains (XVII)-class instances at TASK-0030/31/32/33. Past ADR-006 D3 evidence-bar 3+ promotion threshold by significant margin. Canonicalized at PMN-012 §3; canonical-text amendment to `templates/handoff-template.md` deferred to TASK-0035 dedicated template-amendment cycle.
- **F3** (light-touch): Per-role scorecard `source_of_truth_for_framework_anchors` field recommendation — for vendored/pointer-only adopters operating with packaging ambiguity (per F1), scorecards should explicitly declare which canonical source applies to §-anchor references. Carry-forward observation; canonical-text amendment at `templates/role-scorecard-template.md` deferred to TASK-0035.
- **F4** (light-touch): Cross-laptop coordination patterns + friction observations — 6 enumerated observations at PMN-012 §5 (issue-body-as-sufficient-execution-artifact; copy/paste relay risk manageable; remote-visible action gates valuable; local WIP collision risk real; duplicate Codex review triggers possible; branch-number semantics explicit at adopter projects).

## §6. Cycle gates record (verification-first per F2 fix-pattern)

Historical gates anchored to durable evidence (not live state). PR-50 at amas-framework is the canonical live-state surface for ongoing/in-flight gates; verify head SHA + review-thread state from PR-50 directly before acting on any conditional next step.

Completed gates (this cycle):

- **Step-1 pre-flight verification**: completed 2026-05-11; `origin/main` HEAD `98d7324566fd04b4e5bf242825309254938fb127`; cross-reference empirical verification of all employee-churn artifacts (Issue #6 + PR #7 + 4 commits + branch + ADR-003 filename + downstream handoff path) PASS; §-citation verification at core.md PASS; README L30 anchor verification PASS; (XXIV) refinement candidate 2nd in-cycle empirical positive surfaced.
- **Step-2 branch creation**: completed 2026-05-11; `feat/task-0034-employee-churn-adoption-pilot-documentation` from `98d7324`.
- **Step-4.1 → 4.4 authoring**: completed 2026-05-11; handoff + review-context + PMN-012 + README L30 update authored per spec §4.1-§4.4.

In-flight / pending gates (verify live state from PR-50 before acting):

- **Step-9 self-review iteration**: §23.6.2 fixed-point convergence + §5 verification command battery — verify via `git log -1 origin/feat/task-0034-employee-churn-adoption-pilot-documentation` and PR-50 CI state.
- **Step-10 pre-commit stop-and-show**: (e.1) cumulative-diff-stats re-derivation + bidirectional sum-stability + (XVII) file-level enumeration — verify staged-tree state via `git diff --staged --shortstat origin/main` before acting.
- **Step-10.X path-(α') status transition**: `drafted` → `active` token swap on this handoff frontmatter.
- **Step-11 → 17 downstream gates**: Codex desktop pre-commit pass-1 → absorption → commit + PR open + placeholder substitution → `@codex review` invocation → post-PR absorption → (XXVI) Gate A + Gate B → owner merge via §10.5. Each gate's live state visible at PR-50.

## §7. Cycle-close ledger

NEW ledger entries from this cycle (surfaced through step-10.X; downstream entries pending):

- **(I) NEW**: 1st adoption-pilot retroactive-documentation cycle empirical anchor for cycle class establishment per spec §0.1. Sub-class refinement candidate at (XVI) tier framework if pattern recurs across multiple adoption pilots.
- **(II) NEW**: cross-laptop coordination empirical anchor for PMN-012 §5 F4 sub-finding. 1st in-cycle test; cross-cycle accumulation pending future adoption pilots.
- **(III) NEW**: (XXIV) cross-surface meta-class refinement candidate 2nd in-cycle empirical positive at TASK-0034 pre-flight (canonical-source verification of all employee-churn artifacts + §-citation resolution at core.md + README L30 anchors via `gh api` + `grep` against canonical state; zero defects surfaced).
- **(IV) NEW** (per step-10 Architect adjudication of Finding 1): (XXIV)-class Architect-side spec §4.2 review-context frontmatter defect — spec prescribed 1-field `review_target_pr:` only, omitting canonical `status: drafted` field required by `.github/scripts/linked-pr-fix-up.py` substitution contract (Action substitutes `status: drafted → recorded` per `linked-pr-fix-up.py:42`). 2nd cross-cycle (XXIV) Architect-side authoring narrowness at TASK-0034 (1st = spec §3 anticipation narrowness underlying ledger entries (V) + (VIII)). Reinforces PMN-011 §2.4 (XXIV) cross-cycle canonicalization candidacy at TASK-0035. **Builder §24.3 receiving-discipline caught the divergence via canonical Action contract verification at Builder claim-authoring time** — empirical positive sub-observation for receiving-discipline application that PMN-011 §2.4 promotes; PMN-012 §6 monitoring section can note this as continued (XXIV) empirical reinforcement (light-touch addition; doesn't require PMN-012 body amendment at this cycle). Path-(α') restore convention applied at step-10.X: `status: drafted` field added to review-context frontmatter restoring PR-48 precedent.
- **(V) NEW**: (XVII)/BD.4 5th cross-cycle confirmation — Architect-side anticipation narrowness on Architect's own byte-exact prescription. PMN-012 byte-exact transcription came in at 194 ins vs spec §3 anticipated 280-350 ins (low by 86-156 ins); spec body content itself is ~185 lines, so the anticipation envelope was wider than the prescribed content. Plus handoff (131 vs 220-260) + review-context (77 vs 100-140) + README (1/1 vs 3-5/3-5) all came in below low-end. Aggregate 403 ins vs 603-755 anticipated (low by 200 ins). BD.4 byte-exact under-target pattern continuance per PMN-011 §3.
- **(VI) NEW**: (XXIV) cross-surface canonical-source verification 2nd in-cycle empirical positive at handoff §2 cross-reference resolvability authoring time (distinct from pre-flight (III) — this is at handoff authoring surface). All employee-churn cross-references at handoff §2 (Issue #6 + PR #7 URLs + 4 commit SHAs + branch name + ADR-003 downstream filename + downstream handoff path + merge timestamp `2026-05-10T20:42:06Z`) authored against pre-flight `gh api` empirical state; zero authoring-time hallucination defects.
- **(VII) NEW**: F2 fix-pattern self-instantiation empirical test in flight — handoff §6 (Cycle gates record) + §9 (Verification-first current state guidance) authored per PMN-012 §3.3 fix-pattern (historical gates anchored to SHAs/timestamps; PR-50 as canonical live-state surface; conditional verify-before-act framing for in-flight gates). Eat-our-own-dogfood at the cycle that surfaces the finding. Codex pre-commit pass-1 + post-PR pass-1 will surface whether verification-first framing holds across absorption iterations or whether further refinement is needed before TASK-0035 canonical-text amendment to `templates/handoff-template.md`.
- **(VIII) NEW**: README L30 long-line semantics — 1 ins / 1 del net diff is the correct artifact of 2 logical substitutions (paragraph rotation + batch sequence diagram) both landing on same physical long-line markdown paragraph. All 3 grep anchors (`first AMAS adoption pilot completed`, `8d4eb0d`, `Adoption-pilot\[employee-churn complete\]`) confirmed present at L30 by §5.4 verification. (XVII)-class spec anticipation narrowness on physical-line-vs-logical-substitution distinction.
- **(IX) NEW** (per step-10.X (e.1) re-derivation sub-finding): spec §5.1 PMN-012 verification command `head -5` narrowness — `head -5` captures L1-L5 (1 `---` delimiter + 4 fields), missing 5th field `status: drafted` on L6. Architect-side spec verification-command authoring narrowness (same (XXIV)/(X) class as Finding 1 but lighter; verification-command surface, not artifact-content surface). Corrected to `head -7` at Builder verification battery + at review-context claim 2.
- **(X) NEW** [Codex F1 path-(α')]: Architect-side handoff frontmatter schema authoring narrowness — spec §4.1 invented 12-field schema (`handoff_id`, `authored_by`, `authored_at`, `framework_version`, `cycle_class`, `predecessor_cycle`, `successor_cycle`, `downstream_repo_cycle`, `session_context` etc.) without verifying canonical 12-field shape per `templates/handoff-template.md` / `core.md` §14 (canonical fields: `task_id`, `title`, `pr`, `branch`, `linked_predecessor`, `linked_successor`, `linked_pr`, `framework_version_dogfooded`, `production_target`, `spec_source`, `date_authored`, `status`). (XXIV) class major recurrence at canonical-form level; most serious authoring narrowness at TASK-0034. Path-(α') applied at step-12.X: canonical 12-field frontmatter restored; non-canonical fields (`authored_by`, `cycle_class`, `downstream_repo_cycle`, `session_context`) moved to body `## Metadata` block right after H1.
- **(XI) NEW** [Codex F2 path-(α')]: Architect-side review-context frontmatter field invention — `review_target_pr` not in canonical 1-field schema per `templates/review-template.md` / `core.md` §17.7 (canonical: `status: drafted` only). Also wasn't caught at Builder Finding 1 ratification at step-10 — added `status: drafted` but kept the non-canonical `review_target_pr` field. 2nd-layer (XXIV) narrowness — even the discipline-fix application (Finding 1 restore convention) was applied against partially-incorrect schema understanding. Path-(α') applied at step-12.X: canonical 1-field `status: drafted` only; PR reference + reviewer + review scope moved to body `## Metadata` section. Kickoff text updated to remove stale `review_target_pr` reference.
- **(XII) NEW** [Codex F3 path-(α')]: PMN-012 title↔H1 em-dash mismatch — H1 had `: upstream packaging ambiguity ...` vs title's ` — upstream packaging ambiguity ...`. **(XXIV.e) sub-shape recurrence at consecutive cycles** — PMN-011 had same defect at TASK-0033 (XIV); now PMN-012 has same defect at TASK-0034 despite PMN-011 §2.4 promotion of (XXIV) refinement candidate. Pattern: copy-from-prior-PMN inherits the em-dash-vs-colon authoring habit. Path-(α') token swap applied at step-12.X.
- **(XIII) NEW** [Codex F4 path-(α')]: PMN-012 §1 internal cross-reference defect — `documented at §4 below` should be `§5 below` (observation 1 lives at §5 cross-laptop coordination; §4 is per-role scorecard F3 finding). Authoring narrowness on internal PMN body cross-references. (XXIV.h) NEW sub-shape candidate: internal PMN cross-reference verification at PMN body authoring. Path-(α') token swap applied at step-12.X.
- **(XIV) NEW** [Codex F5 path-(α')]: Handoff downstream path-deviation description error at §3 item 5 — conflated `docs/project-brief.md` / `docs/tool-inventory.md` (v2.30 canonical convention at root of `docs/`) with `.amas/` (which is for surfaces-manifest only). (XXIV.i) NEW sub-shape candidate: path-claim semantic-domain verification at body content authoring. Path-(α') correction applied at step-12.X: description rewritten to correctly identify v2.30 canonical layout + employee-churn's local `docs/project/` subdirectory preservation.
- **(XV) NEW** [Codex sub-observation]: AGENTS.md v2.14.1 public substrate URL returned 404 at Codex verification. **NOT TASK-0034 scope**; carry-forward observation for separate amas-framework cycle attention. May indicate stale substrate URL at AGENTS.md needing update. Not addressed at this cycle.
- **(XVI) meta-observation** (cross-cycle ledger only; not amending PMN-012 at this cycle): TASK-0034 spec authoring produced 6 distinct (XXIV)-class defects despite PMN-011 §2.4 promotion of refinement candidate. Pattern across TASK-0033 + TASK-0034: TASK-0033 spec = 5 in-cycle (XXIV) instances; TASK-0034 spec = 6 in-cycle (XXIV) instances. PMN-011 §2.4 (XXIV) refinement candidate as currently formulated covers only canonical-source enumeration (a-sub-shape). Empirically observed sub-shapes extend across (XXIV.b)-(XXIV.i) per (XVI) cross-cycle accumulation. Pattern strongly reinforces canonical-text amendment candidacy at TASK-0035 with paired discipline framing (authoring-time discipline + receiving-discipline catch). Builder §24.3 receiving-discipline + Codex pre-commit pass-1 caught all 5 Codex findings empirically — **paired discipline works even when authoring-time discipline narrows**.
- **(XVII) NEW** [post-PR Codex auto-fire clean verdict]: Codex post-PR review at PR-50 returned **zero Blocking / Major / Minor findings**. All Builder claims at review-context "## Builder claims to verify" empirically validated by Codex's Python frontmatter shape verification + linked_pr regex verification + rg placeholder sweep. **12th cross-cycle empirical positive for §8.1.1.3 cost-class refinement** (zero-iteration convergence at post-PR Codex review for adoption-pilot retroactive-documentation cycle class). Validates Architect step-12 cost-class adjudication that Codex pass-2 NOT REQUIRED after pre-commit pass-1 absorption.
- **(XVIII) NEW** [(h.4) §5.3 auto-fire-first sub-shape confirmed at TASK-0034]: Codex auto-fired on PR-open at `2026-05-11T14:56:29Z` BEFORE owner `@codex review` invocation at `2026-05-11T15:08:07Z` (~12 min delta). Owner-invocation produced duplicate confirmation response at `15:11:28Z`. Auto-fire-first sub-shape continues (h.4) cross-cycle accumulation per PMN-008 §5.8.
- **(XIX) NEW** [Codex external verification limitation honest disclosure]: Codex acknowledged inability to revalidate employee-churn cross-references due to environment constraints (no `gh` binary; API tunnel `403 Forbidden`). Treated as externally unverified rather than asserting revalidated. Builder pre-flight empirical verification at step-1 via `gh api` remains canonical anchor for cross-reference claims; Codex's limitation is environment-specific not a verification gap. Honest-disclosure pattern at Codex side — empirical positive for §24.3 receiving-discipline reach across surfaces (Codex declining to assert beyond its verification capability).
- **(XX) NEW** [verification claim 1 ratification at Codex authorial canonical-source verification]: Codex independently verified handoff canonical 12-field shape against `templates/handoff-template.md` schema; Builder's step-12.X F1 path-(α') canonical schema restoration empirically validated by Codex Python verification. (XXIV.g) sub-shape application at Codex surface — Codex pulled canonical template + counted fields before asserting validation, matching the receiving-discipline pattern Builder applied at step-12 + Architect applied at step-12 ratification (per Architect §4 "(XVII) candidate" inverse-surface observation). Three-surface paired discipline empirically confirmed: authoring (Architect) ↔ receiving (Builder) ↔ ratification (Architect) ↔ post-PR review (Codex).

## §8. Cross-references

- `core.md` §14 universal handoff schema (canonical at PR-41) — applied with adoption-pilot cycle-class adaptation per spec §4.1
- `core.md` §17 + §17.5 + §17.7 templates parent frame + lifecycle + review template
- `core.md` §18.1 PMN-trigger criteria + §18.2 PMN form spec + §18.3 M-A7 (NOT amended this cycle per spec §0.1) + §18.4 (NO v-bump per spec §0.1)
- `core.md` §23.6 + §23.6.1.1 + §23.6.2 + §23.6.3 Architect-side self-review disciplines
- `core.md` §24 + §24.3 + §24.3.1 verify-before-assert meta-pattern + receiving-discipline + Architect ← Builder hand-back five-point check
- ADR-001 D9 (owner squash-merge authority) + D11 (Codex owner-invokes) + D15 (spec-source gitignore)
- ADR-003 D1 (v3.0 ship scope) + D3 (TASK reservation + PMN insertion budget; PMN-012 consumes contingency slot)
- ADR-005 (branch convention regex; `feat/task-####-<kebab-slug>` applied)
- ADR-006 D2 + D3 + D4
- ADR-007 D3 (Part C materialization scoping schedule)
- PMN-001 (k) (chore-fix-up substitution discipline; applied at handoff + PMN-012 `linked_pr` field placeholder)
- PMN-007 §3.3 + §9.1 (12-field handoff frontmatter canonical)
- PMN-008 §5.8 (h.4) (Codex emission pattern auto-fire-or-owner-invoke disjunction)
- PMN-009 sub-shapes; PMN-010 sub-shape 1
- PMN-011 (XVI/XVII/XVIII/XXIV/XXVI refinement candidates; this cycle operationalizes (XVII) bidirectional sum-stability + (XXIV) cross-surface canonical-source verification + (XXVI) two-gate §24.3.1 discipline 3rd-instance test)
- **PMN-012** (this cycle's co-shipped post-merge note; canonicalizes F1 + F2 + F3 + F4 empirical findings)
- TASK-0033 cycle-close handoff (predecessor reference)
- TASK-0035 candidate (successor reference; template-amendment cycle per PMN-012 §3.4 + §4 recommendations)
- employee-churn TASK-0001 — [Issue #6](https://github.com/bryce-murphy/employee-churn/issues/6) + [PR #7](https://github.com/bryce-murphy/employee-churn/pull/7) (downstream cycle this handoff documents)

## §9. Verification-first current state guidance

Per F2 fix-pattern (PMN-012 §3.3): **PR-50 at amas-framework is the canonical live-state surface for this cycle.** This committed handoff is a durable record; do not treat its enumerations of in-flight gates as authoritative live state.

Before acting on any continuation of this cycle:

1. **Verify latest head SHA** from PR-50 or `git log -1 origin/feat/task-0034-employee-churn-adoption-pilot-documentation`.
2. **Verify review-thread state and mergeability** from PR-50 GitHub UI (CI status; Codex review verdict; outstanding review threads).
3. **Verify cycle gate position** conditionally: first inspect PR-50 state, then decide whether Codex pre-commit pass-1 has fired, whether @codex review has been invoked, whether absorption iterations are pending, or whether the cycle is at the owner merge gate.
4. **Only then act**. Do not assume gate position from this handoff; the handoff is a historical record of decisions and authoring evidence, not a live PR dashboard.

This handoff's own authoring is an empirical test of the F2 fix-pattern at the cycle that surfaces the finding — eat-our-own-dogfood at PMN-012 §3 canonicalization. Codex review of this cycle's PR-50 will surface whether the verification-first framing holds across absorption iterations or whether further refinement is needed before TASK-0035 canonical-text amendment to `templates/handoff-template.md`.
