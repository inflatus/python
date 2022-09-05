'''scrape code titles authors and publishers from the dnd modules page'''
'''only scrapes the first section of the page'''

import requests
from bs4 import BeautifulSoup

def main():
    '''scrape titles authors and publishers from the dnd modules page'''
    url = 'https://en.wikipedia.org/wiki/List_of_Dungeons_%26_Dragons_modules'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    table = soup.find('table', class_='wikitable')
    rows = table.find_all('tr')
    for row in rows:
        cells = row.find_all('td')
        if cells:
            code = cells[0].text.strip()
            tsr_number = cells[1].text.strip()
            title = cells[2].text.strip()
            levels = cells[3].text.strip()
            authors = cells[4].text.strip()
            publisher = cells[5].text.strip()
            print(code, tsr_number, title, levels, authors, publisher)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3