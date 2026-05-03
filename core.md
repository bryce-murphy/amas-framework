---
framework_version: 3.0.0
status: partial
filled_by: PR-10 (TASK-0010) Part A — verify-before-assert cluster (§8.1.1, §23.6, §24.3); Part B in TASK-0011+
---

# AMAS v3 Core

*Part A canonical content authored in PR-10 (TASK-0010) per ADR-003. Remainder pending Part B (TASK-0011 onward).*

## §8. Builder receiving Reviewer findings

This section governs the Builder's receiving-side discipline when absorbing Reviewer output during a cycle. The discipline is bidirectionally symmetric to §8.2 (Builder pre-flight against Architect prompt assertions) and §8.3 (owner receiving Builder stop-and-show): each is a §24.3 receiving-side caveat-discipline application at a distinct surface in the cycle's communication topology. Subsections cover Reviewer-output absorption (§8.1) and downstream Builder verification of Reviewer claims against repository state (§8.1.1.2).

### §8.1. Reviewer-output absorption

The Reviewer's verdict is delivered to the Builder via the GitHub API surface as one or both of: a formal Pull Request Review object and a top-level issue-comment summary. The two channels carry distinct content shapes and are not interchangeable: the formal Pull Request Review carries line-anchored findings when they exist; the issue-comment summary carries the verdict text. Subsection §8.1.1 specifies the dual-channel polling discipline that the Builder applies at every Reviewer-output absorption point in a cycle.

#### §8.1.1. Reviewer-output channel handling

Two leaf disciplines apply at Reviewer-output absorption: dual-signal output handling (§8.1.1.1) covering the two delivery channels and their reconciliation, and claimed-action verification (§8.1.1.2) covering the receiving-side verification of any reviewer-claimed action against actual repository state.

##### §8.1.1.1. Reviewer dual-signal output handling

When a Reviewer is invoked on a Pull Request, the review-rendering surface emits the Reviewer's output through two distinct GitHub API endpoints with distinct content shapes. The Builder absorbing Reviewer output cannot rely on single-channel polling.

The two endpoints are:

(a) **Formal Pull Request Review** — accessed via `gh api repos/{owner}/{repo}/pulls/{pull_number}/reviews` or `gh pr view {pull_number} --json reviews`. Carries line-anchored substantive findings when they exist; populated by formal Pull Request Review API objects (e.g. those created via `POST /repos/{owner}/{repo}/pulls/{pull_number}/reviews`).

(b) **Issue-comment summary** — accessed via `gh api repos/{owner}/{repo}/issues/{issue_number}/comments` or `gh pr view {pull_number} --json comments`. Pull Requests are issues from the GitHub API perspective; the issue-comment endpoint receives top-level comments on the PR, including Reviewer-emitted summary verdicts.

Two pass shapes are empirically observed across cycles dogfooded in the AMAS framework production project:

- **Substantive-finding pass shape**: both endpoints emit. Formal Pull Request Review carries line-anchored findings; issue-comment summary carries verdict text restating the findings.
- **Cycle-trailing-clean-Approve pass shape**: only the issue-comment endpoint emits. Formal Pull Request Review emits no object; the issue-comment summary carries boilerplate-style verdict text (typical phrasing: "Codex Review: Didn't find any major issues.").

The empirical observation that cycle-trailing-clean-Approve emits to the issue-comment endpoint only is a preliminary hypothesis under continuing test; the Builder discipline below does not depend on the hypothesis being confirmed. Single-channel polling is structurally unreliable regardless of which pass shape is actually emitted, because the Builder cannot know in advance which shape the cycle will produce.

**Builder discipline.** At each Reviewer-output absorption point in a cycle, Builder polls both endpoints, filters by author and `created_at`/`submitted_at` against last-known-state, and reconciles before treating the absorption as complete:

```bash
# Endpoint (a) — formal Pull Request Review
gh api --paginate repos/{owner}/{repo}/pulls/{pull_number}/reviews \
    --jq '.[] | select(.user.login=="<reviewer>") | select(.submitted_at > "<last-known>" or (.submitted_at == "<last-known>" and .id > <last-seen-id>))'

# Endpoint (b) — issue-comment summary
gh api --paginate repos/{owner}/{repo}/issues/{issue_number}/comments \
    --jq '.[] | select(.user.login=="<reviewer>") | select(.created_at > "<last-known>" or (.created_at == "<last-known>" and .id > <last-seen-id>))'
```

The lexicographic `(timestamp > last-known) OR (timestamp == last-known AND id > last-seen-id)` form handles same-second emission tie-breaks symmetrically across both endpoints. The naive `>=` plus unconditional-id-gate form (`timestamp >= last-known AND id > last-seen-id`) is incorrect: it requires `id > last-seen-id` for ALL results regardless of timestamp, which drops valid new emissions whose timestamp exceeds the boundary but whose id is below the last-seen-id (possible when ids do not strictly track submitted_at/created_at — e.g., a long-drafted review id N1 submitted at t2 after a faster-drafted review id N2 > N1 submitted at t1). The correct form gates the id comparison only inside the same-timestamp tie clause; cross-timestamp emissions pass through the `timestamp > last-known` clause without id constraint. `<last-known>` is the timestamp of the most recently absorbed emission per endpoint; `<last-seen-id>` is that emission's `id`.

