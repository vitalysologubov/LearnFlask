import sys
from getpass import getpass
from webapp import create_app
from webapp.model import db, Users


app = create_app()

with app.app_context():
    user_name = input('Логин:')

    if Users.query.filter(Users.name == user_name).count():
        print('Пользователь с таком логином уже существует!')
        sys.exit()

    password1 = getpass('Пароль:')
    password2 = getpass('Повторите пароль:')

    if not password1 == password2:
        print('Пароли отличаются!')
        sys.exit()

    new_user = Users(name=user_name, role='admin')
    new_user.set_password(password1)

    db.session.add(new_user)
    db.session.commit()
    print(f'Пользоваетль "{user_name}" создан. ИД: {new_user.id}.')
