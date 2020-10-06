from flask import flash, Flask, redirect, render_template, url_for
from flask_login import current_user, LoginManager, login_required, login_user, logout_user
from webapp.forms import LoginForm
from webapp.model import db, News, Users
from webapp.weather import weather_by_city


def create_app():
    """Создание приложения"""

    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        """Загрузка полльзователя"""

        return Users.query.get(user_id)

    @app.route('/')
    def index():
        """Отображение погоды"""

        title = 'Python новости'
        weather = weather_by_city(app.config['WEATHER_DEFAULT_CITY'])
        news = News.query.order_by(News.published.desc()).all()
        return render_template('index.html', title=title, news=news, weather=weather)

    @app.route('/login')
    def login():
        """Авторизация"""

        if current_user.is_authenticated:
            return redirect(url_for('index'))

        title = 'Авторизация'
        login_form = LoginForm()
        return render_template('login.html', title=title, form=login_form)

    @app.route('/proccess_login', methods=['POST'])
    def proccess_login():
        """Процесс авторизации"""

        form = LoginForm()

        if form.validate_on_submit():
            user = Users.query.filter(Users.name == form.name.data).first()

            if user and user.check_password(form.password.data):
                login_user(user)
                flash('Вы вошли в систему.')
                return redirect(url_for('index'))

        flash('Неправильные имя или пароль')
        return redirect(url_for('login'))

    @app.route('/logout')
    def logout():
        """Разлогинивание"""

        logout_user()
        flash('Вы вышли из системы.')
        return redirect(url_for('index'))

    @app.route('/admin')
    @login_required
    def admin_index():
        if current_user.is_admin:
            return 'Привет, админ!'
        else:
            return 'Привет, не админ!'

    return app
