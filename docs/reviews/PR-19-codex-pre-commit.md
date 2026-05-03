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
- Recursive-self-instantiation: PR-19 canonicalizes (in PMN-008) the (r) Builder step-6 self-review fifth surface and (i.5) convention-inference verification disciplines. Builder PR-19 self-review + post-cycle-close re-poll surfaced **eleven defects in PMN-008 cycle itself** across five sweep passes — three §-content defects (Pass 1 step-1 pre-flight) plus four frontmatter/structure convention-inference defects (Pass 2 step-1 pre-flight per (i.5) PMN-file-shape sub-extension) plus one §-citation residual (Pass 3 Builder step-6 (j) sweep post-authoring; PMN-007 §6 (p) → §8.2 (p)) plus two Codex post-PR findings at third-endpoint (Pass 4; Claim 11 unverifiable SHAs + broken markdown link) plus one canonical-text-correctness gap at Builder absorption-discipline surface (Pass 5 — (h.4) two-endpoint poll incomplete; surfaced post-first-fix-up via owner re-poll). All path-(a) routed except defect 11 which routes path-(β) for canonical-text correction at separate cycle. The disciplines PMN-008 canonicalizes self-applied within PMN-008's own authoring cycle to catch defects that escaped Architect §23.6 single-iteration sweep, INCLUDING surfacing a canonical-text-correctness gap (h.4) that survived multiple prior cycles' canonicalization at the Builder absorption-discipline surface. (k.1) positive empirical confirmation at maximum strength; (v) candidate observation registered at PMN-008 §5.7; (h.4) NEW canonical-refinement candidate registered at PMN-008 §5.8.

## Builder claims to verify

The Builder asserts the following at hand-off to Codex desktop pre-commit review. Each claim is verifiable from the working tree at pre-commit time (no future-tense claims per PMN-004 §5 (c)). PR-19 is a pure post-merge-note authoring cycle (PMN-008 + TASK-0018 handoff + PR-19 review-context); no canonical-text changes.

1. **Tracked-file count on feature branch post-Builder-commit** = 101 (98 base + 3 new files: PMN-008 + TASK-0018 handoff + PR-19 review-context). Pre-commit-verifiable per (c) discipline.
   - bash: `git ls-files | wc -l` returns `101` on feature branch post-staging
   - PowerShell: `(git ls-files | Measure-Object -Line).Lines` returns `101`

2. **PMN-008 top-level §-header count** = 7 (§1-§7). Verifiable at pre-commit:
   - bash: `grep -cE "^## §[0-9]+\." docs/post-merge-notes/PMN-008-pr-17-cycle-learnings.md` returns `7`
   - PowerShell: `(Select-String -Path docs/post-merge-notes/PMN-008-pr-17-cycle-learnings.md -Pattern '^## §[0-9]+\.').Count` returns `7`

3. **PMN-008 §1.1 honesty record enumerates 11 defects across 5 sweep passes** (3 §-content defects in Pass 1 step-1 pre-flight + 4 frontmatter/structure defects in Pass 2 step-1 pre-flight per (i.5) PMN-file-shape sub-extension + 1 §-citation residual in Pass 3 Builder step-6 (j) sweep post-authoring + 2 Codex post-PR findings in Pass 4 third-endpoint + 1 canonical-text-correctness gap in Pass 5 (h.4) at Builder absorption-discipline surface). Verifiable at pre-commit:
   - bash: `awk '/^### §1\.1/,/^---/' docs/post-merge-notes/PMN-008-pr-17-cycle-learnings.md | grep -cE "^[0-9]+\. \*\*"` returns `11`
   - PowerShell: equivalent regex via `Select-String`

