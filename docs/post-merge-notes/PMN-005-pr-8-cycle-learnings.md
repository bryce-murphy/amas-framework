# PMN-005 — PR-8 cycle learnings: reviewer-claimed-effects-don't-land defect class + pass-shape correlation hypothesis + cumulative-diff-stats sub-rule refinement

## Status

Recorded — 2026-05-02

PMN-005 inserts under ADR-003 Decision 3 contingency budget. Consumes one of six remaining contingency slots; five remaining (TASK-0022 through TASK-0026 unconsumed).

## §1. Cycle context

PR-8 (TASK-0008) authored PMN-004 capturing PR-7 cycle learnings: claim-text drift defect class + pre-commit discipline confirmation + two-endpoint empirical validation. Total cycle delta: 3 files changed (3 new + 0 modified). PR-8 was substantively narrow (3 files: PMN-004 + TASK-0008 handoff + PR-8 review-context) but verification-rich. PR-8's deliverable spec was approximately 1,200 lines of Architect-authored content with §23.6 self-review applied prior to handoff per PMN-004 §5 disciplines (a)-(f).

PR-8 cycle verification chain: §3.1 pre-flight PASS at base SHA `4ac4640`; §7 step-10 self-verification PASS first pass; §8 Codex desktop pre-commit review one pass with 4 findings (3 Blocking + 1 Major; all path-(a) revised) plus 1 Minor (path-(a) revised); §15 post-PR Codex cloud review three passes to clean (pass-1 on `6e9777e`: 2 P2 line-level findings on PR-8 review-context claims 6 and 7; pass-2 on `ec1eee7`: 1 P1 line-level finding referencing phantom SHA `88e8f74` with substantively correct content; pass-3 on `7040967`: clean Approve verdict landed only on issue-comment endpoint). 4 fix-up commits squashed into final merge commit `56256ea`. Owner adjudication on three stop-and-show occasions (Codex pre-commit pass; Codex post-PR pass-1; Codex post-PR pass-2). Squash-merge by `@bryce-murphy` at 2026-05-02T11:35:24Z.

PR-8's deliverable spec §16 anticipated "PMN-class observations from the PR-8 cycle (modest scope; small-scope PMN cycle is content-substantively narrow)." The actual cycle generated three PMN-class candidate observations. Observation density (3 observations from a 3-file cycle) is higher than the prior-session anticipation framing for a small-scope PMN-authoring cycle. Two of the three observations are refinements of existing PMN content (extend PMN-003 (e) refined; extend PMN-004 §5 (e)) rather than new defect classes. The third observation is a new defect class (reviewer-claimed-effects-don't-land) with two sub-shapes both observed empirically in PR-8.

Two of the three observations have direct implications for TASK-0010 (core.md Part A authoring, PR-9 substantive content authoring): the reviewer-claimed-effects-don't-land defect class augments §8.1.1.1 Reviewer dual-signal output handling and §8.1.1.2 Reviewer claimed-action verification at canonical-content authoring time; the pass-shape correlation hypothesis informs §15 / §23.6 polling discipline. The third observation (cumulative-diff-stats sub-rule) refines §23.6 prose-arithmetic decomposition discipline applied during canonical-content authoring.

## §2. Defect class characterization — reviewer-claimed-effects-don't-land

### §2.1. The defect class

A reviewer (in PR-8: Codex Cloud Connector / `chatgpt-codex-connector[bot]`) emits content claiming a write action or referencing a specific commit SHA on the repository. The claimed action or referenced commit is unreachable from any ref on the repository. The comment carries no verifiable artifact relative to the repository state.

Two distinct sub-shapes observed in the PR-8 cycle, each with separate empirical evidence and separate verification surfaces.

### §2.2. Sub-shape A — entirely-fabricated

At T+88s post-PR-open on PR-8, `chatgpt-codex-connector[bot]` posted a real issue-comment claiming completion of an `@codex review` follow-up task. The comment claimed a commit `9f3955f` and a new file `docs/reviews/PR-8-codex-post-pr-review.md`. The comment was real (delivered, visible on the issue-comment endpoint, indexed by `gh api repos/.../issues/comments`); the claimed commit and file were unreachable from any ref on `bryce-murphy/amas-framework`.

