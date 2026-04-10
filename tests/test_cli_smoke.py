#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    proc = subprocess.run(
        ["python3", str(root / "app" / "tachyrium_cli.py"), "pipeline", "host-copy"],
        check=True,
        capture_output=True,
        text=True,
    )
    data = json.loads(proc.stdout)

    if data["kind"] != "briefing":
        raise SystemExit("cli kind mismatch")
    if data["status"] != "bounded":
        raise SystemExit("cli status mismatch")
    if data["payload"]["classification"] != "projection":
        raise SystemExit("cli classification mismatch")
    if data["payload"]["target_surface"] != "VERIFRAX-SURFACE":
        raise SystemExit("cli target mismatch")
    if data["payload"]["pipeline"] != ["classify", "route", "briefing"]:
        raise SystemExit("cli pipeline mismatch")

    print("CLI_SMOKE_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
