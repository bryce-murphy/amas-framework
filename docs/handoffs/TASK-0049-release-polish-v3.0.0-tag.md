---
task_id: TASK-0049
title: Release polish + v3.0.0 tag — final cycle of v3.0.0 per ADR-008 D2
pr: PR-89
branch: feat/task-0049-release-polish-v3.0.0-tag
linked_predecessor: TASK-0048 (PR-86 squash 0eb51f7; Part C.2 operating-discipline canonical surfaces)
linked_successor: TBD
linked_pr: PR-89 (squash SHA 0a11b84)
framework_version_dogfooded: v3.0.0
production_target: v3.0.0
spec_source: .claude/session-handoffs/TASK-0049-release-polish-v3.0.0-tag-spec.md
date_authored: 2026-06-05
status: resolved
---

# HANDOFF: TASK-0049 — Release polish + v3.0.0 tag

## Metadata

- Task ID: TASK-0049 (matches PR-89 anticipated)
- Linked Issue: none
- Linked PR: PR-89 — https://github.com/bryce-murphy/amas-framework/pull/89 (squash SHA substituted post-merge per PMN-001 (k))
- Linked ADR(s): ADR-003, ADR-006, ADR-007, ADR-008 (D2 final-slot reconciliation)
- Linked Feature Brief: none (release-polish cycle, ADR-008 D2 tracked)
- Linked review-context file: docs/reviews/PR-89-codex-pre-commit.md (phantom-corrected PR-NN→PR-89 at PR-open)
- Owner role: Builder (Claude Code, Windows / Git Bash)
- Previous role: Architect (handoff direction Architect → Builder)
- Timestamp (UTC): 2026-06-05T12:56:14Z
- Last synced commit SHA: 7e2ee62 (main HEAD at pre-flight)
- Branch: feat/task-0049-release-polish-v3.0.0-tag
- Status: active
- Direction: Architect → Builder (universal handoff schema, core.md §14.1)
- Framework version: v3.0.0 (this cycle's bump target)
- Recursive-self-instantiation salience: MEDIUM (per spec §0; version-bump propagation discipline = PMN-019 §2.(v) grep-enumerated bidirectional sweep, baked in as authoring-time input)

## Objective

Ship AMAS v3.0.0 as the final cycle of the v3.0.0 minimum-viable canonical framework per ADR-008 D2 "release polish + v3.0.0 tag" slot. **Polish, not materialization** — no new canonical disciplines; the Part C.2 logic frozen at TASK-0048 is untouched. Three deliverable classes: (a) the §3 grep-enumerated bidirectional version-currency sweep + classification ledger; (b) three `core.md` canonical currency edits (§18.3 M-A7 36th + span; §18.4 drop "(anticipated)"), staged + Gate-A-gated; (c) README finalization + AGENTS.md/CLAUDE.md currentness flips. The v3.0.0 annotated tag is an owner post-merge action (§8), not a Builder deliverable.

## Last completed step  *(GATE-CURRENT — pre-commit / Codex-desktop-pre-commit-approach state)*

§4 canonical edits authored + STAGED; Architect Gate-A FINAL CLEAR received (canonical `core.md` change ratified after three path-(a) refinements R1/R2/R3 + confirmations C-a/C-b). This handoff + the PR-NN review-context authored next; then owner-invoked Codex desktop pre-commit. No commit/push yet.

## Current state  *(GATE-CURRENT — re-derive (e.1) at each staged-tree mutation)*

**Summary**: On branch `feat/task-0049-release-polish-v3.0.0-tag` off `main@7e2ee62`. The four canonical-currency surfaces (README.md, AGENTS.md, CLAUDE.md, core.md) are staged with a balanced 1-for-1 substitution diff. This handoff + the review-context add the two cycle artifacts to the staged tree. Stage-only — no commit, no push, no PR. Codex desktop pre-commit is the next gate (RELAY-ORDERING: this is the pre-commit pass; the binding post-PR re-review comes AFTER PR-open + any finding-addressing push).

**Files modified / authored by Builder**:
1. MODIFIED `README.md` — Status (L7), version-positioning note (L9), reading order (L26), Roadmap paragraph (L30), Contributing currency de-couple (L131)
2. MODIFIED `AGENTS.md` — active-framework-version (L9) + repository-status (L11) currentness flips
3. MODIFIED `CLAUDE.md` — active-framework-version (L9) + repository-status (L11) currentness flips
4. MODIFIED `core.md` — §18.3 M-A7 preamble (L584) + enumeration tail (L586) + count phrase (L588); §18.4 example flip (L600)
5. NEW `docs/handoffs/TASK-0049-release-polish-v3.0.0-tag.md` — this handoff
6. NEW `docs/reviews/PR-NN-codex-pre-commit.md` — review-context + §6 verification battery

**Cumulative-diff-stats** (per `core.md` §23.6.1.1 (e.1) + §23.6.5 reference-volatile-by-pointer — total NOT pinned here; re-derive at each staged-tree mutation):
- Re-derive: `git diff --cached --shortstat` and `git diff --cached --numstat`.
- The four canonical-currency surfaces carry a balanced substitution (per-file ins == del; net line growth 0 across that subset). The two cycle artifacts (this handoff + review-context) are net-additive — re-derive for the live total rather than trusting any pinned figure (a pinned total would be invalidated by this artifact's own addition).

## Decisions made

- **Adj 1 (version tier)**: v2.45 → **v3.0.0 MAJOR** per `core.md` §18.4 (v3.0.0 = the named major-bump example).
- **Adj 2 (surface methodology)**: repo-wide grep token-enumeration over the §3.1 token set; each hit classified `{bump | leave-already-correct | leave-historical}`; bidirectional; metadata class explicitly enumerated (PMN-019 §2.(v)).
- **Adj 3 (canonical edits, Gate-A-gated)**: three `core.md` currency edits staged + Architect Gate-A re-clear before commit/push (canonical-change-no-self-push). FINAL CLEAR received.
- **Gate-A R1**: §18.4 example scope authority = ADR-008 (not "ADR-003 + ADR-008"); no tag-existence claim.
- **Gate-A R2**: README L131 Contributing de-coupled from the now-occurring v3.0 publication to future-release framing (path-(a) currency de-coupling).
- **Gate-A R3**: `core.md` M-A7 term staged as literal `PR-NN` in BOTH §4.1 preamble and enumeration tail; manual PMN-001 (k) substitution at the post-merge chore. "36 consecutive" / "through v3.0.0" kept concrete. Review-context filename carries the same `PR-NN` literal (no linked-pr-fix-up Action constraint applies to it). Handoff frontmatter `pr`/`linked_pr` carry numeric `PR-89` (anticipated) because the linked-pr-fix-up Action regex `PR-(\d+)` requires a numeric token (PR-NN would silently skip substitution).
- **Gate-A C-a (confirmed)**: no release-polish / v3.0.0-tag row exists in the README package-layout tables — nothing to rotate.
- **Gate-A C-b (confirmed)**: README Status preserves the full four-ADR chain (ADR-003 + ADR-006 + ADR-007 + ADR-008); not narrowed.
- **Anti-scope (hard)**: no stub fills; no `roadmap_status` changes; no Part C.2 surface edits beyond version-string currency; no historical-snapshot edits; no Actions/appendix/adapter work; no new ADR; no in-repo CHANGELOG; Builder does NOT create/push the v3.0.0 tag (owner action, §8). 28 deferred-stub `[v3.1-planned]`/`[v3.2-planned]` annotations UNCHANGED.

## Assumptions

- Entry anchor `main@7e2ee62`; working tree clean at entry (verified at pre-flight §8.2).
- Codex Reviewer operational (desktop pre-commit + GitHub-App post-PR) per ADR-001 D11 owner-invokes.
- PR-89 anticipated (highest merged = 88 at authoring per live `gh pr list --state all`); phantom-correct at PR-open.
- Owner runs squash-merge (admin-bypass per ADR-001 D9 / §10.5) and creates the v3.0.0 annotated tag post-merge.

## Risks

- **PR-number drift**: if a PR opens ahead of PR-89, the anticipated number is stale — mitigated by PMN-001 (k) phantom-correct at PR-open against live state, and by the `PR-NN` literal in canonical/review surfaces.
- **Tag-timing semantics**: committed prose says "published from this repository" (state-as-complete-at-commit per §23.6.4); the annotated tag is the owner's immediately-following post-merge marker. No surface asserts the tag exists/was pushed (Gate-A R1 + judgment-call-1 ratified).

## Blocking questions

None outstanding. Gate-A FINAL CLEAR resolved the three refinements + two confirmations.

## Validation run

See §6 of the review-context (`docs/reviews/PR-NN-codex-pre-commit.md`) for the named verification battery. Builder-side at authoring:
- `git diff --cached --shortstat` / `--numstat` — re-derive (e.1).
- Bidirectional close: `git ls-files | xargs grep -nE 'v2\.45'` → zero hits outside `docs/{adr,post-merge-notes,handoffs,reviews}/` (all residual leave-historical).
- core.md §4 same-class sweep: `grep -nE "= 35|35 consecutive|v2\.45|\(anticipated;|PR-89" core.md` → zero (no stale currency form, no anticipated-qualifier, no phantom PR-89 literal in core.md).

## §3. Step-by-step execution record  *(APPEND-ONLY HISTORICAL — never back-refreshed; volatile state by pointer per §23.6.5)*

- **Step 1 (pre-flight §8.2)**: entry anchor `git rev-parse main` = 7e2ee62 (≈ spec); `git status --porcelain` clean; `git ls-files docs/handoffs/ | grep TASK-0049` empty (reservation clear); live `gh pr list --state all` highest merged = 88 (PR-89 anticipated); entry canon confirmed (README v2.45; core.md §18.3 `= 35` / "35 consecutive" / "as of v2.45 … PR-86 / TASK-0048"; §18.4 "(anticipated)").
- **Step 2 (branch)**: `git checkout -b feat/task-0049-release-polish-v3.0.0-tag` off main.
- **Step 3 (§3 sweep + ledger)**: ran §3.1 token greps over `git ls-files`; built the §3.3 classification ledger (embedded below). Every hit classified `{bump | leave-already-correct | leave-historical}`; historical hits classified explicitly (not silently excluded).
- **Step 4 (§5 edits)**: applied README L7/L9/L26/L30 + AGENTS L9/L11 + CLAUDE L9/L11 currency/positioning flips (operational/discipline body untouched; 28 deferred-stub annotations unchanged).
- **Step 5 (§4 edits, stage-only)**: applied core.md L584/L586/L588/L600; ran §4 same-class stale-form sweep (clean); staged all.
- **Step 6 (§4 stop-and-show → Gate A)**: handed back to owner→Architect with the §3.3 ledger, staged-diff envelope by pointer, bidirectional-close result, (XVII) 3-axis sum-stability.
- **Step 7 (Gate-A conditional clear)**: applied R1 (§18.4 ADR-008-only scope), R2 (README L131 de-couple), R3 (core.md M-A7 → `PR-NN` both sites); confirmed C-a (no package-layout row) + C-b (four-ADR chain intact); re-staged; re-derived envelope/bidirectional/3-axis; handed back.
- **Step 8 (Gate-A FINAL clear)**: canonical core.md change ratified. Authored this handoff + the PR-NN review-context; staged.
- **Step 9 (NEXT — owner-invoked Codex desktop pre-commit)**: owner pastes the §Codex-desktop-pre-commit-kickoff prompt; Codex runs the §6 battery; output absorbed verbatim into the review-context.
- **Step 10+ (NEXT)**: Gate A (staged) → commit/push/PR-open (phantom-correct PR number + SHAs per PMN-001 (k)) → Codex post-PR (three-endpoint poll §8.1.1.1) → Gate B → owner squash-merge → PMN-001 (k) chore-fix-up (substitute squash SHA across handoff `pr`/`linked_pr`, review-context, the core.md §4.1 `PR-NN` term) → owner v3.0.0 annotated tag (§8) → cycle-close ledger.

### §3.3 classification ledger (grep-enumerated, bidirectional — PMN-019 §2.(v))

**BUMP (12 changed lines / 4 files)** — currency assertions flipped to v3.0.0-published:

| path:line | token(s) | reason |
|---|---|---|
| README.md:7 | "under active development" / "is in production" | §5.1 Status + primary-positioning → published-state |
| README.md:9 | `v2.45`, "Until v3 publishes", "adopters should reference" | §5.1 version-positioning note → v3.0.0 |
| README.md:26 | "Once v3 ships:" | §5.1 reading-order → shipped framing |
| README.md:30 | "only release polish + the v3.0.0 tag (TASK-0049) remains" + "(TASK-0049 or per actual cycle-count)" | §5.1 Roadmap currency (ADR-006 D4 / ADR-007 single-paragraph precedent) |
| README.md:131 | "guidelines will land alongside v3.0 publication" | Gate-A R2 currency de-couple → future-release framing |
| AGENTS.md:9 | `v2.45`, "in development" | §5.2 active-version currentness flip |
| AGENTS.md:11 | "in active production", "in progress", "after v3.0.0 ships" | §5.2 repo-status currentness flip |
| CLAUDE.md:9 | `v2.45`, "in development" | §5.2 active-version currentness flip |
| CLAUDE.md:11 | "in active production", "in progress" | §5.2 repo-status currentness flip |
| core.md:584 | `v2.45` ("as of v2.45 … PR-86 / TASK-0048") | §4.1 preamble → v3.0.0 / PR-NN / TASK-0049 |
| core.md:586 | `= 35` + "spanning v2.16 through v2.45" | §4.1 enumeration tail (`+ PR-NN = 36`) + §4.2 span (→ v3.0.0) |
| core.md:588 | "35 consecutive substantive cycles" | §4.1 count phrase → 36 |
| core.md:600 | "v3.0.0 (anticipated; …)" | §4.3 example flip → realized-state, ADR-008-amended scope (R1) |

*(README counts as 5 changed lines, core.md as 4; AGENTS/CLAUDE 2 each = 13 changed lines.)*

**LEAVE-ALREADY-CORRECT** (carry 3.0.0 by design; not currency assertions):
- `framework_version: 3.0.0` — trio frontmatter `core.md:2` / `github-reference.md:2` / `usage-guide.md:2`; + YAML-manifest-example content `github-reference.md:327`, `prompts/deep-research-design-brief.md:71`
- `template_version: 3.0.0` — 50 files (templates/ + appendices/ + actions/ + prompts/ frontmatter & YAML comments)
- `amas_version: 3.0` — 7 receiving-surface adapter packs
- `canonical_version: <version>` — 2 (`surfaces-manifest-template.yml` placeholder w/ illustrative "e.g., v2.30" comment)
- `core.md:594` version-sequence "v2.14.1, v2.15, v2.16, v3.0.0, …" (structural, not currency); `core.md:434` + `README.md:34` prose describing the versioning convention (field names, no literal)
- `prompts/greenfield.md:171`, `prompts/retrofit.md:203` forward-refs ("after v3.0.0 release the release tag / README version-positioning governs") — by design; resolve on the README L9 flip; spec §5.1 → no edit
- `prompts/research-deliverable.md:156/172/181/420` "in production" — sample research-deliverable prose, not a framework-version assertion

**LEAVE-HISTORICAL** (correct-by-design pinned snapshots — classified explicitly, not excluded):
- `v2.45` residuals: `docs/handoffs/TASK-0048-…` (6), `docs/post-merge-notes/PMN-019-…` (2), `docs/reviews/PR-86-…` (2) — pinned cycle/PMN/review snapshots
- `framework_version_dogfooded:` — 134 hits across `docs/handoffs/` + `docs/post-merge-notes/`, per-cycle dogfood records pinned to each cycle
- `core.md:586` historical PR enumeration members (PR-9 … PR-86) + "PR-13 / v2.16" + "post-v2.16" — M-A7 empirical-grounding instances, historical-by-design (members stay; only tail/count/span/preamble are bump)
- `docs/features/FEAT-0001-…:9` "AMAS v3.0 (in production via PR-2 through PR-8)" — historical scaffold-feature snapshot
- bulk `v3.0.0` hits across `docs/adr/`, `docs/handoffs/`, `docs/reviews/` (majority of 101 repo-wide v3.0.0 hits) — historical artifacts

**Bidirectional close**: (a) every bump-bucket surface reads v3.0.0 after edits; (b) zero `v2.45` currency-laggard in any canonical-law / root / template / prompt surface (`git grep --cached 'v2\.45' -- core.md README.md AGENTS.md CLAUDE.md github-reference.md usage-guide.md templates/ prompts/` empty). Residual `v2.45` is confined to `docs/{adr,post-merge-notes,handoffs,reviews}/` — pinned historical snapshots **plus this cycle's own documentary references** (this handoff's ledger + the PR-NN review-context describing the flip); those per-dir counts are self-volatile (the cycle's artifacts add to them) and referenced by pointer per §23.6.5, **not pinned**. No `v2.45` remains as an unclassified currency-laggard. *(A prior draft pinned "full-repo residual = 10"; invalidated by these very artifacts — Codex pre-commit Minor, absorbed path-(a).)*

## §10. Cycle-close ledger  *(APPEND-ONLY HISTORICAL — populated at cycle close)*

*(Populated at cycle close: M-A7 36th-instance reconciliation with verified PR + squash SHA; (XVII)/(XXVI) cross-cycle data points; v3.0.0 ship + tag SHA record; any PMN candidates. Pending post-merge.)*

## §11. Session log archive  *(§13.1 in-cycle records; current set per §13.2 in PR body)*

### Builder session — Claude Code (Windows / Git Bash) — 2026-06-05

- Pre-flight §8.2 + branch + §3 sweep/ledger + §5/§4 edits (stage-only) + §4 stop-and-show; Gate-A conditional clear absorbed (R1/R2/R3 + C-a/C-b); Gate-A FINAL clear; handoff + PR-NN review-context authored + staged. Next: owner-invoked Codex desktop pre-commit.
