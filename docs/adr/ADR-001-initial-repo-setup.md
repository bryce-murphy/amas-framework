# ADR-001: Initial repo setup for amas-framework

## Status

Accepted — 2026-04-30; decision 8 PR sequence portion superseded by ADR-003 (2026-05-01)

## Context

The AMAS framework has matured to v2.14.1, materialized in the UPCDS reference project as `docs/ai-operating-system.md` plus three companion files. The framework was authored, evolved, and consumed all within UPCDS, with no separate package boundary. AMAS v3 is being designed as a split-package release per the v3 transition plan v0.2 §3: four layers comprising canonical core, GitHub reference implementation, usage guide, and templates plus Actions plus appendices.

The original v3 transition plan v0.2 PR sequence proposed authoring v3 content as a staging directory inside UPCDS (`amas-v3/`), with PR-9 graduating select content to UPCDS canonical paths. During production kickoff, the project owner identified that this structure conflates framework authoring with framework adoption, and that AMAS — being agnostic to any one repo — should live in its own dedicated repository.

## Decision

Create `amas-framework` as a standalone GitHub repository owned by `bryce-murphy`, public, MIT-licensed, with the following operational decisions:

1. **Standalone repo, not staging-in-UPCDS**. AMAS v3 is authored and released from `amas-framework`. UPCDS becomes one adopter of AMAS, not the implicit owner.
2. **Repo name `amas-framework`** — durable across major versions (avoiding `amas-v3` which would be obsolete at v4).
3. **MIT license** for permissive reuse and adoption.
4. **Public visibility** for adoptability, reusable Actions distribution, and the "AMAS vs other frameworks" appendix per Decision D of the transition plan.
5. **Default branch `main`**.
6. **Dogfooding from day one**. `amas-framework` operates under AMAS v2.14.1 itself: root `AGENTS.md`, root `CLAUDE.md`, `.github/PULL_REQUEST_TEMPLATE.md`, `.github/CODEOWNERS`, ADR discipline, handoff discipline, PMN discipline. The framework eats its own food.
7. **Drop the `amas-v3/` containing directory** for v3 content. In a standalone repo, v3 content lives at the repo root (`core.md`, `github-reference.md`, `usage-guide.md`, etc.). Version is carried in YAML frontmatter and git tags.
8. **PR sequence revised** for the standalone repo:
   - **PR-0** (this PR, TASK-0001): repo bootstrap
   - **PR-2** (TASK-0002): v3 framework package scaffold
   - **PR-3** (TASK-0003): v3 core authored; ADR-002 records v3 architectural decision (formerly "ADR-015" in the transition plan v0.2)
   - **PR-4** through **PR-8** (TASK-0004 through TASK-0008): v3 content per transition plan v0.2 §10
   - **PR-9** (in UPCDS, separate sequence): UPCDS adopts amas-framework v3.0.0; UPCDS ADR-015 records the adoption referencing amas-framework's ADR-002 as upstream rationale
9. **Branch protection deferred** until PR-0 merges. Enables immediately after PR-0 with: require PR + ≥1 approval, admin bypass enabled (§10.5 solo-contributor), dismiss stale reviews on push, no force-push, no branch deletion.
10. **Reviewer**: Codex (GPT-5.5) cross-ecosystem from Builder (Claude Code) per AMAS v2.14.1 §2.3.1. Substantive-only mode per §8.1; owner runs merges via §10.5 solo-contributor bypass.
11. **Codex invocation**: the project owner posts `@codex review` after the PR opens. Builder does not invoke from its side.
12. **No v2.14.2 patch** (Decision A in transition plan v0.2): v2.14.1 is the current canonical; v3 supersedes when published.
13. **Topics on the GitHub repo**: `ai-agents`, `multi-agent`, `ai-coding-assistant`, `governance`, `framework`, `claude`, `codex`, `mcp`, `llm-agents`.
14. **`GITHUB_TOKEN` workflow permissions**: read-only by default (forward-compat target per research finding R-6 / GitHub 2026 security roadmap).
15. **`.gitignore` covers Claude Code harness state, OS noise, editor noise, and local-env files**. Surfaced during PR-0 step 12 (in an earlier prompt iteration) when Claude Code's `.claude/settings.local.json` appeared as an unanticipated working-tree file. Adding `.gitignore` once during bootstrap prevents the same scope-graft from recurring on every subsequent Builder session in this repo. Specific entries: `.claude/`, `Thumbs.db`, `ehthumbs.db`, `Desktop.ini`, `$RECYCLE.BIN/`, `.DS_Store`, `.vscode/`, `.idea/`, `*.swp`, `*.swo`, `*~`, `.env`, `.env.local`, `*.log`. Future per-language additions (e.g., Node `node_modules/`, Python `__pycache__/`) are deferred to the PR that introduces that language surface.