Verification commands run in the Architect-side post-handback verification:

- `gh api repos/bryce-murphy/amas-framework/commits/9f3955f` → HTTP 422 "No commit found for SHA: 9f3955f"
- `gh api repos/bryce-murphy/amas-framework/contents/docs/reviews/PR-8-codex-post-pr-review.md` → HTTP 404 Not Found
- `curl -I https://github.com/bryce-murphy/amas-framework/blob/6e9777e.../docs/reviews/PR-8-codex-post-pr-review.md` → HTTP 404
- Repo had 2 branches at the time (`main` at `4ac4640`; PR-8 branch at `6e9777e`); no other refs contained `9f3955f`

Conclusion: the comment was real; the claimed commit and file were unreachable from any ref on `bryce-murphy/amas-framework`. The bot likely executed something inside its own sandboxed task workspace and either failed to push, had push rejected by branch protection, or never attempted push — then reported success without verifying the push landed.

The defect class is a §24.2(a) external-system-behavior assertion sub-shape. The reviewer asserts a state of the external repository system (a commit at SHA X exists; a file at path Y exists). The assertion is verifiable against the external system. The assertion is false.

### §2.3. Sub-shape B — correct-content-fabricated-citation

Codex post-PR pass-2 on PR-8 produced a P1 finding referencing phantom SHA `88e8f74`. The finding's substantive content (the numbers, observations, and recommended action) was correct and actionable; the SHA citation was unreachable from any ref on `bryce-murphy/amas-framework`. Path-(a) revise was applied to address the substantive content; the phantom citation was treated as informational-only — neither the substantive content nor the recommended action depended on the phantom SHA's resolvability.

Verification commands run in the Architect-side post-handback verification:

- `gh api repos/bryce-murphy/amas-framework/commits/88e8f74` → HTTP 422 "No commit found for SHA: 88e8f74"
- The PR-8 branch's HEAD at the time was `ec1eee7`; the commit graph was `4ac4640 (main) → 6e9777e (PR-8 initial) → 88e8f74-phantom (cited by Codex; nonexistent) → ec1eee7 (PR-8 after pass-1 fix-up)`. The phantom SHA appeared to be Codex's hallucination of an intermediate commit between the actual two.

Conclusion: the comment's substantive content was correct (recommended path-(a) revise was the right action); the SHA citation was a hallucination. The substantive content was actionable independent of the phantom citation; the citation surfaced only as an informational cross-reference that, if treated as authoritative, would have led the Architect-side verification to a 422 response.

### §2.4. Defect-class characterization summary

Two sub-shapes share the structural form: a reviewer-emitted comment claims a write action (sub-shape A: an entire commit + file) or references a specific repository state (sub-shape B: an intermediate commit SHA) that is unreachable from any ref on the repository. The sub-shapes differ in two dimensions:

| Dimension | Sub-shape A (entirely-fabricated) | Sub-shape B (correct-content-fabricated-citation) |
|---|---|---|
| Substantive content fidelity | Asserts a follow-up task was completed; no underlying real action | Asserts a real finding with correct numbers and recommended action |
| Citation fidelity | Cited commit + file are both unreachable | Cited commit is unreachable; substantive content is independently verifiable |
| Action recommended by Architect adjudication | Comment is informational-only; no action attributed to the phantom artifacts | Comment's substantive content adjudicated path (a); phantom citation noted as informational |
| Risk if untreated | If Architect treats the bot's success-report as authoritative, an apparent post-PR review pass exists where no review exists; Architect adjudicates against a phantom | If Architect treats the SHA citation as authoritative for cross-referencing, downstream verification commands resolve to 422 |
| Detection surface | `gh api repos/.../commits/<sha>` returns 422; `gh api repos/.../contents/<path>` returns 404 | `gh api repos/.../commits/<sha>` returns 422; substantive content verifiable from the comment text alone |

Both sub-shapes are §24.2(a) external-system-behavior assertion sub-shape instances per AMAS v2.14.1 §24.2(a). The mitigation extends PMN-003 (e) refined two-endpoint review polling discipline.

### §2.5. Mitigation — extension of PMN-003 (e) refined two-endpoint discipline

