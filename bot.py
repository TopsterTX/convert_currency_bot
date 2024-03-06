# create Telegram bot
import os
import telebot
from dotenv import load_dotenv
from parser import get_currency

# load .env file
load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)


# create convert bot command
@bot.message_handler(commands=['convert'])
def hello(message):
    try:
        denomination = message.text.split()[1]
        currency_code = message.text.split()[2].upper()

        rate = get_currency(currency_code)
        value = float(rate) * float(denomination)
        return bot.send_message(message.chat.id, round(value, 2))
    except IndexError:
        return bot.send_message(message.chat.id, 'Введите сумму и\или код валюты')

bot.infinity_polling()