The `--paginate` flag is required: GitHub REST list endpoints return at most 30 items per page by default; on long-lived PRs (or repos where the Reviewer has emitted many objects) single-page polling produces false-negative "no emission" verdicts when newer Reviewer output lives on a subsequent page. `gh api --paginate` retrieves all pages and concatenates results before jq filtering.

Both polls run; results from both are reconciled. A clean-Approve cycle-trailing pass shows no review object and a fresh issue-comment with boilerplate verdict. A substantive-finding pass shows fresh review object(s) with line-level findings and a fresh issue-comment with verdict text. A no-emission state on both endpoints means the Reviewer has not yet emitted; Builder waits and retries per the project's polling cadence.

**Anti-channel.** Issue-level comments authored by the Reviewer outside the polled-comment shape — for example, a top-level comment that is a clarification request or a process question rather than a verdict — are non-authoritative for substantive verdict regardless of phrasing. Builder treats such comments as informational; verdict status is determined by the formal-review-or-summary pair only.

**Cross-reference.** §8.1.1.1 is a §24.2(a) external-system-behavior assertion application at the Reviewer-output-absorption surface. The verify-before-assert mechanism is the §24 cross-surface meta-pattern applied at this specific receiving direction.

##### §8.1.1.2. Reviewer claimed-action verification

When a Reviewer comment claims an action — that a commit was created, a file was added, a follow-up artifact exists, or a referenced identifier is valid — the comment may be delivered (the two-endpoint poll of §8.1.1.1 establishes delivery) but the claimed action may not correspond to actionable repository state. Delivery and effect are separate verifications.

Two empirically-observed sub-shapes of the reviewer-claimed-effects-don't-land defect class:

**Sub-shape A — entirely-fabricated claim.** Reviewer comment asserts a write action (commit + file pair, follow-up commit, or similar) that was not performed. The cited commit SHA does not resolve; the cited file path does not exist at the cited commit (or anywhere on the repository). Detection surfaces:

- `gh api repos/{owner}/{repo}/commits/<sha>` returns 422 (Unprocessable Entity)
- `gh api repos/{owner}/{repo}/contents/<path>?ref=<sha>` returns 404 (Not Found)

If both surfaces fail, the claim is fabricated. Risk if untreated: Builder or Architect treats the claim as authoritative and adjudicates against repository state that does not exist.

**Sub-shape B — correct-content-fabricated-citation.** Reviewer comment asserts a finding with substantively correct content (e.g., correct numeric counts, correct file references, correct recommended action) but cites an unreachable commit SHA as cross-reference. The substantive content is independently verifiable from the comment text alone; the citation is the only fabricated element. Detection surfaces:

- `gh api repos/{owner}/{repo}/commits/<sha>` returns 422
- Substantive content claims verified against repo state directly (independent of cited SHA) succeed

If the SHA fails but the substantive content holds, the comment is sub-shape B.

**Builder discipline.** When a Reviewer comment asserts any of the following claim categories, Builder verifies the claim against actual repository state via `gh api` calls before treating the claim as effective:

- **Commit existence claim** — a commit SHA cited as authoritative reference (e.g., "I pushed commit abc1234 fixing X")
- **File existence or content claim** — a file path plus content cited (e.g., "I added `docs/foo.md` with the corrected text")
- **Follow-up artifact existence claim** — a follow-up issue or PR cited as filed (e.g., "filed follow-up issue #N")
- **Identifier-pattern compliance claim** — an identifier cited as conforming to a pattern (e.g., a SHA shape, a branch name pattern)

Verification commands by claim category:

```bash
# Commit existence claim
gh api repos/{owner}/{repo}/commits/<sha>

# File existence at a specific commit
gh api repos/{owner}/{repo}/contents/<path>?ref=<sha>

# File existence on a branch
gh api repos/{owner}/{repo}/contents/<path>?ref=<branch>

# Follow-up issue or PR existence
gh api repos/{owner}/{repo}/issues/<n>
gh api repos/{owner}/{repo}/pulls/<n>
```

**Adjudication discipline.** The two sub-shapes adjudicate differently:

- **Sub-shape A**: comment is informational-only. No action is attributed to the phantom artifacts. Builder records that the claim was made but did not land; subsequent cycle decisions do not depend on the claimed action having occurred.
- **Sub-shape B**: comment's substantive content is path-(a) adjudicated on its own merits, subject to standard receiver-side review of the content. The phantom citation is noted as informational; downstream cross-references using the cited SHA are skipped or flagged.

The load-bearing element is separating the substantive review evidence from phantom-affected delivery. A finding with correct content and a fabricated citation is still a real finding; the citation defect is informational, not invalidating. A finding with fabricated content and a fabricated citation is fully informational.

**Cross-reference.** §8.1.1.2 is a §24.2(a) external-system-behavior assertion application — Reviewer comments that claim repository state are external-system-behavior assertions, and the verification discipline is the §24 cross-surface meta-pattern applied at the Reviewer-output-absorption surface. Together with §8.1.1.1 (delivery), §8.1.1.2 (effect) covers the two distinct verifications required at this surface.

##### §8.1.1.3. Bounded-continuation rule for iterative review-finding adjudication

When iterative review processes (Reviewer post-PR review, Builder pre-flight, Architect pre-handoff self-review) surface findings across multiple successive passes, the bounded-continuation rule governs same-class subsequent-finding adjudication. The rule prevents review-cycle non-termination on recurrent same-class findings while preserving correctness on first-finding-in-class.

