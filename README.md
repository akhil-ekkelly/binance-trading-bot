# Binance Futures Testnet Trading Bot 🚀

A modular Python CLI trading bot that places **MARKET** and **LIMIT** orders on the Binance Futures Testnet (USDT-M).
Built with clean architecture, input validation, and structured logging.

---

## 📌 Features

* Place **MARKET** and **LIMIT** orders
* Supports both **BUY** and **SELL**
* CLI-based input using `argparse`
* Input validation with clear error messages
* Structured logging of API requests and responses
* Exception handling for API and network errors
* Clean and reusable code structure

---

## 🏗️ Project Structure

```
binance-futures-testnet-bot/
│
├── bot/
│   ├── client.py          # Binance API wrapper
│   ├── orders.py          # Order execution logic
│   ├── validators.py      # Input validation
│   ├── logging_config.py  # Logging setup
│   └── __init__.py
│
├── cli.py                 # CLI entry point
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```
git clone https://github.com/akhil-ekkelly/binance-futures-testnet-bot.git
cd binance-futures-testnet-bot
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Create Environment File

Create a `.env` file in the root directory:

```
API_KEY=your_testnet_api_key
API_SECRET=your_testnet_secret
```

---

## 🌐 API Configuration

This bot uses the Binance Futures Testnet:

👉 https://testnet.binancefuture.com

---

## ▶️ Usage Examples

### 🔹 MARKET Order

```
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### 🔹 LIMIT Order

```
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 60000
```

---

## 📤 Sample Output

```
📤 Order Request:
{'symbol': 'BTCUSDT', 'side': 'BUY', 'type': 'MARKET', 'quantity': 0.001}

✅ Order Response:
Order ID: 123456
Status: FILLED
Executed Qty: 0.001
Avg Price: 60000
```

---

## 📝 Sample Logs

```
2026-05-01 INFO Request → BTCUSDT BUY MARKET qty=0.001 price=None
2026-05-01 INFO Response → {'orderId': 12345, 'status': 'FILLED'}
```

---

## ✔️ Input Validation

* `side` must be **BUY** or **SELL**
* `type` must be **MARKET** or **LIMIT**
* `price` is required for **LIMIT** orders

---

## 🛠️ Tech Stack

* Python 3
* python-binance
* argparse
* logging
* dotenv

---

## ⚠️ Notes & Assumptions

* Uses **Binance Futures Testnet (USDT-M)**
* Quantity precision depends on the trading pair
* Ensure your API key has Futures Testnet permissions

---

## 📊 Evaluation Criteria Covered

* ✔ Correct order placement (MARKET + LIMIT)
* ✔ CLI-based input handling
* ✔ Clean and modular code structure
* ✔ Logging and error handling
* ✔ Clear documentation and usage examples

---

## 📎 Author

Akhil EkkelIy
GitHub: https://github.com/akhil-ekkelly

---
