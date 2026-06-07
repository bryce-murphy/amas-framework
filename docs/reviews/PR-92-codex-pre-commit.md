---
status: drafted
---

# PR-92 Codex desktop pre-commit review

> PR-NN->PR-92 phantom-correct applied at PR-open (live `gh pr list --state all` confirmed highest merged = 91 -> PR-92; FX-B: only `pr` field + this filename + this body corrected; handoff `linked_pr` and core.md §18.3 `PR-NN` stay literal until post-merge PMN-001(k) chore).

## Metadata

- PR: PR-92 (https://github.com/bryce-murphy/amas-framework/pull/92)
- Branch: feat/task-0050-v3.1-action-layer-enablement
- Cycle: TASK-0050 (v3.1 action-layer enablement — surfaces.yml schema reconciliation + release-track bump posture)
- Linked handoff: docs/handoffs/TASK-0050-v3.1-action-layer-enablement.md
- Status: drafted
- Codex desktop session timestamp (UTC): 2026-06-06

## Builder claims to verify

All commands run from repo root at staged-tree state (`git add -A` applied). RELAY-ORDERING: this is the **pre-commit** pass; the binding post-PR re-review is invoked only AFTER PR-open + any finding-addressing push.

1. **Canonical-law trio frontmatter carries framework_version: 3.0.1 across all three files.** Verifiable at pre-commit:
   - bash: `git grep --cached -n 'framework_version: 3.0.0' -- core.md github-reference.md usage-guide.md` returns **no lines** (all flipped to 3.0.1).
   - bash: `git grep --cached -n '^framework_version:' -- core.md github-reference.md usage-guide.md` returns three lines, all `3.0.1`.
   - Class: spec §5.1 Class A currency; PMN-019 §2.(v) bidirectional sweep.

2. **AGENTS.md:9 / CLAUDE.md:9 carry two-concept framing; "published" does not attach to v3.0.1.** Verifiable at pre-commit:
   - bash: `grep -n 'Active framework version' AGENTS.md CLAUDE.md` returns two lines, both containing "active, in development in this repository" and "latest published release v3.0.0".
   - bash: `git grep -nE 'v3\.0\.1[^.;]*publish|publish[^.;]*v3\.0\.1' AGENTS.md CLAUDE.md README.md core.md github-reference.md usage-guide.md` returns **no lines** (attachment predicate: no "published" clause attaches to v3.0.1 in any canonical surface).
   - Class: Codex pre-commit [F1] FX1+FX2 class sweep; spec §5.1 two-concept framing.

3. **README L9 two-concept form: v3.0.1 labeled in-development; v3.0.0 labeled published adopter-facing.** Verifiable at pre-commit:
   - bash: `grep -n 'v3\.0\.1\|v3\.0\.0' README.md | head -5` — L9 contains "**v3.0.1** (in development" and "**v3.0.0** — the adopter-facing version of record".
   - bash: `grep -c 'published from this repository' README.md` returns `2` (existing historical sentence L7 + Status section; v3.0.1 line does NOT carry this clause).
   - Class: spec §5.1 R1 two-concept form; Gate-A R1.

4. **§7.1 unified surfaces: list-form present; old templates: map-form gone.** Verifiable at pre-commit:
   - bash: `sed -n '/^### .*7\.1\. /,/^### .*7\.2\. /p' github-reference.md | grep -c '  templates:'` returns `0`.
   - bash: `sed -n '/^### .*7\.1\. /,/^### .*7\.2\. /p' github-reference.md | grep -c 'surfaces:'` returns `>=1`.
   - bash: `sed -n '/^### .*7\.1\. /,/^### .*7\.2\. /p' github-reference.md | grep -c 'template_version'` returns `>=1`; `| grep -c 'agents'` returns `>=1`.
   - bash: `sed -n '/^### .*7\.1\. /,/^### .*7\.2\. /p' github-reference.md | grep -ci 'operational.surface path\|adopter.*path\|path.*adopter'` returns `>=1` (path = operational-surface path stated).
   - Class: spec §3.1/§3.4 schema reconciliation + migration note; C1 awk-§ class sweep extended to claim 4.

5. **§7.2 contract: manifest-declared-vs-template-of-record; honest proof obligation; no mandatory operational-surface read (anti-regression load-bearing).** Verifiable at pre-commit:
   - bash: `sed -n '/^### .*7\.2\. /,/^### .*7\.3\. /p' github-reference.md | grep -ci 'from the manifest'` returns `>=1`.
   - bash: `sed -n '/^### .*7\.2\. /,/^### .*7\.3\. /p' github-reference.md | grep -ci 'template-of-record'` returns `>=1`.
   - bash: `sed -n '/^### .*7\.2\. /,/^### .*7\.3\. /p' github-reference.md | grep -ci 'not.*content parity\|not.*byte\|currency.*not\|declared.*currency'` returns `>=1` (honest proof obligation sentence present).
   - bash: `sed -n '/^### .*7\.2\. /,/^### .*7\.3\. /p' github-reference.md | grep -ci 'not from the operational surface file'` returns `>=1` (the manifest-entry-only anti-regression phrasing is present; positive assertion that the correct "not from" language exists rather than a negative pattern that over-matches on the same phrase).
   - Class: spec §3.2 + §2.3 + §2.4 anti-regression; three cross-Architect passes load-bearing settlement; C1 path-(a) per Codex post-PR: awk §-char range silently fails on UTF-8 locales — replaced with sed; negative grep flipped to positive assertion on the load-bearing "not from the operational surface file" phrase.

6. **§7.3 receives receiving-subset sentence; agents field.** Verifiable at pre-commit:
   - bash: `sed -n '/^### .*7\.3\. /,/^## /p' github-reference.md | grep -c 'subset'` returns `>=1`; `| grep -c 'agents'` returns `>=1`.
   - Class: spec §3.3; C1 awk-§ class sweep extended to claim 6.

7. **surfaces-manifest-template.yml rewritten to unified schema; template version 3.0.1; F4 disambiguation comment.** Verifiable at pre-commit:
   - bash: `grep -c '^surfaces:' templates/surfaces-manifest-template.yml` returns `1`.
   - bash: `grep -c '# Template version: 3.0.1' templates/surfaces-manifest-template.yml` returns `1`; `grep -c '# Template version: 3.0.0' templates/surfaces-manifest-template.yml` returns `0`.
   - bash: `grep -ci 'independent of' templates/surfaces-manifest-template.yml` returns `>=1` (F4 disambiguation comment).
   - Class: spec §3.5 template rewrite + template_version bump (material content change per §17.5).

8. **ADR-008 Decision 6 inserted (release-track bump posture).** Verifiable at pre-commit:
   - bash: `grep -ci 'Decision 6\|release-track bump posture' docs/adr/ADR-008-v3-scope-amendment.md` returns `>=2` (heading + body).
   - bash: `grep -c 'intra-release-track' docs/adr/ADR-008-v3-scope-amendment.md` returns `>=1`.
   - Class: spec §4.1; Gate-A versioning-model ratification item.

9. **core.md §18.4 pointer-note present; defers to ADR-008 D6.** Verifiable at pre-commit:
   - bash: `awk '/^### .18\.4\./,/^## .23\./' core.md | grep -ci 'release-track bump posture'` returns `>=1`.
   - bash: `awk '/^### .18\.4\./,/^## .23\./' core.md | grep -ci 'ADR-008'` returns `>=1` (pointer-note defers to ADR-008, does not standalone restate "regardless of content class").
   - Class: spec §4.2 pointer-note (demoted from standalone rule to ADR-008 deferral).

10. **core.md §18.3 M-A7: 37 instances; PR-NN literal; span v3.0.1.** Verifiable at pre-commit:
    - bash: `grep -nE '\+ PR-89 \+ PR-NN = 37' core.md` returns 1 line (enumeration tail).
    - bash: `grep -c 'as of v3.0.1 canonicalization at PR-NN / TASK-0050' core.md` returns `1` (preamble).
    - bash: `grep -c '37 consecutive substantive cycles' core.md` returns `1`.
    - bash: `grep -c 'PR-92' core.md` returns `0` (no phantom numeric PR literal in canonical surface — PR-NN per FX-B).
    - Class: spec §5.2 M-A7 INCLUDE; Gate-A ratification item.

11. **README Action-row description corrected to honest-proof framing.** Verifiable at pre-commit:
    - bash: `grep -ci 'matches surface frontmatter' README.md` returns `0` (abandoned wording gone).
    - bash: `grep -ci 'template-of-record' README.md` returns `>=1` (new description present).
    - bash: `git diff --cached README.md | grep -E '^\+.*\[v3\.1-planned\].*\|$'` returns no added/removed stub rows (only the description text changed).
    - Class: spec §3.7 honest-proof description correction; pass-3 F1.

12. **Cumulative-diff-stats (e.1) — by pointer, not pinned.** Verifiable at pre-commit:
    - bash: `git diff --cached --shortstat` and `git diff --cached --numstat` (re-derive live). Expected shape: 8 canonical edits carry `110 insertions(+), 59 deletions(-)` before cycle artifacts; cycle artifacts (this file + handoff) are net-additive. No pinned self-volatile total per §23.6.5.
    - Class: §23.6.1.1 (e.1); §23.6.5 reference-volatile-by-pointer.

13. **Anti-scope holds — no Action materialized; no prompt edits.** Verifiable at pre-commit:
    - bash: `git diff --cached --name-only | grep -E '^actions/'` returns **no lines** (surface-version-sync-check.yml stub unchanged).
    - bash: `git diff --cached --name-only | grep -E '^prompts/'` returns **no lines** (no prompt edited; deep-research-design-brief.md map-form schema deferred per R3).
    - bash: `git diff --cached --name-only | grep -E '^\.github/workflows/'` returns **no lines**.
    - Class: spec §1 anti-scope (hard); §1 "no Action materialization".

14. **Frontmatter shape conformance + linked_pr canonical regex match.** Verifiable at pre-commit:
    - bash: `head -14 docs/handoffs/TASK-0050-v3.1-action-layer-enablement.md | grep -cE '^(task_id|title|pr|branch|linked_predecessor|linked_successor|linked_pr|framework_version_dogfooded|production_target|spec_source|date_authored|status):'` returns `12` (PMN-007 HEAD canonical 12-field).
    - bash: `head -3 docs/reviews/PR-92-codex-pre-commit.md | grep -cE '^status:'` returns `1` (review-context 1-field).
    - bash: `grep -cE '^linked_pr: PR-[0-9]+ \(Builder fills with squash SHA post-merge per PMN-001 \(k\)\)$' docs/handoffs/TASK-0050-v3.1-action-layer-enablement.md` returns `1` (numeric token satisfied for linked-pr-fix-up Action regex; `pr` field carries `PR-92` confirmed at PR-open; `linked_pr` carries `PR-92` from authoring per FX-B).
    - Class: PMN-007 HEAD canonical 12-field; MC-C linked_pr regex; review-template 1-field.

## Reviewer focus

- Re-run §6 battery (spec §6 claims 1-10): confirm (a) `templates:` map-form absent from §7.1, `surfaces:` list present; (b) §7.2 contract is manifest-declared-vs-template-of-record, no mandatory operational-surface read, honest-proof sentence present; (c) ADR-008 D6 + §18.4 pointer-note staged self-consistently (pointer defers to ADR-008, not standalone); (d) M-A7 `= 37` / "37 consecutive" / `PR-NN` / v3.0.1 preamble; (e) canonical-law trio frontmatter all 3.0.1.
- Confirm "published" does NOT attach to v3.0.1 in any canonical surface (attachment predicate claim 2; FX2 class sweep).
- Confirm §7.2 anti-regression (load-bearing settlement): no instruction to read `template_version` from the operational surface file.
- Confirm README L9 two-concept form: v3.0.1 labeled in-development, v3.0.0 labeled published adopter-facing (not conflated per the v2.42 defect class).
- Confirm ADR-008 D6 text matches spec §4.1 prescription; `core.md` §18.4 pointer-note matches spec §4.2 prescription.
- Cumulative-diff-stats by pointer (no pinned self-volatile total); frontmatter shape + linked_pr regex match.
- Anti-scope: no Action materialized; no prompt edits; no stub filled; no roadmap_status flips.
- Recursive-self-instantiation salience: HIGH — verify the cycle does not introduce a circular dependency (it canonicalizes D6 AND applies D6 to itself; both are explicitly ratified and consistent).

## Codex desktop pre-commit kickoff

```
Please review the pending changes on the current branch (feat/task-0050-v3.1-action-layer-enablement) per the review-context at docs/reviews/PR-92-codex-pre-commit.md. Working tree is at staged-tree state (git add -A applied); review the staged diff.

Cycle scope: TASK-0050 — v3.1 action-layer enablement. Two deliverable classes: (a) schema reconciliation — github-reference.md §7.1/§7.2/§7.3 and templates/surfaces-manifest-template.yml rewritten to the unified surfaces: list-form manifest (old templates: map-form removed; path is the adopter operational-surface path; template_version from manifest entry, not operational surface; honest proof obligation: currency not content parity; optional .yml-marker cross-check); (b) release-track bump posture — ADR-008 Decision 6 amendment + core.md §18.4 pointer-note (intra-release-track cycles bump patch; aggregate minor/major fires once at release completion). Currency: v3.0.0->v3.0.1 across canonical-law trio frontmatter + AGENTS.md + CLAUDE.md + README + surfaces-manifest template. M-A7 §18.3 36->37 (PR-NN literal). README Action-row description corrected. No Action materialized; surface-version-sync-check.yml stays stub.

Please run the named verification battery in "Builder claims to verify" (claims 1-14). Special focus: (1) §7.2 anti-regression — confirm no instruction to read template_version from the operational surface file; (2) "published" attachment predicate — confirm v3.0.1 carries no "published" clause anywhere; (3) linked_pr canonical regex match.

Per ADR-001 D11 owner-invokes convention: surface findings per severity (Blocking -> handback; Major -> path-(a)/(b); Minor -> default path-(b)). Substantive verdict via formal review preferred; issue-comment summary acceptable.

Verbatim-output convention: capture the review verbatim into the review-context's "Codex desktop pre-commit output absorption" section.
```

## Codex desktop pre-commit output absorption

### Codex pass 1 (UTC 2026-06-06)

**Verdict**: Request changes — 1 Blocking; claims 1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14 PASS; claim 2 FAIL (Blocking).

**Findings** (verbatim):

> **[F1] BLOCKING — AGENTS.md:9 and CLAUDE.md:9 carry stale "published from this repository" framing on v3.0.1.**
>
> The initial currency flip changed `AMAS v3.0.0 (published from this repository; ...)` -> `AMAS v3.0.1 (published from this repository; ...)`. The version number is correct (v3.0.1) but the prose framing is wrong: "published from this repository" is a release-event qualifier that applies to v3.0.0, not to the in-development v3.0.1. The README L9 two-concept form (authored correctly per R1: v3.0.1 = in development; v3.0.0 = published adopter-facing) was NOT mirrored to AGENTS.md:9 and CLAUDE.md:9. These two lines create a conflation of the canonical/in-development version with the published release — the same v2.42 defect class the two-concept form was designed to prevent.
>
> This is a defect class, not a two-line instance patch. The actual fix is: (1) FX1 — rewrite both lines to mirror the README L9 two-concept framing; (2) FX2 — class sweep via attachment predicates across all canonical surfaces to confirm "published" never attaches to v3.0.1 anywhere (the sweep IS the fix; the instance patches are consequences of it).
>
> Recommendation: **request changes**. FX1+FX2 before commit.

**Adjudication** (per ADR-001 D11 + `core.md` §8.1.1.3):

- **[F1] (Blocking — published-framing defect class)**: routed **path-(a) revise**. Correct finding. The "published from this repository" framing was stale from the v3.0.0 state; the currency flip preserved the stale prose while updating the version number. FX1+FX2 applied per Architect relay instruction.

**Resolution applied** (path-(a) FX1+FX2):

- **FX1**: AGENTS.md:9 `- **Active framework version**: AMAS v3.0.1 (published from this repository; ...)` -> `- **Active framework version**: AMAS v3.0.1 (active, in development in this repository); latest published release v3.0.0 — see the README version-positioning note`. CLAUDE.md:9 identical flip.
- **FX2 (class sweep)**: `git grep -nE 'publish' AGENTS.md CLAUDE.md README.md core.md github-reference.md usage-guide.md` returns v3.0.0 entries only (the "published from this repository" historical sentence at AGENTS.md:11 / CLAUDE.md:11 + "AMAS v3.0.0 is published from this repository" at README.md:7 — all correctly attach to v3.0.0, not v3.0.1). Attachment predicates `v3\.0\.1[^.;]*publish` and `publish[^.;]*v3\.0\.1` both return empty. Class sweep closes clean.
- Re-stage: shortstat unchanged for the canonical-edit subset (the FX1 fix is an in-place line rewrite on two lines; net 0 for AGENTS.md + CLAUDE.md since length is approximately equivalent). Re-derive (e.1) at final staged tree.

---

### Codex pass 2 — focused re-review (UTC 2026-06-06)

**Per `core.md` §8.1.1.3 bounded-continuation**: Pass 2 is a focused re-review scoped to [F1]-resolved + no-net-new. Not a full battery re-run.

**Verdict**: PASS — no remaining findings.

**Evidence** (verbatim):

> [F1] resolved: AGENTS.md:9 reads "active, in development in this repository"; CLAUDE.md:9 reads identically. "published" does not attach to v3.0.1 in any canonical surface.
> Attachment-predicate sweep: `v3\.0\.1[^.;]*publish` -> no matches; `publish[^.;]*v3\.0\.1` -> no matches.
> Shortstat: unchanged from pre-FX1 canonical-edit subset (8 files, net consistent).
> Quoted fixed lines confirmed as prescribed by FX1.
> Net-new findings: none.
> Verdict: clean.

**Adjudication** (per ADR-001 D11):

- No Blocking, Major, or Minor findings. Staged tree passes the focused re-review. Path to commit/push is clear subject to Gate-A FINAL clear (received).
- [F1] resolved? yes. Net-new? no. Verdict: clean.
- Lesson logged (per §10 Battery discipline): claim 2 predicate must check prose framing *attachment* around the version number, not the version number alone. "v3.0.1 present" ≠ "v3.0.1 framed correctly"; the extended attachment predicate is the load-bearing check.

---

## Codex post-PR review (2026-06-07)

Three-endpoint poll per `core.md` §8.1.1.1 (Builder, 2026-06-07T01:27Z UTC):
- `pulls/92/reviews` → 1 review (`COMMENTED`, `chatgpt-codex-connector[bot]`, commit `b223c11c7b`, timestamp `2026-06-07T01:27:18Z`)
- `issues/92/comments` → 1 comment (owner `@codex review` trigger at `2026-06-07T01:24:31Z`)
- `pulls/92/comments` → 2 line-level comments (both from `chatgpt-codex-connector[bot]`, part of the review above)

**Verdict**: COMMENTED — 1 Major (P2) + 1 Minor (P3); no Blocking.

**Findings** (verbatim):

> **[C1] P2 — Fix the anti-regression verification command** (line comment on `docs/reviews/PR-92-codex-pre-commit.md` line 48):
>
> When this battery is run against the changed `github-reference.md`, this exact grep returns `1`, not `0`, because §7.2 intentionally contains the phrase "not from the operational surface file." Since this review context is the durable verification checklist for the cycle, the advertised expected result makes the load-bearing anti-regression check unreproducible and can cause reviewers to treat the settled contract as failing; narrow the pattern to mandatory-read wording or update the expected count.

> **[C2] P3 — Correct the AGENTS manifest agent list** (line comment on `github-reference.md` §7.1 worked example):
>
> The schema defines `agents` as the slugs that read that receiving surface, but this canonical example lists `claude` on `AGENTS.md` even though the AGENTS template targets Codex and the next entry already maps Claude to `CLAUDE.md`. Adopters copying this example would record Claude as reading both surfaces, which defeats the receiving-surface identity inventory this schema is meant to provide; keep the AGENTS entry to Codex-family agents only.

**Phantom-action audit** (per `core.md` §8.1.1.2): no commits or branches claimed by Codex; findings are textual observations only. No phantom actions.

**Adjudication** (per ADR-001 D11 + `core.md` §8.1.1.3):

- **[C1] (P2/Major — broken anti-regression check command)**: routed **path-(a) revise**. Correct in principle. Diagnosis: the `awk '/^### .7\.2\./,/^### .7\.3\./'` range pattern silently fails on this platform because `awk` does not match the UTF-8 `§` character in the section header (the range captures nothing; grep sees empty input and returns `0` vacuously — a broken check, not a passing one). The `sed -n '/^### .*7\.2\. /,/^### .*7\.3\. /p'` form works correctly. Additionally the negative pattern `'from the operational surface'` over-matches on the correct "not from the operational surface file" language. Fix: replace all four `awk` range extractions in claim 5 with `sed -n`; flip the last bash line to a positive assertion confirming the "not from the operational surface file" anti-regression phrase IS present (returns `>=1`). All four fixed commands verified correct (5a `>=1`, 5b `>=1`, 5c `>=1`, 5d `>=1`).
- **[C2] (P3/Minor — AGENTS.md agents list in worked example)**: routed **path-(b) record-and-proceed**. The `agents: [claude, codex]` value on AGENTS.md in the §7.1 worked example is spec-prescribed (spec §2.2; Gate-A-cleared by Architect across three cross-Architect passes). Changing it requires a design judgment call: whether AGENTS.md in this framework is exclusively the Codex receiving surface (making `[codex]` the correct value) or is legitimately read by multiple agents including Claude (making `[claude, codex]` valid). Per §8.1.1.3 Minor → default path-(b): record and proceed. Carry to TASK-0051 / Architect design review as an intentional open item.

**Resolution applied** (path-(a) C1):

- Edit C1.1: `docs/reviews/PR-92-codex-pre-commit.md` claim 5 — all four `awk '/^### .7\.2\./,/^### .7\.3\./'` replaced with `sed -n '/^### .*7\.2\. /,/^### .*7\.3\. /p'`; last bash line flipped from negative `returns 0` to positive assertion `returns >=1` (confirming the "not from the operational surface file" phrase IS present). Verified: all four commands return `>=1` as expected.
- Edit C1.2 (awk-§ class sweep extended to claims 4 and 6): `awk '/^### .7\.1\./,/^### .7\.2\./'` in claim 4 (all four bash lines) replaced with `sed -n '/^### .*7\.1\. /,/^### .*7\.2\. /p'`; `awk '/^### .7\.3\./,/^## .8\./'` in claim 6 replaced with `sed -n '/^### .*7\.3\. /,/^## /p'`. Re-verified all content values with reliable primitives: 4a=0 (map-form gone), 4b=3 (surfaces: present), 4c=7/8 (template_version/agents present), 4d=1 (path stated), 6a=1 (subset present), 6b=1 (agents present). Content sound; no masked defect found.
- No canonical-law edits; no staged-tree mutations beyond the review-context file itself.
- Shortstat for this fix: review-context only (+N/-N lines in-place edit).

**Gate B status**: [C1] resolved path-(a); [C2] recorded path-(b). No Blocking; no unresolved Major. Path to owner squash-merge is clear.
