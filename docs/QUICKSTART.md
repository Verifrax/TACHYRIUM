# TACHYRIUM Quickstart

## Validate the canonical candidate fixture

```bash
python3 cli/validate_candidate_object.py fixtures/candidate-object.valid.json
````

## Run the bounded executable seeds

```bash
python3 app/generate_candidate_object.py host-copy VERIFRAX-SURFACE "Bounded host-copy candidate for review."
python3 app/route_candidate_target.py host-copy "Bounded route for host copy review."
python3 app/classify_subject.py host-copy
python3 app/map_topology.py SYNTAGMARIUM
python3 app/detect_contradiction.py repo-role verification proof-publication
python3 app/build_briefing.py host-copy projection VERIFRAX-SURFACE
python3 app/run_pipeline.py host-copy
```

## Run the smoke tests

```bash
python3 tests/test_candidate_object_contract.py
python3 tests/test_candidate_object_schema_smoke.py
python3 tests/test_generator_smoke.py
python3 tests/test_router_smoke.py
python3 tests/test_classifier_smoke.py
python3 tests/test_topology_smoke.py
python3 tests/test_contradiction_smoke.py
python3 tests/test_briefing_smoke.py
python3 tests/test_pipeline_smoke.py
```

## Boundary reminder

All outputs remain bounded, subordinate, reviewable, and non-sovereign.
