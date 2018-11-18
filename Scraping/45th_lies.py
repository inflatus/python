# need to revist / throwing an error
# RuntimeWarning: numpy.dtype size changed, may indicate binary
# incompatibility. Expected 96, got 88 return f(*args, **kwds)
# will load and parse the data of the President's Lies
# from the NY Times

import requests
from bs4 import BeautifulSoup
import pandas as pd

# grabbing the url
r = requests.get('http://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html')

# parsing the url
soup = BeautifulSoup(r.text, 'html.parser')
results = soup.find_all('span', attrs={'class': 'short-desc'})

# creating the records
records = []
for result in results:
    date = result.find('strong').text[0:-1] + ', 2017'
    lie = result.contents[1][1:-2]
    explanation = result.find('a').text[1:-1]
    url = result.find('a')['href']
    records.append((date, lie, explanation, url))

# creating the csv
df = pd.DataFrame(records, columns=['date', 'lie', 'explanation', 'url'])
df['date'] = pd.to_datetime(df['date'])
df.to_csv('45th_lies.csv', index=False, encoding='utf-8')
