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
            str(root / "app" / "detect_contradiction.py"),
            "repo-role",
            "verification",
            "proof-publication",
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    data = json.loads(proc.stdout)

    if data["kind"] != "analysis":
        raise SystemExit("contradiction kind mismatch")
    if data["status"] != "bounded":
        raise SystemExit("contradiction status mismatch")
    if data["payload"]["contradiction_detected"] is not True:
        raise SystemExit("contradiction detection mismatch")

    print("CONTRADICTION_SMOKE_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
