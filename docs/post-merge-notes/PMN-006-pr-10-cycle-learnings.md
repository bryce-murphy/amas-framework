# PMN-006 — PR-10 cycle learnings: verification-artifact-validity discipline split (g)/(h) + cross-document state verification (i) + bounded-continuation rule + four preliminary observations

## Status

Recorded — 2026-05-02

PMN-006 inserts under ADR-003 Decision 3 contingency budget. Consumes one of five remaining contingency slots; four remaining (TASK-0023 through TASK-0026 unconsumed).

## §1. Cycle context

PR-10 (TASK-0010) authored core.md Part A — the first substantive-canonical-content cycle in the project. Five canonical leaf sections (§8.1.1.1 Reviewer dual-signal output handling; §8.1.1.2 Reviewer claimed-action verification; §23.6.1 §23.6 self-review sweep set; §23.6.2 §23.6 self-review iteration count empirical pattern; §24.3.1 Architect ← Builder hand-back symmetric-application clause) plus minimal parent frames for §8 / §23 / §24 landed at squash-merge `80f5a4a` on 2026-05-02.

Cycle shape was novel relative to all prior cycles: 5 commits on the feature branch (PR-open commit + 4 Codex-driven fix-ups); 5 Codex post-PR review passes absorbed via two-endpoint `--paginate` poll discipline (PMN-003 (e) refined + PMN-005 §2.5). Substantive empirical material accumulated from this cycle drives PMN-006 substantively.

Nine observation clusters drive PMN-006 (§2 through §7 below): the 8 originally scoped clusters (a)-(h) plus (i) cross-document state verification, surfaced by Builder pre-flight on the TASK-0011 spec itself and adopted into scope at owner adjudication post-pre-flight. Substantively larger than typical small-PMN (PMN-005 had 3 observations; small-PMN cadence has historically run 3-5); largest PMN since PMN-001 (15 observations).

### §1.1. Honesty record

Nine defects originated in or were surfaced during this cycle:

1. **§8.1.1.1 polling commands (canonical text on main)** — strict `>` timestamp filter has same-second-event dropout failure mode (sub-shape (h.3) per the (g)/(h) discipline split this PMN canonicalizes — see §3). Authored by Architect at PR-10 spec time, missed by Architect §23.6 self-review (6 iterations), missed by Builder step-10 sweep, missed by Codex pre-commit, missed by Codex post-PR passes 1-4. Caught by Codex post-PR pass 5. The defect applies symmetrically to both endpoints in core.md §8.1.1.1: `pulls/{pull_number}/reviews` filtering on `submitted_at` and `issues/{issue_number}/comments` filtering on `created_at`.

2. **§24.3.1 point 2 (canonical text on main)** — `git fetch && git status` does not prove tip-SHA; should be `git rev-parse HEAD` plus expected SHA comparison (sub-shape (h.2)). Same review-chain history as defect 1: authored by Architect, missed by all 4 prior review stages, caught by pass 5.

3. **§23.6 sweep-set gap** — existing PMN-004 §5 (a)-(f) + PMN-005 sub-rule (e.1) sweep set did not include verification-artifact-validity as a class. Defects 1 and 2 are the empirical surfacing of the gap. Motivates the (g)/(h) discipline split this PMN canonicalizes.

4. **PR-10→PMN-006 inbound handoff §2 .gitkeep claim was correct; PMN-006 spec session-2 authoring inverted empirical reality**. The PR-10→PMN-006 inbound handoff said `docs/post-merge-notes/` should contain 6 entries (5 PMN + .gitkeep). PMN-006 spec session-2 authoring (Architect, this cycle) misread Builder's pre-scoping diagnostic and inverted the framing into "handoff was wrong; .gitkeep removed once tracked content lands; expect 5." Builder pre-flight verified via `git ls-files docs/post-merge-notes/` and surfaced that `.gitkeep` IS tracked (added at bootstrap commit `c1ec54f`, never removed). The original handoff was correct; the spec's correction-of-the-handoff was wrong. §24.2(b) artifact-content assertion sub-shape: spec asserted repository state without verifying against actual `git ls-files`.

5. **PMN-006 cycle pre-scoping verification-command portability slip** — Architect issued Bash-form verification commands (`#` comments, `wc`, `ls`) in instructions to a cmd terminal. PMN-004 §5 (b) discipline already canonicalized portability across bash/cmd/PowerShell. Recursive irony: Architect about to canonicalize a (b) sweep-set extension slipped on the existing (b) discipline.

6. **PMN-006 spec §4.1 substitution-incompleteness vs core.md HEAD reality** — initial spec §4.1 covered only the `created_at` form of the strict-`>` filter and assumed a single endpoint. core.md HEAD §8.1.1.1 has two endpoints with two different timestamp fields (`submitted_at` for reviews; `created_at` for comments); (h.3) discipline applies symmetrically. Initial §4.1 also omitted the surrounding `select(.user.login==...)` author filter; literal application would have discarded it. Surfaced by Builder pre-flight pass 1; spec re-authored to cover both endpoints and preserve the author filter. Recursive-self-instantiation: defect 6 is itself an (h.2) sub-shape (command-achieves-claimed-verification) within the spec's correction directive.

