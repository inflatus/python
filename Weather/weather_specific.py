'''grab the current weather for Martinsville Indiana using google weather'''

import urllib.request
import json
import sys

def get_weather():
    '''get the weather'''
    url = 'http://www.google.com/ig/api?weather=46151'
    try:
        data = urllib.request.urlopen(url).read()
    except urllib.error.URLError as error:
        print(error)
        sys.exit(1)
    data = data.decode('utf-8')
    data = json.loads(data)
    return data

def main():
    '''main function'''
    data = get_weather()
    print(data['weather']['current_conditions']['condition']['data'])
    print(data['weather']['current_conditions']['temp_f']['data'])
    print(data['weather']['current_conditions']['humidity']['data'])
    print(data['weather']['current_conditions']['wind_condition']['data'])

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
# Path: Weather/weather_specific.py
