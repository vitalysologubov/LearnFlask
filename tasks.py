from celery import Celery
from celery.schedules import crontab

from webapp import create_app
from webapp.news.parsers.habr import get_news_snippets, get_news_content


flask_app = create_app()
celery_app = Celery('tasks', broker=flask_app.config['REDIS_BROKER'])


@celery_app.task
def news_snippets():
    with flask_app.app_context():
        get_news_snippets()


@celery_app.task
def news_content():
    with flask_app.app_context():
        get_news_content()


@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(crontab(minute='*/5'), news_snippets.s())
    sender.add_periodic_task(crontab(minute='*/5'), news_content.s())
