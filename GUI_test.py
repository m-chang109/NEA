#GUI_test.py
from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys

class ButtonFunctions():
    def __init__(self, *args, **kwargs):
        self.name = "foo"
        #testbutton = QtWidgets.QPushButton(MainWindow)
        #testbutton.setText("click me")
    
    def universal_function(self, s):
        print("click",s)
        
    def quick_pop_up(self): # generates a popup
        msg = QMessageBox()
        msg.setWindowTitle("Quick Scan")
        msg.setText("Select the device to scan")
        x= msg.exec_()
    

class MainWindow(QMainWindow, ButtonFunctions): #Inherits attributes from QMainWindow and Button Functions
    
    def __init__(self,*args,**kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        self.setWindowTitle("Network Scanner") #Application Name
        self.setGeometry(420,220,1080,720) #Set (xpos,ypos,width,height) of application window
        
        label = QLabel("test")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)
        
        toolbar = QToolBar("My Main toolbar")
        self.addToolBar(toolbar)
        
        #buttons on toolBar
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
        #file_menu.addAction
        
        
        edit_menu = menu.addMenu("&Edit")
        
        
        view_menu = menu.addMenu("&View")
        
        tools_menu = menu.addMenu("&Tools")
        

        #test combo box
        comboBox = QComboBox(self)
        comboBox.addItem("bird")
        comboBox.addItem("Windows")
        comboBox.addItem("CDE")
        comboBox.addItem("Plastique")
        comboBox.addItem("Clean")
        comboBox.addItem("bird")
        
        comboBox.move (50,250)


  
        
        



if __name__ == "__main__":                                
    app = QApplication(sys.argv) #Initialize the app
    window = MainWindow()
    window.show()
    sys.exit(app.exec_()) #so that the software can exit properly once X is pushed
