# using json and the Weather Underground API
# pulling weather data and displaying
# able to accept user input and validate

import urllib.request
import json
from API_KEYS import WEATHER_UNDERGROUND_KEY
from us_states import states

# asking for state ID

while True:
    state = input('What is the 2 letter state? ')
    if state in states:
        break
    else:
        print('Try again')


# asking for City
while True:
    try:
        # input city from user
        city = input('What is the city name? > If there is a space use _ ie. San_Francisco < ')
        f = urllib.request.urlopen('http://api.wunderground.com/api/' + WEATHER_UNDERGROUND_KEY + '/geolookup/conditions/q/' + state + '/' + city + '.json')

        # decoding the text
        json_string = f.read().decode('utf-8')

        # parsing the information
        parsed_json = json.loads(json_string)
        location = parsed_json['location']['city']
        temp_f = parsed_json['current_observation']['temp_f']
        relative_humidity = parsed_json['current_observation']['relative_humidity']
        wind_mph = parsed_json['current_observation']['wind_mph']
        wind_gust = parsed_json['current_observation']['wind_gust_mph']
        pressure_mb = parsed_json['current_observation']['pressure_mb']
        feels_like = parsed_json['current_observation']['feelslike_f']
        visibility_mi = parsed_json['current_observation']['visibility_mi']
        precipitation_in = parsed_json['current_observation']['precip_today_in']
        weather = parsed_json['current_observation']['weather']
        break

    # raising exception if city is not able to load
    # will loop back to ask question again
    except Exception:
        print('Either you have spelled the city wrong or your choice is out in the boondocks! Change the city.')


print('Current temperature in {} is: {} F'.format(location, temp_f))
print('Relative Humidity is at: {}'.format(relative_humidity))
print('Winds are: {} mph'.format(wind_mph))
print('Wind gusts are at: {} mph'.format(wind_gust))
print('Pressure is: {} mb'.format(pressure_mb))
print('Feels like: {} F'.format(feels_like))
print('Visibility is: {} mi'.format(visibility_mi))
print('Precipitation today: {} inches'.format(precipitation_in))
print('General weather is: {}'.format(weather))
f.close()
