# AR Gauntlet Sectional

A 30-question Analytical Reasoning sectional (6 sets × 5 questions) in CLAT 2026 Section IV formats, set well above CLAT difficulty.

- `AR_Gauntlet_Sectional_Paper.docx`: question booklet with an answer sheet. No answers inside.
- `AR_Gauntlet_Sectional_Answer_Key.docx`: key, CLAT 2026 AR analysis, solutions, and the trap in every question.
- `ar_gauntlet.html`: the online test (stopwatch, flags, scoring at +1 / −0.25, explanations after submitting).
- `source/`: `paper.py` holds all content; `build.py` builds the three files. `p*.py` are the constraint solvers for each set, and `v*.py` check every keyed answer against every valid arrangement.
