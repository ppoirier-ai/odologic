# Odologic

A judgment ledger for machine intelligence. Every claim an LLM asserts or a document
contains is traced along depends_on edges down to a floor of first principles, or it is
marked as ungrounded. Named from Greek hodos (path): odological tracing is the walk from
a standing claim to the floor.

## What it does

Every text you or your AI agent relies on makes claims. Odologic takes each claim,
requires evidence for it, and traces it down a chain of dependencies to first principles,
or marks it: assumption, contested, defeated, or unaudited. Nothing stands on fluency alone.

The result:

- Your AI agent stops asserting things that are provably false, because its output is
  checked against a ledger of standing, defeated, and contested claims.
- You learn which claims in any document actually hold, which are marketing, and
  which are contradicted by evidence you did not know existed.
- Every defeat is kept and becomes a hard negative, so agents get smarter with use,
  not just better at guessing.

## Status

Design and fixtures phase. Engine intentionally not started. The user-facing system is
being nailed down first, in UI mockups and fixtures, so the backend serves a real usage
model instead of an imagined one. Two flows define the product:

1. Paste a plain document, get every claim grounded or marked. No LLM required.
2. Audit an LLM's output, see which assertions survive tracing.

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