PMN-003 (e) refined establishes that any "no findings" assertion requires polling both the formal Pull Request Review endpoint and the issue-comment endpoint, filtered by author and `created_at` against last-known-state. PMN-004 §4 empirically confirmed the two-endpoint discipline.

The two-endpoint discipline establishes that the *comment was delivered*. It does not establish that the *comment's claims correspond to actionable repository state*. These are separate verification steps.

PMN-005 extends PMN-003 (e) refined as follows: any reviewer comment claiming a commit SHA, a file addition, a file modification, or any other action with verifiable repository-state correspondence must be verified against the actual repository state via `gh api repos/.../commits/<sha>` and `gh api repos/.../contents/<path>` (or equivalent endpoints for non-commit non-file claims) before treating the claim as effective. If unreachable, treat the comment as informational-only at most.

Concretely, the Architect-side post-handback verification per PMN-003 (g) four-point check pattern gains a fifth point: comment-content verification against repo state. The four-point pattern was: (i) PR comments both endpoints, (ii) branch state, (iii) file content against prescription, (iv) phantom-action audit. The fifth point: (v) comment-content claim verification against repository state via `gh api` for any claim of a commit SHA, file addition, or file modification.

The fifth point is operationally cheap: each `gh api repos/.../commits/<sha>` call is a single HTTP request; failures return 422 cleanly; success returns the commit object. The cost is one additional `gh api` call per reviewer claim of a commit SHA. The benefit is structural: the Architect adjudicates against verified repository state rather than against the reviewer's assertion of repository state.

### §2.6. Empirical evidence from PR-8

Both sub-shapes were observed in the PR-8 cycle:

- **Sub-shape A**: at T+88s post-PR-open, `chatgpt-codex-connector[bot]` posted a comment claiming completion of an `@codex review` follow-up. Architect-side post-handback verification surfaced the discrepancy via `gh api repos/.../commits/9f3955f` returning 422. Adjudication: comment treated as informational-only; no action attributed to the phantom artifacts.

- **Sub-shape B**: Codex post-PR pass-2 P1 finding referenced phantom SHA `88e8f74`. The finding's substantive content was correct (path-(a) revise on the cited cross-surface count claim); the SHA citation was a hallucination. Architect-side post-handback verification surfaced the discrepancy via `gh api repos/.../commits/88e8f74` returning 422. Adjudication: substantive content path-(a) revised; phantom citation noted as informational.

The defect class is high-confidence. Two independent sub-shape observations within a single 3-file cycle on a single reviewer (Codex Cloud Connector) is strong evidence the defect class is structural to the reviewer's behavior, not incidental. The mitigation (fifth-point comment-content verification) is structurally cheap and structurally complete: any reviewer claim with verifiable repository-state correspondence is verifiable; any claim without verifiable correspondence is informational-only by construction.

## §3. Pass-shape correlation hypothesis (preliminary)

### §3.1. The hypothesis

Pass shape correlates with whether Codex finds substantive issues. Findings → formal Pull Request Review with line-level comments. Clean Approve → issue-comment only, no formal Pull Request Review, no line-level comments.

Confidence: preliminary; 3 data points across 2 cycles; consistent with hypothesis; needs approximately 3 more cycles for higher confidence. PMN-005 records the hypothesis with explicit confidence qualification; future cycles record their pass shapes against the hypothesis.

### §3.2. Empirical data from PR-7 and PR-8

| Pass | Cycle | Commit | Formal Pull Request Review | Line-level findings | Issue-comment verdict |
|---|---|---|---|---|---|
| 2 | PR-7 | `e212e36` | absent | none | "Codex Review: Didn't find any major issues. Swish!" |
| 1 | PR-8 | `6e9777e` | yes | 2 P2 | (none separate from formal review body) |
| 2 | PR-8 | `ec1eee7` | yes | 1 P1 | (none separate from formal review body) |
| 3 | PR-8 | `7040967` | absent | none | "Codex Review: Didn't find any major issues. Can't wait for the next one!" |

