---
task_id: TASK-0054
title: predicate-hygiene cycle — claim-artifact-parity (§24.7), gate-current-refresh (§23.6.5), held clarifications
pr: PR-102
branch: fix/task-0054-predicate-hygiene
linked_predecessor: TASK-0053 (PR-100 squash 7502cb9 prose-currency sweep)
linked_successor: TBD
linked_pr: PR-102 (squash SHA d5473f9)
framework_version_dogfooded: AMAS v3.0.4
production_target: AMAS v3.0
spec_source: .claude/session-handoffs/TASK-0054-spec.md
date_authored: 2026-06-10
status: resolved
---

# HANDOFF: TASK-0054

## Metadata

- Task ID: TASK-0054 (matches PR-102 anticipated)
- Linked Issue: none
- Linked PR: PR-102 — URL TBD at PR-open
- Linked ADR(s): ADR-006 D3 (evidence-bar for canonicalization), ADR-008 D6 (release-track bump posture)
- Linked Feature Brief: none
- Linked review-context file: docs/reviews/PR-102-codex-pre-commit.md
- Owner role: Builder (Claude Sonnet 4.6, session context)
- Previous role: Architect (handoff direction Architect → Builder)
- Timestamp (UTC): 2026-06-10T00:00:00Z
- Last synced commit SHA: 01854d8
- Branch: fix/task-0054-predicate-hygiene
- Status: drafted
- Direction: Architect → Builder (universal handoff schema, v2.14.1 §14.1)
- Framework version: AMAS v3.0.4
- Recursive-self-instantiation salience: HIGH — this cycle modifies the canonical framework that governs this cycle's own execution (predicate-hygiene disciplines applied while the cycle executes under those disciplines)

## Objective

Predicate-hygiene cycle canonicalizing three workstreams against the AMAS v3 canonical-law trio (`core.md`, `github-reference.md`) and `templates/handoff-template.md`:

1. **WS0 (Adj-4)**: Patch bump 3.0.3 → 3.0.4 at 11 version-of-record sites per ADR-008 D6 release-track posture. Sites: 3 trio frontmatter + `README.md` + 5 `.amas/surfaces.yml` entries (`framework_version` + 4 `canonical_version`) + `AGENTS.md` + `CLAUDE.md` (positioning-line accuracy; prior-cycle precedent TASK-0052 confirmed). Gate A path-(a): initial §7.1-based exclusion reversed by Architect adjudication; Builder surface catching Architect ratification-surface error per §24.4 paired-discipline.
2. **WS1 (Adj-1)**: Canonicalize claim-artifact-parity as `### §24.7. Claim-artifact-parity` inserted after §24.6 in `core.md`. Names the cross-surface invariant already instantiated at §8.1.1.2, §24.3.1 Points 4-5, and §23.6.4. No new mechanism; naming consolidation only.
3. **WS2**: Extend `core.md` §23.6.5 empirical-grounding paragraph with TASK-0053 (PR-100) cross-cycle confirmation (gate-current handoff staleness caught at post-PR Codex review; §24.6 (B.ii) operationally-hazardous adjudication).
4. **WS3a (Adj-2)**: Rename "dual-signal" → "three-endpoint" at 4 sites: `core.md` §8.1.1 preamble + §8.1.1.1 heading; `github-reference.md` §6.3 opening breadcrumb + §8 cross-ref. `usage-guide.md` already uses "three-endpoint" language; zero edits needed there.
5. **WS3b**: Fix `core.md` §18.4 ADR-008 citations: `ADR-008:` → `ADR-008 D6:` and `ADR-008 for` → `ADR-008 D6 for`. The release-track bump posture paragraph cites D6 generically; this makes the decision-level citation explicit.
6. **WS3c (Adj-3)**: Add body-`- Status:` vs frontmatter `status:` clarification at two sites: one sentence appended to `core.md` §13.2 "Sole canonical cycle-close marker" paragraph; one new bullet in `templates/handoff-template.md` Usage notes (after "Status field lifecycle" bullet). Grounded in TASK-0053 post-PR P2 finding (gate-current handoff fields stale; §24.6 (B.ii) operationally-hazardous).

## Last completed step

Step 3 (all edits applied — WS0 through WS3c). §23.6.2 self-review in progress; Gate A staged-tree derivation pending.

## Current state

**Summary**: All 6 workstream edits applied on branch `fix/task-0054-predicate-hygiene`. Self-review in progress; pre-commit gate (Gate A) pending.

