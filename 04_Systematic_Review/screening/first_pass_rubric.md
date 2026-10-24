# Title/abstract screening rubric (criteria v2, frozen) — Deliverable 04

Review question: comparative evidence on tools based on generative LLMs designed to elicit higher-education students' OWN reasoning, and their effects on reflection/metacognition, self-regulation, critical thinking, AI dependence/over-reliance, academic integrity, learning performance measured by a test.

Decide for each record: INCLUDE, UNSURE or EXCLUDE (+ code). Use ONLY title and abstract. When in doubt -> UNSURE (UNSURE records go to full-text review; false negatives are worse than false positives).

Check codes in this FIXED ORDER and assign the FIRST one that CLEARLY fails. If an earlier criterion is uncertain and a later one clearly fails, assign the later one.
1. E1 Population: fails if <80% of the sample are higher-education students (undergraduate or postgraduate) and results are not reported separately; or no student participants at all (teachers, staff, datasets, benchmarks).
2. E4 Document type: review (systematic, scoping, narrative), conceptual/theoretical paper, essay, editorial, framework proposal without a primary outcome study, or study protocol.
3. E7 Not peer-reviewed / not a full paper: arXiv/SSRN/preprint servers, posters, extended abstracts, works-in-progress.
4. E2 No generative LLM (GPT-3 or later; e.g., ChatGPT, GPT-4, Llama, ERNIE, Gemini, Claude, custom GPTs). Rule-based chatbots or non-generative AI fail.
5. E3 The TOOL ITSELF does not scaffold the student's own reasoning.
   - PASS (can be INCLUDE): abstract states the tool asks questions (Socratic), gives graded hints instead of solutions, prompts reflection or metacognition, withholds answers, acts as a configured peer/assessor that makes students reason, or a GenAI agent delivers regulation scaffolds.
   - UNSURE band: tool is configured/purpose-built with pedagogical instructions (custom GPT, system prompt, RAG mentor, "scaffolded GenAI", purpose-built pedagogical agent) but the abstract does not say whether it elicits reasoning; or it is unclear whether the scaffolding is in the tool or in the instruction.
   - E3: unconfigured LLM used as generic assistant, content generator, writing aid or source of answers/feedback; LLM used by the teacher; studies comparing using AI vs not using AI with no scaffolding in the tool; surveys/interviews about general GenAI use; teaching-practice reports with generic tools.
   Words like "guidance", "feedback", "assistance" alone are NOT enough to pass.
6. E5 Design: fails if no control/comparison group (single-group pre-post, case study, survey, qualitative only, design case) or non-counterbalanced within-subjects. Eligible: randomised, quasi-experimental with control group, counterbalanced crossover. If the abstract does not state the design clearly but suggests a comparison -> UNSURE.
7. E6 No outcome among: reflection/metacognition, self-regulation, critical thinking, AI dependence/over-reliance, academic integrity, learning performance measured by a test/exam/score.
8. E8 Published outside 2022–2026.
9. E9 Language other than English or Spanish (judge by the full text language signal, e.g., non-Latin title).

INCLUDE only when all criteria plausibly pass on the abstract. Also add flag SNOWBALL to E4 records whose topic is LLM tools that scaffold HE students' reasoning/metacognition/self-regulation/integrity.

Calibration examples from the pilots (author decisions):
- INCLUDE: ChatGPT with hints instead of answers vs traditional ChatGPT, RCT, undergraduates, SRL/knowledge. ChatGPT configured as "virtual peer" in a peer-assessment cycle vs traditional ChatGPT, RCT, critical thinking. Socratic GenAI formative assessment tool, quasi-experimental, quiz scores.
- UNSURE: GenAI agent delivering adaptive socially-shared-regulation scaffolds vs static worksheets (outcome fit unclear); custom GPT/RAG mentors in quasi-experiment (configuration unclear); purpose-built multimodal pedagogical agent with task generation/diagnostics (function unclear); metacognitive prompts in a GenAI environment vs none (unclear if delivered by the tool).
- E3: unconfigured ChatGPT as writing feedback provider vs AWE vs control (even if randomised); ChatGPT replacing a tutor; ChatGPT+Midjourney as generic tools in design-based learning; TAM/UTAUT surveys.
- E4: editorials, essays, narrative syntheses, conceptual frameworks, literature analyses.
- E7: arXiv design case of a guardrailed tutor.

OUTPUT: a CSV with header rid,decision,code,flag,note — one row per record, in the input order; code empty for INCLUDE/UNSURE; flag = SNOWBALL or empty; note = one short reason (<= 20 words, no commas or wrap note in double quotes).