Three of these are cycle-trailing-clean-Approve passes (PR-7 pass-2 and PR-8 pass-3), or substantive-finding passes (PR-8 pass-1, PR-8 pass-2). Two of the cycle-trailing-clean-Approve passes (PR-7 pass-2 and PR-8 pass-3) landed on the issue-comment endpoint only, with no formal Pull Request Review object. The two substantive-finding passes (PR-8 pass-1 and PR-8 pass-2) created formal Pull Request Review objects with line-level comments and corresponding issue-comment summaries.

### §3.3. Hypothesis articulation

Findings → formal Pull Request Review path: when Codex's review of a commit produces line-level findings, the review-rendering surface emits both a formal Pull Request Review (with line-level comments attached) and an issue-comment summary. The formal Pull Request Review carries the substantive findings; the issue-comment summary carries the verdict text. Both endpoints land.

Clean Approve → issue-comment-only path: when Codex's review of a commit produces no line-level findings, the review-rendering surface emits only an issue-comment summary with the boilerplate-style verdict ("Codex Review: Didn't find any major issues. <enthusiasm-token>!"). No formal Pull Request Review object is created; the issue-comment is the sole substantive surface for the verdict.

The hypothesis is structural to Codex's review-emission behavior; it is not specific to this project. The implication is that single-channel polling on `gh pr view --json reviews` after a fix-up commit is unreliable for clean-Approve detection. The two-endpoint discipline (PMN-003 (e) refined) is necessary not just defensively but as the only reliable channel for the cycle-trailing pass shape.

### §3.4. Confidence qualification

The hypothesis is preliminary. Three data points across two cycles is suggestive but not conclusive. The hypothesis is consistent with the available evidence; the available evidence does not rule out alternative hypotheses (e.g., pass-shape correlates with `@codex review` invocation timing rather than with finding content; pass-shape correlates with commit-message length; pass-shape correlates with file-count-change magnitude). Approximately 3 more cycles are needed to test the hypothesis against alternatives.

PMN-005 canonicalizes the hypothesis with explicit confidence qualification. Future cycles record their Codex pass shapes (formal Pull Request Review present/absent; line-level findings count; issue-comment verdict text) and add to the data set. If the hypothesis holds across 5-6 cycles total, confidence promotes to "established" and the hypothesis becomes a canonicalized framework prediction. If the hypothesis fails across 5-6 cycles, the alternative hypotheses are tested.

### §3.5. Operational implication for current cycles

Independent of confidence level, the operational implication is clear: the two-endpoint discipline is required. PMN-003 (e) refined remains the canonical discipline. PMN-005 §3 records the empirical observation that the cycle-trailing-clean-Approve pass shape is the issue-comment-only path; reliance on the formal Pull Request Review endpoint alone for cycle-trailing-clean-Approve detection is structurally unreliable.

The hypothesis does not change the discipline; it provides additional empirical grounding for why the discipline is structurally necessary. PMN-005 cross-references PMN-003 (e) refined and PMN-004 §4 (which empirically confirmed PMN-003 (e) refined on the PR-7 cycle data).

## §4. Path-(a)-revision-propagation gap on Validation run Evidence / cumulative diff stats sub-rule (refinement of PMN-004 §5 (e))

### §4.1. The defect

The PR-8 cycle had three iterations of prose-arithmetic drift on the same handoff §"Validation run" Evidence section. The Evidence text contained approximate per-file insertion counts (`~155 / ~62 / ~95`) that were stale pre-revision rough estimates. After path-(a) revisions to claims 6/7/9/10 in the PR-8 review-context, the per-file insertion counts changed (actual: 117 / 112 / 128) but the Evidence section was not updated to reflect the post-revision actuals. The drift was caught only by Codex post-PR pass-1 P2 finding 2.

The defect is a §24.2(b) artifact-content assertion sub-shape with propagation-incompleteness flavor. PMN-003 (a) refined recapitulation-consistency re-check after in-cycle path-(a) revisions covers the four claim-touched files; PMN-004 §2.3 extended the re-check to include verification-command surfaces. Neither extension explicitly named cumulative diff stats / approximate counts as a re-check target.

### §4.2. The recursive irony

The PR-8 cycle's deliverable, which articulates the very sub-finding PMN-004 §2.3 ("the recapitulation-consistency re-check on the four claim-touched files must extend to the four claim-touched verification-command surfaces"), manifested the same defect class in its own Validation run Evidence section. The discipline articulated in PMN-004 §5 (e) prose-arithmetic decomposition was not sufficient by itself; an explicit sub-rule for "after path-(a) revisions, re-derive cumulative diff stats" was missing.

