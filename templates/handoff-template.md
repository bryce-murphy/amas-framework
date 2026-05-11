---
template_version: 3.0.0
status: filled
filled_by: PR-35 (TASK-0027)
---

# Handoff template

Universal handoff for AMAS cycle-execution. Carries the current state of a task: branch, last completed step, blockers, exact next action, validation evidence. Per `core.md` §14 handoff schema and v2.14.1 §14 substrate.

## Frontmatter (canonical 12-field form per PMN-007 HEAD canonical)

```yaml
---
task_id: TASK-####
title: <one-line cycle-scope summary>
pr: PR-N  # N = anticipated or actual PR number, numeric digits per regex \d+ (e.g., PR-1, PR-35, PR-100); NOT literal "N" or "XX"
branch: <type>/task-####-<kebab-slug>  # per github-reference.md §2.2 + ADR-005
linked_predecessor: TASK-#### (PR-N squash <short-sha> <description>)
linked_successor: TBD  # populated when subsequent cycle anchors
linked_pr: PR-N (Builder fills with squash SHA post-merge per PMN-001 (k))
framework_version_dogfooded: AMAS vX.Y[.Z]  # current canonical at handoff-authoring time
production_target: AMAS v3.0  # or as-applicable for non-amas-framework projects
spec_source: <path-to-spec>  # e.g., .claude/session-handoffs/TASK-####-spec.md (gitignored per ADR-001 D15)
date_authored: YYYY-MM-DD
status: drafted | active | resolved
---
```

**Frontmatter conformance discipline** (MC-C — `linked_pr` canonical regex form):

The `linked_pr` field MUST match the canonical regex enforced by `.github/scripts/linked-pr-fix-up.py:35`:

```
^linked_pr: PR-(\d+) \(Builder fills with squash SHA post-merge per PMN-001 \(k\)\)[ \t]*$
```

Drift from this exact form (e.g., `PR-N (squash SHA TBD at PR-open; substituted post-merge per PMN-001 (k))`, OR any non-numeric placeholder for the digit slot such as `PR-XX` / `PR-####`, OR any other variant) causes the linked-pr-fix-up Action to skip substitution silently, leaving the durable handoff carrying the placeholder post-merge. Per PMN-001 (k) convention: Builder validates `linked_pr` placeholder form against the canonical regex empirically before authoring handoff frontmatter — substituting a concrete numeric PR number for `N` BEFORE staging. Verification (using a concrete numeric PR-1 example to demonstrate Match):

```python
python -c "import re; print(re.match(r'^linked_pr: PR-(\d+) \(Builder fills with squash SHA post-merge per PMN-001 \(k\)\)[ \t]*$', 'linked_pr: PR-1 (Builder fills with squash SHA post-merge per PMN-001 (k))'))"
# returns: <re.Match object; span=(0, 67), match='linked_pr: PR-1 (Builder fills with squash SHA post-merge per PMN-001 (k))'>
```

Counter-example (confirms `PR-XX` literal placeholder does NOT match — would silently skip Action substitution):

```python
python -c "import re; print(re.match(r'^linked_pr: PR-(\d+) \(Builder fills with squash SHA post-merge per PMN-001 \(k\)\)[ \t]*$', 'linked_pr: PR-XX (Builder fills with squash SHA post-merge per PMN-001 (k))'))"
# returns: None
```

**Frontmatter field semantics**:

