# Investor framing: problem, solution, and the value matrix

Status: first pass, 2026-09-14. Sits under the inspectability axis doc
(docs/inspectability-axis-why-now.md) and the landscape doc
(docs/competitive-and-market.md). Numbers referenced here are sourced in those two files.

# Part 1, problem and solution

## The one line

Every previous tool you offloaded thinking to could show its work. The model cannot. Odologic is
the ledger that puts the work back.

## The problem, in three layers

Say the layers in order, because each one is sold to a different listener.

Layer 1, the answer became cheap. A frontier model will produce a confident, well formatted
answer to almost any question you can pose. Capability is no longer the constraint, and every
dollar of it makes the interface layer more valuable, not less.

Layer 2, the derivation disappeared. The model is non deterministic, keeps no replayable trace,
and its self reported reasoning is unfaithful. So there is no way to walk from a conclusion back
to the ground it stands on. Every earlier cognitive tool that absorbed delegation was safe
because its substrate was inspectable by construction: arithmetic on paper shows its work, and a
spreadsheet recomputes on demand and can be traced, cell to cell, back to its sources. When
spreadsheets started producing errors in finance and in published economics, the industry
responded with dependency tracing, not abandonment. The model is the first tool in that line
that took the judgment layer and returned nothing inspectable.

Layer 3, nobody owns the record. The person does not have one. The lab cannot provide one,
because it is not neutral, it sells to the operator rather than the person, and it cannot hold a
record that must survive switching to its competitor. The enterprise holds a compliance artefact
instead, a risk register row or a logged decision event, which records that a decision happened
and never what it rested on. So the thing every knowledge worker now generates in volume,
reasoning with a model, is the one thing with no owner and no on file record.

## Why the existing tools do not fix it

Four groups, one gap. Governance and GRC platforms record policies, controls and attestations.
Observability and evaluation platforms record traces, spans and scores. Guardrails and grounding
stacks can show you a source and cannot show you what defeated what. Argument mapping and note
tools prove people will maintain structured claims and give them away free, without a status
lifecycle, a defeat relation, or anything a model can consume. Provenance is solved as a
standard, W3C PROV-O exists, and no standards body has a vocabulary for defeasibility.

## The solution

One sentence: Odologic is a user owned ledger of judgment, recording claims with status,
attachments of defeat, and provenance, and projecting a compact brief into whatever model you
are talking to.

Two jobs, exactly. Selection: pick the right context and the right logic for this turn, and only
that. Trace: record the interaction locally, including which items were selected and by what
signal.

What that produces, concretely. A claim has status (theorem, observation, assumption, contested,
defeated). Defeats are attached, never summarised away. Provenance is first class, so model
output can never re enter the map wearing your name. A model may propose items and may never
certify one. The brief is inspectable before or after the interaction, and the trace records
which context was selected, which is the only way to attribute a bad answer to a bad injection
instead of blaming the model.

## Why now

Why an audit layer, why next to a model, why not earlier: because the model is the first
cognitive tool whose delegated layer left nothing inspectable, and because the layer it took was
the scarce one. Atrophy concentrates in whatever layer you hand over. Handing over arithmetic is
free. Handing over judgment hands over the binding constraint. That is the whole reason the
industry needs a layer beside the model rather than inside it.

## What we do not claim

Say these out loud, they buy credibility:

1. Not mind reading. The ledger reconstructs the envelope, inputs, permissions, actions,
   outcomes, plus the human's stated positions. Self reported chain of thought is not evidence.
2. Not a substitute for a model, and no capability race. Odologic does not out reason anything.
3. Not a truth engine. It records who holds what, with what status, defeated by what. It does not
   decide what is true.
4. Not a proven market. The category does not exist yet, which is why the argument leans on the
   Excel analogy rather than on comparables.

# Part 2, the value matrix and the business model

## The two axes

Rows: who holds the judgment. Columns: what the buyer is paying for.

    who holds it      pays for performance              pays for accountability
    human alone       nothing, this is the old world    calibration, personal track record
    human plus model  the brief, faster and cheaper     the trace, the ledger, export
    model alone       nobody pays, or the lab pays      attestation, containment, evidence

Read it as a map of where value sits today and where it moves.

    cell                                  buyer today                value direction
    human alone, performance              none                       flat
    human alone, accountability           the person, later employers rising
    human plus model, performance         the person, per seat        falling as models improve
    human plus model, accountability      the person, the enterprise  rising
    model alone, performance              labs, and it deflates       falling
    model alone, accountability           enterprises, insurers, labs rising, speculative

## Where AGI fits

