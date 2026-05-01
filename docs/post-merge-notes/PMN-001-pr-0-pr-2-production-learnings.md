# PMN-001: PR-1 + PR-2 production learnings

## Metadata

- PMN ID: PMN-001
- Source PRs: PR #1 (TASK-0001 repo bootstrap, merged at SHA `c1ec54f`), PR #2 (TASK-0002 v3 framework package scaffold, merged at SHA `0e7eef4`)
- Authored: 2026-05-01
- Author surface: Architect (Claude Opus 4.7, Claude.ai Project)
- Framework version dogfooded: AMAS v2.14.1
- Status: accepted

## Mid-life adoption note

Per AMAS v2.14.1 §18 mid-life PMN-convention adoption clause: this is the first post-merge note authored under the convention in the `amas-framework` project. Two prior PRs are §18-eligible — PR #1 (created ADR-001 establishing the standalone repo's durable system shape; established branch protection and the Builder/Reviewer cycle pattern) and PR #2 (established the v3 framework package directory structure; produced unexpected review friction including the Architect-side encoding misdiagnosis incident). Both prior eligible PRs are addressed jointly in this PMN-001 rather than as separate retrospective PMNs, on the rationale that the observations from PR #1 and PR #2 cluster into common patterns and are more legible as a single durable record. No other prior eligible PRs exist for this project. Per the framework, retrospective backfill for prior PRs is owner-decided; the explicit decision recorded here is "joint-coverage in PMN-001."

## Trigger basis

Three of §18's five trigger categories fire for the joint coverage of PR #1 + PR #2:

1. **Architecture change.** PR #1 created `docs/adr/ADR-001-initial-repo-setup.md` with 15 architectural decisions establishing the standalone repo's durable system shape (durable name, MIT/public, default `main`, dogfood from day one, v3 content at root, PR sequence reservation, owner-handled `@codex review`, branch-protection deferral, GITHUB_TOKEN read-only posture, topics list, harness-directory gitignore, plus four others). PR #2 established the v3 framework package directory structure (50 stubs + 2 archive prompts) which durably anchors v3 content authoring across PR-3 onward.

2. **Workflow change.** PR #1 established branch protection on `main` (Posture 2 Rulesets: PRs required, 1 approval, code-owner review, conversation resolution, squash-only merge, pull-request-only admin bypass), authored `.github/CODEOWNERS` and `.github/PULL_REQUEST_TEMPLATE.md`, and codified the entire Builder/Reviewer cycle pattern for this repo. PR #2 demonstrated and refined the Builder/Reviewer cycle in practice including the pre-commit Codex desktop review pattern.

3. **Unexpected review friction.** PR #2 produced one significant flushed effort (an encoding fix-up commit authored and never executed) and surfaced four distinct Architect-side defect classes including count drift across three instances, review-pipeline encoding misdiagnosis, and two delivery-format misses. Builder caught the Architect's encoding misdiagnosis at pre-flight via §8.2 byte-fidelity verification — the framework discipline working as designed, but representing a cluster of patterns that warrant durable capture. The PMN-001 authoring session itself surfaced an additional friction point (chat-block delivery failure for large prompts), captured as observation (h.2) below.

The remaining two trigger categories (tool-assignment change, validation-strategy change) do not fire for these PRs.

## Observations

The 15 observations below cluster into three groups: framework spec gaps that PR-3 onward addresses; Architect-side review and authoring discipline; and surface-format and handoff-shape discipline.

### Cluster 1: Framework spec gaps that PR-3 onward addresses

**Observation (a) — Pre-commit Reviewer-cycle gap.** AMAS v2.14.1's review discipline (§8.1, §8.1.1) codifies post-PR Reviewer engagement but does not codify pre-commit review by an assigned Reviewer surface. PR #2 ran a pre-commit Codex desktop review (between Builder authoring complete and `git add`) per ad-hoc prompt direction; the discipline worked but was not framework-canonical. **Structural fix:** v3 `core.md` adds canonical pre-commit Reviewer-cycle rule. Pre-commit review by Reviewer surface, cross-ecosystem from Builder, between authoring complete and `git add`. Reviewer-role-driven (not surface-specific) — project's assigned Reviewer surface instantiates the rule.

