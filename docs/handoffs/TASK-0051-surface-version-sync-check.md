---
task_id: TASK-0051
title: surface-version-sync-check Action materialization (first v3.1 Batch-P4 Action)
pr: PR-95
branch: feat/task-0051-surface-version-sync-check
linked_predecessor: TASK-0050 (PR-92 squash 265d2a8; surfaces.yml schema reconciliation + release-track posture)
linked_successor: TBD
linked_pr: PR-95 (Builder fills with squash SHA post-merge per PMN-001 (k))
framework_version_dogfooded: AMAS v3.0.2
production_target: AMAS v3.1
spec_source: .claude/session-handoffs/amas-cycle-kickoff-task0050-surface-version-sync-check.md + TASK-0051 re-kick directive (deltas + correction)
date_authored: 2026-06-07
status: active
---

# HANDOFF: TASK-0051 — surface-version-sync-check Action materialization

## Metadata

- Task ID: TASK-0051 (matches PR-95)
- Linked Issue: none
- Linked PR: PR-95 (squash SHA substituted post-merge per PMN-001(k))
- Linked ADR(s): ADR-008 (D4 v3.1 Batch-P4 roadmap; D6 release-track bump posture — this cycle bumps patch v3.0.1 -> v3.0.2 intra-v3.1-track)
- Linked Feature Brief: none (materialization cycle per ADR-008 D4 v3.1 enablement track)
- Linked review-context file: docs/reviews/PR-95-codex-pre-commit.md
- Owner role: Builder (Claude Code, Windows)
- Previous role: Architect (handoff direction Architect -> Builder)
- Timestamp (UTC): 2026-06-07
- Last synced commit SHA: 962a8ae (main HEAD at pre-flight; PR-94 TASK-0050 close-reconciliation)
- Branch: feat/task-0051-surface-version-sync-check
- Status: active
- Direction: Architect -> Builder (universal handoff schema, core.md §14.1)
- Framework version: AMAS v3.0.2 (patch bump; intra-v3.1-track per ADR-008 D6)
- Recursive-self-instantiation salience: MEDIUM (the manifest self-entry tracks the very Action that reads it — circularity guarded by version-equality; see §10)

## Objective

Materialize the first v3.1 Batch-P4 deterministic Action: fill the
`actions/surface-version-sync-check.yml` stub with a working surface-version
currency check against `.amas/surfaces.yml` per `github-reference.md`
§7.1/§7.2/§7.3, instantiate it operationally (advisory), and author the
populated dogfood manifest the Action validates. This retires the manual
grep-sweep stopgap for surface-version drift. The Action proves declared
template-version CURRENCY against the template-of-record — NOT byte/content
parity (explicit §7.2 non-goal).

Deliverable classes (D1-D8): (D1) materialize canonical Action; (D2) author
`.amas/surfaces.yml`; (D3) operational advisory workflow; (D4) §7.1 example
one-liner (Codex PR-92 [C2] resolution); (D5) stale-version negative fixture;
(D6) currency bump v3.0.1 -> v3.0.2 (trio frontmatter x3 + in-development
markers, two-concept discipline); (D7) M-A7 §18.3 37 -> 38; (D8) this handoff +
PR-NN review-context.

## Last completed step

All ten surfaces staged (`git add -A`); §6 verification battery run on reliable
primitives (sed / grep -nE; the Action's check logic live-run against both the
real manifest [PASS] and the stale fixture [FAIL]); this handoff + PR-NN
review-context authored + staged. **Next: Gate-A stop-and-show — HAND BACK.**
No commit; no push; no PR. Four canonical-law-trio edits (D4 §7.1, D6 x3
frontmatter, D7 §18.3) flagged for Architect Gate-A re-clear.

## Current state

**Summary**: On branch `feat/task-0051-surface-version-sync-check` off
`main@962a8ae`. Ten surfaces staged (4 new, 6 modified). No commit; no push.
Gate-A stop-and-show is the immediate next action.