7. **PMN-006 spec §5 step 2 reservation-mechanism error** — initial spec §5 step 2 directed Builder to "Add row to `docs/task-reservations.md` (or equivalent per current convention at HEAD)". No such file exists; the actual ADR-003 Decision 3 reservation mechanism is handoff-file-presence (the `docs/handoffs/TASK-####-<slug>.md` file IS the reservation). Initial spec also referenced "ADR-001 decision 8 + ADR-002 task-reservation amendment" — both partially superseded by ADR-003 Decision 3. Surfaced by Builder pre-flight pass 2 after spec revision absorbing defects 1-4 + defect 6 from pass 1. Recursive-self-instantiation: defect 7 is an (i.2) sub-shape (filesystem path assertion) — spec asserted a filesystem path without verification. The (i) discipline that this very PMN canonicalizes did not catch this in spec §23.6 self-review iterations 1-6; only Builder's iterative pre-flight surfaced it.

8. **PMN-006 spec iteration-7 / iteration-8 propagation gaps — three residuals** — spec iteration 7 (adopting (i) cluster) and iteration 8 (rewriting §5 step 2) propagated through most surfaces but missed three summary/intro surfaces: §5 preamble (still referencing "ADR-001 decision 8 + ADR-002 task-reservation amendment" instead of ADR-003 Decision 3); §6 sweep-set intro (still describing inheritance as `(g) and (h)` instead of `(g), (h), and (i)`); §12.1 sweep-set self-application list (still missing (i)). Surfaced by Builder pre-flight pass 3. Routed to path-(β) record-and-proceed per bounded-continuation rule (§5 below) because same-class (recapitulation-consistency / cross-document state verification) as defects 6/7. The decision NOT to apply iteration-9 micro-fix is itself empirical material for §7 iterative-pre-flight pattern preliminary refinement: each iteration in response to pre-flight introduces new propagation surfaces; iteration-9 micro-fix would be the same shape of revision that produced residuals 1-3 in the first place. The bounded-continuation rule serves as the structural stop condition for spec-revision iterations triggered by pre-flight findings — first finding in a defect class triggers path-(a) revision (iteration 8 was that revision); subsequent same-class findings route to PMN evidence (defect 8 is that evidence).

9. **PMN-006 spec deliverable 5 asserted a non-existent README "PMN file table"** — spec §2 deliverable 5 directs Builder to "append PR-11 row to PMN file table" and spec §5 step 8 says "Update README PMN file table to add PR-11 row." Surfaced by Builder during step 8 execution: README has no PMN file table — only the Package layout tables (Canonical law, Prompts, Templates, Actions, Appendices), all for substantive-content scaffold stubs. Historical pattern (verified via `git log --all --oneline -- README.md`): PMN-001 / PMN-002 / PMN-003 / PMN-004 / PMN-005 PRs did NOT modify README. The spec's deliverable 5 thus has no extant target. Routed to path-(β) record-and-proceed per bounded-continuation rule §5.3 (same (i) class as defects 6/7/8 — Architect-asserted facts about target-document state not verified against actual state). Step 8 SKIPPED; deliverable count adjusts from 5 deliverables to 4 (3 new files + 1 file modification, not 2 file modifications); cumulative-diff-stats and cross-surface count claims downstream adjust accordingly. **Sub-shape**: (i.3) content-pattern assertion — spec asserted a specific table ("PMN file table") existed in README; actual file content does not contain such a table. The defect was missed by Architect §23.6 self-review iterations 1-8, missed by Builder pre-flight passes 1-3 (none of those passes ran a verification command against README to check for the asserted table). The verification command Builder pre-flight should have run is `grep -in "PMN file" README.md` or equivalent; not having done so during pre-flight is itself a (i) sweep gap, surfaced empirically only at step 8 execution time when Builder went to perform the asserted update.

The framework operated as designed for defects 1 and 2. Multi-stage review (§23.6 self-review + Builder step-10 + Codex pre-commit + Codex post-PR auto-fire + Codex post-PR manual `@codex review`) is load-bearing, not redundant. Pass 5 caught what 4 prior review stages missed. Defects 6, 7, 8 were caught by Builder pre-flight passes 1, 2, 3 respectively before any commits; defect 9 was caught by Builder at step 8 execution time (post-pre-flight). The framework's session-handoff verification step (spec §5 step 1) is structurally load-bearing for defects of class (i.1) and (i.2) (tracked-file presence; filesystem path); defect 9 surfaces a (i.3) content-pattern sub-shape that requires verification at the time the assertion is acted on (step 8 execution), not at session start when the assertion is read. This is a refinement to the (i) discipline canonical placement: (i.3) verification is properly distributed across the cycle's execution, not concentrated at session start. Defects 3, 4, 5, 6, 7, 8, 9 are §23.6 sweep-set gaps that the (g)/(h)/(i) discipline split (§3 and §7 below) addresses canonically.

### §1.2. Substantive-content scope step-up

PMN-006 has 9 observation clusters; PMN-005 had 3; small-PMN cadence has historically run 3-5. Substantive-content-authoring scope (PR-10, Part B forthcoming at TASK-0012, later large canonical documents split across cycles per `partial` convention per §6) produces empirical material at a step-up rate that the framework's small-PMN cadence does not fully accommodate at single-cycle scope.

