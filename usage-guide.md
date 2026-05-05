---
framework_version: 3.0.0
status: drafted
filled_by: PR-29 (TASK-0024)
---

# AMAS v3 Usage Guide

Status: drafted at TASK-0024.
Companion to: `core.md` (canonical framework law) + `github-reference.md` (GitHub-specific implementation of core). This guide is practical operational guidance; the canonical-law trio is the rule source. Where this guide and the canonical-law trio disagree, the canonical-law trio wins.

---

## §0. What this guide is

This guide is for someone who has read the v3 canonical-law trio (`core.md` + `github-reference.md`) — or at least skimmed them — and is about to apply the framework to a real project. It covers the choices you actually make in the first week, the common friction points, and the operational patterns that the canonical-law trio describes but doesn't walk through end-to-end.

This guide is **not** a replacement for the canonical-law trio. The trio is the rule source. This guide explains how to operate under those rules without re-litigating them.

If you are looking for:
- the rules themselves → `core.md` + `github-reference.md`
- the kickoff prompt to paste into an AI → `prompts/greenfield.md`, `prompts/retrofit.md`, or `prompts/upgrade.md` (forthcoming at TASK-0025+)
- worked examples of what good artifacts look like → this guide, §10 onward
- project-type-specific guidance → `appendices/project-types/*.md` (forthcoming at TASK-0025+)
- documentation-MCP server selection guidance → `appendices/documentation-mcp-options.md` (forthcoming at TASK-0026+)
- positioning relative to other frameworks → `appendices/amas-vs-other-frameworks.md` (forthcoming at TASK-0026+)
- regulated-tier extension (HIPAA, PCI-DSS, SOX, GDPR, FDA 21 CFR Part 11) → `appendices/regulated-tier-extension.md` (forthcoming at TASK-0026+)

---

## §1. Before your first session

Three things to get right before you open a chat with an AI:

**§1.1. Clone into a non-synced directory.** Do not clone the repo into OneDrive, Dropbox, iCloud Drive, Google Drive File Stream, or any other real-time sync folder. The canonical-law trio explains why; the symptoms include git state corruption, phantom merge conflicts, and confused agentic file-watching. Put clones in `C:\dev\`, `~/code/`, `~/dev/`, or similar.

**§1.2. Know your entry path.** If the project is brand new (no code, no documents, no prior decisions), use the greenfield path (`prompts/greenfield.md`). If the project has any pre-existing durable state — code, a manual, a playbook, a spreadsheet of rules that has accumulated over years — use the retrofit path (`prompts/retrofit.md`). The framework rules are identical for both; only the first session differs.

**§1.3. Pick your first Architect candidate.** You do not need to have the final Architect / Builder / Reviewer assignment figured out before the kickoff session. The point of the kickoff is to produce that assignment. But you do need to pick one AI surface to run the kickoff session on. Usually this is whichever AI you find easiest to think with for architecture and scoping — ChatGPT Project, Claude.ai Project, or similar. That surface runs the kickoff; the scorecard it produces may or may not keep it in the Architect role afterward.

---

## §2. The kickoff session

The kickoff session is a single chat where you attach the canonical-law trio, paste the appropriate prompt, and answer the AI's questions until the kickoff packet is ready to commit.

**§2.1. Attach, then paste.** Both `prompts/greenfield.md` and `prompts/retrofit.md` assume `core.md` + `github-reference.md` are already in the AI's context when the prompt is pasted. If your chosen surface supports attachments or project knowledge files, attach the canonical-law trio first. If it only supports pasted context, paste the trio first as separate messages, then paste the prompt.

**§2.2. Use the standalone prompts.** Use the standalone greenfield, retrofit, or upgrade prompt at `prompts/`. The canonical-law trio defines the rules; the prompts wrap kickoff orchestration around the rules. The prompts may add operational scaffolding the canonical-law trio doesn't carry (operating-environment confirmation, three-tier framing surfacing, project-type appendix selection, multi-surface review pipeline opt-in). Use the prompts.

**§2.3. What the kickoff produces.** Full kickoff produces the bootstrap artifact set per `core.md` §3.1 (forthcoming at Part C+) — the list includes README, CODEOWNERS, AGENTS.md, CLAUDE.md, the canonical-doc reference, project-brief, tool-inventory, role-assignment-scorecard, the bootstrap ADR (ADR-000), GitHub Issue templates, and the GitHub PR template. Two artifacts that trip people up:

- `docs/handoffs/TASK-0000-project-bootstrap.md` — the handoff for the bootstrap task itself. TASK-0000 is reserved for this. The first real feature task is TASK-0001.
- `CODEOWNERS` — the repo-level governance file. It belongs in the bootstrap file list. If you don't know what to put in it yet, a single line with your GitHub username and the repo root is a valid starting point: `* @your-github-username`.

Lite kickoff produces a smaller set per `core.md` lite-kickoff specification. The trade-off: lite is faster but upgrades to full are one-way and have triggers you should know in advance.

**§2.4. Operating environment.** Both prompts ask about your operating environment before scoring the Tool Inventory. Answer honestly. If your project runs on a work laptop with an enterprise AI license and admin-managed GitHub access, that is a constrained-professional environment and the constrained-professional overlay applies. If it runs on your personal laptop with your personal accounts, it does not. A project running on the same machine can be personal for one repo and constrained-professional for another; the distinction is per-project, not per-machine.

**§2.5. Three-tier solo-operator framing.** AMAS calibrates to **production-tier** solo-operator governance by default (see §8 below). The kickoff prompt flags whether your project is light-tier (prototype / decision-logging-first), production-tier (real customers, the AMAS default), or regulated-tier (HIPAA / PCI-DSS / SOX / GDPR / FDA 21 CFR Part 11). The default works for most projects. Light-tier and regulated-tier are documented in §8 below + the regulated-tier-extension appendix.

**§2.6. When Builder and Reviewer must share an ecosystem.** In most projects you want Builder on one ecosystem (e.g., Claude Code) and Reviewer on the other (e.g., `@codex review` on GitHub). Cross-ecosystem independence is the single biggest reason the framework separates these roles. But some environments block one ecosystem entirely — policy-gated tools, admin-gated apps, or simply nothing installed. In those cases, apply the canonical fallback per `core.md`:
- Stronger documentation — every architecture-affecting change gets an ADR, not just the ones that feel durable.
- Stricter human approval — a human reads and signs off on architecture-heavy changes rather than letting the Reviewer's verdict stand alone.
- A TMP decision recording that the project is in the fallback with an explicit exit trigger — usually "when the other ecosystem becomes available."

The prompts call this out explicitly. If the AI produces a scorecard that puts Builder and Reviewer on the same ecosystem without invoking the fallback, push back.

**§2.7. Kickoff follow-ups.** Kickoff sessions — especially retrofit — often surface governance corrections that are out of scope for the kickoff PR but must land before the first feature stage. Common cases: a superseding ADR, a deferred-file addition, a branch-protection correction, a reframe-pending resolution. Record these in the Project Brief's "Kickoff follow-ups" section so the transition from kickoff to first feature stage is sequenced cleanly.

**§2.8. Reframe-pending flagging (retrofit only).** If a retrofit kickoff session reframes the project mid-session (e.g., from "running system" to "canonical specification document"), pre-reframe artifacts produced earlier in the same session may now conflict with post-reframe scope. Flag them as "reframe-pending" in the Project Brief rather than silently patching or ignoring. A downstream session resolves the conflict.

**§2.9. Architect-to-Builder prompt construction.** The first Architect-to-Builder prompt — the one that hands a task to the Builder after kickoff — applies `core.md` §23 prompt-construction discipline. The kickoff session doesn't produce that prompt, but it should mention §23 so the handoff to the first-feature session isn't caught flat-footed. See §9 of this guide for the §23 walkthrough.

**§2.10. Substantive-only Reviewer engagement.** If the scorecard lands a substantive-only Reviewer (bot reviewer via GitHub App — `@codex review`, `@claude`, or equivalent), `core.md` §8.1.1 governs what the Builder does with Reviewer findings starting on the first PR. The kickoff prompt flags this. See §7 of this guide for the §8.1.1 walkthrough.

---

## §3. First real task: issue → branch → PR → review → merge

Every real task after the kickoff bootstrap follows the same shape. Here's what you should see.

**§3.1. Issue.** The Architect opens a GitHub Issue with a TASK-#### prefix (`TASK-0001: Add session-export endpoint`). The TASK-#### is assigned at issue creation and is stable forever — it threads through every artifact the task touches.

**§3.2. Feature Brief (sometimes).** Not every task needs one. The canonical-law trio gives the rules: mandatory when the task changes user-visible behavior, spans more than one session, touches architecture beyond a single file, has unresolved edge cases, or is blocked on a design decision. Optional when the task is a bug fix, a single-function change, or the Issue title already fully describes the behavior change.

If a Feature Brief exists, it lives at `docs/features/FEAT-####-<slug>.md`. The FEAT-#### may be the same number as the TASK-#### for a single-task feature, or a separate number for a multi-task feature.

