#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    proc = subprocess.run(
        ["python3", str(root / "app" / "run_pipeline.py"), "host-copy"],
        check=True,
        capture_output=True,
        text=True,
    )
    data = json.loads(proc.stdout)

    if data["kind"] != "briefing":
        raise SystemExit("pipeline kind mismatch")
    if data["status"] != "bounded":
        raise SystemExit("pipeline status mismatch")
    if data["payload"]["classification"] != "projection":
        raise SystemExit("pipeline classification mismatch")
    if data["payload"]["target_surface"] != "VERIFRAX-SURFACE":
        raise SystemExit("pipeline target mismatch")
    if data["payload"]["pipeline"] != ["classify", "route", "briefing"]:
        raise SystemExit("pipeline stages mismatch")

    print("PIPELINE_SMOKE_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
