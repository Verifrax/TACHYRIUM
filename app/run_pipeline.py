#!/usr/bin/env python3
from __future__ import annotations

import json
import sys

from tachyrium_pkg.runtime import pipeline_result

def build_pipeline_result(subject: str) -> dict:
    return pipeline_result(subject)


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: run_pipeline.py <subject>", file=sys.stderr)
        return 2

    print(json.dumps(build_pipeline_result(argv[1]), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