PMN-006 records this as observation only. No M-A8 monitoring item is introduced this cycle — single data point insufficient for monitoring-item promotion per the standard applied to clusters (a) and (c) (preliminary hypothesis pending ~3 cycles of evidence). If Part B (TASK-0012) and subsequent multi-cycle canonical-document authoring also produce step-up scope, M-A8 (or ADR-004-level cadence adjustment) materializes at TASK-0023 reconciliation with empirical grounding.

## §2. (a) §23.6.2 convergence-count role-axis-dependence — preliminary hypothesis

§23.6.2 canonical text (landed at PR-10) explicitly names 4 as empirical-not-normative: "the four-iteration figure is empirical pattern, not normative target; convergence is the normative criterion." PR-10 cycle data adds a refinement candidate.

**Empirical**: Architect content-authoring at substantive-spec scope (TASK-0010 spec, ~1052 lines): 6 iterations to convergence (recorded in PR-10 spec §12.1). Builder mechanical-application at substantive-content scope: 2-3 iterations (section-citation sweep: 2 iterations; cumulative-diff-stats sub-rule (e.1) per PMN-005 §4.4: 3 iterations).

**Hypothesis**: convergence-count is **role-axis-dependent** in addition to scope-axis-dependent. Architect authoring substantive content from scratch needs more iterations than Builder mechanically applying byte-exact prescription. Mechanism candidate: byte-exact prescription paste transfers cognitive-frame work from Builder to Architect — the iteration that authored the canonical text (Architect) is different from the iteration that pasted it (Builder); Architect's higher iteration count absorbs the cognitive-frame work that Builder no longer does at paste time.

**Single-data-point caveat**: single substantive-spec-scope cycle. ~3 more cycles needed before canonicalization. Part B (TASK-0012) provides next data point; subsequent canonical-document authoring (github-reference, usage-guide, templates) provides further data.

**No canonical change to §23.6.2 in this PMN**. Observation recorded; canonicalization deferred to PMN with sufficient evidence.

## §3. (b) → (g) + (h) split: verification-artifact-validity discipline canonicalization

PR-10 surfaced six sub-shapes empirically observed by Codex post-PR review where verification commands or claim blocks within committed artifacts had defects passing through prior review stages. The six sub-shapes resolve into two orthogonal discipline classes plus one re-classification.

### §3.1. (g) Verification-artifact internal consistency

The claim block (verification command, declared timing, example output, surrounding prose) is internally consistent — it agrees with itself.

**Sub-shapes**:

- **(g.1) Timing-correctness across surfaces**. Each verification command produces its asserted result at the verification time named (e.g., post-commit `git status` after staging is non-empty pre-commit; the timing label and example output must match the verification time the claim specifies). Caught by Codex pre-commit on TASK-0010 handoff.

- **(g.2) Within-claim-block label-vs-example consistency**. Within a single claim block, the label asserts a property the example output must carry (e.g., post-stage label paired with ` M`-format pre-stage output is mismatched). Caught by Codex post-PR pass 4.

### §3.2. (h) Verification-command operational correctness

The verification command's output domain actually proves what's claimed — independent of whether the claim block is internally consistent.

**Sub-shapes**:

- **(h.1) Pagination**. Verification commands must work under reasonable production conditions including page-boundary completeness (e.g., `gh api --paginate`). Caught by Codex post-PR pass 2.

- **(h.2) Command-achieves-claimed-verification**. The named verification command's output domain must cover the claim's verification need (e.g., `git status` does not prove tip-SHA; `git rev-parse HEAD` does). Caught by Codex post-PR pass 5. Drives the §24.3.1 point 2 canonical-text correction in PR-11.

- **(h.3) Filter-boundary completeness**. Strict-comparator filters on coarse-granularity inputs drop boundary-coincident emissions (e.g., strict `>` on second-granularity timestamps drops same-second emissions; `>=` plus last-seen-ID tie-breaker is the canonical form). Caught by Codex post-PR pass 5. Drives the §8.1.1.1 polling-commands canonical-text correction in PR-11 (applied symmetrically to both `submitted_at` and `created_at` endpoints).

### §3.3. Orthogonality of (g) and (h)

(g) and (h) are independent. A claim block can pass (g) while failing (h) — the §8.1.1.1 polling commands as authored in PR-10 had the strict `>` filter, the example output, and the declared timing all internally consistent (passed (g)), but the command's output domain didn't catch same-second emissions (failed (h.3)). A claim block can also pass (h) while failing (g) — operationally correct command paired with mislabeled timing or mismatched example output.

### §3.4. (b.3) reclassification — frontmatter-vs-body to PMN-003 (a) refined extension

PR-10 also surfaced frontmatter-vs-body consistency (when canonical content body is filled, frontmatter status / filled_by / etc. must reconcile to match), originally tracked as sub-shape (b.3). On reflection, this is not a verification-artifact-validity case but a recapitulation-consistency case — frontmatter location vs body location within the same file after body fill.

**Reclassified** as refinement to PMN-003 (a) refined recapitulation-consistency re-check: the re-check extends to frontmatter-vs-body reconciliation in addition to existing surfaces (PMN body vs verification prompts; multiple artifacts after path-(a) revision; verification-command surfaces per PMN-004 §2.3).

### §3.5. Canonical effects

