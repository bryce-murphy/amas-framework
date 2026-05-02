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
    --jq '.[] | select(.user.login=="<reviewer>") | select(.submitted_at >= "<last-known>" and .id > <last-seen-id>)'

# Endpoint (b) — issue-comment summary
gh api --paginate repos/{owner}/{repo}/issues/{issue_number}/comments \
    --jq '.[] | select(.user.login=="<reviewer>") | select(.created_at >= "<last-known>" and .id > <last-seen-id>)'
```

The `>=` plus `id` filter handles same-second emission tie-breaks symmetrically across both endpoints: strict `>` on second-granularity timestamps drops boundary-coincident emissions, while `>=` paired with a strict-`>` last-seen-ID tie-breaker catches same-second emissions and excludes the previously-seen boundary emission by ID. `<last-known>` is the timestamp of the most recently absorbed emission per endpoint; `<last-seen-id>` is that emission's `id`.

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
