---
status: drafted
---

# PR-102 Codex desktop pre-commit review

## Metadata

- PR: PR-102 (anticipated; verify at PR-open)
- Branch: fix/task-0054-predicate-hygiene
- Cycle: TASK-0054
- Linked handoff: docs/handoffs/TASK-0054-predicate-hygiene.md
- Status: drafted
- Codex desktop session timestamp (UTC): TBD at pre-commit review invocation

## Builder claims to verify

1. **Cumulative-diff-stats per `core.md` §23.6.1.1 (e.1) — 10 files, sum-stable.** At staged state:
   - bash: `git diff --staged --shortstat` returns `10 files changed, 338 insertions(+), 18 deletions(-)`
   - bash: `git diff --staged --numstat` returns per-file rows:
     ```
     5	5	.amas/surfaces.yml
     1	1	AGENTS.md
     1	1	CLAUDE.md
     1	1	README.md
     20	6	core.md
     163	0	docs/handoffs/TASK-0054-predicate-hygiene.md
     142	0	docs/reviews/PR-102-codex-pre-commit.md
     3	3	github-reference.md
     1	0	templates/handoff-template.md
     1	1	usage-guide.md
     ```
   - Bidirectional sum-stable: per-file insertion sum 5+1+1+1+20+163+142+3+1+1 = 338 equals shortstat insertions; per-file deletion sum 5+1+1+1+6+0+0+3+0+1 = 18 equals shortstat deletions.

2. **WS3a — the `dual-signal` label is removed from all live canonical-law sites; one intentional breadcrumb retained.** The four live label occurrences (core.md ×2, github-reference.md ×2) were renamed to `three-endpoint` at b795b38. Verify per canonical surface:
   - bash: `grep -n "dual-signal" core.md` → no matches
   - bash: `grep -n "dual-signal" usage-guide.md` → no matches
   - bash: `grep -n "dual-signal" github-reference.md` → exactly one match: the intentional §6.3 legacy breadcrumb (`formerly labeled \`dual-signal\``)
   - Note: the broad repo-wide `grep -r "dual-signal" --include="*.md" .` is NOT a zero-residual predicate — it additionally returns this cycle's own descriptive text (handoff + review-context files describing the rename) and append-only historical docs (prior-cycle handoffs, PMNs, prompts). Those are expected out-of-scope-for-WS3a residuals, not live canonical labels.

3. **WS3b — §18.4 ADR-008 D6 citations present at both target strings.**
   - bash: `grep "ADR-008 D6" core.md` returns one line (line 610) containing both `canonicalized at ADR-008 D6:` and `See ADR-008 D6 for the decision.` (both citations appear in the same §18.4 release-track paragraph)

4. **WS0 — 11 version-of-record sites bumped to 3.0.4 (3 trio frontmatter + README.md + 5 surfaces.yml + AGENTS.md + CLAUDE.md).**
   - bash: `grep "framework_version: 3.0.4" core.md github-reference.md usage-guide.md .amas/surfaces.yml` returns 4 lines (one per file)
   - bash: `grep "v3.0.4" README.md` returns line 9 containing `**v3.0.4**`
   - bash: `grep "canonical_version: 3.0.4" .amas/surfaces.yml` returns 4 lines
   - bash: `grep "v3.0.4" AGENTS.md CLAUDE.md` returns the `Active framework version: AMAS v3.0.4` line in each file
   - bash: `grep "3.0.3" core.md github-reference.md usage-guide.md README.md .amas/surfaces.yml AGENTS.md CLAUDE.md` returns only the README.md `Adopter migration note (v3.0.3)` historical reference — no version-of-record line carries 3.0.3

5. **WS1 — §24.7 Claim-artifact-parity present in core.md after §24.6.**
   - bash: `grep -n "§24.7" core.md` returns a line containing `### §24.7. Claim-artifact-parity`
   - bash: `grep -c "Claim-artifact-parity" core.md` returns `3` (the §24.7 heading, the opening paragraph, and the unifying-rule paragraph)

6. **WS2 — §23.6.5 empirical grounding extended with TASK-0053 sentence.**
   - bash: `grep "TASK-0053 (PR-100)" core.md` returns the line in §23.6.5 containing `Subsequent cross-cycle reinforcement at TASK-0053 (PR-100)`

