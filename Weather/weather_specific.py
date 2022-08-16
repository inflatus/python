# grab the current weather for Martinsville
# display the temp, feels like temp
# weather phrase, high/low temps and uv index

import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.google.com/search?client=firefox-b-1-d&q=weather')
soup = BeautifulSoup(r.text, 'html.parser')

temp = soup.find('div', attrs={'class': 'vk_bk TylWce SGNhVe'})
feels_like = soup.find('div', attrs={'class': 'TodayDetailsCard-feels'})
phrase = soup.find('div', attrs={'class': 'TodayDetailsCard-phrase'})
hilo = soup.find('div', attrs={'class': 'TodayDetailsCard-hilo'})

print('The temperature in Martinsville is', temp)
#print(feels_like)
#print(phrase)
#print(hilo[:13])
#print(hilo[13:])
