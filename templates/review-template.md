---
template_version: 3.0.0
status: filled
filled_by: PR-35 (TASK-0027)
---

# Review-context template

Review-context file format for Codex desktop pre-commit + Codex post-PR reviews per ADR-001 D11 owner-invokes convention. Two variants share substantive structure with per-variant body section adjustments.

## Frontmatter (canonical 1-field form)

```yaml
---
status: drafted
---
```

**Status field lifecycle** (per `.github/scripts/linked-pr-fix-up.py` canonical transitions):
- `drafted` (pre-stage; pre-Codex-pass) → `recorded` (post-merge per PMN-001 (k) Action substitution).

Drift from this exact form breaks Action transition. Verification via the `.github/scripts/linked-pr-fix-up.py` canonical pattern matching at frontmatter-only scope.

## Body sections (Codex desktop pre-commit variant)

````markdown
# PR-XX Codex desktop pre-commit review

## Metadata

- PR: PR-XX (anticipated or actual)
- Branch: <branch-name per Option B per ADR-005>
- Cycle: TASK-####
- Linked handoff: docs/handoffs/TASK-####-<slug>.md
- Status: drafted | recorded
- Codex desktop session timestamp (UTC): <ISO-8601 datetime>

## Builder claims to verify

<Numbered list of claims about staged-tree state. Each claim includes:>

1. **<Claim statement>**. Verifiable at pre-commit:
   - bash: `<verification command>` returns `<expected output>`
   - PowerShell: `<equivalent command if cross-platform Builder>`
   - Class: <PMN-009 (i.5) sub-shape A/B/C/D | PMN-010 sub-shape 1-7 | other; cite per cycle-applicable framework>

2. ...

<Recommended claim coverage for substantive cycles:>
- Cumulative-diff-stats per `core.md` §23.6.1.1 (e.1) staged-tree re-derivation
- §-citation correctness against current canonical state (per PMN-010 sub-shape 1)
- Class A v-bump applied per cycle scope (if substantive content cycle)
- Stub frontmatter updates applied per ADR-003 §Consequences distributed-update discipline (if filling stubs)
- M-A7 enumeration verification (if substantive-cycle PR)
- (j) all-instances grep sweep results
- Frontmatter shape conformance per applicable canonical form (PMN-007 HEAD canonical 12-field for handoffs; 1-field for review-contexts)
- Cross-document state preservation (Class B/C version markers preserved verbatim where prescribed)

## Reviewer focus

<Focus areas for Codex desktop pre-commit attention. Typical inclusions:>

- Substantive content shape verification (does the authored content match the spec prescription byte-exactly where prescribed?)
- §-citation resolution against current canonical state
- Cumulative-diff-stats matches review-context claims
- Frontmatter shape conformance
- (j)/(g)/(h)/(i) sweeps on review-context's own claim blocks (per PMN-008 §5.8)
- Recursive-self-instantiation salience check (per PMN-008 §3.1; document if MEDIUM or MAXIMUM)

## Codex desktop pre-commit kickoff

<Copy-paste-ready prompt for owner to paste into Codex desktop with project repository attached. Format: code-fenced block per PMN-002 (d) reliable-copy convention.>

```
Please review the pending changes on the current branch (<branch-name>) per the review-context at docs/reviews/PR-XX-codex-pre-commit.md. Working tree at staged-tree state per TASK-0025 cycle-close Item 4 lesson.

Cycle scope: <one-paragraph summary of substantive deliverables>

Pre-flight + step-2 stop-and-show context: <Builder pre-flight findings + Architect step-2 ratification scope notes>

Per ADR-001 D11 owner-invokes convention: please run pre-commit review, surface findings per severity (Blocking → handback; Major → path-(a)/(β); Minor → default path-(b)). Substantive verdict via formal review (`gh pr view` reviews endpoint) preferred; issue-comment summary acceptable; line-level review-comments acceptable.

Verbatim-output convention: capture review verbatim into the review-context file ## Codex desktop pre-commit output absorption section.
```

## Codex desktop pre-commit output absorption

<Initial state: placeholder — populated post-Codex-pass. After Codex returns:>

### Codex pass <N> (UTC <timestamp>)

**Verdict**: <Approved / Major findings / Blocking findings>

**Findings** (verbatim):

> <Codex output verbatim>

**Adjudication** (per ADR-001 D11):

- <Finding 1>: routed path-(a) revise / path-(β) record-and-proceed / Blocking handback per `core.md` §8.1.1.3.
- ...

**Resolution applied** (if path-(a)):

- Edit X.N: <file:line> <pre-state> → <post-state>. Verifiable at next-iteration: `<command>` returns `<expected>`.
````

## Body sections (Codex post-PR variant)

Substantive structure parallels pre-commit variant with these adjustments:

- **Title**: `# PR-XX Codex desktop post-PR review` (or `# PR-XX Codex post-PR review` for `@codex review` invocation).
- **Metadata adds**: post-PR poll timestamp (UTC); three-endpoint poll evidence per `core.md` §8.1.1.1; (w) Codex post-PR autonomous-action emission monitoring (if applicable).
- **Builder claims** preserved (already verified at pre-commit; serve as forward-reference for post-PR Codex against actual-merged state if Codex post-PR re-verifies).
- **Reviewer focus** adjusts to post-PR scope (full-PR diff, not staged-tree only).
- **Three-endpoint poll record** populated per `core.md` §8.1.1.1: `pulls/{pr}/reviews` + `issues/{pr}/comments` + `pulls/{pr}/comments` outputs verbatim.
- **(w) cross-cycle data point** noted if Codex emits autonomously pre-trigger.

## Usage notes

- **One review-context per PR per Codex pass-set**: pre-commit review-context separate from post-PR review-context typically; some cycles consolidate per cycle convention.
- **Verbatim-output convention**: Codex output captured verbatim (not paraphrased) per `core.md` §8.1.1.2 phantom-action verification discipline.
- **Path-(a) iteration**: each path-(a) revision triggers re-stage + (j)-sweep + cumulative-diff-stats re-derivation per `core.md` §23.6.1.1 (e.1).
- **Bounded-continuation rule**: review iterations bounded per `core.md` §8.1.1.3 cost-class refinement (pure-token-swap one-iteration; genuinely-asymptotic break-out).
- **Status transition**: `drafted` (pre-Codex-pass) → `recorded` (post-merge per PMN-001 (k) Action substitution). Drift breaks Action transition.

## Cross-references

- **core.md §8.1.1.1** — three-endpoint poll discipline.
- **core.md §8.1.1.2** — phantom-action verification (Reviewer claimed-action).
- **core.md §8.1.1.3** — bounded-continuation rule + cost-class refinement.
- **core.md §23.6.1.1** — (e.1) cumulative-diff-stats re-derivation.
- **ADR-001 D11** — owner-invokes Codex review convention.
- **ADR-001 D9** — admin-bypass posture (Posture 2 Rulesets).
- **PMN-001 (k)** — chore-fix-up substitution discipline (status transition `drafted` → `recorded`).
- **PMN-002 (d)** — code-fenced kickoff prompt convention.
- **PMN-008 §5.8 (h.4)** — Codex-output-endpoint-coverage discipline.
- **v2.14.1 §17 / §17.7** — review template substrate.
