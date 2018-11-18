# need to revist this to pull information by other means
# script relies on user(s) OS installs
# nmap, whois and host need to be installed

import os
import subprocess


def get_ip_address(url):
    command = 'host ' + url
    process = os.popen(command)
    results = str(process.read())
    marker = results.find('has address') + 12
    return results[marker:].splitlines()[0]


def get_nmap(ip):
    command = 'nmap -F ' + ip
    process = os.popen(command)
    results = str(process.read())
    return results


def get_ping(ip):
    command = 'ping -c 5 ' + ip
    process = os.popen(command)
    results = str(process.read())
    return results


def get_whois(ip):
    command = 'whois ' + ip
    process = os.popen(command)
    results = str(process.read())
    return results


def get_host(ip):
    command = 'host -l ' + ip
    process = os.popen(command)
    results = str(process.read())
    return results

# clearing the screen
subprocess.call('clear', shell=True)

# getting url input
url = input('Type in url you wish to use: ')
ip = (get_ip_address(url))

# writing information to file
f = open('%s _ip_information.txt' % url, 'w')
f.write(ip)
f.write(get_nmap(ip))
f.write(get_ping(ip))
f.write(get_whois(ip))
f.write(get_host(ip))
f.close()
