#!/usr/bin/env python3
from __future__ import annotations

import json
import sys

from object_builder import build_object

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


def classify_subject(subject: str) -> str:
    return CLASS_MAP.get(subject, "analysis")


def route_subject(subject: str) -> str:
    return ROUTE_MAP.get(subject, "TACHYRIUM")


def build_pipeline_result(subject: str) -> dict:
    classification = classify_subject(subject)
    target_surface = route_subject(subject)
    return build_object(
        kind="briefing",
        source_surface="TACHYRIUM",
        target_surface="TACHYRIUM",
        status="bounded",
        summary=f"Bounded pipeline briefing prepared for {subject}.",
        payload={
            "subject": subject,
            "classification": classification,
            "target_surface": target_surface,
            "pipeline": ["classify", "route", "briefing"],
            "scope": "bounded",
        },
        notes=[
            "review required",
            "non-authoritative",
        ],
    )


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: run_pipeline.py <subject>", file=sys.stderr)
        return 2

    print(json.dumps(build_pipeline_result(argv[1]), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
