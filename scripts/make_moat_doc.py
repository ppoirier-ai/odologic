import sys, re, json
sys.path.insert(0, '/root/.hermes/skills/productivity/google-workspace/scripts')
from google_api import build_service

docs = build_service("docs", "v1")
drive = build_service("drive", "v3")

TITLE = "Competitive moats: what holds value in a post-AGI market"

# ---------------- content blocks ----------------
# ('h1'|'h2'|'h3', text) ('p', text) ('bullets', [..]) ('numbers', [..]) ('table', [[...]]) ('callout', text)

B = []
def h1(t): B.append(('h1', t))
def h2(t): B.append(('h2', t))
def h3(t): B.append(('h3', t))
def p(t): B.append(('p', t))
def bl(items): B.append(('bullets', items))
def nl(items): B.append(('numbers', items))
def tb(rows): B.append(('table', rows))
def co(t): B.append(('callout', t))

h1(TITLE)

p("Status: working note, September 2026. Three moat candidates are assessed as proposed, then a "
  "catalogue of moats that could survive in a world where cognition is abundant and software is "
  "trivial. Sources for the numbers referenced here live in the Odologic repo docs, in "
  "competitive-and-market.md and moat-design.md.")

h2("1. The test")

p("If software is trivial and cognition is abundant, then any moat made of thinking is rentable. "
  "The test for every candidate below is one question: can a party with unlimited cognition obtain "
  "or replicate this?")

p("Only three classes pass that test:")
bl([
  "Legal and institutional constraints: things that require a licence, a contract, a court, an insurer or a regulator to exist.",
  "Hardware roots of trust: keys, enclaves, attestation, and the ability to prove that something was erased.",
  "Human acts that cannot be synthesised: consent, accountability, and outcomes that only exist once real time has passed.",
])
p("Everything else (features, model quality, content, taste, speed) is copyable, and copying is cheap.")

h2("2. Candidate 1: network effect, individual data versus collective crowdsourced data")

p("The proposal is that aggregate crowdsourced judgment becomes exponentially more valuable than "
  "any individual map, and that this curve is the moat. The mechanism is real but the exponent is not.")

h3("Why it does not compound exponentially here")
nl([
  "Judgment is domain partitioned. Aggregate value scales within a domain, not with global contributor count. Cardiology adjudication does not improve a supply chain adjudication, so the structure is many small pools with modest n, not one network.",
  "The data is text, and text is distillable. Anything that can be absorbed and reproduced cannot be the moat.",
  "Aggregate accuracy depends on independence, and independence degrades as a pool grows. The diversity prediction theorem rewards heterogeneity and has documented counterexamples, so the marginal contributor is worth less exactly where the network effect is supposed to bite.",
  "There is no exclusivity. A contributor can give the same judgment to a lab, an expert network and a ledger. Multi homing kills the classic form.",
])
p("What the aggregate still buys is coverage, error correction and legitimacy. Those are worth paying "
  "for, and they do not compound superlinearly. Treat the collective map as a market position that "
  "has to be built institutionally, not as a curve that arrives by itself.")

p("One design consequence that matters more than the curve: the aggregate must be consented and "
  "revocable. Unconsented aggregation is a liability under provenance rules, and it destroys the "
  "legitimacy that was the only durable part.")

h2("3. Candidate 2: financial network effect, or the token economy")

p("This candidate is correctly described: a token creates an incentive to be early, because price is "
  "supposed to rise as adoption grows. It also contains the seed of its own reversal, and the reversal "
  "is mechanical rather than sentimental.")

