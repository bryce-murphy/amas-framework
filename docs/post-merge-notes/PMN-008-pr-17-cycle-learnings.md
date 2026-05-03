---
post_merge_note_id: PMN-008
title: PR-15 + PR-17 cycle learnings — (r) fifth review surface, (i.5) convention-inference verification, (t) two-data-point preliminary
linked_pr: PR-19 (squash SHA ddc54a4)
framework_version_dogfooded: AMAS v2.17
status: recorded
---

# PMN-008 — PR-15 + PR-17 cycle learnings — (r) fifth review surface, (i.5) convention-inference verification, (t) two-data-point preliminary

## Status

Drafted — 2026-05-03

PMN-008 inserts under ADR-003 Decision 3 contingency budget. Consumes one of four remaining contingency slots; three remaining (TASK-0025 through TASK-0027 unconsumed). Status flips to Recorded post-merge per PMN-001 (k) Linked PR fix-up substitution + status flip convention.

## §1. Trigger basis and observations register

PMN-008 documents cycle learnings across two source cycles: PR-15 (TASK-0015 substantive cycle / squash SHA `ace6608`) + PR-17 (TASK-0017 substantive cycle / squash SHA `ce44836`). Linked predecessor: PMN-007 (authored at TASK-0015 / PR-15; documents PR-13 cycle learnings). Authoring task: TASK-0018 / PR-19. Framework version dogfooded: AMAS v2.17.

Trigger: two candidates registered at PMN-007 monitoring register (TASK-0017 spec §1.3) reached canonical refinement threshold across PR-15 (TASK-0015) and PR-17 (TASK-0017) cycles:

- **(r) Builder step-6 self-review fifth surface**: two strong cross-cycle confirmations (PR-15 + PR-17)
- **(i.5) convention-inference verification sub-shape**: two cross-cycle confirmations (PR-15 step-1 stop-and-show + PR-17 step-1 stop-and-show)

One candidate originally projected as third canonical-refinement-threshold-reached at TASK-0017 cycle close was demoted at PMN-008 authoring after Builder PR-19 step-1 self-review surfacing — see §2 below:

- **(t) pre-merge record-updates-as-fix-up**: two-data-point preliminary (PR-15 + PR-17 only); PR-13 cycle close used §18.3 M-A7 amend-on-main authoring per TASK-0015 handoff explicit sub-shape distinction, NOT (t) pre-merge feature-branch fix-up. (t) carries forward as monitoring item per §5.6.

