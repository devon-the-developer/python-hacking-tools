import portscanner

targets_ip = input('[+] Enter Target To Scan For Vulnerable Open Ports: ')
port_number = int(input('[+] * Enter Amount Of Ports You Want To Scan(500 - first 500 ports: '))
vul_file = input('[+] * Entter Path To The File With Vulnerable Softwares: ')
print('\n')

portscanner.scan(targets_ip)