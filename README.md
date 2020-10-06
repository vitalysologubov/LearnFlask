# Трек: веб-разработка

### Функционал:
1. Парсинг новостей с сайта python.org и их сохранение в базу данных.
2. Получение информации о температуре на примере города Санкт-Петербург.
3. Отображение информации с использованием фреймворка Bootstrap.
4. Добавление формы авторизации пользователя.

### Установка:
1. Клонировать репозиторий с GitHub: `git clone https://github.com/vitalysologubov/learn_flask.git`
2. Создать виртуальное окружение: `python -m venv env`
3. Установить зависимости `pip install -r requirements.txt`
4. Создать базу данных `python create_db.py`
5. Загрузить новости в базу данных `python get_news.py`
6. Создать администратора `python create_admin.py`
7. Запустить приложение: `set FLASK_APP=webapp && flask run`
8. Открыть в веб-браузере адрес: `http://127.0.0.1:5000/`

### config.py:
WEATHER_DEFAULT_CITY = 'name_of_city'
WEATHER_API_KEY = 'api_key'
WEATHER_URL = 'api_weather_url'
SQLALCHEMY_DATABASE_URI = 'path_to_db'
SECRET_KEY = 'secret_key'
