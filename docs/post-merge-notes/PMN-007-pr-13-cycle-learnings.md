---
post_merge_note_id: PMN-007
title: PR-13 cycle learnings — bounded-continuation cost-class refinement + iterative-multi-surface pattern + PMN-001 (k) mechanism-vs-discipline + recursive-self-instantiation cluster + (h) retirement
linked_pr: PR-15 (Builder fills with squash SHA post-merge per PMN-001 (k))
framework_version_dogfooded: AMAS v2.16
status: drafted
---

# PMN-007 — PR-13 cycle learnings: bounded-continuation cost-class refinement + iterative-multi-surface pattern + PMN-001 (k) mechanism-vs-discipline + recursive-self-instantiation cluster + (h) retirement

## Status

Recorded — 2026-05-03

PMN-007 inserts under ADR-003 Decision 3 contingency budget. Consumes one of five remaining contingency slots; four remaining (TASK-0024 through TASK-0027 unconsumed).

## §1. Cycle context

PR-13 (TASK-0012) authored core.md Part B — the second core.md substantive-canonical-content cycle in the project. Seven canonical leaves landed in core.md at squash-merge `6086a16` on 2026-05-03 (130 source-line count): §17 minimal parent frame; §18 parent frame; §18.1 trigger basis baseline migration from v2.14.1; §18.2 form spec baseline migration; §18.3 M-A7 §-section text (NEW canonical text for the merge-commit-body data integration pattern); §18.4 framework version-bump trigger criteria (NEW canonical text formalizing the substantive-reading discipline); §8.1.1.3 bounded-continuation rule (NEW canonical text for the cross-surface bounded-iteration discipline). Framework version bumped v2.15 → v2.16 per §18.4 substantive-reading minor criterion — first canonical-document version bump applying §18.4 criteria the cycle itself canonicalized; recursive self-instantiation per §18.3 (d). PR-14 PMN-001 (k) chore-fix-up squash-merged at `e6a592b` shortly after.

Cycle shape was novel relative to all prior cycles in defect surfacing density: 23 spec-origination + execution defects across review surfaces (Architect §23.6 17 + Builder pre-flight 3 + Codex pre-commit 2 + Codex post-PR pass 1 1 = 23) vs PMN-006 baseline of 4 spec-time defects = ~5.75x. Pre-authoring verification batch (applied at PR-13 spec authoring session start per discipline candidate from PR-11 cycle handoff) was empirically insufficient as standalone — see §9 below. Iterative §23.6 sweep + multi-surface review pipeline remained load-bearing.

Eight observation umbrellas drive PMN-007 (§2 through §9 below) absorbing 16 candidate clusters — 8 inherited from PR-11 cycle handoff §4 ((a) cost-class refinement + (b) bounded-continuation back-citation + (c) iterative-pre-flight + iterative-post-PR-review + (d) auto-trigger reliability + (e) PMN-001 (k) execution form refinement + (f) within-cycle (e.1) analog + (g) bounded-continuation cross-surface generalization + (h) substantive-reading version bump) + 8 new this cycle ((i) pre-authoring verification batch insufficient-as-standalone + (j) same-class propagation residuals + (k) recursive-self-instantiation cluster + (l) bounded-iteration family composition refinement + (m) Reviewer citation sub-shape B + (n) cycle-trailing-clean-Approve third empirical instance + (o) memory-hygiene-on-canonicalization + (p) §18.3 operational-ordering ambiguity).

### §1.1. Honesty record

Twenty-three defects originated in or were surfaced during this cycle:

1. **Architect §23.6 iteration-2 batch (15 defects)** — comprehensive sweep of (g)/(h)/(i) sub-shapes plus PMN-004 §5 (a)-(f) inherited surfaced 15 defects in iteration-2 self-review (after iteration-1 baseline draft). Defect classes: (i.4) recap-consistency cross-§-section count drift (4 instances); (e) prose-arithmetic decomposition gaps (3 instances); (f) §-citation correctness slips (2 instances); (i.2) filesystem-path assertion drift (2 instances); (i.3) content-pattern assertion drift (2 instances); (h.2) verification-command-achieves-claimed-verification gaps (2 instances). All 15 routed path-(a) in iteration-3 revision.

2. **Architect §23.6 iteration-3 batch (2 defects)** — iteration-3 introduced 2 new defects via path-(a) propagation residuals: §-section count claim drifted between §-section count assertions in iteration-3-revised body and unchanged preamble; cumulative-diff-stats per (e.1) sub-rule drifted between iteration-3-revised line-count claims and unchanged total-diff claim. Both routed path-(a) in iteration-4. Iteration-4 zero-defect convergence reached (4-iteration-to-fixed-point per §23.6.2 norm).

3. **Builder pre-flight iteration-5 P1** — cross-document state assertion drift on §17 parent-frame line-count: spec asserted §17 minimal parent frame at "5 lines" (correct) but downstream cumulative-diff-stats summary subtracted using outdated value from iteration-2 draft. (i.4) sub-shape × (e.1) sub-rule cross-class. Routed path-(a) per §8.1.1.3 cost-class refinement (single instance, not asymptotic).

4. **Builder pre-flight iteration-5 P2** — (e.1) cumulative-diff-stats drift across Builder's verification claim 6 (cumulative ins+del should equal Σ per-§-section line counts; spec asserted total of 198 vs Σ = 197 from per-§ values). Routed path-(a) per §8.1.1.3 cost-class refinement. **Critical adjudication**: at preliminary cost-class refinement framing, this could route path-(β) under "asymptotic recursion noise"; Architect adjudicated load-bearing per pure-token-swap cascade analysis (correction is one-iteration fixed-point: change one number, no new propagation surfaces). This adjudication is the empirical seed for §2 (l) bounded-iteration family composition refinement canonicalization in §2 below.

5. **Builder pre-flight iteration-5 P3** — (i.4) recap-consistency on §-section enumeration in spec preamble: preamble lists "7 leaves" but enumeration shows 7 entries with one mis-numbered (§18.2 cited as §18.3 in preamble); cross-§-section count was correct (7) but enumeration internal recap was off. Routed path-(a) per §8.1.1.3 cost-class refinement.

