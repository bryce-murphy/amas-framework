---
status: drafted
---

# PR-52 Codex desktop pre-commit review

## Metadata

- Review target: [PR-52](https://github.com/bryce-murphy/amas-framework/pull/52) substantive squash at TASK-0035 canonical-text amendment cycle
- Branch: `feat/task-0035-canonical-text-amendment-bundle` (Option B per ADR-005)
- Cycle: TASK-0035 (canonical-text amendment cycle; continuing established class from TASK-0021 / TASK-0023 / TASK-0030 precedents per spec §0.1)
- Reviewer: Codex desktop (owner-invoked per ADR-001 D11; or auto-fire per (h.4) §5.3 disjunction)
- Review scope: canonical-text amendment verification at 7 amendment surfaces + §18.3 M-A7 20th-instance enumeration correctness + Class A v-bump completeness + co-shipped artifact frontmatter conformance
- Linked handoff: `docs/handoffs/TASK-0035-canonical-text-amendment-bundle.md`
- Linked predecessor handoff: `docs/handoffs/TASK-0034-employee-churn-adoption-pilot.md` (PR-50)
- Codex desktop session timestamp (UTC): 2026-05-11 (Codex desktop pre-commit pass-1 owner-invoked at step-11)

## Reviewer focus

Codex Reviewer is asked to verify **CANONICAL-TEXT AMENDMENT CORRECTNESS** + **CROSS-REFERENCE ACCURACY** + **§18.3 M-A7 ENUMERATION SEMANTIC INTEGRITY** at amas-framework cycle artifacts. This is a substantive canonical-text amendment cycle (Class A v-bump v2.30 → v2.31 + new canonical text in discipline cluster + §18.3 M-A7 20th-instance amendment).

Specifically verify:

1. **7 amendment surfaces at `core.md` + `templates/handoff-template.md`** correctly applied per spec §4.1-§4.7 byte-exact prescriptions (verification commands enumerated at Builder claims block below).
2. **§18.3 M-A7 amendment per Path C** (PR-48 enumerated as 20th instance; PR-50 NOT enumerated per adoption-pilot cycle-class exclusion). Internal consistency at L458 preamble + L460 enumeration / span + L462 count. Step-1 reconciliation rationale at handoff §10 ledger entries (I)/(II)/(III).
3. **(XXIV) self-instantiation positive at Builder pre-flight surface** — BD-1 reconciliation (Adj 6 REVISED per Path C) is a positive empirical test of four-surface paired-discipline canonicalization being shipped this cycle. Step-1 stop-and-show + ratification record captured at handoff §10 + this review-context.
4. **(XVII) bidirectional sum-stability self-instantiation test** at this cycle's own (e.1) re-derivations (step-10 + step-12.X) — cycle ships (XVII) canonicalization; cycle's own staged-tree exercises the discipline at 3 axes both directions.
5. **path-(α') canonicalization self-instantiation test** at this cycle's own handoff frontmatter status transition (step-10.X `drafted → active` token-swap discipline) — 6th cross-cycle empirical positive expected.
6. **(XXVI) two-gate Gate A + Gate B canonicalization self-instantiation test** at this cycle's own step-16 + step-16.X gates — 4th cross-cycle empirical positive expected.
7. **F2 verification-first current-state guidance self-instantiation** at this cycle's own handoff §6 + §9 (cycle ships F2 fix-pattern at templates; cycle's own handoff exemplifies the pattern).
8. **Class A v-bump completeness** at 4 sites (README L9 ×2 + AGENTS L9 + CLAUDE L9) v2.30 → v2.31; (j) all-instances grep sweep for residual `v2.30` references (legitimate historical-record span endpoint at core.md L460 preserved per §23.6.3 sub-shape A canonical-impact-surface-completeness check).
9. **README L30 distributed-update** correctness (paragraph extension + batch sequence diagram extension per spec §4.10).

## Builder claims to verify

1. **Handoff frontmatter canonical 12-field form per `templates/handoff-template.md`**: `head -14 docs/handoffs/TASK-0035-canonical-text-amendment-bundle.md | grep -cE "^(task_id|title|pr|branch|linked_predecessor|linked_successor|linked_pr|framework_version_dogfooded|production_target|spec_source|date_authored|status):"` returns 12. Class: `templates/handoff-template.md` canonical 12-field form per PMN-007 HEAD canonical.

2. **PR-52 review-context frontmatter 1-field canonical form**: `head -3 docs/reviews/PR-52-codex-pre-commit.md | grep -cE "^(status):"` returns 1. Class: `templates/review-template.md` canonical 1-field form per `core.md` §17.7.

3. **`linked_pr` field canonical regex form**: `python -c "import re; print(re.match(r'^linked_pr: PR-(\d+) \(Builder fills with squash SHA post-merge per PMN-001 \(k\)\)[ \t]*$', 'linked_pr: PR-52 (Builder fills with squash SHA post-merge per PMN-001 (k))'))"` returns Match object. Class: PMN-001 (k) Action substitution contract.

4. **§4.1 (XVII) bidirectional sum-stability amendment at `core.md` §23.6.1.1**: `grep -nE "Bidirectional sum-stability check" core.md` returns 1 line within §23.6.1.1 span; `grep -nE "File-level change-source enumeration" core.md` returns 1 line within same span. Class: spec §4.1 byte-exact amendment.

5. **§4.2 (XIV) role-invariance amendment at `core.md` §23.6.3**: `grep -nE "^\*\*Role-invariance\.\*\*" core.md` returns 1 line within §23.6.3 span before §24 opens. Class: spec §4.2 byte-exact amendment.

6. **§4.3 path-(α') discipline amendment at `core.md` §23.6.3 + `templates/handoff-template.md`**: `grep -nE "Discipline-side fix application at status transition gates" core.md` returns 1 line within §23.6.3 span; `grep -nE "Path-\(α'\) discipline at pre-merge gate" templates/handoff-template.md` returns 1 line within Usage notes section. Class: spec §4.3 dual-surface byte-exact amendment.

7. **§4.4 (XXIV) four-surface paired-discipline amendment + new §24.4 at `core.md`**: `grep -nE "^### §24\.4\." core.md` returns 1 line; `grep -nE "Four-surface paired-discipline composition" core.md` returns 1 line. Class: spec §4.4 new sub-section authoring.

8. **§4.5 (XXVI) two-gate application surface clause amendment at `core.md` §24.3.1**: `grep -nE "^\*\*\(XXVI\) Two-gate application surface clause\.\*\*" core.md` returns 1 line within §24.3.1 span; `grep -nE "^\*\*Gate A surface-adapted Point 2" core.md` returns 1 line; `grep -nE "^\*\*Gate B Point 2 — base-form branch tip-SHA verification\.\*\*" core.md` returns 1 line (post step-15.Z3 path-(a) Finding H absorption — Gate A Point-2 surface-adapted to staged-tree-content parity verification; Gate B Point-2 retains base-form HEAD-SHA + clean-tree mechanism). Class: spec §4.5 byte-exact amendment + step-15.Z2 Finding E generic-form correction + step-15.Z3 Finding H surface-applicability refinement.

9. **§4.6 cost-class empirical-grounding strengthening at `core.md` §8.1.1.3**: `grep -nE "Empirical grounding \(cross-cycle accumulation\)" core.md` returns 1 line within §8.1.1.3 span. Class: spec §4.6 byte-exact amendment.

10. **§4.7 F2 verification-first guidance at `templates/handoff-template.md`**: `grep -nE "Verification-first current-state guidance" templates/handoff-template.md` returns 1 line within Usage notes section; `grep -nE "PMN-012 §3\.3 F2 fix-pattern" templates/handoff-template.md` returns 1 line within same context. Class: spec §4.7 byte-exact amendment.

11. **§4.8 §18.3 M-A7 amendment per Path C (4 sub-substitutions)**: `grep -nE "as of v2\.31 canonicalization at PR-52 / TASK-0035" core.md` returns 1 line at L460 (preamble per Sub-1, single-attribution canonical form post step-12 absorption Finding F1 correction per TASK-0032 precedent); `grep -nE "\+ PR-45 \+ PR-48 = 20" core.md` returns 1 line at L462 (enumeration per Sub-2 Path C); `grep -nE "spanning v2\.16 through v2\.30 canonicalization" core.md` returns 1 line at L462 (span per Sub-3); `grep -nE "20 consecutive substantive cycles" core.md` returns 1 line at L464 (count per Sub-4). Line anchors L460/L462/L464 reflect +2 shift from §4.6 paragraph addition before §14 per BD-5 step-10 informational. Class: spec §4.8 byte-exact amendment per Adj 6 REVISED at step-1 ratification (Path C; PR-48 = 20th; PR-50 excluded per adoption-pilot cycle-class) + step-12 Finding F1 single-attribution canonical-form correction.

12. **§4.9 Class A v-bump v2.30 → v2.31 (4 sites)**: `grep -oE "v2\.31" README.md AGENTS.md CLAUDE.md | wc -l` returns 4 (occurrence count; README L9 contains 2 occurrences on a single line, AGENTS L9 + CLAUDE L9 each 1 occurrence — total 4 sites). NOTE: spec §5.4 form `grep -cE "v2\.31" README.md AGENTS.md CLAUDE.md` returns 3 (line-count semantic; `-c` returns matching-LINES-per-file count, not occurrence count) — Builder path-(a) revised the verification command form at step-9 self-review per (XXIV.b)-class authoring narrowness sub-finding (spec §5.4 verification command per-occurrence vs per-line semantic mismatch). Empirical residual sweep: `grep -nE "v2\.30" README.md AGENTS.md CLAUDE.md core.md | grep -vE "spanning v2\.16 through v2\.30 canonicalization"` returns 0 lines (no Class A residuals; legitimate historical-record span endpoint at core.md L462 preserved per §23.6.3 sub-shape A canonical-impact-surface-completeness check). Class: spec §4.9 + §18.4 substantive-reading minor criterion.

13. **§4.10 README L30 distributed-update**: `grep -nE "canonical-text amendment bundle landed at PR-52" README.md` returns 1 line at L30; `grep -nE "Canonical-text-amendment\[7-cluster bundle landed\]" README.md` returns 1 line at L30. Class: spec §4.10 byte-exact + Item 14 retroactive-supersession-marking sub-rule.

14. **Cumulative-diff-stats per `core.md` §23.6.1.1 (e.1) staged-tree convention + (XVII) bidirectional sum-stability self-instantiation**: `git diff --staged --shortstat origin/main` returns staged-tree shortstat; `git diff --staged --numstat origin/main` returns 7 numstat lines; per-file row enumerates ALL source-section contributions per (XVII) refinement-being-canonicalized at this cycle. Bidirectional sum-stability check applied at all 3 axes (ins/del/file-count) per §23.6.1.1 amendment landed at this cycle. Spec §3 anticipated ~270-450 ins / ~11-22 del / 7 files. Re-derived at step-10. Class: §23.6.1.1 (e.1) + (XVII) self-instantiation.

15. **F2 fix-pattern self-instantiation at this cycle's own handoff §6 + §9**: handoff §6 "Cycle gates record" enumerates historical gates with SHAs/timestamps + in-flight gates with verify-before-act framing; handoff §9 "Verification-first current state guidance" anchors to PR-52 as canonical live-state surface with 4-step verify-before-act procedure. Cycle that ships F2 fix-pattern exemplifies the pattern in its own deliverable. Class: F2 fix-pattern operationalization; cycle-of-amendment positive self-instantiation.

16. **handoff frontmatter `status: drafted → active` pre-merge transition discipline — 6th cross-cycle empirical test surface**: Builder applies path-(α') discipline-side fix at step-10.X pre-commit stop-and-show staged-tree gate. handoff frontmatter L13 transitions `status: drafted` (file creation state) → `status: active` (pre-merge state) before `git push` + `gh pr create`. Applied without owner prompting at step-10.X (per path-(α') canonical promotion at this cycle's §4.3 amendment) = 6th cross-cycle positive (TASK-0030/31/32/33/34/35). Class: path-(α') discipline canonicalization being shipped + self-instantiation 6th cross-cycle confirmation.

