# using socket to retrieve IP address and hostname

import socket

# open the socket and connect to google DNS
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 80))

# get IP address and host name
ip_address = (s.getsockname()[0])
host_name = socket.gethostname()

# print gathered information
print(ip_address)
print(host_name)

# close the socket
s.close()