h3("The positive loop")
bl([
  "Early participants are paid in an asset whose value is a claim on future adoption, so early participation is rewarded more than late participation.",
  "The rising price buys attention, which buys adoption, which lifts the price. Coordination around a shared ledger or curation task gets easier when there is a common scoreboard.",
])
h3("The negative loop, which is the part to design against")
bl([
  "A token price is a claim on future adoption, so it prices in the plateau before the plateau arrives. When growth decelerates, the asset re rates first and the product feels it second.",
  "At the plateau, holding is no longer rewarded and the rational move is to exit, so the incentive that bootstrapped supply now drains it. Reflexivity runs both directions.",
  "Mercenary capital leaves first, which is the capital that set the price, which is the signal everyone else was reading.",
  "Contributor quality tracks token price rather than verified accuracy, so the quality gate becomes a price gate. That is the opposite of the calibration gating this product needs.",
  "Governance concentrates in the largest holders, so the legitimacy story dies the moment whales finish voting.",
  "Regulatory classification risk attaches to the whole company, not to one feature.",
])
h3("If a token is used at all, the design rules")
nl([
  "Fiat subscription stays the front door. Crypto rails should remain a rail, never the identity.",
  "Pay for verified contribution, not for appreciation. The reward should be a work payment for a scoped, calibration gated item.",
  "Stake is non transferable, locked, or decaying, so holding cannot be the strategy and exiting is not a yield trade.",
  "No deposit taking, no float, no promised yield. No custody of other people's money.",
  "Membership bonds are refundable rather than appreciating, so the incentive is to stay and to participate.",
])
p("Verdict: a token is a coordination mechanism for bootstrapping supply, not a moat. As the lead story "
  "it is a liability, because its price becomes the product's public scoreboard and the negative loop "
  "is then read as the company failing.")

h2("4. Candidate 3: branding")

p("The instinct is right and the conclusion needs refining. Selection pressure moves away from emotion, "
  "but it does not move away from risk.")

bl([
  "What an agent selects on is verifiable properties: uptime, cost, compliance, attestation, indemnity, exit rights. An agent does not buy because the logo feels good.",
  "So brand is converted into machine readable claims. Certification, audit rights, insurance, service levels, provenance attributes. What used to live in reputation has to live in an artefact.",
  "Where brand still bites is where a human institution holds the liability. A committee, a regulator, an insurer or a court will not accept an API response as evidence, and will not accept an unattributed system as the accountable party. In that room the question is not which product is nicer, it is which named entity is answerable.",
  "That means brand stops being mood and becomes a certified trust signal. Which is not really branding, it is the legal personality and institutional entrenchment entries in the catalogue below.",
])
p("Verdict: brand as feeling is dead in an agent mediated market. Brand as a verified, contractually "
  "supported trust attribute is alive, and it is a consequence of the moats below rather than an "
  "independent one.")

h2("5. The catalogue: moats that can survive abundant cognition")

p("Each entry is scored on the same question: what makes it hard to obtain by a party with unlimited "
  "cognition, and what does holding it cost us.")

h3("M1. Neutrality with credible commitments")
p("Why it survives: a landlord cannot be neutral. A lab rents the model it would be judging, an employer "
  "is a party to the disputes it would adjudicate, and a memory vendor is a feature of somebody else's "
  "stack. None of them can be the record both sides accept.")
p("What it costs: neutrality is only a moat when faking it is expensive. It has to be built from things "
  "that are hard to reverse, which means local first architecture, a source available schema, a no "
  "custody covenant in the charter, a steward structure, and guaranteed export. Every one of those "
  "costs margin or optionality.")

h3("M2. Legal personality and insurable accountability")
p("Why it survives: an AGI cannot be sued, insured, licensed or bonded in any way that matters, and it "
  "cannot post capital against a loss. A legal entity with capital reserve, errors and omissions cover, "
  "indemnification capacity and a named officer is doing something cognition cannot do. Liability "
  "absorption is the most underrated moat of the next decade, because capability increases the demand "
  "for someone to blame and the supply of blame taking entities does not scale with compute.")
p("What it costs: real capital, real insurance, real legal exposure, and the discipline to refuse work "
  "outside the insured envelope.")

h3("M3. Hardware roots of trust, and the revocation asymmetry")
p("Why it survives: a key in an enclave and an attestation report are physical facts. Once a fact is in "
  "model weights it cannot be withdrawn, while a ledger can honour withdrawal, prove it, and produce the "
  "record that revocation happened. As consent and provenance requirements land, provable erasure becomes "
  "an obligation and the absorbed copy becomes permanently out of compliance while the signed record "
  "is not. Confidential computing with attested CPU and GPU enclaves is already shipping, so this is "
  "available rather than speculative.")
p("What it costs: engineering, premium compute, and the honesty that enclaves cover the sensitive tail "
  "rather than the mainstream in 2026.")

h3("M4. Institutional entrenchment: being the record that gets cited")
p("Why it survives: once a contract, an audit standard, an insurer or a regulator points at one ledger as "
  "authoritative, displacing it is a re litigation nobody wants. This is how credit bureaus, exchanges "
  "and certification bodies hold their position, and none of them are defended by software.")
