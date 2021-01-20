#network_map.py

import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network
from subprocess import Popen, PIPE
G = nx.Graph()

G.add_node("Device 1", label = "Macbook")
G.add_node("Device 2", label = "Raspberry Pi")
G.add_node("Device 3", label = "Synology")
G.add_node("Device 4", label = "Apple TV")
G.add_node("Device 5", label = "iPhone")
G.add_node("Device 6", label = "Windows")
G.add_node("Device 7", label = "Desktop")
G.add_node("Router")

G.add_edges_from([("Router","Device 1"),("Router","Device 2"),("Router","Device 3"),("Router","Device 4"),("Router","Device 5"),("Router","Device 6"),("Router","Device 7")])

nx.draw(G)
plt.savefig("network.png")
plt.show()
    
class Device():
    
    def __init__(self,ip_address,mac_address,hostname,device_type):
        self.ip_address = ip_address
        self.mac_address = mac_address
        self.hostname = hostname
        self.device_type = device_type
    
    def __repr__(self):
        return f'Device Name: {self.hostname}\nIP Address:{self.ip_address}'
    
    def getIPAddress(self):
        return self.ip_address
    
    def getMACAddress(self):
        return self.mac_address
    
    def getHostName(self):
        return self.hostname
    
class CentralNode(Device):
    
    def __init__(self,connected_devices):
        self.connected_devices = connected_devices

d1 = Device("192.168.1.44","65:2A:4B:2F:33","LAPTOP","Laptop")