
# TACHYRIUM Development Guide

## Purpose

This guide gives a single bounded developer workflow for the current repository state.

## Task runner

Use the repository `Makefile` for the normalized local workflow.

## Commands

### Check runtime compatibility

```bash
make doctor
```

### Validate all fixtures

```bash
make validate-fixtures
```

### Run the unified smoke suite

```bash
make smoke
```

### Run install smoke

```bash
make install-smoke
```

### Run full local bounded verification

```bash
make all
```

### Run the unified bounded CLI

```bash
python3 app/tachyrium_cli.py pipeline host-copy
```

### Run the package CLI module

```bash
python3 -m tachyrium_pkg.cli pipeline host-copy
```

## Rule

These commands verify bounded cognition surfaces only.

They do not elevate any output into sovereign truth, authority, execution legitimacy, enforcement, or final verification.