p("What it costs: one narrow domain, years of sales patience, and accepting that the reference record is "
  "a slow asset.")

h3("M5. Licences, permits and exclusive rights")
p("Why it survives: scarcity created by law is scarce even for a superintelligence. Regulated activity "
  "requires an approved party, procurement requires an eligible vendor, and some data can only be "
  "lawfully obtained by an entity that has consented rights.")
p("What it costs: compliance overhead and a willingness to operate in unglamorous domains.")

h3("M6. Consent and legitimacy as non synthesised inputs")
p("Why it survives: a model can generate an opinion, and it cannot be the party that consented to "
  "something. Legitimacy requires an actual human act and a record of it, and machine generated content "
  "increasingly needs to prove that a human is behind it.")
p("What it costs: contributor care, governance voice, and paying people properly, which is a permanent "
  "cost rather than a one time build.")

h3("M7. Time locked outcome data")
p("Why it survives: a calibration record needs the world to resolve. Five years of being right takes "
  "five years, and no amount of compute compresses it. This is the only moat that is literally made of "
  "waiting, and it is therefore the one an incumbent can never buy retroactively.")
p("What it costs: patience, outcome collection discipline, and resisting the temptation to score "
  "predictions on their own terms rather than against realised results.")

h3("M8. Standard and coordination position")
p("Why it survives: if the schema becomes the interchange format for defeasible claims, everyone else "
  "implements our definition and the reference implementation, the conformance suite and the "
  "verification service become the commercial position. Standards are weak at capture and strong at "
  "entrenchment.")
p("What it costs: opening the schema, which gives away the only thing that currently looks like an "
  "asset, and running a governance process that is genuinely not ours to rig.")

h3("M9. Accumulated private history (switching cost)")
p("Why it survives: a competitor can start fresh but cannot back fill a person's history, and history is "
  "what makes a calibration record meaningful. It is a mild moat and it protects retention, not "
  "acquisition.")
p("What it costs: nothing, provided export stays real.")

h3("M10. Physical bottlenecks (listed for completeness, not for us)")
p("Energy contracts, fabrication capacity, land, spectrum, logistics. Rock solid and irrelevant to a "
  "judgment ledger, except as a reminder that the strongest long term moats are usually physical or "
  "legal rather than informational.")

h3("M11. Contractual embedding")
p("Why it survives: the moment an attestation line item appears in a signed master agreement, the "
  "record is part of somebody's compliance evidence and removal means re papering the relationship. "
  "This is how unglamorous enterprise categories become permanent.")
p("What it costs: enterprise sales capacity and the patience to be a line item rather than a platform.")

h2("6. Scoring")

tb([
  ["Moat", "Durability in a post-AGI market", "Time to build", "Can an AGI bypass it", "Cost to us"],
  ["M1 Neutrality with commitments", "High", "Medium", "No, by construction", "Margin, optionality, control"],
  ["M2 Legal personality and insurable accountability", "High", "Short to medium", "No", "Capital, insurance, exposure"],
  ["M3 Hardware roots and revocation", "High", "Short", "No, it is physical", "Engineering, premium compute"],
  ["M4 Institutional entrenchment", "High", "Long", "No, it needs the institution", "Domain focus, sales patience"],
  ["M5 Licences and permits", "High", "Medium to long", "No", "Compliance overhead"],
  ["M6 Consent and legitimacy", "High", "Long", "No, it needs a human act", "Permanent contributor cost"],
  ["M7 Time locked outcomes", "High", "Long, cannot be compressed", "No, it needs elapsed time", "Patience"],
  ["M8 Standard position", "Medium to high", "Medium to long", "Partly, they can adopt or fork", "Opening the schema"],
  ["M9 Accumulated history", "Low to medium", "Grows with users", "Yes, over time", "None"],
  ["M11 Contractual embedding", "Medium to high", "Medium", "Yes, by replacement", "Enterprise sales"],
  ["Data network effect", "Low", "n/a", "Yes, they can absorb it", "Wasted effort"],
  ["Token economy", "Low, and negative at plateau", "Short", "Yes, and it is reflexive", "Reflexivity, regulation"],
  ["Brand as emotion", "None in agent mediated buying", "n/a", "Yes", "n/a"],
])

h2("7. Anti-moats: what will not hold")

