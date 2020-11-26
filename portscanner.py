import socket
from IPy import IP

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        #establish connection with target machine
        sock.connect((ipaddress, port))
        print('[+] Port ' + str(port) +  ' is Open')
    except: 
        print('[-] Port ' + str(port) +  ' is Closed')

ipaddress = input('[+] Enter Target To Scan')

for port in range(50, 90):
    scan_port(ipaddress, port)