**§3.3. Branch.** The Builder creates a branch matching `<type>/<id>-<summary>` per `github-reference.md` §2.2 branch convention. Examples: `feat/0001-session-export`, `fix/0023-cache-bug`. A GitHub Action validates branch names on PR open per `github-reference.md` §6.2 anticipated Actions. Before creating the branch, the Builder runs pre-flight per `core.md` §8.2 (forthcoming at Part C+) to verify branch-name regex compliance, base-branch freshness, and working-tree state. Pre-flight is the catch point for branch-name regex mistakes — it is much cheaper than force-pushing a rename.

**§3.4. Handoff file.** The Builder creates or updates `docs/handoffs/TASK-####-<slug>.md` at the start of work per the universal handoff schema. The handoff carries the current state of the task: current branch, last completed step, blockers, exact next action, validation evidence. If you return to the task after any meaningful pause, the handoff is where you pick up — not the chat history. The "Exact next step" block in particular is what subsequent Architect-to-Builder prompts will reference (see §9 below).

**§3.5. PR.** When the Builder is ready for review, they open a PR against main with `.github/PULL_REQUEST_TEMPLATE.md` (the operational instantiation per `github-reference.md` §4.2; canonical source ships at `templates/PULL_REQUEST_TEMPLATE.md`) filled in. PR title starts with TASK-####. The PR body carries the most recent AI Session Log (or on multi-session PRs, the complete set of session subsections). Before `git push` and before `gh pr create`, the Builder runs stop-and-show per `core.md` §8.3 (forthcoming at Part C+): presents the exact branch name, commit title and body, PR body, and diff summary, then waits for explicit approval.

**§3.6. Ready-for-review.** Before the Builder marks the PR ready for review, they run through the PR template's Ready-for-review checklist. This is the single most useful mechanical gate in the framework. It catches task-ID / feature-ID mismatches, missing Feature Briefs, stale handoffs, unsupported validation claims, and the redaction rules.

**§3.7. Review.** The Reviewer runs the review protocol from `templates/review-template.md` Review guidelines (for Codex) or the equivalent Claude instruction set. In most AI-reviewer setups you will need to post `@codex review` or `@claude` as a PR comment to trigger the review manually — auto-review-on-PR-open is documented as a capability but does not fire reliably. On cross-ecosystem projects, the Reviewer also checks that the PR body's AI Session Log carries one subsection per distinct meaningful session, and surfaces Builder-side omissions of `core.md` §8.1.1 engagement rules (trigger, reply, resolution) as findings.

**§3.8. Builder engagement with findings.** Once the Reviewer's findings land, `core.md` §8.1.1 applies: the Builder re-invokes the Reviewer after every push addressing findings (rule a), replies to every line comment before bypass-merge naming the addressing commit SHA (rule b), and resolves threads only after a clean re-review (rule c). See §7 below for the walkthrough.

**§3.9. Merge.** The human merges. If the repo is single-contributor, the merge uses GitHub's bypass mechanism with explicit acknowledgment in the squash-commit message or a pinned PR comment per `core.md` §10.5 (forthcoming at Part C+). This is supported, not a workflow violation. Each bypass invocation acknowledges full operator responsibility for the merge state; no additional artifact is required at single-cycle scope per `github-reference.md` §3.2. Sustained-multi-contributor projects should document the bypass posture in an ADR.

