#GUI_test.py
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys


class MainWindow(QMainWindow):
    
    def __init__(self,*args,**kwargs):
        app = QApplication(sys.argv) #Initialize the app
        super(MainWindow, self).__init__(*args, **kwargs)
        
        self.setWindowTitle("Network Scanner") #Application Name
        self.setGeometry(420,220,1080,720) #Set (xpos,ypos,width,height) of application window
        self.show()
        
        label = QLabel("test")
        
        label.setAlignment(Qt.AlignCenter)
        
        self.setCentralWidget(label)
        
        self.windowTitleChanged.connect(lambda x: self.afunction())
        sys.exit(app.exec_()) #so that the software can exit properly once X is pushed
        





MainWindow()


