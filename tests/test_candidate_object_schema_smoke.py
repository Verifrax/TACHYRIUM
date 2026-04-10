#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    schema_path = root / "schemas" / "candidate-object.schema.json"
    schema = json.loads(schema_path.read_text(encoding="utf-8"))

    required = {"kind", "source_surface", "target_surface", "status", "summary", "payload"}
    props = set(schema.get("properties", {}).keys())

    if schema.get("type") != "object":
        raise SystemExit("schema root type must be object")
    if schema.get("additionalProperties") is not False:
        raise SystemExit("additionalProperties must be false")
    if set(schema.get("required", [])) != required:
        raise SystemExit("required keys mismatch")
    if not required.issubset(props):
        raise SystemExit("properties missing required keys")

    print("SCHEMA_SMOKE_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
