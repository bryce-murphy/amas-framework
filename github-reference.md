---
framework_version: 3.0.4
status: recorded
filled_by: PR-17 (TASK-0017)
---

# github-reference.md — GitHub-specific implementation of AMAS canonical law

## §1. Purpose and relationship to canonical law

This document is the second member of the AMAS canonical-law trio. core.md is the canonical-law foundation; this file translates canonical-law principles to GitHub-specific operational mechanics; usage-guide.md (third trio member, anticipated subsequent substantive cycle per ADR-003 Decision 2) provides practical operating guidance.

The reading order is core.md first, then this file, then usage-guide.md. Each canonical-law trio member cites only previously-merged trio members and other canonical text in core.md per ADR-003 tight-coupling dependency order discipline; this file cites core.md §-sections present in core.md HEAD at TASK-0017 cycle authoring time per cited-§-existence verification discipline.

The scope of this file is GitHub-specific implementation: branch naming conventions, branch protection postures, GitHub artifact templates references, AI agent identity mechanics, deterministic Actions reference, surface-file synchronization manifest, enforcement layer model. This file does not restate canonical-law principles — those are in core.md and cited by reference using the form `core.md §X.Y` for canonical-text citations.

Adopters using a non-GitHub canonical-state system (e.g., GitLab, Bitbucket, custom) substitute equivalent mechanics; AMAS does not currently ship reference implementations for non-GitHub systems. Future minor versions may add reference implementations for additional systems; v3.0 ships GitHub reference only.

## §2. Repository structure and branch naming

### §2.1. Canonical directory layout

The canonical AMAS-adopted repository layout is:

```text
/
├── README.md
├── CLAUDE.md
├── AGENTS.md
├── CODEOWNERS
├── core.md
├── github-reference.md
├── usage-guide.md
├── prompts/
│   ├── greenfield.md
│   ├── retrofit.md
│   └── upgrade.md
├── templates/
│   ├── handoff-template.md
│   ├── review-template.md
│   ├── post-merge-note-template.md
│   ├── ADR-template.md
│   ├── role-scorecard-template.md
│   ├── feature-brief-template.md
│   ├── project-brief-template.md
│   ├── tool-inventory-template.md
│   ├── surfaces-manifest-template.yml
│   ├── AGENTS.md
│   ├── CLAUDE.md
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── ISSUE_TEMPLATE/
├── actions/
│   └── (workflow files; see §6 below)
├── appendices/
│   └── (flat + project-type appendices; see ADR-003 Decision 2)
├── adapters/
│   └── (receiving-surface adapter packs; see ADR-003 Decision 2)
├── docs/
│   ├── adr/
│   ├── handoffs/
│   ├── post-merge-notes/
│   └── reviews/
└── .github/
    ├── ISSUE_TEMPLATE/
    │   └── (instantiated from templates/ISSUE_TEMPLATE/)
    ├── PULL_REQUEST_TEMPLATE.md (instantiated from templates/PULL_REQUEST_TEMPLATE.md)
    └── workflows/
        └── (instantiated from actions/)
```

The `templates/` directory is the canonical source for all GitHub-instantiated artifacts; `.github/` is the operational GitHub-recognized location. Adopters instantiate from `templates/` to `.github/` either manually at adoption time or via a future Action (anticipated post-v3.0).

The `docs/` directory holds durable project-state artifacts: ADRs (architectural decisions), handoffs (TASK-NNNN handoff files per direction-specific schema), post-merge-notes (PMN-NNNN files per core.md §18 discipline), and reviews (PR-NN review-context files per core.md §8.1 discipline).

### §2.2. Branch naming convention

Use the branch pattern:

`<type>/task-####-<kebab-slug>`

Where `<type>` is one of:

- `feat` — new user-visible functionality
- `fix` — bug fix
- `chore` — maintenance, dependency bumps, tooling, docs-only
- `adr` — ADR-only PR (no code change, just a durable decision being proposed)
- `shadow` — Reviewer's shadow implementation of an existing Issue
- `spike` — exploratory, not intended to merge (must be closed or converted)

