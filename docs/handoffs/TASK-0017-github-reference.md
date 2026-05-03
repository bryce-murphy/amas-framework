---
task_id: TASK-0017
title: github-reference.md substantive content authoring (canonical-law trio second member)
pr: PR-17
branch: feat/task-0017-github-reference
linked_predecessor: TASK-0015 / PR-15 (squash SHA ace6608); TASK-0015 PMN-001 (k) chore-fix-up / PR-16 (squash SHA d274b87)
linked_successor: TBD (next substantive cycle; anticipated usage-guide.md authoring)
linked_pr: PR-17 (Builder fills with squash SHA post-merge per PMN-001 (k))
framework_version_dogfooded: AMAS v2.17
production_target: AMAS v3.0
spec_source: .claude/session-handoffs/TASK-0017-spec.md (gitignored per ADR-001 decision 15)
date_authored: 2026-05-03
status: active
---

# TASK-0017 — github-reference.md substantive content authoring (canonical-law trio second member)

## Metadata

- TASK ID: TASK-0017
- PR: PR-17
- Branch: `feat/task-0017-github-reference`
- Author surface: Builder (Claude Code, Claude Opus 4.7, Windows 11 + Git Bash)
- Date authored: 2026-05-03
- Linked records: PMN-001 (h.2)/(k); PMN-002 (a)/(d); PMN-003 (a)-refined/(e)-refined; PMN-004 §5 (a)-(f) + §1 4-iteration self-review; PMN-005 §2.5/§4.4 (e.1); PMN-006 §3 (g)/(h)/(i) + §5.3 bounded-continuation generalized + §3.4 frontmatter-vs-body sub-clause; PMN-007 §3.1 four-surface refinement + §4 PMN-001 (k) mechanism-vs-discipline canonicalization; ADR-001 decisions 9/11/15; ADR-003 Decision 2 (canonical-law trio second member; tight-coupling dependency order)
- Framework version dogfooded: AMAS v2.17
- Production target: AMAS v3.0
- Spec source: `.claude/session-handoffs/TASK-0017-spec.md` (gitignored per ADR-001 decision 15)

## Last completed step

[Filled at hand-back per established pattern.]

## Current state

[Filled at hand-back per established pattern.]

## Decisions made

The handoff records inherited Architect-decided scope decisions per spec §1-§4 plus in-cycle Builder-pre-flight-surfaced adjudications:

- **Phase 1 D1 §-header structure** — 8 top-level §-sections in github-reference.md per spec §1.4. Decomposition: §1 purpose + §2 repo structure + branch naming + §3 branch protection + governance + §4 GitHub artifact templates reference + §5 AI agent identity + §6 deterministic Actions reference + §7 surface-file synchronization + §8 cross-references = 8.
- **Phase 1 D2 source-line target** — ~500-650 lines target per spec §1.4. Body-vs-total-line distinction surfaced at iteration time per (i.4) recap-consistency sub-shape (anticipated by spec §6.1 claim 4 framing).
- **Phase 1 D3 forward-reference discipline** — explicit "ships at PR-N per ADR-003 Decision 2" pointers (not naming specific PR numbers) per spec §1.4.
- **Phase 1 D4 framework version bump** — v2.16 → v2.17 per §18.4 substantive-reading minor criterion. Second canonical-document version bump applying §18.4 (first was PR-13 self-instantiation; this is second-instance application of canonical text).
- **Phase 1 D5 README + stub frontmatter updates** — per ADR-003 §Consequences distributed-update discipline. README "Package layout" row + "Status" canonical-version-of-record line; github-reference.md frontmatter `filled_by` + `status` field updates at content-fill (`framework_version` field preserved at stub value 3.0.0 per ADR-003 §Consequences "Stub framework_version field untouched").
- **Phase 1 D6 PMN-008 candidates as monitoring items** — 9 candidates registered per spec §1.3 (q / r / (j)-extension / s / (i.5) / t / (k.3) / (d) / (meta-1)). Emission deferred until material accumulates beyond single-cycle preliminary across the candidate set.
- **Phase 1 D7 extended pre-authoring batch + (i.5) sub-shape** — applied at spec §5.1 step 1.
- **Phase 1 D8 multi-stage review pipeline** — full five-surface (Architect §23.6 + Builder pre-flight + Builder step-6 self-review per (r) candidate + Codex pre-commit + Codex post-PR).
- **Phase 1 D9 bounded-continuation routing** — §8.1.1.3 cost-class refinement applies (genuinely-asymptotic-vs-pure-token-swap distinction).
- **Phase 1 D10 (j) same-class sweep** — at every path-(a) revision per PMN-007 (j) cluster.
- **Step 1 / Step 7 stop-and-show — core.md framework version marker placement** (Architect adjudication this cycle): core.md does NOT carry a canonical-version-of-record marker. Two `v2.16` references at lines 223 and 234 are historical/cross-document state preserved verbatim — line 223 dates the M-A7 promotion event at PR-13 (`as of v2.16 canonicalization (this PR)`); line 234 is sequence enumeration with `...` continuation marker explicitly signaling illustrative-not-canonical-registry. README.md line 9 is the canonical-version-of-record. **Implication**: deliverable count = 4 (not 5); spec §6.1 claim 9 → N/A; spec §3.5 step 7 substantively no-op. (i.5) convention-inference verification operated as designed — pre-flight grep'd, classified, surfaced rather than inferred. Second-data-point strengthens (i.5) PMN-008 candidate observation.
- **Spec §6.1 claim 12 verification mismatch** (Builder pre-flight surfaced finding): `grep -c "^framework_version:" github-reference.md` returns 2, not 1 as claim 12 anticipated. Cause: §7.1 manifest YAML example contains `framework_version: 3.0.0` at line-start (no indent inside ```yaml fence). Class: verification-claim-vs-byte-exact-content mismatch (the byte-exact §4 content includes the manifest YAML example; claim 12 was authored assuming frontmatter-only matches). Routed in-cycle per §8.1.1.3 cost-class refinement (pure-token-swap class) — claim 12 verification reframed in PR-17 review-context to acknowledge 2 matches (frontmatter + §7.1 YAML example) and assert frontmatter value preservation distinct from grep count.
- **Spec §6.1 claim 4 line-count target** (Builder pre-flight surfaced finding): actual `wc -l github-reference.md` = 391, below 500-650 target. Anticipated by spec §6.1 claim 4 framing ("body-vs-total-line distinction surfaced at iteration time per (i.4) recap-consistency sub-shape"). Class: recap-consistency drift in scoping decision. Routed: claim 4 reframed in PR-17 review-context to assert actual count + (i.4) recap-consistency observation; not a content defect, the byte-exact §4 spec content was 385 lines + frontmatter.
- **Builder step-6 self-review §-citation defect on github-reference.md line 148** (Architect-adjudicated path-(a) fix applied): line 148 originally cited `core.md §10 / §8 references` — §10 not in core.md HEAD §-header set (anachronistic v2.14.1 reference; bypass content migrated from v2.14.1 §10.5-§10.6 to github-reference.md §3.2 in canonical-law trio split). Routing: pure-token-swap per §8.1.1.3 cost-class refinement; path-(a) applied byte-exactly. **Applied fix per Architect adjudication**: `core.md §10 / §8 references` → `v2.14.1 §10.5-§10.6 single-contributor bypass migration source per ADR-003 transition plan §4 row 10` (parallels §6.1 migration-source attribution form canonicalized at iter-2 Defect E1; cites actual v2.14.1 source rather than contriving §24 reference). (j) full-pattern sweep per Architect-refined discipline: zero new core.md §-citation residuals introduced by fix; pre-existing §1 from "core.md §1-§24" span notation at line 367 conventionally permissive. (j)-sweep-completeness candidate refinement registered as PMN-008 monitoring sub-observation (iteration-2 spec sweep caught Defects E1-E4 §15 cluster but missed §10 in §3.2 separate-context propagation residual).
- **Codex post-PR pass 1 Finding 1 — branch regex repo-convention divergence — DEFERRED to separate cycle per Architect adjudication path-(β)**: github-reference.md §2.2 byte-exact regex `^(feat|fix|chore|adr|shadow|spike)/[0-9]+-(...)$` (preserved verbatim from v2.14.1 §6.1) does not match the repo's actual branch convention (`<type>/task-NNNN-<slug>` per CLAUDE.md). Cost-class assessment: **genuinely-asymptotic** per §8.1.1.3 — pure-token-swap (extending regex to permit `task-` prefix) would silently extend canonical text beyond v2.14.1 §6.1 source without canonical-source attribution + ADR-class adjudication (content-drift discipline violation). Resolution requires multi-document reconciliation: read CLAUDE.md to verify claimed `task-NNNN-` form is canonical-as-stated; reconcile against v2.14.1 §6.1; adjudicate which is canonical for AMAS v3; update github-reference.md regex if extension is canonical; update CLAUDE.md / AGENTS.md if repo convention needs alignment to canonical; potentially amend ADR-001 if convention is project-specific extension. github-reference.md ships with v2.14.1 §6.1 verbatim regex this cycle; reconciliation cycle is anticipated next-or-following per Architect Phase 1 scoping consideration. New PMN-008 candidate observation **(u)** v2.14.1-canonical-vs-repo-convention divergence shape registered (single-data-point this cycle; watch usage-guide.md / anticipated trio-third-member authoring for analogous divergences).
- **Codex post-PR pass 1 Finding 2 — advisory/blocking contradiction at github-reference.md §2.3 line 114 — Architect-adjudicated path-(a) fix applied**: §2.3 line 110 said "Non-matching branches do not merge without a human override" (canonical policy = blocking-with-override) while line 114 said "failure is non-blocking by default (advisory) but configurable to blocking" (Architect-asserted at iter-1 spec authoring without canonical-source grounding — v2.14.1 §6.1.1 specifies the policy form not the Action-default-configuration form). Cost-class: pure-token-swap per §8.1.1.3 (single-paragraph clarifying edit). Applied byte-exactly: replaced second paragraph with substitute that (a) removes unsupported "non-blocking by default" claim; (b) clarifies layer distinction (Action emits status; branch protection enforces blocking); (c) preserves original semantic (adopters configure enforcement via branch protection); (d) cross-references §3.1 for canonical enforcement integration; (e) aligns to v2.14.1 §6.1.1 canonical policy "should not merge without override". (j) same-class sweep on advisory-vs-blocking contradictions across full file: §6.1 lines 266 + 269 align with canonical policy (no defect); §6.3 line 289 "advisory" refers to review-emission shape not Action-blocking (no defect); only line 114 had the contradiction.

## Assumptions

- TASK-0017 is the next available TASK number per ADR-003 Decision 3 (verified at step 1 pre-flight: `git ls-files docs/handoffs/` returns 13 files TASK-0001 through TASK-0015; this handoff IS the reservation per ADR-001 decision 15 gitignored-spec convention).
- PR-17 is the next available PR number (verified at step 1: `gh pr list --state open --search "TASK-0017"` returns no results; `git log --oneline --all | grep TASK-0017` returns no merged commits).
- Base SHA `d274b87ab5bdeb1c4fba9d027471721f03d97137` is current `main` HEAD (squash-merge SHA of PR-16, the TASK-0015 PMN-001 (k) chore-fix-up).
- Branch protection on `main` is live and configured per ADR-001 decision 9.
- `gh` CLI authenticated with `repo` scope minimum.
- Codex desktop is available to the owner for step 10 pre-commit review per ADR-001 decision 11 owner-invokes convention.
- `core.md` exists at repo root with 21 §-header structure per spec §5.1 verification (verified at step 1 pre-flight: `grep -nE "^#{1,6} §[0-9]" core.md | wc -l` returns 21).
- `github-reference.md` exists in stub state per ADR-003 PR-7 sweep at repo root (verified at step 1: `head -10 github-reference.md` returns frontmatter `framework_version: 3.0.0` + `status: stub` + `filled_by: per ADR-003`).
- v2.14.1 reference text unavailable at Builder surface (`amas-v2.14.1.md` absent); spec §4 byte-exact canonical text for github-reference.md is authoritative.
- Phase 1 owner adjudications recorded in spec §1-§4 inherited; no re-litigation at session start (except Builder pre-flight defect surfacing per §8 stop-and-show pattern, adjudicated by Architect this cycle on core.md version-marker placement).
- Pre-flight per spec §5.1 confirms: 96 tracked files; clean working tree; main only branch; 21 §-headers in core.md; 8 in docs/post-merge-notes/; 13 in docs/handoffs/; 12 in docs/reviews/; 3 in docs/adr/; ≥1 README mention of github-reference.md; v2.16 references in core.md at lines 223+234 (historical/cross-document state per Architect adjudication); v2.16 in README.md at line 9 (canonical-version-of-record); no merged TASK-0017 commit.

## Risks

- **Surgical-or-defer guard on README.md modifications** (per spec §7): if existing "Package layout" row format is more complex than per-row scope, surface stop-and-show. Mitigation: Builder reads existing structure before applying surgical updates.
- **Frontmatter convention drift** (per spec §7): stub frontmatter convention per ADR-003 PR-7 sweep verified at pre-flight; actual fields confirmed `framework_version` + `status` + `filled_by` order; convention preserved.
- **Pre-authoring batch (extended per (i) + (i.5)) as testable hypothesis** (per spec §7): if TASK-0017 cycle defect count materially exceeds PMN-007 cycle's 11 net distinct baseline, the extended batch + (i.5) sub-shape composition is empirically insufficient — PMN-008 records definitive negative evidence. Currently tracking via spec §1.1 honesty record material to be carried to PMN-008 cycle.
- **Bounded-continuation cost-class self-application** (per spec §7 + (l) failure-mode self-instantiation): this cycle that applies §8.1.1.3 cost-class refinement + (l) bounded-iteration family composition refinement to its own iteration routing must apply correctly per (k.1) positive self-instantiation discipline. Mitigation: explicit cost-class adjudication framing at any path-(β) routing decision.
- **Forward-reference scope drift** (per spec §7): forward-references use "anticipated per ADR-003 Decision 2" framing rather than naming specific PR numbers. Mitigation: per-cycle-row updates per ADR-003 §Consequences distributed-update discipline at the cycles that ship the referenced content.
- **Cluster consolidation pressure for PMN-008 candidates** (per spec §7): 9 candidate observations registered as monitoring items. If TASK-0017 cycle close produces additional empirical material strengthening any candidate beyond single-cycle preliminary, PMN-008 emission may be warranted at cycle close rather than deferred. Architect adjudicates at cycle close.
- **(meta-1) Architect-side context-anchoring drift recurrence** (per spec §7): this spec's authoring is itself an Architect adjudication surface. Mitigation: explicit (meta-1) sweep at §23.6 self-review iteration application.
- **(t) sub-shape pre-merge fix-up commit form** (per spec §5.16): substantive cycle record updates land in fix-up commit on feature branch pre-merge per PMN-007 preliminary two-data-point sub-shape. Third empirical instance of (t) sub-shape if this cycle applies the pattern (PR-13 + PR-15 + PR-17). Three-data-point reaches canonical refinement threshold; PMN-008 candidate refinement.

## Decision points

- **Verification claim 12 reframing** (per Decisions made above): claim 12 expects 1 frontmatter match; actual is 2 (frontmatter + §7.1 manifest YAML example). Routed in-cycle per §8.1.1.3 (pure-token-swap); reframed at PR-17 review-context. If Codex pre-commit or post-PR adjudicates this as defective scope, path-(a) revise per bounded-continuation rule.
- **Verification claim 4 line-count target reframing** (per Decisions made above): claim 4 expects 500-650 lines; actual is 391. Anticipated by spec framing ((i.4) recap-consistency); reframed at PR-17 review-context to assert actual + observation. If reviewers adjudicate as defective scope, path-(a) revise per bounded-continuation rule.
- **(t) sub-shape pre-merge fix-up commit application** (per spec §5.16): apply per established pattern (PR-13 + PR-15 precedents). If owner declines, path-(a) revise to traditional post-merge linked_pr fix-up only.
- **Cost-class routing application in-cycle** (per spec §7 self-application risk): pure-token-swap → path-(a); genuinely-asymptotic → path-(β). Self-instantiation discipline applies (the cycle that applies the rule applies it correctly to its own routing).

## Exact next step

Builder continues §5 step sequence post-handoff creation:

1. **Step 5** — Create `docs/reviews/PR-17-codex-pre-commit.md` per spec §3.3 + §6.1 verifiable claims enumeration.
2. **Step 6** — README.md "Package layout" row + "Status" line surgical update per spec §3.4.
3. **Step 7** — N/A per stop-and-show resolution (core.md does not carry canonical-version-of-record marker).
4. **Step 8** — Step-6 self-review per (r) candidate fifth-surface; (h.x) verification-command + (g.x) verification-artifact + (i.4) recap-consistency sweep against §6.1 claims.
5. **Step 9** — Stop-and-show before commit: list staged files + diff stat + cumulative-diff-stats per (e.1) + verification claim summary.
6. **Step 10** — Owner invokes Codex desktop pre-commit review per ADR-001 decision 11.
7. **Step 11** — Path-(a) revisions if pre-commit findings; bounded-continuation rule §8.1.1.3 applies.
8. **Step 12** — Self-verification iterative-to-fixed-point per §23.6.2 + extended (i) pre-authoring batch.
9. **Step 13** — Commit per spec §5.13.
10. **Step 14** — Push + open PR-17.
11. **Step 15** — Owner invokes `@codex review` post-PR; Builder absorbs Codex post-PR review via two-endpoint poll per core.md §8.1.1.1.
12. **Step 16** — Pre-merge fix-up commit per (t) sub-shape: PR-17 review-context post-PR Codex absorption + this handoff `## Last completed step` + `## Current state` fill.
13. **Step 17** — Hand-back: Architect §24.3.1 five-point post-handback check; owner squash-merges; merge SHA substituted into linked_pr field per PMN-001 (k); Architect updates merge-commit-body per core.md §18.3 with M-A7 seventh empirical instance; Architect adjudicates PMN-008 emission per cycle-summary observations.

## Reassessment / expiry

Handoff status flips to `resolved` after PR-17 is merged + linked_pr substitution + status flip per PMN-001 (k) Linked PR fix-up convention (small-chore-PR mechanism applies if branch protection requires; per PMN-007 §4 mechanism-vs-discipline distinction). If pre-commit Codex review or post-PR Codex review exceeds scope or owner declines stop-and-show, status flips to `blocked` pending Architect direction. Bounded-continuation rule applies if same-class findings recur per §8.1.1.3 (refined PMN-007 cycle).

Spec source diverges from main per PMN-006 §6.1 (e) sub-rule once any path-(a) revision lands on feature branch; future cycles paste from main, not spec, per PMN-006 §6.1.