**Rule statement.**

- **First finding in a class** → path-(a) revise. Apply the canonical correction; iterate the review.
- **Subsequent same-class finding** → path-(β) record-and-proceed. Acknowledge the finding; record evidence in cycle artifacts (handoff Validation run, PMN evidence, merge-commit-body); proceed without further iteration on the recurrent class.
- **Carry to PMN** if substantive. If the class is a candidate framework-discipline refinement, the recurrence is PMN-eligible content per §18.1 (e) unexpected review friction.

**Class definition.** A "class" is a defect family — same sub-shape under §23.6.1 sweep set categories (e.g., (g.1) timing-correctness, (h.3) filter-boundary, (i.4) recapitulation-consistency). Two findings sharing the same sub-shape are same-class; findings in different sub-shapes are distinct classes regardless of surface similarity.

**Cross-surface application.** The rule applies at multiple iteration-pair surfaces:

- Reviewer post-PR review surface — Reviewer surfaces findings across review passes; Builder applies bounded-continuation at fix-up commit adjudication.
- Builder pre-flight surface — Builder surfaces spec defects across pre-flight passes; Architect applies bounded-continuation at spec revision adjudication.
- Architect pre-handoff self-review surface — §23.6 4-iteration-to-fixed-point self-review; bounded-continuation governs path-(β) routing of subsequent same-class self-review iterations beyond convergence.

The cross-surface generalization is empirically grounded in two cycles (PR-10 Reviewer surface; PR-11 spec-revision surface) per PMN-006 §5.3. Future cycles that surface bounded-continuation at additional surfaces extend the application set without changing the rule.

**Bounded-iteration family.** The bounded-continuation rule is a member of the bounded-iteration discipline family, which also includes:

- §23.6.2 4-iteration-to-fixed-point self-review (PMN-004 §1 empirical grounding). Architect-side iteration cap.
- §23.6.1 sub-rule (e.1) cumulative-diff-stats re-derivation (PMN-005 §4.4). Iteration trigger on path-(a) revisions affecting diff stats.
- §8.1.1.3 bounded-continuation rule (this section). Iteration termination on same-class recurrence.

Family members compose: bounded-continuation governs path-(a) vs path-(β) routing; (e.1) re-derives cumulative-diff-stats after path-(a) revisions; §23.6.2 caps self-review iterations independent of routing decisions.

**Recording guidance.** Path-(β) record-and-proceed events are recorded in cycle artifacts per the surface where the rule was applied: review-context Adjudication / fix-up section for Reviewer surface; handoff Risks or Validation run section for Builder pre-flight surface; spec defect log for Architect self-review surface. The recording surface preserves evidence for PMN promotion decisions at cycle close per §18.1 (e) unexpected review friction trigger evaluation.

**Cost-class refinement.** Path-(β) routing presupposes that subsequent same-class findings are not load-bearing — they are noise around the canonical correction the first-finding path-(a) revise already applied. When subsequent same-class findings ARE load-bearing (e.g., the class instance affects future-cycle correctness in a non-cosmetic way), the rule routes to path-(a) regardless of repetition count. Cost-class refinement is preliminary at single-data-point empirical evidence (PR-11 cycle Codex post-PR pass 4 hybrid adjudication: line 102 load-bearing → path-(a); line 106 cosmetic → path-(β)) and is recorded in PMN-007 candidate observation register as preliminary; canonicalization deferred to ~2-3 more cycles of cost-class adjudication evidence.

**Cost-class sub-distinction — genuinely-asymptotic vs pure-token-swap cascades**: when applying the cost-class refinement to determine path-(a) revise vs path-(β) record-and-proceed routing, distinguish (i) genuinely-asymptotic recursion boundaries — structural changes that shift downstream surface line counts, where each iteration's correction introduces new propagation surfaces requiring further iteration; bounded-iteration acceptance is appropriate at the asymptote — from (ii) pure-token-swap cascades — single-iteration convergence at a stable fixed-point where text values match git stat in one iteration without introducing new propagation surfaces. Pure-token-swap cascades terminate at one-iteration fixed-point and always route path-(a); only structural-shift cascades (genuinely-asymptotic class) warrant bounded-iteration acceptance via path-(β). The distinction is empirically grounded by PMN-007 §2 (PR-13 cycle iteration-5 (e.1) cascade routed path-(β) under preliminary cost-class refinement at canonicalizing cycle; Codex post-PR pass 1 surfaced the routing as load-bearing failure case — durable repo surfaces inconsistent across three numbers; cascade was avoidable, not asymptotic).

## §17. Templates

This section houses the canonical template forms for project artifacts. Each template specifies required structure, required fields, and authoring surface for an artifact class. Template leaves canonicalize incrementally across the v3.0 substantive-content authoring sequence; this cycle establishes the parent frame, with leaf canonicalization (ADR template, PR template, Review summary template, CLAUDE.md template, AGENTS.md template, project-instruction-files template) deferred to subsequent template-batch cycles per ADR-003 Decision 2 (PR-15 / PR-16).

Templates are mechanism, not policy. The discipline that templates encode (handoff schema at §14.1, review schema at §8.1.1, post-merge note schema at §18.2) is canonicalized in the §-section that defines the discipline. The template form at §17 is the artifact-construction surface that pairs with the discipline.

