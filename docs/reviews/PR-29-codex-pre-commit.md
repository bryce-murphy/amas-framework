---
status: drafted
---

# PR-29 Codex desktop pre-commit review context

## Metadata

- PR ID: PR-29
- TASK ID: TASK-0024
- Branch: `feat/task-0024-usage-guide-substantive-fill`
- Base SHA: `9365b4bf15f55d035052fac800cd169eda6af806` (squash-merge of PR-28 chore on main, 2026-05-05T15:14:21Z; PR-28 = TASK-0023 linked-PR substitution chore-fix-up auto-fired by linked-pr-fix-up Action shipped at PR-21)
- Builder: Claude Code (Claude Opus 4.7, Windows 11 + Git Bash)
- Reviewer: Codex (GPT-5.5) — desktop, pre-commit, untracked working tree
- Architect (this PR's): Claude Opus 4.7 (Claude.ai Project)
- Owner: Bryce Murphy (`@bryce-murphy`)
- Framework version: AMAS v2.20 → v2.21 (dogfooded post-§18.4 substantive-reading minor bump applied this cycle — fourth minor-tier bump after v2.17 → v2.18 at PR-21, v2.18.1 → v2.19 at PR-25, and v2.19 → v2.20 at PR-27; substantive content addition: usage-guide.md scaffold-stub → 388-line substantive content fill, third canonical-law-trio document materialized; first non-self-instantiating canonical-application of §23.6.3 reference-verification discipline shipped at TASK-0023; Path B `(forthcoming at Part C+)` qualifier convention introduced this cycle)
- Severity taxonomy: Blocking / Major / Minor (three-level; per repo discipline; standing per PMN-004 §5 (a))
- Disciplines applied (PMN-004 §5 (a)-(f) + PMN-005 sub-rule (e.1) + PMN-006 (g)/(h)/(i) + PMN-006 §5.3 bounded-continuation rule generalized + PMN-006 §3.4 frontmatter-vs-body sub-clause + PMN-007 §2.4 cost-class refinement + PMN-007 §3.1 four-surface iterative-pre-flight + iterative-post-PR-review pattern + PMN-007 §9.1 (i) extended pre-authoring verification batch + PMN-007 §4 PMN-001 (k) mechanism-vs-discipline canonicalization + PMN-008 §3.2 five-surface review pipeline + PMN-008 §4.2 (i.5) convention-inference verification with PMN-file-shape sub-extension + PMN-008 §5.8 (h.4) three-endpoint Codex poll discipline canonical at core.md §8.1.1.1 since v2.19 + PMN-009 / core.md §23.6.3 reference-verification before spec authoring CANONICAL since v2.20; first non-self-instantiating canonical-application this cycle): severity taxonomy three-level (a); verification-command portability (b); no future-tense pre-commit claims (c); pre-commit cross-surface scope clarity (d); §23.6 prose-arithmetic decomposition (e) with sub-rule (e.1) cumulative-diff-stats re-derivation; section-citation correctness sweep (f); verification-artifact internal consistency (g); verification-command operational correctness (h) with sub-shapes (h.1)/(h.2)/(h.3)/(h.4); cross-document state verification (i) with sub-shapes (i.1)/(i.2)/(i.3)/(i.4)/(i.5); §23.6.2 iterative-to-fixed-point self-review; §23.6.3 reference-verification before spec authoring (first non-self-instantiating canonical-application — TASK-0023 was self-instantiating); §8.1.1.3 bounded-continuation rule with cost-class refinement.
- Substantive-content-cycle context: PR-29 is the largest single-document substantive-content cycle in project history. Three coupled deliverables co-shipped: (1) usage-guide.md scaffold-stub (9 lines) → substantive content fill (388 lines, §0–§13 structure, 14 top-level §-sections; v2.14.1 substrate restructured into v3 split-package form per transition plan v0.2 Decision A + framework-evolution-since-v2.14.1 absorbed); (2) README.md Class A canonical-version-of-record bump v2.20 → v2.21 + per-PR-row update at "Canonical law" table for usage-guide.md `Filled by` cell `PR-11 (TASK-0011)` forecast → `PR-29 (TASK-0024)` actual; (3) usage-guide.md frontmatter `status: stub` → `drafted` + `filled_by: per ADR-003` → `filled_by: PR-29 (TASK-0024)` (subsumed by deliverable 1 since same file). Builder pre-flight (i.5) batch surfaced 1 MAJOR finding + 6 routine items at step-1 stop-and-show: (i.5)(c) MAJOR — 12 forward-referenced core.md §-citations in spec §4 content prescription do not resolve in current core.md (status: partial; only §8/§17/§18/§23/§24 materialized to date); Architect adjudication: Path B refined qualifier `(forthcoming at Part C+)` applied at every occurrence; path-(a) in-cycle correction; owner approved. Single-cycle catch volume (12 distinct §-citations across 20 occurrence-sites) classified as 14th cumulative-empirical-record confirmation of §23.6.3 / PMN-009 / TASK-0023 self-instantiation pattern (13 → 14); primary substantive evidence for PMN-010 authoring at TASK-0025+.

## Builder claims to verify

The Builder asserts the following at hand-off to Codex desktop pre-commit review. Each claim is verifiable from the working tree at pre-commit time (no future-tense claims per PMN-004 §5 (c)). PR-29 ships usage-guide.md substantive content fill + README.md Class A v-bump + Canonical-law table per-PR-row update + TASK-0024 handoff + PR-29 review-context.

1. **Working-tree state at pre-commit (staged): 2 staged-added + 2 staged-modified**. Convention note: this cycle stages all changes before Codex pre-commit pass per the (e.1) cumulative-diff-stats requirement (`git diff --shortstat origin/main` on untracked tree omits new files; staged-tree form returns the correct cumulative count). Verifiable at pre-commit per (c) + (h.2) discipline.
   - bash (staged-added): `git status --porcelain | grep -c "^A "` returns `2` (2 staged-added: `docs/handoffs/TASK-0024-usage-guide-substantive-fill.md` + `docs/reviews/PR-29-codex-pre-commit.md`).
   - bash (staged-modified): `git status --porcelain | grep -c "^M "` returns `2` (2 staged-modified: `usage-guide.md`, `README.md`).
   - PowerShell: `(git status --porcelain | Select-String "^A ").Count` returns `2`; `(git status --porcelain | Select-String "^M ").Count` returns `2`.

2. **usage-guide.md substantive content fill — file body matches §4 content prescription verbatim** (frontmatter + 14 top-level §-sections §0–§13). Verifiable at pre-commit:
   - bash: `grep -cE "^## §" usage-guide.md` returns `14` (14 top-level §-sections: §0, §1, §2, §3, §4, §5, §6, §7, §8, §9, §10, §11, §12, §13).
   - bash: `grep -nE "^## §" usage-guide.md` returns 14 lines (one per top-level section header) with §-numbers in canonical order §0 → §13.
   - bash: `head -5 usage-guide.md` returns frontmatter lines: `---` + `framework_version: 3.0.0` + `status: drafted` + `filled_by: PR-29 (TASK-0024)` + `---`.
   - bash: `wc -l usage-guide.md` returns `388` (landed exact source-line count at step-12 commit; unchanged through step-16 fix-up which modifies 2 existing lines without net line-count delta).

3. **All §-citations to current core.md verified against current canonical state.** Each citation in usage-guide.md to `core.md §X` for sections that exist in current core.md (status: partial; §8/§17/§18/§23/§24 materialized) is verifiable against current `core.md` heading set. Verifiable at pre-commit:
   - bash: `grep -nE "core\.md\` §[0-9]" usage-guide.md` enumerates all `core.md §X` citations (markdown-formatted with backticks); each citation manually reconciled against `grep -nE "^#{1,6} §" core.md` heading set.
   - Resolved citations (sections currently in core.md): §8.1.1, §8.1.1.1, §8.1.1.2, §8.1.1.3, §17, §18, §23, §23.6, §23.6.1, §23.6.1.1, §23.6.2, §23.6.3, §24, §24.2, §24.3, §24.3.1.

4. **Forward-referenced core.md §-citations carry Path B qualifier `(forthcoming at Part C+)` at every occurrence.** Architect adjudication at step-1 stop-and-show; path-(a) in-cycle correction; refined qualifier form per Builder execution-mechanics note (Architect-ratified). At step-1 stop-and-show, finding enumerated 12 anticipated forward-referenced sections (§2.2.2, §2.3.4, §2.3.6, §2.3.7, §3.1, §3.4.1, §3.4.2, §5.4, §8.2, §8.3, §10.5, §17.5) per union of spec §1 + §4 + §7 prescription text. Step-9 self-review (j) sweep refined to 9 distinct sections actually cited in §4 body content (§2.2.2, §2.3.4, §2.3.7, §3.1, §5.4, §8.2, §8.3, §10.5, §17.5); the other 3 of the 12 (§2.3.6, §3.4.1, §3.4.2) appear in spec §7 anticipated-citation list but not in §4 materialized body — over-anticipation in spec §7 prediction, not a defect. All 9 actually-cited sections will materialize in core.md Part C+ per ADR-003 D2 plan. Verifiable at pre-commit:
   - bash: `grep -oE "forthcoming at Part C\+" usage-guide.md | wc -l` returns `27` (27 qualifier-instance occurrences across 9 distinct forward-referenced §-sections at every cited site). Per-§ instance breakdown: §8.2 = 10; §8.3 = 5; §2.3.7 = 4; §2.2.2 = 2; §5.4 = 2; §3.1 = 1; §10.5 = 1; §17.5 = 1; §2.3.4 = 1. Sum: 10+5+4+2+2+1+1+1+1 = 27 ✓.
   - bash: `grep -cE "forthcoming at Part C\+" usage-guide.md` returns `20` (20 distinct lines contain at least one qualifier; multi-qualifier-per-line sites — e.g., §10.1 line 295 has 2 §8.2 qualifiers; §9.12 line 287 has 2 §2.3.7 + 1 §2.3.4; §9.13 + §10.18 each combine §2.2.2 + §5.4 — yield 27 total instances on 20 lines). Both counts are correct at distinct grain levels: lines = 20 (-c flag); instance occurrences = 27 (-o flag).
   - bash: `grep -nE "§(2\.2\.2|2\.3\.4|2\.3\.6|2\.3\.7|3\.1|3\.4\.1|3\.4\.2|5\.4|8\.2|8\.3|10\.5|17\.5)\b" usage-guide.md` enumerates all forward-ref §-citations; manual review confirms every site referencing core.md (whether prefixed with `core.md §` or naked-when-context-resolves-to-core.md) carries the Path B qualifier. Note: usage-guide's own section anchors (§3.1 Issue, §5.4 FEAT-#### vs TASK-####, §8.2 Tool Inventory, §8.3 Constrained-professional, §10.5 Reviewer-§-citation friction) intentionally do not carry the qualifier since they are usage-guide's own headings, not forward-references to core.md.
   - bash: post-correction qualifier-presence sweep — for each of 9 actually-cited forward-ref §-sections, `grep -nE "core\.md §<sec>" usage-guide.md` and naked-context occurrences all show qualifier inline; 0 unqualified residuals.

5. **All §-citations to github-reference.md verified.** Anticipated: §2.2 (branch convention) + §6.2 (anticipated Actions). Both resolve in current github-reference.md heading set (lines 75 + 271 respectively). Verifiable at pre-commit:
   - bash: `grep -nE "github-reference\.md\` §[0-9]" usage-guide.md` enumerates github-reference.md citations; reconcile against `grep -nE "^#{1,6} §" github-reference.md` heading set.
   - Resolved citations: §2.2 (branch convention), §6.2 (anticipated Actions). Two distinct sections; multi-occurrence: §6.2 cited at usage-guide §3.3 + §7.1 + §10.14; §2.2 cited at usage-guide §3.3.

6. **Forward-references to forthcoming files use anticipation-language qualifier.** Each forward-reference to `prompts/*.md` / `appendices/*.md` carries explicit "(forthcoming at TASK-####+)" qualifier. Verifiable at pre-commit:
   - bash: `grep -nE "forthcoming at TASK-" usage-guide.md` returns multiple lines covering: prompts/{greenfield,retrofit,upgrade}.md (forthcoming at TASK-0025+); appendices/project-types/*.md (forthcoming at TASK-0025+); appendices/documentation-mcp-options.md (forthcoming at TASK-0026+); appendices/amas-vs-other-frameworks.md (forthcoming at TASK-0026+); appendices/regulated-tier-extension.md (forthcoming at TASK-0026+).
   - Pre-flight (i.5) batch verified each forward-referenced file exists at expected path as scaffold-stub state; anticipation-language TASK-#### numbering matches ADR-003 D2 PR plan + cycle-close-ledger contingency-slot accounting.

7. **README.md Class A v-bump applied** — line 9 contains `v2.21` × 2; `v2.20` not present at line 9. Verifiable at pre-commit:
   - bash: `sed -n '9p' README.md` returns post-bump line containing `v2.21` × 2 instances on the same physical line.
   - bash: `grep -nE "\bv2\.20\b" README.md` returns no lines (Class A surgically migrated; no residual at canonical version-of-record surface).
   - bash: `grep -nE "\bv2\.21\b" README.md` returns line 9 with two `v2.21` instances (the only `v2.21` references in README per Class A surgical edit shape).

8. **README.md per-PR-row update at usage-guide.md row** — `Filled by` cell text contains `PR-29 (TASK-0024)`; previous forecast text `PR-11 (TASK-0011)` not present. Verifiable at pre-commit:
   - bash: `grep -nA0 "usage-guide.md" README.md` returns the table row at line 42 with `PR-29 (TASK-0024)` in the `Filled by` cell.
   - bash: `grep -E "PR-11.*TASK-0011" README.md` returns 0 lines (forecast text replaced).
   - bash: `grep -E "PR-29.*TASK-0024" README.md` returns 1 line (line 42 `Canonical law` table row for usage-guide.md).

9. **No regressions at Class B/C version markers** — `v2.14.1` operating-framework anchors preserved verbatim across AGENTS.md / CLAUDE.md / docs/adr/ADR-001-initial-repo-setup.md; historical version markers in core.md / handoff frontmatters / PMN bodies / prior review-contexts preserved verbatim. Verifiable at pre-commit:
   - bash: `grep -cE "v2\.14\.1" AGENTS.md CLAUDE.md docs/adr/ADR-001-initial-repo-setup.md` returns existing v2.14.1 operating-framework anchor counts unchanged from origin/main baseline.
   - bash: `git diff origin/main -- AGENTS.md CLAUDE.md docs/adr/ADR-001-initial-repo-setup.md` returns no lines (no diff — Class B surfaces untouched).
   - bash: `git diff origin/main -- docs/post-merge-notes/ docs/handoffs/TASK-0023-pmn-009-absorption.md docs/reviews/PR-27-codex-pre-commit.md` returns no lines (Class C historical narrative surfaces untouched at this cycle).

10. **Five-surface review pipeline framing matches PMN-008 §3.2 canonical text.** usage-guide.md §7.6 enumerates the five surfaces in canonical order (Architect §23.6 self-review → Builder pre-flight → Builder step-6 self-review → Codex desktop pre-commit → Codex cloud post-PR). Verifiable at pre-commit:
   - bash: `grep -A8 "five surfaces" usage-guide.md` shows numbered enumeration; verify five-element list with canonical-order anchors.
   - bash: `grep -nE "(Architect §23\.6 self-review|Builder pre-flight|Builder step-6 self-review|Codex desktop pre-commit|Codex cloud post-PR)" usage-guide.md` returns 5+ lines (anchors present in §7.6 + §13 one-page reference).

11. **Three-tier solo-operator framing matches transition plan v0.2 Decision E.** usage-guide.md §8.5 enumerates light / production (AMAS default) / regulated tiers. Verifiable at pre-commit:
    - bash: `grep -nE "Light tier|Production tier|Regulated tier" usage-guide.md` returns 3 distinct tier headings + body content per tier.
    - bash: `grep -n "AMAS default" usage-guide.md` returns one line in §8.5 production-tier body (default-tier identification).
    - bash: `grep -nE "HIPAA|PCI-DSS|SOX|GDPR|FDA 21 CFR Part 11" usage-guide.md` returns lines in §0 + §2.5 + §8.5 (regulated-tier domain enumeration consistency).

12. **§24.3.1 five-point check enumerated correctly.** usage-guide.md §9.10 enumerates the five points in canonical order matching `core.md` §24.3.1 (three-endpoint poll, branch tip-SHA, file content audit, phantom-action audit, comment-content claim verification). Verifiable at pre-commit:
    - bash: `grep -A8 "five-point check" usage-guide.md` shows enumeration.
    - bash: `grep -nE "Three-endpoint poll|Branch tip-SHA|File content audit|Phantom-action audit|Comment-content claim" usage-guide.md` returns 5+ lines (anchors present in §9.10 + §13 one-page reference).

13. **§23.6 sub-section enumeration correct.** usage-guide.md §9.7 enumerates §23.6.1 (prose-arithmetic) + §23.6.2 (iterative-to-fixed-point) + §23.6.3 (reference-verification) in canonical order. Verifiable at pre-commit:
    - bash: `grep -nE "§23\.6\.[123]" usage-guide.md` returns lines covering all three sub-sections in §9.7 + §13 one-page reference.

14. **(j) all-instances grep sweep across all artifacts** authored or modified this cycle. Verifiable at pre-commit:
    - bash: `grep -nE "(core\.md|github-reference\.md|usage-guide\.md|ADR-00[0-9]+|PMN-00[0-9]+|TASK-[0-9]+|PR-[0-9]+|§[0-9]+(\.[0-9]+)*)" usage-guide.md | wc -l` returns `157` citations for usage-guide.md (substantial citation count given single-document substantive-content cycle; canonical-law-trio cross-references + version-anchor citations + cycle-cross-references).
    - bash: `grep -nE "(core\.md|github-reference\.md|usage-guide\.md|ADR-00[0-9]+|PMN-00[0-9]+|TASK-[0-9]+|PR-[0-9]+|§[0-9]+(\.[0-9]+)*)" docs/handoffs/TASK-0024-usage-guide-substantive-fill.md | wc -l` returns `67` citations for the handoff (post-step-9 self-review fix-up cycle absorbed).
    - bash: `grep -nE "(core\.md|github-reference\.md|usage-guide\.md|ADR-00[0-9]+|PMN-00[0-9]+|TASK-[0-9]+|PR-[0-9]+|§[0-9]+(\.[0-9]+)*)" docs/reviews/PR-29-codex-pre-commit.md | wc -l` returns `60` citations for this review-context (post-step-9 self-review fix-up cycle absorbed).
    - Each citation in newly-authored content (usage-guide.md materialization + handoff + review-context) manually verified against canonical source by Builder at step-9 self-review (j) sweep iteration.

15. **Cumulative-diff-stats per (e.1) sub-rule**: per-file numstat sums reconcile to `git diff --staged --shortstat` total exactly; no `~`-prefixed approximate counts in any artifact. Pre-commit (staged-aware) form per TASK-0023 cycle-close N4 observation. Final landed at step-12 commit:
    - bash: `git diff --staged --numstat origin/main` returns 4 rows (full per-file numstat at staged-tree state at step-9 self-review iteration): `382	3	usage-guide.md` + `2	2	README.md` + `171	0	docs/handoffs/TASK-0024-usage-guide-substantive-fill.md` + `106	0	docs/reviews/PR-29-codex-pre-commit.md`. Step-11 Codex absorption iteration extends handoff (cycle-close-ledger entries N1-N10 + Validation run rewrite) and this review-context (Codex output absorption section); final landed numstat re-derived at step-12 commit.
    - bash: `git diff --staged --shortstat origin/main` at step-9 returns `4 files changed, 661 insertions(+), 5 deletions(-)`; final landed shortstat at step-12 commit reflects step-11 Codex absorption iteration deltas.
    - Sum-stability check at step-9: insertion-column sum 382+2+171+106 = 661 ✓; deletion-column sum 3+2+0+0 = 5 ✓. Step-12 final-landed sum-stability check applied at commit time. All cited counts in this review-context (claims 1, 2, 4, 7, 8, 14, 15) re-derived from current staged state at pre-commit; no approximate (`~`-prefixed) counts.

16. **Severity taxonomy three-level enumeration** present in this review-context per Metadata bullet (Blocking / Major / Minor). PMN-004 §5 (a) standing.

## Reviewer focus (Codex desktop)

For each Builder claim above, verify the verification command produces the asserted result. Specific focus areas:

- **§4 content prescription self-application sweep**: usage-guide.md substantive content describes operational disciplines being canonicalized at this very project. Verify the disciplines as described match canonical-text-state (cross-document state verification at the canonical-law-trio surface). Specific check: §7.6 five-surface enumeration matches PMN-008 §3.2; §8.5 three-tier framing matches transition plan v0.2 Decision E; §9.7 §23.6.1/2/3 enumeration matches core.md §23.6 parent prose post-TASK-0023 amendment; §9.10 five-point post-handback check matches core.md §24.3.1.
- **Path B qualifier convention coverage**: novel convention introduced this cycle per Architect adjudication of (i.5)(c) MAJOR finding at step-1 stop-and-show. Verify: every forward-referenced core.md §-citation site (12 distinct sections × multiple occurrence sites) carries the qualifier `(forthcoming at Part C+)` in the form `core.md §X.Y (forthcoming at Part C+)` or naked-context-resolves-to-core.md form `(§X.Y (forthcoming at Part C+))`; usage-guide's own section anchors (§3.1, §5.4, §8.2, §8.3, §10.5 as section headings) intentionally do not carry the qualifier. No phantom citations to forthcoming sections that lack the qualifier.
- **(g)/(h)/(i) sweep on this review-context's own claim blocks**: each claim's verification command timing labels match what the command produces (g.1); example outputs match labels (g.2); commands prove what they claim (h.2); §-citations resolve against HEAD canonical set (i.5).
- **Forward-reference convention coverage**: verify each "(forthcoming at TASK-####+)" qualifier for forward-referenced files is consistent with ADR-003 D2 PR plan + cycle-close-ledger contingency-slot accounting (TASK-0025+ for prompts + project-types appendices; TASK-0026+ for documentation-mcp-options + amas-vs-other-frameworks + regulated-tier-extension appendices).
- **v3 framing adaptation correctness**: usage-guide content preserves v2.14.1 substantive guidance per transition plan v0.2 Decision A (restructure-only); v3 expansion absorbing PMN-002–PMN-009 evolution + ADR-003/004 + three-tier framing + multi-surface review pipeline; v3 reduction dropping v2.14.1 §11.3–§11.6.3 + §10.22–§10.27 version-specific changelog. Verify §-citation consistency across the full content surface; cascade-miss class is the largest risk per PMN-009 + (i.5)(c) MAJOR finding precedent.

## Codex desktop pre-commit output absorption

Codex desktop pre-commit pass executed by owner per ADR-001 D11. Findings: 2 Major + 1 Minor.

### Finding 1 [Major] — Branch convention drift in usage-guide.md §3.3 + §5.3

**Codex finding (verbatim summary)**: usage-guide.md §3.3 + §5.3 use `<type>/<id>-<summary>` form (examples `feat/0001-session-export`, `feat/0042-session-export`) which conflicts with repo operating instructions and current branch shape `<type>/task-####-<slug>`. PMN-008 explicitly recorded this branch-regex divergence as active watch for the usage-guide cycle. Confidence: 0.84.

**Adjudication path**: **Path α — record-and-proceed** (Architect adjudication; owner-confirmed).

**Reasoning**:
- usage-guide.md §3.3 + §5.3 align with sibling v3 canonical-law-trio member `github-reference.md §2.2` (which canonicalizes `<type>/<id>-<summary>` form at line 79). v3-internal consistency holds across both shipping v3 documents.
- Drift is at v2.14.1 ↔ v3 transition boundary (AGENTS.md/CLAUDE.md cite "AMAS v2.14.1 §6.1" form `<type>/task-####-<kebab-slug>`), not within-v3 defect.
- Path β would create new within-v3 drift between sibling canonical-law-trio documents — strictly worse than current state.
- Path γ (surgical scope-expansion to amend github-reference.md §2.2 + usage-guide.md together) exceeds spec §2 deliverable boundaries; surgical-or-defer guard active per PMN-006 precedent.
- Path δ (defer to follow-up TASK) is premature: AGENTS.md/CLAUDE.md → v3 migration cycle is the natural ADR-warranted surface where this question must be resolved with all surfaces in view.

**Cycle-class**: genuinely-asymptotic per §8.1.1.3 (requires structural decision; not pure-token-swap). No in-cycle Builder-side mechanical fix.

**PMN-008 watch carry-forward**: status remains active. AGENTS.md/CLAUDE.md → v3 migration cycle is the natural ADR-warranted surface for reconciliation. Substantive direction-decision deferred to that cycle.

**Substantive direction-observation (out of scope this cycle, surfaced at Architect adjudication for future-ADR awareness)**: lived practice `<type>/task-####-<kebab-slug>` threads TASK-#### into branch names, reinforcing AMAS's TASK-#### centrality and making branches self-documenting. The `feat/123-auth-refresh` form looks like generic git-flow imported from issue-based workflows; "123" doesn't map to AMAS's organizing principle since AMAS doesn't use issue numbers as primary identifiers. Possible TASK-0017 github-reference.md authoring imported a generic example without consulting AMAS's TASK-#### centrality. Future ADR cycle's likely conclusion: v3 trio adopts the lived form. Confidence on substantive direction: medium-high (not load-bearing for this cycle's routing).

### Finding 2 [Major] — Review-context unfilled placeholders at Claims 14 + 15

**Codex finding (verbatim summary)**: Claims 14 and 15 contained `Builder fills exact value/counts` placeholders and Claim 15 used `X insertions / Y deletions`, despite the same review-context asserting no future-tense claims and exact staged-tree verification. Confidence: 0.92.

**Adjudication path**: **path-(a) in-cycle correction** (Architect adjudication; owner-confirmed; bundled with Finding 1 routing in single iteration).

**Cycle-class**: pure-token-swap per §8.1.1.3 (mechanical substitution of concrete values; one-iteration fixed-point convergence; no Codex re-invocation per cost-class refinement).

**Fix-up applied** (this iteration; values from canonical spec §3 step 9 (j) sweep regex):
- Claim 14 (j) sweep counts: usage-guide=`157`, handoff=`67`, review-context=`60`. Codex's regex variant reported 157/68/61 — 1-line systematic delta on handoff + review-context likely reflects regex-clause difference, not noise; canonical spec regex produces 157/67/60.
- Claim 15 numstat: `382 3 usage-guide.md` + `2 2 README.md` + `171 0 docs/handoffs/TASK-0024-usage-guide-substantive-fill.md` + `106 0 docs/reviews/PR-29-codex-pre-commit.md`.
- Claim 15 shortstat: `4 files changed, 661 insertions(+), 5 deletions(-)`.
- Claim 15 sum-stability check: insertions 382+2+171+106 = 661 ✓; deletions 3+2+0+0 = 5 ✓.

**Regex-delta sub-observation**: 1-line systematic delta between canonical (j) sweep regex (Builder; spec §3 step 9) and Codex regex variant on handoff (67 vs 68) and review-context (60 vs 61). Pattern is systematic, not random — likely regex-clause difference (e.g., extra anchor or unanchored boundary). Carry to cycle-close ledger as monitoring observation; future-cycle PMN-eligible if pattern recurs.

### Finding 3 [Minor] — Spec internal inconsistency (`13 sections` vs actual 14)

**Codex finding (verbatim summary)**: Spec at `.claude/session-handoffs/TASK-0024-spec.md` line 119 says "13 top-level §-sections (§0–§12 + one-page reference at §13)", but §0 through §13 inclusive is 14 sections. Spec §7 Claim 1 correctly says 14. Pure-token-swap wording defect. Confidence: 0.98.

**Adjudication path**: **path-(β) record-and-proceed** (Architect adjudication; owner-confirmed).

**Reasoning**: Spec file is gitignored per ADR-001 D15; out of scope for PR commit. Discipline observation: this is *within-spec* drift (distinct class from §23.6.3 *cross-document* drift) — internal-consistency category in spec-authoring discipline namespace, not reference-verification category.

**Cycle-class**: out-of-scope (gitignored); no in-cycle artifact change. Cycle-close-ledger entry; refinement-eligible at future PMN authoring (could fold into PMN-010 as co-class observation, or stand alone — framing decision deferred to TASK-0025 PMN-010 authoring time when full evidence base is in view).

### Verified passing claims (Codex confirmed)

All 16 Builder claims verified passing except Finding 2 (placeholders) and Finding 1 (substantive content drift). Specifically Codex confirmed:

- Staged tree: 2 modified + 2 added (claim 1) ✓
- usage-guide.md: 388 lines, 14 §-section headings, frontmatter correct (claim 2) ✓
- core.md citations resolve for §8.1.1*, §17, §18, §23.6*, §24* (claim 3) ✓
- Path B qualifier coverage: 27 instances on 20 lines; per-section counts match the claim (claim 4) ✓
- github-reference.md citations resolve (claim 5) ✓
- Forward-reference file qualifiers (claim 6) ✓
- README.md Class A v-bump v2.20→v2.21 (claim 7) ✓
- README.md per-PR-row update PR-29 (TASK-0024) (claim 8) ✓
- Class B/C version markers preserved (claim 9) ✓
- PMN-008 five-surface pipeline match (claim 10) ✓
- Three-tier solo-operator framing (claim 11) ✓
- §24.3.1 five-point check enumeration (claim 12) ✓
- §23.6 sub-section enumeration (claim 13) ✓
- Cumulative-diff-stats reconciliation (claim 15 — values now substituted) ✓
- Severity taxonomy three-level (claim 16) ✓
- `git diff --staged --check` clean ✓

### (i.5) cumulative empirical record update

**16th cumulative-record confirmation**: Codex pre-commit catch on Finding 1 (branch-convention drift) — first downstream-gate catch surface where Codex flagged a pre-existing v2.14.1↔v3 drift not surfaced at Builder pre-flight (i.5)(c) because pre-flight scope was forward-ref §-citations within v3, not branch-name-shape cross-doc consistency. Adds Codex-pre-commit-surface to (i.5) catch-surface segmentation: was {Builder pre-flight, Codex pre-commit, GitHub PR-open API} for forward-ref-§-citation class; now {Builder pre-flight (forward-ref-§-citation class), Codex pre-commit (cross-doc-shape-drift class)} segmentation. Strengthens PMN-010 evidence base for TASK-0025+ authoring with surface-class segmentation detail.
