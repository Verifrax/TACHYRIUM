#!/usr/bin/env python3
from __future__ import annotations

import json
import sys

from object_builder import build_object

REPO_CLASS_MAP = {
    "SYNTAGMARIUM": "law",
    "ORBISTIUM": "state",
    "CONSONORIUM": "reconciliation",
    "TACHYRIUM": "cognition",
    "VERIFRAX": "authored-source",
    "AUCTORISEAL": "authority",
    "CORPIFORM": "execution",
    "cicullis": "enforcement",
    "VERIFRAX-SURFACE": "projection-infrastructure",
    "VERIFRAX-verify": "verification",
    "proof": "proof-publication",
    "VERIFRAX-DOCS": "docs",
    "VERIFRAX-STATUS": "status",
    "VERIFRAX-WWW": "root",
}


def classify_repo(repo_name: str) -> str:
    return REPO_CLASS_MAP.get(repo_name, "adjacent")


def build_topology_summary(repo_name: str) -> dict:
    repo_class = classify_repo(repo_name)
    return build_object(
        kind="summary",
        source_surface="TACHYRIUM",
        target_surface="TACHYRIUM",
        status="bounded",
        summary=f"Repository {repo_name} mapped to topology class {repo_class}.",
        payload={
            "repo": repo_name,
            "topology_class": repo_class,
            "scope": "bounded",
        },
        notes=[
            "review allowed",
            "non-authoritative",
        ],
    )


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: map_topology.py <repo_name>", file=sys.stderr)
        return 2

    print(json.dumps(build_topology_summary(argv[1]), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