bl([
  "Software features. One product cycle of work, as the memory vendors already demonstrate.",
  "Model quality. Not our asset, and it belongs to somebody else's capital budget.",
  "Content corpora. Distillable, as the Stack Overflow collapse and the absorption analysis both show.",
  "Data volume without consent. Progressively a liability rather than an asset.",
  "User interface and taste. Copied in a weekend.",
  "Community goodwill without governance. Evaporates the first time the platform captures value, which is the documented Stack Exchange moderator strike pattern.",
  "Being first. In a category with trivial replication, first is a cost centre, not a moat.",
  "Patents on software logic. Weak, slow, and expensive to enforce against large parties.",
])

h2("8. Tests to run next quarter")

nl([
  "Reference test. Will an outside party accept our record in place of their own paperwork in a live decision? Ask a compliance officer, an insurer, an audit firm and a journal. One yes starts an institutional moat.",
  "Revocation test. Will an enterprise pay specifically for provable withdrawal and erasure across vendors? This is the fastest commercial proof of the hardware roots position.",
  "Aggregate price test. Will a buyer pay materially more for the aggregate record than for the sum of individual records? If not, the network effect story has to be dropped from the pitch.",
  "Counterparty test. Does a lab or an employer accept a ledger they do not control? If every incumbent demands custody, the position is real but the market is narrower and slower.",
  "Embedding test. Will an attestation line item survive into a signed master agreement, even at token value? Signed paper is the beginning of M11.",
])

h2("9. What this implies")

co("The moats that survive are legal, institutional and physical, plus consent, plus elapsed time. "
   "Data is the raw material that makes a position possible. It is not the position. The company that "
   "matches this analysis is a neutral registry with a commercial arm selling verification, "
   "deployment and attestation, where the neutrality is structurally true rather than promised.")

p("Two consequences worth stating plainly. First, the pitch should stop leading with the data network "
  "effect and start leading with the position: the neutral record both sides can accept, provable "
  "revocation, and a credential that only time can mint. Second, the shape of the company follows from "
  "the choice of moat. If neutrality is the moat, then the margin and control that neutrality costs is "
  "not a sacrifice, it is the purchase price.")

doc = docs.documents().create(body={"title": TITLE}).execute()
doc_id = doc["documentId"]

# ---------------- build text with markers ----------------
text_parts = []
para_marks = []   # (start, end, style, text)
table_marks = []  # (start, end, rows)
pos = 1

def emit(s):
    global pos
    start = pos
    text_parts.append(s)
    pos += len(s)
    return start

for kind, payload in B:
    if kind in ("h1", "h2", "h3"):
        s = payload + "\n"
        st = emit(s)
        para_marks.append((st, st + len(s), {"h1": "HEADING_1", "h2": "HEADING_2", "h3": "HEADING_3"}[kind], s))
    elif kind == "p":
        s = payload + "\n"
        st = emit(s)
        para_marks.append((st, st + len(s), "NORMAL", s))
    elif kind in ("bullets", "numbers"):
        first = pos
        for it in payload:
            s = it + "\n"
            emit(s)
        para_marks.append((first, pos, "BULLET" if kind == "bullets" else "NUMBER", None))
    elif kind == "callout":
        s = payload + "\n"
        st = emit(s)
        para_marks.append((st, st + len(s), "CALLOUT", s))
    elif kind == "table":
        s = "@@TBL@@\n"
        st = emit(s)
        table_marks.append((st, st + len(s), payload))

full = "".join(text_parts)
docs.documents().batchUpdate(documentId=doc_id, body={"requests": [
    {"insertText": {"location": {"index": 1}, "text": full}}]}).execute()

# ---------------- formatting ----------------
reqs = []
for start, end, style, raw in para_marks:
    if style == "NORMAL":
        continue
    if style in ("HEADING_1", "HEADING_2", "HEADING_3"):
        reqs.append({"updateParagraphStyle": {
            "paragraphStyle": {"namedStyleType": style},
            "range": {"startIndex": start, "endIndex": end},
            "fields": "namedStyleType"}})
    elif style in ("BULLET", "NUMBER"):
        reqs.append({"createParagraphBullets": {
            "range": {"startIndex": start, "endIndex": end},
            "bulletPreset": "BULLET_DISC_CIRCLE_SQUARE" if style == "BULLET" else "NUMBERED_DECIMAL_NESTED"}})
    elif style == "CALLOUT":
        reqs.append({"updateParagraphStyle": {
            "paragraphStyle": {"shading": {"backgroundColor": {"color": {"rgbColor": {
                "red": 0.92, "green": 0.96, "blue": 0.85}}}}},
            "range": {"startIndex": start, "endIndex": end},
            "fields": "shading"}})

