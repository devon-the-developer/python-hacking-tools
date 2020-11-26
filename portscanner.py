import socket
from IPy import IP

def scan(target):
    converted_ip = check_ip(target)
    print('\n' + '[-_0 Scanning Target] ' + str(target))
    for port in range(70, 90):
            scan_port(converted_ip, port)

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
        pass
    
targets = input('[+] Enter Target/s To Scan (split multiple targets with ,): ')
if ',' in targets:
    for ipaddress in targets.split(','):
        scan(ipaddress.strip(' '))
else:
    scan(targets)


        
        