#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    proc = subprocess.run(
        ["python3", "-m", "tachyrium_pkg.cli", "pipeline", "host-copy"],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
    )
    data = json.loads(proc.stdout)

    if data["kind"] != "briefing":
        raise SystemExit("package cli kind mismatch")
    if data["status"] != "bounded":
        raise SystemExit("package cli status mismatch")
    if data["payload"]["classification"] != "projection":
        raise SystemExit("package cli classification mismatch")
    if data["payload"]["target_surface"] != "VERIFRAX-SURFACE":
        raise SystemExit("package cli target mismatch")

    print("PACKAGE_CLI_SMOKE_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
