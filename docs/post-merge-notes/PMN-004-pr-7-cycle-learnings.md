# PMN-004 — PR-7 cycle learnings: claim-text drift defect class + pre-commit discipline confirmation + two-endpoint empirical validation

## Status

Recorded — 2026-05-02

PMN-004 inserts under ADR-003 Decision 3 contingency budget. Consumes one of seven contingency slots; six remaining (TASK-0021 through TASK-0026 unconsumed).

## §1. Cycle context

PR-7 (TASK-0007) authored ADR-003 + README full sweep + ADR-001 Status update + 50-stub frontmatter sweep. Total cycle delta: 55 files changed (3 new + 52 modified). The cycle was structurally large but content-substantively narrow: one ADR file, one mechanical sweep across 50 stubs, one README modification across 7 sub-tables, one single-line ADR-001 Status update. PR-7's deliverable spec was approximately 1,094 lines of Architect-authored content with §23.6 self-review applied prior to handoff.

PR-7 deliverable spec §16 anticipated "one to three PMN-class observations from the PR-7 cycle (modest scope; ADR + sweep is structural rather than substantive content authoring)." The actual cycle generated five PMN-class candidate observations. The over-yield does not indicate the cycle was unusually defective; it indicates the deliverable's authoring discipline was tested at the limits of the framework's instrumentation. Specifically, the same defect class (claim-text drift across surfaces) appeared at multiple scales — within Architect-authored content, across path-(a) revision boundaries, in informal prose, and in section-citation references.

PR-7 cycle verification chain: §8.2 pre-flight PASS at SHA 0f93eada37c1d5563946ee911b6016d72dc75803; §10 step-10 self-verification PASS first pass; §11 Codex desktop pre-commit review three passes to clean (pass 1: 4 Blocking + 2 Major findings; pass 2: 3 Blocking findings; pass 3: clean — totaling 9 pre-commit findings caught and corrected); §15 post-PR Codex cloud review two passes to clean (pass 1: 1 P2 line-level on README Roadmap arithmetic; pass 2: clean — verdict landed only on issue-comment endpoint, not formal Pull Request Review endpoint). 11 path-(a) revisions across 7 distinct artifact loci (review-context claims 2, 4, 6, 7, 10; review-context §24 focus bullet; handoff Validation run + Evidence line; README Roadmap line). Zero path-(b) record-and-proceed acceptances. Owner adjudication on three stop-and-show occasions (Findings 1+2 pre-Codex; Codex pass 1; Codex pass 2 plus one proactive). Squash-merge by `@bryce-murphy` at 2026-05-02T01:55:11Z, merge commit `4ac4640`.

## §2. Defect class characterization — claim-text drift across multiple authored surfaces

### §2.1. The defect class

When the same factual claim (a numeric count, a verification command, a file path, a section-number citation, an arithmetic decomposition) appears across multiple authored surfaces in a single deliverable, inconsistencies between surfaces are easy to introduce and easy to miss. The PR-7 deliverable's surfaces included: review-context claims (10 enumerated), review-context Reviewer focus areas, review-context Reviewer-direction shape, handoff §Risks + §Validation run, spec §13.1 self-review row, spec §7.3 verification expected-output, spec §9.1 commit message, spec §9.3 PR body, README modification spec section-citations, ADR-003 §Consequences narrative — at least ten distinct surfaces in a single 1,094-line deliverable.

The defect class differs from PMN-003 (a) refined ("recapitulation-consistency check after in-cycle path-(a) revisions") in three ways:

(i) PMN-003 (a) refined addresses recapitulation across the four claim-touched files after revision; the claim-text drift defect class addresses claim consistency across multiple surfaces *within* a single artifact and *across* multiple artifacts in the deliverable, including before any revision occurs.

(ii) PMN-003 (a) refined applies primarily to file-content recapitulation; the claim-text drift defect class includes prose-arithmetic claims, verification-command outputs, section-number citations, and informal narrative consistency.

(iii) PMN-003 (a) refined is triggered by path-(a) revisions; the claim-text drift defect class is present at first-pass authoring time, before any revision.

### §2.2. Empirical evidence from PR-7

