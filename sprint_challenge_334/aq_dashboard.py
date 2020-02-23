"""OpenAQ Air Quality Dashboard with Flask."""
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import openaq

api = openaq.OpenAQ()

APP = Flask(__name__)
APP.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///scdb.sqlite3"
APP.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
DB = SQLAlchemy(APP)


class Record(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    datetime = DB.Column(DB.String(25))
    value = DB.Column(DB.Float, nullable=False)
    
    def __repr__(self):
        return f'<Date_UTC: {self.datetime}, concentration of carbon dioxide PPM: {self.value},'


@APP.route('/')
def root():
    """Base view."""
    status, body = api.measurements(city='Los Angeles', parameter='pm25')
    results = body['results']
    for result in results:
        date_utc = result['date']['utc']
        ppm = result['value']
        date_utc_ppm = Record(datetime=str(date_utc), value=ppm)
        DB.session.add(date_utc_ppm)
    DB.session.commit()
    vvsv = Record.query.filter(Record.value >= 10).all()
    return render_template('scresult.html', vvsv=vvsv)


@APP.route('/refresh')
def refresh():
    """Pull fresh data from Open AQ and replace existing data."""
    DB.drop_all()
    DB.create_all()
    # TODO Get data from OpenAQ, make Record objects with it, and add to db
    DB.session.commit()
    return 'Data refreshed!'


if __name__ == "__main__":
    APP.run()


# FLASK_APP=aq_dashboard.py flask run
