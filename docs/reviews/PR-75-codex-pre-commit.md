---
status: drafted
---

# PR-75 Codex desktop pre-commit review

## Metadata

- PR: PR-75 (anticipated; canonical at PR-open)
- Branch: `feat/task-0046-batch-p3-greenfield-prompt` per ADR-005 Option B + `github-reference.md` §2.2 regex
- Cycle: TASK-0046 — Batch P3 greenfield kickoff prompt (split cycle 1 of 2). Fill `prompts/greenfield.md` (stub → drafted); co-shipped: §18.3 M-A7 32nd-instance + Class A v-bump v2.41 → v2.42 + README roadmap L30 4-anchor post-split shift + README Prompts row + usage-guide L22/L370 forthcoming-qualifier sweep.
- Linked handoff: `docs/handoffs/TASK-0046-batch-p3-greenfield-prompt.md`
- Status: drafted | recorded (`drafted` at pre-stage / pre-Codex-pass; `recorded` post-merge per PMN-001 (k) Action substitution)
- Codex desktop session timestamp (UTC): <populated post Codex desktop pre-commit pass>
- Cycle class: Batch P3 substantive content-fill (prompt scaffold), split cycle 1 of 2 — §0 salience HIGH (first prompt-class cycle; §23.6.5 behavioral empirical test #1; recursive self-application)

## Builder claims to verify

**These claims are a snapshot at pre-commit Gate A.** Per the TASK-0046 §23.6.5 behavioral discipline (spec §7), this 12-claim block is append-only-historical: it is frozen at the pre-commit staged-tree state and is NOT back-edited when later absorptions change underlying facts. Post-absorption changes are recorded in the "Codex desktop pre-commit output absorption" / post-PR sections below, NOT retrofitted into these claims. Verified per `core.md` §8.1.1.2 phantom-action verification discipline + PMN-010 §-citation correctness.

1. **`prompts/greenfield.md` frontmatter transition landed (snapshot at pre-commit Gate A)**.
   - bash: `head -5 prompts/greenfield.md | grep -E "^status: drafted$"` returns 1 hit
   - bash: `head -5 prompts/greenfield.md | grep -E "^filled_by: PR-75 \(TASK-0046\)$"` returns 1 hit
   - bash: `head -5 prompts/greenfield.md | grep -E "^template_version: 3\.0\.0$"` returns 1 hit
   - Class: stub → drafted content-fill per spec §1 + ADR-003 `filled_by` update convention

2. **`prompts/greenfield.md` 7-obligation coverage (snapshot at pre-commit Gate A)**.
   - bash: `grep -cE "^## Step " prompts/greenfield.md` returns `7` (Step 0 context + Steps 1-6 = 7 section headers)
   - bash: `grep -nE "ecosystem-fallback guard" prompts/greenfield.md` returns ≥1 hit (obligation 4 guard present)
   - bash: `grep -nE "\* @your-github-username" prompts/greenfield.md` returns 1 hit (CODEOWNERS trip-up present)
   - bash: `grep -nE "TASK-0000 is reserved" prompts/greenfield.md` returns 1 hit (TASK-0000 trip-up present)
   - bash: `grep -nE "core\.md. §3\.1 \(forthcoming at Part C\+\)" prompts/greenfield.md` returns ≥1 hit (§3.1 referenced forthcoming, NOT materialized)
   - Class: 7 content obligations per spec §2, paste-ready operator prose; operator-usability ("will an operator know exactly what to answer/do next?") is the primary review priority per spec §9, alongside canonical-reference correctness

3. **`prompts/greenfield.md` bootstrap artifact set verbatim per usage-guide §2.3 (snapshot at pre-commit Gate A)**.
   - bash: `grep -nE "README .* CODEOWNERS .* AGENTS|CODEOWNERS|role-assignment-scorecard" prompts/greenfield.md` resolves the 11-item set (README, CODEOWNERS, AGENTS.md, CLAUDE.md, canonical-doc reference, project-brief, tool-inventory, role-assignment-scorecard, ADR-000, GitHub Issue templates, GitHub PR template)
   - bash: `grep -nE "lite kickoff|one-way" prompts/greenfield.md` returns ≥1 hit (lite-kickoff smaller-set + one-way-upgrade caveat present)
   - Class: bootstrap set enumeration matches usage-guide §2.3 exactly; no invented artifacts; §3.1 referenced as forthcoming (not materialized)

4. **`prompts/greenfield.md` citation resolvability (snapshot at pre-commit Gate A)**.
   - Every cited section resolves against current main: usage-guide §8 (three-tier), §9 (§23 walkthrough), §2.1/§2.3/§2.4/§2.5/§2.6/§2.7/§2.9; core.md §3.1 (forthcoming), §8.1.1, §23; project-initiation §7; template paths (`templates/project-brief-template.md`, `templates/tool-inventory-template.md`, `templates/role-scorecard-template.md`, `templates/ISSUE_TEMPLATE/project-initiation.md`).
   - Class: forthcoming-reference discipline — §3.1 cited `(forthcoming at Part C+)`, no unmaterialized-section over-assertion (spec §3)

5. **`core.md` §18.3 M-A7 32nd-instance amendment landed (snapshot at pre-commit Gate A)**.
   - bash: `grep -nE "as of v2\.42 canonicalization at PR-75 / TASK-0046" core.md` returns 1 hit (preamble)
   - bash: `grep -nE "\+ PR-73 \+ PR-75 = 32" core.md` returns 1 hit (count line)
   - bash: `grep -nE "spanning v2\.16 through v2\.42 canonicalization" core.md` returns 1 hit (span; same git line as count per (XXI) line-shared)
   - bash: `grep -nE "across 32 consecutive substantive cycles" core.md` returns 1 hit (steady-state)
   - Class: M-A7 promotion-pattern empirical 32nd instance per (XXI) line-shared substitution

6. **`core.md` §18.3 M-A7 zero residuals at v2.41/31 anchor strings (snapshot at pre-commit Gate A)**.
   - bash: `grep -c "= 31" core.md` returns `0`
   - bash: `grep -nE "PR-73 = 31|through v2\.41 canonicalization|31 consecutive substantive cycles|as of v2\.41 canonicalization at PR-73" core.md` returns 0 hits
   - Class: (j) all-instances grep sweep; prior-instance anchor strings fully replaced; other M-A7 doctrine/evidence mentions are non-count text (untouched by design)

7. **Class A v-bump v2.41 → v2.42 at 4 sites landed (snapshot at pre-commit Gate A)**.
   - bash: `grep -oE "v2\.42" README.md AGENTS.md CLAUDE.md | wc -l` returns `4` (README L9 ×2 + AGENTS L9 + CLAUDE L9)
   - bash: `grep -oE "v2\.41|v2\.40" README.md AGENTS.md CLAUDE.md` returns 0 hits
   - Note: `core.md` §18.3 historical-record `through v2.42 canonicalization` is legitimate M-A7 historical reference, NOT Class A scope
   - Class: minor v-bump per `core.md` §18.4 substantive-reading criterion; AGENTS/CLAUDE L12 roadmap text task-number-free (NOT v-bump sites; untouched)

8. **README roadmap L30 four-anchor post-split shift landed (Finding A) (snapshot at pre-commit Gate A)**.
   - bash: `grep -nE "Batch P3 greenfield \(TASK-0046\) → Batch P3 retrofit \+ upgrade \(TASK-0047\) → Part C\.2 \(operating-discipline; TASK-0048\) → release polish \+ v3\.0\.0 tag \(TASK-0049" README.md` returns 1 hit (end-sequence)
   - bash: `grep -nE "§10\.5 \+ §23\.6\.5\) anticipated at TASK-0048 before v3\.0\.0 release" README.md` returns 1 hit (mid-paragraph anchor — Finding A second anchor)
   - bash: `grep -c "TASK-0047) → Part C.2 (operating-discipline; TASK-0048)" README.md` confirms no stale pre-split sequence remains
   - Class: post-split task-number shift (greenfield 0046 / retrofit+upgrade 0047 / Part C.2 0048 / release 0049); both L30 anchors updated per Finding A; no 5th anchor (L7 task-number-free)

9. **README Prompts table greenfield row landed; retrofit/upgrade rows preserved (snapshot at pre-commit Gate A)**.
   - bash: `grep -nE "^\| .prompts/greenfield\.md. \| Project kickoff \(project-type-aware\) \| PR-75 \(TASK-0046\) \|$" README.md` returns 1 hit
   - bash: `grep -cE "Batch P3 \(ADR-006\); pending content-fill cycle" README.md` returns `2` (retrofit + upgrade rows unchanged)
   - Class: greenfield-only row update per spec §4.5; retrofit/upgrade remain pending (TASK-0047)

10. **usage-guide forthcoming-qualifier sweep at L22 + L370 landed (Finding B) (snapshot at pre-commit Gate A)**.
    - bash: `grep -nE "prompts/greenfield\.md. \(.prompts/retrofit\.md. \+ .prompts/upgrade\.md. forthcoming at TASK-0047\)" usage-guide.md` returns 1 hit (L22; greenfield live, retrofit/upgrade forthcoming at TASK-0047)
    - bash: `grep -nE ".retrofit\.md. \+ .upgrade\.md. forthcoming at TASK-0047\.$" usage-guide.md` returns 1 hit (L370 one-page reference)
    - bash: `grep -cE "prompts/(greenfield|retrofit|upgrade)\.md.*forthcoming at TASK-0025\+" usage-guide.md` returns `0` for the two swept lines (greenfield no longer forthcoming-grouped)
    - Note: §11.3 (`prompts/upgrade.md` (forthcoming at TASK-0025+)`) + L24 appendices line retained per anti-scope (report-only; see handoff §10 (V)); §1.2 + §2.1 carry no qualifier (untouched)
    - Class: greenfield-only qualifier drop per ADR-006 D4 retroactive-supersession-marking; (XXIV.k) parallel-form coherence; retrofit/upgrade preserved

11. **Frontmatter canonical conformance (snapshot at pre-commit Gate A)**.
    - bash: `head -14 docs/handoffs/TASK-0046-batch-p3-greenfield-prompt.md | grep -cE "^(task_id|title|pr|branch|linked_predecessor|linked_successor|linked_pr|framework_version_dogfooded|production_target|spec_source|date_authored|status):"` returns `12`
    - bash: `grep -E "^linked_pr: PR-75 \(Builder fills with squash SHA post-merge per PMN-001 \(k\)\)$" docs/handoffs/TASK-0046-batch-p3-greenfield-prompt.md` returns 1 hit (Adj 11 canonical regex placeholder; numeric digit per Action regex `PR-(\d+)`)
    - bash: `head -3 docs/reviews/PR-75-codex-pre-commit.md | grep -E "^status: drafted$"` returns 1 hit (§17.7 1-field)
    - Class: PMN-007 HEAD 12-field handoff + §17.7 1-field review-context conformance + Adj 11 regex placeholder form

12. **(XVII) bidirectional sum-stability + envelope (snapshot at pre-commit Gate A)**.
    - bash: `git diff --stat` aggregate equals per-file numstat sum at all 3 axes (ins / del / file-count); per-file rows sum to shortstat.
    - Envelope per spec §6: anticipated ~380-600 ins / ~12-18 del / 6-8 files; actual reported at Gate A stop-and-show. greenfield body 155 lines < ~260 substantive-scope-creep trigger; no retrofit/upgrade mode-logic added (trigger NOT met).
    - Class: (XVII) bidirectional sum-stability per spec §9 + Adj 8 (XIV) sweep; bookkeeping-class breach disposition (a) available per ADR-006 D3 if documentation content drives the upper band

## Reviewer focus

Per `core.md` §24.5 multi-surface review pipeline surface 3 (Codex pre-commit) + spec §9 verification priorities:

- **Greenfield prompt scaffold correctness + operator-usability**: do the 7 content obligations land as paste-ready operator guidance? The primary question per spec §9 is **"will an operator reading this know exactly what to answer/do next at each step?"** — not only canonical-reference correctness. Flag any step that reads as a checklist/outline rather than runnable session guidance.
- **Forthcoming-reference discipline**: §3.1 cited `(forthcoming at Part C+)`; no unmaterialized-section over-assertion; bootstrap set presented as operational guidance sourced through usage-guide §2.3, not as materialized canonical law.
- **§18.3 M-A7 32nd-instance (XXI) line-shared**: count line carries BOTH `+ PR-75 = 32` AND `through v2.42` at a single git line; preamble + steady-state amended independently; `= 31` residual = 0.
- **Class A v2.42 4-site coherence**: README L9 ×2 + AGENTS L9 + CLAUDE L9; zero v2.41/v2.40 residuals; AGENTS/CLAUDE L12 roadmap text correctly untouched.
- **README L30 Finding A two-anchor completeness**: both the mid-paragraph "anticipated at TASK-0048" AND the end-sequence reflect post-split numbering; no stale TASK-0047-as-Part-C.2 reference; Prompts greenfield row correct + retrofit/upgrade rows preserved.
- **usage-guide Finding B sweep**: L22 + L370 greenfield-forthcoming dropped (greenfield live), retrofit/upgrade retained forthcoming at TASK-0047; §1.2/§2.1/§11.3/L24 untouched.
- **Anti-scope**: NO retrofit/upgrade prompt content; NO `core.md` §3.1 materialization; NO §23.6.5 canonical-law text; NO other Part C.2 surfaces (§8.2/§8.3/§13/§10.5); NO usage-guide §-body edits beyond the qualifier sweep.
- **(XVII) bidirectional sum-stability** at staged tree (all 3 axes); Adj 11 canonical regex placeholder at handoff L8.

## §23.6.5 behavioral taxonomy for this review

This cycle applies the §23.6.5 refresh discipline **behaviorally** (text canonicalizes at Part C.2 / TASK-0048). The handoff (`docs/handoffs/TASK-0046-batch-p3-greenfield-prompt.md`) body surfaces fall in two tiers — Reviewer must apply this taxonomy when assessing staleness:

- **gate-current** surfaces (refreshed ONLY at gates — Gate A initial + each Gate A re-application after absorption + Gate B + Gate B re-applications; inter-gate staleness is by-design and is NOT a finding): **§Last completed step**, **§Current state Summary**, **§Cumulative-diff-stats**.
- **append-only historical** surfaces (only ever appended, never back-refreshed; they reference volatile state BY POINTER, e.g. "see §Cumulative-diff-stats", not by pinned value): **§3 step-by-step** execution record, **pre-commit absorption** section, **post-PR review** section, **§10 ledger**.

The governing rule is: `do not flag append-only historical surfaces as stale against post-absorption state`. A pinned value or step reference inside an append-only historical surface that no longer matches the latest staged-tree state is correct by design (it is a historical record of the state at the time that entry was appended), not a defect. Likewise, the pre-commit claims block in THIS review-context is a **snapshot at pre-commit Gate A** — append-only-historical; post-absorption fact changes are recorded in the absorption / post-PR sections below, not retrofitted into the claims. Staleness findings are in-scope ONLY against gate-current surfaces that were not refreshed at a gate where they should have been. The sole canonical cycle-close marker is action-filled frontmatter (`linked_pr` squash SHA + handoff `status: resolved` + this review-context `status: recorded`); no body surface is a close marker.

## Codex desktop pre-commit kickoff

```
Please review the pending changes on the current branch (feat/task-0046-batch-p3-greenfield-prompt) per the review-context at docs/reviews/PR-75-codex-pre-commit.md. Working tree at staged-tree state per TASK-0025 cycle-close Item 4 lesson.

Cycle scope: Batch P3 greenfield kickoff prompt (split cycle 1 of 2). Fill prompts/greenfield.md (stub → drafted) with the canonical paste-ready greenfield project-kickoff prompt (7 content obligations: preamble/attach-then-paste, operating-environment, three-tier framing, role-assignment scorecard + ecosystem-fallback guard, bootstrap artifact set production, kickoff follow-ups + first-feature handoff, cross-references). Co-shipped: core.md §18.3 M-A7 32nd-instance ((XXI) line-shared) + Class A v-bump v2.41 → v2.42 minor at 4 sites (README L9 ×2 + AGENTS L9 + CLAUDE L9) + README roadmap L30 four-anchor post-split shift + README Prompts table greenfield row + usage-guide L22/L370 forthcoming-qualifier sweep (greenfield only; retrofit/upgrade retained at TASK-0047) + TASK-0046 handoff + PR-75 pre-commit review-context.

Pre-flight HEAD anchor: post-PR-74-merge state at main (a030554).

Verification priorities at pre-commit (HIGH §0 salience; first prompt-class cycle):
- greenfield prompt scaffold correctness (7 content obligations) AND operator-usability — "will an operator know exactly what to answer/do next?" (paste-ready, not just a checklist), not only canonical-reference correctness
- forthcoming-reference discipline (§3.1 cited as (forthcoming at Part C+); no unmaterialized-section over-assertion)
- §18.3 M-A7 32nd-instance (XXI) line-shared (= 31 residual = 0)
- Class A v2.42 4-site coherence (zero v2.41/v2.40 residuals)
- README L30 Finding A two-anchor shift + Prompts row correctness (no stale TASK-number)
- usage-guide Finding B sweep (greenfield dropped; retrofit/upgrade preserved at TASK-0047)
- Adj 11 canonical regex placeholder at handoff L8
- anti-scope (NO retrofit/upgrade content; NO §3.1 materialization; NO §23.6.5 canonical text; NO Part C.2 surfaces; NO usage-guide §-body edits beyond the qualifier sweep)
- (XVII) bidirectional sum-stability

§23.6.5 behavioral taxonomy for this review: this cycle applies the §23.6.5 refresh discipline behaviorally. The TASK-0046 handoff body has gate-current surfaces (§Last completed step, §Current state Summary, §Cumulative-diff-stats) and append-only historical surfaces (§3 step-by-step, pre-commit absorption, post-PR review, §10 ledger). The rule is: do not flag append-only historical surfaces as stale against post-absorption state — pinned values inside them are historical records, correct by design. The pre-commit claims block in this review-context is a snapshot at pre-commit Gate A (append-only historical); it is not back-edited at absorption. Staleness findings are in-scope only against gate-current surfaces not refreshed at a gate.
```

## Codex desktop pre-commit output absorption

Populated post Codex desktop pre-commit pass-1 per `core.md` §8.1.1.2 phantom-action verification discipline; verbatim capture convention. Adjudication + Resolution sub-sections populated post Architect routing ratification at chat surface per ADR-001 D11. Per the §23.6.5 behavioral discipline: post-absorption fact changes are recorded HERE (append-only), NOT retrofitted into the pre-commit claims block above (which is frozen as the snapshot at pre-commit Gate A).

### Pre-commit pass-1 absorption (append-only-historical)

Codex desktop pre-commit pass-1: 2 substantive findings, 0 blocking.

- **F-1 (gate-current staleness)** — Codex flagged the handoff's gate-current next-step/status surface as stale (it still described the pre-flip "drafted → active token-swap pending" state after the path-(α') flip had completed). Disposition: **path-(β)** — resolved by refreshing the gate-current surfaces at this Gate A re-application (which IS a §23.6.5 gate): §Last completed step + §Current state Summary + exact-next-step now describe the post-flip / pass-1-absorbed reality. No append-only surface back-edited.
- **F-2 (Project-Brief "Kickoff follow-ups" reference)** — greenfield Step 5 (mirroring `usage-guide.md` §2.7) references a Project Brief "Kickoff follow-ups" section that `templates/project-brief-template.md` does not materialize. Disposition: **path-(a)** — hardened `prompts/greenfield.md` Step 5 with a within-line graceful-degradation parenthetical ("add the heading if the brief doesn't already carry one"); section name retained for §2.7 parallel-form. **path-(β)** — root template/canonical gap logged at handoff §10 ledger (VIII) as a carry-forward (candidate PMN); `project-brief-template.md` + `usage-guide.md` left untouched (root fix anti-scope this cycle).

**§23.6.5 empirical note (input to TASK-0048 canonicalization):** zero append-only-historical surfaces were re-flagged as stale by Codex pass-1 — the behavioral suppression clause (`do not flag append-only historical surfaces as stale against post-absorption state`) held. The sole staleness finding (F-1) was against a **gate-current** surface and was correctly deferred to gate-refresh. Empirical signal: gate-current next-step/status pinning is the residual staleness source under the §23.6.5 discipline — flagged as a §23.6.5 design input for TASK-0048 (vs TASK-0045, where append-only claim-7/8/12 churn dominated; the append-only-snapshot refinement appears to have eliminated that churn class this cycle).

### Post-PR pass-1 absorption (append-only-historical)

Codex desktop post-PR pass-1 (owner-invoked `@codex review` per ADR-001 D11; reviewed commit `a63b272`): 1 legitimate gate-current finding (P2), 2 suggestions, plus phantom delivery-layer claims.

- **Phantom delivery-layer claims (§8.1.1.2)** — Codex's summary claimed it "Committed the changes on the current branch: `2b5cfd1`" and "Created a PR via `make_pr`". Both verified **non-existent** against repo state: `git cat-file -t 2b5cfd1` → not a valid object; no follow-up branch/PR in the all-state PR list; PR #75 branch tip remained `a63b272`; working tree clean. Codex narrated step-11's already-authored work (gate-current diff-stats refresh + review-context absorption) as its own commits. Caught by phantom-action verification; no action propagated. Logged at handoff §10 ledger (IX).
- **P2 (gate-current status staleness)** — handoff §Current-state file-list item 1 still carried `status: stub → drafted` while the file is `status: active` (and the §Current-state Summary already said active). Disposition: **path-(a)** within-line gate-current refresh (`stub → drafted` → `stub → active`); a completeness grep confirmed zero stale-status residuals in any gate-current surface. Correct finding; confirms the pre-commit F-1 lesson (a gate-current refresh can miss sibling instances).
- **Step-4 hardening (suggestion → accepted)** — Codex suggested the kickoff collect concrete project-profile inputs before drafting bootstrap artifacts. Disposition: **path-(a)** — folded a project-profile elicitation (project name + one-line purpose + problem space/domain) into Step 4's lead-in before bootstrap-set production; no step renumbering; enriches obligation 5. Greenfield body reopened (ratified at step-3) per Architect routing.
- **usage-guide §2.1 alignment (suggestion → declined)** — Codex suggested aligning usage-guide §2.1 to require the full trio before pasting (matching greenfield Step 0). Disposition: **path-(β) decline/carry-forward** — usage-guide §-body edits beyond the L22/L370 sweep are anti-scope this cycle (spec §5). Logged at handoff §10 ledger (X) for a future usage-guide-touch cycle (with the ledger-(VIII) §2.7 root-gap). `usage-guide.md` left untouched.

**§23.6.5 final empirical note (input to TASK-0048 canonicalization):** across BOTH Codex phases (pre-commit pass-1 + post-PR pass-1), **zero** append-only-historical surfaces were re-flagged stale — the suppression clause `do not flag append-only historical surfaces as stale against post-absorption state` eliminated the append-only re-flagging that drove TASK-0045's claim-7/8/12 rewrite churn. The sole residual staleness class was **gate-current status pinning** (F-1 at pre-commit + P2 at post-PR; P2 shows even a gate-current refresh can miss sibling instances). TASK-0048 §23.6.5 design input: **keep the append-only suppression clause as-is**; address gate-current status pinning specifically (minimize the number of pinned-status surfaces, and/or add a status-residual completeness grep to the gate-current refresh routine).
