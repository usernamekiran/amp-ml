- 2026-09-28 created files required for basic work-flow.
  - `train_baseline.py` works as intended.
  - tweaking is required

- 2026-10-02 changed training method from random 80-20 to static input files, testing from dedicated `test.csv`

- 2026-10-09 changed training method, utilises the database with +100k vetted entries.
  - `train_hard_negatives`
  - the increased iput data imporoved the accuracy drastically.
