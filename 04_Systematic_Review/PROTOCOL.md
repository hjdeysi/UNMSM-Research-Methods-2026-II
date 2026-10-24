# Deliverable 04 — Review protocol (v2, 2026-10-24, revised after the blind pilot)

v1 was frozen at commit `e9f8363` before any screening. v2 changes only the I3 definition and the order of exclusion codes, as decided by the author after the pilot (see *Pilot results and changes*).

**Design.** Rapid review following the Cochrane Rapid Reviews Methods Group guidance (Garritty et al., 2021, https://doi.org/10.1016/j.jclinepi.2020.10.007; Garritty et al., 2024, https://doi.org/10.1136/bmj-2023-076335): one human reviewer, AI-assisted first-pass screening, and a cap of 10 included studies set by the assignment. It is not a full systematic review. Reporting follows PRISMA 2020 (Page et al., 2021, https://doi.org/10.1136/bmj.n71).

## Review question
What comparative evidence exists on tools based on generative large language models that are designed to elicit higher-education students' own reasoning, and what effects do they report on reflection/metacognition, self-regulation, critical thinking, AI dependence, academic integrity and learning performance?

## Eligibility criteria (each with a mirror exclusion code)

| Code | Inclusion | Exclusion |
|---|---|---|
| I1 / E1 | ≥80 % of the sample in higher education (undergraduate or postgraduate), or results reported separately for that subgroup | Population not eligible |
| I2 / E2 | Tool based on a generative LLM (GPT-3 or later) | No generative LLM |
| I3 / E3 | The **tool itself** is designed or configured to elicit the student's own reasoning (Socratic questions, graded hints, reflection or metacognitive prompts, withholding answers). Pedagogical scaffolding placed *around* an unconfigured LLM does not satisfy I3 | No scaffolding of the student's own reasoning by the tool |
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
1. **Order of exclusion codes (v2): E1 → E4 → E7 → E2 → E3 → E5 → E6 → E8 → E9**; E10 and E11 apply only at full text. The nature of the document (E4 review/conceptual/protocol, E7 not peer-reviewed or not a full paper) is checked before content criteria.
2. Each excluded record gets the **first criterion in that order that clearly fails**. If an earlier criterion is uncertain and a later one clearly fails, the later code is assigned.
3. When in doubt at title/abstract, the record is marked UNSURE and goes to full text. Records without abstract (n = 20) go directly to full text.
4. **I3 operational definition (option a, approved by the author).**
   - *Passes:* the abstract states that the tool asks questions, gives graded hints instead of solutions, prompts reflection or metacognition, or is built to withhold answers (e.g., Socratic tutor, hint-based ChatGPT assistant, LLM-guided self-reflection, GenAI agent delivering regulation scaffolds).
   - *UNSURE:* the tool is configured with pedagogical instructions (custom GPT, system prompt, RAG mentor, "scaffolded" GenAI) but the abstract does not say whether it elicits reasoning; or the scaffolding could be either in the tool or in the instruction.
   - *E3:* unconfigured LLM used as a generic assistant, content generator or source of answers/feedback; LLM used by the teacher; comparison of using vs not using AI with no scaffolding in the tool.
5. Records coded E4 whose topic meets I1–I3 are flagged SNOWBALL; their reference lists are screened with the same criteria and reported under "identification via other methods", together with Zhou, Liu & Chiu (2026).
6. Decisions are taken on the **original abstract**; translations are reading aids only.

## Procedure
1. **Blind pilot.** 50 records drawn at random (seed 20261024, excluding records without abstract) are screened independently by the author and by the AI. The AI decisions were frozen before the author's pilot; SHA-256 of the file: `8c0235bf905f444e0ae2b3397b383bc7eb573ee52aed90efd8c1319a336f4b66`. Report Cohen's kappa (3 categories and binary include+unsure vs exclude) and percentage agreement; criteria definitions are adjusted and re-frozen afterwards.
2. **First pass.** The AI screens the remaining records.
3. **Verification.** The author reviews all INCLUDE/UNSURE records and a random sample of EXCLUDE records, blind to the AI label.
4. **Reporting.** Pilot kappa and false-negative rate reported in the PRISMA diagram (records excluded by human vs by automation) and in the AI-use disclosure.

## Pilot results and changes (2026-10-24)
Blind pilot, 50 random records (seed 20261024). The AI file matched the SHA-256 published before the author screened. Files: `screening/pilot_human_decisions.xlsx`, `screening/pilot_AI_decisions.csv`, `screening/pilot_comparison.csv`.

| Measure | Value |
|---|---|
| Binary agreement (to full text vs excluded) | 80 % (40/50) |
| Cohen's kappa, binary | 0.48 |
| PABAK | 0.60 |
| Cohen's kappa, 3 categories | 0.22 (mainly INCLUDE vs UNSURE, both to full text) |
| Exclusion code agreement among records both excluded | 17/33 |

All 10 binary disagreements had the same direction (author passes, AI excludes); 8 concerned I3 and 2 concerned E5 (no control group stated). Code disagreements came from the v1 order, which coded document type after content. Changes adopted in v2: (i) I3 kept as tool-level scaffolding (option a) with the operational definition above and an explicit UNSURE band to reduce false negatives in the AI first pass; (ii) new code order E1 → E4 → E7 → E2 → E3 → E5 → E6 → E8 → E9.

## Second blind pilot (criteria v2)
20 new random records (seed 2026102402, excluding pilot 1 and records without abstract). AI decisions frozen before the author screens; SHA-256: `185cd08111ad49759d8820ea6b84947b4b1273a368f1e6db199616b1120c2ce9`.

Results (AI file matched the registered hash): binary agreement 95 % (19/20); Cohen's kappa 0.64 (binary) and 0.65 (3 categories); PABAK 0.90; exclusion-code agreement 17/18. Low prevalence (2/20 to full text) widens uncertainty around kappa. The only binary disagreement (R128: author UNSURE, AI E3) concerned a purpose-built pedagogical agent whose reasoning-eliciting function was unclear; under rule 4 it belongs to the UNSURE band, so the author's decision is adopted and the AI first pass is instructed to place purpose-built pedagogical agents of unclear function in UNSURE. **Criteria v2 are frozen for the first pass (2026-10-24).**

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
