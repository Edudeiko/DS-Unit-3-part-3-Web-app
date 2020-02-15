import os
from dotenv import load_dotenv

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from web_app.models import db, User, Tweet, migrate
from web_app.routes import my_routes
# from web_app.more_routes import more_routes
from web_app.twitter_service import twitter_api_client

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", default="OOPS")

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["TWITTER_API_CLIENT"] = twitter_api_client()

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(my_routes)
    # app.register_blueprint(more_routes)

    return app



# AAAH I ACTUALLY THINK THE API CLIENT DOESN'T
# YET MAKE ANY REQUESTS! 
# SO THAT LAST STEP MIGHT HAVE BEEN UNNECESSARY!


# FLASK_APP=app.py flask db init #> generates app/migrations dir

# run both when changing the schema:
# FLASK_APP=app.py flask db migrate #> creates the db (with "alembic_version" table)
# FLASK_APP=app.py flask db upgrade #> creates the "users" table
# FLASK_APP=app.py flask run or set FLASK_APP=app.py, then only flask run
