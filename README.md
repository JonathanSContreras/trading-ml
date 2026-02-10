# ML Trading Bot

> **⚠️ Work in Progress** - An educational machine learning project exploring algorithmic trading

## Overview

This project is a learning exercise in applying machine learning to financial markets. The goal is to build an autonomous trading system that uses ML models to predict price movements and execute trades on stocks and ETFs, starting with swing trading (2-5 day holds).

**This is NOT financial advice. This is a learning project to gain hands-on ML experience.**

## Goals

- 🎓 **Primary**: Learn machine learning concepts through a real-world application
- 📊 **Secondary**: Build a functional trading system that can operate autonomously
- 🚀 **Tertiary**: Create a public dashboard to showcase model performance and trading activity

**Expected Outcome**: Gain practical ML skills, not necessarily profitable trades. If the bot doesn't lose money catastrophically, that's a win.

## Approach

### Phase 1: Backtesting & Model Development *(In Progress)*
- Historical data analysis using technical indicators
- Classical ML models (Random Forest, XGBoost)
- Walk-forward validation to avoid look-ahead bias
- Performance metrics: returns, Sharpe ratio, win rate, drawdown

### Phase 2: Paper Trading *(Planned)*
- Real-time simulation using Alpaca paper trading API
- Daily execution loop
- Performance monitoring and logging

### Phase 3: Dashboard *(Planned)*
- Public web interface showing:
  - Real-time P&L and portfolio positions
  - Trade history and outcomes
  - Model confidence and performance metrics
  - Feature importance visualizations

### Phase 4: Small-Scale Live Trading *(Maybe)*
- If paper trading shows promise, deploy with minimal capital ($50-100)
- Risk management and position sizing
- Continuous learning and model refinement

## Tech Stack

**Machine Learning & Data**
- Python (pandas, scikit-learn, XGBoost)
- yfinance / Alpha Vantage for market data
- PostgreSQL for trade/performance logging

**Trading Execution**
- Alpaca API for paper/live trading

**Dashboard** *(Planned)*
- Backend: FastAPI/Flask
- Frontend: React/Next.js
- Deployment: Vercel + Railway/Render

## Project Constraints

- **Time**: ~10 hours/week development
- **Timeline**: 4-6 month initial build
- **Scope**: Starting with 2-3 liquid ETFs (SPY, QQQ, IWM)
- **Strategy**: Swing trading only (day trading may be added later)

## Current Status

🔄 **Phase 1 - Data Collection & Feature Engineering**

- [ ] Historical data pipeline
- [ ] Technical indicator calculations
- [ ] First baseline model
- [ ] Backtesting framework
- [ ] Model evaluation and iteration

## Why This Project?

Stock market prediction is notoriously difficult, which makes it a perfect learning challenge:
- Immediate feedback loops (did the prediction work?)
- Real constraints (API limits, market hours, data quality)
- Multi-disciplinary (ML + software engineering + domain knowledge)
- Practical application of theoretical concepts

## Realistic Expectations

- 📉 The model probably won't beat buy-and-hold SPY
- 🎯 Markets are hard to predict, especially short-term movements
- 🔧 Most value is in the learning process, not the returns
- 📚 Expect lots of iteration, failed experiments, and debugging

## Future Enhancements

- Deep learning models (LSTM, Transformers)
- Sentiment analysis from news/social media
- Day trading module
- Multi-asset support (options, crypto)
- Advanced risk management

---

**Disclaimer**: This is an educational project. Do not use this for actual trading without understanding the risks. Past performance does not guarantee future results.

---