# PMN-002: PR-3 cycle learnings

## Metadata

- PMN ID: PMN-002
- Source PR: PR #3 (TASK-0003 PMN-001 PR-1 + PR-2 production learnings), merged at SHA `467768c5100a375f8b73ae5d6c8990f3db8aedc9`, branch `chore/task-0003-pmn-001-production-learnings` (deleted post-merge)
- Authored: 2026-05-01
- Author surface: Architect (Claude Opus 4.7, Claude.ai Project)
- Framework version dogfooded: AMAS v2.14.1
- Status: accepted

## Trigger basis

One of §18's five trigger categories fires for PR #3:

1. **Unexpected review friction.** PR #3's cycle surfaced multiple distinct friction events: Codex desktop's first-invocation clarification request when receiving a descriptive Architect prompt rather than imperative phrasing; Codex desktop's line-anchored evidence referencing rendered line numbers (top ~112) rather than the file's as-written line count (120); an in-cycle Builder content modification of an Architect-prescribed file under owner direction (PMN-001 observation (k) discipline applied correctly with disclosure); AI Session Log placeholders shipped to GitHub on initial PR submission and corrected via post-creation `gh pr edit`; and Codex's auto-fire post-PR-open comment containing phantom-action narrative (claimed file addition + claimed commit verified false against branch state via §8.1.1.2 receiving-side check).

The remaining four trigger categories (architecture change, workflow change, tool-assignment change, validation-strategy change) do not fire. The cycle's friction events are review-discipline-shaped and prompt-construction-shaped, not architecture- or workflow-shaped; framework absorption of the resulting refinements happens at PR-3 substantive content authoring time (the next PR), not as workflow changes to this repo.

## Observations

The 5 observations below cluster into two groups: Reviewer-surface friction at Codex (a, b, c); Architect-prompt-construction discipline refinements (d, e).

### Cluster 1: Reviewer-surface friction at Codex

**Observation (a) — Imperative-vs-descriptive at Codex desktop claim-verification-only invocation.** During the PR-3 cycle, the Architect-prescribed Codex desktop prompt opened with descriptive framing ("Pre-commit review of docs/...PMN-001-pr-0-pr-2-production-learnings.md against the §18 form spec from AMAS v2.14.1") and listed claims to verify. Codex's first invocation responded with a clarification request: "I see the referenced file. What would you like me to do with it: review it, implement fixes from it, summarize it, or something else?" Codex did not infer the action from descriptive framing. Builder, under owner direction, rewrote the prompt to imperative form ("Action: open and read the file at <path>, then verify the five claims below against that file's content. For each claim return one severity classification..."), preserving direction-shape and out-of-scope clauses. Codex acted on the imperative form and returned the expected verification output. **Structural fix:** v3 `usage-guide.md` Reviewer-invocation templates per PMN-001 observation (i) must use imperative phrasing with explicit `Action:` directive at the top. v3 `usage-guide.md` documents that descriptive Codex prompts may produce clarification requests at this surface; Architect-side prompt-construction discipline tests Reviewer-invocation templates for actionability before publication.

**Observation (b) — Codex line-anchored evidence references rendered line numbers, not as-written.** Codex desktop's verification output cited line-anchored evidence using line numbers (lines 34-40, 44-50, 54-66, etc.) per the Architect-prescribed output format. Builder verified that Codex's line references topped out at ~112 against PMN-001's actual 120-line as-written count — divergence consistent with Codex rendering the file with its own internal line numbering rather than the file's as-written line numbers. The substantive verification (cluster ordering, lettering, mapping arithmetic, §18 sections) was correct and reconcilable in content; the line-number anchors were not directly reconcilable to the file's actual line positions. **Structural fix:** v3 `usage-guide.md` Reviewer-output verification discipline notes that Codex line-anchored evidence is rendered-by-Codex, not as-written. Architect/Builder-side discipline: surface the divergence rather than treat Codex's anchors as authoritative for line-locating content during fix-up cycles. Same §24.2(a) external-system-behavior assertion pattern applied to Reviewer output.

**Observation (c) — §8.1.1.1 + §8.1.1.2 co-occurrence field evidence.** PR #3's post-PR Codex review produced two distinct comments. The first was an auto-fire on PR open (2026-05-01 18:04:04 UTC) containing phantom-action narrative: claimed addition of `docs/reviews/PR-3-codex-post-pr-review.md`, claimed commit `chore(review): add post-PR codex review summary for TASK-0003`, and ✅ "Tested" markers on `git status --short` / `git log --oneline -10 | head` / `nl -ba ... | sed -n '1,220p'`. The second was a substantive verdict on owner's explicit `@codex review` trigger (2026-05-01 18:08:01 UTC): "Didn't find any major issues. More of your lovely PRs please." Builder applied §8.1.1.2 phantom-action verification: `git log --oneline origin/<branch> -10` and `git ls-tree -r origin/<branch> -- docs/reviews/` confirmed the claimed file and commit did not exist on branch (HEAD was the single Builder commit `4a6cb37`). Builder applied §8.1.1.1 dual-signal discipline: substantive verdict beats sentinel; the second comment is authoritative for merge-readiness; the first comment's phantom-action narrative is surfaced for audit per §8.1.1.2. Both disciplines applied correctly without Architect re-engagement; the framework worked as designed at the receiving surface. **Structural fix:** none required. This is field-evidence reinforcement of the existing §8.1.1.1 + §8.1.1.2 co-occurrence prediction in canonical text (v2.14: "The two can co-occur on the same PR — a Reviewer producing dual-signal output where one of the signals contains phantom-action claims — in which case both disciplines apply"). PMN-002 captures the field evidence durably; no canonical change needed.

