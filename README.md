# bitcoin-price-tracker

A minimal, extensible Bitcoin price tracker with a clean CLI, optional alerts, simple ASCII charts, Docker support, and GitHub Actions CI. Default data source: CoinGecko (no API key required).

## Features
- Fetch current BTC spot price (default: USD) from CoinGecko.
- Show 24h change, high/low, and last updated timestamp.
- Render a tiny ASCII sparkline from the last 24h.
- Threshold alerts (exit code and optional command hook).
- Pluggable data source layer to add other exchanges/APIs later.

## Quickstart
```
# Python 3.10+
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m src.btc_tracker.cli --help

# One‑liners
python -m src.btc_tracker.cli price --vs USD
python -m src.btc_tracker.cli watch --vs BRL --interval 15 --times 20
python -m src.btc_tracker.cli price --vs USD --alert-below 55000
```

## Project layout
```
.
├── .github
│   └── workflows
│       └── ci.yml
├── .gitignore
├── Dockerfile
├── LICENSE
├── Makefile
├── README.md
├── requirements.txt
├── setup.cfg
├── src
│   └── btc_tracker
│       ├── __init__.py
│       ├── api.py
│       ├── ascii.py
│       ├── cli.py
│       └── utils.py
└── tests
    └── test_api.py
```

## Usage
```
# Current price
python -m src.btc_tracker.cli price --vs USD

# Watch mode (pull price repeatedly)
python -m src.btc_tracker.cli watch --vs USD --interval 10 --times 12

# Alerts
python -m src.btc_tracker.cli price --vs USD --alert-above 70000
python -m src.btc_tracker.cli price --vs USD --alert-below 55000 --on-alert "echo 'Alert fired'"
```

## Configuration
- Default data provider: CoinGecko.
- Environment variables (optional):
  - `HTTP_TIMEOUT` (seconds, default 10)
