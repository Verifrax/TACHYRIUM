#!/usr/bin/env python3
from __future__ import annotations

import json
import sys


def build_briefing(subject: str, classification: str, target_surface: str) -> dict:
    return {
        "kind": "briefing",
        "source_surface": "TACHYRIUM",
        "target_surface": "TACHYRIUM",
        "status": "bounded",
        "summary": f"Bounded briefing prepared for {subject}.",
        "payload": {
            "subject": subject,
            "classification": classification,
            "target_surface": target_surface,
            "scope": "bounded"
        },
        "notes": [
            "review required",
            "non-authoritative"
        ]
    }


def main(argv: list[str]) -> int:
    if len(argv) != 4:
        print("usage: build_briefing.py <subject> <classification> <target_surface>", file=sys.stderr)
        return 2

    subject, classification, target_surface = argv[1], argv[2], argv[3]
    print(json.dumps(build_briefing(subject, classification, target_surface), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