**Observation (b) — Audit-as-TASK misclassification.** Codex desktop, when asked to perform a readiness-check audit on PR #1, mistakenly authored a TASK handoff for the audit (filename observed: `TASK-0001-codex-pr-review-readiness-handoff.md`). Audits are pre-action checkpoints, not tasks. **Structural fix:** v3 `usage-guide.md` names the artifact class for pre-action checkpoints (likely "audit" or "checkpoint") distinct from TASK handoffs, and clarifies what does and does not warrant a TASK handoff.

**Observation (i) — Reviewer invocation direction-shape patterns.** PR #2's Reviewer invocations (Codex desktop pre-commit; post-PR `@codex review`) used different direction levels incidentally rather than deliberately. Codex desktop received a structured embedded prompt block (high direction); post-PR `@codex review` received bare invocation (auto-discover via AGENTS.md). Both worked; neither was a deliberate choice. **Structural fix:** v3 `core.md` defines four named direction-shape patterns: auto-discover / directed-scope / claim-verification-only / free-form-substantive. v3 `usage-guide.md` provides paste-ready invocation templates per pattern. v3 §17.7 review template gains a "Direction shape requested" field; Reviewer's output begins by acknowledging the shape and confirming whether followed.

**Observation (k) — Builder-uncertainty-on-canonical-rule-edge-case escalation.** Builder caught an edge case during the PR #2 P3 fix-up: a small enrichment (parenthetical) added to a prescribed Reviewer fix. Builder correctly recognized the edge, surfaced via §8.3 stop-and-show, and asked Architect for direction rather than self-assessing whether the enrichment was within scope. **Structural fix:** v3 `core.md` adds explicit clause directing Builder to surface uncertainty when a fix may exceed the Reviewer's prescribed scope, rather than self-assess. Reinforces the canonical rule from PR #2 ("Builder fix that directly implements a Reviewer's prescribed change does not require re-review; goes beyond does") with an explicit edge-case escalation pattern.

### Cluster 2: Architect-side review and authoring discipline

**Observation (c) — Architect §3-count-derivation defect.** Three count drift instances across PR #1 + PR #2: PR #1 v1 truncated count, PR #2 v1 scratch-work count, PR #2 v2 off-by-one (claimed 66/57/56/1/9; correct values 65/56/55/1/9). Pattern: count table headline numbers stated as standalone values, not derived from explicit arithmetic shown in the prompt. **Structural fix:** v3 framework Architect-side authoring discipline requires count tables to display explicit arithmetic (e.g., "10 PR-1 + 55 new = 65 tracked"). Architect §23.6 self-review checklist gains an item: "Do count table headline numbers reconcile to the prompt's own enumeration via shown arithmetic?"

**Observation (d) — Architect-side review-pipeline encoding misdiagnosis.** Architect declared a Blocking finding (claimed 264 character corruptions across 55 files) based on `gh pr diff 2 > pr-2-diff.txt` output captured via PowerShell 5.1's UTF-16 LE redirect. Builder caught the error via §8.2 pre-flight: faithful diff capture (using `cmd /c "chcp 65001 >nul && git diff > <file>"`) confirmed source bytes were correct (zero corruptions). Architect retracted the finding. **Structural fix:** v3 framework Architect-side review discipline requires review-pipeline byte-fidelity verification before substantive review against captured bytes. Specifically: pick one source file containing a known multi-byte character (e.g., `§` at `C2 A7`), capture via the same pipeline as the review artifact, byte-compare against `git show`. Mismatch implies a different pipeline is needed before review proceeds. Lands in v3 `usage-guide.md` and as Architect §23.6 self-review checklist item.

**Observation (g) — §24 cross-surface verification benefits from external Reviewer perspective.** Codex's post-PR review on PR #2 caught two §24 cross-surface drift findings (README version-metadata claim too broad; review-context diff-stat stale at 1844 vs. actual 1852) that Architect's §23.6 self-review and Architect-side §24 sweep had missed. **Structural fix:** v3 `core.md` §24 sweep canonical rule gains explicit Reviewer-side verification of PR-meta cross-surface consistency, not only Architect-side. The same mental model that authored the drift is the one self-reviewing for it; external Reviewer perspective is structurally necessary for PR-meta drift detection.

