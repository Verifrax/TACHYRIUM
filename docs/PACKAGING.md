# TACHYRIUM Packaging Guide

## Purpose

This guide defines the current packaging surface for TACHYRIUM.

## Current state

TACHYRIUM now has project metadata through `pyproject.toml`.

This packaging surface exists for repository identity, release coherence, and future bounded install normalization.

## What packaging means here

Packaging does not make TACHYRIUM a sovereign runtime.

Packaging only gives the bounded repository a normalized Python project surface.

## Current packaging rule

Any future packaging expansion must preserve:

- subordinate output status
- repository boundary compliance
- non-sovereign execution
- alignment with `docs/contracts/BOUNDARY_MANIFEST.md`

## Current bounded metadata anchors

- `pyproject.toml`
- `RELEASE.md`
- `schemas/release-manifest.json`
- `docs/contracts/BOUNDARY_MANIFEST.md`
