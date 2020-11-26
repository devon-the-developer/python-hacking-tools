import socket
from IPy import IP

def check_ip(ip):
    #check if value given is IP or domainname 
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        #establish connection with target machine
        sock.connect((ipaddress, port))
        print('[+] Port ' + str(port) +  ' is Open')
    except: 
        print('[-] Port ' + str(port) +  ' is Closed')

ipaddress = input('[+] Enter Target To Scan: ')
converted_ip = check_ip(ipaddress)

for port in range(50, 90):
    scan_port(converted_ip, port)