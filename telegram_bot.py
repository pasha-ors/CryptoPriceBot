import telebot
import time

from scraper import get_crypto_prices

TELEGRAM_BOT_TOKEN = ""
CHAT_ID = ""

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)


def send_price_report():
    while True:
        prices = get_crypto_prices()

        if not prices:
            bot.send_message(CHAT_ID, "❌ Failed to retrieve cryptocurrency data!")
        else:
            message = "📊 *Current Cryptocurrency Prices:*\n"

            for name, price in prices.items():
                message += f"🔹 {name}: *{price}*\n"

            bot.send_message(CHAT_ID, message, parse_mode="Markdown")

        time.sleep(30)


if __name__ == "__main__":
    send_price_report()

