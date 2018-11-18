import requests
from API_KEYS import WEATHER_UNDERGROUND_KEY

state = input('State ')
city = input('City ')

resp = requests.head('http://api.wunderground.com/api/' + WEATHER_UNDERGROUND_KEY + '/geolookup/conditions/q/' + state + '/' + city + '.json')
print(resp.status_code, resp.text, resp.headers)
