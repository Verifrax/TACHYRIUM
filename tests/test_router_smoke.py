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
            str(root / "app" / "route_candidate_target.py"),
            "host-copy",
            "Bounded route for host copy review.",
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    data = json.loads(proc.stdout)

    if data["kind"] != "candidate":
        raise SystemExit("router kind mismatch")
    if data["source_surface"] != "TACHYRIUM":
        raise SystemExit("router source_surface mismatch")
    if data["target_surface"] != "VERIFRAX-SURFACE":
        raise SystemExit("router target_surface mismatch")
    if data["status"] != "subordinate":
        raise SystemExit("router status mismatch")
    if data["payload"]["intent"] != "route":
        raise SystemExit("router intent mismatch")

    print("ROUTER_SMOKE_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
