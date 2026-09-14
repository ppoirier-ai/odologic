# Distillation risk: what happens when the model eats the map

Status: first pass, 2026-09-14. This is the sharpest threat to the product, and the answer is not
that it cannot happen. It happens. The answer is that absorption destroys a specific part of the
value and leaves a different part intact, and the product has to be aimed at the second part.

## The threat, stated precisely

If the brief is injected as context, the model sees it, and the lab sees what the model sees. So
the map leaks outward every time it is used, and an ever changing map does not fix that, because
each version is absorbed on the way past. Three variants, in increasing order of seriousness.

Variant 1, weight level. Prompts are retained and used for training or distillation, so your
positions end up as a tendency in a model you do not control. This variant is the most discussed
and the least dangerous for enterprise deals, because it is contractually addressable. OpenAI
offers zero data retention to eligible API customers (announced 19 August 2026), has stated since
March 2023 that API data is not used to train models unless the customer opts in, and Anthropic
offers ZDR arrangements for the Claude API and Claude Code for Enterprise subject to approval.
Sources: https://openai.com/index/offering-zero-data-retention-for-frontier-models/ and
https://platform.claude.com/docs/en/manage-claude/api-and-data-retention

Variant 2, in context absorption, and this is the one worth worrying about. No training required.
A session level or memory level model of you is built and kept inside the product, and the
assistant memory features make it a designed behaviour rather than an accident. This is not
hypothetical: Claude already ships memory import and export, and the documented import flow is a
prompt that asks your previous provider to dump your memory. So the pattern of pulling a user's
context into a landlord's store is already shipped and normalised.

Variant 3, population consensus. At scale, absorbed maps across millions of users give a lab an
aggregate model of human judgment, with no consent and no payment. This is the variant that
actually threatens the collective map, because it is the aggregate built without the individuals.

## What distillation actually loses, and why it is not symmetric

Absorbing a map gets you the state, not the process. Four things do not come across, and each one
is a load bearing part of the value.

    absorbed                        not absorbed
    your positions                  the defeats attached to them
    the current version             the version history and what it superseded
    the content                     provenance, consent, and who is answerable
    a snapshot of you               the record of whether you were right

And there is a failure mode inside the loss, which is the useful part: an absorbed map goes stale
silently. The lab's copy is a mirror of a former you, and a mirror is worse than a stranger
because it launders old errors back as confident agreement. The lab cannot self correct it,
because it does not know the map changed. The ledger does, because the change is the record.

So the honest formulation: absorption destroys personalisation value, which is the value that
decays anyway as models get stronger, and it cannot destroy verification value, which is the
value that compounds, because verification is exactly the question of what is current, consented
and defeated.

## Absorption is not free for the lab

An absorbed map is an unaudited, unprovenanced, unversioned snapshot with no consent chain. In a
regulated or contractual setting that is a liability, not an asset, and the direction of
regulation makes it worse for them over time: the more provenance requirements land, the more an
untraced belief about a user is a problem to hold. The strategic version of this argument is that
traced judgment becomes an asset and untraced judgment becomes a legal exposure, and the ledger
sits on the right side of that line.

## The defense stack

Layer 1, product inversion. Never price the brief. The brief is a consumable, it will be eaten,
and pricing it monetises a depreciating asset. Price verification instead: the ledger's second
job becomes telling the user what the model currently believes about them, where that belief came
from, and whether it is out of date. This is the same inversion that runs through the whole
thesis: personalisation value falls as capability rises, verification value rises.

Layer 2, an absorption detector, which turns the threat into a feature. Version and expire every
brief, sign or hash the selection, and keep the superseded versions in the trace. Then probe the
model with questions that only a stale absorbed map would answer, and compare its answers to the
current ledger. If it echoes a position you defeated three weeks ago, you have demonstrated
retention and staleness in one test, and you can hand the user a report that says what the model
believes, when it learned it, and what has changed since. No lab can provide that report about
itself.

Layer 3, technical containment, which reduces the harvest per turn but cannot stop it. Inject
only what this turn needs, per the brief spec, so the surface per interaction is small. Keep a
sealed ledger separate from the injectable brief, so values and anything you would never want
absorbed simply never enter a prompt. For the highest sensitivity tier, the only real answer is
that inference does not leave the perimeter: a local model, or confidential computing with
attested enclaves, where access to prompts is gated by hardware attestation rather than by policy.
This is no longer theoretical (NVIDIA confidential computing on Hopper, Blackwell and later, and
current research on end to end CPU and GPU TEE inference), but it is partial in 2026 and it bills
at a premium. Sources: https://www.nvidia.com/en-us/data-center/solutions/confidential-computing/
and https://arxiv.org/html/2606.31408v1

