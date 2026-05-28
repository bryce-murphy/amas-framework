---
template_version: 3.0.0
status: recorded
filled_by: PR-71 (TASK-0044)
---

# Chore Issue template

Canonical-source chore Issue template for AMAS-adopted repositories. At an adopter project, this template materializes as `.github/ISSUE_TEMPLATE/chore.md` (the operational instantiation). The canonical-source-vs-operational distinction lives at `github-reference.md` §4.3: operators copy the body sections from this canonical-source form to the operational `.github/ISSUE_TEMPLATE/` instantiation; canonical-source amendments propagate via the same mirror discipline. The 5-section canonical body below is the authoritative form. At operational instantiation, the canonical-source AMAS 3-field frontmatter is replaced by GitHub's legacy-markdown ISSUE_TEMPLATE frontmatter (name + about + labels + assignees per GitHub Docs canonical); opening framing + closing Cross-references may also be stripped per GitHub-recognition hygiene.

## §1. Linked records

- **TASK**: <TASK-#### anticipated per `github-reference.md` §2.2 branch + handoff convention; assigned at cycle planning>
- **ADR(s)**: <ADR-### links if the chore implicates architectural decisions per `core.md` §18 ADR-trigger criteria; N/A otherwise>
- **Prior PMNs in scope**: <PMN-### links to post-merge notes whose findings carry-forward into this chore scope; N/A if none>
- **Prior Issues in scope**: <Issue-# links to predecessor Issues this chore continues or unblocks; N/A if none>
- **Prior PRs in scope**: <PR-# links to predecessor PRs this chore cleans up after or follows on from; N/A if none>

## §2. Problem + justification

<1-paragraph what + why framing.>

- What needs cleaning up, refreshing, or maintaining (the observable condition at present state).
- Why now — the trigger that surfaces this chore as worth a cycle (e.g., post-merge silent-miss audit, surface drift between mirrored files, stale reference after a canonical amendment, accumulated bookkeeping deferred from prior cycles).
- Cross-surface scope if applicable: enumerate which canonical or operational surfaces are touched and whether the chore is purely mechanical (substitution / rename / path update) or carries content (ledger entry, refresh, rotation).

## §3. Scope

Bulleted enumeration of files + surfaces touched:

- <file or surface 1: nature of edit>
- <file or surface 2: nature of edit>
- <…>

Explicit non-mutating-canonical-law assertion if applicable: "chore does not amend canonical law; coupled `core.md` §X.Y substitutions are mechanical line-shared per (XXI), not substantive canonical-law amendments." If the chore DOES amend canonical law, reclassify as `feat` per `github-reference.md` §2.2 branch convention and route through the feature Issue template (`templates/ISSUE_TEMPLATE/feature.md`) instead.

## §4. Acceptance criteria + verification

Issue closure conditions specific to the chore (mark complete when ALL boxes checked). MUST include verification surfaces — bash commands, file paths to inspect, or receiving-surface configuration checks — that confirm closure deterministically.

Closure conditions checklist:

- [ ] <surface 1> refreshed / substituted / cleaned per §3 scope
- [ ] <surface 2> refreshed / substituted / cleaned per §3 scope
- [ ] Cross-surface coherence verified per `core.md` §24 if the chore touches multiple canonical surfaces
- [ ] Bookkeeping artifact (ledger entry / PMN cross-reference / handoff refresh) authored if the chore carries content beyond pure substitution
- [ ] PR opened + reviewed + merged per project review pipeline

Verification surfaces enumeration — how will we know this cleanup is complete? Enumerate bash commands, file inspection paths, or receiving-surface configuration checks where applicable:

- `<verification command 1>` returns <expected output>
- `<verification command 2>` returns <expected output>
- File inspection at `<path>` confirms <expected condition>
- Receiving-surface check at `<surface>` confirms <expected configuration>

Cross-repo canonical references at acceptance criteria literals should resolve via `github-reference.md` §X form rather than amas-framework-local references; adopters at non-amas-framework projects copy this template and will not have local `ADR-N` resolution at their canonical surface.

## §5. Out of scope

Explicit deferrals to follow-up cycles:

- Substantive feature work surfaced during the chore (separate Issue + separate cycle per `templates/ISSUE_TEMPLATE/feature.md`)
- Canonical-law amendment beyond mechanical line-shared substitution (reclassify as `feat` per §3 above)
- Refactoring or restructuring not strictly necessary for the closure conditions at §4
- Documentation polish beyond the surfaces named at §3 scope
- Operational-instantiation downstream consumers if the chore touches canonical-source surfaces only (separate adoption cycle per project policy)

## Cross-references

- Canonical-source-vs-operational distinction: `github-reference.md` §4.3
- Operational instantiation path: `.github/ISSUE_TEMPLATE/chore.md`
- Branch convention: `github-reference.md` §2.2 (chore branches use the `chore/` prefix per the canonical regex)
- ADR canonical form: `templates/ADR-template.md` (only when chore unexpectedly crosses `core.md` §18 ADR-trigger criteria; otherwise no ADR warranted)
- PMN canonical form: `templates/post-merge-note-template.md` (when chore retrospectively codifies a cross-cycle pattern per `core.md` §18.1 trigger criteria)
- Sibling canonical-source templates: `templates/ISSUE_TEMPLATE/project-initiation.md` + `templates/ISSUE_TEMPLATE/feature.md` + `templates/ISSUE_TEMPLATE/retrospective.md`
- Pull-request template: `templates/PULL_REQUEST_TEMPLATE.md`
