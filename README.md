# Odologic

 formerly TruthMachine, renamed September 2026

A judgment ledger for machine intelligence. Every claim an LLM asserts or a document
contains is traced along depends_on edges down to a floor of first principles, or it is
marked as ungrounded. Named from Greek hodos (path): odological tracing is the walk from
a standing claim to the floor.

## Status

Design and fixtures phase. Engine intentionally not started. Two questions must be
answered in UI mockups first, per Patrick:

1. How does a user use this on a pure text document, with no LLM in the loop?
2. How does a user use this to audit an LLM's output?

## Layout

    fixtures/                  structured example data, the source of truth for mockups
      teleport_llm.json        LLM audit example: model claims teleportation
      label_doc.json           pure document example: product label groundings
      render.py                fixture to HTML renderer, shared by all mockups
    sketches/                  disposable UI variants
      themes/tokens.css        shared minimal tokens
      001-analyzer/            variant A
      002-workbook/            variant B

## Object model (from the design doc, unchanged)

    Term        concept, entity, event. Never true or false.
    Judgment    claim about Terms, with a status.
    Certificate  evidence: schema, measurement with logged protocol, or labeled axiom.
    Defeat      rebut, undercut, or undermine.

    Statuses: theorem | observation | assumption | contested | defeated | unaudited

## Fixture rules

Fixtures are hand built JSON. No engine, no inference. They encode exactly what the
closer would derive, so the UI conversation happens before the engine exists.