6. **Codex desktop pre-commit pass 1 Claim 1 Blocking** — verification command for Builder claim 1 (PR-13 review-context filename existence) targeted ephemeral CI-only state per (c) discipline boundary. Routed path-(β) per §8.1.1.3 cost-class refinement (ephemeral-surface verification falls outside pre-commit verifiable scope per (c) discipline; Builder claim restated to target durable surface).

7. **Codex desktop pre-commit pass 1 Claim 14 Blocking** — handoff body claim diverged from frontmatter post-iteration-revision (handoff §Current state field cited iteration-5 line-count value; handoff frontmatter `linked_pr` field unchanged from iteration-4 placeholder). PMN-006 §3.4 frontmatter-vs-body sub-clause direct empirical recurrence. Routed path-(a) revise.

8. **Codex cloud post-PR pass 1 P2** — handoff line 156 cited stale 545 vs committed 547 vs durable repo 546; durable repo surfaces inconsistent across three numbers across handoff body / frontmatter / merge-commit-body. Routed path-(a) per §8.1.1.3 cost-class refinement — sixth same-class (i.4) cycle finding, but load-bearing per Architect post-pass adjudication (durable repo surfaces should converge, not asymptote at recursion noise). Plus phantom-SHA verification per §8.1.1.2 sub-shape B: Codex cited fabricated SHA `a7330d0c722801268dec6ac6d1e389a3c33e3e15` (HTTP 422) while substantive content was correct (verified against actual SHA `bbec1323`). Sub-shape B (correct-content-fabricated-citation) empirical instance from Reviewer-side surface, distinct from Builder hand-back claimed-action surface — sub-shape canonicalization at §8.1.1.2 already covers this category.

9. **Codex cloud post-PR pass 2 cycle-trailing-clean Approve** — third empirical instance of cycle-trailing-clean-Approve pass shape per §8.1.1.1 (PR-10 pass 5 + PR-11 cycle close + PR-13 cycle close).

10-23. (Detailed Architect §23.6 iteration-2 sub-instances and iteration-3 propagation specifics aggregate into items 1-2 above; explicit per-defect enumeration available in PR-13 spec source `.claude/session-handoffs/TASK-0012-spec.md` §18 defect log per ADR-001 decision 15 gitignored-spec convention.)

The framework's multi-stage review pipeline operated as designed: Architect §23.6 caught 17 defects across 4 iterations to fixed-point; Builder pre-flight surfaced 3 additional sub-shapes Architect missed; Codex desktop pre-commit caught 2 Blocking findings across path-(a) and path-(β) routing; Codex cloud post-PR caught 1 load-bearing same-class finding the prior 4 surfaces missed plus phantom-SHA citation. Cycle-trailing-clean Approve at pass 2 confirmed defect-free state at cycle close.

Empirical interpretation: pre-authoring verification batch is **insufficient as standalone defect-prevention discipline** at substantive-content-cycle scope. See §9 below for (i) refinement candidate canonicalizing the pre-authoring batch extension to direct grep-against-canonical-document for §-header enumeration. Iterative §23.6 sweep + multi-surface review pipeline remain load-bearing.

### §1.2. M-A8 second-data-point evidence

PMN-006 §1.2 + §9.2 introduced M-A8 (substantive-content-cycle scope step-up driving PMN-cadence step-up) as preliminary single-data-point monitoring item; PR-10 cycle was the single data point. PR-13 cycle is the second data point: 130 lines new canonical text + 402 handoff lines + 422 review-context lines + 23 cycle defects = unambiguously substantive-content scale. M-A8 advances from preliminary single-data-point to **preliminary two-data-point**. PMN-007 cycle is candidate third data point — if PMN-007 cycle reaches substantive-content scale (likely given consolidated 11-§-header structure), M-A8 reaches canonical refinement threshold at PMN-008. Promotion adjudication deferred to PMN-008 cycle; reconciliation at TASK-0023 per PMN-006 §9.2 monitoring framing.

### §1.3. M-A6 counting convention re-verification

Architect-side counting drift surfaced and corrected at TASK-0015 spec authoring time (per architect-to-architect handoff §3 honesty record entry on Architect-side counting convention drift). The canonical convention per Phase 1 D2 (PMN-006 cycle) + PR-11/PR-12/PR-13/PR-14 precedent: chore-PRs that materialize PMN-001 (k) substitution mechanism are NOT separate denominator entries in M-A6 — they belong to their substantive cycle's denominator entry. Pre-PMN-007: 6 PMNs / 12 substantive cycles = 50%. Post-PMN-007: 7 PMNs / 13 substantive cycles = 54%, within ADR-003 forecast upper bound (7/13 ≈ 54%). M-A6 contingency budget: 5 slots remaining (TASK-0023 through TASK-0027); trigger event remains TASK-0023.

## §2. Bounded-continuation rule refinement umbrella

This umbrella absorbs four canonicalization-adjacent observation clusters: (a) cost-class refinement to bounded-continuation rule §8.1.1.3; (g) bounded-continuation rule cross-surface generalization (saturated this cycle); (l) bounded-iteration family composition refinement distinguishing genuinely-asymptotic from pure-token-swap cascades; (f) within-cycle (e.1) analog (Evidence-section staleness after Evidence-fill) — subsumed under (l) per the genuinely-asymptotic-vs-pure-token-swap distinction (PR-13 cycle iteration-5 (e.1) cascade is the empirical material driving (l)).

### §2.1. (a) cost-class refinement empirical evidence

§8.1.1.3 was canonicalized at PR-13 with a preliminary cost-class refinement clause distinguishing path-(a) revise vs path-(β) record-and-proceed routing. The cycle empirically applied the cost-class refinement **6 times in-cycle**: P1/P2/P3 Builder pre-flight (§1.1 defects 3-5); Codex pre-commit Claim 1 (§1.1 defect 6); Codex pre-commit Claim 14 (§1.1 defect 7); Codex post-PR pass 1 P2 (§1.1 defect 8). Two cycle iterations of (e.1) cascade also routed under cost-class refinement: iteration-3 propagation (§1.1 defect 2) + iteration-5 (e.1) cascade.

