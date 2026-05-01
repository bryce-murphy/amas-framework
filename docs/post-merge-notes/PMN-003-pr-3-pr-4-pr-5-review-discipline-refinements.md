# PMN-003 — PR-3 + PR-4 + PR-5 review-discipline refinements

## Metadata

- PMN ID: PMN-003
- Source PRs: PR-3 (TASK-0003), PR-4 (TASK-0004), PR-5 (TASK-0005)
- Author surface: Architect (Claude Opus 4.7, Claude.ai Project)
- Date authored: 2026-05-01
- Linked records: ADR-001, ADR-002, PMN-001, PMN-002, TASK-0003, TASK-0004, TASK-0005
- Framework version dogfooded: AMAS v2.14.1
- Production target: AMAS v3.0

---

## Trigger basis

Three of §18's five trigger categories apply:

- **Workflow change** — observations refine receiving-side discipline at three surfaces (Reviewer-output absorption, Builder verification, Architect hand-back receipt) in ways that change how the Builder/Reviewer/Architect loop operates on this repo. The §24.3 symmetric-application clause (observation (g)) extends the cross-surface meta-pattern to a fifth receiving direction (Architect ← Builder hand-back), which is a workflow-shape change.
- **Unexpected review friction** — five of seven observations originated as review-cycle surprises: PR-3 auto-fire phantom-action narratives ((b)), PR-4 missed line-level findings via single-endpoint check ((e)), PR-4 stale parenthetical placeholders in committed handoff metadata ((d)), PR-4 silent heading drop in Edit operation ((f)), PR-5 fast-response issue-level "Approve" stub misread as substantive verdict ((c) anti-channel). PMN-002 already named some of the PR-3 cycle friction; PMN-003 extends with PR-4 and PR-5 evidence and refines the framing.
- **Architecture change** — observation (g) motivates a §24.3 mechanism extension in v3 `core.md` (symmetric receiving-side caveat-discipline), which is durable system shape touching the canonical text. ADR-002 (v2.14.1-tracked at this project) formalized the TASK reservation amendment; PMN-003 (g) is the framework-shaping observation that motivates the §24.3 extension at v3 authoring time.

The remaining two §18 categories — tool-assignment change, validation-strategy change — do not apply to PR-3 / PR-4 / PR-5.

---

## Retroactive-backfill consideration

PMN-001 was the project's first PMN and addressed retroactive-backfill for PR-1 + PR-2 explicitly. PMN-002 covered PR-3 cycle learnings as authored at the time. PMN-003 covers PR-3 + PR-4 + PR-5 review-discipline refinements as a unified cluster — PR-3 and PR-4 evidence carries forward from the prior chat-context running list (recovered into this canonical PMN); PR-5 evidence is fresh and authored at-cycle. No prior session content is unrecovered. The convention is now fully PMN-fileform-tracked from PR-1 forward; this note records that the backfill question is closed at PMN-003 authoring time.

---

## Observations

The seven observations cluster into three groups by which surface's receiving-side discipline they refine. Field evidence draws on PR-3, PR-4, AND PR-5 cycles. Observations that originated in PR-3 or PR-4 cycles are refined by TASK-0005 (PR-5) cycle field evidence; refinements update wording within existing observations rather than spawning new categories.

### Cluster 1 — Reviewer-surface friction at Codex

**(a) Verification-prompt source-of-truth drift from PMN body content within the same cycle's artifacts.**

PR-4 cycle. The PMN-002 body documented two Codex post-PR comments. The verification prompt's source-of-truth context section conflated owner-trigger timing with Codex output sequence and named three timestamps. Codex pre-commit review caught it via claim-verification-only output as a Minor finding. Architect adjudicated path (b); PMN-002 body was correct, the verification prompt was the artifact in error.

This is a §24.2(b) propagation-incompleteness sub-shape between two recapitulation locations within the same PMN cycle's artifacts (the PMN body and an accompanying verification prompt). Field evidence reinforcement of existing canonical text — not a new sub-shape, an instance of the existing one operating within a single cycle's deliverable set.