- (g) and (h) added to the standing PMN sweep set as new top-level disciplines, alongside PMN-004 §5 (a)-(f) and PMN-005 sub-rule (e.1).
- PMN-003 (a) refined extended with frontmatter-vs-body sub-clause.
- core.md §8.1.1.1 polling commands corrected per (h.3) — applied symmetrically to both `submitted_at` (reviews endpoint) and `created_at` (comments endpoint), preserving `select(.user.login == "<reviewer>")` author filter.
- core.md §24.3.1 point 2 corrected per (h.2) — `git fetch && git status` replaced by `git rev-parse HEAD` + expected-SHA comparison (with `git status --porcelain` empty as additional clean-tree check).

## §4. (c) Pass-shape Reviewer-specificity — preliminary hypothesis

§8.1.1.1 canonical text says: "Substantive-finding pass shape: both endpoints emit. Formal Pull Request Review carries line-anchored findings; issue-comment summary carries verdict text restating the findings." Empirical observation across all 4 substantive-finding passes on PR-10 with `chatgpt-codex-connector[bot]` reviewer: endpoint (a) formal Pull Request Review emits (boilerplate body + line-anchored review comments); endpoint (b) issue-comment summary is silent (no separate emission beyond the formal review).

**Hypothesis**, two possibilities:
- (i) Reviewer-specific — `chatgpt-codex-connector[bot]` specifically emits this way; human-Reviewers may emit per the canonical text.
- (ii) Reviewer-implementation-specific — the codex-connector implementation emits this way; future bot-Reviewers may differ.

**Single-data-point caveat**: 4 passes within a single cycle on a single Reviewer. ~3 more cycles needed before canonical refinement.

**No canonical change to §8.1.1.1 in this PMN**. The two-endpoint polling discipline (PMN-003 (e) refined) remains correct independently of pass-shape framing — both endpoints must be polled to catch any pass shape, including this Reviewer's single-endpoint emission pattern.

## §5. (d) Iterative-fix-up-cycle pattern + bounded-continuation rule

### §5.1. Iterative-fix-up-cycle pattern

PR-10 had 4 fix-up commits driven by Codex auto-re-review on each push. Prior cycles (PR-2 through PR-9) had 0-1 fix-ups. Step-up correlates with substantive-content-cycle scope: PR-10 was the first substantive-canonical-content cycle, and the fix-up count steps up with empirical material density.

### §5.2. Auto-trigger reliability sub-observation

3/3 auto-triggers worked for passes 2-4 (auto-fired from each push). The 4th auto-trigger (pass 5 from `e686f9d` push) did not fire within a 25-minute timeout window. Manual `@codex review` invocation triggered pass 5 at ~10 minutes after invocation.

Possible causes (preliminary, single-data-point):
- Rate-limit / cooldown after 4 reviews in ~50 minutes.
- Below-threshold diff size (1 ins / 1 del at `e686f9d`).
- Codex's own decision-not-to-re-review heuristic.
- Transient outage.

Single data point; preliminary. Manual `@codex review` invocation remains the structural fallback per ADR-001 decision 11 (owner invokes Codex review).

### §5.3. Bounded-continuation rule

**Application context**: Reviewer post-PR review of a substantive-content cycle produces iterative findings (pass N → fix-up → pass N+1). The framework needs a stop condition; otherwise iteration is unbounded.

**Rule statement**: after any path-(a) revision addresses a defect class once, residuals of the same class detected in subsequent passes route to PMN evidence rather than fix-up #N+1. The first revision is a real correction; subsequent same-class detection is canonicalization material.

**Mechanism**: Architect-side judgment at adjudication time — is this finding a new defect class (path-(a) revision) or a residual of an already-revised class (path-(b) record-and-proceed; carry to PMN)?

**Empirical grounding (PR-10)**: pass 5 produced two findings ((h.2) and (h.3)). Both were of the same class (verification-command operational correctness) as findings already addressed in passes 1-4 on different commands. Pass 5 findings were absorbed-but-not-actioned per this rule applied at adjudication time; canonical-text corrections to §8.1.1.1 and §24.3.1 land in PR-11 (this cycle) rather than as fix-up #5 in PR-10.

**Empirical grounding (PR-11 spec authoring)**: the rule generalizes across iteration-pair surfaces — first applied at the Reviewer post-PR review surface (where it was canonicalized), then applied at the Architect-side spec-revision surface in response to Builder pre-flight findings. Iteration 8 was the path-(a) revision for cross-document state verification residuals; defect 8 (residuals 1-3 from pre-flight pass 3) is the same-class subsequent finding routed to PMN evidence rather than iteration-9 fix-up. Owner-adjudicated this generalization at PMN-006 cycle.

### §5.4. Cross-reference parallel bounded-iteration patterns

- §23.6.2 4-iteration-to-fixed-point self-review (PMN-004 §1).
- PMN-005 §4.4 sub-rule (e.1) cumulative-diff-stats re-derivation triggered by path-(a) revisions.
- §5.3 above bounded-continuation rule at Reviewer post-PR review surface; generalized this cycle to spec-revision surface.

The bounded-continuation rule is a third member of the bounded-iteration family. (d) sub-observation: the rule generalizes across iteration-pair surfaces, not Reviewer-specific. Empirical grounding for the cross-surface generalization is two cycles (PR-10 Reviewer surface; PR-11 spec-revision surface) — preliminary. ~2-3 more cross-surface applications needed before canonicalization.

### §5.5. Canonical placement

