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

## Competitor findings, sourced

Status note: the subagent fan out that was supposed to gather this timed out four times over.
Everything below was pulled and read by me directly, so it is a partial set, not a finished
landscape. Rows marked PENDING are still unverified and must not go in front of an investor.

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

### Group 2, governance, compliance, observability (PENDING)

### Group 3, guardrails, provenance, grounding, graph and temporal databases (PENDING)

### Group 4, argument and deliberation mapping tools (PENDING)

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
