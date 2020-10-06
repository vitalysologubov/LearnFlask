from datetime import datetime
from sqlalchemy.orm import relationship

from webapp.db import db


class News(db.Model):
    """Новости"""

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    url = db.Column(db.String, unique=True, nullable=False)
    published = db.Column(db.DateTime, nullable=False)
    text = db.Column(db.Text, nullable=True)

    def comments_count(self):
        """Количество комментариев"""

        return Comment.query.filter(Comment.news_id == self.id).count()

    def __repr__(self):
        return f'News: {self.title} {self.url}'


class Comment(db.Model):
    """Комментарии"""

    id = db.Column(db.Integer, primary_key=True)
    news_id = db.Column(db.Integer, db.ForeignKey('news.id', ondelete='CASCADE'), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), index=True)
    text = db.Column(db.Text, nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.now())

    news = relationship('News', backref='comments')
    user = relationship('User', backref='comments')

    def __repr__(self):
        return f'Comment: {self.id}'
