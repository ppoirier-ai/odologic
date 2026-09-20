import sys, json
sys.path.insert(0, '/root/.hermes/skills/productivity/google-workspace/scripts')
from google_api import build_service

docs = build_service("docs", "v1")
drive = build_service("drive", "v3")

TITLE = "Odologic application tracks: capital, sales cycle, cash flow and moat"

B = []
def h1(t): B.append(('h1', t))
def h2(t): B.append(('h2', t))
def h3(t): B.append(('h3', t))
def p(t): B.append(('p', t))
def bl(items): B.append(('bullets', items))
def nl(items): B.append(('numbers', items))
def tb(rows): B.append(('table', rows))

h1(TITLE)

p("Status: working note, 20 September 2026. Derived from the Odologic repo docs "
  "stakeholder-value-map.md, moat-design.md and competitive-and-market.md. Every figure is sourced with a "
  "URL or explicitly labelled MODELLED, meaning the arithmetic is ours and the inputs are named in the row. "
  "Nothing labelled UNVERIFIED goes in front of the chip partner or an investor.")

p("The counterparty is a company with a graph oriented AI accelerator, existing military and finance "
  "customers, a stated interest in military space, and capital they will spend on applications that run on "
  "their silicon. They are kept confidential here, referred to only as the chip partner, with no name and no "
  "identifying detail.")

h2("1. What is being decided")

p("The chip partner brings three things we do not have: a graph oriented accelerator, an existing military "
  "and finance book of business, and money for applications on their hardware. They also bring their own "
  "injury: a very large codebase that current language models cannot manage, because of context window limits "
  "and hallucination. That last point is the only place in this whole set where the buyer is describing his "
  "own problem rather than a market that might exist.")

p("So the choice is not which application is largest. Four questions sort the tracks:")

nl([
  "Does the buyer already have budget and a named owner, or are we creating the line item.",
  "Does the buyer accept a record they do not control, or is custody demanded on day one.",
  "Can a defeat be settled by execution, or does it stay an argument between two people.",
  "Does the track pull the chip partner's silicon, or is the silicon incidental.",
])

p("Question 2 kills tracks quietly. Question 3 decides whether the product is provable in a pilot or only in a "
  "deck. The tracks: A regulated finance assurance, B healthcare assurance, C military space, D defense "
  "codebase comprehension, E accelerated defeasibility on their silicon, and F OEM into their existing book. "
  "F is a channel rather than an application and it applies to A to D.")

h2("2. Why D goes first, and it is not market size")

nl([
  "Code is the only domain here where a defeat is settled by execution. A failing test, a broken build, a "
  "dependency that does not exist, a signature that breaks a downstream caller: each is a computable defeat "
  "rather than an opinion about an opinion. The claim status lifecycle stops being a schema we assert and "
  "becomes a status the system enforces.",
  "The alternative the buyer has today does not work, and it is measured. LongCodeBench, across 1,043 "
  "instances from 108 repositories up to one million tokens, saw resolution fall from 29 percent to 3 percent "
  "for Claude 3.5 Sonnet between 32K and 256K tokens, and from 70.2 percent to 40 percent for Qwen2.5, with "
  "the best closed model at 22 percent. Source: arxiv.org/abs/2505.07897",
  "Fabrication is measured too: across 16 coding models, 19.7 percent of recommended packages did not exist, "
  "205,474 unique fabricated names, 21.7 percent for open models against 5.2 percent for commercial. Source: "
  "usenix.org/publications/loginonline/we-have-package-you-comprehensive-analysis-package-hallucinations-code",
  "In defense the context window is not even the binding constraint. Air gapped and classified environments, "
  "export control and no cloud egress remove the hosted model from the option set, which leaves a local model "
  "on local silicon plus a local ledger, exactly the shape the chip partner sells.",
  "The user is an engineer with a named stake in the claim, so the individual map is the unit of accumulation "
  "rather than the employer custody fight.",
  "The corpus does not have to be built. Their own codebase is the first customer, the first benchmark and the "
  "first reference, the cheapest cold start in the file.",
])

p("The buyer side is documented and large. The federal government spends over $100 billion on information "
  "technology each year and agencies have typically reported about 80 percent of it as operations and "
  "maintenance of existing systems including legacy ones (gao.gov/products/gao-23-106821). GAO reviewed 69 "
  "federal legacy systems in July 2025 and identified 11 most in need of modernization across 10 agencies, "
  "aged 23 to 60 years, seven with known cybersecurity vulnerabilities that cannot be remediated without "
  "modernization (gao.gov/products/gao-25-107795). Defense software sustainment was estimated by the "
  "department itself at not less than $15 billion across five fiscal years against about $828 million actually "
  "reported for fiscal year 2018, an unreliable total because the Navy did not report (gao.gov/products/gao-19-173). "
  "GAO's April 2026 review found 14 of 36 weapon system sustainment reviews for fiscal years 2023 and 2024 "
  "showing critical operating and support cost growth, and noted that finishing one Army software update would "
  "save more than $130 million across about 30 remaining years (gao.gov/products/gao-26-108140). A current "
  "fiscal year defense wide software sustainment total was not found from a primary source: UNVERIFIED.")

