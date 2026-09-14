# Plain language pass: retiring "judgment ledger"

Date: 2026-09-14
Trigger: "judgment ledger" fails the three second test with investors and customers.

## Why it fails

Two abstractions are stacked, so a listener has to translate twice before they
hear a product.

- "Judgment" reads as opinion (I judged it fair), as a legal ruling, or as the
  word for poor decisions. It is the opposite of evidence in everyday speech.
  Nobody hears "a claim with a status" from it.
- "Ledger" is accounting and crypto vocabulary. It makes people think of
  bookkeeping, a wallet, or a database, not of proof.
- Together they describe our data structure, not the buyer's problem. Neither
  word says who buys this, or what changes for them.

The internal object model is good engineering. It is not marketing copy. Terms
like Judgment, Certificate, Defeat, kernel, and floor should stay inside the
repo and the technical docs.

## Term map: internal to public

  Judgment (object)      claim, with a status
  Judgment ledger        evidence trail, claim audit trail, receipts
  Certificate            evidence, source, proof
  Defeat                 contradicting evidence, an overturned claim
  Defeated (status)      overturned
  Theorem (status)       proven from first principles
  Observation (status)   measured
  Assumption (status)    assumed, and labeled as such
  Contested (status)     disputed
  Unaudited (status)     not yet checked
  Term                   entity, concept (never user facing)
  Floor                  first principles (this phrase already lands, keep it)
  Kernel                 the checker, a small rule engine outside the model
  Worldsheet             internal only, delete from any public surface

"Trace" is the verb to keep. It is plain English, and it is the name: Odologic
comes from hodos, the path. Every claim traces to its source, or it is marked
unproven. The brand and the mechanism say the same thing.

## Candidate category nouns, ranked

1. Evidence trail. Understood instantly by researchers, lawyers, auditors, and
   enterprise buyers. Maps to a budget line already in existence (audit,
   compliance, AI governance). Best pick.
2. Claim audit trail. Same idea, more enterprise, slightly longer. Use in
   enterprise decks and security reviews.
3. Receipts. The most memorable and the most plain. "Receipts for every claim
   your AI makes." Slightly casual for a bank, excellent for general positioning.
4. Scorecard. Matches the strategy line about keeping score of reasoning quality.
   Weaker on evidence, stronger on comparison and calibration over time.
5. Proof layer or truth layer. Reject both. They oversell. An observation is not
   a proof, and we deliberately refuse the word truth.

## What I would run

Category:

  The evidence trail for AI claims.

Mechanism, using the brand's own verb:

  Every claim traces to its source, or it is marked unproven.

Buyer consequence:

  Know which claims hold, and which are only fluent.

Deck and cold intro:

  Language models propose. The evidence trail decides.

## Cost to apply

Roughly 30 user visible strings, plus docs and fixtures:

  sketches/003-clickthrough/index.html   8
  sketches/004-argument-graph/index.html 7
  fixtures/render.py                     6
  docs/landing-copy.md                   5
  sketches/001-analyzer/index.html       3
  README.md                              3
  sketches/002-workbook/index.html       2
  sketches/002-workbook/index_run.html   2

Worst offenders in visible copy: "Odologic is a judgment ledger" (sketch 002
footer), "Ledger inspector" (sketch 001 pane), "The defeat is written to the
ledger" and "What the ledger now holds" (sketch 003).

Keep "defeat" as the internal object name in fixtures and the object model, and
use "overturned" only on public surfaces.

## Two registers, one substrate (added 2026-09-14)

Correction from Patrick: "evidence trail" sells to business, and lands badly with
individuals. For an individual the pain is not audit, it is continuity. They
re-explain themselves every session, their assistant forgets what it was told,
and it contradicts what the two of them agreed last week.

That pain has a name in our own architecture: the cognitive brief, the compact
projection of the map injected as context. So the individual pitch and the
business pitch are two faces of the same artifact. Nothing needs to be rebuilt.

Register ladder:

  Individual      automatic context management, continuity, portability
  Business        evidence trail, provenance, audit
  Governance      attestation, containment, evidentiary record

### The one true differentiator, in each register

Business: every claim shows its evidence or is marked unproven.

Individual: your AI remembers you, and it remembers what it got wrong.

