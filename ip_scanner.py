#ip_scanner.py

import subprocess

ip_type_selection = str(input("1. 192.168.1.xxx\n2. 127.0.0.xxx\n3. 10.0.0.xxx\n4. Others\nSelect IP address type: ")) #standard local IP address with subnet mask 255.255.255.0

if ip_type_selection == "1":
    priv_ip = "192.168.1."
elif ip_type_selection == "2":
    priv_ip = "127.0.0."
elif ip_type_selection == "3":
    priv_ip = "10.0.0."
elif ip_type_selection == "4":
    priv_ip = str(input("Please enter the first 3 values of your private IP address: "))
else:
    pass

user_input = str(input("Enter IP range (e.g. 0-255): ")) #ip range to scan

user_input = user_input.split("-")

for ping in range (int(user_input[0]), int(user_input[1])+1): #loop over every specified IP address
    ip_addr = priv_ip + str(ping)
    try:
        result = subprocess.check_call(['ping', '-n', '3', ip_addr]) #ping check on every IP address by sending ICMP packages and waiting for responses
    except subprocess.CalledProcessError as e:
        print(f'Run time Error') #Incase Run time error occurs
    
    '''
    if result is 0:
        print(f'ping to {ip_addr} OK')
    elif result is 2:
        print(f'no response from {ip_addr}')
    else:
        print(f'ping to {ip_addr} failed')
    '''
''' '''

