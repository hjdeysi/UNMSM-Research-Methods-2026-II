# Deliverable 05 - Reproducible ML Pipeline (GitHub repository)

Course: Research Methods and Scientific Integrity in AI and Advanced Technologies\
Universidad Nacional Mayor de San Marcos - UNMSM, 2026-II\
Student: Deisy Lizbeth Acosta Ticse

**Repository:** https://github.com/hjdeysi/repro-lab

| Requirement | Where |
|---|---|
| ≥ 4 commits | 5 commits in the repository history |
| Leakage-free Pipeline | `src/train.py` (StandardScaler inside a scikit-learn Pipeline, evaluated with stratified 5-fold CV) |
| 5 seeds logged in MLflow, mean ± SD | `src/run_seeds.py`, `results_summary.csv` — accuracy **0.9786 ± 0.0031** (sample SD, ddof = 1) |
| Stranger test | `README.md` + `requirements.txt`; verified in a fresh clone and a fresh virtual environment before submission |
