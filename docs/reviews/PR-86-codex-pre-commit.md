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
