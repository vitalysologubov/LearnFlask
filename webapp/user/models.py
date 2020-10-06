from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from webapp.db import db


class User(db.Model, UserMixin):
    """Пользователи"""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True, unique=True)
    password = db.Column(db.String(128))
    role = db.Column(db.String(10), index=True)
    email = db.Column(db.String(50), unique=True)

    def set_password(self, password):
        """Получение хэша пароля"""

        self.password = generate_password_hash(password)

    def check_password(self, password):
        """Проверка хэша пароля"""

        return check_password_hash(self.password, password)

    @property
    def is_admin(self):
        """Проверка роли"""

        return self.role == 'admin'

    def __repr__(self):
        return f'User: {self.name} {self.id}'
