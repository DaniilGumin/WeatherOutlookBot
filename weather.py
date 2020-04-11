def create_forecast_message(observation) -> str:
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
    forecast_message = '{0}, {1}\
                        \n🌡 {2}°С, по ощущениям {3}°С \
                        \n{4} {5}\
                        \nВетер {6}м/c\
                        \nОблака: {7} % ' \
        .format(city,
                country,
                temperature,
                feels_like,
                emoji,
                weather_description,
                speed_of_wind,
                clouds_percent)
    return forecast_message


def get_emoji_by_icon_name(icon_name):
    emoji = ''
    if icon_name == '01d':
        emoji = '☀️'
    elif icon_name == '01n':
        emoji = '🌑'
    elif icon_name.startswith('02'):
        emoji = '🌤'
    elif icon_name.startswith('03'):
        emoji = '☁️'
    elif icon_name.startswith('04'):
        emoji = '☁️☁️'
    elif icon_name.startswith('09'):
        emoji = '🌧'
    elif icon_name.startswith('10'):
        emoji = '🌦'
    elif icon_name.startswith('11'):
        emoji = '🌩'
    elif icon_name.startswith('13'):
        emoji = '❄️'
    elif icon_name.startswith('50'):
        emoji = '🌫'
    return emoji