4. **PMN-008 §5 monitoring register enumerates §5.1 through §5.8** (eight monitoring items: (u), (q') DISCONFIRMED, (j)-extension, (h.x)-extension, (s) absorption, (t) demotion, (v) NEW, (h.4) NEW canonical-refinement candidate). Verifiable at pre-commit:
   - bash: `grep -cE "^### §5\.[0-9]+\." docs/post-merge-notes/PMN-008-pr-17-cycle-learnings.md` returns `8`
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

11. **PMN-008 cites squash SHAs reachable from `main` HEAD**: `ace6608` (PR-15 squash), `ce44836` (PR-17 squash), `52ee07e` (PR-18 squash). Verifiable at pre-commit (only main-reachable squash SHAs are claimed cross-verifiable; pre-merge fix-up commit SHAs cited in §2.2 table — `a64e401` / `d57766e` / `723c571` — are NOT main-reachable post-squash and are recorded as historical (t)-sub-shape diff-size data points cross-referenced to the individual PR-15 + PR-17 review-context records, not as main-history cross-verifiable references; this Claim 11 reframe absorbs Codex post-PR Finding 1 path-(a) per PMN-008 cycle close):
    - bash: `for sha in ace6608 ce44836 52ee07e; do git log --oneline main | grep -q "^$sha" || echo "MISSING: $sha"; done` returns empty (all three present in main)
    - PowerShell: `'ace6608','ce44836','52ee07e' | ForEach-Object { if (-not (git log --oneline main | Select-String "^$_")) { "MISSING: $_" } }` returns empty
    - Cross-reference for pre-merge fix-up commit SHAs (recorded for completeness, not cross-verifiable against main): see PR-15 review-context (`docs/reviews/PR-15-codex-pre-commit.md`) for `a64e401` provenance; see PR-17 review-context (`docs/reviews/PR-17-codex-pre-commit.md`) for `d57766e` + `723c571` provenance.

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

**First fix-up commit `eac8301`** (Codex post-PR absorption initial framing + handoff body fill per (t) sub-shape — subsequently superseded by second fix-up after (h.4) discovery): 2 files / 38+/13- ; Σ per-file = 25+/12- + 13+/1- = 38+/13- = total ✓.

**Second fix-up commit (this commit)** path-(a) revisions for Codex post-PR Pass 4 + Pass 5 (h.4) findings + (q') disconfirmation + (j) broken-link sweep: 3 files / 110 insertions / 36 deletions; Σ per-file = 65+/15- (PMN-008) + 9+/3- (handoff) + 36+/18- (review-context) = 110+/36- = total ✓ self-stable.

PR-19 cumulative additions vs base main post-second-fix-up: 473 (first commit) + (38-13) net (first fix-up) + (110-36) net (second fix-up) = 473 + 25 + 74 = 572. Verifiable via `gh pr view 19 --json additions,deletions` post-push.

## Honesty record — Builder PR-19 step-1 self-review (pre-flight pre-authoring batch)

Per PMN-008 §1.1 honesty record — recorded here at the review-context surface for cross-cycle traceability:

**Pass 1 — §-content sweep** (3 defects caught in Architect-drafted PMN-008 spec content):

1. **§2.1 (t) three-data-point claim conflated PR-13 §18.3 M-A7 amend-on-main with (t) pre-merge feature-branch fix-up**, falsifying the canonical-refinement-threshold claim. Verified against git history: PR-15 has `a64e401` (2 files / 76+/3-); PR-17 has `d57766e` (3 files / 38+/2-) + `723c571` (2 files / 88+/3-); PR-13 has none of this shape. Path-(a) routed: §2 reshaped as demotion record; (t) carries forward as monitoring item §5.6.
2. **§4.2 cited github-reference.md §3.5 placement target without verification** (§3 has only §3.1/§3.2/§3.3 in HEAD; no §3.5). (i.5) self-application failure. Path-(a) routed: drop specific anchor; defer placement to TASK-0019 Phase 1 scoping.
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

Codex post-PR review invoked by owner via `@codex review` issue comment at `2026-05-03T22:19:01Z`; Codex auto-fire at `2026-05-03T22:22:19Z` reviewing commit `70fa920af8`.

### First-pass absorption record (subsequently superseded — see correction record below)

Initial Builder absorption applied a two-endpoint poll per core.md §8.1.1.1 corrected canonical lexicographic form:

- **Endpoint 1 (PR reviews)**: 1 review by `chatgpt-codex-connector[bot]` (state `COMMENTED`; body 621 chars — auto-fire informational template only, no Blocking/Major/Minor findings).
- **Endpoint 2 (PR issue comments)**: 1 comment from owner (`@codex review` invocation trigger; not a Codex finding).

Pass-1 was framed as zero substantive findings → clean-first-pass shape; (q') three-data-point strengthening claim recorded; first cycle-final fix-up commit `eac8301` landed with that framing.

### Correction record — (h.4) endpoint-coverage gap surfaced post-fix-up

Owner-driven re-poll surfaced **two real Codex findings at a third endpoint** (`pulls/{pr}/comments` — line-level review comments) that the two-endpoint poll did not cover:

- **Finding 1 (P1 — Major-severity-equivalent)** at PR-19 review-context Claim 11 (line 66 of `docs/reviews/PR-19-codex-pre-commit.md` at fix-up tip `eac8301`): Claim 11 listed pre-merge fix-up SHAs (`a64e401`, `d57766e`, `723c571`) as cross-verifiable against `git log --oneline main`. **Real defect**: those SHAs are not in `main` history (squash-merged out at PR-15 / PR-17 close); claim's verification path is operationally broken. Path-(a) routed: drop SHA enumeration from main-cross-verifiable claim; reframe Claim 11 as "main-reachable squash SHAs only (`ace6608`/`ce44836`/`52ee07e`) cross-verifiable against main; pre-merge fix-up SHAs in §2.2 table cross-referenced to PR-15/PR-17 review-contexts as historical (t)-sub-shape diff-size data points, not main-history references". Pure-token-swap class per §8.1.1.3 cost-class refinement.
- **Finding 2 (P3 — Minor-severity-equivalent)** at TASK-0018 handoff line 69 (`docs/handoffs/TASK-0018-pmn-008-pr-17-cycle-learnings.md`): broken markdown link `[github-reference.md](github-reference.md)` from a file at `docs/handoffs/` resolves to `docs/handoffs/github-reference.md` (does not exist); actual file at repo root. **Real defect**. Path-(a) routed: drop markdown-link wrapper to plain text reference (matches PMN-007 / PMN-006 / PMN-005 / PMN-004 prior-PMN convention; (i.5) PMN-file-shape sub-extension would have caught this if applied at authoring time). (j) same-class sweep on `\]\([a-zA-Z][^):/]*\.md\)` pattern across all three deliverables surfaced 6 total broken-link instances (5 in PMN-008 + 1 in handoff + 1 in review-context); all path-(a) routed to plain-text references.

**(h.4) Codex-output-endpoint-coverage NEW defect class** registered at PMN-008 §5.8 with five-data-point empirical evidence (PR-11: 11 inline comments; PR-13: 1; PR-15: 0; PR-17: 6; PR-19: 2). Five-of-five recent PRs with at-least-one inline comment except PR-15. The two-endpoint poll framing canonicalized at core.md §8.1.1.1 corrected lexicographic form is structurally INCOMPLETE — a third endpoint (`pulls/{pr}/comments`) carries the most defect-dense Codex output channel. (h.4) registers as immediate canonical-refinement candidate (not preliminary monitoring) given empirical evidence already spans five data points; canonical text correction at core.md §8.1.1.1 deferred to separate cycle (anticipated TASK-0021 or following) per spec-level edit needing its own cycle.

**(q') candidate disconfirmed at PR-19**: original framing claimed PR-19 = third clean-first-pass data point for small-scope-clean prediction. Actual PR-19 = 2 findings (1 Major + 1 Minor); does NOT fit small-scope-clean prediction. (q') demoted at PMN-008 §5.2 with explicit disconfirmation event recorded.

### Final absorption result

Two findings; both path-(a) routed; pure-token-swap cost class. (h.4) NEW defect class surfaced at Builder-side endpoint-coverage gap; (q') disconfirmed; (t) sub-shape continues to apply for cycle-final-state-record discipline. Cycle close NOT clean-first-pass; absorption record at this artifact corrected via second cycle-final fix-up commit. First fix-up commit `eac8301` durable git history retains false framing per §3.1 GitHub branch protection (force-push disabled); correction lands at this review-context surface and propagates into squash-merge commit body via Architect §18.3 M-A7 authoring fresh post-merge.

Path-(β) deferrals: core.md §8.1.1.1 canonical text correction (separate cycle).
