---
template_version: 3.0.0
status: drafted
filled_by: PR-64 (TASK-0041)
---

# Pull request template

Canonical-source pull-request template for AMAS-adopted repositories. At an adopter project, this template materializes as `.github/PULL_REQUEST_TEMPLATE.md` (the operational instantiation) — GitHub autopopulates PR descriptions from the operational form. The canonical-source-vs-operational distinction lives at `github-reference.md` §4.2: operators copy the body sections from this canonical-source form to the operational `.github/PULL_REQUEST_TEMPLATE.md` instantiation; canonical-source amendments propagate via the same mirror discipline. The 7-section canonical body below is the authoritative form; operational instantiation may strip frontmatter + opening framing + closing cross-references per GitHub-autopopulation hygiene; substrate-qualifier notes at canonical-source body (e.g., Ready-for-review §8.2 + §8.3 substrate qualifier per ADR-007 D3 / Part C.2 materialization) may also be operationally stripped per project policy on substrate-reference exposure to PR autopopulation form.

## Linked records

- Issue: #
- TASK:
- ADR(s):
- FEAT:
- Prior PMNs (if relevant):
- Prior handoffs in this chain:

## Summary

<one-paragraph description of what this PR does>

## Decisions in this PR

<ADR-eligible decisions made or affirmed in this PR. If a decision warrants its own ADR, name it here and link.>

## Validation

<commands run, evidence of passing tests / checks, any manual verification>

## Reviewer focus

<specific areas the Reviewer should pay attention to: phantom-action-prone surfaces, §24 propagation candidates, etc.>

## Ready for review (Builder confirms before marking PR ready)

> Note: §8.2 + §8.3 references below reflect AMAS v2.14.1 substrate; corresponding sections forthcoming at canonical-law Part C.2 materialization per ADR-007 D3.

- [ ] §8.2 pre-flight completed and reported
- [ ] §8.3 stop-and-show approved by owner
- [ ] All claimed actions in this PR are true
- [ ] Branch name matches `github-reference.md` §2.2 per ADR-005
- [ ] All template sections populated

## AI Session Log (current PR-state log set per §13.2; prior superseded sets migrated per §13.1)

<one subsection per distinct meaningful session, in canonical heading format:
### <Role> session — <Model and interface> — <YYYY-MM-DD>>

## Cross-references

- Canonical-source-vs-operational distinction: `github-reference.md` §4.2
- Operational instantiation path: `.github/PULL_REQUEST_TEMPLATE.md`
- Branch convention: `github-reference.md` §2.2 + ADR-005
- AI Session Log canonical form: AMAS v2.14.1 §13.1 + §13.2 substrate (forthcoming at Part C+ in v3 `core.md`)
- Sibling canonical-source templates: `templates/ISSUE_TEMPLATE/` (Batch P2; ship-pending per ADR-006 D2)
