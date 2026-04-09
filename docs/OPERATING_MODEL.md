# TACHYRIUM Operating Model

## Purpose

This document defines how TACHYRIUM operates as cognition infrastructure inside the Verifrax stack.

## Operating rule

```text
interpret -> structure -> propose -> route
```

Never:

```text
declare -> authorize -> execute -> finalize
```

## Core loop

1. ingest operator intent or stack state
2. normalize into bounded structures
3. compare against known repo, host, and law boundaries
4. classify ambiguity or contradiction
5. generate candidate outputs
6. route candidate outputs to the correct sovereign or adjacent repo
7. stop before authority, execution, or truth-finalization boundaries

## Review rule

Every TACHYRIUM output must be reviewable as a subordinate artifact.

If an output cannot be safely reviewed as subordinate, it is too strong for this repo.

## Safe output classes

* repo relation maps
* bounded recommendations
* contradiction clusters
* README draft candidates
* host-copy candidates
* issue or repair summaries
* operator briefing objects

## Unsafe output classes

* law changes presented as final
* accepted state mutation
* authority issuance
* execution permission
* receipt generation of record
* verification verdict finalization

## Human control rule

Human or deterministic sovereign systems remain load-bearing where law, state, authority, execution, or truth are involved.

TACHYRIUM may prepare judgment.
TACHYRIUM may not silently replace it.
