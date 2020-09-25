from flask import Flask, render_template
from webapp.model import db, News
from webapp.weather import weather_by_city


def create_app():
    """Создание приложения"""

    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    def index():
        """Отображение погоды"""

        title = 'Python новости'
        weather = weather_by_city(app.config['WEATHER_DEFAULT_CITY'])
        news = News.query.order_by(News.published.desc()).all()
        return render_template('index.html', title=title, news=news, weather=weather)

    return app
