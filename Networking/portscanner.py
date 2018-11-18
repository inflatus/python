# portsanner for IPv4 addresses and/or hostnames
# probing addresses is invasive
# make sure you are doing the right thing

import validators
import socket
import subprocess
import sys
from datetime import datetime

# clearing the screen
subprocess.call('clear', shell=True)


def is_valid(address):
    # returns the validator result, True or False.
    return validators.ip_address.ipv4(remote_server) or validators.domain(remote_server)


while True:  # True is always True. This loop will never end.
    remote_server = input('Enter a remote host to scan: ')
    if remote_server == 'exit':
        sys.exit(0)
    if is_valid(remote_server):
        break
    else:
        print(
            'This address was not recognized as a valid IPv4 address or hostname.'
            'Please try again. Type \'exit\' to quit.'
        )

remote_serverIP = socket.gethostbyname(remote_server)

# print the scanning ip
print('*' * 60)
print('Please wait, scanning remote host of well-know ports', remote_serverIP)
print('*' * 60)

# time scan started
start_time = datetime.now()

# scan all ports between 1 and 1024
try:
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remote_serverIP, port))
        if result == 0:
            print('Port {}: 	 Open'.format(port))
        sock.close()

# error handling
except KeyboardInterrupt:
    print('You pressed Ctrl+C')
    sys.exit(1)

except socket.gaierror:
    print('Hostname could not be resolved')
    sys.exit(1)

except socket.error:
    print('Could not connect to server')
    sys.exit(1)

# time for script to finish
end_time = datetime.now()
completion_time = end_time - start_time

# print completion time
print('Scanning completed in: ', completion_time)
