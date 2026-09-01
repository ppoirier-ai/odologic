## Variant: Analyzer (operator console)

### Design stance
Dense, dark, tool-first operator console. The user is a professional auditor reviewing work the
system (or an LLM) already did: everything is laid out for scan, filter, and drilldown.

### Key choices
- Layout: three columns, source doc / judgment stack / ledger inspector
- Typography: system sans, mono for IDs and trace lines
- Color: dark console palette; status colors on chips and stats only
- Interaction: tab switch between LLM audit and document grounding; status filter chips;
  action buttons (flag hard negative, hold as assumption)

### Trade-offs
- Strong at: parallel evidence, professional credibility, scalable to hundreds of judgments
- Weak at: first-run comprehension. A cold user sees a wall of chrome before the story.

### Best for
Analysts, research fraud triage, and any workflow where the judgment ledger already
exists and someone audits it. This is the professional's view.

### Demonstrates
- LLM example: teleport claim audit (J1 defeated, undercut + rebut, floor theorems J3/J4)
- Pure doc example: Omega-3 label (L1..L6, assumption vs defeated distinction, FDA rebut)
- Ledger inspector: reputation decay, suggested actions, append-only event stream
