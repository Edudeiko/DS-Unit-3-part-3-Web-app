"""4 make an adjustment to app file."""
import os
from dotenv import load_dotenv

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from web_app.models import db, migrate  # User, Tweet
# from web_app.routes import my_routes
from web_app.new_routes import new_routes
# from web_app.twitter_service import twitter_api_client

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", default="OOPS")


def create_app():
    app = Flask(__name__)
    app.config["CUSTOM_VAR"] = 5  # just an example of app config
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    # app.config["TWITTER_API_CLIENT"] = twitter_api_client()

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(new_routes)
    # app.register_blueprint(more_routes)

    return app

# def create_app():
#     app = Flask(__name__)
# #     # app.config["CUSTOM_VAR"] = 5  # just an example of app config
#     app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
#     app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# #     # app.config["TWITTER_API_CLIENT"] = twitter_api_client()

#     DB.init_app(app)
#     # migrate.init_app(app, db)

#     # app.register_blueprint(my_routes)
#     # app.register_blueprint(more_routes)
#     # app.register_blueprint(new_routes)
#     @app.route('/')
#     def root():
#         users = User.query.all()
#         return render_template('base.html', title = 'Home', users=users)

#     @app.route('/reset')
#     def reset():
#         DB.drop_all()
#         DB.create_all()
#         return render_template('base.html', title='Reset', users=[])

#     @app.route('/user', methods=['POST'])
#     @app.route('/user/<name>', methods=['GET'])
#     def user(name=None, message=''):
#         name = name or request.values['user_name']
#         try:
#             if request.method == 'POST':
#                 add_or_update_user(name)
#                 message = "User {} successfully added".format(name)
#             tweets = User.query.filter(User.name == name).one().tweets
#         except Exception as e:
#             message = "Error adding {}: {}".format(name, e)
#             tweets = []
#         return render_template('user.html', title=name, tweets=tweets,
#         message=message)

#     @app.route('/compare', methods=['POST'])
#     def compare(message=''):
#         user1, user2 = sorted([request.values['user1'],
#                                request.values['user2']])
#         if user1 == user2:
#             message = 'Cannot compare a user to themselves!'
#         else:
#             prediction = predict_user(user1, user2, request.values['tweet_text'])
#             message = '"{}" is more likely to be said by {} than {}'.format(
#             request.values['tweet_text'], user1 if prediction else user2,
#             user2 if prediction else user1
#             )
#         return render_template('prediction.html', title='Prediction', message=message)
#     return app


# FLASK_APP=app.py flask db init #> generates app/migrations dir

# run both when changing the schema:
# FLASK_APP=app.py flask db migrate #> creates the db (with "alembic_version" table)
# FLASK_APP=app.py flask db upgrade #> creates the "users" table
# FLASK_APP=app.py flask run or set FLASK_APP=app.py, then only flask run
# FLASK_APP=web_app.py flask run
# git push heroku master
# heroku run bash then exit
# heroku config
# heroku config:set BASILICA_API_KEY="_____"
# heroku config:set TWITTER_API_KEY="_____"
# heroku config:set TWITTER_API_SECRET="______"
# heroku config:set TWITTER_ACCESS_TOKEN="______"
# heroku config:set TWITTER_ACCESS_TOKEN_SECRET="_____"
# heroku addons:create heroku-postgresql:hobby-dev
# DATABASE_URL="postgres://USERNAME:PASSWORD@HOST:5432/DB_NAME"
# FLASK_APP=web_app flask db init # may see Error: Directory migrations already exists and is not empty and its ok
# FLASK_APP=web_app flask db stamp head # if you see an error about Target database is not up to date
# FLASK_APP=web_app flask db migrate
# FLASK_APP=web_app flask db upgrade
