# need to revisit this script
# this does not do much other than list all the available ips
# no longer shows available ip's errors out

import subprocess
import ipaddress

network_address = input('Enter a network address in CIDR format(example 192.168.1.0/24): ')

ip_network = ipaddress.ip_network(network_address)
for all_hosts in ip_network.hosts():
    print(all_hosts)

    status, result = subprocess.getstatusoutput('ping -c1 -w2 ' + all_hosts)

if status == 0:
    print('Host ' + all_hosts + ' is UP')
else:
    print('Host ' + all_hosts + ' is DOWN')
