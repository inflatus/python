# this will download the Dragon Magazine issues from
# https://annarchive.com/dragon.html
# appears that the site is blocking crawlers / scrapers
# regardless of header info
# 
# using wget command to retrieve the files
# will keep this as a reminder that sometimes reinventing the wheel
# is not always best

import requests
from bs4 import BeautifulSoup
import urllib.request


def get_magazine():
    dragon_url = 'https://annarchive.com/dragon.html'

    headers = {}
    headers['User-Agent']= 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'
    req = urllib.request.Request(dragon_url, headers = headers)
    resp = urllib.request.urlopen(req)
    resp_data = resp.read()

    # get the url
    r = requests.get(dragon_url)

    # create the beautifulsoup object
    soup = BeautifulSoup(r.content, 'lxml')

    # find all links
    links = soup.findAll('a')

    # filter the pdfs
    magazines = [dragon_url + link['href'] for link in links if link['href'].endswith('.pdf')]

    return magazines


def download_magazines(magazines):

    for link in magazines:
        urllib.request.urlretrieve(link, '/home/inflatus/Python/Python/Scraping/')

    print('All Magazines Downloaded')
    return


if __name__ == '__main__':
    magazines = get_magazine()
    download_magazines(magazines)