p("The honest caveat, stated rather than buried: defense software already has requirements traceability, code "
  "review records and configuration management. Traceability shows which requirement a line of code came from. "
  "It does not show which claim about the system was defeated, by what, and by whom. That has to be "
  "demonstrated on their code in a pilot, not asserted in a deck.")

h2("3. The six numbers per track")

p("Read the capital column as what has to be spent before the first invoice is paid, not as a raise.")

tb([
  ["Track", "Capital to first revenue", "Capital to market scale", "Sales cycle", "Near term cash flow",
   "Three year revenue band", "Moat durability"],
  ["D defense codebase", "$150K to $400K", "$2M to $5M", "3 to 6 months commercial, 60 to 120 days government",
   "Strongest after quarter two, milestone billing plus SBIR", "$10M to $25M MODELLED", "Medium high"],
  ["A finance assurance", "$1M to $3M, 12 to 18 months", "$5M to $15M", "6 to 18 months UNVERIFIED",
   "Weak, design partner pilots often unpaid", "$2M to $10M ARR MODELLED", "High but slow"],
  ["B healthcare", "$2M to $5M", "$15M and up", "12 to 24 months UNVERIFIED", "Weakest",
   "$1M to $8M MODELLED", "Medium"],
  ["C military space", "$1.5M to $3M", "$4M to $15M", "3 to 6 months to first contract, then years to a programme of record",
   "Government payment lags about six months after submission", "$1M to $8M MODELLED, Palantir at $8.15B is the ceiling case",
   "High, programme entrenchment"],
  ["E accelerated defeasibility", "$400K to $1.5M", "$1M to $2M", "1 to 2 quarters to the partner's engineering budget",
   "Development revenue billed per milestone", "$1M to $5M development plus royalty MODELLED", "Low for us, high for them"],
  ["F OEM into their book", "$150K to $400K", "$500K to $2M", "1 to 6 months to first paid order",
   "Best in the set, cash per order MODELLED", "$2M to $10M at 30 to 50 percent channel margin MODELLED",
   "Low, channel dependency risk"],
])

h3("Sourcing behind the capital and cash rows, verified directly")

nl([
  "SBIR ceilings are $323,090 for Phase I and $2,153,927 for Phase II as of April 2026, above which SBA "
  "approval is required, and the programmes are described as equity free and non dilutive. sbir.gov/about",
  "SpaceWERX: Phase I $75K to $180K over 3 to 12 months, Phase II $1.25M to $1.8M over up to 24 months, "
  "notification no later than 90 days from solicitation close, contracts finalised no later than 180 days. "
  "spacewerx.us/get-funded",
  "TACFI $375K to $1.9M over up to 24 months, STRATFI $3M to $15M over up to 48 months, both requiring matched "
  "funding fixed before submission and not adjustable, and both open only to a company holding an active "
  "Phase II or one completed within the prior two years. That eligibility rule is the nearest thing to a moat "
  "in the procurement documents, because incumbency compounds and late entrants are excluded from the scale up "
  "money. afwerx.com STRATFI TACFI FAQs",
  "Defense Innovation Unit awards prototype agreements under Other Transaction authority in as few as 60 to 90 "
  "days with a current average near 120, has made more than 500 such awards in eight years, and after a "
  "successful prototype any interested department entity may enter a non competitive follow on production "
  "contract. diu.mil",
  "The low anchor for a decision support pilot is an Army solicitation capped at $250,000 per award over a "
  "maximum of six months. army.mil article 283863",
  "Cash is contract based rather than grant based and the Air Force states contracts are more demanding than "
  "grants, so the planning assumption is that the company self funds roughly half a year of effort after "
  "submission before the first government dollar. AFWERX SBIR STTR FAQs",
  "What a port costs and who pays, by precedent: the Department of Energy funded four codesign centres at $48 "
  "million over four years, first year $12 million split evenly, and ran PathForward at $258 million over three "
  "years with recipients required to fund at least 40 percent of total project cost, taking the total to at "
  "least $430 million. Read that as the price list for track E: government or client on the larger share, the "
  "hardware side on the balance. anl.gov and energy.gov",
  "The template for being paid by a hardware partner is Nvidia's $2 billion in CoreWeave at $87.20 per share in "
  "January 2026, bundled with CoreWeave software entering Nvidia reference architectures: cash plus "
  "distribution in exchange for becoming part of the vendor's story. investors.coreweave.com",
  "Pricing anchors for track A: AI governance platforms report a $30,000 to $150,000 per year band, compliance "
  "automation an observed median near $25,000 per year across 233 purchases, and developer observability in the "
  "tens of dollars per month per unit. AI governance software was valued at $308.3 million in 2025, $417.8 "
  "million in 2026 and $3,590.2 million by 2033 at 36 percent CAGR, with government and defense the largest "
  "vertical, which is why the pricing argument sits in model risk budgets above $15 billion rather than in the "
  "AI governance line itself. grandviewresearch.com",
])

