# 🎓 QuantAcademy

> Interactive quantitative finance learning platform with hands-on coding exercises, live market simulations, and progressive curriculum from basics to LLM-powered trading.

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30+-red.svg)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 🎯 Why This Project?

Most quant learning resources are either:
- **Too theoretical**: Heavy on math, light on implementation
- **Too fragmented**: YouTube videos and blog posts without structure
- **Outdated**: Don't cover modern approaches like LLM integration

**QuantAcademy bridges this gap** with a structured, hands-on curriculum that takes you from basic indicators to cutting-edge AI trading strategies.

## ✨ Features

### 📚 Progressive Curriculum
- **10 Modules**: From Python basics to multi-agent systems
- **50+ Interactive Lessons**: Jupyter notebooks with embedded exercises
- **Real Market Data**: Practice with actual historical data
- **Instant Feedback**: Automated grading and hints

### 🎮 Interactive Sandbox
- **Paper Trading Simulator**: Test strategies with fake money, real data
- **Strategy Playground**: Drag-and-drop strategy builder
- **Backtesting Arena**: Compare your strategy against benchmarks
- **LLM Lab**: Experiment with GPT/Claude for market analysis

### 🏆 Gamification
- **Achievement System**: Earn badges for milestones
- **Leaderboards**: Weekly paper trading competitions
- **Projects**: Real-world capstone projects with peer review
- **Certificates**: Completion certificates for LinkedIn

## 📖 Curriculum Overview

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
├── curriculum/
│   ├── module_01_python_foundations/
│   │   ├── lesson_01_numpy_pandas/
│   │   │   ├── lesson.ipynb         # Interactive lesson
│   │   │   ├── exercises.ipynb      # Practice problems
│   │   │   ├── solutions.ipynb      # Reference solutions
│   │   │   └── quiz.yaml            # Auto-graded quiz
│   │   └── ...
│   ├── module_02_technical_analysis/
│   └── ...
├── sandbox/
│   ├── paper_trading/               # Paper trading simulator
│   ├── strategy_builder/            # Visual strategy builder
│   ├── backtest_arena/              # Backtesting environment
│   └── llm_lab/                     # LLM experimentation
├── platform/
│   ├── app.py                       # Main Streamlit app
│   ├── components/
│   │   ├── lesson_viewer.py
│   │   ├── code_editor.py
│   │   ├── chart_widget.py
│   │   └── quiz_component.py
│   ├── auth/                        # User authentication
│   ├── progress/                    # Progress tracking
│   └── gamification/                # Achievements, leaderboards
├── data/
│   ├── market_data/                 # Historical data
│   ├── news_data/                   # Sample news datasets
│   └── user_data/                   # User progress (local)
├── grading/
│   ├── autograder.py                # Exercise grading
│   └── rubrics/                     # Grading criteria
├── tests/
└── docs/
```

## 🚀 Quick Start

### Local Installation

```bash
# Clone repository
git clone https://github.com/Caesarcph/quantacademy.git
cd quantacademy

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Download sample data
python scripts/download_data.py

# Launch platform
streamlit run platform/app.py
```

### Docker

```bash
docker-compose up -d
# Open http://localhost:8501
```

### Cloud Deployment

```bash
# Deploy to Streamlit Cloud (free)
# 1. Fork this repo
# 2. Go to share.streamlit.io
# 3. Deploy from your fork
```

## 📸 Screenshots

### Lesson View
```
┌─────────────────────────────────────────────────────────────┐
│ Module 2: Technical Analysis > Lesson 2.2: Trend Indicators │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ## Moving Averages                                         │
│                                                             │
│  A moving average smooths price data by creating a          │
│  constantly updated average price...                        │
│                                                             │
│  [Interactive Chart: AAPL with 20/50 SMA]                   │
│                                                             │
│  ### Try It Yourself                                        │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ # Calculate 20-day SMA for the 'close' column       │   │
│  │ sma_20 = df['close'].rolling(___).mean()            │   │
│  │                                                     │   │
│  │ [Run Code]  [Hint]  [Solution]                      │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ✅ Exercise 1/5 Complete    [Next Exercise →]              │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│ Progress: ████████░░ 80%    ⭐ 450 XP    🏆 3 Badges         │
└─────────────────────────────────────────────────────────────┘
```

### Paper Trading Simulator
```
┌─────────────────────────────────────────────────────────────┐
│               Paper Trading Simulator                        │
├─────────────────────────────────────────────────────────────┤
│ Portfolio Value: $107,234.56 (+7.23%)                       │
│                                                             │
│ [AAPL Chart with Entry/Exit Points]                         │
│                                                             │
│ Open Positions:                                             │
│ ┌────────────────────────────────────────────────────────┐ │
│ │ AAPL   100 shares  @ $178.50   P&L: +$234.00 (+1.3%)  │ │
│ │ GOOGL   50 shares  @ $142.30   P&L: -$45.00 (-0.6%)   │ │
│ └────────────────────────────────────────────────────────┘ │
│                                                             │
│ Quick Trade: [AAPL ▼] [100] [BUY] [SELL]                    │
│                                                             │
│ Strategy Running: SMA Crossover ✅                          │
│ Next Signal Check: 14:30:00                                 │
└─────────────────────────────────────────────────────────────┘
```

## 🎮 Gamification System

### Achievements

| Badge | Name | Requirement |
|-------|------|-------------|
| 🌱 | First Steps | Complete Module 1 |
| 📊 | Chart Master | Pass all Technical Analysis quizzes |
| 🔬 | Data Scientist | Complete ML module with 90%+ |
| 🤖 | AI Trader | Build your first LLM strategy |
| 💎 | Consistent | 30-day learning streak |
| 🏆 | Top Trader | Weekly paper trading top 10 |

### XP System

| Action | XP |
|--------|-----|
| Complete Lesson | +50 |
| Pass Quiz (>80%) | +100 |
| Complete Project | +500 |
| Weekly Trading Challenge | +200 |
| Help in Community | +25 |

## 🛠️ Development Roadmap

### Phase 1: Core Platform (Weeks 1-4)
- [ ] Streamlit application scaffold
- [ ] Lesson viewer with Jupyter integration
- [ ] Code editor with execution sandbox
- [ ] Progress tracking system
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
- [ ] Achievement system
- [ ] Leaderboards
- [ ] Discussion forums
- [ ] Peer review for projects

### Phase 6: Polish & Launch (Weeks 23-24)
- [ ] Performance optimization
- [ ] Mobile responsiveness
- [ ] Documentation
- [ ] Public launch

## 💡 Sample Lesson: LLM Trading Agent

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

MIT License - Educational use encouraged!

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io)
- Financial data from [Yahoo Finance](https://finance.yahoo.com)
- Inspired by Coursera, DataCamp, and QuantConnect

---

**Star ⭐ if you want to see this project come to life!**