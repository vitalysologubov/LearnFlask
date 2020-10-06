from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user, login_user, logout_user

from webapp.db import db
from webapp.utils import get_redirect_target
from webapp.user.forms import LoginForm, RegistrationForm
from webapp.user.models import User


blueprint = Blueprint('user', __name__, url_prefix='/users')


@blueprint.route('/registration')
def registration():
    """Регистрация"""

    if current_user.is_authenticated:
        return redirect(url_for('news.index'))

    title = 'Регистрация'
    form = RegistrationForm()

    return render_template('user/registration.html', title=title, form=form)


@blueprint.route('/proccess_registration', methods=['POST'])
def proccess_registration():
    """Процесс регистрации"""

    form = RegistrationForm()

    if form.validate_on_submit():
        new_user = User(name=form.name.data, email=form.email.data, role='user')
        new_user.set_password(form.password1.data)

        db.session.add(new_user)
        db.session.commit()

        flash('Регистрация завершена.')
        return redirect(url_for('news.index'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f'Ошибка в поле {getattr(form, field).label.text}: {error}.')

    return redirect(url_for('user.registration'))


@blueprint.route('/login')
def login():
    """Авторизация"""

    if current_user.is_authenticated:
        return redirect(get_redirect_target())

    title = 'Авторизация'
    form = LoginForm()

    return render_template('user/login.html', title=title, form=form)


@blueprint.route('/proccess_login', methods=['POST'])
def proccess_login():
    """Процесс авторизации"""

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter(User.name == form.name.data).first()

        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash('Вы вошли в систему.')

            return redirect(get_redirect_target())

    flash('Неправильное имя или пароль')

    return redirect(get_redirect_target())


@blueprint.route('/logout')
def logout():
    """Разлогинивание"""

    logout_user()
    flash('Вы вышли из системы.')

    return redirect(get_redirect_target())
