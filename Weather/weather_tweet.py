# will tweet the current weather
# https://www.wunderground.com/weather/api/
# weather undergroud will no longer provide free api keys
# thank you for providing the keys in the past
# they have been a great help


import urllib.request
import json
from API_KEYS import WEATHER_UNDERGROUND_KEY
import tweepy
from API_KEYS import INFLATUS_CWEATHER
from API_KEYS import INFLATUS_CWEATHER_SECRET
from API_KEYS import INFLATUS_AWEATHER
from API_KEYS import INFLATUS_AWEATHER_SECRET

# keys
consumer_key = INFLATUS_CWEATHER
consumer_secret = INFLATUS_CWEATHER_SECRET
access_token = INFLATUS_AWEATHER
access_token_secret = INFLATUS_AWEATHER_SECRET

# authentication with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# getting the url
f = urllib.request.urlopen('http://api.wunderground.com/api/' + WEATHER_UNDERGROUND_KEY + '/geolookup/conditions/q/IN/Martinsville.json')

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

# tweeting the data
temp_f = ('Current temperature in {} is: {} F'.format(location, temp_f))
relative_humidity = ('Relative Humidity is at: {}'.format(relative_humidity))
wind_mph = ('Winds are: {} mph'.format(wind_mph))
wind_gust = ('Wind gusts are at: {} mph'.format(wind_gust))
pressure_mb = ('Pressure is: {} mb'.format(pressure_mb))
feels_like = ('Feels like: {} F'.format(feels_like))
visibility_mi = ('Visibility is: {} mi'.format(visibility_mi))
precipitation_in = ('Precipitation today: {} inches'.format(precipitation_in))
weather = ('General weather is: {}'.format(weather))

# status = api.update_status(status=tweet)

# trying to combine all varibles into one tweet
tweet = (temp_f, relative_humidity, wind_mph, wind_gust, pressure_mb, feels_like, visibility_mi, precipitation_in, weather)
print (tweet)

