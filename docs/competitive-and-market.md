# Competitive landscape and opportunity sizing

Status: framework first, 2026-09-14. Research is being gathered against this rubric; the
per competitor tables and the market figures land underneath once sourced. Nothing in this
file should go in front of an investor until every number carries a source.

## Why the competitor set changed

The earlier competitor list was built around the old framing (audit tool, or personal memory)
and it named the wrong neighbours. Once the axis is whether the derivation survives the
delegation, the competition splits into four groups that do not compete with each other, and
only one of them is a real substitute.

    group                          what they keep                what they lose
    memory and context layers      preferences, facts, history   judgment, defeats, provenance
    observability and eval         spans, scores, telemetry      the human's reasoning
    governance and compliance      policies, inventory, reports  per decision derivation
    provenance and grounding       document to citation link     the claim and its attacks

Odologic's claim is that it is the only layer that keeps the derivation itself: a claim, its
status, what defeated it, who it came from, and which of those items were injected into a
given model turn.

## Scoring rubric

Every competitor gets scored on the same four questions. The first is the one that matters.

1. Derivation inspectability. Can a user walk from an output back to the exact context that
   produced it, and see why that context was selected? Yes, partly, no.
2. Judgment versus facts. Does it hold the human's reasoning and its defeasibility (what was
   attacked, what survived), or does it hold facts, preferences and context?
3. Provenance discipline. Is the origin of each item first class (you, a document, a model
   proposal), and can model output be prevented from re entering wearing your name?
4. Ownership and portability. User owned, exportable, and survives leaving the vendor, or
   landlord held.

## The structural defence to test

The durable claim in the brainstorm was that incumbents cannot be neutral, portable, or
custodial. That is a testable claim and it should be tested against each group rather than
asserted: a memory vendor that also rents the model has a conflict, an observability vendor
sells to the operator rather than the person, a governance vendor sells the compliance
artefact rather than the decision trail. The counter case to look for is a well funded memory
or observability player adding claim status and defeats on top of an existing base, which is
the cheapest path for anyone to close the gap. Both are being researched.

## Opportunity: three ways to size it, and only one is a headline

The TAM question has three answers and they are not interchangeable, so the doc will keep
them separate.

1. Top down, from sectors that already have budget: AI governance, AI observability and eval,
   knowledge management, decision intelligence, expert networks. Headline number, and the
   weakest one, because Odologic is not replacing those budgets, it is a new line item beside
   them.
2. Bottom up, from the same population that already pays per seat for AI: knowledge workers
   times a subscription, with the enterprise tier on top. This is the honest near term number
   and the one to put in the model.
3. Value of the aggregate, if the collective map argument holds: priced like an expert
   network or a data licensing market (user times domain times verified quality), not like
   seat software. Largest, most speculative, and only credible with evidence that aggregated
   judgment is worth more than individual judgment. That evidence is the thing the research
   has to settle, because the whole crowdsourcing and contributor economy story rests on it.

## The collective map question, stated honestly

Earlier position: an aggregate map is worth more than an individual one on coverage and error
correction, content value depreciates through distillation, and the durable value is
legitimacy, diversity and provenance.

That is currently a belief with a mechanism sketch. It survives or dies on four facts:

1. Do aggregated human judgments beat individual ones, and under what conditions (diversity,
   independence, and the correlated error failure mode)?
2. What does provenance clean human judgment actually sell for (data licensing deals, expert
   network rates) versus what raw content sells for?
3. What happened to open knowledge projects when models started consuming them (Stack
   Overflow is the live experiment)?
4. Does quality gating by demonstrated calibration, rather than volume, actually resist
   farming, or does every attempt at this degrade into volume chasing?

Answers to those four decide whether the crowdsourcing section of the thesis is a revenue
line or a governance argument. They should not be blended.

## What human judgment actually sells for (pricing regimes, sourced)

