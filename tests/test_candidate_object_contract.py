#!/usr/bin/env python3
from __future__ import annotations

import json
import runpy
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE = runpy.run_path(str(ROOT / "cli" / "validate_candidate_object.py"))
validate_candidate_object = MODULE["validate_candidate_object"]


def main() -> int:
    fixture = ROOT / "fixtures" / "candidate-object.valid.json"
    data = json.loads(fixture.read_text(encoding="utf-8"))

    ok, errors = validate_candidate_object(data)
    if not ok:
        raise SystemExit("fixture failed validation: " + "; ".join(errors))

    print("TEST_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
