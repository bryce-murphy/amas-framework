---
status: drafted
---

# PR-95 Codex desktop pre-commit review — TASK-0051 surface-version-sync-check materialization

## Metadata

- PR: PR-95
- Branch: feat/task-0051-surface-version-sync-check
- Cycle: TASK-0051 (surface-version-sync-check Action materialization — first v3.1 Batch-P4 Action)
- Linked handoff: docs/handoffs/TASK-0051-surface-version-sync-check.md
- Status: drafted
- Codex desktop session timestamp (UTC): TBD

## Builder claims to verify

All commands run from repo root at staged-tree state (`git add -A` applied). Reliable primitives only (sed / grep -nE; NEVER awk over a `§`-bearing range — awk silently fails the UTF-8 `§` byte range, per PR-92 [C1]). RELAY-ORDERING: this is the **pre-commit** pass; the binding post-PR re-review is invoked only AFTER PR-open + any finding-addressing push.

1. **D1 — Action materialized; `# template_version` STAYS 3.0.0 (NOT bumped).**
   - bash: `grep -cE '^# template_version: 3\.0\.0' actions/surface-version-sync-check.yml` -> `1`.
   - bash: `grep -cE '^# template_version: 3\.0\.1' actions/surface-version-sync-check.yml` -> `0`.
   - bash: `grep -c 'will author this workflow' actions/surface-version-sync-check.yml` -> `0` (stub body gone).
   - bash: `grep -cE '^name: surface-version-sync-check$' actions/surface-version-sync-check.yml` -> `1`.
   - Class: D1 Architect-locked correction (§17.5 stub->fill keeps template_version; greenfield/retrofit/upgrade precedent).

2. **D2 — `.amas/surfaces.yml` present; 5 entries; self-entry 3.0.0; surfaces_manifest 3.0.1; linked-pr-fix-up excluded.**
   - bash: `grep -cE '^[[:space:]]*-[[:space:]]+name:' .amas/surfaces.yml` -> `5`.
   - bash: `grep -A2 'name: surface-version-sync-check' .amas/surfaces.yml | grep -c 'template_version: 3.0.0'` -> `1` (self-entry equals the Action marker -> no self-fail; `-A2` because `path:` sits between `name:` and `template_version:` in the manifest structure).
   - bash: `grep -A2 'name: surfaces_manifest' .amas/surfaces.yml | grep -c 'template_version: 3.0.1'` -> `1` (same `-A2` rationale).
   - bash: `grep -c 'name: linked-pr-fix-up' .amas/surfaces.yml` -> `0` (excluded; no template-of-record).
   - Class: D2 coverage + circularity guard.

3. **D3 — operational advisory workflow present; advisory (not a required status check).**
   - bash: `test -f .github/workflows/surface-version-sync-check.yml && echo present` -> `present`.
   - bash: `grep -ci 'advisory' .github/workflows/surface-version-sync-check.yml` -> `>=1`.
   - Class: D3 §6.2 canonical-source -> operational mirror; anti-scope F3 (no required-status-check).

4. **D4 — §7.1 example AGENTS.md `agents: [codex]` (Codex PR-92 [C2] resolution).**
   - bash: `grep -c 'agents: \[claude, codex\]' github-reference.md` -> `0`.
   - bash: `grep -c 'agents: \[codex\]' github-reference.md` -> `1`.
   - Class: D4 = resolution of carried-forward Codex PR-92 [C2] (P3).

5. **D5 — stale-version negative fixture present; Action FAILs on it, PASSes on real manifest (live-run).**
   - bash: `test -f actions/fixtures/surface-version-sync-check/stale-manifest.yml && echo present` -> `present`.
   - bash: `grep -c 'template_version: 2.14.1' actions/fixtures/surface-version-sync-check/stale-manifest.yml` -> `1` (deliberately stale entry).
   - LIVE-RUN (Builder, authoring): the Action check step, run with `AMAS_SURFACES_MANIFEST=actions/fixtures/surface-version-sync-check/stale-manifest.yml`, emits `[FAIL] AGENTS.md: 2.14.1 != 3.0.0 (stale)` + `[ OK ] CLAUDE.md` and exits 1; run against `.amas/surfaces.yml` emits 5x `[ OK ]` and exits 0.
   - Class: D5 negative-path proof (currency comparison flags drift, selectively).

