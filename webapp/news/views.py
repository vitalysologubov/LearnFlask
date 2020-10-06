from flask import abort, Blueprint, current_app, flash, redirect, render_template
from flask_login import current_user, login_required

from webapp.db import db
from webapp.utils import get_redirect_target
from webapp.news.forms import CommentForm
from webapp.news.models import Comment, News
from webapp.weather import weather_by_city


blueprint = Blueprint('news', __name__)


@blueprint.route('/')
def index():
    """Главная страница на которой отображаются новости и прогноз погоды"""

    title = 'Python новости'
    news = News.query.filter(News.text.isnot(None)).order_by(News.published.desc()).all()
    weather = weather_by_city(current_app.config['WEATHER_DEFAULT_CITY'])

    return render_template('news/index.html', title=title, news_list=news, weather=weather)


@blueprint.route('/news/<int:news_id>')
def single_news(news_id):
    """Содержание новости"""

    news = News.query.filter(News.id == news_id).first()

    if not news:
        abort(404)

    form = CommentForm(news_id=news.id)

    return render_template('news/single_news.html', title=news.title, news=news, form=form)


@blueprint.route('/news/add_comment', methods=['POST'])
@login_required
def add_comment():
    """Добавление комментариев"""

    form = CommentForm()

    if form.validate_on_submit():
        comment = Comment(news_id=form.news_id.data, user_id=current_user.id, text=form.comment.data)
        db.session.add(comment)
        db.session.commit()
        flash('Комментарий успешно добавлен.')
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f'Ошибка в поле {getattr(form, field).label.text}: {error}.')

    return redirect(get_redirect_target())