§23.6 Architect self-review caught five instances of the defect class pre-handoff (acknowledged in spec §13.1 as "first-pass error" corrections: commit-message file-count breakdown 4-new+51-modified vs correct 3-new+52-modified; §7.3 PowerShell .md count 41 vs correct 40; §7.3 PowerShell total 51 vs correct 50; PR body file count narrative; §13.1 self-review row referencing both variants). §23.6 self-review missed a sixth instance: §8 review-context claim 6 stating "41 .md / total 51" while §7.1 / §7.3 / §13.2 all stated 40/50. The Builder's first downstream verification caught the missed instance and surfaced it as a Major finding at stop-and-show §12 with path-(a) recommendation; Architect adjudicated path-(a) revise.

Codex desktop pre-commit review caught nine more instances across two passes: pass 1 (4 Blocking + 2 Major findings) included verification-command portability gaps (`Test-Path` is PowerShell-only), surface-scope misalignment in claim-7 (PR body referenced as pre-commit-verifiable when it does not exist at pre-commit time), future-tense claims with no pre-commit verification ("will be recorded in PR body"), and cross-surface count claim drift between review-context arithmetic and handoff Risks. Pass 2 (3 Blocking findings) included shell-portability of `head`/`wc`/`grep` commands in Windows cmd context and §24 focus pre-commit scope (the §24 cross-surface focus bullet referenced PR body as a pre-commit surface). Pass 3 clean.

Post-PR cloud Codex review caught one additional instance: README §5.2 Roadmap parenthetical "(PR-7 ADR-003 + PR-8 through PR-19 content + PR-19 release tag)" double-named PR-19 and implied 14 slots while the surrounding text said "thirteen substantive content PRs." This drift was in the spec source, transcribed verbatim per §5.2 instruction, and escaped both §23.6 Architect self-review (which checked structural counts but not informal prose arithmetic) and pre-commit Codex review (which checked verification-command outputs but did not re-derive arithmetic from prose).

Total empirical defects in this class on the PR-7 cycle: 5 (caught and corrected by §23.6 Architect self-review pre-handoff) + 1 (caught by Builder downstream verification, §8 review-context claim 6 41/51) + 9 (caught by pre-commit Codex review across two passes) + 1 (caught by post-PR cloud Codex review, README Roadmap arithmetic) = 16 total instances across one deliverable.

### §2.3. Mechanism

Each surface is authored at a different step of the deliverable construction. The claim instances are not generated from a single source of truth; manual reconciliation across surfaces fails when (a) the deliverable exceeds the working memory of the Architect's authoring session, (b) revisions to one surface are not propagated to all other surfaces by definition, (c) informal prose arithmetic is not subject to the same structural review as table-form arithmetic, and (d) section-number citations are sufficiently small-grain that they evade attention during structural sweeps.

Sub-finding from path-(a) revision propagation: in Codex pre-commit pass 2 → pass 3, a path-(a) revision to handoff Evidence line introduced a *new* claim-text drift (a `git ls-tree HEAD` output assertion that was incorrect by counting convention). The Builder caught it via §23.6 recapitulation-consistency re-check before pass 3, demonstrating that PMN-003 (a) refined applies but with extended scope: the recapitulation-consistency re-check on the four claim-touched *files* must extend to the four claim-touched *verification-command surfaces*, which is a slightly different scope than PMN-003 (a) refined originally specified.

## §3. Empirical case for pre-commit Codex desktop review — keep the gate

Pre-commit Codex desktop review caught nine findings across two passes that §23.6 missed. Three findings were Major (would have generated path-(a) revise post-PR but with elevated cost); six were Blocking (would have forced path-(a) revise post-PR with elevated cost). All nine would have surfaced post-PR otherwise.

Cost comparison:

| Path | Per-finding cost (post-PR) | Per-finding cost (pre-commit) |
|---|---|---|
| Detection | 1 cloud Codex review pass + 5-10min two-endpoint poll wait | 1 desktop Codex review pass against working tree |
| Correction | 1 fix-up commit + 1 push + 1 re-poll cloud-review pass | path-(a) revision in working tree before stage |
| Net cost per finding | ~1 commit + ~1 cloud pass + polling overhead | ~1 working-tree edit |

For nine findings, the pre-commit gate prevented approximately nine fix-up commits + nine cloud-review re-poll passes + nine polling overhead intervals. The pre-commit Codex desktop review remains mandatory; not optimized away as ceremony cost.

The pre-commit gate also has a useful property the post-PR gate does not: it operates on the untracked working tree before any commit history is written. Working-tree state can be revised arbitrarily without history pollution. Post-PR fix-up commits are visible in the squash-merge audit trail (PR-7's three commits — substantive + Linked-PR-fix-up + README-Roadmap-fix-up — were all preserved as the squash-merge body's "Squashed commits absorbed" enumeration).

