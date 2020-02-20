from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


class User(db.Model):
    """Twitter users"""
    id = db.Column(db.BigInteger, primary_key=True)
    screen_name = db.Column(db.String(128), nullable=False)
    followers_count = db.Column(db.Integer)
    latest_tweet_id = db.Column(db.BigInteger)

    # def __repr__(self):
    #     return '<User {}>'.format(self.screen_name)


class Tweet(db.Model):
    """Tweets we pull"""
    id = db.Column(db.BigInteger, primary_key=True)
    user_id = db.Column(db.BigInteger, db.ForeignKey('user.id'), nullable=False)
    full_text = db.Column(db.String(500))
    user = db.relationship('User', backref=db.backref('tweets', lazy=True))

    embedding = db.Column(db.PickleType, nullable=False)

    # def __repr__(self):
    #     return '<Tweet {}>'.format(self.full_text)