Sub-rule under §8.1.1.x cluster (specific §-numbering: §8.1.1.3 if Part A established the .1/.2 split firmly; otherwise sub-bullet within §8.1.1.1). Light touch; not a new top-level §-section. Builder authors per current core.md structure at HEAD when the rule is canonicalized in core.md (deferred to Part B per §6 below).

## §6. Refinement and convention items grouped

### §6.1. (e) Spec-source-vs-canonical-text divergence after fix-up

**Empirical**: when canonical text is corrected via fix-up post-spec-paste, the gitignored spec source diverges from main. PR-10 demonstrated the divergence after fix-up #2 (`--paginate` correction).

**Sub-rule recommendation**: spec source amended OR explicitly archived as superseded; future cycles paste from main, not spec.

**Practical impact** low at PR-10 close (spec is gitignored per ADR-001 decision 15; only relevant if Architect re-references for next-cycle spec authoring). Sub-rule recorded for cycles where re-reference might occur. No canonical change in this PMN.

### §6.2. (f) M-A7 promotion — operationally canonical

Three data points of the merge-commit-body data integration pattern:

1. `3d10c76` (PR-9 squash) — merge body integrated PMN-005 finalized observations including post-PR-window content.
2. `80f5a4a` (PR-10 squash) — merge body integrated post-PR-review-window content (5-pass absorption summary; PMN-006 (b) taxonomy in final form; pass-5 findings; auto-trigger sub-observation).
3. `80f5a4a` merge body explicitly self-references the pattern: "M-A7 promotion trigger met (second instance of the merge-commit-body data integration pattern this cycle)" — strongest possible empirical confirmation.

**M-A7 advances** from candidate to **operationally canonical pending §-section text in core.md**. §-section text in core.md (placement TBD between §17 cycle-close and §18 trigger discipline) defers to Part B authoring (TASK-0012). Authoring §-section text in PMN-006 without surrounding §17 / §18 context risks the same in-isolation-correctness-but-mis-fit problem the §8.1.1.1 and §24.3.1 defects exhibit.

**No core.md change in this PMN for M-A7**. Status updated in PMN-006 monitoring register.

### §6.3. (g) `partial` status convention

Project-wide convention introduced this cycle for canonical documents filled per part. Current usage: core.md frontmatter `status: partial` after PR-10 merge (Part A in; Part B pending). Future large canonical documents split across multiple cycles inherit the convention.

Cross-reference recorded; small enough to canonicalize via PMN-006 cross-reference rather than ADR or §-section. **No core.md change for the convention itself in this PMN**.

### §6.4. (h) Substantive-reading version-bump trigger criteria

PR-10 applied substantive-reading interpretation (600+ lines of new canonical text = feature event regardless of placement within existing §-numbering) per PR-10 spec §1.4. Bumped v2.14.1 → v2.15.

**Trigger criteria are under-formalized**: strict-literal reading of prior versioning convention would have produced no bump or patch only. PMN-006 records the criterion ambiguity. Canonicalization deferred to §18 trigger discipline at later applicable cycle. **No core.md change in this PMN for (h)**.

## §7. (i) Cross-document state verification — discipline canonicalization

This cluster is the third sweep-set extension this PMN canonicalizes (alongside (g) and (h)) and is empirically grounded by Builder-pre-flight findings on PMN-006 cycle's own TASK-0011 spec.

### §7.1. Background

§23.6 self-review applied in isolation by Architect produced false-positive convergence at iteration 5 on the TASK-0011 spec. Builder pre-flight at spec §5 step 1 surfaced 4 substantive defects that survived all 5 Architect iterations:

1. `.gitkeep` tracked-file presence inverted from empirical reality (per §1.1 defect 4).
2. `core.md` filesystem path assumed (`docs/spec/core.md`) vs actual (repo root).
3. core.md §8.1.1.1 has TWO endpoints with TWO timestamp fields (`submitted_at` reviews + `created_at` comments); spec §4.1 covered only one (per §1.1 defect 6).
4. core.md §8.1.1.1 selectors wrap a `select(.user.login == "<reviewer>")` author filter; spec §4.1 substitution as authored would have discarded it (per §1.1 defect 6).

A fifth defect surfaced on Builder pre-flight pass 2 after spec revision: §5 step 2 directed Builder to `docs/task-reservations.md` — non-existent file (per §1.1 defect 7). A sixth, seventh, and eighth surfaced on Builder pre-flight pass 3 as iteration-7 / iteration-8 propagation residuals (per §1.1 defect 8). A ninth surfaced at step 8 execution time (post-pre-flight): spec deliverable 5 asserted a non-existent README "PMN file table" (per §1.1 defect 9).

### §7.2. Discipline statement

Architect-asserted facts about repository state — tracked-file presence, filesystem paths, file content patterns, surrounding-context preservation requirements — must be verified against actual repository state via `git ls-files`, file inspection, and content `grep` before declaring spec convergence. Verification source-of-truth is the actual repository, not intermediate diagnostic reports, not assumed conventions, not inbound-handoff recapitulation, not Architect's recall of prior cycle state.

### §7.3. Sub-shapes