Empirical pattern: cost-class refinement is well-grounded as distinguishing dimension; preliminary single-data-point at PR-11 cycle handoff (a) candidate now strengthens to preliminary multi-data-point with self-instantiation evidence (PR-13 cycle canonicalized §8.1.1.3 + applied cost-class refinement 6+ times within same cycle). Strongest possible empirical signal by self-application at canonicalizing cycle.

### §2.2. (g) cross-surface generalization saturation

Bounded-continuation rule was originally articulated at Reviewer post-PR review surface (PMN-005 §2 / PR-10 pass 5 adjudication); generalized to Architect-side spec-revision surface at PMN-006 §5.3 with preliminary 2-cycle empirical grounding. PR-13 cycle saw bounded-continuation rule applied across **5 surface types within single cycle**: Architect §23.6 self-review iteration-3 propagation residuals; Builder pre-flight pass routing; Codex pre-commit Claim 1 ephemeral-surface routing; Codex post-PR pass 1 same-class routing; (e.1) iteration cascade routing. Cross-surface generalization is empirically saturated; canonicalization at §8.1.1.3 covers this; further refinement to (g) deferred unless cross-surface application surfaces additional sub-shapes beyond the current 5-surface set.

### §2.3. (l) bounded-iteration family composition refinement — joint canonicalization with (a)

The PR-13 cycle iteration-5 (e.1) cascade was routed path-(β) under preliminary cost-class refinement framing as "recursion-boundary noise" — but Codex post-PR pass 1 surfaced this routing as load-bearing failure case. Durable repo surfaces were inconsistent across three numbers (handoff body 545 vs frontmatter 547 vs merge-commit-body 546); the cascade was avoidable, not asymptotic.

**Refinement**: cost-class refinement clause should distinguish (i) genuinely-asymptotic recursion boundaries — structural changes that shift downstream surface line counts, where each iteration's correction introduces new propagation surfaces; bounded-iteration acceptance via path-(β) is appropriate at the asymptote — from (ii) pure-token-swap cascades — single-iteration convergence at a stable fixed-point where text values match git stat in one iteration without introducing new propagation surfaces. Pure-token-swap cascades terminate at one-iteration fixed-point and always route path-(a); only structural-shift cascades (genuinely-asymptotic class) warrant bounded-iteration acceptance via path-(β).

**Empirical grounding**: failure-mode self-instantiation evidence at the canonicalizing cycle. PR-13 cycle's iteration-5 (e.1) cascade was a pure-token-swap cascade (handoff body / frontmatter / merge-commit-body line-count number swap); routing path-(β) was incorrect under the genuinely-asymptotic-vs-pure-token-swap distinction this refinement canonicalizes. The cycle that canonicalizes the rule produces a counter-example to its own routing application — strongest possible empirical signal that the distinction is load-bearing.

### §2.4. Joint canonicalization at core.md §8.1.1.3

PMN-007 jointly canonicalizes (a) cost-class refinement empirical strengthening + (l) bounded-iteration family composition refinement at core.md §8.1.1.3 cost-class clause level. The byte-exact addition (per TASK-0015 spec §3.4) appends the genuinely-asymptotic-vs-pure-token-swap distinction to the existing cost-class refinement paragraph. (g) cross-surface generalization saturation is recorded in PMN-007 text without core.md modification (no further refinement to canonical text needed; saturation evidence recorded in PMN cross-reference).

### §2.5. Cross-reference parallel bounded-iteration patterns

The bounded-iteration family now comprises four members per PMN-006 §5.4 + this PMN's refinement:

- §23.6.2 4-iteration-to-fixed-point self-review (PMN-004 §1).
- §23.6.1.1 (e.1) cumulative-diff-stats re-derivation (PMN-005 §4.4).
- §8.1.1.3 bounded-continuation rule (PMN-006 §5.3 + cross-surface generalization saturated this PMN).
- §8.1.1.3 cost-class refinement with genuinely-asymptotic-vs-pure-token-swap distinction (jointly canonicalized this PMN per §2.4 above).

The four members operate at distinct surfaces: §23.6.2 at Architect spec authoring; §23.6.1.1 at path-(a) revision arithmetic re-derivation; §8.1.1.3 at multi-surface bounded-continuation routing; §8.1.1.3 cost-class at routing-decision level within bounded-continuation. Composition: a path-(a) revision (e.g., from Codex post-PR finding) triggers §23.6.1.1 (e.1) cumulative-diff-stats re-derivation; if the re-derivation surfaces additional same-class findings, §8.1.1.3 cost-class distinguishes whether the cascade is genuinely-asymptotic (route path-(β) per §8.1.1.3 bounded-continuation) or pure-token-swap (route path-(a) per §8.1.1.3 cost-class refinement); §23.6.2 4-iteration-to-fixed-point applies to spec-authoring iteration count independent of bounded-continuation routing.

## §3. Iterative-multi-surface pattern umbrella

This umbrella absorbs three canonicalization-adjacent clusters: (b) bounded-continuation back-citation discipline; (c) iterative-pre-flight + iterative-post-PR-review pattern (refined to four-surface scope this cycle); (j) same-class propagation residuals across iteration surfaces.

### §3.1. (c) Iterative-pre-flight + iterative-post-PR-review four-surface refinement

PR-11 cycle established preliminary two-surface pattern (Builder pre-flight + Codex post-PR review iterations). PR-13 cycle saw four-surface iterative pattern applied within single cycle: Architect §23.6 self-review (4 iterations to fixed-point); Builder pre-flight (1 substantive iteration on iteration-5 spec); Codex desktop pre-commit (1 pass surfacing 2 Blocking findings); Codex cloud post-PR (2 passes; pass 1 substantive findings; pass 2 cycle-trailing-clean Approve).

Strong second data point relative to PR-11 cycle's two-surface evidence. **Refinement**: PMN-006 §3.9 (or wherever the iterative-pre-flight pattern was preliminary documented) refines from two-surface to four-surface. The four surfaces in canonical order:

1. Architect §23.6 self-review (multi-iteration to fixed-point per §23.6.2)
2. Builder pre-flight on Architect-handed spec
3. Codex desktop pre-commit on PR-open commit
4. Codex cloud post-PR review (multi-pass per §8.1.1.1 cycle-trailing-clean handling)