## Alternatives considered

**(A) Staging directory `amas-v3/` in UPCDS** (the transition plan v0.2 §3 default). Rejected because it conflates authoring with adoption and offers no clean version-pinning model for adopters who want reusable Actions or templated artifacts.

**(B) Repo name `amas-v3`**. Rejected because it would become misleading at v4; durability of the repo name is more valuable than version-explicit naming.

**(C) Apache 2.0 license** instead of MIT. Considered for explicit patent grant. Deferred to MIT for simplicity; can be revisited if patent concerns emerge.

**(D) Skip dogfooding** (treat amas-framework as a passive container of files for adoption). Rejected because dogfooding catches usability problems before adopters do, and the live repo files double as worked examples.

**(E) Bundle bootstrap into PR-2** (single PR creating both the meta files and the v3 framework scaffold). Rejected because PR-2 should be reviewable on package shape alone per the production kickoff handoff; bootstrap is a separate durable decision worth its own PR.

**(F) Defer `.gitignore` to a later PR**. Rejected because every subsequent Builder session in this repo will produce the same untracked harness state, and PR-0 is the only PR where adding a meta-file is mechanical-shape work; later PRs have substantive content that should be the review focus, not gitignore scope-graft.

## Consequences

- **PR-0** establishes the repo's operating discipline before any v3 content lands. Future PRs benefit from a real PR template, real CODEOWNERS, real AGENTS/CLAUDE files, and a `.gitignore` covering harness/OS/editor noise.
- **The v3 transition plan v0.2 §10 PR sequence** is renumbered for amas-framework: TASK ids shift from 0020+ (UPCDS-relative) to 0001+ (amas-framework-relative). v3 architectural decision ADR shifts from "ADR-015" to ADR-002.
- **UPCDS gets its own ADR-015** when it adopts v3, referencing amas-framework's ADR-002. Cross-repo ADR linkage is a new pattern but supported by the framework's universal handoff schema.
- **Solo-contributor branch protection model** continues. Codex remains the configured Reviewer in substantive-only mode.
- **v2.14.1 reference**: amas-framework operates under v2.14.1 (whose canonical lives in UPCDS) until v3 publishes from this repo. After v3 ships, amas-framework will self-adopt v3 in a separate self-adoption PR (analogous to UPCDS PR-9).
- **Adopters of v3** will reference amas-framework releases by version tag (`v3.0.0`, `v3.1.0`, etc.) and pull templates / Actions via reusable-workflow `uses:` references pinned to commit SHA or version tag per AMAS v3 transition plan §7 distribution patterns.
- **Future per-language additions to `.gitignore`** are deferred to the PR that introduces the language surface. PR-7 (CI workflows) may add JavaScript/TypeScript runtime entries if the workflows compose composite actions in those languages; PR-8 (appendices) is unlikely to require ignore additions.

## Evidence / references

- AMAS v3 production kickoff handoff (`amas-v3-production-kickoff-handoff.md`)
- AMAS v3 transition plan v0.2 (`amas-v3-transition-plan-v0_2.md`) — primary production spec
- AMAS v2.14.1 canonical at https://github.com/recruiting-tech/upcds/blob/main/docs/ai-operating-system.md
- AMAS v3 Research Deliverable (`amas-v3-research-deliverable.md`) including the OX MCP STDIO advisory P0 finding
- Owner decisions captured in chat session, 2026-04-30: standalone repo direction; repo name `amas-framework`; dogfood yes; bootstrap as PR-0; Codex invocation owner-handled; topics list; `GITHUB_TOKEN` read-only default; UPCDS canonical URL `https://github.com/recruiting-tech/upcds/blob/main/docs/ai-operating-system.md`; `.gitignore` adopted after step-12 surprise in earlier prompt iteration
