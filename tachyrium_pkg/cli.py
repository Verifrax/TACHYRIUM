from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

COMMANDS = {
    "generate": "app/generate_candidate_object.py",
    "route": "app/route_candidate_target.py",
    "classify": "app/classify_subject.py",
    "topology": "app/map_topology.py",
    "contradiction": "app/detect_contradiction.py",
    "briefing": "app/build_briefing.py",
    "pipeline": "app/run_pipeline.py",
}


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv if argv is None else argv)
    if len(args) < 2 or args[1] not in COMMANDS:
        print(
            "usage: tachyrium <generate|route|classify|topology|contradiction|briefing|pipeline> ...",
            file=sys.stderr,
        )
        return 2

    cmd = [sys.executable, str(ROOT / COMMANDS[args[1]]), *args[2:]]
    proc = subprocess.run(cmd, text=True, capture_output=True)

    if proc.stdout:
        print(proc.stdout, end="")
    if proc.stderr:
        print(proc.stderr, end="", file=sys.stderr)

    return proc.returncode


if __name__ == "__main__":
    raise SystemExit(main())