This is a recursive self-instantiation of the claim-text drift defect class PMN-004 §2 articulates. PMN-004 §2.2 explicitly noted that "§23.6 self-review caught five instances of the defect class pre-handoff" and "§23.6 self-review missed a sixth instance" — the PR-8 cycle adds another instance to the missed-by-self-review category, surfaced only by post-PR Codex pass-1.

### §4.3. Additional empirical evidence — section-citation slip surviving §23.6 self-review in the PR-8→PR-9 session handoff

A further instance of the defect class surfaced in the PR-8→PR-9 Architect-to-Architect session handoff itself. The handoff's §9 step 5 and §10 both reference "PMN-004 §10 4-iteration pattern." PMN-004 has §1 through §8 only; PMN-004 has no §9 and no §10. Verification: `grep -cE "^## §[0-9]" docs/post-merge-notes/PMN-004-pr-7-cycle-learnings.md` returns `8`; PR-8 review-context claim 9 attests this count.

The "4-iteration pattern" referenced in the handoff is best interpreted as referring to PR-7's empirical iteration count documented in PMN-004 §1 cycle context: §23.6 Architect self-review (caught 5 instances per §2.2) + Codex desktop pre-commit review three passes to clean (caught 4 Blocking + 2 Major in pass-1, 3 Blocking in pass-2, clean in pass-3) = 4 review iterations to fixed-point. The pattern is real and is documented in PMN-004 §1; the citation pointing to "§10" is the slip.

The handoff's §10 self-attestation explicitly stated "§23.6 4-iteration-to-fixed-point self-review (PMN-004 §10): applied to this handoff prior to providing it; one iteration sufficient for convergence on this artifact (single-document scope, no cross-deliverable surfaces)." One iteration was not sufficient for convergence on this specific section-citation. The slip survived the prior session's §23.6 self-review.

This is empirical evidence that section-citation drift can survive §23.6 self-review even when the author is aware of the discipline and explicitly attests application. The mitigation is the cumulative-diff-stats sub-rule articulated in §4.4 below combined with the PMN-004 §5 (f) section-citation correctness sweep applied iteratively to convergence.

### §4.4. Sub-rule within PMN-004 §5 (e) prose-arithmetic decomposition

PMN-005 refines PMN-004 §5 (e) by adding an explicit sub-rule:

> **(e.1) Cumulative-diff-stats re-derivation after path-(a) revisions.** After any path-(a) revision to any artifact in a deliverable, re-derive any cumulative diff stats and any approximate counts to landed exact counts. Specifically: handoff §"Validation run" Evidence per-file insertion / deletion counts; total-file-count claims; tracked-file-count delta; any "approximate" or `~`-prefixed numbers anywhere in the deliverable. The re-derivation must be explicit (run `git diff --stat` with the actual ref against actual current branch state) rather than inferential.

The sub-rule is a refinement of the existing discipline, not a new top-level discipline. PMN-005 inherits all of PMN-004 §5 (a)-(f) by reference; the sub-rule (e.1) extends (e) with an explicit re-derivation requirement triggered by path-(a) revisions.

### §4.5. Where the sub-rule applies

The sub-rule (e.1) applies to all four review surfaces:

- **§23.6 Architect self-review (Architect side)**: at Architect-authored deliverable spec self-review, after any path-(a) revision applied during self-review iteration, re-derive cumulative diff stats explicitly via `git diff --stat HEAD` (or equivalent) against actual current state.

- **Step-10 self-verification (Builder side)**: at Builder step-10 self-verification, after any path-(a) revision applied during step-10 iteration, re-derive cumulative diff stats explicitly via `git diff --stat HEAD` against actual current state.

- **Pre-commit Codex review (Codex side)**: pre-commit Codex review identifies any prose-arithmetic claim with approximate or `~`-prefixed numbers; verifies the number against actual `git diff --stat` output; flags any divergence as a Major or Blocking finding depending on whether the claim is committed or pre-commit-existing.