7. **WS3c — core.md §13.2 body-Status sentence present; handoff-template.md body-Status bullet present.**
   - bash: `grep "not an Action-maintained mirror of frontmatter" core.md` returns the §13.2 sentence
   - bash: `grep "Body.*- Status.*vs frontmatter" templates/handoff-template.md` returns the Usage notes bullet

8. **Handoff frontmatter `status: active` (path-(α') flip applied); body `- Status:` stays `drafted` (gate-snapshot per WS3c clarification).**
   - bash: `head -15 docs/handoffs/TASK-0054-predicate-hygiene.md | grep "^status:"` returns `status: active`
   - bash: `grep "^- Status:" docs/handoffs/TASK-0054-predicate-hygiene.md` returns `- Status: drafted`

9. **WS0 site-count reconciliation (Gate A path-(a)): initial §7.1-based exclusion of AGENTS.md / CLAUDE.md reversed; both files bumped to v3.0.4.**
   - bash: `grep "v3.0.4" AGENTS.md CLAUDE.md` returns `Active framework version: AMAS v3.0.4` in both files
   - bash: `grep "3.0.3" AGENTS.md CLAUDE.md` returns no output (empty — v3.0.3 not present in either file)
   - Note: §7.1 governs sync-version / `template_version` marker (manifest is authoritative); it does not license a stale `Active framework version` positioning line. Accuracy + TASK-0052 precedent govern. Builder surface caught Architect ratification-surface §7.1 misapplication per §24.4 paired-discipline.

## Reviewer focus

1. **Canonical-text accuracy** — confirm §24.7 text matches spec verbatim; §23.6.5 empirical-grounding sentence accurately reflects TASK-0053 P2 finding at `docs/reviews/PR-100-codex-pre-commit.md` lines 120–131; §13.2 body-Status sentence and handoff-template.md bullet match Architect-supplied texts.
2. **WS3a completeness** — confirm zero "dual-signal" residuals across all tracked surfaces; confirm github-reference.md §6.3 breadcrumb uses correct "formerly labeled `dual-signal`" legacy-label framing.
3. **WS0 version-of-record classification** — confirm 11 sites bumped (3 trio frontmatter + README.md line 9 + 5 surfaces.yml + AGENTS.md + CLAUDE.md); historical references (README.md line 11 migration note) unchanged; no template_version values altered.
4. **Diff-stats sum-stability** — confirm Claim 1 shortstat matches per-file numstat column sums in both directions.
5. **Scope containment** — confirm no M-A7 count in §18.3 incremented; no ADR-010/011 or §6.1 enforcement-layer text touched; no template_version values changed; no historical version references (README.md line 11) altered.
6. **Ledger item confirmed / path-(β) deferred (Architect-ratified) — WS3c body-Status freeze-vs-refresh ambiguity**: body `- Status:` cadence (freeze-at-drafting vs refresh-at-gates) is intentionally deferred to a future cycle; Architect ratified path-(β) at pre-commit pass-1 adjudication 2026-06-10. Current §13.2 / handoff-template text is correct as written. See handoff §10 deferred-ledger entry for the interaction-note (refresh-at-gates ceiling + this cycle's self-instantiation). No action required this cycle.

## Codex desktop pre-commit kickoff

```
Please review the pending changes on branch fix/task-0054-predicate-hygiene per the review-context at docs/reviews/PR-102-codex-pre-commit.md.

Cycle scope: TASK-0054 predicate-hygiene — six workstreams: (WS0) patch bump 3.0.3→3.0.4 at 11 version-of-record sites (3 trio frontmatter + README.md + 5 surfaces.yml + AGENTS.md + CLAUDE.md); (WS1) new §24.7 Claim-artifact-parity section in core.md after §24.6; (WS2) §23.6.5 empirical-grounding extension with TASK-0053 cross-cycle confirmation sentence; (WS3a) "dual-signal" → "three-endpoint" rename at 4 sites (core.md ×2, github-reference.md ×2); (WS3b) ADR-008 D6 citation fix at core.md §18.4 (×2 strings); (WS3c) body-Status snapshot clarification at core.md §13.2 + templates/handoff-template.md Usage notes.

Per ADR-001 D11 owner-invokes convention: please run pre-commit review, surface findings per severity (Blocking → handback; Major → path-(a)/(β); Minor → default path-(b)). Substantive verdict via formal review preferred; issue-comment summary or line-level review-comments acceptable.

Verbatim-output convention: capture review verbatim into docs/reviews/PR-102-codex-pre-commit.md ## Codex desktop pre-commit output absorption section.

```

## Codex desktop pre-commit output absorption

### Review Summary

Verdict: REQUEST CHANGES

Blocking findings: none.

Major findings:

1. `core.md:724` — The new TASK-0053 empirical-grounding sentence overstates the cited source by saying the stale gate-current fields were "left stale after cycle completion" and by framing the confirmed case as "post-completion-gate staleness." The cited source at `docs/reviews/PR-100-codex-pre-commit.md:120-131` supports a narrower claim: after a post-PR fix-up commit, the TASK-0053 handoff still told a resuming Builder that the fix-up was in progress even though the same commit recorded the fix as applied. That source does not establish post-cycle-completion staleness in the merge/cycle-close sense. Please narrow the sentence to the verified artifact, e.g. "gate-current handoff fields left stale after a post-PR fix-up commit..." and "post-fix-up staleness," or otherwise cite a source that actually establishes cycle-completion timing.

Minor findings:

1. `docs/handoffs/TASK-0054-predicate-hygiene.md:115`, `docs/reviews/PR-102-codex-pre-commit.md:18`, and `docs/reviews/PR-102-codex-pre-commit.md:82` still carry pre-Gate-A-correction counts/classification. The handoff out-of-scope register says `AGENTS.md` / `CLAUDE.md` version positioning text is "excluded per §7.1" even though the staged diff modifies both files and the handoff's own Decisions section says the exclusion was reversed. The review-context heading says "8 files" while the staged shortstat is 10 files, and the embedded kickoff block still says WS0 covers 9 version-of-record sites while the Gate A-cleared scope is 11. These are documentary claim-artifact-parity defects in the review/handoff surfaces; update them or explicitly mark the older values as historical pre-correction state.

2. `core.md:259` and `templates/handoff-template.md:153` improve the body `- Status:` vs frontmatter distinction, but they still leave the freeze-vs-refresh rule underdetermined. The text establishes that the linked-pr-fix-up Action does not maintain the body field at merge, but it does not say whether the Builder should refresh the body `- Status:` at each hand-back/gate or freeze the value from initial handoff drafting. This cycle self-instantiates freeze-at-drafting (`status: active` frontmatter, body `- Status: drafted`), so the ambiguity is visible. Treat as the already-logged ledger candidate if intentionally deferred; otherwise add one sentence naming the intended lifecycle.

Validation notes:

- WS0 current version-of-record sites verify correctly: `core.md`, `github-reference.md`, `usage-guide.md`, `README.md`, `.amas/surfaces.yml` framework/canonical entries, `AGENTS.md`, and `CLAUDE.md` carry 3.0.4; the only remaining 3.0.3 reference in those version surfaces is the README historical migration note.
- WS3a verifies clean: no tracked Markdown occurrence of `dual-signal` remains; the `github-reference.md` §6.3 breadcrumb uses "formerly labeled `dual-signal`" as the single legacy breadcrumb.
- WS3b verifies clean: `core.md` §18.4 now cites ADR-008 D6, and ADR-008 Decision 6 is the release-track bump posture source.
- WS1 §24.7 is inserted after §24.6, and its cited surface targets resolve: §8.1.1.2, §24.3.1 Points 4-5, and §23.6.4 are present.
- Staged cumulative diff stats before this output absorption verified as 10 files, 288 insertions, 18 deletions; per-file numstat sums match in both directions.
- Frontmatter shape for the new handoff and review-context is parseable, and the handoff frontmatter is `status: active`.

Recommendation: Request changes for the Major source-fidelity issue in `core.md`; the two Minor findings can route through the default path-(b) cleanup unless the owner chooses to defer the body-status lifecycle wording to a future cycle.

### Pass-1 adjudication (Architect — 2026-06-10)

- **Major #1 (`core.md:724`)**: path-(a) — WS2 §23.6.5 sentence replaced with source-accurate framing: "after a post-PR fix-up commit, the handoff's gate-current fields still indicated the fix-up was in progress while that same commit recorded it as applied — a stale gate-current residual surfaced at post-PR review, confirming the gate-current predicate catches post-fix-up staleness, a case distinct from the by-design inter-gate staleness the taxonomy permits." Source-verified at edit time against lines 120-122 of PR-100 review-context (post-fix-up timing ✓, in-progress-vs-applied detail ✓, post-fix-up staleness framing ✓). §8.1.1.3 pass-2 exemption does NOT apply (content rewrite, not pure-token-swap); pass-2 required after re-staging.
- **Minor #1** (three residuals): path-(a) — (a) handoff out-of-scope register corrected: "excluded per §7.1" → "IN scope; both bumped"; (b) review-context heading corrected: "8 files" → "10 files"; (c) kickoff block corrected: "9 version-of-record sites" → "11 version-of-record sites (3 trio frontmatter + README.md + 5 surfaces.yml + AGENTS.md + CLAUDE.md)". Routed path-(a) by owner (leaving stale claims in the cycle that canonicalizes claim-artifact-parity is off-thesis).
- **Minor #2** (`core.md:259`, `templates/handoff-template.md:153`): path-(β) defer — body-`Status` freeze-vs-refresh cadence belongs in a dedicated future cycle; the likely-correct refresh-at-gates answer creates a ceiling (cannot reach `resolved`, which is Action-maintained on frontmatter only) making this cycle's self-instantiation non-conformant as a bolt-on. Current §13.2 / handoff-template text correct as written. Architect-ratified intentional deferral; recorded in handoff §10 deferred-ledger entry with interaction-note.
- **Post-PR annotation (Architect — 2026-06-10):** [Architect adjudication note (post-PR): the pass-1 Validation-notes assertion above ("WS3a verifies clean: no tracked Markdown occurrence of `dual-signal` remains") was found inaccurate at post-PR review — the broad `grep -r "dual-signal" --include="*.md" .` returns the intentional §6.3 breadcrumb plus this cycle's descriptive text and append-only historical docs. The live Claim 2 was corrected at `e929889` to a per-surface verification; see `docs/reviews/PR-102-codex-post-pr.md`. The verbatim above is preserved unedited per the PMN-002 (a) verbatim convention.]

### Codex desktop pre-commit pass-2 output

Verdict: CLEAN — no Blocking, Major, or Minor residual findings in the focused pass-2 scope.

Focused pass-2 checks:

1. WS2 §23.6.5 source-fidelity correction: PASS. The staged `core.md` sentence now states that after a post-PR fix-up commit, the handoff's gate-current fields still indicated the fix-up was in progress while that same commit recorded it as applied. That matches the cited PR-100 source at `docs/reviews/PR-100-codex-pre-commit.md:120-131` and no longer overstates the timing as cycle-completion or post-completion-gate staleness.

2. Minor #1 three residuals: PASS. The handoff out-of-scope register now says `AGENTS.md` / `CLAUDE.md` are in scope and both bumped to v3.0.4; the review-context cumulative-diff heading now says 10 files; and the embedded kickoff block now says 11 version-of-record sites with the expected site breakdown.

3. Minor #2 deferral framing: PASS. `docs/handoffs/TASK-0054-predicate-hygiene.md` §10 records the body-`Status` freeze-vs-refresh ambiguity as an Architect-ratified path-(β) deferred ledger item, including the interaction note that the cadence refinement belongs in a dedicated future cycle. `docs/reviews/PR-102-codex-pre-commit.md` also marks the item as no-action-required this cycle.

Validation notes:

- Staged tree verified at `10 files changed, 319 insertions(+), 18 deletions(-)` with numstat sums stable in both directions.
- The reviewed pass-2 changes stay within the stated focused scope; no new scope item is required before commit.

Recommendation: Proceed to commit after the owner/Builder completes the required stop-and-show sequencing. No pass-2 absorption fix-up is requested.
