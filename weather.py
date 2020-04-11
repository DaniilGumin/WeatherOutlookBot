def create_forecast_message(observation) -> str:
    location = observation.get_location()
    city = location.get_name()
    country = location.get_country()
    weather_forecast = observation.get_weather()
    temperatures = weather_forecast.get_temperature(unit='celsius')
    temperature = temperatures['temp']
    feels_like = temperatures['feels_like']
    speed_of_wind = weather_forecast.get_wind()['speed']
    weather_description = weather_forecast.get_detailed_status()
    clouds_percent = weather_forecast.get_clouds()
    forecast_message = '{0}, {1}\
                        \n🌡 {2}°С, по ощущениям {3}°С \
                        \n{4}\
                        \nВетер {5}м/c\
                        \nОблака: {6} % ' \
        .format(city,
                country,
                temperature,
                feels_like,
                weather_description,
                speed_of_wind,
                clouds_percent)
    return forecast_message