## §18. Post-merge note discipline

Post-merge notes (PMNs) are durable artifacts capturing learnings from merged PRs that warrant cross-cycle preservation. The PMN convention separates from in-cycle artifacts (handoff at §14.1, review-context at §8.1.1, AI Session Log at §13) by spanning across cycles: a PMN authored at cycle N captures observations from cycle N's merged PR(s) that future cycles N+1 through cycle close apply as standing discipline.

§18 organizes into four leaves. §18.1 names the trigger criteria that determine when a merged PR warrants a PMN. §18.2 specifies the PMN artifact form (directory, naming, required sections, authoring surface). §18.3 covers the merge-commit-body data integration pattern that captures cycle-close-window content adjacent to the PMN itself. §18.4 names the framework version-bump trigger criteria, structurally parallel to §18.1's PMN-trigger criteria but applied to the framework's own canonical-document version sequence.

The §18 leaves co-evolve: PMN content drives observation accumulation, merge-commit-body integration captures post-PR-window observations the PMN does not yet absorb, version-bump trigger criteria adjudicate when accumulated canonical changes constitute a bumpable feature event. Together they form the cycle-close discipline cluster.

### §18.1. Trigger basis — PMN trigger criteria

A post-merge note is required, not optional, when the merged PR involved any of the five trigger categories below. For trivial changes — typo fixes, dependency bumps with no behavior change, documentation-only PRs that don't surface review friction — a PMN remains optional.

**(a) Architecture change.** The PR modified durable system shape in a way that affected or motivated an ADR — new ADR, superseded ADR, or an existing ADR's area touched substantively. Architecture changes warrant cycle-summary preservation because their downstream effects propagate across multiple subsequent cycles; the PMN captures the rationale for the change at the moment it lands rather than reconstructing rationale from a future ADR's text alone.

**(b) Workflow change.** The PR changed how the Builder/Reviewer loop operates on this repo — new required status check, new branch-protection rule, new review-escalation trigger, new handoff pattern, new pre-flight discipline, new self-review sweep set member. Workflow changes warrant preservation because the discipline drift between intended workflow and actual practice is empirically high; the PMN records the discipline as canonical at landing.

**(c) Tool-assignment change.** The PR reflects a role reassignment under §2.3.4 (or equivalent project-specific assignment table), or a change in which surface performs a role, or a change in the Reviewer mode per §8.1. Tool-assignment changes warrant preservation because the project's assignment table is the authoritative reference for "who does what" and changes to that reference inform downstream cycle planning.

**(d) Validation-strategy change.** The PR added, removed, or materially changed the validation commands — new test framework, removed test suite, new CI check, retired CI check, new manual-validation requirement, new verification command portability requirement. Validation-strategy changes warrant preservation because validation discipline is the operational layer between Builder claims and merged state; changes there inform Builder/Reviewer engagement patterns going forward.

**(e) Unexpected review friction.** The review process itself produced surprises worth recording — a finding no one anticipated, a class of defect the Reviewer caught that suggests a gap in Builder discipline, a handoff that didn't carry enough context, a bypass that felt wrong even though it was supported, a Reviewer claimed-action verification surfacing a phantom-action class not previously named. Friction-driven PMNs are the highest-leverage trigger because they surface latent defect classes before they recur.

**Trigger overlap.** Multiple categories may apply to a single PR. Naming all applicable categories with a one-sentence justification per category is the canonical form; partial coverage of multi-category triggers risks understating the cycle's substantive change footprint.

