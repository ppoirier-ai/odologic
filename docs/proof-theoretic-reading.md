# Proof-theoretic reading of Odologic

Each classical proof method, mapped to its Odologic counterpart. Keep these in mind
when tracing hypotheses and statements: every trace in the ledger is one of these
patterns, and knowing which one tells you what to check.

| Proof method | Odologic mechanism | Status |
|---|---|---|
| Direct proof | depends_on trace to the floor | implemented (core design) |
| Proof by contradiction (reductio) | REBUT defeat: claim and standing floor theorem cannot both hold | implemented (teleport example, D2) |
| Proof by construction | measurement Certificate: replayable protocol, re-derive the claim yourself | implemented (CoA in label example) |
| Proof by induction | the closer's cascade: status change propagates along depends_on edges, semi-naive fixed point | implemented (closer semantics) |
| Proof by counterexample | defeats as hard negatives in training | implemented |
| Proof by contraposition | mint the contrapositive pattern when a defeat lands: "for any claim of this type, the floor excludes it" | latent, design opportunity |
| Proof by exhaustion (cases) | explicit case sets: every image, every dataset version, every sub-claim checked | latent, needed for fraud triage |
| Conditional/auxiliary proof | rival hypothetical worldsheets: promote an assumption, draw consequences, compare with the observed world | open question, candidate semantics for `contested` |

## Guidance for tracing

When a hypothesis or statement enters the ledger, ask which proof shape the trace is:

- If it should hold by derivation from knowns → direct trace; build depends_on edges.
- If it is asserted against a standing claim → expect a reductio shape; look for the
  floor theorem it contradicts, not just missing evidence.
- If it is empirical → construction; require a replayable measurement certificate.
- If its fate depends on another claim resolving → cascade/induction shape; the closer
  re-fires, humans watch the delta.
- If it is universal ("all X are Y") → one counterexample suffices; record it as a
  defeat and queue the hard negative.
- If it is multi-part → exhaustion shape; enumerate the case set explicitly and track
  which cases are checked.
- If it is genuinely in dispute → consider rival worldsheets (auxiliary proof) rather
  than a single contested flag.