## §4. Empirical confirmation of PMN-003 (e) refined two-endpoint discipline

PMN-003 (e) refined specified that post-PR Codex cloud reviews require polling on both `gh pr view --json reviews` (formal Pull Request Review endpoint) and `gh api repos/<owner>/<repo>/issues/<n>/comments` (issue-comment endpoint), with re-poll at 5-10 minute intervals if either endpoint is empty.

PR-7's post-PR review cycle empirically confirmed the discipline. Pass 1 (initial `@codex review` invocation) created a formal Pull Request Review on the formal endpoint at 2026-05-02T01:27:02Z (COMMENTED, with Approve verdict + 1 P2 line-level finding) and a corresponding issue-comment summary at 2026-05-02T01:23:19Z (full Approve summary). Single-channel polling on either endpoint would have caught pass 1.

Pass 2 (after Roadmap arithmetic fix-up), invoked by a second `@codex review` comment, did not create a new formal Pull Request Review. Pass 2's verdict appeared only on the issue-comment endpoint at 2026-05-02T01:44:25Z as `Codex Review: Didn't find any major issues. Swish!`. Single-channel polling on `gh pr view --json reviews` would have missed pass 2 entirely.

Mechanism: pass 1 was triggered by formal-review auto-fire on PR-open with reviewer-assignment metadata; this auto-fire creates a formal Pull Request Review object. Pass 2 was triggered by a second `@codex review` comment subsequent to pass 1's resolution; this routes through a different mechanism (comment-triggered review path) and produces only an issue-comment surface, not a new formal Pull Request Review.

The two-endpoint discipline + filtering by author and by `created_at` against last-known-state is the discipline that surfaces both pass forms reliably. PMN-003 (e) refined is empirically validated rather than theoretically anticipated. PMN-004 cross-references rather than re-derives.

## §5. Refined disciplines — six items

These disciplines are canonical via PMN-004 reference and apply to all subsequent cycles' Architect-authored deliverables. They will materialize in core.md Part B at TASK-0010 (when §23 enhancements canonicalize); they apply by reference now to all spec authoring.

**(a) Severity taxonomy three-level enumeration**: review-context files enumerate Blocking / Major / Minor with explicit definitions in `## Reviewer-direction shape` section. No two-level (Blocking / Minor) framing acceptable. Already standing per Meta-observation 1 of PR-6→PR-7 incoming session handoff. PMN-004 confirms standing.

**(b) Verification-command portability**: any verification command in claim text must be runnable in the shell environment available to whatever surface will execute it. Bash (Builder typical environment), Windows cmd (Codex desktop typical environment), or PowerShell (alternative Windows environment) forms must each be supplied or a shell-agnostic raw command output expectation must be specified. Single-shell-only commands without explicit "bash-only" qualifier are defects.

**(c) No future-tense claims at pre-commit time**: every Builder claim's verification command must produce verifiable output at pre-commit time against the working tree. Claims of the form "will be recorded in PR body," "will be verifiable post-stage," or "will be substituted at PR-open" are post-commit claims; they belong in post-PR verification scope, not pre-commit Codex desktop review scope. If a pre-commit-verifiable counterpart exists, the claim must reference that counterpart explicitly.

**(d) Pre-commit cross-surface scope clarity**: §24 cross-surface focus area in review-context files enumerates only pre-commit-existing surfaces (review-context, handoff, working-tree files modified in the PR). PR body, post-PR `@codex review` outcomes, merge-commit content, and other post-commit artifacts are post-commit verification scope; they are addressed in post-PR verification sections of the deliverable, not in pre-commit review-context Reviewer focus.

**(e) §23.6 prose-arithmetic decomposition**: §23.6 self-review extends to include decomposition of any informal prose arithmetic in the deliverable. Where any informal prose claim contains arithmetic — for example, "thirteen substantive PRs (PR-7 ADR-003 + PR-8 through PR-19 content + PR-19 release tag)" — §23.6 must decompose the parenthetical and verify the arithmetic against the structural counts elsewhere in the deliverable. Same discipline applies to count claims in commit message bodies and PR body summaries.

**(f) Spec source citation correctness sweep**: §23.6 self-review extends to include a sweep over all internal section-number references (e.g., "Hand back at §16" when actual hand-back is §14). Same defect class as the claim-text drift defect class but at the section-citation level. Sweep applies to thin pointer prompts, handoff Exact next step references, review-context Reviewer focus references, and any other surface that cites a section number elsewhere in the deliverable.

