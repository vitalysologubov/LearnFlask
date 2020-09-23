from flask import Flask, render_template
from python_news import get_python_news
from weather import weather_by_city


app = Flask(__name__)


@app.route('/')
def index():
    """Отображение погоды"""

    title = 'Python новости'
    weather = weather_by_city('Saint Petersburg, Russia')
    news = get_python_news()

    return render_template('index.html', title=title, news=news, weather=weather)


if __name__ == '__main__':
    """Вызов приложения"""

    app.run()
