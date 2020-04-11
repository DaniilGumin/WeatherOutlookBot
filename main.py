import logging
import os

from telegram.ext import Filters, MessageHandler
from telegram.ext import Updater

logging.basicConfig(filename='events.log', level=logging.INFO, format='%(asctime)s %(message)s')

TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN_WEATHER_FORECAST_BOT')
WEATHER_API_KEY = os.environ.get('WEATHER_API_KEY')
PROXY_URL = os.environ.get('PROXY_URL')

REQUEST_KWARGS = {}
if PROXY_URL is not None:
    REQUEST_KWARGS['proxy_url'] = PROXY_URL

updater = Updater(TELEGRAM_TOKEN, use_context=True, request_kwargs=REQUEST_KWARGS)
dispatcher = updater.dispatcher


def on_message_received(update, context):
    chat_id = update.message.chat_id
    message_text = update.message.text
    updater.bot.send_message(chat_id=chat_id, text=message_text)


dispatcher.add_handler(MessageHandler(Filters.text, on_message_received))
updater.start_polling()
logging.info('Bot started')
