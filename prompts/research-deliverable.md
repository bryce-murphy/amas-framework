<!-- Archived 2026-04-30 from amas-v3-research-deliverable.md. AMAS v3 production input. -->

# AMAS v3 Research Deliverable

**Status**: Researcher → Architect handoff per AMAS v3 universal handoff schema
**Author**: Claude (Researcher role, receiving chat) for AMAS v3 robustness validation
**Companion to**: `amas-v3-research-handoff.md` (the Architect's handoff spec); `amas-v3-transition-plan.md`; `amas-v2_14_1.md` canonical; `deep-research-report.md` Design Brief
**Authored**: 2026-04-30
**Sizing**: ~9,500 words across 12 questions plus a risk register and a P0 callout

---

## P0 callout (read this before anything else)

The handoff document specifies that any security advisory affecting MCP authorization or Tool Inventory fields must be surfaced as P0 regardless of question priority. **One such advisory exists and is highly material to AMAS v3**:

On **April 15, 2026**, OX Security disclosed a systemic architectural vulnerability in Anthropic's Model Context Protocol (MCP) STDIO interface ([OX Security advisory](https://www.ox.security/blog/the-mother-of-all-ai-supply-chains-critical-systemic-vulnerability-at-the-core-of-the-mcp/), retrieved 2026-04-30). The flaw is present in Anthropic's official MCP SDKs across Python, TypeScript, Java, and Rust. STDIO transport launches a local subprocess by command; the command executes whether or not the subprocess actually starts as an MCP server. A malicious command passed in returns an error but the side effect runs. OX Security reports 150M+ downloads of affected code, 7,000+ public servers, ~200,000 vulnerable instances, and at least ten CVEs assigned to downstream products including Cursor, Windsurf (zero-click — CVE-2026-30615), VS Code, Claude Code, Gemini CLI, LiteLLM, Flowise, GPT Researcher, Agent Zero, and LangChain-Chatchat ([American Banker coverage](https://www.americanbanker.com/news/unpatched-ai-flaw-poses-risk-to-banking-sector), 2026-04-21, retrieved 2026-04-30).

Anthropic has confirmed the behavior is by design and has declined to patch the protocol-level architecture, taking the position that input sanitization is the implementer's responsibility ([State of Surveillance summary](https://stateofsurveillance.org/news/anthropic-mcp-vulnerability-rce-ai-supply-chain-150-million-downloads-2026/), retrieved 2026-04-30).

**Implications for AMAS v3 Tool Inventory and ref-impl:**
- v3 Tool Inventory documentation should **explicitly warn** that STDIO MCP servers run with the host user's privileges and that any input that flows into the spawn command is an injection vector
- v3 should **prefer HTTP/SSE transport with OAuth 2.1** for any non-trivial MCP server adoption and treat STDIO as the local-development-only path
- For STDIO usage that is unavoidable, v3 should require a tight allowlist of executables, reject inline-execution flags (`-c`, `-e`, `--eval`), and run the MCP host process inside a sandbox container with constrained filesystem and network egress
- AMAS Tool Inventory fields should add: `transport_mode` (stdio | http | sse), `auth_mechanism` (oauth2.1 | bearer | none), `allowlist_path` (for STDIO), `sandbox_required` (boolean)
- **This contradicts a tacit assumption** in the v2.14.1 canonical and the transition plan that MCP integration is broadly safe-by-default. Both documents should be revised to surface STDIO risk and to align with the November 2025 MCP authorization spec rather than treating MCP integration as a uniform abstraction.

This advisory should be referenced in v3's Tool Inventory section and ADR-015. The risk register at the end of this deliverable formalizes mitigation candidates.

---

## Q1. Receiving-surface adapter validation

### Findings summary

The transition plan's adapter set (Claude Code, Codex cloud, ChatGPT, Cursor, Gemini, GitHub Copilot, human maintainer) is largely accurate as of 2026-04-30, but every receiving surface has shipped meaningful changes since the transition plan was authored, and adapter packs need updates before v3 production. The biggest change is that surfaces are converging on common patterns — agent modes, MCP support, in-IDE hooks, persistent memory, and async cloud execution — while diverging on transport security, sandbox semantics, and approval mechanics. The "adapters live in tool appendices because they evolve faster than core" decision (user fork #3) is empirically validated: every surface I checked shipped at least one breaking or semi-breaking change in the last six months.

**Per-surface verification**:

- **Claude Code**: All transition-plan claims hold. Project-scoped `.mcp.json` is canonical, `--add-dir` and `/add-dir` slash command grant additional working directories, and the configuration scope hierarchy (managed → user → project → local) is documented ([Claude Code Settings docs](https://code.claude.com/docs/en/settings), retrieved 2026-04-30). New evolution not reflected in the adapter pack: Claude Code now ships a **plugins / marketplaces system** with `enabledPlugins` and `extraKnownMarketplaces` settings; a **Tool Search** feature reduces context cost when many MCP servers are configured; and **Skills** (`.claude/skills/`) are now first-class extension points alongside subagents and hooks.
- **Codex cloud**: Two-phase runtime model is confirmed: setup phase has internet for dependency installation, agent phase off by default with optional configurable internet access ([Codex Cloud Environments docs](https://developers.openai.com/codex/cloud/environments), retrieved 2026-04-30). AGENTS.md still canonical for project-specific lint/test commands ([Custom instructions doc](https://developers.openai.com/codex/guides/agents-md), retrieved 2026-04-30). New: secrets are removed before agent phase starts; web search defaults to a cached mode (with `live` and `disabled` alternatives) explicitly to mitigate prompt injection; the changelog documents continued AGENTS.md discovery refactors ([Codex Changelog April 2026](https://developers.openai.com/codex/changelog), retrieved 2026-04-30).
- **ChatGPT**: "No-direct-repo-write" claim still essentially correct, but with caveats. Projects gained MCP support in September 2025 with a Developer Mode, "Company Knowledge" cross-connector search, and full project sharing across all paid tiers ([ChatGPT Business release notes](https://help.openai.com/en/articles/11391654-chatgpt-business-release-notes), retrieved 2026-04-30). Context window: 256k total in Thinking mode (128k input / 128k max output) ([ChatGPT release notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes), retrieved 2026-04-30). ChatGPT proper still does not have direct repo write, but it can now invoke Codex from inside the same workspace, and connected MCP servers can take write actions in third-party tools. Adapter pack should note this: ChatGPT-as-Architect remains accurate, but the "no write" claim is narrowing.
- **Cursor**: Background agents in isolated Ubuntu VMs is confirmed, branch-push to GitHub is confirmed, MCP setup confirmed, internet access available with package installation ([Cursor Background Agents docs](https://docs.cursor.com/en/background-agent), retrieved 2026-04-30). Major new evolution: **Cursor 3.2 (April 24, 2026)** introduced `/multitask` async subagents that fan out to parallel work, multi-root workspaces, expanded worktrees experience ([Cursor Changelog](https://cursor.com/changelog), retrieved 2026-04-30). Privacy Mode must be disabled for background agents (a quiet but meaningful trust constraint). Cursor agents have a documented phantom-action signal: agents sometimes claim a task is done when it is not ([Morph Cursor guide](https://www.morphllm.com/cursor-background-agents), retrieved 2026-04-30); a Cursor forum bug report describes background agents intermittently failing to push the branch ([Cursor forum thread](https://forum.cursor.com/t/git-parts-of-cursor-background-cloud-agent-is-not-working-reliable/148759), retrieved 2026-04-30). Adapter should list Cursor as a phantom-action surface alongside Codex.
- **Gemini**: GitHub Code Assist app provides automatic PR review with `gemini-code-assist[bot]` added as reviewer; `/gemini` invocation works for `/review`, `/summary`, `/help`, mention via `@gemini-code-assist` ([Gemini Code Assist GitHub docs](https://developers.google.com/gemini-code-assist/docs/use-code-assist-github), retrieved 2026-04-30). Gemini CLI ReAct loop is confirmed at the official docs and source-level analysis ([Gemini CLI docs](https://developers.google.com/gemini-code-assist/docs/gemini-cli), retrieved 2026-04-30; [Read OSS deep dive](https://readoss.com/en/google-gemini/gemini-cli/inside-agentic-loop-how-gemini-cli-processes-prompt), retrieved 2026-04-30). New evolution: agent mode replaced "tools" feature on October 14, 2025; persistent memory is now supported on GitHub Code Assist; Gemini CLI gained hooks in January 2026 ([New Stack Gemini CLI hooks](https://thenewstack.io/gemini-cli-gets-its-hooks-into-the-agentic-development-loop/), retrieved 2026-04-30); Gemini Code Assist explicitly does **not** generate suggestions inside `.github/workflows/` to avoid introducing insecure CI ([Review GitHub code with Code Assist](https://developers.google.com/gemini-code-assist/docs/review-repo-code), retrieved 2026-04-30).
- **GitHub Copilot**: Approval-non-counting caveat is confirmed: Copilot's reviews don't count toward required approvals; the user who initiates a Copilot coding-agent PR has their approval not count toward required approvals; the coding agent itself cannot approve or merge ([GitHub Copilot code review docs](https://docs.github.com/copilot/using-github-copilot/code-review/using-copilot-code-review), retrieved 2026-04-30; [Reviewing Copilot PRs](https://docs.github.com/copilot/how-tos/agents/copilot-coding-agent/reviewing-a-pull-request-created-by-copilot), retrieved 2026-04-30). Copilot code review now runs on agentic tool-calling architecture using GitHub Actions runners — a non-trivial coupling. **Material billing change**: starting June 1, 2026, Copilot code review will consume GitHub Actions minutes ([GitHub blog April 27, 2026](https://github.blog/changelog/2026-04-27-github-copilot-code-review-will-start-consuming-github-actions-minutes-on-june-1-2026/), retrieved 2026-04-30). Copilot Memory is now available for Pro/Pro+ users.
- **Human maintainer**: No verification needed; the adapter is conceptual rather than product-state.

### Key sources

- Claude Code Settings & MCP — https://code.claude.com/docs/en/settings (retrieved 2026-04-30): canonical scope hierarchy, plugins, project `.mcp.json`
- OpenAI Codex Cloud Environments — https://developers.openai.com/codex/cloud/environments (retrieved 2026-04-30): two-phase model, secrets, AGENTS.md
- Cursor Background Agents — https://docs.cursor.com/en/background-agent (retrieved 2026-04-30): isolated Ubuntu VMs, branch push, environment.json
- Gemini Code Assist on GitHub — https://developers.google.com/gemini-code-assist/docs/use-code-assist-github (retrieved 2026-04-30): /gemini commands, auto PR review
- GitHub Copilot code review docs — https://docs.github.com/copilot/using-github-copilot/code-review/using-copilot-code-review (retrieved 2026-04-30): approval-non-counting caveat

### Recommendations for v3

1. Update each adapter pack with at least the deltas listed above; revisit before v3 publish
2. Add a **last-validated-on date** field to each adapter pack header so adopters can reason about staleness
3. Add Cursor to the explicit phantom-action surface list; the transition plan currently calls out only Codex as "highest-evidence phantom-action surface" but Cursor evidence is now substantial
4. ChatGPT adapter should document the MCP/Codex integration paths and clarify that "no direct repo write" applies only to ChatGPT-the-product, not to Codex-from-inside-ChatGPT
5. Gemini adapter should document the `.github/workflows/` exclusion as a security positive that AMAS adopters can rely on
6. GitHub Copilot adapter must include the June 1, 2026 Actions-minutes billing change as a planning consideration; AMAS Actions documentation should account for the billing model

### Evidence quality

**Settled** for product-state claims (every claim above is sourced to vendor documentation). **Contested** for "Cursor as a phantom-action surface" claim — this is supported by community signals and product reviews but not an explicit vendor-documented characterization. **Settled** for the user-fork-#3 thesis (adapters evolve faster than core); the ~6-month survey shows every surface shipped meaningful changes.

---

## Q2. MCP authorization and security spec current state

### Findings summary

The MCP authorization specification has matured significantly since the Design Brief's research run. The current draft (2025-11-25 spec, with continued refinement in 2026 drafts) places MCP servers as OAuth 2.1 resource servers and mandates a specific subset of OAuth 2.1, RFC 9728, RFC 8414, RFC 7591, and RFC 8707 ([MCP Authorization spec](https://modelcontextprotocol.io/specification/draft/basic/authorization), retrieved 2026-04-30). For HTTP transport, the requirements that AMAS v3 should treat as canonical:

- **OAuth 2.1 with PKCE (S256)** is mandatory for all clients, including confidential clients
- **All authorization endpoints MUST be served over HTTPS**; redirect URIs MUST be either localhost or HTTPS
- **Token audience validation** via RFC 8707 Resource Indicators is mandatory: MCP servers MUST validate that access tokens were issued specifically for them
- **Token isolation** (no passthrough): MCP clients MUST NOT send tokens to the MCP server other than ones issued by the MCP server's authorization server
- **Protected Resource Metadata** (RFC 9728) is mandatory for servers; clients MUST use it for authorization-server discovery
- **Authorization Server Metadata** (RFC 8414) and/or **OpenID Connect Discovery 1.0** is mandatory for AS metadata exposure
- **Dynamic Client Registration** (RFC 7591) and **Client ID Metadata Documents** (CIMD, draft-ietf-oauth-client-id-metadata-document-00) are SHOULD-support, optional but encouraged

For STDIO transport, the spec explicitly says implementations SHOULD NOT follow this authorization specification and instead retrieve credentials from the environment. This is the surface where the OX Security advisory (P0 above) lives.

**Spec changes since the Design Brief**: the spec went through three major revisions; the current model decouples the MCP server from the authorization server (earlier drafts had them coupled). RFC 8707 audience binding is the "fundamental solution to the Confused Deputy problem" — confirmed by RFC and by deep-dive analyses ([Kane.mx technical deconstruction](https://kane.mx/posts/2025/mcp-authorization-oauth-rfc-deep-dive/), retrieved 2026-04-30). However, real-world IdP support is uneven: Auth0, Okta, Microsoft Entra, and Google Identity each have proprietary audience parameters that predate RFC 8707, and only Ping Identity is reported to natively support all MCP-required RFCs.

**Sampling-feature attack class**: Palo Alto Unit 42 documented a separate class of attack against the MCP `sampling` feature, where a malicious server can request LLM completions through the client and exfiltrate or manipulate context ([Unit 42 research](https://unit42.paloaltonetworks.com/model-context-protocol-attack-vectors/), December 2025, retrieved 2026-04-30). This is independent of the STDIO command-injection class.

**Prompt injection / tool poisoning**: a recognized attack class on MCP servers; mitigations include allowlisting tools, treating MCP server outputs as untrusted data, and not auto-executing instructions encountered in tool returns ([Practical DevSecOps MCP security](https://www.practical-devsecops.com/mcp-security-vulnerabilities/), retrieved 2026-04-30).

### Key sources

- MCP Authorization spec (current draft) — https://modelcontextprotocol.io/specification/draft/basic/authorization (retrieved 2026-04-30): canonical normative reference
- ChatForest MCP authentication guide (March 2026) — https://chatforest.com/guides/mcp-authentication-oauth/ (retrieved 2026-04-30): full landscape including extension points
- Kane.mx OAuth/RFC deep dive — https://kane.mx/posts/2025/mcp-authorization-oauth-rfc-deep-dive/ (retrieved 2026-04-30): IdP compatibility matrix
- OX Security STDIO advisory — https://www.ox.security/blog/the-mother-of-all-ai-supply-chains-critical-systemic-vulnerability-at-the-core-of-the-mcp/ (April 15, 2026, retrieved 2026-04-30): the P0 advisory
- Unit 42 sampling-feature attack — https://unit42.paloaltonetworks.com/model-context-protocol-attack-vectors/ (December 2025, retrieved 2026-04-30): independent attack class

### Recommendations for v3

1. Tool Inventory schema should add fields: `transport_mode`, `auth_mechanism`, `audience_validated` (boolean), `discovery_endpoint`, `scopes_required`, and `last_audited_date`
2. v3 prose should establish a **default posture**: OAuth 2.1 + PKCE + audience validation for HTTP MCP; STDIO only when the executable is on a tight allowlist and runs in a sandbox
3. v3 should distinguish "public-facing MCP" (full spec mandatory) from "internal team MCP" (Bearer token may be acceptable but with explicit caveats); this maps to the spec authors' own intent
4. v3 should reference the November 2025 spec as the floor and note that the spec is still evolving (point at the modelcontextprotocol.io draft)
5. AMAS Actions for MCP onboarding should include a verification step: discovery endpoint reachable, audience binding present, no token passthrough
6. The transition plan's MCP Tool Inventory description should be revised to call out the STDIO advisory and direct adopters to HTTP+OAuth where possible

### Evidence quality

**Settled** for the spec's normative requirements (sourced to the official spec). **Settled** for the existence of the OX Security advisory and its technical mechanism. **Contested** for vendor-IdP compliance claims (only one source maps Ping Identity as fully compliant); other sources may differ. **Unknown** for the rate at which downstream products will patch over the next quarter.

---

## Q3. Context7 alternatives and limitations

### Findings summary

Context7 ships an MCP server that retrieves up-to-date, version-specific documentation and code examples for libraries. The Design Brief covered Context7 as the canonical documentation-retrieval MCP option. As of early 2026, the alternatives ecosystem has expanded materially, and Context7 has documented limitations.

**Reported failure modes for Context7**:
- Coverage gaps for very-recent library releases (Context7 pre-scans documentation, so newly-released library versions may not be indexed yet)
- Library-matching accuracy varies; users can use the slash-syntax `/owner/repo` to bypass the matching step
- A widely-cited benchmark from Deepcon (a competing tool, so weight accordingly) reports Context7 at 65% accuracy across 20 contextual scenarios using Autogen, LangGraph, OpenAI Agents, Agno, and OpenRouter SDK; Deepcon claims 90% on the same set ([DEV Community alternatives roundup](https://dev.to/moshe_io/top-7-mcp-alternatives-for-context7-in-2026-2555), retrieved 2026-04-30)

**Alternative tools surveyed** (with brief notes):
- **Deepcon** — claims 90% accuracy benchmark; ~1,000 tokens per response; freemium pricing $8–20/mo
- **Docfork** — open-source MIT, 9,000+ libraries, "Cabinets" feature locks an agent's context to a verified library stack to prevent context poisoning, edge-cached retrieval at ~200ms p95
- **Rtfmbro** — just-in-time fetching from the package's GitHub vs. Context7's pre-scan; better for very-recent releases
- **DeepWiki** — transforms GitHub repos into AI wikis with diagrams and Q&A
- **Ref Tools** — 5k token cap with session awareness; designed for context-window pressure
- **GitMCP** — direct GitHub API for code and documentation
- **Exa** — neuro-semantic search engine for general web content including up-to-date docs
- **Visioncraft MCP** — Computer Vision and GenAI focus, 100k+ repos, "Raven" engine for real-time updates ([Visioncraft comparison](https://www.augmentedstartups.com/blog/visioncraft-mcp-vs-context7-llm-context-management), retrieved 2026-04-30)
- **MCP server benchmarks** — there is now a community benchmark at github.com/opactorai/context-bench

**Practical guidance from the alternatives roundup**: MCP supports multiple servers simultaneously, so using Context7 for breadth and a different tool (e.g., Docfork's Cabinets, or a local tool for proprietary code) for project-specific context is a viable pattern.

### Key sources

- DEV Community 7 MCP alternatives — https://dev.to/moshe_io/top-7-mcp-alternatives-for-context7-in-2026-2555 (February 2026, retrieved 2026-04-30): Deepcon benchmark numbers, alternatives summary
- MCP.Directory Context7 alternatives — https://mcp.directory/blog/top-context7-mcp-alternatives (November 2025, retrieved 2026-04-30): broader alternative inventory
- Awesome MCP Servers Context7 entry — https://mcpservers.org/servers/upstash/context7-mcp (retrieved 2026-04-30): canonical Context7 usage including slash syntax

### Recommendations for v3

1. Frame Context7 as **one option, not the canonical documentation-retrieval MCP**, to reduce vendor lock-in framing in v2.14.1's Context7 emphasis
2. Add a brief **"choosing a documentation MCP"** section in the appendix with criteria: token budget per response, library coverage, recency of releases, version specificity, on-premises support
3. For very-recent library releases, recommend pairing Context7 with a just-in-time alternative like Rtfmbro or web-search grounding
4. Note that Context7's accuracy is debated and that adopters should benchmark against their own use cases rather than relying on vendor benchmarks
5. AMAS v3 should not endorse a single documentation MCP; instead it should establish the principle (ground LLM-generated code in current documentation) and let adopters choose

### Evidence quality

**Contested** for accuracy claims; the 65% vs. 90% benchmark comes from a competing vendor and should be weighted accordingly. **Settled** for the existence of multiple alternatives and their broad capability differences. **Unknown** for failure-mode rates in production; community signals exist but I did not find structured failure-mode data.

---

## Q4. GitHub Actions reusable workflows + composite actions: current best practices

### Findings summary

The transition plan proposes nine starter Actions, packaged for sharing across repositories. The current best-practice landscape is well-documented and is in active evolution: GitHub published a 2026 security roadmap on March 30, 2026 outlining material changes to how reusable workflows handle secrets, immutability, and policy ([GitHub blog: Actions 2026 security roadmap](https://github.blog/news-insights/product-news/whats-coming-to-our-github-actions-2026-security-roadmap/), retrieved 2026-04-30). v3 should be authored against current best practices and should be forward-compatible with the 2026 roadmap changes.

**Reusable workflows vs. composite actions choice**:
- **Reusable workflows** can contain entire jobs with their own `runs-on`, services, and strategy matrix; they are called at the job level via `uses: org/repo/.github/workflows/file.yml@ref`; secrets must be explicitly passed (or `secrets: inherit`); each step is logged separately; cannot have steps added before/after in the calling job
- **Composite actions** bundle steps into a single step; they can be called from any job step; they appear as one collapsed step in logs; every `run` step inside requires explicit `shell:`; they can pass outputs to subsequent steps in the calling job
- **Choice criterion**: reusable workflow if the work needs its own `runs-on` or whole-job semantics; composite action otherwise ([GitHub docs on reusing workflow configurations](https://docs.github.com/en/actions/concepts/workflows-and-actions/reusing-workflow-configurations), retrieved 2026-04-30)

**Versioning**:
- Pin to a specific commit SHA in production for security ([GitHub Well-Architected: Securing Actions](https://wellarchitected.github.com/library/application-security/recommendations/actions-security/), February 2026, retrieved 2026-04-30)
- Distribute with semver tags (`v1`, `v2`); consider major-version moving tags for non-breaking updates with users opting into specific patches via SHA pin
- Composite actions support `uses: org/repo@v1` major-version syntax; reusable workflows historically required exact version refs but the ecosystem has matured around the same convention
- Use Dependabot for automatic version-bump PRs; Dependabot supports the GitHub repository syntax (e.g., `actions/checkout@v6`) and updates inline version comments

**Security**:
- Enforce minimum `GITHUB_TOKEN` permissions per workflow; default to read-only contents
- Prefer **OIDC** for cloud-provider authentication over long-lived secrets
- Avoid `pull_request_target` event in untrusted-fork contexts; treat artifacts and outputs from triggering workflows as untrusted in `workflow_run` workflows
- Never use `latest` or floating refs in production; SHA-pin or semver-tag-pin
- Explicit secret inheritance is becoming the policy norm (the 2026 roadmap calls implicit secret inheritance "trust boundary blurring")
- The 2026 roadmap promises **immutable releases** (publishing-side stricter requirements), **scoped secrets** (binding credentials to specific execution contexts), and **workflow execution rules with evaluate mode** (assess policy impact before enforcement)

**Reference distribution patterns**:
- Single repo for all reusable workflows + composite actions (easier cross-testing) vs. separate repos per concern (clearer ownership, independent versioning); both patterns are documented and used widely ([GitHub Community discussion on enterprise reusable workflows](https://github.com/orgs/community/discussions/171037), retrieved 2026-04-30)
- For development, branch-based testing (point caller workflow to a feature branch) plus relative-path local testing in a sandbox repo
- Ship with both `main` (development) and tagged-stable refs; production callers reference tags only

### Key sources

- GitHub Actions 2026 security roadmap — https://github.blog/news-insights/product-news/whats-coming-to-our-github-actions-2026-security-roadmap/ (March 30, 2026, retrieved 2026-04-30): forward-looking security changes
- GitHub docs on reusable workflow vs. composite action — https://docs.github.com/en/actions/concepts/workflows-and-actions/reusing-workflow-configurations (retrieved 2026-04-30): authoritative semantic comparison
- GitHub Well-Architected Actions security — https://wellarchitected.github.com/library/application-security/recommendations/actions-security/ (February 2026, retrieved 2026-04-30): SHA-pinning, mutable dependency avoidance, OIDC
- GitHub Actions Patterns dev.to guide — https://dev.to/thesius_code_7a136ae718b7/github-actions-workflows-github-actions-patterns-best-practices-pge (March 2026, retrieved 2026-04-30): practical templates

### Recommendations for v3

1. AMAS-distributed Actions should be packaged primarily as **reusable workflows** when they contain orchestration (e.g., `ai-attribution-check.yml` is a job-level orchestration), and as **composite actions** when they bundle a few steps into a callable unit (e.g., `attest-bot-identity` could be composite)
2. Use **semver tags + commit SHA pinning** convention; ship with both `v1` major-tag and pinnable patch tags (`v1.0.3`)
3. Document the **forward-compatibility plan** with the 2026 GitHub roadmap: AMAS should plan for explicit secret passing, scoped secrets, and immutable releases by default
4. Provide a **Dependabot configuration template** for adopters so AMAS Action updates flow as PRs they can review
5. Add a section on **workflow injection** mitigation specifically: AMAS Actions consume PR titles, commit messages, branch names, and comment bodies, all of which are untrusted; templates should never use `${{ github.event.* }}` in `run:` blocks unsanitized
6. Provide a **test harness** using `act` or self-hosted runners so adopters can validate AMAS workflows before merging; the dev.to patterns guide has good templates to start from

### Evidence quality

**Settled** for current GitHub Actions semantics and security guidance. **Settled** for the reusable-workflow-vs-composite-action choice criteria. **Forward-looking, partially unknown** for the 2026 security roadmap deliverables; v3 should plan for them as design constraints but not assume they are available at v3 publish time.

---

## Q5. AI coding framework prior art: governance pattern survey

### Findings summary

The agentic-AI coding framework landscape is large and active. AMAS occupies a distinct conceptual position: most surveyed frameworks focus on **capability extension and orchestration** (do more things), while AMAS focuses on **operating discipline** (do things safely with verifiable claims, role separation, and audit). The most directly relevant academic synthesis I located is "Clawed and Dangerous: Can We Trust Open Agentic Systems?" — a survey of 50 papers introducing a six-dimensional analytical taxonomy and an evaluation scorecard ([arXiv 2603.26221](https://arxiv.org/html/2603.26221), retrieved 2026-04-30). It identifies persistent gaps in deployment controls, operational governance, persistent-memory integrity, and capability revocation — gaps AMAS partially addresses through its role separation, claim verification, and surface-file synchronization mechanisms.

**Per-framework brief**:

- **Aider** (44k stars): pair-programming via diffs and patches, strong git workflows, executes generated code directly on the user's machine without sandboxing. Governance: minimal — the trust model is the user reading every diff before applying. AMAS comparison: AMAS's deterministic-enforcement Actions and claim verification add safety AMAS adopters using Aider can layer on top.
- **OpenHands** (formerly OpenDevin, 72k stars): open-source autonomous coding agent, sandboxed Docker containers with event-stream architecture, multi-agent delegation, 72% on SWE-bench Verified ([OpenHands docs](https://openhands.dev/), retrieved 2026-04-30). Governance: Docker isolation + auditable action traces + GitHub PR creation as the human review gate. AMAS comparison: OpenHands gives strong execution isolation; AMAS adds the meta-governance about role separation, claimed-action verification, and surface-file synchronization, none of which OpenHands defines.
- **Devin (Cognition)**: proprietary autonomous coding agent. Governance: opinionated managed environment, PR-creation as the human review gate. AMAS comparison: Devin's PR-as-gate matches AMAS canonical assumption; AMAS's claimed-action discipline matters more for Devin than for foreground tools because Devin runs autonomously.
- **Cursor (with background agents)**: Ubuntu VMs, branch-push, Privacy Mode trade-off, `/multitask` async subagents (Cursor 3.2). Governance: branch isolation as the human review boundary; Privacy Mode disabled is a quiet trust escalation. AMAS comparison: Cursor's branch-isolation pattern aligns with AMAS's GitHub-canonical assumption; AMAS's surface-file sync should prevent CLAUDE.md and AGENTS.md drift between Cursor sessions.
- **GitHub Copilot (coding agent)**: agentic tool-calling architecture on GitHub Actions runners, isolated containers, cannot approve/merge. Governance: native to GitHub branch-protection rules and CODEOWNERS. AMAS comparison: AMAS Actions reinforce Copilot's approval-non-counting caveat; AMAS reference impl is largely a superset of Copilot's native governance.
- **Anthropic Claude Skills / Agent Skills**: SKILL.md folder format with progressive disclosure (~100 token metadata + <5k token body + on-demand resources), works across Claude.ai, Claude Code, API ([Anthropic Skills overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview), retrieved 2026-04-30). The community is converging on agentskills.io as a vendor-neutral standard. Governance: trusted-source advisory (skills can execute arbitrary code), per-skill `allowed-tools` permission grants. AMAS comparison: Skills are about capability extension, not governance discipline; AMAS could ship reference-implementation patterns *as a Skill* (for example, a `claimed-action-verification` skill that hooks into Claude Code's review workflow). The two are complementary.
- **AWS Bedrock Agents / Azure AI Studio**: enterprise agent orchestration platforms. Evidence insufficient for a deep comparison; both ship governance features (IAM scoping, audit logs) but their abstraction level is different (cloud-managed agents vs. AMAS's framework-as-doc).
- **LangChain / LangGraph**: agent orchestration library; governance is application-layer, not framework-layer. Not directly comparable.
- **"Agentic Engineering Framework"** (4 GitHub stars): a small competitor concept — provider-neutral CLI-agent governance with task-driven workflows, context budget management, healing loops, audit ([awesome-cli-coding-agents listing](https://github.com/bradAGI/awesome-cli-coding-agents), retrieved 2026-04-30). Conceptually closest to AMAS in stated mission; small community.

**What AMAS does that competitors don't** (worth defending in v3 prose):
- **Two-part review robustness model**: separating substantive review from claimed-action verification is not a pattern I found in any other framework's documentation
- **Surface-file synchronization with manifest + Action**: drift-after-upgrade detection at the framework-version level. The closest analogues are GitOps and IaC patterns (covered in Q9), but those are at the infrastructure layer, not the framework-doc layer.
- **Explicit role separation** (Architect / Builder / Reviewer / Researcher / Tooling-Automation Agent / Maintainer): I did not find an equivalent in the surveyed frameworks. Most either flatten into "agent" or split only by lifecycle phase (planner / executor / verifier).
- **Universal handoff schema with direction-explicit variants**: not found elsewhere as a first-class concept.
- **Calibrated optional roles with re-score triggers**: not found elsewhere; the closest analogue is HELM's multi-dimensional scoring (Q12), but that's evaluation, not operational role assignment.

**Candidate ideas AMAS should consider borrowing**:
- **Progressive disclosure** (from Skills): AMAS docs are large; a SKILL.md-style metadata-first pattern for the reference impl would reduce context cost for adopters
- **Hooks** (from Claude Code and Gemini CLI): deterministic checks at lifecycle events (pre-tool, post-tool, session-start, etc.) could complement AMAS's Actions for in-session enforcement
- **Sandbox profiles** (from OpenHands and Codex): AMAS could specify required sandbox properties for certain Reviewer surfaces rather than leaving it to adopters
- **HMAC tool receipts** (from "Tool Receipts" research, see Q8): cryptographic proof of tool execution would harden claimed-action verification
- **Model-version pinning** (from solo-dev governance, see Q11): AMAS Tool Capability Model could include explicit pinned-model expectations to control behavior drift

### Key sources

- "Clawed and Dangerous" arxiv survey — https://arxiv.org/html/2603.26221 (retrieved 2026-04-30): six-dimensional taxonomy, gap analysis, scorecard
- OpenHands review — https://aicoolies.com/reviews/openhands-review (March 2026, retrieved 2026-04-30): governance shape and benchmark performance
- Claude Skills docs — https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview (retrieved 2026-04-30): progressive disclosure pattern
- Awesome CLI Coding Agents — https://github.com/bradAGI/awesome-cli-coding-agents (retrieved 2026-04-30): broad framework inventory

### Recommendations for v3

1. v3 prose should explicitly **claim** the two-part review model, role separation discipline, surface-file sync, and universal handoff schema as AMAS-distinctive contributions; the claim is defensible based on this survey
2. v3 should adopt **progressive disclosure** as a documentation pattern: a thin metadata layer per section, with details lazy-loaded
3. v3 should add a **comparison appendix** ("AMAS vs. other frameworks") that adopters can use to decide what AMAS adds on top of whatever they're already running
4. v3 should reference the "Clawed and Dangerous" survey when defending the operational-governance gap claim
5. Consider shipping a reference-impl Skill that an adopter using Claude Code can install to get a starter AMAS adoption (this is a future PR, not blocking v3 publish)

### Evidence quality

**Settled** for the per-framework feature claims (vendor-documented). **Contested** for relative quality — different sources give different rankings of OpenHands vs. Devin vs. SWE-agent depending on benchmark. **Settled but recent** for the gap analysis from "Clawed and Dangerous"; the survey's date and methodology should be re-checked at v3 publish.

---

## Q6. Project-type best practices

### Findings summary

The transition plan proposes five project-type appendices (API/app, research/methodology, code reports / data analysis / dashboards, documents-only, mixed). The structure is sound. Each project type has well-established industry references that the appendix should anchor to.

**API / app**:
- **OWASP API Security Top 10 (2023)** is the canonical reference for API risk classes; broken object-level authorization, broken authentication, and broken function-level authorization head the list ([OWASP API Security Project](https://owasp.org/www-project-api-security/), retrieved 2026-04-30; [Top 10 list](https://owasp.org/API-Security/editions/2023/en/0x11-t10/), retrieved 2026-04-30)
- **OWASP LLM Top 10** for AI-augmented apps (prompt injection, training data poisoning, supply chain) — directly relevant when AMAS-built apps use LLMs themselves
- **12-Factor App** methodology (codebase, dependencies, config, etc.) for cloud-native apps
- **Google API Design Guide** and **Microsoft REST API Guidelines** for API contract design
- **Continuous Delivery** (Humble & Farley) for release engineering posture
- AMAS-specific operating concerns: API/app projects benefit from the **Tooling/Automation Agent** role; tests, deploy automation, and observability all benefit from a dedicated role; security review should reference OWASP top 10 as a checklist artifact

**Research / methodology**:
- **PRISMA** for systematic review reporting; **CONSORT** for randomized trials; both have updated 2020-era versions
- **FAIR principles** (Findable, Accessible, Interoperable, Reusable) for data management — endorsed by NIH and adopted as a standard reference ([NIH FAIR alignment](https://bioinformatics.ccr.cancer.gov/docs/btep-coding-club/CC2024/Quarto/GettingStarted_with_Quarto_orig.html), retrieved 2026-04-30)
- **Preregistration** practices (OSF, AsPredicted) for hypothesis-locking
- AMAS-specific operating concerns: research projects need an **explicit Researcher role**, and the project's main artifact is often the research note / report rather than code; the Reviewer role for research must include methodology critique, not just code review

**Code reports / data analysis / dashboards**:
- **Quarto** as a current-generation literate-programming tool; combines code, prose, and outputs; renders to multiple formats ([Quarto reproducible workflows](https://maria.quarto.pub/notes-on-reproducible-workflows/), retrieved 2026-04-30)
- **R Markdown** and **Jupyter notebooks** as predecessor / parallel options
- **Tufte's Visual Display of Quantitative Information** and **Few's *Information Dashboard Design*** as canonical references on display craft; **Wilke's Fundamentals of Data Visualization** is a current open-source companion ([Healy data viz reference list](https://socviz.co/), retrieved 2026-04-30)
- **DAMA-DMBOK** as the reference body for data governance; useful for dashboards used in regulated environments
- AMAS-specific operating concerns: dashboards / reports often have **derivative artifacts** (cached data, pre-computed aggregates) that drift; the Surface manifest concept could extend to "data surfaces" that the dashboard depends on

**Documents-only**:
- **Microsoft Style Guide** and **Google developer documentation style guide** for technical writing standards
- **Diátaxis** framework for documentation (tutorials / how-to / reference / explanation as four distinct modes)
- **Documentation-as-code** practices: docs in version control, reviewed via PR, built and tested via CI
- AMAS-specific operating concerns: documents-only projects collapse Builder and Reviewer naturally; the two-part review model still applies (substantive review of content; verification that referenced facts exist); claim verification for citations is high-value

**Mixed**:
- The harder case. There is no canonical reference for "multi-output project shape." Recommend AMAS adopt a **dominant-type-with-secondary-types** framing: declare one primary project type and one or more secondary types; apply the primary type's appendix first, then add secondary type concerns
- **Software Engineering Body of Knowledge (SWEBOK)** is a broad reference for the integration concerns
- AMAS-specific operating concerns: mixed projects benefit most from explicit role separation because the cross-type interactions are where coordination breaks

### Key sources

- OWASP API Security Top 10 — https://owasp.org/API-Security/ (retrieved 2026-04-30): canonical API risk reference
- Quarto reproducible workflows — https://maria.quarto.pub/notes-on-reproducible-workflows/ (retrieved 2026-04-30): current literate-programming reference
- API documentation knowledge taxonomy — https://arxiv.org/pdf/1907.13260 (retrieved 2026-04-30): five-dimensional API doc taxonomy
- Data Visualization (Healy) — https://socviz.co/ (retrieved 2026-04-30): Tufte/Wilke/Wickham reading list

### Recommendations for v3

1. Each appendix should open with **3–5 authoritative references** with URLs and short notes on what they contribute, not a full literature review
2. Each appendix should include an **AMAS operating-concerns** section explicitly: which optional roles are most valuable for this project type, what is canonically expected vs. optional
3. The **mixed-type** appendix should explicitly use the dominant-with-secondary pattern, since the literature does not have a canonical reference for true multi-output projects
4. For the API/app appendix, reference both the **API Security Top 10** and the **LLM Top 10**, since AMAS-built apps will increasingly call LLMs themselves
5. For the research appendix, include a recommendation that the **Researcher role be canonical (not optional)** for research-type projects — this aligns with the user fork that elevated optional roles in calibration

### Evidence quality

**Settled** for the existence and authority of the references cited (OWASP, PRISMA, FAIR, Diátaxis, Quarto/Tufte, etc.). **Contested** for "best" patterns within each type — communities have multiple competing schools (e.g., R Markdown vs. Jupyter for analysis, Microsoft vs. Google style for writing). **Unknown** for adoption rates of each reference in the AMAS-target audience; v3 should not over-prescribe.

---

## Q7. Multi-surface review empirical evidence

### Findings summary

AMAS v2.14.1 §24.2(b) asserts that single-surface mitigation is insufficient and multi-surface receiving-side review is load-bearing. The strongest external supporting evidence comes from two sources: (1) the established code-review-effectiveness literature, which establishes that multi-reviewer setups detect different defect classes; and (2) the agent-governance literature (covered in Q5 and Q8), which establishes that AI-coding agents systematically fail in ways that single-pass review does not catch.

**Code review effectiveness literature**:
- **Bosu, Greiler, Bird (MSR 2015)** — "Characteristics of Useful Code Reviews: An Empirical Study at Microsoft" — analysed 1.5M review comments from five Microsoft projects; found wide variation in reviewer effectiveness even with the same technique on the same artifact, citing earlier work by Rigby et al. ([Bosu et al. 2015](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/bosu2015useful.pdf), retrieved 2026-04-30). The study did not directly measure multi-reviewer effect sizes, but the variation finding supports AMAS's underlying claim that no single reviewer catches everything.
- **Sadowski, Söderberg, Church, Sipko, Bacchelli (ICSE SEIP 2018)** — "Modern Code Review: A Case Study at Google" — Google's review practice emphasizes detailed review explanations; the case-study methodology limits effect-size claims but the descriptive evidence is consistent with multi-reviewer benefit
- **Jureczko (IET Software 2020)** — comparison of tool-assisted vs. over-the-shoulder review at Ocado; effects depend on review size and technique

**AI-augmented review literature**:
- The "Clawed and Dangerous" survey (Q5) documents that single-tool review systematically misses issues that emerge from agentic execution: capability over-privilege, persistent-memory tampering, and revocation gaps
- Coordinated audits between April and September 2025 disclosed exploitable weaknesses across major coding agents (Claude Code, Cursor, Copilot, OpenHands, Devin, Cline, Amazon Q, Windsurf), supporting the claim that no single agent's defenses are sufficient
- A September 2025 Chinese state-sponsored espionage campaign reportedly used Claude Code with MCP-connected tools, with most steps executed autonomously, and was identified through cross-system signals rather than single-tool detection ([Anthropic statement referenced in Clawed and Dangerous survey](https://arxiv.org/html/2603.26221), retrieved 2026-04-30)

**Conditions where multi-surface review is strongest**:
- When surfaces have different blind spots (e.g., one surface is sandbox-isolated and another has deep repo context, so each catches different defect classes)
- When the artifact is high-stakes (security-relevant code, regulated workflows)
- When the surfaces have **different prompts and reviewers acting on the same diff** — this is the key AMAS pattern

**Conditions where multi-surface is marginal**:
- Small, well-scoped diffs where any single competent reviewer catches the issues
- Boilerplate / mechanical changes (dependency bumps, formatting) where the marginal reviewer adds cost without adding signal

**Effect sizes**: I did not find a clean published effect-size number specifically for "AI multi-surface review reduces defect rate by X%". The literature is qualitative or single-case-study at this point. AMAS v3 should be careful not to overclaim — the empirical evidence supports the claim that single-surface is insufficient and that multi-surface adds detection capacity, but does not yet quantify the marginal benefit.

### Key sources

- Bosu, Greiler, Bird (MSR 2015) — https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/bosu2015useful.pdf (retrieved 2026-04-30): reviewer-variance evidence
- Sadowski et al. (ICSE SEIP 2018) — Modern Code Review at Google
- "Clawed and Dangerous" arxiv survey — https://arxiv.org/html/2603.26221 (retrieved 2026-04-30): coordinated-audit evidence across agents
- Awesome Code Review Research bibliography — https://github.com/mgreiler/awesome-code-review-research (retrieved 2026-04-30): broader literature inventory

### Recommendations for v3

1. v3 prose should keep the multi-surface claim but **frame it as supported-by-multiple-converging-lines-of-evidence rather than as a quantified effect size**
2. Add a brief evidence-base footnote pointing at Bosu et al., Sadowski et al., and the "Clawed and Dangerous" survey
3. Note that the strongest evidence is for **agent-specific failure modes** (the audits), not for general code review effect sizes; v3 should ground the multi-surface claim in the agent-failure literature rather than the older code review literature
4. Consider commissioning or encouraging an empirical study within UPCDS or a similar reference project to quantify multi-surface benefit; this is a research opportunity v3 can flag

### Evidence quality

**Settled** for the existence of the underlying claim (single-surface insufficiency, multi-surface adds capacity). **Contested / unknown** for effect sizes; the literature does not yet quantify "AI multi-surface review reduces phantom-action incidents by X%". Marked as evidence-supported-but-not-yet-quantified.

---

## Q8. Phantom-action / claim-verification mitigation patterns

### Findings summary

AMAS v2.14.1 §8.1.1.2 names four claim categories (commit existence, file existence, follow-up artifact existence, identifier-pattern compliance). The published academic taxonomy is broader and more granular, but AMAS's four categories are a reasonable subset and are consistent with the literature. The clearest gap: AMAS could extend the taxonomy and adopt some of the verification mechanisms that the academic and industry frameworks describe.

**Published taxonomies of agent hallucinations**:

- **MIRAGE-Bench** ([arXiv 2507.21017](https://arxiv.org/pdf/2507.21017), retrieved 2026-04-30): three-category taxonomy: unfaithful to **task instructions**, unfaithful to **execution history**, unfaithful to **environment observations**. AMAS's claimed-action class corresponds primarily to "unfaithful to execution history" — the agent claims an action it did not take.
- **AgentHallu** ([arXiv 2601.06818](https://arxiv.org/pdf/2601.06818), retrieved 2026-04-30): five top-level categories with 14 sub-categories: Planning, Retrieval, Reasoning, Human-Interaction, **Tool-Use**. Tool-use is reported as the most challenging category to detect (best model achieves 11.6% step-localization accuracy). AMAS's four categories all fall under Tool-Use in this taxonomy.
- **HalluciNot / HDM-2** (AIMon Labs, [arXiv 2504.07069](https://arxiv.org/pdf/2504.07069), retrieved 2026-04-30): enterprise taxonomy: context-based, common-knowledge, enterprise-specific, innocuous. Less directly applicable to agentic claim verification but useful for enterprise adoption framing.
- **Tool Receipts** ([arXiv 2603.10060](https://arxiv.org/pdf/2603.10060), retrieved 2026-04-30): epistemic taxonomy mapping LLM agent claims to Indian-philosophy categories (pratyakṣa = direct quote from tool output; anumāna = inference from tool data; śabda = external-source claim; abhāva = absence claim; ungrounded = no evidence). Implements **HMAC-signed tool execution receipts** with <15ms verification overhead. This is the most operationally interesting framework for AMAS to consider.
- **Survey "From Illusion to Insight"** ([MDPI AI 2025](https://www.mdpi.com/2673-2688/6/10/260), retrieved 2026-04-30): six-category mitigation taxonomy: Training/Learning, Architectural Modifications, Input/Prompt Optimization, Post-Generation Quality Control, Interpretability/Diagnostic, Agent-Based Orchestration

**The "execution hallucinations" class**: defined in a recent agent-hallucinations survey as "where LLM-based agents claim to have completed certain sub-stages during the execution phase, but in reality, they have not actually been performed or accomplished" ([LLM Agents Hallucinations survey paper](https://studylib.net/doc/28277236/mactg-relatedpaper1), retrieved 2026-04-30). This is precisely AMAS's phantom-action class, and the literature now has a name for it.

**Comparison to AMAS's four categories**:
- AMAS: commit existence; file existence; follow-up artifact existence; identifier-pattern compliance
- Implicit in AMAS but not enumerated: **claimed test execution** (was the test actually run?), **claimed external API call** (was the API call actually made?), **claimed dependency installation** (was the package actually installed?), **claimed permission grant or revocation** (was the permission actually changed?)
- The literature's tool-use category covers all of these; AMAS could extend to a fifth and sixth category

**Detection patterns from the literature**:
- **Self-consistency** — sample multiple completions and check agreement
- **Uncertainty estimation** — the model reports confidence; low-confidence claims flagged
- **Retrieval-augmented verification** — claims are checked against an authoritative source
- **Fine-tuned classifiers** — purpose-built models that classify outputs as faithful or hallucinated
- **LLM-as-a-judge** — a separate LLM evaluates the agent's claims
- **Tool execution receipts** (HMAC-signed) — cryptographic proof of every tool call, cross-referenced against agent claims in real time
- **Execution-based validators** — code is actually run and outputs compared against claims

**AMAS's `claimed-action-verification.yml` Action**: the tool-receipt pattern is the strongest match for what the Action could implement. For GitHub-canonical claims (commit existence, file existence, follow-up artifact existence), the verification is direct (the GitHub API is the receipt). For non-GitHub claims (test execution, external API call), AMAS would need a receipt-emitting pattern in the reference impl — possibly via GitHub Actions logs or via an explicit test-result artifact.

### Key sources

- MIRAGE-Bench taxonomy — https://arxiv.org/pdf/2507.21017 (retrieved 2026-04-30): three-axis hallucination taxonomy
- AgentHallu benchmark — https://arxiv.org/pdf/2601.06818 (retrieved 2026-04-30): five-category, 14-subcategory taxonomy with 693 trajectories
- Tool Receipts framework — https://arxiv.org/pdf/2603.10060 (retrieved 2026-04-30): HMAC-signed execution receipts with epistemic typing
- LLM Agents Hallucinations survey (definition of "execution hallucinations") — https://studylib.net/doc/28277236/mactg-relatedpaper1 (retrieved 2026-04-30)

### Recommendations for v3

1. v3 should **extend the four-category framing** to a more general principle: "any claim of execution that is not directly verifiable against an authoritative artifact is a candidate phantom action." The four current categories then become **canonical examples**, not the closed list.
2. v3 should **explicitly add** at least two new examples: claimed test execution and claimed external API call. Both are common in agentic workflows.
3. v3 should reference the published taxonomy (MIRAGE-Bench's three-axis split, or AgentHallu's tool-use sub-categories) so adopters who want to go deeper have a literature anchor
4. v3 should describe **tool execution receipts as a forward-looking mechanism** for `claimed-action-verification.yml`. Initial implementation can use GitHub APIs as receipts; later versions could adopt HMAC-signed receipts for non-GitHub claims.
5. v3 should clarify that the four categories are GitHub-reference-impl examples, not framework-canonical exhaustive enumeration; the canonical principle is the broader "execution claim verification" discipline

### Evidence quality

**Settled** for the existence and authority of the published taxonomies. **Contested** for which taxonomy is "best"; multiple competing taxonomies exist and each has different framing. **Settled** for the gap (literature has multiple clean taxonomies; AMAS's four-category framing is a reasonable but non-exhaustive subset). **Unknown** for the relative effectiveness of the various detection patterns in production AMAS adoption; benchmarking would be needed.

---

## Q9. Surface-file drift as recognized problem in OSS framework evolution

### Findings summary

The drift-after-upgrade problem is a recognized class with extensive industry literature, primarily under the **configuration drift** name in DevOps and **GitOps reconciliation** in Kubernetes contexts. AMAS's surface-file synchronization is conceptually adjacent to but not identical to these patterns; AMAS sits at a different abstraction layer (framework documentation surfaces) than the cited tools (infrastructure / deployment configuration).

**Established patterns**:

- **Configuration synchronization** — Martin Fowler's bliki entry describes the canonical pattern: define desired state in a manifest; a tool periodically (or continuously) reconciles actual to desired ([Fowler bliki: Configuration Synchronization](https://martinfowler.com/bliki/ConfigurationSynchronization.html), retrieved 2026-04-30). Tools: CFEngine, Puppet, Chef, Ansible.
- **GitOps** — Git as single source of truth for declarative infrastructure; tools (ArgoCD, Flux) reconcile cluster state to Git state ([OpenLiberty GitOps and ArgoCD piece](https://openliberty.io/blog/2024/04/26/argocd-drift-pt1.html), retrieved 2026-04-30). Closest conceptual analogue to AMAS surface-file sync: the manifest is the source of truth, the actual files are reconciled.
- **Infrastructure as Code (IaC)** — Terraform, CloudFormation, OpenTofu, Pulumi: declarative state files, drift detection via plan comparison ([Spacelift configuration drift overview](https://spacelift.io/blog/what-is-configuration-drift), retrieved 2026-04-30)
- **Immutable infrastructure** — discard rather than reconcile; PhoenixServers and ImmutableServers patterns
- **SBOM standards** — CycloneDX, SPDX, in-toto — software bill of materials for supply-chain integrity; relevant for tracking what AMAS-distributed Actions an adopter has installed and at what version
- **Schema versioning** — OpenAPI, JSON Schema; both have explicit version-evolution patterns (additive vs. breaking)
- **Migration tooling** — codemods (jscodeshift, OpenRewrite), Renovate, Dependabot; close to AMAS's "human-driven migration with detection" but with automated rewriting
- **Documentation drift** — the Diátaxis framework and DocOps practices recognize documentation drift as a class but do not have a canonical detection mechanism; documentation drift is usually caught by reader reports, not by automated detection

**Key conceptual observation**: AMAS's surface-file sync is **closest to GitOps** in pattern (manifest declares desired state, drift detection action compares actual to manifest). It differs in that the "actual state" being checked is documentation files (CLAUDE.md, AGENTS.md, etc.) rather than infrastructure resources. The detection mechanism (an Action that reads `surfaces.yml` and compares to actual file presence and content hashes) is consistent with GitOps drift-detection patterns.

**Patterns AMAS could borrow**:
- **Auto-remediation** — ArgoCD can auto-sync when drift is detected; AMAS could offer an opt-in auto-remediation Action that opens a PR with the manifest-aligned files when drift is detected
- **Codemod-style migrations** — when v3 changes the surface manifest format from v2.14.1, a codemod could automate the migration; this is more user-friendly than human-driven migration
- **Audit-only mode** — like Terraform's `plan`, AMAS could have an explicit "drift-report" mode that doesn't change anything, useful for adopters in restrictive environments

**Conceptual difference from GitOps**: GitOps assumes the operator has full control of the deployment target. AMAS surface-file sync assumes the *adopter* has full control of their repo, but AMAS has only declarative authority (the manifest) over what should exist. AMAS cannot force-sync files; it can only detect drift and ask. This is fine and arguably preferable, but the prose should make it clear.

### Key sources

- Fowler bliki: Configuration Synchronization — https://martinfowler.com/bliki/ConfigurationSynchronization.html (retrieved 2026-04-30): canonical pattern reference
- OpenLiberty GitOps and drift — https://openliberty.io/blog/2024/04/26/argocd-drift-pt1.html (retrieved 2026-04-30): GitOps pattern explanation
- Spacelift configuration drift — https://spacelift.io/blog/what-is-configuration-drift (February 2026, retrieved 2026-04-30): tool inventory and patterns
- IBM Configuration Drift overview — https://www.ibm.com/think/topics/configuration-drift (retrieved 2026-04-30): conceptual framing

### Recommendations for v3

1. v3 prose should **frame surface-file sync as analogous to GitOps drift reconciliation, at the framework-doc layer**. Adopters familiar with GitOps will recognize the pattern; adopters new to it have a clean reference.
2. The surface-file sync Action should support both **detect-only** and **propose-changes-as-PR** modes, mirroring the IaC plan/apply distinction
3. v3 could ship a **codemod-style migration tool** for v2.14.1 → v3 surface manifest format changes; this would be user-friendly and is consistent with industry pattern
4. Include a section on **what surface-file sync does not promise**: it does not enforce content correctness inside files, only their existence and structural conformance to the manifest. Adopters should not over-rely on it.
5. Consider adopting **manifest checksums** (like SBOM) so surface-file drift detection can identify content changes, not just file additions/removals

### Evidence quality

**Settled** for the existence of the broader configuration-drift problem class and standard patterns. **Contested** for "best pattern for AMAS specifically" since AMAS's domain (framework-doc surface sync) is not exactly any of the cited domains. **Unknown** for adoption rates of GitOps-style auto-remediation among AMAS-target audience.

---

## Q10. AI agent identity verification on GitHub

### Findings summary

GitHub already has well-established mechanisms for distinguishing bot from human reviewers, and these are sufficient for AMAS's review-freshness checks at v3 timeframe. Looking forward, cryptographic agent-identity standards are emerging but not yet mainstream.

**Current GitHub mechanisms**:

- **GitHub App users have a `[bot]` suffix** in the slug (e.g., `gemini-code-assist[bot]`, `dependabot[bot]`); the `User` API returns `type: "Bot"` for these accounts
- **PR review object metadata** includes the reviewer's `user.type` field; AMAS Actions can filter on this to distinguish bot vs. human reviews
- **Bot user ID** is distinct from App ID; this catches some adopters off guard ([dev.to AI agent identity guide](https://dev.to/agent_paaru/each-ai-agent-gets-its-own-github-identity-how-we-gave-every-bot-its-own-bot-commit-signature-1197), March 2026, retrieved 2026-04-30)
- **GitHub Apps with installation access tokens** (1-hour TTL) are the standard pattern for bot authentication; the `actions/create-github-app-token` Action handles token minting ([create-github-app-token docs](https://github.com/actions/create-github-app-token), retrieved 2026-04-30)
- **Sigstore / cosign** for commit signing exists but is not widely adopted for AI agent identity; signed commits are a stronger but less common signal

**Emerging standards**:

- **HTTP Message Signatures (RFC 9421)** — public-key cryptographic signing of HTTP requests by AI agents, with a public-key registry for verification. HUMAN Security shipped an open-source showcase implementation ([HUMAN Verified AI Agent](https://github.com/HumanSecurity/human-verified-ai-agent), retrieved 2026-04-30). This is the most likely future direction for cross-vendor agent identity.
- **AgentsID** — a registry-style standard with per-agent capability scopes, audit logging, and revocation ([AgentsID GitHub](https://github.com/AgentsID-dev/agentsid), retrieved 2026-04-30). Notes that 88% of MCP servers need authentication but only 8.5% use OAuth, and 53% rely on static API keys — a significant identity-management gap
- **Better Auth's Agent Auth Protocol** — open-source agent authentication, capability-based authorization, service discovery ([better-auth/agent-auth-protocol](https://github.com/better-auth/agent-auth-protocol), retrieved 2026-04-30)
- **Auth0 for AI Agents** — commercial offering for agent identity with token vaults and human-in-loop approvals

**For AMAS today**:

The simplest and most reliable mechanism is the GitHub `user.type == "Bot"` filter on PR review objects. This is documented, stable, and supported across all AMAS-target surfaces. AMAS's review-freshness check should:

1. Fetch the latest reviews on the PR via GitHub API
2. Group reviews by `user.type` (Bot vs. User)
3. For each, check `submitted_at` against `head_sha` push timestamps
4. Apply different policies per type if needed (e.g., bot reviews older than the head SHA may be auto-dismissed; human reviews are flagged for re-confirmation but not auto-dismissed)

For commit-author verification (e.g., distinguishing AI-generated commits in CODEOWNERS contexts), the noreply email pattern `<bot-user-id>+<app-slug>[bot]@users.noreply.github.com` is canonical; AMAS Actions can parse the author email reliably.

### Key sources

- GitHub create-github-app-token Action — https://github.com/actions/create-github-app-token (retrieved 2026-04-30): canonical bot-token minting pattern
- HUMAN Verified AI Agent — https://github.com/HumanSecurity/human-verified-ai-agent (retrieved 2026-04-30): HTTP Message Signatures showcase
- AgentsID — https://github.com/AgentsID-dev/agentsid (retrieved 2026-04-30): agent identity statistics and registry pattern
- AI agent GitHub identity guide — https://dev.to/agent_paaru/each-ai-agent-gets-its-own-github-identity-how-we-gave-every-bot-its-own-bot-commit-signature-1197 (March 2026, retrieved 2026-04-30): practical implementation

### Recommendations for v3

1. v3's review-freshness Action should use **`user.type == "Bot"`** as the canonical bot-vs-human signal; this is sufficient for AMAS reference impl
2. v3 prose should mention HTTP Message Signatures (RFC 9421) and AgentsID as **forward-looking standards** that AMAS may adopt in a future minor version when they reach broader adoption
3. v3 should require AMAS-distributed Actions to use **GitHub Apps with installation access tokens**, not user-PATs, for bot identity; document this in the Actions appendix
4. AMAS should include a recommendation that adopters **separate AI-agent commits from human commits via dedicated GitHub App identities**, so audit trails and CODEOWNERS work correctly
5. Statistics worth surfacing in v3 prose: the AgentsID-cited numbers (88% of MCP servers need auth, 8.5% use OAuth, 53% rely on static API keys) underscore why AMAS Tool Inventory should require explicit auth-mechanism documentation

### Evidence quality

**Settled** for current GitHub bot-identification mechanisms. **Settled but emerging** for HTTP Message Signatures and agent-identity standards; v3 should track but not depend on them. **Contested** for the AgentsID statistics (single-source); AMAS prose should hedge.

---

## Q11. Solo-operator AI development governance patterns

### Findings summary

AMAS's single-contributor bypass (v2.14.1 §10.5/§10.6) is one approach among several established patterns for solo-operator AI development governance. The patterns I surveyed split into three families: (1) lightweight discipline patterns (decision logs, model pinning, policy-as-code), (2) AI-augmented review patterns (CodeRabbit, PR-Agent, Copilot review for solo OSS), and (3) tiered-governance patterns (different rigor for prototype vs. production).

**Surveyed patterns**:

- **Tiered governance** — a solo developer's "governance-assistant" pattern with three tiers: Quick (prototypes / weekend projects), Standard (client deliverables / production), Enterprise (regulated data) ([Building token-efficient AI workspace](https://selltinfoil.com/blog/building-token-efficient-ai-workspace/), November 2025, retrieved 2026-04-30). The pattern explicitly recognizes that governance is not binary and that projects evolve up the tiers.
- **Decision-logging-first** — every AI inference produces a structured immutable record (model, input hash, output summary, confidence, policy version, timestamp); pin model versions; output auditing; policy-as-code in YAML in version control ([Build AI governance into your solo dev stack](https://dev.to/software_mvp-factory/build-ai-governance-into-your-solo-dev-stack-a-practical-workshop-2feg), February 2026, retrieved 2026-04-30). Pattern claim: "decision logging covers 60% of governance requirements." Useful as a baseline.
- **AI-as-first-reviewer for solo OSS** — CodeRabbit (free for open source), PR-Agent, Copilot code review; the maintainer remains the human-in-loop second reviewer. CodeRabbit's free OSS tier includes 200 files/hour and 3 back-to-back reviews followed by 4/hour ([CodeRabbit OSS guide](https://dev.to/rahulxsingh/coderabbit-for-open-source-ai-code-reviews-for-oss-projects-134i), March 2026, retrieved 2026-04-30). This is a partial substitute for AMAS's "second human reviewer" requirement but does not satisfy the principle that the reviewer be independent.
- **Inject-standards-into-contributors'-AI-tools** — for OSS maintainers, CLAUDE.md and AGENTS.md communicate project conventions to whatever AI tool a contributor uses; the matplotlib incident is a cautionary tale where automated AI publishing without a human review gate caused real harm ([OSS maintainers AI standards injection](https://nonconvexlabs.com/blog/oss-maintainers-can-inject-their-standards-into-contributors-ai-tools), retrieved 2026-04-30). AMAS's surface-file synchronization is consistent with this pattern.
- **Bot-identity separation** — solo developers running multiple AI agents create per-agent GitHub identities so audit trails and branch protections work correctly (Q10).

**Comparison to AMAS bypass mechanism**: AMAS v2.14.1 §10.5/§10.6 specifies a single-contributor bypass that allows the solo developer to merge their own code under specific conditions while preserving the rest of the framework. The literature broadly endorses this kind of accommodation: solo-operator governance should not require a second human reviewer that doesn't exist. AMAS's approach is more elaborate than typical solo-dev guides, which fits a framework that scales to multi-contributor projects.

**Is AMAS's solo-operator bypass overcomplicated, undercomplicated, or appropriately calibrated?**

- **Possibly somewhat over-complicated** for the lightest project tier (prototypes / experiments / weekend projects). Adopters at this tier typically want decision-log + model-pin + policy-as-code, not a full framework adoption.
- **Appropriately calibrated** for the middle tier (production projects with real customers). The bypass mechanism's structural separations (Architect identity, claim verification, CODEOWNERS exclusion) match what real solo-operator production projects need.
- **Under-specified** for the heavy tier (regulated data, healthcare, finance). Solo developers in regulated domains may want more than AMAS provides — full AI-decision audit trails, model-version pinning enforced, blocked egress for AI inference. AMAS could reference the heavy-tier patterns from the literature without absorbing them.

### Key sources

- Building token-efficient AI workspace — https://selltinfoil.com/blog/building-token-efficient-ai-workspace/ (November 2025, retrieved 2026-04-30): tiered-governance pattern from a solo dev
- Build AI governance into solo dev stack — https://dev.to/software_mvp-factory/build-ai-governance-into-your-solo-dev-stack-a-practical-workshop-2feg (February 2026, retrieved 2026-04-30): decision-logging-first pattern
- OSS maintainer AI standards injection — https://nonconvexlabs.com/blog/oss-maintainers-can-inject-their-standards-into-contributors-ai-tools (retrieved 2026-04-30): cautionary case + CLAUDE.md/AGENTS.md pattern
- CodeRabbit for OSS — https://dev.to/rahulxsingh/coderabbit-for-open-source-ai-code-reviews-for-oss-projects-134i (March 2026, retrieved 2026-04-30): AI-as-first-reviewer pattern

### Recommendations for v3

1. v3 should **explicitly position the solo-operator bypass as the middle of three tiers**, with light-tier guidance (decision logs, model pinning) and heavy-tier guidance (full audit trails) referenced rather than absorbed
2. v3 prose should reference the matplotlib incident or similar as a cautionary tale for over-automation in solo / OSS contexts
3. v3 should recommend **AI-as-first-reviewer** as the canonical solo-operator review pattern: a different AI surface than the one that produced the change reviews it, with the solo human reviewing the output of both
4. v3 should retain the bypass mechanism but add a **brief commentary** that the mechanism is calibrated to production-tier projects and may be over-elaborate for prototypes; adopters can simplify in their own ADR
5. Consider adding a **lightweight starter** option in the reference impl for prototype-tier solo developers — minimal Actions, no reference-impl scaffolding, documentation-only AMAS adoption

### Evidence quality

**Settled** for the existence of multiple patterns. **Contested** for "best" pattern for solo operators; the literature is opinionated and inconsistent. **Settled** for the principle that solo-operator governance must accommodate the absence of a second human reviewer.

---

## Q12. Vendor-neutral AI capability taxonomies

### Findings summary

The transition plan defines a capability-class taxonomy (with claimed-action-honesty and dual-signal-handling as AMAS-specific dimensions). Established industry / academic taxonomies cover overlapping but not identical dimensions. AMAS adds genuinely new dimensions; aligning on terminology where possible and clearly flagging AMAS-specific dimensions is the right approach.

**Established taxonomies**:

- **HELM (Holistic Evaluation of Language Models)** — Stanford CRFM. Multi-dimensional: scenarios × metrics × capabilities. The metrics include Accuracy, Calibration, Robustness, Fairness, Bias, Toxicity, Efficiency ([Galileo LLM benchmarks summary](https://galileo.ai/blog/llm-benchmarks-categories), retrieved 2026-04-30). HELM is the most comprehensive multi-dimensional evaluation framework.
- **MMLU (Massive Multitask Language Understanding)** — 57 subjects benchmark; tests knowledge breadth and zero-/few-shot learning
- **BIG-Bench** — 200+ tasks; the broadest benchmark by task count, including reasoning, multilingual, and creative tasks
- **GSM8K, MATH** — arithmetic and mathematical reasoning benchmarks
- **HumanEval, MBPP** — code generation benchmarks
- **TruthfulQA** — calibrated honesty / factuality benchmark
- **SWE-bench Verified** — software engineering tasks; OpenHands reaches 72% with Claude 4
- **Industry comparison resources**: Artificial Analysis, LLM-Stats, leaderboards with capability dimensions
- **Anthropic / OpenAI / Google model cards** — vendor-published capability descriptions; not standardized across vendors

**AMAS-specific dimensions worth defending**:

- **Claimed-action-honesty** — does the model accurately report what it actually did? This dimension is not directly measured by HELM, MMLU, BIG-Bench, GSM8K, HumanEval, or TruthfulQA. AgentHallu's tool-use-hallucination sub-categories (Q8) are the closest published analog, but AgentHallu measures detection by external judges, not the model's own honesty about its actions.
- **Dual-signal-handling** — can the model handle two inputs (e.g., a task instruction plus a piece of context) without one corrupting the other? Closest analog: **prompt injection robustness benchmarks** (SubVersa, AgentDojo). Worth aligning on terminology.

**AMAS dimensions that should align with industry**:

- AMAS's "reasoning" capability could explicitly reference HELM's reasoning dimension or BBH (Big Bench Hard) for benchmark grounding
- AMAS's "code generation" or "code execution" capability could reference SWE-bench Verified
- AMAS's "calibration" or "uncertainty" capability could reference HELM's Calibration metric

**Why HELM-only alignment is insufficient**: HELM measures *evaluation outputs* (does the model do X correctly?). AMAS measures *operating role assignments* (which surface should be the Reviewer for this project?). These are different concerns. AMAS's taxonomy is functional (what the model is asked to do in the AMAS workflow), HELM's is empirical (how accurately the model performs on a benchmark). v3 should not collapse the two.

### Key sources

- Galileo: LLM benchmark categories — https://galileo.ai/blog/llm-benchmarks-categories (March 2025, retrieved 2026-04-30): multi-benchmark survey
- Adaline: Modern LLM evaluation frameworks — https://www.adaline.ai/blog/evaluating-large-language-models (March 2026, retrieved 2026-04-30): HELM, MMLU, BIG-Bench in detail
- HELM benchmark notes — https://www.shedge.com/metrics/llm-benchmarks/helm-benchmark/ (retrieved 2026-04-30): HELM's top-down approach
- Artificial Analysis coding agents — https://artificialanalysis.ai/agents/coding (retrieved 2026-04-30): industry-comparison resource

### Recommendations for v3

1. v3 should **align AMAS capability dimensions with HELM where they overlap** and **explicitly flag AMAS-specific dimensions where they don't**. The Tool Capability Model appendix should have an "alignment with industry taxonomies" sub-section.
2. v3 should claim **claimed-action-honesty** and **dual-signal-handling** as AMAS-specific dimensions; the survey supports the claim that these aren't covered by HELM, MMLU, BIG-Bench, etc.
3. v3 prose should reference **HELM, MMLU, SWE-bench, AgentHallu** as anchors that adopters can use when scoring surfaces against AMAS dimensions
4. v3 should warn against **collapsing functional capability dimensions (what role is this surface assigned?) with empirical capability dimensions (how well does this surface perform on a benchmark?)** — they are related but not identical
5. Consider proposing a small set of **AMAS-specific evaluation prompts** for claimed-action-honesty that adopters can run; this would give the dimension empirical grounding without requiring a new benchmark suite

### Evidence quality

**Settled** for the existence and authority of HELM, MMLU, BIG-Bench, etc. **Settled** for the gap (AMAS dimensions are not all covered by industry benchmarks). **Unknown** for whether HELM or another framework will absorb claimed-action-honesty in the future; it's plausible but not visible at the moment.

---

## Risks to AMAS v3 design (risk register)

The following risks are surfaced explicitly per the handoff's required-output format. Each entry: description / likelihood / impact / mitigation candidate.

### R-001 — MCP STDIO command-injection vulnerability propagates to AMAS adopters

**Description**: The OX Security advisory of April 15, 2026 establishes that the MCP STDIO transport executes commands regardless of whether the spawned process is actually a valid MCP server. Anthropic has declined to patch at the protocol level. AMAS adopters using STDIO MCP servers (which is the default configuration for `.mcp.json`) inherit this exposure and may not realize it.

**Likelihood**: high (the vulnerability is disclosed, exploitable, and unpatched at protocol level)
**Impact**: high (RCE on adopter's machine; sensitive credentials, repo contents, and chat histories exposed)

**Mitigation candidates**:
- v3 Tool Inventory must explicitly warn about STDIO command injection and recommend HTTP+OAuth where possible
- Tool Inventory schema must add `transport_mode`, `auth_mechanism`, `sandbox_required` fields
- Reference impl should ship a starter `.mcp.json` template that uses HTTP transport for non-trivial tools
- An AMAS Action should validate MCP configurations against a baseline (e.g., reject unsigned commands, require allowlist for STDIO)
- ADR-015 should record AMAS's posture toward this advisory explicitly

### R-002 — Adapter pack staleness across surface changes

**Description**: All six receiving surfaces (Q1) shipped meaningful changes in the last six months. Adapter packs that lock to specific product behaviors will go stale rapidly. The transition plan recognizes this (user fork #3) but the appendix structure does not yet enforce a freshness discipline.

**Likelihood**: high (every product changes monthly or faster)
**Impact**: medium (adopters following stale adapters get incorrect behavior)

**Mitigation candidates**:
- Each adapter pack header includes a `last_validated_on` date and the AMAS version it was authored against
- An AMAS Action could ping adapter pack URLs (the canonical vendor doc URLs) and warn when content has changed
- v3 should publish adapter packs as separate versioned releases so adopters can pin
- v3 should explicitly disclaim that adapter packs are reference implementations, not canonical guarantees of vendor behavior

### R-003 — MCP authorization spec evolution outpaces AMAS Tool Inventory schema

**Description**: The MCP authorization spec is at draft state and has gone through three major revisions. AMAS Tool Inventory fields aligned to the November 2025 spec may not match a future spec.

**Likelihood**: medium (spec is stabilizing but still evolving)
**Impact**: medium (adopters who fully implement against the current spec are unlikely to be wrong, but interfaces may shift)

**Mitigation candidates**:
- Tool Inventory schema should reference spec version explicitly (e.g., `mcp_spec_version: "2025-11-25"`)
- v3 should commit to tracking the spec and shipping schema updates as minor versions
- v3 should adopt MUST-level requirements as canonical, leave SHOULD-level requirements as appendix recommendations to allow flexibility

### R-004 — Cursor and other phantom-action surfaces under-listed in transition plan

**Description**: The transition plan lists Codex as the highest-evidence phantom-action surface. Q1 found community-level evidence that Cursor background agents also exhibit phantom-action behavior, and Cursor 3.2 just shipped multi-agent fanout that may amplify the problem.

**Likelihood**: medium-high (Cursor evidence is community-level, not vendor-disclosed)
**Impact**: medium (adopters using Cursor without phantom-action vigilance miss real failure modes)

**Mitigation candidates**:
- v3 prose should list Cursor (background agents and `/multitask`) alongside Codex as a phantom-action-prone surface
- The `claimed-action-verification.yml` Action should explicitly cover Cursor branch-push verification
- Adapter pack for Cursor should include phantom-action discussion

### R-005 — June 1, 2026 Copilot billing change creates planning friction for AMAS adopters

**Description**: Starting June 1, 2026, GitHub Copilot code review will consume GitHub Actions minutes, in addition to the existing premium-request units. Adopters running heavy Copilot review on private repos will see new costs. AMAS prose may need to advise.

**Likelihood**: certain (announced)
**Impact**: low-medium (affects costs, not capability)

**Mitigation candidates**:
- AMAS GitHub Copilot adapter should mention the billing change explicitly
- v3 cost-considerations appendix could include a brief section on AI-tool Actions cost planning
- v3 prose should not depend on Copilot review being free / unmetered

### R-006 — Context7 framing in v2.14.1 may overspecify the documentation-MCP choice

**Description**: v2.14.1 emphasizes Context7 as the canonical doc-retrieval MCP. The 2026 alternatives ecosystem is broader, and Context7 has documented limitations including coverage of very-recent libraries and a contested benchmark accuracy.

**Likelihood**: medium (depends on v3 prose decisions)
**Impact**: low-medium (vendor lock-in framing, missed benefits of alternatives)

**Mitigation candidates**:
- v3 should de-emphasize Context7-as-canonical and instead establish the principle (ground LLM code in current docs); list Context7 as one option
- Add a "choosing a documentation MCP" sub-section in the appendix

### R-007 — Empirical claim about multi-surface review is qualitative, not quantified

**Description**: AMAS v2.14.1 §24.2(b) makes a strong claim that single-surface review is insufficient. The supporting evidence is qualitative (audits, surveys, case studies). No published effect-size number quantifies the marginal benefit of multi-surface review.

**Likelihood**: medium (claim is defensible but not yet quantified)
**Impact**: low-medium (skeptical adopters may want effect sizes; AMAS doesn't have them)

**Mitigation candidates**:
- v3 prose should frame the claim as "supported by multiple converging lines of evidence" rather than as a quantified effect size
- v3 should reference the specific evidence (Bosu et al., Sadowski et al., "Clawed and Dangerous") as footnotes
- Consider commissioning an empirical study within UPCDS or a similar reference project to quantify; flag this as future work

### R-008 — AMAS phantom-action category list (4 items) is non-exhaustive vs. published taxonomies

**Description**: AMAS's four claim categories (commit, file, follow-up artifact, identifier-pattern) cover GitHub-canonical examples but miss claimed test execution, claimed external API calls, and other tool-use hallucinations from the academic literature.

**Likelihood**: medium (the taxonomy is a reasonable subset, not wrong)
**Impact**: low-medium (adopters extending AMAS to non-GitHub Reviewer surfaces will need extension)

**Mitigation candidates**:
- v3 should reframe the four categories as **canonical examples**, not the closed list
- v3 should add at least two more examples (claimed test execution, claimed API call)
- v3 should reference MIRAGE-Bench / AgentHallu / Tool Receipts taxonomies for adopters who want deeper coverage

### R-009 — Surface-file sync mechanism does not address content correctness

**Description**: `surfaces.yml` + manifest-sync Action detects file presence and structural drift but not content correctness. Adopters may over-rely on it as a quality signal.

**Likelihood**: medium (the failure mode is silent)
**Impact**: low-medium (adopters mistake structural conformance for content correctness)

**Mitigation candidates**:
- v3 prose should explicitly state what surface-file sync does NOT promise
- Consider adding **manifest checksums** so content drift can also be detected
- Document a separate review pattern for content correctness

### R-010 — AMAS solo-operator bypass may be over-complicated for prototype-tier projects

**Description**: Q11 found that solo-operator governance has at least three tiers (prototype / production / regulated). AMAS's bypass mechanism is calibrated to the production tier and may feel heavy for prototypes.

**Likelihood**: medium (depends on adopter project shape)
**Impact**: low (adopters can simplify in their own ADR)

**Mitigation candidates**:
- v3 should explicitly call the bypass "production-tier solo-operator" calibration
- Consider shipping a lightweight starter for prototype-tier adopters
- Document the tier-up pattern (when to graduate from prototype to production)

### R-011 — Capability dimensions diverge from industry benchmarks in non-trivial ways

**Description**: AMAS's capability dimensions include claimed-action-honesty and dual-signal-handling, which are not covered by HELM / MMLU / BIG-Bench. Adopters used to industry benchmarks may not understand AMAS's dimensions.

**Likelihood**: medium
**Impact**: low (adopters can learn the difference; v3 prose can clarify)

**Mitigation candidates**:
- v3 should align on industry terminology where possible and explicitly flag AMAS-specific dimensions
- Tool Capability Model appendix should reference HELM, MMLU, SWE-bench as anchors
- AMAS-specific evaluation prompts for claimed-action-honesty would help adopters score surfaces

### R-012 — Reusable workflow distribution friction at scale (GitHub 2026 roadmap evolution)

**Description**: The GitHub Actions 2026 security roadmap will change implicit secret inheritance, immutable-release publishing, and scoped-secret behavior. AMAS Actions distributed before these changes ship will need re-validation.

**Likelihood**: high (announced)
**Impact**: medium (AMAS may need to re-publish Actions with updated security posture)

**Mitigation candidates**:
- v3 ships Actions with explicit secret passing (no `secrets: inherit`)
- v3 plans for immutable release semantics from the start
- v3 should commit to a tracking discipline for the GitHub roadmap and re-publish as needed

---

## Notes on this deliverable

**Coverage**: 12 questions addressed; one P0 finding flagged; risk register with 12 entries.

**What I marked "evidence insufficient" or "unknown"**: AWS Bedrock Agents and Azure AI Studio governance details (Q5) — I did not find sufficient public documentation to compare governance shape rigorously. Quantified effect sizes for multi-surface review benefit (Q7). Vendor IdP compliance with the full MCP RFC stack beyond Ping Identity (Q2).

**What I did not recommend changing**: the user-fork decisions (solo-operator bypass, surface-file sync as canonical, adapters in tool appendix, Context7 framing, v3 scope discipline, project-type appendices). These were user-confirmed in the transition plan; this research deliverable surfaces refinements, not reversals.

**Citation discipline**: all claims sourced to URL + retrieval date; no quotes 15+ words; one direct quote per source maximum (and most sources paraphrased rather than quoted). No song lyrics, poems, or reproduced article paragraphs.

End of deliverable.
