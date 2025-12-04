import os
import logging
from dotenv import load_dotenv
from binance import Client

# basic logging setup
logging.basicConfig(
    filename="bot.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

# simple helper message in log
logging.info("Starting the trading bot file...")


class SimpleFuturesBot:
    def __init__(self):
        """
        Basic setup for connecting to Binance Futures Testnet.
        Uses .env file for API key and secret.
        """
        load_dotenv()

        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")

        if not api_key or not api_secret:
            raise Exception("API keys are missing. Please check your .env file.")

        # create client in testnet mode
        self.client = Client(api_key, api_secret, testnet=True)

        # testnet futures endpoint (important)
        self.client.API_URL = "https://testnet.binancefuture.com"
        self.client.FUTURES_API_URL = "https://testnet.binancefuture.com"

        # let Binance handle time instead of Windows system
        self.client.use_server_time = True

        logging.info("Client initialized for Binance Testnet Futures")

    # basic market order function
    def place_market(self, symbol, side, qty):
        try:
            logging.info(f"Trying market order: {symbol}, {side}, qty={qty}")
            resp = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=qty,
                recvWindow=60000,  # give more time buffer
            )
            return resp
        except Exception as e:
            logging.error(f"Market order failed: {e}")
            raise

    # basic limit order function
    def place_limit(self, symbol, side, qty, price):
        try:
            logging.info(f"Trying limit order: {symbol}, {side}, qty={qty}, price={price}")
            resp = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                timeInForce="GTC",
                quantity=qty,
                price=price,
                recvWindow=60000,
            )
            return resp
        except Exception as e:
            logging.error(f"Limit order failed: {e}")
            raise


def get_float(msg):
    while True:
        try:
            v = float(input(msg))
            if v > 0:
                return v
        except:
            pass
        print("Please enter a valid number.")


def main():
    print("=== Binance Futures Testnet Bot ===")
    print("All logs will be saved in bot.log\n")

    try:
        bot = SimpleFuturesBot()
    except Exception as e:
        print("Error initializing bot:", e)
        return

    # take inputs
    sym = input("Symbol (e.g., BTCUSDT): ").upper()
    side = input("Side (BUY/SELL): ").upper()

    if side not in ["BUY", "SELL"]:
        print("Invalid side. Only BUY or SELL allowed.")
        return

    otype = input("Order type (MARKET or LIMIT): ").upper()
    qty = get_float("Quantity: ")

    try:
        if otype == "MARKET":
            order = bot.place_market(sym, side, qty)
        elif otype == "LIMIT":
            price = get_float("Limit Price: ")
            order = bot.place_limit(sym, side, qty, price)
        else:
            print("Invalid order type.")
            return

        print("\nOrder Response:")
        print("Status:", order.get("status"))
        print("Order ID:", order.get("orderId"))
        print("Client ID:", order.get("clientOrderId"))

    except Exception as e:
        print("Error placing order:", e)


if __name__ == "__main__":
    main()