- **Architect-side post-handback verification (Architect adjudication side)**: at PR-close hand-back, the Architect-side four-point check pattern (extended in §2.5 above to a five-point pattern) gains a sixth point: verify cumulative-diff-stats claims in handoff Evidence section against actual `gh api repos/.../pulls/<n>/files` output for the merged PR.

The sub-rule's operational cost is low: one `git diff --stat HEAD` invocation per path-(a) revision iteration, plus the visual cross-check of any `~`-prefixed numbers in the deliverable's prose. The benefit is structural: cumulative diff stats are then verified-by-construction at the time of authoring, not by post-hoc Codex finding.

### §4.6. Carryforward to PMN-005's own self-review

The sub-rule (e.1) is applied to PMN-005's own §23.6 self-review. The Architect's deliverable spec for TASK-0009 includes explicit cumulative-diff-stats verification at §12 self-review record. The Builder's step-10 self-verification at §7 of this spec includes explicit cumulative-diff-stats verification. The pre-commit Codex review prompt at §4 of this spec embedded in the PR-9 review-context file includes the cumulative-diff-stats verification prompt.

## §5. Refined disciplines summary

PMN-005 introduces no new top-level disciplines. PMN-005 refines two existing disciplines and inherits the rest by reference.

**Refinement 1 — PMN-003 (e) refined two-endpoint discipline (extended in PMN-005 §2.5):** any reviewer comment claiming a commit SHA, a file addition, a file modification, or any other action with verifiable repository-state correspondence must be verified against the actual repository state via `gh api repos/.../commits/<sha>` and `gh api repos/.../contents/<path>` (or equivalent endpoints for non-commit non-file claims) before treating the claim as effective. If unreachable, treat the comment as informational-only at most. The two-endpoint discipline establishes that the comment was *delivered*; comment-content verification against repo state establishes whether the comment's *claims correspond to actionable repository state*. These are separate verification steps; both required.

The refinement adds a fifth point to PMN-003 (g) Architect-side post-handback four-point check pattern: (v) comment-content claim verification against repository state for any claim of a commit SHA, file addition, or file modification.

**Refinement 2 — PMN-004 §5 (e) prose-arithmetic decomposition (extended in PMN-005 §4.4):** sub-rule (e.1) cumulative-diff-stats re-derivation after path-(a) revisions. After any path-(a) revision to any artifact in a deliverable, re-derive any cumulative diff stats and any approximate counts to landed exact counts. Specifically: handoff §"Validation run" Evidence per-file insertion / deletion counts; total-file-count claims; tracked-file-count delta; any "approximate" or `~`-prefixed numbers anywhere in the deliverable. The re-derivation must be explicit (run `git diff --stat` with the actual ref against actual current branch state) rather than inferential.

Inherited disciplines (standing per PMN-004 §5):

- **(a) Severity taxonomy three-level enumeration** — Blocking / Major / Minor with explicit definitions; no two-level framing acceptable.
- **(b) Verification-command portability** — bash, Windows cmd, or PowerShell forms supplied; single-shell-only commands without explicit qualifier are defects.
- **(c) No future-tense claims at pre-commit time** — every Builder claim's verification command must produce verifiable output at pre-commit time against the working tree.
- **(d) Pre-commit cross-surface scope clarity** — count claims and consistency checks enumerate only the pre-commit-existing surfaces; PR body and other post-commit surfaces are explicitly segregated to post-PR verification scope.
- **(e) §23.6 prose-arithmetic decomposition** — every prose-arithmetic claim is decomposed into operands and a relationship; the decomposition is verified at §23.6 self-review and at step-10 self-verification. Sub-rule (e.1) added by PMN-005.
- **(f) Section-citation correctness sweep** — every `§N` citation refers to a section that exists in the cited document at the cited number; sweep applied iteratively to convergence.

Defects identified by PMN-005 that the existing disciplines did not catch:

