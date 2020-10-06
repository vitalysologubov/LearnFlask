from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError

from webapp.user.models import User


class LoginForm(FlaskForm):
    """Форма авторизации"""

    name = StringField('Логин :', validators=[DataRequired()], render_kw={'class': 'form-control'})
    password = PasswordField('Пароль:', validators=[DataRequired()], render_kw={'class': 'form-control'})
    remember_me = BooleanField('Запомнить меня', default=True, render_kw={'class': 'form-check-input'})
    submit = SubmitField('Отправить', render_kw={'class': 'btn btn-primary'})


class RegistrationForm(FlaskForm):
    """Форма регистрации"""

    name = StringField('Логин :', validators=[DataRequired()], render_kw={'class': 'form-control'})
    email = StringField(
        'Электронная почта :', validators=[DataRequired(), Email()], render_kw={'class': 'form-control'})
    password1 = PasswordField('Пароль:', validators=[DataRequired()], render_kw={'class': 'form-control'})
    password2 = PasswordField(
        'Повторите пароль:', validators=[DataRequired(), EqualTo('password1')], render_kw={'class': 'form-control'})
    submit = SubmitField('Зарегистрироваться', render_kw={'class': 'btn btn-primary'})

    def validate_name(self, name):
        """Валидатор имени"""

        user_count = User.query.filter_by(name=name.data).count()

        if user_count > 0:
            raise ValidationError('Пользователь уже существует.')

    def validate_email(self, email):
        """Валидатор электронной почты"""

        email_count = User.query.filter_by(name=email.data).count()

        if email_count > 0:
            raise ValidationError('Электронная почта уже существует.')
