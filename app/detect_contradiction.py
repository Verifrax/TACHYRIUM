#!/usr/bin/env python3
from __future__ import annotations

import json
import sys

from object_builder import build_object


def detect(subject: str, current: str, proposed: str) -> dict:
    contradicted = current.strip() != proposed.strip()
    return build_object(
        kind="analysis",
        source_surface="TACHYRIUM",
        target_surface="TACHYRIUM",
        status="bounded",
        summary=f"Contradiction analysis completed for {subject}.",
        payload={
            "subject": subject,
            "current": current,
            "proposed": proposed,
            "contradiction_detected": contradicted,
            "scope": "bounded",
        },
        notes=[
            "review required",
            "non-authoritative",
        ],
    )


def main(argv: list[str]) -> int:
    if len(argv) != 4:
        print("usage: detect_contradiction.py <subject> <current> <proposed>", file=sys.stderr)
        return 2

    print(json.dumps(detect(argv[1], argv[2], argv[3]), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