The numeric portion is a 4-digit zero-padded TASK identifier (`task-0001`, `task-0023`, `task-0410`) threading the branch into the AMAS TASK-#### centrality discipline. The `<kebab-slug>` is lowercase letters, digits, hyphens, and periods. Periods are permitted only inside version-like substrings (e.g., `v2.5`, `v1.0.0`, `node-18.17`). Slugs must not start or end with a period.

Examples:

- `feat/task-0123-auth-refresh`
- `fix/task-0241-cache-key-bug`
- `chore/task-0302-bump-node-20`
- `chore/task-0001-framework-upgrade-v2.5`
- `adr/task-0017-session-storage`
- `shadow/task-0123-auth-refresh`
- `spike/task-0410-graphql-evaluation`

The reference regex is:

```text
^(feat|fix|chore|adr|shadow|spike)/task-[0-9]{4}-([a-z0-9]|[a-z0-9][a-z0-9.-]*[a-z0-9])$
```

The alternation allows either a one-character summary or a longer summary that does not start or end with a period. Periods remain permitted inside the summary; the convention is to use them for version-like substrings even though the regex does not enforce that intent mechanically.

### §2.3. Branch-name enforcement

A GitHub Action validates branch names against the §2.2 pattern on PR open. Non-matching branches do not merge without a human override and a documented reason. The reference Action ships at `actions/branch-name-check.yml` per ADR-003 Decision 2 (anticipated PR; see §6 below for the full Actions reference).

The Action check executes the §2.2 canonical regex against the head branch name; non-matching branches produce a non-passing status check. Blocking semantics derive from branch protection per §3.1 (required-status-checks integration); without that integration, the check status is advisory. Adopters integrate the check into branch protection's required-status-checks list to enforce the §2.2 convention deterministically per the canonical "no merge without override" policy.

## §3. Branch protection and single-contributor governance

### §3.1. Required branch protections

