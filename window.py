#!/usr/bin/python
import ctypes
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
so = ctypes.cdll.LoadLibrary('./lib.so')

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Project")
        self.fsbutton = QPushButton(self,text = 'First Sample')
        # self.input = QTextEdit(self)
        # self.input.move(10,10)
        # self.btnhtml=QPushButton(self,text='HTML')
        # self.btnhtml.move(120,10)
        # self.btntxt=QPushButton(self,text='TXT')
        # self.btntxt.move(120,50)
        # self.btnq=QPushButton(self,text="Quit")
        # self.btnq.move(10,50)
        self.setFixedSize(600,400)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()