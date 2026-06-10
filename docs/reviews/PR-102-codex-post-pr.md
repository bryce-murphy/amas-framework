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

---

## Pass-2 — three-endpoint poll record (post fix-up `e929889`)

- Poll timestamp (UTC): 2026-06-10T18:41:43Z (review submitted) / polled ~2026-06-10T18:45:00Z
- Reviewed commit: e92988966a3c82bcf3fcedaf9f716b579db9bf46

**Endpoint 1 — `pulls/102/reviews`**: 2 entries from `chatgpt-codex-connector[bot]` — pass-1 (18:13:21Z on b795b381a0, already recorded above) + pass-2 (18:41:43Z on e92988966a) — state `COMMENTED`. Pass-2 body: boilerplate Codex header. Substantive findings via line comments (Endpoint 3).

**Endpoint 2 — `issues/102/comments`**: 2 owner invocation entries only (18:10:31Z, 18:39:15Z). No Codex substantive content.

**Endpoint 3 — `pulls/102/comments`**: 3 line comments total — pass-1 P2 (18:13:21Z, already recorded) + 2 new pass-2 P2 comments (18:41:43Z on e92988966a). Verbatim below.

§7.4 settling-period satisfied (substantive Endpoint-3 content present on the re-review commit).

## Codex post-PR pass-2 output (verbatim)

### Review object (Endpoint 1) — state: COMMENTED, commit e92988966a

> ### 💡 Codex Review
>
> Here are some automated review suggestions for this pull request.
>
> **Reviewed commit:** `e92988966a`
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

### Line comment 1 (Endpoint 3) — `docs/reviews/PR-102-codex-pre-commit.md` line 114

Badge: `P2-yellow`

> **Correct the stale WS3a no-residual validation**
>
> On commit `c387f74`, this validation note is false: `git grep -n "dual-signal" -- '*.md'` still returns the intentional `github-reference.md` breadcrumb plus many tracked Markdown hits in the new TASK-0054 handoff/review-context and historical docs/prompts. Because this file is used as review evidence for the predicate-hygiene cycle, leaving a broad "no tracked Markdown occurrence" assertion here can cause downstream reviewers to accept a phantom validation instead of the intended narrower canonical-surface check.

### Line comment 2 (Endpoint 3) — `docs/reviews/PR-102-codex-pre-commit.md` line 53

Badge: `P2-yellow`

> **Fix the Claim-artifact-parity grep count**
>
> The stated verification command does not match the tree: on `c387f74`, `grep -c "Claim-artifact-parity" core.md` returns `3`, not `2`, because the term appears in the heading, the opening paragraph, and the unifying-rule paragraph. This makes the review-context evidence internally false in the same cycle that is adding claim-artifact-parity checks, so any consumer rerunning the documented command will see a mismatch.

## Builder verification of pass-2 findings

**Pass-2 Finding 1 (line 114 — stale verbatim WS3a note):** The flagged line is in the pass-1 Codex verbatim output absorption section (`## Codex desktop pre-commit output absorption` → `Validation notes`), which states: "WS3a verifies clean: no tracked Markdown occurrence of `dual-signal` remains; the `github-reference.md` §6.3 breadcrumb uses 'formerly labeled `dual-signal`' as the single legacy breadcrumb." This is the Codex pass-1 verbatim output — a historical append-only record. The corrected per-surface claim is in Claim 2 (Builder claims section), which was corrected at fix-up `e929889`. Whether the verbatim historical note requires annotation or is appropriately preserved as-is under §23.6.5 suppression is Architect's adjudication.

**Pass-2 Finding 2 (line 53 — Claim-artifact-parity count): confirmed.** `grep -c "Claim-artifact-parity" core.md` returns **3**, not 2. Occurrences: line 830 (heading), line 832 (opening paragraph), line 840 (unifying-rule paragraph). Claim 5 in the review-context states `returns \`2\` (heading + body occurrence)` — this is false; the count is 3 and the description "heading + body occurrence" only accounts for 2. **Finding confirmed accurate; live claim surface (Builder Claims section).**

