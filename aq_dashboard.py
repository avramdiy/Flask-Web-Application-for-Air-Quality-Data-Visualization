from openaq import OpenAQ
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
DB = SQLAlchemy(app)
api = OpenAQ()


@app.route('/')
def root():
    """Base view, returns list of "potentially risky" air qualities."""
    #   return str(get_results())  # Part 2, pre-model solution, *all* results
    return str(Record.query.filter(Record.value >= 18).all())


@app.route('/refresh')
def refresh():
    """Replace existing data with data from OpenAQ."""
    DB.drop_all()
    DB.create_all()
    for result in get_results():
        record = Record(datetime=result[0], value=result[1])
        DB.session.add(record)
    DB.session.commit()
    return root()


def get_results():
    """Pull from Open AQ, return as list of datetime/value tuples."""
    _, body = api.measurements(parameter='pm25')
    results = []
    for result in body['results']:
        results.append((result['date']['utc'], result['value']))
    return results


class Record(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    datetime = DB.Column(DB.String(25))  # TODO real datetime
    value = DB.Column(DB.Float, nullable=False)

    def __repr__(self):
        return '< Time {} --- Value {} >'.format(self.datetime, self.value)
