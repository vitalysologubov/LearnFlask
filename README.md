# LearnFlask

### Функционал:
1. Парсинг новостей с habr.com и сохранение их в базу данных.
2. Получение информации о температуре на примере города Санкт-Петербург.
3. Отображение информации с использованием фреймворка Bootstrap.
4. Регистрация и авторизация пользователей.
5. Комментирование новостей.

### Установка:
1. Клонировать репозиторий с GitHub: `git clone https://github.com/vitalysologubov/LearnFlask.git`
2. Создать виртуальное окружение: `python -m venv env`
3. Установить зависимости: `pip install -r requirements.txt`
4. Создать миграцию базы данных: `set FLASK_APP=webapp && flask db stamp head && flask db migrate -m "Migrating tables"`
5. Выполнить миграцию базы данных: `set FLASK_APP=webapp && flask db upgrade`
6. Добавить администратора: `python create_admin.py`
7. Запустить приложение: `set FLASK_APP=webapp && flask run`
8. Открыть приложение в веб-браузере: `http://127.0.0.1:5000/`

### Celery:
* Запуск Celery: `set FORKED_BY_MULTIPROCESSING=1 && celery -A tasks worker --loglevel=info -P eventlet`
* Запуск Celery-beat: `celery -A tasks beat`

### config.py:
* WEATHER_DEFAULT_CITY = 'name_of_city'
* WEATHER_API_KEY = 'api_key'
* WEATHER_URL = 'api_weather_url'
* SQLALCHEMY_DATABASE_URI = 'path_to_db'
* SQLALCHEMY_TRACK_MODIFICATIONS = 'True or False'
* REMEMBER_COOKIE_DURATION = 'timedelta(days=number_of_days)'
* REDIS_BROKER = 'path_to_redis'
* USER_AGENT = 'user_agent'
* SECRET_KEY = 'secret_key'