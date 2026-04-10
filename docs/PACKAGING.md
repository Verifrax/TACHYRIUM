# TACHYRIUM Packaging Guide

## Purpose

This guide defines the current packaging surface for TACHYRIUM.

## Current state

TACHYRIUM now has project metadata through `pyproject.toml` and an installable bounded CLI package surface through `tachyrium_pkg`.

## What packaging means here

Packaging does not make TACHYRIUM a sovereign runtime.

Packaging only gives the bounded repository a normalized Python project surface and console entrypoint.

## Current packaging rule

Any future packaging expansion must preserve:

- subordinate output status
- repository boundary compliance
- non-sovereign execution
- alignment with `docs/contracts/BOUNDARY_MANIFEST.md`

## Current bounded metadata anchors

- `pyproject.toml`
- `tachyrium_pkg/__init__.py`
- `tachyrium_pkg/cli.py`
- `RELEASE.md`
- `schemas/release-manifest.json`
- `docs/contracts/BOUNDARY_MANIFEST.md`
