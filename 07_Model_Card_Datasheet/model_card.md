# Model Card — Virtue-Based Reflective Scaffolding Agent (planned, v0.1)

Deliverable 07 · Research Methods and Scientific Integrity in AI · UNMSM 2026-II · Deisy Lizbeth Acosta Ticse
Framework: Mitchell et al. (2019), *Model Cards for Model Reporting*, FAT* '19, 220–229. https://doi.org/10.1145/3287560.3287596

**Adaptation note.** Model cards were proposed for *trained models*. This artifact is a **system built on a base large language model** whose behaviour is set by prompting and, possibly, retrieval; no model is trained in the planned design. The card therefore documents the system, and refers base-model properties to the provider's own documentation. **Status: PLANNED — NOT YET IMPLEMENTED OR EVALUATED.**

## 1. Model details
| Element | Documentation | Status |
|---|---|---|
| Type | LLM-based conversational agent implementing Socratic, virtue-oriented scaffolding when a student asks it to complete academic work | Defined |
| Base model | Commercial LLM accessed through an API (specific provider and version to be fixed and reported) | Defined (provider UNKNOWN) |
| Privacy condition of the API choice | No student data sent to the provider without a data-processing agreement; messages pseudonymised before sending; provider's data-retention terms documented | Planned |
| Configuration | System prompt and scaffolding policy derived from the annotated corpus (see datasheet) | Planned |
| Research approach | Design Science Research; contribution: nascent design theory (Hevner et al., 2004; Gregor & Hevner, 2013) | Defined |

## 2. Intended use
| Element | Documentation | Status |
|---|---|---|
| Primary use | Prompt undergraduates to deliberate (prudence, honesty) before delegating academic work to generative AI | Defined |
| Users | Undergraduates in Peruvian university courses, in Spanish | Defined |
| Out of scope | Grading; misconduct detection or sanctioning; replacing the instructor; use outside the evaluated courses without re-evaluation | Defined |

## 3. Factors
| Element | Documentation | Status |
|---|---|---|
| Relevant factors | Course section (unit of assignment), discipline, prior AI use, baseline reflection level | Planned |
| Evaluation factors | Results reported per condition and, where sample allows, per section | Planned |

## 4. Metrics
| Element | Documentation | Status |
|---|---|---|
| Metacognitive reflection | Coding of reflections/logs with the four-category scheme of Kember et al. (2008) | Defined (Spanish adaptation pending) |
| AI dependence | DAI scale (Morales-García et al., 2024), developed with Peruvian university students | Defined |
| Product integrity | Composite: log-based provenance ratio + blinded expert rubric | Planned (content validity pending) |
| Manipulation check | Perceived restrictiveness of the restrictive-normative condition | Planned |
| Behavioural check | Rate at which the agent withholds full solutions (answer leakage) | Planned |

## 5. Evaluation data
| Element | Documentation | Status |
|---|---|---|
| Design | Sequential explanatory mixed methods; quasi-experiment with three conditions (agent, unrestricted, restrictive-normative); intact section as unit, ≥ 2 sections per condition; multilevel models | Defined |
| Data | Pre/post measures and conversation logs — **NOT YET COLLECTED** | UNKNOWN |
| Lesson from Deliverable 04 | Include an unassisted post-test, since gains with the tool may not persist without it | Planned |

## 6. Training data
No model is trained. The annotated corpus informs the system prompt and scaffolding policy (see datasheet). If fine-tuning is later adopted, this section must be completed. — **Not applicable (planned design)**

## 7. Quantitative analyses
None yet. Results will be reported for every outcome, by condition, with effect sizes, whether or not they support the hypotheses. — **UNKNOWN**

## 8. Ethical considerations
| Risk | Mitigation | Status |
|---|---|---|
| Researcher is designer, instructor and evaluator | Ethics approval; consent collected by a third party and decoupled from grading; blinded external coders | Planned |
| Student data exposure (API provider) | Logs pseudonymised at capture and before any API call; data-processing agreement with the provider; institution-controlled storage; never in public repositories | Defined |
| Paternalism / frustration | Agent asks rather than refuses; monitor disengagement in logs | Planned |
| Moralising or cultural bias in virtue judgments | Exemplar-anchored annotation; expert validation | Planned |

## 9. Caveats and recommendations
Evidence from the Deliverable 04 review shows that tool-level scaffolding improved process measures more consistently than unassisted performance; claims about the agent should be limited to what the evaluation measures. The agent must not be presented as a detector of academic misconduct.

## References
Gregor, S., & Hevner, A. R. (2013). *MIS Quarterly, 37*(2), 337–355. https://doi.org/10.25300/MISQ/2013/37.2.01 · Hevner, A. R., et al. (2004). *MIS Quarterly, 28*(1), 75–105. https://doi.org/10.2307/25148625 · Kember, D., et al. (2008). *Assessment & Evaluation in Higher Education, 33*(4), 369–379. https://doi.org/10.1080/02602930701293355 · Morales-García, W. C., et al. (2024). *Frontiers in Education, 9*, 1323898. https://doi.org/10.3389/feduc.2024.1323898
