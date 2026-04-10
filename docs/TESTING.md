# TACHYRIUM Testing Guide

## Purpose

This guide defines the current bounded testing surface for TACHYRIUM.

## Validation entrypoints

### Canonical fixture validation

```bash
python3 cli/validate_candidate_object.py fixtures/candidate-object.valid.json
python3 cli/validate_candidate_object.py fixtures/router-candidate.valid.json
python3 cli/validate_candidate_object.py fixtures/classification-summary.valid.json
python3 cli/validate_candidate_object.py fixtures/topology-summary.valid.json
python3 cli/validate_candidate_object.py fixtures/contradiction-analysis.valid.json
python3 cli/validate_candidate_object.py fixtures/briefing.valid.json
python3 cli/validate_candidate_object.py fixtures/pipeline-briefing.valid.json
````

### Unified smoke run

```bash
python3 tests/run_all_smoke.py
```

## Test rule

Every executable cognition surface added to TACHYRIUM should have:

* at least one bounded fixture
* at least one smoke test
* continued compatibility with subordinate output validation

## Boundary rule

Passing tests does not elevate outputs into sovereign truth, authority, execution legitimacy, enforcement, or final verification.