The canonical branch protection posture for `main` (or the project's default branch) is:

- **Require pull request before merging**: yes; require approvals: minimum 1 (raise per project size and risk tolerance)
- **Dismiss stale pull request approvals when new commits are pushed**: yes
- **Require review from CODEOWNERS**: yes if CODEOWNERS file exists
- **Restrict who can push to matching branches**: yes; allowlist limited to project owners + AMAS-distributed bot identities (see §5)
- **Allow force pushes**: no
- **Allow deletions**: no
- **Require linear history**: optional (recommended for projects using squash-merge convention per AMAS canonical merge discipline)
- **Require status checks to pass before merging**: yes; at minimum the AMAS-distributed Actions enumerated in §6.2 below

These protections enforce canonical-law principles in core.md (specifically the squash-merge + linear-history + claimed-action verification surfaces). Adopters with stricter requirements (e.g., regulated industries) may add additional protections per project-type appendix guidance (anticipated future content per ADR-003 Decision 2).

### §3.2. Single-contributor governance posture

For solo-operator AMAS-adopted projects (one human + AI agents), strict enforcement of the §3.1 protections without bypass mechanism creates a deadlock: the solo operator cannot self-approve PRs they author. AMAS canonical law (core.md) recognizes single-contributor bypass as an operational concession; this file specifies the GitHub-specific mechanism.

**Posture-2 admin-bypass via Rulesets**: GitHub Rulesets (introduced in 2024-2025) support per-actor bypass on otherwise-strict rules. Configure a ruleset for the default branch with the §3.1 protections, then add an admin bypass for the solo-operator account. This preserves the protections for any future contributor while permitting solo-operator merge of self-authored PRs.

**Configuration steps** (administrator UI):

1. Repository → Settings → Rules → Rulesets → New branch ruleset
2. Name: `main-protection` (or per project convention)
3. Target branches: `main` (or default branch pattern)
4. Bypass list: solo-operator account (Repository admin role)
5. Branch rules: enable §3.1 list above
6. Save and enable

**Recording the bypass**: when the solo-operator uses admin bypass to self-merge, the bypass is logged automatically by GitHub. Per AMAS canonical-law discipline (v2.14.1 §10.5-§10.6 single-contributor bypass migration source per ADR-003 transition plan §4 row 10), each bypass invocation is the implicit acknowledgment that the operator owns full responsibility for the merge state. No additional artifact is required at single-cycle scope; sustained-multi-contributor projects should document the bypass posture in an ADR.

### §3.3. CODEOWNERS pattern

The canonical CODEOWNERS file declares ownership of substantive directories and files. Pattern:

```text
# Canonical-law surfaces
/core.md @<solo-operator-or-architect-team>
/github-reference.md @<solo-operator-or-architect-team>
/usage-guide.md @<solo-operator-or-architect-team>
/prompts/ @<solo-operator-or-architect-team>

# Templates
/templates/ @<template-maintainer-team>

# Actions
/actions/ @<actions-maintainer-team>
/.github/workflows/ @<actions-maintainer-team>

# Project-state durable artifacts
/docs/adr/ @<solo-operator-or-architect-team>
/docs/handoffs/ @<all-contributors>
/docs/post-merge-notes/ @<solo-operator-or-architect-team>
/docs/reviews/ @<all-contributors>
```

Solo-operator projects use the solo operator as the owner across all entries. Multi-contributor projects partition ownership per role assignment per core.md role-model framing.

## §4. GitHub artifact templates reference

### §4.1. Reading order

The canonical reading order at AMAS-adopted repository:

1. README.md (project-specific orientation)
2. AGENTS.md or CLAUDE.md (AI-agent operating expectations; per receiving-surface adapter)
3. core.md (AMAS canonical law)
4. This file (github-reference.md; GitHub operational mechanics)
5. usage-guide.md (practical operating guidance)
6. Project-specific docs/adr/ entries (durable architectural decisions)
7. Templates and appendices as needed

### §4.2. PR template

The canonical PR template ships at `templates/PULL_REQUEST_TEMPLATE.md`; the operational instantiation lives at `.github/PULL_REQUEST_TEMPLATE.md`. The template requires per-PR completion of: linked TASK / handoff / review-context references; substantive change summary; test plan checklist; deferred-items declaration; cycle-defect honesty record (preliminary; refined per cycle empirical evidence).

The concrete template ships at the GitHub-artifact templates batch per ADR-003 Decision 2 (anticipated TASK-0019 / PR-19 or per PMN-shifted sequence; current sequence ships templates batch after canonical-law trio completion).

### §4.3. Issue templates

Issue templates ship at `templates/ISSUE_TEMPLATE/` and instantiate at `.github/ISSUE_TEMPLATE/`. Canonical issue types:

- `project-initiation.md` (Issue 0; project-bootstrap shape) — shipped at PR-68 (TASK-0043)
- `feature.md` (standard feature task) — shipped at PR-68 (TASK-0043)
- `chore.md` (maintenance / chore task) — shipped at PR-71 (TASK-0044)
- `retrospective.md` (PMN companion issue; optional) — shipped at PR-71 (TASK-0044)

### §4.4. AI agent instruction files

`AGENTS.md` (Codex-targeted) and `CLAUDE.md` (Claude-targeted) are canonical AI-agent instruction files at repository root. Each file declares: receiving-surface identity (which AI agent the file targets); operational expectations (which AMAS canonical-law sections apply); project-specific overlays (project context that supplements canonical law).

Future receiving-surface adapter packs (Cursor, Gemini, Copilot, human-maintainer) ship at `adapters/` per ADR-003 Decision 2 (anticipated separate batch).

## §5. AI agent identity

### §5.1. GitHub App vs user-PAT

AMAS-distributed Actions and AI-agent commits use GitHub App installation access tokens, not user personal access tokens (PATs). Rationale:

- **Audit trail separation**: GitHub App identities produce commits attributable to the app, distinguishing AI-generated commits from human commits in CODEOWNERS contexts and review attribution.
- **Token rotation**: installation access tokens are short-lived (1 hour default) and auto-rotated; PATs require manual rotation and create long-lived credential exposure.
- **Per-repository scope**: GitHub Apps grant permissions per-repository at install time; PATs grant permissions per-token at issuance time without per-repository granularity (with limited exception via fine-grained PATs).

The canonical bot-token minting Action is `actions/create-github-app-token` (canonical reference; see §8 cross-references for retrieval URL). AMAS-distributed Actions use this pattern by default.

### §5.2. Bot identification — user.type signal

The canonical bot-vs-human signal is the GitHub API's `user.type == "Bot"` field. AMAS-distributed Actions use this signal for bot identification; AMAS canonical law (core.md) treats bot-attributed reviews and bot-attributed commits per the principles in core.md §8.1 (review attribution) and core.md §24 (cross-surface verify-before-assert).

Forward-looking standards (see §5.5 below) — HTTP Message Signatures (RFC 9421) and AgentsID — may supplement or extend the user.type signal in future minor versions when they reach broader adoption.

### §5.3. CODEOWNERS implications

Adopters separating AI-agent commits from human commits via dedicated GitHub App identities preserve audit trail correctness and CODEOWNERS approval discipline. Pattern:

- Each AI agent (Builder, Reviewer, etc.) is provisioned as a separate GitHub App with installation in the project repository
- Each app's commits are attributable to the app's identity
- CODEOWNERS rules can require human approval on PRs authored by AI-agent identities; or can permit AI-agent self-approval per per-project bypass posture (similar to single-contributor bypass per §3.2)

This pattern is recommended for AMAS-adopted projects with substantive AI-agent activity. Solo-operator projects with ad-hoc AI-agent use may defer per-agent app provisioning until the activity warrants it.

### §5.4. noreply email canonical pattern

The canonical noreply email pattern for GitHub bot-attributed commits is:

```text
<bot-user-id>+<app-slug>[bot]@users.noreply.github.com
```

AMAS-distributed Actions parse this pattern reliably for commit-author verification. Example: `12345678+amas-builder[bot]@users.noreply.github.com`.

### §5.5. Forward-looking standards

The following standards are tracked but not depended on at v3.0:

- **HTTP Message Signatures (RFC 9421)**: standardized cryptographic signatures for HTTP messages; potential future foundation for AI-agent identity verification beyond user.type. AMAS may adopt in a future minor version when the standard reaches broader adoption.
- **AgentsID**: agent identity statistics and registry pattern. AMAS may reference AgentsID in future Tool Inventory schema extensions.

These standards are explicitly track-don't-depend at v3.0; the canonical AMAS implementation uses GitHub-native mechanisms (user.type Bot + GitHub App identity + noreply email pattern) as primary identity signals.

## §6. Deterministic Actions reference

### §6.1. Enforcement layer model

The enforcement layer model (sourced from AMAS v2.14.1 §15 and migrated to this file as part of canonical-law trio restructure per ADR-003 transition plan §4 row 10) names three layers:

- **Tool-level enforcement**: hooks, scripts, CI checks executed at developer or AI-agent surface (e.g., pre-commit hooks, local lint)
- **GitHub-level enforcement**: branch protections, required status checks, merge restrictions executed at the GitHub platform layer (the only layer that prevents direct merge to protected branches)
- **Human-gate enforcement**: review approvals, ADR sign-offs, manual operator decisions executed at human discretion

Per v2.14.1 §15.1 patch (preserved at this restructure): tool-level enforcement cannot prevent direct merge to a protected branch; only GitHub-level enforcement prevents the merge gate. This file's reference to "deterministic enforcement via Actions" refers specifically to GitHub-level Action checks integrated with branch protection required-status-checks.

### §6.2. Anticipated Actions

The canonical AMAS-distributed Actions ship at `actions/` (canonical source) and instantiate at `.github/workflows/` (operational location). The full set per ADR-003 Decision 2 anticipated batch:

- **branch-name-check.yml** — validates branch names against §2.2 pattern on PR open
- **pr-template-check.yml** — validates PR body against `templates/PULL_REQUEST_TEMPLATE.md` required fields on PR open + push
- **linked-records-check.yml** — verifies PR body references valid TASK / handoff / review-context records on PR open + push
- **ai-session-log-check.yml** — validates AI Session Log presence per core.md AI Session Log discipline
- **review-freshness-check.yml** — verifies that PR review attribution matches current head SHA (stale-review dismissal trigger)
- **surface-version-sync-check.yml** — validates that surface-file synchronization manifest (`.amas/surfaces.yml`; see §7 below) reflects current template versions
- **artifact-path-check.yml** — validates that ADRs / handoffs / reviews / PMNs land at canonical paths per repository structure conventions
- **claimed-action-verification.yml** — verifies bot-claimed actions against actual repository state per core.md §8.1.1.2 phantom-action verification discipline
- **mcp-config-validation.yml** — validates MCP Tool Inventory configuration if MCP transport is in use per project Tool Inventory

These ship at the AMAS-distributed Actions batch per ADR-003 Decision 2 (anticipated PR per current PMN-shifted sequence). github-reference.md forward-references them; concrete implementations land at the Actions PR.

### §6.3. Three-endpoint review polling operationalization

Per core.md §8.1.1.1 (Reviewer three-endpoint output handling — formerly labeled `dual-signal`; the discipline operationally spans three endpoint surfaces), AI-agent reviews emit across three distinct GitHub API endpoints with distinct content shapes: formal Pull Request Review objects, top-level issue-comment summaries, and line-level review comments. AMAS-distributed `review-freshness-check.yml` Action operationalizes this by polling all three endpoints:

```text
GET /repos/{owner}/{repo}/pulls/{pull_number}/reviews
GET /repos/{owner}/{repo}/issues/{issue_number}/comments
GET /repos/{owner}/{repo}/pulls/{pull_number}/comments
```

For each endpoint, the Action:

1. Fetches latest entries (paginated)
2. Filters by approved bot identities (per §5)
3. Groups by `submitted_at` / `created_at` timestamp
4. Validates freshness against current head SHA per endpoint-specific rule:
   - `pulls/{pull_number}/reviews`: validate the formal review's `commit_id` against current head SHA (stale-review rule).
   - `issues/{issue_number}/comments`: validate `created_at` against the current-head push timestamp; top-level issue comments carry no intrinsic `commit_id`.
   - `pulls/{pull_number}/comments`: validate the line-level review comment's `commit_id` / commit metadata where present, with a `created_at`-vs-push-timestamp fallback where commit metadata is unavailable.
5. Marks entries older than current head as stale; emits status check result accordingly

The lexicographic tie-break form per core.md §8.1.1.1 (h.3) canonical text applies symmetrically across all three endpoints: cross-timestamp emissions pass the timestamp filter without id constraint; same-timestamp emissions tie-break by id. This object-id tie-break (absorption ordering) is distinct from the per-endpoint `commit_id` staleness check at step 4.

### §6.4. Phantom-action verification operationalization

Per core.md §8.1.1.2 (Reviewer claimed-action verification), AI-agent claims about created or modified files / commits / PRs may diverge from actual repository state. AMAS-distributed `claimed-action-verification.yml` Action operationalizes this by parsing AI-agent review/comment content for action-claim patterns and verifying against repository state.

Action-claim patterns include:

- "Created file X" → verify file X exists at current head SHA
- "Modified file X" → verify file X diff includes claimed changes
- "Created commit Y" → verify commit Y is reachable from current branch
- "Created PR Z" → verify PR Z exists and is associated with current branch
- "Created issue Z" → verify issue Z exists and is in expected state

Sub-shapes per core.md §8.1.1.2 canonical text apply: each sub-shape requires explicit verification against repository state per §8.1.1.2 discipline. Builder identifies specific sub-shape definitions from current core.md §8.1.1.2 text at content authoring time per (i.5) convention-inference verification (cite-by-canonical-text-reading rather than Architect-asserted per-sub-shape description).

## §7. Surface-file synchronization

### §7.1. Manifest format

AMAS adopts a canonical surface-file synchronization manifest at `.amas/surfaces.yml` documenting all framework-versioned surfaces in the adopted project. The manifest is a single canonical file per project: top-level keys anchor the manifest (`framework_version`, `reference_impl`, `project_id`, `status`) and a `surfaces:` **list** enumerates every AMAS-distributed templated surface in use. Format:

```yaml
framework_version: <version>
reference_impl: github
project_id: <project-slug>
status: active

surfaces:
  - name: AGENTS.md
    path: AGENTS.md
    template_version: 3.0.0      # Action reads this
    canonical_version: <version>     # framework anchor (optional)
    agents: [codex]              # receiving surface (Codex products read AGENTS.md)
    status: active
  - name: CLAUDE.md
    path: CLAUDE.md
    template_version: 3.0.0
    canonical_version: <version>
    agents: [claude]
    status: active
  - name: pr_template
    path: .github/PULL_REQUEST_TEMPLATE.md
    template_version: 3.0.0      # templated, non-receiving (no agents key)
    status: active
  - name: branch_check
    path: .github/workflows/branch-name-check.yml
    template_version: 3.0.0
    status: active
  # ... one entry per AMAS-distributed templated surface in use ...
```

**Field model.** Each `surfaces:` entry carries:

- `name` (string) — REQUIRED.
- `path` (repo-relative path) — REQUIRED. The **adopter operational-surface path** where the instantiated surface lives in the project. It is NOT the template-of-record path; the Action derives template-of-record resolution separately (§7.2).
- `template_version` (string) — REQUIRED; the **authoritative declared sync-version** for the surface: the version of the AMAS-distributed template the surface was instantiated from / last synced to. The sync-check Action reads this value **from the manifest entry** (not from the operational surface file). Coarse / major-aligned per `core.md` §17.5.
- `canonical_version` (string) — OPTIONAL; the fine-grained AMAS framework version the surface content is anchored to (informational framework-anchor tracking).
- `agents` (list of agent slugs) — OPTIONAL; present **iff** the surface is a receiving surface (per-agent operating-frame file; see §7.3). Absence indicates a non-receiving templated surface.
- `status` (`active|superseded`) — OPTIONAL (default `active`).
- `notes` (string) — OPTIONAL.

Operational surfaces are **not required** to carry an in-file version marker — the manifest entry is the per-surface version-of-record. The canonical PR template permits operational instantiations to strip frontmatter, and `CLAUDE.md` / `AGENTS.md` carry only positioning text, not `template_version`; the declared sync-version lives in the manifest, maintained by the owner/adopter at AMAS-version-bump time.

The manifest is the canonical source of truth for which surfaces the adopted project synchronizes against AMAS framework releases. Adopters update the manifest at AMAS-version-bump time as part of the upgrade cycle.

**Migration note (v2.30-era → v3 unified schema).** The v2.30-era surfaces manifest (filled at PR-48) used a receiving-surface-only shape keyed by `canonical_version`. The v3 unified schema is **additive**: it adds `template_version` (Action-read) and `reference_impl`, retains `canonical_version` / `agents` / `status` / `notes`, and converts the header to top-level `framework_version` / `project_id` / `status`. Adopters upgrading instantiate the v3 template and, per surface, add `template_version` (the template major the surface was instantiated from). Concrete `upgrade.md` prompt wording is deferred to the Action-materialization cycle.

### §7.2. Sync check Action

AMAS-distributed `surface-version-sync-check.yml` Action (materializes at v3.1 per ADR-008 D4; stub at v3.0.x) validates that each manifest entry's declared template-version is current against the canonical template-of-record. The Action:

1. Reads `.amas/surfaces.yml` at PR head SHA
2. For each entry in the `surfaces:` list, takes the entry's declared `template_version` **from the manifest entry** (not from the operational surface file) and resolves the canonical template-of-record version for that surface
3. Compares the manifest-declared version against the template-of-record version
4. Emits status check result; an entry whose declared version is behind the template-of-record, or whose template-of-record cannot be resolved, produces non-passing status

**Proof obligation.** This Action proves declared template-version **currency** — that each manifest entry's declared `template_version` is current against the template-of-record. It does **not** prove byte/content parity of the operational surface: a manifest may declare `AGENTS.md` at `template_version: 3.0.0`, match the record, and pass while the operational body has drifted. Content/byte parity is an explicit **non-goal** (a hash comparison would false-positive on legitimately-customized operational surfaces). Marker-less Markdown operational surfaces (`CLAUDE.md`, `.github/PULL_REQUEST_TEMPLATE.md`) are not required to carry an in-file version marker; the manifest entry is the per-surface declared sync-version.

**Optional surface cross-check.** For surfaces that carry a parseable in-file version marker (e.g. `.yml` workflows via a `# template_version:` comment), the Action MAY additionally cross-check the surface-declared version against the manifest entry, recovering surface-parity evidence where it exists. This is permitted, not required.

### §7.3. Templated vs non-templated surfaces

Not all repository surfaces are templated. The synchronization manifest tracks only templated surfaces — surfaces whose canonical content lives in AMAS-distributed templates and is instantiated at the adopted project. Project-specific surfaces (e.g., project README, project ADRs, project handoffs) are non-templated and not tracked in the manifest.

The distinction matters for sync-check scope: the Action validates manifest-tracked surfaces only, not the entire repository file set. Adopters with project-specific surfaces that warrant sync discipline may extend the manifest schema in a future minor version.

Receiving surfaces — per-agent operating-frame files such as `AGENTS.md`, `CLAUDE.md`, `.cursorrules` — are a **subset** of templated surfaces and additionally carry an `agents` field naming the AI agents that read them; non-receiving templated surfaces (workflows, PR templates) omit the `agents` field.

## §8. Cross-references

- **core.md §1-§24**: canonical-law foundations cited throughout this file
- **core.md §8.1.1.1**: Reviewer three-endpoint output handling — operationalized in §6.3 above
- **core.md §8.1.1.2**: Reviewer claimed-action verification — operationalized in §6.4 above
- **core.md §8.1.1.3**: bounded-continuation rule for iterative review-finding adjudication — referenced as routing discipline for cycle-execution iterations
- **core.md §17 / §18 / §18.1-§18.4**: post-merge note discipline + framework version-bump trigger criteria — applies to this file's own framework version bump per cycle scope
- **core.md §23.6 / §23.6.1 / §23.6.1.1 / §23.6.2**: Architect pre-handoff self-review disciplines — applies at this file's spec authoring iteration
- **core.md §24 / §24.2 / §24.3 / §24.3.1**: cross-surface verify-before-assert meta-pattern — referenced as canonical principle for §6 verification disciplines

- **ADR-001**: initial repo setup decisions including reading order, branch protection, AI Session Log convention
- **ADR-003**: full v3.0 package PR plan + tight-coupling dependency order discipline + distributed-update discipline for README and stub frontmatter

- **v2.14.1 §6.1**: branch naming convention substrate for §2.2 above; deliberately diverged per ADR-005 (`<type>/<id>-<summary>` substrate → `<type>/task-####-<kebab-slug>` v3 canonical) to align with AMAS TASK-#### centrality + lived practice
- **v2.14.1 §10.5-§10.6**: single-contributor bypass source for §3.2 above
- **v2.14.1 §15**: enforcement layer model source for §6.1 above (with §15.1 patch fix preserved)

- **GitHub create-github-app-token Action**: https://github.com/actions/create-github-app-token (canonical bot-token minting pattern referenced in §5.1)

- **Forward-references** (anticipated subsequent PRs per ADR-003 Decision 2):
  - `templates/` batch: AGENTS.md, CLAUDE.md, PR template, issue templates, handoff template, review template, post-merge-note template, ADR template, role-scorecard template, feature-brief template, project-brief template, tool-inventory template, surfaces-manifest template
  - `prompts/` batch: greenfield, retrofit, upgrade
  - `actions/` batch: branch-name-check, pr-template-check, linked-records-check, ai-session-log-check, review-freshness-check, surface-version-sync-check, artifact-path-check, claimed-action-verification, mcp-config-validation
  - `appendices/` flat batch: mcp-integration, documentation-mcp-options, tool-capability-model, vendor-surface-guidance, github-review-automation, amas-vs-other-frameworks, regulated-tier-extension
  - `appendices/` project-type batch: api-app, research-methodology, code-reports-data-analysis, documents-only, mixed
  - `adapters/` batch: claude-code, codex, chatgpt, cursor, gemini, copilot, human-maintainer
  - `usage-guide.md`: canonical-law trio third member; ships at next substantive cycle anticipated post this cycle
