# Learning graphs

A learning graph is a directed acyclic graph (DAG) of concepts. An edge `A -> B` means **learn A before B**. Teaching order is a topological sort. The critical path is the longest chain.

Do not build a 400-node textbook graph for a 12-page PDF. Scale to the source.

| Source size | Target nodes |
| lesson / one chapter / one site task | 8–40 |
| multi-chapter book or course | 40–120 |
| full intelligent textbook | 200–600, only if the user asked for a textbook |

## Node

```
id: c12
label: Export button   # short, Title Case, <= 40 chars
kind: term | procedure | principle | ui | theorem
bloom: remember | understand | apply | analyze | evaluate | create
evidence: p.14 | https://...#export | shot-03.png
prereq: [c3, c7]
status: unknown | known | shaky | mastered
modality: text | image | audio | video | ui | mixed
```

`status` is learner state, not source state. Update it from checks.

## Edge types (keep two in the teaching graph)

- `requires` — cannot teach B without A (hard prereq)
- `helps` — useful but skippable (soft). Soft edges do not block topo order

Do not add `similar_to` or `conflicts_with` into the teaching DAG. Park those in NOTES.

## Extraction rules

1. A concept is a thing the learner can fail independently. "The Stripe dashboard" is too big. "API key vs publishable key" is a concept.
2. Every node cites evidence in the source pack. No evidence → `UNGROUNDED` and either drop it or mark it.
3. Foundational nodes have empty `prereq`.
4. Every non-root has at least one `requires` edge.
5. No self-edges. No cycles. If a cycle appears, the labels are wrong — split the node (definition vs use).
6. Prefer fewer, sharper nodes over a glossary dump.

## Files in the lesson pack

- `CONCEPTS.md` — human table
- `concepts.json` — machine graph (nodes + requires + helps)
- `learning-graph.csv` — `id,label,requires,helps,bloom,evidence,status`
- `GRAPH.md` — Mermaid flowchart plus roots, sinks, critical path

Generate and validate with:

```
python scripts/graph_tools.py /home/workdir/artifacts/lessons/<slug>
```

The script refuses to write GRAPH.md if it finds a cycle. Fix the edges, rerun.

## How the graph drives teaching

- Diagnose against roots first, then walk the critical path
- A failed check marks that node `shaky` and blocks dependents until retaught
- PLAN.md units are connected components or path slices, not chapter titles copied blindly
- If the source order fights the DAG, teach DAG order and note the reshuffle in OUTLINE.md

## Quality bar

- Acyclic
- At least one root and one sink
- Isolated nodes allowed only if they are true side quests, listed under out-of-scope or optional
- Labels unique
- Bloom level set
- Evidence set
