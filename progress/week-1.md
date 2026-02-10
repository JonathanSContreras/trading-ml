# Week 1: Foundation & Data Pipeline

**Timeline:** Days 1-7  
**Time Budget:** 10 hours  
**Goal:** Get data flowing and understand what you're working with

---

## Day 1-2: Environment Setup (2 hours)

- [ ] Create GitHub repo
- [ ] Set up Python virtual environment (`python -m venv venv`)
- [ ] Install core libraries:
  ```bash
  pip install pandas numpy yfinance ta scikit-learn matplotlib seaborn jupyter
  ```
- [ ] Create basic project structure:
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
- [ ] Initialize git and make first commit

---

## Day 3-4: Data Collection (4 hours)

- [ ] Write `data_collection.py` script to download historical data
- [ ] Download 2 years of daily data for starter stocks:
  - SPY (S&P 500 ETF)
  - QQQ (Nasdaq ETF)
  - AAPL (Apple)
  - MSFT (Microsoft)
  - TSLA (Tesla)
- [ ] Save data to CSV with proper date indexing
- [ ] Create Jupyter notebook `01_data_exploration.ipynb`
- [ ] Visualize data:
  - [ ] Price charts over time
  - [ ] Volume patterns
  - [ ] Basic moving averages (20-day, 50-day)
- [ ] Document any data quality issues

---

## Day 5-7: Feature Engineering Basics (4 hours)

- [ ] Create `feature_engineering.py` module
- [ ] Implement technical indicators:
  - [ ] Simple Moving Averages (SMA 20, 50, 200)
  - [ ] Exponential Moving Average (EMA 12, 26)
  - [ ] RSI (Relative Strength Index)
  - [ ] MACD (Moving Average Convergence Divergence)
  - [ ] Bollinger Bands
  - [ ] Volume indicators (Volume SMA, Volume ratio)
- [ ] Create target variable:
  - [ ] Define prediction target (e.g., "price increases >1% in next 3 days")
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