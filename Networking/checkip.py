import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('http://checkip.dyndns.com/').read()

soup = bs.BeautifulSoup(sauce, 'lxml')

print(soup.body.text)
