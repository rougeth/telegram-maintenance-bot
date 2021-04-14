import os
import sys

import telebot


if not (TELEGRAM_TOKEN := os.environ.get("TELEGRAM_TOKEN")):
    print(
        "You must specify a token of Telegram Bot API. Use the TELEGRAM_TOKEN "
        "environment variable or pass it as an argument to the script."
    )
    exit(1)

MAITENANCE_MESSAGE = os.environ.get(
    "MAITENANCE_MESSAGE",
    "⚠️ I'm in *Maintenance Mode*. Please come back later."
)


bot = telebot.TeleBot(TELEGRAM_TOKEN, parse_mode="markdown")

@bot.message_handler(func=lambda message: True)
def maintenance_bot(message):
    bot.send_message(message.chat.id, MAITENANCE_MESSAGE)


bot.polling()