**Observation (l) — Architect predictions about diff-shape are §24.2(a) external-system assertions.** Architect predicted "diff will shrink by 1 line" on PR #2 P3 fix-up; Builder reported actual diff totals were unchanged (parenthetical-strip's line saving balanced by audit-context fold's line cost). Builder's transparency note is the framework discipline working. **Structural fix:** Architect should report predictions explicitly rather than implicitly, so they're verifiable. Builder's prediction-vs-actual report is part of phantom-action discipline, not pedantry. Lands as a small clause in v3 `usage-guide.md` Architect-side phantom-action discipline section.

### Cluster 3: Surface-format and handoff-shape discipline

**Observation (e) — Windows PowerShell 5.1 byte-stream redirect corruption.** PowerShell 5.1's `>` and `Out-File` redirects pass UTF-8 stdout through `[Console]::OutputEncoding` (defaults to system code page on Windows; CP437 or CP1252) before writing to file, corrupting multi-byte UTF-8 sequences. Verified during PR #2 with both `gh pr diff` and `git diff` outputs. **Structural fix:** v3 framework appendix (likely `appendices/vendor-surface-guidance.md` or a new `appendices/windows-operational-guidance.md`) documents the byte-safe pattern on Windows: `cmd /c "chcp 65001 >nul && <utf-8-producing-command> > <output-file>"`. PowerShell 7+ handles UTF-8 natively. Affects diff-capture, file-content capture, any pipeline that ingests external tool stdout.

**Observation (f) — Review-capture pipelines are §24.2(a) surfaces.** Pipelines that capture source bytes (diff dumps, file dumps, etc.) are themselves external-system-behavior surfaces requiring byte-fidelity verification before substantive review against the captured artifact. Same principle as observation (d) but framed as a framework discipline, not just an Architect-side review item. **Structural fix:** v3 `core.md` §24 cross-surface verify-before-assert rule explicitly names review-capture pipelines as a §24.2(a) surface class.

**Observation (h) — Architect → Builder direction format.** Direction split across narrative + code block + post-script + decisions interleaved creates phantom-action and partial-direction risk: Builder may receive only the part the owner copied, not the whole. **Structural fix:** v3 framework canonical rule — Architect direction to Builder must be delivered as a single self-contained delivery, copyable as one operation by the owner. Two valid mechanisms (see (h.1) and (h.2)). Architect-side personal context, framework-level reasoning, PMN observations, and post-script commentary belong outside the delivery, never inside or after-with-mixed-content.

**Observation (h.1) — In-chat copyable block placement.** When direction content is small enough that chat rendering preserves source faithfully on selection-copy (rough threshold: ≤500 lines, no nested code fences, no complex tables, no deeply nested structures), the in-chat block mechanism is valid. The block must be demarcated unambiguously (e.g., `[BEGIN response to Builder]` ... `[END response to Builder]`) and must be the **last content** in the message — all owner-only commentary above the block, not below. Selecting from `[BEGIN]` to end-of-message yields exactly the block. **Structural fix:** v3 `usage-guide.md` Architect-side delivery discipline section names this as the canonical placement pattern when in-chat block delivery is used.

