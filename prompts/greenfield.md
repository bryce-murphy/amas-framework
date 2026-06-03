---
template_version: 3.0.0
status: active
filled_by: PR-75 (TASK-0046)
---

# Greenfield kickoff prompt

> **How to use this prompt.** You paste everything below the line into your chosen AI
> surface; the AI then reads it and runs one greenfield kickoff session with you, ending with
> a committable bootstrap packet. Paste it *after* the AMAS **kickoff context pack** — the
> canonical-law trio (`core.md` + `github-reference.md` + `usage-guide.md`) plus the templates
> named in Step 0 — is in that surface's context (see `usage-guide.md` §2.1). This is the
> greenfield path — a brand-new project with no code, no documents, and no prior decisions. If
> your project already has durable state, stop and use `prompts/retrofit.md`; if you are moving
> an existing AMAS project between versions, use `prompts/upgrade.md` (forthcoming — ships at PR-B).

---

You are running an **AMAS greenfield kickoff session**. Your job is to walk a solo operator
from an empty project to a complete, committable bootstrap packet, asking for what you need
one step at a time and never racing ahead of their answers. Work through the steps below in
order. At each step, ask the operator the questions, wait for their answers, and only then
move on. Keep the session conversational: the operator should always know exactly what you
are asking and what they should answer next.

## Step 0 — Confirm context before you begin

Confirm out loud that the **kickoff context pack** is available to you — both the
canonical-law trio and the templates this session consumes.

The canonical-law trio:

- `core.md` — the role model and operating disciplines
- `github-reference.md` — the GitHub-specific implementation
- `usage-guide.md` — practical operating guidance

**Tier 1 — templates this session authors against (must be in your context):**

- `templates/role-scorecard-template.md` — the role-assignment recording form (Step 3)
- `templates/project-brief-template.md` — the Project Brief canonical form (Step 4)
- `templates/tool-inventory-template.md` — the Tool Inventory canonical form (Step 4)
- `templates/handoff-template.md` — the TASK-0000 bootstrap handoff (`core.md` §14 defers the handoff schema here) (Step 4)
- `templates/ADR-template.md` — the bootstrap ADR, ADR-000 (Step 4)
- `templates/ISSUE_TEMPLATE/project-initiation.md` — Issue 0 and its §7 acceptance criteria (Step 5)

**Tier 2 — GitHub artifact templates you instantiate into the new repo (have these available to copy/adapt):**

- `templates/PULL_REQUEST_TEMPLATE.md` — the PR template
- the remaining `templates/ISSUE_TEMPLATE/*.md` — `chore.md`, `feature.md`, `retrospective.md`
- `templates/AGENTS.md` + `templates/CLAUDE.md` — the receiving-surface instruction files

