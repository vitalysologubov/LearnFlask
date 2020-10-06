import locale
import platform
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

from webapp.db import db
from webapp.news.models import News
from webapp.news.parsers.utils import get_html, save_news


if platform.system() == 'Windows':
    locale.setlocale(locale.LC_ALL, 'russian')
else:
    locale.setlocale(locale.LC_TIME, 'ru_RU')


def parse_news_date(date):
    """Парсинг даты публикации"""

    if 'сегодня' in date:
        today = datetime.now()
        date = date.replace('сегодня', today.strftime('%d %B %Y'))
    elif 'вчера' in date:
        yesterday = datetime.now() - timedelta(days=1)
        date = date.replace('вчера', yesterday.strftime('%d %B %Y'))

    try:
        return datetime.strptime(date, '%d %B %Y в %H:%M')
    except ValueError:
        return datetime.now()


def get_news_snippets():
    """Получение сниппетов"""

    html = get_html('https://habr.com/ru/search/?target_type=posts&q=Python&order_by=date')

    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_news = soup.find('ul', class_='content-list_posts').findAll('li', class_='content-list__item_post')

        for news in all_news:
            title = news.find('a', class_='post__title_link').text
            url = news.find('a', class_='post__title_link')['href']
            published = news.find('span', class_='post__time').text
            published = parse_news_date(published)

            save_news(title, url, published)


def get_news_content():
    """Получение содержания"""

    news_without_text = News.query.filter(News.text.is_(None))

    for news in news_without_text:
        html = get_html(news.url)

        if html:
            soup = BeautifulSoup(html, 'html.parser')
            article = soup.find('div', class_='post__text').decode_contents()

            if article:
                news.text = article
                db.session.add(news)
                db.session.commit()
