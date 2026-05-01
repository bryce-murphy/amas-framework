# HANDOFF: TASK-0001 — amas-framework repo bootstrap

## Metadata
- Task ID: TASK-0001
- Linked Issue: n/a (bootstrap task; tracked via this handoff and the PR)
- Linked PR: https://github.com/bryce-murphy/amas-framework/pull/1
- Linked ADR(s): ADR-001 (authored in this PR)
- Linked Feature Brief: n/a (bootstrap task per lite judgment; ADR-001 is the spec)
- Owner role: Architect (Claude.ai) → Builder (Claude Code)
- Previous role: Architect produced this handoff
- Timestamp (UTC): 2026-04-30T23:08:46Z
- Last synced commit SHA: eaee2a3af38c298e06cc03c7c1b7b5e0cfe66215
- Branch: chore/task-0001-repo-bootstrap
- Status: active
- Direction: Architect → Builder (universal handoff schema, AMAS v2.14.1 §14.1)
- Framework version: AMAS v2.14.1

## Objective

Bootstrap the `amas-framework` repository with operational scaffolding (LICENSE already present, README replaced, AGENTS.md, CLAUDE.md, PR template, CODEOWNERS, `.gitignore`, ADR-001 recording the standalone-repo decisions) before substantive v3 content lands in PR-2. Dogfooded: the repo follows AMAS v2.14.1 from day one.

## Last completed step

Architect produced this handoff and the corresponding Builder prompt. Owner created the GitHub repo with placeholder README and MIT license, configured topics (`ai-agents`, `multi-agent`, `ai-coding-assistant`, `governance`, `framework`, `claude`, `codex`, `mcp`, `llm-agents`), set Actions workflow permissions to read-only, confirmed `gh` CLI authenticated, confirmed local clone at `C:\Users\BryceMurphy\repos\amas-framework`, and confirmed UPCDS canonical URL at `https://github.com/recruiting-tech/upcds/blob/main/docs/ai-operating-system.md`.

## Current state

- Summary: repo exists on GitHub with two commits on main (Initial commit; Create README.md). Local clone is clean. Working tree has only `.git/`, `LICENSE` (MIT), and placeholder `README.md` (and possibly `.claude/` harness directory which is gitignored as part of this PR).
- Files changed: none yet.

## Decisions made

Recorded in ADR-001 (authored in this PR). 15 decisions, summary:

1. Standalone repo `amas-framework` (vs. UPCDS staging)
2. Repo name durable across major versions
3. MIT license
4. Public visibility
5. Default branch `main`
6. Dogfooded from day one
7. v3 content lands at repo root
8. PR sequence renumbered: TASK-0001 (this) through TASK-0008
9. Branch protection deferred until after PR-0 merges
10. Reviewer is Codex; substantive-only mode
11. Codex invocation: owner-handled (Builder does not invoke)
12. No v2.14.2 patch
13. Topics list
14. `GITHUB_TOKEN` workflow permissions read-only
15. `.gitignore` covers Claude Code harness state, OS noise, editor noise, local-env files

## Assumptions

- TASK-0001 is the next available TASK number (verified in step 1 pre-flight; new repo so this should be uncontested)
- Existing LICENSE is MIT (verified in step 1 pre-flight)
- UPCDS canonical URL is `https://github.com/recruiting-tech/upcds/blob/main/docs/ai-operating-system.md` (owner-confirmed)
- `gh` CLI is authenticated; auth has at least `repo` scope; `workflow` scope can be added before PR-7 — not required for PR-0
- Solo-contributor branch protection enables AFTER PR-0 merges
- This handoff plus ADR-001 plus the Builder prompt are the complete spec; no Feature Brief required for PR-0
- `.claude/` harness directory may exist locally; `.gitignore` (authored at step 11.5) handles exclusion

## Risks

- **LICENSE format mismatch** (low; mitigated by step 1 check): if `LICENSE` is not the standard MIT text GitHub generates, surface and wait for owner direction before proceeding.
- **Existing files in working tree beyond LICENSE+README+`.claude/`** (low; mitigated by step 1 `Get-ChildItem -Force` check): surface and wait.
- **Concurrent work in another session that creates TASK-0001 first** (very low for a fresh repo, but possible): step 1 pre-flight catches this.
- **PR creation auth failure** (low; mitigated by step 1 `gh auth status` and `gh repo view` checks): if `gh pr create` fails despite passing pre-flight, surface and do not retry blindly.
- **Linked-PR fix-up commit producing unexpected diff** (very low): the fix-up commit should change exactly one line in `docs/handoffs/TASK-0001-repo-bootstrap.md`. If `git diff --stat HEAD~1` after the fix-up shows anything else, surface.
- **Future Claude Code sessions creating new harness files outside `.claude/`** that aren't covered by the current `.gitignore` (low; mitigated by recurring §8.2 pre-flight which surfaces untracked files): if a future session surfaces a new ignored-class artifact, treat it as a §18-class learning event candidate and surface to Architect.

## Blocking questions

None at handoff time. If any surface during execution, stop and surface to owner.

## Validation run