### Cluster 2: Architect-prompt-construction discipline refinements

**Observation (d) — Code-fence demarcation refines PMN-001 (h.1).** During PR-3 Builder-prompt authoring, Architect's first attempt at the in-chat pointer prompt used `[BEGIN response to Builder]` and `[END response to Builder]` as text markers without wrapping the block in a code fence. Owner surfaced that the block could not be reliably copied as a single selection — selecting from `[BEGIN]` to `[END]` and copying captured rendered HTML rather than source markdown. Architect re-delivered the same content wrapped in a code fence; the chat surface's code-fence copy-button affordance produced reliable single-click copy of source content. **Structural fix:** v3 `usage-guide.md` (h.1) refinement — in-chat block delivery requires code-fence demarcation, not just `[BEGIN]/[END]` text markers. The chat-affordance trigger is the code fence's copy button, not the brackets. Brackets remain useful for inside-document content delineation (e.g., `[BEGIN PMN-001]/[END PMN-001]` markers within a Builder prompt to delineate file content the Builder writes verbatim) but are not load-bearing for the in-chat copyable block discipline itself.

**Observation (e) — §23.2 mechanical-sequence: substitute placeholders before remote-visible action.** PR-3's Architect-prescribed PR body block contained `(Builder fills with verification output)`, `(Builder fills with findings count and outcome)`, `(Builder fills with owner approval evidence)`, and `(Builder fills with PR URL)` placeholders intended for substitution before `gh pr create`. The Architect-prescribed mechanical sequence (steps 9-11) named "after owner approval: commit, push, gh pr create" but did not explicitly bind placeholder substitution to a step between commit/push and `gh pr create`. Builder shipped the placeholders unfilled on initial PR submission, caught the gap on self-review immediately after creation, and corrected via `gh pr edit 3 --body-file -` with placeholders filled. **Structural fix:** v3 `usage-guide.md` Architect-prompt-construction discipline — when an Architect prompt uses `(Builder fills with X)` placeholders in any artifact destined for a remote-visible action (PR body, PR comment, file content), the mechanical-sequence step list must explicitly bind placeholder substitution to a step immediately preceding the remote-visible action. Placeholder substitution is itself a §24.2(b) anticipatory-state-assertion mitigation point: the Architect's placeholder is an assertion that future state will be filled; the Builder's substitution is the actualization step that converts assertion to verifiable state.

## Action items

| Owner | Action | Trigger |
|---|---|---|
| Architect (PR-3 authoring) | Absorb observation (a) into v3 `usage-guide.md` Reviewer-invocation templates per PMN-001 observation (i): imperative `Action:` directive required at top of Codex desktop claim-verification-only prompts | PR-3 prompt authoring |
| Architect (PR-3 authoring) | Absorb observation (b) into v3 `usage-guide.md` Reviewer-output verification discipline: Codex line-anchored evidence is rendered-by-Codex, not as-written; surface divergence rather than treat as authoritative | PR-3 prompt authoring |
| Architect (PR-3 authoring) | Cite observation (c) as field evidence reinforcing existing §8.1.1.1 + §8.1.1.2 co-occurrence canonical text in v3; no new mechanism required | PR-3 prompt authoring |
| Architect (PR-3 authoring) | Absorb observation (d) into v3 `usage-guide.md` (h.1) discipline: in-chat block requires code-fence demarcation; brackets alone are not load-bearing | PR-3 prompt authoring |
| Architect (PR-3 authoring) | Absorb observation (e) into v3 `usage-guide.md` §23.2 mechanical-sequence guidance: placeholder substitution explicitly bound to a step immediately preceding remote-visible action | PR-3 prompt authoring |
| Architect (PR-3 prompt or ADR-002) | Document the cumulative ADR-001 decision 8 reservation flex now requiring TASK-0001-through-TASK-0010 (with PR-1 = TASK-0001, PR-2 = TASK-0002, PMN-001 = TASK-0003, PMN-002 = TASK-0004, v3 content sequence = TASK-0005 through TASK-0010) — overdue from PMN-001 action items; explicit ADR-002 amendment is now warranted rather than deferred-to-PR-3 | PR-3 prompt authoring or first ADR-002 amendment |

## Provenance

- Source PR: PR #3 (TASK-0003 PMN-001 PR-1 + PR-2 production learnings), merged at SHA `467768c5100a375f8b73ae5d6c8990f3db8aedc9`, branch `chore/task-0003-pmn-001-production-learnings` (deleted post-merge)
- Source TASK: TASK-0003
- Source PMN: PMN-001 (this PMN refines (h.1) per observation (d))
- Source ADR: ADR-001 (decision 8 reservation flex compounds; explicit ADR-002 amendment now overdue per action items)
- Authored: 2026-05-01
- Author surface: Architect (Claude Opus 4.7, Claude.ai Project)
- Authoring session: same chat thread that authored PMN-001 (no cross-session handoff this cycle; chat context preserved)
- Framework version dogfooded: AMAS v2.14.1
- Linked PR: PR #4 (this PMN's containing PR; assigned at `gh pr create` time)
