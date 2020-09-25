from flask import Flask, render_template
from webapp.python_news import get_python_news
from webapp.weather import weather_by_city


def create_app():
    """Создание приложения"""

    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    @app.route('/')
    def index():
        """Отображение погоды"""

        title = 'Python новости'
        weather = weather_by_city(app.config['WEATHER_DEFAULT_CITY'])
        news = get_python_news()

        return render_template('index.html', title=title, news=news, weather=weather)

    return app