## Pass-2 adjudication (Architect — 2026-06-10)

**Comprehensive live-claim audit (§24.7 / §23.6.3 reference-verification on evidence file):**

| Claim | Command(s) | Actual output | Status |
|---|---|---|---|
| C1 (diff-stats) | `git diff --staged --shortstat` | N/A — historical staged-tree snapshot; describes pre-commit state before b795b38; not re-runnable against committed tree | N/A (historical) |
| C2a | `grep -n "dual-signal" core.md` | no matches | ✓ |
| C2b | `grep -n "dual-signal" usage-guide.md` | no matches | ✓ |
| C2c | `grep -n "dual-signal" github-reference.md` | 1 match at line 289 (§6.3 breadcrumb) | ✓ |
| C3 | `grep "ADR-008 D6" core.md` | 1 line (line 610) containing both strings — NOT "two lines" | ✗ → FIXED |
| C4a | `grep "framework_version: 3.0.4" core.md ...` | 4 lines (one per file) | ✓ |
| C4b | `grep "v3.0.4" README.md` | 1 line containing `**v3.0.4**` | ✓ |
| C4c | `grep "canonical_version: 3.0.4" .amas/surfaces.yml` | 4 lines | ✓ |
| C4d | `grep "v3.0.4" AGENTS.md CLAUDE.md` | 2 lines (one per file) | ✓ |
| C4e | `grep "3.0.3" core.md ... CLAUDE.md` | README.md Adopter migration note only | ✓ |
| C5a | `grep -n "§24.7" core.md` | line 830: `### §24.7. Claim-artifact-parity` | ✓ |
| C5b | `grep -c "Claim-artifact-parity" core.md` | **3** (heading l.830, opening paragraph l.832, unifying-rule l.840) — NOT "2" | ✗ → FIXED |
| C6 | `grep "TASK-0053 (PR-100)" core.md` | 1 line containing `Subsequent cross-cycle reinforcement at TASK-0053 (PR-100)` | ✓ |
| C7a | `grep "not an Action-maintained mirror of frontmatter" core.md` | 1 line (§13.2 sentence) | ✓ |
| C7b | `grep "Body.*- Status.*vs frontmatter" templates/handoff-template.md` | 1 line (Usage notes bullet) | ✓ |
| C8a | `head -15 docs/handoffs/TASK-0054-predicate-hygiene.md \| grep "^status:"` | `status: active` | ✓ |
| C8b | `grep "^- Status:" docs/handoffs/TASK-0054-predicate-hygiene.md` | `- Status: drafted` | ✓ |
| C9a | `grep "v3.0.4" AGENTS.md CLAUDE.md` | 2 lines (one per file) | ✓ |
| C9b | `grep "3.0.3" AGENTS.md CLAUDE.md` | no matches | ✓ |

**Two live-claim false assertions found and corrected (path-(a)):**

- **Claim 3** (`grep "ADR-008 D6" core.md`): stated "returns two lines" — actual is one line (line 610) containing both target strings in the same §18.4 paragraph. Corrected to "returns one line (line 610) containing both..."
- **Claim 5b** (`grep -c "Claim-artifact-parity" core.md`): stated "returns `2` (heading + body occurrence)" — actual is `3` (heading l.830, opening paragraph l.832, unifying-rule paragraph l.840). Corrected per Codex pass-2 P2 finding and Architect path-(a) routing.

**Finding 1 (pass-1 verbatim WS3a note) — path-(β), annotation added:**

Line 114 is in the Codex pass-1 verbatim output absorption section — historical record preserved unedited per PMN-002 (a) verbatim convention and §23.6.5 append-only suppression clause. An editorial annotation was added to the author-controlled pass-1 adjudication subsection of `docs/reviews/PR-102-codex-pre-commit.md` noting the inaccuracy and the correction path; the verbatim quote itself is unchanged. If this annotation is re-raised at pass-3, it is subsequent-same-class and will be accepted at merge per §24.6 (B.i) Stop-Iteration framework (reach trajectory: pre-arm activated at reach 2→3).