**Files authored / modified by Builder**:
1. MODIFIED `core.md` — WS0 (framework_version bump) + WS1 (§24.7 insertion) + WS2 (§23.6.5 extension) + WS3a (2 dual-signal renames) + WS3b (2 ADR-008 D6 citations) + WS3c (§13.2 sentence)
2. MODIFIED `github-reference.md` — WS0 (framework_version bump) + WS3a (2 dual-signal renames)
3. MODIFIED `usage-guide.md` — WS0 (framework_version bump)
4. MODIFIED `README.md` — WS0 (version-of-record line 9)
5. MODIFIED `.amas/surfaces.yml` — WS0 (framework_version + 4 canonical_version bumps)
6. MODIFIED `templates/handoff-template.md` — WS3c (body-Status bullet)
7. NEW `docs/handoffs/TASK-0054-predicate-hygiene.md` — this handoff
8. NEW `docs/reviews/PR-102-codex-pre-commit.md` — review-context file (to be authored at Gate A)

**Cumulative-diff-stats** (per `core.md` §23.6.1.1 (e.1) staged-tree convention):
- `git diff --staged --shortstat` returns `10 files changed, 338 insertions(+), 18 deletions(-)`
- Per-file numstat: `.amas/surfaces.yml` 5/5 · `AGENTS.md` 1/1 · `CLAUDE.md` 1/1 · `README.md` 1/1 · `core.md` 20/6 · handoff 163/0 · review-context 142/0 · `github-reference.md` 3/3 · `templates/handoff-template.md` 1/0 · `usage-guide.md` 1/1. Sum-stable: 338/18.

## Decisions made

- **Adj-1 RATIFIED**: §24.7 canonical claim-artifact-parity section inserted after §24.6 (owner-ratified 2026-06-10)
- **Adj-2 RATIFIED**: "dual-signal" → "three-endpoint" rename at 4 sites with legacy breadcrumb at github-reference.md §6.3 (owner-ratified 2026-06-10)
- **Adj-3 RATIFIED**: body-`- Status:` clarification at core.md §13.2 + handoff-template.md Usage notes (owner-ratified 2026-06-10)
- **Adj-4 RATIFIED**: patch bump 3.0.3 → 3.0.4 per ADR-008 D6 (owner-ratified 2026-06-10)
- **WS0 site count = 11 (Gate A path-(a) correction)**: initial §7.1-based exclusion of `AGENTS.md` / `CLAUDE.md` reversed by Architect Gate A adjudication — `v3.0.3` positioning line is a factual statement that is wrong at v3.0.4; §7.1 governs sync-version/template_version, not positioning accuracy. Sites: 3 trio frontmatter + `README.md` + 5 `.amas/surfaces.yml` + `AGENTS.md` + `CLAUDE.md` = 11.
- **WS2 empirical sentence**: Architect-supplied verbatim; verified against TASK-0053 P2 source at docs/reviews/PR-100-codex-pre-commit.md lines 120-131 — framing accurate (no adjustment required).

## Assumptions

- Clean working tree at pre-flight (verified: PASS)
- HEAD `01854d8` matches expected (verified: PASS)
- Branch `fix/task-0054-predicate-hygiene` regex-compliant per ADR-005 (verified: PASS)
- Codex Reviewer operational per ADR-001 D11 owner-invokes convention
- PR-102 anticipated (PR-100 = TASK-0053 main; PR-101 = TASK-0053 fix-up; PR-102 = TASK-0054 anticipated)
- §24.7 text verbatim per spec; §23.6.5 WS2 sentence Architect-supplied and source-verified; WS3c texts Architect-supplied

## §1. Cycle scope deliverables

| # | File | Change | WS |
|---|------|--------|----|
| 1 | `core.md` | framework_version: 3.0.3 → 3.0.4 | WS0 |
| 2 | `core.md` | §8.1.1 preamble: dual-signal → three-endpoint | WS3a |
| 3 | `core.md` | §8.1.1.1 heading: dual-signal → three-endpoint | WS3a |
| 4 | `core.md` | §18.4: ADR-008 → ADR-008 D6 (×2) | WS3b |
| 5 | `core.md` | §23.6.5 empirical grounding: TASK-0053 sentence appended | WS2 |
| 6 | `core.md` | §24.7 Claim-artifact-parity inserted after §24.6 | WS1 |
| 7 | `core.md` | §13.2: body-Status sentence appended | WS3c |
| 8 | `github-reference.md` | framework_version: 3.0.3 → 3.0.4 | WS0 |
| 9 | `github-reference.md` | §6.3 breadcrumb: dual-signal → three-endpoint | WS3a |
| 10 | `github-reference.md` | §8 cross-ref: dual-signal → three-endpoint | WS3a |
| 11 | `usage-guide.md` | framework_version: 3.0.3 → 3.0.4 | WS0 |
| 12 | `README.md` | v3.0.3 → v3.0.4 (line 9 version-of-record) | WS0 |
| 13 | `.amas/surfaces.yml` | framework_version + 4 canonical_version bumps | WS0 |
| 13a | `AGENTS.md` | Active framework version: v3.0.3 → v3.0.4 (path-(a) correction) | WS0 |
| 13b | `CLAUDE.md` | Active framework version: v3.0.3 → v3.0.4 (path-(a) correction) | WS0 |
| 14 | `templates/handoff-template.md` | body-Status bullet in Usage notes | WS3c |
| 15 | NEW `docs/handoffs/TASK-0054-predicate-hygiene.md` | this handoff | — |
| 16 | NEW `docs/reviews/PR-102-codex-pre-commit.md` | review-context | — |