- The reviewer-claimed-effects-don't-land defect class operates on a verification surface (external system behavior) that PMN-003 (e) refined did not explicitly include; PMN-005 extends PMN-003 (e) refined to include comment-content verification against repo state.
- The cumulative-diff-stats sub-rule (e.1) operates on a re-derivation surface (path-(a)-revision-triggered cumulative-stats re-derivation) that PMN-004 §5 (e) did not explicitly include; PMN-005 adds (e.1) as a sub-rule within (e).
- The section-citation slip in the PR-8→PR-9 Architect-to-Architect session handoff surviving §23.6 self-review (per §4.3 above) is a §5 (f) section-citation correctness sweep failure mode; the existing discipline is correct but the iterative-to-convergence application was insufficient at one iteration. PMN-005 does not modify (f) but notes the empirical evidence that one iteration is sometimes insufficient even when the author is aware of the discipline and explicitly attests application; iterative application until no slip is detected (fixed-point convergence) is the standing discipline.

## §6. Anticipated forward integration

**TASK-0010 spec (next, core.md Part A authoring)** carries forward all six PMN-004 §5 disciplines (a)-(f) plus PMN-005's two refinements. Specifically:

- Severity taxonomy three-level enumeration in PR-10 review-context (per (a)).
- Verification commands in bash + cmd forms throughout (per (b)).
- All Builder claims are pre-commit-verifiable (per (c)).
- Pre-commit cross-surface scope clarity (per (d)).
- §23.6 prose-arithmetic decomposition with sub-rule (e.1) cumulative-diff-stats re-derivation applied to the spec's content tables and prose narratives.
- Section-citation correctness sweep applied iteratively to convergence (per (f)).
- Architect-side post-handback verification five-point check pattern (per PMN-005 §2.5; extends PMN-003 (g) four-point pattern with comment-content claim verification).

TASK-0010 (core.md Part A authoring) materializes §8.1.1.1 Reviewer dual-signal output handling and §8.1.1.2 Reviewer claimed-action verification canonical text. The PMN-005 reviewer-claimed-effects-don't-land defect class informs §8.1.1.2 substantively: the canonical text on Reviewer claimed-action verification names the two sub-shapes (entirely-fabricated and correct-content-fabricated-citation) and prescribes the comment-content verification against repo state as the canonical mitigation.

The pass-shape correlation hypothesis (PMN-005 §3) is preliminary at canonical-content-authoring time. TASK-0010 spec §8.1.1.1 Reviewer dual-signal output handling does not canonicalize the hypothesis as a framework prediction; instead, it canonicalizes the operational discipline (two-endpoint polling per PMN-003 (e) refined) that the hypothesis empirically grounds. If the hypothesis is confirmed across 3 more cycles, a future PMN can promote the hypothesis to a canonical framework prediction; the canonical framework discipline (two-endpoint polling) is independent of hypothesis confirmation.

**TASK-0011 spec (subsequent, core.md Part B authoring)** materializes §23.6 enhancements canonically. Disciplines (a), (e), (f) plus sub-rule (e.1) become canonical §23.6 sub-section text. Disciplines (b), (c), (d) materialize in their respective §-sections. The §23.6 4-iteration-to-fixed-point self-review pattern (empirically observed in PR-7 per PMN-004 §1; observed surviving in the PR-8→PR-9 session handoff section-citation slip per PMN-005 §4.3) materializes as canonical §23.6 sub-section text on iterative self-review.

**Future PMN/ADR cycles** apply PMN-005's two refinements globally. PMN-006+ and ADR-004+ inherit the refinements as standing.

**Monitoring item M-A6**: PMN-rate-vs-budget tracking. Pre-PMN-005 rate: 4 PMNs in 8 merged cycles = 50%. Post-PMN-005-merge: 5 PMNs in 9 merged cycles = 56%. ADR-003 Decision 3 forecast range: 3-7 PMNs across 13 substantive cycles = 23% to 54% rate. The post-PMN-005-merge rate (56%) exceeds the forecast upper bound (54%) by 2 percentage points. The exceedance does not trigger M-A6 promotion (trigger remains at TASK-0023, three contingency slots remaining: TASK-0024, TASK-0025, TASK-0026). The 2-pp exceedance is noted as a monitoring continuity item; surfaced as evidence at TASK-0023 evaluation point. If the rate stays at or above 50% across the next 3-4 substantive cycles, ADR-004 reservation extension may be warranted earlier than TASK-0023.