The matrix is a forecast, not a snapshot, and the point is that the columns invert as capability
rises.

Stage 1, now. Performance is the easy sell. A person pays because briefing every model wastes
their time. Accountability is a smaller, more durable sale to the same person. Revenue: consumer
and prosumer subscription, priced attached to a seat they already pay for (Copilot is $30 per
user per month, ChatGPT Business premium $100, so a judgment layer at a fraction of that never
requests a new budget line).

Stage 2, mid. Performance demand softens as models need less briefing, and the enterprise
becomes the buyer of record: an organisation wants an aggregated, consented view of how its
people reason, with dissent preserved and provenance intact. Revenue: enterprise aggregation and
governance, which is the core B2B line in the earlier brainstorm, priced per seat plus a
platform fee. This is where the defensible part of the record lives, because it compounds.

Stage 3, high capability or AGI. Performance cells deflate toward zero, and two things inflate.
First, attestation: what was authorized, what was done, what happened, machine to machine, which
is why human and machine agents are symmetric first class subjects in the schema. Second,
legitimacy: as machine generated content and judgment become abundant, provenance clean human
judgment becomes the scarce input, and the price of it is set by markets that already exist. The
Tegus comparable ($930M for a shared, consented insight library), the Shutterstock benchmark (20
percent average royalty to contributors on dataset licensing), Mercor's estimated $2.00B
annualized revenue for expert judgment sold by the hour, and roughly $24B a month of settled
judgment across Kalshi and Polymarket.

The honest caveat, stated as insurance rather than as plan: under full labour displacement the
audit of human judgment loses its buyer, and the surviving business is machine to machine
attestation. The schema hedges that today because it costs nothing to do so.

## Where humans fit

Four roles, and the pitch should name all four, because they are what make the human side
non substitutable rather than romantic.

1. Source of legitimacy. Consent, identity and accountability cannot be synthesised. A model can
   generate an opinion; it cannot be the party that is answerable for one.
2. Adjudicator. Defeat relations are authored by a person, or they are a model grading itself.
   This is the anti mirror guard in the brief spec: retrieval explicitly includes items that
   contradict the current prompt, and a mirror is worse than a stranger because it launders your
   errors back to you as confirmation.
3. Calibration record. A person's track record, confidence against outcome, is the only durable
   credential in the system and the thing nobody else can hold across models and employers.
4. Diversity input. Crowd accuracy depends on independence and diversity, and the diversity
   prediction theorem has documented counterexamples, so diversity must be paired with
   adjudication. Humans supply the out of distribution signal, and the ledger is what keeps it
   from collapsing into correlated error.

## Business model mapped to the matrix

    line                      who pays         what they buy                    anchor
    1 free local individual   nobody           the ledger plus the brief        acquisition, near zero marginal cost
    2 paid sync and relay     the individual   portability across devices       seat fraction pricing
    3 enterprise aggregation  the employer     consented org view, dissent,     per seat plus platform fee
                                               export, attestation
    4 contributor economy     buyers of        scoped, provenance clean,        Shutterstock 20% royalty,
                              judgment         calibration gated items          Tegus $930M comparable
    5 machine attestation     labs, insurers,  authorization and evidence for   per attestation, speculative
                              enterprises      machine actions

Sequencing: line 1 and 2 first, because they cost nothing and produce the compounding record.
Line 3 is the revenue that funds the company. Line 4 launches only with a quality gate that
pays on demonstrated calibration rather than volume, because every existing attempt
(expert networks by the hour, crowd platforms by the task, prediction markets by trading profit)
pays for something other than being right, and that is the gap as well as the risk. Line 5 is
the hedge, not the pitch.

What stays ruled out, from the earlier brainstorm and still correct: deposit taking or float,
surveillance style aggregation of groups without consent, map rental as a perpetual royalty
(distillation kills it), and backtested trading alpha.

## Open decisions for discussion

1. Does the free tier include the brief, or is briefing the paid feature? Free briefing maximises
   the compounding record and gives the moat away; paid briefing monetises early and slows
   accumulation.
2. Enterprise buys aggregation, custody, or attestation? Aggregation is legitimate and sellable,
   custody is the toxic version, attestation is the durable one.
3. Does the contributor economy launch in year one, or after the individual record exists? Launch
   early and the map is thin, launch late and the largest number stays theoretical.
4. Is the collective map sold, or only used to improve the individual product? Selling invites
   distillation, not selling leaves Tegus sized value on the table.
5. Does attestation get priced per call from day one, or bundled into enterprise until a machine
   buyer actually exists?
