
# TACHYRIUM Documentation Index

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

## Guides

* `docs/OPERATOR_HANDBOOK.md`
* `docs/QUICKSTART.md`
* `docs/TESTING.md`
* `docs/DEVELOPMENT.md`
* `docs/INSTALL.md`
* `docs/ENVIRONMENT.md`
* `docs/PACKAGING.md`
* `docs/MAINTENANCE.md`
* `docs/REPOSITORY_INVENTORY.md`

## Planes

* `docs/planes/PLANES.md`

## Machine-readable

* `schemas/candidate-object.schema.json`
* `schemas/release-manifest.json`
* `schemas/repository-inventory.json`

## Prompting

* `prompts/PROMPT_CONTRACT.md`

## Validation

* `cli/validate_candidate_object.py`
* `cli/check_python_runtime.py`
* `tests/run_all_smoke.py`
* `tests/test_install_smoke.py`

## Executable surfaces

* `app/object_builder.py`
* `app/tachyrium_cli.py`
* `app/generate_candidate_object.py`
* `app/route_candidate_target.py`
* `app/classify_subject.py`
* `app/map_topology.py`
* `app/detect_contradiction.py`
* `app/build_briefing.py`
* `app/run_pipeline.py`

## Package surface

* `pyproject.toml`
* `tachyrium_pkg/__init__.py`
* `tachyrium_pkg/cli.py`
  EOF

cat > docs/REPOSITORY_INVENTORY.md <<'EOF'

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
* `cli/check_python_runtime.py`
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
* `tests/test_package_cli_smoke.py`
* `tests/test_install_smoke.py`

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

## Package surface

* `pyproject.toml`
* `tachyrium_pkg/__init__.py`
* `tachyrium_pkg/cli.py`

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
  EOF

cat > docs/QUICKSTART.md <<'EOF'

# TACHYRIUM Quickstart

## Check runtime compatibility

```bash
make doctor
```

## Validate all fixtures

```bash
make validate-fixtures
```

## Run the unified CLI

```bash
python3 app/tachyrium_cli.py pipeline host-copy
```

## Run the installed package CLI

```bash
python3 -m tachyrium_pkg.cli pipeline host-copy
```

## Run the unified smoke suite

```bash
make smoke
```

## Run install smoke

```bash
make install-smoke
```

## Run full local bounded verification

```bash
make all
```

## Boundary reminder

All outputs remain bounded, subordinate, reviewable, and non-sovereign.