That second sentence is the whole wedge, because every memory product shipping
today stores everything as true. Extract and retrieve (Mem0), temporal knowledge
graph (Zep), self-editing memory blocks (Letta) all treat what was said as a
fact to keep. None of them record a contradiction, none of them mark a statement
overturned, and none turn a correction into a permanent negative. Memory with
standing is a different object.

### Caveat: this category is crowded and funded

Verified 2026-09. Memory layers are a real market with Apache 2.0 cores:

  Mem0            59.9k stars, hosted from $19/mo, graph memory at the $249 Pro tier
  Zep / Graphiti  28.2k stars, temporal knowledge graph, Flex near $104/mo
  Letta           23.6k stars, $10M seed at $70M post, self-editing memory
  Cloudflare      Agents state substrate, $5/mo plus usage
  plus            Supermemory, Graphlit

Consequences to accept before writing the individual line:

1. "Memory" is a commodity word. Saying memory invites comparison to a $19/mo
   API. "Context management" is AI developer vocabulary, which is fine for the
   MCP crowd (Grok CLI, Claude Code, IDE agents) and wrong for a normal person.
2. "Graph memory" is already a shipped feature name at Mem0. Our graph is not
   the differentiator, standing is.
3. Open source alone differentiates nothing. All three cores are Apache 2.0.
4. The real competitor in the individual tier is not a startup, it is the lab's
   bundled free memory. Note Anthropic's 2026 memory import, free for all tiers,
   explicitly a switching cost play. That is one direction of import into one
   vendor, not a neutral store the user owns, which is exactly the gap named in
   the strategy doc: labs cannot be portable, custodial, or neutral.

### Line for the individual register

Plain person:

  Stop repeating yourself. Your AI remembers you, and remembers what it got wrong.

Prosumer or developer:

  Automatic context for every AI you use, portable, and yours.

Do not run "memory" or "context management" naked on a homepage. Either one
alone drops us into a crowded commodity shelf. Carry the correction, standing,
or portability edge in the same breath.

### Homepage consequence

One homepage cannot sell audit and continuity at once, so ladder it:

  Headline, evidence trail for the claims you rely on.
  Consumer stripe, health, product, and finance claims, "does this claim hold".
    Our omega-3 label fixture is already an individual case, not an enterprise one.
  Second stripe, your assistant remembers what was overturned, and your context
    follows you across models.

The free individual tier is also the data story: context that compounds is what
fills the map that later supports calibration and the collective signal. So the
individual register is strategically aligned, not a distraction, provided it
stays the entry tier and the business line stays the revenue line.

## Reframe v2: collective mind, individual record (2026-09-14)

Patrick's framing: "LLMs are their own collective intelligence, odologic is your
digital self that can work with LLMs with or without you."

Verdict: this is the best frame so far, and it fixes the flaw that killed the LDG
slogan. It complements LLMs instead of negating them, so it protects the MCP
distribution strategy rather than fighting the labs. Two repairs, then run it.

### Repair 1: name the axis, so the claim becomes checkable

"LLMs are their own collective intelligence" is the right intuition and a
dangerous sentence. It invites the unfalsifiable reading (LLMs are a hive mind,
are conscious, want things) and an investor eye roll. Say the checkable version
instead, which leads straight into the product:

  An LLM is the aggregate of what everyone wrote, with no record of who was right.

That is provable from how they are built, it is not a claim about minds, and the
gap it names is the product. Then the axis has a clean pair of names:

  Collective intelligence   the LLM. Trained on everything written, by everyone,
                            fluent, and with no memory of who was right.
  Individual record         Odologic. What one person knows, on what evidence,
                            and what they had to overturn.

"Record" keeps the substance that "digital self" loses. It is also the term that
carries ownership, portability, and evidence in one word.

### Repair 2: "with or without you" must be authority, not autonomy

Read cold, "works without you" means: an agent acts in your name while you are
not watching, unattributed. That is the framing that gets you a deepfake or
impersonation headline, and it is the wrong legal posture. The same capability
stated as delegated authority is stronger and sellable, and it connects straight
to the attestation and containment roadmap:

  It works for you while you sleep, and every action it takes is one you can
  defend afterward.

  Delegated. Attributed. Revocable.