Six monitoring items carry forward (five from TASK-0017 spec §1.3 + (t) demotion). Three new candidates registered: (u) v2.14.1-canonical-vs-repo-convention divergence (from PR-17 Codex post-PR pass 1); (v) self-instantiation-via-failure-and-correction at the surface canonicalizing the discipline (from PMN-008 authoring cycle itself — see §1.1 below); (h.4) Codex-output-endpoint-coverage canonical-text correctness gap (NEW immediate-canonical-refinement candidate at five-data-point empirical evidence; surfaced post-first-fix-up at PR-19 cycle close — see §5.8 below). One existing candidate disconfirmed: (q') clean-first-pass conditional on PR scope (PR-19 produced findings; small-scope-clean prediction not supported — see §5.2 below).

### §1.1. Honesty record carried forward + PMN-008 authoring honesty record

PR-17 cycle defect tally: 15 net distinct (~1.36× PR-15 baseline of 11). Three-surface defect decomposition:

- **Architect §23.6 spec authoring (iterations 2-5)**: 12 fix events / 8 distinct defect clusters. Notable: (j) same-class sweep at iteration-2 caught §15 propagation but missed §10 in §3.2 (separate token, separate context) — escaped to Builder step-6 self-review surface.
- **Builder step-6 self-review surface (per (r) candidate)**: 5 path-(a) candidates before Codex — §10 §-citation defect (j)-sweep miss + 4 verification-command/scope reframes (claim 6 BRE/ERE flag bug, claim 12 frontmatter-vs-body scope, claim 13 scope mismatch, claim 4 line-count target overestimate).
- **Codex post-PR surfaces**: 2 substantive content findings (Finding 1 path-(β) deferred; Finding 2 path-(a) resolved).

**PMN-008 authoring honesty record**: Architect §23.6 self-review on PMN-008 was single-iteration "clean enough for presentation" — insufficient. Builder PR-19 self-review and post-cycle-close re-poll surfaced **eleven substantive defects across five sweep passes** (seven pre-authoring at step-1 pre-flight + one post-authoring at step-6 (j) sweep + two at Codex post-PR third-endpoint + one at Builder absorption-discipline gap surface):

**Pass 1 — §-content sweep** (3 defects):
1. **§2.1 (t) three-data-point claim conflated PR-13 §18.3 M-A7 amend-on-main with (t) pre-merge feature-branch fix-up**, falsifying the canonical-refinement-threshold claim. PR-13 cycle close had no feature-branch fix-up commit; the three-data-point framing collapsed the (t)-vs-M-A7 distinction that TASK-0015 handoff §`Decisions made` explicitly preserved. Verified against actual git history: PR-15 has a64e401 (2 files / 76+/3-); PR-17 has d57766e (3 files / 38+/2-) + 723c571 (2 files / 88+/3-); PR-13 has none of this shape. Path-(a) routed: § §2 reshaped as demotion record; (t) carries forward as monitoring item §5.6.
2. **§4.2 cited github-reference.md §3.5 placement target without verification** (§3 has only §3.1/§3.2/§3.3 in HEAD; no §3.5). Same defect class as TASK-0017 spec iteration-2 Defect E (Architect-asserted-without-verification — failed to grep actual canonical structure). (i.5) self-application failure on the very discipline PMN-008 canonicalizes. Path-(a) routed: drop specific anchor; defer placement adjudication to TASK-0019 Phase 1 scoping.
3. **§7 PMN-006 cross-reference anchored to §3 instead of correct §1.1/§3.2**. PMN-006 §3 is titled "(b) → (g) + (h) split: verification-artifact-validity discipline canonicalization"; the multi-surface-mitigation load-bearing framing lives in §1.1 honesty record + §3.2 (h) canonicalization. Path-(a) routed: re-anchor cross-reference.

**Pass 2 — frontmatter/structure convention-inference sweep** (4 defects, Builder applied (i.5) to surface inference gaps in PMN-008 file shape vs PMN-007 HEAD canonical precedent):

4. **Frontmatter field convention divergence** from PMN-007 HEAD (`post_merge_note_id` / `linked_pr` with squash-SHA-placeholder / `framework_version_dogfooded` / `status: drafted`). Architect-spec frontmatter used novel `pmn_id` / `task_id` / `pr` / `source_cycles` / `linked_predecessor` / `status: active` shape. Path-(a) routed: replace with PMN-007 canonical frontmatter; lift `source_cycles` / `task_id` / `linked_predecessor` framing into §1 prose where it expresses more flexibly. Architect adjudication confirmed no new convention intended; drift caught by Builder pre-flight (i.5) inference verification against canonical source.
5. **`linked_predecessor` value error**: "PMN-007 (TASK-0013 / PR-13 cycle learnings)" — TASK-0013 is unused/reserved; PMN-007 was authored at TASK-0015 / PR-15 (the "PR-13 cycle learnings" phrase is correct as PMN-007's filename slug content but the predecessor anchor is where PMN-007 file landed, not the cycle PMN-007 documents). Path-(a) routed: TASK-0013 → TASK-0015 in §1 prose; clarify the slug-vs-anchor distinction inline.
6. **Missing `## Status` section** between H1 and §1. PMN-004 / PMN-005 / PMN-006 / PMN-007 all begin with `## Status` containing "Recorded — DATE" (or "Drafted —" pre-merge) + ADR-003 contingency-budget framing. Path-(a) routed: add canonical `## Status` section per PMN-007 precedent.
7. **Frontmatter `title` field vs H1 heading content mismatch**: title elaborated "(r) fifth review surface, (i.5) convention-inference verification, (t) two-data-point preliminary"; H1 was shorter "PR-15 + PR-17 cycle learnings". PMN-007 precedent has matching content in both surfaces. Path-(a) routed: align H1 to title field's longer canonical-refinement enumeration form.

All seven defects path-(a) routed via Architect spec-authoring revisions before Builder commit (no path-(β) deferrals at this surface).

**Pass 3 — Builder step-6 self-review (j) sweep on §-citations after authoring** (1 defect; the (r) discipline operating at its canonical surface, post-authoring, rather than at step-1 pre-flight):

8. **PMN-007 §6 (p) cross-reference incorrect** — Architect-drafted spec referenced "PMN-007 §6 (p) M-A7 amend-on-main framing"; (p) is actually canonicalized at PMN-007 §8.2 (PMN-007 §6 is "Auto-trigger reliability — preliminary observation"). Defect propagated from spec into Builder-authored PMN-008 §2.2 table row + TASK-0018 handoff `Linked records` enumeration. Caught at Builder step-6 (j) all-instances sweep on `PMN-007 §[0-9]+(\.[0-9]+)?` pattern across all three deliverable files. Path-(a) routed: pure-token-swap (single-iteration fix; replace `§6` with `§8.2` in two locations). This is the third empirical instance of (r) Builder step-6 self-review at PMN-008 cycle (after the 7 pre-flight defects at Pass 1 + Pass 2), and operates at the canonical surface specified in §3.1 below: "§-citation residuals that escape Architect sweep" — exactly the defect class caught.

**Pass 4 — Codex post-PR review (third-endpoint inline comments)** (2 defects caught by Codex at line-level review-comments endpoint; surfaced post-Builder-first-fix-up via owner-driven re-poll exposing the (h.4) absorption-discipline gap):

9. **PR-19 review-context Claim 11 unverifiable pre-merge-fix-up SHAs against `git log --oneline main`** (P1 — Major-equivalent severity per Codex badge convention). Pre-merge fix-up SHAs `a64e401` / `d57766e` / `723c571` are squash-merged-out at PR-15/PR-17 close — not on main; only present on remote feature-branch refs. Claim 11's "Cross-verifiable against `git log --oneline main` for each SHA" was operationally false for those three SHAs. Path-(a) routed: drop SHA enumeration from main-cross-verifiable claim; reframe Claim 11 as "main-reachable squash SHAs only (`ace6608`/`ce44836`/`52ee07e`) cross-verifiable against main; pre-merge fix-up SHAs in §2.2 table cross-referenced to PR-15/PR-17 review-context records as historical (t)-sub-shape diff-size data points." Pure-token-swap class per §8.1.1.3.
10. **TASK-0018 handoff broken markdown link `[github-reference.md](github-reference.md)` from `docs/handoffs/`** (P3 — Minor-equivalent severity). Markdown-link relative path resolves to non-existent `docs/handoffs/github-reference.md`; actual file at repo root. (i.5) PMN-file-shape sub-extension would have caught this if applied at authoring time (prior PMN convention is plain-text references). (j) same-class sweep on `\]\([a-zA-Z][^):/]*\.md\)` pattern across all three deliverables surfaced 6 total broken-link instances (4 in PMN-008 + 1 in handoff + 1 in review-context). Path-(a) routed: drop markdown-link wrapper to plain-text reference matching prior-PMN convention.

**Pass 5 — (h.4) Codex-output-endpoint-coverage canonical-text correctness gap discovered at Builder-side absorption surface** (1 defect; meta-level — defect in canonicalized Builder absorption discipline that masked the Pass 4 findings):

11. **Two-endpoint-poll framing canonicalized at core.md §8.1.1.1 corrected lexicographic form is structurally INCOMPLETE.** Builder applied the canonical two-endpoint poll (PR reviews + issue comments) at first-cycle-close absorption and framed PR-19 as zero-substantive-findings clean-first-pass. Owner-driven re-poll surfaced the (h.4) gap: GitHub's review API exposes line-level inline review comments at a third endpoint (`pulls/{pr}/comments`) that the canonical text does NOT cover. Empirical evidence at five data points (PR-11: 11; PR-13: 1; PR-15: 0; PR-17: 6; PR-19: 2) — the third endpoint is the most defect-dense Codex output channel. (h.4) registered at §5.8 as immediate-canonical-refinement candidate (five-data-point evidence over-meets standard 2-3-cycle promotion threshold). core.md §8.1.1.1 canonical text correction routed path-(a) but **deferred to separate cycle** (anticipated TASK-0021 or following) per canonical-text-edit-warrants-its-own-cycle discipline. Pending core.md correction, Builder absorption discipline at all PMN-008-onward cycles MUST poll all three endpoints regardless of canonical-text current state.

11-defect tally final: 3 §-content (Pass 1 step-1 pre-flight) + 4 frontmatter/structure (Pass 2 step-1 pre-flight per (i.5)) + 1 §-citation residual (Pass 3 step-6 (j) sweep post-authoring) + 2 Codex post-PR findings at third-endpoint (Pass 4) + 1 canonical-text-correctness gap at Builder absorption surface (Pass 5 — (h.4)). Defects 1-8 caught at cycle-internal Builder surfaces; defects 9-10 caught at Codex post-PR third-endpoint; defect 11 caught at owner re-poll surfacing the absorption-discipline gap. All path-(a) routed; one path-(β) deferral (core.md §8.1.1.1 canonical text correction).

**Recursive empirical confirmation of (r) fifth-surface canonical refinement** at strongest possible strength: the discipline PMN-008 canonicalizes self-applied at the very next PR cycle (PR-19 PMN-008 authoring) to catch defects that escaped Architect §23.6 single-iteration sweep on PMN-008 itself. The 11-defect tally splits across five distinct sweep passes (Pass 1 + Pass 2 step-1 pre-flight; Pass 3 step-6 self-review post-authoring; Pass 4 Codex post-PR third-endpoint; Pass 5 (h.4) absorption-discipline gap) — each pass catches defect classes that align with surface-coverage characterization (§3.1 below). Strong empirical reinforcement that multi-surface mitigation per PMN-006 §1.1 / §3.2 framing is structurally load-bearing — single Architect-surface fixed-point is insufficient, AND the canonical absorption-discipline framing itself can carry correctness gaps that only owner-side judgment surfaces. The framework's reflexive refinement disciplines are doing real work at multiple cycle-close surfaces.

**(v) candidate observation registered** (§5.7 below): when a PMN canonicalizes a discipline, defects in that PMN's own authoring (caught at the canonicalized discipline's downstream surfaces) provide the strongest possible empirical confirmation of the discipline's load-bearing role. (v) self-instantiation-via-failure-and-correction at the surface canonicalizing the discipline. Single-cycle observation; promotion threshold = 2-3 cross-cycle confirmations.

Empirical interpretation: multi-surface mitigation per PMN-006 §1.1 / §3.2 framing confirmed load-bearing across both source cycles (PR-15 + PR-17) AND PMN-008 authoring cycle itself.

---

## §2. Status update: (t) pre-merge record-updates-as-fix-up — demoted to monitoring

### §2.1. Demotion event

At TASK-0017 cycle close, Architect adjudicated (t) as having reached three-data-point canonical-refinement threshold based on PR-13 + PR-15 + PR-17 enumeration. PMN-008 spec drafting carried the three-data-point framing into §2 as canonical refinement.

Builder PR-19 step-1 self-review verified the framing against actual git history and surfaced that PR-13 cycle close did NOT use (t) pre-merge feature-branch fix-up. PR-13 cycle close used §18.3 M-A7 amend-on-main / merge-commit-body authoring instead — a structurally distinct sub-shape that TASK-0015 handoff explicitly distinguished from (t):

> "(t) pre-merge record-updates-as-fix-up sub-shape … NOT §18.3 M-A7" — TASK-0015 handoff `## Decisions made` section (line 44).

Architect's three-data-point claim collapsed the (t)-vs-M-A7 distinction. The TASK-0017 cycle adjudication (and the pre-merge commit message + post-merge amendment for PR-17 `ce44836`) propagated the imprecise three-data-point framing.

### §2.2. Verified two-data-point empirical evidence

Per Builder verification against git history at TASK-0018 / PR-19 authoring:

| Cycle | Sub-shape | Pre-merge feature-branch fix-up commits |
|---|---|---|
| PR-13 (TASK-0012) | §18.3 M-A7 amend-on-main authoring | None (cycle close used merge-commit-body authoring per PMN-007 §8.2 (p)) |
| PR-15 (TASK-0015) | (t) pre-merge feature-branch fix-up | `a64e401` (2 files, 76+/3-) |
| PR-17 (TASK-0017) | (t) pre-merge feature-branch fix-up | `d57766e` (3 files, 38+/2-) + `723c571` (2 files, 88+/3-) |

(t) is two-data-point preliminary (PR-15 + PR-17). Canonical-refinement threshold not yet reached; one more cross-cycle confirmation required.

### §2.3. Demotion to monitoring register

(t) carries forward as monitoring item §5.6 below. Promotion trigger: third cross-cycle confirmation of pre-merge feature-branch fix-up commit shape in a substantive-content cycle (anticipated TASK-0019 usage-guide.md cycle or following). At three-data-point reached, (t) becomes canonical-refinement candidate; PMN at that cycle proposes Builder execution steps template addition.

### §2.4. Sub-shape taxonomy preserved as preliminary observation

Across two-data-point set, the (t) sub-shape diff size varies materially: PR-15 `a64e401` = 2 files / 76+/3-; PR-17 fix-up-1 `d57766e` = 3 files / 38+/2-; PR-17 fix-up-2 `723c571` = 2 files / 88+/3-. This rules out small-diff-only framing of (t). Sub-shape taxonomy is preliminary; canonical refinement at three-data-point cycle should describe size variation explicitly.

The chore-fix-up sub-shape interaction (canonical-content-frontmatter-status-flippability per Builder PR-18 observation) is a separate sub-shape on the post-merge chore-fix-up surface (PR-12, PR-14, PR-16, PR-18) — distinct from (t) pre-merge feature-branch fix-up. Both interact during cycle close but are structurally separable.

---

## §3. Canonical refinement: (r) Builder step-6 self-review fifth surface

### §3.1. Observation

**Two strong cross-cycle confirmations** (PR-15 + PR-17):

- **PR-15 cycle**: Builder step-6 self-review surfaced (h.2) verification-command defect on claim 8 (missing `--json` flag) before Codex pre-commit. Single-data-point at PMN-007 cycle.
- **PR-17 cycle**: Builder step-6 self-review surfaced 5 path-(a) candidates before Codex — including a §-citation defect (core.md §10 not in HEAD set) that escaped Architect §23.6 5-iteration self-review fixed-point, plus 4 verification-command/scope reframes. Codex post-PR then surfaced 2 additional substantive content findings that Builder step-6 was not positioned to catch (canonical-text content-level review).

Empirical characterization of each surface's defect-class coverage:

| Surface | Defect class caught |
|---|---|
| Architect §23.6 self-review | Prose-arithmetic, recap-consistency, §-citation correctness against known HEAD set, Architect-asserted-without-verification claims |
| Builder step-6 self-review | Verification-command operational correctness, frontmatter-vs-body scope mixing, §-citation residuals that escape Architect sweep, claim-scope mismatches |
| Codex pre-commit | Verification-artifact internal consistency, cross-claim consistency |
| Codex post-PR | Substantive content findings, canonical-text correctness, advisory/blocking contradictions, v2.14.1-vs-repo-convention divergences |

Each surface catches distinct defect classes; multi-surface composition is structurally load-bearing per PMN-006 §1.1 + §3.2 framing.

### §3.2. Canonical refinement

**PMN-007 §3.1 four-surface iterative review pipeline** extends to **five-surface** as the canonical default:

1. Architect §23.6 self-review (iterative to fixed-point per §23.6.2)
2. Builder pre-flight (extended per (i) refinement + (i.5) sub-shape)
3. **Builder step-6 self-review** ← promoted from (r) candidate to canonical default
4. Codex desktop pre-commit (owner invokes per ADR-001 decision 11)
5. Codex cloud post-PR (owner invokes `@codex review` per ADR-001 decision 11)

**Action items**: Builder execution steps canonical template (usage-guide.md TASK-0019) includes step-6 self-review as an explicit numbered step. Architect spec authoring for future cycles names five surfaces in §5 review pipeline and §8 stop-and-show points. PR review-context files enumerate findings per surface with explicit surface label.

---

## §4. Canonical refinement: (i.5) convention-inference verification sub-shape

### §4.1. Observation

**Two cross-cycle confirmations** (PR-15 + PR-17 step-1 stop-and-show):

- **PR-15 cycle**: Builder pre-flight surfaced Mismatch 2 — Architect inferred chore-fix-up PRs do not generate separate review-context files from convention memory; Builder verified against actual `git ls-files docs/reviews/` and confirmed the inference was correct but needed empirical grounding rather than convention-assertion.
- **PR-17 cycle**: Builder pre-flight step-1 surfaced correct classification of core.md v2.16 references at lines 223 and 234 as historical/cross-document state preserved verbatim — not canonical-version-of-record requiring bump. Builder applied (i.5) correctly: grep'd for all v2.16 placements, classified each against canonical-version-of-record vs historical/enumeration, surfaced before applying rather than assuming.

Class A/B/C version-marker classification scheme emerged as canonical refinement candidate:

| Class | Form | Treatment |
|---|---|---|
| A | Single declarative line "current canonical version is vX.Y" | Canonical-version-of-record; bump at substantive-content cycles per §18.4 |
| B | Historical date-stamping in prose ("as of vX.Y canonicalization (this PR)") | Preserve verbatim; records prior event |
| C | Sequence enumeration with continuation markers ("v2.14.1, v2.15, v2.16, v3.0.0, ...") | Preserve verbatim; illustrative sample not registry |

### §4.2. Canonical refinement

**(i.5) sub-shape promoted** from monitoring candidate to canonical pre-authoring batch discipline. Extended form:

> **(i.5) Convention-inference verification**: when asserting expected counts, forms, or values that could be inferred from convention memory rather than direct verification, verify against actual canonical source before asserting. Applied to: file-class-existence counts (verify via `git ls-files <dir> | wc -l`); canonical-version-of-record placements (verify via grep + Class A/B/C classification); stub frontmatter field values (verify via `head -10 <file>`); §-citation existence in HEAD set (verify via `grep -nE "^#{1,6} §N" <canonical-file>`); **PMN-file-shape convention-inference against HEAD canonical precedent** (verify frontmatter field set + `## Status` section presence + title↔H1 alignment via `head -15 <prior-PMN-file>` — this sub-extension empirically grounded by PMN-008 authoring Pass 2 (i.5) sweep catching 4 frontmatter/structure defects).

**(j) sweep completeness refinement**: the (j) same-class propagation residual sweep should enumerate ALL instances of the defect-class pattern via grep, not only same-token instances. For §-citation correctness defects, sweep = `grep -nE "<canonical-file>\.md §[0-9]+" <file>` and verify each hit against HEAD §-header set. PR-17 demonstrated that sweeping §15-token instances while missing §10-token instances in a separate context produces incomplete coverage.

**Action items**: Architect §23.6 self-review discipline (canonical §23.6.1 text) adds (i.5) sub-shape to the standing pre-authoring sweep, including the PMN-file-shape sub-extension. (j) sweep procedure adds explicit grep-all-instances instruction. Version-marker classification scheme (Class A/B/C) canonical placement deferred to TASK-0019 usage-guide.md authoring — Architect Phase 1 scoping at TASK-0019 adjudicates whether the scheme lives in usage-guide.md operating guidance (procedural framing) or extends github-reference.md (structural framing) via a new §-section or §1 Purpose subsection. Verbatim scheme text preserved in this PMN's §4.1 above for forward-reference at TASK-0019 authoring.

---

## §5. Monitoring register

### §5.1. (u) v2.14.1-canonical-vs-repo-convention divergence — NEW, single-cycle

**Observation**: github-reference.md §2.2 preserves v2.14.1 §6.1 branch regex verbatim (`^(feat|fix|chore|adr|shadow|spike)/[0-9]+-(...)`). Codex post-PR pass 1 surfaced that the repo's actual branch convention uses `<type>/task-NNNN-<slug>` (per CLAUDE.md), which fails the regex (task-NNNN prefix contains `task-` before digits, not bare digits). Finding routed path-(β) — genuinely-asymptotic: canonical-source determination + multi-document reconciliation + ADR-class durable decision required.

**Watch**: usage-guide.md cycle + templates/prompts/Actions cycles. Does analogous divergence surface where v2.14.1-migrated content conflicts with actual repo operating convention? Each instance = additional evidence.

**Promotion trigger**: 2-3 cross-cycle instances surfacing analogous divergence shape, or next-cycle Architect Phase 1 scoping adjudication on branch regex canonical-source determination (ADR-class durable decision on whether CLAUDE.md `task-NNNN` form or v2.14.1 §6.1 numeric-id form is canonical for v3).

### §5.2. (q') clean-first-pass conditional on PR scope — DISCONFIRMED at PR-19

**Original observation**: PR-15 Codex post-PR = clean first pass (0 findings; (q) initial candidate). PR-17 Codex post-PR pass 1 = 2 substantive content findings. The divergence appeared to correlate with PR content-surface size: PR-15 was a smaller canonical-text extension; PR-17 was a full canonical-law-trio-member authoring.

**Original refinement candidate** (now disconfirmed): (q') = "clean-first-pass Codex post-PR shape is conditional on PR scope (small canonical-text extension ≈ clean; full canonical-law-trio-member authoring ≈ findings expected)."

**Disconfirmation event at PR-19 cycle close**: PR-19 is small-scope PMN-only chore-class cycle (no canonical-text changes; 3 new files / 473 insertions first commit). Per (q') prediction, PR-19 should have produced clean-first-pass. Initial Builder absorption framed PR-19 as clean-first-pass, but that framing was structurally false due to (h.4) endpoint-coverage gap (see §5.8 below). Corrected absorption per third-endpoint poll surfaced **2 actual Codex findings** (1 Major-equivalent on PR-19 review-context Claim 11 unverifiable SHAs; 1 Minor-equivalent on TASK-0018 handoff broken markdown link). PR-19 cycle thus produced findings at small-scope cycle — disconfirms the small-scope-clean prediction.

**Refined empirical state**:

| Cycle | Scope | Codex findings (post-3-endpoint-poll) |
|---|---|---|
| PR-15 (TASK-0015 / PMN-007 + small core.md surgical) | Smaller canonical-text extension | 0 ((q) initial single-data-point) |
| PR-17 (TASK-0017 / github-reference.md) | Full canonical-law-trio-member authoring | 2 substantive findings |
| PR-19 (TASK-0018 / PMN-008) | PMN-only chore-class | 2 findings (1 Major-equivalent + 1 Minor-equivalent) |

(q') scope-conditional prediction is NOT supported by three-data-point set. PR-19 small-scope-with-findings ≠ small-scope-clean. **(q') demoted from canonical-refinement candidate back to monitoring**; disconfirmation event explicitly recorded. Possible reframings for next-PMN consideration: (q'') Codex-output-density correlates with deliverable type rather than scope (PMN authoring + handoff body authoring may produce specific defect classes that small-canonical-text-extension cycles do not); (q''') findings-frequency is uniform across scope buckets and prior framing was anchored on PR-15's coincidental clean-first-pass shape. Each candidate would require its own data point accumulation; defer to next-PMN authoring.

**Watch**: TASK-0019 (usage-guide.md authoring; full canonical-law-trio-member) — fourth data point. If TASK-0019 produces findings, it confirms findings-are-norm; if clean, supports a refined scope-conditional pattern with PR-19 as anomaly. Continue monitoring.

### §5.3. (j)-extension same-class sweep completeness — single-cycle, refined

**Observation**: PR-17 demonstrated (j) sweep operated correctly on §15-token instances at iteration-2 but missed §10 in §3.2 (separate token, separate context). Builder step-6 self-review surface caught the residual.

**Status**: empirical evidence that (j) sweep must be defined as all-instances enumeration, not same-token propagation. Canonical refinement partially addressed in §4.2 above ((j) sweep completeness refinement). Full application to Architect §23.6 iteration procedure deferred to usage-guide.md authoring where §23.6 operational guidance is canonicalized in prose.

### §5.4. (h.x)-extension Architect verification-command-execution discipline — single-cycle

**Observation**: PR-17 spec §6.1 claims 6 and 12 contained grep-command errors that escaped Architect §23.6 5-iteration self-review (claim 6: BRE `^(feat|...)` literal-paren match issue; claim 12: frontmatter-vs-body scope conflation). Builder step-6 self-review caught both.

**Refinement candidate**: Architect §23.6 verification-command correctness sweep should include mental-execution of each grep/bash/PowerShell command to verify the command's output domain covers the claim's verification need (extends PMN-006 §3.2 (h.2) sub-shape to Architect-side spec authoring surface, not only Builder verification-artifact authoring surface).

**Promotion trigger**: second cross-cycle confirmation of Architect-authored grep-command error caught at downstream surface rather than Architect §23.6 sweep.

### §5.5. (s) pre-commit pipeline sufficiency — surface-class-differentiated framing

**Observation**: five-surface pipeline (Architect §23.6 + Builder pre-flight + Builder step-6 + Codex pre-commit + Codex post-PR) is sufficient in the sense that no defects have escaped to post-merge discovery in recent cycles. However, (s) framing as "pipeline sufficiency hypothesis" was imprecise. Better framing: each surface has a characteristic defect-class coverage (per §3.1 above); sufficiency = composition of coverage across surfaces; no single surface is self-sufficient.

**Status**: (s) as originally framed (sufficiency hypothesis) is replaced by the empirical characterization in §3.1. Retire (s) as separate monitoring item; absorb into canonical five-surface characterization per §3.2.

### §5.6. (t) pre-merge feature-branch fix-up — two-data-point preliminary (DEMOTED from canonical-refinement claim)

**Observation**: per §2 above, (t) canonical-refinement-threshold claim at TASK-0017 cycle close was incorrect. Verified empirical evidence is two-data-point: PR-15 `a64e401` (2 files / 76+/3-) + PR-17 `d57766e` + `723c571` (3 files / 38+/2- + 2 files / 88+/3-). PR-13 cycle close used §18.3 M-A7 amend-on-main authoring — distinct sub-shape per TASK-0015 handoff explicit distinction.

**Watch**: TASK-0019 cycle (usage-guide.md authoring) and following substantive cycles. Does pre-merge feature-branch fix-up commit shape continue to apply? Each substantive-content cycle provides a data point. Sub-shape diff size variation (PR-15 76+/3- vs PR-17 fix-ups 38+/2- and 88+/3-) suggests size is not stable; canonical refinement at three-data-point cycle should describe variation explicitly.

**Promotion trigger**: third cross-cycle confirmation of pre-merge feature-branch fix-up commit in a substantive-content cycle. PMN at the three-data-point-reached cycle proposes Builder execution steps template canonical addition per §2 above demotion-record framing.

### §5.7. (v) self-instantiation-via-failure-and-correction at the surface canonicalizing the discipline — NEW, single-cycle

**Observation**: PMN-008 canonicalizes (r) fifth-surface Builder step-6 self-review and (i.5) convention-inference verification disciplines. Builder PR-19 self-review and post-cycle-close re-poll caught eleven defects in PMN-008 cycle itself (see §1.1) across five sweep passes — three §-content defects (Pass 1 pre-flight) plus four frontmatter/structure defects (Pass 2 pre-flight per (i.5) sub-extension) plus one §-citation residual (Pass 3 Builder step-6 (j) sweep post-authoring) plus two Codex post-PR findings (Pass 4 third-endpoint) plus one canonical-text-correctness gap at Builder absorption-discipline surface (Pass 5 — (h.4)). Defects 1-8 arose from Architect failure to apply (r) / (i.5) / (j) to PMN-008's own authoring; defects 9-10 from Architect-Builder joint failure to apply (i.5) (broken markdown link) and (h.2) (unverifiable claim) to PR-19 review-context Claim 11 + handoff link path; defect 11 from canonical-text-correctness gap inherited from core.md §8.1.1.1 two-endpoint framing. The disciplines self-instantiate negatively at the Architect + Builder pre-cycle-close surfaces and positively at downstream Builder + Codex + owner-judgment surfaces within the same authoring cycle.

**Refinement candidate**: (v) = "when a PMN canonicalizes a discipline, defects in that PMN's own authoring (caught at the canonicalized discipline's downstream surfaces) provide the strongest possible empirical confirmation of the discipline's load-bearing role." (k.1) positive empirical confirmation at maximum strength: the canonicalizing PMN is shaped into correctness BY the very discipline it canonicalizes, applied at downstream surfaces.

**Watch**: TASK-0019 usage-guide.md cycle is the next authoring cycle that canonicalizes operating-guidance disciplines; does the same self-instantiation-via-failure-and-correction pattern apply? Each instance = additional evidence. Anticipated specifically: does Builder pre-flight or step-6 self-review catch defects in usage-guide.md's articulation of (r) / (i.5) / (j) operating guidance arising from Architect failure to apply those very disciplines at usage-guide.md authoring time?

**Promotion trigger**: 2-3 cross-cycle confirmations of the self-instantiation-via-failure-and-correction pattern in canonicalization PMNs. At promotion, (v) becomes canonical observation about the empirical-strength relationship between a discipline's canonicalization cycle and the downstream-surface confirmations of its load-bearing role.

### §5.8. (h.4) Codex-output-endpoint-coverage canonical-text correctness gap — NEW, five-data-point empirical evidence, immediate canonical-refinement candidate

**Observation**: Builder-side absorption discipline canonicalized at core.md §8.1.1.1 names a two-endpoint poll (PR reviews endpoint + issue comments endpoint) for capturing Codex post-PR output. Empirical evidence at PR-19 cycle close surfaced that GitHub's review API exposes a third endpoint (`pulls/{pr}/comments` — line-level review comments) that the canonical two-endpoint framing does NOT cover. This is the most defect-dense Codex output channel:

| Cycle | `pulls/{pr}/reviews` (Endpoint 1) | `issues/{pr}/comments` (Endpoint 2) | `pulls/{pr}/comments` (Endpoint 3 — uncovered by canonical text) |
|---|---|---|---|
| PR-11 | (per PMN-006 §1.1 absorption record) | (per PMN-006) | 11 inline comments |
| PR-13 | per PMN-007 absorption | per PMN-007 | 1 inline comment |
| PR-15 | per PMN-007 §9.3 (clean-first-pass) | per PMN-007 | 0 inline comments |
| PR-17 | per TASK-0017 cycle absorption | per TASK-0017 cycle | 6 inline comments |
| PR-19 | 1 review (auto-fire informational template) | 1 comment (owner @codex review trigger) | **2 inline comments (missed by Builder; surfaced by owner re-poll)** |

Five-of-five recent PRs had at-least-one inline comment except PR-15. The two-endpoint framing canonicalized at core.md §8.1.1.1 corrected lexicographic form survived multiple §23.6 self-review cycles + multiple Codex post-PR passes + canonical-text bake-in across PMN-003 (e) refined → PMN-005 §2.5 → PMN-006 → PMN-007 → core.md HEAD post-PR-13. Across that entire trajectory, neither Architect nor Codex caught that the API exposes line-level comments at a separate endpoint.

**Architect-side honesty record (PMN-008 cycle-close discovery)**: the (h.4) gap is Architect-canonicalized. The framework's own multi-surface mitigation surfaced the defect at Builder step-15-equivalent post-PR review absorption surface — the only surface where the gap operationally bites — empirically confirming that multi-surface mitigation per PMN-006 §1.1 / §3.2 framing remains structurally load-bearing across **canonical-text correctness defects**, not only verification-artifact correctness defects.

**Refinement candidate**: (h.4) = "Codex post-PR review output spans THREE GitHub API endpoints, not two. Canonical absorption requires polling `pulls/{pr}/reviews` (PR-level review summaries; state machine for APPROVED/CHANGES_REQUESTED/COMMENTED) + `issues/{pr}/comments` (top-level discussion thread; owner `@codex review` invocation triggers + Codex top-level responses) + `pulls/{pr}/comments` (line-level inline review comments; the most defect-dense Codex output channel)."

**Promotion threshold REACHED at PR-19 single cycle close**: empirical evidence already spans five data points (PR-11 + PR-13 + PR-15 + PR-17 + PR-19). Standard 2-3-cycle promotion threshold is over-met by 2-3x. (h.4) is **immediate canonical-refinement candidate**, not preliminary monitoring.

**Action items**:
- core.md §8.1.1.1 canonical text correction: surgical paragraph edit replacing "two-endpoint" framing with "three-endpoint" framing including explicit enumeration. Cost-class assessment: pure-token-swap (single-iteration text edit). Routing: path-(a). **Deferred to separate cycle** (anticipated TASK-0021 or following per M-A6 contingency budget) — canonical-text edit warrants its own spec + multi-stage review pipeline + framework version bump consideration per §18.4 substantive-reading minor criterion.
- Builder-side absorption discipline: pending core.md §8.1.1.1 correction, future cycles MUST poll all three endpoints regardless of canonical-text current state. Discipline applies to all PMN-008-onward cycles via this PMN's empirical record. Divergence between canonical text (two-endpoint, awaiting correction) and operational discipline (three-endpoint, immediate) is an explicit transitional state per (h.4) registration; readers should treat PMN-008 §5.8 as authoritative for Reviewer-output absorption discipline until canonical-text correction lands.

---

## §6. Anticipated forward integration

**TASK-0019 spec (usage-guide.md authoring)** carries forward PMN-008's two canonical refinements as defaults plus immediate-canonical-refinement-candidate (h.4) plus disconfirmation-event (q'):

- Five-surface review pipeline per (r) as canonical default in §5 of spec; **all post-PR Codex absorption MUST poll three endpoints per (h.4) §5.8** pending core.md §8.1.1.1 canonical text correction at separate cycle.
- (i.5) + Class A/B/C version-marker classification + (j) all-instances sweep completeness in pre-authoring batch per §4.2; (i.5) PMN-file-shape sub-extension applies at any PMN authoring within the cycle (includes plain-text-not-markdown-link convention for cross-file references per (i.5) sub-extension empirically grounded by PMN-008 cycle Pass 4 broken-link findings).
- Class A/B/C version-marker classification scheme canonical placement adjudicated at TASK-0019 Phase 1 scoping (placement candidates: usage-guide.md operating guidance, github-reference.md new §-section or §1 Purpose subsection, or both).
- (t) pre-merge feature-branch fix-up commit applied per established two-data-point pattern (NOT yet canonical default; if TASK-0019 cycle applies the pattern, three-data-point reached and PMN proposes canonical addition per §5.6).
- (u) v2.14.1-canonical-vs-repo-convention divergence watch applies — usage-guide.md migration sources include v2.14.1 §21/§22 prompts; verify these against actual repo operating convention at content authoring time.
- (v) self-instantiation-via-failure-and-correction watch applies — usage-guide.md canonicalizes operating-guidance disciplines; observe whether Builder downstream surfaces catch defects in usage-guide.md's articulation of those disciplines arising from Architect failure to apply them at authoring time.
- (q') disconfirmation event (PMN-008 cycle close) noted; reframings (q'') / (q''') possible at next-PMN cycle if additional findings-frequency data points accumulate; defer detailed reframing to TASK-0019 cycle close.
- (s) retired as standalone monitoring item; absorbed into five-surface characterization.

**(h.4) canonical-text correction cycle** (deferred from PR-19 path-(β)): anticipated TASK-0021 or following per M-A6 contingency budget. Architect drafts surgical paragraph edit at core.md §8.1.1.1 replacing "two-endpoint" framing with "three-endpoint" framing including explicit enumeration of `pulls/{pr}/reviews` + `issues/{pr}/comments` + `pulls/{pr}/comments`. Cycle scope: small canonical-text edit + framework version bump consideration per §18.4 substantive-reading minor criterion + canonical-refinement record at the cycle's PMN. Pending the correction, all PMN-008-onward Builder absorption applies three-endpoint poll regardless of canonical-text current state.

**Branch regex reconciliation cycle** (deferred from PR-17 path-(β)): anticipated at TASK-0019 Phase 1 scoping or following. Architect adjudicates: (a) read CLAUDE.md actual `task-NNNN` form; (b) determine canonical source for v3 branch convention (CLAUDE.md vs v2.14.1 §6.1 vs new ADR); (c) update github-reference.md §2.2/§2.3 via surgical fix if canonical source is CLAUDE.md form; otherwise record canonical-source-is-v2.14.1 as ADR.

**M-A6 post-PMN-008-merge**: 8 PMNs / 15 cycles = 53%. Above post-TASK-0017 50% calculation (denominator +1 for PMN-008 cycle; numerator +1). Within ADR-003 Decision 3 forecast range upper bound (~54%). Contingency slot count reconciliation deferred to TASK-0023 per established M-A6 monitoring register convention.

---

## §7. Cross-references

- **PMN-007**: source monitoring register; (t)/(r)/(i.5) initial candidate registrations; bounded-continuation rule §8.1.1.3 cost-class refinement; §3.1 four-surface pipeline. Authored at TASK-0015 / PR-15 (squash SHA `ace6608`); documents PR-13 cycle learnings.
- **PMN-006**: §1.1 honesty record + §3.2 (h) canonicalization for multi-surface-mitigation load-bearing framing; §3.1 (g)/(h) verification-artifact disciplines; §3.2 (h.2) command-achieves-claimed-verification sub-shape; §6.2 M-A7 operationally canonical; §5 bounded-continuation rule generalization; §3.4 (b.3) frontmatter-vs-body sub-clause.
- **PMN-005**: §2 reviewer-claimed-effects-don't-land; §4.4 (e.1) cumulative-diff-stats sub-rule; §2.5 five-point post-handback check pattern.
- **PMN-004**: §5 (a)-(f) standing disciplines; §1 4-iteration self-review empirical pattern.
- **PMN-001**: (h.2) file-based Builder direction; (k) Linked PR fix-up substitution discipline.
- **ADR-003**: Decision 2 PR plan; Decision 3 TASK reservation; §Consequences per-PR distributed-update discipline.
- **core.md §8.1.1.3**: bounded-continuation rule with cost-class refinement; (t)/(r)/(i.5) path-(a) vs path-(β) routing self-applied correctly per (k.1) positive self-instantiation discipline; (v) candidate observation extends (k.1) framing to canonicalization-PMN cycles specifically.
- **core.md §18.3**: M-A7 merge-commit-body data integration; sixth empirical instance at PR-17 (`ce44836`).
- **core.md §23.6 / §23.6.1 / §23.6.2**: Architect pre-handoff self-review disciplines; (i.5) sub-shape with PMN-file-shape sub-extension + (j) all-instances sweep apply.
- **TASK-0015 handoff** (`docs/handoffs/TASK-0015-pmn-007-pr-13-cycle-learnings.md`): explicit (t)-vs-§18.3-M-A7 sub-shape distinction at `## Decisions made` line 44; load-bearing for §2.1 demotion event.
- **PR-15 (TASK-0015 / `ace6608`)**: (t) data point 1; (r) data point 1; (i.5) data point 1.
- **PR-17 (TASK-0017 / `ce44836`)**: (t) data point 2; (r) data point 2; (i.5) data point 2; (u) new candidate; source cycle for this PMN.
- **PR-18 (squash SHA `52ee07e`)**: PMN-001 (k) chore-fix-up for TASK-0017; 2-file 3+/3- sub-shape (canonical-content-frontmatter-status-flippability interaction).
- **TASK-0018 (this PMN)**: TASK-0019 (next, anticipated usage-guide.md authoring).
