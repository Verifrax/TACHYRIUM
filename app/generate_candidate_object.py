#!/usr/bin/env python3
from __future__ import annotations

import json
import sys


def build_candidate(subject: str, target_surface: str, summary: str) -> dict:
    return {
        "kind": "candidate",
        "source_surface": "TACHYRIUM",
        "target_surface": target_surface,
        "status": "subordinate",
        "summary": summary,
        "payload": {
            "subject": subject,
            "intent": "draft",
            "scope": "bounded"
        },
        "notes": [
            "review required",
            "non-authoritative"
        ]
    }


def main(argv: list[str]) -> int:
    if len(argv) != 4:
        print("usage: generate_candidate_object.py <subject> <target_surface> <summary>", file=sys.stderr)
        return 2

    subject, target_surface, summary = argv[1], argv[2], argv[3]
    obj = build_candidate(subject, target_surface, summary)
    print(json.dumps(obj, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