**§3.10. Archive.** The human (or Builder in single-contributor mode) archives the final review-context into `docs/reviews/PR-####-codex-pre-commit.md` (Codex pre-commit) and the post-PR review state into the same review-context (or the PR body, depending on the project's adopted convention). The PR remains the working conversation; the archived copy is the durable record.

**§3.11. Post-merge note.** Optional for trivial changes. Required when the PR involved architecture change, workflow change, tool-assignment change, validation-strategy change, or unexpected review friction per `core.md` §18. PMN authoring lives at `docs/post-merge-notes/PMN-####-<slug>.md`. This is where the project learns from itself.

---

## §4. Session boundaries and write-back

The framework's continuity promise depends on one rule: at every session boundary, current state is written back to GitHub.

**§4.1. What counts as a session boundary.** A session ends when you commit and push, formally hand off, or step away for more than 30 minutes. These are the only three exits. Small commits in the middle of a flowing work session do not each need write-back; the session ending does.

**§4.2. What "meaningful" means.** A meaningful session changes scope, architecture, code, tests/validation, assumptions, blockers, or next-step ownership. Reading the repo, running tests without changing anything, or staring at a diagram does not make a meaningful session. Write-back is required after meaningful sessions only.

**§4.3. Where the write-back goes.** Placement rules per `core.md`:
- Before a PR exists: Issue comment + handoff update.
- After a PR exists: PR description or PR comment + handoff update.
- Durable architecture change: ADR.
- Temporary exception: `docs/decisions/TMP-*`.
- Substantive review: review-context.
- Review-engagement session: the session log's optional "Review engagement" field, populated when the session engaged with Reviewer findings.

**§4.4. Redaction.** Never paste secrets, tokens, raw credentials, or raw confidential payloads into durable artifacts. Reference-and-summarize instead. If the content is load-bearing for a decision, summarize the decision's reasoning without reproducing the data.

---

## §5. The TASK-#### / FEAT-#### ID system

**§5.1. Why the IDs matter.** As a repo grows, the most expensive retrieval is "find everything related to the session-export work." Without a stable ID, this is a full-text search across Issues, PRs, docs, and commits. With a stable ID, it's a single `grep -r TASK-0042 .`. The framework elevates this to a first-class rule so every artifact-producing session threads the ID.

**§5.2. TASK-#### assignment.**
- Four digits, zero-padded. `TASK-0001`, not `TASK-1` or `TASK-001`.
- Assigned at the point the task is first recorded — usually when the Issue is opened. The Architect makes the assignment.
- TASK-0000 is reserved for the project bootstrap / retrofit-adoption task. The first real feature task is TASK-0001.
- The ID does not change if the task is re-scoped, split, or merged with another task. Re-scoping produces new IDs for new tasks, not retroactive renumbering.
- Counter authority: the repo's highest-numbered existing TASK-#### across any artifact is authoritative. The Architect increments from that number. The Builder re-verifies this in pre-flight per `core.md` §8.2 (forthcoming at Part C+) before assuming a TASK-#### for a new task.

**§5.3. Where TASK-#### appears.**
- GitHub Issue title: `TASK-0042: Add session-export endpoint`
- Feature Brief filename (if one exists): `docs/features/FEAT-0042-session-export.md` (same numeric ID for single-task features by convention)
- Handoff filename: `docs/handoffs/TASK-0042-<slug>.md`
- PR title: `TASK-0042: add session-export endpoint`
- Branch name (numeric portion): `feat/0042-session-export`
- Review-context filename: `docs/reviews/PR-####-codex-pre-commit.md` (PR-#### is independent; review-context cross-references the TASK-####)
- Post-merge note, session logs, and non-code artifacts all carry the same TASK-####

**§5.4. FEAT-#### vs TASK-####.** A Feature Brief may aggregate multiple tasks. In that case the feature gets a FEAT-#### and each constituent task keeps its own TASK-####. For single-task features the two numeric IDs may coincide by convention but the prefixes are still distinct. The PR template Ready-for-review checklist checks both: the PR title's TASK-#### must match the Issue and handoff, and the linked Feature Brief's FEAT-#### must be the correct feature brief for this task.

---

## §6. Handoffs and session logs

Handoffs and session logs are related but distinct. Getting them confused is the most common source of bloat-drift on long PRs.

**§6.1. The handoff file is the task's durable state.** It lives at `docs/handoffs/TASK-####-<slug>.md` and carries the current state of the task: branch, last completed step, blockers, next action, validation. The handoff survives everything — PR squash-merge, PR close, branch deletion, role reassignment. If you ever lose a chat and need to resume, the handoff is where you resume from.

**§6.2. The AI Session Log is a per-session record.** Each meaningful session produces one. It records what happened in *that* session: objective, state, files changed, decisions made, assumptions, open questions, validation status, review engagement if any, next action, handoff target.

**§6.3. Single-session PRs: most recent log in the PR body.** Not every log — just the most recent. When you finish a new session, you update the PR body to show the new log, replacing the previous one.

**§6.4. Multi-session PRs: complete set in the PR body.** On cross-ecosystem projects, most PRs will involve more than one session — typically an Architect session that produces the artifact and a Builder session that opens the PR, sometimes followed by later Builder updates or Reviewer-requested changes. The rule: the PR body carries the *complete set* of session subsections needed to explain the current PR state, one per distinct meaningful session, chronologically ordered. When a new session occurs, the previous complete set migrates to the handoff's `## Session log archive` section, and the PR body is replaced with a new complete set that includes the new session.

A session that did not materially contribute to the PR's current state does not need its own subsection. The test is: did the session produce or change output that the PR is committing? If yes, subsection required. If no, it belongs only in the handoff session-log archive, not in the PR body.

**§6.5. Prior logs migrate.** Whether single-session or multi-session, prior PR-body content migrates to the `## Session log archive` section of the handoff file. Oldest at top, newest at bottom. An acceptable fallback is a PR comment posted before the PR body is replaced. Either way, the PR body always carries exactly the current state's complete set, so reviewers don't have to scroll past stale context.

**§6.6. Review engagement field.** The session log template carries an optional "Review engagement" section. Populate it only when the session engaged with Reviewer findings — it records which threads were addressed, replied-to, resolved, or left open. Sessions that didn't touch review threads leave the field empty or omit it entirely.

---

## §7. Builder engagement with substantive-only Reviewer findings

`core.md` §8.1.1 governs what the Builder does once a substantive-only Reviewer's findings land. It applies on GitHub-hosted projects with a GitHub App Reviewer (`@codex review`, `@claude`, or equivalent); projects on other platforms need analog rules that §8.1.1 does not prescribe.

The three rules in plain operational terms:

**§7.1. Rule (a) — Trigger after every push.** The Reviewer's "auto-review on PR open" is unreliable, and that unreliability extends to follow-up pushes. Every push that changes what the Reviewer would review — initial push, fix-a-finding push, scope-expansion push, anything — needs a re-review. If auto-review hasn't fired after a brief wait consistent with the repo's normal behavior, the Builder posts `@codex review` (or the equivalent) manually. If manual invocation becomes repetitive across a repo, add a GitHub Action per `github-reference.md` §6.2 anticipated Actions that posts the invocation on every push automatically.

**§7.2. Rule (b) — Reply before bypass-merge.** Every Reviewer line comment gets a Builder reply before bypass-merge. The reply is short: name the commit SHA that addressed it and state in one sentence how. For unaddressed findings: either reference the follow-up PR/Issue that will handle it, or state the reason for declining with any supporting ADR or Feature Brief reference. Silent pushes that address findings without thread engagement are not acceptable.

**§7.3. Rule (c) — Resolve only after a clean re-review.** GitHub's default is that the reviewer who raised a thread resolves it. That convention works for human reviewers but breaks for bot reviewers. Under §8.1.1, the Builder resolves a thread when and only when: (i) they've replied per rule (b), (ii) they've re-invoked the Reviewer per rule (a) on the push that addresses the finding, and (iii) the re-review does not re-raise the finding or raise a net-new related finding. If the re-review re-raises it, the thread stays open.

**§7.4. Three-endpoint poll for "no findings" assertions.** Per `core.md` §8.1.1.1 canonical text, Codex post-PR review output may emit at any of three endpoints: (a) `pulls/{pr}/reviews` (formal Pull Request Review), (b) `issues/{pr}/comments` (issue-comment summary), (c) `pulls/{pr}/comments` (line-level review-comments). A "no findings" assertion requires polling all three endpoints and either (i) at least one endpoint returns substantive verdict content, OR (ii) a 5–10 minute settling period has elapsed with all three endpoints stable empty. Single-endpoint check OR single-poll is a verify-before-assert failure per `core.md` §24.2(a).

**§7.5. Reviewer claimed-action verification (§8.1.1.2).** Some Reviewer surfaces produce output describing claimed actions (commits, files, follow-up artifacts, identifier patterns) that may not match actual repo state — typical of Reviewer surfaces with non-transparent tool-execution paths. The Builder verifies each claimed action across four claim categories: (i) commit existence (the commit by SHA exists at the claimed location), (ii) file existence (the file exists at the claimed path), (iii) follow-up artifact existence (the PR/Issue/branch/comment exists), (iv) identifier-pattern compliance (filenames, numbers, prefixes match actual project state and convention). The four categories are empirically grounded; novel categories surfacing in field evidence are §18 PMN candidates.

**§7.6. Multi-surface review pipeline — converging lines of evidence.** No single review surface catches all defect classes. The framework's empirical pipeline is five surfaces:
1. **Architect §23.6 self-review** (iterative-to-fixed-point per §23.6.2 + §23.6.3 reference-verification before authoring) — catches prose-arithmetic, recapitulation-consistency, §-citation correctness, Architect-asserted-without-verification claims.
2. **Builder pre-flight (§8.2 (forthcoming at Part C+))** — catches frontmatter convention divergence, structural-element count off-by-one, line-number off-by-one in code references, section-structure form divergence (per §23.6.3 sub-shapes A/B/C/D).
3. **Builder step-6 self-review** — catches verification-command operational correctness, frontmatter-vs-body scope mixing, §-citation residuals that escape Architect sweep, claim-scope mismatches.
4. **Codex desktop pre-commit** — catches verification-artifact internal consistency, cross-claim consistency, canonical-text correctness pre-commit.
5. **Codex cloud post-PR** — catches substantive content findings, advisory/blocking contradictions, v2.14.1-vs-repo-convention divergences, boundary cases.

Each surface catches distinct defect classes; multi-surface composition is structurally load-bearing. The framing follows the "converging lines of evidence" principle: no single surface is sufficient; the surfaces are not redundant; their composite is the discipline.

**§7.7. Timer heuristic (not framework rule).** In practice on reference projects using `@codex review`, a 2–5 minute wait is usually long enough to tell whether auto-review is going to fire. The framework deliberately doesn't hardcode that number — it varies by CI configuration, GitHub App health, and network conditions. But as a practical heuristic, "wait about 5 minutes, then invoke manually" is a reasonable starting point.

**§7.8. If the scorecard lands a human Reviewer instead.** §8.1.1 is scoped to substantive-only Reviewers. If the Reviewer is a human with write access, GitHub's default convention holds — the human reviewer resolves threads, and rule (c) does not apply. Rules (a) and (b) apply in spirit (humans benefit from re-review triggers and reply discipline too) but are not framework-mandated for human reviewers.

---

## §8. Operating environment + three-tier solo-operator framing

**§8.1. Environment is per-project, not per-user.** One person can operate the framework on a personal project (laptop, personal GitHub, personal AI subscriptions) and a work project (managed laptop, org-managed GitHub, enterprise AI licensing) simultaneously. The framework doc itself doesn't change; per-project artifacts do. Expect different Tool Inventory contents, different Scorecard results, different Reviewer modes, and possibly different TMP decisions per project.

**§8.2. Tool Inventory access-type tags.** The canonical-law trio's tags represent what's actually available:
- `available` — confirmed usable right now.
- `subscription-gated` — tool exists; blocked by a plan/license we don't have. Changes with subscription.
- `policy-gated` — tool exists and is purchasable; blocked by org policy. Durable until policy changes.
- `admin-gated` — tool is usable at repo/org level but requires admin action we can't perform.
- `not-yet-attempted` — plausibly available but not yet set up.

The Role Assignment Scorecard is scored against the `available` set, not the aspirational set. `policy-gated` and `admin-gated` are the durable constraints worth surfacing loudly.

**§8.3. The constrained-professional overlay.** Not a standalone profile but an overlay. You pick a base profile (App/API, Data/Quarto, Automation, or default) and then adjust weights against observed constraints in the Tool Inventory. The overlay does not hard-code weight numbers because the framework has limited multi-environment evidence so far; numeric calibration is a future-release concern.

**§8.4. Agent autonomy.** Three distinct limits on running autonomous code-writing agents:
- **Policy constraint** — an AI-use policy says agents may not modify files without human review.
- **Permission constraint** — admin rights required, MDM blocks, or network restrictions prevent the agent from functioning.
- **Trust-of-use constraint** — the tech works and policy permits it, but the project owner has not yet established trust for unattended agent authority.

The three produce the same observable behavior ("no autonomous agents running") but have different exit conditions. Record the decision in the Project Brief's Operating environment block, name the binding mechanism, and state the revisit trigger. Agent-autonomy posture is operational state, not durable architecture — transitions are TMP decisions or notes, not ADRs.

**§8.5. Three-tier solo-operator framing.** Solo-operator governance has three tiers:

- **Light tier.** Prototype-class projects, weekend hacks, decision-logging-first solo dev. Minimal Actions; documentation-only AMAS adoption optional; the bypass mechanism may be over-elaborate. Adopters can simplify in their own ADR.
- **Production tier (AMAS default).** Solo developer, real customers, production traffic. The bypass mechanism's structural separations (Architect identity, claim verification, CODEOWNERS exclusion) match what real solo-operator production projects need. AMAS calibrates to this tier as default.
- **Regulated tier.** Solo developer in regulated domains — HIPAA, PCI-DSS, SOX, GDPR, FDA 21 CFR Part 11. May want more than AMAS provides — full AI-decision audit trails, model-version pinning enforced, blocked egress for AI inference. AMAS provides the discipline structure; regulated-tier specifics live at `appendices/regulated-tier-extension.md` (forthcoming at TASK-0026+).

The kickoff prompt asks which tier applies. Most solo developers are at production tier. If you're at light tier, you can simplify in your kickoff ADR. If you're at regulated tier, the regulated-tier-extension appendix is required reading.

---

## §9. Architect-side prompt construction + pre-handoff self-review

`core.md` §23 governs how the Architect writes prompts that direct Builder sessions. It complements `templates/CLAUDE.md` / `templates/AGENTS.md` (Builder-facing instruction files) and `templates/review-template.md` (Reviewer-facing operational template) by addressing the prompt-authoring side, not by adding a new repo-level file. No `ARCHITECT.md` is required.

**§9.1. Two prompt shapes.** Every Architect-to-Builder prompt collapses to one of two shapes:

- **Handoff-driven** — a handoff file exists for the task. The prompt points the Builder at the handoff, instructs it to read and confirm the plan, and stops before execution. The prompt is thin; the handoff carries the detail.
- **Direct-instruction** — the task is small enough that a handoff file is overhead. The prompt carries the full mechanical sequence inline. Good for: a small fix after a Reviewer finding, a status-field update, a rerun of an existing command, a scope-adjustment that doesn't justify opening a handoff.

If the task is large or multi-session and no handoff exists yet, produce the handoff first and use the handoff-driven shape.

**§9.2. Required prompt elements.** Regardless of shape, every prompt needs: opening framing (one or two sentences on owner/role/goal), concrete file locations (absolute paths for outside-the-repo, repo-relative for inside, don't mix), mechanical sequence (numbered shell-level steps), stop conditions (with a catch-all as the last condition), scope protection (specific "do not" items, not "stay in scope"), and a hand-back point (exact step + what's handed back).

In practice on reference projects, prompts tend to carry three to six stop conditions and two to five scope-protection items. The canonical §23.2 deliberately does not hardcode these counts; they vary by task.

**§9.3. Stop conditions are the element most often omitted.** Of the six required elements, stop conditions are the most commonly missed and the most commonly responsible for over-extension past the intended stop point. When the Builder gets a prompt without stop conditions, the Builder's drive toward completion fills the gap, often past where it should have handed back. When in doubt, name more stop conditions rather than fewer.

**§9.4. Architecture decisions don't belong in Builder prompts.** A prompt that tells the Builder to decide an architecture question is an architecture decision made outside the ADR mechanism. Test every prompt condition for mechanical-vs-judgment: if there's one right answer (branch-name conflict → add suffix, stash-then-apply → standard sequence), put the decision in the prompt. If there's judgment involved (TASK-ID shifts, scope-drift triage, Reviewer-finding triage, ADR supersession), the prompt instructs the Builder to stop and surface the condition, not to decide it. When in doubt, treat it as a judgment condition and stop.

**§9.5. Hand-back points are explicit.** "When you're done" is not a hand-back point. "After the PR is open and the Reviewer posts its review, hand back with PR URL and Reviewer findings verbatim, before merge" is. Bypass-merge is the human's action; the Builder never performs it.

**§9.6. Inherited owner preferences.** Applies only when owner preferences about Architect-to-Builder prompting have accumulated across sessions or contributors. Solo single-contributor projects where one human plays both roles can skip this. Where it applies: the Architect inherits preferences from prior sessions as defaults (filesystem vs. pasted content, verification-gate explicitness, always-human actions, surface trust levels). Repos can codify project-specific preferences in `docs/architect-reference.md`; the framework-level §23 covers most cases without it.

**§9.7. Pre-handoff self-review (§23.6).** Before handing an artifact to the Builder, the Architect runs three sub-section disciplines:

- **§23.6.1 — Prose-arithmetic decomposition** with cumulative-diff-stats re-derivation per §23.6.1.1 (e.1) sub-rule. Every arithmetic claim in the spec text is decomposed into operand expressions; cumulative-diff-stats are re-derived from `git diff --shortstat` (or staged-tree equivalent) at pre-commit time, not propagated from prior iterations.

- **§23.6.2 — Iterative-to-fixed-point self-review.** Run sweep passes until no new defects surface. Per PMN-006 empirical record, single-iteration self-review is insufficient; the discipline is iteration-to-convergence. Sweep set categories per PMN-006 §3 + §7: (g) verification-artifact internal consistency, (h) verification-command operational correctness with sub-shapes (h.1)/(h.2)/(h.3)/(h.4), (i) cross-document state verification with sub-shapes (i.1)/(i.2)/(i.3)/(i.4)/(i.5).

- **§23.6.3 — Reference-verification before spec authoring.** Every specific reference value in the spec text is either (i) verified against actual canonical source at authoring time (sub-shapes A/D — convention shapes and form structures), or (ii) explicitly marked as deferred for Builder pre-flight (i.5) batch verification (sub-shapes B/C — line numbers and structural-element counts). Plus standing pre-authoring data-currency precondition: data sources used for verification are themselves current.

**§9.8. §24 cross-surface verify-before-assert meta-pattern.** `core.md` §24 names the meta-pattern that §8.1.1.1, §23.6, §8.2 (forthcoming at Part C+), and §8.3 (forthcoming at Part C+) have all been applying as specific instances. The failure shape: an actor (Architect, Builder, or Reviewer) asserts a fact about an external system, an artifact's content, or a receiving-side expectation without verifying it against actual state, and the assertion turns out to be wrong. The mitigation is at the receiving surface — receiving-side caveat-discipline catches the divergence before damage propagates.

**§9.9. Five receiving directions of caveat-discipline (§24.3).** Five surfaces apply receiving-side caveat-discipline:
1. Builder pre-flight against Architect-asserted external-system state in prompts (§8.2 (forthcoming at Part C+))
2. Architect pre-handoff self-review against own-authored claims (§23.6, §23.6.1, §23.6.2, §23.6.3)
3. Builder receiving Reviewer findings (§8.1.1, §8.1.1.1, §8.1.1.2)
4. Owner receiving Builder stop-and-show (§8.3 (forthcoming at Part C+))
5. Architect ← Builder hand-back (§24.3.1)

**§9.10. §24.3.1 default Architect-side post-handback five-point check.** When Builder hands back to Architect at cycle close, the Architect runs:
1. Three-endpoint poll of Reviewer output (per §8.1.1.1) — confirm Reviewer output as Builder reported it; reconcile against last-known-state via all three endpoints.
2. Branch tip-SHA verification — `git rev-parse HEAD` output must match the expected SHA from the prior session's hand-back; additionally `git status --porcelain` must be empty.
3. File content audit against prescription — for each file Builder claims to have authored or modified, verify content matches the spec's prescription.
4. Phantom-action audit — verify no claimed action lacks corresponding repository state.
5. Comment-content claim verification (per §8.1.1.2) — for any Reviewer comment Builder reports as adjudicated, verify the comment's substantive content claims against actual repository state.

A project may codify a project-specific check pattern in repo-local Architect reference. The five-point pattern is the default.

**§9.11. §8.1.1.3 bounded-continuation rule and cost-class refinement.** Iterative fix-up cycles on the same defect class within a single cycle have a bounded-continuation discipline. Per PMN-007 §2.4 cost-class refinement: pure-token-swap defect class (mechanical substitution; example: §-citation correction, line-number off-by-one fix) converges at one-iteration fixed-point; Codex re-invocation is discouraged for pure-token-swap fix-ups. Genuinely-asymptotic defect class (requires structural decisions, multi-document reconciliation, ADR-class durable decision) warrants additional iteration cycles. Distinguishing the two at adjudication time is the discipline.

**§9.12. Failover protocol (§2.3.7 (forthcoming at Part C+)).** When a role holder becomes temporarily unavailable mid-task — usage limit hit, API rate limit, model outage, auth/connector failure — the project does not silently switch to a different tool. §2.3.7 (forthcoming at Part C+) specifies the protocol: pause and preserve state, classify task risk by principles, preserve ecosystem separation through one of three named compensating-review options (A: opposite-ecosystem app Reviewer; B: human owner; C: deferred review with named maximum window), decide task-local vs §2.3.4 (forthcoming at Part C+) re-evaluation, name return-to-normal trigger. Failover handoff lives at `docs/handoffs/FAILOVER-TASK-####-<date>.md`.

**§9.13. Unavailable technical controls (§2.2.2 (forthcoming at Part C+) + §5.4 (forthcoming at Part C+)).** When the operating environment prevents technical enforcement of an intended governance control (branch protection rulesets, CI checks, required-approval policies, GitHub Apps), a TMP decision is required before feature work continues. The TMP names the intended control, the gap, the procedural mitigations, and exit triggers. The project must not document or imply technical enforcement of policy-only controls.

---

## §10. Friction patterns

**§10.1. "The Architect's prompt asserted something about gh CLI behavior that turned out to be wrong, and I caught it during pre-flight."** External-system-behavior assertion failure per `core.md` §24 sub-shape (a). The Builder's pre-flight per §8.2 (forthcoming at Part C+) catches this when the assertion would gate a destructive or remote-visible action. Beyond §8.2 (forthcoming at Part C+)'s enumerated checks, surface "the prompt says X; my actual finding is Y; here is the divergence" rather than silently working around the discrepancy.

**§10.2. "The handoff's cross-reference points to a section that doesn't exist."** Artifact-content assertion failure per `core.md` §24 sub-shape (b). §23.6.2's internal-consistency check covers the artifact being handed off; cross-document references and time-stale validation evidence require analogous discipline at handoff-time.

**§10.3. "The Reviewer flagged a finding and the Architect's fix-up extended it to a sibling line that turned out to not have the same problem."** Fix-scope over-extension per `core.md` §24 sub-shape (d). The mitigation is mechanical literal-match verification at the Builder execution stage — `str_replace`'s literal-match check or analogous mechanical verification rejects the unwarranted extension's `old_str` because it doesn't exist in the file as the Architect remembered it.

**§10.4. "The Reviewer caught a miscount or an un-swept term in my handoff artifact."** §23.6.2 case. Two sub-checks prevent it and both are needed. Sweep verification: before handing off, run a full-file search on every distinctive term you edited during the session — term names, finding IDs, convention tokens, section references. Cascade misses (same term appearing in the edited line plus 2–5 other places that need the same correction) are the common pattern. Derived-count recomputation: re-derive every tally, total, or enumeration size from current content, not from memory of an earlier draft state.

**§10.5. "The Reviewer caught a §-citation that points to a section that doesn't exist in HEAD."** §23.6.3 sub-shape A or B. The pre-authoring (i.5) sweep against the actual canonical document's `^#` heading set catches this before handoff. Build a list of all §-citations in the artifact via `grep -nE "<canonical-file>\.md §[0-9]+"`, verify each against the canonical document's current heading set via `grep -nE "^#{1,6} §" <canonical-file>.md`, and reconcile divergences.

**§10.6. "The Reviewer pre-commit pass came back clean but post-PR caught something the pre-commit pass missed."** Multi-surface review pipeline working as designed (§7.6). Each surface catches distinct defect classes; pre-commit catches verification-artifact internal consistency, post-PR catches substantive content findings and boundary cases. Both surfaces are load-bearing.

**§10.7. "I'm placing an externally-authored artifact and the Reviewer caught an acceptance-criteria gap I missed."** §23.6 scope-clarification case. The acceptance-criteria sweep applies to externally-authored artifacts the Architect handles for placement, not just Architect-authored artifacts. Architect-time discovery is one re-engagement; Reviewer-time discovery is the same re-engagement plus a fix-up cycle on an open PR. Run §23.6 against the externally-authored artifact at the same point in the cycle you would run it against an Architect-authored artifact.

**§10.8. "I just realized this project has been running §18 conversationally and never produced a single PMN file."** §18 form specification case. PMNs are repo-tracked artifacts under `docs/post-merge-notes/PMN-####-<slug>.md`. The first PMN authored under the convention should explicitly address retroactive-backfill considerations for prior §18-eligible PRs — owner decides whether to author retrospective notes; the framework does not mandate retrospective backfill.

**§10.9. "Codex (or `@claude`) gave me two different reviews on the same commit."** §8.1.1.1 case. This is the abnormal case the section is scoped for, and it is most often correlated with a configuration-state change mid-cycle — Reviewer-environment configuration, GitHub App re-installation, auth/token rotation, permission grants. Steady-state Reviewer behavior is single-trigger single-output. When you see two outputs and they don't agree: substantive findings beat sentinels by default, the Architect-supplied inline reply names the sentinel and identifies the substantive finding as authoritative (with link to the sentinel for audit), and resolution still requires a clean re-review per §8.1.1 rule (c).

**§10.10. "An ADR I wrote three weeks ago turned out wrong. Should I edit it?"** No. Per `core.md` §17.5 (forthcoming at Part C+) (or canonical equivalent): accepted ADRs are not edited in place. Write a new ADR that supersedes the old one. Update the old ADR's Status field to `superseded by ADR-###` and leave its Context / Decision / Alternatives sections unchanged. The narrow exception is typographical corrections — broken links, misspelled names, formatting — anything that doesn't change the decision.

**§10.11. "A new ADR only supersedes part of an older one."** Permitted optional qualifier on the Status line: `Status: accepted; partially superseded by ADR-### (<scope>)`. Use it when the new ADR invalidates one section of the old ADR while leaving the rest in effect.

**§10.12. "The Builder proceeded silently and hit a CI failure."** That is a §8.2 (forthcoming at Part C+) pre-flight gap. The Builder should have stopped and reported before the action that failed. Feed this back: name the preconditions that were not checked, and ask the Builder to confirm them explicitly before the next destructive step. If the pattern repeats across multiple PRs, escalate.

**§10.13. "The Reviewer's review threads are piling up unresolved."** On substantive-only Reviewer PRs, the Reviewer doesn't re-engage with individual threads after its initial review. Under §8.1.1 rule (c), the Builder resolves threads — but only after replying (rule b), re-invoking the Reviewer (rule a), and confirming the re-review didn't re-raise the finding.

**§10.14. "Every follow-up push needs a manual `@codex review`."** Yes — §8.1.1 rule (a) names this explicitly. Auto-trigger on follow-up pushes is as unreliable as auto-trigger on PR-open. If manual invocation becomes a recurring drag, add a GitHub Action that posts the invocation comment on every push (per `github-reference.md` §6.2 anticipated Actions).

**§10.15. "My Architect keeps writing prompts that tell the Builder to decide architecture questions."** §23.3 is the check. Every prompt condition gets tested: is there one right answer (mechanical), or is there judgment involved? If judgment, the prompt instructs the Builder to stop and surface the condition, not to decide it.

**§10.16. "The Builder over-extended past where it should have handed back."** Check the prompt's stop conditions and hand-back point. The most common cause is a vague hand-back point ("when you're done") rather than a specific one ("after the PR is open and Reviewer posts its review, hand back with PR URL and Reviewer findings verbatim, before merge").

**§10.17. "My Builder hit a usage limit mid-task and I'm tempted to just have the Reviewer take over."** Don't switch silently. Run §2.3.7 (forthcoming at Part C+). The protocol takes minutes: pause and capture inherited state per the failover-handoff template, classify the task as low-risk or high-risk by principles, name the compensating-review option (A opposite-ecosystem app, B owner, or C deferred), and record the return-to-normal trigger.

**§10.18. "GitHub won't actually enforce my branch protection rulesets on this repo."** §2.2.2 (forthcoming at Part C+) + §5.4 (forthcoming at Part C+) case. Private personal repos, certain account types, and specific org configurations may not technically enforce branch protection or required-approval policies even when the settings are configured. The required response is a TMP decision naming the intended control, the enforcement gap, the procedural mitigations, and exit triggers. Do not document the control as "enforced" anywhere when it is in fact only policy-enforced.

**§10.19. "The cycle handoff from a previous Architect session referenced a count that turned out to be wrong."** §23.6.3 case. Architect-side reference-verification before spec authoring is the discipline. Either verify the count against canonical source at authoring time (sub-shape A/D path), or explicitly mark as deferred for Builder pre-flight (i.5) batch (sub-shape B/C path). Don't assert specific counts from memory or from inherited cycle-artifact text without verification.

**§10.20. "The cycle anticipated a PR number that turned out to be off by one because an intervening cycle consumed a number."** §23.6.3 boundary case (provisional sub-shape E — externally-determined-at-consumption values). PR numbers, squash SHAs, auto-fire bot timestamps, GitHub-assigned IDs are externally-determined at consumption time. Mark them in spec as "verify at PR-open" or "Builder substitutes at consumption time"; don't commit to specific values at spec authoring.

**§10.21. "Cumulative-diff-stats from `git diff origin/main` don't match what's on the working tree."** Cumulative-diff-stats on untracked working tree don't include new files. Use `git diff --staged --shortstat origin/main` after `git add` of all modified + new files; reconcile per-file decomposition arithmetic against the staged-tree total. (e.1) sub-rule applies at the staged-tree surface.

**§10.22. "The Codex post-PR auto-fire emission landed before I posted `@codex review`."** This is the (w) candidate observation pattern (autonomous emission before owner trigger). Verify the emission is autonomous (not a triggered emission timestamped after a trigger you might have missed) by polling all three endpoints per §7.4 and reconciling timestamps; autonomous emissions can land at any of the three endpoints, not only `issues/<pr>/comments`. Autonomous pre-trigger emissions are useful supplemental review-evidence but don't substitute for the formal three-endpoint poll per §7.4.

---

## §11. Lite → full transitions

**§11.1. Lite → full triggers.** Move from lite to full when any of these fire: a second contributor joins; scope expands beyond the original definition of done; a second ADR (beyond ADR-000) is needed; the project passes one week of active work; the project becomes user-facing or gains a deployment target. When in doubt, upgrade.

**§11.2. The upgrade itself.** The current Architect owns it. It's a single bounded session: create the missing artifacts, open the deferred folders (`docs/questions/`, `docs/decisions/`, `docs/handoffs/`, etc.), and backfill the handoff file from the most recent PR. It is not a rewrite — pre-upgrade work stays as it was.

**§11.3. v3 inter-version upgrades.** Future v3.x → v3.y transitions are covered by `prompts/upgrade.md` (forthcoming at TASK-0025+). v3.0 → v3.1+ deprecation is deferred per transition plan v0.2 Decision A — v3.0 is restructure-only; substantive deprecation lands at v3.1+.

---

## §12. What this framework is not

Four things this framework deliberately does not do, so you do not have to litigate them with your AI of choice:

**§12.1. It does not hard-code vendors to roles.** The Architect / Builder / Reviewer assignments come from the scorecard, not from tradition. If ChatGPT scores better as Architect this month, it's the Architect. If Claude Code scores better next month, Claude Code is the Builder. Cross-ecosystem independence between Builder and Reviewer is the structural rule; which specific model holds which specific role is evidence-driven.

**§12.2. It does not require scaffolding before the first project.** Extension points (Claude skills, Custom GPTs, hooks, subagents) are optional. Build them only after observed friction shows where automation actually helps. The one accelerator reasonable to build pre-project is repo scaffolding — a cookiecutter, shell script, or skill that generates the canonical folder structure in one command — because that friction is obvious from day one.

**§12.3. It does not pretend durable memory lives in AI chats.** The canonical rule is: if it is not written into GitHub, it does not exist. Every chat can be lost, every project surface can be deprecated, every model can change. The artifacts in `docs/` are what survives.

**§12.4. It does not require a repo-level instruction file for the Architect.** The canonical-law trio specifies Architect discipline at `core.md` §23 (prompt construction), §23.6 (pre-handoff self-review), §24 (cross-surface verify-before-assert), §24.3.1 (post-handback five-point check), and the §-cluster around §8.1.1 (Reviewer-output absorption). Repo-specific owner preferences can optionally live in `docs/architect-reference.md` but are not required.

---

## §13. One-page reference

- **Canonical-law trio:** `core.md` (rules) + `github-reference.md` (GitHub-specific implementation) + `usage-guide.md` (this guide). Trio wins on rule conflicts.
- **Kickoff prompts:** `prompts/greenfield.md` (new project) / `prompts/retrofit.md` (existing project) / `prompts/upgrade.md` (inter-version upgrade). Forthcoming at TASK-0025+.
- **Bootstrap file list:** README, CODEOWNERS, CLAUDE.md, AGENTS.md, canonical-law trio reference, project-brief, tool-inventory, role-assignment-scorecard, ADR-000, GitHub Issue templates, GitHub PR template.
- **TASK ID reservation:** TASK-0000 = bootstrap. TASK-0001 = first real task.
- **Handoff path:** `docs/handoffs/TASK-####-<slug>.md` per universal handoff schema.
- **Review-context path:** `docs/reviews/PR-####-codex-pre-commit.md` (Codex pre-commit) + post-PR review state recorded into same review-context.
- **PMN path:** `docs/post-merge-notes/PMN-####-<slug>.md` per `core.md` §18 form.
- **ADR path:** `docs/adr/ADR-###-<slug>.md` per `core.md` ADR convention.
- **Failover handoff path:** `docs/handoffs/FAILOVER-TASK-####-<date>.md` per §2.3.7 (forthcoming at Part C+).
- **Five receiving directions of caveat-discipline:** Builder pre-flight (§8.2 (forthcoming at Part C+)), Architect pre-handoff self-review (§23.6), Builder receiving Reviewer findings (§8.1.1), Owner receiving Builder stop-and-show (§8.3 (forthcoming at Part C+)), Architect ← Builder hand-back (§24.3.1).
- **Five-surface review pipeline:** Architect §23.6 self-review → Builder pre-flight → Builder step-6 self-review → Codex desktop pre-commit → Codex cloud post-PR.
- **Architect-side post-handback five-point check:** three-endpoint poll, branch tip-SHA verification, file content audit, phantom-action audit, comment-content claim verification.
- **§23.6 self-review sub-sections:** §23.6.1 prose-arithmetic decomposition (with §23.6.1.1 (e.1) cumulative-diff-stats re-derivation) + §23.6.2 iterative-to-fixed-point + §23.6.3 reference-verification before spec authoring.
- **Three-endpoint Codex poll per §8.1.1.1:** `pulls/{pr}/reviews` + `issues/{pr}/comments` + `pulls/{pr}/comments`. No-findings assertion requires all-three-empty + 5-10 minute settling period OR substantive verdict at any endpoint.
- **Three-tier solo-operator framing:** light (prototype) / production (AMAS default) / regulated (HIPAA/PCI/SOX/GDPR/FDA — see regulated-tier-extension appendix).
- **Cost-class refinement per §8.1.1.3:** pure-token-swap (one-iteration fixed-point) vs genuinely-asymptotic (requires structural decision). Codex re-invocation discouraged for pure-token-swap.
- **Bypass rule:** Single-contributor repos bypass with acknowledgment in the squash-commit message, PR comment, or PR template `Bypass used` field per `github-reference.md` §3.2; sustained-multi-contributor projects document bypass posture in an ADR.
- **ADR edit discipline:** Accepted ADRs are not edited in place. Supersede with a new ADR; update the old one's Status to `superseded by ADR-###`. For partial supersession: `Status: accepted; partially superseded by ADR-### (<scope>)`.
- **Executor pre-flight per §8.2 (forthcoming at Part C+):** Before any repo-writing action, verify base branch, working-tree state, file-existence assumptions, CI-format compliance, numerical identifier assumptions, base-branch freshness. Stop-and-report on failure.
- **Stop-and-show per §8.3 (forthcoming at Part C+):** Before `git push`, `gh pr create`, `gh pr edit`, branch deletion, force push, out-of-scope file edits — present exact planned action and wait for explicit approval.
- **Architect-to-Builder prompt construction per §23:** Two shapes — handoff-driven or direct-instruction. Every prompt carries opening framing, concrete file locations, mechanical sequence, stop conditions, scope protection, hand-back point.
- **Status field (5 options):** `proposed | active | blocked | resolved | stale`. ADRs use a different 4-option set: `proposed | accepted | superseded | deprecated`, with optional partial-supersession qualifier.
