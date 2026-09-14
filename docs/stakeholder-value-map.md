# Stakeholder value map, and where AGI moves it

Status: first pass, 2026-09-14. Ordering matters here and this doc enforces it: identify where
the value is first, map the stakeholders to that value second, and derive the business model
third. Business model is Part E and it is deliberately the shortest part, because a pricing
scheme that does not fall out of the value map is a guess. Facts referenced with numbers are
sourced in docs/competitive-and-market.md.

# Part A, the two value objects

There are exactly two things being built, and they are not the same asset. Confusing them is how
this pitch goes wrong, because one is a personal asset and the other is a public good with a
price.

V1, the individual cognitive map. One person's claims, positions, defeats, resolutions,
calibration record and constraints, held privately and locally. Its value to that person is
spared re-explaining, a record of their own reasoning, and a portable credential that survives
changing models and employers.

Properties of V1:
- Private by default, compounding slowly, worthless to anyone else.
- It is an asset the individual owns and can carry, which is the whole adoption argument.
- It is unverifiable by third parties unless the holder chooses to open it.

V2, the collective human cognition map. Consented, scoped, calibration gated contributions
across many people, plus the settlement and provenance record of who contributed what. Its value
is coverage, error correction, and legitimacy: it is the live evidence that a judgment came from
an accountable human rather than a generated string.

Properties of V2:
- Public-good-ish in character, which is exactly why it cannot be sold as a file: distillation
  erodes content, and Stack Overflow is the demonstration (a corpus valuable enough to license
  while its contributor supply collapsed).
- Its durable value is legitimacy, diversity and provenance, none of which survive being copied.
- It only exists if the individuals are compensated and have a governance voice, so V2's
  integrity depends on V1 being respected.

The relationship to state plainly: V1 is the unit of accumulation, V2 is the unit of leverage.
Every stakeholder wants a different one of those, and that is the whole map.

# Part B, stakeholders against the two value objects

Four stakeholders, and each one is mapped on four questions: what they contribute, what they get,
what they would pay for, and how they could defect.

## 1. Individuals

Contribute: claims, defeats, adjudications, outcome data (was I right), time, and consent. They
are the only source of the raw material in both value objects, and the only source of legitimacy.

Get from V1: less re-explaining, better model output, a private record of their own reasoning,
defensibility when questioned, and a personal calibration record that is portable.

Get from V2: the option to be paid for scoped contributions, a governance voice, and the
epistemic benefit of other people's defeats, which is the part a single person cannot generate
alone.

Pay for: V1 attached to a seat they already buy (Copilot is $30 per user per month, ChatGPT
Business premium $100, so a judgment layer at a fraction of that asks for no new budget line).
V2: they are paid, not charged.

Defection path: export and leave. Guaranteed export is what keeps this from being a lock-in
story, and Claude already ships memory import and export, so the expectation exists.

Their leverage: exit, plus the fact that consent cannot be manufactured. If they do not
contribute, V2 does not exist.

## 2. Businesses (employers, enterprises)

Contribute: budget, work scope context, consent infrastructure, distribution inside the org, and
the demand that makes accountability a paid line item.

Get from V1: nothing directly, and this is where the conflict lives. They get the work scope
view, not the person's capability layer. The employment law analogy holds: work product versus
skill. An employer licenses what was decided at work, the individual keeps the calibration record
and the reasoning habits.

Get from V2: a consented, aggregated view of how the organisation reasons, with dissent preserved
and provenance intact, plus institutional memory that survives attrition, plus the audit and
attestation artefact for regulators. This is the defensibility purchase, and it is the largest
near term wallet in the map.

Pay for: per seat plus a platform fee, and a metered attestation line item. Anchor: enterprise
compliance budgets and AI governance spend already exist (Forrester puts AI governance software
spend at 30 percent CAGR to 2030, in the landscape doc).

Defection path: build it in house, demand custody, or buy the bundle that already satisfies their
written audit obligations (a GRC platform plus an observability platform, which is the nearest
substitute identified in the landscape work). The custody demand is the toxic one: it converts
the ledger of a person into monitoring of an employee, and it kills contributor supply.

Their leverage: the money, and the ability to make the individual's participation a condition of
employment. Any product design that lets them do that has chosen its side.

## 3. LLMs and frontier labs

Contribute: the reasoning substrate everything sits on, plus distribution (an MCP surface means
every harness they improve becomes our delivery channel), and the compute and capability that
make the brief valuable in the first place.

Get from V1: personalisation quality. A model with the brief answers in your frame rather than
asking you to re-establish it. This is real but depreciating, because a stronger model needs less
briefing.

Get from V2: something far more valuable than text, which is the record of what was rejected and
why. Training corpora contain conclusions; a judgment ledger contains defeats, adjudications and
calibration outcomes, which is the difference between knowing what people said and knowing which
of two claims survived contact. That is evaluation and preference signal of a kind that is hard
to synthesise, and it is the thing that stays valuable when raw content is worthless.

Pay for: data licences (Reddit sold its corpus to Google for roughly $60M a year; Shutterstock
pays contributors a 20 percent average royalty on dataset licensing) or attestation services for
their own agents. They can also choose not to pay and simply build memory plus status themselves,
which the landscape work shows is one product cycle of work.