- **(i.1) Tracked-file presence** assertions verified against `git ls-files <path>` (defect surfacing 1).
- **(i.2) Filesystem path assertions** verified against repo-root inspection or `git ls-files <pattern>` (defect surfacings 2 and 5).
- **(i.3) Content-pattern assertions** (assumed text in target file) verified against actual file content via `grep` or direct read (defect surfacings 3, 4, and 9). Verification timing: distributed across cycle execution, not concentrated at session start — defect 9 surfaced at step 8 execution time when Builder went to perform the asserted update, not at pre-flight when the assertion was read. Builder pre-flight should run a `grep` against any spec-asserted target-document content pattern at session start, but the discipline as currently practiced concentrates pre-flight verification on existence (i.1) and path (i.2) checks; content-pattern (i.3) verification at session start is a refinement candidate for the (i) discipline canonical placement.
- **(i.4) Surrounding-context-preservation assertions** verified against actual surrounding text in target file (defect surfacing 4 — author filter context). Also covers within-spec recapitulation-consistency between locally-fixed §-section and global summary/intro surfaces (defect 8 residuals 1-3).

### §7.4. Distinction from (g) and (h)

- (g) verification-artifact internal consistency: claim block agrees with itself (verification command, declared timing, example output, surrounding prose all coherent).
- (h) verification-command operational correctness: command's output domain proves what's claimed.
- (i) cross-document state verification: Architect's assertions about external (cross-document) repository state match actual repository state.

(g) and (h) operate within a single artifact; (i) operates across artifacts (spec asserting facts about other repository content). All three are independent — a claim block can pass (g) and (h) and still fail (i) if the spec's assertion about target-file content is wrong; the §4.1 substitution defect (defect 6) is exactly this case.

### §7.5. Two-surface mitigation discipline

§23.6 self-review extended to require cross-document state verification before convergence-declaration. For each Architect assertion about the form / content / path of a target file (e.g., "core.md §8.1.1.1 contains pattern X"), Architect runs the actual verification command and confirms the assertion against output. The (i) sweep is a fixed-point pre-condition: cannot declare §23.6 convergence without it.

**Empirical caveat**: false-positive convergence at iteration 5 means the (i) discipline cannot be fully self-applied. Architect-side (i) sweep catches some assertions but Architect's blindspots on its own assertions persist. Builder pre-flight is the structurally necessary second review surface for (i). Empirically-grounded structural claim: **(i) sweep is at minimum two-surface — Architect-side sweep at §23.6 self-review, then Builder-side pre-flight verification at spec §5 step 1, treated as cumulative not redundant**.

### §7.6. Iterative-pre-flight pattern (preliminary refinement)

PMN-006-cycle empirical: Builder pre-flight is itself iterative. Defect 7 (§5 step 2 reservation-mechanism error) was surfaced by Builder's SECOND pre-flight pass after spec revision absorbing defects 1-4 + defect 6 from pass 1. Defect 8 (three iteration-7 / iteration-8 propagation residuals) was surfaced by Builder's THIRD pre-flight pass after iteration-7 (i)-cluster adoption + iteration-8 (§5 step 2 rewrite).

**Pattern**: each iteration in response to Builder pre-flight findings introduces new assertions about repository state that themselves require verification. Single-pass Builder pre-flight is insufficient when spec revisions absorb prior-pass findings.

**Recommended canonical refinement at sufficient evidence accumulation**: (i) sweep is iterative across Builder pre-flight passes; convergence requires Builder-side fixed-point (no new assertions surfacing on a clean-pass iteration), in addition to the two-surface Architect-vs-Builder cumulation. Recorded as preliminary observation; ~2-3 more cycles needed before promotion to canonical refinement.

**Bounded-continuation as stop condition**: applying the bounded-continuation rule (§5.3 above, generalized cross-surface) provides the structural stop condition for spec-revision iterations triggered by pre-flight findings. Iteration 8 was the path-(a) revision for cross-document state verification residuals; defect 8 is the path-(b) record-and-proceed material — same-class residuals routed to PMN evidence rather than iteration-9 fix-up. Without the bounded-continuation rule, the iterative-pre-flight pattern has no convergence guarantee in finite spec-revision iterations.

### §7.7. Canonical effects

- (i) added to the standing PMN sweep set as new top-level discipline, alongside (g) and (h) introduced this PMN.
- §23.6 self-review checklist gains (i) sweep as fixed-point pre-condition.
- Builder pre-flight (spec §5 step 1) gains explicit (i) verification step (already present implicitly in this cycle; canonicalize for future cycles).

### §7.8. Single-data-point caveat

1 cycle's empirical evidence (this cycle's TASK-0011 spec). 9 distinct sub-defect surfacings within that single cycle (4 pre-flight pass-1 + 1 pre-flight pass-2 + 3 pre-flight pass-3 residuals + 1 step-8-execution-time defect 9). Above the typical 1-cycle/1-data-point threshold for single-cycle observation but below the ~3-cycle threshold for canonical-refinement promotion. (i) is canonicalized at PMN-006 because the discipline addition is small and the cycle introducing (g)/(h) is the right context for grouping; future cycles refine sub-shape taxonomy if additional sub-defect classes surface. The defect-9 surfacing-at-step-8-execution-time data point is a refinement candidate to the (i) discipline canonical-placement: (i.3) content-pattern verification timing should be distributed across cycle execution rather than concentrated at session-start pre-flight.

## §8. Refined disciplines summary

PMN-006 introduces three new top-level disciplines and refines two existing ones; inherits the rest by reference.

