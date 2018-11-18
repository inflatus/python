# using JSON and the WeatherUnderground API
# parsing data and emailing it to myself


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import urllib.request
import json
from API_KEYS import EMAIL_ADDRESS, EMAIL_PASSWORD
from API_KEYS import WEATHER_UNDERGROUND_KEY

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

# setting the data for location and temperature
data = (('Current temperature in {} is: {} F\n'.format(location, temp_f)) +
        ('Relative Humidity is at: {}\n'.format(relative_humidity)) +
        ('Winds are: {} mph\n'.format(wind_mph)) +
        ('Wind gusts are at: {} mph\n'.format(wind_gust)) +
        ('Pressure is: {} mb\n'.format(pressure_mb)) +
        ('Feels like: {} F\n'.format(feels_like)) +
        ('Visibility is: {} mi\n'.format(visibility_mi)) +
        ('Precipitation today: {} inches\n'.format(precipitation_in)) +
        ('General weather is: {}'.format(weather)))

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