The decomposition is explicit per (e):
- Pre-merge: 4 PMNs (PMN-001 + PMN-002 + PMN-003 + PMN-004) in 8 merged cycles (PR-1 + PR-2 + PR-3 + PR-4 + PR-5 + PR-6 + PR-7 + PR-8); 4/8 = 0.5 = 50%.
- Post-PMN-005-merge: 5 PMNs (PMN-001 + PMN-002 + PMN-003 + PMN-004 + PMN-005) in 9 merged cycles (PR-1 through PR-9); 5/9 = 0.5555... ≈ 56% (rounded to nearest percentage point).
- Forecast upper bound: 7 PMNs across 13 substantive cycles; 7/13 = 0.5384... ≈ 54% (rounded to nearest percentage point).
- Exceedance: 56% − 54% = 2 percentage points.

## §7. Cross-references

- **ADR-001** decisions 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15 unchanged; decision 8 PR sequence portion superseded by ADR-003 (per PR-7).
- **ADR-002** Decision 3 anticipation pattern absorbed and extended by ADR-003 Decision 3; PMN-005 inserts under ADR-003 Decision 3 contingency budget.
- **ADR-003** Decision 2 (12 substantive content PR plan, anticipated PR-8 through PR-19 in original numbering, shifted to PR-9 through PR-20 post-PMN-004, shifted to PR-10 through PR-21 post-PMN-005); Decision 3 (TASK reservation through TASK-0026, consuming a second contingency slot for PMN-005; five remaining); §Consequences (per-PR-row-update discipline for README and stub frontmatter, first empirically tested at PR-10 / TASK-0010 close — the README "Canonical law" row staying briefly stale across PR-8 and PR-9 cycles is the explicit second test of the discipline ADR-003 §Consequences established).
- **PMN-001** (h.2) file-based Builder direction; (k) Linked PR fix-up substitution.
- **PMN-002** (a) refined imperative `Action:` phrasing; (d) code-fenced thin pointer prompt.
- **PMN-003** (a) refined recapitulation-consistency re-check (extended in PMN-004 §2.3 to include verification-command surfaces); (e) refined two-endpoint review polling (extended in PMN-005 §2.5 to include comment-content verification against repo state); (g) four-point Architect-side post-handback verification (extended in PMN-005 §2.5 to a five-point pattern); (j) and (m) receiving-surface format declaration.
- **PMN-004** §2 claim-text drift defect class characterization; §2.3 recapitulation-consistency re-check extension to verification-command surfaces; §4 two-endpoint discipline empirical confirmation; §5 six refined disciplines (a)-(f); §5 (e) prose-arithmetic decomposition (extended in PMN-005 §4.4 with sub-rule (e.1) cumulative-diff-stats re-derivation).
- **FEAT-0001** PR-2 v3 framework package scaffold spec — the staleness-defect substrate that ADR-003 + PR-7 sweep resolved structurally.
- **PR-8 (TASK-0008)** the cycle whose learnings PMN-005 captures.
- **Session handoff 2026-05-02** (PR-8 close → PMN-005 / TASK-0009 authoring) the source of the three candidate observations and the seven prior-session decisions confirmed by owner.
- **AMAS v2.14.1 §8.1.1.1** Reviewer dual-signal output handling — pass-shape correlation hypothesis is a §8.1.1.1 application surface.
- **AMAS v2.14.1 §8.1.1.2** Reviewer claimed-action verification — reviewer-claimed-effects-don't-land defect class is a §8.1.1.2 application surface.
- **AMAS v2.14.1 §18** post-merge note canonical form — PMN-005 follows it.
- **AMAS v2.14.1 §23.6** Architect pre-handoff self-review — sub-rule (e.1) cumulative-diff-stats re-derivation extends §23.6 sweep scope.
- **AMAS v2.14.1 §24.2(a)** external-system-behavior assertion sub-shape — both sub-shapes of reviewer-claimed-effects-don't-land are §24.2(a) instances.
- **AMAS v2.14.1 §24.2(b)** artifact-content assertion sub-shape with propagation-incompleteness flavor — path-(a)-revision-propagation gap on Validation run Evidence is a §24.2(b) instance.
- **AMAS v2.14.1 §24.3** receiving-side caveat-discipline — Architect receiving Builder hand-back claims; PMN-005 §2.5 five-point check extends the pattern.