6. **D6 — currency bump v3.0.1 -> v3.0.2 (trio frontmatter x3 + in-development markers); v3.0.0-published preserved; no "published" on v3.0.2.**
   - bash: `grep -cE '^framework_version: 3\.0\.2' core.md github-reference.md usage-guide.md` (per file) -> `1` each (3 total).
   - bash: `grep -c 'v3.0.2' README.md AGENTS.md CLAUDE.md` -> `>=1` each (in-development marker bumped).
   - bash: `grep -nE 'v3\.0\.2[^.;]*publish|publish[^.;]*v3\.0\.2' README.md AGENTS.md CLAUDE.md core.md github-reference.md usage-guide.md` -> **no lines** (attachment predicate: "published" never attaches to v3.0.2 — the PR-92 [F1] defect class).
   - bash: `grep -c 'v3.0.0 is published' README.md` -> `>=1`; `grep -c 'latest published release v3.0.0' AGENTS.md CLAUDE.md` -> `1` each (published references preserved).
   - SCOPING: `grep -nE '3\.0\.1' core.md github-reference.md usage-guide.md` -> only `github-reference.md:327/336/342` (the §7.1 worked example; example content, NOT a D6 target).
   - Class: D6 two-concept currency; battery scoped to frontmatter + in-development markers only.

7. **D7 — M-A7 §18.3 37 -> 38; PR-NN literal; span v3.0.2; preamble TASK-0051.**
   - bash: `grep -cE '\+ PR-89 \+ PR-92 \+ PR-NN = 38' core.md` -> `1`.
   - bash: `grep -c 'as of v3.0.2 canonicalization at PR-NN / TASK-0051' core.md` -> `1`.
   - bash: `grep -c '38 consecutive substantive cycles' core.md` -> `1`.
   - bash: `grep -c '= 37' core.md` -> `0` (no stale 37 count).
   - bash: `grep -c 'PR-95' core.md` -> `0` (no phantom numeric PR literal; PR-NN per FX-B).
   - Class: D7 M-A7 INCLUDE (38th); canonical edit (Gate-A re-clear).

8. **D8 — handoff 12-field (PMN-007 HEAD canonical); review-context 1-field.**
   - bash: `head -14 docs/handoffs/TASK-0051-surface-version-sync-check.md | grep -cE '^(task_id|title|pr|branch|linked_predecessor|linked_successor|linked_pr|framework_version_dogfooded|production_target|spec_source|date_authored|status):'` -> `12`.
   - bash: `head -3 docs/reviews/PR-95-codex-pre-commit.md | grep -cE '^status:'` -> `1`.
   - bash: `grep -cE '^linked_pr: PR-[A-Z0-9]+ \(Builder fills with squash SHA post-merge per PMN-001 \(k\)\)$' docs/handoffs/TASK-0051-surface-version-sync-check.md` -> `1` (placeholder form; FX-B substitutes PR-NN -> numeric at PR-open, satisfying the linked-pr-fix-up Action regex).
   - Class: D8 PMN-007 HEAD canonical 12-field; review-template 1-field.

9. **Anti-scope holds.**
   - bash: `git diff --cached --name-only | grep -E '^prompts/'` -> **no lines**.
   - bash: `git diff --cached --name-only | grep -E '^actions/' | grep -v surface-version-sync-check` -> **no lines** (no second Action).
   - bash: `git diff --cached --name-only | grep -E '^\.github/workflows/' | grep -v surface-version-sync-check` -> **no lines**.
   - Class: spec anti-scope (no second Action; no prompts-currency edit; no canonical §6 battery-template repair).

