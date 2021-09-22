import json
from datetime import date, timedelta

import numpy as np
import requests
from typing import List

from settings import API_KEY


class Parameter:
    """State class"""

    def __init__(self, name: str, average: float = None, median: float = None, minimum: float = None,
                 maximum: float = None, values: List[float] = None):
        self.name = name
        if average is not None and median is not None and minimum is not None and maximum is not None:
            self.average = average
            self.median = median
            self.minimum = minimum
            self.maximum = maximum
        elif values is not None:
            self.calculate(values)

    def __str__(self):
        return '{' + f' "{self.name}":' + '{' \
                                          f'"average": {self.average}, ' \
                                          f'"median": {self.median}, ' \
                                          f'"min": {self.minimum}, ' \
                                          f'"max": {self.maximum}' \
                                          '}}'

    def calculate(self, arr: [float]):
        self.minimum = np.min(arr).round(1)
        self.maximum = np.max(arr).round(1)
        self.median = np.median(arr).round(1)
        self.average = np.average(arr).round(1)


class City:
    """Simple city abstraction"""

    def __init__(self, location: str, days: int = 0):
        self.city = location
        self.location = location
        self.date_from = (date.today() - timedelta(days=max(int(days), 0))).isoformat()
        self.date_to = date.today().isoformat()
        self.temperature_c = Parameter('temperature_c')
        self.humidity = Parameter('humidity')
        self.pressure_mb = Parameter('pressure_mb')

    def __str__(self):
        return '{'f'"city": "{self.city}": "from": {self.date_from}, "to": "{self.date_to}"\n' \
               f'{self.temperature_c},\n' \
               f'{self.humidity},\n' \
               f'{self.pressure_mb}\n'

    def get_weather(self):
        url_endpoint = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/' \
                       f'{self.location}/{self.date_from}/{self.date_to}?unitGroup=metric&key={API_KEY}'
        try:
            raw_data = requests.get(url_endpoint).text
            data = json.loads(raw_data)
            self.temperature_c.calculate([item['temp'] for item in data['days']])
            self.humidity.calculate([item['humidity'] for item in data['days']])
            self.pressure_mb.calculate([item['pressure'] for item in data['days']])
            return raw_data
        except Exception as e:
            print(e)