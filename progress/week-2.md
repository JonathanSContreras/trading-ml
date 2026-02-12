# Week 2: First Model & Evaluation

## Goal
Train a binary classifier on AAPL, evaluate it honestly, and have a working end-to-end ML pipeline you can generalize to other tickers.

---

## Context & Constraints
- [ ] Confirm train set is 2024 AAPL data (processed, from `data/processed/`)
- [ ] Confirm test set is 2025 AAPL data
- [ ] Confirm `target` column is present (1 = next day up, 0 = next day down)
- [ ] Note the baseline to beat: ~56% accuracy (always predicting "up")

---

## Feature Set (starting lean)
Use these 6 features for your first model run:
- [ ] `RSI_14`
- [ ] `MACD_Histogram_9`
- [ ] `Volume_Ratio_20`
- [ ] `Daily_Return`
- [ ] `Price_Relative_to_MA_20` (or `Price_Relative_to_MA_50` — pick one)
- [ ] `Bollinger_Normalized_20.`

Explicitly **exclude**: raw Bollinger values, OBV raw, any column that required `shift(-n)` to build.

**Consider for a second run**: `Return_Day_5` or `Return_Day_10` — these are now backward-looking (how much the stock moved over the past N days), so they're safe as model inputs. Could capture recent momentum that daily return alone doesn't.

---

## Tasks

### 1. Build `03_first_model.ipynb`

**Step 1 — Load and split**
- [ ] Load `data/processed/AAPL_with_features.csv`
- [ ] Parse `Date` as index, sort ascending
- [ ] Split on date: everything in 2024 → train, everything 2025+ → test
- [ ] Print shape of each split to confirm sizes look right

**Step 2 — Prepare X and y**
- [ ] Select your 6 feature columns into `X_train`, `X_test`
- [ ] Extract `target` into `y_train`, `y_test`

**Step 3 — Train logistic regression**
- [ ] Use `sklearn.linear_model.LogisticRegression`
- [ ] Set `max_iter=1000`, `random_state=42`, everything else default
- [ ] Fit on train, predict on test

**Step 4 — Train random forest**
- [ ] Use `sklearn.ensemble.RandomForestClassifier`
- [ ] Set `n_estimators=100`, `max_depth=5`, `random_state=42`
- [ ] Fit on train, predict on test

---

### 2. Evaluate Both Models

**Standard metrics**
- [ ] Print accuracy for both models (note the 56% baseline explicitly)
- [ ] Print `classification_report` for both (precision, recall, F1 per class)
- [ ] Plot confusion matrix using `ConfusionMatrixDisplay` for both

**Confidence-sliced accuracy**
- [ ] Get predicted probabilities via `predict_proba` for both models
- [ ] Filter to predictions where `prob > 0.6` or `prob < 0.4`
- [ ] Report accuracy on that subset and how many predictions fell into it
- [ ] Note whether high-confidence accuracy is meaningfully better than overall accuracy

**Feature importance (Random Forest only)**
- [ ] Extract `rf.feature_importances_` paired with feature names
- [ ] Plot a bar chart showing which features the model leans on most

---

### 3. Inspect Wrong Predictions
- [ ] Build a DataFrame: Date, actual, predicted, probability
- [ ] Filter to wrong predictions only
- [ ] Spend 10–15 minutes eyeballing for patterns — clustering in time, around earnings, high-volatility stretches
- [ ] Write 2–3 sentences summarizing what you noticed

---

### 4. Document Results in `results/week2_summary.md`
- [ ] Train period, test period, sample counts for each
- [ ] Features used
- [ ] Logistic regression: accuracy, precision, recall
- [ ] Random forest: accuracy, precision, recall
- [ ] Confidence-sliced accuracy for whichever model performed better
- [ ] 2–3 sentences on what the wrong predictions looked like
- [ ] Honest assessment: did you beat the baseline, and does it feel meaningful or lucky?

---

## Success Criteria
- [ ] Working train/test pipeline that is strictly date-ordered
- [ ] At least two models trained and compared
- [ ] Feature importances reviewed for random forest
- [ ] Wrong predictions inspected manually
- [ ] Written summary committed to `results/week2_summary.md`

---

## What Week 3 Will Depend On
- If both models hover near baseline → Week 3 focuses on feature engineering (lag features, regime indicators, sector features)
- If random forest meaningfully beats logistic regression → explore what the tree is doing, consider light hyperparameter tuning with a proper validation window
- If logistic regression is competitive with random forest → useful finding; your signal (if any) may be close to linear

---

## Files to Produce
```
notebooks/03_first_model.ipynb   ← main work
results/week2_summary.md         ← written findings
```
Optional: `src/train_model.py` if you want to start extracting reusable training logic out of the notebook.