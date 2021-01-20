#GUI_test.py
'''
https://pythonbasics.org/pyqt-list-box/
'''

from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeySequence, QImage, QPixmap
#import threaded_tcp_scan.py

import sys

class ButtonFunctions():
    def __init__(self, *args, **kwargs):
        self.name = "foosball"
    
    def universal_function(self, s):
        print(55) #to check if the buttons work
        
    def quick_pop_up(self): # generates a popup
        msg = QMessageBox()
        msg.setWindowTitle("Quick Scan")
        msg.setText("Select the device to scan")
        x= msg.exec_()
    
    def exit_button(self, s):
        #sys.exit(app.exec_())   program crashes if this button is pressed
        pass
    
    def selected_device(self, device):
        print(device)
    

class MainWindow(QMainWindow, ButtonFunctions): #Inherits attributes from QMainWindow and ButtonFunctions
    
    def __init__(self,*args,**kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        mdi = QMdiArea()
        self.setWindowTitle("Network Scanner") #Application Name
        self.setGeometry(420,220,1080,720) #Set (xpos,ypos,width,height) of application window
        self.setCentralWidget(mdi)
        
        
        toolbar = QToolBar("My Main toolbar")
        self.addToolBar(toolbar)
        
        #actions on toolbar
        quick_action = QAction("Quick Scan", self) #Does a Quick Scan on a network device
        quick_action.triggered.connect(self.quick_pop_up) 
        
        inspect_action = QAction("Inspect", self) #Inspects the properties of a device
        inspect_action.triggered.connect(self.universal_function) #universal'''
        
        scan_action = QAction("Scan", self)
        scan_action.triggered.connect(self.universal_function) #universal'''
        
        stop_action = QAction("Stop", self)
        stop_action.triggered.connect(self.universal_function) #universal'''
        
        toggle_action = QAction ("Pause / Resume", self)
        toggle_action.triggered.connect(self.universal_function) #universal'''
        
        #actions on menubar
        new_action = QAction("New Scan Session", self)
        new_action.triggered.connect(self.universal_function) #universal'''
        
        open_action = QAction("Open.. ", self)
        open_action.triggered.connect(self.universal_function) #universal'''
        
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.universal_function) #universal'''
        exit_action.setShortcut(QKeySequence("Ctrl+Q"))
        
        saveas_action = QAction ("Save as...",self)
        saveas_action.triggered.connect(self.universal_function) #universal'''
        saveas_action.setShortcut(QKeySequence("Ctrl+Shift+S"))
        
        manual_action = QAction ("User manual", self)
        manual_action.triggered.connect(self.universal_function) #universal'''
        
        #Adding buttons onto toolBar
        toolbar.addAction(quick_action)
        toolbar.addAction(inspect_action)
        toolbar.addAction(scan_action)
        toolbar.addAction(stop_action)
        toolbar.addAction(toggle_action)
               
        self.setStatusBar(QStatusBar(self))
        
        #Add Menu Bar
        menu = self.menuBar()
        
        #Menu Bar Options
        file_menu = menu.addMenu("&File")
        
        edit_menu = menu.addMenu("&Edit")
        
        view_menu = menu.addMenu("&View")
        
        tools_menu = menu.addMenu("&Tools")
        
        help_menu = menu.addMenu("&Help")
        
        #Menu Bar Dropdown Options
        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addAction(saveas_action)
        file_menu.addSeparator()
        file_menu.addAction(exit_action)
        
        help_menu.addAction(manual_action)
        
        #List of devices
        device_list = QListWidget()
        device_list.addItems(["Device 1","Device 2","Device 3"])
        device_list.sortItems()
        device_list.clicked.connect(self.selected_device)
        
        #MDI subwindow for device_list
        device_subwindow = QMdiSubWindow()
        device_subwindow.setWidget(device_list)
        device_subwindow.setWindowTitle("Devices")
        mdi.addSubWindow(device_subwindow)
        
        
        #Network Map
        net_map_img = QPixmap("nmap.jpg")
        net_map_label = QLabel()
        net_map = net_map_label.setPixmap(net_map_img)
        #self.setCentralWidget(net_map)
        
        #MDI subwindow for net_map
        net_subwindow = QMdiSubWindow()
        net_subwindow.setWidget(net_map) #Not real network map, placeholder
        net_subwindow.setWindowTitle("Network Map")
        mdi.addSubWindow(net_subwindow)
        
        #Shell
        
        #MDI subwindow for shell
        shell_subwindow = QMdiSubWindow()
        shell_subwindow.setWindowTitle("Shell")
        mdi.addSubWindow(shell_subwindow)
        
        #mdi positioning experiments
        mdi.tileSubWindows()
        mdi.viewMode()
        #test combo box
        '''
        comboBox = QComboBox(self)
        comboBox.addItem("bird")
        comboBox.addItem("Windows")
        comboBox.addItem("CDE")
        comboBox.addItem("Plastique")
        comboBox.addItem("Clean")
        comboBox.addItem("bird")
        
        comboBox.move (50,250)
        '''

class Shell():
    #A class for the shell to interpret command inputs
    def __init__(self):
        pass

class Network_Map():
    #A class for the Network Map (NetworkX)
    pass


    
if __name__ == "__main__":                                
    app = QApplication(sys.argv) #Initialize the app
    window = MainWindow()
    window.show()
    sys.exit(app.exec_()) #so that the program can exit and stop properly once X is pushed