Six distinct regimes, and they price completely different things. This is the most useful
table in the doc, because it shows there is no established price for what Odologic proposes to
sell.

    regime                        example                 price                   paid on
    1 conversation                GLG, Third Bridge       ~$400 to $2,000 a call  time and credentials
    2 consented insight library   Tegus (to AlphaSense)   $930M acquisition       one call resold to many
    3 expert hour at scale        Mercor                  ~$109 an hour average   credentials and time
    4 per task commodity judgment Toloka, Scale          $0.02 to $0.20 an item  volume
    5 scored forecasting          Metaculus               paid nothing            reputation only
    6 settled market price        Kalshi, Polymarket      trading P&L plus fees   capital at risk

Verified anchors for the ones that matter:

Tegus. AlphaSense closed the acquisition of Tegus for $930 million on 8 July 2024, alongside a
$650M round that took AlphaSense to a $4B valuation. This is the clearest single price ever put
on a shared, consented library of human insight, and it is the closest comparable to a
collective map. Source:
https://www.prnewswire.com/news-releases/alphasense-completes-acquisition-of-tegus-302190934.html

Mercor. Annualized revenue estimated at $2.00B with a $10B valuation in 2025 and $486M raised,
per Sacra, updated August 2026. Sacra is an estimate shop rather than a filing, so treat as
estimated. Implication: expert judgment can be metered by the hour and sold to AI labs at
billions, which sets the ceiling on what time and credentials alone are worth. Source:
https://sacra.com/c/mercor/

Shutterstock. Contributors receive a 20 percent average corporate royalty on the revenue
Shutterstock receives for dataset licensing, per Shutterstock's own contributor help page, and
the company reported $104 million of AI licensing revenue in 2023. This is the only clean
published revenue share rate for clean human data, and it is the honest benchmark for a
contributor payout on a shared map. Sources:
https://submit.shutterstock.com/help/en/articles/10594694-shutterstock-data-licensing-and-the-contributor-fund
and https://petapixel.com/2024/06/04/shutterstock-made-104-million-licensing-assets-to-ai-devs-last-year/

Prediction markets. Combined monthly volume on the major platforms rose from under $5B in
September 2025 to about $24B in April 2026, with sports making up 80 percent of Kalshi volume.
Settled judgment clears at scale, but the mix says the volume is entertainment-adjacent rather
than analytical. Source:
https://www.pewresearch.org/short-reads/2026/05/27/trading-volume-on-prediction-markets-has-soared-in-recent-months/

News Corp and Axel Springer to OpenAI. Reported at more than $250M over five years and at tens
of millions of euros a year respectively. Both are press reported rather than confirmed by the
parties in a filing, and I could not re-pull the primary pages (one blocked, one paywalled), so
these stay as reported. The mechanism they demonstrate is the one that matters: price tracked
accountable authorship and editorial process, not token count.

The gap this exposes. Nobody in this evidence base pays a person on verified track record.
Expert networks pay per hour, crowd platforms pay per task, prediction markets pay through
trading profit and loss, Metaculus pays reputation only, and even Shutterstock's 20 percent is
a share of licensing revenue rather than a function of how right anyone was. Quality weighted
compensation against a calibration record is genuinely un-priced in the market. That cuts both
ways and both sides belong in the pitch: it is the differentiator, and it is the reason there
is no benchmark to anchor price expectations against.

## The collective map: what the evidence supports, and what it does not

Four facts decide the crowdsourcing section. Stated as findings, not hopes.

1. Aggregation beats the typical individual, but only under conditions. The standard
conditions are diversity, independence, decentralization and aggregation, and Page's diversity
prediction theorem (PNAS 2004) formalizes it: crowd error equals average individual error minus
diversity. There is also counter evidence, an empirical study that found no significant
correlation between prediction diversity and collective error, so diversity alone is not a
mechanism. The design consequence is the important part: a ledger that records each person's
claim and position separately preserves independence and makes aggregation explicit, and
adjudicated defeats are what stop diversity from degrading into correlated error. Odologic's
structure is not a nicety here, it is the thing the theorem requires.

