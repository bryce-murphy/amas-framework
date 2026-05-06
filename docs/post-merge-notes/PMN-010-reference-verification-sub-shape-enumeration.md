---
post_merge_note_id: PMN-010
title: Reference-verification sub-shape enumeration + Architect-spec-authoring-origin meta-pattern
linked_pr: PR-31 (Builder fills with squash SHA post-merge per PMN-001 (k))
framework_version_dogfooded: AMAS v2.21 → v2.22
status: drafted
---

# PMN-010 — Reference-verification sub-shape enumeration + Architect-spec-authoring-origin meta-pattern

## Status

Drafted at TASK-0025. Documentation-only at this cycle (canonical promotion to core.md §23.6.3 sub-shape enumeration deferred to dedicated TASK after multi-cycle data accumulation per Architect Phase 1 scoping).

## §1. Cycle context

PMN-010 documents the empirical record of §23.6.3 reference-verification-before-spec-authoring discipline across TASK-0023 (canonicalization cycle) + TASK-0024 (first non-self-instantiating canonical-application). The discipline was canonicalized at core.md §23.6.3 at TASK-0023/PR-27 ship absorbing PMN-009 §5 recommendation; TASK-0024 was the first cycle applying §23.6.3 to non-self-instantiating spec authoring (TASK-0023 was self-instantiating — the cycle canonicalizing the discipline applied it to its own spec authoring).

