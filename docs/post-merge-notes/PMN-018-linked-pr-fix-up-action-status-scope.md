---
post_merge_note_id: PMN-018
title: PMN-001 (k) linked-pr-fix-up Action over-reach — path-scope the status transitions
linked_pr: PR-77 (squash SHA 5125138)
framework_version_dogfooded: AMAS v2.42 (no bump — manual chore-fix-up)
status: recorded
---

# PMN-018 — PMN-001 (k) linked-pr-fix-up Action over-reach: path-scope the status transitions

## Status

Recorded. Manual chore-fix-up (no TASK number; anticipated PR #77). No version bump, no M-A7 amendment, no roadmap change. Branch `chore/task-0046-pmn-001-k` is recursion-guard-matched, so the Action skips PR #77's own merge — the fix's first live run is the TASK-0047 chore-fix-up (see Validation plan).

## Context / defect

The PMN-001 (k) linked-pr-fix-up Action (`.github/workflows/linked-pr-fix-up.yml` → `.github/scripts/linked-pr-fix-up.py`) auto-substitutes canonical frontmatter placeholders in the files a squash-merged PR changed, then opens a chore-fix-up PR. Its `apply_substitutions()` applied `STATUS_TRANSITIONS` (`drafted → recorded`, `active → resolved`) to the YAML frontmatter of **every** changed file with a `.md/.yml/.yaml` suffix — with **no path / artifact-type scoping**. The workflow header comment *documented* the intended scoping (`active → resolved (TASK handoffs)`, `drafted → recorded (PMN + canonical-content artifacts)`), but the code did not enforce it: a documented-but-not-enforced gap.

At the TASK-0046 chore-fix-up (PR #76, squash `5ad3a7c`), this flipped `prompts/greenfield.md` `status: active → resolved`. `resolved` is a handoff/task close-marker; for a live reusable prompt artifact the correct terminal lifecycle state is `active`. TASK-0046 was the **first cycle to ship a `status: active` prompt artifact** (greenfield went `stub → drafted → active` via the path-(α') flip), so it was the first to expose the over-reach. The three intended writes (handoff `linked_pr` backfill + handoff `active → resolved` + review-context `drafted → recorded`) were correct; greenfield was the sole over-swept file.

## Detection

Caught by post-merge §8.1.1.2 verification applied to the **Action's own outputs** (the verify-the-Action-output discipline: the Action's fire signal is verified, not trusted), during TASK-0046 step-15 post-PR cleanup — `git show 5ad3a7c --stat` revealed a third changed file (`prompts/greenfield.md`) beyond the two intended backfill targets. Not surfaced by the Action's success signal, which reported normal completion. This is the same verify-before-assert posture that earlier in the same cycle caught a Codex phantom-action (handoff ledger (IX)).

## Fix

1. **`.github/scripts/linked-pr-fix-up.py`** — `STATUS_TRANSITIONS` application is now path-scoped via a per-transition prefix allowlist (`STATUS_TRANSITION_PATH_PREFIXES`): `active → resolved` applies only to changed files under `docs/handoffs/`; `drafted → recorded` only under `docs/reviews/` + `docs/post-merge-notes/`. Files outside those prefixes (notably `prompts/`, `templates/`) are excluded from status flips. `apply_substitutions()` now takes the file's repo-relative path to make the scoping decision.
2. **`.github/workflows/linked-pr-fix-up.yml`** — header comment corrected to describe the now-implemented path-scoping (closes the documented-but-not-enforced gap).
3. **`prompts/greenfield.md`** — `status: resolved` restored to `status: active` (correct terminal state for a live reusable prompt).

The `PLACEHOLDER_PATTERN` (linked_pr SHA backfill) was **not** part of the defect — it is strict-matched and only the cycle handoff carries the exact placeholder — and was left untouched. The changed-file harvesting (`git diff --name-only`) is also unchanged; only the `STATUS_TRANSITIONS` application became path-scoped.

## Noted residuals (carry-forward — not fixed here)

- **(i) Directory-binding vs placeholder-coupling.** Binding `active → resolved` to `docs/handoffs/` could mis-flip a *successor* handoff if one ever rode in the same squash as the cycle handoff. Non-manifesting today (successor handoffs are authored post-merge in a later cycle, never co-shipped). The more robust future hardening is to couple the `active → resolved` flip to the presence of the `linked_pr` placeholder in the same file (the handoff is the only artifact that carries it), rather than to a directory prefix. Deferred.
- **(ii) "PMN-001 (k)" label collision.** The repo-wide convention uses "PMN-001 (k)" for the chore-fix-up / linked-pr-substitution discipline (per ADR-004 + PMN-007 §4 + the Action name/commits), but PMN-001's literal **Observation (k)** is an unrelated "Builder-uncertainty-escalation" note. The label is established and regex/identity-load-bearing across the ecosystem; a repo-wide relabel is a separate canonical-reconciliation carry-forward, not in scope here.
- **(iii) No script-test infrastructure.** The repo has no `tests/` dir / pytest config / CI test step, so no regression test was added for `apply_substitutions` this chore (per direction: do not add test infra if none exists). Test-coverage gap is a hardening carry-forward: when script-test infra is introduced, add a test asserting handoff `active → resolved`, review-context + PMN `drafted → recorded`, `prompts/` + `templates/` untouched, and `PLACEHOLDER_PATTERN` behavior unchanged.

## Validation plan

This chore guard-skips the Action on its own merge (PR #77's branch matches `^chore/task-[0-9]+-(linked-pr-fix-up|pmn-001-k)$`). The fix's **first live run is the TASK-0047 chore-fix-up**: verify there via §8.1.1.2 that (a) `prompts/retrofit.md` + `prompts/upgrade.md` (which ship at `status: active`) are left **untouched**, and (b) TASK-0047's handoff (`active → resolved`), review-context (`drafted → recorded`), and any co-shipped PMN (`drafted → recorded`) transition **correctly**. Until then, the fix is verified only by code-trace + self-review (no live run).

Note: because PR #77's merge is guard-skipped, `linked_pr` here is **not** auto-backfilled — the owner backfills the PR #77 squash SHA manually post-merge (per the manual chore-fix-up precedent, PR-70 / TASK-0043).

## Cross-references

- **ADR-004** — pre-Actions-batch insertion decision; ships the linked-pr-fix-up Action automating the PMN-001 (k) chore-fix-up substitution discipline.
- **PMN-007 §4** — PMN-001 (k) mechanism-vs-discipline canonicalization.
- **Action files** — `.github/workflows/linked-pr-fix-up.yml` + `.github/scripts/linked-pr-fix-up.py` (the substitution mechanism).
- ("PMN-001 (k)" is the conventional label for this discipline; its substantive home is the references above — see residual (ii).)
- TASK-0046 handoff §10 ledger entry (IX) records the originating over-reach observation.

## Codex review record

Codex pre-commit pass (PR #77 staged tree) — this section is the durable record (no separate cycle handoff for this no-TASK chore).

- **Execution validation: PASS.** Codex ran the fix in its sandbox (bundled Python — unavailable in the Builder's local Windows env, where correctness was established by manual code-trace): `py_compile` clean, and all 8 scoping cases passed — handoff `active → resolved`; review-context + PMN `drafted → recorded`; `prompts/` (`retrofit.md`, `upgrade.md`, `greenfield.md`) + `templates/` untouched; handoff-at-`drafted` untouched; `linked_pr` placeholder backfill path-agnostic; strict-placeholder non-match behavior unchanged.
- **F-1–F-4: clean.** `PLACEHOLDER_PATTERN` integrity (logic byte-unchanged); yml header comment corrected; `prompts/greenfield.md` restored to `status: active`; cross-references resolve (ADR-004 + PMN-007 §4 + Action files).
- **F-5 (MINOR): absorbed path-(a).** The yml's generated chore-fix-up PR-body text still described the unscoped `status: drafted → recorded` ("PMN + canonical-content artifacts") and `active → resolved` ("TASK handoffs"). Updated to mirror the header comment's path-scoped wording (`active → resolved` → `docs/handoffs/`; `drafted → recorded` → `docs/reviews/` + `docs/post-merge-notes/`; prompts/templates excluded). Generated-string text only — no script logic change, no re-execution needed.
