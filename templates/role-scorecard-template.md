---
template_version: 3.0.0
status: filled
filled_by: PR-45 (TASK-0032)
---

# Role scorecard template

Canonical template form for AMAS role scorecards. A role scorecard captures role identity, authority boundaries, standing responsibilities, cycle-phase responsibilities, and discipline references for an AMAS role (Architect / Builder / Reviewer per `core.md` §2.X (forthcoming at Part A; AMAS v2.14.1 §2.3 substrate) canonical role definitions; project-specific role overrides at adopting projects).

## Frontmatter

Filled role scorecards carry 4-field YAML frontmatter:

- `role_id`: canonical role identifier (e.g., `architect`, `builder`, `reviewer`); lowercase
- `status`: lifecycle state (`active | superseded`)
- `filled_by`: PR/TASK reference at content-fill time (`PR-NN (TASK-####)`)
- `framework_version`: AMAS canonical version when authored or last amended

## Body section structure

Filled role scorecards document the following canonical body sequence as actual H2 headings:

- **Role identity**: canonical role name + tool/surface affinity (e.g., Architect → Claude.ai Project; Builder → Claude Code; Reviewer → Codex desktop). Cite `core.md §2.X (forthcoming at Part A; AMAS v2.14.1 §2.3 substrate)` for canonical role definitions.
- **Authority boundary**: enumerate decisions within role authority (analytical adjudication / spec authoring / cycle-close ledger maintenance) and decisions reserved to owner (merge / strategic direction / scope ratification per ADR-001 D11).
- **Standing responsibilities**: cross-cycle disciplines applied at every cycle position (e.g., §24 verify-before-assert; §23.6 self-review; §8.1.1.3 cost-class refinement).
- **Cycle-phase responsibilities**: per-phase responsibilities mapped to cycle protocol phases (Phase 1 spec authoring / Phase 2 substantive authoring / Phase 3 review absorption / Phase 4 cycle close).
- **Disciplines applied**: enumerated §-references to canonical disciplines the role exercises (e.g., Architect: §14.1, §14.4, §14.7, §23.6, §24; Builder: §14.2, §8.2 (forthcoming at Part C.2), §23.6.1, §23.6.2; Reviewer: §8.1.1, §8.1.1.2, §8.1.1.3).
- **Cross-references**: pointers to related canonical surfaces (canonical-law sections / ADRs / paired role scorecards).

## Path conventions

Filled role scorecards live at `docs/role-scorecards/<role_id>.md` for project-instantiated role definitions. The template at `templates/role-scorecard-template.md` is the canonical form-of-record at framework-package level. Adopting projects instantiate role scorecards under `docs/role-scorecards/` at project initiation per project-brief role declaration.

## Authoring surface

Role scorecards canonicalize at framework-package level via this template; project-specific role instantiations author at project-initiation cycles, ratified by the owner. Standing role definitions amend at role-discipline-canonicalization cycles (rare; tied to canonical-law role-section amendments at `core.md` §2.X (forthcoming at Part A; AMAS v2.14.1 §2.3 substrate)).

## Cross-references

- `core.md §2.X` (forthcoming at Part A; AMAS v2.14.1 §2.3 substrate) — canonical AMAS role definitions
- `core.md §14.1-§14.6` — direction-specific handoff variants per role pair
- `core.md §17.5` — template lifecycle
- `templates/project-brief-template.md` — project-brief role declaration form
- ADR-001 D9 — reading order convention
- ADR-001 D11 — owner-invokes review convention
- ADR-006 D2 — Batch P1 process templates batch
