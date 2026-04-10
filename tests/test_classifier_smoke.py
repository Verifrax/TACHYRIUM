#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    proc = subprocess.run(
        ["python3", str(root / "app" / "classify_subject.py"), "host-copy"],
        check=True,
        capture_output=True,
        text=True,
    )
    data = json.loads(proc.stdout)

    if data["kind"] != "summary":
        raise SystemExit("classifier kind mismatch")
    if data["source_surface"] != "TACHYRIUM":
        raise SystemExit("classifier source mismatch")
    if data["target_surface"] != "TACHYRIUM":
        raise SystemExit("classifier target mismatch")
    if data["status"] != "bounded":
        raise SystemExit("classifier status mismatch")
    if data["payload"]["classification"] != "projection":
        raise SystemExit("classifier classification mismatch")

    print("CLASSIFIER_SMOKE_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
