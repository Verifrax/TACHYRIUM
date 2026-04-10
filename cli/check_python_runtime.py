#!/usr/bin/env python3

import sys


def main() -> int:
    v = sys.version_info
    if (v.major, v.minor) < (3, 11):
        print(f"PYTHON_RUNTIME_TOO_OLD: {v.major}.{v.minor} (need 3.11+)")
        return 1

    print(f"PYTHON_RUNTIME_OK: {v.major}.{v.minor}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