10. **Cumulative-diff-stats (e.1) — by pointer, not pinned.**
    - bash: `git diff --cached --shortstat` and `git diff --cached --numstat` (re-derive live). Pre-D8 staged: `10 files changed, 398 insertions(+), 16 deletions(-)`; cycle artifacts net-additive. No pinned self-volatile total per §23.6.5.
    - Class: §23.6.1.1 (e.1); §23.6.5 reference-volatile-by-pointer.

## Reviewer focus

- **Builder-reconstructed elements** (the full TASK-0051 Builder D1-D8 contract was not in the Builder session; deltas + D1 correction supplied): confirm (a) D1 surface->template-of-record resolution mechanism + mode guard; (b) D3 operational-mirror form; (c) D5 fixture location; (d) D7 "(XXI) cluster" -> §18.3 584/586/588 target; (e) roadmap_status / README [v3.1-planned] hold (not flipped). See handoff §Builder-reconstructed.
- Confirm D1 `# template_version` STAYS 3.0.0 (not 3.0.1) and the manifest self-entry matches it (no Action self-fail).
- Confirm §7.2 honest-proof posture preserved: currency-not-parity; comparison manifest-declared vs template-of-record; optional `.yml`-marker cross-check advisory only.
- Confirm the attachment predicate: "published" does NOT attach to v3.0.2 anywhere (PR-92 [F1] defect class).
- Confirm D6 zero-3.0.1-residual scoping leaves the §7.1 example (327/336/342) intact.
- Anti-scope: no second Action; no prompt edits; no §6 battery-template repair.

## Codex desktop pre-commit kickoff

```
Please review the pending changes on the current branch (feat/task-0051-surface-version-sync-check) per the review-context at docs/reviews/PR-95-codex-pre-commit.md. Working tree is at staged-tree state (git add -A applied); review the staged diff.

Cycle scope: TASK-0051 — materialize the first v3.1 Batch-P4 Action. Deliverables: (D1) fill actions/surface-version-sync-check.yml from stub to a working surface-version currency check per github-reference.md §7.1/§7.2/§7.3 — its own # template_version STAYS 3.0.0 (stub->fill, not a material-content bump per §17.5); (D2) .amas/surfaces.yml dogfood manifest (5 entries; self-entry declares 3.0.0 to match the Action marker; surfaces_manifest 3.0.1; linked-pr-fix-up excluded — no template-of-record); (D3) .github/workflows/surface-version-sync-check.yml operational ADVISORY instantiation (not a required status check); (D4) github-reference.md §7.1 example agents: [claude, codex] -> [codex] (resolves the carried-forward Codex PR-92 [C2]); (D5) actions/fixtures/.../stale-manifest.yml negative fixture; (D6) currency v3.0.1 -> v3.0.2 across trio frontmatter (x3) + README/AGENTS/CLAUDE in-development markers (two-concept: v3.0.0 published preserved; no "published" attaches to v3.0.2); (D7) core.md §18.3 M-A7 37 -> 38 (PR-NN literal; span v3.0.2; preamble TASK-0051).

Please run the named verification battery in "Builder claims to verify" (claims 1-10). Special focus: (1) D1 template_version STAYS 3.0.0 and the manifest self-entry matches it; (2) the "published" attachment predicate — v3.0.2 carries no "published" clause anywhere; (3) §7.2 honest-proof posture (currency-not-parity, manifest-declared vs template-of-record, no mandatory operational-surface read); (4) D6 zero-3.0.1-residual scoping leaves the §7.1 example intact; (5) the Builder-reconstructed elements flagged in Reviewer focus.

Per ADR-001 D11 owner-invokes convention: surface findings per severity (Blocking -> handback; Major -> path-(a)/(b); Minor -> default path-(b)). Substantive verdict via formal review preferred; issue-comment summary acceptable.

Verbatim-output convention: capture the review verbatim into the review-context's "Codex desktop pre-commit output absorption" section.
```

## Codex desktop pre-commit output absorption