2. Correlated error is the failure mode to design against, not disagreement. Where
contributors see each other's positions or chase the same incentive, errors correlate and the
crowd collapses toward a single amplified opinion. Consequence: scoping and separation, no
upvote chasing, no popularity signal on claims, and a record of who influenced what.

3. Content value does depreciate, and Stack Overflow is the live proof. The corpus was licensed
to model providers while its contributor supply collapsed: peak of roughly 207k questions a
month in March 2014 down to launch era lows, and only 3,862 questions in December 2025, a 78
percent year over year drop. The nuance that matters for us: the decline started in 2014, a
decade before LLMs, tracking tougher closures of "low quality" questions. So the commons was
killed twice, once by over-gating that was not contestable and once by substitution.
Consequence: any gating in Odologic must be a recorded, auditable adjudication, never closed
authority.

4. Legitimacy is the durable asset, and there is a price benchmark for it. The premium deals
paid for accountable human authorship rather than volume, and the 2023 Stack Exchange moderator
strike is the case study in what happens when the platform captures the value and the
contributors are shut out. Consequence: if a contributor cannot see a path from their scoped
item to pay and to a governance voice, supply leaves regardless of how good the aggregation is.

Net read on the original claim: "a collective map is worth more than an individual one" is
supported on coverage, error correction and price (Tegus at $930M is the proof that a shared
insight library has real value), and it is NOT yet supported on a mechanism for paying
contributors by verified accuracy, because that mechanism does not exist anywhere in the
evidence. The honest line for the deck is that the collective map is a governance and
legitimacy asset with a demonstrated acquisition comparable, not a proven revenue line.

## Competitor findings, sourced

Status note: the fan out that gathered this was uneven. Three of the six children timed out
after searching for ten minutes without answering, so groups 2, 3 and 4 come from two children
that did finish, and I re-verified their load bearing figures (Credo AI, Arize, Langfuse and
ClickHouse) directly. Group 1 I gathered myself. Rows marked PENDING or UNVERIFIED are exactly
that and must not go in front of an investor without re-sourcing.

### Group 1, memory and context layers

These are the systems that try to remember the user across sessions. They are the group a
buyer will compare Odologic against first, and they are the weakest fit on the axis.

Mem0. The memory layer for AI, memory layer as infrastructure for other apps, $24M round
announced 28 October 2025, plus a free hobby tier and paid plans. Stores extracted facts and
preferences about the user to inject as context. It has the plumbing and the distribution, and
what it does not have is status or defeasibility: a stored item has no theorem/assumption
distinction, no defeats, and citation-wise it is provenance-light. That is the row to watch,
because adding claim status to an existing memory store is the cheapest possible version of
this product. Sources: https://mem0.ai/series-a and https://mem0.ai/pricing

Engram. AI memory startup, raised $98 million announced 23 June 2026, investors include
General Catalyst, Kleiner Perkins, Sequoia and Andrej Karpathy, positioned around cutting
token costs through better memory. This is the newest well funded entrant and it confirms the
memory layer is a funded category, not a niche. It is an efficiency play, not a judgment play,
which is the useful contrast: capital is flowing to "remember more cheaply", not to "record
what was defeated and by whom". Source:
https://www.cnbc.com/2026/06/23/ai-memory-startup-focused-on-cutting-token-costs-raises-98-million.html

Claude memory, import and export. Anthropic ships memory import and export for Free, Pro,
Max and Team plans on web and desktop, and the documented flow is literally a prompt you paste
asking your current provider to dump your memory, then re-importing it into Claude. This
matters twice. First, per assistant memory portability already exists, which weakens the
strongest form of the lock-in argument: the mass of remembered facts is not actually trapped.
Second, it sharpens the real gap, because what gets exported is a pile of facts in prose with
no status, no defeats, and no record of which were injected where. The thing that is not
exportable is the derivation, not the content. Source:
https://support.claude.com/en/articles/12123587-import-and-export-your-memory-from-claude

