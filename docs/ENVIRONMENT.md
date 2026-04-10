# TACHYRIUM Environment Guide

## Purpose

This guide defines the current interpreter and local runtime expectations for TACHYRIUM.

## Required Python

TACHYRIUM requires Python 3.11 or newer.

## Local runtime check

```bash
python3 cli/check_python_runtime.py
````

## Why this matters

The repository now has:

* bounded packaging metadata
* a bounded console entrypoint
* install smoke validation

Those surfaces should run against an explicit compatible interpreter rather than an ambient system default.

## Normal local rule

Use Python 3.11+ for:

* local installation
* smoke tests
* package CLI usage
* CI parity
  