### Codex desktop pre-commit review — 2026-06-07

**Findings**

Blocking: none.

Major:

- [M1] `actions/surface-version-sync-check.yml:101` / `.github/workflows/surface-version-sync-check.yml:55` — the optional `.yml` operational-surface cross-check currently treats any un-commented YAML `template_version:` key as an in-file marker because `read_marker()` uses `^#?[[:space:]]*template[ _]version:`. On the real dogfood manifest, the `surfaces_manifest` operational path is `.amas/surfaces.yml`; that file has nested per-entry `template_version` fields but no top-level operational marker. The live run therefore emits a false advisory warning on an otherwise current manifest: `::warning::(advisory) surfaces_manifest: operational-surface marker 3.0.0 != manifest-declared 3.0.1`. This contradicts the claimed clean real-manifest proof and weakens the §7.2 posture: optional operational-surface evidence should recover marker parity where an operational marker exists, not parse the manifest's own entry data as a marker. Suggested path-(a)/(b): either narrow the advisory cross-check marker for `.yml` operational files to comment markers only (`^#[[:space:]]*template...`) while preserving markdown/frontmatter template-of-record parsing, or explicitly skip `.amas/surfaces.yml` for operational-surface advisory marker checks unless the manifest has its own top-level/comment template marker.

Minor:

- [m1] `docs/reviews/PR-NN-codex-pre-commit.md:31` / `:32` — the D2 verification commands use `grep -A1 'name: ...'`, but `.amas/surfaces.yml` places `path:` between `name:` and `template_version:`. Running the stated shape returns `0`, not the claimed `1`, for both the self-entry and `surfaces_manifest`. The substantive manifest entries are correct (`surface-version-sync-check` declares `3.0.0`; `surfaces_manifest` declares `3.0.1`), but the battery should use `-A2` or a block-aware check so the pre-commit context remains reliable.

**Verification Summary**

- D1 confirmed: `# template_version: 3.0.0` count `1`; `3.0.1` count `0`; stub text count `0`; `name: surface-version-sync-check` count `1`.
- D2 substantively confirmed: 5 manifest entries; linked-pr-fix-up absent; self-entry is present at `.amas/surfaces.yml:50-52` with `template_version: 3.0.0`; `surfaces_manifest` is present at `.amas/surfaces.yml:38-40` with `template_version: 3.0.1`. The stated `grep -A1` commands are defective as noted above.
- D3 confirmed: operational workflow exists and names itself advisory; it mirrors the canonical Action, including the M1 extractor issue.
- D4 confirmed: `agents: [claude, codex]` count `0`; `agents: [codex]` count `1`.
- D5 confirmed with live Git Bash run: real manifest exits `0`; stale fixture exits `1` and flags `AGENTS.md` stale while keeping `CLAUDE.md` OK. Real manifest also emits the false advisory warning described in M1.
- D6 confirmed: trio frontmatter is `3.0.2` in all three files; README/AGENTS/CLAUDE each contain `v3.0.2`; no `v3.0.2` + publish/published attachment lines were found; v3.0.0-published language remains preserved; trio `3.0.1` residuals are only the github-reference §7.1 example lines 327/336/342.
- D7 confirmed: `+ PR-89 + PR-92 + PR-NN = 38`, `as of v3.0.2 canonicalization at PR-NN / TASK-0051`, and `38 consecutive substantive cycles` each occur once; stale `= 37` and `PR-95` counts are `0`.
- D8 confirmed: handoff 12-field count `12`; review-context frontmatter status count `1`; linked_pr placeholder regex count `1`.
- D9 anti-scope confirmed: no `prompts/` edits; no second Action; no other workflow edits.
- D10 live staged stats: `12 files changed, 680 insertions(+), 16 deletions(-)`.

Live Action run excerpt:

