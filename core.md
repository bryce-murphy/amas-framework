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

The Reviewer's verdict is delivered to the Builder via the GitHub API surface across three distinct endpoints: a formal Pull Request Review object, a top-level issue-comment summary, and line-level review comments. The three endpoints carry distinct content shapes and are not interchangeable: the formal Pull Request Review carries the PR-level review state machine and any review-body prose; the issue-comment summary carries the verdict text; the line-level review-comments endpoint carries line-anchored findings. Subsection §8.1.1 specifies the three-endpoint polling discipline that the Builder applies at every Reviewer-output absorption point in a cycle.

#### §8.1.1. Reviewer-output channel handling

Two leaf disciplines apply at Reviewer-output absorption: dual-signal output handling (§8.1.1.1) covering the three delivery endpoints and their reconciliation, and claimed-action verification (§8.1.1.2) covering the receiving-side verification of any reviewer-claimed action against actual repository state.

##### §8.1.1.1. Reviewer dual-signal output handling

When a Reviewer is invoked on a Pull Request, the review-rendering surface emits the Reviewer's output through three distinct GitHub API endpoints with distinct content shapes. The Builder absorbing Reviewer output cannot rely on single-channel polling.

The three endpoints are:

(a) **Formal Pull Request Review** — accessed via `gh api repos/{owner}/{repo}/pulls/{pull_number}/reviews` or `gh pr view {pull_number} --json reviews`. Carries the PR-level review summary state machine (APPROVED / CHANGES_REQUESTED / COMMENTED) and the substantive review body prose when the Reviewer attaches one to the formal review submission; populated by formal Pull Request Review API objects (e.g. those created via `POST /repos/{owner}/{repo}/pulls/{pull_number}/reviews`).

(b) **Issue-comment summary** — accessed via `gh api repos/{owner}/{repo}/issues/{issue_number}/comments` or `gh pr view {pull_number} --json comments`. Pull Requests are issues from the GitHub API perspective; the issue-comment endpoint receives top-level comments on the PR, including Reviewer-emitted summary verdicts and autonomous bot comments outside the formal-review submission shape.

(c) **Line-level review comments** — accessed via `gh api repos/{owner}/{repo}/pulls/{pull_number}/comments`. Carries line-anchored substantive findings — review comments attached to specific file/line locations rather than to the PR as a whole. Empirically the most defect-dense Reviewer output channel.

Two pass shapes are empirically observed across cycles dogfooded in the AMAS framework production project:

- **Substantive-finding pass shape**: at least one endpoint carries substantive content. Endpoint (a) may carry the review state plus any review-body prose; endpoint (b) may carry verdict text; endpoint (c) may carry line-anchored findings. Per the empirical-pattern note below, the substantive content distribution across endpoints varies per cycle — Builder polls all three endpoints and reconciles.
- **Cycle-trailing-clean-Approve pass shape**: no substantive content emits at any endpoint, with formal review state at endpoint (a) reaching APPROVED or remaining COMMENTED with boilerplate-only body (typical body phrasing: "Codex Review: Didn't find any major issues."). Builder treats no-substantive-emission across all three endpoints as a clean cycle, subject to the settling-period rule below.

The empirical observation that cycle-trailing-clean-Approve emits to the issue-comment endpoint only is a preliminary hypothesis under continuing test; the Builder discipline below does not depend on the hypothesis being confirmed. Single-channel polling is structurally unreliable regardless of which pass shape is actually emitted, because the Builder cannot know in advance which shape the cycle will produce.

**Empirical pattern (substantive-verdict landing surface).** Across the framework's production-project cycle record, the substantive verdict has empirically landed at any one of the three endpoints — sometimes only at (b) (boilerplate-style summary), sometimes only at (a) (review body without line comments), sometimes only at (c) (line-anchored findings without summary verdict), and sometimes across two or all three jointly. Builder cannot pre-judge which endpoint will carry the verdict for a given cycle; the discipline is to poll all three.

**Builder discipline.** At each Reviewer-output absorption point in a cycle, Builder polls all three endpoints, filters by author and `created_at`/`submitted_at` against last-known-state, and reconciles before treating the absorption as complete:

```bash
# Endpoint (a) — formal Pull Request Review
gh api --paginate repos/{owner}/{repo}/pulls/{pull_number}/reviews \
    --jq '.[] | select(.user.login=="<reviewer>") | select(.submitted_at > "<last-known>" or (.submitted_at == "<last-known>" and .id > <last-seen-id>))'

# Endpoint (b) — issue-comment summary
gh api --paginate repos/{owner}/{repo}/issues/{issue_number}/comments \
    --jq '.[] | select(.user.login=="<reviewer>") | select(.created_at > "<last-known>" or (.created_at == "<last-known>" and .id > <last-seen-id>))'

# Endpoint (c) — line-level review comments
gh api --paginate repos/{owner}/{repo}/pulls/{pull_number}/comments \
    --jq '.[] | select(.user.login=="<reviewer>") | select(.created_at > "<last-known>" or (.created_at == "<last-known>" and .id > <last-seen-id>))'
```

The lexicographic `(timestamp > last-known) OR (timestamp == last-known AND id > last-seen-id)` form handles same-second emission tie-breaks symmetrically across all three endpoints. The naive `>=` plus unconditional-id-gate form (`timestamp >= last-known AND id > last-seen-id`) is incorrect: it requires `id > last-seen-id` for ALL results regardless of timestamp, which drops valid new emissions whose timestamp exceeds the boundary but whose id is below the last-seen-id (possible when ids do not strictly track submitted_at/created_at — e.g., a long-drafted review id N1 submitted at t2 after a faster-drafted review id N2 > N1 submitted at t1). The correct form gates the id comparison only inside the same-timestamp tie clause; cross-timestamp emissions pass through the `timestamp > last-known` clause without id constraint. `<last-known>` is the timestamp of the most recently absorbed emission per endpoint; `<last-seen-id>` is that emission's `id`.

The `--paginate` flag is required: GitHub REST list endpoints return at most 30 items per page by default; on long-lived PRs (or repos where the Reviewer has emitted many objects) single-page polling produces false-negative "no emission" verdicts when newer Reviewer output lives on a subsequent page. `gh api --paginate` retrieves all pages and concatenates results before jq filtering.

All three polls run; results from all three are reconciled. A clean-Approve cycle-trailing pass shows no review object, no line comments, and a fresh issue-comment with boilerplate verdict. A substantive-finding pass shows some combination of fresh review object(s), fresh line comments at specific file/line locations, and a fresh issue-comment with verdict text — varying per cycle per the empirical-pattern note above. A no-emission state on all three endpoints means the Reviewer has not yet emitted; Builder waits and retries per the project's polling cadence.

**Anti-channel.** Comments authored by the Reviewer outside the three polled forms — for example, a top-level issue comment that is a clarification request or process question rather than a verdict, or a line-level review comment that is a clarification rather than a finding — are non-authoritative for substantive verdict regardless of phrasing. Builder treats such comments as informational; verdict status is determined by the formal-review, summary-comment, and line-comment triple only.

**Cross-reference.** §8.1.1.1 is a §24.2(a) external-system-behavior assertion application at the Reviewer-output-absorption surface. The verify-before-assert mechanism is the §24 cross-surface meta-pattern applied at this specific receiving direction. The three-endpoint enumeration above absorbs the recommendation matured at PMN-008 §5.8 (h.4) across 8 cycles' empirical evidence (PR-11 / PR-13 / PR-15 / PR-17 / PR-19 / PR-21 / PR-23 / PR-24).

##### §8.1.1.2. Reviewer claimed-action verification

When a Reviewer comment claims an action — that a commit was created, a file was added, a follow-up artifact exists, or a referenced identifier is valid — the comment may be delivered (the three-endpoint poll of §8.1.1.1 establishes delivery) but the claimed action may not correspond to actionable repository state. Delivery and effect are separate verifications.

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