**Files modified / authored by Builder**:
1. MODIFIED `actions/surface-version-sync-check.yml` — stub -> filled canonical Action; `# template_version: 3.0.0` RETAINED (NOT bumped — see D1 / §10); status stub -> recorded; filled_by PR-NN (TASK-0051)
2. NEW `.amas/surfaces.yml` — populated dogfood manifest (5 surface entries; self-entry declares 3.0.0 with circularity-guard comment)
3. NEW `.github/workflows/surface-version-sync-check.yml` — operational advisory instantiation (NOT a required status check, per F3)
4. MODIFIED `github-reference.md` — §7.1 example `agents: [claude, codex]` -> `[codex]` (D4); frontmatter v3.0.1 -> v3.0.2 (D6)
5. NEW `actions/fixtures/surface-version-sync-check/stale-manifest.yml` — negative fixture (D5)
6. MODIFIED `core.md` — frontmatter v3.0.2 (D6); §18.3 M-A7 37 -> 38 + span v3.0.2 + PR-NN + TASK-0051 (D7)
7. MODIFIED `usage-guide.md` — frontmatter v3.0.2 (D6)
8. MODIFIED `README.md` — L9 in-development marker v3.0.2 (D6; v3.0.0 published preserved)
9. MODIFIED `AGENTS.md` — L9 in-development marker v3.0.2 (D6)
10. MODIFIED `CLAUDE.md` — L9 in-development marker v3.0.2 (D6)
11. NEW `docs/handoffs/TASK-0051-surface-version-sync-check.md` — this handoff
12. NEW `docs/reviews/PR-NN-codex-pre-commit.md` — review-context + §6 battery

**Cumulative-diff-stats** (per core.md §23.6.1.1 (e.1) — re-derive at each staged-tree mutation):
- Re-derive: `git diff --cached --shortstat` and `git diff --cached --numstat`.
- Pre-D8 staged total: `10 files changed, 398 insertions(+), 16 deletions(-)`. The two cycle artifacts (this handoff + review-context) are net-additive; re-derive for the live total rather than trusting a pinned figure.

## Decisions made

- **D1 (template_version STAYS 3.0.0 — Architect-locked correction)**: the Action's own `# template_version` is NOT bumped to 3.0.1. Per `core.md` §17.5, `template_version` bumps only on material content change to an already-filled template; this is a stub -> fill (initial materialization at the 3.0 major baseline), controlled by the greenfield/retrofit/upgrade precedent that kept `template_version: 3.0.0` through materialization. The manifest sync-check self-entry also declares 3.0.0 (kept equal so the Action passes when checking itself). This REVERSES a carried-forward "bump to 3.0.1" decision from a prior session.
- **D2 (manifest coverage)**: 5 entries — `AGENTS.md`, `CLAUDE.md`, `pr_template`, `surfaces_manifest`, sync-check self-entry. `surfaces_manifest` declares 3.0.1 (its template-of-record was revised at TASK-0050); all others 3.0.0. EXCLUDES `.github/workflows/linked-pr-fix-up.yml` (no template-of-record under `actions/`; shipped operationally at PR-21 per ADR-004).
- **D4 (§7.1 example fix)**: resolves Codex PR-92 [C2] (P3, carried forward) — AGENTS.md is the Codex receiving surface, so the worked example reads `agents: [codex]`, not `[claude, codex]`.
- **D6 (currency bump v3.0.2)**: patch bump per ADR-008 D6 release-track posture (intra-v3.1-track). Two-concept discipline: only the in-development version bumps; v3.0.0-published references preserved; no "published" clause attaches to v3.0.2 (the PR-92 [F1] defect class). The §7.1 example block (github-reference.md:327/336/342) legitimately retains `3.0.1` as example content — D6's zero-residual battery scopes to frontmatter + in-development markers only.
- **D7 (M-A7 INCLUDE — 38th)**: TASK-0051 materializes a canonical Action — substantive, not a defect-fix or chore exclusion. `= 38`, "38 consecutive", span v2.16 through v3.0.2, preamble "as of v3.0.2 canonicalization at PR-NN / TASK-0051". PR-NN literal through the substantive squash; resolved via PMN-001(k) at the post-merge chore.

## Builder-reconstructed elements (FLAGGED for Architect Gate-A confirmation)

The full TASK-0051 Builder D1-D8 contract was not present in the Builder
session context; the re-kick supplied deltas + the D1 correction. The following
were reconstructed from canonical spec (§7.1/§7.2/§7.3) + anti-scope + precedent
and REQUIRE Architect confirmation:

