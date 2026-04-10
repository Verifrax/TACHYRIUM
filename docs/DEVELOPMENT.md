# TACHYRIUM Development Guide

## Purpose

This guide gives a single bounded developer workflow for the current repository state.

## Task runner

Use the repository `Makefile` for the normalized local workflow.

## Commands

### Validate all fixtures

```bash
make validate-fixtures
```

### Run the unified smoke suite

```bash
make smoke
```

### Run full local bounded verification

```bash
make all
```

### Run the unified bounded CLI

```bash
python3 app/tachyrium_cli.py pipeline host-copy
```

## Rule

These commands verify bounded cognition surfaces only.

They do not elevate any output into sovereign truth, authority, execution legitimacy, enforcement, or final verification.
