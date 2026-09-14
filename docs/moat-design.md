# Moat design: what can actually hold, and what cannot

Status: first pass, 2026-09-14. Written after the absorption analysis
(docs/distillation-risk-and-absorption.md), because absorption is what kills the obvious moat
story. This doc says which moats are dead, which are alive, and what has to be given up to make
the alive ones credible.

## The claim under test

The working hypothesis was: crowdsourced aggregate data is the moat, provided aggregate data is
exponentially more valuable than individual data. Test it honestly, because the answer changes the
company's shape.

## Why the data network effect fails here

Four reasons, and they are structural rather than execution problems.

1. Judgment is domain partitioned. Aggregate value does not scale with global contributor count,
   it scales within a domain. Cardiology adjudication does not improve a supply chain adjudication.
   So the correct model is many small pools, each with modest n, which gives you sublinear global
   returns and no exponential curve. Cross domain transfer exists (calibration habits and defeat
   patterns generalise somewhat), but it is weak enough that no buyer will pay a superlinear price
   for it.

2. The data is text, and text is distillable. A moat built on content fails against a party that
   can absorb content, which is exactly what the previous doc establishes. Anything that can be
   swallowed and reproduced cannot be the moat, and a corpus can be swallowed.

3. Aggregate value depends on independence, and independence degrades as the pool grows. The
   diversity prediction theorem rewards heterogeneity and has documented counterexamples where
   diversity and collective accuracy were uncorrelated. Bigger pools correlate. So the marginal
   contributor's value falls precisely as the network effect is supposed to kick in.

4. There is no exclusivity. A contributor can contribute the same judgment to a lab, an expert
   network and a ledger. Multi homing kills data network effects in the classic form.

Conclusion: the data network effect is not the moat, and designing around it is where the
viability doubt is coming from. It is real, but it is a market position that must be built
institutionally rather than a curve that arrives automatically.

## What could hold instead, ranked by durability

### 1. Neutrality as a position, made credible by commitments (strongest, and it is the only one labs cannot copy)

This is the one asset a landlord is structurally disqualified from holding. A lab rents the model
and sells to the operator. An employer is a party to the disputes it would adjudicate. A memory
vendor is a feature of somebody else's stack. So the position is not "we have better data", it is
"we are the party both sides can accept".

The catch is that a commitment is only a moat if faking it is expensive. Which means the moat has
to be built out of things that are hard to reverse:

    commitment                        how it becomes credible
    local first architecture          data resides with the person by design, not by policy
    source available schema           others can implement it, which is what makes the
                                      neutrality claim believable
    no custody covenant               in the charter, not in the terms of service
    steward or foundation structure   ownership that cannot be sold out from under users
    guaranteed export                 withdrawal is real, and it is the proof consent exists

Read that list as a price list. Every line costs margin or optionality, and each one is what
converts a promise into a position. If the company will not pay those prices, it has the promise
without the position, and the moat is not there.

### 2. The revocation asymmetry (the sharpest technical asymmetry available)

Once a fact is in model weights it cannot be withdrawn. A ledger can honor withdrawal, prove it,
and produce the record that withdrawal happened. As provenance and consent requirements land, the
ability to demonstrate erasure and revocation becomes a compliance obligation rather than a
feature, and it is the one thing no absorbed copy can provide.

This is a genuinely new moat line and it follows directly from the absorption problem: the
weakness of distillation becomes the strength of a record that can be revoked, because the lab's
copy is permanently out of compliance and yours is not.

### 3. Institutional entrenchment: being the record both parties cite (durable, slow, capital light)

The clearinghouse version. Not "we have the most data", but "our record is the one referenced in
the contract, the audit, the dispute, the underwriting". Once a regulator, insurer, auditor or
employer points at one ledger as authoritative, displacement is a re-litigation nobody wants.
This is how credit bureaus, exchanges and certification bodies actually hold their position, and
none of them are defended by software.

Requires: a specific recurring dispute, in a specific domain, where two parties already want a
neutral record. Realistic first candidates: institutional review and research provenance,
financial disclosure and analyst adjudication, clinical or regulatory submissions.

