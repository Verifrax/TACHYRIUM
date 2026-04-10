
# TACHYRIUM Testing Guide

## Purpose

This guide defines the current bounded testing surface for TACHYRIUM.

## Validation entrypoints

### Check runtime compatibility

```bash
make doctor
```

### Validate all fixtures

```bash
make validate-fixtures
```

### Run unified smoke run

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

## Test rule

Every executable cognition surface added to TACHYRIUM should have:

* at least one bounded fixture
* at least one smoke test
* continued compatibility with subordinate output validation

## Boundary rule

Passing tests does not elevate outputs into sovereign truth, authority, execution legitimacy, enforcement, or final verification.