```text
LIVE real manifest
  [ OK ] AGENTS.md: declared 3.0.0 == template-of-record 3.0.0
  [ OK ] CLAUDE.md: declared 3.0.0 == template-of-record 3.0.0
  [ OK ] pr_template: declared 3.0.0 == template-of-record 3.0.0
  [ OK ] surfaces_manifest: declared 3.0.1 == template-of-record 3.0.1
    ::warning::(advisory) surfaces_manifest: operational-surface marker 3.0.0 != manifest-declared 3.0.1
  [ OK ] surface-version-sync-check: declared 3.0.0 == template-of-record 3.0.0
RESULT=0

LIVE stale fixture
  [FAIL] AGENTS.md: declared 2.14.1 != template-of-record 3.0.0 (stale / behind)
  [ OK ] CLAUDE.md: declared 3.0.0 == template-of-record 3.0.0
RESULT=1
```

**Builder-Reconstructed Focus**

D1 resolution mechanism and mode guard are directionally confirmed, subject to M1 on marker extraction. D3 operational mirror form is confirmed, but it mirrors the same M1 issue. D5 fixture location is confirmed. D7 §18.3 target is confirmed; no `(XXI)` anchor was edited. `roadmap_status: v3.1-planned` and README `[v3.1-planned]` hold posture is confirmed.

**Recommendation**

Request changes (Major, path-(a)/(b)): fix or consciously accept the false advisory warning before commit/PR. Minor m1 should default path-(b) unless the owner wants the review-context battery corrected in the same patch.

---

### Finding adjudication + resolution (Builder — 2026-06-07)

**M1 — path-(a) applied (both mirrored files).**
Root cause: `read_marker()` used `^#?[[:space:]]*template[ _]version:` — the optional `#` caused it to match bare YAML data keys (e.g., the per-entry `template_version:` nested inside `.amas/surfaces.yml`), producing a false advisory on `surfaces_manifest`. The fix: the optional cross-check no longer reuses `read_marker()`; instead it uses an inline comment-anchored extraction `grep -m1 -E '^#[[:space:]]*[Tt]emplate[_ ]version:'` that structurally excludes all data keys (they lack the leading `#`). The `read_marker()` function itself is unchanged — it still correctly handles both YAML-comment and markdown-frontmatter template-of-record markers.

Files changed:
- `actions/surface-version-sync-check.yml`: optional cross-check block updated + explanatory comment added (class note: bare data keys; PR-92 [C1] class).
- `.github/workflows/surface-version-sync-check.yml`: same update, mirrored per §6.2 canonical-source→operational-mirror discipline.

**m1 — path-(a) applied (review-context battery).**
Lines 31–32: `grep -A1` → `grep -A2` with rationale comment (`path:` sits between `name:` and `template_version:` in the manifest structure, so `-A1` only reaches `path:` — not `template_version:`). Claim-artifact-parity restored: the documented command now returns `1` for both self-entry and surfaces_manifest checks.

**Post-fix live re-run evidence:**

Real manifest (`.amas/surfaces.yml`):
```text
  [ OK ] AGENTS.md: 3.0.0 == 3.0.0
  [ OK ] CLAUDE.md: 3.0.0 == 3.0.0
  [ OK ] pr_template: 3.0.0 == 3.0.0
  [ OK ] surfaces_manifest: 3.0.1 == 3.0.1
  [ OK ] surface-version-sync-check: 3.0.0 == 3.0.0
RESULT=0
```
No false advisory. 5×OK. Exit 0. ✓

Stale fixture (`actions/fixtures/surface-version-sync-check/stale-manifest.yml`):
```text
  [FAIL] AGENTS.md: 2.14.1 != 3.0.0 (stale)
  [ OK ] CLAUDE.md: 3.0.0 == 3.0.0
RESULT=1
```
Core predicate untouched. [FAIL]+[OK] selective detection preserved. Exit 1. ✓

Neither fix touches the canonical-law trio (D4/D6/D7 unchanged). Gate-A canonical re-clear on those four edits remains in force from the prior Architect clear.

**Updated diff stats (post-fix re-stage):** `12 files changed, 735 insertions(+), 16 deletions(-)`.
