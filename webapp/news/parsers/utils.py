import requests
from flask import current_app

from webapp.db import db
from webapp.news.models import News


def get_html(url):
    """Получение html"""

    headers = {'User-Agent': current_app.config['USER_AGENT']}

    try:
        result = requests.get(url, headers=headers)
        result.raise_for_status()

        return result.text
    except (requests.RequestException, ValueError) as error:
        print(f'Ошибка получения html: {error}.')
        return False


def save_news(title, url, published):
    """Сохранение новостей в БД"""

    news_exists = News.query.filter(News.url == url).count()

    if not news_exists:
        news = News(title=title, url=url, published=published)
        db.session.add(news)
        db.session.commit()
