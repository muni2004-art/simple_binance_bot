# Simple Binance Futures Testnet Trading Bot

This is a **single-file** Python project for the Binance USDT-M Futures **testnet**.

It supports:
- Market orders (BUY / SELL)
- Limit orders (BUY / SELL)
- Command-line input (interactive)
- Logging of all actions and errors to `bot.log`

## Setup

1. Install Python 3.10+.
2. Open a terminal in this folder.
3. (Optional but recommended) Create & activate a virtual environment:

   bash
   python -m venv venv

   # Windows:
   venv\Scripts\activate


4. # Now Install dependencies:

   bash
   ------ pip install -r requirements.txt
   

5. Copy `.env.example` to `.env` and put your **Binance Futures Testnet** API key and secret:

   ini
   BINANCE_API_KEY=your_testnet_api_key_here
   BINANCE_API_SECRET=your_testnet_secret_here
   

6. Run the bot:

   bash
   python bot.py
   

Follow the prompts to choose symbol, side (BUY/SELL), order type (MARKET/LIMIT),
quantity, and (for LIMIT) price.

All logs will be stored in `bot.log`.


what i got after ecxecution #  python bot.py

=== Binance Futures Testnet Bot ===
All actions will be logged to bot.log

Enter symbol (e.g., BTCUSDT): btcusdt
Enter side (BUY/SELL): buy
Enter order type (MARKET/LIMIT): market
Enter quantity: 0.01

❌ Error placing order: APIError(code=-1021): Timestamp for this request was 1000ms ahead of the server's time.

 why i got this error Sometimes the Binance Testnet gives the error APIError(code=-1021).
This happens when the  computer's time is a little ahead of Binance’s server time.
It’s a common issue on Windows computers and is not caused by the bot itself.

The bot works normally on any system where the clock is properly synced with internet time but i am system time configurstion is matched with binance testnet
