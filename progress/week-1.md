# Week 1: Foundation & Data Pipeline

**Timeline:** Days 1-7  
**Time Budget:** 10 hours  
**Goal:** Get data flowing and understand what you're working with

---

## Day 1-2: Environment Setup (2 hours)

- [x] Create GitHub repo (2/9)
- [x] Set up Python virtual environment (`python -m venv venv`) (2/9)
- [x] Install core libraries: (2/9)
  ```bash
  pip install pandas numpy yfinance ta scikit-learn matplotlib seaborn jupyter
  ```
- [x] Create basic project structure: (2/9)
  ```
  trading-ml/
  ├── data/
  ├── models/
  ├── notebooks/
  ├── src/
  │   ├── data_collection.py
  │   ├── feature_engineering.py
  │   └── utils.py
  ├── progress/
  └── tests/
  ```
- [x] Initialize git and make first commit (2/9)

---

## Day 3-4: Data Collection (4 hours)

- [x] Write `data_collection.py` script to download historical data (2/9)
- [x] Download 2 years of daily data for starter stocks: (2/9)
  - SPY (S&P 500 ETF)
  - QQQ (Nasdaq ETF)
  - AAPL (Apple)
  - MSFT (Microsoft)
  - TSLA (Tesla)
- [x] Save data to CSV with proper date indexing (2/9)
- [x] Create Jupyter notebook `01_data_exploration.ipynb` (2/9)
- [x] Visualize data: (2/10)
  - [x] Price charts over time (2/9)
  - [x] Volume patterns (2/10)
  - [x] Basic moving averages (20-day, 50-day) (2/10)
- [x] Document any data quality issues (2/9)
  - Had to mess with multi-index header and the unnanmes index column (going from multi-index header to single clean header)

---

## Day 5-7: Feature Engineering Basics (4 hours)

- [x] Create `feature_engineering.py` module (2/10)
- [ ] Implement technical indicators:
  - [x] Simple Moving Averages (SMA 20, 50, 200) (2/11)
  - [x] Exponential Moving Average (EMA 12, 26) (2/11)
  - [x] RSI (Relative Strength Index) (2/11)
  - [x] MACD (Moving Average Convergence Divergence) (2/11)
  - [x] Bollinger Bands (2/11)
  - [x] Volume indicators (Volume SMA, Volume ratio, On-Balance Volume) (2/11)
- [ ] Create target variable (AAPL only first, generalize later):
  - [ ] Define prediction target: does next day's close go up or down? (binary: 1 = up, 0 = down)
  - [ ] Label historical data with target
- [ ] Create visualization notebook `02_feature_analysis.ipynb`:
  - [ ] Plot features vs target variable
  - [ ] Check for obvious patterns
  - [ ] Identify potential signal vs noise
- [ ] Save processed data with features to `data/processed/`

---

## End of Week Deliverables

✅ **Working data pipeline** that downloads and stores historical stock data  
✅ **Processed dataset** with 10+ engineered features  
✅ **2 Jupyter notebooks** showing data exploration and feature analysis  
✅ **Clean repo structure** ready for model development

---

## Notes & Learnings

_Use this section to document what you learned, challenges faced, and ideas for next week:_

- 
- 
- 

---

## Next Week Preview

Week 2 will focus on building your first backtesting framework and training a simple Logistic Regression model to predict trade signals.