## Codex desktop pre-commit kickoff

```
Please review the pending changes on the current branch (feat/task-0035-canonical-text-amendment-bundle) per the review-context at docs/reviews/PR-52-codex-pre-commit.md. Working tree at staged-tree state per TASK-0025 cycle-close Item 4 lesson.

Cycle class: canonical-text amendment cycle (continuing established class from TASK-0021 / TASK-0023 / TASK-0030 precedents). Class A v-bump tier: minor v2.30 → v2.31 per core.md §18.4 substantive-reading minor criterion (new canonical text in discipline cluster).

Cycle scope at amas-framework: 7 substantive amendments + 5 standard cycle artifacts.

Substantive amendments:
- core.md §23.6.1.1 (e.1): (XVII) bidirectional sum-stability discipline canonicalization (+ file-level change-source enumeration).
- core.md §23.6.3: (XIV) sweep-scope completeness role-invariance + path-(α') discipline-side fix canonicalization.
- core.md §24.3.1: (XXVI) two-gate Gate A + Gate B discipline extension of five-point check.
- core.md NEW §24.4: (XXIV) four-surface paired-discipline composition (authoring + receiving + ratification + post-PR review).
- core.md §8.1.1.3: cost-class one-iteration convergence empirical-grounding strengthening (12 cross-cycle positives accumulated).
- templates/handoff-template.md: path-(α') discipline cross-reference + F2 verification-first current-state guidance per PMN-012 §3.3 fix-pattern.

Standard cycle artifacts:
- core.md §18.3 M-A7 20th-instance amendment per Path C (PR-48 enumerated; PR-50 excluded per adoption-pilot cycle-class M-A7 exclusion; revised at step-1 ratification turn per Adj 6 REVISED — handoff §10 ledger entries (I)/(II)/(III)).
- Class A v-bump v2.30 → v2.31 at 4 sites (README L9 ×2 + AGENTS L9 + CLAUDE L9).
- README L30 distributed-update (canonical-text amendment bundle marker + batch sequence diagram extension).
- NEW docs/handoffs/TASK-0035-canonical-text-amendment-bundle.md (handoff with canonical 12-field frontmatter; F2 fix-pattern applied at §6 + §9 per self-instantiation test).
- NEW docs/reviews/PR-52-codex-pre-commit.md (this file; canonical 1-field status: drafted frontmatter).

Codex Reviewer focus: verify CANONICAL-TEXT AMENDMENT CORRECTNESS + CROSS-REFERENCE ACCURACY + §18.3 M-A7 ENUMERATION SEMANTIC INTEGRITY. 16-item Builder claims block enumerated at review-context. Key step-1 ratification context: Adj 6 REVISED per Path C (Architect spec authoring narrowness on TASK-0033 (IX) anticipation; Builder pre-flight (XXIV.a) self-instantiation positive at receiving-surface; reconciliation rationale + carry-forward standing question at handoff §10).

Per ADR-001 D11 owner-invokes convention: please run pre-commit review, surface findings per severity (Blocking → handback; Major → path-(a)/(β); Minor → default path-(b)). Substantive verdict via formal review (gh pr view reviews endpoint) preferred; issue-comment summary acceptable; line-level review-comments acceptable.

Verbatim-output convention: capture review verbatim into the review-context file ## Codex desktop pre-commit output absorption section per PMN-002 (a) + core.md §8.1.1.2 phantom-action verification discipline.
```