Each surface catches sub-shape defects the prior surfaces missed; the framework's multi-stage review pipeline is structurally load-bearing. Empirically grounded by PR-13 cycle's 23-defect distribution across surfaces (17/3/2/1) with each surface contributing distinct sub-shapes (Architect: comprehensive-coverage-with-iteration-residuals; Builder: cross-document-state + recap-consistency; Codex pre-commit: verification-claim-validity + frontmatter-vs-body; Codex post-PR: durable-surface-convergence + phantom-citation).

### §3.2. (b) Bounded-continuation back-citation discipline preliminary

PR-11 cycle introduced preliminary back-citation pattern at Reviewer post-PR review surface — once a finding is routed path-(β) record-and-proceed, the receiving PMN entry should back-cite to the canonical-text-landing point of the bounded-continuation rule that drove the routing. Single data point at PR-11 cycle. PR-13 cycle path-(β) routings (Codex pre-commit Claim 1 §1.1 defect 6) provide potential second data point; canonicalization deferred unless the back-citation pattern appears at the canonical-text-landing point of (a)/(l) joint refinement in §2.4 above and at PMN-008 next-cycle text.

Recorded as preliminary single-data-point + second-instance-candidate; canonicalization threshold ~3 data points.

### §3.3. (j) Same-class propagation residuals across iteration surfaces

PR-13 cycle empirical pattern: when correcting a same-class defect at one iteration surface, propagation residuals frequently surface at adjacent iteration surfaces because each surface-correction fixes the surface where the defect was named, not the propagation residuals at adjacent surfaces.

Two empirical instances within this cycle:

1. **Iteration 5 Builder pre-flight P2 corrected §5.2 + §7 claim 2 but missed §14 prompt source** — Codex Claim 1 surfaced this gap at next surface. Same-class (i.4) recap-consistency defect; correction at Builder pre-flight surface fixed the named surfaces but not the propagation residual at the §14 surface that Codex pre-commit subsequently scrutinized.

2. **Architect direction-prompt "anticipated ~1+/1-" estimate under-counted PR-12's canonical 2+/2- shape** — Builder caught at PR-14 pre-flight surface. Architect direction-prompt assertion was a propagation residual from earlier iteration (PR-12 was first chore-fix-up at canonical 2+/2- shape; Architect direction estimate at PR-14 chore-fix-up authoring slipped to "1+/1-" — propagation residual from possibly anchoring on a different prior instance). Builder pre-flight surface verification-against-PR-12-precedent surfaced the slip.

**Refinement candidate**: when correcting a same-class defect at one iteration surface, sweep all related surfaces for same-class propagation residuals before declaring convergence at the originating surface. Empirically two-instance single-cycle evidence; ~2-3 cycles needed before canonical refinement promotion.

PMN-007 records (j) as substantive new observation cluster; canonicalization deferred.

## §4. PMN-001 (k) execution form refinement

This §-section canonicalizes the (e) candidate from PR-11 cycle handoff §4 — PMN-001 (k) execution form refinement with mechanism-vs-discipline distinction. Two-instance evidence reached this cycle.

### §4.1. Empirical evidence

PR-12 (TASK-0011 chore-fix-up) was the first empirical instance of branch-protection-adapted PMN-001 (k) substitution mechanism: instead of direct push to main (the original PMN-001 (k) execution shape), branch protection necessitated a small chore PR (1-file 2-insertions/2-deletions linked_pr substitution + status flip). PR-14 (TASK-0012 chore-fix-up) was the second empirical instance. Mechanism stable across both instances: feature branch with single commit, fast-forward-eligible, single PR with 1-file diff, owner squash-merge.

### §4.2. Mechanism-vs-discipline distinction canonicalized

The PMN-001 (k) **discipline** is unchanged: post-merge linked_pr substitution + status flip on the cycle's TASK handoff frontmatter. The discipline preserves canonical state (handoff status accurately reflects post-merge state; linked_pr is the durable squash SHA, not a placeholder).

The PMN-001 (k) **mechanism** adapts to repo branch protection state: if direct push to main is allowed (no branch protection on main), direct-push mechanism applies (original PMN-001 form); if branch protection requires PR for any commit to main, small-chore-PR mechanism applies (PR-12/PR-14 form: feature branch + single 2+/2- commit + PR + squash-merge).

Refinement: PMN-001 (k) canonical text describes the discipline (linked_pr substitution + status flip post-merge); the mechanism (direct push vs small chore PR) adapts to branch protection state and is not part of the discipline canonical text. Future projects adopting AMAS framework where main branch protection is configured differently apply the discipline via the appropriate mechanism for their repo's branch protection state.

### §4.3. Canonical placement

PMN-001 (k) canonical text refinement: add a clarification clause to PMN-001 (k) that the mechanism adapts to repo branch protection state. Light touch; not a new top-level §-section. Builder authors per PMN-001 current text — see TASK-0015 spec §3.5 for byte-exact instruction (cross-reference to spec). [NOTE: spec does not separately enumerate this; PMN-007 records the distinction as canonical refinement; PMN-001 text amendment deferred to PMN-008 cycle if reference-impl-level documentation is needed, OR canonicalized by reference via PMN-007 §4 cross-reference for current-cycle scope.]

**Adopted scope this cycle**: canonicalize the distinction at PMN-007 §4 by-reference; PMN-001 text amendment deferred (PMN-001 text remains as-is; PMN-007 §4 is the authoritative reference for the mechanism-vs-discipline distinction). Light-touch canonicalization avoids the cross-document-state-verification complexity of editing PMN-001 in this cycle.

### §4.4. Canonical effects

- PMN-001 (k) substitution discipline preserved as authored.
- Mechanism-vs-discipline distinction canonicalized at PMN-007 §4 (this cluster).
- Future substantive cycles' PMN-001 (k) chore-fix-up apply the mechanism adapted to branch protection state per §4.2 above.
- Forward integration: TASK-0015 cycle anticipates PMN-001 (k) chore-fix-up at PR-16 = TASK-0016 if needed (per PR-12 / PR-14 precedent); the chore-fix-up applies the small-chore-PR mechanism per current branch protection on main.

## §5. Recursive-self-instantiation cluster

This §-section records (k) recursive-self-instantiation cluster with three sub-shapes empirically grounded this cycle. Cluster is substantively novel; canonical promotion deferred to ~2-3 more cycles. Sub-shapes recorded as preliminary.

