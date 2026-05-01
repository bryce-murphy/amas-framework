# HANDOFF: TASK-0002 — AMAS v3 framework package scaffold

## Metadata

- Task ID: TASK-0002
- Linked Issue: n/a (Feature-Brief-tracked; FEAT-0001 is the spec)
- Linked PR: <set after gh pr create — fill in step 16 fix-up commit>
- Linked ADR(s): ADR-001 (decisions 7-8 cover this PR's scope; no new ADR for PR-2)
- Linked Feature Brief: FEAT-0001 (`docs/features/FEAT-0001-v3-package-scaffold.md`)
- Linked review-context file: `docs/reviews/PR-2-codex-pre-commit.md`
- Owner role: Architect (Claude.ai) → Builder (Claude Code)
- Previous role: Architect produced this handoff
- Timestamp (UTC): 2026-05-01T13:43:45Z
- Last synced commit SHA: c1ec54f0015415329143a989e392b09005877f12
- Branch: feat/task-0002-v3-package-scaffold
- Status: active
- Direction: Architect → Builder (universal handoff schema, AMAS v2.14.1 §14.1)
- Framework version: AMAS v2.14.1 (dogfooded)

## Objective

Author the v3 framework package scaffold per FEAT-0001, ADR-001 decisions 7-8, and AMAS v3 transition plan v0.2 §3. 50 stub files across 5 stub classes (canonical-framework, template-markdown, YAML-comment template, adapter-pack, action-yaml) plus 2 archive prompts plus 1 root README modification. PR-2 authors stubs only; substantive framework content lands in PR-3 onward.

## Last completed step

Architect produced this handoff, FEAT-0001 Feature Brief, the v2 Builder prompt, and the review-context file template. Owner merged PR-1 (TASK-0001 repo bootstrap) at SHA c1ec54f, enabled branch protection on `main` per ADR-001 decision 9 (PRs required, 1 approval, code-owner review, conversation resolution, squash-only merge, admin bypass scoped to PR-merge action only), and confirmed the documentation-MCP mechanism for this project (web-search + owner verification).

## Current state

- Summary: `main` is at c1ec54f with 10 tracked files from PR-0. Local clone clean. `.claude/` may exist locally and is gitignored.
- Files changed: none yet.

## Decisions made

- PR-2 scope = stubs only (per ADR-001 decision 8 and FEAT-0001 in-scope/out-of-scope)
- 6-class organization: A canonical-framework (3), B template-markdown (30), B' YAML-comment template (1), C adapter-pack (7), D action-yaml (9), E archive-prompt (2), F README-modification (1)
- Codex desktop pre-commit review at step 11 (pre-stage, untracked working tree) per AMAS v3 framework discipline
- Codex post-PR review (`@codex review`) invoked by owner after PR opens per ADR-001 decision 11
- No new ADR for PR-2 (ADR-001 covers; ADR-002 reserved for PR-3 substantive v3 architectural decision)
- Single Feature Brief (FEAT-0001) authored alongside this PR

## Assumptions

- TASK-0002 is the next available TASK number (verified in step 1 pre-flight)
- FEAT-0001 is the next available Feature Brief ID (verified in step 1 pre-flight)
- Base SHA `c1ec54f0015415329143a989e392b09005877f12` is current `main` (verified in step 1)
- Branch protection on `main` is live and configured per ADR-001 decision 9
- `gh` CLI authenticated with `repo` scope minimum
- Project knowledge contains readable copies of `deep-research-report.md` and `amas-v3-research-deliverable.md` for archive authoring
- Codex desktop is available to the owner for step 11 pre-commit review

## Risks

- **Count drift across §3, FEAT-0001, review-context, PR body, TASK-0002 handoff**: 5 surfaces all assert 65/56/55/1/9 (revised from prompt's 66/57/56/1/9 after step-10 reconciliation; see Validation run). Mitigation: §24 cross-surface sweep in Codex desktop review at step 11 + post-PR `@codex review`.
- **Frontmatter typos in 50 stubs**: scale risk. Mitigation: §4 class templates precise; spot-checks at step 10; Codex desktop verification at step 11.
- **Archive corruption during copy-from-project-knowledge**: byte-level encoding check at step 10; Codex desktop integrity check at step 11.
- **Substantive content authored in stubs**: §9 do-not list explicit; FEAT-0001 acceptance criterion #5; Codex desktop scope-check at step 11.
- **`.claude/` leak into staged commit**: §12 step verification; stop condition.
- **Linked-PR fix-up commit unexpectedly changes more than Linked PR line**: stop condition on `git diff --stat HEAD~1` showing >1 file.
- **Codex desktop sandbox limitations**: `.git/index.lock` write may fail in `workspace-write` mode; review uses read-only git inspection. Mitigation: review prompt explicitly uses read-only commands.

## Blocking questions

None at handoff time. If any surface during execution, stop and surface to owner.

## Validation run

- **Commands**:
  - `git fetch origin && git checkout main && git pull --ff-only origin main && git rev-parse HEAD` (pre-flight)
  - `gh auth status` and `gh repo view bryce-murphy/amas-framework --json …` (pre-flight)
  - `Test-Path` checks against all target paths and against next-available TASK-0002 / FEAT-0001 (pre-flight)
  - `git checkout -b feat/task-0002-v3-package-scaffold`
  - File authoring via the Write/Edit tools and `[System.IO.File]::WriteAllText` with UTF-8 (no BOM)
  - `git ls-tree -r --name-only origin/main` (PR-0 enumeration)
  - `git add --intent-to-add . ; git status --porcelain ; git diff --stat HEAD` (count + diff verification)
  - Per-file frontmatter spot-checks via `Get-Content … -TotalCount`
  - Byte-level em-dash check via `[System.IO.File]::ReadAllBytes` scanning for `E2 80 94`
  - Byte-level `§` check via scanning for `C2 A7`

- **Results**:
  - §8.2 pre-flight: PASS on all preconditions (base SHA `c1ec54f0015415329143a989e392b09005877f12`; clean working tree except local `.claude/`; all target paths absent; TASK-0002 and FEAT-0001 next-available; branch regex matches §6.1; `gh` auth with `repo`+`workflow` scopes; repo public/MIT/main).
  - **File counts revised at step 10**: prompt §3 claimed 66/57/56/1/9 but actual tree state is **65 / 56 / 55 / 1 / 9** (tracked / changed / new / modified / unchanged). The prompt's enumeration in §3 lists 50 stubs + 2 archives + 3 PR-meta files = 55 new (the README is the 1 modified, not a 56th new file). FEAT-0001 acceptance criterion #1 and the review-context file have been corrected to match actual values; surfaced to owner at step 10 and option (a) — correct count claims to actual — selected.
  - All 50 stubs present and matching their §4 class templates. All 2 archives present with provenance comment as line 1 and source content verbatim from line 3.
  - README modification: `git diff README.md` shows 93 insertions, 0 deletions; H2 section order is Status → What is AMAS? → Reading order → Roadmap → Package layout → License → Contributing.
  - UTF-8 encoding: all authored files written without BOM; `§` round-trips as `C2 A7`; archive `prompts/research-deliverable.md` retains 137 em-dash sequences (`E2 80 94`).

- **Evidence**:
  - `git status --porcelain` after `--intent-to-add`: 1 ` M README.md` + 55 ` A` entries = 56 changed.
  - `git diff --stat HEAD` (last line): `56 files changed, 1822 insertions(+)`.
  - PR-0 baseline: 10 files (`.github/CODEOWNERS`, `.github/PULL_REQUEST_TEMPLATE.md`, `.gitignore`, `AGENTS.md`, `CLAUDE.md`, `LICENSE`, `README.md`, `docs/adr/ADR-001-initial-repo-setup.md`, `docs/handoffs/TASK-0001-repo-bootstrap.md`, `docs/post-merge-notes/.gitkeep`).
  - Branch tip will hold 10 PR-0 + 55 new = 65 tracked.
  - Note: git emits `LF will be replaced by CRLF` warnings for the 53 new text files due to default `core.autocrlf` on Windows. Working-tree bytes are LF; index/commit bytes will be normalized per `core.autocrlf`. Not a defect.

## Exact next step

Run the v2 Builder prompt for TASK-0002 from step 1 forward.
- Codex desktop pre-commit review at step 11 (using prompt block embedded in `docs/reviews/PR-2-codex-pre-commit.md`).
- Stop-and-show at step 13.
- Linked-PR fix-up at step 16.
- Hand back at step 16 with PR URL, file count, handoff metadata confirmation, Codex review outcome, and explicit no-`@codex review`-from-Builder note.

## Reassessment / expiry

This handoff is stale 7 days after PR opens or immediately on any v0.2 transition plan revision, ADR-001 amendment, or FEAT-0001 amendment. Re-read FEAT-0001 and ADR-001 before resuming if delayed.

## Session log archive (prior logs migrated from PR body per §13.1)

<!-- Empty at PR-2 open. Builder appends per §13.2 if PR has multiple sessions. -->
