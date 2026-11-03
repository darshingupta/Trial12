# Step-Up Sectionals: RC and LR-CR

Two CLAT sectionals in the question types CLAT set from 2022 to 2026, pitched one step above Career Launcher Countdown mocks.

| Sectional | Questions | Time | Sets |
|---|---|---|---|
| RC Step-Up Sectional | 24 (4 passages × 6) | 30 min | fiction (unreliable narrator), history (the census and caste), science (why organisms age), philosophy (is gratitude a debt?) |
| LR-CR Step-Up Sectional | 26 (4 × 5 and 1 × 6) | 32 min | compulsory attendance, Punjab's paddy law, a leaked question paper (CLAT 2026 deduction set), blind auditions, an outpatient queue (CLAT 2024/25 consultant case) |

Marking is +1 / −0.25 / 0.

## Files

- `RC_Step_Up_Sectional_Paper.docx` and `LR_CR_Step_Up_Sectional_Paper.docx`: question booklets with an answer sheet. No answers anywhere inside.
- `RC_Step_Up_Sectional_Answer_Key.docx` and `LR_CR_Step_Up_Sectional_Answer_Key.docx`. Each key contains:
  - answers at a glance;
  - the CLAT 2022–2026 type survey the paper is built on;
  - what makes the paper harder than CL;
  - the trap each wrong option sets, mapped to your CL mock misses;
  - the blind-solve audit;
  - a full explanation of every question.
- `RC_Step_Up_Sectional.html` and `LR_CR_Step_Up_Sectional.html`: the online timed tests. They have a countdown, flags, answers that survive a reload, and scoring with trap codes and explanations after you submit.
- `source/`:
  - `rc.py` and `lr.py` hold the passages, questions, keys and trap codes.
  - `rc_ex.py` and `lr_ex.py` hold the explanations.
  - `build.py` builds the Word files and the test page from `template.html`.

Rebuild with:

```bash
cd source && python3 build.py rc .. && python3 build.py lr ..
```

## How the papers were checked

Each paper was blind-solved by an independent solver, working without the key, in rounds. The solver flagged any question with two defensible answers, any error, any easy question and any tell. Every flagged question was rebuilt or replaced and then solved again blind. The answer key's "Blind-solve audit" section records what each round found and what changed.
