from flask import Flask
from weather import weather_by_city


app = Flask(__name__)


@app.route('/')
def index():
    """Отображение погоды"""

    city_weather = weather_by_city('Saint Petersburg, Russia')

    if city_weather:
        return (
            f'Привет! Погода в Санкт-Петербурге: {city_weather["temp_C"]}°, по ощущениям: '
            f'{city_weather["FeelsLikeC"]}°.'
        )
    else:
        return 'Сервис погоды времено недоступен'


if __name__ == "__main__":
    """Вызов приложения"""

    app.run()
