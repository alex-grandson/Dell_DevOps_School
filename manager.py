import datetime
import pandas as pd
from datetime import date

from models import City


def get_cities():
    return pd.read_csv('db/cities.csv', delimiter=';', decimal='.').to_numpy()


def get_date(n_days: int):
    today = date.today()
    diff = datetime.timedelta(days=n_days)
    return [(today - diff).isoformat(), today.isoformat()]


def is_valid_day(days: str):
    return days.isnumeric() and int(days) >= 0


if __name__ == '__main__':
    city = City('Moscow', 3)
    # print('city.get_weather(): ', city.get_weather())
    city.get_weather()
    print(city)