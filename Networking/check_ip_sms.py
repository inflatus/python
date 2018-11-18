# requires a twilio account
# using the old credentials and it fails
# when I revisit this code I will update API KEYS
# have not had the need to use this yet

import bs4 as bs
import urllib.request
from twilio.rest import Client
from API_KEYS import ACCOUNT_TOKEN, ACCOUNT_KEY, TWILIO_PHONE, CELL_PHONE

# grab IP address
sauce = urllib.request.urlopen('http://checkip.dyndns.com/').read()

soup = bs.BeautifulSoup(sauce, 'lxml')

# print the IP address
print(soup.body.text)

# setting up twilio information
client = Client(ACCOUNT_KEY, ACCOUNT_TOKEN)

# sending the IP address via sms
message = client.api.account.messages.create(to=(CELL_PHONE), from_=(TWILIO_PHONE), body=(soup.body.text))
