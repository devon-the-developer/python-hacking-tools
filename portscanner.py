import socket
from IPy import IP

ipaddress = input('[+] Enter Target To Scan')
port = 80

try:
    sock = socket.socket()
    #establish connection with target machine
    sock.connect((ipaddress, port))
    print('[+] Port 80 is Open')
except: 
    print('[-] Port 80 is Closed')