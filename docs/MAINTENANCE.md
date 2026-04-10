# TACHYRIUM Maintenance Guide

## Purpose

This guide defines how to maintain TACHYRIUM without boundary drift.

## Maintenance priorities

1. preserve repository role
2. preserve subordinate output status
3. preserve machine-readable legibility
4. preserve smoke-test coverage
5. align public documentation with actual repository state

## Before merging new work

Check:

- README still matches actual repo state
- boundary manifest still matches executable surfaces
- release state still matches repository maturity
- inventory still matches files present
- smoke tests still pass
- no executable surface crossed into sovereign behavior

## Drift signals

The repository is drifting if a change tries to:

- define law
- define accepted truth
- authorize action
- perform execution of record
- produce final enforcement
- produce final verification truth

## Corrective rule

If a change increases sovereignty rather than bounded cognition, stop and redirect it out of TACHYRIUM.
