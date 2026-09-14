# Why now: the inspectability axis

Status: first pass, 2026-09-14. This is the investor facing "why now" argument. It replaces
the continuity framing (Odologic is the next step in a long line of cognitive tools) with a
sharper and more defensible one.

## The wrong version, and why it is wrong

The tempting pitch: writing, notation, double entry bookkeeping, Excel, and now LLMs are all
cognitive offloading, each one boosted human performance, so Odologic is the next step in
that line.

It is tempting because it is flattering and almost right. It fails on one counterexample
that every sharp listener already has loaded: GPS. GPS is offloading too, and the evidence
is that it degrades spatial reasoning. If the pitch is "offloading is fine, look at the
history," a single GPS question kills the slide.

Conceding the word is also the wrong move. Notation is a cognitive technology. So is
writing. So is Excel. None of them atrophied the layer that mattered, and the extended mind
argument is correct: the tool becomes part of the reasoning system rather than a substitute
for it.

## The real axis: does the derivation survive the delegation?

Not offload versus no offload. The axis is whether the derivation survives the delegation.

Pencil and paper arithmetic. Deterministic. The work shows on the page. You can redo it.

Excel. Deterministic, replayable, inspectable. Same inputs, same outputs. Click a cell and
see the formula. Trace precedents and dependents. Find the error. Arithmetic got delegated;
model choice, assumptions, and interpretation stayed with the human. And here is the
precedent that matters. When spreadsheets started producing errors in finance and in
published economics (the best known case being a heavily cited austerity paper whose
findings turned on a spreadsheet coding error, found by a reader who opened the file), the
industry did not abandon the spreadsheet. It built dependency tracing, arrows from a cell
back to its sources, so you can walk from a number to the floor it stands on. That is this
product, pointed at a different substrate.

GPS. Not inspectable. You get a route you cannot verify, cannot reconstruct, cannot replay.
You keep the answer and lose the derivation.

Every cognitive technology that safely absorbed delegation did so because its substrate was
inspectable by construction. Arithmetic on paper shows its work. A spreadsheet recomputes on
demand.

## What the language model broke

The language model does not have that property.

Non deterministic. No replayable derivation. Self reported reasoning is unfaithful, so even
the trace it offers is not evidence.

This is the first cognitive tool in the line where the delegated layer is the judgment
layer itself, and where nothing inspectable is left behind. It took the scarce layer and
returned an answer with no floor under it.

## The positioning that follows

Odologic is not another step in the same direction. The last step broke the property every
previous step shared, and Odologic restores it.

    Excel, for judgment.

Which means the derivation has to be manufactured explicitly, because the substrate will not
supply it. That is the product. Claim, attack, defeat, reinstate, recorded, with the
provenance of each item, so that a number of any kind can be walked back to the ground it
stands on.

This framing is stronger than continuity on two counts. It answers why now, and it explains
why the LLM is the first cognitive tool that needed an audit layer built next to it before
the industry could trust the delegating.

## The atrophy objection, answered properly

Atrophy concentrates in whatever layer you hand over.

Hand over arithmetic and nobody cares, because arithmetic is not the binding constraint.

Hand over the judgment and you hand over the thing that was scarce. That is the GPS case,
which is also why GPS is the right analogy for an unsupervised model and the wrong one for a
ledgered brief.

The brief spec takes load off in exactly the safe place (re explaining yourself to every
model) and adds load where the check happens (looking at what was selected and why). That is
the pencil, not the GPS.

## Where this goes

Investor thesis one pager: "why now" section.

Landing copy: the dependency tracing line is the plain language version of the whole
category, one sentence, no jargon.

Deck: one slide. Pencil, Excel with its dependency arrows, GPS, then a language model with
nothing under it, then the ledger.

## Open questions

1. Is "the derivation survives the delegation" the right phrase for a non technical reader,
   or does it need a plain language twin (a number you can walk back to its floor)?
2. Does the Excel precedent hold under close scrutiny? Dependency tracing arrived in later
   spreadsheet versions rather than in the first ones, so the honest line is that the
   auditing features followed the errors, not that they shipped together. Confirm the
   version and date before it goes on a slide, and confirm the austerity paper citation
   (the numbers and the mechanism, not just the anecdote).
