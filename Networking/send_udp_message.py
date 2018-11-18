import socket
import subprocess

# clearing the screen
subprocess.call('clear', shell=True)

# gather IPv4 information and message
ip = input('Enter an IPv4 address to send message: ')
port = 5005
message = input('Enter a message to send: ')

# print inforamtion gathered
print('UDP target IP:', ip)
print('UDP target port:', port)
print('message:', message)

# open port and send message
sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP
sock.sendto(message.encode('utf-8'), (ip, port))
sock.close()
