---
post_merge_note_id: PMN-012
title: First AMAS adoption pilot — upstream packaging ambiguity + handoff-currency recursion findings + cross-laptop coordination patterns
linked_pr: PR-50 (squash SHA 7331aaf)
framework_version_dogfooded: AMAS v2.30 (adoption-pilot retroactive-documentation cycle class; no v-bump per spec §0.1)
status: recorded
---

# PMN-012 — First AMAS adoption pilot — upstream packaging ambiguity + handoff-currency recursion findings + cross-laptop coordination patterns

## Status

Drafted at TASK-0034 (adoption-pilot retroactive-documentation cycle; first of its kind at AMAS framework). PMN-012 inserts under ADR-003 Decision 3 contingency budget; consumes one contingency slot. M-A6 PMN-emission rate post-PMN-012: 12/19 ≈ 63% (vs prior 11/19 ≈ 58% at PMN-011); within ADR-003 forecast calibration band.

## §1. Cycle context

TASK-0034 is the first **adoption-pilot retroactive-documentation cycle** at AMAS framework. The downstream cycle at `bryce-murphy/employee-churn` (TASK-0001: AMAS v2.10→v2.30 process-template retrofit) executed end-to-end via Issue #6 → PR #7 → squash merge `8d4eb0d`. Upstream amas-framework documented the pilot retroactively at this cycle.

Cross-repo coordination occurred across two laptops: upstream Architect (Claude Opus 4.7) at work laptop where amas-framework local checkout lives + downstream Architect (ChatGPT 5.5 Thinking + GitHub connector) at personal laptop where employee-churn local clone lives. Bryce served as coordination relay between laptops.

The pilot empirically demonstrated two substantive findings at upstream + several light-touch sub-findings. The downstream cycle ran to completion without waiting for upstream TASK-0034 spec — itself an important adoption finding documented at §5 below.

## §2. F1 — Upstream v2.30/v3.0 packaging ambiguity

### §2.1. Empirical observation

`bryce-murphy/amas-framework` is actively producing AMAS v3.0. Its `v2.30` tag (created at commit `98d7324` during TASK-0034 pre-cycle preparation) contains:

- `core.md` declaring `framework_version: 3.0.0` and `status: partial` with heading "AMAS v3 Core"
- Process templates declaring `template_version: 3.0.0` fields

Meanwhile, amas-framework README + AGENTS.md + CLAUDE.md + ADR references at v2.30 state advertise canonical version as v2.30. Adopter-facing surfaces claim v2.30; canonical content surfaces declare v3.0 partial.

### §2.2. Adopter impact at employee-churn

Per ChatGPT employee-churn Architect investigation at TASK-0001 scoping turn: "amas-framework@v2.30/core.md is partial v3 work-in-progress, not a clean v2.30 canonical core. For downstream adoption, v2.30-era is usable as a process-template reference layer only unless upstream provides a stable adopter-facing canonical core."

employee-churn TASK-0001 adapted to this empirical finding by:
1. Preserving local v2.10 operating-system core at `docs/ai-operating-system.md` (not replaced with stub-pointer)
2. Adding upgrade notice documenting the packaging ambiguity
3. Marking AGENTS.md / CLAUDE.md §-anchors as inherited-v2.10 (not resolved against v2.30 ref)
4. Scoping the adoption to "v2.30-era process-template layer" (not full canonical core replacement)

This adapter pattern is the right empirical response to the packaging ambiguity, but it represents real adopter friction.

### §2.3. Discipline candidate (canonical promotion form)

Future amas-framework cycle should adjudicate one of these durable packaging policies:

- **(a) Release-tag clean-content policy**: releases/tags must preserve clean adopter-facing canonical core files. `main` may carry v-next work; adopter refs MUST point to immutable release artifacts that match marketed version.
- **(b) Adopter-manifest policy**: templates and core versioning may diverge; adopters must use a manifest to identify compatible canonical sets at adoption time.
- **(c) Status-quo with caveat**: continue current pattern; document the v2.30/v3 ambiguity explicitly at README + AGENTS.md + CLAUDE.md so adopters know to expect it.

PMN-012 captures the empirical observation; canonicalization deferred to dedicated future cycle (ADR adjudication when upstream is ready to make durable policy decision per ChatGPT recommendation). Cross-cycle accumulation pending future adoption pilots.

## §3. F2 — Handoff-currency recursion at handoff template form

### §3.1. Empirical observation

Per ChatGPT employee-churn Architect hand-back at TASK-0001 cycle close: handoff-currency recursion surfaced during Codex review at employee-churn (Codex C3 + C3-bis findings, both same defect class). The handoff template at amas-framework (current canonical at `templates/handoff-template.md` v2.30-era) conflates two functions:

1. **Durable handoff record**: scope, decisions, risks, assumptions, validation patterns, successor guidance
2. **Live workflow state tracker**: current branch SHA, pending commit/push/reply steps, active review-thread state, mergeability

The latter is inherently volatile. Every absorption commit changes the facts the handoff just recorded. Result: handoff content goes stale immediately after each iteration. Codex correctly flagged this at employee-churn — first as stale next-step state (C2), then as stale current-state wording (C3+C3-bis on same class).

The deeper cause: **present-tense live-state claims in an artifact committed to git**. A committed file is a historical record. It should not pretend to be the current PR dashboard.

### §3.2. Recurrence at amas-framework (retrospective explanation)

This finding retrospectively explains a pattern observed across recent amas-framework cycles: (XVII) cumulative-diff-stats anticipation narrowness recurring at each cycle's stop-and-show iterations. The handoff at each amas-framework cycle tries to track live cycle state (current cumulative-diff-stats, current branch HEAD, current PR state), which goes stale at every iteration, causing apparent narrowness even when synthesis is correct.

Empirical reach: TASK-0030 + TASK-0031 + TASK-0032 + TASK-0033 all exhibited (XVII)-class instances at handoff state-snapshot fields. The handoff-currency recursion finding provides the explanatory mechanism.

### §3.3. Durable fix pattern (canonicalized at PMN-012; canonical-text amendment deferred to TASK-0035)

Per ChatGPT employee-churn Architect recommendation:

1. **Historical gates instead of live task state**: "Last completed step" becomes a list of completed historical gates anchored to SHAs, timestamps, and thread IDs. Audit-friendly without pretending to be live.

2. **Verification-first current state**: "Current state" reframed to say PR is canonical live-state surface; verify latest head SHA from PR or `git log -1`; verify review-thread state and mergeability from GitHub before acting.

3. **Conditional next steps**: "Exact next step" becomes conditional rather than brittle: first inspect PR, then decide whether replies are missing, whether another review is needed, or whether to move to owner merge gate.

### §3.4. Recommended canonical-text amendments (deferred to TASK-0035)

`templates/handoff-template.md` body guidance:

```markdown
## Last completed step / historical gates

Record only completed gates. Anchor them to issue numbers, PR numbers, commit SHAs, review timestamps, or thread IDs when useful. Do not describe work as "currently in progress" unless this handoff is intentionally pre-commit and will be updated before merge.

## Current state

The PR / issue / branch is the canonical live-state surface. This section should either:
1. record durable facts that will remain true after the next commit, or
2. instruct the next actor how to verify live state.

Avoid pinning transient values such as current HEAD SHA, working tree state, review-thread state, or pending push/reply actions unless paired with "verify before acting."

## Exact next step

Use verification-first conditional steps when the task is already in PR/review state:
- verify PR head SHA
- verify review-thread state
- verify mergeability / CI
- only then act
```

Frontmatter distinction candidate:

```yaml
status: active-at-authoring
live_state_source: PR / issue / branch
```

OR avoid `status` field that becomes stale unless there is a post-merge update step (which adds process overhead).

### §3.5. Cross-cycle reach + promotion candidacy

(XVII)-class instances across TASK-0030/31/32/33 = 4 cross-cycle confirmations. Handoff-currency recursion is the root-cause explanatory mechanism. Strongest canonical-text amendment candidacy at TASK-0035 dedicated template-amendment cycle. **Past ADR-006 D3 evidence-bar 3+ promotion threshold by significant margin.**

## §4. F3 — Per-role scorecard `source_of_truth_for_framework_anchors` field recommendation (light-touch)

Per ChatGPT employee-churn Architect observation at TASK-0001 cycle close: per-role scorecard authoring at employee-churn surfaced that role scorecards reference framework §-anchors at canonical sources. For vendored/pointer-only adopters operating with packaging ambiguity (per F1), the scorecard should explicitly declare which canonical source applies to §-anchor references.

Recommended template amendment (deferred to TASK-0035):

```yaml
source_of_truth_for_framework_anchors: [local file / upstream version / unresolved]
```

OR visible note block in body:

```markdown
> §-anchor source of truth: [local file / upstream version / unresolved]
```

Particularly important for vendored/pointer-only adopters. Carry-forward observation; cross-cycle accumulation pending.

## §5. F4 — Cross-laptop coordination patterns + friction observations (light-touch)

The TASK-0034 cycle empirically tested cross-laptop coordination across upstream (work laptop) + downstream (personal laptop) for the first time at AMAS framework. Friction observations:

1. **Issue/body as sufficient execution artifact**: downstream ratified Issue #6 body was enough to drive Builder execution. Upstream TASK-0034 spec was not on the critical path once downstream scope was ratified. Adoption-pilot cycles may not require upstream Architect to direct downstream execution — downstream Architect (with project context) can drive once scope is ratified.

2. **Copy/paste relay risk manageable**: cycle relied on frequent hand-backs between ChatGPT, Claude Code, Codex/GitHub, and upstream Claude. Process worked because each hand-back used explicit current state, issue/PR numbers, branch names, and stop conditions.

3. **Remote-visible action gates valuable**: stop-and-show gates produced the biggest saves — stashing TASK-0002 WIP, issue creation, branch creation, PR creation, Codex replies, PR-body updates, local branch force-delete after squash.

4. **Local WIP collision risk real**: Builder pre-flight found uncommitted Next.js scaffold on stale branch using old TASK-0001 namespace. Stash gate prevented app implementation from contaminating governance retrofit. Empirical positive for pre-flight discipline.

5. **Duplicate Codex review triggers possible**: C3 + C3-bis came from two `@codex review` triggers against same commit. Duplicate finding was still useful but creates redundant absorption work.

6. **Branch-number semantics explicit at adopter projects**: branch used GitHub issue number `6`, not logical task number `0001`. Correct for employee-churn's branch-name workflow; should be highlighted in cross-repo docs to avoid accidental `chore/task-0001-...` branches.

Cross-cycle accumulation pending future adoption pilots. Carry-forward observations; canonical-text amendments deferred until pattern recurs.

## §6. Recommended monitoring vs canonical promotion

PMN-012 canonicalizes findings at PMN body framing only; core.md canonical-text amendments deferred per ADR-006 D3 lightweight-absorption-preferred-default + ADR-007 D3 Part C materialization scoping schedule.

Promotion candidates queued at TASK-0035+ §23.6.3 sub-shape A consolidation cycle:

- **F2 handoff-currency recursion** → `templates/handoff-template.md` body amendment (strongest candidacy; past evidence-bar with retrospective (XVII) cross-cycle reach)
- **F3 per-role scorecard `source_of_truth_for_framework_anchors`** → `templates/role-scorecard-template.md` body amendment (lighter; first-instance)
- **F1 packaging ambiguity** → ADR candidacy when upstream is ready to make durable packaging policy decision; PMN body framing currently sufficient

Cycle-class recognition (adoption-pilot retroactive-documentation cycle) canonicalized at TASK-0034 spec §0.1; canonical-text amendment at `core.md` §18 family deferred until pattern recurs across multiple adoption pilots.

## §7. Cross-references

- `core.md` §14 universal handoff schema (canonical at PR-41) — applied
- `core.md` §17 + §17.5 + §17.7 templates parent frame + lifecycle + review template
- `core.md` §18.1 PMN-trigger criteria — applied at PMN-012 cycle-trigger adjudication
- `core.md` §18.2 PMN form specification — applied at PMN-012 form authoring
- `core.md` §18.3 M-A7 monitoring item — NOT amended at this cycle (adoption-pilot cycle class not enumerated per spec §0.1)
- `core.md` §18.4 framework version-bump trigger criteria — NO v-bump triggered per spec §0.1 cycle classification
- `core.md` §23.6 self-review iteration discipline
- `core.md` §23.6.3 reference-verification-before-spec-authoring
- `core.md` §24 + §24.3 + §24.3.1 verify-before-assert meta-pattern + receiving-discipline + Architect ← Builder hand-back five-point check
- ADR-001 D9 + D11 + D15
- ADR-003 D1 + D3 (PMN-012 consumes contingency slot)
- ADR-006 D3 (evidence-bar threshold reference)
- PMN-001 (k) — chore-fix-up Action substitution discipline
- PMN-007 §3.3 — 12-field handoff frontmatter canonical
- PMN-008 §5.8 (h.4) — Codex emission pattern
- PMN-011 (XXIV.a)-(XXIV.f) cross-surface meta-class typology + §2.4 refinement candidate
- TASK-0033 handoff — predecessor cycle reference
- TASK-0034 handoff — this cycle's primary cross-reference
- employee-churn TASK-0001: https://github.com/bryce-murphy/employee-churn/pull/7 (downstream cycle this PMN documents)
- `templates/handoff-template.md` — F2 canonical-text amendment candidate at TASK-0035
- `templates/role-scorecard-template.md` — F3 canonical-text amendment candidate at TASK-0035