**Explicit out-of-scope register:**
- ADR-010 / ADR-011 control-stack cluster — separate track; not touched
- §6.1 / enforcement-layer text — separate track; not touched
- M-A7 count in §18.3 — not incremented (DO NOT increment)
- `usage-guide.md` dual-signal occurrences — zero (§7.4 already uses "Three-endpoint poll")
- `AGENTS.md` / `CLAUDE.md` — IN scope; both bumped to v3.0.4 (positioning-line accuracy; §7.1-based exclusion reversed by Architect Gate A adjudication)
- Historical version references and migration notes — excluded
- `template_version` values — excluded (track template-of-record, not framework version)

## §2. Cycle gates

- **Gate A (pre-commit)**: staged-tree diff-stats + per-file numstat; §23.6.2 self-review completed before staging; Architect §24.3.1 five-point check before commit authorization.
- **Gate B (pre-push)**: post-commit SHA verification + `git status --porcelain` clean.

## §3. Step-by-step execution record

- **Step 1** (pre-flight): 10/10 PASS. HEAD `01854d8`, clean tree, branch name valid, 9 version-of-record sites classified (AGENTS.md/CLAUDE.md excluded per §7.1), TASK-0053 finding retrieved (docs/reviews/PR-100-codex-pre-commit.md lines 120-131), all old_str anchors confirmed (WS3a ×4, WS3b ×2, WS3c §13.2 anchor, WS2 §23.6.5 line 724). Step-1 stop-and-show presented; Adj-1/2/3/4 ratified by owner 2026-06-10.
- **Step 2** (branch): branch `fix/task-0054-predicate-hygiene` created from `01854d8`.
- **Step 3** (edits): WS0 (9 version sites) + WS1 (§24.7) + WS2 (§23.6.5 extension) + WS3a (4 sites) + WS3b (2 strings) + WS3c (§13.2 + handoff-template) applied.
- **Step 4** (handoff authored): this file.
- **Step 5** (§23.6.2 self-review): PASS — pass 1 clean; dual-signal grep residual zero; §24.7 cross-refs all resolved (§8.1.1.2, §23.6.4, §24.2(a), §24.3, §24.3.1, §24.4, ADR-006 D3 all confirmed present); README.md historical migration note (v3.0.3) confirmed untouched. Converged at pass 1.
- **Step 6** (Gate A + path-(a) + Codex pass-1 absorption): Gate A WS0 visible-gap surfaced; Architect reversed §7.1-based exclusion (path-(a)); AGENTS.md + CLAUDE.md bumped; WS0 corrected 9→11; diff stats stabilized 288/18/10 files. Codex pre-commit pass-1 returned REQUEST CHANGES (0 Blocking, 1 Major, 2 Minor): Major #1 path-(a) WS2 sentence replaced; Minor #1 path-(a) three residuals corrected; Minor #2 path-(β) deferred (Architect-ratified). Re-staging in progress; pass-2 required (§8.1.1.3 non-exempt — content rewrite).

## §5. Self-review record

Self-review pass 1 (2026-06-10): dual-signal grep residual check PASS (zero occurrences in any .md file); §24.7 cross-reference resolution PASS (all 7 cited targets confirmed present); version-of-record vs historical classification PASS (README.md line 11 `Adopter migration note (v3.0.3)` confirmed unchanged; AGENTS.md/CLAUDE.md in-file text intentionally not bumped per §7.1 Architect adjudication at time of self-review). Converged at pass 1. Codex pre-commit pass-1 (2026-06-10): WS2 §23.6.5 sentence source-fidelity gap caught (overstatement vs source lines 120-122); corrected at Major #1 path-(a). AGENTS.md/CLAUDE.md §7.1 exclusion was already in the process of being reversed by Architect Gate A adjudication at the time of self-review; Minor #1 residuals (pre-correction stale claims) caught at Codex pass-1 and corrected path-(a). Self-review did not catch these because the path-(a) corrections were still in progress at self-review time.

## §6. Pre-commit absorption

*(Step-6+ Codex desktop output absorption — to be populated at Gate A / post-commit.)*

## §7. Commit + push + PR-open record

*(Populated after Gate A authorization.)*

