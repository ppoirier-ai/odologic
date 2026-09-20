# Application tracks, and the capital question behind them

Status: second pass, 2026-09-20. The frame is settled and every figure is either sourced with a
URL or explicitly labelled MODELLED or UNVERIFIED. MODELLED means the arithmetic is mine and the
inputs are the rows named underneath it. Nothing marked UNVERIFIED goes in front of the chip
partner or an investor. Companion docs: docs/stakeholder-value-map.md (the value objects and the
stakeholder map, which this file derives from rather than restates), docs/moat-design.md, and
docs/competitive-and-market.md.

The counterparty is the graph accelerator company, referred to here as the chip partner. They are
kept confidential: no name, no architecture detail, no identifying facts, in this repo or in any
shared copy.

## What is actually being decided

The chip partner has three things we do not: a graph oriented accelerator, an existing military
and finance book of business, and capital they will spend on applications that run on their
silicon. They also have one specific pain of their own, which is the reason this conversation is
happening at all: a very large codebase that current language models cannot manage, because of
context window limits and hallucination. That last point is the only place in the whole set where
the buyer describes his own injury rather than a market that might exist.

So the choice is not which application is largest. It is four questions, and they sort the tracks
by themselves:

1. Does the buyer already have budget and a named owner, or are we creating the line item.
2. Does the buyer accept a record they do not control, or is custody demanded on day one.
3. Can a defeat be settled by execution, or does it stay an argument between two people.
4. Does the track pull the chip partner's silicon, or is the silicon incidental.

Question 2 kills tracks quietly. Question 3 decides whether the product is provable in a pilot or
only in a deck.

## The tracks, defined

    A regulated finance assurance      banking, insurance, trading. Model risk management and audit
                                       already exist and already have owners.
    B healthcare assurance             clinical documentation, regulatory submission, payer review.
    C military space                   space domain awareness, satellite tasking, command and
                                       control decision audit. Buyer is government, entry via primes.
    D defense codebase comprehension   large codebase understanding, change impact, hallucination
                                       control, starting with the chip partner's own codebase.
    E accelerated defeasibility        the ledger logic executed on their hardware as a co-designed
                                       capability, sold as silicon differentiation.
    F OEM into their book              Odologic inside their existing military and finance customer
                                       relationships.

F is a channel rather than an application, and it applies to A, B, C and D. It is kept separate
because its cash timing is completely different, and that difference is the main reason to be in
this conversation at all.

## Why D is the first move, and it is not market size

1. Code is the only domain in this set where a defeat can be settled by execution. A failing test,
   a broken build, a dependency that does not exist, a signature that breaks a downstream caller:
   each is a computable defeat rather than an opinion about an opinion. The claim status lifecycle
   stops being a schema we assert and becomes a status the system enforces. Every other track
   requires us to argue that defeasibility is real, and here it can be shown.
2. The alternative the buyer has today is a frontier model over a context window, and the
   published measurements say that alternative does not work. LongCodeBench, evaluated across
   1,043 instances from 108 repositories up to one million tokens, measured resolution falling
   from 29 percent to 3 percent for Claude 3.5 Sonnet as context grew from 32K to 256K tokens, and
   from 70.2 percent to 40 percent for Qwen2.5, with the best closed model at 22 percent and open
   models in single digits. Source: https://arxiv.org/abs/2505.07897 . The original SWE-bench
   paper found the best model of its time resolving 1.96 percent of 2,294 real issues, and framed
   the task as requiring coordinated change across multiple functions, classes and files rather
   than local edits. Source: https://arxiv.org/abs/2310.06770 . Positional degradation is measured
   separately: accuracy is highest when relevant material sits at the start or end of the input
   and degrades in the middle, to the point that one model scored below its own closed book
   accuracy when the relevant document sat mid context. Source: https://arxiv.org/abs/2307.03172 .
   Fabrication is measured too: across 16 coding models tested, 19.7 percent of recommended
   packages did not exist, 205,474 unique fabricated names, higher for open models at 21.7 percent
   than for commercial models at 5.2 percent. Source:
   https://www.usenix.org/publications/loginonline/we-have-package-you-comprehensive-analysis-package-hallucinations-code
3. In defense the context window is not even the binding constraint, and this is where the chip
   partner's hardware stops being incidental. Air gapped and classified environments, export
   control, and no cloud egress remove the hosted model from the option set. What is left is a
   local model on local silicon plus a local ledger, which is exactly the shape they sell.