**Empirical grounding (cross-cycle accumulation).** Cost-class one-iteration convergence at pure-token-swap class has accumulated 12 cross-cycle empirical positives across TASK-0019 through TASK-0034 cycles at the **pre-commit Codex desktop pass surface**: every cycle's pre-commit Codex pass-1 absorption applying path-(α')/path-(α)/path-(a) class fixes has converged at one iteration; zero cross-cycle empirical negatives surface. **Pre-commit Codex desktop pass-2** re-invocation is therefore NOT REQUIRED at pure-token-swap class absorption per §8.1.1.3 cost-class refinement; owner-ratification gate at re-derived (e.1) post-fix surface sufficient for pre-commit pass-2 exemption. Pattern is strongly canonicalized beyond ADR-006 D3 evidence-bar (3+ confirmations) by factor 4×. **Post-PR Reviewer re-review per `usage-guide.md` §7.1 + §7.3 remains binding** for every push addressing findings, including pure-token-swap class fix-up pushes; cost-class refinement at this section governs pre-commit pass-2 invocation only and does not extend to post-PR re-review discipline.

## §14. Universal handoff schema

A handoff is a cross-role or cross-session work-transition artifact that records the current state of a cycle for the receiving role or session. Handoffs are the durable-context bridge between roles (Architect → Builder, Builder → Architect, Builder → Reviewer) and across sessions of the same role; in-chat context is ephemeral and cannot serve this function. The artifact is git-tracked at `docs/handoffs/TASK-####-<kebab-slug>.md`, where `<kebab-slug>` matches the branch-name slug per `github-reference.md` §2.2 (Option B per ADR-005).

The schema serves three functions: (a) durable cycle-state preservation across role and session boundaries; (b) verification anchor for receiving-role pre-flight per §8.2 (forthcoming at Part C+); (c) audit-trail anchor for cycle-close ledger authoring at hand-back and post-merge-note authoring at cycle close.

**Frontmatter form**: PMN-007 HEAD canonical 12-field form. The 12-field enumeration and `linked_pr` MC-C canonical-regex form are canonicalized at `templates/handoff-template.md` filled content; that template is the canonical surface. Per the mechanism-not-policy framing of §17, this section names the discipline and cites the template; the template carries the substantive form-detail.

**Body section structure**: canonical sections per observable cycle patterns at TASK-0021 onward — Metadata, Objective, Last completed step, Current state (including cumulative-diff-stats per §23.6.1.1 (e.1) staged-tree re-derivation), Decisions made, Assumptions, Risks, Blocking questions, Validation run, Exact next step, then numbered §-prescription sections (§1 through §N) per cycle structure, Cycle-close ledger, and Session log archive. The filled body section template at `templates/handoff-template.md` is the canonical surface.

**Path conventions**: `docs/handoffs/TASK-####-<kebab-slug>.md`. The TASK-#### counter is monotonically incremented across cycles; the highest existing TASK-#### across any artifact in the repo is authoritative for the next-cycle counter assignment.

**Status field lifecycle**: `drafted` (pre-stage) → `active` (post-stage / pre-merge) → `resolved` (post-merge per PMN-001 (k) Action substitution). Drift from these exact values breaks the linked-pr-fix-up Action's status transition per `.github/scripts/linked-pr-fix-up.py` canonical regex.

**Direction-variant overview**: §14.1 through §14.7 enumerate seven direction-specific variants. Each inherits the §14 universal frontmatter and body section structure with per-variant adjustments specified at the variant's section. The variants are: Architect → Builder (§14.1), Builder → Reviewer (§14.2), Reviewer → Builder (§14.3), Reviewer → Architect (§14.4), Builder → Architect (§14.5), Human → AI (§14.6), AI → Human (§14.7).

### §14.1. Architect → Builder

The canonical primary handoff direction. Architect authors a TASK-#### spec at session start; Builder receives spec at Claude Code session kickoff per PMN-002 (d) code-fenced kickoff prompt convention.

**Frontmatter**: §14 universal 12-field form unchanged.

**Body structure**: §14 universal canonical sections; §-prescription sections (§1-§N) prescribe substantive deliverables per cycle structure. Cycle-class designation in §1 (substantive-content / architectural / lightweight-absorption / chore) determines anticipated cycle-bandwidth + recursive-self-instantiation salience.

**Architect-side responsibilities**:
- Spec authoring with §24 verify-before-assert at all claims about repo state
- §23.6 self-review pass before handoff hand-off (§23.6 + §23.6.1 + §23.6.2 + §23.6.3)
- Phase 1 staged adjudications enumerated in spec for owner ratification at Builder step-1 stop-and-show
- §23.6.3 sub-shape A canonical-impact-surface-completeness check + template-content authoring meta-pattern applied at spec authoring

**Builder-side responsibilities**:
- Pre-flight verification batch per §8.2 substrate (Part C.2; v2.14.1 §8.2 substrate) — branch-name regex compliance, base-branch freshness, working-tree state, (i.5) sub-shape sweeps
- Step-1 stop-and-show surfacing all Phase 1 adjudications + pre-flight findings before Step-2 branch creation
- Substantive content authoring per spec §4 prescriptions
- Step-10 pre-commit stop-and-show with cumulative-diff-stats per (e.1) + verification claims

**File path**: `docs/handoffs/TASK-####-<kebab-slug>.md`. `<kebab-slug>` matches branch-name slug.

**Cross-references**: §14 (universal); §23.6.3; `github-reference.md` §2.2; `templates/handoff-template.md`.

### §14.2. Builder → Reviewer

The Builder hands a review-context kickoff prompt to the Reviewer (Codex desktop or `@codex review` invocation) per PMN-002 (d) code-fenced kickoff prompt convention. The transition surface is the review-context file rather than a separate handoff file; the review-context body's "Codex desktop pre-commit kickoff" or "Codex post-PR kickoff" section carries the kickoff prompt.

**Frontmatter**: review-context 1-field canonical form per §17.7. Status field lifecycle: `drafted` (pre-Codex-pass) → `recorded` (post-merge per PMN-001 (k) Action substitution).

**Body structure**: review-context body sections per §17.7 — Metadata, Builder claims to verify, Reviewer focus, kickoff section, output absorption section.

**Builder-side responsibilities**:
- Author the review-context Builder claims with cross-platform verification commands per PMN-004 §5 (b) cross-platform verification discipline
- Author the Reviewer focus section enumerating cycle-relevant focus areas
- Author the kickoff prompt code-fenced per PMN-002 (d) reliable-copy convention
- Pose the kickoff to the Reviewer per ADR-001 D11 owner-invokes convention (the project owner is the actual paster on Codex desktop)

**Reviewer-side responsibilities**:
- Run the review per the kickoff prompt directives
- Emit findings per the convention's severity taxonomy per PMN-004 §5 (a) three-level (Blocking / Major / Minor)

**File path**: `docs/reviews/PR-NN-codex-pre-commit.md` (pre-commit variant) or `docs/reviews/PR-NN-codex-post-pr.md` (post-PR variant).

**Cross-references**: §17.7; §8.1.1; ADR-001 D11; PMN-002 (d); PMN-004 §5 (a) + (b); `templates/review-template.md`.

### §14.3. Reviewer → Builder

Reviewer output (Codex pre-commit or post-PR review) absorbed verbatim per PMN-002 (a) verbatim-output convention into the review-context output-absorption section. The absorption is the durable record; the receiving Builder reads the absorbed output as input to fix-up authoring or path-(β) record-and-proceed adjudication.

**Frontmatter**: review-context 1-field form unchanged at this direction; status remains `drafted` until post-merge transition.

**Body structure**: review-context output-absorption section populated. Each Codex pass appears as a numbered subsection (Codex pass 1, Codex pass 2, ...) with verdict, verbatim findings, adjudication routing per §8.1.1.3 (path-(a) revise / path-(β) record-and-proceed / Blocking handback), and resolution applied at path-(a) iterations.