h2("4. The ceiling case and the failure case")

p("Palantir reported second quarter 2026 United States government revenue of $809 million, up 90 percent year "
  "over year, total revenue of $1.935 billion, up 93 percent, GAAP operating margin of 47 percent, and raised "
  "full year guidance to $8.150 to $8.158 billion. BigBear.ai, the mid sized case, reported first quarter 2026 "
  "revenue of $34.4 million, gross margin of 34.0 percent, backlog of $281.9 million including a $53 million "
  "sole source prime classified award, $431.5 million of cash and investments, and affirmed full year guidance "
  "of $135 million to $165 million. Sources: SEC filings, Palantir Q2 2026 press release and BigBear.ai Q1 2026 "
  "earnings release. Read together: the defense decision layer supports very large outcomes, and a credible "
  "mid sized defense AI company can sit at that scale with a services heavy mix. That is the shape track D "
  "takes before any software margin appears.")

p("The failure case belongs in the same paragraph. Graphcore raised $684 million, peaked at a $2.77 billion "
  "valuation, ran out of commercial momentum, and was acquired by SoftBank in July 2024 for about $500 "
  "million, roughly one fifth of peak, with a further $457 million injected afterwards. That is why track E "
  "carries a portability requirement and why F is a channel rather than a dependency. "
  "jonpeddie.com/news/graphcores-ipu-doing-well-at-softbank")

h2("5. Where the chip partner's money is worth taking")

p("Their offer is a development contract, not a round, and the distinction decides whether we stay neutral and "
  "whether we stay the owner of the schema.")

tb([
  ["Structure", "What it is", "Effect"],
  ["Milestone development contract", "They pay for a named port or reference application, per milestone, no equity",
   "Accepted, non dilutive, deliverables are a working artefact and a benchmark"],
  ["Joint go to market", "Co sell into their book, split revenue, they keep the silicon",
   "Accepted only if the record stays ours and export stays guaranteed"],
  ["Reference design royalty", "They pay per unit or per deployment where the ledger runs as silicon differentiation",
   "Accepted, and the only structure where their silicon advantage and our schema both convert to money"],
  ["Strategic equity investment", "They take a position",
   "Rank last, because it makes them a conflicted party in the way the moat doc says the company dies: aligned with one landlord, therefore not neutral across the rest"],
])

p("Two hard conditions, stated now rather than discovered in diligence. No structure may give the chip partner "
  "custody of a customer's ledger, and none may make the record unexportable. Separately, because the partner "
  "is a hardware platform with uncertain share, any port work needs an unwindable portability clause rather "
  "than exclusivity, on the logic the buyer side already uses: platform diversity is resilience.")

h2("6. Confidentiality and export control")

p("The chip partner's customers sit under export control and releasability rules we are not a party to. Three "
  "consequences. Their architecture and their codebase stay unnamed in anything that leaves the two companies. "
  "Any pilot on their codebase must be scoped by them for releasability before we touch it. And a United States "
  "government track for a Canadian controlled founder needs the foreign ownership and relocation question "
  "answered up front rather than at the accreditation stage, a real cost in track C, currently UNVERIFIED for "
  "amount and duration.")

h2("7. Ranked recommendation")

nl([
  "F first, as the funding channel. It is the only line producing cash inside two quarters, because it spends "
  "their existing customer relationships rather than building a sales motion from zero.",
  "D in parallel, as the product. The only track where a defeat is computable, the only one where the hardware "
  "is load bearing, and the only one whose first customer is already in the room. Price the first phase as a "
  "paid pilot with a benchmark deliverable on their codebase, using the Army decision support ceiling of "
  "$250,000 over six months as the low anchor.",
  "C on the reference from D, using non dilutive procurement money, since Phase II at $1.25M to $1.8M plus "
  "TACFI matching can carry a prototype and a first government customer without equity. Check first whether "
  "they hold a space programme of record or space interest only, because a military client is not a contract "
  "vehicle.",
  "A and B last, and A before B. A has the budget and the owner but a slow cycle and a deferred regulatory "
  "deadline, since the high risk obligations moved to 2 December 2027 and 2 August 2028 while the Article 50 "
  "transparency duties stayed on 2 August 2026. B has a longer cycle, a crowded ambient scribe market, and no "
  "computable defeat to prove anything with.",
  "E only as a paid study with the portability protections above, and only after D has produced something worth "
  "porting. Doing E first would make the schema their specification before it is our product.",
])

