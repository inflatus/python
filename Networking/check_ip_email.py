import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import bs4 as bs
import urllib.request
from API_KEYS import EMAIL_ADDRESS, EMAIL_PASSWORD

# grab IP address
sauce = urllib.request.urlopen('http://checkip.dyndns.com/').read()

soup = bs.BeautifulSoup(sauce, 'lxml')

# compose email message
fromaddr = (EMAIL_ADDRESS)
toaddr = (EMAIL_ADDRESS)
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Public IP"

body = (soup.body.text)
msg.attach(MIMEText(body, 'plain'))

# authenticate and send email
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, (EMAIL_PASSWORD))
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
