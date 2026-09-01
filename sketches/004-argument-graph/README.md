## Variant: Argument graph (visual trace)

### Design stance
The trace as a navigable graph, not a list. Nodes are claims, terms, certificates, and
defeats; edges are the logic relations between them. Click a node to focus its
neighborhood and open the detail panel.

### Key mechanics
- Click a judgment node: side panel opens with four sections:
  1. Corroborating — certificates and facts that support it
  2. Disproving — defeats, with their type (rebut / undercut / undermine)
  3. Balance of argument — a for/against bar with the verdict on this balance
  4. Must be true for this to stand (downward dependencies) and
     Follows if this is true (what it grounds)
- Focus mode: clicking dims everything outside the node's one-hop neighborhood
- Each judgment node carries a miniature for/against balance bar on its face
- The kernel sits outside the graph, connected only by its audit relation

### Philosophy anchors (documented for later use in docs)
- Toulmin model: claim / grounds / warrant / backing / rebuttal / qualifier —
  maps to Judgment / Certificate / floor rule / axiom / Defeat / status. The Toulmin
  "warrant" is exactly our floor rule: the inference license linking evidence to claim.
- Dung argumentation frameworks (1995): directed graphs where nodes are arguments and
  edges are attacks; defeat by attack, reinstatement when the attacker is itself
  defeated. Our Defeat/rebut/undercut typology and "defeated vs standing" statuses are
  a typed refinement of Dung semantics.
- Formal proof theory (mathematical "Analysis"): what we call the trace to floor is a
  proof skeleton — antecedents (depends_on), inference rules (floor rules), and
  lemmas (theorems). The graph view is the natural deduction tree plus its negations.

### Layout (teleport worldsheet)
Three columns: judgments (J1 J2 J3 J4), terms (T2 T1) at left, certificates (C1 C2 C3)
third column, defeats (D1 D2) fourth column, kernel below the judgment column.

### Notes
Hand-positioned nodes; edges drawn as quadratic curves with anchors on node borders.
index_shot.html is the screenshot harness (?focus=J1), not part of the demo.