## Codex desktop pre-commit output absorption

### Codex desktop pre-commit review — 2026-05-11

Recommendation: **Request changes**.

#### Blocking findings

None.

#### Major findings

1. **[Major] `core.md` §18.3 preamble misattributes v2.31 canonicalization to PR-48 / TASK-0033.**
   - File/line: `core.md:460`
   - Evidence: line 460 reads `as of v2.31 canonicalization at PR-48 / TASK-0033 + canonical-text amendment at PR-52 / TASK-0035`. PR-48 / TASK-0033 is the enumerated 20th M-A7 instance and prior v2.30-era substantive cycle; this cycle's Class A bump is v2.30 → v2.31 at PR-52 / TASK-0035. The current wording makes the M-A7 cumulative-status preamble semantically wrong at the exact surface the review-context asks Codex to verify.
   - Required fix: reword the parenthetical so v2.31 attaches to PR-52 / TASK-0035, while PR-48 / TASK-0033 remains the enumerated 20th instance.

2. **[Major] `core.md` §24.4 contains a spec-local cross-reference instead of a canonical-text cross-reference.**
   - File/line: `core.md:614`
   - Evidence: the new canonical text says `per role-invariance §4.2 amendment above`. `core.md` has no §4.2 heading; §4.2 is the task/spec prescription identifier, not a stable canonical-law section. This leaks implementation-spec structure into canonical text and leaves future readers with an unresolvable canonical reference.
   - Required fix: cite the landed canonical surface directly, e.g. `per role-invariance discipline in §23.6.3`, or equivalent wording tied to `core.md` headings.

