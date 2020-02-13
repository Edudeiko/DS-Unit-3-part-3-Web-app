# DS-Unit-3-part-3-Web-app
web app deployment

# Setup

Setup virtual environment:

pipenv install --python 3.7

pipenv install Flask Flask-SQLAlchemy Flask-Migrate

pipenv shell

# Setup database:

cd web_app

FLASK_APP=app.py flask db init #> generates app/migrations dir

# run both when changing the schema:
FLASK_APP=app.py flask db migrate #> creates the db (with "alembic_version" table)
FLASK_APP=app.py flask db upgrade #> creates the "users" table
Run

# Run the app:

FLASK_APP=app.py flask run