# 🎓 QuantAcademy

> Interactive quantitative finance learning platform (early MVP). The goal: hands-on coding exercises, market simulations, and a progressive curriculum from basics to LLM-powered trading.

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-red.svg)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 📌 Status

**Early MVP: a Streamlit shell with local progress tracking. No lesson content exists yet.**

What works today:
- A Streamlit app (`platform/app.py`) with a sidebar listing the 10 planned modules plus "Paper Trading" and "Strategy Builder" pages.
  All of these pages are placeholders ("under development").
- On each module page you can click **Mark module complete** to earn 100 XP.
- Local progress (XP, daily streak, completed modules) saved to `~/.quantacademy/progress.json`, with basic validation.
- Four basic achievement badges shown in the sidebar.
- `scripts/download_data.py` writes small **synthetic** sample CSVs (no network, no API keys). The app does not read them yet.

Everything else in this README (lessons, notebooks, exercises, auto-grading, paper trading, strategy builder,
LLM Lab, leaderboards, certificates) is **planned** and not implemented. See [ROADMAP.md](ROADMAP.md).
There are no automated tests yet.

## 🎯 Why This Project?

Most quant learning resources are either:
- **Too theoretical**: Heavy on math, light on implementation
- **Too fragmented**: YouTube videos and blog posts without structure
- **Outdated**: Don't cover modern approaches like LLM integration

**QuantAcademy aims to bridge this gap** with a structured, hands-on curriculum that takes you from basic indicators to modern AI trading strategies.

## ✨ Features

### ✅ Local Progress Tracking (MVP, implemented)
- Stores XP / streak / module completion locally in `~/.quantacademy/progress.json`
- Atomic writes; malformed or missing files fall back to a fresh state
- Designed for single-user local development; can be replaced by DB later