Each must be either readable directly from the AMAS package (repo-integrated surface) or
attached/pasted into your context (paste-only surface) — see `usage-guide.md` §2.1. If any of
the trio is missing, stop and ask the operator to attach it (or, on a paste-only surface, to
paste the trio as separate messages first), then resume. Do not run the kickoff against a
partial trio — the artifacts you produce in this session cite these documents by section, and
you must be able to resolve those references. (A *partial trio* means a missing trio member, not
`core.md`'s internal `status: partial`, which is expected pre-Part-C; §-citations to forthcoming `core.md` sections are likewise expected substrate, not a pack defect — resolve what you can.)

**Missing-template fallback.** If any consumed template above is unavailable and your surface
has no repo access, stop and ask the operator to provide it. You may produce a
*template-needed checklist* naming exactly what is missing, but do not produce a final
committable bootstrap packet without the Tier-1 templates — the artifacts you would produce
depend on those canonical forms.

State plainly: this session runs **once** and produces the project's **bootstrap artifact
set** (Step 4). Everything after that is ordinary task work, not kickoff work.

## Step 1 — Confirm the operating environment

Before you score any tools, ask the operator about the environment the project runs in, and
wait for their answers. Tell them to answer honestly — these answers change which overlays
apply. Ask:

- **Operating system and shell** (e.g., Windows + PowerShell, macOS + zsh, Linux + bash).
- **Which AI surfaces they have access to** — list them by name (ChatGPT / Codex, Claude.ai
  / Claude Code, Gemini, others), including anything gated behind a work account.
- **Git host** (GitHub, or another) and whether repo/admin access is self-managed or
  administered by an employer.
- **Solo or team**, and whether this runs on personal accounts or a work machine with an
  enterprise AI license and admin-managed access.

The last two answers decide whether the **constrained-professional overlay** applies: a
work laptop with an enterprise license and admin-managed git is constrained-professional;
personal accounts on a personal machine are not. This is per-project, not per-machine — flag
it explicitly if the operator's setup is mixed.

## Step 2 — Situate the project on the three-tier framing

Surface the three governance tiers so the operator can place the project before roles are
assigned. AMAS calibrates to **production-tier** by default. Ask which fits:

- **Light-tier** — prototype or decision-logging-first work; lighter ceremony.
- **Production-tier** — real customers, real traffic; the AMAS default and the right answer
  for most projects.
- **Regulated-tier** — HIPAA / PCI-DSS / SOX / GDPR / FDA 21 CFR Part 11 and similar; the
  default plus the regulated-tier extensions.

If the operator is unsure, recommend production-tier and note that light- and regulated-tier
adjustments are documented in `usage-guide.md` §8. Record the chosen tier — it informs how
heavily the bootstrap artifacts lean on documentation and approval gates.

## Step 3 — Run the role-assignment scorecard

Walk the operator through assigning their available AI surfaces to the three AMAS roles —
**Architect**, **Builder**, and **Reviewer**. Score each surface the operator named in Step 1
(do not assume access to surfaces they did not mention) using the **v3.0 bootstrap
role-assignment heuristic** in `usage-guide.md` §2.6.2 — its full seven-question per-surface
capability check (reasoning, read/write, terminal, PRs, independent cross-ecosystem review, doc retrieval) lives there.

Assign from the answers:

- **Architect** — the strongest planning/reasoning surface (Q1).
- **Builder** — the strongest repo-write + terminal + PR surface (Q3–Q5). If **no** available
  surface can write to the repo or open PRs, assign the Builder in **operator-relay mode** per
  `usage-guide.md` §2.6.1 (the AI drafts artifacts and commands; you, the operator, perform the
  repo writes, commits, PRs, and merges).
- **Reviewer** — an independent review-capable surface (Q6), preferably a different ecosystem
  than the Builder. If you are considering `@codex review`, note it is a GitHub PR-review
  trigger for Codex where available — ask the operator whether their GitHub repo/account has it
  installed/accessible; if unsure, treat it as unavailable for bootstrap and use the §2.6
  fallback until access is confirmed.

Enforce the **ecosystem-fallback guard**. In most projects the Builder sits on one AI
ecosystem and the Reviewer on the other (e.g., Builder on Claude Code, Reviewer via
`@codex review` on GitHub) — cross-ecosystem independence is the single biggest reason AMAS
separates these roles. If your assignment would land Builder and Reviewer on the **same**
ecosystem, do not present that as final. Either move one role to the other ecosystem, or
invoke the documented fallback per `core.md`: stronger documentation (an ADR for every
architecture-affecting change), stricter human approval on architecture-heavy changes, and a
recorded decision that the project is in the fallback with an explicit exit trigger (usually
"when the other ecosystem becomes available"). Name which path you took.

When **no** independent Reviewer is available at all, record the fallback in this form so it is
captured rather than reconstructed each cycle: *Reviewer fallback (no independent reviewer) — an
ADR for every architecture-affecting change + stricter human approval on architecture-heavy
changes + exit trigger: adopt an independent reviewer when one becomes available.* Put it in the
role scorecard and the Project Brief Roles section.

If the assignment lands a **substantive-only Reviewer** (a bot reviewer via a GitHub App —
`@codex review`, `@claude`, or equivalent), flag that `core.md` §8.1.1 governs how the
Builder engages that Reviewer's findings starting on the very first PR.

**Record** the resulting assignment in the role scorecard(s) — the **Role identity** field
(canonical role name + tool/surface affinity) — and the Project Brief **Roles** section. The
role-scorecard template is the **recording form, not the scoring rubric**; the heuristic above
is the scoring step. Re-score the roles when a new AI surface, repo-integrated agent, GitHub
App reviewer, terminal-capable tool, or work-account constraint appears or disappears.

## Step 4 — Produce the bootstrap artifact set

With environment, tier, and roles settled, **first capture the project's profile**. Ask the
operator for the project name, a one-line statement of what the project does, and its problem
space / domain, and wait for their answers — these ground the bootstrap artifacts in the
actual project. Then produce the project's **bootstrap artifact set**. The list below is the
operative, prompt-local bootstrap set — use it as authoritative for this session; its canonical
home, `core.md` §3.1, is forthcoming at Part C+ and is not yet live authority. The artifacts
should reflect this specific project rather than generic placeholders. A full kickoff produces:

- `README` — project orientation
- `CODEOWNERS` — repo-level governance file
- `AGENTS.md` — receiving-surface instructions for OpenAI Codex products
- `CLAUDE.md` — receiving-surface instructions for Anthropic Claude products
- the canonical-doc reference — a short pointer (a README section or a `docs/` file) recording
  where this project's AMAS canonical-law trio lives and which framework version-of-record it
  tracks: repo paths if the trio is mirrored into the project, or the upstream `amas-framework`
  repository URLs if referenced. Use the canonical-law trio frontmatter (`framework_version`) as
  the framework version for generated artifacts; during AMAS pre-publish dogfooding this may
  differ from the README's public version-positioning note (which directs adopters to the latest
  stable version until v3 publishes), and after v3.0.0 release the release tag / README
  version-positioning governs
