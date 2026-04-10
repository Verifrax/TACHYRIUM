#!/usr/bin/env python3
from __future__ import annotations

import subprocess
from pathlib import Path


COMMANDS = [
    ["python3", "tests/test_candidate_object_contract.py"],
    ["python3", "tests/test_candidate_object_schema_smoke.py"],
    ["python3", "tests/test_generator_smoke.py"],
    ["python3", "tests/test_router_smoke.py"],
    ["python3", "tests/test_classifier_smoke.py"],
    ["python3", "tests/test_topology_smoke.py"],
    ["python3", "tests/test_contradiction_smoke.py"],
    ["python3", "tests/test_briefing_smoke.py"],
    ["python3", "tests/test_pipeline_smoke.py"],
    ["python3", "tests/test_cli_smoke.py"],
    ["python3", "tests/test_package_cli_smoke.py"],
]


def main() -> int:
    root = Path(__file__).resolve().parents[1]

    for cmd in COMMANDS:
        print("RUN", " ".join(cmd))
        subprocess.run(cmd, cwd=root, check=True)

    print("ALL_SMOKE_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
