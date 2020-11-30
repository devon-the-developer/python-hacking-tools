import socket
from IPy import IP

def scan(target):
    converted_ip = check_ip(target)
    print('\n' + '[-_0 Scanning Target] ' + str(target))
    for port in range(1, 500):
            scan_port(converted_ip, port)

def check_ip(ip):
    #check if value given is IP or domainname 
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)

def get_banner(s):
    #not sure how to check if get_banner is working 
    banner = s.recv(1024)
    return banner

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.6)
        #establish connection with target machine
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            print('[+] Open Port ' + str(port) +  ' : ' + str(banner))
        except:
            print('[+] Open Port ' + str(port) + ' | ')
    except: 
        pass

if __name__ == "__main__":   
    targets = input('[+] Enter Target/s To Scan (split multiple targets with ,): ')
    if ',' in targets:
        for ipaddress in targets.split(','):
            scan(ipaddress.strip(' '))
    else:
        scan(targets)


        
        