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
            str(root / "app" / "build_briefing.py"),
            "host-copy",
            "projection",
            "VERIFRAX-SURFACE",
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    data = json.loads(proc.stdout)

    if data["kind"] != "briefing":
        raise SystemExit("briefing kind mismatch")
    if data["status"] != "bounded":
        raise SystemExit("briefing status mismatch")
    if data["payload"]["classification"] != "projection":
        raise SystemExit("briefing classification mismatch")
    if data["payload"]["target_surface"] != "VERIFRAX-SURFACE":
        raise SystemExit("briefing target mismatch")

    print("BRIEFING_SMOKE_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
