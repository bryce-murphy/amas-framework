---
status: recorded
---

# PR-25 Codex desktop pre-commit review context

## Metadata

- PR ID: PR-25
- TASK ID: TASK-0021
- Branch: `feat/task-0021-three-endpoint-poll-canonicalization`
- Base SHA: `a88b410e5e70bdef043278f22253dd19ff364616` (squash-merge of PR-24 chore on main, 2026-05-04 17:15:54Z)
- Builder: Claude Code (Claude Opus 4.7, Windows 11 + Git Bash)
- Reviewer: Codex (GPT-5.5) — desktop, pre-commit, untracked working tree
- Architect (this PR's): Claude Opus 4.7 (Claude.ai Project)
- Owner: Bryce Murphy (`@bryce-murphy`)
- Framework version: AMAS v2.18.1 → v2.19 (dogfooded post-§18.4 substantive-reading minor bump applied this cycle — second minor-tier bump after v2.17 → v2.18 at PR-21; new canonical text at core.md §8.1.1.1 absorbing PMN-008 §5.8 (h.4) recommendation + new PMN-009 documenting (i.5) Architect-spec-drift catch discipline canonicalization-candidate)
- Severity taxonomy: Blocking / Major / Minor (three-level; per repo discipline; standing per PMN-004 §5 (a))
- Disciplines applied (PMN-004 §5 (a)-(f) + PMN-005 sub-rule (e.1) + PMN-006 (g)/(h)/(i) + PMN-006 §5.3 bounded-continuation rule generalized + PMN-006 §3.4 frontmatter-vs-body sub-clause + PMN-007 §2.4 cost-class refinement + PMN-007 §3.1 four-surface iterative-pre-flight + iterative-post-PR-review pattern + PMN-007 §9.1 (i) extended pre-authoring verification batch + PMN-007 §4 PMN-001 (k) mechanism-vs-discipline canonicalization + PMN-008 §3.2 five-surface review pipeline + PMN-008 §4.2 (i.5) convention-inference verification with PMN-file-shape sub-extension + PMN-008 §5.8 (h.4) three-endpoint Codex poll discipline NOW CANONICAL at core.md §8.1.1.1 per this cycle's amendment): severity taxonomy three-level (a); verification-command portability (b); no future-tense pre-commit claims (c); pre-commit cross-surface scope clarity (d); §23.6 prose-arithmetic decomposition (e) with sub-rule (e.1) cumulative-diff-stats re-derivation; section-citation correctness sweep (f); verification-artifact internal consistency (g); verification-command operational correctness (h) with sub-shapes (h.1)/(h.2)/(h.3)/(h.4); cross-document state verification (i) with sub-shapes (i.1)/(i.2)/(i.3)/(i.4)/(i.5); §23.6.2 iterative-to-fixed-point self-review; §8.1.1.3 bounded-continuation rule with cost-class refinement.
- Substantive-content-cycle context: PR-25 is the canonical-text-amendment cycle for the (h.4) Codex-output-endpoint-coverage discipline matured across 8 cycles (PR-11 / PR-13 / PR-15 / PR-17 / PR-19 / PR-21 / PR-23 / PR-24). Three coupled deliverables co-shipped per Architect Phase 1 Q1 bundling adjudication: (1) core.md §8.1.1.1 surgical amendment adding `pulls/{pr}/comments` as third polling endpoint with parallel (h.3) lexicographic OR form, refining (h.4) pattern via empirical-pattern note, updating settling-period rule (token-swap-only per Architect Q2 adjudication; no new numeric prose introduced), correcting endpoint (a) description per PMN-008 §5.8 framing per Architect Q1 adjudication; (2) PMN-009 authoring documenting (i.5) Architect-spec-drift catch discipline with 4 cross-cycle field evidence + recommended §23.6 sub-rule (g) addition (canonical absorption deferred to TASK-0022+ per PMN-005 propose-then-absorb cadence); (3) operational hygiene + version bump — `.gitignore` `__pycache__/` Python-group addition (cycle-close ledger Item 14); README.md Class A canonical-version-of-record bump v2.18.1 → v2.19. Builder pre-flight surfaced 4 stop-and-show questions (Q1 endpoint (a) rewrite scope; Q2 settling-period prose form; Q3 Class A v-bump scope confirmation; Q4 .gitignore placement convention) — all four adjudicated by owner before branch creation; no convention-divergence findings against (i.5) batch sample reads.

## Builder claims to verify

The Builder asserts the following at hand-off to Codex desktop pre-commit review. Each claim is verifiable from the working tree at pre-commit time (no future-tense claims per PMN-004 §5 (c)). PR-25 ships the core.md §8.1.1.1 three-endpoint canonicalization + PMN-009 + TASK-0021 handoff + PR-25 review-context + README.md Class A v-bump v2.18.1 → v2.19 + `.gitignore` `__pycache__/` Python-group addition.

1. **Working-tree state: 3 new files + 3 modified files**. Verifiable at pre-commit per (c) + (h.2) discipline (working-tree-aware forms; no future-tense commit-time semantics).
   - bash (pre-commit, untracked-aware): `git status --porcelain | grep -c "^??"` returns `3` (3 NEW: `docs/handoffs/TASK-0021-three-endpoint-poll-canonicalization.md` + `docs/post-merge-notes/PMN-009-i5-architect-spec-drift-catch-discipline.md` + `docs/reviews/PR-25-codex-pre-commit.md`).
   - bash (pre-commit, modified-aware): `git status --porcelain | grep -c "^ M"` returns `3` (3 modified: `core.md`, `README.md`, `.gitignore`).
   - bash (pre-commit baseline): `git ls-files | wc -l` returns `108` (untracked files not counted). Post-stage (after `git add` of the 3 new files): `git ls-files | wc -l` returns `111`.

2. **§8.1.1.1 amendment surgical scope honored** per spec §4 surgical-or-defer guard + Architect Q1/Q2 adjudications: the amendment is confined to lines 23–60 of pre-amendment core.md (the §8.1.1.1 subsection); no surrounding subsection is touched; §8.1.1.1's structural shape (heading, endpoint enumeration, pass-shape paragraph, Builder-discipline + bash block, lexicographic-explanation paragraph, --paginate paragraph, reconciliation paragraph, Anti-channel paragraph, Cross-reference paragraph) is preserved with localized edits inside each. No subsection inserted; no paragraph reordered. Verifiable at pre-commit:
   - bash: `git diff origin/main -- core.md` shows §8.1.1.1 hunk additions confined to that subsection (the next-following subsection `##### §8.1.1.2.` heading line is unmodified at line 70 in post-amendment; line 62 in pre-amendment; the 8-line offset matches the §8.1.1.1 hunk's net +8 lines exactly), verifiable via `grep -n "^##### §8.1.1.2" core.md`. Cross-reference cluster fix-up at L17 / L21 / L72 / L331 absorbed in same commit per Codex Blocking adjudication (Architect Item 1 path-α); see Adjudication and fix-up section below for scope.
   - bash: `git diff --numstat origin/main -- core.md` returns the post-fix-up numstat for core.md (§8.1.1.1 hunk + 4 cross-reference fix-up locations); see Adjudication section below for current values.
   - bash: `wc -l core.md` returns the post-fix-up line count.

3. **§8.1.1.1 third endpoint canonical form** — `pulls/{pr}/comments` polling endpoint added with parallel timestamp filter form to the existing two endpoints; (h.3) lexicographic OR form preserved per PMN-006 precedent. Verifiable at pre-commit:
   - bash: `grep -n "Endpoint (c)" core.md` returns one line in the bash block plus the `(c) **Line-level review comments**` enumeration item.
   - bash: `grep -nE "pulls/\{(owner|pull_number)\}.*comments" core.md` returns lines for the new endpoint (c) bash query block and the new (c) enumeration item, both referencing `pulls/{pull_number}/comments`.
   - bash: the lexicographic OR form `select(.created_at > "<last-known>" or (.created_at == "<last-known>" and .id > <last-seen-id>))` appears in the new (c) bash block byte-exactly matching the existing (b) bash block's `created_at` form (per (h.3) discipline; preserved verbatim).

4. **§8.1.1.1 (h.4) pattern refinement and settling-period token-swap (Architect Q2 adjudication: token-swap only; no new numeric prose introduced)**. Verifiable at pre-commit:
   - bash: the new `**Empirical pattern (substantive-verdict landing surface).**` paragraph exists in the amended §8.1.1.1, naming "any one of the three endpoints" and enumerating the (a)/(b)/(c) cases plus joint-emission case.
   - bash: `grep -n "polling cadence" core.md` returns exactly one line (the existing wording preserved); `grep -nE "5.{1,3}10 ?minute" core.md` returns no lines (no numeric "5–10 minute settling period" prose introduced — Architect Q2 token-swap-only adjudication honored).
   - bash: `grep -cE "(both|three) endpoints" core.md` shows post-amendment uses "all three endpoints" / "across all three endpoints" forms; `grep -nE "\bboth endpoints\b" core.md` returns no matches in §8.1.1.1 (token-swap from "both" → "all three" applied at all reconciliation/settling-period prose surfaces).

5. **§8.1.1.1 endpoint (a) description rewrite per Architect Q1 adjudication (PMN-008 §5.8 framing)**: endpoint (a) description corrected from "carries line-anchored substantive findings when they exist" (pre-amendment) to "carries the PR-level review summary state machine (APPROVED / CHANGES_REQUESTED / COMMENTED) and the substantive review body prose..." (post-amendment); endpoint (c) is now the canonical home for "line-anchored substantive findings". Verifiable at pre-commit:
   - bash: `grep -n "review summary state machine" core.md` returns one line (the new (a) description).
   - bash: `grep -n "line-anchored substantive findings" core.md` returns one line — at endpoint (c)'s description, not at endpoint (a) (the value moved between endpoints; the phrase appears exactly once post-amendment).
   - bash: `git diff origin/main -- core.md` shows the (a) description rewrite as a single-item rewrite within the existing enumeration, not subsection-level restructuring.

6. **§8.1.1.1 PMN-008 §5.8 (h.4) absorption cross-reference note**: the Cross-reference paragraph now records that the three-endpoint enumeration "absorbs the recommendation matured at PMN-008 §5.8 (h.4) across 8 cycles' empirical evidence (PR-11 / PR-13 / PR-15 / PR-17 / PR-19 / PR-21 / PR-23 / PR-24)". Verifiable at pre-commit:
   - bash: `grep -n "PMN-008 §5.8" core.md` returns one line in the Cross-reference paragraph; cycle enumeration `PR-11 / PR-13 / PR-15 / PR-17 / PR-19 / PR-21 / PR-23 / PR-24` appears verbatim.

7. **PMN-009 form conformance** per PMN-006 + PMN-008 priors. Verifiable at pre-commit:
   - bash: PMN-009 frontmatter contains `post_merge_note_id: PMN-009` + `title:` + `linked_pr:` + `framework_version_dogfooded: AMAS v2.18.1` + `status: drafted` (5 fields matching PMN-008 frontmatter shape).
   - bash: `grep -cE "^#" docs/post-merge-notes/PMN-009-i5-architect-spec-drift-catch-discipline.md` returns `10` (10 structural headings: `# PMN-009 — title` + `## Status` + `## §1. Cycle context` + `### §1.1. Honesty record` + `## §2. Sub-shape characterization` + `## §3. Common root cause` + `## §4. Catch-surface analysis` + `## §5. Recommended canonical refinement` + `## §6. Anticipated forward integration` + `## §7. Cross-references`).
   - bash: `wc -l docs/post-merge-notes/PMN-009-i5-architect-spec-drift-catch-discipline.md` returns `96` (under spec §5 target 150-220 line range; content-complete across all prescribed §-sections; surfaced at step-9 self-review for owner judgment).

8. **PMN-009 sub-shape characterization correctness**: 4 sub-shapes A/B/C/D enumerated in §2 with each sub-shape traceable to specific cycle-evidence data points enumerated in §1.1. Verifiable at pre-commit:
   - bash: `grep -nE "Sub-shape [ABCD]" docs/post-merge-notes/PMN-009-i5-architect-spec-drift-catch-discipline.md` returns 8 lines (4 sub-shape enumerations in §2 + 4 sub-shape attributions in §1.1 data points 1-4).
   - bash: §1.1 data points 1-4 are individually attributed to TASK-0019 (data point 1 → sub-shape A; data point 4 → sub-shape D) and TASK-0020 (data point 2 → sub-shape B; data point 3 with two sub-instances 3a + 3b → sub-shape C) cycle-evidence; data points 1, 2, 4 caught entirely at Builder pre-flight (i.5) batch; data point 3 caught at two surfaces (3a Builder pre-flight + 3b Codex pre-commit).

9. **PMN-009 canonical refinement recommendation deferral**: PMN-009 §5 proposes §23.6 sub-rule (g) addition; canonical absorption explicitly deferred to TASK-0022+ per PMN-005 propose-then-absorb cadence (recommendation, not amendment). Verifiable at pre-commit:
   - bash: `grep -n "deferred to TASK-0022" docs/post-merge-notes/PMN-009-i5-architect-spec-drift-catch-discipline.md` returns one line in §5 stating absorption deferral; `grep -n "PMN-005" docs/post-merge-notes/PMN-009-i5-architect-spec-drift-catch-discipline.md` returns lines invoking the propose-then-absorb precedent.
   - bash: no `core.md` modification at §23.6 in this PR's diff: `git diff origin/main -- core.md | grep -nE "^\+.*§23\.6"` returns no additions naming §23.6 (PMN-009 proposes; absorption deferred; no canonical text touches §23.6 this cycle).

10. **(j) all-instances grep sweep** across all artifacts authored or modified this cycle. Verifiable at pre-commit:
    - bash: `grep -nE "(core\.md|github-reference\.md|ADR-00[0-9]+|PMN-00[0-9]+|TASK-[0-9]+|PR-[0-9]+)" docs/post-merge-notes/PMN-009-i5-architect-spec-drift-catch-discipline.md | wc -l` returns `28` (citations across §1, §1.1 data points, §2, §3, §4, §5, §7 cross-references). Each citation manually verified against the canonical source by Builder at step 9 self-review (j) sweep iteration.
    - bash: `grep -nE "(core\.md|github-reference\.md|ADR-00[0-9]+|PMN-00[0-9]+|TASK-[0-9]+|PR-[0-9]+)" docs/handoffs/TASK-0021-three-endpoint-poll-canonicalization.md | wc -l` returns substantial citation count (handoff embeds spec-prescription content + cycle-reference enumerations).
    - bash: `grep -nE "(core\.md|github-reference\.md|ADR-00[0-9]+|PMN-00[0-9]+|TASK-[0-9]+|PR-[0-9]+)" docs/reviews/PR-25-codex-pre-commit.md | wc -l` returns this review-context's citation count.
    - bash: `grep -nE "(PMN-00[0-9]+|PR-[0-9]+)" core.md` returns the §8.1.1.1 Cross-reference paragraph's PMN-008 §5.8 + 8-cycle enumeration; verified.

11. **Class A v-bump applied per Q3 adjudication**: README.md line 9 `v2.18.1` × 2 → `v2.19` × 2; no `v2.18.1` remaining at Class A canonical-version-of-record surface. Verifiable at pre-commit:
    - bash: `grep -nE "v2\.19" README.md` returns line 9 (with two `v2.19` instances on the same line per Class A surgical edit shape).
    - bash: `grep -nE "\bv2\.18\.1\b" README.md` returns no lines (Class A surgically migrated; no residual at canonical version-of-record surface).
    - bash: `git diff --numstat origin/main -- README.md` returns `1	1	README.md` (single-line replacement; both Class A instances on the same physical line).
    - Class B/C version markers preserved verbatim: `grep -cE "v2\.14\.1" AGENTS.md CLAUDE.md docs/adr/ADR-001-initial-repo-setup.md` returns the existing `v2.14.1` operating-framework anchor counts unchanged from `origin/main`; `grep -cE "v2\.(14|15|16|17|18)" core.md` historical-anchor counts unchanged.

12. **`.gitignore` `__pycache__/` addition per Q4 adjudication**: new `# Python` group appended at end-of-file with `__pycache__/` pattern; pre-existing entries unchanged. Verifiable at pre-commit:
    - bash: `git diff origin/main -- .gitignore` shows additive 3-line block (`<blank-line>` + `# Python` + `__pycache__/`); no pre-existing line modified.
    - bash: `git diff --numstat origin/main -- .gitignore` returns `3	0	.gitignore` (3 insertions, 0 deletions).
    - bash: `git status --porcelain | grep "__pycache__"` returns no lines (the `.github/scripts/__pycache__/` directory that previously appeared as untracked is now excluded by the new .gitignore entry).

13. **TASK-0021 handoff structural-headings count + section ordering** matches TASK-0019 + TASK-0020 priors per PMN-007 HEAD canonical 12-field frontmatter convention. Verifiable at pre-commit:
    - bash: `grep -cE "^#" docs/handoffs/TASK-0021-three-endpoint-poll-canonicalization.md` returns `38` (matches the spec-prescribed structural-heading count for substantive-content cycle handoffs of this scope).
    - bash: TASK-0021 frontmatter contains 12 fields (`task_id`, `title`, `pr`, `branch`, `linked_predecessor`, `linked_successor`, `linked_pr`, `framework_version_dogfooded`, `production_target`, `spec_source`, `date_authored`, `status`); identical field set to TASK-0019 + TASK-0020 priors per PMN-007 HEAD canonical 12-field convention.
    - bash: `grep -nE "^## " docs/handoffs/TASK-0021-three-endpoint-poll-canonicalization.md` returns the canonical section sequence Metadata → Objective → Last completed step → Current state → Decisions made → Assumptions → Risks → Blocking questions → Validation run → Exact next step → §-prescription sections → Reassessment → Post-PR Codex review state → Sign-off → Session log archive.

14. **Cumulative-diff-stats self-stability** per (e.1) sub-rule: per-file numstat sums match `git diff --staged --shortstat` total exactly; no `~`-prefixed approximate counts in any artifact. Pre-commit (untracked-aware) form:
    - bash: `git diff --numstat origin/main` returns 3 rows for modified files (`3	0	.gitignore` + `1	1	README.md` + `19	11	core.md`); modified-only sum is `23 insertions / 12 deletions`.
    - bash: post-stage (`git add` of all 3 new files + 3 modified files), `git diff --staged --shortstat origin/main` will return cumulative additions = modified-only 23 + new-file source-line counts (PMN-009 + TASK-0021 handoff + PR-25 review-context, each verifiable via `wc -l`); deletions remain at 12. Sum-stability claim: per-file `git diff --staged --numstat` insertion-column sum equals the shortstat insertions count exactly at any pre-commit moment.
    - All cited counts in this review-context (claims 1, 2, 7, 10, 11, 12, 13) re-derived from current working-tree state at pre-commit; no approximate (`~`-prefixed) counts. The handoff Validation run section quotes specific blob hashes + line counts captured at step-9 self-review snapshot; if the handoff is further edited between step-9 and Codex pre-commit, blob hashes drift and Builder records the post-edit hashes at step-10 stop-and-show.

15. **M-A7 enumeration verification**: PR-25 = 9th empirical instance per `PR-9 + PR-10 + PR-11 + PR-13 + PR-15 + PR-17 + PR-19 + PR-21 + PR-25 = 9` (substantive-cycle PR enumeration; defect-fix PR-23 + chore-fix-up PRs PR-22/PR-24 are M-A7 ineligible per the established class distinction). Verified by explicit enumeration before authoring per the PR-17 cycle close lesson. Architect performs the actual M-A7 amendment post-merge per core.md §18.3; PR-25 review-context records the count for forward reference.

16. **Self-instantiation note** (informational, not a verification claim): PR-25 ships the canonical text for the very three-endpoint poll discipline that will be applied at PR-25 post-PR Codex review absorption (step 15 of the spec). The amended §8.1.1.1 canonical text's first canonical-application is the absorption surface for Codex's review of PR-25 itself. Recursive self-instantiation pattern; surfaced for Architect step-17 hand-back monitoring per (h.4) absorption-discipline gap analog.

## Codex desktop pre-commit kickoff (copy-paste-ready)

```
PR-25 (TASK-0021) ships three coupled deliverables:

1. core.md §8.1.1.1 surgical amendment — adds `pulls/{pr}/comments` as third polling endpoint with parallel (h.3) lexicographic OR timestamp filter; rewrites endpoint (a) description per PMN-008 §5.8 framing (PR-level review summary state machine; substantive review body); adds empirical-pattern note ("substantive verdict can land at any of three endpoints"); updates settling-period rule via token-swap only ("both endpoints" → "all three endpoints"; no new numeric prose). Cross-reference paragraph absorbs PMN-008 §5.8 (h.4) recommendation matured across 8 cycles. Net +8 lines (19 insertions / 11 deletions).

2. PMN-009 — documents (i.5) Architect-spec-drift catch discipline canonicalization-candidate with 4 cross-cycle field evidence data points decomposed into 4 sub-shapes (A frontmatter / B structural-element count / C line-number / D form). Proposes §23.6 sub-rule (g) addition for Architect-side reference-verification before spec authoring. Canonical absorption deferred to TASK-0022+ per PMN-005 propose-then-absorb cadence (PMN-009 ships as recommendation, NOT amendment to §23.6 canonical text this cycle).

3. Operational hygiene + Class A v-bump — README.md line 9 `v2.18.1` × 2 → `v2.19` × 2 per §18.4 minor criterion; .gitignore new `# Python` group with `__pycache__/` exclusion per Architect Q4 adjudication.

Working tree at pre-commit (post-Codex-fix-up absorption): 3 new files + 3 modified files; modified-files post-fix-up sum recorded in Adjudication and fix-up section below; new-file source-line counts each verifiable via `wc -l`. No `~`-prefixed approximate counts in any artifact per (e.1) self-stability discipline.

Please review against the 16 Builder claims in `docs/reviews/PR-25-codex-pre-commit.md`. Particular attention to:
- Claim 2 surgical-or-defer attestation: §8.1.1.1 amendment is confined to the subsection; structural shape preserved; no subsection inserted; no paragraph reordered.
- Claim 4 settling-period token-swap-only: no "5–10 minute" numeric prose introduced; loose "polling cadence" wording preserved per Architect Q2 adjudication.
- Claim 5 endpoint (a) rewrite: line-anchored substantive findings phrase moved from endpoint (a) to endpoint (c); endpoint (a) now reflects PMN-008 §5.8 framing (review summary state machine).
- Claim 9 PMN-009 absorption deferral: no §23.6 canonical text amendment this cycle; the proposal lands at PMN-009 §5 only.
- Claim 10 (j) sweep: ~30 §-citations across artifacts; verify each against canonical source.
- Claim 14 cumulative-diff-stats self-stability: all counts pre-commit-verifiable; no approximations.

Severity taxonomy: Blocking / Major / Minor.
```

## Codex desktop pre-commit output

Codex returned **Request changes** with 1 Blocking + 3 Major + 1 Minor. Verbatim output:

> **Review Summary**
>
> Recommendation: **Request changes**.
>
> Blocking:
> - `core.md` still contains canonical two-channel/two-endpoint instructions outside the surgical hunk: lines 17, 21, 72, and 331. That blocks the "three-endpoint discipline now canonical" claim from being safely true.
>
> Major:
> - PMN-009's A/B/C/D evidence decomposition is not verified: §1.1 has A/B/C/C-variant, while D is introduced later as extra evidence.
> - PMN-009 is 96 lines against the handoff's 150-220 source-line target, unless the owner explicitly accepted that target miss.
> - Cumulative diff/count artifacts are stale: actual cumulative pre-stage is `673 insertions / 12 deletions`, and new files are `96 + 430 + 124 = 650` source lines.
>
> Minor:
> - Claim 2's review-context line note says §8.1.1.2 is post-amendment line 65; actual current line is 70. The user prompt's line-70 framing is correct.
>
> **Claim Verification**
>
> 1. Verified: working tree is 3 modified + 3 untracked; tracked count is 108.
> 2. Partially verified: §8.1.1.1 hunk is surgical, `19/11`, `core.md` is 339 lines, next heading is line 70. The line-65 claim is stale, and stale surrounding references remain.
> 3. Verified: endpoint (c) and matching `created_at` lexicographic filter are present.
> 4. Verified within §8.1.1.1: no `5–10 minute` prose; one `polling cadence`; no `both endpoints`.
> 5. Verified: endpoint (a) has review state machine wording; line-anchored findings phrase appears only at endpoint (c).
> 6. Verified: PMN-008 §5.8 and the 8-cycle PR list appear in the cross-reference.
> 7. Partially verified: PMN form/headings/frontmatter verified; line target not met.
> 8. Not verified: A/B/C/D traceability to four §1.1 data points is inconsistent.
> 9. Verified: PMN defers §23.6 absorption; no `core.md` diff additions naming §23.6.
> 10. Partially verified: PMN-009 citation count is 28; cited PMN/TASK/ADR files and PR-21/PR-23 SHAs check out. The evidence mapping issue affects the sweep's substantive correctness.
> 11. Verified: README line 9 has two `v2.19` instances and no `v2.18.1`; README diff is `1/1`.
> 12. Verified: `.gitignore` adds blank line + `# Python` + `__pycache__/`; no pycache appears in status.
> 13. Verified: TASK-0021 handoff has 38 headings and 12-field frontmatter matching TASK-0019/0020 shape.
> 14. Not verified: current cumulative count is 673/12 and artifacts still contain approximate/stale counts.
> 15. Verified as forward-reference: origin/main has the listed prior substantive instances; PR-25 would be the ninth if shipped.
> 16. Informational only; no verification finding beyond the blocking stale-reference issue above.

## Adjudication and fix-up

All five Codex findings verified real against working tree at the pre-commit snapshot. Architect adjudicated via the Builder verification + adjudication-routing surface. Per-finding outcomes:

### Blocking — core.md cross-reference cluster (Architect Item 1: path-α; apply within cycle)

**Finding**: core.md L17 (§8.1 parent) + L21 (§8.1.1 frame) + L72 (§8.1.1.2 first paragraph) + L331 (§24.3.1 five-point check item 1) carried stale two-channel/two-endpoint canonical text after the §8.1.1.1 amendment landed, creating internal contradiction at canonical-text scope (§8.1.1.1 says three endpoints; cross-referencing surfaces still said two).

**Adjudication**: path-α expand §4 amendment scope. Architect Phase 1 scoping defect — original §4 prescription was confined to §8.1.1.1's subsection without sweeping cross-referencing surfaces. Cost class bounded (4 surgical token-swaps or single-sentence rewrites; ~6–10 lines net additional change); pure-token-swap class per §8.1.1.3.

**Fix-up applied**:
- L17 §8.1: rewritten to "delivered through three distinct GitHub API endpoints" form; "line-anchored findings" attribution moved off endpoint (a) (now lives at endpoint (c) per Q1 framing); "dual-channel polling discipline" → "three-endpoint polling discipline".
- L21 §8.1.1: "two delivery channels" → "three delivery endpoints".
- L72 §8.1.1.2: "two-endpoint poll of §8.1.1.1" → "three-endpoint poll of §8.1.1.1".
- L331 §24.3.1 item 1: "Two-endpoint poll" → "Three-endpoint poll"; "both formal-review and issue-comment endpoints" → "all three endpoints (formal-review, issue-comment, line-comment)".

Verifiable post-fix-up: `grep -nE "(two-endpoint|two endpoints|dual-channel|two delivery channels|two channels|both formal-review)" core.md` returns no lines.

### Major 1 — PMN-009 sub-shape mapping (Architect Item 2: option (i); 4-to-4 A/B/C/D)

**Finding**: PMN-009 §1.1 enumerated 4 numbered data points mapping to A/B/C/C-variant; §2 introduced sub-shape D as extra evidence with explicit caveat that it was "not numbered as one of the four §1.1 data points". Review-context Claim 8 asserted A/B/C/D traceability to §1.1 data points — self-inconsistent.

**Adjudication**: option (i) renumber §1.1 to 4-to-4 A/B/C/D mapping. Cleaner form per Codex's expected mapping.

**Fix-up applied**:
- Data point 1 unchanged (TASK-0019 frontmatter → sub-shape A).
- Data point 2 unchanged (TASK-0020 ADR-004 §Consequences point-count → sub-shape B).
- Data point 3 combined: TASK-0020 .py line-number (sub-instance 3a; Builder pre-flight catch) + TASK-0020 .yml line-23/24 (sub-instance 3b; Codex pre-commit catch) → sub-shape C with two distinct catch surfaces.
- Data point 4 promoted from §2 narrative to numbered §1.1 entry: TASK-0019 ADR-004 form catch → sub-shape D.
- §2 sub-shape D paragraph simplified — "not numbered" caveat removed; cross-references §1.1 data point 4.
- §4 catch-surface analysis rewritten to reflect the 4-data-point / mixed-catch-surface pattern (data points 1, 2, 4 caught at Builder pre-flight; data point 3 caught at two surfaces — 3a Builder pre-flight + 3b Codex pre-commit).
- §7 Cross-references updated: PR-21 line points to data points 1 + 4 (sub-shapes A + D); PR-23 line points to data points 2 + 3 (sub-shapes B + C two sub-instances).

Review-context Claim 8 holds verbatim post-fix-up.

### Major 2 — PMN-009 line count (Architect Item 3: path-(β) record-and-proceed)

**Finding**: PMN-009 96 lines vs spec §5 target 150-220.

**Adjudication**: path-(β) record-and-proceed per Architect step-10 stop-and-show prior adjudication (this cycle, item 1). Spec §5 target was authored from wrong reference class (PMN-006 / PMN-008 multi-cluster scope); PMN-009 → PMN-005 single-cluster analog holds. Content-complete across §-sections (§1 + §1.1 + §2 + §3 + §4 + §5 + §6 + §7); padding to hit 150-line floor would dilute field-evidence focus.

**Fix-up applied**: no content change to PMN-009 line count; recorded here per PMN-002 (a) verbatim-discipline. Codex flag noted; prior Architect adjudication referenced. Cycle-close ledger Architect-carry: this is empirical evidence that spec target ranges authored without verifying against actual reference-class artifacts is itself a sub-shape of (i.5) Architect-spec-authoring drift — fifth confirming data point for the (i.5) discipline this cycle alone, with PMN-009 itself self-instantiating against this drift class.

### Major 3 — stale cumulative-diff-stats numbers (Architect Item 4: path-(a) revise)

**Finding**: review-context kickoff text quoted "+500 lines on new files; net cumulative ~511 insertions" — stale and approximate per Codex (e.1) sub-rule violation. Handoff Validation run quoted "404 (handoff)" / "624 source lines" / "647 insertions" — also stale.

**Adjudication**: path-(a) revise. Update both surfaces with current 650 / 673 numbers; accept further small drift per "step-9 freeze; will drift modestly from this snapshot per pre-commit absorption" qualifier-prose.

**Fix-up applied**: review-context kickoff text reframed to defer specific numbers to this Adjudication section; handoff Validation run cumulative-diff-stats line updated to current post-fix-up values per the Final-state diff snapshot below.

### Minor 1 — Claim 2 line-65 → line-70 (Architect Item 4: path-(a) revise)

**Finding**: review-context Claim 2 stated "line 65 in post-amendment" for §8.1.1.2 heading. Actual post-amendment line is 70 (62 + net 8 line addition).

**Adjudication**: path-(a) token-swap.

**Fix-up applied**: Claim 2 wording updated to reference line 70 (post-amendment) and the 8-line offset rationale.

### Final post-fix-up state (Builder records at second pre-commit stop-and-show)

Post-fix-up cumulative-diff-stats, blob hashes, and (j)-sweep re-run results recorded by Builder at second stop-and-show before commit. Codex re-invocation: optional per §8.1.1.3 bounded-continuation rule — pure-token-swap fix-ups + structurally-bounded PMN-009 renumbering converge at one-iteration fixed-point per TASK-0019 + TASK-0020 cycle convention.

## Post-PR Codex review absorption

After PR-25 was opened with the original (pre-this-section) commit `e05a92a` pushed to `feat/task-0021-three-endpoint-poll-canonicalization`, owner posted `@codex review` per ADR-001 decision 11 owner-invokes convention. Codex emitted across all three endpoints per the canonical-text-being-shipped's first canonical-application (recursive self-instantiation event). Builder ran the three-endpoint poll per the amended §8.1.1.1 discipline.

### Three-endpoint poll outcomes

| Endpoint | Reviewer | Submitted | State / shape | Substantive content |
|---|---|---|---|---|
| (a) `pulls/25/reviews` | `chatgpt-codex-connector[bot]` | 2026-05-04T19:35:14Z | COMMENTED, boilerplate body | None — review body is "Codex Review" boilerplate ("Here are some automated review suggestions"); no findings in the formal review object |
| (b) `issues/25/comments` | `chatgpt-codex-connector[bot]` | 2026-05-04T19:32:52Z | Summary comment | Phantom-action narrative (§8.1.1.2 Sub-shape A; verified below); recommendation **Comment** with stated "no Blocking/Major findings"; minor maintenance note about line/diff metadata sync |
| (c) `pulls/25/comments` | `chatgpt-codex-connector[bot]` | 2026-05-04T19:35:14Z | Line-level review comment at `core.md:37` | **1 Major-equivalent finding (P2 yellow badge)**: canonical-text contradiction in the freshly-shipped §8.1.1.1 pass-shape vs. empirical-pattern paragraphs |

### Endpoint (b) phantom-action narrative — §8.1.1.2 Sub-shape A

Codex bot autonomous emission at 19:32:52Z claimed three write actions (file `docs/reviews/PR-25-codex-post-pr-review.md`, commit `0a5ff60` titled "docs(review): add PR-25 post-PR codex review summary", `make_pr` PR titled "docs: add PR-25 post-PR Codex review summary artifact"). All three verified phantom per §8.1.1.2:

- File lookup `gh api repos/bryce-murphy/amas-framework/contents/docs/reviews/PR-25-codex-post-pr-review.md`: HTTP 404 Not Found.
- Commit lookup `gh api repos/bryce-murphy/amas-framework/commits/0a5ff60`: HTTP 422 "No commit found for SHA: 0a5ff60".
- Open PR list `gh pr list --state open`: only PR-25 open; no second PR opened.

Sub-shape A discipline applied: informational-only absorption; no defensive write actions taken; cycle decisions do not depend on the claimed actions having occurred.

Cycle-close ledger Item 6 (w) third-instance evidence; PMN-010-co-ship-eligible at TASK-0022 absorption cycle. Pattern characterization across three cycles: TASK-0019 PR-21 cycle (Sub-shape A positive-action claims) + TASK-0020 PR-23 cycle (Sub-shape A-anti / negative-action claims) + TASK-0021 PR-25 cycle (Sub-shape A positive-action claims, this turn). Three cross-cycle data points; promotion-eligible.

### Endpoint (c) Major finding — canonical-text contradiction (P2 / Major-equivalent)

Verbatim Codex line-level comment at `core.md:37`:

> **Reconcile contradictory substantive-pass definitions**
>
> This section now gives conflicting canonical behavior: the "Substantive-finding pass shape" says endpoint output is joint across (a)/(b)/(c), but the new empirical-pattern paragraph says substantive verdicts can appear on only one endpoint (including only (a) or only (c)). That contradiction can cause reviewers/builders to incorrectly treat valid single-endpoint substantive output as missing data or protocol failure. Please make these rules consistent (for example, define substantive passes as appearing on one or more endpoints).

**Verification**: finding is real. The pass-shape paragraph stated "endpoints emit jointly" while the empirical-pattern paragraph stated substantive verdict can land at "any one of the three endpoints". PR-25's own review surface self-instantiated the empirical-pattern reality (endpoint (a) boilerplate-only; endpoint (b) phantom-narrative without verdict-text restatement; endpoint (c) substantive Major) — under the pass-shape's "joint emission" rule, this would not qualify as a substantive-finding pass; under the empirical-pattern's "any one of three" rule, it does. The pass-shape definition required softening to align with the empirical-pattern.

### Adjudication and fix-up — path-(a) Option A surgical pass-shape rewrite

Architect adjudicated path-(a) Option A: surgical-token-swap-equivalent rewrite at the two pass-shape bullet definitions; preserve structural shape (two-pass-shape categorization retained); align with the empirical-pattern's "one or more endpoints emit" framing. Estimated cost class bounded per §8.1.1.3; same class as Q2 settling-period token-swap from earlier this cycle.

**Substantive-finding pass shape** rewritten to: "at least one endpoint carries substantive content. Endpoint (a) may carry the review state plus any review-body prose; endpoint (b) may carry verdict text; endpoint (c) may carry line-anchored findings. Per the empirical-pattern note below, the substantive content distribution across endpoints varies per cycle — Builder polls all three endpoints and reconciles."

**Cycle-trailing-clean-Approve pass shape** rewritten in parallel terms: "no substantive content emits at any endpoint, with formal review state at endpoint (a) reaching APPROVED or remaining COMMENTED with boilerplate-only body (typical body phrasing: 'Codex Review: Didn't find any major issues.'). Builder treats no-substantive-emission across all three endpoints as a clean cycle, subject to the settling-period rule below."

**Verifiable post-fix-up**: `grep -nE "(endpoints emit jointly|only the issue-comment endpoint emits)" core.md` returns no lines (stale assertions removed); grep for the new wording returns the rewritten paragraphs at lines 35-36 of post-fix-up core.md.

### Recursive self-instantiation note

PR-25's own three-endpoint poll absorption surface surfaced a defect in the canonical text being shipped at PR-25 — a defect that prior surfaces (Architect §23.6 self-review, Builder pre-flight (i.5), Codex pre-commit pass 1, Architect adjudication chain) all missed. This is the (r) fifth-surface canonical-refinement pattern self-applying at strongest-possible-strength: the three-endpoint poll discipline this cycle ships catches a defect in this cycle's own canonical-text scope at its own first canonical-application surface. Cycle-close ledger Architect-carry: this is fourth Architect Phase 1 scoping defect this cycle (§4 Amendment 2 named the empirical-pattern note addition but did not name reconciliation of the existing pass-shape definitions with the new empirical-pattern framing); strengthens (i.5) discipline candidate confirming evidence to 7 cross-cycle data points.