4. The user is an engineer with a named stake in the claim, so the individual map in
   docs/stakeholder-value-map.md is the unit of accumulation, rather than opening with the
   employer custody fight.
5. The corpus does not have to be built. The chip partner's own codebase is the first customer,
   the first benchmark and the first reference, which is the cheapest cold start in this file.

The buyer side is large and documented, which is the other half of the argument. The federal
government spends over $100 billion on information technology each year and agencies have
typically reported about 80 percent of it as operations and maintenance of existing systems
including legacy ones, and ten critical legacy systems aged about 8 to 51 years cost about $337
million annually to operate and maintain collectively. Source:
https://www.gao.gov/products/gao-23-106821 . In July 2025 GAO reviewed 69 federal legacy systems
and identified 11 most in need of modernization across 10 agencies, ages 23 to 60 years, eight
using outdated languages, four on unsupported hardware or software, seven operating with known
cybersecurity vulnerabilities that cannot be remediated without modernization, with the Treasury
systems running on COBOL and Assembly. Source: https://www.gao.gov/products/gao-25-107795 .
Defense software sustainment was estimated by the department itself at not less than $15 billion
across five fiscal years, against only about $828 million actually reported for fiscal year 2018,
and that total is itself unreliable because the Navy did not report under the updated policy.
Source: https://www.gao.gov/products/gao-19-173 . GAO's April 2026 sustainment review found 14 of
36 weapon system sustainment reviews for fiscal years 2023 and 2024 showing critical operating and
support cost growth, and noted that completing one Army software update would save more than $130
million across about 30 remaining years of the program. Source:
https://www.gao.gov/products/gao-26-108140 . A current fiscal year total for defense wide software
sustainment was not located from a primary source: UNVERIFIED.

The honest caveat, stated rather than buried: defense software already has requirements
traceability, code review records and configuration management, and a reviewer will say they have
that. Traceability shows which requirement a line of code came from. It does not show which claim
about the system was defeated, by what, and by whom. That has to be demonstrated on their code in
a pilot, not asserted in a deck.

## The six numbers per track

Read the capital column as what has to be spent before the first invoice is paid, not as a raise.
Every row is MODELLED unless a source is named in the list underneath.

    track  capital to    capital to     sales cycle     near term cash      three year      moat
           first revenue  market scale  length          flow, 4 quarters    revenue band    durability
    D      $150K to      $2M to $5M     3 to 6 months   strongest after     $10M to $25M    medium high
           $400K                        commercial, 60  quarter two via     MODELLED
                                         to 120 days     milestone billing
                                         government      plus SBIR
    A      $1M to $3M    $5M to $15M    6 to 18 months  weak, design        $2M to $10M     high but slow
           (12 to 18                    UNVERIFIED      partner pilots      ARR MODELLED
           months)                                      often unpaid
    B      $2M to $5M    $15M and up    12 to 24        weakest             $1M to $8M      medium
                                         UNVERIFIED                          MODELLED
    C      $1.5M to     $4M to $15M    3 to 6 months   government          $1M to $8M      high,
           $3M                          to first         payment lags about  MODELLED,       programme
                                        contract, then   6 months after      Palantir at     entrenchment
                                        years to a       submission          $8.15B is the
                                        programme of                         ceiling case
                                        record
    E      $400K to     $1M to $2M     1 to 2 quarters  development         $1M to $5M      low for us,
           $1.5M                        to the partner's revenue billed     development     high for
                                         engineering     per milestone       plus royalty    them
                                         budget                              MODELLED
    F      $150K to     $500K to $2M   1 to 6 months   best in the set,    $2M to $10M     low, channel
           $400K                        to first paid    cash per order      at 30 to 50     dependency
                                        order            MODELLED            percent channel risk
                                                                             margin MODELLED

Sourcing behind the capital and cash rows, each verified by reading the primary page:

1. Statutory SBIR ceilings are $323,090 for a Phase I and $2,153,927 for a Phase II as of April
   2026, above which Small Business Administration approval is required, and the programmes are
   described by the government as equity free and non dilutive. Source:
   https://www.sbir.gov/about
2. SpaceWERX publishes Phase I at $75K to $180K over 3 to 12 months and Phase II at $1.25M to
   $1.8M over up to 24 months, with applicant notification no later than 90 days from solicitation
   close and contracts finalised no later than 180 days from solicitation close. Source:
   https://spacewerx.us/get-funded/
