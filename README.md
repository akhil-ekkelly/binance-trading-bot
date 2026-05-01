# Binance Futures Testnet Trading Bot 🚀

A simple Python CLI trading bot to place MARKET and LIMIT orders on Binance Futures Testnet.

## Features
- MARKET and LIMIT orders
- BUY and SELL support
- CLI input validation
- Logging to file
- Error handling

## Setup

1. Install dependencies:
   pip install -r requirements.txt

2. Create a `.env` file:
   API_KEY=your_key
   API_SECRET=your_secret

3. Run examples:

### MARKET Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

### LIMIT Order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000

## Logs
Logs are stored in:
logs/trading_bot.log

## Assumptions
- Uses Binance Futures Testnet
- Quantity precision depends on symbol
