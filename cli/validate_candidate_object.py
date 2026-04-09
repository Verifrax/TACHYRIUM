#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ALLOWED_KIND = {"candidate", "draft", "summary", "suggestion", "briefing", "analysis"}
ALLOWED_STATUS = {"subordinate", "review-required", "bounded"}
REQUIRED_KEYS = {"kind", "source_surface", "target_surface", "status", "summary", "payload"}
ALLOWED_KEYS = REQUIRED_KEYS | {"notes"}


def validate_candidate_object(data: object) -> tuple[bool, list[str]]:
    errors: list[str] = []

    if not isinstance(data, dict):
        return False, ["root must be an object"]

    keys = set(data.keys())
    missing = sorted(REQUIRED_KEYS - keys)
    extra = sorted(keys - ALLOWED_KEYS)

    if missing:
        errors.append("missing required keys: " + ", ".join(missing))
    if extra:
        errors.append("unexpected keys: " + ", ".join(extra))

    kind = data.get("kind")
    if kind not in ALLOWED_KIND:
        errors.append("kind must be one of: " + ", ".join(sorted(ALLOWED_KIND)))

    source_surface = data.get("source_surface")
    if not isinstance(source_surface, str) or not source_surface.strip():
        errors.append("source_surface must be a non-empty string")

    target_surface = data.get("target_surface")
    if not isinstance(target_surface, str) or not target_surface.strip():
        errors.append("target_surface must be a non-empty string")

    status = data.get("status")
    if status not in ALLOWED_STATUS:
        errors.append("status must be one of: " + ", ".join(sorted(ALLOWED_STATUS)))

    summary = data.get("summary")
    if not isinstance(summary, str) or not summary.strip():
        errors.append("summary must be a non-empty string")

    payload = data.get("payload")
    if not isinstance(payload, dict):
        errors.append("payload must be an object")

    notes = data.get("notes")
    if notes is not None:
        if not isinstance(notes, list) or any(not isinstance(item, str) for item in notes):
            errors.append("notes must be an array of strings when present")

    return len(errors) == 0, errors


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_candidate_object.py <path>", file=sys.stderr)
        return 2

    path = Path(argv[1])
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"ERROR: file not found: {path}", file=sys.stderr)
        return 2
    except json.JSONDecodeError as exc:
        print(f"ERROR: invalid json: {exc}", file=sys.stderr)
        return 2

    ok, errors = validate_candidate_object(data)
    if ok:
        print("VALID")
        return 0

    print("INVALID", file=sys.stderr)
    for err in errors:
        print(f"- {err}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
