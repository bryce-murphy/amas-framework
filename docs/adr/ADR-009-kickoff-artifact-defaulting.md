---
adr_id: ADR-009
title: v3.0 kickoff-artifact defaulting — schema-valid defaults + non-blocking forthcoming markers (amends ADR-008 D3 at the kickoff-artifact layer)
status: Accepted
date: 2026-06-02
amends: ADR-008 (extends Decision 3 release-surface semantics to the kickoff-artifact layer; no predecessor Decision superseded)
supersedes: none
superseded_by: none
---

# ADR-009 — v3.0 kickoff-artifact defaulting: schema-valid defaults + non-blocking forthcoming markers

## Status

Accepted — 2026-06-02.

Amends ADR-008 (Decision 3 extension; no supersession). ADR-008 Decision 3 established release-surface semantics for deferred stubs (`roadmap_status` annotation distinguishing v3.0-required / v3.1-planned / v3.2-planned). This ADR extends the same plan-vs-instantiate principle from the package-distribution layer to the **kickoff-artifact layer** — the Batch P3 prompts and the templates they instantiate. No ADR-008 Decision is altered or superseded; ADR-008 §Status is unchanged per the amend-via-new-ADR convention (`templates/ADR-template.md` ADR edit discipline + usage-guide §10.10/§10.11).

Effective immediately for v3 in-repo cycle direction (Batch P3 kickoff prompts + the templates they consume).

## Context

The Batch P3 project-kickoff prompts (`prompts/greenfield.md` + `prompts/retrofit.md`, with `prompts/upgrade.md` to follow) drive an operator from project start to a committable bootstrap packet. During TASK-0047 adopter-runnability smoke testing (Mode-1 naive-comprehension + a push-through-to-Step-7 pass), the prompts repeatedly depended on canonical content that v3.0 has deliberately deferred:

- `core.md` §3.1 (the bootstrap-set + lite-kickoff specification) is forthcoming at Part C+.
- The Project Brief's `doc_mcp_mechanism` is a REQUIRED field, but the richer doc-MCP options appendix is v3.2-planned.
- The PR template's Ready-for-review checklist cites §8.2/§8.3, which materialize at Part C.2 (TASK-0048).
- `core.md §2.X` role definitions are forthcoming; kickoff role assignment proceeds off prompt prose.

The smoke gate showed that a bare "forthcoming" marker sitting inside a REQUIRED field, a checkbox, or an acceptance criterion reads to an operator as a hard wall — a place where they are asked to satisfy a contract against a spec that does not exist yet. That is a relabeled wall, not a graceful deferral.

## Decision

### Decision 1 — v3.0 kickoff artifacts default rather than fabricate

v3.0 kickoff artifacts (the Batch P3 prompts and the templates they instantiate) **may carry schema-valid defaults and explicit non-blocking forthcoming markers for not-yet-materialized v3.0/v3.2 canonical surfaces; a kickoff must never require operators to fabricate values from deferred specs.** Concretely:

- **Where v3.0 defines the content** — materialize it in the artifact.
- **Where a later surface will define it** (Part C.2 at v3.0; Batches P5–P7 at v3.2) — EITHER set a schema-valid default the current artifact contract accepts, OR use an explicit non-blocking forthcoming marker that states how to proceed and points to where it materializes.
- **A deferred dependency must never sit as a bare "forthcoming" inside a required field, checkbox, or acceptance criterion.** That is the disallowed relabeled-wall shape.

Worked instances at v3.0: `doc_mcp_mechanism` carries the schema-valid default `manual canonical-doc reference + owner-verified retrieval` (richer options forthcoming v3.2); the TASK-0000 bootstrap handoff uses the `PR-0` schema-valid sentinel for pre-PR-open authoring (satisfies the strict `PR-(\d+)` form; replaced with the real bootstrap PR number before merge, since the fix-up Action preserves the numeric token and substitutes only the SHA), `linked_predecessor: none`, `spec_source: ADR-000`; the PR-template §8.2/§8.3 items are marked non-blocking (`N/A until Part C.2 (TASK-0048)`) rather than asserted as false attestations.

**Scope.** This principle applies only where a v3.0 kickoff artifact references a canonical surface not yet materialized in the release train; it does not permit replacing available v3.0 guidance with forthcoming markers. Where v3.0 guidance exists, materialize it — a forthcoming marker is only for genuinely-deferred surfaces.

## Alternatives considered

### (A) Keep bare "forthcoming" markers in required fields

Rejected. This is the shape the smoke gate flagged as a hard wall: an operator confronts a required field / checkbox / acceptance criterion whose governing spec does not exist, and either fabricates a value or stalls. Defaulting + non-blocking markers preserve the deferred-content signal without blocking the operator.

### (B) Materialize the deferred canonical surfaces now (pull §3.1 / Part C.2 / P5–P7 forward)

Rejected. Contradicts the ADR-008 D2 minimum-viable scope and the ADR-007 Part-C ordering. Materializing those surfaces is later-cycle work (Part C.2 at TASK-0048; P5–P7 at v3.2); the kickoff artifacts only need to be runnable against the current contracts, which defaulting achieves at far lower cost.

## Consequences

- The Batch P3 prompts and the templates they instantiate (`project-brief-template.md`, `handoff-template.md`, `PULL_REQUEST_TEMPLATE.md`) carry schema-valid defaults / non-blocking markers per Decision 1; this is the acceptance gate for the kickoff-runnability remediation.
- The PR-template §8.2/§8.3 non-blocking markers are temporary v3.0-internal forthcoming markers; **TASK-0048 (Part C.2) replaces them with the real attestation** when §8.2/§8.3 materialize.
- Future v3.0 kickoff-surface authoring applies this principle as the standing rule; a deferred dependency in a required field/checkbox/criterion is a defect of this class.
- No predecessor ADR Decision is superseded; ADR-003 / ADR-006 / ADR-007 / ADR-008 §Status fields unchanged per amendment convention.

## Cross-references

- **ADR-008** Decision 3 (release-surface semantics for deferred stubs; `roadmap_status` annotation) — this ADR extends D3's plan-vs-instantiate principle to the kickoff-artifact layer.
- **ADR-007** Decision 2 + 3 — Part C.2 operating-discipline canonical surfaces (§8.2 / §8.3 / §13 / §10.5 / §23.6.5) materialize at TASK-0048; the PR-template non-blocking markers point here.
- **`templates/ADR-template.md`** — canonical 7-field frontmatter + 6-section body + ADR edit discipline (amend via new ADR; predecessor §Status unchanged).
- **`templates/project-brief-template.md`** — `doc_mcp_mechanism` v3.0 default.
- **`templates/handoff-template.md`** — TASK-0000 bootstrap-case frontmatter (PR-0 sentinel / none / ADR-000).
- **`templates/PULL_REQUEST_TEMPLATE.md`** — §8.2/§8.3 non-blocking markers.
- **`prompts/greenfield.md` + `prompts/retrofit.md`** — Batch P3 kickoff prompts applying the principle.
- **TASK-0047** — Batch P3 kickoff-prompt cycle; adopter-runnability smoke findings motivating this ADR.
- **`appendices/documentation-mcp-options.md`** (`roadmap_status: v3.2-planned`) — richer doc-MCP options home.
