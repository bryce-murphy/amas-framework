---
status: drafted
---

# PR-102 Codex post-PR review

## Metadata

- PR: PR-102
- Branch: fix/task-0054-predicate-hygiene
- Cycle: TASK-0054
- Linked handoff: docs/handoffs/TASK-0054-predicate-hygiene.md
- Linked pre-commit review-context: docs/reviews/PR-102-codex-pre-commit.md
- Status: drafted
- Post-PR poll timestamp (UTC): 2026-06-10T18:13:21Z (review submitted) / polled ~2026-06-10T18:15:00Z
- Reviewed commit: b795b381a0d48d1dc0832f5fbc9ee9b32df192cc

## Three-endpoint poll record (per core.md §8.1.1.1)

**Endpoint 1 — `pulls/102/reviews`**: 1 entry from `chatgpt-codex-connector[bot]` — state `COMMENTED`, submitted 2026-06-10T18:13:21Z, on commit `b795b381a0d48d1dc0832f5fbc9ee9b32df192cc`. Body: boilerplate Codex header + details block ("Here are some automated review suggestions…"). Substantive findings delivered via line comments (Endpoint 3).

**Endpoint 2 — `issues/102/comments`**: 1 entry from `bryce-murphy` — owner's `@codex review` invocation comment (2026-06-10T18:10:31Z). No Codex substantive content on this endpoint.

**Endpoint 3 — `pulls/102/comments`**: 1 line comment from `chatgpt-codex-connector[bot]` — on `docs/reviews/PR-102-codex-pre-commit.md` lines 35–36, submitted 2026-06-10T18:13:21Z. This is the substantive finding; captured verbatim below.

All three endpoints polled after Codex's review timestamp; no additional comments detected. §7.4 settling-period satisfied (single endpoint carries substantive verdict; other two endpoints stable-empty for Codex content).

## Codex post-PR output (verbatim)

### Review object (Endpoint 1) — state: COMMENTED

> ### 💡 Codex Review
>
> Here are some automated review suggestions for this pull request.
>
> **Reviewed commit:** `b795b381a0`
>
> <details><summary>ℹ️ About Codex in GitHub</summary>
>
> [Your team has set up Codex to review pull requests in this repo](https://chatgpt.com/codex/cloud/settings/general). Reviews are triggered when you
> - Open a pull request for review
> - Mark a draft as ready
> - Comment "@codex review".
>
> If Codex has suggestions, it will comment; otherwise it will react with 👍.
>
> Codex can also answer questions or update the PR. Try commenting "@codex address that feedback".
>
> </details>

### Line comment (Endpoint 3) — `docs/reviews/PR-102-codex-pre-commit.md` lines 35–36

Badge: `P2-yellow`

> **Replace the false zero-residual grep claim**
>
> This validation claim is false as written: running the exact `grep -r "dual-signal" --include="*.md" .` predicate on this commit still returns the intentional `github-reference.md` legacy breadcrumb, historical PMN/prompt hits, and this new TASK-0054 handoff's own WS3a descriptions. Because this review-context file is used as verification evidence for the predicate-hygiene cycle, the zero-residual assertion creates a phantom validation record; narrow the command to the intended canonical surfaces or list the expected historical/breadcrumb residuals instead.

## Builder verification of finding

Running `grep -r "dual-signal" --include="*.md" .` on the committed tree returns results in:
- `github-reference.md` — intentional legacy breadcrumb at §6.3 ("formerly labeled `dual-signal`")
- `docs/handoffs/TASK-0054-predicate-hygiene.md` — WS3a scope descriptions ("dual-signal → three-endpoint rename")
- `docs/reviews/PR-102-codex-pre-commit.md` — Claim 2 grep pattern text + Reviewer focus item 2 + kickoff block
- `docs/handoffs/TASK-0052-three-endpoint-canonical-reconciliation.md` — prior-cycle HOLD references
- `docs/reviews/PR-98-codex-pre-commit.md` — prior-cycle review-context scope-protection clause
- `docs/post-merge-notes/PMN-*.md` — historical PMN documents referencing prior canonical name
- `prompts/research-deliverable.md` — framework dimensions reference

**Finding confirmed accurate.** The claim at `docs/reviews/PR-102-codex-pre-commit.md` lines 35–36 as written is false for the broad `--include="*.md" .` scope. The canonical-law surfaces (core.md, github-reference.md, usage-guide.md) are free of "dual-signal" as a live label — but github-reference.md §6.3 retains the intentional legacy breadcrumb ("formerly labeled `dual-signal`"), and the handoff + review-context themselves use the term descriptively.

**Substantive content (WS3a) is correct**: the four live "dual-signal" label sites in the canonical trio were renamed to "three-endpoint" at `b795b38`. The Codex finding is documentary — it flags an over-broad grep claim in the pre-commit review-context, not an error in the canonical content itself.

## Adjudication (Architect — 2026-06-10)

- **P2 finding** (`docs/reviews/PR-102-codex-pre-commit.md` lines 35–36): path-(a) class-sweep. Finding accurate and on-thesis — a false "grep returns empty" validation claim is a §24.7 claim-artifact-parity violation inside the cycle that canonicalizes §24.7.

**Route: class-sweep, not instance-fix.** The false broad-grep-empty assertion appeared at three live claim surfaces:
  1. `docs/reviews/PR-102-codex-pre-commit.md` Claim 2 (flagged locus) — corrected to per-surface statements (core.md 0, usage-guide.md 0, github-reference.md 1 breadcrumb) with breadcrumb explanation.
  2. `docs/handoffs/TASK-0054-predicate-hygiene.md` — §3 step record + §5 self-review record assert "zero occurrences in any .md file"; these are append-only historical snapshots per §23.6.5 suppression clause — NOT edited. No live validation-evidence section asserts the broad grep.
  3. PR-102 body Validation section — corrected to per-surface statement in the body file; `gh pr edit` applied.

**§24.5 multi-surface-pipeline note**: the false zero-residual grep claim originated at the Gate A self-review presentations and survived both pre-commit Codex passes (pass-1 and pass-2) without being flagged. Post-PR Codex caught it. This is the §24.5 multi-surface review pipeline functioning as designed — sequential independent passes catching what earlier passes missed. It is also the strongest in-cycle empirical instantiation of §24.7: the claim-artifact-parity cycle's own evidence file carried a claim-artifact-parity defect.

**Origination note**: pre-commit self-review ran the broad grep and observed zero residuals at self-review time — which was accurate at that moment (before the handoff and review-context files were written). The claim was then forward-projected as a verifiable assertion ("returns no output"), which became false once the handoff + review-context files (which describe the rename) were added to the tracked tree. The lesson (candidate for §10 ledger): pre-commit "grep empty" validations should run the literal command on the staged tree and read its output, not assert emptiness from substantive intent.
