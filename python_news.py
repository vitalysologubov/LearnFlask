import requests
from bs4 import BeautifulSoup


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
        result = []

        for news in all_news:
            title = news.find('a').text
            url = news.find('a')['href']
            published = news.find('time').text

            result.append({
                'title': title,
                'url': url,
                'published': published
            })

        return result

    return False
