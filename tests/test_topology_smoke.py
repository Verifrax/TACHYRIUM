#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    proc = subprocess.run(
        ["python3", str(root / "app" / "map_topology.py"), "SYNTAGMARIUM"],
        check=True,
        capture_output=True,
        text=True,
    )
    data = json.loads(proc.stdout)

    if data["kind"] != "summary":
        raise SystemExit("topology kind mismatch")
    if data["source_surface"] != "TACHYRIUM":
        raise SystemExit("topology source mismatch")
    if data["target_surface"] != "TACHYRIUM":
        raise SystemExit("topology target mismatch")
    if data["status"] != "bounded":
        raise SystemExit("topology status mismatch")
    if data["payload"]["topology_class"] != "law":
        raise SystemExit("topology classification mismatch")

    print("TOPOLOGY_SMOKE_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
