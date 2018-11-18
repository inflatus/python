# grab the current weather for Martinsville
# display the temp, feels like temp
# weather phrase, high/low temps and uv index

import requests
from bs4 import BeautifulSoup

r = requests.get('https://weather.com/weather/today/l/39.43,-86.42')
soup = BeautifulSoup(r.text, 'html.parser')

temp = soup.find('div', attrs={'class': 'today_nowcard-temp'})
feels_like = soup.find('div', attrs={'class': 'today_nowcard-feels'})
phrase = soup.find('div', attrs={'class': 'today_nowcard-phrase'})
hilo = soup.find('div', attrs={'class': 'today_nowcard-hilo'})

print('The temperature in Martinsville is', temp.text)
print(feels_like.text)
print(phrase.text)
print(hilo.text[:13])
print(hilo.text[13:])
