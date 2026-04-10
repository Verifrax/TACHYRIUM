#!/usr/bin/env python3
from __future__ import annotations

import json
import sys

from object_builder import build_object

ROUTE_MAP = {
    "host-copy": "VERIFRAX-SURFACE",
    "readme-draft": "VERIFRAX",
    "evidence-summary": "VERIFRAX",
    "authority-clarification": "AUCTORISEAL",
    "execution-clarification": "CORPIFORM",
    "verification-guidance": "VERIFRAX-verify",
    "proof-organization": "proof",
    "docs-draft": "VERIFRAX-DOCS",
    "status-summary": "VERIFRAX-STATUS",
    "topology-summary": "ARCHITECTURE",
}


def route_subject(subject: str) -> str:
    return ROUTE_MAP.get(subject, "TACHYRIUM")


def build_routed_candidate(subject: str, summary: str) -> dict:
    return build_object(
        kind="candidate",
        source_surface="TACHYRIUM",
        target_surface=route_subject(subject),
        status="subordinate",
        summary=summary,
        payload={
            "subject": subject,
            "intent": "route",
            "scope": "bounded",
        },
        notes=[
            "review required",
            "non-authoritative",
        ],
    )


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print("usage: route_candidate_target.py <subject> <summary>", file=sys.stderr)
        return 2

    subject, summary = argv[1], argv[2]
    print(json.dumps(build_routed_candidate(subject, summary), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