Glean. Enterprise search and assistant with a reported $200M+ ARR and a $150M Series F at a
$7.2B valuation announced June 2025. PENDING, the press page returned an empty body when I
pulled it, so the ARR and valuation figures are unconfirmed and should be checked against the
Glean blog post or the funding announcement before use.

Notion AI, Obsidian plus AI plugins, Rewind/Limitless, Gemini personalization, Dust. PENDING,
not yet sourced.

### Group 2, governance, compliance, observability and evaluation

Two sub clusters, and neither records a judgment.

Governance and GRC platforms. Credo AI (model inventory, policy packs mapped to NIST AI RMF
and the EU AI Act, risk assessments, approval workflows; $21M Series B in July 2024 taking
total funding to $41.3M, from the company's own blog), Holistic AI (bias and robustness
auditing plus regulation readiness, funding UNVERIFIED because the aggregator figure I saw was
clearly a scraped mashup), IBM watsonx.governance (model cards, lifecycle gates, drift and
fairness monitoring, evidence collection), Microsoft Foundry with the Responsible AI dashboard,
Vanta and Drata (compliance automation with AI modules bolted onto SOC 2 style evidence
collection), and OneTrust (AI inventory and assessment inside a privacy suite). What they all
record is policies, controls, risks, attestations and evidence artefacts. A risk is a scored
register row, not a claim that can be defeated by an attached counter claim. That is the whole
gap in one sentence.

Observability and evaluation. LangSmith, Langfuse, Arize, Braintrust, Weights and Biases Weave,
Humanloop, Patronus AI and Galileo. These record traces, spans, tokens, scores, evaluator
versions, annotations and detectors. Arize announced a $70M Series C on 20 February 2025
(confirmed on the press release and the company blog). Langfuse's acquisition by ClickHouse is
confirmed from two primary sources, ClickHouse's own post and Langfuse's joining announcement,
and it matters: an open source, self hostable telemetry store removes the data sovereignty
objection in the observability layer, so that cannot be part of our differentiation story.

The structural read, which is more important than any single row: an enterprise can satisfy
its written audit obligations today with a GRC platform plus an observability platform, and
neither of those records defeasibility. The nearest substitute is therefore not a vendor, it is
that bundle. The two highest threats are Microsoft's Responsible AI dashboard, because decision
path and counterfactual views are the only derivation-like inspectability in the whole set, and
the generic enterprise phrase "AI decision audit trail", because a governance committee will
accept it as the answer while it logs inputs, model version, outcome and approver without any
structured warrant. Odologic's job in that room is to show the difference between logging a
decision and warranting a judgment.

### Group 3, guardrails, provenance and grounding, graph and temporal databases

Guardrails. NVIDIA NeMo Guardrails (free, Apache licensed, programmable Colang rails), Guardrails
AI (validators enforcing output schemas), Lakera (prompt injection and jailbreak detection,
acquired by Check Point), Robust Intelligence (now Cisco AI Defense). All of them govern model
inputs and outputs. None of them inspects judgment. The threat is positioning, not product:
"we have guardrails" can be mistaken for "we have inspectable judgment".

Provenance and grounding, the closest overlap on our own axis. Microsoft GraphRAG (MIT
licensed, entity and community graph over a corpus, source text unit provenance) is the single
most common "we already have that" objection, because its output looks authoritative while
conflicting statements are merged into community summaries rather than adjudicated. Vectara
(citation bearing grounded generation plus a hallucination detection model) and whyhow.ai
(chunk level provenance links, early stage, corporate status uncertain as of 2026) are the
enterprise grade versions. Chroma is storage with arbitrary metadata, which is exactly how
teams convince themselves they can fake a judgment ledger. The pattern across all of them:
they can show you the source, they cannot show you what defeated what.

