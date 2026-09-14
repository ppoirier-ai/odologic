import sys, json
sys.path.insert(0, '/root/.hermes/skills/productivity/google-workspace/scripts')
from google_api import build_service

DOC = "1WxMrB-dygKsnuQTIEK9LQIQ_R0i4aoWKvurSMxJW39I"
docs = build_service("docs", "v1")

SEC = [
    ("h2", "10. Correction: the token economy, revised"),
    ("p", "The verdict in section 3 was too blunt. The negative loop is a design outcome rather than a law: it is produced by the choice to reward holding with price. Change that and the loop changes."),
    ("b", "Non transferable stake, so there is nothing to cash out and the plateau stops being an event."),
    ("b", "Pay for verified contribution rather than appreciation, so income does not depend on the price chart and the quality gate cannot be bought."),
    ("b", "Refund membership bonds at par, denominated in the unit of work, which removes the upside to speculate on and the downside to panic about in the same stroke."),
    ("b", "Denominate rewards as service claims, so value tracks usefulness rather than adoption sentiment."),
    ("b", "Cap governance weight per domain and by calibration, so a whale cannot buy the neutrality the position rests on."),
    ("b", "Fund rewards and buybacks from revenue, never from emissions."),
    ("p", "The trade that has to be named: every one of those fixes removes speculative upside, and speculative upside is the only reason a token bootstraps faster than an ordinary product. So the honest claim is that you can have the negative loop removed or the speculative bootstrap, not both."),
    ("c", "The version that does work is not a financial network effect at all. The token is the access right to a scarce, quality gated resource, meaning the entitlement to contribute in a domain or to consume the aggregate. The network effect is coordination and licensing rather than price, membership is earned rather than bought, and supply cannot be inflated."),
    ("p", "The real blocker is distribution, and it is not a design problem. The circle is that the price needs buyers, buyers need the network, the network needs contributors, and contributors need a reason to show up. Without distribution you pay for attention with emissions, which buys mercenary supply that leaves when emissions slow. That is the negative loop arriving early instead of late."),
    ("n", "Distribution first, ideally somebody else's, since an MCP surface inside harnesses people already use needs no token at all."),
    ("n", "Then tokenize the contribution layer where users already exist, because a token amplifies a network and cannot substitute for one."),
    ("n", "Token last, only for the collective map, where the scarce entitlement actually exists. Never for access to the individual ledger, which stays a plain subscription."),
    ("p", "What this changes in the pitch: drop the claim that a token creates the moat. Keep two narrower claims that survive scrutiny, that a non transferable earned entitlement is a rights ledger and therefore an institutional asset, and that the collective map's scarce resource is permission to contribute rather than volume of content."),
]

# build text
parts, marks, pos = [], [], 0
for kind, text in SEC:
    s = text + "\n"
    marks.append((pos, pos + len(s), kind))
    parts.append(s)
    pos += len(s)
full = "".join(parts)

doc = docs.documents().get(documentId=DOC).execute()
end = doc['body']['content'][-1]['endIndex'] - 1

docs.documents().batchUpdate(documentId=DOC, body={"requests": [
    {"insertText": {"location": {"index": end}, "text": full}}]}).execute()

reqs = []
for start, stop, kind in marks:
    a, b = end + start, end + stop
    if kind == "h2":
        reqs.append({"updateParagraphStyle": {"paragraphStyle": {"namedStyleType": "HEADING_2"},
                     "range": {"startIndex": a, "endIndex": b}, "fields": "namedStyleType"}})
    elif kind == "c":
        reqs.append({"updateParagraphStyle": {"paragraphStyle": {"shading": {"backgroundColor": {"color": {"rgbColor": {"red": 0.92, "green": 0.96, "blue": 0.85}}}}},
                     "range": {"startIndex": a, "endIndex": b}, "fields": "shading"}})
    elif kind in ("b", "n"):
        reqs.append({"createParagraphBullets": {"range": {"startIndex": a, "endIndex": b},
                     "bulletPreset": "BULLET_DISC_CIRCLE_SQUARE" if kind == "b" else "NUMBERED_DECIMAL_NESTED"}})

docs.documents().batchUpdate(documentId=DOC, body={"requests": reqs}).execute()
print(json.dumps({"appended_chars": len(full), "requests": len(reqs), "at_index": end}))