**Observation (h.2) — File-based Builder direction (NEW from PMN-001 authoring session).** When direction content exceeds chat-rendering reliability — large content (>~500 lines), nested code fences, complex embedded tables, or deeply nested structures — the in-chat block mechanism (h.1) fails because the chat surface's markdown renderer distorts source on selection-copy. The owner cannot reliably reproduce source bytes via the "select [BEGIN] to [END]" gesture; rendered HTML is captured instead. **Structural fix:** the file-based delivery mechanism is co-equal with (h.1) in-chat block: Architect produces the direction as a markdown file artifact; owner saves to a known repo-local path (gitignored area, e.g., `.claude/architect-prompts/TASK-####-builder-prompt.md` if the project follows the `.claude/` harness-directory gitignore convention from ADR-001); the in-chat direction is a thin pointer prompt directing Builder to read the saved file. The pointer prompt itself follows (h)+(h.1) — small self-contained block at message bottom. Cleanup: owner deletes the prompt file after the PR merges; no durable repo footprint. **Discovery provenance:** observed during the PMN-001 authoring session itself. The Architect's first attempt used the (h.1) in-chat block pattern for a ~6k-word Builder prompt with three embedded file bodies and nested code fences. Owner surfaced that the rendered block could not be reliably copied as source. Architect adopted the file-based pattern in-cycle and added (h.2) to PMN-001's observation set as a real-time refinement to (h)+(h.1).

**Observation (j) — Builder → Architect hand-back format.** Same principle as (h) inverted: hand-back format must be optimized for the receiving Architect surface (Claude.ai Project, ChatGPT, Codex desktop, raw API, etc.) and must declare receiving-surface format pattern. Different surfaces have different ingestion characteristics. **Structural fix:** v3 universal handoff schema (`templates/handoff-template.md`) gains a "Receiving surface" field and a "Format pattern" field. v3 `usage-guide.md` documents named format patterns: Claude.ai-optimized / ChatGPT-optimized / Codex-CLI-optimized / Codex-desktop-optimized / raw-API-optimized.

**Observation (m) — Architect → Architect handoff (between sessions in the same project).** Same principle as (j): the format must be optimized for the receiving Architect surface and must declare receiving-surface format. For Claude.ai Project chats, the handoff is a markdown document the owner pastes as the first message in the new chat. Receiving Architect cannot see prior chat history; project_knowledge_search recovers partial context only; explicit handoff is the durable surface. **Structural fix:** v3 framework canonical names the session-handoff pattern. v3 `usage-guide.md` provides a session-handoff template. Session handoffs may live at `docs/handoffs/SESSION-HANDOFF-YYYY-MM-DD-<topic>.md` if durable, or as ephemeral artifacts the owner copies into the new chat as context.

## Three structural-fix recommendations

PR-3 onward content authoring will absorb these into canonical text:

1. **Universal handoff schema upgrade** — receiving-surface field, format-pattern field, single-self-contained-delivery requirement (in-chat block per (h.1) OR file-based pointer per (h.2)), direction-shape field for Reviewer invocations, audit/checkpoint artifact class distinct from TASK. Maps to observations (b), (h), (h.1), (h.2), (i), (j), (m).

2. **Cross-surface verification expansion** — §24 sweep includes review-pipeline byte-fidelity as a verifiable surface; Reviewer-side §24 verification of PR-meta surfaces; explicit pre-commit Reviewer-cycle canonical rule. Maps to observations (a), (d), (e), (f), (g), (k).

3. **Architect-side authoring discipline** — explicit-arithmetic count tables; §23.6 self-review checklist additions for prediction reporting, review-pipeline byte-fidelity, count-derivation reconciliation. Maps to observations (c), (d), (l).

