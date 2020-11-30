import socket
from IPy import IP

class PortScan():
    banners = []
    open_ports = []
    def __init__(self, target, port_num):
        self.target = target
        self.port_num = port_num
        

    def scan(self):
        print('\n' + '[-_0 Scanning Target] ' + str(self.target))
        for port in range(1, self.port_num):
                if(port % 10 == 0):
                    print("scanning port: ", port)
                self.scan_port(port)

    def check_ip(self):
        #check if value given is IP or domainname 
        try:
            IP(self.target)
            return(self.target)
        except ValueError:
            return socket.gethostbyname(self.target)

    def scan_port(self, port):
        try:
            converted_ip = self.check_ip()
            sock = socket.socket()
            sock.settimeout(0.5)
            #establish connection with target machine
            sock.connect((converted_ip, port))
            self.open_ports.append(port)
            try:
                banner = sock.recv(1024).decode().strip('\n').strip('\r')
                print('[+] Open Port ' + str(port) +  ' : ' + str(banner))
                self.banners.append(banner)
            except:
                print('[+] Open Port ' + str(port))
                self.banners.append(' ')
            sock.close()
        except: 
            pass
        


        
        