## Variant: Workbook (single-question flow)

### Design stance
Editorial, light, content-first. One question: "does this text hold?" The user pastes
anything (LLM answer or plain document), gets a verdict banner, then claim-by-claim
results with why-this expan­ders. The product tells one story end to end.

### Key choices
- Layout: single column, stepped (paste, verdict, actions), generous whitespace
- Typography: system sans, large lede, warm paper background
- Color: paper tones; status colors only on chips and trace lines
- Interaction: two example loaders, Trace it button, smooth scroll to results,
  why? expander per claim (state transition)

### Trade-offs
- Strong at: first five minutes comprehension, marketing demo, non technical users
- Weak at: audit throughput, no filtering, no ledger visibility; hides the machinery

### Best for
The demo, the landing flow, and any user with one document and one question.
This is the buyer's view.