- **D1 resolution mechanism**: surface->template-of-record resolved by canonical `name` convention (AGENTS.md/CLAUDE.md/pr_template/surfaces_manifest -> `templates/...`; any other name -> `actions/<name>.yml`); version markers read with grep/sed; SELF/VENDORED vs ADOPTER mode guard (adopter mode emits non-passing, never silent pass) keyed on presence of `templates/` + `actions/`. Env overrides `AMAS_REFERENCE_ROOT` + `AMAS_SURFACES_MANIFEST` added for vendoring + fixture testability.
- **D3 form**: operational mirror of the canonical Action (per §6.2 canonical-source -> operational mirror), advisory (not wired as required status check, F3).
- **D5 location**: `actions/fixtures/surface-version-sync-check/stale-manifest.yml` (declares AGENTS.md at stale 2.14.1 + a current control entry).
- **D7 "(XXI) cluster" label**: the re-kick referenced "the (XXI) cluster"; the actual M-A7 count region is core.md §18.3 lines 584/586/588 (no "(XXI)" anchor there — "(XXI)" appears only at core.md:783 in a PMN-012 §3.4 context). Edited 584/586/588; confirm this is the intended target.
- **roadmap_status / README [v3.1-planned]**: the Architect cycle kickoff flagged "whether materializing ONE Action flips its roadmap_status / README [v3.1-planned] annotation now or holds until the v3.1 release" as a genuine scoping decision. NOT pre-decided: the Action retains `# roadmap_status: v3.1-planned` and README L84 retains `[v3.1-planned]`. Confirm hold-vs-flip.

## Assumptions

- Entry anchor `main@962a8ae` (PR-94 TASK-0050 close-reconciliation); working tree clean at entry (verified at pre-flight §8.2); open PRs empty; M-A7 reads PR-92 / 37 at entry.
- Next PR ~PR-95 (highest merged = 94 at authoring; live-bind at PR-open per FX-B / PMN-019 F1).
- SELF mode applies in the dogfood repo (templates/ + actions/ present at root), so every template-of-record resolves locally and the live Action passes on the current manifest.
- No live v3 adopter has instantiated the v3 surfaces manifest, so the new manifest + Action have no live-adopter breakage.

## Risks

- **PR-number drift**: anticipated number stale if a PR opens ahead — mitigated by PR-NN literal + FX-B phantom-correct at PR-open.
- **Reconstruction divergence**: the D1 resolution mechanism / D3 form / D5 location are Builder-reconstructed; if they diverge from the Architect's intended contract, rework lands at Gate A (nothing committed). Flagged above.
- **Circularity**: the self-entry tracks the Action that checks it — guarded by declaring the self-entry version equal to the Action's own marker (3.0.0). Logged §10.

## Blocking questions

1. Confirm the five Builder-reconstructed elements above (D1 mechanism, D3 form, D5 location, D7 "(XXI)" target, roadmap_status hold-vs-flip).
2. Confirm the four canonical-law-trio edits (D4 §7.1, D6 x3 frontmatter, D7 §18.3) for Gate-A re-clear before commit.

## Validation run

See §6 of the review-context (`docs/reviews/PR-NN-codex-pre-commit.md`) for the
named verification battery (claims 1-N). Builder-side live evidence at
authoring:
- `git diff --cached --shortstat` -> `10 files changed, 398 insertions(+), 16 deletions(-)` (pre-D8; re-derive live).
- Action check live-run, real manifest: all 5 surfaces `[ OK ]`, `RESULT=PASS(0)`.
- Action check live-run, stale fixture (`AMAS_SURFACES_MANIFEST=actions/fixtures/.../stale-manifest.yml`): AGENTS.md `[FAIL] 2.14.1 != 3.0.0`, CLAUDE.md `[ OK ]` (control), `RESULT=FAIL(1)`.
- `grep -c 'agents: \[claude, codex\]' github-reference.md` -> `0`; `grep -c 'agents: \[codex\]'` -> `1` (D4).
- `grep -nE '^framework_version: 3\.0\.2' core.md github-reference.md usage-guide.md` -> 3 lines (D6).
- Attachment predicate `v3\.0\.2[^.;]*publish|publish[^.;]*v3\.0\.2` across canonical surfaces -> empty (no "published" on v3.0.2).
- `grep -cE '\+ PR-92 \+ PR-NN = 38' core.md` -> `1`; `grep -c '38 consecutive substantive cycles' core.md` -> `1` (D7).