### §5.1. (k.1) Positive self-instantiation

The cycle that canonicalizes a pattern self-instantiates the pattern as the strongest possible empirical confirmation. PR-13 cycle empirical instances:

- §18.3 (d) self-referential pattern-promotion entry — pattern self-named at canonicalizing cycle. The PR-13 merge-commit-body explicitly named M-A7 promotion as "fifth instance of the merge-commit-body data integration pattern" — the cycle that promotes the pattern self-instantiates the pattern.
- §18.4 first canonical-document version bump applying its own criteria — v2.15 → v2.16 bump at PR-13 was the first application of §18.4 substantive-reading criteria the same cycle canonicalized.

Pattern: self-instantiation evidence at canonicalizing cycle is structural empirical confirmation that the canonicalized pattern operates correctly when applied to its own instantiation context.

### §5.2. (k.2) Failure-mode self-instantiation

The cycle that canonicalizes a rule can also produce a counter-example to its own discipline application. PR-13 cycle empirical instance:

- §8.1.1.3 cost-class refinement applied to iteration-5 (e.1) cascade as path-(β) "recursion-boundary noise" — but Codex post-PR pass 1 surfaced this as load-bearing failure case (durable repo surfaces inconsistent across three numbers; cascade was avoidable, not asymptotic).

Pattern: failure-mode self-instantiation is **structural empirical material** — both kinds of self-instantiation (positive at §5.1 + failure-mode at §5.2) are PMN-substantive evidence. The failure-mode case directly motivates §2.3 (l) bounded-iteration family composition refinement above; without the failure-mode self-instantiation evidence, the (l) refinement would lack the strongest empirical signal.

### §5.3. (k.3) Cleanup-phase coordination state-report-verification (NEW sub-shape)

PR-14 cleanup phase saw two owner-state-report-vs-actual-state discrepancies during the chore-fix-up cycle:

1. **"merged" misreport at first cleanup attempt** — owner-state-report claimed PR-14 was merged; verification surfaced PR-14 was still open. Cleanup action would have been silent destructive (e.g., branch deletion on still-open PR).
2. **"branch deleted" misreport** — owner-state-report claimed branch was deleted; verification surfaced origin still had branch at `0018e9a`. Cleanup action would have been silent no-op masking the mismatch.

Builder applied §24-style verify-before-assert at cleanup-phase coordination — discipline that worked: don't silently take destructive action on owner state-claim; verify first; surface discrepancy if found. Sub-shape distinct from §8.1.1.2 (Reviewer-claimed-action verification) and §24.3.1 (Builder-claimed-action verification at hand-back). Two-event single-cycle evidence; ~1-2 more cycles would confirm structural-vs-incidental.

PMN-007 records (k.3) as substantive new sub-shape; canonicalization deferred to ~1-2 cycles of cross-cycle confirmation.

## §6. Auto-trigger reliability — preliminary observation

PR-11 cycle handoff §4 introduced (d) auto-trigger reliability — diff-size correlation hypothesis as preliminary single-anomaly-pattern observation. Hypothesis: small-diff PRs (e.g., 1-ins/1-del) may not trigger Codex auto-review within typical window; large-diff PRs reliably trigger.

PR-13 cycle empirical evidence: substantive diff (+547 lines) saw post-PR Codex review fire within typical window — falls outside small-diff anomaly shape and is consistent with hypothesis (large diff = no anomaly). Doesn't add anomaly cycles. Continues preliminary single-anomaly-pattern observation.

PR-14 cycle empirical evidence: 1-file 2+/2- chore PR — auto-trigger reliability uncertain (chore PR closed quickly via owner-merge; specific timing of Codex auto-review fire vs manual `@codex review` invocation not separately recorded). Could be second anomaly-pattern data point if specifically tracked at next chore-fix-up cycle.

PMN-007 records (d) as preliminary single-anomaly-pattern; canonicalization threshold ~3 anomaly cycles, currently at 2 anomaly cycles per PR-11 cycle handoff + PR-14 candidate. Future cycles should track auto-trigger fire timing on small-diff PRs explicitly to confirm or refute the hypothesis.

## §7. Substantive-content scope step-up + (h) retirement + monitoring-register state

This §-section consolidates: (h) substantive-reading version-bump retirement; M-A8 advancement to two-data-point preliminary; M-A6 within-budget at 7/13 = 54%; M-A7 retired (canonicalized at core.md §18.3 last cycle); monitoring memory hygiene (subsumed under §8 below).

### §7.1. (h) Substantive-reading version-bump retirement

PR-11 cycle handoff (h) candidate was preliminary three-data-point pattern: PR-10 substantive-reading bump v2.14.1 → v2.15; PR-13 substantive-reading bump v2.15 → v2.16; canonicalization at core.md §18.4 covers the discipline. PR-13 cycle is empirically the first canonical-document version bump applying §18.4 criteria the cycle itself canonicalized — recursive self-instantiation per §5.1 (k.1) above.

(h) candidate is now subsumed by canonical text at §18.4. **(h) retired** with explicit changelog reasoning at PMN-007: (h) candidate observation cluster reached three-data-point pattern + canonical text at §18.4 covers the discipline; further candidate-status tracking is redundant with canonical text.

### §7.2. M-A7 retirement (already canonical)

M-A7 advanced from operationally canonical to canonical §-section text in core.md §18.3 at PR-13. Monitoring register entry retired with explicit changelog reasoning at PMN-007. Memory-hygiene observation: monitoring memory `project_m_a7_monitoring_candidate.md` removed post-canonicalization per Builder's memory hygiene step at PR-13 cycle close. See §8 below for canonicalization of memory-hygiene-on-canonicalization sub-aspect.

### §7.3. M-A6 PMN-emission-rate within budget

Pre-PMN-007: 6/12 = 50%. Post-PMN-007: 7/13 = 54%, within ADR-003 forecast upper bound (7/13 ≈ 54%). M-A6 trigger event remains TASK-0023; **5 contingency slots remaining** post-PMN-007 (TASK-0023 through TASK-0027). M-A6 marginal-exceedance pattern (PMN-005 +2pp; PMN-006 +1pp) resolves toward forecast as PMN-007 lands at 54% = forecast upper bound exactly.

### §7.4. M-A8 two-data-point preliminary

