import requests
from bs4 import BeautifulSoup
from datetime import datetime
from webapp.model import db, News


def get_html(url):
    """Получение html"""

    try:
        result = requests.get(url)
        result.raise_for_status()

        return result.text
    except (requests.RequestException, ValueError) as error:
        print(f'Ошибка получения html: {error}.')
        return False


def get_python_news():
    """Получение раздела новостей из hmtl"""

    html = get_html('https://www.python.org/blogs')

    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_news = soup.find('ul', class_='list-recent-posts').findAll('li')

        for news in all_news:
            title = news.find('a').text
            url = news.find('a')['href']
            published = news.find('time').text.lower().replace('sept', 'sep')

            try:
                published = datetime.strptime(published, '%b. %d, %Y')
            except ValueError as error:
                published = datetime.now()

            save_python_news(title, url, published)


def save_python_news(title, url, published):
    """Сохранение новостей в БД"""

    news_exists = News.query.filter(News.url == url).count()

    if not news_exists:
        news = News(title=title, url=url, published=published)
        db.session.add(news)
        db.session.commit()