3. TACFI is $375K to $1.9M over up to 24 months and STRATFI is $3M to $15M over up to 48 months,
   both requiring matched funding, with the match type and the requested amount fixed before
   submission and not adjustable afterwards, and both available only to a company holding an
   active Phase II or one completed within the prior two years. Source:
   https://afwerx.com/wp-content/uploads/PY25-STRATFI-TACFI-FAQs-CLEARED_AFRL-2024-3838_v2.pdf .
   That eligibility rule is the closest thing to a moat in the procurement documents, because
   incumbency compounds and late entrants are excluded from the scale up money.
4. The Defense Innovation Unit awards prototype agreements under Other Transaction authority in
   as few as 60 to 90 days, with a current average closer to 120 days, has conducted more than 500
   such awards in eight years, and after a successful prototype any interested department entity
   may enter a non competitive follow on production contract. Source:
   https://www.diu.mil/latest/advancing-dod-operational-capabilities-with-software-acquisition-reform
5. The smallest check in this exact niche, and the honest low anchor for a decision support pilot,
   is an Army solicitation capped at $250,000 per award over a maximum of six months. Source:
   https://www.army.mil/article/283863/army_sbirsttr_unveils_250k_aiml_decision_support_funding_opportunity
6. Cash is contract based rather than grant based, and the Air Force states contracts are more
   demanding than grants, which is why the planning assumption is that the company self funds
   roughly half a year of effort after submission before the first government dollar. Source:
   https://afwerx.com/wp-content/uploads/2024-07-29-2024-07-18-DAF-SBIR_STTR-FAQs-Dec-2022_CLEARED_AFRL-2023-0179_rev07172024.pdf
7. What a port costs and who pays for it, by precedent: the Department of Energy funded four
   codesign centres at $48 million over four years with the first year at $12 million split
   evenly, and ran PathForward at $258 million over three years with recipients required to fund
   at least 40 percent of total project cost, taking total investment to at least $430 million.
   Sources:
   https://www.anl.gov/article/exascale-computing-project-announces-48-million-to-establish-four-exascale-codesign-centers
   and https://www.energy.gov/articles/department-energy-awards-six-research-contracts-totaling-258-million-accelerate-us
   Read that as the price list for track E: government or client on the larger share, the hardware
   side on the balance.
8. The template for being paid by a hardware partner is Nvidia's $2 billion investment in CoreWeave
   at $87.20 per share in January 2026, bundled with CoreWeave software being folded into Nvidia
   reference architectures, which is cash plus distribution in exchange for becoming part of the
   vendor's story. Source:
   https://investors.coreweave.com/news/news-details/2026/NVIDIA-and-CoreWeave-Strengthen-Collaboration-to-Accelerate-Buildout-of-AI-Factories/default.aspx
9. Pricing anchors for track A, from the market rather than from optimism: AI governance platforms
   sell in a reported $30,000 to $150,000 per year band, compliance automation has an observed
   median around $25,000 per year across 233 purchases, and developer observability prices per unit
   in the tens of dollars per month. Sources in docs/competitive-and-market.md. The budget holder
   is model risk and the second line of defence, and the adjacent budgets are far larger than the
   AI governance line itself, which matters because AI governance software was valued at $308.3
   million in 2025 rising to $417.8 million in 2026 and $3,590.2 million by 2033 at 36 percent
   CAGR, with government and defence the largest vertical. Source:
   https://www.grandviewresearch.com/industry-analysis/ai-governance-market-report

## The ceiling case and the failure case, so the bands are not read in isolation

Palantir reported second quarter 2026 United States government revenue of $809 million, up 90
percent year over year, total revenue of $1.935 billion, up 93 percent, GAAP operating margin of
47 percent, and raised full year guidance to $8.150 to $8.158 billion. Source:
https://www.sec.gov/Archives/edgar/data/1321655/000132165526000039/a2026q2ex991pressrelease.htm .
BigBear.ai, the mid sized case rather than the ceiling case, reported first quarter 2026 revenue of
$34.4 million, gross margin of 34.0 percent, backlog of $281.9 million including a $53 million sole
source prime classified award, total available cash and investments of $431.5 million, and affirmed
full year 2026 guidance of $135 million to $165 million. Source:
https://www.sec.gov/Archives/edgar/data/1836981/000183698126000047/earningsrelease-1q26.htm .
Read together: the defense decision layer supports very large outcomes, and a credible mid sized
defense AI company can sit at that scale with a services heavy mix. That is the shape track D takes
before any software margin appears.