**New discipline 1 — (g) Verification-artifact internal consistency** (§3.1 above). Sub-shapes (g.1) timing-correctness across surfaces; (g.2) within-claim-block label-vs-example consistency.

**New discipline 2 — (h) Verification-command operational correctness** (§3.2 above). Sub-shapes (h.1) pagination; (h.2) command-achieves-claimed-verification; (h.3) filter-boundary completeness.

**New discipline 3 — (i) Cross-document state verification** (§7 above). Sub-shapes (i.1) tracked-file presence; (i.2) filesystem path assertions; (i.3) content-pattern assertions; (i.4) surrounding-context-preservation assertions including within-spec recapitulation-consistency.

**Refinement 1 — PMN-003 (a) refined recapitulation-consistency re-check, extended with frontmatter-vs-body sub-clause** (§3.4 above). Re-check now extends to: PMN body vs verification prompts within the same cycle (existing); multiple artifacts after path-(a) revision (existing); verification-command surfaces (PMN-004 §2.3); frontmatter vs body when body content is filled (NEW).

**Refinement 2 — Bounded-continuation rule generalized cross-surface** (§5.3 above). Originally articulated at Reviewer post-PR review surface; PMN-006 generalizes to Architect-side spec-revision surface in response to Builder pre-flight findings. (d) sub-observation: rule generalizes across iteration-pair surfaces, not Reviewer-specific. Preliminary at 2 cycles of cross-surface evidence; ~2-3 more cross-surface applications needed before canonicalization.

Inherited disciplines (standing per PMN-004 §5 + PMN-005 §4.4):

- **(a) Severity taxonomy three-level enumeration** — Blocking / Major / Minor with explicit definitions; no two-level framing acceptable.
- **(b) Verification-command portability** — bash, Windows cmd, or PowerShell forms supplied; single-shell-only commands without explicit qualifier are defects.
- **(c) No future-tense claims at pre-commit time** — every Builder claim's verification command must produce verifiable output at pre-commit time against the working tree.
- **(d) Pre-commit cross-surface scope clarity** — count claims and consistency checks enumerate only the pre-commit-existing surfaces.
- **(e) §23.6 prose-arithmetic decomposition** — every prose-arithmetic claim is decomposed into operands and a relationship; verified at §23.6 self-review and at step-10 self-verification.
  - **(e.1) Cumulative-diff-stats re-derivation after path-(a) revisions** (PMN-005 sub-rule).
- **(f) Section-citation correctness sweep** — every `§N` citation refers to a section that exists in the cited document at the cited number; sweep applied iteratively to convergence.

Defects identified by PMN-006 that the existing disciplines did not catch (per §1.1 honesty record):

- The verification-artifact-validity class (g)/(h) operates on a surface (verification command output domain + within-block consistency) that PMN-004 §5 (a)-(f) + PMN-005 sub-rule (e.1) did not explicitly include; PMN-006 adds (g) and (h) as new top-level disciplines.
- The cross-document state verification class (i) operates on a surface (Architect-asserted facts about cross-document repository state) that no prior discipline included; PMN-006 adds (i) as a new top-level discipline.
- The bounded-continuation rule originally articulated at the Reviewer post-PR review surface generalizes cross-surface; PMN-006 records the generalization with preliminary 2-cycle empirical grounding.

## §9. Anticipated forward integration + cross-references

### §9.1. Forward integration

**TASK-0011 (this PR-11 cycle)** materializes the (g) / (h) / (i) discipline split + bounded-continuation rule generalization in PMN-006 substantive content + applies (g) / (h) at PR-11 review-context authoring + applies (i) at Builder pre-flight on the TASK-0011 spec itself (recursive-self-instantiation of (i) discipline that drove its canonicalization).

**TASK-0012 spec (next, core.md Part B authoring)** carries forward all PMN-006 disciplines plus inherited PMN-004 §5 (a)-(f) + PMN-005 sub-rule (e.1). Specifically:

- (g) / (h) / (i) sweep applied at Architect §23.6 self-review and Builder pre-flight.
- Bounded-continuation rule (§5.3 generalized) applied at adjudication time for Reviewer post-PR review and spec-revision iteration both.
- M-A7 §-section text canonicalized in core.md (placement between §17 cycle-close and §18 trigger discipline per §6.2 above).
- Bounded-continuation rule §-section text canonicalized in core.md (sub-rule under §8.1.1.x cluster per §5.5 above).

**Future PMN/ADR cycles** apply PMN-006's three new disciplines + two refinements globally. PMN-007+ and ADR-004+ inherit the disciplines as standing.

### §9.2. Monitoring items

**Monitoring item M-A6**: PMN-rate-vs-budget tracking. Pre-PMN-006-merge rate (post-PR-10-merge state): 5 PMNs in 10 merged cycles (PR-1 through PR-10) = 50%. Post-PMN-006-merge: 6 PMNs in 11 merged cycles (PR-1 through PR-11) = 55%. ADR-003 Decision 3 forecast range: 3-7 PMNs across 13 substantive cycles = 23% to 54% rate. The post-PMN-006-merge rate (55%) exceeds the forecast upper bound (54%) by 1 percentage point. The exceedance does not trigger M-A6 promotion (trigger remains at TASK-0023, four contingency slots remaining: TASK-0023 through TASK-0026). The 1-pp exceedance is noted as a monitoring continuity item; surfaced as evidence at TASK-0023 evaluation point.