**Builder-side responsibilities**:
- Capture Reviewer output verbatim — no paraphrase, no summary substitution per §8.1.1.2 phantom-action verification discipline
- Adjudicate routing per §8.1.1.3 cost-class refinement (pure-token-swap one-iteration vs genuinely-asymptotic break-out)
- Apply severity taxonomy three-level per PMN-004 §5 (a) at adjudication time
- Re-stage + (j)-sweep + cumulative-diff-stats re-derivation per §23.6.1.1 (e.1) at each path-(a) iteration

**Reviewer-side note**: the Reviewer does not author this section directly; the Builder absorbs the Reviewer output into it. The verbatim convention prevents Builder paraphrase from masking phantom-action discrepancies between claimed and actual Reviewer output.

**Cross-references**: §8.1.1; §8.1.1.2; §8.1.1.3; §17.7; §23.6.1.1; PMN-002 (a); PMN-004 §5 (a).

### §14.4. Reviewer → Architect

Reviewer post-PR feedback surfaces to the Architect via the review-context "Post-PR Codex review state" section paired with the handoff "Post-PR Codex review state" section. No new file is created; communication flows through the existing review-context and handoff artifacts at the post-PR window.

**Frontmatter**: existing review-context 1-field form and existing handoff 12-field form; no new artifact.

**Body structure**: review-context post-PR section populated per §17.7 Codex post-PR variant — three-endpoint poll record per §8.1.1.1, verdict, verbatim findings, adjudication routing.

**Receiver (Architect) responsibilities**:
- Three-endpoint poll of Reviewer output per §8.1.1.1 (`pulls/{pr}/reviews` + `issues/{pr}/comments` + `pulls/{pr}/comments`)
- Adjudicate findings per §8.1.1.3 cost-class refinement (path-(a) revise vs path-(β) record-and-proceed vs Blocking handback)
- Surface adjudication via cycle-close ledger or in-cycle path-(a) fix-up authoring as appropriate

**Reviewer-side note**: the same verbatim-output discipline as §14.3 applies; the Architect absorbs Reviewer output verbatim into the post-PR section.

**Cross-references**: §8.1.1.1; §8.1.1.3; §17.7; §24.3.1; PMN-002 (a).

### §14.5. Builder → Architect

The Builder hands back to the Architect at stop-and-show points and at cycle-close hand-back. The transition surface is the existing TASK-#### handoff file with `## Last completed step` updated to the current cycle position and the cycle-close ledger populated at hand-back.

**Frontmatter**: handoff §14 universal 12-field form unchanged; `status` field remains `drafted` or `active` per the cycle's progression at hand-back.

**Body structure**: §14 universal canonical sections; absorption surfaces include `## Last completed step` updated at each hand-back, `## Current state` re-derived per (e.1) staged-tree convention, `## Decisions made` extended with in-cycle adjudications, and `## §10. Cycle-close ledger` populated at cycle-close hand-back with carry-forward observations and PMN candidacy notes.

**Builder-side responsibilities**:
- Update `## Last completed step` to the resume-anchor for the next session
- Re-derive `## Current state` cumulative-diff-stats per §23.6.1.1 (e.1) at each hand-back
- Author cycle-close ledger items per ADR-006 D3 evidence-bar discipline (observation-recording, not canonicalization-pre-commitment)
- Surface stop-and-show prompt per §8.3 (forthcoming at Part C+) at each hand-back

**Architect-side responsibilities**:
- Run the §24.3.1 five-point post-handback check at cycle-close hand-back (three-endpoint poll, branch tip-SHA verification, file-content audit, phantom-action audit, comment-content claim verification)
- Author squash-merge body content at owner squash-merge instant
- Adjudicate cycle-close ledger items for next-cycle scope or PMN candidacy

**Cross-references**: §8.3 (forthcoming at Part C+); §10.5 (forthcoming at Part C+); §23.6.1.1; §24.3.1; ADR-006 D3.

### §14.6. Human → AI

Owner kickoff messages, Phase 1 adjudication ratifications, scoping ratifications, and strategic-direction decisions flow from the human owner to the AI roles (Architect, Builder, Reviewer). No file artifact carries this direction; communication is via the chat interface (Claude.ai for Architect, Claude Code for Builder, Codex desktop for Reviewer).

**Frontmatter / body structure**: not applicable; no file artifact.

**Owner-side role**:
- Ratify Phase 1 adjudications at Builder step-1 stop-and-show before substantive authoring proceeds
- Ratify or override Architect recommendations on adjudications surfaced at any cycle gate
- Hold squash-merge authority per ADR-001 D9 admin-bypass posture (the owner is the only role authorized to merge)
- Set strategic direction across cycles, including ADR-class decisions and out-of-band scope adjustments

**AI-side note**: AI roles act within owner-ratified scope; out-of-scope or ambiguous conditions route back to the owner per §8.3 (forthcoming at Part C+) stop-and-show discipline.

**Cross-references**: ADR-001 D9; ADR-001 D11; §8.3 (forthcoming at Part C+); spec §0 standing-scope ratifications convention.

### §14.7. AI → Human

The AI surfaces options, recommendations, decision tables, and stop-and-show findings to the human owner for ratification or override. No file artifact carries this direction; communication is via the chat interface paired with the durable handoff and review-context artifacts the AI authors.

**Frontmatter / body structure**: not applicable; no file artifact for the chat surfacing itself. The AI authors decision-supporting content into the durable artifacts (handoff for Builder/Architect surfacings; review-context for Reviewer-related surfacings).

**AI-side responsibilities**:
- Surface options with explicit benefits, trade-offs, and Architect or Builder recommendations
- Apply Item 13 anti-binary-routing at outcome adjudications — surface multi-option framings rather than binary "do or don't" routings when judgment is involved
- Retain analytical and authoring judgment within owner-ratified scope; escalate out-of-scope or ambiguous conditions per §8.3 (forthcoming at Part C+)
- Apply §24 verify-before-assert at all claim-making contexts in the surfacing

**Architect-side surfacing pattern**: Phase 1 adjudication recommendations at spec authoring; cycle-close ledger surfacing at cycle close.

**Builder-side surfacing pattern**: pre-flight findings at step-1 stop-and-show; cumulative-diff-stats and verification-claims surfacing at step-10 pre-commit stop-and-show.

**Cross-references**: §24; ADR-006 D3 evidence-bar discipline; spec §1.3 Phase 1 adjudication convention.

## §17. Templates

This section houses the canonical template forms for project artifacts. Each template specifies required structure, required fields, and authoring surface for an artifact class. Template leaves canonicalize incrementally across the v3.0 substantive-content authoring sequence; this cycle establishes the parent frame, with leaf canonicalization (ADR template, PR template, Review summary template, CLAUDE.md template, AGENTS.md template, project-instruction-files template) deferred to subsequent template-batch cycles per ADR-003 Decision 2 (PR-15 / PR-16).

Templates are mechanism, not policy. The discipline that templates encode (handoff schema at §14, review schema at §8.1.1, post-merge note schema at §18.2) is canonicalized in the §-section that defines the discipline. The template form at §17 is the artifact-construction surface that pairs with the discipline.

### §17.5. Template lifecycle

Templates progress through canonical lifecycle phases tracked in YAML frontmatter `status` field:

- **`stub`**: scaffold-stub state per FEAT-0001 v3 framework package scaffold (PR-2). Frontmatter `status: stub` + `filled_by: per ADR-003` (or successor canonical plan reference). Body content minimal (4-9 lines typical) — scaffolding only, no substantive content.
- **`drafted`**: substantive content authored at template-batch substantive cycle. Frontmatter `status: drafted` + `filled_by: PR-NN (TASK-####)` (actual PR/TASK number at content-fill time). Body fully populated with canonical content.
- **`filled`**: synonym for `drafted` post-merge; some templates use `filled` directly when content-fill cycle ratifies substantive content as final at merge. Frontmatter `status: filled` + `filled_by: PR-NN (TASK-####)`.
- **`recorded`** (review-context only): post-merge state for review-context files per PMN-001 (k) Action substitution. Status field transitions `drafted` → `recorded` at chore-fix-up squash post-merge.

