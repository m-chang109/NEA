import socket

print("Enter an IP address to scan.")
target = input("> ")

print("*" * 40)
print(f'Scanning {target}')
print("*" * 40)

i=0
for port in range (1,1000):
    print(f'Scanning port {port}')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((target,port))
    if result == 0:
        print("Port: " + str(port) + " Open")
        i += 1
    s.close()

print(f'Scan complete: {i} open port(s) found')

'''
20: File Transfer Protocol (FTP) Data Transfer

21: File Transfer Protocol (FTP) Command Control

22: Secure Shell (SSH)

23: Telnet - Remote login service, unencrypted text messages

25: Simple Mail Transfer Protocol (SMTP) E-mail Routing

53: Domain Name System (DNS) service

80: Hypertext Transfer Protocol (HTTP) used in World Wide Web

110: Post Office Protocol (POP3) used by e-mail clients to retrieve e-mail from a server

119: Network News Transfer Protocol (NNTP)

123: Network Time Protocol (NTP)

143: Internet Message Access Protocol (IMAP) Management of Digital Mail

161: Simple Network Management Protocol (SNMP)

194: Internet Relay Chat (IRC)

443: HTTP Secure (HTTPS) HTTP over TLS/SSL
'''
# 
# class PortScan():
#     
#     def port_scanner(targets, ports = [22,23,53,80,443]):
        
        
        