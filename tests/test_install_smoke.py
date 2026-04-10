#!/usr/bin/env python3

import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path

root = Path.cwd()

requested = os.environ.get("TACHYRIUM_PYTHON")
candidates = [requested] if requested else ["python3.13", "python3.12", "python3.11"]

base_python = None
for name in candidates:
    if name and shutil.which(name):
        base_python = name
        break

if base_python is None:
    print("INSTALL_SMOKE_SKIPPED: no python3.11+ interpreter found locally")
    raise SystemExit(0)

with tempfile.TemporaryDirectory() as td:
    venv = Path(td) / "venv"

    subprocess.run([base_python, "-m", "venv", str(venv)], cwd=root, check=True)

    py = venv / "bin" / "python"
    tachyrium = venv / "bin" / "tachyrium"

    subprocess.run([str(py), "-m", "pip", "install", str(root)], cwd=root, check=True)

    proc = subprocess.run(
        [str(tachyrium), "pipeline", "host-copy"],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
    )
    data = json.loads(proc.stdout)

    if data["kind"] != "briefing":
        raise SystemExit("install smoke kind mismatch")
    if data["status"] != "bounded":
        raise SystemExit("install smoke status mismatch")
    if data["payload"]["classification"] != "projection":
        raise SystemExit("install smoke classification mismatch")
    if data["payload"]["target_surface"] != "VERIFRAX-SURFACE":
        raise SystemExit("install smoke target mismatch")

print("INSTALL_SMOKE_OK")