**TASK-0005 cycle field-evidence refinement candidate folded into structural fix:** the in-cycle path-(a) revision adding `## Alternatives considered` to ADR-002 propagated to the handoff's `## Decisions made` mention but not to the handoff's earlier line saying ADR-002 "omits" the section. §23.6 recapitulation-consistency check at handoff-issue time was clean; the propagation gap opened DURING in-cycle revision. Re-running §23.6 recapitulation-consistency after in-cycle revisions was not part of the discipline. Codex post-PR review caught it; path-(a) fix-up resolved.

**Structural fix (usage-guide-level):** v3 `usage-guide.md` Architect §23.6 self-review checklist gains two items:
1. Verify recapitulation-location consistency between PMN body and any verification prompts referencing it within the same cycle.
2. Re-run recapitulation-consistency check after any in-cycle path-(a) revision that touches asserted facts in multiple artifacts (e.g., ADR + handoff + review-context).

No new mechanism; tightening of the §23.6 sweep scope and trigger conditions.

**(b) §8.1.1.1 + §8.1.1.2 co-occurrence is a conditional Codex behavior, not a guaranteed channel.**

PR-3 and PR-4 both exhibited identical pattern: Codex auto-fire on PR open producing phantom-action narrative ("I committed X," "I created file Y") accompanied by ✅ "Tested" markers, with permalink-self-contradiction (Codex's own permalinks resolve against actual branch HEAD, not the claimed-commit SHA in the narrative). Substantive verdict only on explicit `@codex review` trigger. Two-cycle evidence base (PR-3, PR-4) initially supported "systemic pattern" framing in chat-context running discussion.

**TASK-0005 cycle field-evidence refinement:** PR-5 produced **NO PR-open auto-fire**. The 44-second window between PR-open (20:25:23Z) and explicit `@codex review` trigger (20:26:07Z) carried no auto-fire event; the first Codex event was `subscribed` at 20:26:09Z, two seconds after the explicit trigger comment.

Three-cycle evidence base (PR-3 auto-fire present, PR-4 auto-fire present, PR-5 auto-fire absent) qualifies the original "systemic pattern" framing: Codex auto-fire is **conditional, not unconditional**. Possible explanations include suppression by a quick explicit trigger, latency exceeding the 44-second window so the explicit trigger preempted, or conditional Codex configuration. The exact mechanism is below the threshold for investigation; the framework-shaping conclusion is that absence of auto-fire is not evidence of review failure.

**Structural fix (usage-guide-level):** v3 `usage-guide.md` Reviewer-output absorption section frames Codex auto-fire on PR open as a **conditional supplemental pattern, not a guaranteed channel**. When auto-fire occurs (PR-3, PR-4 evidence), it routinely produces phantom-action narratives with falsifiable commit claims; treat as standard sentinel signal per §8.1.1.1 and apply Builder claim-category verification per §8.1.1.2 (now codified at v2.14). When auto-fire does not occur (PR-5 evidence), absence does not indicate review failure — the explicit `@codex review` trigger is the reliable substantive-verdict path. Receiving-side discipline does not depend on auto-fire occurring.

Field-evidence basis: PR-3, PR-4, PR-5 cycles.

**(c) Codex substantive-verdict signal channels are inconsistent across cycles, plus an anti-channel.**

Original framing from PR-3 + PR-4 evidence named three potential substantive-verdict no-findings channels: (i) explicit text in COMMENTED body, (ii) COMMENTED state + boilerplate-only body + no suggestion comments (the "no comment ≠ no review" pattern), (iii) 👍 reaction (named by Codex's own boilerplate as resolution semantics, not observed in PR-3 or PR-4 evidence at this project).

**TASK-0005 cycle field-evidence refinement:** PR-5 surfaced a fourth pattern that is **NOT** a substantive verdict.

In PR-5, the first Codex event after the explicit `@codex review` trigger was an issue-level "Approve, 0 findings" stub from `chatgpt-codex-connector`, posted ~24 seconds after the trigger. This was Signal 1. Signal 2 was the formal Pull Request Review (COMMENTED state, boilerplate-only body, attached to the actual head commit) ~2.5 minutes later. Signal 3 was a P2 line-level review comment posted alongside Signal 2.

Builder initially treated Signal 1 as the substantive verdict and asserted "Codex approved with 0 findings via different channel." Owner flagged that the actual review was still in flight; Builder retracted. The actual review arrived via Signals 2 and 3 and contained one P2 finding requiring fix-up.

Channel (iv) — issue-level Codex comments posted to the PR's discussion thread — is therefore an **anti-channel**: looks like a verdict, isn't one. Substantive verdict at this project comes only via the formal Pull Request Review endpoints (`gh pr view --json reviews` for review state; `gh api repos/<owner>/<repo>/pulls/<N>/comments` for line-level comments). Issue-level Codex comments on the PR thread are non-authoritative regardless of phrasing.

**Structural fix (usage-guide-level):** v3 `usage-guide.md` Reviewer-output absorption section codifies:
- **Two observed substantive-verdict channels** in this project's evidence base: (i) explicit text in COMMENTED body (PR-3), (ii) COMMENTED state + boilerplate-only body + no suggestion comments (PR-4). Receiving-side discipline must accommodate "no comment ≠ no review" — COMMENTED state with boilerplate-only body IS the verdict when no suggestion comments follow.
- **Future-instance candidate** named by Codex's own boilerplate, not yet observed at this project: 👍 reaction. Treated as future-instance candidate per §18 monitoring; promote when first instance observed.
- **Anti-channel:** issue-level Codex comments (on the PR's discussion thread, distinct from formal review endpoints) are non-authoritative for substantive verdict regardless of phrasing. Only formal endpoints — Pull Request Reviews (`gh pr view --json reviews`) and line-level review comments (`gh api repos/<owner>/<repo>/pulls/<N>/comments`) — are authoritative (PR-5 evidence).

### Cluster 2 — Builder-side verification discipline refinements

**(d) Placeholder-substitution audit must extend to all committed artifacts, not just PR-body placeholders.**

PR-4 cycle. PMN-002 (e) framed the discipline around `(Builder fills with X)` placeholders in the PR body since that's where PR-3's friction occurred. PR-4 exposed the same failure mode in handoff metadata: an Architect-prescribed parenthetical `(Builder updates with HH:MM at handoff creation)` was preserved verbatim into the committed handoff file because the step-8 placeholder-substitution audit didn't enumerate file-content placeholders. Codex line-level review caught it post-creation; Builder fix-up cycle resolved at SHA `6779529`.

**TASK-0005 cycle confirming evidence (working-as-designed):** the §5 placeholder-substitution audit ran cleanly with all 12 commit-time substitutions enumerated and 2 deferred sections (Post-PR review state, Sign-off) explicitly named. Builder also self-caught two missed `TBD` placeholders in the review-context status block before the §5 audit stop-and-show — i.e., the audit step itself trapped what an earlier substitution sweep missed. PMN-003 (d) discipline working as designed when the audit covers all artifacts.

**Structural fix (usage-guide + §23.2-level, extending PMN-002 (e)):** v3 `usage-guide.md` Architect-prompt-construction discipline directs that when prompts contain `(Builder ... with X)` placeholder patterns, the prompt enumerate ALL such patterns across ALL artifacts to be committed — handoff files, review-context files, PR body, commit messages — not just remote-visible PR body. The placeholder-substitution audit step in v3 §23.2's mechanical-sequence guidance binds to **"before any committed artifact reaches the index"**, not just **"before remote-visible action."** Lands as an explicit all-artifact enumeration requirement in receiving-side stop-and-show templates.

**(e) Builder review-state assertions about "no findings" require BOTH API endpoints AND non-premature polling. Single-endpoint check OR single-poll is §24.2(a) external-system-behavior assertion failure.**

PR-4 cycle. Builder asserted "post-PR Codex review is COMMENTED state with boilerplate-only body and no findings" based on `gh pr view --json reviews` rollup. That endpoint does not surface line-level review comments. Two P3 line-level review comments were missed; required `gh api repos/<owner>/<repo>/pulls/<N>/comments` to discover. §24.2(a) failure on the asserting side; receiving surface (Architect) caught only because Architect re-checked.

**TASK-0005 cycle field-evidence refinement:** single-poll across both endpoints is also a failure mode. PR-5 Builder polled both endpoints once shortly after the explicit `@codex review` trigger (when only Signal 1 fast-response stub had landed), saw both formal endpoints empty, and asserted "no findings via different channel." Premature reading. The actual review landed ~2 minutes later via both formal endpoints with a P2 finding.

**Structural fix (usage-guide + §23.2-level):** v3 `usage-guide.md` Builder-side Reviewer-output verification discipline — review-state assertions about "no findings" must:
1. Check **BOTH** endpoints: `gh pr view --json reviews` (substantive review state) AND `gh api repos/<owner>/<repo>/pulls/<N>/comments` (line-level review comments).
2. **Re-poll, don't single-poll.** After `@codex review` trigger, do not assert "no findings" until either at least one formal endpoint returns non-empty content, OR a settling period (5–10 minutes) has elapsed with all endpoints stable empty.

Single-endpoint check OR single-poll is §24.2(a) external-system-behavior assertion failure. Lands as explicit two-endpoint check + re-poll-or-settling-period requirement in receiving-side review-state verification template.

**(f) Edit-time partial-section replacement can silently drop section headings.**

PR-4 cycle. Builder's path-(b) fix-up at step 7 used Edit's `old_string` containing `## Adjudication / fix-up\n\n**Path taken: escalation...` and `new_string` starting `**Path taken: (b)...`, which dropped the `##` heading. The diff was visible in Edit's response but not noticed. Codex line-level review caught the resulting broken cross-reference; Builder fix-up cycle resolved.

**TASK-0005 cycle confirming evidence (working-as-designed):** three Edit operations against content adjacent to `##` headings during the cycle; post-edit Read-verify confirmed all surrounding headings preserved in each case. PMN-003 (f) discipline working as designed when applied.

**Structural fix (usage-guide-level):** v3 `usage-guide.md` Builder-side editing discipline — when an Edit's `old_string` includes structural headings (any `##` or higher heading), verify the `new_string` preserves them, or post-edit Read-verify the file. Tooling-shaped observation but framework-discipline relevance: post-edit Read-verify is a §24-flavored receiving-side caveat-discipline applied to the asserting-side surface (Edit's effect) before downstream action takes the Edit's claimed result as authoritative.

### Cluster 3 — Architect-side discipline refinements

**(g) Architect-side §24.2(a) caveat-discipline applies symmetrically to Builder hand-back claims about external-system state.**

PR-4 cycle. Architect signed off on merge-readiness based on Builder's hand-back claim that "post-PR Codex review is clean (COMMENTED with no findings)." Builder's underlying verification was incomplete (single-endpoint check per (e)); the missed line-level findings cascaded into the merge-readiness sign-off.

Framework canonical text (AMAS v2.14.1 §24) codifies §24.2(a) as Architect-asserts → Builder-verifies (Architect prompt makes external-system claims; Builder pre-flight catches via §8.2). PR-4 surfaces the inverse direction: **Builder-asserts → Architect-receives**. The Architect-side caveat-discipline applies symmetrically — Architect treats Builder hand-back claims about external-system state (Reviewer output, repo state, gh CLI output, etc.) as §24.2(a) assertions requiring receiving-side verification before sign-off, not just receipts to acknowledge.

**TASK-0005 cycle confirming evidence (working-as-designed and load-bearing):** Architect ran a four-point verification before sign-off (PR comments via both endpoints, branch state, file content against prescriptions, phantom-action audit). The path-(a) fix-up cycle was triggered by exactly this discipline catching the line-43 stale text via the "actual file content against prescription" leg of the four-point check. (g) discipline both working as designed and **load-bearing** — without it, the line-43 staleness would have shipped into merge.

**Structural fix (most framework-shaping of the three; spans both core.md and usage-guide):**

- **v3 `core.md` §24.3 (Receiving-side caveat-discipline)** gains an explicit symmetric-application clause: "The receiving-side caveat-discipline applies bidirectionally. Architect receiving Builder hand-back claims about external-system state (Reviewer output, repo state, gh CLI output, file content against prescription, etc.) treats those claims as §24.2(a) assertions requiring verification before sign-off, not just receipts to acknowledge. The mechanism is parallel to existing §8.2 Builder-side pre-flight discipline against Architect-asserted external-system state in prompts — same §24 mechanism, opposite receiving direction."

- **v3 `usage-guide.md`** Architect-side discipline section: when Builder hand-back asserts external-system state (Reviewer findings status, branch state, file content matching prescription), Architect cross-references against the artifact (PR comments via both endpoints, `git status` output, file content) before sign-off where verification is cheap. Concrete four-point check pattern (PR comments via both endpoints, branch state, file content against prescription, phantom-action audit) recommended as default; project may codify a project-specific check pattern in repo-local Architect reference per §23.5 inherited owner preferences.

**Open placement question for v3 authoring (informational, not for PMN-003 to resolve):** the four existing §24.3 receiving directions in v2.14.1 each have core-doc surface-specific anchors (§8.2 Builder pre-flight, §23.6 Architect pre-handoff self-review, §8.1.1 / §8.1.1.1 / §8.1.1.2 Builder receiving Reviewer findings, §8.3 owner receiving Builder stop-and-show). Observation (g) introduces a fifth direction (Architect receiving Builder hand-back) whose mechanical discipline is currently scoped to the v3 usage-guide. Whether v3 adds a fifth core-doc surface-specific section parallel to §8.2 is a v3-authoring placement question to be decided at PR-7 / PR-8 (the substantive v3 content authoring PRs), not at PMN-003 authoring. PMN-003 records the question informationally so it surfaces at v3-authoring time.

---

## Action items / Structural-fix recommendations

PR-7 onward content authoring (substantive v3 canonical text) absorbs three structural-fix recommendations:

1. **Reviewer-output absorption refinements (usage-guide-level).** Maps to observations (a), (b), (c).
   - Two observed substantive-verdict signal channels named (per (c) (i) and (ii)).
   - 👍 reaction named as Codex-boilerplate-asserted future-instance candidate, not yet observed at this project (per (c) (iii)).
   - Issue-level Codex comments named as anti-channel — non-authoritative for substantive verdict regardless of phrasing (per (c) (iv)).
   - Codex auto-fire framed as conditional supplemental pattern, not guaranteed channel; absence not evidence of review failure (per (b)).
   - §23.6 self-review checklist gains: (i) recapitulation-location consistency between PMN body and verification prompts within same cycle, (ii) re-run recapitulation check after in-cycle path-(a) revisions touching multiple artifacts (per (a)).
   - **Owner:** v3 PR-7 / PR-8 / PR-9 Architect (substantive v3 content authoring sequence).

2. **Builder-side verification discipline expansions (usage-guide + §23.2-level).** Maps to observations (d), (e), (f).
   - Placeholder-substitution audit scope extended to ALL committed artifacts (handoff, review-context, PR body, commit messages), not just PR body (per (d)).
   - Two-endpoint review-state check + re-poll-or-settling-period discipline codified for "no findings" assertions (per (e)).
   - Post-edit heading-preservation Read-verify named as required Builder discipline when Edit's `old_string` includes `##` or higher heading (per (f)).
   - **Owner:** v3 PR-7 / PR-8 / PR-9 Architect.

3. **§24.3 symmetric receiving-side caveat-discipline (core.md-level + usage-guide-level).** Maps to observation (g). Most framework-shaping of the three; extends §24 mechanism description, not just usage-guide.
   - v3 `core.md` §24.3 gains explicit symmetric-application clause covering Architect receiving Builder hand-back claims, parallel to existing Builder receiving Architect prompt direction.
   - v3 `usage-guide.md` documents concrete four-point check pattern (PR comments both endpoints, branch state, file content against prescription, phantom-action audit) as default Architect-side discipline at hand-back receipt.
   - **Open placement question** noted for v3 authoring (whether to add a fifth core-doc surface-specific section parallel to §8.2). PMN-003 does not resolve.
   - **Owner:** v3 PR-7 Architect (core.md authoring) for the §24.3 clause; v3 PR-9 Architect (usage-guide authoring) for the four-point check pattern.

**Mapping arithmetic:** 3 + 3 + 1 = 7 mapping slots; 7 unique observations; no double-counts. Same arithmetic as PR-4 and PR-5 cycle running discussions; refinements (TASK-0005 evidence) update wording within observations, not the mapping.

---

## Provenance

### Source PRs

| PR | TASK | Branch (squash-merged) | Source observations |
|---|---|---|---|
| PR-3 | TASK-0003 | `chore/task-0003-pmn-001-production-learnings` | (b) initial framing; (c) initial channel inventory |
| PR-4 | TASK-0004 | `chore/task-0004-pmn-002-pr-3-cycle-learnings` | (a), (d), (e), (f), (g) primary evidence |
| PR-5 | TASK-0005 | `chore/task-0005-adr-002-task-reservation-amendment` | (b), (c), (e) refinements; (a) implicit refinement candidate; (d), (f), (g) confirming evidence |

### Linked records

- ADR-001 — initial repo setup; 15 decisions including decision 11 (owner handles Codex invocation) and decision 8 (TASK reservation, superseded by ADR-002).
- ADR-002 — TASK reservation amendment; extended TASK-0001-through-0008 to TASK-0001-through-0012; PMN-insertion pattern recognized as framework feature (Decision 3).
- PMN-001 — first PMN under §18 convention; 15 observations from PR-1 + PR-2 production learnings; established §18 PMN-fileform discipline at this project.
- PMN-002 — second PMN; 5 observations from PR-3 cycle review-discipline learnings; PMN-003 (d) extends PMN-002 (e)'s placeholder-substitution audit scope from PR-body-only to all-committed-artifacts. Other PMN-003 observations document PR-4 and PR-5 cycle field evidence at this PMN's authoring time.
- TASK-0003 / TASK-0004 / TASK-0005 handoffs — durable cycle records preserved at `docs/handoffs/`.
- PR-3 / PR-4 / PR-5 review-context files — pre-commit Codex review evidence and post-PR review state preserved at `docs/reviews/`.

### Framework-text references

- AMAS v2.14.1 §18 — post-merge note canonical form (this PMN follows it).
- AMAS v2.14.1 §24 — cross-surface verify-before-assert meta-pattern; (g)'s structural fix extends §24.3.
- AMAS v2.14.1 §24.2(a) — external-system-behavior assertion sub-shape; (e) and (g) are §24.2(a) instances.
- AMAS v2.14.1 §24.2(b) — artifact-content assertion sub-shape including propagation-incompleteness flavor; (a) is a §24.2(b) instance.
- AMAS v2.14.1 §8.1.1.1 — Reviewer dual-signal output handling; (b) auto-fire pattern is a §8.1.1.1 application.
- AMAS v2.14.1 §8.1.1.2 — Reviewer claimed-action verification; (b) auto-fire phantom-action narratives are §8.1.1.2 applications.
- AMAS v2.14.1 §23.6 — Architect pre-handoff self-review; (a) extends §23.6 sweep scope and re-trigger conditions.
- AMAS v2.14.1 §10.5 — single-contributor bypass; PR-3, PR-4, PR-5 all merged via §10.5.

### Three-cycle evidence base summary

- **PR-3 cycle**: Codex auto-fire on PR open present; substantive-verdict channel (i) (explicit text in COMMENTED body) observed.
- **PR-4 cycle**: Codex auto-fire on PR open present; substantive-verdict channel (ii) (COMMENTED + boilerplate + no suggestions) observed; line-level findings via single-endpoint check missed; handoff metadata placeholder preserved verbatim; Edit-time heading drop; Builder hand-back claim about no-findings status incomplete.
- **PR-5 cycle**: Codex auto-fire on PR open absent (44s pre-trigger window); fast-response issue-level "Approve" stub anti-channel observed; single-poll across both endpoints when timed too early observed as failure mode; (d), (f), (g) disciplines confirming as working-as-designed; in-cycle path-(a) revision triggered §24.2(b) propagation gap not caught by §23.6 re-running discipline.

End of PMN-003.