**Trigger threshold.** The trigger criteria above name necessary conditions for required PMN authorship. Optional PMNs (cycles that don't hit any of the five categories but still produced learning the next reader of the project would benefit from) remain owner-adjudicated. The default for owner-adjudicated optional cases is "author the PMN" — under-documenting cycle learnings is a structural drift the framework optimizes against; over-documenting is a ceremony cost the framework absorbs.

### §18.2. PMN artifact form spec

The PMN artifact form is canonical, not advisory. The framework already specifies form for analogous durable artifacts — handoffs at §14.1, ADRs at §7.1, templates at §17 — because specifying a discipline without specifying a form produces a discipline-erosion failure mode where the rule survives across cycles but the content does not. PMNs are repo-tracked artifacts under version control; the form below is the canonical structure.

**Directory.** `docs/post-merge-notes/`. PMNs are version-controlled alongside other durable repository artifacts.

**Naming.** `PMN-####-<slug>.md` with sequential numbering starting at 001, scoped per-project. The slug is short and descriptive (e.g., `pr-10-cycle-learnings`). The PMN-#### identifier is independent of TASK-#### identifiers — a single PMN may cover one PR or multiple related PRs depending on the trigger pattern. PMN numbering is independent of merge order; PMNs land in the order they are authored, not the order their source PRs merged.

**Required sections.** A minimal PMN template includes the four sections below. Additional sections (cycle context with honesty record, observation clusters, refined disciplines summary, anticipated forward integration, monitoring items, cross-references) are project-specific extensions that appear when the PMN's substantive content warrants them; the four required sections are the load-bearing minimum.

- **Trigger basis** — which of §18.1's five trigger categories apply (architecture / workflow / tool-assignment / validation-strategy / unexpected-review-friction), with a one-sentence justification for each named trigger. Multiple triggers may apply.
- **Observations** — the durable lessons from the merged PR(s). What surprised, what worked, what would be done differently next time. Observations are framed for cross-cycle reference, not narrative recall.
- **Action items** — concrete follow-up actions with named owners. May be empty if the observations are documentation-only. Each action item names an owner surface and a target cycle for action absorption.
- **Provenance** — source PR(s), source TASK(s), date authored, author surface (Architect / Reviewer per the §18.1 (a)-(e) authoring assignment).

**Authoring surface.** The Architect or the Reviewer authors the post-merge note. The Builder is not the lead role for PMN authorship — the Builder's role is implementation, and post-merge learning is reflective work that belongs at the Architect or Reviewer surface. The Builder may surface observation candidates at hand-back; the Architect adjudicates which observations promote to PMN content and authors the PMN.

**Mid-life PMN-convention adoption.** When a project adopts post-merge-note discipline mid-life — that is, after the project has merged PRs that would have been §18.1-eligible — the first PMN authored under the convention should explicitly address retroactive-backfill considerations for prior eligible PRs. The project owner decides whether to author retrospective post-merge notes based on whether the originating sessions' content is still recoverable; the framework does not mandate retrospective backfill. The first PMN names the prior eligible PRs, the recoverability assessment for each, and the backfill decision (author retrospective PMNs, accept the gap with explicit acknowledgment, or some hybrid).

**Scope-per-PMN.** A single PMN may cover one PR or multiple related PRs. Multi-PR PMNs are appropriate when observations cluster naturally (e.g., PMN-001 covered PR-1 + PR-2 production learnings under joint coverage; PMN-003 covered PR-3 + PR-4 + PR-5 review-discipline refinements). Single-PR PMNs are appropriate when observations are PR-specific. The grouping decision is owner-adjudicated at PMN authoring time; the form spec accommodates both.

### §18.3. Merge-commit-body data integration

Between PR-open and squash-merge, post-PR-window content accumulates that is relevant to the cycle's durable record but does not warrant a fix-up commit on the feature branch. This includes Reviewer-engagement absorption summaries (review-pass count, findings disposition, fix-up commits absorbed), late-cycle observations spotted at cycle close that are too small for PMN scope, finalized cycle-summary observations the Architect surfaces post-handoff, and self-referential entries naming pattern-promotion events that the cycle itself instantiated. The merge-commit-body — the body content of the squash-merge commit that closes the cycle — is the canonical surface for capturing this content.

**Pattern statement.** The merge-commit-body integrates post-PR-window content the feature-branch commits do not capture. The Architect updates the merge-commit-body with this content before owner-squash-merges; owner reviews the body content as part of the squash-merge action. After merge, the body content is durably preserved on `main`'s commit history.

**Content classes.** Four content classes empirically integrate at this surface:

- **(a) Reviewer-engagement absorption summary** — count and disposition of Reviewer review passes (pre-commit Codex, post-PR Codex), findings severity histogram, fix-up commits absorbed, threads addressed/replied/resolved per §8.1.1 rule (b)/(c) discipline.
- **(b) Late-cycle small observations** — observations spotted at cycle close that don't warrant PMN promotion (single-data-point preliminary, sub-shape refinement candidates, cycle-specific noise) but the next reader of the project would benefit from knowing happened.
- **(c) Cycle-summary observations** — Architect-surfaced post-handoff observations that wouldn't fit in the handoff's structured form. Hand-back format constrains content to in-cycle Builder-perspective; the Architect's cycle-summary observations live alongside the Builder hand-back, not within it.
- **(d) Self-referential pattern-promotion entries** — when the cycle itself instantiates a pattern the cycle is canonicalizing (recursive self-instantiation), the merge body explicitly names the instantiation as evidence: "M-A7 promotion trigger met (second instance of the merge-commit-body data integration pattern this cycle)" — the strongest possible empirical confirmation of pattern presence is the pattern self-naming at the cycle that promotes it.

**Discipline.** The Architect authors the merge-commit-body update post-handoff, before owner squash-merges. Content classes (a) through (d) are integrated as a cycle-close addendum; the body's structure is at Architect discretion (no template is canonical at this surface — the content varies cycle-to-cycle by what actually accumulated). Owner reviews the body content as part of the squash-merge action; if owner disagrees with content, owner edits before squash.

**Cross-reference: §13.1 / §13.2 distinction.** The merge-commit-body data integration pattern is structurally distinct from the AI Session Log storage rule at §13.1 (most recent log in PR body, prior logs migrate to handoff `## Session log archive`). §13.1 governs in-cycle Builder-perspective session records; §18.3 governs post-handoff Architect-perspective cycle-close content. Both surfaces preserve durable content but at different abstraction layers — §13.1 captures session-grain reasoning, §18.3 captures cycle-grain observations.

**Cross-reference: §18.2 PMN form spec.** Content class (a) Reviewer-engagement absorption summary may be substantively rich enough to warrant PMN content rather than merge-commit-body content. The threshold is the §18.1 trigger criteria: if absorption surfaces a recurrent defect class, novel sub-shape, or workflow change, the absorption belongs in a PMN with cross-reference to the merge-commit-body summary. If absorption is descriptive cycle history without learning content, the merge-commit-body is sufficient.

**Recording guidance.** A single instance of the pattern (one cycle integrating post-PR-window content into merge-commit-body) is normal cycle close, not a §18.1 trigger event. Recurring instances, instances where the integration surfaces novel content classes, or instances where pattern absence (a cycle that doesn't integrate when it could have) drives downstream cycle defects are §18.1 trigger candidates under "workflow change" or "unexpected review friction."

**Empirical grounding.** Four empirical instances at the AMAS framework production project as of v2.16 canonicalization (this PR):

1. `3d10c76` (PR-9 squash, 2026-05-02) — instance of class (c) cycle-summary observations: PMN-005 finalized observations integration including post-PR-window content not in feature-branch commits.
2. `80f5a4a` (PR-10 squash, 2026-05-02) — instance of class (a) Reviewer-engagement absorption summary: 5-pass Codex post-PR review absorption summary with PMN-006 (b) taxonomy in final form, pass-5 findings, auto-trigger sub-observation.
3. `80f5a4a` (PR-10 squash, same commit) — instance of class (d) self-referential pattern-promotion entry: explicit "M-A7 promotion trigger met (second instance of the merge-commit-body data integration pattern this cycle)" — strongest possible empirical confirmation by pattern self-naming at the cycle that promotes it.
4. `817c12f` (PR-11 squash, 2026-05-02) — instance of class (a) Reviewer-engagement absorption summary: 5-finding Codex post-PR review absorption (4 path-(a) + 1 path-(β); cycle close at 3 review passes within spec §5 step 15's 4-pass cap), bounded-continuation rule applications recorded.

Four-instance evidence (PMN-005 §6/§7 candidate framing → PMN-006 §6.2 operationally canonical → PMN-006 §6.2 explicit canonical-text deferral to Part B → this PR canonical §-section text) promotes M-A7 from operationally canonical to canonical §-section text.

### §18.4. Framework version-bump trigger criteria

The framework's canonical document version sequence (v2.14.1, v2.15, v2.16, v3.0.0, ...) advances by version-bump events. Bump-trigger criteria are structurally parallel to §18.1's PMN-trigger criteria but applied to the framework's own canonical document rather than to project-specific cycle-close adjudication. This section names the criteria that warrant a bump, distinguishes patch / minor / major bump tiers, and prescribes the substantive-reading interpretation for borderline cases.

**Patch bump (vN.M.P → vN.M.(P+1)).** Patch bumps correct internal contradictions, cross-file inconsistencies, and miscounts in recently-shipped minor versions without adding new framework content. The corrected text is what was substantively intended at the prior release; existing adopters need not re-adopt unless corrections materially affect their use. Empirically grounded examples: v2.13.1 (filename standardization, §24 reframing, §24.3 example reframe, §12 count correction); v2.13.2 (§14 preamble count, canonical-doc filename standardization); v2.14.1 (seven defects across §15 misframing, retrofit Notes drift, etc.). Patch bumps preserve all section numbers; no renumbering or restructuring; no new mechanisms; no monitoring item changes.

**Minor bump (vN.M → vN.(M+1)).** Minor bumps add substantive new canonical text in a feature-class cluster, introduce new mechanisms, add new monitoring items, or canonicalize new disciplines. Minor bumps preserve backward compatibility — existing adopters can absorb the bump incrementally without restructuring their projects. Empirically grounded examples: v2.14 (Reviewer claimed-action verification at §8.1.1.2 + §24.3.1 cross-reference + §24.2(b) refinements); v2.15 (PR-10 substantive new canonical text in §8.1.1.1 / §8.1.1.2 / §23.6.1 / §23.6.2 / §24.3.1 leaves + minimal parent frames for §8 / §23 / §24).

**Major bump (vN → v(N+1)).** Major bumps restructure canonical patterns, introduce breaking changes to artifact forms, or cascade superseded ADR effects across multiple sections. Major bumps may require adopters to migrate. Empirically grounded examples: v3.0.0 (anticipated; full v3 framework package release per ADR-003 Decision 1 + Decision 2 12-content-PR sequence, transitioning from v2.x in-canonical-document framework to v3 distributed package shape).

**Substantive-reading interpretation.** The bump-tier criteria above use substantive content as the discriminator, not strict-literal section-number changes. A cycle that adds substantial new canonical text within existing §-numbering (e.g., a new sub-section §8.1.1.3 under existing §8.1.1) is a feature event qualifying for minor bump even if no new top-level §-number is introduced. A cycle that corrects a same-section inconsistency without new content is a patch event even if the corrected text is substantial. The substantive-reading interpretation prevents §-numbering ceremony from gating semantically-meaningful version progression.

The strict-literal alternative — bump only when a new top-level §-section is added — produces under-bumping: substantial canonical-text additions silently absorb into existing §-numbering and the version sequence understates framework evolution. The substantive-reading interpretation is canonical; strict-literal interpretation is non-canonical.

**Application discipline.** The cycle Architect adjudicates the bump-or-not-bump call at cycle close, after canonical content is authored and before owner squash-merges. Adjudication considers: (i) substantive-content scope (lines of new canonical text, number of new disciplines / monitoring items / mechanisms); (ii) feature-class cluster boundaries (single-cluster minor; multi-cluster substantive may warrant evaluation against major); (iii) backward-compatibility (any breaking change to artifact forms or canonical patterns); (iv) cross-section dependency (whether new content cascades into multiple sections that all need updating).

If the Architect adjudication is ambiguous (e.g., the cycle's content sits at the patch/minor boundary), the default is to bump — under-bumping understates evolution, over-bumping is a noop for adopters who absorb incrementally.

**Cross-reference: §18.1.** Bump-trigger criteria and PMN-trigger criteria are independent. A cycle may trigger PMN authorship without triggering a version bump (e.g., a workflow-change PMN documenting a new pre-flight discipline that doesn't add canonical text). A cycle may trigger a version bump without PMN authorship (rare; typically a substantive-content cycle without unexpected friction).

**Recording guidance.** Bump-trigger adjudication occurs at cycle close. When the bump-or-not-bump call is non-obvious (substantive-reading boundary cases), the cycle Architect records the adjudication rationale in the merge-commit-body per §18.3 — preserves the rationale alongside the cycle's other cycle-close content. Owner reviews the rationale as part of squash-merge action.

## §23. Architect pre-handoff self-review

This section governs the Architect's receiving-side discipline against own-authored claims at the point of handoff to Builder. The discipline is bidirectionally symmetric to §8.2 (Builder pre-flight against Architect prompt assertions) and is canonicalized as §24.3 receiving-side caveat-discipline. The Architect treats own-authored arithmetic claims, section citations, and prose-arithmetic decompositions as §24.2(a) external-system-behavior assertions requiring self-verification before handoff.

### §23.6. Self-review disciplines

Two leaf disciplines apply at Architect pre-handoff self-review: prose-arithmetic decomposition with cumulative-diff-stats re-derivation (§23.6.1), and 4-iteration-to-fixed-point self-review (§23.6.2). Both apply iteratively to fixed-point per §23.6.2.

#### §23.6.1. Prose-arithmetic decomposition

Architect-authored deliverable specs and review-context files contain arithmetic claims — counts (file totals, line totals, diff stats), percentages (PMN-emission-rate, monitoring-item exceedance), sums (cumulative additions across PRs), ratios (claim-density, observation-density). Each claim is a §24.2(a) external-system-behavior assertion about a derivable value, and each is a candidate for prose-arithmetic drift across surfaces in the same deliverable.

The discipline is **prose-arithmetic decomposition**: every arithmetic claim in the spec text is decomposed into its operand expressions in the spec text itself, and each operand expression resolves to a verifiable source. If the spec writes "the PR adds 3 files," the spec also writes the operand decomposition: e.g., "1 PMN file + 1 handoff file + 1 review-context file = 3 files." If the spec writes "PMN-rate is 5/9 = 56%," the spec also writes the operands: e.g., "5 PMNs (PMN-001 through PMN-005) over 9 cycles (PR-1 through PR-9, excluding PR-0 pre-pre-commit-discipline) = 55.56%, displayed as 56%."

Path-(a) revision propagates through operands: if any operand source changes (a new PMN authored mid-cycle; a path-(a) revision adds a file), the spec re-derives every claim that depends on that operand. Claims that share operands cluster; revising one operand revises all claims in the cluster.

##### §23.6.1.1. Sub-rule (e.1) — Cumulative-diff-stats re-derivation

After any path-(a) revision to any artifact in a deliverable, cumulative diff stats and any approximate counts are re-derived from `git diff --stat` against the actual current branch state. The re-derivation produces landed exact counts: integer values matching `git diff --stat` output, never approximate counts (no `~`-prefixed numbers in any handoff or review-context Validation run Evidence section).

Approximate counts in pre-commit Builder claims are a defect class. They cannot be verified against the working tree at pre-commit time (the working tree carries an exact count, not an approximate one), and they propagate drift if the actual count differs from the approximation when the count changes through subsequent revisions. The cumulative-diff-stats re-derivation is run iteratively, after every path-(a) revision iteration, until the deliverable's pre-commit state is final. The Validation run Evidence section of each handoff is populated only with landed exact counts at the final pre-commit state.

The sub-rule's empirical grounding: the PR-8 cycle had three iterations of prose-arithmetic drift on the Validation run Evidence section before the gap was named in PMN-005 §4.4 and canonicalized here.

#### §23.6.2. Iterative-to-fixed-point self-review

Architect §23.6 self-review applies iteratively to fixed-point. Single-iteration self-review is empirically insufficient: section-citation slips and prose-arithmetic drift can survive a single iteration of self-review, because the iteration that authored a defect is the same iteration that proofread it — the cognitive frame that introduced the slip is the same frame that scans for slips.

Empirical observation across three consecutive cycles in the AMAS framework production project (PR-7, PR-8, PR-9): four iterations are required for convergence. Iterations 1–3 each may catch defects; iteration 4 confirms convergence (no new defects detected).

**Discipline.** §23.6 self-review is applied to a deliverable spec or any Architect-authored artifact subject to the discipline as follows:

- **Iteration 1** — initial self-review pass against the §23.6 sweep set: section-citation correctness, prose-arithmetic decomposition (per §23.6.1), claim-text consistency across surfaces, phantom-action audit, scope-leakage check.
- **Iteration 2** — re-application of the same sweep set; if defects caught, path-(a) revise and proceed; if no defects, iteration 3 is the convergence check.
- **Iteration 3** — re-application; same convergence check.
- **Iteration 4** — final sweep; no defects detected = convergence; defects detected = iteration 5+ until convergence.

**Convergence is fixed-point.** An iteration that detects zero defects following an iteration that detected zero defects is convergence. A single zero-defect iteration is not convergence — it may have missed defects the prior iteration caught implicitly. Two consecutive zero-defect iterations is convergence.

**Iteration count is empirical, not normative.** Four iterations is the observed convergence count across three cycles; it is not a hard rule. If a deliverable converges in three iterations (two consecutive zero-defect iterations), three is sufficient. If a deliverable does not converge in four iterations (defects continuing to surface), iteration 5+ is run until convergence.

**Anti-pattern: attestation drift.** A §23.6 self-review record's claim about *what was verified* must itself be verified against *what was actually applied to the body*. The overclaim pattern — attestation lists citations that aren't in the body, or claims sweeps that weren't run — is a recurring failure mode where the attestation text is authored from a checklist of disciplines rather than from the actual content of the artifact under review. Iteration 2+ specifically scans the §23.6 self-review record for attestation drift.

## §24. Cross-surface verify-before-assert meta-pattern

This section names the cross-surface verify-before-assert meta-pattern that recurs across the framework's §-section disciplines. The pattern is: claims about external-system state (repository state, tool output, file content, collaborator output) are §24.2(a) assertions requiring verification against the asserted state at receiving time, regardless of who authored the claim or which surface the claim was authored on. Subsections enumerate the meta-pattern's sub-shapes (§24.2) and the receiving-side caveat-discipline that operationalizes the pattern at each receiving direction (§24.3).

### §24.2. Sub-shape characterization

The four pre-existing sub-shapes — (a) external-system-behavior assertion, (b) propagation-incompleteness, (c) anticipatory-state assertion, (d) cross-receiving-direction symmetry — are inherited from prior framework versions and are not modified by Part A canonicalization. Part A applications cite §24.2(a) for external-system-behavior assertion at Reviewer-output-absorption (§8.1.1.1, §8.1.1.2), Architect pre-handoff self-review (§23.6 family), and Architect ← Builder hand-back (§24.3 fifth direction below).

### §24.3. Receiving-side caveat-discipline

The receiving-side caveat-discipline operationalizes the §24 meta-pattern at each receiving direction in the cycle's communication topology. Five receiving directions are canonicalized:

- Builder pre-flight against Architect-asserted external-system state in prompts (§8.2)
- Architect pre-handoff self-review against own-authored claims (§23.6, §23.6.1, §23.6.2)
- Builder receiving Reviewer findings (§8.1.1, §8.1.1.1, §8.1.1.2)
- Owner receiving Builder stop-and-show (§8.3)
- Architect ← Builder hand-back (§24.3.1 below)

#### §24.3.1. Architect ← Builder hand-back symmetric-application clause

The §24.3 receiving-side caveat-discipline applies bidirectionally. The four pre-existing receiving directions cover Builder, Architect (own-authored), Builder (Reviewer-emitted), and owner. A fifth receiving direction is added by symmetric-application clause: **Architect ← Builder hand-back.**

When Builder hands back to Architect at cycle close, the hand-back contains claims about external-system state — Reviewer output observed, branch state, gh CLI output, file content matching prescription, phantom-action absence. Architect treats those claims as §24.2(a) assertions requiring verification before sign-off, not just receipts to acknowledge. The mechanism is parallel to §8.2 Builder-side pre-flight discipline against Architect-asserted external-system state in prompts: same §24 mechanism, opposite receiving direction. Both are §24.2(a) verify-before-assert applications at receiving-side; the symmetry is structural, not coincidental.

**Default Architect-side post-handback five-point check pattern.** Where verification is cheap (a handful of API calls, a few git commands), Architect runs the five-point check against the hand-back claims:

1. **Two-endpoint poll of Reviewer output** (per §8.1.1.1) — confirm Reviewer output as Builder reported it; reconcile against last-known-state via both formal-review and issue-comment endpoints.
2. **Branch tip-SHA verification** — `git rev-parse HEAD` output must match the expected SHA from the prior session's hand-back; additionally `git status --porcelain` must be empty (clean working tree). The `git status` clean-tree check is necessary-but-not-sufficient on its own — SHA equality is the load-bearing tip-state proof, with clean-tree as adjunct check; `git status` alone reports working-tree state and ahead/behind upstream but does not prove HEAD equals an expected SHA.
3. **File content audit against prescription** — for each file Builder claims to have authored or modified, verify content matches the spec's §2 prescription. `git show <sha>:<path>` or equivalent.
4. **Phantom-action audit** — verify no claimed action lacks corresponding repository state (commits exist; files exist; counts match). Inverse of §8.1.1.2 sub-shape A check applied to Builder hand-back.
5. **Comment-content claim verification** (per §8.1.1.2) — for any Reviewer comment Builder reports as adjudicated, verify the comment's substantive content claims against actual repository state, not just delivery.

A project may codify a project-specific check pattern in repo-local Architect reference per §23.5 inherited owner preferences. The five-point pattern is the default; project-specific deviations are documented at the project level.

**Provenance.** This clause was pre-flagged at PMN-003 (g) as deferred to v3 substantive content authoring. The four-point check pattern (PMN-003 (g)) extended to five-point in PMN-005 §2.5 in light of the reviewer-claimed-effects-don't-land defect class. §24.3.1 canonicalizes the five-point pattern.