3. **[Major] TASK-0035 handoff still says the cycle is awaiting step-9/step-10 despite the staged-tree review state.**
   - File/lines: `docs/handoffs/TASK-0035-canonical-text-amendment-bundle.md:43`, `docs/handoffs/TASK-0035-canonical-text-amendment-bundle.md:63`, `docs/handoffs/TASK-0035-canonical-text-amendment-bundle.md:112`, `docs/handoffs/TASK-0035-canonical-text-amendment-bundle.md:127`, `docs/handoffs/TASK-0035-canonical-text-amendment-bundle.md:188`
   - Evidence: the handoff frontmatter is already `status: active`, and this pre-commit review is being run at staged-tree state after step-10.X per the owner invocation and review-context claims. But the durable handoff body still says last completed step is Step-4.11, cumulative stats are `TBD at step-10`, Step-9/10/10.X are pending, exact next step is Step-9, and the session log says it is awaiting step-9 + step-10. That contradicts the staged-tree state and undermines the handoff as the durable current-state artifact, even with the F2 verify-before-act guidance.
   - Required fix: update the handoff's current-state / validation / exact-next-step / session-log fields to match the actual pre-commit review state, including the re-derived `336 insertions / 7 deletions / 7 files` evidence or an explicitly current pointer to the review-context if the PR is intentionally the live-state surface.

#### Minor findings

None.

#### Verified claims / passing checks

- Pre-absorption staged diff envelope verified before this review output was inserted: `7 files changed, 336 insertions(+), 7 deletions(-)`.
- Pre-absorption per-file numstat sums verified: insertions `1+1+2+37+188+105+2 = 336`; deletions `1+1+2+3+0+0+0 = 7`; file count `7 = 7`.
- Review-output absorption itself adds lines to `docs/reviews/PR-52-codex-pre-commit.md`; post-absorption staged-tree stats require the normal step-12.X re-derivation before any commit claim.
- Branch verified as `feat/task-0035-canonical-text-amendment-bundle`.
- Handoff frontmatter has 12 canonical fields; review-context frontmatter has 1 `status` field; `linked_pr` regex shape matches.
- Class A v-bump occurrence count verified at 4 `v2.31` occurrences across README / AGENTS / CLAUDE; residual `v2.30` sweep outside the legitimate §18.3 historical span returned no lines.
- README distributed-update markers verified.
- `git diff --staged --check origin/main` returned no whitespace errors.

#### External / unavailable checks

- Formal GitHub PR review could not be submitted: GitHub API lookup for `bryce-murphy/amas-framework#52` returned 404, which is consistent with this being a pre-commit staged-tree review before PR open.
- The v2.14.1 substrate URL from AGENTS.md was not reachable from this environment (GitHub 404 / search miss), so substrate verification was limited to locally materialized v3 trio content plus current repo state.

### Adjudication (Architect step-12)

All 3 Major findings routed path-(a) revise per `core.md` §8.1.1.3 cost-class refinement (pure-token-swap class first-finding-in-class; one-iteration convergence anticipated). Codex pass-2 NOT REQUIRED per §8.1.1.3 cost-class refinement strengthened at §4.6 amendment landing this cycle (13th cross-cycle empirical positive).

