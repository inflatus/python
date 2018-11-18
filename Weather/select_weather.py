# using json and the Weather Underground API
# pulling weather data and displaying
# able to accept user input and validate

# API_KEYS and Main Modules
import urllib.request
import json
from API_KEYS import WEATHER_UNDERGROUND_KEY
from us_states import states

# API_KEYS and Twitter
import tweepy
from API_KEYS import INFLATUS_CWEATHER
from API_KEYS import INFLATUS_CWEATHER_SECRET
from API_KEYS import INFLATUS_AWEATHER
from API_KEYS import INFLATUS_AWEATHER_SECRET

# API_KEYS and Email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from API_KEYS import EMAIL_ADDRESS, EMAIL_PASSWORD


def validate_location():
    # asking for state ID
    while True:
        state = input('What is the 2 letter state? ').upper()
        if state in states:
            break
        else:
            print('Try again')

    # asking for City
    while True:
        try:
            # input city from user
            city = input('What is the city name? > If there is a space use _ ie. San_Francisco < ').title()
            f = urllib.request.urlopen('http://api.wunderground.com/api/' + WEATHER_UNDERGROUND_KEY + '/geolookup/conditions/q/' + state + '/' + city + '.json')

            # decoding the text
            json_string = f.read().decode('utf-8')

            # parsing the information
            location_data = dict()
            parsed_json = json.loads(json_string)

            location_data['city'] = parsed_json['location']['city']
            location_data['temp_f'] = parsed_json['current_observation']['temp_f']
            location_data['relative_humidity'] = parsed_json['current_observation']['relative_humidity']
            location_data['wind_mph'] = parsed_json['current_observation']['wind_mph']
            location_data['wind_gust_mph'] = parsed_json['current_observation']['wind_gust_mph']
            location_data['pressure_mb'] = parsed_json['current_observation']['pressure_mb']
            location_data['feels_like'] = parsed_json['current_observation']['feelslike_f']
            location_data['visibility_mi'] = parsed_json['current_observation']['visibility_mi']
            location_data['precip_today_in'] = parsed_json['current_observation']['precip_today_in']
            location_data['weather'] = parsed_json['current_observation']['weather']
            break

            # raising exception if city is not able to load
            # will loop back to ask question again
        except Exception:
            print('Either you have spelled the city wrong or your choice is out in the boondocks! Change the city.')
    return location_data


def _get_weather_display_info(location):
    data = [
        'Current temperature in {} is: {} F\n'.format(location['city'], location['temp_f']),
        'Relative Humidity is at: {}\n'.format(location['relative_humidity']),
        'Winds are: {} mph\n'.format(location['wind_mph']),
        'Wind gusts are at: {} mph\n'.format(location['wind_gust_mph']),
        'Pressure is: {} mb\n'.format(location['pressure_mb']),
        'Feels like: {} F\n'.format(location['feels_like']),
        'Visibility is: {} mi\n'.format(location['visibility_mi']),
        'Precipitation today: {} inches\n'.format(location['precip_today_in']),
        'General weather is: {}\n'.format(location['weather'])
    ]
    return data


def display_weather(location):
    data = _get_weather_display_info(location)
    for line in data:
        print(line)


def email_weather(location):
    # setting the data for location and temperature
    data = '\n'.join(_get_weather_display_info(location))

    # compose email message
    fromaddr = (EMAIL_ADDRESS)
    toaddr = (EMAIL_ADDRESS)
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Current Weather"

    body = (data)
    msg.attach(MIMEText(body, 'plain'))

    # authenticate and send email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, (EMAIL_PASSWORD))
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()


def tweet_weather(location):
    # keys
    consumer_key = INFLATUS_CWEATHER
    consumer_secret = INFLATUS_CWEATHER_SECRET
    access_token = INFLATUS_AWEATHER
    access_token_secret = INFLATUS_AWEATHER_SECRET

    # authentication with Twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    # tweeting the data
    data = _get_weather_display_info(location)

    for line in data:
        api.update_status(status=line)


def main():
    location_data = validate_location()
    display_weather(location_data)
    email_weather(location_data)
    tweet_weather(location_data)


if __name__ == '__main__':
    main()