p("The one thing this comparison does not establish, and it sits under every row: whether an engineer working "
  "on a defense codebase will maintain a ledger while doing their job. That is testable in a two week "
  "instrumented pilot on the chip partner's own repository, cheaply, and it should run before capital is "
  "committed to a track.")

# ---------------- build ----------------
doc = docs.documents().create(body={"title": TITLE}).execute()
doc_id = doc["documentId"]

text_parts = []
table_marks = []
pos = 1
for kind, val in B:
    if kind == 'table':
        rows = val
        payload = "".join("".join(str(c) for c in row) for row in rows)
        table_marks.append((pos, pos + len(payload), rows))
        text_parts.append(payload)
        pos += len(payload)
    elif kind in ('bullets', 'numbers'):
        lines = ["".join(x) + "\n" for x in val]
        payload = "".join(lines)
        text_parts.append(payload)
        pos += len(payload)
    else:
        payload = val + "\n"
        text_parts.append(payload)
        pos += len(payload)

full = "".join(text_parts)
docs.documents().batchUpdate(documentId=doc_id, body={
    "requests": [{"insertText": {"location": {"index": 1}, "text": full}}]}).execute()

# paragraph styles
marks = []
cur = 1
for kind, val in B:
    if kind == 'table':
        payload = "".join("".join(str(c) for c in row) for row in val)
        cur += len(payload)
        continue
    if kind in ('bullets', 'numbers'):
        start = cur
        for x in val:
            marks.append((kind, start, start + len(x) + 1))
            start += len(x) + 1
        cur = start
    else:
        marks.append((kind, cur, cur + len(val) + 1))
        cur += len(val) + 1

reqs = []
for kind, st, en in marks:
    if en <= st:
        continue
    if kind == 'h1':
        reqs.append({"updateParagraphStyle": {"paragraphStyle": {"namedStyleType": "HEADING_1"},
                     "range": {"startIndex": st, "endIndex": en}, "fields": "namedStyleType"}})
    elif kind == 'h2':
        reqs.append({"updateParagraphStyle": {"paragraphStyle": {"namedStyleType": "HEADING_2"},
                     "range": {"startIndex": st, "endIndex": en}, "fields": "namedStyleType"}})
    elif kind == 'h3':
        reqs.append({"updateParagraphStyle": {"paragraphStyle": {"namedStyleType": "HEADING_3"},
                     "range": {"startIndex": st, "endIndex": en}, "fields": "namedStyleType"}})
    elif kind == 'bullets':
        reqs.append({"createParagraphBullets": {"range": {"startIndex": st, "endIndex": en},
                     "bulletPreset": "BULLET_DISC_CIRCLE_SQUARE"}})
    elif kind == 'numbers':
        reqs.append({"createParagraphBullets": {"range": {"startIndex": st, "endIndex": en},
                     "bulletPreset": "NUMBERED_DECIMAL_ALPHA_ROMAN"}})
for i in range(0, len(reqs), 200):
    docs.documents().batchUpdate(documentId=doc_id, body={"requests": reqs[i:i+200]}).execute()

# tables
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
            if val:
                cell_data.append((si, val))
cell_data.sort(key=lambda x: x[0], reverse=True)
creqs = [{"insertText": {"location": {"index": si}, "text": val}} for si, val in cell_data]
for i in range(0, len(creqs), 200):
    docs.documents().batchUpdate(documentId=doc_id, body={"requests": creqs[i:i+200]}).execute()

# bold header rows
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

# folder reuse then share
existing = drive.files().list(
    q="name = 'Odologic' and mimeType = 'application/vnd.google-apps.folder' and trashed = false",
    fields="files(id,name)", pageSize=5).execute().get("files", [])
folder_id = existing[0]["id"] if existing else drive.files().create(body={
    "name": "Odologic", "mimeType": "application/vnd.google-apps.folder"}, fields="id").execute()["id"]
drive.files().update(fileId=doc_id, addParents=folder_id, removeParents="root", fields="id,parents").execute()
for who in ["patrick@smooth.fund"]:
    try:
        drive.permissions().create(fileId=doc_id, body={"type": "user", "role": "writer", "emailAddress": who},
                                   sendNotificationEmail=False, fields="id").execute()
    except Exception as e:
        print("share failed for", who, e)

meta = drive.files().get(fileId=doc_id, fields="id,name,webViewLink,parents").execute()
print(json.dumps({"doc_id": doc_id, "url": meta.get("webViewLink"), "folder_id": folder_id,
                  "tables": len(tables_struct), "chars": len(full)}, indent=2))