- **F1 routing**: path-(a) revise with CORRECTED target form per TASK-0032 single-attribution canonical precedent. Builder's initial proposal preserved non-canonical "+" combining-attribution form; Architect ratification revised to single-attribution rotation (`as of v2.31 canonicalization at PR-52 / TASK-0035`). PR-48 not lost — preserved at L462 enumeration list. (XXIV.a/b) hybrid sub-shape at ratification surface 3 NEW catalog (Architect step-1 Sub-1 target form authoring narrowness).
- **F2 routing**: path-(a) revise all 3 instances per Builder (j)-sweep extension at core.md L563/L614/L621. **(XXIV.c) NEW sub-shape catalog candidate** — spec-local-vs-canonical-cross-reference narrowness; amendment text canonicalized at `core.md` must reference canonical sections, not spec section identifiers.
- **F3 routing**: path-(a) revise per Builder 5-field handoff state-snapshot updates. F2 handoff-currency self-instantiation positive at this cycle (cycle ships F2 canonicalization at §4.7; cycle's own handoff exhibits F2 pattern at template-amendment surface).

### Resolution applied (step-12.X)

Builder applied 3 path-(a) fixes at staged-tree state:

- **F1 fix**: `core.md` L460 → `as of v2.31 canonicalization at PR-52 / TASK-0035` (single-attribution canonical form).
- **F2 fixes** (3 instances per (j)-sweep extension):
  - `core.md` L563: `per §24.3 amendment below` → `per §24.4 four-surface paired-discipline composition below`
  - `core.md` L614: `per role-invariance §4.2 amendment above` → `per role-invariance discipline at §23.6.3 above`
  - `core.md` L621: `paired-discipline composition framing + role-invariance §23.6.3 amendment` → `paired-discipline composition framing at §24.4 + role-invariance discipline at §23.6.3 above`
- **F3 fixes** (handoff state-snapshot field updates):
  - `docs/handoffs/TASK-0035-canonical-text-amendment-bundle.md` Last completed step → step-12 absorption with sequence record
  - Cumulative-diff-stats section → step-10/10.X/12/12.X trajectory with bidirectional sum-stability check results
  - §3 step-by-step execution record → extended through step-12 absorption
  - Exact next step → step-12.X (e.1) re-derivation hand-back
  - §11 Session log archive → session 1 record updated through step-12 absorption
- **Item 14 sweep**: handoff §10 ledger entries (X)-(XV) added per absorption-cycle observations (Findings 1-3 routing + sub-shape catalogs + cost-class one-iteration 13th positive + (XVII) staged-tree-mutating-absorption clause self-instantiation positive + (XXIV) cumulative 7-instance running count at TASK-0035).

### Absorption status

- Codex output: captured verbatim per PMN-002 (a) at this review-context §"Codex desktop pre-commit output absorption" section.
- Adjudication: path-(a) all 3 findings per §8.1.1.3 pure-token-swap class one-iteration convergence (canonicalization being strengthened at §4.6 amendment landing this cycle).
- Resolution: 3 fixes applied at core.md L460/L563/L614/L621 + handoff state-snapshot fields + §10 ledger entries.
- (j)-sweep post-fix: `grep -nE "§4\.[0-9]+ amendment|§24\.3 amendment below|§23\.6\.3 amendment|§24\.4 amendment" core.md` returns 0 lines (Finding 2 class fully swept).
- (e.1) re-derivation post-absorption-fixes: surfaced at step-12.X stop-and-show.
- Codex pass-2: NOT REQUIRED per §8.1.1.3 cost-class refinement (13th cross-cycle empirical positive for pure-token-swap one-iteration convergence at this cycle's absorption surface).

## Post-PR Codex review state

### Three-endpoint poll (step-15) — 2026-05-11

Per `core.md` §8.1.1.1 three-endpoint poll discipline + `usage-guide.md` §7.4 canonical:

- **Endpoint 1 — formal review** (`gh pr view 52 --json reviews`): 1 formal review at `PRR_kwDOSRIPSM7-VaJA`, state `COMMENTED` (not `CHANGES_REQUESTED`); standard Codex banner body only; submittedAt `2026-05-11T20:06:35Z`; reviewed commit `978d2c1b72` (matches origin/feat HEAD post-step-13b).
- **Endpoint 2 — issue-comments** (`gh api repos/.../issues/52/comments`): 1 comment — owner `bryce-murphy` posted `@codex review` at `2026-05-11T20:04:06Z`. **Owner-invoked** per ADR-001 D11 standard convention (NOT auto-fire — counter-evidence for TASK-0034 (XVIII) "auto-fire-first" 1st-instance NEW sub-shape pattern repeating at TASK-0035; sub-shape is NOT 2/2 cross-cycle data points).
- **Endpoint 3 — line-comments** (`gh api repos/.../pulls/52/comments`): 1 line-level comment at `core.md:157` by `chatgpt-codex-connector[bot]`; substantive finding captured below.

### Codex post-PR pass-1 substantive finding (verbatim per PMN-002 (a))

**[P2] Preserve clean re-review after finding fixes** — line-comment at `core.md:157`

> This new exemption lets Builders skip Codex pass-2 after any "pure-token-swap" path-(a) absorption, but the live workflow still requires a re-review on every push that addresses findings and only allows thread resolution after that clean re-review (`usage-guide.md` §7.1/§7.3, lines 179 and 183 in this commit). In the common case where a pre-commit or post-PR finding is fixed by a token swap, following this text would leave the fix unverified by the Reviewer and any review thread unresolved under the framework's own rules; narrow the exemption to non-pushed local bookkeeping or update the thread-resolution/re-review rules consistently.

Comment URL: https://github.com/bryce-murphy/amas-framework/pull/52#discussion_r3221804673

### §8.1.1.2 phantom-action verification of Codex citation

Empirical verification of Codex citation per `core.md` §8.1.1.2 + four-category claim verification per `usage-guide.md` §7.5:

- **(i) file existence**: `usage-guide.md` exists at repo root ✓
- **(iv) identifier-pattern compliance**: §7.1 + §7.3 §-numbers exist at `usage-guide.md` ✓
- **Line references** (179 / 183) empirically verified at HEAD `978d2c1`:
  - L179 = `**§7.1. Rule (a) — Trigger after every push.**` body — content matches Codex citation semantic ✓
  - L183 = `**§7.3. Rule (c) — Resolve only after a clean re-review.**` body — content matches Codex citation semantic ✓
- **Pre-fix state (documented for cycle-close ledger)**: §4.6 amendment at `core.md` L157 originally claimed "Codex pass-2 re-invocation is therefore NOT REQUIRED at pure-token-swap class absorption" + cited scope "every cycle's Codex pre-commit + post-PR absorption iterations" (explicitly including post-PR); `usage-guide.md` §7.1 requires "re-review" "on every push that addresses findings"; `usage-guide.md` §7.3 requires "clean re-review" before thread resolution. The two surfaces were in direct operational conflict at post-PR re-review surface for pure-token-swap class absorption fix-up pushes. Surface 4 Codex post-PR pass-1 surfaced this conflict at PR-52 line-comment `3221804673`.
- **Post-step-15.X fix state (current at `a3ed3fa` onward)**: Path-(a.1) absorption narrowed §4.6 scope to pre-commit Codex desktop pass-2 only; explicitly preserved post-PR Reviewer re-review per `usage-guide.md` §7.1+§7.3 as binding. Conflict resolved at `core.md` surface. Cross-canonical-surface coherence at `usage-guide.md` §9.11 (L285) + quick-reference (L382) further extended at step-15.Y per Path-(γ.a) ratification (surgical scope-narrowing at both surfaces; no operational-discipline change).

Codex citation correct; no phantom-action.

### Cross-surface (XXIV) self-instantiation positive #9 at surface 4 post-PR

This Codex post-PR pass-1 finding catches Architect spec-authoring narrowness at §4.6 amendment scope (conflated pre-commit pass-2 NOT REQUIRED with post-PR re-review NOT REQUIRED). **9th (XXIV)-class instance at TASK-0035** (8 pre-step-15 per handoff §10 (XV)/(XVI) + 1 here at surface 4 post-PR). **Surface 4 post-PR functional at LANDING-CYCLE of (XXIV) four-surface paired-discipline composition canonicalization being shipped at §4.4 amendment** — empirical reinforcement of the canonicalization itself at its own ratification cycle.

### Codex post-PR pass-2 re-review (step-15.Y) — 2026-05-11

Three-endpoint poll #2 post step-15.X fix-up commit `a3ed3fa`:

- **Endpoint 1**: 2 new Codex re-reviews at `a3ed3fa` (20:17:38Z + 20:23:37Z; both `COMMENTED`, banner-only).
- **Endpoint 2**: re-review trigger at 20:15:07Z (Builder per Rule (a)) + additional `@codex review` at 20:20:52Z.
- **Endpoint 3**: 2 NEW substantive findings at `a3ed3fa`.

**Re-review verdict per `usage-guide.md` §7.3 Rule (c)**: NOT CLEAN — 2 net-new P2 findings. Original thread `3221804673` stays open until clean re-review.

#### Codex re-review Finding A (verbatim per PMN-002 (a))

**[P2] Update usage-guide pure-token-swap carve-outs** — line-comment `3221873409` at `core.md:157`:

> This narrows the exemption to pre-commit pass-2 and says post-PR re-review remains binding, but the public usage guide still gives the unqualified advice that "Codex re-invocation is discouraged for pure-token-swap fix-ups" in §9.11 and repeats it in the quick reference (`usage-guide.md` lines 285 and 382), while §7.1/§7.3 require re-review after every pushed fix. In the common post-PR pure-token-swap case, readers following the guide rather than this new core paragraph can still skip the required re-review/thread-resolution gate, so the cross-file fix-up is incomplete.

#### Codex re-review Finding B (verbatim per PMN-002 (a))

**[P2] Update the conflict verification after the fix lands** — line-comment `3221909669` at `docs/reviews/PR-52-codex-pre-commit.md:207`:

> This verification block still says the §4.6 conflict is "empirically real" and quotes the pre-fix wording that included post-PR absorption, but the `core.md` line 157 in this same commit has already been narrowed to the pre-commit Codex desktop pass and explicitly says post-PR re-review remains binding. Leaving the stale verification text in the durable review context creates a phantom current-state claim and can mislead the cycle-close ledger or a successor session into treating an already-resolved canonical conflict as still present.

#### §8.1.1.2 phantom-action verification

Empirically verified at HEAD `a3ed3fa`:
- **usage-guide.md §9.11 L285** ✓: contains "Codex re-invocation is discouraged for pure-token-swap fix-ups" unqualified.
- **usage-guide.md quick-reference L382** ✓: contains "Codex re-invocation discouraged for pure-token-swap" unqualified.
- **Review-context L207** ✓: contained the pre-fix conflict-verification framing per step-15 phantom-action section authoring (now updated at step-15.Y per Finding B path-(a) routing to pre-fix-state + post-fix-state documentation form).

Both Codex citations correct; no phantom-action.

#### Adjudication (Architect step-15.Y) + Resolution applied

- **Finding A routing**: **Path-(γ.a)** — extend fix-up to usage-guide.md §9.11 + quick-reference. Adj 1 cycle-scope EXPLICITLY EXPANDED (7 → 9 amendment surfaces; 7 → 8 files). Distinct from step-15 Path-(a.3) rejection: Path-(γ.a) is scope-NARROWING surgical token-swap (consistent with already-binding §7.1+§7.3), NOT substantive operational-discipline change.
- **Finding B routing**: **Path-(a)** — review-context L207 region updated to pre-fix-state + post-fix-state documentation form per F2 fix-pattern (PMN-012 §3.3) being canonicalized at §4.7 amendment landing this cycle.
- **Resolution applied at step-15.Y**:
  - `usage-guide.md` §9.11 L285 → scope to "pre-commit Codex desktop pass-2 re-invocation is discouraged" + cross-reference to §7.1+§7.3 post-PR binding.
  - `usage-guide.md` quick-reference L382 → scope to "Pre-commit Codex desktop pass-2 re-invocation discouraged" + post-PR cross-reference.
  - `docs/reviews/PR-52-codex-pre-commit.md` L207 region → pre-fix-state documented for cycle-close ledger + current post-step-15.X fix state acknowledged.
- **Item 14 sweep**: handoff §10 ledger entries (XXIII)-(XXVII) per ratification §5.

#### Cross-surface (XXIV) self-instantiation positives #10 + #11 at surface 4 post-PR pass-2

(XXIV.k) sub-shape catalog: 2 in-cycle instances at distinct canonical surfaces (pass-1: core.md §4.6 ↔ usage-guide.md §7.1+§7.3; pass-2: usage-guide.md §9.11 + quick-reference ↔ corrected §4.6). PMN-level canonicalization candidacy strengthens at TASK-0035; carry-forward to TASK-0036+ PMN candidacy. Surface 4 iterative-catch structure: each Codex pass surfaces new (XXIV.k) instances at DIFFERENT canonical-text surfaces; implicit sub-canonicalization candidate for §24.4 amendment extension at TASK-0036+ PMN cycle-close.

### Codex post-PR pass-3 + pass-4 re-review (step-15.Z) — 2026-05-11

Three-endpoint poll #3 post step-15.Y fix-up commit `05f3912`:

- **Endpoint 1**: 2 new Codex re-reviews at `05f3912` (20:49:40Z + 20:57:51Z; both `COMMENTED`, banner-only).
- **Endpoint 2**: Builder re-invocation at 20:47:18Z + additional `@codex review` at 20:55:09Z.
- **Endpoint 3**: 2 NEW substantive P2 findings at `05f3912`.

**Re-review verdict per `usage-guide.md` §7.3 Rule (c)**: NOT CLEAN at pass-3 + pass-4. 2 new P2 findings; all prior threads stay open.

#### Codex pass-3 Finding C (verbatim per PMN-002 (a))

**[P2] Fix the stale §18.3 verification command** — line-comment `3222055135` at `docs/reviews/PR-52-codex-pre-commit.md:56`:

> This verification claim no longer matches the canonical text after the F1 absorption: running the quoted `grep -nE "as of v2\.31 canonicalization at PR-48 / TASK-0033 \+ canonical-text amendment at PR-52 / TASK-0035" core.md` returns no lines, because `core.md` now says `as of v2.31 canonicalization at PR-52 / TASK-0035` at line 460. Any successor session or reviewer following this durable claim will see a false failure while verifying the §18.3 M-A7 amendment, so the review context should be updated to the landed string and current line references.

#### Codex pass-4 Finding D (verbatim per PMN-002 (a))

**[P2] Update the handoff's current gate before shipping** — line-comment `3222096823` at `docs/handoffs/TASK-0035-canonical-text-amendment-bundle.md:47`:

> This active handoff still tells the next session that the last completed step is Step-12 and that Step-12.X/Step-13 are pending, but the same artifact now contains post-PR step-15.Y absorption records and the actual diff already includes the later `usage-guide.md` fix-up. Since AGENTS.md requires the active handoff to be read before acting, a successor following this top-level state block would resume from the wrong gate and verify the wrong file set instead of continuing from the post-PR re-review/finalization state.

#### Adjudication (Architect step-15.Z) — MIXED ROUTING

- **Finding C routing**: **path-(a)** — load-bearing successor-verification anchor; review-context Builder claim 11 at L56 updated to landed §18.3 single-attribution form per step-12 Finding F1 correction. Item-14-sweep miss at step-12.X absorption is upstream root cause (claim 11 not updated when Sub-1 target form corrected at step-12 ratification).
- **Finding D routing**: **path-(β) record-and-proceed** per `core.md` §8.1.1.3 bounded-continuation rule:
  - 3rd same-class F2-handoff-currency instance at TASK-0035 cycle (F3 step-12 path-(a) + Finding B step-15.Y path-(a) + Finding D step-15.Z path-(β)).
  - Default routing for same-class subsequent finding per §8.1.1.3.
  - Load-bearing override does NOT apply: §4.7 amendment landing this cycle codifies handoff body fields as F2 historical record by design (not live tracker); §9 verification-first anchor + 4-step verify-before-act procedure handles successor verification; PR-52 is canonical live-state surface.
  - Handoff body block fields (Last completed step, Exact next step, §3 step-by-step, §11 session log) are F2 intrinsic recurrence per §4.7 amendment text framing.
- **Sub-canonicalization gap surfaced**: `core.md` §4.7 amendment + `usage-guide.md` §7.3 Rule (c) clean-re-review gate collision at path-(β) F2 acknowledged instances. Canonical mitigation at this cycle: owner admin-bypass per ADR-001 D9 + `core.md` §10.5 single-contributor bypass at step-17 merge. **(XXIV.k.cycle-termination) NEW sub-canonicalization candidate carry-forward to TASK-0036+**.

#### Resolution applied (step-15.Z)

- **Finding C path-(a)** applied: review-context L56 claim 11 verification command updated to single-attribution form (`as of v2\.31 canonicalization at PR-52 / TASK-0035`) + landed L460/L462/L464 anchors per BD-5 step-10 informational + step-12 Finding F1 correction provenance noted.
- **Finding D path-(β)** recorded: this Adjudication section captures the routing decision verbatim per PMN-002 (a); handoff §10 ledger entries (XXX)-(XXXII) at next Item 14 sweep; Builder reply at finding thread cites §8.1.1.3 + §4.7 + ledger entry.

#### Cross-surface (XXIV) self-instantiation positive #12 + #13 at surface 4 post-PR pass-3/pass-4

Surface 4 iterative-catch structure empirically confirmed at 4 sub-iterations within single cycle (pass-1 + pass-2 + pass-3 + pass-4). (XXIV) cycle-cumulative running total at TASK-0035 step-15.Z = **13 instances**. Cross-cycle trajectory TASK-0033 (5) + TASK-0034 (6) + TASK-0035 (13). Pattern strengthening continues; cycle is empirically maximally exercising §4.4 four-surface paired-discipline canonicalization being shipped.

### Codex post-PR pass-5 + pass-6 re-review (step-15.Z2) — 2026-05-11

Three-endpoint poll #4 post step-15.Z fix-up commit `c7bf22b`:
- **Endpoint 1**: 2 new Codex re-reviews at `c7bf22b` (21:09:43Z + 21:13:19Z; both `COMMENTED`, banner-only).
- **Endpoint 2**: Builder re-invocation at 21:06:06Z + additional `@codex review` at 21:10:25Z.
- **Endpoint 3**: 3 NEW substantive P2 findings at `c7bf22b`.

**Re-review verdict per `usage-guide.md` §7.3 Rule (c)**: NOT CLEAN at pass-5 + pass-6. 3 new P2 findings at NEW non-F2 defect classes. F2 handoff-currency class NOT re-raised (step-15.Z path-(β) for Finding D holds).

#### Codex pass-5 Finding E (verbatim per PMN-002 (a))

**[P2] Use the actual branch ref for Gate B** — line-comment `3222165419` at `core.md:606`:

> For any task branch whose type is not `feat` (allowed by `github-reference.md` §2.2: `fix`, `chore`, `adr`, `shadow`, `spike`), this new Gate B procedure tells successors to compare against `origin/feat` instead of the PR's actual head ref, so the required SHA concordance check will either fail on a missing ref or verify the wrong branch. The same hard-code is copied into the handoff template's resume command, so please phrase this as `origin/<branch>` / the PR `headRefName` rather than `origin/feat`.

#### Codex pass-6 Finding F (verbatim per PMN-002 (a))

**[P2] Use the full branch ref instead of hard-coding feat** — line-comment `3222181753` at `templates/handoff-template.md:148`:

> For successor sessions on any non-`feat` task, this template points at a remote ref that cannot exist: `github-reference.md` §2.2 allows `fix`, `chore`, `adr`, `shadow`, and `spike` branch prefixes as well as `feat`, so a handoff with `branch: chore/task-...` would tell the Builder to run `git log -1 origin/feat/chore/task-...` instead of `origin/chore/task-...`. That breaks the verification-first guidance exactly when resuming those cycles; the command should use the complete branch value after `origin/`.

#### Codex pass-6 Finding G (verbatim per PMN-002 (a))

**[P2] Split the gh api poll into valid endpoint calls** — line-comment `3222181759` at `docs/handoffs/TASK-0035-canonical-text-amendment-bundle.md:158`:

> When a successor follows this Step-11+ check in Bash/Git Bash, `{reviews,comments}` is brace-expanded into two separate positional arguments, but the [gh manual](https://cli.github.com/manual/gh_api) defines `gh api <endpoint> [flags]` with a single endpoint argument. Because `reviews` and `comments` are separate PR endpoints, this should be documented as two `gh api` calls (or another explicit polling sequence); otherwise the live-state verification command can fail before the user sees the Codex review state.

#### Adjudication (Architect step-15.Z2) — Option (c) RATIFIED

All 3 findings path-(a) per §8.1.1.3 first-finding-in-class + load-bearing substantive correctness at canonical-text + handoff durable-record surfaces. **NEW Architect explicit Stop-Iteration authority canonicalization candidate** introduced (mitigates (XXIV.k.cycle-termination) sub-canonicalization gap): if pass-7 surfaces NEW load-bearing substantive class findings beyond MC-A envelope + session-budget feasibility, Architect invokes Stop-Iteration based on (a) session-budget, (b) defect-class severity vs cycle-scope expansion, (c) TASK-0036+ carry-forward viability. TASK-0035 = 1st-instance empirical anchor.

#### Resolution applied (step-15.Z2)

- **Finding E path-(a)**: core.md §4.5 Gate B amendment (4 instances at L603/L606/L606/L608) updated from hard-coded `origin/feat` to generic `origin/<branch>` form + explicit reference to ADR-005 branch type variability (`feat|fix|chore|adr|shadow|spike`).
- **Finding F path-(a)**: templates/handoff-template.md §4.7 amendment (L148) updated from `git log -1 origin/feat/<branch>` to `git log -1 origin/<branch>` + explicit reference to ADR-005 valid prefixes.
- **Finding G path-(a)**: docs/handoffs/TASK-0035-...md §6 In-flight gates (L158) updated from shell-brace-expanded form to 3 separate `gh api` calls per `core.md` §8.1.1.1 three-endpoint poll canonical.
- **(j)-sweep extension at step-15.Z2 application**: 3 additional `origin/feat` instances at core.md L603/L608 caught + review-context claim 8 verification command updated to match new canonical text (4 total surfaces touched for Finding E class; 1 surface for Finding F; 1 surface for Finding G). Other `origin/feat` references at handoff L177/L203 + review-context L186 retained as **concrete-this-cycle references** (THIS cycle's branch IS `feat/...`); NOT hard-coded-generic-example defects.
- **Item 14 sweep**: handoff §10 ledger entries (XXXIII)-(XXXV) per ratification §6.

#### Cross-surface (XXIV) self-instantiation positives #14 + #15 + #16 at surface 4 post-PR pass-5/pass-6

3 new findings at 2 NEW (XXIV) sub-shapes:
- (XXIV.l) example-narrowness-vs-canonical-generality (Findings E + F)
- (XXIV.m) shell-command-form correctness (Finding G)

(XXIV) cycle-cumulative running total at TASK-0035 step-15.Z2 = **16 instances** across all 4 surfaces. Cross-cycle trajectory TASK-0033 (5) + TASK-0034 (6) + TASK-0035 (16). Pattern strengthening at maximum exercise of §4.4 four-surface paired-discipline canonicalization. Implicit sub-canonicalization candidate for §24.4 + §4.7 amendment extension at TASK-0036+ — extending (XXIV) sub-shape catalog with (XXIV.l) + (XXIV.m) + (XXIV.k.cycle-termination).
