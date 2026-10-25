# Deliverable 04 - Mini Systematic Review + PRISMA 2020 + Gap Analysis

Course: Research Methods and Scientific Integrity in AI and Advanced Technologies\
Universidad Nacional Mayor de San Marcos - UNMSM, 2026-II\
Student: Deisy Lizbeth Acosta Ticse

**Design:** rapid review (one human reviewer, AI-assisted first-pass screening, cap of 10 studies under a pre-specified prioritisation rule), reported with PRISMA 2020.

**Review question:** What comparative evidence exists on tools based on generative large language models that are designed to elicit higher-education students' own reasoning, and what effects do they report on reflection/metacognition, self-regulation, critical thinking, AI dependence, academic integrity and learning performance?

## Components required by the brief

| Component | File |
|---|---|
| 1. 10 key articles from a documented Boolean search in Semantic Scholar | Search string and log: [`search/search_notes.md`](search/search_notes.md), [`search/run_search.py`](search/run_search.py), [`search/search_log.tsv`](search/search_log.tsv) · Included studies: [`synthesis/D04_extraction_and_gaps.xlsx`](synthesis/D04_extraction_and_gaps.xlsx) (sheet *Extraction_matrix*) · Zotero/Mendeley import: [`synthesis/D04_included_10.ris`](synthesis/D04_included_10.ris) |
| 2. PRISMA 2020 flow diagram (official template), four phases, counts that add up | [`prisma/PRISMA_2020_flow_D04_Acosta.pdf`](prisma/PRISMA_2020_flow_D04_Acosta.pdf) (counts in [`prisma/counts.json`](prisma/counts.json)) |
| 3. Gap analysis table (knowledge · methodological · contextual · theoretical) with evidence from the corpus | [`synthesis/D04_extraction_and_gaps.xlsx`](synthesis/D04_extraction_and_gaps.xlsx) (sheet *Gap_analysis*) |

## Method record
- Protocol, criteria, pilots, deviations and decisions with dates: [`PROTOCOL.md`](PROTOCOL.md)
- Screening files (pilots, AI first pass, blind verification, full-text assessment): [`screening/`](screening/)

**Counts:** identified 617 → duplicates 2 → screened 615 → excluded at title/abstract 507 (human 98, tool 409) → sought 108 → not retrieved 11, not assessed after the cap 75 → assessed 22 → excluded 12 → **included 10**.

## Declared limitations
Single human reviewer; AI-assisted first pass (blind verification: 1 of 45 sampled exclusions rescued, 2.2 %); 11 full texts not retrieved; cap of 10 studies (75 reports not assessed); no citation searching ("other methods" branch); two included studies do not name the LLM and one journal does not declare peer review.

## AI-use disclosure
Claude (Anthropic) was used to run and document the search, to perform the first-pass title/abstract screening under criteria set and piloted by the author, to extract full-text evidence, and to draft the extraction matrix. The author wrote the gap statements; Claude checked them against the extraction matrix, corrected counts and edited the English, and the author approved the final text. All eligibility decisions are the author's.
