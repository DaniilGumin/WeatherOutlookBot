import logging
import os

import pyowm
from pyowm.exceptions.api_response_error import NotFoundError
from telegram.ext import Filters, MessageHandler, CommandHandler, CallbackQueryHandler
from telegram.ext import Updater

from Services import weather, keyboard
from Database.IDatabase import IDatabase
from Database.SqliteDatabase import SqliteDatabase

logging.basicConfig(filename='events.log', level=logging.INFO, format='%(asctime)s %(message)s')

WEATHER_API_KEY = os.environ.get('WEATHER_API_KEY')
owm = pyowm.OWM(WEATHER_API_KEY)
owm.set_language('ru')

PROXY_URL = os.environ.get('PROXY_URL')
REQUEST_KWARGS = {}
if PROXY_URL is not None:
    REQUEST_KWARGS['proxy_url'] = PROXY_URL

TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN_WEATHER_FORECAST_BOT')
updater = Updater(TELEGRAM_TOKEN, use_context=True, request_kwargs=REQUEST_KWARGS)
DATABASE: IDatabase = SqliteDatabase()
dispatcher = updater.dispatcher


def start(update, context):
    chat_id = update.message.chat_id
    greeting_text = 'Привет! Я подскажу тебе прогноз погоды и помогу выбрать, что надеть!\n\
🌇 Введи название города или отправь геолокацию.\n\n\
Иногда названия городов совпадают, поэтому я рекомендую использовать геолокацию.\
Если нет возможности отправить геолокацию, можно сделать поиск по названию точнее. \
Для этого после названия города через запятую укажи страну, например: Москва, RU'
    updater.bot.send_message(chat_id=chat_id, text=greeting_text)


def on_message_received(update, context):
    chat_id = update.message.chat_id
    city_name = update.message.text
    try:
        forecast_message = on_city_name_received(city_name)
        DATABASE.save_last_city_for_user(chat_id, city_name)
        markup = keyboard.create_markup(city_name)
    except NotFoundError:
        forecast_message = 'Город не найден 👀 \nПопробуй поискать по геолокации'
        markup = None
    updater.bot.send_message(chat_id=chat_id, text=forecast_message, reply_markup=markup)


def on_city_name_received(city_name: str) -> str:
    observation = owm.weather_at_place(city_name)
    forecast_message = weather.create_forecast_message(observation)
    return forecast_message


def on_location_received(update, context):
    chat_id = update.message.chat_id
    location = update.message.location
    forecast_message = on_city_location_received(location)
    city_name = owm.weather_at_coords(location.latitude, location.longitude).get_location().get_name()
    DATABASE.save_last_city_for_user(chat_id, city_name)
    markup = keyboard.create_markup(city_name)
    updater.bot.send_message(chat_id=chat_id, text=forecast_message, reply_markup=markup)


def on_city_location_received(location):
    observation = owm.weather_at_coords(location.latitude, location.longitude)
    forecast_message = weather.create_forecast_message(observation)
    return forecast_message


start_handler = CommandHandler('start', start)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(MessageHandler(Filters.text, on_message_received))
dispatcher.add_handler(MessageHandler(Filters.location, on_location_received))

updater.start_polling()
logging.info('Bot started')