# bold: **...** inside normal paragraphs, and the text before a colon in bullets
bold_ranges = []
for start, end, style, raw in para_marks:
    if raw is None:
        continue
    for m in re.finditer(r"\*\*(.+?)\*\*", raw):
        pre = raw[:m.start()].count("**")
        bs = start + m.start() - pre * 2
        bold_ranges.append((bs, bs + len(m.group(1))))

for bs, be in bold_ranges:
    reqs.append({"updateTextStyle": {"textStyle": {"bold": True},
                 "range": {"startIndex": bs, "endIndex": be}, "fields": "bold"}})

for i in range(0, len(reqs), 200):
    docs.documents().batchUpdate(documentId=doc_id, body={"requests": reqs[i:i+200]}).execute()

# ---------------- tables ----------------
for start, end, rows in sorted(table_marks, key=lambda t: -t[0]):
    docs.documents().batchUpdate(documentId=doc_id, body={"requests": [
        {"deleteContentRange": {"range": {"startIndex": start, "endIndex": end}}},
        {"insertTable": {"location": {"index": start}, "rows": len(rows), "columns": len(rows[0])}}]}).execute()

doc = docs.documents().get(documentId=doc_id).execute()
tables_struct = [el for el in doc["body"]["content"] if "table" in el]
cell_data = []
for tbl_el, rows in zip(tables_struct, [t[2] for t in table_marks]):
    for ri, row in enumerate(tbl_el["table"].get("tableRows", [])):
        for ci, cell in enumerate(row.get("tableCells", [])):
            content = cell.get("content", [])
            si = content[0].get("startIndex", 0) if content else 0
            val = rows[ri][ci] if ri < len(rows) and ci < len(rows[ri]) else ""
            cell_data.append((si, val))

cell_data.sort(key=lambda x: x[0], reverse=True)
creqs = [{"insertText": {"location": {"index": si}, "text": val}} for si, val in cell_data if val]
for i in range(0, len(creqs), 200):
    docs.documents().batchUpdate(documentId=doc_id, body={"requests": creqs[i:i+200]}).execute()

# style header rows of every table + bold header text
doc = docs.documents().get(documentId=doc_id).execute()
tables_struct = [el for el in doc["body"]["content"] if "table" in el]
sreqs = []
for tbl_el, rows in zip(tables_struct, [t[2] for t in table_marks]):
    tstart = tbl_el["startIndex"]
    for ci in range(len(rows[0])):
        sreqs.append({"updateTableCellStyle": {
            "tableCellStyle": {"backgroundColor": {"color": {"rgbColor": {
                "red": 0.85, "green": 0.91, "blue": 0.97}}}},
            "tableRange": {"tableCellLocation": {
                "tableStartLocation": {"index": tstart}, "rowIndex": 0, "columnIndex": ci},
                "rowSpan": 1, "columnSpan": 1},
            "fields": "backgroundColor"}})
    for row in tbl_el["table"].get("tableRows", [])[:1]:
        for cell in row.get("tableCells", []):
            c = cell.get("content", [])
            if c:
                si = c[0].get("startIndex", 0)
                ei = c[0].get("endIndex", si)
                if ei > si + 1:
                    sreqs.append({"updateTextStyle": {"textStyle": {"bold": True},
                                  "range": {"startIndex": si, "endIndex": ei - 1}, "fields": "bold"}})
for i in range(0, len(sreqs), 200):
    docs.documents().batchUpdate(documentId=doc_id, body={"requests": sreqs[i:i+200]}).execute()

# ---------------- folder + share ----------------
folder = drive.files().create(body={
    "name": "Odologic", "mimeType": "application/vnd.google-apps.folder"}, fields="id").execute()
drive.files().update(fileId=doc_id, addParents=folder["id"], removeParents="root", fields="id,parents").execute()
drive.permissions().create(fileId=doc_id, body={"type": "anyone", "role": "reader"}, fields="id").execute()

meta = drive.files().get(fileId=doc_id, fields="id,name,webViewLink,parents").execute()
print(json.dumps({"doc_id": doc_id, "url": meta.get("webViewLink"), "folder_id": folder["id"],
                  "tables": len(tables_struct), "chars": len(full)}, indent=2))
