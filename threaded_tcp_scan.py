#threaded_tcp_scan.py

import argparse
import threading
import socket

results = threading.Semaphore(value=1)

def connScan(Host, Port): #TCP connect scan for a specific port (Host is string, Port is int)
    try: #try to do a TCP connection with specified port
        connSkt = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Define port
        connSkt.connect_ex((Host, Port)) #connect to the port and check if it is open
        #connSkt.send('Dummy Message')
        #reply = connSkt.recv(100) #wait for 100 milliseconds for a reply
        print(f'{Port} is open')
        #results.acquire() #Makes a log of the results
    except: #If the port doesn't connect
        print(f'{Port} is closed')
        #results.acquire() 
    finally:
        #results.release() #Release all results
        connSkt.close()
    return None

def portScan(HostIP, Ports): 
    try: #Try to get name of device
        hostName = socket.gethostbyname(HostIP) 
    except:
        print("Unknown host")
        return None
    try: 
        hostIP = socket.gethostbyaddr(hostName)
        print(f'Scan Result for device: {hostName}')
    except:
        print(f'Scan Result for: {hostIP}')
    socket.setdefaulttimeout(10)
    for port in Ports:
        print(f'Scanning port {port}')
        thread = threading.Thread(target=connScan, args=(HostIP, port)) #threads scan
        thread.start()
    

    
    
        