def create_forecast_message(observation) -> str:
    """
    Собирает всю необходимую информацию о погоде и возвращает её в виде строки, которая
    содержит 'город', 'страну', 'температуру', 'температуру по ощущениям', 'эмодзи с погодой', 'скорость ветра'
    'процент облаков', 'одежду, которую стоит одеть'
    """
    location = observation.get_location()
    city = location.get_name()
    country = location.get_country()
    weather_forecast = observation.get_weather()
    temperatures = weather_forecast.get_temperature(unit='celsius')
    temperature = temperatures['temp']
    feels_like = temperatures['feels_like']
    speed_of_wind = weather_forecast.get_wind()['speed']
    icon_name = weather_forecast.get_weather_icon_name()
    emoji = get_emoji_by_icon_name(icon_name)
    weather_description = weather_forecast.get_detailed_status()
    clouds_percent = weather_forecast.get_clouds()
    is_raining = icon_name.startswith('09') or icon_name.startswith('10')
    is_sunny = icon_name == '01d' or icon_name.startswith('02')
    clothes = what_to_wear(feels_like, is_raining, is_sunny)
    forecast_message = f'{city}, {country}\
                        \n🌡 {temperature}°С, по ощущениям {feels_like}°С\
                        \n{emoji} {weather_description}\
                        \nВетер {speed_of_wind}м/c\
                        \nОблака: {clouds_percent} %\
                        \n{clothes}'
    return forecast_message


def get_emoji_by_icon_name(icon_name: str) -> str:
    """
    Возвращает строковое представление эмодзи на основе полученного параметра icon_name
    """
    emoji = ''
    if icon_name == '01d':
        emoji = '☀'
    elif icon_name == '01n':
        emoji = '🌑'
    elif icon_name.startswith('02'):
        emoji = '🌤'
    elif icon_name.startswith('03'):
        emoji = '☁'
    elif icon_name.startswith('04'):
        emoji = '☁️☁'
    elif icon_name.startswith('09'):
        emoji = '🌧'
    elif icon_name.startswith('10'):
        emoji = '🌦'
    elif icon_name.startswith('11'):
        emoji = '🌩'
    elif icon_name.startswith('13'):
        emoji = '❄'
    elif icon_name.startswith('50'):
        emoji = '🌫'
    return emoji


def what_to_wear(feels_like: float, is_raining: bool, is_sunny: bool) -> str:
    """
    Возвращает строку, которая содержит список вещей, которые стоит надеть, на основе полученных данных о погоде
    """
    text = 'Что надеть? '
    if feels_like < -25:
        text += 'Надевай всё, что есть!'
    elif feels_like < -20:
        text += 'Шапка-ушанка, шарф, перчатки, тёплая куртка, толстовка, утеплённые штаны, ботинки'
    elif feels_like < -10:
        text += 'Шапка-ушанка, шарф, перчатки, тёплая куртка, кофта, утеплённые штаны, ботинки'
    elif feels_like < 0:
        text += 'Шапка, шарф, куртка, брюки, ботинки'
    elif feels_like < 7:
        text += 'Шапка, ветровка, брюки или джинсы, ботинки'
    elif feels_like < 15:
        text += 'Ветровка, брюки или джинсы, кеды или кроссовки'
    elif feels_like < 20:
        text += 'Лёгкая кофта, футболка, шорты, кеды или кроссовки'
    elif feels_like < 25:
        text += 'Футболка или рубашка с коротким рукавом, шорты, кеды или кроссовки'
    elif feels_like < 35:
        text += 'Шорты, майка, сланцы🩴'
    else:
        text = 'Берегись солнечного удара 👊🌝👊'
    if is_sunny and 20 < feels_like < 35:
        text += ', кепка или панамка'
    elif is_raining:
        text += ', зонтик☂'
    return text