Temporal and logic databases. XTDB and Datomic, plus the Datalog lineage of Crux. Immutable
history plus explicit rules gives a fully inspectable substrate, and no claim semantics at all.
A sophisticated buyer can say "XTDB plus our schema is Odologic", and the honest answer is that
the substrate plus the schema is the product, and almost nobody builds the schema or the brief.

Provenance as a standard. W3C PROV-O, RDF reification, named graphs, and frameworks like
Cognee and TrustGraph. This is the sharpest reframe in the whole exercise: provenance is
genuinely solved as a standard. Nobody has a published vocabulary for claim status or defeat.
So provenance is table stakes and judgment is the missing layer, and that is how the wedge
should be stated: status lifecycle, computed defeat, and the brief. Not provenance.

### Group 4, argument mapping and personal knowledge management

The strongest rhetorical threats live here, because these are the tools that already prove
people will do the work.

Kialo. Structured pro and con debate trees where an objection is literally a competing node.
Free for public and education use, paid tiers for private and enterprise (tier pricing
UNVERIFIED). It is the closest consumer grade match on defeasibility, and it lacks provenance
typing, model proposal lineage, and any brief a model can consume. Cite it as validation that
the behaviour exists, not as an empty competitor.

Argdown. A plain text, markdown-like argument format with typed attacks including undercutters
and rebuttals, free and open source, file based and fully portable. This is the "we could just
use a text format" objection in its strongest form, and it is a real one: the format is solved
and free, so the differentiation has to be the lifecycle, the provenance typing and the brief.

Rationale. Commercial visual argument mapping for decisions, tree based, no AI native brief.

Obsidian with AI plugins, and the wider linked note tools (Logseq, Roam, RemNote, Tana,
Anytype). Local first markdown, plugin ecosystem, LLM query over the vault, maximum ownership
and portability. This is the highest switching cost problem we have: for a technical user, the
vault plus a plugin already looks like most of the value proposition, for free, minus the
rigour. Two consequences, and both are product requirements rather than positioning: Odologic
must import from a vault on day one, and it must sell the ledger rather than the notes, because
if it looks like a note app it will be compared to a free one.

## Closing read: where the wedge actually is

Across all four groups, no product in this scan ships a first class claim status lifecycle
(theorem, observation, assumption, contested, defeated), computes defeat relations, or projects
a compact brief back into an arbitrary model. Groups 1 and 2 compete for the trust budget.
Groups 3 and 4 compete for the workflow and the substrate. The two objections to rehearse until
they are boring: "GraphRAG already gives us provenance" (answer: provenance is table stakes,
PROV-O solved it, adjudication is what is missing) and "my Obsidian vault plus a plugin is
enough" (answer: nothing enforces status, nothing computes defeat, and here is the import).


## Verified anchors so far (direct sources, not subagent output)

These were pulled and read directly. Figures from vendor sponsored or SEO report mills are
labelled as such.

AI governance software:
- The Business Research Company, AI Governance global market report 2026: growing to $2.63B
  in 2030 at 44.3% CAGR. https://www.thebusinessresearchcompany.com/report/ai-governance-global-market-report
- MarketsandMarkets, AI Governance Market forecast to 2029: 45.3% CAGR.
  https://www.marketsandmarkets.com/Market-Reports/ai-governance-market-176187291.html
- Forrester, AI governance software spend: 30% CAGR 2024 to 2030 (independent, and notably
  lower than the two report mills, which is the honest range to quote).
  https://www.forrester.com/blogs/ai-governance-software-spend-will-see-30-cagr-from-2024-to-2030/

LLM observability and eval:
- LLM observability platform market, $2.69B in 2026 to $9.26B by 2030, 36.2% CAGR, and the
  same firm reports $1.97B in 2025. https://www.researchandmarkets.com/reports/6215671/large-language-model-llm-observability and
  https://www.thebusinessresearchcompany.com/report/large-language-model-llm-observability-platform-global-market-report