## §8. Post-PR Codex review state

*(Populated step-13+.)*

## §9. Sign-off

*(Architect §24.3.1 five-point check; populated at hand-back.)*

## §10. Cycle-close ledger

**Gate A path-(a) role-invariance instance:** Builder execution surface (Gate A WS0 visible-gap surfacing) caught an Architect ratification-surface error (§7.1 misapplication excluding AGENTS.md/CLAUDE.md from bump). Recorded as §24.4 paired-discipline catch per Architect adjudication. Non-blocking; resolved in-cycle.

**Deferred ledger item (Architect-ratified, path-(β)) — body-`Status` freeze-vs-refresh ambiguity:** WS3c text ("records the gate state at which it was written") does not settle whether the body `- Status:` snapshot freezes at drafting-time or refreshes at each gate hand-back. Open decision: the likely-correct refresh-at-gates answer cannot reach `resolved` (Action-maintained on frontmatter only), creating a logical ceiling for the body field; this would make this cycle's own freeze-at-drafting self-instantiation non-conformant — hence the cadence refinement belongs in a dedicated future cycle, not as an in-cycle bolt-on. Current §13.2 / handoff-template text is correct as written (does not mandate freeze); the cadence refinement is the deferred scope. Intentionally deferred and Architect-ratified at pre-commit pass-1 adjudication (2026-06-10); Minor #2 path-(β).

**Post-PR Codex P2 — §24.5 multi-surface catch + §24.7 self-instantiation (path-(a) class-sweep):** Post-PR Codex flagged a false zero-residual grep claim (`grep -r "dual-signal" --include="*.md" .` returns empty) in the pre-commit review-context Claim 2. The broad grep additionally returns this cycle's descriptive text (handoff + review-context WS3a descriptions) and append-only historical docs — expected out-of-scope residuals, not live canonical labels. The per-surface statements are accurate: core.md 0, usage-guide.md 0, github-reference.md exactly 1 intentional §6.3 breadcrumb. Corrected path-(a) class-sweep: pre-commit review-context Claim 2 + PR body Validation section updated to per-surface statements; §3 step record + §5 self-review record are append-only historical snapshots (not edited per §23.6.5 suppression clause). This is the §24.5 multi-surface pipeline functioning — the claim survived pre-commit pass-1 and pass-2 and was caught post-PR. It is also the strongest in-cycle empirical confirmation of §24.7's load-bearingness: the claim-artifact-parity cycle's own evidence file instantiated a claim-artifact-parity defect. **Candidate lesson:** pre-commit "grep empty" validations should run the literal command on the staged tree and read its output rather than asserting emptiness from substantive intent.

**Candidate ledger item — patch-precise version in positioning files:** Whether `AGENTS.md` / `CLAUDE.md` should carry patch-precise `v3.0.4` vs. ADR-008 D5 "v3.0 minimum-viable" major-positioning intent is an open adjudication question. TASK-0054 keeps them current as-is (per prior-cycle precedent and accuracy principle). Future cycle should adjudicate the canonical positioning convention. Not a TASK-0054 scope item.

**§24.6 Stop-Iteration override-signal — cycle-close (2026-06-10):**
- **Trigger**: post-PR pass-3, reach 3 (pass-4 terminal per §24.6 condition (A)); sub-shape = gate-current cumulative-diff-stats staleness post-fix-up (handoff `§Cumulative-diff-stats` records Gate A staged-tree snapshot while committed branch includes post-PR fix-up documentation commits).
- **Condition invoked**: (B.i) documentary — within-cycle gate artifact in evidence file; not a downstream-cycle resume input; self-referential (e.1) refresh cascade per PMN-007 §2; iterative-catch saturation at third consecutive documentary post-PR P2.
- **(B.ii) surgical fixes**: none.
- **Accepted residual + accurate value**: handoff gate-current surfaces (`§Cumulative-diff-stats`, `§Last completed step`, `§Current state Summary`) reflect the Gate A staged-tree snapshot (10 files / 338 insertions / 18 deletions). **Accurate committed-branch cumulative: 11 files changed, 524 insertions(+), 18 deletions(-).** The +1 file / +186 insertions delta is `docs/reviews/PR-102-codex-post-pr.md` (new file, 180/0) plus fix-up review-context edits in `docs/reviews/PR-102-codex-pre-commit.md` across fix-up commits `e929889` + `9caf4ee`. Recording the accurate value here satisfies claim-artifact-parity in the durable record while the labeled Gate A snapshot is accepted per (B.i).
- **Rationale**: within-cycle artifact; self-referential refresh cascade (handoff is part of its own diff); not downstream-consumed by TASK-0055 or any operative surface.

## §11. Session log archive

*(Builder session record appended at Gate B / PR-open.)*
