#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    proc = subprocess.run(
        [
            "python3",
            str(root / "app" / "generate_candidate_object.py"),
            "host-copy",
            "VERIFRAX-SURFACE",
            "Bounded host-copy candidate for review.",
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    data = json.loads(proc.stdout)

    if data["kind"] != "candidate":
        raise SystemExit("generator kind mismatch")
    if data["source_surface"] != "TACHYRIUM":
        raise SystemExit("generator source_surface mismatch")
    if data["target_surface"] != "VERIFRAX-SURFACE":
        raise SystemExit("generator target_surface mismatch")
    if data["status"] != "subordinate":
        raise SystemExit("generator status mismatch")

    print("GENERATOR_SMOKE_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