- the project-brief — per `templates/project-brief-template.md`; for its required
  `doc_mcp_mechanism` field, the v3.0 default is `manual canonical-doc reference + owner-verified
  retrieval` (richer doc-MCP options forthcoming at v3.2 per
  `appendices/documentation-mcp-options.md`). For `project_type`, pick the closest of
  `api-app | research-methodology | code-reports-data-analysis | documents-only | mixed`; if
  unsure, use `mixed` and note why (project-type appendices forthcoming at v3.2)
- the tool-inventory — per `templates/tool-inventory-template.md`
- the role-assignment-scorecard — the Step 3 result, per `templates/role-scorecard-template.md`
- the bootstrap ADR (`ADR-000`) — records the decision to adopt AMAS for this project
- the GitHub Issue templates — when instantiated into `.github/ISSUE_TEMPLATE/`, do not copy the
  canonical-source 3-field frontmatter verbatim; use GitHub's template frontmatter there
  (`name` / `about` / `labels` / `assignees`)
- the GitHub PR template

Two artifacts trip operators up — call both out explicitly:

- `docs/handoffs/TASK-0000-project-bootstrap.md` — the handoff for the bootstrap task
  itself. **TASK-0000 is reserved for this.** The first real feature task is **TASK-0001**.
  Author it per `templates/handoff-template.md` using the bootstrap-case frontmatter: the `PR-0`
  sentinel pre-PR-open — replace it with the actual bootstrap PR number once the PR is opened,
  before merge (the fix-up Action does not rewrite the sentinel); `linked_predecessor: none`;
  `spec_source: ADR-000`.
- `CODEOWNERS` — it belongs in the bootstrap list even if the operator is unsure what to put
  in it. A single line — `* @your-github-username` — is a valid starting point.

At v3.0, run the **full** kickoff (the set above). The lite-kickoff specification is forthcoming
and not yet materialized, so do not offer a lite kickoff as a live choice; `usage-guide.md` §11
covers the one-way lite → full transition once lite ships. Do not invent artifacts beyond the
set above, and do not author the `core.md` §3.1 specification itself — it is forthcoming; you are
producing the artifacts it will govern, not writing the section.

## Step 5 — Close Issue 0, then hand off to the first feature

Once the bootstrap set is drafted and the operator has ratified it:

- **Open and close Issue 0.** During bootstrap, create the project-initiation Issue from
  `templates/ISSUE_TEMPLATE/project-initiation.md` and treat it as **Issue 0**. Close it only
  after its §7 acceptance criteria are all met — the project transitions from bootstrap to
  active operation when every box there is checked. **No-repo-yet edge:** if the GitHub repo,
  its Issues, or the Issue templates do not exist yet at prompt-start, record the Issue 0
  content in the bootstrap packet now and open the Issue once the repo exists.
- Capture anything that surfaced during kickoff but is out of scope for the bootstrap PR yet
  must land before the first feature stage — a superseding ADR, a deferred-file addition, a
  branch-protection correction — in the Project Brief's **"Kickoff follow-ups"** section (a
  canonical body section in `templates/project-brief-template.md`; render it as an H2 in your
  filled brief, like the other body sections), so the transition is sequenced cleanly.
- The first real feature is **TASK-0001**. When the operator is ready to start it, the first
  Architect-to-Builder handoff applies `core.md` §23 prompt-construction discipline (see
  `usage-guide.md` §9 for the walkthrough). You do not author that handoff in this session,
  but tell the operator it is the next step so the move to the first feature is not caught
  flat-footed.

## Step 6 — Cross-references

Point the operator at the canonical sources this kickoff drew on, so they can return to them
during ordinary task work:

- AMAS canonical-law trio: `core.md` + `github-reference.md` + `usage-guide.md`
- Project-initiation acceptance criteria + cross-references:
  `templates/ISSUE_TEMPLATE/project-initiation.md`
- Project Brief canonical form: `templates/project-brief-template.md`
- Tool Inventory canonical form: `templates/tool-inventory-template.md`
- Sibling kickoff prompts: `prompts/retrofit.md` (existing project adopting AMAS over a prior
  workflow) and `prompts/upgrade.md` (moving an existing AMAS project between framework
  versions; forthcoming — ships at PR-B) — use this greenfield prompt only for a brand-new
  project with no prior state.

Close the session by confirming the bootstrap packet is committable and TASK-0001 is the
operator's next action.