Layer 4, contractual, and be honest about who it protects. ZDR and no train terms protect the
enterprise buyer who can negotiate them. They do not protect a consumer, and they cannot be
verified from outside, only detected after the fact by the layer 2 probe. So the consumer tier's
protection has to be a product property (local first, sealed ledger, minimal injection), not a
contract.

## Why this strengthens the thesis instead of killing it

If every lab absorbs a private map, then every lab ends up holding a different, private, partial
model of you, and none of them are commensurable with each other. Meanwhile the human's actual
record, with defeats, provenance and outcomes, is the only thing that is neutral across all of
them and portable between them. Absorption is therefore an argument for the clearinghouse
position, not against it, but only if the ledger is where verification lives and only if the
record is not itself absorbed in a usable form.

## The residual risks, stated plainly so they are not discovered later

1. Population scale absorption. If labs hold an aggregate of everyone's maps, the collective map's
   market could be undercut by an aggregate nobody consented to. Defenses are fragmentation (scoped
   consented subsets, per domain gates rather than one big pool), the legitimacy premium (buyers
   who need provenance cannot accept "we absorbed it"), and regulation that makes untraced data a
   liability.
2. The feature gap. Claim status and defeats inside an existing memory product is one product
   cycle of work, already flagged in the landscape doc. Absorption plus status would be the
   combination that hurts.
3. Enclaves are partial. Local and confidential inference cover the sensitive tail, not the
   mainstream, in 2026.
4. You cannot verify a promise, only detect a violation. The probe is evidence, not prevention, and
   the pitch should say evidence.

## If confidentiality arrives (FHE or attested enclaves)

Assume the strong version: inference runs on ciphertext, or inside an attested enclave, and the
provider never reads the prompt or the answer. Then:

1. Variant 1 and variant 2 absorption die. A provider cannot train on, or memorise, what it
   cannot read, so per user absorption and population consensus both become infeasible rather
   than merely forbidden.
2. The content moat is dead in the same stroke, and this is the important part: if nobody can
   read user maps, then no vendor can build an exclusive corpus advantage out of them. So the
   question of who accumulates the most content stops mattering.
3. The aggregate moat survives, but only as a consented aggregate, and it gets stronger. Because
   unauthorised aggregation becomes cryptographically infeasible instead of legally prohibited,
   the licensed aggregate turns into a genuinely exclusive asset: it cannot be scraped, cannot be
   absorbed, and can only be granted. Cryptography converts a legal restriction into a physical
   one, which is precisely the property that makes the strongest moats strong.
4. Cryptography creates no exclusivity on its own. FHE is an open standard, so if it becomes
   universal every vendor offers blindness and confidentiality stops being a differentiator, the
   same way open source telemetry already removed data sovereignty as a differentiator. What
   remains exclusive is the keys, the consent, and the calibration credential.
5. Verification becomes the new moat layer. Encrypted inference means the user cannot see what
   was computed, so the demand shifts to proving it: attestation reports, signed records of what
   the model was given and what it returned. That is a longer lease on the hardware roots and
   revocation entry in the catalogue, and it is a new one: verifiable inference records.
6. New vulnerability, and it is not small. If confidentiality depends on trusted hardware, the
   party that can read everything becomes the silicon vendor, since enclave trust is trust in
   their attestation. Provider level absorption is replaced by hardware vendor level trust, which
   is a landlord nobody in this story controls. A TEE based answer to absorption moves the trust
   problem down one layer rather than removing it.
7. Practical caveats. Homomorphic inference at transformer scale carries heavy overhead today, so
   attested enclaves are the realistic near term form, and their trust model differs. Providers
   may also refuse encrypted inference outright, because they cannot moderate what they cannot
   read, which means confidentiality will likely arrive through local open weight models first,
   and in that scenario the counterparty is not a lab at all.
8. The weakest link moves to the endpoint. If the ledger and the brief sit on the user's device
   in plaintext, or the harness is the decrypting party, the leak is the client rather than the
   provider.

Net: a data moat still exists, but its location moves from content to access, and its enforcement
moves from terms of service to mathematics. The exclusivity still comes from consent, calibration
and institutional position, because the cryptography is available to everyone.



## Product implications, in order of urgency

1. Sign or hash brief selections and store them in the trace, so any later claim about what the
   model knew is checkable against a version.
2. Give every brief a validity window and keep superseded versions queryable.
3. Build the probe suite as a first class feature, and sell the report.
4. Split sealed ledger from injectable brief as a schema level distinction, not a setting.
5. Never price the brief. Price sync, enterprise aggregation, verification and attestation.
6. Keep the local and confidential inference tier on the roadmap as the answer for the accounts
   that cannot accept prompt exposure at all.