**Template version vs framework version**:

Templates carry `template_version: 3.0.0` in YAML frontmatter (or YAML comment for `.yml` files). Framework version is carried in canonical-law trio (`core.md` / `github-reference.md` / `usage-guide.md`) frontmatter `framework_version` field + README.md Class A canonical-version-of-record line. Template-version vs framework-version distinction: templates version with the framework major version (template_version 3.0.0 ships with framework_version 3.0.0); per-cycle minor/patch framework-version bumps do NOT bump template_version unless template content materially changes.

**Filled-by field semantics**:

`filled_by` field on every stub points at canonical plan reference (currently `per ADR-003`, post-ADR-006 reference may rotate to `per ADR-006` for unfilled stubs at content-fill time per ADR-003 §Consequences distributed-update discipline + ADR-006 D4 + Item 14 retroactive-supersession-marking sub-rule). Each substantive content PR updates its filled stub's `filled_by` field to `PR-NN (TASK-####)` at content-fill time.

**Authoring surface**:

Substantive template content fills at template-batch substantive cycles per ADR-006 D2 batch sequence (Batch P1 process templates / Batch P2 GitHub-artifact templates / Batch P3 prompts). Per-cycle distributed-update sweeps drop forward-reference qualifiers across just-relevant surfaces at each content-fill cycle per ADR-006 D4.

**Cross-references**: §17 (parent frame); §18.4 (framework version-bump trigger criteria); ADR-003 (canonical plan reference + distributed-update discipline); ADR-006 (batch sequence); ADR-007 (Part C materialization scoping).

### §17.7. Review template

The review template canonicalizes the form for Codex desktop pre-commit + post-PR review-context files per ADR-001 D11 owner-invokes convention. Two variants share substantive structure with per-variant body section adjustments. Canonical surface: `templates/review-template.md` filled at PR-35 (TASK-0027); this section names the discipline per the mechanism-not-policy framing of §17.

**Frontmatter (canonical 1-field form)**:

```yaml
---
status: drafted
---
```

Status field lifecycle (per `.github/scripts/linked-pr-fix-up.py` canonical transitions):
- `drafted` (pre-stage; pre-Codex-pass) → `recorded` (post-merge per PMN-001 (k) Action substitution).

Drift from this exact form breaks Action transition. Verification via `.github/scripts/linked-pr-fix-up.py` canonical pattern matching at frontmatter-only scope.

**Body sections (Codex desktop pre-commit variant)**:

Canonical body section sequence: Metadata / Builder claims to verify / Reviewer focus / Codex desktop pre-commit kickoff / Codex desktop pre-commit output absorption.

- **Builder claims to verify**: numbered list of claims about staged-tree state. Each claim includes verification command (bash + PowerShell + cmd-side as cross-platform Builder requires per PMN-004 §5 (b) findstr codepage caveat for `§` byte sequence). Claim coverage per cycle scope: cumulative-diff-stats per §23.6.1.1 (e.1) + §-citation correctness + Class A v-bump per cycle scope + stub frontmatter updates per ADR-003 §Consequences + M-A7 enumeration verification + (j) all-instances grep sweep results + frontmatter shape conformance + cross-document state preservation.
- **Reviewer focus**: focus areas for Codex desktop pre-commit attention — substantive content shape verification + §-citation resolution + cumulative-diff-stats reconciliation + frontmatter shape conformance + (j)/(g)/(h)/(i) sweeps + recursive-self-instantiation salience check per PMN-008 §3.1.
- **Codex desktop pre-commit kickoff**: copy-paste-ready prompt for owner to paste into Codex desktop with project repository attached. Code-fenced per PMN-002 (d) reliable-copy convention.
- **Codex desktop pre-commit output absorption**: verbatim Codex output captured per PMN-002 (a) verbatim-output convention + `core.md` §8.1.1.2 phantom-action verification discipline.

**Body sections (Codex post-PR variant)**:

Differential structure from pre-commit variant:
- **Builder claims** preserved (already verified at pre-commit; serve as forward-reference for post-PR Codex against actual-merged state).
- **Reviewer focus** adjusts to post-PR scope (full-PR diff, not staged-tree only).
- **Three-endpoint poll record** populated per `core.md` §8.1.1.1: `pulls/{pr}/reviews` + `issues/{pr}/comments` + `pulls/{pr}/comments` outputs verbatim.
- **(w) cross-cycle data point** noted if Codex emits autonomously pre-trigger.

**Path conventions**:

- Pre-commit: `docs/reviews/PR-NN-codex-pre-commit.md`
- Post-PR: `docs/reviews/PR-NN-codex-post-pr.md` (when separate file; some cycles consolidate to single review-context per cycle convention)

**Bounded-continuation rule application**:

Review iterations bounded per `core.md` §8.1.1.3 cost-class refinement (pure-token-swap one-iteration; genuinely-asymptotic break-out). Each path-(a) revision triggers re-stage + (j)-sweep + cumulative-diff-stats re-derivation per §23.6.1.1 (e.1).

**Cross-references**: §8.1.1.1 (three-endpoint poll); §8.1.1.2 (phantom-action verification); §8.1.1.3 (bounded-continuation rule + cost-class refinement); §17 (parent frame); §17.5 (template lifecycle); §23.6.1.1 (e.1 cumulative-diff-stats re-derivation); ADR-001 D11; PMN-001 (k); PMN-002 (a) + (d); PMN-008 §5.8 (h.4); `templates/review-template.md` (canonical surface).

## §18. Post-merge note discipline

Post-merge notes (PMNs) are durable artifacts capturing learnings from merged PRs that warrant cross-cycle preservation. The PMN convention separates from in-cycle artifacts (handoff at §14, review-context at §8.1.1, AI Session Log at §13) by spanning across cycles: a PMN authored at cycle N captures observations from cycle N's merged PR(s) that future cycles N+1 through cycle close apply as standing discipline.

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

The PMN artifact form is canonical, not advisory. The framework already specifies form for analogous durable artifacts — handoffs at §14, ADRs at §7.1, templates at §17 — because specifying a discipline without specifying a form produces a discipline-erosion failure mode where the rule survives across cycles but the content does not. PMNs are repo-tracked artifacts under version control; the form below is the canonical structure.

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

**Cumulative empirical instances post-v2.16 canonicalization** (as of v2.37 canonicalization at PR-64 / TASK-0041):

The original four-instance empirical grounding above documented the M-A7 promotion event at PR-13 / v2.16. Subsequent substantive-cycle PRs have continued instantiating the M-A7 pattern at consistent cadence. Cumulative count per established enumeration `PR-9 + PR-10 + PR-11 + PR-13 + PR-15 + PR-17 + PR-19 + PR-21 + PR-25 + PR-27 + PR-29 + PR-31 + PR-33 + PR-35 + PR-37 + PR-39 + PR-41 + PR-43 + PR-45 + PR-48 + PR-52 + PR-54 + PR-56 + PR-58 + PR-60 + PR-62 + PR-64 = 27` empirical instances spanning v2.16 through v2.37 canonicalization (substantive-cycle PRs only; defect-fix patches and chore-fix-up substitution PRs excluded per established M-A7 inclusion criterion).

The pattern has stabilized into operational steady-state across 27 consecutive substantive cycles; further cumulative-count amendments occur as Architect-side post-merge maintenance per established M-A7 cadence.

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

Three leaf disciplines apply at Architect pre-handoff self-review: prose-arithmetic decomposition with cumulative-diff-stats re-derivation (§23.6.1), 4-iteration-to-fixed-point self-review (§23.6.2), and reference-verification before spec authoring (§23.6.3). §23.6.1 and §23.6.2 apply iteratively to fixed-point per §23.6.2; §23.6.3 applies at spec-authoring time prior to handoff.

#### §23.6.1. Prose-arithmetic decomposition

