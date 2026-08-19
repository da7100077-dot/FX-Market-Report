# FX Market Report Telegram Bot

Educational forex bot with live exchange rates and educational articles.

## Quick Start

1. Create a `.env` file with your `BOT_TOKEN` (see `.env.example`).
2. Install dependencies: `pip install -r requirements.txt`
3. Run: `python main.py`

The bot will run in polling mode and also serve a health check on `PORT`.

## Deploy on Railway

1. Push this repository to GitHub.
2. On Railway, create a new project from your repo.
3. Add the environment variable `BOT_TOKEN` (only required).
4. Railway will start the bot – it will automatically use polling and health checks.

## Commands

- `/start` – show main menu
- `/help` – get help
- `/market` – show market overview
- `/pairs` – view currency pairs
- `/education` – learn about forex
- `/about` – about this bot
- `/disclaimer` – legal disclaimer

## Notes

- No webhook configuration needed – the bot uses polling by default.
- The Economic Calendar button is a placeholder; you can add an Alpha Vantage API key later if desired.
- Exchange rates are fetched from the free Frankfurter API (no key required).