Cumulative empirical record (instance-count basis): 13 baseline at TASK-0023 close (4 PMN-009 + 3 TASK-0022 + 6 TASK-0023 instances; the TASK-0023 self-instantiating cycle is subsumed in baseline rather than enumerated separately) → 30 at TASK-0024 close (+17 instances across 6 catch events; see §3 table) → 33 at TASK-0025 step-2 (+3 instances at Builder pre-flight surface on PMN-010's own spec authoring; see §3 table). Plus 2 §8.1.1.2 phantom-SHA observations (action-claim fabrication N13 + body-reference fabrication N17) within single PR-29 review cycle (phantom-action namespace cross-referenced at §5; namespace-distinct from (i.5) reference-verification but conceptually adjacent).

PMN-010 enumerates 7 (i.5) sub-classes empirically grounded across the predecessor cycles. These sub-classes are documented at PMN-monitoring level; promotion to core.md §23.6.3 canonical sub-shape enumeration is deferred to dedicated TASK after additional cycle data accumulation tests sub-class stability + boundaries.

### §1.1. Honesty record

**Authoring-time §23.6.3 self-application** (this cycle's authoring applies the very discipline being documented):
- Spec §4 content prescription verified against canonical state via `project_knowledge_search` at authoring time (sub-shape A verify-at-authoring): core.md §23.6.3 / §23.6 / §24.3 line numbers + canonical text + PMN-008 §5.8 / PMN-009 §2 / PMN-001 (k) cross-references all resolved.
- Authored from TASK-0024 cycle-close ledger N1-N19 + PR-29 review-context Codex absorption record + iter-1-through-5 finding enumeration as primary empirical source material.
- Spec-context-vs-body-citation conflation class (TASK-0024 N11) explicitly avoided: §-citations enumerated in §4 body content distinguished from spec-context references in §1 / §2.
- Recursive-self-instantiation salience high: any (i.5) drift in PMN-010 spec authoring or Builder execution itself becomes empirical data for the discipline PMN-010 documents (k.1 positive self-instantiation per PMN-008 §3.1).

**Builder pre-flight (i.5) catches at TASK-0025 step-2** strengthen PMN-010's evidence base via (k.1) positive self-instantiation per PMN-008 §3.1: 3 additional drift instances surfaced at Builder pre-flight on PMN-010 spec authoring (sub-shape 1 forward-ref-§-citation correctness on §8.1.1.2 labels; sub-shape 4 spec-context-vs-body conflation in §1.1 line numbers; §23.6.1 prose-arithmetic decomposition class on cumulative-count narrative). Documented in §3 cumulative empirical record table. The discipline operates effectively against its own canonicalization-cycle's spec authoring drift.

**Empirical evidence boundaries**:
- 7-sub-shape enumeration is empirically grounded at the data-point counts named per sub-shape in §2; not all sub-shapes have equivalent empirical strength (forward-ref-§-citation has 12+ instances; intra-doc consistency has 1 instance).
- Architect-spec-authoring-origin meta-pattern (§4) is grounded in TASK-0024 Finding 6 (first-bypass ADR contradiction) + TASK-0024 N9 sub-shape-D handoff title catch + TASK-0023 step-1 sub-shape-D handoff title catch + 3 TASK-0025 step-2 Builder pre-flight catches on PMN-010 spec — six cross-cycle data points within one Architect-side authoring origin class.
- Phantom-action class cross-reference (§5) is grounded in PMN-008 §5.8 (h.4) namespace + 2 PR-29 sub-class instances (N13 + N17); the PMN-008 namespace already canonical at core.md §8.1.1.2 since v2.19.

## §2. Sub-shape enumeration

PMN-010 enumerates 7 (i.5) sub-classes empirically grounded across TASK-0023 + TASK-0024 cycles. Each sub-class is documented at PMN-monitoring level; canonical promotion to core.md §23.6.3 sub-shape enumeration deferred per Architect Phase 1 scoping.

### Sub-shape 1: Forward-reference §-citation correctness against named-source-state

**Description**: spec authoring cites §-numbers in named source documents that do not resolve in the source's current state. Specifically, citations of §-headings that don't exist as headings (anachronistic references; references to forthcoming canonical text not yet materialized; references that mismatch source-document §-numbering scheme).

**Empirical evidence**: TASK-0024 step-1 (i.5)(c) MAJOR finding — 12 forward-referenced core.md §-citations in spec §4 content prescription did not resolve in current core.md (status: partial; only §8/§17/§18/§23/§24 materialized to date). Refined to 9 actually-cited at step-9 (j) sweep. 12+ instance occurrences across 20 distinct lines in usage-guide.md materialized body. Additional cross-cycle precedent at TASK-0017 PR-17 cycle (line 148 §10 anachronistic citation; v2.14.1 §10.5-§10.6 → §3.2 migration). Additional TASK-0025 step-2 instance: PMN-010 spec authoring referenced "§8.1.1.2 four-category verification framework (i)/(ii)/(iii)/(iv)" labels that do not appear in canonical §8.1.1.2 text (which uses Sub-shape A / Sub-shape B adjudication labels plus four claim categories enumerated as bullets); Builder pre-flight (i.5) caught at step-2; Architect path-(a) substitution applied pre-execution.

**Catch surfaces**: Builder pre-flight (i.5)(c); Codex pre-commit (j) sweep; Codex post-PR; Architect §23.6.2 self-review at step-9 if (j) sweep applied.

**Resolution pattern**: Path B `(forthcoming at Part C+)` qualifier convention introduced TASK-0024 (Architect-adjudicated path-(a) at step-1; refined form). Anticipation-language qualifier symmetric to §0 `(forthcoming at TASK-####+)` for forward-referenced files. Future Part C+ materialization cycles drop qualifier as part of materialization-cycle's already-implicit cross-ref update cost.

### Sub-shape 2: Cross-document artifact-path verification

**Description**: spec authoring cites artifact paths or references whose current canonical state diverges from sibling-document state or lived-repo state. Distinct from sub-shape 1 (which is §-numbering correctness within a named source) — sub-shape 2 is artifact-existence and artifact-path correctness across multiple canonical surfaces.

**Empirical evidence**: TASK-0024 N12 / Codex post-PR iter 1 Finding 1 — usage-guide.md §3.2 + §5.3 introduced `docs/features/FEAT-####/brief.md` directory-style form against 3-surface-consistent lived practice on flat-file form `docs/features/FEAT-####-<slug>.md`. github-reference.md had zero canonicalization on Feature Brief path. Real adopter harm: operators following directory-style form would create non-discoverable Feature Brief artifacts.

**Catch surfaces**: Codex post-PR (cross-doc state verification). Pre-flight (i.5)(c) batch did not historically include cross-doc artifact-path consistency sweep at TASK-0023 / TASK-0024 spec authoring time.

**Resolution pattern**: path-(a) substitution with lived-practice-aligned form. github-reference.md → Feature Brief path canonicalization is forward refinement (TASK-0026+ v3 canonical-law-trio artifact-path-convention review).

### Sub-shape 3: Intra-document cross-section consistency

**Description**: spec authoring within a single document introduces internal contradictions between §-sections within that same document. Distinct from sub-shapes 1+2 (cross-document) — sub-shape 3 is within-document cross-section consistency.

**Empirical evidence**: TASK-0024 N18 / Codex post-PR iter 3 Finding 4 — usage-guide.md §10.22 (auto-fire emission verification) instructed single-endpoint poll (`gh api ... issues/<pr>/comments`) which contradicted same-document §7.4 three-endpoint poll discipline (canonical per core.md §8.1.1.1). Real adopter harm: operators following §10.22 literally would miss autonomous emissions landing in non-issue endpoints.

**Catch surfaces**: Codex post-PR (cross-section consistency verification). Pre-flight (i.5)(c) scope did not include intra-document cross-section consistency sweep at TASK-0024 spec authoring time.

**Resolution pattern**: path-(a) cross-reference form (preserve single-source-of-truth at authoritative §-section; cross-pointer form preserves source-of-truth concentration).

### Sub-shape 4: Spec-context-vs-body-citation conflation

**Description**: spec authoring conflates spec-context references (in spec §1 background, spec §7 anticipated claims, spec §10 risk discussion, etc.) with body-prescription citations (in spec §4 actual content prescription that materializes verbatim). The conflation produces over-enumeration when spec-context references are unioned with body citations as if both materialize.

**Empirical evidence**: TASK-0024 N4 + N11 — step-1 (i.5)(c) MAJOR finding enumerated 12 forward-referenced §-citations; step-9 (j) sweep refined to 9 actually-cited in materialized §4 body. 3 sections (§2.3.6, §3.4.1, §3.4.2) were spec-context references (§2.3.6 "implied by spec §1"; §3.4.1/§3.4.2 "anticipated per spec §7 claim 2") not §4 prescription body materialization citations. Builder step-1 finding conservatively unioned anticipated + body-cited; canonical step-9 (j) sweep correctly narrowed to actually-cited. Additional TASK-0025 step-2 instance: PMN-010 spec §1.1 honesty record cited core.md line numbers ("§23.6 parent prose at line 268"; "§24.3 direction #2 at line 334") that drifted from current canonical state (§23.6 at line 266; §24.3 at line 329); these were spec-context references in §1.1 (non-materializing into PMN-010 body) — Builder pre-flight (i.5) caught the line-number drift but adjudicated as informational-only since the references don't propagate into PMN-010 body content.

**Catch surfaces**: Builder step-1 (i.5)(c) initial finding; Architect §23.6.2 step-9 self-review refinement via (j) sweep; corrected at step-9 self-review iteration before commit.

**Resolution pattern**: §23.6.2 iterative-to-fixed-point self-review with (j) all-instances grep sweep narrows to actually-cited. Authoring discipline refinement candidate: Architect spec authoring should pre-tag spec-context references (in spec §1/§7/§10) explicitly as non-materialization to avoid Builder over-enumeration at step-1 (i.5)(c).

### Sub-shape 5: Phantom-action class (§8.1.1.2 namespace)

**Description**: review-output (Codex post-PR; Builder hand-back; Reviewer surface) claims actions or references SHAs/files/PRs that do not exist in repo state. PMN-008 §5.8 (h.4) namespace; canonical at core.md §8.1.1.2 since PR-25 / TASK-0021. Cross-referenced here because phantom-action observations strengthen the broader (i.5) reference-verification framing — phantom-action is a distinct namespace but conceptually adjacent to spec-authoring reference-verification (both are "claims that don't match canonical state").

**Empirical evidence**: PR-29 cycle accumulated 2 distinct phantom-SHA sub-classes within single review cycle:
- **N13 sub-class — action-claim fabrication**: Codex bot summary at iter 1 claimed `e234894` commit + `make_pr` tool action; HTTP 422 on commit verification; no follow-up PR exists. Specific identifiers fabricated.
- **N17 sub-class — body-reference fabrication**: Codex re-review at iter 2 fix-up commit `7cb557d` referenced `ad8af2a` SHA in shell example (`git diff --shortstat ad8af2a^ ad8af2a`); SHA does not exist in any branch/ref. Codex's substantive diff-stats claim 765/5 matched reality at re-review time; only the SHA in shell example was fabricated.

**Pattern strengthening**: 2 distinct sub-classes within single PR-29 cycle is empirical evidence that PMN-008 (h.4) phantom-action namespace is accumulating across canonicalization. Forward-cycle relevance: pattern recurrence at TASK-0026+ may warrant either Codex-replacement evaluation OR discipline shift to "verify all Codex-cited SHAs against git before crediting" as canonical text expansion at core.md §8.1.1.2.

**Catch surfaces**: §8.1.1.2 verification discipline applies to four claim categories (commit existence, file existence, follow-up artifact existence, identifier-pattern compliance) with two adjudication sub-shapes (Sub-shape A entirely-fabricated claims; Sub-shape B correct-content-fabricated-citation); operates symmetrically across Builder hand-back surface + Reviewer-side surface (PMN-007 §9.2 (m) cross-side symmetry).

**Resolution pattern**: path-(β) record-and-proceed for phantom-action observations; informational-only absorption per §8.1.1.2 sub-shape A canonical handling.

### Sub-shape 6: Stub-vs-operational artifact-path distinction

**Description**: specific sub-class within sub-shape 2 cross-doc artifact-path namespace. Spec authoring cites artifact paths to canonical-source files (e.g., `templates/X.md`) when the operationally-relevant target is the GitHub-instantiated counterpart (e.g., `.github/X.md`). The canonical-source vs operational-instantiation distinction (canonicalized at github-reference.md §4.2 for PR template) applies symmetrically across other GitHub-instantiated artifacts.

**Empirical evidence**: TASK-0024 N19 / Codex post-PR iter 4 Finding 5 — usage-guide.md §3.5 line 93 instructed operators to fill `templates/PULL_REQUEST_TEMPLATE.md` (canonical source / scaffold-stub) when actual operational template at `.github/PULL_REQUEST_TEMPLATE.md` is populated and serves PR body autopopulation. github-reference.md §4.2 already canonicalizes the canonical-source-vs-operational distinction. Real adopter harm: operators following §3.5 literally fill stub; live PR body misses operational template content.

**Catch surfaces**: Codex post-PR (cross-doc state verification with stub-vs-operational distinction).

**Resolution pattern**: path-(a) substitution to operational instantiation path. Distinct sub-class from sub-shape 2 generic cross-doc-artifact-path; the stub-vs-operational distinction has its own canonical surface at github-reference.md §4.2 that should anchor spec-authoring verification.

**Boundary clarification**: the canonical-source-vs-operational distinction applies WHERE AN OPERATIONAL COUNTERPART EXISTS (i.e., the GitHub-instantiated mechanism auto-loads or auto-surfaces a counterpart artifact). For artifacts WITHOUT a GitHub-instantiated operational counterpart — e.g., `templates/review-template.md` (no `.github/review-template.md` auto-load mechanism exists in GitHub; operators paste from `templates/` directly into Reviewer prompt context) — the canonical-source IS the operational source; the distinction does not apply. Empirical falsification at TASK-0025 step-2 pre-flight: TASK-0025 spec §1 deliverable 2 anticipated a usage-guide.md §3.7 review-template canonical-source-vs-operational fix paralleling TASK-0024 N19 / Finding 5 (PR template); Builder pre-flight verified no `.github/` review-template operational counterpart exists, voiding the deliverable. The boundary clarification refines sub-shape 6's applicability: the distinction is conditional on operational-counterpart-existence, not universal. Future spec-authoring verification at this sub-shape should first confirm operational-counterpart existence before applying canonical-source-vs-operational substitution.

### Sub-shape 7: Within-v3-trio rule-contradiction without v2.14.1-substrate-grounding

**Description**: spec authoring introduces NEW substantive rule assertions in v3 canonical-law-trio documents that contradict sibling v3 trio documents' canonical-law assertions. Distinguishing characteristic: the new assertion has NO v2.14.1 substrate grounding (was not migrated from v2.14.1 source per ADR-003 transition plan §4 row mappings); the contradicting sibling assertion IS v2.14.1-grounded. The within-v3-trio rule-contradiction class is a sub-class of cross-document state verification (sub-shape 2) but specifically about substantive policy/rule content rather than artifact-path or §-citation form.

**Empirical evidence**: TASK-0024 N19 / Codex post-PR iter 4 Finding 6 — usage-guide.md §3.9 + §13 asserted "first bypass = dedicated ADR" rule. Sibling v3 doc github-reference.md §3.2 (v2.14.1 §10.5-§10.6 grounded per ADR-003 transition plan §4 row 10 attribution) asserts "no additional artifact required at single-cycle scope; sustained-multi-contributor projects should document the bypass posture in an ADR." Direct rule contradiction. Real adopter harm: operators following usage-guide create unnecessary ADRs; following github-reference don't.

**Architect-spec-authoring origin**: the "first bypass = ADR" assertion in usage-guide.md §3.9 + §13 was introduced THIS cycle by Architect spec authoring without consulting sibling v3 doc github-reference.md §3.2 — i.e., violated §23.6.3 reference-verification-before-spec-authoring discipline at the spec-authoring surface itself. See §4 (Architect-spec-authoring-origin meta-pattern) for elevated framing.

**Catch surfaces**: Codex post-PR iter 4 (cross-doc canonical-law-trio substantive-rule consistency). Pre-flight (i.5)(c) batch + step-9 self-review + Codex pre-commit + Codex post-PR iters 1-3 all missed this drift; iter 4 caught it.

**Resolution pattern**: path-(a) substitution to align with v2.14.1-grounded sibling-doc form. Distinct sub-class from sub-shape 2 because the v2.14.1-substrate-grounding criterion adds substantive-content correctness verification beyond mere artifact-path / §-citation form.

## §3. Cumulative empirical record

§23.6.3 reference-verification discipline empirical record across cycles since canonicalization (TASK-0023/PR-27 ship). The 13-instance baseline at TASK-0023 close (4 PMN-009 confirmations + 3 TASK-0022 PMN-008 (i.5) instances + 6 TASK-0023 self-instantiating-cycle instances) is subsumed in baseline; the table starts at TASK-0024 cycle additions.

| Cycle | Source surface | Catch surface | Sub-shape | Volume |
|---|---|---|---|---|
| TASK-0024 step-1 | Architect spec authoring | Builder pre-flight (i.5)(c) | Sub-shape 1 (forward-ref-§-citation) | 9 instances (12 step-1 → 9 step-9 sweep refinement) |
| TASK-0024 step-9 | Builder step-9 self-review | (j) sweep refinement | Sub-shape 4 (spec-context-vs-body conflation) | 3 instances (narrowed union of 12 → 9 body-only) |
| TASK-0024 Codex pre-commit | Architect spec authoring | Codex desktop pre-commit | Cross-doc-shape-drift on branch convention (Path α record-and-proceed) | 1 instance |
| TASK-0024 Codex post-PR iter 1 | Architect spec authoring | Codex post-PR | Sub-shape 2 (cross-doc-artifact-path: Feature Brief) | 1 instance |
| TASK-0024 Codex post-PR iter 3 | Architect spec authoring | Codex post-PR | Sub-shape 3 (intra-doc cross-section consistency) | 1 instance |
| TASK-0024 Codex post-PR iter 4 | Architect spec authoring | Codex post-PR | Sub-shape 6 (stub-vs-operational) + Sub-shape 7 (within-v3-trio rule-contradiction) | 2 instances |
| TASK-0025 step-2 | Architect spec authoring (PMN-010 spec) | Builder pre-flight (i.5) | Sub-shape 1 (§8.1.1.2 labels) + Sub-shape 4 (§1.1 line numbers) + §23.6.1 prose-arithmetic (cumulative-count narrative) | 3 instances |

Cumulative confirmation count (instance basis): 13 baseline (TASK-0023 close, subsumed) → 30 (TASK-0024 close, +17 = 9+3+1+1+1+2 across 6 catch events) → 33 (TASK-0025 step-2, +3 across 1 catch event on PMN-010's own spec authoring).

Multi-surface review pipeline operating at 5 distinct catch surfaces across the cumulative record: Builder pre-flight + Architect step-9 self-review (j) sweep refinement + Codex pre-commit + Codex post-PR + recursive Builder pre-flight on PMN-010 spec. Codex post-PR surface specifically catches sub-shapes 2/3/6/7 (cross-doc state verification + intra-doc cross-section consistency + within-v3-trio rule-contradiction) that other catch surfaces have not historically caught at scale.

The N1 narrative framing at PR-29 review-context line 20 ("13 → 14") and at PR-29 cycle-internal advances ("13 → 17 through Codex post-PR iter 1") is preserved as historical-reference advance-event-bounded count. PMN-010's record-keeping commits to instance count for cross-cycle stability.

## §4. Architect-spec-authoring-origin meta-pattern

The cumulative confirmations across TASK-0023 + TASK-0024 + TASK-0025 share a common origin: **Architect-side spec authoring drift introduces canonical-text correctness defects that are then caught at downstream Builder/Reviewer surfaces**. This is not a mere accumulation of unrelated (i.5) instances — there is a structural pattern.

**§23.6.3 was canonicalized at TASK-0023 specifically to catch this class** (PMN-009 §5 recommendation absorbed as canonical sub-section parallel to §23.6.1 / §23.6.2 with verify-or-defer paths). TASK-0024 is the first non-self-instantiating canonical-application of §23.6.3. **At TASK-0024, despite §23.6.3 canonicalization + Architect-side discipline self-application + multi-surface review pipeline (pre-flight + step-9 self-review + Codex pre-commit + Codex post-PR iters 1-3), Architect-introduced rule-contradiction defect (sub-shape 7) survived to Codex post-PR iter 4 catch surface**.

This is meaningful empirical evidence: **Architect-spec-authoring remains a load-bearing source of (i.5) defects even after §23.6.3 canonicalization**. The discipline catches what's downstream-verifiable; what's not pre-verified at authoring-time relies on downstream surfaces to catch.

The TASK-0024 iter-4 Finding 6 catch is particularly telling because it required cross-doc state verification at substantive-rule-content level (not just §-citation form or artifact-path). The Architect-side authoring discipline at TASK-0024 spec authoring (which was applying §23.6.3 sub-shape A verify-at-authoring) did not include substantive-rule-content consistency verification across v3 canonical-law-trio sibling documents. The verification scope was forward-ref-§-citation focused.

TASK-0025 step-2 adds 3 additional data points within the same Architect-side authoring origin class — all caught at Builder pre-flight surface on PMN-010's own spec authoring. Total cross-cycle data points within Architect-spec-authoring-origin class: 6 (TASK-0023 step-1 sub-shape-D handoff title catch + TASK-0024 N9 sub-shape-D handoff title catch + TASK-0024 Finding 6 first-bypass ADR contradiction + 3 TASK-0025 step-2 PMN-010-spec catches). The discipline canonicalized to catch this class continues catching it, including on the document canonicalizing the discipline (recursive self-instantiation per (k.1) PMN-008 §3.1).

**Important framing**: catches at Builder pre-flight surface are not a discipline failure — they are §23.6.3 sub-shape B (defer-to-Builder-pre-flight) operating as designed. The framework explicitly tolerates verify-at-Builder-pre-flight because Architect-side verification scope is bounded (project_knowledge_search constraints; canonical state changes between authoring and execution; etc.). The 6 cross-cycle data points strengthen the discipline's empirical effectiveness rather than indicating its inadequacy.

**Forward refinement candidate**: §23.6.3 sub-shape enumeration should explicitly include "cross-doc canonical-law-trio substantive-rule consistency" as a distinct sub-class (sub-shape 7 above) within Architect-side pre-authoring verification scope. Architect spec authoring of v3 canonical-law-trio documents should apply substantive-rule-content sweep across sibling trio documents (`grep -nE "(canonical|policy|requirement|rule|MUST|SHOULD)" core.md github-reference.md usage-guide.md` or analogous) at authoring time, not only §-citation correctness sweep.

This refinement is documented at PMN-monitoring level here; canonical promotion to core.md §23.6.3 deferred per Phase 1 Decision C1.

## §5. Phantom-action class cross-reference

PMN-008 §5.8 (h.4) phantom-action namespace canonical at core.md §8.1.1.2 since PR-25 / TASK-0021. PR-29 review cycle accumulated 2 distinct phantom-SHA sub-classes within single review cycle (N13 action-claim fabrication + N17 body-reference fabrication).

The phantom-action class is namespace-distinct from (i.5) reference-verification but conceptually adjacent: both involve claims that don't match canonical state. (i.5) is Architect-side authoring claims; phantom-action is Reviewer-side / Builder-side post-authoring claims. Both rely on downstream verification to catch.

**Pattern strengthening**: 2 distinct phantom-SHA sub-classes within single PR-29 cycle is meaningful evidence the pattern is not isolated. Across PMN-008 §5.8 framing + PR-21 phantom-action observation + PR-23 / PR-25 cycle absorption priors + PR-27 cycle absorption + PR-29's 2 sub-classes, the phantom-SHA / phantom-action namespace has accumulated ≥5 cross-cycle data points.

**Forward-cycle relevance**:
- **Codex-replacement evaluation**: if pattern recurrence at TASK-0026/27+ continues, evaluate alternative Reviewer surfaces (different LLM provider; different review tool; different prompt framing for Codex). Threshold for evaluation: PMN-monitoring-level observation now; canonical evaluation TASK warranted at ≥3 cross-cycle data points after this PMN.
- **Discipline shift candidate**: alternative is to canonicalize "verify all Codex-cited SHAs against git before crediting" as expanded §8.1.1.2 four-category verification or as PMN-008 (h.4) namespace expansion. Forward refinement candidate; canonical promotion deferred.

## §6. Iterative-discovery pattern observation

TASK-0024 cycle achieved convergence at 5-iteration Codex post-PR sequence (initial + 4 re-triggers). Iteration-finding-volume sequence: iter 1 = 3 findings; iter 2 = 2 findings; iter 3 = 1 finding; iter 4 = 2 findings; iter 5 = 0 findings (clean convergence).

**Pattern characterization**: distinct from same-class asymptotic-convergence trap (which §8.1.1.3 line-count-preserving substitutions solve — empirically demonstrated at iter 2 → iter 3 validation-stat staleness convergence). Iterative-discovery is a distinct pattern where each re-review applies different review lens and surfaces new defect class not raised at prior iterations.

**Convergence forecast was open at iter 4**: volume bounce 3→2→1→2 was non-monotonic; character-based threshold (correctness-space vs preference-space) governed continued iteration. Per Architect-owner ship-judgment framework adopted at iter 3: pivot to path-(β) only when remaining defects shift from correctness-space to preference-space (stylistic, non-canonical, reasonable-reviewer-disagreement OR substantive-but-minor). Iter 4 findings were squarely correctness-space (real adopter harm); continued iteration warranted. Iter 5 was clean.

**Bounded-continuation cost-class extension candidate** for §8.1.1.3:
- Original §8.1.1.3 cost-class refinement covers same-class asymptotic-convergence (pure-token-swap converges at one iteration).
- TASK-0024 surfaced iterative-discovery as a distinct exhaustion class — not asymptotic on a single defect class; finite class enumeration where each iteration applies a different lens.
- Cost-class extension candidate: "iterative-discovery exhaustion" — different defect classes per iteration; convergence at correctness-space exhaustion; ship-judgment pivot to path-(β) when findings cross to preference-space or substantive-but-minor.

This refinement is documented at PMN-monitoring level; canonical promotion to core.md §8.1.1.3 deferred to dedicated TASK after multi-cycle calibration of the ship-judgment framework.

## §7. Codex-discipline-review framing for TASK-0026/27+

PMN-008 §5.8 (h.4) phantom-action accumulation + sub-shape 5 phantom-action class cross-reference in this PMN raise a forward-looking question: **at what point does the multi-surface review pipeline's reliance on Codex post-PR review surface warrant re-evaluation?**

Empirical evidence to date:
- Codex post-PR catches what other surfaces miss (4 of 7 sub-shapes in §2 enumerated above were caught primarily at Codex post-PR; pre-flight + step-9 self-review + Codex pre-commit didn't catch them).
- Codex post-PR also produces phantom-action / phantom-SHA outputs at meaningful frequency (≥5 cross-cycle data points; 2 sub-classes within single PR-29 cycle).
- Multi-surface review pipeline tolerates Codex's failure modes via §8.1.1.2 four-category verification framework (operational impact zero; absorbed at PMN namespace).

**Net assessment**: Codex post-PR is load-bearing for catch-coverage but produces unreliable claim-content. The §8.1.1.2 framework is the tolerance mechanism. As long as the four-category verification framework is applied consistently, Codex's failure modes are operationally absorbed.

**Forward question** for TASK-0026/27+ awareness:
- (a) Pattern recurrence — if phantom-SHA / phantom-action sub-classes continue accumulating, the §8.1.1.2 framework's verification cost increases per cycle. At what cumulative cost does Codex-replacement evaluation become warranted?
- (b) Alternative Reviewer surface evaluation — different LLM provider; different review tool; different prompt framing. Comparison against Codex's catch-coverage value.
- (c) Discipline shift canonicalization — expand §8.1.1.2 verification scope (currently four claim categories with Sub-shape A / Sub-shape B adjudication) to canonicalize "verify all Reviewer-cited SHAs against git before crediting" as default verification rather than only post-flag.

These are forward-monitoring-only at PMN-010; not adjudicated decisions. PMN-010 records the question for cycle-close ledger surface in TASK-0026 spec authoring.

## §8. Recommended monitoring vs canonical promotion

PMN-010 sub-shape enumeration is documentation-only at this cycle. Canonical promotion to core.md §23.6.3 sub-shape enumeration is deferred per Architect Phase 1 scoping (Decision C1).

Promotion criteria recommended for future TASK to evaluate:
- Sub-shape stability across ≥2 additional cycles (no boundary-shifts in sub-class definition; no new sub-classes emerging that fragment existing ones)
- Cross-cycle data point accumulation per sub-shape (some sub-shapes in §2 have only 1 data point; those would benefit from additional data before canonical promotion)
- Refinement candidates from §4 (cross-doc canonical-law-trio substantive-rule consistency as Architect-side pre-authoring verification scope expansion) and §6 (iterative-discovery exhaustion as §8.1.1.3 cost-class extension) tested empirically before canonical promotion

Anticipated forward TASK:
- TASK-0026 (AGENTS.md/CLAUDE.md → v3 migration + branch-convention ADR) — applies §23.6.3 self-instantiation to migration spec authoring; surfaces additional empirical data
- TASK-0027+ (canonical promotion candidate) — dedicated TASK absorbing PMN-010 sub-shapes into core.md §23.6.3 sub-shape enumeration if multi-cycle stability holds

## §9. Cross-references

- core.md §8.1.1.1 three-endpoint poll (canonical at v2.19+; PR-25/TASK-0021 ship)
- core.md §8.1.1.2 phantom-action verification (four claim categories with Sub-shape A / Sub-shape B adjudication; canonical at v2.19+)
- core.md §8.1.1.3 bounded-continuation rule with cost-class refinement (canonical at v2.16+; PR-13/TASK-0012 ship)
- core.md §23.6.3 reference-verification-before-spec-authoring (canonical at v2.20+; PR-27/TASK-0023 ship)
- core.md §24.3 receiving-side caveat-discipline (5 receiving directions; direction #2 enumerates §23.6 cluster)
- PMN-005 propose-then-absorb cadence
- PMN-006 §3 (g)/(h)/(i) sweep-set categories
- PMN-007 §9.1 (i) extended pre-authoring verification batch + §9.2 (m) Reviewer-side citation correctness sub-shape
- PMN-008 §3.1 (k.1) positive self-instantiation + §4.2 (i.5) convention-inference verification with PMN-file-shape sub-extension + §5.8 (h.4) Codex-output-endpoint-coverage discipline
- PMN-009 §2 sub-shapes A/B/C/D (spec-authoring drift catch discipline characterization; PMN-010 builds on this)
- TASK-0023 cycle-close (canonicalization cycle for §23.6.3)
- TASK-0024 cycle-close ledger N1-N19 + PR-29 review-context Codex absorption record (primary empirical source material for PMN-010)
- TASK-0025 step-2 Builder pre-flight (i.5) catches on PMN-010 spec authoring (recursive-self-instantiation evidence)
