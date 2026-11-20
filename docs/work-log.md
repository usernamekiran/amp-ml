## Current status

- production models planned: two models for production-level (different purposes), various models during development/testing phase

- entries vetted: approximately 13,000
- target entries: 25,000+
- no futher test runs till 25k entries are vetted manually


## Chronological notes

- 2026-09-28 created files required for basic workflow.
  - `train_baseline.py` works as intended.
  - further tuning is required.

- 2026-10-02 changed the training method from random 80/20 train-test split to static input files, testing using a dedicated `test.csv`

- 2026-10-09 changed training method, utilises the database with +100k vetted entries.
  - `train_hard_negatives`
  - the increased input/training data significantly improved accuracy.
  
- 2026-10-13
  - decided to consolidate all functionality into a single model, and to consolidate training data.

- 2026-10-25
  - decided to scrape all the input files, and to use production database for training.
  - consolidated data:
    - for false positives: `false_positives` table
    - for positive/confirmed identification: `fetched` table.
      - `confirmed_table` to be created?
    - for pairing logic: `fetched` table
    - for avoiding false negatives: logic from training

- 2026-11
  - determined that a single model was not technically viable for all intended purposes.
  - decided to use two separate models for production-level, each serving a different purpose.
  - exploring multiple models during development/testing phase - `tf-idf + logistic regression`, `neural network`, `tf-idf + LR + ANN`
  - vetting:
    - 2% of db entries contain hard incorrect entries.
    - there are about 5% entries that are syntactically correct, work in practice, but are not suitable for training the model.
    - at least 25k entries need to be vetted manually for training both the models.
      - to avoid a homogeneous dataset, entries will be extracted in batches at incremental intervals throughout the existing production database.