Architect-authored deliverable specs and review-context files contain arithmetic claims — counts (file totals, line totals, diff stats), percentages (PMN-emission-rate, monitoring-item exceedance), sums (cumulative additions across PRs), ratios (claim-density, observation-density). Each claim is a §24.2(a) external-system-behavior assertion about a derivable value, and each is a candidate for prose-arithmetic drift across surfaces in the same deliverable.

The discipline is **prose-arithmetic decomposition**: every arithmetic claim in the spec text is decomposed into its operand expressions in the spec text itself, and each operand expression resolves to a verifiable source. If the spec writes "the PR adds 3 files," the spec also writes the operand decomposition: e.g., "1 PMN file + 1 handoff file + 1 review-context file = 3 files." If the spec writes "PMN-rate is 5/9 = 56%," the spec also writes the operands: e.g., "5 PMNs (PMN-001 through PMN-005) over 9 cycles (PR-1 through PR-9, excluding PR-0 pre-pre-commit-discipline) = 55.56%, displayed as 56%."

Path-(a) revision propagates through operands: if any operand source changes (a new PMN authored mid-cycle; a path-(a) revision adds a file), the spec re-derives every claim that depends on that operand. Claims that share operands cluster; revising one operand revises all claims in the cluster.

##### §23.6.1.1. Sub-rule (e.1) — Cumulative-diff-stats re-derivation

After any path-(a) revision to any artifact in a deliverable, cumulative diff stats and any approximate counts are re-derived from `git diff --stat` against the actual current branch state. The re-derivation produces landed exact counts: integer values matching `git diff --stat` output, never approximate counts (no `~`-prefixed numbers in any handoff or review-context Validation run Evidence section).

Approximate counts in pre-commit Builder claims are a defect class. They cannot be verified against the working tree at pre-commit time (the working tree carries an exact count, not an approximate one), and they propagate drift if the actual count differs from the approximation when the count changes through subsequent revisions. The cumulative-diff-stats re-derivation is run iteratively, after every path-(a) revision iteration, until the deliverable's pre-commit state is final. The Validation run Evidence section of each handoff is populated only with landed exact counts at the final pre-commit state.

The sub-rule's empirical grounding: the PR-8 cycle had three iterations of prose-arithmetic drift on the Validation run Evidence section before the gap was named in PMN-005 §4.4 and canonicalized here.

**Bidirectional sum-stability check.** Cumulative-diff-stats re-derivation triggers a bidirectional sum-stability check at three axes: per-file insertion sum equals aggregate insertion count exactly; per-file deletion sum equals aggregate deletion count exactly; per-file count equals aggregate file count exactly. Both directions are checked: aggregate decomposed against per-file sum, and per-file sum reconstructed against aggregate. Divergence at any axis at any (e.1) re-derivation iteration surfaces as a Major Builder-discovery class requiring path-(α) revision before staged-tree state is treated as authoritative.

The check applies at all staged-tree-mutating actions, including absorption operations. Codex pass absorption itself mutates the staged tree; re-derivation post-absorption is mandatory, not optional. Empirical grounding: 5+ in-cycle positives across TASK-0030 through TASK-0034 cycles; canonical text materialized at TASK-0035 (PR-52 squash `18f3b21`); 3 cross-cycle empirical positives at TASK-0036 (PR-54 squash `faa6a37`) at step-10 + step-15.X + step-15.Y staged-tree-mutating-action re-derivation surfaces. (XVII) bidirectional sum-stability is load-bearing canonical discipline; ADR-006 D3 evidence-bar 3+ threshold reached at TASK-0036 cross-cycle accumulation; promotion canonicalized at TASK-0037 (PR-56).