- **task_id** — primary identifier; matches handoff filename and branch task-#### segment.
- **title** — one-line summary (typically PR title without conventional-commits prefix).
- **pr** — anticipated or actual PR number; reconciled at Builder pre-flight (sub-shape E provisional handling for pre-PR-open authoring).
- **branch** — Option B form per ADR-005 `<type>/task-####-<kebab-slug>` (regex enforced via `.github/workflows/branch-name-check.yml` post-fill).
- **linked_predecessor** — prior TASK with PR squash SHA + description; supports cycle-history forward-reference traversal.
- **linked_successor** — subsequent TASK; populated when next cycle anchors. `TBD` at authoring time.
- **linked_pr** — canonical placeholder form per MC-C discipline above; substituted post-merge by linked-pr-fix-up Action.
- **framework_version_dogfooded** — current canonical AMAS version at handoff-authoring time (per README line 9 canonical-version-of-record).
- **production_target** — version this cycle's content targets (typically `AMAS v3.0` for amas-framework; project-specific for adopters).
- **spec_source** — path to authoring spec (typically `.claude/session-handoffs/TASK-####-spec.md` per ADR-001 D15 gitignored convention).
- **date_authored** — handoff authoring date (Builder authoring or Architect substantive amendment).
- **status** — lifecycle state per `.github/scripts/linked-pr-fix-up.py` transitions: `drafted` (pre-stage) → `active` (post-stage / pre-merge) → `resolved` (post-merge per PMN-001 (k) Action substitution).

## Body sections (canonical lived-practice form per TASK-0023+ adjudication)

```markdown
# HANDOFF: TASK-####

## Metadata

- Task ID: TASK-#### (matches PR-XX anticipated or actual)
- Linked Issue: <issue-number-or-`none`>
- Linked PR: PR-XX — URL TBD at PR-open (substituted at step-13 per PMN-001 (k))
- Linked ADR(s): ADR-NNN (cycle-relevant ADRs)
- Linked Feature Brief: FEAT-#### (if applicable; `none` for ADR-tracked or chore cycles)
- Linked review-context file: docs/reviews/PR-XX-codex-pre-commit.md
- Owner role: Builder (Claude Opus / Codex / etc., session context)
- Previous role: Architect (handoff direction Architect → Builder)
- Timestamp (UTC): <ISO-8601 datetime>
- Last synced commit SHA: <main HEAD SHA at pre-flight>
- Branch: <branch-name per Option B>
- Status: drafted | active | resolved
- Direction: Architect → Builder (universal handoff schema, v2.14.1 §14.1)
- Framework version: <current canonical version>
- (Optional) Recursive-self-instantiation salience: NONE | LOW | MEDIUM | MAXIMUM (per PMN-008 §3.1 framework)

## Objective

<one-paragraph cycle scope summary; substantive deliverables enumeration if multiple>

## Last completed step

<latest step in step-by-step prescription that has been executed; serves as resume-anchor for session-continuation>

## Current state

**Summary**: <repo state at this point in cycle; staged-tree state convention per (e.1) re-derivation>

**Files to be authored / modified by Builder**:
1. NEW <path> — <description>
2. MODIFIED <path> — <description>
...

**Cumulative-diff-stats** (per `core.md` §23.6.1.1 (e.1) staged-tree convention):
- `git diff --staged --shortstat origin/main` returns `N files changed, X insertions(+), Y deletions(-)`.
- Per-file numstat: `<insertions>\t<deletions>\t<path>` × N. Sum-stability: per-file insertion sum equals shortstat insertions exactly at any pre-commit moment.

## Decisions made

<Architect-decided scope decisions per spec § + in-cycle Builder-pre-flight-surfaced adjudications. Bullet form; cite spec § or stop-and-show event reference.>

## Assumptions

- <repo-state assumptions verified at pre-flight — branch protection, base SHA, gh CLI auth, etc.>
- <discipline assumptions — Codex Reviewer operational, etc.>

## §1. <cycle-specific section> ... §10. Cycle-close ledger

<Numbered §-sections per cycle structure. TASK-0023+ canonical structure typical:>

- §1. Cycle scope deliverables enumeration (parallel to spec §1)
- §2. Cycle gates (parallel to spec §2)
- §3. Step-by-step execution record
- §4. <substantive-content evidence per deliverable>
- §5. Self-review record (step-9 §23.6.2 iteration log)
- §6. Pre-commit absorption (step-11 Codex desktop output absorption)
- §7. Commit + push + PR-open record
- §8. Post-PR Codex review state (populated step-13+)
- §9. Sign-off (step-17 §24.3.1 five-point check; Architect populates)
- §10. Cycle-close ledger (cycle-close observations + carry-forward monitoring + new PMN candidates)

## §11. Session log archive

<Architect session record(s) + Builder session record(s); per cycle iteration. Most recent session in PR body per AMAS v2.14.1 §13.1 (forthcoming at Part C+); prior sessions migrated here.>
```

