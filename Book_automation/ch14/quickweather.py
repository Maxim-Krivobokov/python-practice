#! python3
# quickweather.py - выводит прогноз погоды для заданного населенного пункта

import json, requests, sys

# detect city name from sys.arg

if len(sys.argv) < 2:
    print('Usage: quickweather.py <Location>')
    sys.exit()

location = ' '.join(sys.argv[1:])

url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3' % (location)

response = requests.get(url)

response.raise_for_status()

print(response.text)