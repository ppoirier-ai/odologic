# Decentralized architecture and token accrual

Status: first pass, 2026-09-14. Companion to token-design.md and moat-design.md. Not legal advice.

## The split that matters

You are right that blockchains are excellent for peer to peer financial interaction, and right
that Odologic's data is not time series. The conclusion I would draw is a hard split, not a
compromise:

    layer                        substrate                         why
    judgment graph               local bitemporal graph store      semantic, high write volume,
                                                                   private, needs iteration speed
    tamper evidence              signed Merkle roots, published    cheap, no token, no regulatory
                                 to a transparency log or chain    surface
    entitlements and rights      on chain, non transferable        scarce, order sensitive, must be
                                                                   verifiable by strangers
    money and disputes           on chain settlement and bonds     the thing chains are actually
                                                                   good at
    aggregate computation        MPC or FHE with verifiable        the only way to compute across
                                 results                           private local stores

Blockchains are append only, globally replicated state machines built for ordering and settling
scarce assets. A judgment graph is a property graph with defeat edges, status lifecycles,
provenance and scope, plus a per turn trace. Putting that on a replicated ledger pays the
replication cost for the wrong property and puts the most sensitive artefact on the least
controllable substrate.

## What should not go on chain

1. The graph itself. Latency, iteration speed and query complexity all get worse, and nothing about
   the graph needs global agreement. Two people's maps are not in conflict; they are separate
   records that occasionally get compared.
2. The trace. It is the most sensitive artefact the product holds. It belongs on the device, with
   anchors published, not replicated.
3. The brief. It is a projection, computed locally, and it changes every turn.

## What does belong on chain

Entitlements (the right to contribute in a domain, or to consume an aggregate), stakes and
slashing bonds, payouts to contributors, and dispute resolution with bonded challenges. All of
those are low volume, high value, order sensitive, and need to be verifiable by a stranger who
does not trust us. That is precisely the workload a chain is for.

## The edge computing version, and its hard part

Data lives with the owner, compute happens locally, and only proofs, roots and settlements travel.
The hard part is the aggregate: if local stores are private, computing a collective map requires
multi party computation or homomorphic aggregation plus a way to verify that the computation was
done correctly. That is a research grade dependency, not a launch feature, and it should be
sequenced as such.

## Progressive decentralization, in order

    stage   what ships                                   chain use          token
    v1      local ledger, signed brief selections        none               none
    v2      published anchors and heartbeat roots        anchoring only     none
    v3      entitlements, payouts, stakes, slashing      settlement layer   required for access
    v4      aggregate via MPC or FHE, verified           verification       same token, now for
                                                                           consumption rights

Decentralize where centralization is the risk, which is custody, the entitlement registry, dispute
resolution and settlement. Do not decentralize the graph. A fully decentralized graph store is a
research project that makes the product slower and worse, and it is not the part anyone distrusts.

## Token accrual without promising returns

Value has to be designed into mechanics, not into marketing. The mechanisms that accrue value from
necessity rather than from expectation:

1. The token is required, not encouraged. Access to a scarce entitlement or the right to post a
   stake cannot be bought with dollars.
2. Capped supply of entitlements per domain, so scarcity is real and cannot be inflated by us.
3. Sinks: fees are burned, or paid to service providers, so usage removes supply.
4. No emissions funded rewards. Rewards come from revenue, so there is nothing to sell into.
5. Revenue funded buybacks are the strongest accrual mechanism and the closest to the legal line,
   which is the trade off in the next section.

The marketing rule that follows: never describe appreciation, never publish projections, never
frame holding as an investment. Accrual is a byproduct of necessity and anyone who notices it
noticed it themselves.

## The one trade off worth being explicit about

Transferability is where accrual comes from and where legal risk comes from, and they cannot be
separated. A non transferable token is the cleanest legal position and it cannot accrue value. A
transferable token with genuine utility can accrue, and it invites the analysis. The spectrum in
between is restrictions: jurisdictional gating, lockups, accreditation, no secondary listing,
and a design where the market exists because the token is needed rather than because it was sold.

## What the 2026 regulatory posture does and does not change

It genuinely helps. The SEC has been issuing an interpretive framework applying Howey to crypto
assets rather than asserting by enforcement, and the SEC withdrew its securities classification
in the Solana matter, which is a real shift in posture.

It does not remove the risk, for four reasons. Howey is a Supreme Court test, so an administration
cannot repeal it, only decline to enforce it. Private plaintiffs can sue regardless of SEC posture,
and class actions do not need the agency's permission. The CLARITY Act is not law: H.R.3633's
latest action is Senate cloture on 8 August 2026, with revised text circulated on 22 July 2026, so
it is a live bill rather than a defence, and a bill is not something a company revises. And the
exposure is not only American: state regulators, tax treatment, and non US regimes all apply, and
a design that depends on who holds the White House is a political risk rather than a legal
foundation.

Get an opinion from counsel before launch, keep the marketing discipline above, and design so that
both outcomes of the bill are survivable.

## Recommendation

No chain and no token in v1. Ship the local ledger, sign the brief selections, publish anchors.
Add on chain entitlements and settlement when payouts to strangers actually exist, because that is
the first moment a chain solves a real problem rather than a narrative one, and it is also the
first moment a token is needed rather than desired.