Defection path: build it, or distil it. Distillation is the specific risk that V2's content value
decays, which is why the sellable asset must be live legitimacy rather than a file.

Their leverage: enormous, and structurally conflicted. A lab cannot be neutral across models. It
sells to the operator rather than the person. It cannot hold a record that has to survive
switching to its competitor. That is the argument for why the record cannot be theirs, and it is
also why their biggest contribution to us is distribution rather than custody.

## 4. Odologic (the company)

Contribute: the schema and the lifecycle (theorem, observation, assumption, contested, defeated),
the defeat relation, provenance typing, the brief projection, the consent and settlement ledger,
the calibration gate, and neutrality across models.

Get: revenue from businesses and individuals, a spread on the contributor economy, attestation
fees, and the position itself, a clearinghouse between mutually distrusting parties: individuals
against employers, employers against labs, labs against auditors.

Pay for: the category creation cost, the extraction quality work, and the cold start.

Defection path for the whole company: the three ways it stops being needed. If it takes custody
it becomes a surveillance vendor and loses individuals. If it affiliates with a lab it loses
neutrality and therefore labs two through five. If it sells the map as a file, the file is copied
and the legitimacy is gone. Those three are the same failure wearing three coats: it stops being
the neutral party.

Its leverage: neutrality, which is not a feature and cannot be retrofitted by a landlord, plus the
accumulated record, which cannot be copied retrospectively.

# Part C, the value matrix against AGI

Two axes again: whose judgment, and what is being paid for. Read with AGI as a moving dial.

    who holds judgment   performance value        accountability value
    human alone          none                     calibration record, legitimacy        rising
    human plus model     the brief                the trace, export                    rising
                                                  (brief falling, trace rising)
    model alone          deflates to zero         attestation, containment             rising
                                                  (speculative buyer)

Three stages, and the honest reading of each:

Stage 1, now. Performance is the easy sale and accountability is the durable one, both to the same
individual. V1 accumulates. V2 barely exists. Revenue is thin and that is expected.

Stage 2, mid. Model capability rises, briefing demand softens, and the employer becomes the buyer
of record for V2, which is where the money actually is. V1 keeps compounding underneath and stays
the individual's property, which is what makes V2 marketable as consented rather than harvested.

Stage 3, AGI or near it. Performance cells go to zero. Two things inflate. Attestation, which is
machine to machine and needs the schema to have treated machine agents as subjects all along.
And legitimacy, because when machine judgment is abundant the scarce input is a judgment that is
traceable to an accountable party, and markets for that already exist at real prices (Tegus at
$930M for a consented insight library, Mercor at an estimated $2.00B selling expert judgment,
roughly $24B a month of settled judgment across the prediction markets).

The tail case, stated as insurance not plan: under full labour displacement, the audit of human
judgment loses its buyer, and what survives is machine to machine attestation plus human
legitimacy as a premium input rather than a labour input.

# Part D, conflicts to name in the room

These are the questions an investor will ask, so they should be on the slide before they are
asked from the floor.

1. Individual versus employer. Custody and surveillance versus ownership and portability. Answer:
   work scope licenses to the employer, capability layer stays with the person.
2. Individual versus lab. The lab wants the record for signal, the individual wants to be paid
   for it and to keep it. Answer: consent plus settlement, never silent harvest.
3. Employer versus lab. When a model's decision causes harm, who is answerable. Answer: the
   ledger records authorization and evidence for both sides, which is why it can sell to both.
4. Odologic versus all three. Neutrality is the asset, and every revenue line that compromises it
   is a short term win. Answer: local first, guaranteed export, no custody, no lab alignment.

# Part E, what falls out for the business model (derived, not asserted)

Only after A to D, and this part should stay short until the value map above is agreed.

    line                    value object   stakeholder     mechanism              state
    1 free local ledger     V1             individual      free, near zero        build now
                                                          marginal cost
    2 paid sync and relay   V1             individual      seat fraction          build now
    3 enterprise aggregation V2            business        per seat plus          funding revenue
                                                          platform fee
    4 contributor economy   V2             individual      quality gated payout,  later, after
                                            and business   20% royalty benchmark  track record exists
    5 attestation           V2             labs, business  metered per record     hedge, price it
                                                                                 from day one

The sequencing is a consequence of the value map, not a preference. V1 must exist and compound
before V2 has anything to aggregate, and V2 must be consented and settled before it can be sold
without destroying itself. Attestation cannot be the opening pitch because the buyer does not
exist yet, but the pricing line item should exist in enterprise contracts so it is real when the
buyer arrives.

# Part F, what is still unproven in this map

1. Whether individuals pay for V1 at all, or only use the free tier. Unmeasured.
2. Whether the employer will accept a consented, scoped view rather than demanding custody. This
   is the single biggest commercial assumption in the map and it has no evidence yet.
3. Whether anyone pays for contributor judgment on verified calibration, since no market does
   that today (expert networks pay per hour, crowd platforms per task, prediction markets by
   trading profit, Metaculus in reputation only).
4. Whether V2 is worth more than V1 in money as well as in argument. Supported on price and error
   correction (the Tegus comparable), not supported on mechanism.
5. Whether attestation ever becomes a real budget line outside regulated industries.
