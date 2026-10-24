# Deliverable 04 — Review protocol (v1, frozen 2026-10-24 before screening)

**Design.** Rapid review following the Cochrane Rapid Reviews Methods Group guidance (Garritty et al., 2021, https://doi.org/10.1016/j.jclinepi.2020.10.007; Garritty et al., 2024, https://doi.org/10.1136/bmj-2023-076335): one human reviewer, AI-assisted first-pass screening, and a cap of 10 included studies set by the assignment. It is not a full systematic review. Reporting follows PRISMA 2020 (Page et al., 2021, https://doi.org/10.1136/bmj.n71).

## Review question
What comparative evidence exists on tools based on generative large language models that are designed to elicit higher-education students' own reasoning, and what effects do they report on reflection/metacognition, self-regulation, critical thinking, AI dependence, academic integrity and learning performance?

## Eligibility criteria (each with a mirror exclusion code)

| Code | Inclusion | Exclusion |
|---|---|---|
| I1 / E1 | ≥80 % of the sample in higher education (undergraduate or postgraduate), or results reported separately for that subgroup | Population not eligible |
| I2 / E2 | Tool based on a generative LLM (GPT-3 or later) | No generative LLM |
| I3 / E3 | Tool designed or configured to elicit the student's own reasoning (Socratic questions, graded hints, reflection or metacognitive prompts, withholding answers) | No scaffolding of the student's own reasoning |
| — / E4 | Primary empirical study | Review, conceptual paper or protocol |
| I5 / E5 | Randomised, quasi-experimental with a control group, or counterbalanced crossover | Single-group pre-post or no control |
| I4 / E6 | At least one outcome among: reflection/metacognition, self-regulation, critical thinking, AI dependence/over-reliance, academic integrity, learning performance measured by a test. Self-reported and objective measures accepted; type recorded at extraction | No outcome of interest |
| I6 / E7 | Peer-reviewed journal article or full conference paper | Poster, extended abstract, work-in-progress, preprint |
| — / E8 | Published 2022 to search date (2026-10-24) | Outside window |
| — / E9 | English or Spanish (declared as language bias) | Other language |
| — / E10 | — | Full text not available (full-text stage only) |
| — / E11 | — | Duplicate report of the same study; studies are counted, not articles (full-text stage only) |

Comparators are coded separately at extraction: **C1** scaffolded LLM vs unscaffolded LLM; **C2** scaffolded LLM vs non-AI condition.

## Screening rules
1. Each excluded record gets the **first criterion that clearly fails**, in the fixed order E1→E11. If an earlier criterion is uncertain and a later one clearly fails, the later code is assigned.
2. When in doubt at title/abstract, the record is marked UNSURE and goes to full text. Records without abstract (n = 20) go directly to full text.
3. I3 at title/abstract: passes or UNSURE only when the abstract describes the tool's function with scaffolding terms (Socratic, scaffold, hints, reflection/metacognitive prompts, not giving answers). "Guidance", "feedback" or "assistance" alone are coded E3.
4. Papers with no specific tool (theoretical or survey studies) fail at E3 by the fixed order; E4 therefore applies mainly to reviews, frameworks and protocols about scaffolding tools.
5. Records coded E4 whose topic meets I1–I3 are flagged SNOWBALL; their reference lists are screened with the same criteria and reported under "identification via other methods", together with Zhou, Liu & Chiu (2026).

## Procedure
1. **Blind pilot.** 50 records drawn at random (seed 20261024, excluding records without abstract) are screened independently by the author and by the AI. The AI decisions were frozen before the author's pilot; SHA-256 of the file: `8c0235bf905f444e0ae2b3397b383bc7eb573ee52aed90efd8c1319a336f4b66`. Report Cohen's kappa (3 categories and binary include+unsure vs exclude) and percentage agreement; criteria definitions are adjusted and re-frozen afterwards.
2. **First pass.** The AI screens the remaining records.
3. **Verification.** The author reviews all INCLUDE/UNSURE records and a random sample of EXCLUDE records, blind to the AI label.
4. **Reporting.** Pilot kappa and false-negative rate reported in the PRISMA diagram (records excluded by human vs by automation) and in the AI-use disclosure.

## Prioritisation if more than 10 studies are eligible (fixed before screening)
Randomised > quasi-experimental with control > counterbalanced crossover; then larger N; then more recent. Declared as a limitation.

## Seed test of the criteria
| Seed | I1 | I2 | I3 | I4 | I5 | I6 | Result |
|---|---|---|---|---|---|---|---|
| Lee et al. (2024) | ✓ undergraduates | ✓ ChatGPT | ✓ hints instead of answers | ✓ SRL, knowledge | ✓ RCT | ✓ | Eligible |
| Kumar et al. (2024) | ✓ undergraduates | ✓ LLM | ✓ LLM-guided self-reflection | ✓ proctored exam | ✓ randomised field experiments | ✓ L@S full paper | Eligible |
| Bereznikova et al. (2026) | ✓ 68/80 = 85 % HE | ✓ GenAI | ✓ Socratic prompts | ✓ perceived critical thinking | ✗ fixed-order within-subjects, no control | ✓ | E5 → context |

## Search
See `search/search_notes.md`, `search/run_search.py` and `search/search_log.tsv`. Final search: 617 records identified, 2 duplicates removed, 615 screened.
