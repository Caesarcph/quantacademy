"""Create local sample datasets for QuantAcademy.

This keeps Quick Start reproducible without external API keys.
"""

from __future__ import annotations

import csv
from datetime import date, timedelta
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MARKET_DIR = ROOT / "data" / "market_data"
NEWS_DIR = ROOT / "data" / "news_data"
USER_DIR = ROOT / "data" / "user_data"


def _ensure_dirs() -> None:
    for p in (MARKET_DIR, NEWS_DIR, USER_DIR):
        p.mkdir(parents=True, exist_ok=True)


def _write_market_csv() -> Path:
    out = MARKET_DIR / "aapl_sample_daily.csv"
    start = date.today() - timedelta(days=9)
    rows = []
    close = 185.0
    for i in range(10):
        day = start + timedelta(days=i)
        close += (-1) ** i * 0.8
        rows.append(
            {
                "date": day.isoformat(),
                "open": f"{close - 0.5:.2f}",
                "high": f"{close + 1.0:.2f}",
                "low": f"{close - 1.2:.2f}",
                "close": f"{close:.2f}",
                "volume": str(95000000 + i * 120000),
            }
        )

    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    return out


def _write_news_csv() -> Path:
    out = NEWS_DIR / "sample_finance_news.csv"
    rows = [
        {"date": date.today().isoformat(), "title": "Fed keeps rates unchanged", "sentiment": "neutral"},
        {"date": (date.today() - timedelta(days=1)).isoformat(), "title": "Tech stocks rally on earnings", "sentiment": "positive"},
        {"date": (date.today() - timedelta(days=2)).isoformat(), "title": "Oil volatility pressures markets", "sentiment": "negative"},
    ]
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["date", "title", "sentiment"])
        w.writeheader()
        w.writerows(rows)
    return out


def main() -> None:
    _ensure_dirs()
    market = _write_market_csv()
    news = _write_news_csv()
    print("Sample data ready:")
    print(f"- {market}")
    print(f"- {news}")


if __name__ == "__main__":
    main()