## §6. §23.6 enhancements — what materializes in core.md Part B (TASK-0010)

The PMN-004 §5 disciplines (a)-(f) apply by reference now via PMN-004. A subset of them — disciplines (a), (e), (f) — are §23.6-specific and will materialize as canonical §23.6 expansion text when TASK-0010 (core.md Part B authoring, §18-§24) lands. Disciplines (b), (c), (d) are not §23.6-specific; they apply to the deliverable construction discipline globally and may materialize in other §-sections (§14 handoff schema, §17 PR template, §8.1.1 review schema) as those sections are canonicalized.

The deferred materialization is acceptable because (i) the disciplines apply now by PMN-004 reference; (ii) canonicalization happens in dependency order per ADR-003 Decision 2 (§23 lives in Part B; Part B is PR-10 / TASK-0010 in the renumbered sequence post-PMN-004); (iii) the canonical text gets to absorb any further refinements observed during TASK-0009 (core Part A authoring, the first observation point post-PMN-004).

## §7. Anticipated forward integration

**TASK-0009 spec (next, core Part A authoring)** carries forward all six disciplines (a)-(f). Specifically: severity taxonomy three-level enumeration in PR-9 review-context (per (a)); verification commands in bash + cmd forms throughout (per (b)); all Builder claims are pre-commit-verifiable, with explicit post-PR claims segregated to post-PR verification sections (per (c) and (d)); §23.6 prose-arithmetic decomposition applied to the spec's content tables and prose narratives (per (e)); section-citation correctness sweep on the thin pointer prompt and all internal cross-references (per (f)).

**TASK-0010 spec (subsequent, core Part B authoring)** materializes §23.6 enhancements canonically. Disciplines (a), (e), (f) become canonical §23.6 sub-section text. Disciplines (b), (c), (d) materialize in their respective §-sections.

**Future PMN/ADR cycles** apply §5 disciplines globally. PMN-005+ and ADR-004+ inherit the disciplines as standing.

**Monitoring item M-A6**: PMN-rate-vs-budget tracking. Current rate 3 PMNs in 7 merged cycles (PMN-001 / PMN-002 / PMN-003) = 43% PMN frequency. Post-PMN-004: 4 PMNs in 8 merged cycles = 50%. ADR-003 Decision 3 forecast range: 3-7 PMNs across 13 substantive cycles = 23% to 54% rate. Currently within forecast range, in the upper half. Promotion trigger at TASK-0023 (3 contingency slots remaining: TASK-0024, TASK-0025, TASK-0026). At promotion: re-evaluate vs forecast; consider ADR-004 reservation extension if rate has stayed at or exceeded 50%; accept tail-cycle rate decrease if rate has dropped below 35%.

## §8. Cross-references

- **ADR-001** decisions 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15 unchanged; decision 8 PR sequence portion superseded by ADR-003 (per PR-7).
- **ADR-002** Decision 3 anticipation pattern absorbed and extended by ADR-003 Decision 3; PMN-004 inserts under ADR-003 Decision 3 contingency budget.
- **ADR-003** Decision 2 (12 substantive content PR plan, anticipated PR-8 through PR-19 in original numbering, shifted to PR-9 through PR-20 post-PMN-004); Decision 3 (TASK reservation through TASK-0026, consuming one contingency slot for PMN-004; six remaining); §Consequences (per-PR-row-update discipline for README and stub frontmatter, first empirically tested at PR-9 / TASK-0009 close).
- **PMN-001** (h.2) file-based Builder direction; (k) Linked PR fix-up substitution.
- **PMN-002** (a) refined imperative `Action:` phrasing; (d) code-fenced thin pointer prompt.
- **PMN-003** (a) refined recapitulation-consistency re-check (extended in PMN-004 §2.3 to include verification-command surfaces); (e) refined two-endpoint review polling (empirically confirmed in PMN-004 §4); (g) four-point Architect-side post-handback verification; (j) and (m) receiving-surface format declaration.
- **FEAT-0001** PR-2 v3 framework package scaffold spec — the staleness-defect substrate that ADR-003 + PR-7 sweep resolved structurally.
- **PR-7 (TASK-0007)** the cycle whose learnings PMN-004 captures.
- **Session handoff 2026-05-02** (PR-7 close → PMN-004 / TASK-0008 authoring) the source of the five candidate observations.