## §3. Step-by-step execution record *(APPEND-ONLY HISTORICAL — never back-refreshed)*

- **Step 1 (pre-flight §8.2)**: `git rev-parse main` = `962a8ae`; `git status` clean; `gh pr list --state open` empty; no `docs/handoffs/TASK-0051-*`; M-A7 reads `PR-92 / = 37 / 37 consecutive` (entry baseline).
- **Step 2 (branch)**: `git switch -c feat/task-0051-surface-version-sync-check` off `962a8ae`.
- **Step 3 (author D1-D7, stage-only)**: materialized the Action (D1; template_version 3.0.0 retained); authored manifest (D2) + advisory workflow (D3) + negative fixture (D5); §7.1 one-liner (D4); frontmatter x3 + in-development markers v3.0.2 (D6); M-A7 37 -> 38 (D7).
- **Step 4 (§6 battery)**: ran on reliable primitives; live-ran the Action check against real manifest (PASS) + stale fixture (FAIL).
- **Step 5 (D8 cycle artifacts)**: authored this handoff + PR-NN review-context; staged.
- **Step 6 (NEXT — Gate-A stop-and-show)**: HAND BACK with staged-diff envelope, battery results, four canonical edits flagged + five reconstructed elements flagged. No commit until Architect Gate-A clear.

## §9. Sign-off *(Architect populates at hand-back per core.md §24.3.1)*

TBD — populated at Architect Gate-A re-clear.

## §10. Cycle-close ledger

**Bump adjudication.** v3.0.1 -> v3.0.2 PATCH per ADR-008 Decision 6 release-track bump posture (intra-v3.1-track; the aggregate v3.1.0 minor fires once at v3.1 release when all 9 Actions ship). Two-concept currency: in-development version only; v3.0.0-published preserved.

**M-A7.** 38th instance = PR-NN (INCLUDE). Materializing a canonical Action is substantive. §18.3 amended to `+ PR-92 + PR-NN = 38`, "38 consecutive substantive cycles", span v2.16 through v3.0.2, preamble "as of v3.0.2 canonicalization at PR-NN / TASK-0051". PR-NN carried literal through the substantive squash; resolved via PMN-001(k) at the post-merge chore.

**Materialization.** First v3.1 Batch-P4 Action filled. Reads the exact `surfaces:` list-form schema TASK-0050 reconciled (no second-order schema ambiguity). Currency-not-parity honored: comparison is manifest-declared vs template-of-record, coarse/major-aligned per §17.5; optional `.yml`-marker cross-check advisory only.

**Circularity guard.** The manifest self-entry tracks the operational instantiation of the Action that performs the check. Declaring the self-entry `template_version: 3.0.0` equal to the Action's own `# template_version: 3.0.0` marker keeps the Action passing on itself — no circular self-fail.

**Anti-scope held.** No second Action materialized; no `prompts/` edits (deep-research-design-brief map-form schema carry-forward NOT swept this cycle); no canonical §6 battery-template repair; only `surface-version-sync-check.yml` (canonical + operational) touched under Actions/workflows.

**Carry-forward.**
- `prompts/deep-research-design-brief.md` map-form schema (TASK-0050 R3 carry-forward) — still deferred; not in this cycle's scope.
- Promote the advisory workflow to a required status check (F3 deferral) at a later cycle.
- Reconstructed-contract elements (§Builder-reconstructed) pending Architect confirmation.

## §11. Session log archive *(§13.1 in-cycle records; current set per §13.2 in PR body)*

### Builder session — Claude Code (Windows) — 2026-06-07

Re-verified pre-flight live items (base_sha 962a8ae; open PRs empty; M-A7 PR-92/37); branched; surfaced missing Builder D1-D8 contract and proceeded on reconstruction path under standing GO + hard Gate-A backstop; authored D1-D8 from canonical spec + re-kick deltas + correction; ran §6 battery incl. live Action runs (PASS on real manifest, FAIL on stale fixture); authored cycle artifacts. Next: Gate-A stop-and-show / hand back.
