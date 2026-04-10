#!/usr/bin/env python3
from __future__ import annotations

import json
import sys

from object_builder import build_object


def build_candidate(subject: str, target_surface: str, summary: str) -> dict:
    return build_object(
        kind="candidate",
        source_surface="TACHYRIUM",
        target_surface=target_surface,
        status="subordinate",
        summary=summary,
        payload={
            "subject": subject,
            "intent": "draft",
            "scope": "bounded",
        },
        notes=[
            "review required",
            "non-authoritative",
        ],
    )


def main(argv: list[str]) -> int:
    if len(argv) != 4:
        print("usage: generate_candidate_object.py <subject> <target_surface> <summary>", file=sys.stderr)
        return 2

    subject, target_surface, summary = argv[1], argv[2], argv[3]
    print(json.dumps(build_candidate(subject, target_surface, summary), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
