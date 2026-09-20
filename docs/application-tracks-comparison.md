# Application tracks, and the capital question behind them

Status: first pass, 2026-09-20. Drafted while the sourcing fan out is still running, so this
file has two kinds of content and they are labelled. The analytical sections are settled. Any
number marked PENDING is not yet sourced and must not leave this repo until it carries a source
URL. Companion docs: docs/stakeholder-value-map.md (the value objects and the stakeholder map,
which this file derives from rather than restates), docs/moat-design.md, and
docs/competitive-and-market.md.

The prospective counterparty in this file is the graph accelerator company, referred to from
here as the chip partner. They are kept confidential: no name, and no details that identify
them, anywhere in this repo or in any shared copy.

## What is actually being decided

The chip partner has three things we do not: a graph oriented accelerator, an existing military
and finance book of business, and capital they are willing to spend on applications that run on
their silicon. They also have one specific pain of their own: a very large codebase that current
language models cannot manage, because of context window limits and hallucination. That last
point is not a side note, it is the only place in this whole set where the buyer is describing
his own injury rather than a market that might exist.

So the question is not which application is largest. It is four questions, and they decide
different tracks:

1. Does the buyer already have budget and a named owner, or are we creating the line item.
2. Does the buyer accept a record they do not control, or does custody get demanded on day one.
3. Can a defeat be settled by execution, or does it stay an argument between two people.
4. Does the track pull our chip partner's silicon, or is the silicon incidental.

Question 2 is the one that kills tracks quietly. Question 3 is the one that decides whether the
product is provable in a pilot rather than in a deck.

## The tracks, defined before they are compared

    A regulated finance assurance    banking, insurance, trading desks. Model risk management and
                                     audit already exist and already have owners.
    B healthcare assurance           clinical documentation, regulatory submissions, payer review.
    C military space                 space domain awareness, satellite tasking, command and control
                                     decision audit. Buyer is government, integration via primes.
    D defense codebase comprehension the chip partner's own large codebase and its military
                                     analogues. Comprehension, change impact, hallucination control.
    E accelerated defeasibility      the ledger logic executed on their hardware as a co-designed
                                     capability, sold as silicon differentiation.
    F OEM into their book            Odologic as an application inside their existing military and
                                     finance customer relationships.

F is not really an application, it is a channel, and it applies to A, B, C and D. It is kept
separate because its sales cycle and cash flow profile are completely different from the same
product sold direct, and that difference is the whole point of the partnership.

## D is the strongest first move, and the reason is not the size of the market

Four reasons, and the first is structural rather than commercial.

1. Code is the only domain in this set where a defeat can be settled by execution. A build
   failure, a failing test, a dependency that does not exist, a call that breaks a downstream
   contract: each one is a computable defeat, not an opinion about an opinion. The claim status
   lifecycle stops being a schema we assert and becomes a status that a machine can enforce. In
   every other track we have to argue that defeasibility is real. Here we can show it.
2. The alternative the buyer faces is a frontier model over a context window, and that
   alternative is disqualified in the defense setting for reasons that have nothing to do with
   quality: air gapped or classified environments, export control, and no cloud egress. The
   answer is a local model on local silicon plus a local ledger, which is precisely the shape
   the chip partner sells. This is the one track where their hardware is not incidental.
3. The user of the product is a person whose judgment the ledger is actually recording, an
   engineer with a named stake in the claim, rather than a committee. That restores the V1
   value object (the individual cognitive map, docs/stakeholder-value-map.md) as the unit of
   accumulation, instead of starting with the employer custody fight.
4. It is testable on a corpus we do not have to build. The chip partner's own codebase is the
   first customer, the first benchmark and the first reference. That is the cheapest possible
   cold start anywhere in this file.

The honest caveat: doctrine and compliance obligations in defense software are matched today by
process artefacts (requirements traceability, code review records, configuration management),
and a reviewer can say "we already have traceability". The answer is the same as the GraphRAG
answer and it has to be demonstrated, not asserted: traceability shows which requirement a line
of code came from, and it does not show which claim about the system was defeated, by what, and
by whom. PENDING: the specific doctrine names and the specific traceability artefacts they
mandate, with sources.

## Where the chip partner's money is worth taking, and where it is not

They are offering to fund applications. That is a development contract, not a round, and the
distinction matters more here than it usually does, because it decides whether Odologic stays
neutral and whether it stays the owner of the schema.

    structure                        what it is                    effect on neutrality and control
    milestone development contract   they pay for a named port or   accepted, non dilutive, deliverables
                                     reference application, per      are a working artefact and a benchmark
                                     milestone, no equity
    joint go to market               co sell into their book, split  accepted only if the record stays ours
                                     revenue, they keep the silicon  and export stays guaranteed
    reference design royalty         they pay per unit or per       accepted, and it is the only structure
                                     deployment if the ledger runs   where their hardware advantage and our
                                     as silicon differentiation      schema both convert to money
    strategic equity investment      they take a position            rank last. It converts the chip partner
                                                                     into a conflicted party in exactly the
                                                                     way docs/moat-design.md says the
                                                                     company dies: aligned with one
                                                                     landlord, therefore not neutral across
                                                                     the rest.

One hard condition, stated now rather than discovered in diligence: no structure may give the
chip partner custody of a customer's ledger, and none may make the record unexportable. If the
deal requires either, the capital is not worth the position, and that is the same verdict the
moat doc already reached about custody in general.

## PENDING, the six numbers per track

Nothing below has been filled in. The fan out is gathering the following, and each row needs a
source URL before it appears here.

    track   capital to     capital to     sales cycle   near term      three year     moat
            first revenue  market scale   length        cash flow      revenue band   durability
    A
    B
    C
    D
    E
    F

Also pending, and load bearing:

1. What an air gapped deployment inside a defense environment actually requires, and what that
   adds to cost and time per track (accreditation, personnel, facilities).
2. What the American procurement vehicles pay at each stage, named, and how long each takes
   from application to cash.
3. What a graph or accelerator port actually costs in engineering months, and how much of it is
   paid by the silicon vendor rather than by the application company, by precedent.
4. Measured performance of current language models on very large codebases, and whether the
   failure is reported as context window exhaustion, hallucinated dependencies, or both.
5. Defense software sustainment spend, from budget documents rather than from vendor sponsored
   marketing.

## Open decisions this file creates

1. If D is first, does the pitch to the chip partner become a codebase comprehension pilot
   priced as development work, or does it become the reference application in the OEM structure.
2. Does the accelerated defeasibility track (E) begin as a paid feasibility study or as a
   joint reference design. E is the only track where our logic becomes their specification.
3. Military space (C) needs a partner who already holds the contract vehicle. The chip partner
   has military clients, but a military client is not the same as a military space program of
   record, and that gap has to be checked before C is costed.
4. Confidentiality: how much of the chip partner's architecture can appear in an internal
   business model at all, given the export control regime their customers sit under.
