- 2026-09-28 created files required for basic work-flow.
  - `train_baseline.py` works as intended.
  - tweaking is required

- 2026-10-02 changed training method from random 80-20 to static input files, testing from dedicated `test.csv`

- 2026-10-09 changed training method, utilises the database with +100k vetted entries.
  - `train_hard_negatives`
  - the increased input/training data imporoved the accuracy drastically.
  
- 2026-10-13
  - decided to consolidate models, and training data.

- 2026-10-25
  - consolidated data:
    - for false positives: `false_positives` table
    - for positive/confirmed identification: `fetched` table.
      - `confirmed_table` to be created?
    - for pairing logic: `fetched` table
    - for avoiding false negatives: logic from training