Expert networks (closest existing market to paying for human judgment):
- Inex One estimate: industry reached about $3B in 2025, growing 12% annually across 2023 to
  2025. https://inex.one/blog/expert-network-market-size
- IBISWorld: US expert network revenue $1.8B in 2025, 7.0% five year CAGR. The gap between
  these two is definitional (US only versus global), worth stating rather than averaging.

Stack Overflow, as the live experiment in what happens when models consume a knowledge
commons:
- Only 3,862 questions posted in December 2025, a 78 percent drop year over year, on top of
  earlier declines. https://www.devclass.com/ai-ml/2026/01/05/dramatic-drop-in-stack-overflow-questions-as-devs-look-elsewhere-for-help/4079575
- May 2025 monthly question volume down to launch era 2009 levels.
  https://blog.pragmaticengineer.com/stack-overflow-is-almost-dead/

What provenance clean human text actually sold for:
- Google and Reddit, roughly $60M per year, reported February 2024.
  https://www.reuters.com/technology/reddit-ai-content-licensing-deal-with-google-sources-say-2024-02-22/ and
  https://www.cbsnews.com/news/google-reddit-60-million-deal-ai-training/

Collective judgment, the academic anchor:
- Diversity prediction theorem (Page, PNAS 2004): crowd error equals average individual error
  minus diversity, so accuracy comes from diversity, not from averaging alone.
- PNAS follow up on optimal incentives for collective intelligence: rewarding accurate
  minority predictions produces optimal diversity, which is the mechanism a contributor payout
  scheme has to respect. https://www.pnas.org/doi/10.1073/pnas.1618722114

Adjacent software budgets:
- Knowledge management software: $16.22B in 2026 to $37.64B by 2031, 18.34% growth, Mordor
  Intelligence. https://www.mordorintelligence.com/industry-reports/knowledge-management-software-market
- Decision intelligence: $13.3B in 2024 to $50.1B by 2030, 24.7% CAGR, MarketsandMarkets.
  https://www.prnewswire.com/news-releases/decision-intelligence-market-worth-50-1-billion-by-2030---exclusive-report-by-marketsandmarkets-302096971.html
- Treat both as context, not as TAM. Odologic is not replacing either budget.
- One figure to refuse to use: "AI based personalization, $661B by 2030." The definition is so
  broad it prices nothing. Worth keeping in the doc as an example of the number not to quote.
  https://www.thebusinessresearchcompany.com/report/artificial-intelligence-ai-based-personalization-global-market-report

Bottom up inputs, per seat pricing actually published by the vendors:
- Microsoft 365 Copilot: $30 per user per month enterprise add on on the Microsoft pricing
  page, $25.20 listed for business, and Microsoft's own calculator context puts real cost with
  a base plan at $30 to $90 per user per month.
  https://www.microsoft.com/en-us/microsoft-365-copilot/pricing/enterprise and
  https://www.microsoft.com/en-us/microsoft-365-copilot/pricing
- ChatGPT Business premium seat: $100 per user per month billed annually, $125 monthly, from
  the OpenAI help center. https://help.openai.com/en/articles/8792828-what-is-chatgpt-business
- ChatGPT Enterprise: no published price, quote only, with 2026 procurement reports converging
  at $45 to $75 per seat per month and a reported 150 seat minimum. Reported, not published.
  https://coworker.ai/blog/chatgpt-enterprise-pricing
- Implication for the model: a judgment layer priced at a fraction of a seat already being
  paid for is inside the noise of existing AI spend, which is the argument for attaching rather
  than asking for a new budget line.

## Open questions

1. Is the bottom up seat model large enough to raise on, or does the raise depend on the
   enterprise aggregation story? Answer follows from the sizing research.
2. Which single competitor, if any, is one feature away from this? That determines how much
   the pitch rests on execution speed versus structural position.
3. Does the collective map get sold (contributor economy, licensing) or only used to make the
   individual product better? Selling it invites the distillation problem in the brainstorm;
   not selling it leaves the largest number on the table.
