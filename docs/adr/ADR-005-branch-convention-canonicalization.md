# ADR-005 — Branch convention canonicalization (Option B: deliberate divergence aligning to TASK-#### centrality + lived practice)

## Status

Accepted — 2026-05-06.

Effective: immediately for v3 canonical-law-trio prescription; lived practice already aligns. Branches existing at ADR-005 merge time preserved as canonical-form-aligned record. This ADR's own branch (`feat/task-0026-agents-claude-v3-migration-branch-convention-adr`) is grandfathered as Option B form per current lived practice; no retroactive renaming.

## Context

v2.14.1 §6.1 prescribes branch convention `<type>/<id>-<summary>` (bare numeric id, Option A). v3 canonical-law-trio (`github-reference.md` §2.2 + `usage-guide.md` §3.3 / §5.3) preserves this verbatim per ADR-003 transition plan §4 mapping (branch naming → GitHub ref impl + Action).

`AGENTS.md` and `CLAUDE.md` prescribe `<type>/task-####-<kebab-slug>` form (Option B), threading TASK-#### into branch names — consistent with AMAS's TASK-#### centrality across all durable artifacts (handoffs, PMNs, reviews, ADRs all reference TASK-####).

Lived practice (32/32 = 100% of merged PRs PR-1 through PR-32) follows Option B form. The "drift" was `AGENTS.md`/`CLAUDE.md` authoring against AMAS's organizing principle (TASK-#### centrality) rather than against v2.14.1 §6.1 verbatim text.

PMN-008 §5.1 (u) registered the divergence; TASK-0017 PR-17 path-(β) deferral identified ADR-class adjudication as resolution path. TASK-0024 N7 + TASK-0025 cycle-close ledger surfaced Option B as Architect-side anticipated reconciliation outcome at medium-high confidence.

A coupled drift: `AGENTS.md` allowed-types list (`feat, fix, chore, docs, adr, refactor, test, ci`) extends v2.14.1 §6.1 substrate AND v3 trio canonical (both: `feat, fix, chore, adr, shadow, spike`) with four conventional-commit types (`docs, refactor, test, ci`) while dropping two canonical types (`shadow, spike`). This is also drift, not deliberate v2.14.1 extension. ADR-005 reconciles this alongside the branch-form decision.

## Decision

**v3 canonical branch convention = `<type>/task-####-<kebab-slug>` (Option B), deliberately diverging from v2.14.1 §6.1 substrate to align with AMAS TASK-#### centrality + lived practice + self-documenting form for TASK numbers crossing 100+.**

This is a substantive divergence from v2.14.1 §6.1 per ADR-003 D2 restructure-only-discipline boundary: D2 is preserve-by-default, NOT preserve-without-exception. Substantive direction-decisions warrant ADR adjudication. ADR-005 documents this as deliberate divergence paralleling transition-plan v0.2 Decision E precedent (regulated-tier as additive layer beyond v2.14.1 substrate).

v3 trio amends per §Migration mapping table below. `AGENTS.md` / `CLAUDE.md` preserve Option B prescription (current Option B prescription is canonical); citation updates from `v2.14.1 §6.1` to v3 canonical (`github-reference.md` §2.2 per ADR-005).

**Coupled allowed-types reconciliation**: v3 canonical allowed-types list = `feat, fix, chore, adr, shadow, spike` (matches v2.14.1 §6.1 substrate verbatim; v3 trio preserves verbatim). `AGENTS.md` aligns to v3 trio canonical (drops `docs, refactor, test, ci`; restores `shadow, spike`).

## Migration mapping table

