# AMAS Framework

GitHub-native framework for AI-assisted projects: role separation (Architect / Builder / Reviewer), universal handoff schema, surface-file synchronization, claimed-action verification, and deterministic enforcement via Actions.

## Status

This repository is under active development. **AMAS v3.0 is in production** via a planned 9-PR sequence. See [docs/adr/ADR-001-initial-repo-setup.md](docs/adr/ADR-001-initial-repo-setup.md) for the standalone-repo decision and the full PR sequence.

The current canonical AMAS framework version is **v2.14.1**, materialized in the UPCDS reference project. Until v3 publishes from this repository, adopters should reference v2.14.1.

## What is AMAS?

AMAS (AI Multi-Agent System) is an operating-system framework for projects that combine human and AI work. It defines:

- **Roles**: Architect, Builder, Reviewer (required) plus optional Researcher, Release Manager, Tooling/Automation Agent, and Adjudicator
- **Universal handoff schema** with seven direction-specific variants (Architect→Builder, Builder→Reviewer, Reviewer→Builder, Reviewer→Architect, Builder→Architect, Human→AI, AI→Human)
- **GitHub-as-canonical-memory** discipline: durable artifacts (ADRs, handoffs, post-merge notes) live in version control, not in chat history
- **Deterministic enforcement** via GitHub Actions for branch naming, PR templates, linked records, surface-file synchronization, and claimed-action verification
- **Surface-file synchronization** to keep AGENTS.md, CLAUDE.md, PR templates, and workflows aligned with the framework version
- **Phantom-action verification**: catching AI claims about actions that did not actually occur

## Reading order

1. This README
2. [AGENTS.md](AGENTS.md) (Codex-targeted) or [CLAUDE.md](CLAUDE.md) (Claude-targeted) for AI agent operating expectations on this repository
3. Once v3 ships: `core.md`, `github-reference.md`, `usage-guide.md`, plus the templates, Actions, and appendices

## Roadmap

v3 production is sequenced across PR-0 (bootstrap) through PR-8 (v3 framework content). PR-9 (a separate PR sequence in the UPCDS reference project) will adopt v3.0.0 there. See [ADR-001](docs/adr/ADR-001-initial-repo-setup.md) for the full PR sequence.

## License

MIT. See [LICENSE](LICENSE).

## Contributing

Contribution guidelines will land alongside v3.0 publication. Until then, framework changes are coordinated through the project owner via the PR sequence.
