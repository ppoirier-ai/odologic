## Variant: Click-through walkthrough (canonical demo)

### Design stance
The narrative demo. Every screen is a real step a user would take, with the two usage modes
side by side from the home screen: interacting with an LLM agent, and checking a plain
document with no AI in the loop.

### The two walkthroughs

Walkthrough 1 (with an LLM):
1. s-chat1: you ask your agent "Can a person get from Tokyo to New York in five minutes?"
2. s-chat2: the agent answers with a teleport claim, red-underlined by the check
3. s-chat3: click the flagged claim to see the full trace to the floor, both defeats
4. s-chat4: interstitial: the defeat is written to the ledger permanently
5. s-chat5: the corrected answer, physics cited, claim gone
6. s-learn: what the ledger now holds: hard negatives and source reputation 2/1

Walkthrough 2 (plain document, no AI):
1. s-doc1: paste an Omega-3 supplement label
2. s-doc2: the verdict banner, six claims with statuses
3. s-doc3: a claim that holds (trace to CoA measurement)
4. s-doc4: why marketing becomes a labeled assumption, not a defeat
5. s-doc5: the FDA defeat of "supports heart health", with the floor it should have met
6. s-learn2: actions: export grounded set, notify compliance, queue hard negative

### Implementation notes
Single self-contained HTML file, screens toggled by go(id). index_shot.html is a
screenshot harness variant (accepts ?screen=) and is not part of the demo.