### ✅ Basic Achievements (MVP, implemented)
- Sidebar badges unlocked from local progress (see [Gamification System](#-gamification-system))

### 📚 Progressive Curriculum (planned)
- **10 Modules**: From Python basics to multi-agent systems (currently placeholder pages in the app)
- **49 Interactive Lessons**: Jupyter notebooks with embedded exercises (planned; see outline below)
- **Real Market Data**: Practice with actual historical data (planned; only synthetic samples today)
- **Instant Feedback**: Automated grading and hints (planned)

### 🎮 Interactive Sandbox (planned)
- **Paper Trading Simulator**: Test strategies with fake money, real data
- **Strategy Playground**: Drag-and-drop strategy builder
- **Backtesting Arena**: Compare your strategy against benchmarks
- **LLM Lab**: Experiment with GPT/Claude for market analysis

### 🏆 Gamification (planned extensions)
- **More Achievements**: Badges for quizzes, projects and trading milestones
- **Leaderboards**: Weekly paper trading competitions
- **Projects**: Real-world capstone projects with peer review
- **Certificates**: Completion certificates for LinkedIn

## 📖 Curriculum Overview (planned)

Module titles below appear as placeholder pages in the app; none of the lessons have been written yet.

```
Module 1: Python for Finance Foundations
├── 1.1 NumPy & Pandas Essentials
├── 1.2 Time Series Manipulation
├── 1.3 Financial Data APIs
└── 1.4 Project: Build Your First Data Pipeline

Module 2: Technical Analysis Fundamentals
├── 2.1 Price Action & Candlesticks
├── 2.2 Trend Indicators (MA, EMA, MACD)
├── 2.3 Momentum Indicators (RSI, Stochastic)
├── 2.4 Volatility (Bollinger, ATR)
└── 2.5 Project: Multi-Indicator Dashboard

Module 3: Statistical Analysis
├── 3.1 Returns Analysis & Distribution
├── 3.2 Correlation & Cointegration
├── 3.3 Hypothesis Testing for Strategies
└── 3.4 Project: Pairs Trading Strategy

Module 4: Backtesting Fundamentals
├── 4.1 Backtesting Architecture
├── 4.2 Common Pitfalls (Lookahead, Survivorship)
├── 4.3 Performance Metrics Deep Dive
├── 4.4 Walk-Forward Optimization
└── 4.5 Project: Build a Backtest Engine

Module 5: Risk Management
├── 5.1 Position Sizing Methods
├── 5.2 Stop Loss Strategies
├── 5.3 Portfolio Risk (VaR, CVaR)
├── 5.4 Kelly Criterion
└── 5.5 Project: Risk-Managed Portfolio

Module 6: Machine Learning for Trading
├── 6.1 Feature Engineering
├── 6.2 Classification Models
├── 6.3 Regression for Price Prediction
├── 6.4 Cross-Validation for Time Series
└── 6.5 Project: ML Signal Generator

Module 7: Deep Learning Applications
├── 7.1 LSTM for Sequence Prediction
├── 7.2 Transformer Architecture Basics
├── 7.3 Attention Mechanisms
├── 7.4 Training & Evaluation
└── 7.5 Project: Deep Learning Strategy

Module 8: Natural Language Processing
├── 8.1 Text Processing Pipeline
├── 8.2 Sentiment Analysis Basics
├── 8.3 FinBERT & Domain Models
├── 8.4 News Impact Analysis
└── 8.5 Project: News-Based Trading Bot

Module 9: LLM-Powered Trading (Advanced)
├── 9.1 LLM Fundamentals for Finance
├── 9.2 Prompt Engineering for Analysis
├── 9.3 Chain-of-Thought Reasoning
├── 9.4 Function Calling & Tool Use
├── 9.5 Building Trading Agents
└── 9.6 Project: LLM Trading Assistant

Module 10: Multi-Agent Systems (Expert)
├── 10.1 Multi-Agent Architectures
├── 10.2 Consensus Mechanisms
├── 10.3 Agent Communication Protocols
├── 10.4 Orchestration & Coordination
└── 10.5 Capstone: Multi-Agent Trading System
```

## 🏗️ Project Structure

```
quantacademy/
├── platform/
│   ├── __init__.py
│   ├── app.py                       # Main Streamlit app (navigation, placeholders, progress UI)
│   └── progress/
│       ├── __init__.py
│       └── storage.py               # JSON progress storage, streaks, XP, achievements
├── scripts/
│   └── download_data.py             # Writes synthetic sample CSVs (no download, no API keys)
├── data/
│   ├── market_data/
│   │   └── aapl_sample_daily.csv    # 10 synthetic daily bars
│   └── news_data/
│       └── sample_finance_news.csv  # 3 synthetic headlines
├── .env.example                     # Placeholder for future API keys (not read by the code yet)
├── requirements.txt                 # streamlit
├── requirements-dev.txt             # pytest, ruff, black
├── CONTRIBUTING.md
├── ROADMAP.md
└── LICENSE
```

Planned directories (not created yet): `curriculum/` (lesson notebooks, exercises, quizzes), `sandbox/`
(paper trading, strategy builder, backtest arena, LLM lab), `platform/components/`, `platform/auth/`,
`platform/gamification/`, `grading/` (autograder), `tests/`, `docs/`.

## 🚀 Quick Start

### Local Installation

```bash
# Clone repository
git clone https://github.com/Caesarcph/quantacademy.git
cd quantacademy

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
source venv/bin/activate        # On Linux/Mac
# venv\Scripts\activate         # On Windows

# Install core dependencies
pip install -r requirements.txt

# Optional: Install development dependencies (pytest, ruff, black)
pip install -r requirements-dev.txt

# Optional: environment template (no variables are used by the current code)
cp .env.example .env

# Optional: regenerate the synthetic sample data in data/ (overwrites the committed sample CSVs)
python scripts/download_data.py

# Launch the platform
streamlit run platform/app.py

# Open your browser to: http://localhost:8501
```

### Cloud Deployment (untested)

```bash
# Deploy to Streamlit Cloud (free) - not yet tried for this repo
# 1. Fork this repo
# 2. Go to share.streamlit.io
# 3. Deploy from your fork with main file path: platform/app.py
```

Docker support is planned (no `Dockerfile` / `docker-compose.yml` yet).

## 🎮 Gamification System

### Achievements

Implemented today (computed from local progress):

| Badge | Name | Requirement |
|-------|------|-------------|
| 🌱 | First Steps | Complete 1 module |
| 📚 | Halfway There | Complete 5 modules |
| 🏆 | Quant Graduate | Complete all 10 modules |
| 💎 | Consistent | 7-day learning streak |

Planned:

| Badge | Name | Requirement |
|-------|------|-------------|
| 📊 | Chart Master | Pass all Technical Analysis quizzes |
| 🔬 | Data Scientist | Complete ML module with 90%+ |
| 🤖 | AI Trader | Build your first LLM strategy |
| 🏆 | Top Trader | Weekly paper trading top 10 |

### XP System

| Action | XP | Status |
|--------|-----|--------|
| Mark module complete | +100 | Implemented (once per module) |
| Complete Lesson | +50 | Planned |
| Pass Quiz (>80%) | +100 | Planned |
| Complete Project | +500 | Planned |
| Weekly Trading Challenge | +200 | Planned |
| Help in Community | +25 | Planned |

## 🛠️ Development Roadmap

Detailed list in [ROADMAP.md](ROADMAP.md).

### Phase 1: Core Platform (Weeks 1-4)
- [x] Streamlit application scaffold
- [ ] Lesson viewer with Jupyter integration
- [ ] Code editor with execution sandbox
- [x] Progress tracking system (local JSON, single user)
- [ ] User authentication (local)

### Phase 2: Curriculum Development (Weeks 5-10)
- [ ] Modules 1-5: Fundamentals
- [ ] Interactive exercises with auto-grading
- [ ] Quiz system with randomization
- [ ] Video content integration

### Phase 3: Sandbox Features (Weeks 11-14)
- [ ] Paper trading simulator
- [ ] Real-time market data integration
- [ ] Strategy builder UI
- [ ] Backtesting environment

### Phase 4: Advanced Content (Weeks 15-18)
- [ ] Modules 6-8: ML/DL/NLP
- [ ] LLM Lab with API integration
- [ ] Module 9-10: LLM & Multi-agent

### Phase 5: Gamification & Community (Weeks 19-22)
- [x] Achievement system (basic, 4 badges)
- [ ] Leaderboards
- [ ] Discussion forums
- [ ] Peer review for projects

### Phase 6: Polish & Launch (Weeks 23-24)
- [ ] Performance optimization
- [ ] Mobile responsiveness
- [ ] Documentation
- [ ] Public launch

## 💡 Sample Lesson: LLM Trading Agent (planned)

Illustrative design sketch for Module 9.5. The `quantacademy.llm` package and `TradingAgent` class do **not** exist yet,
so this code will not run.

```python
# Module 9.5: Building Trading Agents
# Exercise: Create a simple LLM trading agent

from quantacademy.llm import TradingAgent

class MyTradingAgent(TradingAgent):
    """
    Your task: Complete the analyze_market method
    to have the LLM evaluate current market conditions.
    """
    
    def analyze_market(self, market_data: dict) -> dict:
        # TODO: Build a prompt that includes:
        # 1. Current price and recent price history
        # 2. Key technical indicators
        # 3. Recent news headlines
        
        prompt = f"""
        Analyze the following market data for {market_data['symbol']}:
        
        Current Price: ${market_data['price']:.2f}
        24h Change: {market_data['change_24h']:.2%}
        
        Technical Indicators:
        - RSI(14): {market_data['rsi']:.1f}
        - MACD: {market_data['macd']:.4f}
        - 50 SMA: ${market_data['sma_50']:.2f}
        
        Recent Headlines:
        {self.format_headlines(market_data['news'])}
        
        Based on this data, provide:
        1. Market sentiment (bullish/neutral/bearish)
        2. Confidence level (0-100)
        3. Suggested action (buy/hold/sell)
        4. Brief reasoning (2-3 sentences)
        
        Respond in JSON format.
        """
        
        response = self.llm.analyze(prompt)
        return self.parse_response(response)

# Test your agent!
agent = MyTradingAgent(model="claude-sonnet-4-20250514")
result = agent.analyze_market(sample_market_data)

# Expected output structure:
# {
#     "sentiment": "bullish",
#     "confidence": 75,
#     "action": "buy",
#     "reasoning": "RSI indicates oversold conditions..."
# }
```

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md).

### Ways to Contribute
1. **Content**: Write lessons, exercises, or quizzes
2. **Code**: Improve platform features
3. **Translation**: Help translate to other languages
4. **Testing**: Report bugs and suggest improvements

## 📄 License

[MIT License](LICENSE) - Educational use encouraged!

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io)
- Inspired by Coursera, DataCamp, and QuantConnect

---

**Star ⭐ if you want to see this project come to life!**
