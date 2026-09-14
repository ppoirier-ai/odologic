# Cognitive brief spec

Status: first pass, 2026-09-14. This is the v1 product surface. No actions, no delegation,
no agents acting on your behalf. The brief selects context and the map records the
interaction.

## Purpose

You should not have to re explain yourself to every model. A map of your standing
positions, your constraints, and your history of reasoning gets projected down to a
compact brief and injected as context for each LLM interaction. The interaction itself
is written back into the map.

Two jobs exactly:
1. Selection. Pick the right context and the right logic for this turn, and only that.
2. Trace. Record the interaction, including which context was selected, locally.

## What the brief is not

Not a memory dump. Not a personality prompt. Not a summary of the whole map. The brief
is a bounded, per interaction projection. If it does not fit a context budget it is not
a brief.

Not a retrieval of opinions to agree with. This is the central failure mode: a system
that hands an LLM your prior positions will produce a model that mirrors you, and a
mirror is worse than a stranger because it launders your errors back to you as
confirmation. Guard: every retrieved item carries its status and its defeats, and
retrieval explicitly includes items that contradict the current prompt.

## Two tiers

Core, stable, small. Injected every interaction. Identity, current projects, hard
constraints, standing conventions, values held as values. Target a few hundred tokens.
Changes slowly, versioned, human approved.

Retrieved, per interaction. Selected by the signals below for this specific turn.
Everything else in the map stays on disk.

## Retrieval signals, ranked

1. Contradiction. Items you hold that conflict with the current prompt or with a claim
   the model just made. Highest value retrieval, and the reason this is not just memory.
   A mirror retrieves agreement. The brief retrieves disagreement with evidence.
2. Standing. theorem and observation outrank assumption. contested and defeated are
   retrieved only in the contradiction channel, labeled as such, never as positions you
   hold.
3. Scope. Personal, work, project, domain. Work scope items do not surface in personal
   prompts unless the map says to.
4. Recency and activity. Recently touched projects and recently reasoned topics.
5. Similarity. Embedding match, last. It is the cheapest signal and the one every memory
   product already has. It is the tiebreaker, not the mechanism.

## What every retrieved item carries

    content        the claim or position in plain language
    status         theorem | observation | assumption | contested | defeated | unaudited
    scope          personal | work | project:<id> | domain:<name>
    provenance     you | documented source | model proposal, unauthorized
    defeats        attached, never stitched off, never summarized into "roughly"
    date           when it entered and when it was last contested

An item injected without its defeats is a lie of omission. An item injected without
provenance lets model output back in wearing your name.

## Injection rules

1. Values and facts are separate relations. Values are never scored by falsifiability
   and never retrieved as if they were evidence.
2. A model can propose items into the map. A model can never certify one. Proposals
   enter as unaudited and are not injected as standing until you approve.
3. Everything injected is labeled with its provenance. The model must be able to tell
   which context came from you, which came from a document, and which it invented.
4. No defeated item enters the brief as a position you hold.
5. The brief is inspectable. Before or after any interaction you can see exactly what
   was injected. Silent injection is not acceptable in a system that claims traceability.

## Interaction trace

Recorded locally, per interaction, in the map:

    interaction_id
    timestamp
    prompt_hash and prompt        the request, verbatim
    brief_version                 which core revision was live
    selected_items[]              ids of every map item injected, with the signal that
                                  selected each one
    model_id, harness             which model, which client
    output                        verbatim
    claims_extracted[]            claims in the output, each with an id
    new_items_proposed[]          what the model tried to write into the map, unaudited
    user_corrections[]            what you changed afterward

The selected_items field is the point. Recording only prompts and answers gives you a
chat log. Recording which context was selected is the only way to later attribute a bad
answer to a bad injection instead of blaming the model.

## Storage

    map.sqlite
      terms, judgments, certificates, defeats      the existing object model
      agents                                        you, and later machines
      core_brief                                    versioned stable tier
      interactions, selected_items                  the trace
      proposals                                     unaudited model output awaiting review

Local first, no cloud default. The trace is the most sensitive artifact this product
will ever hold. Export must be guaranteed and complete.

## Cold start

An empty map produces an empty brief. Bootstrap from what already exists, not from
interrogating you. Candidate sources in order of value: hard constraints and standing
conventions, current projects and their state, existing written positions (docs, memos,
published pieces), domain knowledge from the wikis, writing and style rules. Each
ingested item enters with provenance and status. Documented claims can be observation or
theorem. Your positions enter as your own. Nothing enters as certified.

## Failure modes

Echo chamber. Guarded by the contradiction channel and by never retrieving agreement as
the primary signal.

Self confirming loop. The map is written by the same models that consume it. Guarded by
proposal versus certification, and by unaudited never being injectable as standing.

Context rot. The brief grows until it is a dump. Guarded by the core budget and by
selection being per turn rather than cumulative.

Trace as liability. The map records your reasoning, so a breach is a full cognitive
dump. Local first is a requirement, not a preference.

## Open questions

1. Core brief authorship. Do you write it, or does it get derived and then approved?
2. Contradiction detection quality. Is embedding similarity enough to find items that
   conflict, or does it need an adjudication pass? Likely the latter, at pennies per turn.
3. Does the brief get injected for every model, or does difficulty gate it? Cost model
   depends on the answer.
4. What is the smallest map that beats no map at all? Worth measuring before building the
   rest.
