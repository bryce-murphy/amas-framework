---
post_merge_note_id: PMN-019
title: TASK-0048 monitoring register — four TASK-0047 carry-in observations + first-evidence
linked_pr: PR-86 (Builder fills with squash SHA post-merge per PMN-001 (k))
framework_version_dogfooded: AMAS v2.44 → v2.45
status: drafted
---

# PMN-019 — TASK-0048 monitoring register — four TASK-0047 carry-in observations + first-evidence

## Status

Drafted at TASK-0048 (Part C.2 operating-discipline canonical surfaces; anticipated PR-86 — verified against live `gh pr list`, highest merged = #85; phantom-correct at PR-open). **Bounded to observation registration + first-evidence** per ADR-006 D3 observe-then-canonicalize; this is **NOT** a second substantive canonicalization. The four observations below ride the observe-then-canonicalize track — canonicalization (if warranted) follows at a future cycle once the evidence bar (3+ cross-cycle confirmations) is reached. Registration ≠ canonicalization.

## §1. Cycle context

TASK-0048 materialized the five Part C.2 operating-discipline canonical surfaces in `core.md` (§8.2 Builder pre-flight, §8.3 stop-and-show, §13 / §13.1 / §13.2 AI Session Log, §10.5 single-contributor bypass, §23.6.5 session-budget hand-back) and executed the class-bound DROP/REWRITE/STAY qualifier sweep + the D2 materialized-only operational migration across the just-relevant surfaces, plus standard cycle distributed-update (Class A v2.44 → v2.45, §18.3 M-A7 35th-instance, README roadmap rotation).

This PMN registers four monitoring carry-ins surfaced at TASK-0047 cycle-close as standing observations and records TASK-0048 as the **first post-registration evidence cycle** for each. The observation clock starts/continues here; the observations are not promoted to canonical text by this PMN.

### §1.1. Honesty record

- This PMN is authored at Gate A (pre-commit, staged-tree state); `linked_pr` carries the canonical PMN-001 (k) placeholder regex form (anticipated PR-86), substituted with the verified squash SHA at the post-merge chore.
- Recursive-self-instantiation salience: **MEDIUM→MAXIMUM** — observation (ii) class-sweep-not-instance-fix and (iii) gate-current-refresh-at-each-transition were actively practiced by this very cycle (see §2). **Empirical confirmation from the red-team**: the cycle's own handoff initially FAILED to conform to two disciplines this cycle canonicalizes — F2 (the §13.1 session record carried ratification *requests* only, not the §8.3 payload+ratification pairs §13.1 requires) and F3 (the handoff's append-only surfaces were not labelled with the canonical §23.6.5 names "§3 step-by-step" / "§10 cycle-close ledger"). Both were caught by the red-team and corrected. This is the strongest possible recursive-self-instantiation evidence: the artifact that canonicalizes a discipline must be audited against that very discipline, because first-draft conformance is not automatic. Flagged per PMN-008 §3.1. **Further confirmation (post-PR pass-5)**: the §23.6.5 *canonical text itself* carried an internal contradiction (the append-only "not by pinned value" rule vs the suppression clause's "pinned historical value is correct-by-design") — and this very cycle's post-PR records (passes 3–4 quoting prior diff totals + verbatim Codex output) were exactly the historical pinned values the unqualified rule would have wrongly flagged. The cycle thus generated the counter-example to its own freshly-authored canon, caught at post-PR re-review and fixed path-(a) (narrow the rule to current/live state). Canonical-text self-instantiation defects are real, not just artifact-level.
- No canonical-text proposal is advanced here; §2 records evidence only.

## §2. Monitoring register — four TASK-0047 carry-in observations

### §2.(i) Comprehensive pre-merge red-team

- **Observation**: a standardized full Codex desktop red-team at the pre-merge gate (in addition to the GitHub-App post-PR pass) is a candidate standing discipline for substantive canonical-text cycles.
- **This-cycle application + first-evidence**: the standardized red-team prompt first ran **prematurely** (against entry-state `main`, no diff) — the anti-phantom guard held (no findings fabricated against a non-existent diff). The **real pre-commit + pre-merge red-team then ran against the full staged diff and caught 3 path-(a) findings — 1 Blocking (F1, PR-85 stale-anticipation) + 2 Major (F2 §13.1 conformance gap, F3 §23.6.5 surface-name gap)** — all preventable, all absorbed before commit. **The trigger paid off**: a comprehensive pre-merge red-team caught a Blocking phantom-PR-number defect that the Builder's own §5 battery passed over (the battery verified frontmatter-regex conformance but trusted the stale anticipated number). Strong first-evidence that the standalone red-team is non-redundant with the Builder self-review.
- **Observe-then-canonicalize status**: 1 substantive cross-cycle data point (3 caught finds); continue observing toward 3+.

### §2.(ii) Class-sweep-not-instance-fix

- **Observation**: sweep a qualifier/citation population as a complete CLASS across all surfaces, never as a flagged-line list — instance-fix systematically under-counts.
- **This-cycle application + first-evidence**: produced **first-class evidence at the step-1b enumeration** — sweeping `(forthcoming at Part C+)` as a class surfaced **7 strict-literal-missed syntactic variants** (e.g. `(Part C.2; v2.14.1 §8.2 substrate)`, `(forthcoming at Part C.2)`, PR-template checklist attestations) **+ 2 stale Part-C.1 residues** (§17.5 @ usage-guide:332; §14-as-forthcoming) that an instance-fix would have missed. Reinforced at §4.6: materialization of §13.1/§13.2 surfaced a **stale-§13.1-attribution CLASS** (L546 + handoff-template:143 + templates L68/L69) — three surfaces an instance-fix of the one flagged line (L546) would have missed.
- **Counter-example (negative evidence, post-PR pass 3)**: the post-PR pass-2 P2 absorption **instance-fixed** the gate-current section headings/content but did NOT class-sweep ALL gate-current-state references — leaving the §23.6.5 legend pointer (L18) + the §Cumulative-diff-stats "re-derived at Gate A" pointer (L44) stale. Pass-3 caught the residual (a recurrence). Confirms the discipline by its breach: an instance-fix under-counted exactly as the observation predicts; the pass-3 resolution was done as a proper class-sweep (grep ALL `Gate A` refs → fix {L18, L44}, retain historical mentions). Strongest evidence yet — a measured cost of NOT class-sweeping within this very cycle.
- **Second recurrence (negative evidence, post-PR pass 4)**: pass-3's de-pin was itself incomplete — the pass-3 *resolution narrative* in the review-context pinned the volatile total "+478/−61", which the terminal-fix (L44 478→493) then superseded; pass-4 flagged the inconsistency. Resolution (correct this time): **de-pin, not re-pin** — narrative records reference the volatile total **by pointer** per §23.6.5 (kept only the stable canonical +187/−61 pinned at §Cumulative-diff-stats L42; L44 full-total re-derived to fixed-point). Two in-cycle recurrences of the **self-volatile-pinned-total** sub-class.
- **Observe-then-canonicalize status**: strong evidence (two positive instances + two negative/recurrence instances within one cycle); continue observing toward the 3+ bar.

### §2.(iii) Gate-current-refresh-at-each-state-transition

- **Observation**: gate-current handoff surfaces refresh at each gate transition; inter-gate staleness is by-design.
- **This-cycle application + first-evidence**: applied across **every cluster hand-back** this cycle (C1–C4 + §4.6 + §4.7 + this Gate-A pass) — §Cumulative-diff-stats re-derived (e.1) at each staged-tree mutation; §Last completed step + §Current state refreshed at each stop-and-show. This observation is now also **canonicalized as §23.6.5 text this cycle** (the taxonomy), so future evidence shifts from "observed practice" to "conformance against canonical §23.6.5."
- **Observe-then-canonicalize status**: practice-confirmed this cycle; the taxonomy reached its own evidence bar and was canonicalized at §23.6.5 (TASK-0046/0047 behavioral test #1). Continue monitoring §23.6.5 conformance.
- **Pass-2 agreement evidence**: the Codex post-PR pass-2 P2 independently flagged the gate-current surfaces as stale and correctly stated that **§23.6.5 suppression covers append-only surfaces only, NOT gate-current ones** — external confirmation of the gate-current/append-only boundary canonicalized this cycle.
- **Relay-ordering hazard (light observation; observe-then-canonicalize)**: the binding post-PR re-review (`usage-guide.md` §7.1/§7.3) must be **sequenced AFTER the finding-addressing push**. A process desync — re-review invoked while a fix-up is staged but un-pushed — causes Codex to re-flag the unchanged head with the same already-resolved finding. **Two in-cycle instances**: pass-2 (P1 + P2 re-flagged against un-pushed `9098bd2`; fix-up held at §8.3 stop-and-show) + **pass-6** (pass-5 P2 re-flagged against un-pushed `7daa361`; fix-up held awaiting Gate A re-clear on the canonical change). Candidate discipline: "push the fix-up THEN re-invoke" — 2 data points; continue observing toward 3+. Registration only; not canonicalized.
- **§23.6.5-refinement candidate (light; observe-then-canonicalize, NOT a this-cycle change)**: the handoff §Cumulative-diff-stats **full-staged-total** figure is **self-volatile** — every absorption push edits the handoff (and review-context/PMN), changing the total the figure records, so a gate-current full-total recurs stale at each commit and needs a fixed-point re-derivation each push (observed at pass-3: editing L44 to record the total is self-referential). Candidate refinement: reframe the full-staged-total line as a **commit-pinned snapshot** ("as of `<commit>`", append-only / §23.6.5-suppression-protected) rather than a gate-current pointer — keeping only the **stable canonical+operational figure** (byte-unchanged across artifact-only fix-ups) as the gate-current number. Registration only; defer canonicalization to a future §23.6.5 amendment cycle. **Strengthened at pass-4 to 2 in-cycle data points** (pass-3 = the gate-current pointers; pass-4 = the review-context resolution's own pinned total). Partial mitigation already applied this cycle as plain §23.6.5 *conformance* (narrative records reference the total by pointer; only the stable canonical +187/−61 stays pinned gate-current) — the *deferred* part is the structural reframe of L44's full-total to an append-only commit-pinned snapshot, surfaced to the owner for a ratification decision.

### §2.(iv) Claim-artifact-parity

- **Observation**: every claim asserted in a hand-back must have a corresponding verifiable artifact (measured, not narrated).
- **This-cycle application + first-evidence**: Codex's independent **entry-state corroboration** (the premature red-team independently re-measured entry `main` = b46e46e / v2.44 / M-A7=34) corroborated the Builder pre-flight; the **L546 finding** and the **materialized-vs-cited reconciliations** (every §5-battery claim backed by a shown grep/numstat). **Strongest evidence: F1** — the anticipated PR-85 was a *claim asserted without a live artifact* (the Builder trusted the entry-handoff's "highest = 84" instead of re-running `gh pr list`); Codex's live-state check exposed the parity break (PR-85 already MERGED). Confirms claim-artifact-parity must bind to LIVE state, not a prior artifact's assertion — now hardened into the cycle protocol (handoff §Exact-next-step PR-open re-verification).
- **Observe-then-canonicalize status**: strong first-evidence (a live parity break caught); continue observing toward 3+.

## §3. Cross-references

- **ADR-006 D3** — observe-then-canonicalize evidence-bar discipline (3+ cross-cycle confirmations).
- **`core.md` §23.6.5** — session-budget hand-back + gate-current/append-only taxonomy (observation (iii) canonicalized this cycle).
- **`core.md` §24.5 / §24.6** — multi-surface review pipeline + Stop-Iteration (observation (i) red-team context).
- **`core.md` §8.1.1.2 / §24** — claimed-action verification / verify-before-assert (observation (iv)).
- **PMN-001 (k)** — linked_pr placeholder substitution discipline.
- **PMN-008 §3.1** — recursive-self-instantiation salience framing.
- **TASK-0047 cycle-close** — origin of the four carry-in observations.
