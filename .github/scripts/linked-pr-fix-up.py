#!/usr/bin/env python3
"""PMN-001 (k) Linked PR fix-up substitution.

Reads CHANGED_FILES, SQUASH_SHA, PR_NUMBER from environment.
Scans each changed file's frontmatter for canonical placeholder patterns
and applies substitutions in place.

Substitutions (YAML frontmatter only — between leading ``---`` markers):

- ``linked_pr: PR-N (Builder fills with squash SHA post-merge per PMN-001 (k))``
  -> ``linked_pr: PR-N (squash SHA <short-sha>)``
- ``status: drafted`` -> ``status: recorded``
- ``status: active``  -> ``status: resolved``

Outputs ``changes-applied=true|false`` to GITHUB_OUTPUT.

Returns non-zero exit code only on hard error (missing required env, file I/O
failure on a file that should be present). No-placeholder-found is not an
error; it sets ``changes-applied=false`` and exits 0.

Idempotency: re-running on already-substituted files is a no-op (placeholder
text is no longer present, regex doesn't match, nothing to substitute).
"""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path

# Canonical placeholder pattern. Strict match — anything other than this exact
# form (e.g., convention drift, manual edits) won't substitute. That's the
# intended safety property: silent miss, not silent corruption.
PLACEHOLDER_PATTERN = re.compile(
    r'^linked_pr: PR-(\d+) \(Builder fills with squash SHA post-merge per PMN-001 \(k\)\)\s*$',
    re.MULTILINE,
)

# Status field transitions. Other values (e.g., ``partial`` for core.md,
# ``final`` if it exists) are not in the mapping and won't be touched.
STATUS_TRANSITIONS: dict[str, str] = {
    'drafted': 'recorded',
    'active': 'resolved',
}

FRONTMATTER_DELIM = re.compile(r'^---\s*$', re.MULTILINE)

ELIGIBLE_SUFFIXES = {'.md', '.yml', '.yaml'}


def parse_frontmatter_bounds(content: str) -> tuple[int, int] | None:
    """Return (body_start, body_end) of YAML frontmatter, or None if absent.

    Frontmatter requires file content to start with ``---``. Body is the slice
    between the first and second ``---`` delimiter lines.
    """
    if not content.startswith('---'):
        return None
    matches = list(FRONTMATTER_DELIM.finditer(content))
    if len(matches) < 2:
        return None
    return matches[0].end(), matches[1].start()


def apply_substitutions(content: str, short_sha: str) -> tuple[str, bool]:
    """Apply canonical PMN-001 (k) substitutions to the YAML frontmatter.

    Returns ``(new_content, changed)``. Returns ``(content, False)`` if no
    frontmatter is present or no patterns matched.
    """
    bounds = parse_frontmatter_bounds(content)
    if bounds is None:
        return content, False

    fm_start, fm_end = bounds
    head = content[:fm_start]
    fm_body = content[fm_start:fm_end]
    tail = content[fm_end:]

    new_fm = fm_body
    changed = False

    # 1. linked_pr placeholder substitution
    if PLACEHOLDER_PATTERN.search(new_fm):
        new_fm = PLACEHOLDER_PATTERN.sub(
            lambda m: f'linked_pr: PR-{m.group(1)} (squash SHA {short_sha})',
            new_fm,
        )
        changed = True

    # 2. status flips
    for old, new in STATUS_TRANSITIONS.items():
        pattern = re.compile(rf'^status: {re.escape(old)}\s*$', re.MULTILINE)
        if pattern.search(new_fm):
            new_fm = pattern.sub(f'status: {new}', new_fm)
            changed = True

    if changed:
        return head + new_fm + tail, True
    return content, False


def main() -> int:
    pr_number = os.environ.get('PR_NUMBER', '').strip()
    squash_sha = os.environ.get('SQUASH_SHA', '').strip()
    changed_files_raw = os.environ.get('CHANGED_FILES', '')

    if not squash_sha:
        print('::error::SQUASH_SHA env var missing or empty', file=sys.stderr)
        return 1

    short_sha = squash_sha[:7]
    changed_files = [f.strip() for f in changed_files_raw.splitlines() if f.strip()]

    print(
        f'Processing {len(changed_files)} changed file(s) '
        f'for PR #{pr_number} (squash {short_sha})'
    )

    any_changes = False
    for fp in changed_files:
        path = Path(fp)
        if not path.exists():
            # File was deleted in the squash; nothing to substitute
            continue
        if not path.is_file():
            continue
        if path.suffix.lower() not in ELIGIBLE_SUFFIXES:
            continue
        try:
            content = path.read_text(encoding='utf-8')
        except (UnicodeDecodeError, OSError) as exc:
            print(f'::warning::Skipping {fp} ({exc.__class__.__name__}: {exc})')
            continue

        new_content, changed = apply_substitutions(content, short_sha)
        if changed:
            try:
                path.write_text(new_content, encoding='utf-8')
            except OSError as exc:
                print(f'::error::Write failed for {fp} ({exc})', file=sys.stderr)
                return 1
            any_changes = True
            print(f'Substituted: {fp}')

    output_file = os.environ.get('GITHUB_OUTPUT')
    if output_file:
        with open(output_file, 'a', encoding='utf-8') as f:
            f.write(f'changes-applied={"true" if any_changes else "false"}\n')

    if not any_changes:
        print('No canonical placeholder patterns found; chore-fix-up PR will not be opened.')

    return 0


if __name__ == '__main__':
    sys.exit(main())
