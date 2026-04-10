# TACHYRIUM Repository Inventory

## Core

* `README.md`
* `TACHYRIUM.md`
* `RUNTIME.md`
* `RELEASE.md`
* `CHANGELOG.md`

## Contracts

* `docs/interfaces/INTERFACE_CONTRACT.md`
* `docs/contracts/INPUT_CONTRACT.md`
* `docs/contracts/OUTPUT_CONTRACT.md`
* `docs/contracts/BOUNDARY_MANIFEST.md`

## Structure

* `docs/INDEX.md`
* `docs/planes/PLANES.md`

## Machine-readable

* `schemas/candidate-object.schema.json`
* `schemas/release-manifest.json`
* `schemas/repository-inventory.json`

## Prompting

* `prompts/PROMPT_CONTRACT.md`

## Validation

* `cli/validate_candidate_object.py`
* `tests/run_all_smoke.py`
* `tests/test_candidate_object_contract.py`
* `tests/test_candidate_object_schema_smoke.py`
* `tests/test_generator_smoke.py`
* `tests/test_router_smoke.py`
* `tests/test_classifier_smoke.py`
* `tests/test_topology_smoke.py`
* `tests/test_contradiction_smoke.py`
* `tests/test_briefing_smoke.py`
* `tests/test_pipeline_smoke.py`
* `tests/test_cli_smoke.py`

## Bounded executable surfaces

* `app/object_builder.py`
* `app/tachyrium_cli.py`
* `app/generate_candidate_object.py`
* `app/route_candidate_target.py`
* `app/classify_subject.py`
* `app/map_topology.py`
* `app/detect_contradiction.py`
* `app/build_briefing.py`
* `app/run_pipeline.py`

## Fixtures

* `fixtures/candidate-object.valid.json`
* `fixtures/router-candidate.valid.json`
* `fixtures/classification-summary.valid.json`
* `fixtures/topology-summary.valid.json`
* `fixtures/contradiction-analysis.valid.json`
* `fixtures/briefing.valid.json`
* `fixtures/pipeline-briefing.valid.json`

## Example outputs

* `outputs/examples/candidate-object.example.json`
* `outputs/examples/router-candidate.example.json`
* `outputs/examples/classification-summary.example.json`
* `outputs/examples/topology-summary.example.json`
* `outputs/examples/contradiction-analysis.example.json`
* `outputs/examples/briefing.example.json`
* `outputs/examples/pipeline-briefing.example.json`
  