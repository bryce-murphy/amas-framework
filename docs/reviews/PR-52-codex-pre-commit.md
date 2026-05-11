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
- Codex desktop session timestamp (UTC): TBD at owner invocation

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

8. **§4.5 (XXVI) two-gate Gate A + Gate B amendment at `core.md` §24.3.1**: `grep -nE "Two-gate Gate A \+ Gate B discipline" core.md` returns 1 line within §24.3.1 span; `grep -nE "Gate A — staged-tree pre-commit state" core.md` returns 1 line; `grep -nE "Gate B — origin/feat empirical attestation" core.md` returns 1 line. Class: spec §4.5 byte-exact amendment.

9. **§4.6 cost-class empirical-grounding strengthening at `core.md` §8.1.1.3**: `grep -nE "Empirical grounding \(cross-cycle accumulation\)" core.md` returns 1 line within §8.1.1.3 span. Class: spec §4.6 byte-exact amendment.

10. **§4.7 F2 verification-first guidance at `templates/handoff-template.md`**: `grep -nE "Verification-first current-state guidance" templates/handoff-template.md` returns 1 line within Usage notes section; `grep -nE "PMN-012 §3\.3 F2 fix-pattern" templates/handoff-template.md` returns 1 line within same context. Class: spec §4.7 byte-exact amendment.

11. **§4.8 §18.3 M-A7 amendment per Path C (4 sub-substitutions)**: `grep -nE "as of v2\.31 canonicalization at PR-48 / TASK-0033 \+ canonical-text amendment at PR-52 / TASK-0035" core.md` returns 1 line at L458 (preamble per Sub-1); `grep -nE "\+ PR-45 \+ PR-48 = 20" core.md` returns 1 line at L460 (enumeration per Sub-2 Path C); `grep -nE "spanning v2\.16 through v2\.30 canonicalization" core.md` returns 1 line at L460 (span per Sub-3); `grep -nE "20 consecutive substantive cycles" core.md` returns 1 line at L462 (count per Sub-4). Class: spec §4.8 byte-exact amendment per Adj 6 REVISED at step-1 ratification (Path C; PR-48 = 20th; PR-50 excluded per adoption-pilot cycle-class).

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

(Populated at step-15 post-`@codex review`.)
