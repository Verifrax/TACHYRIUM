from __future__ import annotations

import json
import sys

from tachyrium_pkg.runtime import (
    classify_subject,
    generate_candidate,
    pipeline_result,
    route_candidate,
)

USAGE = "usage: tachyrium <generate|route|classify|topology|contradiction|briefing|pipeline> ..."


def _topology(subject: str) -> dict:
    return {
        "kind": "summary",
        "source_surface": "TACHYRIUM",
        "target_surface": "TACHYRIUM",
        "status": "bounded",
        "summary": f"Repository {subject} mapped for bounded topology handling.",
        "payload": {
            "subject": subject,
            "topology_class": "law" if subject == "SYNTAGMARIUM" else "analysis",
            "scope": "bounded",
        },
        "notes": ["review allowed", "non-authoritative"],
    }


def _contradiction(current: str, proposed: str) -> dict:
    return {
        "kind": "analysis",
        "source_surface": "TACHYRIUM",
        "target_surface": "TACHYRIUM",
        "status": "bounded",
        "summary": "Bounded contradiction analysis prepared.",
        "payload": {
            "current": current,
            "proposed": proposed,
            "scope": "bounded",
        },
        "notes": ["review required", "non-authoritative"],
    }


def _briefing(subject: str, summary: str) -> dict:
    return {
        "kind": "briefing",
        "source_surface": "TACHYRIUM",
        "target_surface": "TACHYRIUM",
        "status": "bounded",
        "summary": summary,
        "payload": {
            "subject": subject,
            "scope": "bounded",
        },
        "notes": ["review required", "non-authoritative"],
    }


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)

    if not args:
        print(USAGE, file=sys.stderr)
        return 2

    command = args[0]

    if command == "pipeline":
        if len(args) != 2:
            print("usage: tachyrium pipeline <subject>", file=sys.stderr)
            return 2
        obj = pipeline_result(args[1])
    elif command == "classify":
        if len(args) != 2:
            print("usage: tachyrium classify <subject>", file=sys.stderr)
            return 2
        obj = classify_subject(args[1])
    elif command == "route":
        if len(args) != 3:
            print("usage: tachyrium route <subject> <summary>", file=sys.stderr)
            return 2
        obj = route_candidate(args[1], args[2])
    elif command == "generate":
        if len(args) != 4:
            print("usage: tachyrium generate <subject> <target_surface> <summary>", file=sys.stderr)
            return 2
        obj = generate_candidate(args[1], args[2], args[3])
    elif command == "topology":
        if len(args) != 2:
            print("usage: tachyrium topology <subject>", file=sys.stderr)
            return 2
        obj = _topology(args[1])
    elif command == "contradiction":
        if len(args) != 3:
            print("usage: tachyrium contradiction <current> <proposed>", file=sys.stderr)
            return 2
        obj = _contradiction(args[1], args[2])
    elif command == "briefing":
        if len(args) != 3:
            print("usage: tachyrium briefing <subject> <summary>", file=sys.stderr)
            return 2
        obj = _briefing(args[1], args[2])
    else:
        print(USAGE, file=sys.stderr)
        return 2

    print(json.dumps(obj, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