Per §1.2 above. PR-10 + PR-13 = two data points of substantive-content-cycle scope step-up. Preliminary two-data-point; canonicalization threshold ~3 cycles. PMN-007 cycle is candidate third data point.

## §8. Discipline-articulation refinements

This §-section absorbs (o) memory-hygiene-on-canonicalization + (p) §18.3 operational-ordering ambiguity. Both are discipline-articulation refinements at preliminary single-data-point evidence.

### §8.1. (o) Memory-hygiene-on-canonicalization

When monitoring memory resolves to canonical text (e.g., M-A7 → core.md §18.3), the corresponding monitoring memory should be removed since state is derivable-from-HEAD per memory discipline. M-A7 monitoring memory `project_m_a7_monitoring_candidate.md` was removed post-canonicalization at PR-13 cycle close.

Pattern: monitoring memories that resolve to canonical text get state-derivable-from-HEAD treatment, not stale-memory accumulation. Canonicalization-driven memory hygiene preserves the principle that canonical state lives in the repo (HEAD) and memories cover only what is not yet canonical or what aids cross-session continuity beyond HEAD-derivable state.

Single-data-point preliminary; PMN-007 records (o) as discipline-articulation refinement candidate. Canonicalization deferred to ~2-3 cycles of cross-cycle confirmation OR to a memory-discipline canonical-text update if a broader memory-discipline §-section emerges in core.md.

### §8.2. (p) §18.3 operational-ordering ambiguity

§18.3 specifies Architect updates merge-commit-body before owner-squash-merges — but PR-13 cycle's actual squash-merge happened with auto-populated body (the explicit M-A7 self-reference appeared in subsequent merge-commit-body amendment, not the initial squash-merge body). Two reasonable interpretations:

- **(a) strict interpretation**: §18.3 requires pre-squash body authoring; PR-13 cycle violated ordering.
- **(b) lenient interpretation**: §18.3's authoring window extends to "before final cycle close" and amend-on-main fix-up is in scope.

Owner ratified default **(b) lenient interpretation** at PR-13 cycle close per architect-to-architect handoff §7. Operational-ordering ambiguity warrants explicit canonicalization at later cycle: §18.3 canonical text should explicitly state authoring window extends to amend-on-main fix-up (lenient interpretation explicit) OR explicitly require pre-squash body authoring (strict interpretation explicit). Single-data-point preliminary; PMN-007 records (p) as discipline-articulation refinement candidate with refinement candidate text as: "§18.3 authoring window: merge-commit-body authoring may occur (i) at squash-merge time via owner-author of merge body; (ii) post-squash via amend-on-main fix-up commit by Architect or owner. Either path is canonical; the requirement is body-content-completeness before final cycle close, not body-content-completeness at squash-merge instant."

Canonicalization deferred to PMN-008 or later cycle; ~1-2 more cycles of operational evidence may surface additional sub-shapes (e.g., "what if amend-on-main fix-up is itself blocked by branch protection?") that should inform canonical text.

## §9. Pre-authoring batch + Reviewer citation + cycle-trailing-clean preliminary observations

This §-section consolidates: (i) pre-authoring verification batch insufficient as standalone discipline; (m) Reviewer-side citation correctness sub-shape B; (n) cycle-trailing-clean-Approve pass shape third empirical instance.

### §9.1. (i) Pre-authoring verification batch insufficient as standalone

PR-13 cycle empirical evidence per §1.1 above: 23 spec-origination + execution defects = ~5.75x PMN-006 baseline despite pre-authoring verification batch applied at session start (per discipline candidate from PR-11 cycle handoff — discipline that the batch + iterative-§23.6-sweep composition was sufficient was the testable hypothesis).

Mechanism candidates per PR-13 spec defect log §18 (gitignored per ADR-001 decision 15):

- (i) substantive-content cycle scope produces more surface than small-PMN cycles — 130 lines new canonical text + 11 §-sections at PMN-007 scope = larger surface for defect emergence.
- (ii) pre-authoring batch covers source-of-truth grounding via project_knowledge_search but NOT direct grep-against-canonical-document for §-header enumeration — Architect inferred §-header baseline from prior-PR review-context's "leaves" framing rather than direct verification.
- (iii) §15 sweep at authoring time without explicit iterative application is insufficient — single-pass authoring with §15 sweep at end-of-authoring misses propagation residuals from path-(a) revisions; iterative §23.6 sweep with multi-iteration to fixed-point is structurally load-bearing.
- (iv) Architect-side §23.6 sweep does not catch all (i.4) sub-shapes — Builder pre-flight surface catches different sub-shapes per PMN-006 §3 multi-surface mitigation framing; the surfaces are complementary, not redundant.

**Refinement candidate**: extend pre-authoring verification batch to include direct `grep -nE "^#{1,6} §[0-9]" core.md` (bash) or `Select-String -Path core.md -Pattern '^#{1,6} §[0-9]'` (PowerShell, per (b) cmd-portability discipline) for §-header enumeration when authoring spec baseline assertions, rather than inferring baseline from prior-PR review-context's "leaves" framing. This refinement is empirically tested at PMN-007 spec authoring time (this very spec) — applied at TASK-0015 spec authoring per architect-to-architect handoff §C.1 verification result; ground truth for PMN-007 baseline §-counts.

Single-cycle empirical evidence at PR-13 cycle (insufficient-as-standalone) + single-cycle empirical application at TASK-0015 (extended-batch-as-tested). PMN-007 records (i) as substantive new observation cluster with refinement candidate carried forward to PMN-008+ for canonicalization adjudication based on PMN-007 cycle defect count vs PR-13 cycle's 17 Architect-side baseline.

### §9.2. (m) Reviewer-side citation correctness sub-shape B

Codex post-PR pass 1 cited fabricated SHA `a7330d0c722801268dec6ac6d1e389a3c33e3e15` (HTTP 422) while substantive content was correct (verified against actual SHA `bbec1323`). §8.1.1.2 sub-shape B (correct-content-fabricated-citation) empirical instance from Reviewer-side surface, distinct from Builder hand-back claimed-action surface.

