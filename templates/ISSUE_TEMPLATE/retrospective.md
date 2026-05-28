---
template_version: 3.0.0
status: recorded
filled_by: PR-71 (TASK-0044)
---

# Retrospective Issue template

Canonical-source retrospective Issue template for AMAS-adopted repositories. At an adopter project, this template materializes as `.github/ISSUE_TEMPLATE/retrospective.md` (the operational instantiation). The canonical-source-vs-operational distinction lives at `github-reference.md` §4.3: operators copy the body sections from this canonical-source form to the operational `.github/ISSUE_TEMPLATE/` instantiation; canonical-source amendments propagate via the same mirror discipline. The 6-section canonical body below is the authoritative form. At operational instantiation, the canonical-source AMAS 3-field frontmatter is replaced by GitHub's legacy-markdown ISSUE_TEMPLATE frontmatter (name + about + labels + assignees per GitHub Docs canonical); opening framing + closing Cross-references may also be stripped per GitHub-recognition hygiene.

A retrospective Issue is distinct from the sibling chore + feature + project-initiation templates in temporal posture: it anchors PMN-companion authoring AFTER a cycle ships, rather than launching a cycle. Adopters open a retrospective Issue when a shipped cycle warrants cross-cycle pattern codification per `core.md` §18.1 PMN-trigger criteria; the PMN body lives at `docs/post-merge-notes/PMN-###-<slug>.md` per `templates/post-merge-note-template.md`, and this Issue tracks the retrospective surface itself (links, discussion, acceptance criteria for the PMN landing).

## §1. Linked records

- **PR retrospected**: <PR-### squash-merged + commit SHA, e.g., `PR-68 (commit SHA 3ed5a38)`>
- **TASK retrospected**: <TASK-#### the retrospective covers>
- **PMN co-shipped or anticipated**: <link to `docs/post-merge-notes/PMN-###-<slug>.md` if a PMN has been authored or is scheduled; N/A if no PMN warranted per `core.md` §18.1 trigger criteria>
- **Predecessor PMNs whose patterns this retrospective continues**: <PMN-### links to prior post-merge notes whose carry-forward observations this retrospective extends; N/A if none>
- **Cycle-close ledger anchor**: <cross-reference to the retrospected cycle's handoff §10 cycle-close ledger at `docs/handoffs/TASK-####-<slug>.md`>

## §2. Cycle context

<1-paragraph framing of the cycle being retrospected.>

- What cycle shipped (scope summary in 1-2 sentences) + the cycle's ship state at retrospective authoring moment (merged + squash SHA + canonical version anchor if applicable).
- Adopter-relevant outcome summary: what the cycle changed at the canonical or operational surface set; whether the change was substantive-content (new canonical text or template body fill), mechanical (substitution / rename / path update), or process-discipline (cycle-protocol refinement applied without canonical-text amendment).

## §3. What worked

Bulleted enumeration of positive observations + empirical confirmations from the retrospected cycle. Cross-reference canonical disciplines that performed as designed:

- <discipline / surface 1>: <empirical observation that confirmed canonical-designed function>
- <discipline / surface 2>: <empirical observation>
- <…>

Examples (substitute with cycle-specific observations): `core.md` §24.5 multi-surface review pipeline catching upstream-surface defects at downstream surfaces; (XVII) bidirectional sum-stability holding at staged-tree measurement; (XXI) line-shared substitution discipline applied cleanly at coupled canonical-law amendments; state-current language at handoff §Current state Summary surface maintained at cycle-progression boundaries.

## §4. What didn't / observations worth flagging

Bulleted enumeration of defect observations from the retrospected cycle. Group by defect-class surface where applicable:

- **Architect-side defect observations**: <enumerate (XXIV.a-n) catalog entries surfaced at Architect spec authoring / routing / ratification surfaces; sub-class shape where empirical evidence supports>
- **Builder-side defect observations**: <enumerate (XXIV.a-n) entries at Builder authoring / verification / hand-back surfaces>
- **Reviewer-side defect observations**: <enumerate Reviewer-surface defects, including phantom-claim handling per `core.md` §8.1.1.2 and bounded-continuation surfaces per `core.md` §8.1.1.3>
- **Cross-surface coordination observations**: <enumerate carriers that cross role boundaries — joint Architect + Builder narrowness, post-merge silent-miss surfaces, routing-state-currency narrowness>

Defect-class is distinct from severity: defect-class names the root-cause shape (e.g., "canonical-source enumeration narrowness at adopter-copy-shape literals"); severity classifies blocking vs absorbable per `core.md` §8.1.1 (or project-policy equivalent). Authoring guidance: surface defect-class first, then severity disposition.

## §5. PMN candidacies + carry-forward

This Issue §5 is the anchoring surface; the PMN file body §6.x carry-forward framework is the authoring surface. Enumerate PMN link + 1-2 sentence pointer summary here; full candidacy enumeration lives in `docs/post-merge-notes/PMN-###-<slug>.md`:

- <PMN-### candidacy>: <1-2 sentence summary of the cross-cycle pattern + cross-cycle reach count at the candidacy moment>
- <PMN-### candidacy>: <…>

The anti-duplication constraint is structural: candidacy enumeration full text lives in the PMN file body, not here. If a candidacy is referenced here without a corresponding PMN entry, either author the PMN entry or remove the §5 reference; do not duplicate the candidacy enumeration between this surface and the PMN body.

## §6. Forward implications

Bounded scope: 1-2 sentence framings of discipline refinements proposed for successor cycles. Full proposal text lives in the PMN body per `templates/post-merge-note-template.md` §6.x carry-forward framework:

- <refinement 1>: <1-2 sentence framing of proposed successor-cycle behavior + cross-reference to PMN body section where full proposal lives>
- <refinement 2>: <…>

## Cross-references

- PMN canonical form: `templates/post-merge-note-template.md` (PMN body §6.x carry-forward framework is the authoring surface for full candidacy enumeration)
- Canonical-source-vs-operational distinction: `github-reference.md` §4.3
- Operational instantiation path: `.github/ISSUE_TEMPLATE/retrospective.md`
- Branch convention: `github-reference.md` §2.2 (retrospective Issues do not typically launch a branch; if a follow-on cycle is warranted, the new cycle uses its own `feat`/`fix`/`chore` branch per the canonical regex)
- Sibling canonical-source templates: `templates/ISSUE_TEMPLATE/project-initiation.md` + `templates/ISSUE_TEMPLATE/feature.md` + `templates/ISSUE_TEMPLATE/chore.md`
- Pull-request template: `templates/PULL_REQUEST_TEMPLATE.md`
- Handoff template: `templates/handoff-template.md` (handoff §10 cycle-close ledger is the canonical anchor for cycle-close observations; this Issue §4 + §5 carry-forward links into the ledger)
- ADR template: `templates/ADR-template.md` (when a retrospective surface promotes a refinement to canonical-law amendment per `core.md` §18 ADR-trigger criteria)
