# Datasheet — Spanish Academic-Integrity Scenarios Annotated for Virtues (planned, v0.1)

Deliverable 07 · Research Methods and Scientific Integrity in AI · UNMSM 2026-II · Deisy Lizbeth Acosta Ticse
Framework: Gebru et al. (2021), *Datasheets for Datasets*, Communications of the ACM, 64(12), 86–92. https://doi.org/10.1145/3458723

**Dataset status: PLANNED — NOT YET COLLECTED.** Each element is labelled **Defined** (decision taken), **Planned** (designed, not executed), or **UNKNOWN** (depends on approvals or data not yet available), with the action required before collection.

Scope: this datasheet covers the annotated scenario corpus (thesis artifact 1). Conversation logs produced in the evaluation are a separate dataset and will have their own datasheet.

## 1. Motivation
| Element | Documentation | Status | Action before collection |
|---|---|---|---|
| Purpose | Provide a Spanish-language resource of academic-integrity scenarios involving generative AI, annotated for the four cardinal virtues (prudence, justice, fortitude, temperance) plus academic honesty, to inform the design and evaluation of a reflective scaffolding agent | Defined | — |
| Gap addressed | Existing moral-judgment resources (e.g., ETHICS; Hendrycks et al., 2021) are in English, crowd-annotated without a unified philosophical framework, and outside the academic-integrity domain | Defined | Checked against the Deliverable 04 review: none of the 10 included studies measures academic integrity or an ethical outcome |
| Creators | Doctoral researcher (UNMSM, DSR thesis) | Defined | — |
| Funding | Self-funded; external calls to be assessed | UNKNOWN | Confirm before collection |

## 2. Composition
| Element | Documentation | Status | Action before collection |
|---|---|---|---|
| Instance | One written scenario in which a university student faces a decision about delegating academic work to generative AI | Defined | Freeze the scenario template |
| Labels | Per scenario and per virtue: relevance and enacted/violated judgment, anchored in expert-validated exemplar cases (not rule-based definitions) | Planned | Write the annotation guide with exemplars |
| Number of instances | — | UNKNOWN | Set by pilot agreement and annotation budget |
| Scenario source | Both: scenarios written by experts and scenarios adapted from documented cases | Defined | Remove identifiers from adapted cases; record origin of each scenario |
| Personal data | Scenarios are not intended to contain personal data | Planned | Screening step to remove identifiers if real cases are adapted |
| Language | Spanish (Peruvian university context) | Defined | — |
| Splits | — | UNKNOWN | Define after size is known; split by scenario to avoid leakage |

## 3. Collection process
| Element | Documentation | Status | Action before collection |
|---|---|---|---|
| Validation | Content validity of virtue definitions and scenarios by expert judgment (formative, artificial FEDS episode; Venable et al., 2016) | Planned | Recruit experts; define validity index |
| Annotators | Trained annotators; number not yet fixed | UNKNOWN | Recruit and train; record annotator profiles |
| Timeframe | Thesis plan: corpus construction 2027-I to 2027-II | Planned | Confirm after ethics approval |
| Ethics | Approval by an institutional research ethics committee before any collection | Planned | Submit protocol |

## 4. Preprocessing / annotation
| Element | Documentation | Status | Action before collection |
|---|---|---|---|
| Agreement | Krippendorff's alpha **reported per virtue, not aggregated** (Hayes & Krippendorff, 2007) | Defined | Set acceptance threshold in the guide |
| Pilot | Pilot annotation round before full annotation | Planned | Run and revise guide |
| Raw data kept | Raw annotations kept alongside adjudicated labels | Planned | Define storage format and versioning |

## 5. Uses
| Element | Documentation | Status |
|---|---|---|
| Intended | Designing and evaluating the reflective scaffolding agent; research on virtue-based annotation | Defined |
| Not intended | Grading students; detecting misconduct; profiling individuals' moral character | Defined |
| Known risk | Operationalising prudence may drift towards a rulebook, the restrictive logic the thesis questions; mitigated by exemplar anchoring and per-virtue reporting | Defined |

## 6. Distribution
| Element | Documentation | Status | Action before collection |
|---|---|---|---|
| Release | Open release of the corpus and annotation guide **if ethics approval permits** | Planned | Align with consent and approval |
| Licence | — | UNKNOWN | Choose licence before release |

## 7. Maintenance
| Element | Documentation | Status |
|---|---|---|
| Maintainer | Doctoral researcher | Defined |
| Versioning | Semantic versions of corpus, guide and agreement report | Planned |
| Error reporting | Issue tracker in the project repository | Planned |

## References
Hayes, A. F., & Krippendorff, K. (2007). *Communication Methods and Measures, 1*(1), 77–89. https://doi.org/10.1080/19312450709336664 · Hendrycks, D., et al. (2021). Aligning AI with shared human values. *ICLR*. https://doi.org/10.48550/arXiv.2008.02275 · Venable, J., Pries-Heje, J., & Baskerville, R. (2016). *European Journal of Information Systems, 25*(1), 77–89. https://doi.org/10.1057/ejis.2014.36