## Usage notes

- **Direction-specific variants**: this template is the universal Architect → Builder direction. Other directions (Builder → Reviewer, Reviewer → Builder, Builder → Architect, Reviewer → Architect, Human → AI, AI → Human) follow the same frontmatter form with direction-specific body adjustments per `core.md` §14.2-§14.7 (canonical at v3) and v2.14.1 §14.2-§14.7 substrate.
- **Pre-flight discipline**: Builder runs `core.md` §8.2 (forthcoming at Part C+) pre-flight before authoring handoff body — verify branch-name regex compliance, base-branch freshness, working-tree state.
- **Stop-and-show discipline**: Before commit/push, Builder presents handoff at step-2 stop-and-show (pre-flight findings) + step-10 stop-and-show (pre-commit) per `core.md` §8.3 (forthcoming at Part C+).
- **Hand-back to Architect**: Architect receives handoff at step-17 + performs `core.md` §24.3.1 five-point post-handback check before authorizing merge per ADR-001 D9 admin-bypass posture.
- **Status field lifecycle**: `drafted` (pre-stage) → `active` (post-stage / pre-merge) → `resolved` (post-merge per PMN-001 (k) Action). Drift breaks Action substitution.
- **Path-(α') discipline at pre-merge gate**: Builder applies handoff frontmatter `status: drafted → active` token-swap at pre-merge stop-and-show staged-tree gate per `core.md` §23.6.3 path-(α') discipline-side fix. Status field MUST be `active` at merge time for PMN-001 (k) Action substitution to fire. `drafted` state at merge breaks Action transition silently.
- **Verification-first current-state guidance** (per PMN-012 §3.3 F2 fix-pattern): the durable handoff is a historical record; the PR is the canonical live-state surface for in-flight cycle gates. When a successor session resumes work mid-cycle: verify latest branch HEAD via `git log -1 origin/<branch>` (where `<branch>` = full branch name from this handoff's frontmatter `branch:` field; covers all ADR-005 valid prefixes `feat|fix|chore|adr|shadow|spike`) or `gh api repos/.../pulls/<PR>` against PR-NN state; verify cycle-gate live state against PR-NN comments / reviews / commits rather than handoff §-section enumerations (which are anchored to handoff-authoring time, not necessarily current). Historical gates anchored to SHAs / timestamps remain valid; in-flight gates require verify-before-act at successor surface. Pattern empirically validated at TASK-0034 cycle (handoff §6 + §9 self-instantiation test).

## Cross-references

- **core.md §14** (handoff schema; canonical at v3) — universal handoff structure.
- **core.md §8.2 / §8.3** (forthcoming at Part C+) — pre-flight + stop-and-show disciplines.
- **core.md §23.6 / §23.6.1 / §23.6.2 / §23.6.3** — Architect-side spec authoring + self-review disciplines applied at handoff-source-spec authoring.
- **core.md §24.3.1** — Architect five-point post-handback check applied at handoff hand-back.
- **github-reference.md §2.2** — branch convention per ADR-005 (Option B `<type>/task-####-<kebab-slug>`).
- **github-reference.md §6.2** — linked-pr-fix-up Action substitution discipline anchor.
- **ADR-001 D9** (admin-bypass posture); **D11** (owner-invokes Codex review); **D15** (gitignored spec convention).
- **ADR-005** (branch convention canonicalization).
- **PMN-001 (k)** (linked-pr-fix-up substitution discipline canonical form).
- **PMN-007** HEAD canonical 12-field frontmatter form.
- **v2.14.1 §14** — handoff template substrate.