The rule: never say it acts as you. Always say it acts for you, under authority
you granted, and the evidence of what it did is kept.

### Hero candidates, best first

  AI has a collective mind. You get a record of your own.

  LLMs know what everyone wrote. Odologic knows what holds.

  There are two intelligences now. One is collective, fluent, and unaccountable.
  The other is yours.

  LLMs are everyone's intelligence. Odologic is yours.

### Where this frame wins

1. It removes the anti LLM problem. Language models propose, your record decides,
   which is exactly the effect the FAQ already describes and the MCP server is
   built to serve.
2. It is legible to an individual in one breath, and it is legible to an
   investor as a durable asset rather than a feature. It is the anti obsolescence
   argument in plain words: capability gets cheaper, the record gets more
   valuable.
3. It runs the individual and business registers at once without a contradiction,
   because the record is the same object in both.

### Words to use and avoid

  keep      collective mind, individual record, yours, owned, portable,
            what holds, what you overturned, under your authority, revocable
  use once  digital self. Strong emotional pull, so keep it in the narrative and
            never as the category noun. Crowded meanings (digital twin,
            psychology, AI clone products) and it implies identity capture.
  never     acts as you, your clone, your avatar, replaces you, autonomous

## Reframe v3: the principal in a world of agents (2026-09-14)

Patrick's illustration: on Grok you can run a set of agents, each with its own
specialty, but you are still one human. Odologic could be the digital version of
you that works with those agents on your behalf, carrying your cognition and
memories.

The illustration is right and it names the real bottleneck. Three repairs.

### Repair 1: the copy is the wrong mechanism, and the wrong claim

"a copy of your cognition and memories" cannot be built and should not be
claimed. There is no mechanism for copying cognition, and the sentence invites
the two questions that end the pitch: so it is a clone of my brain, and where
does the copy live.

What we actually do is a projection, which is already the cognitive brief in the
strategy doc, and already the get_cognitive_brief tool in the MCP scaffold. One
record, projected as a compact brief into whatever agent needs it. So:

  not a copy of you, an interface to you

And the sharper reason to reject "copy" on the merits, which is a selling point
once said correctly: copies drift. Two copies of you in two agents will disagree
within a week, which is precisely the failure the ledger exists to prevent. The
value is a single source of truth for one person's standing knowledge.

  The same record, read by every agent, never duplicated.

Privacy follows from the same sentence, and it belongs in the pitch. Agents get
the brief, never the map. The full record stays local and owner held, which is
the strategy doc's privacy boundary and its adoption argument.

### Repair 2: the bottleneck is the principal, not another worker

In a world of many agents, the scarce thing is not another agent. It is you.
Every specialist starts cold, none of them know what you already rejected, and
you end up as the serialization layer, retyping your own context into each one.

  Ten agents work for you. None of them know what you already overturned.
  Odologic is the one that does, so the other nine can ask it.

That is the product in his example, and it is legible to anyone who has run more
than one agent at a time.

### Repair 3: use agency law vocabulary. It is free precision

Agency law already has the exact words for this, and investors, enterprise
buyers, and lawyers all read them correctly:

  principal        the person on whose behalf an agent acts. That is us.
  agent            the worker. Grok's specialists, Claude Code, any MCP client.
  delegated authority   what the agent may do, with scope, granted by the principal.
  attribution      every action traceable to the principal who authorized it.
  revocation       the principal can withdraw authority.

Positioning consequence: agents are labor, and orchestration is a crowded
category. The principal layer is empty. Odologic is not another worker.

  LLMs and their agents are the labor. Odologic is the principal.

### Line ladder for this register

  Present in every agent, without being the bottleneck in any.

  Your agents each have their own expertise. Odologic is the one with yours.

  It knows what you know, and it cannot be talked out of what you already
  overturned.

That last one is the strongest claim we have, because it is the only sentence in
this register that only we can say.

### Consequence for the build

This is not a new direction. It is the MCP scaffold already on the artifact list,
read aloud, four tools:

  get_cognitive_brief   project the record into an agent's context
  log_judgment          agents write claims back to the record
  challenge             the record argues back from cited evidence
  attest                authority, scope, and what was done

So the pitch for the agent era is a copy exercise on that scaffold, not a rebuild.