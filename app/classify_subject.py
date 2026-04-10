#!/usr/bin/env python3
from __future__ import annotations

import json
import sys


CLASS_MAP = {
    "host-copy": "projection",
    "readme-draft": "projection",
    "docs-draft": "projection",
    "topology-summary": "topology",
    "evidence-summary": "analysis",
    "authority-clarification": "analysis",
    "execution-clarification": "analysis",
    "verification-guidance": "routing",
    "proof-organization": "routing",
    "status-summary": "analysis",
}


def classify_subject(subject: str) -> dict:
    classification = CLASS_MAP.get(subject, "analysis")
    return {
        "kind": "summary",
        "source_surface": "TACHYRIUM",
        "target_surface": "TACHYRIUM",
        "status": "bounded",
        "summary": f"Subject {subject} classified for bounded cognition handling.",
        "payload": {
            "subject": subject,
            "classification": classification,
            "scope": "bounded"
        },
        "notes": [
            "review allowed",
            "non-authoritative"
        ]
    }


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: classify_subject.py <subject>", file=sys.stderr)
        return 2

    print(json.dumps(classify_subject(argv[1]), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
