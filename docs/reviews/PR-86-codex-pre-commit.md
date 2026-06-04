---
status: drafted
---

# PR-86 Codex desktop pre-commit review

## Metadata

- PR: PR-86 (anticipated; verified against live `gh pr list --state all` — highest merged = #85; phantom-correct at PR-open per PMN-001 (k))
- Branch: `feat/task-0048-part-c2-operating-discipline-canonical-surfaces`
- Cycle: TASK-0048 (Part C.2 operating-discipline canonical surfaces)
- Linked handoff: `docs/handoffs/TASK-0048-part-c2-operating-discipline-canonical-surfaces.md`
- Status: drafted
- Codex desktop session timestamp (UTC): <ISO-8601 — populated at pass>

## Builder claims to verify

1. **Five Part C.2 members materialized, document-ordered**. `grep -nE "^#{2,5} §(8\.2|8\.3|10\.5|13|13\.1|13\.2|23\.6\.5)\." core.md` → §8.2 → §8.3 → §10.5 → §13/§13.1/§13.2 → §23.6.5; §23.6.5 between §23.6.4 and §24. Class: PMN-010 sub-shape 1 (§-citation/structure).
2. **Each member carries schema elements + a checkable predicate + a Cross-references line** per spec §4.1–§4.4. Class: structural.
3. **In-scope qualifier residue = 0**. No `(forthcoming at Part C+)` (strict OR variant) references §8.2/§8.3/§13/§13.1/§13.2/§10.5/§23.6.5 or the materialized §17.5/§14. Class: PMN-010 sub-shape 1.
4. **STAY-13 preserved byte-unchanged**. usage-guide 62/306(×3)/308(×2)/346/348(×2)/394 + AGENTS:20 + github-ref 148/379 = 13, all present + unchanged. Class: (j) all-instances sweep.
5. **D2 migration materialized-only**. Root AGENTS/CLAUDE cite `core.md §8.2/§8.3/§13/§10.5/§14/§23.6.5`; §2.3.6 (+ §23.2) retained as v2.14.1 substrate (no over-migration); AGENTS:58 now `core.md §8.3`. Class: PMN-010 sub-shape 1.
6. **PR-template canonical converged + mirror no-op**. `templates/PULL_REQUEST_TEMPLATE.md` shows live §8.2/§8.3 attestations + `:56` migrated to `core.md §13/§13.1/§13.2` + Cross-references retained; `.github/PULL_REQUEST_TEMPLATE.md` byte-unchanged. Class: cross-document state.
7. **§10.5 → `github-reference.md` §3.2 cross-ref present; provenance untouched**. github-reference.md :148/:379 byte-unchanged. Class: PMN-010 sub-shape 1.
8. **Class A v2.45 4-site coherence + M-A7 35th internal consistency**. v2.45 ×2 README L9 + AGENTS L9 + CLAUDE L9; zero v2.44/v2.43. M-A7 concordant across 5 sub-claims (snapshot header v2.45/PR-NN/TASK-0048; enumeration 35 terms; span v2.45; count 35; preamble PR-13/v2.16). Class: PMN-010 sub-shape 1 + M-A7 enumeration verification.
9. **(XVII) bidirectional sum-stability**. Occurrence DROP 41 + REWRITE 14 + STAY 13 = 68; line-edit 37 DROP + 14 REWRITE + 1 bare-ref + 1 L546 = 53; cumulative-diff-stats re-derived (e.1) at final staged tree. Class: PMN-005 (e.1).
10. **All new/updated cross-references resolve**; zero open same-cycle forward-refs (§8.3→§10.5, §13.1/§13.2→§23.6.5 both resolved). Class: PMN-010 reference-verification.
11. **Anti-scope honored**: no Batch P4 Actions; no fold-in (§2.2.2/§2.3.4/§2.3.6/§2.3.7/§3.1/§5.4 STAY); no §10.6; PMN bounded to registration + first-evidence. Class: scope.

## Reviewer focus

- Schema-grade conformance: does each §8.2/§8.3/§13.x/§10.5/§23.6.5 carry an explicit, machine-checkable predicate (not prose-only) a v3.1 Action could read?
- §-citation resolution against current canonical state (post +128 authoring shift).
- The M-A7 `PR-NN` placeholder: confirm it is a deliberate manual-substitution placeholder (NOT Action-governed) at BOTH L583 + L585, flagged in the handoff Cycle-close ledger.
- §23.6.5 §10-disambiguation reads unambiguously (handoff-body §10 vs core.md §10).
- Recursive-self-instantiation salience: the handoff conforms to §13.1/§13.2 + §23.6.5 it canonicalizes (MEDIUM per PMN-008 §3.1).
- (j)/(g)/(h)/(i) sweeps on this review-context's own claim blocks.

## Codex desktop pre-commit kickoff

```
Please review the pending changes on the current branch (feat/task-0048-part-c2-operating-discipline-canonical-surfaces) per the review-context at docs/reviews/PR-86-codex-pre-commit.md. Working tree at staged-tree state.

Cycle scope: TASK-0048 Part C.2 — materialize the five operating-discipline canonical surfaces in core.md (§8.2 Builder pre-flight, §8.3 stop-and-show, §13/§13.1/§13.2 AI Session Log, §10.5 single-contributor bypass, §23.6.5 session-budget hand-back), each schema-grade (explicit schema elements + a checkable predicate a v3.1 Action could read + Cross-references). Plus the class-bound DROP(41)/REWRITE(14)/STAY(13) qualifier sweep, the D2 materialized-only root-file migration, the L546 + two Item-14 cross-ref migrations, the +1 bare-ref, Class A v2.44→v2.45 (4 sites), and the §18.3 M-A7 35th-instance amendment. Batch P4 Actions are DEFERRED to v3.1 (out of scope).

Pre-flight + stop-and-show context: step-1 pre-flight 16/16 PASS (entry b46e46e / v2.44 / M-A7=34, zero drift); every cluster + sweep + standard-surfaces pass cleared a stop-and-show; §5 battery 10/10 PASS at this Gate-A hand-back.

Per ADR-001 D11 owner-invokes convention: please run pre-commit review, surface findings per severity (Blocking → handback; Major → path-(a)/(β); Minor → default path-(b)). Pay special attention to: in-scope qualifier residue = 0 vs STAY-13 preservation; D2 materialized-only (no §2.3.6 over-migration); the M-A7 PR-NN manual-substitution placeholder; schema-grade checkable predicates; zero open forward-refs. Substantive verdict via formal review preferred; issue-comment summary acceptable; line-level review-comments acceptable.

Verbatim-output convention: capture review verbatim into the review-context file ## Codex desktop pre-commit output absorption section.
```

## Codex desktop pre-commit output absorption

### Codex pass 1 (pre-commit + comprehensive pre-merge red-team)

**Verdict**: 3 findings — 1 Blocking, 2 Major. All routed path-(a).

**Findings** (verbatim):

> **F1 — BLOCKING.** PR-85 is already MERGED (TASK-0047 PR-B close-reconciliation). The anticipation came from the stale handoff "highest = 84" instead of live verification. Run `gh pr list --state all` now; set the anticipated number to highest+1 (→ PR-86, barring an intervening PR). Correct PR-85 → PR-86 at handoff frontmatter linked_pr, handoff assumption, PMN-019 linked_pr, review-context body; AND `git mv` the review-context filename. M-A7 `PR-NN` (core.md L583/L585) is UNAFFECTED — leave it (manual, out of Action scope). HARDEN: at PR-open (step 9) re-run `gh pr list`; if the real number diverges, correct ALL anticipated-PR refs before the post-PR pass and merge (§8.2 pre-flight applied to PR-number anticipation: verify live state, not a prior handoff).
>
> **F2 — MAJOR.** New §13.1 requires session records to carry the §8.3 payloads WITH their owner ratifications (absence = violation). The handoff §13.1 record carries the ratification REQUESTS only. Update each §13.1 session entry to carry the §8.3 payload + the owner ratification that followed — make the cycle's own record conform.
>
> **F3 — MAJOR.** Re-label the handoff's append-only surfaces from "§Sub-phase execution record" / unnumbered "Cycle-close ledger" to the canonical §23.6.5 names "§3 step-by-step execution record" and "§10 cycle-close ledger." Do NOT change canonical §23.6.5 — it stands; the handoff maps to it.

**Adjudication** (per ADR-001 D11 / `core.md` §8.1.1.3):

- **F1** — path-(a) Blocking. Live `gh pr list --state all -L 5` confirms #85 MERGED (TASK-0047 PR-B close-reconciliation); highest = 85 → anticipated **PR-86**. Real verify-before-assert miss (trusted stale handoff over live state). Corrected all four anticipated-PR refs + renamed the review-context file; M-A7 `PR-NN` left untouched (manual, out of Action scope); cycle protocol hardened with a PR-open live re-verification step.
- **F2** — path-(a) Major. The handoff is the cycle's own §13.1 record and must conform to the §13.1 grammar it canonicalizes; updated the session entry to pair each §8.3 stop-and-show payload with its owner ratification.
- **F3** — path-(a) Major. Re-labelled the handoff's append-only surfaces to the canonical §23.6.5 names; canonical §23.6.5 unchanged.

**Resolution applied** (path-(a)):

- F1: PR-85 → PR-86 at handoff `linked_pr` (L8) + §Assumptions; PMN-019 `linked_pr` (L4); review-context title + Metadata + kickoff; `git mv PR-85-codex-pre-commit.md PR-86-codex-pre-commit.md`. Handoff Exact-next-step hardened with PR-open re-verification (§8.2 applied to PR-number anticipation). Verify: `gh pr list --state all` highest = 85; `grep -rn "PR-85" docs/` returns no anticipated-PR ref.
- F2: handoff §13.1 session entry now carries, per stop-and-show, the §8.3 payload + owner ratification. Verify: handoff §13.1 "Stop-and-show points reached" lists payload+ratification pairs.
- F3: handoff legend + surface headings now read "§3 step-by-step execution record" + "§10 cycle-close ledger." Verify: `grep -n "§3 step-by-step\|§10 cycle-close" handoff` resolves; canonical `core.md` §23.6.5 byte-unchanged.
- PMN-019 §2 first-evidence updated: F1/F2/F3 recorded as red-team caught-here-but-missed-upstream monitoring evidence.

## Codex post-PR review output absorption

Three-endpoint poll per `core.md` §8.1.1.1 (reviewed commit `9098bd2`): endpoint (a) formal review = COMMENTED boilerplate (points to line comments); endpoint (b) issue-comment = owner `@codex review` invocation; **endpoint (c) line-level = the substantive verdict (1 P1)**.

### Codex post-PR pass 1 (UTC 2026-06-04T00:02)

**Verdict**: 1 P1 finding (line-level), routed path-(a).

**Finding** (verbatim):

> **[P1] Record ratification for the final Gate A payloads** (`docs/handoffs/TASK-0048-…:113`). In the committed PR state these stop-and-show entries are no longer pending: the PR/commit record says Gate A was re-cleared and commit/push/PR-open were authorized, while the review-context claims F2 was fixed by pairing each §8.3 payload with owner ratification. Leaving these §13.1 entries as `awaiting ratification` / `awaiting Gate A re-application` means the handoff still lacks the owner-ratification half for the Gate A and absorption payloads, so the cycle's own durable record remains non-conformant with the new §13.1/§8.3 predicate.

**Adjudication** (per `core.md` §8.1.1.3): **path-(a) revise**, P1 load-bearing. Subsequent finding in the §13.1-conformance class (same class as the pre-commit F2), but load-bearing — a real conformance defect in the committed durable artifact — so the cost-class refinement routes path-(a) regardless of repetition. NOT suppression-clause-protected: the §13.1 predicate requires the ratification half; "awaiting" for a now-completed ratification is a missing required field (§23.6.4 describe-state-as-complete-at-commit), not a protected pinned historical value. Codex correct.

**Resolution applied** (path-(a)): handoff §13.1 final entries updated to record the completed ratifications — Pass C / Gate A → **owner ratified (Gate A cleared)**; Codex pre-commit absorption → **owner ratified (Gate A re-cleared)**; added commit/push/PR-open (step 9) → **owner authorized** (+ PR-open live re-verification: actual = anticipated PR-86); the only remaining `awaiting` entry is the in-progress post-PR fix-up (accurate as-of this commit). Hand-back point → Gate B. Canonical §13.1/§23.6.5 unchanged; canonical-law untouched (fix is handoff-artifact-only). Verify: `grep -c "awaiting" handoff §13.1` = 1 (the truthful in-progress entry only).

### Codex post-PR pass 2 (UTC 2026-06-04T00:37) — re-review against the UN-PUSHED commit

**Verdict**: 2 line-level findings (1 P1 re-stated, 1 P2 new), both against commit `9098bd2`.

**Findings** (verbatim):

> **[P1] Record ratifications for completed Gate A actions** (`…:113`). In the post-PR/Gate-B context being reviewed, these §13.1 entries are no longer genuinely pending: the pre-commit absorption was applied, and the commit/push/PR-open path was authorized per the PR-state log. Leaving the durable §13.1 archive with `awaiting` for these completed §8.3 payloads recreates the prior P1 and violates the new §13.1 enforcement-coupling…
>
> **[P2] Refresh gate-current handoff state for Gate B** (`…:34`). This gate-current surface still says the pre-commit review has not run and that the handoff is waiting for Gate A ratification, even though this re-review is explicitly post-PR… §23.6.5 suppression only protects append-only historical surfaces; the `GATE-CURRENT` sections are the handoff's receiving-state summary, so leaving them at Gate A misdirects the next reviewer/owner.

**Adjudication** (per `core.md` §8.1.1.3): **both findings are ALREADY RESOLVED in the staged-but-un-pushed post-PR-pass-1 fix-up.** ROOT CAUSE = **stale-commit re-review**: the pass-1 fix-up was held at the §8.3 fix-up stop-and-show (never pushed), so Codex re-reviewed the unchanged PR head `9098bd2`, which predates the fix. P1 (re-stated) ← resolved by the §13.1 completed-ratification edit; **P2 (new) ← resolved by the gate-current §Last-completed-step / §Current-state / §Exact-next-step refresh I applied proactively in pass-1 absorption** (P2 independently validates that refresh — and correctly notes §23.6.5 suppression does NOT cover gate-current surfaces). **No new content change required.** Resolution = **push the existing fix-up** so the next Codex re-review sees the fixed state. (Codex agreement with the proactive gate-current refresh is recorded as monitoring evidence for PMN-019 (iii) gate-current-refresh-at-each-transition.)

**Resolution applied**: none beyond pass-1 (findings pre-resolved). Action required = owner ratifies the fix-up push (§8.3); on push, the §13.1/gate-current entries are refreshed to the completed-ratification state per §23.6.4 so the pushed commit is conformant.

### Codex post-PR pass 3 (UTC 2026-06-04T01:04) — re-review against the FIXED HEAD `e7513a9`

**Verdict**: 1 P2 finding (line-level), routed path-(a). (First pass against the actual fixed commit — the relay-ordering desync is resolved; P1 + pass-2 P2 confirmed cleared.)

**Finding** (verbatim):

> **[P2] Refresh the legend's gate-current state** (`…:18`). In the post-PR/Gate-B handoff state, this legend still asserts that the handoff's gate-current surfaces reflect the Gate A pre-commit state, while the actual `Last completed step`, `Current state Summary`, and `Exact next step` sections now describe the post-PR / Gate-B-approach state. Because this sentence is the current taxonomy pointer rather than an append-only historical entry, it can misdirect the next reviewer into treating the refreshed surfaces as intentionally pinned to Gate A.

**Adjudication** (per `core.md` §8.1.1.3): **path-(a) revise**, P2 load-bearing. Same class as pass-2 P2 (gate-current staleness) — a **recurrence caused by an incomplete refresh**: pass-2 absorption instance-fixed the gate-current *section headings/content* but missed the §23.6.5 *legend pointer* (L18) and the §Cumulative-diff-stats *"re-derived at Gate A"* pointer (L44). This is exactly the §23.6.4 narrow-scope-refresh-leaves-residual-staleness failure mode. Cost-class: load-bearing → path-(a). **This time class-swept**: grep'd ALL `Gate A` / gate-current-state references; the stale-pointer class = {L18 legend, L44 diff-stats pointer}; the historical `Gate A` mentions (L34 "cleared twice", §3/§13.1 records) are correct and retained.

**Resolution applied** (path-(a), class-swept): (1) L18 legend → "reflect the **post-PR / Gate-B-approach** state"; (2) L44 → the re-derived full staged total **by pointer** (see §Cumulative-diff-stats / the PR diff; the *stable* gate-current figure is the canonical +187/−61), dropping the stale "re-derived at Gate A". No other stale gate-current pointer remains. Canonical-law byte-unchanged. Logged as PMN-019 (ii) class-sweep-not-instance-fix monitoring evidence (the pass-2 instance-fix should have been a class-sweep; pass-3 caught the residual). *(Pass-4 note: this resolution text originally pinned the volatile total "+478/−61" — itself a recurrence of the self-volatile-pinned-total class; corrected to by-pointer per §23.6.5 reference-volatile-by-pointer.)*

### Codex post-PR pass 4 (UTC 2026-06-04T01:25) — re-review against `aa309fe`

**Verdict**: 1 P2 finding (line-level), routed path-(a). (Pass-4 confirmed pass-3's gate-current class-sweep landed; the only residual was this review-context's own pinned total.)

**Finding** (verbatim):

> **[P2] Record the pass-3 diff total after the fix-up** (`docs/reviews/PR-86-codex-pre-commit.md:120`). This says L44 was updated to the current total of `+478/−61`, but at this HEAD the PR diff is `13 files changed, 493 insertions(+), 61 deletions(-)` and the handoff's L44 now records `+493 / −61` … leaving the audit record internally inconsistent with the fixed-point claim.

**Adjudication** (per `core.md` §8.1.1.3): **path-(a) revise**, P2 load-bearing. **2nd recurrence of the self-volatile-pinned-total class** (pass-3 = legend/L44 pointers; pass-4 = this review-context resolution pinning "+478"). Codex correct. Root cause: a *narrative* record pinned a self-volatile total, which the terminal-fix (L44 478→493) then superseded. **Resolution = de-pin, not re-pin** — narrative records reference volatile state **by pointer** per §23.6.5 (NOT the deferred L44 gate-current refinement). Class-swept all pinned-total references: kept the *stable* canonical +187/−61 (§Cumulative-diff-stats L42), de-pinned the review-context resolution → by-pointer, re-derived L44 (gate-current full-total) to fixed-point.

**Resolution applied** (path-(a), de-pin): review-context resolution (L120) "+478/−61" → by-pointer; pass-4 record (this section) references totals by pointer only; handoff §13.1 + gate-current refreshed (pass-4 push ratification recorded; next re-review framed pass-agnostically); L44 re-derived to fixed-point. PMN-019 (ii) updated: 2nd recurrence logged; the §23.6.5-refinement candidate (de-pin L44's self-volatile full-total, keep only the stable canonical figure as gate-current) strengthened to 2 data points — surfaced to owner for a ratification decision at the fix-up stop-and-show.

### Codex post-PR pass 5 (UTC 2026-06-04T01:46) — re-review against `7daa361`

**Verdict**: 1 P2 finding (line-level), routed path-(a). **First finding in canonical text** this arc (all prior post-PR findings were handoff/review-context artifacts) — the de-pin (pass-4) converged the self-volatile-pinned-total class; pass-5 surfaced a genuine internal contradiction in the §23.6.5 text authored this cycle.

**Finding** (verbatim):

> **[P2] Clarify the append-only pinned-value rule** (`core.md:711`). This blanket statement says append-only historical surfaces must reference volatile state by pointer, not by pinned value, but the same new §23.6.5 suppression clause below says a pinned value in an append-only surface is correct-by-design historical record. In contexts where an append-only record quotes prior diff totals or verbatim reviewer output, this internal contradiction can make valid historical values look like §23.6.5 violations; narrowing this sentence to current/gate-state references would keep the taxonomy consistent.

**Adjudication** (per `core.md` §8.1.1.3): **path-(a) revise**, P2 load-bearing. First finding in the **§23.6.5-internal-consistency** class. Codex correct — the unqualified "not by pinned value" rule contradicts the suppression clause (which protects pinned *historical* values). Self-instantiation note: this very arc created the conflict's trigger (passes 3–4 produced append-only records quoting prior totals "+478/+493" + verbatim Codex output — exactly the historical pinned values the rule would wrongly flag). **This is a canonical-law change** (core.md §23.6.5), unlike the prior artifact-only post-PR fix-ups.

**Resolution applied** (path-(a)): `core.md:711` narrowed — the by-pointer rule now governs **current/live** volatile state; a value pinned as a **historical snapshot** (prior diff totals, verbatim reviewer output) is explicitly carved out as correct-by-design per the suppression clause. In-place edit (no core.md line-count change → canonical figure +187/−61 unchanged). Canonical §23.6.5 suppression clause + checkable predicate intact; the deferred core.md/handoff-template *structural* refinement (PMN-019 candidate) is unaffected. Gate A re-cleared on the canonical change; push ratified.

### Codex post-PR pass 10 (UTC 2026-06-04T13:27) — re-review against `eb09645`

**Verdict**: 1 P2 (line-level), path-(a). **Reverse-direction completion** of the pass-9 §10.5 reconciliation. Pass-10 confirmed the pass-9 core.md fixes landed; the residual was on the usage-guide side. **STAGED, not pushed** (canonical-trio change; standing stage-and-hand-back rule).

**Finding** (verbatim):

> **[P2] Align merge guidance with optional bypass acknowledgment** (`usage-guide.md:118`). For single-contributor merges, this sentence still tells operators to use bypass "with explicit acknowledgment in the squash-commit message or a pinned PR comment," but the newly materialized `core.md` §10.5 and `github-reference.md` §3.2 both say GitHub's automatic bypass log is the acknowledgment and no additional artifact is required at single-cycle scope… readers following §3.9 (and the one-page bypass reference later in this file) will still treat an optional artifact as mandatory…

**Adjudication** (per `core.md` §8.1.1.3): **path-(a) revise**, P2 load-bearing. Same cross-surface-consistency class as pass-9, **opposite direction**: pass-9 aligned core.md §10.5 to usage-guide §3.9's "no additional artifact" clause, but §3.9 *also* carried mandatory-sounding "with explicit acknowledgment in…" phrasing (internally inconsistent) — and the one-page bypass reference (L402) repeated it. Codex correct. The pass-9 "usage-guide unchanged" claim was incomplete: usage-guide's own phrasing needed alignment to the canonical "optional" posture.

**Resolution applied** (path-(a), usage-guide.md — 2 lines):
- **§3.9 (L118):** "uses GitHub's bypass mechanism **per `core.md` §10.5**" + "each invocation is logged automatically + is itself the acknowledgment; **no additional artifact required at single-cycle scope** (squash-msg/pinned-comment **optional, not required**)."
- **One-page bypass rule (L402):** "GitHub's automatic bypass log is the acknowledgment; no additional artifact required (squash-msg / pinned-comment / PR-template `Bypass used` field **optional**)."

core.md byte-unchanged this fix-up; github-reference.md byte-unchanged (it already said "optional"). Canonical figure: usage-guide 14/14 → 15/15 (L402 was previously unchanged vs main); canonical+operational +188/−61 → **+189/−62**. **STAGED; awaiting Gate A + push ratification.**

---

### Codex post-PR pass 9 (UTC 2026-06-04T13:09) — re-review against `173484e`

**Verdict**: 3 findings (2 P1, 1 P2), all path-(a), all **new distinct classes** (cross-surface consistency between materialized canon and `usage-guide.md` / `github-reference.md`). Pass-9 confirmed pass-8 §8.2 timing fix landed. **STAGED, not pushed** (per the standing canonical-fix-up stage-and-hand-back instruction).

**Findings** (verbatim, abridged):

> **[P1] Enforce pre-flight before branching or editing** (`core.md:177`). The §8.2 predicate only requires the report before the first remote-visible action, but the output form + `usage-guide.md` §3.3/§12 place pre-flight before branch creation / repo-writing — a Builder could branch + author files with no pre-flight and still pass, missing the branch/base-state mistake class.
>
> **[P1] Reconcile the bypass acknowledgment surface** (`core.md:221`). §10.5 requires the durable bypass record in the §13 AI Session Log, but `github-reference.md` §3.2 + `usage-guide.md` §3.9 say GitHub's automatic log suffices / no additional artifact required → §10.5's predicate can fail a merge the operational guides explicitly allow.
>
> **[P2] Add PR edits to the stop-and-show trigger list** (`core.md:193`). §8.3 omits `gh pr edit`, which `usage-guide.md` §12 gates; PR-body edits are remote-visible and mutate Session Log / bypass / validation claims.

**Adjudication** (per `core.md` §8.1.1.3): all **path-(a) revise**, first-finding-in-class each; verified real against the cross-referenced surfaces (github-reference §3.2 + usage-guide §3.3/§3.9/§12 read directly). Cross-surface internal-consistency class — the materialized canon over-/under-specified relative to its sibling trio surfaces.

**Resolution applied** (path-(a), 3 canonical edits to core.md):
- **P1-a §8.2** (intro + predicate): pre-flight required **before branch creation and the first repo-writing/remote-visible action** (not merely before push); a session that branches/authors with no preceding pre-flight is a §8.2 violation even if a report later appears before push. Aligns with usage-guide §3.3 + the §8.2 output form.
- **P1-b §10.5** (predicate (5) + acknowledgment surface + checkable predicate + reconciliation line): acknowledgment = GitHub's automatic bypass log; **no additional artifact required at single-cycle scope** (§13 / squash-message / pinned-comment optional). Aligns with github-reference §3.2 + usage-guide §3.9; github-reference.md + usage-guide.md unchanged (canon aligned to them).
- **P2 §8.3** (trigger list): added `gh pr edit` (+ any post-creation PR-body mutation). Aligns with usage-guide §12.

Canonical figure re-derived (the §8.3 `gh pr edit` bullet adds +1 line; see handoff §Cumulative-diff-stats). **STAGED; awaiting Architect Gate A + push ratification.**

---

### Codex post-PR pass 8 (UTC 2026-06-04T12:52) — re-review against `d8f9d9b`

**Verdict**: 1 P2 finding (line-level), routed path-(a). Pass-8 confirmed §13.1 by-pointer fix landed + the by-pointer class exhausted; surfaced a **new, distinct-class** logic defect in §8.2 (pre-branch timing).

**Finding** (verbatim):

> **[P2] Check the proposed branch before pre-branch pre-flight** (`core.md:168`). When §8.2 is run at the pre-branch stop-and-show (the section's own output form and `usage-guide.md` §3.3 both put this before branch creation), the current working branch is still typically `main`, so requiring the **working branch** to match the task-branch regex makes a conforming pre-branch pre-flight fail or encourages Builders to create the branch before the branch-name check. This should validate the proposed branch name at pre-branch time, or distinguish pre-branch from post-branch evidence.

**Adjudication** (per `core.md` §8.1.1.3): **path-(a) revise**, P2 load-bearing. **First finding in the §8.2-pre-branch-timing class** (distinct from the by-pointer-consistency class; NOT a recurrence). Codex correct — and self-instantiating: this cycle's own step-1 pre-flight ran on `main` pre-branch and reported "16/16 PASS" only by silently validating the *proposed* branch name, not the working branch (which was `main`, non-conforming). The canonical item (4) text said "the working branch matches," contradicting the pre-branch output-form timing.

**Resolution applied** (path-(a)): `core.md:168` item (4) now distinguishes **pre-branch** (validate the *proposed* task branch name) from **post-branch** (verify the actual working branch), with an explicit note that at pre-branch time the working branch is the base branch and must not be the regex target. §8.2 output form (pre-branch stop-and-show) + predicate + cross-refs unaffected. Canonical figure re-checked below.

---

### Codex post-PR pass 7 (UTC 2026-06-04T10:31) — re-review against `a6aca94`

**Verdict**: 1 P2 finding (line-level), routed path-(a). Pass-7 confirmed §23.6.5 internal contradiction resolved; surfaced the same live-vs-historical-snapshot ambiguity now in §13.1.

**Finding** (verbatim):

> **[P2] Narrow §13.1's by-pointer rule to live state** (`core.md:237`). When a §13.1 record is used as the durable home for §8.3 payloads, those payloads can include the historical diff/impact summary required by §8.3; this sentence still says cumulative-diff-stats must be referenced by pointer, not pinned by value. That leaves the same current/live-vs-historical-snapshot contradiction in §13.1 that §23.6.5 now fixes, so valid historical payload values can still read as §13.1 violations unless this rule is scoped to current/live volatile references or explicitly inherits the historical-snapshot carveout.

**Adjudication** (per `core.md` §8.1.1.3): **path-(a) revise**, P2 load-bearing. **First finding in the §13.1-by-pointer-consistency class** — the pass-5 §23.6.5 fix exposed the parallel in §13.1 (the §23.6.5 fix cited §23.6.5 as the authority; §13.1 had its own identical unqualified form). Codex correct. Parallel-class resolution: narrow §13.1:237 to **current/live** volatile state, inheriting the §23.6.5 historical-snapshot carveout. In-place edit (net-zero line count → canonical figure +187/−61 unchanged).

**Resolution applied** (path-(a)): `core.md:237` narrowed — "Volatile state (cumulative-diff-stats, current step, next step) is referenced by pointer, not pinned by value" → scoped to current/live state; historical snapshots (§8.3 payload diff/impact summaries, verbatim Reviewer output) carved out as correct-by-design per the §23.6.5 suppression-clause logic. §13.1 predicate + enforcement-coupling + cross-refs intact. Canonical figure +187/−61 unchanged (in-place).

---

### Codex post-PR pass 6 (UTC 2026-06-04T10:06) — stale-head re-flag against `7daa361`

**Verdict**: 1 P2 (line-level), routed **path-(β) record-and-proceed** — stale-head re-flag, not a new defect.

**Finding** (verbatim):

> **[P2] Narrow by-pointer rule to live references** (`core.md:711`). This still says all append-only historical surfaces must reference volatile state by pointer "not by pinned value." For historical snapshots that intentionally preserve the value that was true when written (e.g., prior diff totals or verbatim reviewer-output records), this conflicts with the §23.6.5 suppression clause… Please scope the by-pointer requirement to current/live references so historical snapshot pins are not simultaneously required and forbidden.

**Adjudication** (per `core.md` §8.1.1.3): **path-(β) record-and-proceed**. Same finding, same class, same line as pass-5 P2. **ROOT CAUSE = relay-ordering desync (2nd instance)**: the pass-5 fix-up was staged but awaiting Architect Gate A re-clear on the canonical change; Codex re-reviewed the un-pushed `7daa361` and re-flagged the unchanged text. The staged fix-up pre-resolves this finding exactly. **No new content change.** PMN-019 (iii) relay-ordering observation strengthened to 2 instances (pass-2 + pass-6).
