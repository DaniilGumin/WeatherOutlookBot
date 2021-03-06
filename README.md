# Умный сервис прогноза погоды для Школы CTO Яндекс.Облака
_Сложность - задача со звездочкой_\
![alt text](https://i.imgur.com/xTjazn4.png)
## [Видео с примером работы](https://drive.google.com/file/d/1TCbTQuB8iGzzN7oitKZKSGAkZcbO7dN2/view?usp=sharing)
Бот задеплоен на [Heroku](heroku.com) и доступен в Telegram [@weather_outlook_bot](t.me/weather_outlook_bot)


## Запуск
1. Если вы живете в России, скорее всего, вам понадобится Tor, чтобы обойти блокировку Telegram. Загрузите его с [официального сайта TorProject](https://www.torproject.org/ru/download/tor/) и запустите в режиме sosks-proxy. Например, на Windows для этого достаточно запустить `tor.exe` в консоли. Установите адрес sosks-proxy в переменную окружения PROXY_URL. По умолчанию это socks5h://127.0.0.1:9050

2. [Установите Python 3.8](https://www.python.org/downloads/)

3. Клонируйте репозиторий\
`git clone https://github.com/DaniilGumin/WeatherOutlookBot.git`

4. Установите зависимости\
`pip install -r requirements.txt`
либо
`pip3 install -r requirements.txt`

5. Установите переменные окружения
* TELEGRAM_TOKEN_WEATHER_FORECAST_BOT - токен telegram-бота
* WEATHER_API_KEY - токен OpenWeatherMapAPI

6. Запустите\
`python3 main.py`

## Интерфейс
Интерфейс сервиса реализован в виде Telegram-бота.
Пользователь получает текстовый прозноз погоды, который состоит из:
* Температуры и температуры по ощущениям
* Типа погоды - ясно, облачно, дождь. Кроме текста также высылается соответствующий смайлик
* Скорости ветра
* Информации об облачности
* Рекомендации одежды. Рекомендация дается с учетом температуры, солнечной или дождливой погоды

## Технологии
При разработке бота использовался язык Python 3\
Применялись библиотеки [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) и [pyowm](https://github.com/csparpa/pyowm) (обертка над OpenWeatherMapAPI).

## Алгоритм работы
* Когда бот получает команду /start, он высылает сообщение с инструкцией по использованию. 
* Когда бот получает текстовое сообщение, он рассматривает его как название города и отправляет запрос на получение погоды в OpenWeatherMapAPI. Если OpenWeatherMapAPI сообщает, что такого города нет, пользователю предлагается уточнить запрос или отправить геолокацию города. Если город найден, пользователю высылается прозноз погоды. 
* Когда бот получает сообщение с геолокацией, отправляется запрос в OpenWeatherMapAPI на получение прогноза погоды по координатам. Пользователю высылается сообщение с прогнозом погоды.
