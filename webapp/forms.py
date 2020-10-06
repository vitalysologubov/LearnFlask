from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    """Форма авторизации"""

    name = StringField('Логин :', validators=[DataRequired()], render_kw={'class': 'form-control'})
    password = PasswordField('Пароль:', validators=[DataRequired()], render_kw={'class': 'form-control'})
    submit = SubmitField('Отправить', render_kw={'class': 'btn btn-primary'})