- **Commands**:
  - `git fetch origin && git checkout main && git pull --ff-only origin main` — base sync
  - `git rev-parse HEAD` — captured base SHA `eaee2a3af38c298e06cc03c7c1b7b5e0cfe66215`
  - `git status` — clean tree confirmation (only `.claude/` untracked, acceptable per prompt)
  - `Get-ChildItem -Force` — initial tree confirmed contents `.git/`, `.claude/`, `LICENSE`, `README.md`
  - `Test-Path` checks for `docs/handoffs/TASK-0001-*`, `AGENTS.md`, `CLAUDE.md`, `docs/adr`, `.github/CODEOWNERS`, `.gitignore` — all returned False
  - `Get-Content LICENSE -TotalCount 5` — confirmed line 1 "MIT License", line 3 "Copyright (c) 2026 Bryce Murphy"
  - `gh auth status` — authenticated as `bryce-murphy`; scopes `gist`, `read:org`, `repo`, `workflow`
  - `gh repo view bryce-murphy/amas-framework --json name,visibility,defaultBranchRef,licenseInfo` — confirmed `visibility:PUBLIC`, `licenseInfo.key:mit`, `defaultBranchRef.name:main`
  - Branch name regex match against §6.1 regex `^(feat|fix|chore|docs|adr|refactor|test|ci)/task-\d{4}-[a-z0-9-]+$` — `chore/task-0001-repo-bootstrap` matches
  - `git checkout -b chore/task-0001-repo-bootstrap` — branch created
  - File-creation operations for the 8 new files plus README replacement
  - `mkdir -p docs/post-merge-notes && touch docs/post-merge-notes/.gitkeep` — created 0-byte placeholder
  - `git check-ignore .claude/settings.local.json` — confirmed exit 0; harness path is gitignored
  - `git status` post-`.gitignore` — `.claude/` no longer in untracked list
  - `Get-ChildItem -Recurse -File -Force | Where-Object { ... }` — tree enumeration matched expected 10-file list
  - `git add --intent-to-add . && git diff --stat HEAD` — diff stat
  - UTF-8 byte verification (search for byte sequence `E2 80 94`) for AGENTS.md, CLAUDE.md, ADR-001, handoff

- **Results**:
  - Pre-flight: all 16 preconditions PASS (base sync, working tree, expected-absent paths, LICENSE format, gh auth + scope, repo metadata, branch regex)
  - Tree state: 10 tracked files; 9 changed in this PR (8 new + 1 modified); 1 unchanged (LICENSE); `.claude/` gitignored locally
  - Diff stat:
    ```
     .github/CODEOWNERS                        |  2 +
     .github/PULL_REQUEST_TEMPLATE.md          | 37 ++++++++++++
     .gitignore                                | 23 ++++++++
     AGENTS.md                                 | 62 ++++++++++++++++++++
     CLAUDE.md                                 | 51 +++++++++++++++++
     README.md                                 | 39 ++++++++++++-
     docs/adr/ADR-001-initial-repo-setup.md    | 68 ++++++++++++++++++++++
     docs/handoffs/TASK-0001-repo-bootstrap.md | 94 +++++++++++++++++++++++++++++++
     docs/post-merge-notes/.gitkeep            |  0
     9 files changed, 375 insertions(+), 1 deletion(-)
    ```
    (Validation-run row counts will increment after this fill-out edit; the diff stat above reflects post-step-12 state. Pre-commit recount happens at step 15 staging.)
  - Spot-checks: each authored file's first lines match expected content; PR template begins with `## Linked records`; CODEOWNERS contains exactly two lines; `.gitignore` contains all expected sections (Claude Code, Windows, macOS, Editors/IDEs, Local environment)
  - Encoding: UTF-8 confirmed (em-dash bytes `E2 80 94` present in AGENTS.md, CLAUDE.md, ADR-001, handoff; absent in README.md as expected — README content uses no em-dashes); `.gitkeep` is exactly 0 bytes
  - Line endings: git reported LF→CRLF normalization warnings on Windows for all text files at `git add --intent-to-add` time; this is standard `core.autocrlf` behavior and not an authoring defect

- **Evidence**:
  - Pre-flight pass/fail table reproduced in Builder turn at step 1; all rows PASS
  - `git diff --stat HEAD` output reproduced above verbatim
  - File enumeration matches the explicit 10-file list in step 12 exactly
  - `git check-ignore .claude/settings.local.json` returned exit 0 with the path echoed
  - `git status` post-step-11.5 omitted `.claude/` from the untracked listing
  - UTF-8 byte verification: `[System.IO.File]::ReadAllBytes(...)` scan reported `E2 80 94` present in 4 of 5 markdown files containing em-dashes; sizes — AGENTS.md 4098B, CLAUDE.md 3242B, ADR-001 8240B, handoff 5767B (pre-fill-out), README.md 2467B

## Exact next step

Run the Builder prompt for TASK-0001 from step 1 forward.
- Stop-and-show at step 14 (no URL question — URL is filled in advance; no `.gitignore` question — `.gitignore` is in-prompt as step 11.5).
- Fill Timestamp at step 15 just before commit.
- Fix-up commit at step 18 to fill Linked PR with actual URL.
- Hand back at step 19 with PR URL, head SHA, file count, handoff metadata confirmation.

## Reassessment / expiry

This handoff is stale 7 days after PR opens or immediately on any v0.2 transition plan revision or any change to ADR-001. Re-read the kickoff handoff and ADR-001 before resuming if delayed beyond that window.

## Session log archive (prior logs migrated from PR body per §13.1)

<!-- Empty at bootstrap. Builder appends per §13.2 if PR has multiple sessions. -->