Sub-shape canonicalization at §8.1.1.2 already covers this category. Reviewer-vs-Builder surface distinction is sub-shape-level evidence: (m) records that sub-shape B applies symmetrically across Reviewer-side and Builder-side claimed-action surfaces. PMN-007 records (m) as preliminary single-data-point at Reviewer surface; ~2-3 cross-Reviewer-cycles needed before canonical refinement to §8.1.1.2 explicitly noting cross-side symmetry.

### §9.3. (n) Cycle-trailing-clean-Approve pass shape third empirical instance

PR-13 cycle close was third empirical instance (PR-10 pass 5 + PR-11 cycle close + PR-13 cycle close). Preliminary canonical at §8.1.1.1 advances toward canonicalization threshold. PMN-007 records (n) as preliminary canonical with three-data-point evidence; canonicalization at PMN-008 or later cycle if additional data points accumulate.

The cycle-trailing-clean Approve pass shape: at cycle close after path-(a) revisions absorb prior-pass findings, the next post-PR Codex pass returns clean Approve confirming defect-free state. Pattern provides structural cycle-close signal — the multi-pass review pipeline reaches a verifiable defect-free state, not an asymptotic indefinite-iteration state.

## §10. Refined disciplines summary

PMN-007 introduces zero new top-level disciplines; refines two existing disciplines + retires two preliminary-canonical items + records eight new preliminary observation clusters.

**Refinements**:

- **§8.1.1.3 cost-class refinement extension** (per §2.4 above) — joint canonicalization of (a) cost-class refinement empirical strengthening + (l) bounded-iteration family composition refinement. Genuinely-asymptotic-vs-pure-token-swap distinction added to canonical clause. Canonicalized at core.md §8.1.1.3 cost-class clause level this cycle.
- **PMN-001 (k) mechanism-vs-discipline distinction** (per §4 above) — discipline preserved (linked_pr substitution + status flip post-merge); mechanism (direct push vs small chore PR) adapts to repo branch protection state. Canonicalized at PMN-007 §4 by-reference.

**Retirements**:

- **(h) Substantive-reading version-bump candidate** — three-data-point pattern reached + canonical text at core.md §18.4 covers the discipline; (h) candidate retired with explicit changelog reasoning.
- **M-A7 monitoring item** — canonicalized at core.md §18.3 last cycle (PR-13); monitoring register entry retired this PMN.

**New preliminary observation clusters** (per §3.2 / §3.3 / §5 / §6 / §8 / §9 above):

- **(b) Bounded-continuation back-citation discipline** — preliminary single-data-point + second-instance-candidate.
- **(j) Same-class propagation residuals across iteration surfaces** — preliminary two-instance single-cycle evidence.
- **(k) Recursive-self-instantiation cluster** with three sub-shapes: (k.1) positive self-instantiation; (k.2) failure-mode self-instantiation; (k.3) cleanup-phase coordination state-report-verification.
- **(d) Auto-trigger reliability — diff-size correlation hypothesis** — preliminary two-anomaly-pattern continuing.
- **(o) Memory-hygiene-on-canonicalization** — preliminary single-data-point.
- **(p) §18.3 operational-ordering ambiguity** — preliminary single-data-point with refinement-candidate text.
- **(i) Pre-authoring verification batch insufficient as standalone** — preliminary single-cycle empirical evidence + extended-batch application tested at PMN-007 spec authoring this cycle.
- **(m) Reviewer-side citation correctness sub-shape B** — preliminary single-data-point at Reviewer surface.
- **(n) Cycle-trailing-clean-Approve pass shape** — preliminary three-data-point evidence.

**Canonicalization-adjacency saturation** (no further refinement this cycle):

- **(g) Bounded-continuation rule cross-surface generalization** — empirically saturated at 5-surface application within single PR-13 cycle; no further refinement to §8.1.1.3 needed for (g) surface coverage.
- **(c) Iterative-pre-flight + iterative-post-PR-review pattern** — refined to four-surface scope per §3.1 above; canonical text refinement at relevant §-section deferred to PMN-008+ if reference-impl-level documentation is needed.

**Inherited disciplines** (standing per PMN-004 §5 + PMN-005 §4.4 + PMN-006 §3 + PMN-006 §7 + PMN-006 §5.3):

- **(a) Severity taxonomy three-level enumeration**.
- **(b) Verification-command portability** (bash, Windows cmd, or PowerShell forms; findstr codepage caveat for `§`).
- **(c) No future-tense claims at pre-commit time**.
- **(d) Pre-commit cross-surface scope clarity**.
- **(e) §23.6 prose-arithmetic decomposition** + sub-rule (e.1) cumulative-diff-stats re-derivation.
- **(f) Section-citation correctness sweep**.
- **(g) Verification-artifact internal consistency** with sub-shapes (g.1)/(g.2).
- **(h) Verification-command operational correctness** with sub-shapes (h.1)/(h.2)/(h.3).
- **(i) Cross-document state verification** with sub-shapes (i.1)/(i.2)/(i.3)/(i.4).
- **§8.1.1.3 bounded-continuation rule** generalized cross-surface (now refined per §2.4 above with cost-class genuinely-asymptotic-vs-pure-token-swap distinction).

## §11. Anticipated forward integration + cross-references

### §11.1. Forward integration

**TASK-0015 (this PR-15 cycle)** materializes the (a)/(l) joint canonicalization at core.md §8.1.1.3 + records 8 substantive observation umbrellas + retires (h) candidate + retires M-A7 monitoring item. Multi-stage review pipeline applied: Architect §23.6 self-review iterative-to-fixed-point + Builder pre-flight + Codex desktop pre-commit + Codex cloud post-PR. (i) refinement candidate (extended pre-authoring verification batch with direct grep-against-canonical-document) applied at TASK-0015 spec authoring time per architect-to-architect handoff §C.1.

**TASK-0016 (anticipated PMN-001 (k) chore-fix-up if needed)** applies small-chore-PR mechanism per §4 above; same shape as PR-12 / PR-14.

**TASK-0017 spec (next substantive cycle, anticipated)** carries forward all PMN-007 disciplines plus inherited PMN-004 §5 (a)-(f) + PMN-005 sub-rule (e.1) + PMN-006 §3 (g)/(h) + PMN-006 §7 (i) + PMN-006 §5.3 bounded-continuation generalized + PMN-007 §2.4 cost-class refinement with genuinely-asymptotic-vs-pure-token-swap distinction + PMN-007 §3.1 four-surface iterative-pre-flight + iterative-post-PR-review pattern + PMN-007 §9.1 (i) extended pre-authoring verification batch.

