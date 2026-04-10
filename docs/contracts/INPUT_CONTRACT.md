# TACHYRIUM Input Contract

## Purpose

This document defines the lawful input boundary for TACHYRIUM.

It specifies which inputs may enter TACHYRIUM, how they must be treated, and which input classes are forbidden because they would cause collision with sovereign or adjacent Verifrax surfaces.

## Input axiom

```text
every input must be explicit
every input must be bounded
every input must be non-sovereign unless read-only
````

## Allowed input classes

TACHYRIUM may accept only bounded inputs such as:

* operator prompts
* explicit repo metadata
* explicit host metadata
* explicit package metadata
* explicit artifact metadata
* explicit evidence files
* accepted state references
* contradiction inventories
* repair-plan references
* local files intentionally provided for analysis

## Read-only sovereign inputs

TACHYRIUM may read but may not mutate or impersonate:

* SYNTAGMARIUM law
* ORBISTIUM accepted state
* CONSONORIUM contradiction and repair context
* VERIFRAX evidence-root and authored-source surfaces
* governed repo and host surfaces

## Forbidden input classes

TACHYRIUM must reject, quarantine, or downgrade inputs that attempt to function as:

* constitutional law authored here
* accepted epoch truth authored here
* authority-of-record
* execution permission
* final verification verdict
* hidden undeclared state
* mixed-trust bundles presented as canonical
* convenience prose treated as sovereign override

## Input handling rule

Every input must be treated according to trust position:

* sovereign read-only
* bounded contextual
* subordinate draft material
* untrusted raw material

No input may silently move upward in trust class.

## Stability rule

Implementation must conform downward to this contract.

If an input requires TACHYRIUM to accept sovereign authorship rather than bounded cognition, that input is outside the current lawful scope of the repo.
