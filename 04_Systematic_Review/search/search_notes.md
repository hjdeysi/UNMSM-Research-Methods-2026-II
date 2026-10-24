# Search notes — Deliverable 04

Database: Semantic Scholar Academic Graph API, endpoint `/paper/search/bulk` (matches title + abstract).
Filter: `year=2023-2026`. No publication-type filter (metadata incomplete; non-peer-reviewed records are excluded at screening with a reason code).
Script: `run_search.py`. Every execution is logged in `search_log.tsv` and saved raw in `results/`.

## Iterations (known-item testing against verified seed studies)

| Version | UTC | Records | Seeds retrieved | Decision |
|---|---|---|---|---|
| v1-A interventions | 2026-10-24 15:25 | 910 | Kumar only (1/3 intervention seeds) | Rejected |
| v1-B dependence/integrity | 2026-10-24 15:25 | 1,700 | Morales-García, Chen (2/4 measurement seeds) | Rejected |
| v3-C final | 2026-10-24 15:30 | 614 | Lee, Kumar, Bereznikova (3/3 intervention seeds) | Adopted |

Diagnosis of v1: some prefix wildcards fail silently in the bulk endpoint (e.g. `randomi*` did not match "randomized", while `random*` and the plain word did), and the design block excluded seeds that describe their design without the word "experiment". v3 uses plain words, which the engine matches across inflections (university/universities), and both spellings where needed.

## Final string (v3)
```
+("higher education" | university | universities | undergraduate | undergraduates | college)
+("generative AI" | GenAI | "generative artificial intelligence" | ChatGPT | "large language model" | "large language models" | LLM | LLMs | chatbot | chatbots | "conversational agent" | "conversational agents" | "conversational AI")
+(Socratic | scaffolding | scaffold | "self-reflection" | reflection | metacognitive | metacognition | guidance | hints)
+("critical thinking" | "self-regulated learning" | reflection | dependence | dependency | "over-reliance" | overreliance | "academic integrity" | metacognitive)
+(randomized | randomised | "controlled trial" | "quasi-experimental" | "quasi-experiment" | experiment | experimental | "control group" | "within-domain" | conditions | compares)
```
Not retrieved by v3: Zhou, Liu & Chiu (2026) — to be reported under "identification via other methods" if included.