| Surface | Pre-ADR-005 form | Post-ADR-005 form | Action this cycle |
|---|---|---|---|
| `github-reference.md` §2.2 regex | `^(feat\|fix\|chore\|adr\|shadow\|spike)/[0-9]+-(...)$` (Option A; v2.14.1 §6.1 verbatim) | `^(feat\|fix\|chore\|adr\|shadow\|spike)/task-[0-9]{4}-(...)$` (Option B canonical) | Substantive amendment per Edit T.2 |
| `github-reference.md` §2.2 examples | `feat/123-auth-refresh` etc. (7 bare-id examples) | `feat/task-0123-auth-refresh` etc. (7 task-####- examples) | Substantive amendment per Edit T.2 |
| `github-reference.md` §2.2 prose form | `<type>/<id>-<summary>` | `<type>/task-####-<kebab-slug>` | Substantive amendment per Edit T.1 |
| `github-reference.md` §8 cross-references | "preserved verbatim" attribution | "deliberately diverged per ADR-005" attribution | Substantive amendment per Edit T.4 |
| `usage-guide.md` §3.3 examples | `feat/0001-session-export`, `fix/0023-cache-bug` | `feat/task-0001-session-export`, `fix/task-0023-cache-bug` | Substantive amendment per Edit T.3 |
| `usage-guide.md` §5.3 example | `feat/0042-session-export` | `feat/task-0042-session-export` | Substantive amendment per Edit T.3 |
| `AGENTS.md` branch convention | Option B (canonical-aligned, drift-from-v2.14.1) | Option B (preserved; citation updated to `github-reference.md` §2.2 per ADR-005) | Citation update + framing per Edit A2.4b |
| `CLAUDE.md` branch convention | Option B (canonical-aligned, drift-from-v2.14.1) | Option B (preserved; citation updated to `github-reference.md` §2.2 per ADR-005) | Citation update + framing per Edit C.3.3b |
| `AGENTS.md` allowed-types list | `feat, fix, chore, docs, adr, refactor, test, ci` (drift from both v2.14.1 §6.1 and v3 trio) | `feat, fix, chore, adr, shadow, spike` (v3 trio canonical; matches v2.14.1 §6.1 substrate) | Drift-correction per Edit A2.4b |
| `.github/PULL_REQUEST_TEMPLATE.md` line 31 (Ready-for-review checklist) | `Branch name matches §6.1` (bare; intended as v2.14.1 §6.1 canonical citation; ambiguous post-ADR-005 because v3 `github-reference.md` §6.1 is enforcement-layer model topic) | `Branch name matches \`github-reference.md\` §2.2 per ADR-005` | Substantive amendment per Codex post-PR Finding 2 absorption (path-(a)) |
| `README.md` line 79 (Actions enumeration table — `branch-name-check.yml` Description cell) | `Enforce §6.1 branch regex` (same defect class as PR template; bare §6.1 intended as v2.14.1 §6.1 canonical-regex citation) | `Enforce \`github-reference.md\` §2.2 branch regex per ADR-005` | Substantive amendment per Codex post-PR Finding 2 (j)-sweep absorption (path-(a)) |
| Lived-practice branches | Option B (existing) | Option B (canonical-aligned) | Already aligned; no migration |

## v2.14.1 §6.1 substrate divergence rationale

ADR-005 deliberately diverges from v2.14.1 §6.1 in v3 canonical because:

1. **TASK-#### centrality**. AMAS organizes ALL durable artifacts by TASK-####. Branch names threading `task-####-` align with this organizing principle. Option A's bare-id form orphans the branch from the project's primary identifier scheme.

2. **Lived-practice grounding**. 32/32 = 100% of merged PRs (PR-1 through PR-32) use Option B. Migrating to Option A would require behavioral change for every future branch creation + retroactive churn in past handoff narrations + PR-sequence narrative restructuring — disruptive without adopter benefit.

3. **Self-documenting argument**. `feat/task-0026-agents-claude-v3-migration` is more legible than `feat/26-agents-claude-v3-migration` — especially as TASK numbers cross 100+.

4. **TASK-0017 + TASK-0024 prior signal**. Both prior cycles' Architect-side direction-observations surfaced Option B as anticipated reconciliation outcome at medium-high confidence. ADR-005 ratifies a long-held architectural intuition rather than introducing a novel direction.

5. **ADR-003 D2 boundary**. Restructure-only-discipline is preserve-by-default, NOT preserve-without-exception. Substantive direction-decisions adjudicated via ADR class are explicitly permitted. Transition plan v0.2 Decision E (regulated-tier as additive layer) establishes precedent for v3 substantive additions beyond v2.14.1 substrate.

## Alternatives considered

**Option A canonical (`<type>/<id>-<summary>`)**. Rejected because (i) requires retroactive lived-practice churn affecting every future branch creation; (ii) orphans branch names from AMAS TASK-#### centrality; (iii) less legible at scale as TASK numbers grow; (iv) 100% of repo lived practice already follows Option B, signaling architectural intuition predating ADR-005's adjudication. v2.14.1 §6.1 substrate preservation is preserve-by-default discipline; ADR-005 is the explicit substantive adjudication permitting divergence.

## Consequences

1. `github-reference.md` §2.2 amends per Edits T.1 + T.2 (this cycle, PR-33): prose form, regex, and 7 examples migrate to Option B form (4-digit zero-padded `task-####-` prefix).

2. `usage-guide.md` §3.3 + §5.3 amend per Edit T.3 (this cycle): three example-strings migrate to Option B form.

3. `github-reference.md` §8 cross-references amends per Edit T.4: `v2.14.1 §6.1` attribution shifts from "preserved verbatim" to "deliberately diverged per ADR-005" with substrate-divergence rationale.

4. `AGENTS.md` / `CLAUDE.md` preserve Option B branch-convention prescription; citation updates from `v2.14.1 §6.1` to v3 canonical per Edit A2.4b / C.3.3b. `AGENTS.md` allowed-types list aligns to v3 trio canonical (drops `docs, refactor, test, ci`; restores `shadow, spike`) as drift-correction.

5. PMN-008 §5.1 (u) candidate observation closed (resolved by ADR-005).

6. v2.14.1 substrate-divergence pattern documented as ADR-class precedent for future substantive direction-decisions where v3 canonical chooses to diverge from v2.14.1 substrate. Future divergences cite ADR-005 as precedent for the divergence-via-ADR pattern.

7. Regex enforces 4-digit zero-padded TASK number (`task-[0-9]{4}-`). Lived practice has used both `task-0001` and `task-0025` form historically (all 4-digit per `gh pr list` enumeration); canonical v3 standardizes on 4-digit. No lived-practice branches require regex weakening.

## Cross-references

- `core.md` §23.6.3 (reference-verification before spec authoring) — empirical case for ADR-005 cycle (verbatim retrieval of v2.14.1 §6.1 from UPCDS canonical at Builder pre-flight ratified the Architect pre-staged finding).
- `github-reference.md` §2.2 (post-ADR-005 canonical branch convention).
- v2.14.1 §6.1 (substrate, preserved-by-default; deliberately diverged per this ADR). UPCDS canonical at https://github.com/recruiting-tech/upcds/blob/main/docs/ai-operating-system.md.
- TASK-0017 PR-17 path-(β) deferral framing (the cycle that surfaced the divergence as ADR-class adjudication candidate).
- TASK-0024 N7 + TASK-0025 cycle-close ledger (Architect-side direction-observations Option B at medium-high confidence pre-ADR-005).
- PMN-008 §5.1 (u) candidate observation (closed by ADR-005).
- PMN-010 §2 sub-shape 7 within-v3-trio rule-contradiction adjudication framework.
- ADR-003 D2 restructure-only-discipline + transition plan §4 row mapping ("branch naming" entry maps to GitHub ref impl + Action).
- ADR-002 Decision 3 anticipation pattern (subsequent ADRs documenting substantive direction-decisions; ADR-005 follows the same pattern).
- Transition plan v0.2 Decision E (regulated-tier as additive layer; substantive-divergence-via-ADR precedent).
