# Reproducibility Audit Report

Deliverable 06 · Research Methods and Scientific Integrity in AI · UNMSM 2026-II · Deisy Lizbeth Acosta Ticse
Instrument: Session 6 reproducibility scorecard (9 items; Yes / Partial / No). Audit date: 25 Oct 2026.

## 1. Paper metadata
Hou, X., Liu, Z., Wang, G., & Shi, N. (2026). Bridging awareness and behavior: decoding implicit metacognitive behaviors in AI-assisted programming via fine-grained log analysis. *Frontiers in Psychology, 17*. https://doi.org/10.3389/fpsyg.2026.1790196 (open access).

**Why this paper.** It is one of the 10 studies included in my Deliverable 04 review (record R047), it reports a randomised trial of an AI scaffolding agent, and its headline result is a single post-test difference.

## 2. Experimental setup (as reported)
| Element | Reported |
|---|---|
| Population | 126 undergraduates recruited (convenience sampling), one Python course, one Chinese university; 122 analysed (attrition 3.2 %, by group not reported) |
| Allocation | Individual randomisation with Excel `=RAND()`; AI n = 62, control n = 60; allocation concealment not described |
| Intervention | AI agent in a customised Jupyter Notebook; rule-based triggers (e.g., first keystroke < 60 s, idle > 10 min) launch non-directive metacognitive prompts; example prompts in Table 1; **underlying LLM not named** |
| Control | Native Jupyter Notebook, no AI |
| Outcomes | Post-test programming score (isomorphic task; rubric; two blinded raters; ICC = 0.81 on a 30 % subset); modified MAI (self-report); 11 log-derived behaviour metrics |
| Analysis | t-tests / Mann–Whitney U; linear mixed model for MAI; Bonferroni for the 11 log metrics; Shapiro–Wilk, Q–Q plots, Levene |

## 3. Scorecard
| # | Item | Rating | Evidence and reasoning |
|---|---|---|---|
| 1 | Seeds reported, many runs? | **No** | The `=RAND()` allocation has no recorded seed, so the allocation cannot be regenerated. A single trial; no replication. |
| 2 | Splits described? (here: group allocation) | **Partial** | Method and group sizes given; concealment, attrition by group and age/gender balance not reported. |
| 3 | Leakage checked? (here: contamination and outcome overlap) | **Partial** | Raters blinded (good). No safeguards against information flowing between groups in the same course; the post-test is isomorphic to practice tasks, so it measures near transfer only. |
| 4 | Tuning separated? (here: trigger thresholds) | **Partial** | Thresholds are called "predefined", but their origin is not stated; it is unclear whether they were set before or after seeing this cohort's logs. |
| 5 | Statistical test named? | **Yes** | Tests, assumption checks and correction for the log metrics are named. |
| 6 | Effect size and CI? | **Partial** | Cohen's d and r reported; **no confidence intervals**; the headline d is internally inconsistent (Section 4). |
| 7 | External validation? | **No** | One site, one course, one cohort; authors acknowledge limited generalisability. |
| 8 | Compute documented? | **No** | LLM identity and version, Python/SciPy/Pandas versions, Jupyter extension and hardware are not reported. |
| 9 | Code and data available? | **Partial** | Data "available by the authors, without undue reservation" (on request); no code or full prompt set released. |

**Overall score: 7 / 18 (39 %)** — Yes = 2, Partial = 1, No = 0. **Judgement: low reproducibility.** The design is sound in principle (randomised, blinded scoring, baseline equivalence tested), but a stranger could not rebuild the intervention (unknown model, partial prompts, no code) or regenerate the allocation, and the reported statistics contain inconsistencies.

## 4. Statistical rigor — numbers I recomputed from the reported values
| Reported | Recomputed | Problem |
|---|---|---|
| Post-test 85.2 (SD 9.4, n = 62) vs 76.5 (SD 10.8, n = 60); t(120) = 4.75, **p = 0.002** (Section 5.2) | t = 4.75 gives **p ≈ 0.000006**; Table 7 itself says p < 0.001 | Text and table disagree |
| **d = 0.76** | Pooled SD 10.11 → **d = 0.86**; the reported t is consistent with 0.86, not 0.76 | Effect size misreported |
| No CI | Mean difference 8.7, **95 % CI 5.1 to 12.3** (from reported means/SDs) | CI should be reported |
| Pre-test MAI covariate β = 0.044, SE = 0.012, **p = 0.174** (Table 8) | β/SE = 3.67 → **p ≈ 0.0002** | Coefficient, SE and p cannot all be correct |
| Control MAI 51.9 + 10.9 | = 62.8 (reported 62.5) | Arithmetic slip |
| Two "pre-test" programming measures (Table 6: 52.7 vs 51.0; Table 7: 68.4 vs 67.9) | — | Not explained |

Other concerns: very large effects on log metrics (d = 4.08 and 3.87) from a 21-day intervention warrant scrutiny of metric definitions; no power analysis; multiple-comparison correction applied only to the log metrics, not to all outcome families; recruitment is dated January–February 2025 while log timestamps are from May 2025.

**Exit-ticket number:** the headline *p = 0.002 with d = 0.76* is not a lucky run but a **reporting error**: the reported data imply a larger, more certain effect (d = 0.86, p < 0.001). The error does not overturn the finding, but it shows the numbers were not checked against each other.

## 5. Missing information
LLM name and version; full prompt set and trigger code; randomisation seed and concealment; power analysis; attrition by group; confidence intervals; software and hardware versions; analysis scripts; anonymised log data in a repository; a delayed post-test without the AI (the authors themselves note persistence after removal is unknown).

## 6. Recommendations (three fixes that would help most)
1. **Release the intervention:** name the LLM and version, publish the full prompt set, trigger rules and Jupyter extension code, plus anonymised logs and analysis scripts with pinned versions.
2. **Correct and complete the statistics:** reconcile the p-value, recompute d, fix Table 8, report confidence intervals for every primary effect, and state the multiple-comparison strategy for all outcome families.
3. **Strengthen the design for replication:** pre-register with a power analysis, conceal allocation (seeded, documented), add a delayed post-test without the AI, and replicate in a second course or institution.

## 7. Relevance to my thesis
This study is evidence in my Deliverable 04 review. The audit lowers the weight I give it (already flagged there as "LLM not specified") and turns its gaps into requirements for my own protocol: name the model and version, publish prompts, report CIs, and include an unassisted post-test.

*Verification note: values were extracted from the HTML full text and checked by recomputation; tables should be re-checked against the PDF version of record before citing.*
*AI-use disclosure: Claude (Anthropic) assisted in extracting reported values, recomputing statistics and drafting the report; ratings and judgement reviewed by the author.*
