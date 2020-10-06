from flask_wtf import FlaskForm
from wtforms import HiddenField, SubmitField, StringField
from wtforms.validators import DataRequired, ValidationError

from webapp.news.models import News


class CommentForm(FlaskForm):
    """Форма комментариев"""

    news_id = HiddenField('ID новости', validators=[DataRequired()])
    comment = StringField('Комментарий', validators=[DataRequired()], render_kw={'class': 'form-control'})
    submit = SubmitField('Добавить', render_kw={'class': 'btn btn-primary'})

    def validate_news_id(self, news_id):
        """Проверки ИД новостей"""

        if not News.query.get(news_id.data):
            raise ValidationError(f'Новость с id={news_id.data} не существует.')