The failure case belongs in the same paragraph. Graphcore raised $684 million, peaked at a $2.77
billion valuation, ran out of commercial momentum, and was acquired by SoftBank in July 2024 for
about $500 million, roughly one fifth of peak, with a further $457 million injected afterwards.
Source: https://www.jonpeddie.com/news/graphcores-ipu-doing-well-at-softbank/ . That is why track E
carries a portability requirement and why track F is a channel rather than a dependency.

## Where the chip partner's money is worth taking

Their offer is a development contract, not a round, and the distinction decides whether we remain
neutral and whether we remain the owner of the schema.

    structure                       what it is                    effect
    milestone development contract  they pay for a named port or   accepted, non dilutive, deliverables
                                    reference application, per     are a working artefact and a benchmark
                                    milestone, no equity
    joint go to market              co sell into their book, split  accepted only if the record stays ours
                                    revenue, they keep the silicon  and export stays guaranteed
    reference design royalty        they pay per unit or per        accepted, and the only structure where
                                    deployment where the ledger     their silicon advantage and our schema
                                    runs as silicon                 both convert to money
                                    differentiation
    strategic equity investment     they take a position            rank last, because it makes them a
                                                                    conflicted party in the way
                                                                    docs/moat-design.md says the company
                                                                    dies, aligned with one landlord and
                                                                    therefore not neutral across the rest

Two hard conditions, stated now rather than discovered in diligence. No structure may give the chip
partner custody of a customer's ledger, and none may make the record unexportable. Separately,
because the partner is a hardware platform with uncertain share, any port work needs an unwindable
portability clause rather than exclusivity, on the logic the buyer side already uses: platform
diversity is resilience.

## Confidentiality and export control, which constrains all of it

The chip partner's customers sit under export control and releasability rules we are not a party
to. Three consequences for how this is written and sold. Their architecture and their codebase stay
unnamed in anything that leaves the two companies. Any pilot on their codebase has to be scoped by
them for releasability before we touch it. And a United States government track for a Canadian
controlled founder needs the foreign ownership and relocation question answered up front rather
than at the accreditation stage, which is a real cost item in track C, currently UNVERIFIED for
amount and duration.

## Ranked recommendation

1. F first, as the funding channel. It is the only line that produces cash inside two quarters,
   because it spends the chip partner's existing customer relationships rather than building a
   sales motion from zero.
2. D in parallel, as the product. It is the only track where a defeat is computable, the only one
   where the hardware is load bearing, and the only one whose first customer is already in the
   room. Price the first phase as a paid pilot with a benchmark deliverable on their codebase,
   using the Army decision support ceiling of $250,000 over six months as the low anchor.
3. C on the reference from D, using non dilutive procurement money, since Phase II at $1.25M to
   $1.8M plus TACFI matching can carry a prototype and a first government customer without equity.
   Check first whether the chip partner holds a space programme of record or space interest only,
   because a military client is not a contract vehicle.
4. A and B last, and A before B. A has the budget and the owner but a slow cycle and a deferred
   regulatory deadline, since the high risk obligations moved to 2 December 2027 and 2 August 2028
   while the Article 50 transparency duties stayed on 2 August 2026. B has a longer cycle, a
   crowded ambient scribe market, and no computable defeat to prove anything with.
5. E only as a paid study with the portability protections above, and only after D has produced
   something worth porting. Doing E first would make the schema their specification before it is
   our product.

The one thing this comparison does not establish, and it sits under every row: whether an engineer
working on a defense codebase will maintain a ledger while doing their job. That is testable in a
two week instrumented pilot on the chip partner's own repository, cheaply, and it should run before
capital is committed to a track.

## Open items

1. Does the chip partner hold a military space contract vehicle, or space interest only.
2. What is the releasability boundary on their codebase, and who signs the scoping.
3. UNVERIFIED and needed for track A: a sourced sales cycle length for software into a supervised
   bank, and a sourced cost and duration for accreditation, clearances, FedRAMP or CMMC.
4. UNVERIFIED and needed for track C: the foreign ownership, control or influence review cost and
   duration for a Canadian controlled founder running a defense software pilot.
5. Whether the chip partner will accept a milestone development contract with a portability clause,
   or whether their intent is exclusivity in exchange for the funding.