**File-level change-source enumeration.** At each (e.1) re-derivation, the per-file row enumerates ALL source-section contributions to the per-file delta (e.g., spec §4.1 base + step-10.X path-(α') edits + Item 14 sweep + step-12.X Codex absorption + step-15 post-PR absorption). Enumeration scope is the cumulative cycle history, not the most recent iteration only. Authoring-time enumeration discipline catches drift earlier than reactive surfacing at receiving-side.

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

#### §23.6.3. Reference-verification before spec authoring

Architect-authored deliverable specs reference specific values — line numbers, structural-element counts, convention shapes, form structures, sub-rule letter labels, version numbers, PR/TASK/PMN/ADR cross-references. Each reference is a §24.2(a) external-system-behavior assertion about a derivable value, and each is a candidate for drift between authoring time and execution time when the asserted value is not verified against actual canonical sources at authoring time.

The discipline is **reference-verification before spec authoring**: every specific reference value in the spec text is either (i) verified against actual canonical source at authoring time, or (ii) explicitly marked as deferred for Builder pre-flight (i.5) batch verification. Neither path is universally preferred; the appropriate path depends on the reference class.

**Default-path guidance by reference class.** Convention shapes and form structures (sub-shapes A and D per PMN-009 §2): verify at authoring time. These constrain the structural correctness of what the spec produces; discovering form divergence at Builder pre-flight forces spec revision before execution can begin. Architect samples the canonical priors form (e.g., `head -15 <prior-PMN-file>` for PMN form; sample two or three prior TASK handoffs for handoff frontmatter shape) and authors against verified shape.

Line-number references and structural-element counts (sub-shapes B and C per PMN-009 §2): default to deferral. These specific values may drift between authoring time and Builder execution time even within a single cycle, particularly when intervening cycles ship to main between Architect spec authoring and Builder execution. Architect marks the value as "Builder verifies at pre-flight" rather than committing to a specific count or line number; Builder pre-flight (i.5) batch substitutes the verified value at execution time.

**Sub-shape A authoring-time discipline extensions** (canonicalized at TASK-0028 / PR-37 absorbing TASK-0026 + TASK-0027 cycle-close ledger evidence):

- **Canonical-impact-surface-completeness check**: at spec-authoring time, enumerate all canonical surfaces the cycle's substantive content will touch BEFORE prescribing byte-exact edits. The enumeration scope spans (a) primary-target surface(s) named in cycle scope; (b) cross-reference surfaces consumed by primary-target (Class A canonical-version-of-record sites; ADR cross-reference enumerations; README distributed-update tables; etc.); (c) inline-mention drift candidates at operating-instruction surfaces (AGENTS.md / CLAUDE.md; equivalent receiving-side adapters). Mis-classification of a surface as "untouched" when cycle scope implies an edit reproduces the canonical-impact-surface-incompleteness defect class. Empirically grounded at 3-instance evidence base across TASK-0026 (Codex post-PR Finding 2 migration-mapping table completeness) + TASK-0027 ((i.5)(e) AGENTS/CLAUDE inline-mention drift; Codex pre-commit Finding 2 ADR-006 ADR-004 framing additive-vs-subtractive drift).

- **Template-content authoring meta-pattern**: when authoring template files (`templates/*.md` content), byte-exact canonical-form regions (frontmatter shape; canonical-regex anchors; field-semantics enumerations) are byte-exact ONLY at the canonical-form regions; surrounding explanatory prose follows ordinary spec-authoring discipline (clarity, completeness, cross-reference correctness). Conflating byte-exact-target prescription with explanatory-prose prescription produces (h.2) recurrent-defect-class signature at template-content authoring surface. Empirically grounded at TASK-0027 (h.2) intra-cycle 5-instance recurrence: template-byte-exact-regex sub-cluster (2 instances) at templates/handoff-template.md:21 R.1.1 → R.6 chain.

**Architect adjudication-framework arithmetic discipline.** At adjudication-framework surfaces (path-(a) / path-(β) routing decisions, defect-tally reconciliation, cumulative-diff-stats acceptance, cycle-close ledger arithmetic), Architect re-derives from raw evidence (`git diff --shortstat`, `git log --oneline`, direct artifact reads) rather than trusting Builder-reported per-file decompositions or inherited cycle-artifact text. Builder may have applied (e.1) sub-rule cumulative-diff-stats re-derivation correctly at its own surface; the adjudication surface is a separate verification opportunity at which Architect's own arithmetic verification provides multi-surface mitigation per §24.3 receiving-side caveat-discipline applied symmetrically.

**Standing pre-authoring data-currency precondition.** Reference-verification depends on the data sources used for verification being themselves current. For specs in this project, GitHub-integration-indexed canonical state is current to main HEAD before Step 1 of any spec authoring. Stale data sources produce systematic drift independent of the discipline above; data-currency is a precondition of the discipline operating at all.

**Provenance.** This sub-section absorbs PMN-009's recommended canonical refinement (PMN-009 §5) per PMN-005 propose-then-absorb cadence. Empirical grounding: 4 cross-cycle (i.5) confirmations through TASK-0019 + TASK-0020 (PMN-009 §1.1 data points) plus 3 in-cycle TASK-0022 confirmations including the first downstream-gate catch (Codex pre-commit) of the spec-drift class. The TASK-0022 cycle terminated at handback before absorption could land; this cycle (TASK-0023) absorbs after the empirical pattern further matured.

**Role-invariance.** Reference-verification before spec authoring discipline at §23.6.3 applies symmetrically across roles. Builder receiving-discipline at pre-flight verification batch + Codex pre-commit + post-PR review surfaces apply parallel canonical-source verification against Architect-asserted external-system state. Sweep scope is role-invariant: same defect class catchable at Architect authoring time, Builder receiving time, and Codex review time. Three-surface coverage produces independent defect-detection per PMN-008 §3.2 distinct-surfaces-catch-distinct-defects principle; role-invariance is the canonical-text framing of this composition.

Empirical grounding: 3+ cross-cycle confirmations through TASK-0032 + TASK-0033 + TASK-0034 of role-invariance pattern (each cycle's Codex pre-commit catches Architect-side authoring defects missed at Architect self-review; Builder pre-flight similarly catches authoring-side narrowness). Role-invariance framing is jointly canonicalized at this cycle with (XXIV) four-surface paired-discipline reframing per §24.4 four-surface paired-discipline composition below.

**Discipline-side fix application at status transition gates.** Builder applies path-(α') discipline-side fix at pre-merge stop-and-show staged-tree gate: handoff frontmatter `status: drafted → active` token-swap restores PMN-001 (k) Action substitution contract (Action expects `active` at merge time for `active → resolved` transition; `drafted` state would skip substitution silently). Application is mandatory at pre-merge gate independent of any other path-(a)/(α)/(α')/(β) routing decisions in the absorption iteration. Empirical grounding: 5 cross-cycle positives at TASK-0030 / 0031 / 0032 / 0033 / 0034; first-cross-cycle reach without owner prompting at TASK-0031; canonical promotion at this cycle per ADR-006 D3 evidence-bar.

## §24. Cross-surface verify-before-assert meta-pattern

This section names the cross-surface verify-before-assert meta-pattern that recurs across the framework's §-section disciplines. The pattern is: claims about external-system state (repository state, tool output, file content, collaborator output) are §24.2(a) assertions requiring verification against the asserted state at receiving time, regardless of who authored the claim or which surface the claim was authored on. Subsections enumerate the meta-pattern's sub-shapes (§24.2) and the receiving-side caveat-discipline that operationalizes the pattern at each receiving direction (§24.3).

### §24.2. Sub-shape characterization

The four pre-existing sub-shapes — (a) external-system-behavior assertion, (b) propagation-incompleteness, (c) anticipatory-state assertion, (d) cross-receiving-direction symmetry — are inherited from prior framework versions and are not modified by Part A canonicalization. Part A applications cite §24.2(a) for external-system-behavior assertion at Reviewer-output-absorption (§8.1.1.1, §8.1.1.2), Architect pre-handoff self-review (§23.6 family), and Architect ← Builder hand-back (§24.3 fifth direction below).

### §24.3. Receiving-side caveat-discipline

The receiving-side caveat-discipline operationalizes the §24 meta-pattern at each receiving direction in the cycle's communication topology. Five receiving directions are canonicalized:

- Builder pre-flight against Architect-asserted external-system state in prompts (§8.2)
- Architect pre-handoff self-review against own-authored claims (§23.6, §23.6.1, §23.6.2, §23.6.3)
- Builder receiving Reviewer findings (§8.1.1, §8.1.1.1, §8.1.1.2)
- Owner receiving Builder stop-and-show (§8.3)
- Architect ← Builder hand-back (§24.3.1 below)

#### §24.3.1. Architect ← Builder hand-back symmetric-application clause

The §24.3 receiving-side caveat-discipline applies bidirectionally. The four pre-existing receiving directions cover Builder, Architect (own-authored), Builder (Reviewer-emitted), and owner. A fifth receiving direction is added by symmetric-application clause: **Architect ← Builder hand-back.**

When Builder hands back to Architect at cycle close, the hand-back contains claims about external-system state — Reviewer output observed, branch state, gh CLI output, file content matching prescription, phantom-action absence. Architect treats those claims as §24.2(a) assertions requiring verification before sign-off, not just receipts to acknowledge. The mechanism is parallel to §8.2 Builder-side pre-flight discipline against Architect-asserted external-system state in prompts: same §24 mechanism, opposite receiving direction. Both are §24.2(a) verify-before-assert applications at receiving-side; the symmetry is structural, not coincidental.

**Default Architect-side post-handback five-point check pattern.** Where verification is cheap (a handful of API calls, a few git commands), Architect runs the five-point check against the hand-back claims:

1. **Three-endpoint poll of Reviewer output** (per §8.1.1.1) — confirm Reviewer output as Builder reported it; reconcile against last-known-state via all three endpoints (formal-review, issue-comment, line-comment).
2. **Branch tip-SHA verification** — `git rev-parse HEAD` output must match the expected SHA from the prior session's hand-back; additionally `git status --porcelain` must be empty (clean working tree). The `git status` clean-tree check is necessary-but-not-sufficient on its own — SHA equality is the load-bearing tip-state proof, with clean-tree as adjunct check; `git status` alone reports working-tree state and ahead/behind upstream but does not prove HEAD equals an expected SHA.
3. **File content audit against prescription** — for each file Builder claims to have authored or modified, verify content matches the spec's §2 prescription. `git show <sha>:<path>` or equivalent.
4. **Phantom-action audit** — verify no claimed action lacks corresponding repository state (commits exist; files exist; counts match). Inverse of §8.1.1.2 sub-shape A check applied to Builder hand-back.
5. **Comment-content claim verification** (per §8.1.1.2) — for any Reviewer comment Builder reports as adjudicated, verify the comment's substantive content claims against actual repository state, not just delivery.

A project may codify a project-specific check pattern in repo-local Architect reference per §23.5 inherited owner preferences. The five-point pattern is the default; project-specific deviations are documented at the project level.

**Provenance.** This clause was pre-flagged at PMN-003 (g) as deferred to v3 substantive content authoring. The four-point check pattern (PMN-003 (g)) extended to five-point in PMN-005 §2.5 in light of the reviewer-claimed-effects-don't-land defect class. §24.3.1 canonicalizes the five-point pattern.

**(XXVI) Two-gate application surface clause.** The default five-point check pattern above applies at two distinct ratification surfaces in the cycle protocol — Gate A (staged-tree pre-commit state; applied at post-step-12.X (e.1) re-derivation hand-back, pre-step-13 commit) and Gate B (origin/<branch> post-push state; applied at post-commit / post-push hand-back, pre-owner-merge). Both gates apply the full five-point spirit; surface-specific Point-2 mechanism adaptation applies at Gate A because HEAD references the prior commit at staged-tree state, rendering the base-form HEAD-SHA + clean-tree check operationally inapplicable as a tip-state proof.

**Gate A surface-adapted Point 2 — staged-tree-content parity verification.** At Gate A's pre-commit surface, replace the base-form Point 2 (HEAD-SHA + clean-tree) with: `git diff --staged --shortstat origin/main` parity against the re-derived (e.1) expected delta with (XVII) bidirectional sum-stability check at all three axes (insertions / deletions / file-count); per-file `git diff --staged --numstat origin/main` parity against per-file row enumeration. Staged-tree-content parity is the load-bearing tip-state proof at Gate A surface; the base-form clean-tree adjunct check is inapplicable at Gate A because staged edits intentionally make the working tree non-clean against HEAD.

**Gate B Point 2 — base-form branch tip-SHA verification.** At Gate B's post-push surface, the base-form Point 2 applies as written: `git rev-parse origin/<branch>` SHA equality with the Builder hand-back expected SHA, plus `git status --porcelain` clean-tree adjunct check. HEAD on origin/<branch> equals the expected post-commit SHA at this surface; the base-form Point-2 mechanism is operationally correct without adaptation.

**Points 1, 3, 4, 5 at both gates.** Points 1 (three-endpoint poll), 3 (file content audit), 4 (phantom-action audit), and 5 (comment-content claim verification) apply at both gates per the base-form pattern above; mechanism selection (staged content via `git show :<path>` at Gate A; committed content via `git show <sha>:<path>` at Gate B) follows from the gate surface and does not require canonical adaptation.

**Application protocol.** Gate A and Gate B are sequential ratification surfaces in the cycle protocol — Gate A precedes commit (step-12.X / step-13 boundary); Gate B follows push (step-16.X / step-17 boundary). Both gates apply at each cycle; Point-2 mechanism selection is determined by which surface the hand-back is being received at, not optional. Empirical canonicalization grounded at TASK-0035 Codex pass-7 Finding H + (XXIV.n) canonical-mechanism-vs-surface-applicability sub-shape; reinforced by 4 cross-cycle empirical positives at TASK-0036 (PR-54 squash `faa6a37`) — Gate A staged-tree-content parity at step-12.X; Gate B base-form at step-16/16.X with re-application at iterative-absorption SHAs step-15.X + step-15.Y. (XXVI) two-gate application surface clause is load-bearing canonical discipline; ADR-006 D3 evidence-bar 3+ threshold reached at TASK-0036 cross-cycle accumulation; promotion canonicalized at TASK-0037 (PR-56).

### §24.4. Four-surface paired-discipline composition

The receiving-side caveat-discipline at §24.3 enumerates five receiving directions independently. Empirical cross-cycle observation surfaces a compositional layer: paired-discipline operates across four sequential surfaces in a cycle's authoring → execution chain, with same defect class catchable at distinct surfaces per PMN-008 §3.2 distinct-surfaces-catch-distinct-defects principle. The four surfaces are:

1. **Authoring (Architect-side)** — §23.6.3 reference-verification before spec authoring; canonical-source verification of all external references at spec-authoring time per role-invariance discipline at §23.6.3 above.
2. **Receiving (Builder-side)** — Builder pre-flight verification batch + §8.2 (forthcoming at Part C+) caveat-discipline against Architect-asserted external-system state in prompts; canonical-source verification at receiving surface independent of authoring-side verification.
3. **Ratification (Architect-side, successor or session-spanning)** — §24.3.1 Architect post-handback five-point check applied at hand-back surface; canonical-source verification of Builder-asserted external-system state in hand-back claims independent of receiving-side verification.
4. **Post-PR review (Codex-side)** — Reviewer post-PR review per §8.1.1.1 three-endpoint poll + §8.1.1.2 phantom-action verification; canonical-source verification at independent Reviewer surface independent of authoring + receiving + ratification surfaces.

The four-surface paired-discipline is empirically more robust than three-surface composition (authoring + receiving + ratification) when ratification surface is degraded (e.g., `project_knowledge_search` sync-lag per PMN-012 §3.4 (XXI) carry-forward observation). Post-PR Codex review surface provides redundant canonical-source verification anchor when ratification-time `project_knowledge_search` is sync-lagged.

Empirical grounding: TASK-0033 cycle (5 in-cycle (XXIV)-class instances caught across all 4 surfaces); TASK-0034 cycle (6 in-cycle (XXIV)-class instances; ratification-turn (XXIV.g) sub-shape application at successor Architect surface caught predecessor adjudication-turn schema-count narrowness, demonstrating inverse-surface paired-discipline functional even under acceleration pattern); cross-cycle pattern continues across TASK-0033 + TASK-0034 despite PMN-011 §2.4 promotion at TASK-0033 of refinement candidate as currently formulated (canonical-source enumeration only sub-shape; emergent sub-shapes (XXIV.b)-(XXIV.i) catalogued at PMN-011 + PMN-012). Promotion candidacy at TASK-0035 jointly canonicalizes paired-discipline composition framing at §24.4 + role-invariance discipline at §23.6.3 above.

### §24.5. Multi-surface review pipeline as load-bearing safety-net

At canonical-text amendment cycles, the within-cycle review pipeline composes six surfaces sequentially as a load-bearing safety-net. Each surface has characteristic defect-class coverage per PMN-008 §3.2 distinct-surfaces-catch-distinct-defects principle; no single surface is self-sufficient; composition of coverage across surfaces produces empirical defect-detection robustness beyond any single-surface discipline.

**The six surfaces:**

1. **Architect spec authoring** — pre-edit verification per §23.6.3 reference-verification before spec authoring + per-edit (XXIV.a-n) catalog-application at canonical-text + verification-command-prescription authoring surfaces.
2. **Builder pre-flight (i.5)(c)** — independent canonical-source direct enumeration (e.g., grep at canonical surfaces without character-class restriction; arithmetic-verification by enumeration at count-bearing claims) AS WELL AS spec-prescribed verification commands; catches Architect-side authoring narrowness at receiving surface.
3. **Builder canonical-text authoring** — §23.6.2 iterative-to-fixed-point self-review with (j) all-instances sweep applied at every iteration + measure-before-assert pattern at staged-tree-state assertions.
4. **Codex pre-commit pass-1** — independent reviewer surface at staged-tree state; includes (XIV) sweep-scope completeness verification at substantive content sections (e.g., enumeration paragraph internal consistency: preamble + tail + span endpoint + count parallel-claim concordance).
5. **Codex post-PR pass-1 through pass-N** — independent reviewer surface at post-push state; iterative-catch reach extends as pass-N+1 catches pass-N narrowness at increasing depth at handoff body durable-state + cycle-artifact cross-reference + review-context parallel staged-tree-state assertions.
6. **Builder receiving (XIV) sweep at absorption** — comprehensive sweep-scope completeness application at each Codex pass absorption per role-invariance discipline at §23.6.3 above.

**Iterative-catch reach pattern.** Pass-N+1 catches pass-N narrowness at increasing depth. Bounded-iteration fixed-point convergence at handoff-currency narrowness class typically converges at reach 3-4 rather than reach 1; §8.1.1.3 cost-class refinement one-iteration assumption applies at pure-token-swap class but does not generalize to handoff body durable-state (XIV) sweep narrowness class. Stop-Iteration framework at reach 4+ canonical boundary provides unconditional termination per Architect adjudication; pre-commitment to Stop-Iteration at reach 4+ is standard cycle-protocol baseline.

**Defense-in-depth pairing.** §24.5 multi-surface review pipeline pairs with §23.6.3 catalog-application-at-authoring-surface discipline (authoring-time verification at surface 1) + §24.4 four-surface paired-discipline composition (cross-cycle paired-discipline across the authoring → execution chain). Authoring-time verification + multi-surface within-cycle pipeline + cross-cycle paired-discipline composition together provide the defense-in-depth that single-surface discipline cannot achieve. Each layer addresses defect classes that escape adjacent layers; the layers are complementary, not redundant.

**Application protocol.** All six surfaces apply at each canonical-text amendment cycle. Surface skipping is not optional; surface degradation at any layer (e.g., `project_knowledge_search` sync-lag at Architect ratification surface; settling-period premature-clean assertion at Codex post-PR surface) increases load on adjacent surfaces. Empirical observation at canonical-text amendment cycles: iterative-catch reach 3-4 is normal rather than pathological; multi-surface pipeline empirically catches what single-surface discipline iteratively misses.

Empirical canonicalization grounded at TASK-0035 (Codex passes 1-7 + Stop-Iteration trigger at reach 8 with (XXIV.j/k/l/m/n) NEW catalog content emerging at iterative surfaces 4-7) + TASK-0036 (§6.6 refinement candidate articulation at PMN-013 §6.6 + cycle-close ledger entry (XXIII) empirical reinforcement at every (XIV) sweep authoring surface) + TASK-0037 (1st in-cycle catch via the proposed canonical mechanism: Builder pre-flight (i.5)(c)4 caught Architect spec authoring (XXIV.a)/(XXIV.e) narrowness; 4 post-PR Codex passes caught handoff body durable-state narrowness at increasing iterative depth; Stop-Iteration trigger at reach 4 canonical boundary per pre-commitment). ADR-006 D3 evidence-bar 3+ threshold reached at cross-cycle accumulation; promotion canonicalized at TASK-0038 (PR-58).

### §24.6. Stop-Iteration framework as load-bearing reach-4+ canonical boundary discipline

At canonical-text amendment cycles, when iterative-catch reach at the post-PR Codex review pipeline reaches 4 or more passes with same-class defect-pattern recurrence at handoff body durable-state or cycle-artifact cross-reference surfaces, the Stop-Iteration framework activates unconditionally per Architect pre-commitment. The framework provides bargaining-mechanism guard against iterative-catch saturation where each additional pass surfaces "this one is just a simple fix" reasoning that defeats the canonical-boundary discipline.

**Condition (A) — iterative-catch sweep extension halt.** At reach 4+ canonical boundary, iterative-catch sweep extension halts unconditionally. No additional Codex pass invocation by owner per ADR-001 D11; no expanded (XIV) sweep at the absorption surface; no adjacent-surface enumeration beyond surfaces named by the surfacing Codex finding. Codex-side spontaneous re-reviews after subsequent commit push may still fire autonomously per cross-cycle empirical cadence (~7-15 min post-push); residuals at such spontaneous re-reviews are routed per condition (B) below per residual operational-correctness-impact assessment. Condition (A) is load-bearing for anti-bargaining-mechanism integrity: removing the escape-hatch surface that permits "this finding is just pure-token-swap per §8.1.1.3, so we can fix it in-cycle without violating Stop-Iteration" reasoning. The §8.1.1.3 cost-class convention is real, but using it as the operational-correctness escape hatch at reach 4+ canonical boundary defeats the canonicalization integrity per PMN-013 §5.3 mechanism rationale.

**Condition (B) — residual handling routing.** Findings surfacing at the Stop-Iteration trigger pass are routed by residual class:

(B.i) **Documentary residuals** (handoff body or cycle-artifact assertions that are accurate historical record at the prior staged-tree state but stale relative to current post-absorption staged-tree state; review-context body fields citing pre-fix arithmetic; PMN deferred-work register entries pointing at future-cycle planning that does not affect current-cycle correctness) are accepted at merge with explicit cycle-close ledger entry disclosure noting the residual + the surface + the reason for non-fix. Documentary residuals do not affect post-merge operational correctness of canonical text or PMN-001 (k) Action substitution contract.

(B.ii) **Operationally-hazardous residuals** (handoff §1 Current state Summary serving as durable resume artifact for next-cycle bootstrap; PMN deferred-work register entries serving as TASK-NNNN+ planning input where staleness would mislead next-cycle Architect spec authoring; canonical-text content with operational reference; verification-command prescription that fails on current canonical state) receive **targeted surgical fix at exact named surfaces only**. No expanded (XIV) sweep at the absorption surface; no adjacent-surface enumeration; no propagation discovery beyond the operational hazard named in the surfacing Codex finding. Any further residual surfacing at the Codex pass immediately following surgical fix (typically pass-N+1 spontaneous re-review) is accepted at merge per strict framework adherence — operationally-hazardous residuals at named surfaces are resolved; further findings are by framework definition not operationally hazardous at this cycle's canonical-text or PMN-001 (k) substitution contract surfaces.

**Cycle-close ledger override-signal disclosure.** When condition (B.ii) targeted surgical fix is applied or condition (B.i) accepted-residual-at-merge framing is invoked, the handoff §10 cycle-close ledger receives an explicit override-signal entry naming: (1) the Stop-Iteration trigger pass + reach + sub-shape; (2) the condition invoked (B.i documentary or B.ii operationally-hazardous); (3) for B.ii, the named surfaces receiving surgical fix; (4) any accepted residuals at merge per strict framework adherence. The override-signal disclosure preserves audit trail at the cycle artifact authoritative for next-cycle Architect bootstrap.

**Documentary-vs-operationally-hazardous residual distinction.** The distinction is not pure-token-swap-vs-substantive (which §8.1.1.3 cost-class refinement governs); the distinction is operational-correctness-impact at downstream cycle consumption. A pure-token-swap residual at a handoff §1 Summary line is operationally hazardous (next-cycle Architect reads §1 Summary for resume bootstrap; stale §1 Summary causes spec authoring drift). A substantive prose-rewrite residual at a PMN narrative paragraph documenting historical empirical observation is documentary (future operators consulting PMN read narrative as historical record; staleness is acceptable historical archive form). Architect adjudicates routing at Stop-Iteration trigger surface per residual operational-correctness-impact assessment.

**Application protocol.** Stop-Iteration framework applies unconditionally at all canonical-text amendment cycles at reach 4+ canonical boundary measured by post-PR Codex pass count from pass-1 (e.g., reach 4 = pass-4 fires at iterative-catch). Framework pre-commitment is standard cycle-protocol baseline at every canonical-text amendment cycle Phase 1 ratification (Adj 12 inheritance pattern across TASK-0035 + TASK-0036 + TASK-0037 + TASK-0038 + TASK-0039+). Re-scoping at reach 4+ routes accepted residuals to PMN-001 (k) auto-fire chore-fix-up scope or next-cycle bootstrap rather than in-cycle absorption iteration extension.

**Cross-discipline composition.** §24.6 Stop-Iteration framework composes with §24.5 multi-surface review pipeline (load-bearing safety-net providing the iterative-catch infrastructure that Stop-Iteration framework terminates) + §23.6.3 reference-verification + role-invariance discipline (operative at surfaces 1 + 6 of §24.5 pipeline) + §8.1.1.3 cost-class refinement (one-iteration assumption at pure-token-swap class applies pre-reach-4; reach 4+ canonical boundary overrides at iterative-catch saturation per PMN-013 §6.2 reach-signal observation) + §24.3.1 Gate A + Gate B (post-Stop-Iteration trigger Gate B re-application required at post-surgical-fix or accept-residual SHA).

Empirical canonicalization grounded at TASK-0035 step-15.Z3 (Codex pass-8 surfaced Finding I (XXIV.l) operationally load-bearing defect at shipped canonical; Architect honored Stop-Iteration + routed to PR-53 chore-fix-up per (XXIX) precedent — empirical positive #1 under operational-correctness stress test per PMN-013 §5.2) + TASK-0037 (pass-4 reach-4 canonical boundary fire; (XXIV.d) same-class recurrence at handoff body durable-state; accept-residual-at-merge per pre-commitment — empirical positive #2 per PMN-014 §5.1 carry-forward record) + TASK-0038 (pass-4 reach-4 canonical boundary fire with condition (B) refined application distinguishing documentary vs operationally-hazardous residuals; targeted surgical fix applied at step-15.Z' to exact named operationally-hazardous surfaces; cycle merged at PR-58 squash 369586f — empirical positive #3 with condition (B) refinement empirically grounded per PMN-015 §8 canonicalization-promotion candidates listing + TASK-0038 handoff §1 Current state record + §3 step-15.Z entries). ADR-006 D3 evidence-bar 3+ threshold reached at cross-cycle accumulation; promotion canonicalized at TASK-0039 (PR-60). Cross-domain corroboration at `bryce-murphy/employee-churn` TASK-0003 PR #10 Recommendation 10 (reviewer re-review saturation protocol) per PMN-016 §2.5 cross-domain empirical record sub-section.
