import logging
import os

import pyowm
from telegram.ext import Filters, MessageHandler
from telegram.ext import Updater

import weather

logging.basicConfig(filename='events.log', level=logging.INFO, format='%(asctime)s %(message)s')

WEATHER_API_KEY = os.environ.get('WEATHER_API_KEY')
owm = pyowm.OWM(WEATHER_API_KEY)
owm.set_language("ru")

PROXY_URL = os.environ.get('PROXY_URL')
REQUEST_KWARGS = {}
if PROXY_URL is not None:
    REQUEST_KWARGS['proxy_url'] = PROXY_URL

TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN_WEATHER_FORECAST_BOT')
updater = Updater(TELEGRAM_TOKEN, use_context=True, request_kwargs=REQUEST_KWARGS)
dispatcher = updater.dispatcher


def on_message_received(update, context):
    chat_id = update.message.chat_id
    city_name = update.message.text
    forecast_message = on_city_name_received(city_name)
    updater.bot.send_message(chat_id=chat_id, text=forecast_message)


def on_city_name_received(city_name):
    observation = owm.weather_at_place(city_name)
    forecast_message = weather.create_forecast_message(observation)
    return forecast_message


def on_location_received(update, context):
    chat_id = update.message.chat_id
    location = update.message.location
    forecast_message = on_city_location_received(location)
    updater.bot.send_message(chat_id=chat_id, text=forecast_message)


def on_city_location_received(location):
    observation = owm.weather_at_coords(location.latitude, location.longitude)
    forecast_message = weather.create_forecast_message(observation)
    return forecast_message


dispatcher.add_handler(MessageHandler(Filters.text, on_message_received))
dispatcher.add_handler(MessageHandler(Filters.location, on_location_received))

updater.start_polling()
logging.info('Bot started')