**Future PMN/ADR cycles** apply PMN-007's two refinements + retirements + new observation clusters globally. PMN-008+ and ADR-004+ inherit the refinements as standing.

### §11.2. Monitoring items state

- **M-A6 PMN-rate-vs-budget tracking**: 7/13 = 54% post-PMN-007-merge; within ADR-003 forecast upper bound (7/13 ≈ 54%). Five contingency slots remaining (TASK-0023 through TASK-0027). Trigger remains TASK-0023.
- **M-A7 merge-commit-body data integration pattern**: retired this PMN (canonicalized at core.md §18.3 PR-13).
- **M-A8 substantive-content-cycle scope step-up**: preliminary two-data-point (PR-10 + PR-13). PMN-007 cycle = candidate third data point. Promotion threshold ~3 cycles; reconciliation at TASK-0023 per PMN-006 §9.2 framing.

### §11.3. Cross-references

- **ADR-001** decisions 1-7, 9-15 unchanged; decision 8 PR sequence portion superseded by ADR-002, then by ADR-003 Decision 3.
- **ADR-002** Decision 3 anticipation pattern absorbed and extended by ADR-003 Decision 3; PMN-007 inserts under ADR-003 Decision 3 contingency budget.
- **ADR-003** Decision 2 (12 substantive content PR plan, anticipated PR-8 through PR-19 in original numbering, shifted across PMN insertions; current PR-13 = content-PR 2 of 12 per Decision 2 sequence post-PMN-005/006/007 shifts); Decision 3 (TASK reservation through TASK-0026; PMN-007 consumes a fourth contingency slot; five remaining: TASK-0023 through TASK-0027 — note: original TASK-0026 ceiling extended by one slot via PMN-007 inserting after PMN-006 in the contingency slot consumption pattern, but the TASK-0026 reservation ceiling itself was not extended; the available-slots-from-TASK-0023-onward enumeration is the operational accounting); §Consequences (per-PR-row-update discipline for README and stub frontmatter; package-layout drift remains forecast-form for stubs not yet shipped).
- **PMN-001** (h.2) file-based Builder direction; (k) Linked PR fix-up substitution discipline preserved + mechanism-vs-discipline distinction canonicalized at PMN-007 §4.
- **PMN-002** (a) refined imperative `Action:` phrasing; (d) code-fenced thin pointer prompt.
- **PMN-003** (a) refined recapitulation-consistency re-check; (e) refined two-endpoint review polling; (g) four-point Architect-side post-handback verification (extended in PMN-005 §2.5 to a five-point pattern); (j) and (m) receiving-surface format declaration.
- **PMN-004** §2 claim-text drift defect class characterization; §2.3 recapitulation-consistency re-check extension to verification-command surfaces; §4 two-endpoint discipline empirical confirmation; §5 six refined disciplines (a)-(f); §1 4-iteration self-review empirical pattern.
- **PMN-005** §2 reviewer-claimed-effects-don't-land defect class; §3 pass-shape correlation hypothesis (preliminary); §4.4 sub-rule (e.1) cumulative-diff-stats re-derivation.
- **PMN-006** §3 (g)/(h) discipline split; §7 (i) cross-document state verification; §5.3 bounded-continuation rule cross-surface generalization; §3.4 frontmatter-vs-body sub-clause; §1.1 honesty record + (h.3) lexicographic tie-break correction; §6.2 M-A7 operationally canonical advancement.
- **PR-13 (TASK-0012)** the cycle whose learnings PMN-007 captures; squash-merge `6086a16` 2026-05-03.
- **PR-14 (TASK-0012 PMN-001 (k) chore-fix-up)** second empirical instance of branch-protection-adapted PMN-001 (k) mechanism; squash-merge `e6a592b` 2026-05-03.
- **PR-15 (TASK-0015 / this PR)** the cycle in which PMN-007 + core.md §8.1.1.3 cost-class refinement extension land.
- **TASK-0017 (next substantive cycle, anticipated)** content scope TBD; carries forward all PMN-007 disciplines.
- **core.md §8.1.1.1** Reviewer dual-signal output handling — (n) cycle-trailing-clean-Approve pass shape application surface.
- **core.md §8.1.1.2** Reviewer claimed-action verification — (m) Reviewer-side citation correctness sub-shape B application surface; sub-shape canonicalization covers this category.
- **core.md §8.1.1.3** Bounded-continuation rule for iterative review-finding adjudication — refined this PMN with cost-class genuinely-asymptotic-vs-pure-token-swap distinction.
- **core.md §17** Templates (parent frame; canonicalized PR-13).
- **core.md §18** Post-merge note discipline (parent frame; canonicalized PR-13). PMN-007 follows §18.2 form spec.
- **core.md §18.1** Trigger basis — PMN trigger criteria (canonicalized PR-13).
- **core.md §18.3** Merge-commit-body data integration (canonicalized PR-13; M-A7 §-section text). (k.1) positive self-instantiation surface this PMN.
- **core.md §18.4** Framework version-bump trigger criteria (canonicalized PR-13). (h) retirement subsumed by canonical text.
- **core.md §23** Architect pre-handoff self-review (parent §-section); **core.md §23.6** Self-review disciplines — (g)/(h)/(i) discipline split sweep set + (e.1) sub-rule + extended (i) pre-authoring batch refinement candidate.
- **core.md §23.6.1.1** Sub-rule (e.1) — Cumulative-diff-stats re-derivation (canonical at PR-10 Part A authoring per PMN-005 §4.4 origin).
- **core.md §24** Cross-surface verify-before-assert meta-pattern — (k.3) cleanup-phase coordination state-report-verification sub-shape extends meta-pattern surface set.
- **core.md §24.3** Receiving-side caveat-discipline — Architect receiving Builder pre-flight findings during spec authoring; bounded-continuation rule generalization extends the §24.3 surface set.
- **core.md §24.3.1** Architect ← Builder hand-back symmetric-application clause (canonical at PR-10 Part A authoring + corrected at PR-11 per PMN-006 §1.1 defect 2).
