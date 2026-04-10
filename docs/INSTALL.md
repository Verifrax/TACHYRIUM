# TACHYRIUM Install Guide

## Purpose

This guide defines the current bounded installation surface for TACHYRIUM.

## Python requirement

TACHYRIUM currently requires Python 3.11 or newer.

## Local install

Create a virtual environment with a compatible interpreter and install the repository locally:

```bash
python3.11 -m venv .venv
. .venv/bin/activate
python3 -m pip install .
````

## Console entrypoint

After installation, the bounded CLI is available as:

```bash id="2jv0qs"
tachyrium pipeline host-copy
```

## Install smoke

You can explicitly point the smoke test at a compatible interpreter:

```bash id="g2c4iy"
TACHYRIUM_PYTHON=python3.11 python3 tests/test_install_smoke.py
```

## Boundary rule

Installation does not change repository sovereignty.

The installed command still emits bounded, subordinate, reviewable outputs only.
