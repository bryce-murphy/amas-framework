---
template_version: 3.0.0
status: recorded
filled_by: PR-68 (TASK-0043)
---

# Feature Issue template

Canonical-source feature Issue template for AMAS-adopted repositories. At an adopter project, this template materializes as `.github/ISSUE_TEMPLATE/feature.md` (the operational instantiation). The canonical-source-vs-operational distinction lives at `github-reference.md` §4.3: operators copy the body sections from this canonical-source form to the operational `.github/ISSUE_TEMPLATE/` instantiation; canonical-source amendments propagate via the same mirror discipline. The 6-section canonical body below is the authoritative form. At operational instantiation, the canonical-source AMAS 3-field frontmatter is replaced by GitHub's legacy-markdown ISSUE_TEMPLATE frontmatter (name + about + labels + assignees per GitHub Docs canonical); opening framing + closing Cross-references may also be stripped per GitHub-recognition hygiene.

## §1. Linked records

- **TASK**: <TASK-#### anticipated per `github-reference.md` §2.2 branch + handoff convention; assigned at cycle planning>
- **ADR(s)**: <ADR-### links if the feature implicates architectural decisions per `core.md` §18 ADR-trigger criteria; N/A otherwise>
- **FEAT**: <FEAT-### link to Feature Brief at `docs/features/FEAT-###-<slug>.md` if the feature warrants a Feature Brief per `core.md` §17 trigger criteria; N/A otherwise>
- **Prior PMNs in scope**: <PMN-### links to post-merge notes whose findings carry-forward into this feature scope; N/A if none>
- **Prior Issues in scope**: <Issue-# links to predecessor Issues this feature builds on or depends on; N/A if none>
- **Prior PRs in scope**: <PR-# links to predecessor PRs this feature depends on or amends; N/A if none>

## §2. Problem statement

<1-paragraph what + why framing.>

- The observable problem the feature addresses (what is wrong, missing, or absent today).
- User or operational impact of the current state (who is affected and how).
- Current behavior vs desired behavior (concrete contrast that anchors the acceptance criteria at §4).

## §3. Proposed approach

<1-paragraph how framing.>

- High-level shape of the proposed implementation (the load-bearing design moves; not full implementation detail).
- Substantive design decisions to be made during implementation (link to ADR if any decision crosses `core.md` §18 ADR-trigger criteria; otherwise note as in-scope Builder-side adjudication).
- Cross-surface coordination if multiple receiving surfaces or shared code paths are implicated.

## §4. Acceptance criteria

Issue closure conditions specific to the feature (mark complete when ALL boxes checked):

- [ ] Behavior <X> observable post-implementation at <verification surface, e.g., test run / manual step / dashboard panel>
- [ ] Test coverage <Y> achieved (or test plan otherwise satisfied per project policy)
- [ ] Documentation surface <Z> updated (README / canonical-law trio overlay / Feature Brief / receiving-surface AI-agent instruction files)
- [ ] ADR-### authored if the feature crosses `core.md` §18 ADR-trigger criteria (architectural-decision class)
- [ ] Cross-canonical-surface coherence verified per `core.md` §24 if the feature touches multiple canonical surfaces
- [ ] PR opened + reviewed + merged per project review pipeline

## §5. Out of scope

Explicit deferrals to follow-up cycles:

- Related-but-distinct feature work (separate Issue + separate cycle)
- Refactoring not strictly necessary for the acceptance criteria at §4
- Performance optimization beyond functional correctness threshold
- Documentation polish beyond surfaces named at §4 acceptance criteria
- Operational-instantiation downstream consumers (separate adoption cycle per project policy)

## §6. Risks + open questions

- **Known unknowns**: <enumerate conditions whose resolution emerges during implementation>
- **Design choices pending owner ratification**: <enumerate decisions that need owner sign-off before Builder execution>
- **Cross-cycle coordination dependencies**: <enumerate other cycles or external work the feature depends on or coordinates with>
- **(XXIV.a-n) catalog observations anticipated at implementation**: <enumerate catalog-class observations the receiving Builder should sweep for at step-9 self-review per `core.md` §23.6.2 + §23.6.3>
- **Reviewer-engagement anticipation**: <enumerate review-surface conditions anticipated per `core.md` §24.5 multi-surface review pipeline; e.g., pre-commit pass-1 absorption pattern, post-PR pass-N+ engagement>

## Cross-references

- Canonical-source-vs-operational distinction: `github-reference.md` §4.3
- Operational instantiation path: `.github/ISSUE_TEMPLATE/feature.md`
- Branch convention: `github-reference.md` §2.2 + ADR-005
- Feature Brief canonical form: `templates/feature-brief-template.md` (when feature warrants Feature Brief per `core.md` §17 trigger criteria)
- ADR canonical form: `templates/ADR-template.md` (when feature warrants ADR per `core.md` §18 trigger criteria)
- Sibling canonical-source templates: `templates/ISSUE_TEMPLATE/project-initiation.md` + `templates/ISSUE_TEMPLATE/chore.md` + `templates/ISSUE_TEMPLATE/retrospective.md`
- Pull-request template: `templates/PULL_REQUEST_TEMPLATE.md`
