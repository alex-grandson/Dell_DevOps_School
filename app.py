from flask import Flask, render_template, request

import manager
from models import City

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title='Main', cities=manager.get_cities())

@app.route('/weather', methods=['GET', 'POST'])
def raw_result():
    city = request.values['city']
    days = request.values['days']
    if manager.is_valid_day(days):
        try:
            result_city = City(location=city, days=int(days))
            data = result_city.get_weather()
            return result_city.__dict__()
        except Exception as e:
            return '<h1>Internal Server Error</h1><br>Seems like external api doesn\'t work properly.' + data
    return '{}'


@app.route('/result')
def get_result():
    return render_template('result.html', title='Result')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
