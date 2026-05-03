# PR-19 Codex desktop pre-commit review context

## Metadata

- PR ID: PR-19
- TASK ID: TASK-0018
- Branch: chore/task-0018-pmn-008-pr-17-cycle-learnings
- Base SHA: 52ee07e84628a2d8e5a8ffbf5d1dc6e22b2b35b0 (squash-merge of PR-18 chore on main, 2026-05-03)
- Builder: Claude Code (Claude Opus 4.7)
- Reviewer: Codex (GPT-5.5) — desktop, pre-commit, untracked working tree
- Architect (this PR's): Claude Opus 4.7 (Claude.ai Project)
- Owner: Bryce Murphy (`@bryce-murphy`)
- Framework version: AMAS v2.17 (dogfooded per CLAUDE.md active framework version; PMN-008 cycle does not bump framework_version — pure post-merge-note authoring; no canonical-text changes)
- Severity taxonomy: Blocking / Major / Minor (three-level; per repo discipline; standing per PMN-004 §5 (a))
- Disciplines applied (PMN-004 §5 (a)-(f) + PMN-005 sub-rule (e.1) + PMN-006 (g)/(h)/(i) + PMN-006 §5.3 bounded-continuation rule generalized + PMN-006 §3.4 frontmatter-vs-body sub-clause + PMN-007 §2.4 cost-class refinement with genuinely-asymptotic-vs-pure-token-swap distinction + PMN-007 §3.1 four-surface iterative-pre-flight + iterative-post-PR-review pattern + PMN-007 §9.1 (i) extended pre-authoring verification batch + **PMN-008 §3.2 five-surface review pipeline (canonicalized this cycle)** + **PMN-008 §4.2 (i.5) convention-inference verification with PMN-file-shape sub-extension (canonicalized this cycle)**): severity taxonomy three-level (a); verification-command portability (b); no future-tense pre-commit claims (c); pre-commit cross-surface scope clarity (d); §23.6 prose-arithmetic decomposition (e) with sub-rule (e.1) cumulative-diff-stats re-derivation; section-citation correctness sweep (f); verification-artifact internal consistency (g); verification-command operational correctness (h) with sub-shapes (h.1)/(h.2)/(h.3); cross-document state verification (i) with sub-shapes (i.1)/(i.2)/(i.3)/(i.4)/(i.5); §23.6.2 iterative-to-fixed-point self-review; §8.1.1.3 bounded-continuation rule with cost-class refinement.
- Recursive-self-instantiation: PR-19 canonicalizes (in PMN-008) the (r) Builder step-6 self-review fifth surface and (i.5) convention-inference verification disciplines. Builder PR-19 self-review surfaced **eight defects in PMN-008 itself** across three sweep passes before commit — three §-content defects (Pass 1 step-1 pre-flight) plus four frontmatter/structure convention-inference defects (Pass 2 step-1 pre-flight per (i.5) PMN-file-shape sub-extension) plus one §-citation residual (Pass 3 Builder step-6 (j) sweep post-authoring; PMN-007 §6 (p) → §8.2 (p) correction propagated from spec into deliverables). All eight path-(a) routed (Pass 1 + Pass 2 via Architect spec-authoring revisions; Pass 3 via Builder inline edit). The disciplines PMN-008 canonicalizes self-applied within PMN-008's own authoring cycle to catch defects that escaped Architect §23.6 single-iteration sweep, including operating at the canonical step-6 surface specified in PMN-008 §3.1. (k.1) positive empirical confirmation at maximum strength; (v) candidate observation registered at PMN-008 §5.7.

## Builder claims to verify

The Builder asserts the following at hand-off to Codex desktop pre-commit review. Each claim is verifiable from the working tree at pre-commit time (no future-tense claims per PMN-004 §5 (c)). PR-19 is a pure post-merge-note authoring cycle (PMN-008 + TASK-0018 handoff + PR-19 review-context); no canonical-text changes.

1. **Tracked-file count on feature branch post-Builder-commit** = 101 (98 base + 3 new files: PMN-008 + TASK-0018 handoff + PR-19 review-context). Pre-commit-verifiable per (c) discipline.
   - bash: `git ls-files | wc -l` returns `101` on feature branch post-staging
   - PowerShell: `(git ls-files | Measure-Object -Line).Lines` returns `101`

2. **PMN-008 top-level §-header count** = 7 (§1-§7). Verifiable at pre-commit:
   - bash: `grep -cE "^## §[0-9]+\." docs/post-merge-notes/PMN-008-pr-17-cycle-learnings.md` returns `7`
   - PowerShell: `(Select-String -Path docs/post-merge-notes/PMN-008-pr-17-cycle-learnings.md -Pattern '^## §[0-9]+\.').Count` returns `7`

3. **PMN-008 §1.1 honesty record enumerates 8 defects across 3 sweep passes** (3 §-content defects in Pass 1 step-1 pre-flight + 4 frontmatter/structure defects in Pass 2 step-1 pre-flight per (i.5) PMN-file-shape sub-extension + 1 §-citation residual in Pass 3 Builder step-6 (j) sweep post-authoring). Verifiable at pre-commit:
   - bash: `awk '/^### §1\.1/,/^---/' docs/post-merge-notes/PMN-008-pr-17-cycle-learnings.md | grep -cE "^[0-9]+\. \*\*"` returns `8`
   - PowerShell: equivalent regex via `Select-String`

4. **PMN-008 §5 monitoring register enumerates §5.1 through §5.7** (seven monitoring items: (u), (q'), (j)-extension, (h.x)-extension, (s) absorption, (t) demotion, (v) NEW). Verifiable at pre-commit:
   - bash: `grep -cE "^### §5\.[0-9]+\." docs/post-merge-notes/PMN-008-pr-17-cycle-learnings.md` returns `7`
   - PowerShell: equivalent

5. **PMN-008 frontmatter `post_merge_note_id` is `PMN-008`** per PMN-007 HEAD canonical precedent. Verifiable at pre-commit:
   - bash: `grep -c "^post_merge_note_id: PMN-008$" docs/post-merge-notes/PMN-008-pr-17-cycle-learnings.md` returns `1`
   - PowerShell: equivalent

6. **PMN-008 frontmatter `status` is `drafted`** at file creation per PMN-007 (k) status-flip convention. Verifiable at pre-commit:
   - bash: `grep -c "^status: drafted$" docs/post-merge-notes/PMN-008-pr-17-cycle-learnings.md` returns `1`
   - PowerShell: equivalent
   - Status flips to `recorded` post-merge per PMN-001 (k) Linked PR fix-up substitution + status flip convention.

7. **PMN-008 frontmatter `framework_version_dogfooded` is `AMAS v2.17`** (no version bump this cycle — pure post-merge-note authoring). Verifiable at pre-commit:
   - bash: `grep -c "^framework_version_dogfooded: AMAS v2\.17$" docs/post-merge-notes/PMN-008-pr-17-cycle-learnings.md` returns `1`
   - PowerShell: equivalent regex

8. **PMN-008 has `## Status` section** between H1 and §1 per PMN-004/005/006/007 canonical precedent. Verifiable at pre-commit:
   - bash: `grep -c "^## Status$" docs/post-merge-notes/PMN-008-pr-17-cycle-learnings.md` returns `1`
   - PowerShell: equivalent

9. **PMN-008 frontmatter `title` field exactly matches H1 heading content after the `PMN-008 — ` prefix** per (i.5) title↔H1 alignment defect-7 path-(a) revision. Verifiable at pre-commit:
   - bash: title field via `grep "^title:" docs/post-merge-notes/PMN-008-pr-17-cycle-learnings.md` returns the canonical-refinement-enumeration form; H1 via `grep "^# PMN-008" docs/post-merge-notes/PMN-008-pr-17-cycle-learnings.md` returns the same content prefixed by `# PMN-008 — `
   - PowerShell: equivalent string compare via `Select-String`

10. **PMN-008 cross-references PMN-001 + PMN-004 + PMN-005 + PMN-006 + PMN-007 + ADR-003** in §7. Verifiable at pre-commit:
    - bash: `grep -cE "^- \*\*(PMN-00[14567]|ADR-003)" docs/post-merge-notes/PMN-008-pr-17-cycle-learnings.md` returns `6` (five PMNs + one ADR)
    - PowerShell: equivalent

11. **PMN-008 cites verified squash SHAs and pre-merge fix-up commit SHAs**: `ace6608` (PR-15), `ce44836` (PR-17), `52ee07e` (PR-18), `a64e401` (PR-15 pre-merge fix-up), `d57766e` (PR-17 pre-merge fix-up-1), `723c571` (PR-17 pre-merge fix-up-2). Verifiable at pre-commit:
    - bash: `grep -oE "(ace6608|ce44836|52ee07e|a64e401|d57766e|723c571)" docs/post-merge-notes/PMN-008-pr-17-cycle-learnings.md | sort -u | wc -l` returns `6`
    - PowerShell: `(Select-String -Path docs/post-merge-notes/PMN-008-pr-17-cycle-learnings.md -Pattern '(ace6608|ce44836|52ee07e|a64e401|d57766e|723c571)' -AllMatches).Matches.Value | Sort-Object -Unique | Measure-Object | Select-Object -ExpandProperty Count` returns `6`
    - Cross-verifiable against `git log --oneline main` for each SHA.

12. **PMN-008 cites core.md §-headers that exist in HEAD set**: §8.1.1.3 + §18.3 + §23.6 + §23.6.1 + §23.6.2. Verifiable at pre-commit:
    - bash: `grep -nE "^#{1,6} §(8\.1\.1\.3|18\.3|23\.6(\.[12])?)" core.md` returns ≥5 lines (one per cited §-anchor)
    - PowerShell: equivalent

13. **TASK-0018 handoff frontmatter `task_id` is `TASK-0018`**. Verifiable at pre-commit:
    - bash: `grep -c "^task_id: TASK-0018$" docs/handoffs/TASK-0018-pmn-008-pr-17-cycle-learnings.md` returns `1`
    - PowerShell: equivalent

14. **TASK-0018 handoff frontmatter `framework_version_dogfooded` is `AMAS v2.17`**. Verifiable at pre-commit:
    - bash: `grep -c "^framework_version_dogfooded: AMAS v2\.17$" docs/handoffs/TASK-0018-pmn-008-pr-17-cycle-learnings.md` returns `1`
    - PowerShell: equivalent

15. **PR-19 review-context (this file) exists with the canonical `## Builder claims to verify` structure** and includes Claims 1-15 enumerated. Verifiable at pre-commit:
    - bash: `grep -c "^## Builder claims to verify$" docs/reviews/PR-19-codex-pre-commit.md` returns `1`; `grep -cE "^[0-9]+\. \*\*" docs/reviews/PR-19-codex-pre-commit.md` returns ≥`15`
    - PowerShell: equivalent

## Adjudication ladder (severity guidance)

Per PMN-004 §5 (a) standing three-level severity taxonomy:

- **Blocking**: claim is materially false; blocks merge until path-(a) resolution. Examples: tracked-file count diverges; §-citation references non-existent header; squash SHA does not match git log.
- **Major**: claim is verifiable but contains internal inconsistency or scope mismatch warranting path-(a) revision before merge. Examples: PMN-008 §1.1 enumeration count mismatch with declared 7-defect tally; cross-reference anchor mismatch.
- **Minor**: claim is correct as stated; finding is stylistic / convention-precedent guidance for future cycles. Examples: claim-text wording could be tighter; verification-command form has minor redundancy.

Codex output absorbed verbatim per PMN-002 (a). Path-(a) routing decisions per PMN-007 §2.4 cost-class refinement (genuinely-asymptotic-vs-pure-token-swap distinction); path-(a) for pure-token-swap class (single-iteration fix); path-(β) for genuinely-asymptotic class (multi-cycle deferral).

## Cumulative diff stats (per (e.1) sub-rule)

Pre-Codex first-commit cumulative-diff-stats per (e.1) sub-rule re-derivation (verified post-staging, pre-stop-and-show):

- Files changed: 3 (PMN-008 + TASK-0018 handoff + PR-19 review-context — all NEW)
- Insertions: 473
- Deletions: 0 (no canonical-text or existing-file modifications this cycle)
- Σ per-file: 258 (PMN-008) + 76 (TASK-0018 handoff) + 139 (PR-19 review-context) = 473 = total ✓
- Verification command: `git diff --staged --shortstat` returns `3 files changed, 473 insertions(+)`; per-file via `git diff --staged --shortstat -- <path>` for each deliverable.

Post-Codex absorption + handoff body fill numbers will be re-derived at pre-merge fix-up commit per (e.1) sub-rule + (t) sub-shape.

## Honesty record — Builder PR-19 step-1 self-review (pre-flight pre-authoring batch)

Per PMN-008 §1.1 honesty record — recorded here at the review-context surface for cross-cycle traceability:

**Pass 1 — §-content sweep** (3 defects caught in Architect-drafted PMN-008 spec content):

1. **§2.1 (t) three-data-point claim conflated PR-13 §18.3 M-A7 amend-on-main with (t) pre-merge feature-branch fix-up**, falsifying the canonical-refinement-threshold claim. Verified against git history: PR-15 has `a64e401` (2 files / 76+/3-); PR-17 has `d57766e` (3 files / 38+/2-) + `723c571` (2 files / 88+/3-); PR-13 has none of this shape. Path-(a) routed: §2 reshaped as demotion record; (t) carries forward as monitoring item §5.6.
2. **§4.2 cited [github-reference.md](github-reference.md) §3.5 placement target without verification** (§3 has only §3.1/§3.2/§3.3 in HEAD; no §3.5). (i.5) self-application failure. Path-(a) routed: drop specific anchor; defer placement to TASK-0019 Phase 1 scoping.
3. **§7 PMN-006 cross-reference anchored to §3 instead of correct §1.1/§3.2**. PMN-006 §3 is "(b) → (g) + (h) split: verification-artifact-validity discipline canonicalization"; multi-surface-mitigation framing lives in §1.1 + §3.2. Path-(a) routed: re-anchor.

**Pass 2 — frontmatter/structure convention-inference sweep** (4 defects per (i.5) PMN-file-shape sub-extension against PMN-007 HEAD canonical precedent):

4. **Frontmatter field convention divergence** from PMN-007 HEAD (`post_merge_note_id` / `linked_pr` with squash-SHA-placeholder / `framework_version_dogfooded` / `status: drafted`). Architect-spec frontmatter used novel `pmn_id` / `task_id` / `pr` / `source_cycles` / `linked_predecessor` / `status: active` shape. Path-(a) routed: replace with PMN-007 canonical frontmatter; lift `source_cycles` / `task_id` / `linked_predecessor` framing into §1 prose. Owner adjudication confirmed no new convention intended.
5. **`linked_predecessor` value error**: "PMN-007 (TASK-0013 / PR-13 cycle learnings)" — TASK-0013 is unused/reserved; PMN-007 was authored at TASK-0015 / PR-15. Path-(a) routed: TASK-0013 → TASK-0015 in §1 prose; clarify slug-vs-anchor distinction inline.
6. **Missing `## Status` section** between H1 and §1 per PMN-004/005/006/007 canonical precedent. Path-(a) routed: add canonical `## Status` section.
7. **Frontmatter `title` field vs H1 heading content mismatch**: title elaborated "(r) fifth review surface, (i.5) convention-inference verification, (t) two-data-point preliminary"; H1 was shorter "PR-15 + PR-17 cycle learnings". Path-(a) routed: align H1 to title field's longer canonical-refinement enumeration form.

All seven step-1 pre-flight defects path-(a) routed via Architect spec-authoring revisions before Builder commit; no path-(β) deferrals at the pre-flight surface.

**Pass 3 — Builder step-6 self-review (j) sweep on §-citations after authoring** (1 defect; canonical (r) discipline operating at step-6 post-authoring rather than step-1 pre-flight):

8. **PMN-007 §6 (p) cross-reference incorrect** — Architect-drafted spec referenced "PMN-007 §6 (p) M-A7 amend-on-main framing"; (p) is actually canonicalized at PMN-007 §8.2 (PMN-007 §6 is "Auto-trigger reliability — preliminary observation"). Defect propagated from spec into Builder-authored PMN-008 §2.2 table row + TASK-0018 handoff `Linked records` enumeration. Caught at Builder step-6 (j) all-instances sweep on `PMN-007 §[0-9]+(\.[0-9]+)?` pattern across all three deliverable files. Path-(a) routed: pure-token-swap (single-iteration fix; replace `§6` with `§8.2` in two locations). Empirical instance of (r) Builder step-6 self-review operating at the canonical surface specified in PMN-008 §3.1: "§-citation residuals that escape Architect sweep" — exactly the defect class caught.

## (v) candidate observation — registered alongside (r) recursive empirical confirmations

Per PMN-008 §5.7 monitoring register entry:

> When a PMN canonicalizes a discipline, defects in that PMN's own authoring (caught at the canonicalized discipline's downstream surfaces) provide the strongest possible empirical confirmation of the discipline's load-bearing role. (k.1) positive empirical confirmation at maximum strength: the canonicalizing PMN is shaped into correctness BY the very discipline it canonicalizes, applied at downstream surfaces.

PR-19 cycle = single-cycle observation at PMN-008 authoring. Promotion threshold: 2-3 cross-cycle confirmations. Anticipated next test case: TASK-0019 usage-guide.md authoring cycle (canonicalizes operating-guidance disciplines; observe whether Builder downstream surfaces catch defects in usage-guide.md's articulation of those disciplines arising from Architect failure to apply them at authoring time).

## Post-PR Codex absorption

Codex post-PR review invoked by owner via `@codex review` issue comment at `2026-05-03T22:19:01Z`; Codex auto-fire at `2026-05-03T22:22:19Z` reviewing commit `70fa920af8`. Two-endpoint poll per core.md §8.1.1.1 corrected canonical lexicographic form:

- **Endpoint 1 (PR reviews)**: 1 review by `chatgpt-codex-connector[bot]` (state `COMMENTED`; body 621 chars — auto-fire informational template only, no Blocking/Major/Minor findings, no specific feedback).
- **Endpoint 2 (PR issue comments)**: 1 comment from owner (`@codex review` invocation trigger; not a Codex finding).

**Pass-1 result: zero substantive findings — clean-first-pass shape**. Empirically aligns with (q') candidate prediction per PMN-008 §5.2 small-scope-clean prediction: PR-19 is pure post-merge-note authoring (no canonical-text changes), smaller scope than PR-15 which itself produced clean-first-pass. Third data point for (q') candidate (PR-15 + PR-19 = clean-first-pass for small-scope cycles; PR-17 = findings for full-canonical-law-trio-member authoring); strengthens (q') scope-conditional pattern toward canonical refinement threshold per §5.2 promotion trigger.

Path-(a) revisions: N/A (zero findings).
Path-(β) deferrals: N/A.

**(t) sub-shape applied at this cycle close**: pre-merge fix-up commit on feature branch capturing PR-19 review-context post-PR Codex absorption + TASK-0018 handoff body fill. PR-19 fix-up does NOT count toward (t) §5.6 promotion threshold (restricted to substantive-content cycles per §5.6 promotion-trigger framing; PR-19 is PMN-only chore-class cycle). Sub-shape applies for cycle-final-state-record discipline regardless of substantive-vs-chore classification.

Empirical interpretation: PMN-008 cycle close follows PR-15 cycle close shape (clean-first-pass + (t) fix-up commit for handoff body fill + review-context absorption record). (q') third-data-point strengthening is the most consequential cross-cycle observation at PMN-008 cycle close.