Mapping arithmetic: 7 + 6 + 3 = 16 mapping slots; 15 unique observations + 1 deliberate double-count for (d) which has both surface-class shape (#2) and authoring-discipline shape (#3).

## Session-specific Architect-side defect log

For durable-record completeness; not framework-shaping in themselves but supporting evidence for the observations above.

1. **PR-1 v1 prompt truncation** — chat-rendering issue with nested code fences; resolved in v2 by switching to `[BEGIN <filename>]/[END]` markers. Project-specific tooling artifact; not generalized into framework observation.

2. **PR-2 v1 prompt scratch work** — Architect's own thought-process traces (count reconciliation, "Hmm/wait" markers) embedded in prompt body. Caught in Architect §23.6 self-review during v1→v2 transition; resolved in v2. Project-specific authoring artifact; supporting evidence for observation (c) discipline gap.

3. **PR-2 v2 prompt count off-by-one** — §3 count table claimed 66/57/56/1/9; correct values were 65/56/55/1/9. Builder caught at step 10 verification, surfaced cleanly, count revised to actual. Direct evidence for observation (c).

4. **PR-2 review-pipeline encoding misdiagnosis** — Architect declared a Blocking finding (264 char corruptions) based on mojibake'd diff dump; source bytes were correct. Builder caught at pre-flight stop condition; Architect retracted via faithful diff capture. Direct evidence for observations (d), (e), (f).

5. **Two delivery-format misses across PR-1 + PR-2 sessions** — Architect direction blocks not consistently single-self-contained-copyable (observation h); blocks not consistently placed as last content in message (observation h.1). Both raised by owner during sessions and acknowledged. Direct evidence for observations (h), (h.1).

6. **PMN-001 authoring session in-chat block delivery failure** — Architect's first PMN-001 Builder prompt used the (h.1) in-chat block pattern for ~6k words of content with three embedded file bodies and nested code fences. Owner surfaced that selecting from `[BEGIN response to Builder]` to `[END response to Builder]` and copying captures rendered HTML rather than source markdown — chat surface markdown rendering distorts source on round-trip for content of this size and complexity. Architect adopted file-based delivery (h.2) in-cycle and added the new observation to PMN-001 as a real-time refinement. Direct evidence for observation (h.2); also reinforces observation (h) at the principle level.

Pattern noted in the session handoff: defects clustered in the back half of the ~14 hour session preceding this PMN-authoring session. This observation supports the framework's session-length discipline (which is what observation m's structural fix codifies). Defect 6 occurred in the PMN-authoring session (fresh session) — evidence that fresh-session discipline does not prevent all defect classes; some require new patterns to surface.

## Action items

| Owner | Action | Trigger |
|---|---|---|
| Architect (PR-3 authoring) | Absorb structural fix #1 (universal handoff schema upgrade) into v3 `core.md`, `usage-guide.md`, and `templates/handoff-template.md`; document (h.1) in-chat vs (h.2) file-based delivery as co-equal mechanisms with threshold heuristics | PR-3 prompt authoring |
| Architect (PR-3 authoring) | Absorb structural fix #2 (cross-surface verification expansion) into v3 `core.md` §24 and `usage-guide.md`; add canonical pre-commit Reviewer-cycle rule | PR-3 prompt authoring |
| Architect (PR-3 authoring) | Absorb structural fix #3 (Architect-side authoring discipline) into v3 §23.6 and `usage-guide.md` | PR-3 prompt authoring |
| Architect (PR-3 prompt) | Apply discipline patterns from (h), (h.1), (h.2), (i), (j) when authoring PR-3's Builder prompt — single self-contained delivery (file-based or in-chat per content size threshold), receiving-surface declared, Reviewer-direction-shape declared | PR-3 Builder prompt drafting |
| Architect (PR-3 prompt or ADR-002) | Document ADR-001 decision 8 reservation flex from TASK-0001-through-0008 to TASK-0001-through-0009 with PMN-001 = TASK-0003 interleaved between bootstrap and v3 content sequence | PR-3 prompt authoring or first ADR-002 amendment |
| Owner | Decide whether to pursue v3 content as one PR (PR-3) or decompose into PR-3a / PR-3b / PR-3c sub-PRs at PR-3 prompt authoring time | PR-3 prompt authoring |

## Provenance

- Source PR: PR #1 (TASK-0001 repo bootstrap), merged at SHA `c1ec54f`, branch `chore/task-0001-repo-bootstrap`
- Source PR: PR #2 (TASK-0002 v3 framework package scaffold), merged at SHA `0e7eef4`, branch `feat/task-0002-v3-package-scaffold`
- Source TASKs: TASK-0001, TASK-0002
- Source ADR: ADR-001 (initial repo setup, 15 decisions)
- Source FEAT: FEAT-0001 (v3 package scaffold specification)
- Authored: 2026-05-01
- Author surface: Architect (Claude Opus 4.7, Claude.ai Project)
- Authoring session: cross-session handoff via ephemeral document (per observation (m), durable session-handoff placement is anticipated for v3 codification)
- Framework version dogfooded: AMAS v2.14.1
- Linked PR: PR #3 (this PMN's containing PR; assigned at `gh pr create` time)
