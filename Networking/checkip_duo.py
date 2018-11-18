# check ip using requests
# second go round with a new way to grab ip

import requests

data = requests.get('https://api.ipify.org').text
print('IP Address is', format(data))