### 4. Calibration as a credential (strong if third parties accept it, inert if not)

A domain scoped, outcome scored track record is the only credential that cannot be bought or
back-filled: five years of being right takes five years. Its value is entirely social, so it only
becomes a moat once an outside party accepts it: an employer screening on it, an insurer pricing
on it, a procurement process requiring it. Until then it is a feature.

### 5. Per domain contributor density (real but expensive, and it is the GLG lesson)

Expert networks took decades to assemble accredited pools, which is why they price per call and
why Tegus was worth $930M as an acquisition. A per domain gated pool with demonstrated calibration
is genuinely hard to assemble quickly, and labs have no relationships, no consent legitimacy and
no appetite for accreditation work. This is a slow, relationship intensive moat. It is available
and it is worth less than it looks, because it does not compound superlinearly.

## The honest ranking

    moat                        durability   time to build   what it costs
    neutrality plus commitments high         medium          margin, optionality, control
    revocation asymmetry        high         short           almost nothing, design decision
    institutional entrenchment  high         long            domain focus, sales patience
    calibration credential      medium-high  long            outcome data collection
    per domain density          medium       long            cash and relationships
    data network effect         low          n/a             wasted effort
    software features           none         n/a             n/a

## The falsifiable tests, which should be run before the deck says "moat"

Each test is designed to fail cheaply if the moat is not there.

1. Reference test. Will an outside party accept the ledger's record in place of their own
   paperwork in a real decision? Ask a compliance officer, an insurer, an audit firm, a journal.
   A yes in any one domain is the start of an institutional moat. A no everywhere means the moat
   is a story.
2. Price test. Will a buyer pay materially more for the aggregate record than for the sum of its
   parts (individual records). If the aggregate sells for the same as the pieces, there is no
   network effect and the pricing model has to change.
3. Retention test. Do users refuse to leave, or do they stay because leaving loses history they
   cannot regenerate? The second is the accumulation moat and it is weaker than it sounds: it
   protects retention, it does not win acquisition.
4. Revocation test. Will an enterprise pay specifically for provable withdrawal and erasure across
   vendors? This one is cheap to test and could be the fastest commercial proof of the position.
5. Counterparty test. Does a lab or an employer accept a ledger they do not control? If every
   incumbent demands custody, the position is real but the market is smaller and slower.

## The fork this implies for company shape

If the moats that hold are institutional rather than product, then the company's shape changes,
and the choice should be made deliberately rather than drifted into.

Option A, venture shaped. Build the credential and institutional entrenchment fast in one domain,
raise on becoming the reference record for a category, accept that the software is a means and the
position is the asset. Needs speed, sales capacity, and a domain focus that feels narrow compared
to the current framing.

Option B, steward shaped. A foundation or steward owned entity holds the schema and the neutral
registry, with a commercial arm selling implementation, sync, enterprise deployment and
verification. Slower, lower ceiling, and the neutrality commitment becomes structurally true
rather than contractually promised. This is the version where the moat is the mandate.

Option C, protocol plus reference implementation. Open the schema to make neutrality credible, monetise
the reference implementation, hosted collaboration and verification services. Fastest adoption,
weakest capture, and it invites an incumbent to own the market using your format.

The decision axis is honest: how much margin and control is neutrality worth. Saying "we are the
neutral party" while keeping the option to monetise custody is the one position that fails, because
the commitment is what the moat is made of.

## What to do next quarter, in order

1. Run the revocation test and the reference test, in one domain, with real counterparties. They
   are cheap and they decide the shape of the company.
2. Pick a single domain for institutional entrenchment and say it out loud, even if it narrows the
   pitch. The science demonstration already in the repo is the obvious candidate.
3. Make the commitments real and visible: local first, source available schema, no custody
   covenant, guaranteed export. These cost little now and they are the moat's raw material.
4. Stop pitching the data network effect. Replace it with the position statement: the neutral
   record both sides can accept, plus revocation, plus a per domain credential.