The decomposition is explicit per (e):
- Pre-PMN-006-merge: 5 PMNs (PMN-001 through PMN-005) in 10 merged cycles (PR-1 through PR-10); 5/10 = 0.50 = 50%.
- Post-PMN-006-merge: 6 PMNs (PMN-001 through PMN-006) in 11 merged cycles (PR-1 through PR-11); 6/11 = 0.5454... ≈ 55% (rounded to nearest percentage point).
- Forecast upper bound: 7 PMNs across 13 substantive cycles; 7/13 = 0.5384... ≈ 54% (rounded to nearest percentage point).
- Exceedance: 55% − 54% = 1 percentage point.

**Monitoring item M-A7**: merge-commit-body data integration pattern. Pre-PMN-006: candidate (per PMN-005 §6 / §7 inferences). Post-PMN-006: operationally canonical pending §-section text in core.md (per §6.2 above). Trigger: §-section text canonicalized in core.md Part B (TASK-0012). Resolution: Part B merge.

**Monitoring item M-A8 (potential)**: substantive-content-cycle scope step-up driving PMN-cadence step-up. Pre-PMN-006: not introduced (single data point). Post-PMN-006: not introduced (still single data point per §1.2 above). Promotion threshold: 2-3 cycles of cross-data confirmation; reconciliation at TASK-0023.

### §9.3. Cross-references

- **ADR-001** decisions 1-7, 9-15 unchanged; decision 8 PR sequence portion superseded by ADR-002, then by ADR-003 Decision 3.
- **ADR-002** Decision 3 anticipation pattern absorbed and extended by ADR-003 Decision 3; PMN-006 inserts under ADR-003 Decision 3 contingency budget.
- **ADR-003** Decision 2 (12 substantive content PR plan, anticipated PR-8 through PR-19 in original numbering, shifted to PR-9 through PR-20 post-PMN-004, shifted to PR-10 through PR-21 post-PMN-005, shifted to PR-11 through PR-22 post-PMN-006); Decision 3 (TASK reservation through TASK-0026; PMN-006 consumes a third contingency slot; four remaining: TASK-0023 through TASK-0026); §Consequences (per-PR-row-update discipline for README and stub frontmatter; package-layout drift for usage-guide.md row stays forecast-form per ADR-003 design until usage-guide actually ships).
- **PMN-001** (h.2) file-based Builder direction; (k) Linked PR fix-up substitution.
- **PMN-002** (a) refined imperative `Action:` phrasing; (d) code-fenced thin pointer prompt.
- **PMN-003** (a) refined recapitulation-consistency re-check (extended in PMN-004 §2.3 to include verification-command surfaces; extended in PMN-006 §3.4 with frontmatter-vs-body sub-clause); (e) refined two-endpoint review polling; (g) four-point Architect-side post-handback verification (extended in PMN-005 §2.5 to a five-point pattern); (j) and (m) receiving-surface format declaration.
- **PMN-004** §2 claim-text drift defect class characterization; §2.3 recapitulation-consistency re-check extension to verification-command surfaces; §4 two-endpoint discipline empirical confirmation; §5 six refined disciplines (a)-(f); §1 4-iteration self-review empirical pattern.
- **PMN-005** §2 reviewer-claimed-effects-don't-land defect class; §3 pass-shape correlation hypothesis (preliminary); §4.4 sub-rule (e.1) cumulative-diff-stats re-derivation.
- **PR-10 (TASK-0010)** the cycle whose learnings PMN-006 captures; squash-merge `80f5a4a` 2026-05-02T17:19:51-04:00.
- **PR-11 (TASK-0011 / this PR)** the cycle in which PMN-006 + core.md §8.1.1.1 / §24.3.1 surgical corrections land.
- **TASK-0012 (next, anticipated)** core.md Part B authoring; M-A7 §-section text canonicalization; bounded-continuation rule §-section text canonicalization.
- **AMAS v2.14.1 §8.1.1.1** Reviewer dual-signal output handling — pass-shape Reviewer-specificity hypothesis is a §8.1.1.1 application surface; bounded-continuation rule §-section text candidate placement.
- **AMAS v2.14.1 §8.1.1.2** Reviewer claimed-action verification — extends PMN-005 §2 reviewer-claimed-effects-don't-land defect class.
- **AMAS v2.14.1 §18** post-merge note canonical form — PMN-006 follows it.
- **AMAS v2.14.1 §23.6** Architect pre-handoff self-review — (g) / (h) / (i) discipline split extends §23.6 sweep scope.
- **AMAS v2.14.1 §24.2(a)** external-system-behavior assertion sub-shape.
- **AMAS v2.14.1 §24.2(b)** artifact-content assertion sub-shape — defect 4 (.gitkeep inversion) and defects 6/7/8 (cross-document state verification residuals) are §24.2(b) instances.
- **AMAS v2.14.1 §24.3** receiving-side caveat-discipline — Architect receiving Builder pre-flight findings during spec authoring; bounded-continuation rule generalization extends the §24.3 surface set.
- **core.md (HEAD post-PR-11)** §8.1.1.1 polling-commands corrected per (h.3) symmetric application; §24.3.1 point 2 corrected per (h.2). status remains `partial` until Part B (TASK-0012) lands.
