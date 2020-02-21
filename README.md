# DS-Unit-3-part-3-Web-app

web_app deployment

## Setup

Setup virtual environment:

pipenv install --python 3.7

pipenv install Flask Flask-SQLAlchemy Flask-Migrate

pipenv shell

## Setup database

cd web_app

FLASK_APP=app.py flask db init #> generates app/migrations dir

## run both when changing the schema

FLASK_APP=app.py flask db migrate #> creates the db (with "alembic_version" table)

FLASK_APP=app.py flask db upgrade #> creates the "users" table

## Run the app

FLASK_APP=app.py flask run or set FLASK_APP=app.py, then you can only use flask run

## Heroku

> make sure to pip install all the Necessary libraries, then create pipenv. pipenv will create Pipfile.lock with all your collected libraries. Install gunicorn before creating Pipfile.lock

heroku login

heroku apps

cd /path/to/your/app

pwd # > check the directory first

git remote -v

heroku create #> name of your app or 'heroku create' heroku will assign a random name to your app

git remote -v

git push heroku master

## Debug mode

heroku run bash

---> ls -al

---> exit

heroku config

heroku config:set BASILICA_API_KEY="---------------"

heroku config:set TWITTER_API_KEY="------------------"

heroku config:set TWITTER_API_SECRET="-------------------------"

heroku config:set TWITTER_ACCESS_TOKEN="--------------------------"

heroku config:set TWITTER_ACCESS_TOKEN_SECRET="--------------------------"

heroku config #> to check on the changes

heroku logs

> Could not parse rfc1738 URL from string 'OOPS'

heroku addons:create heroku-postgresql:hobby-dev #> create DATABASE_URL in heroku

heroku config #> Check on changes

## insert parameters in to TablePlus

> username, password, host/socket, database

## Heroku run bash

heroku run bash

FLASK_APP=web_app flask db init #>may see Error: Directory migrations already exists and is not empty and its ok

FLASK_APP=web_app flask db stamp head #> if you see an error about Target database is not up to date

FLASK_APP=web_app flask db migrate

FLASK_APP=web_app flask db upgrade
