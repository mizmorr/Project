# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import ctypes, time
so = ctypes.cdll.LoadLibrary('./lib.so')

def strconv(s):
    farr  = s.split('\n')
    list.reverse(farr)
    time2 = list.pop(farr)
    list.reverse(farr)
    fstring = '\n'.join(farr) 
    return time2, fstring

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(699, 853)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(26, 95, 180))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(145, 145, 144))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(145, 145, 144))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        MainWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        icon = QtGui.QIcon.fromTheme("applications-science")
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 70, 291, 321))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(150, 130, 131, 61))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(10, 130, 124, 19))
        self.label_6.setObjectName("label_6")
        self.spinBox_2 = QtWidgets.QSpinBox(self.tab)
        self.spinBox_2.setGeometry(QtCore.QRect(10, 70, 121, 28))
        self.spinBox_2.setObjectName("spinBox_2")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(160, 70, 111, 18))
        self.label_7.setObjectName("label_7")
        self.progressBar_2 = QtWidgets.QProgressBar(self.tab)
        self.progressBar_2.setGeometry(QtCore.QRect(10, 184, 103, 27))
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName("progressBar_2")
        self.pushButton_9 = QtWidgets.QPushButton(self.tab)
        self.pushButton_9.setGeometry(QtCore.QRect(210, 250, 71, 31))
        self.pushButton_9.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_9.setIcon(icon)
        self.pushButton_9.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_9.setObjectName("pushButton_9")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(160, 70, 111, 18))
        self.label_10.setObjectName("label_10")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(150, 130, 131, 61))
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.spinBox_3 = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox_3.setGeometry(QtCore.QRect(10, 70, 121, 28))
        self.spinBox_3.setObjectName("spinBox_3")
        self.progressBar_3 = QtWidgets.QProgressBar(self.tab_2)
        self.progressBar_3.setGeometry(QtCore.QRect(10, 184, 103, 27))
        self.progressBar_3.setProperty("value", 0)
        self.progressBar_3.setObjectName("progressBar_3")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(10, 130, 124, 19))
        self.label_9.setObjectName("label_9")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_8.setGeometry(QtCore.QRect(210, 250, 71, 31))
        self.pushButton_8.setText("")
        self.pushButton_8.setIcon(icon)
        self.pushButton_8.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_8.setObjectName("pushButton_8")
        self.tabWidget.addTab(self.tab_2, "")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(370, 70, 291, 321))
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_4.setGeometry(QtCore.QRect(210, 280, 71, 31))
        self.pushButton_4.setText("")
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        self.spinBox_4 = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_4.setGeometry(QtCore.QRect(10, 100, 121, 28))
        self.spinBox_4.setObjectName("spinBox_4")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(10, 160, 124, 19))
        self.label_11.setObjectName("label_11")
        self.progressBar_4 = QtWidgets.QProgressBar(self.groupBox_2)
        self.progressBar_4.setGeometry(QtCore.QRect(10, 224, 103, 27))
        self.progressBar_4.setProperty("value", 0)
        self.progressBar_4.setObjectName("progressBar_4")
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(160, 160, 121, 61))
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setGeometry(QtCore.QRect(170, 100, 111, 18))
        self.label_13.setObjectName("label_13")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(370, 470, 291, 311))
        self.groupBox_3.setObjectName("groupBox_3")
        self.spinBox_5 = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_5.setGeometry(QtCore.QRect(10, 50, 131, 28))
        self.spinBox_5.setObjectName("spinBox_5")
        self.label_16 = QtWidgets.QLabel(self.groupBox_3)
        self.label_16.setGeometry(QtCore.QRect(150, 50, 111, 18))
        self.label_16.setObjectName("label_16")
        self.label_14 = QtWidgets.QLabel(self.groupBox_3)
        self.label_14.setGeometry(QtCore.QRect(150, 120, 131, 71))
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.groupBox_3)
        self.label_15.setGeometry(QtCore.QRect(10, 82, 131, 88))
        self.label_15.setObjectName("label_15")
        self.progressBar_5 = QtWidgets.QProgressBar(self.groupBox_3)
        self.progressBar_5.setGeometry(QtCore.QRect(10, 174, 131, 27))
        self.progressBar_5.setProperty("value", 0)
        self.progressBar_5.setObjectName("progressBar_5")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_5.setGeometry(QtCore.QRect(210, 270, 71, 31))
        self.pushButton_5.setText("")
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_5.setObjectName("pushButton_5")
        self.toolBox = QtWidgets.QToolBox(self.centralwidget)
        self.toolBox.setGeometry(QtCore.QRect(20, 470, 291, 321))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(26, 95, 180))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 245, 244))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 113, 216))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(26, 95, 180))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(145, 145, 144))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(214, 214, 214))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(145, 145, 144))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(145, 145, 144))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(246, 245, 244))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(145, 145, 144))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.toolBox.setPalette(palette)
        self.toolBox.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 291, 255))
        self.page.setObjectName("page")
        self.progressBar_6 = QtWidgets.QProgressBar(self.page)
        self.progressBar_6.setGeometry(QtCore.QRect(10, 130, 121, 23))
        self.progressBar_6.setProperty("value", 0)
        self.progressBar_6.setObjectName("progressBar_6")
        self.label_20 = QtWidgets.QLabel(self.page)
        self.label_20.setGeometry(QtCore.QRect(160, 60, 111, 18))
        self.label_20.setObjectName("label_20")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.page)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(10, 180, 161, 71))
        self.plainTextEdit_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.plainTextEdit_2.setReadOnly(True)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.label_17 = QtWidgets.QLabel(self.page)
        self.label_17.setGeometry(QtCore.QRect(190, 180, 66, 18))
        self.label_17.setObjectName("label_17")
        self.spinBox_6 = QtWidgets.QSpinBox(self.page)
        self.spinBox_6.setGeometry(QtCore.QRect(10, 60, 121, 31))
        self.spinBox_6.setObjectName("spinBox_6")
        self.pushButton_6 = QtWidgets.QPushButton(self.page)
        self.pushButton_6.setGeometry(QtCore.QRect(10, 0, 111, 31))
        self.pushButton_6.setText("")
        self.pushButton_6.setIcon(icon)
        self.pushButton_6.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_19 = QtWidgets.QLabel(self.page)
        self.label_19.setGeometry(QtCore.QRect(10, 100, 131, 18))
        self.label_19.setObjectName("label_19")
        self.label_18 = QtWidgets.QLabel(self.page)
        self.label_18.setGeometry(QtCore.QRect(150, 100, 131, 21))
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 291, 255))
        self.page_2.setObjectName("page_2")
        self.label_24 = QtWidgets.QLabel(self.page_2)
        self.label_24.setGeometry(QtCore.QRect(150, 100, 131, 31))
        self.label_24.setText("")
        self.label_24.setObjectName("label_24")
        self.label_21 = QtWidgets.QLabel(self.page_2)
        self.label_21.setGeometry(QtCore.QRect(150, 60, 111, 18))
        self.label_21.setObjectName("label_21")
        self.pushButton_7 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 0, 111, 31))
        self.pushButton_7.setText("")
        self.pushButton_7.setIcon(icon)
        self.pushButton_7.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_7.setObjectName("pushButton_7")
        self.progressBar_7 = QtWidgets.QProgressBar(self.page_2)
        self.progressBar_7.setGeometry(QtCore.QRect(10, 130, 121, 23))
        self.progressBar_7.setProperty("value", 0)
        self.progressBar_7.setObjectName("progressBar_7")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.page_2)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(10, 180, 161, 51))
        self.plainTextEdit_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.plainTextEdit_3.setReadOnly(True)
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.label_23 = QtWidgets.QLabel(self.page_2)
        self.label_23.setGeometry(QtCore.QRect(10, 100, 131, 18))
        self.label_23.setObjectName("label_23")
        self.label_22 = QtWidgets.QLabel(self.page_2)
        self.label_22.setGeometry(QtCore.QRect(180, 180, 66, 18))
        self.label_22.setObjectName("label_22")
        self.spinBox_7 = QtWidgets.QSpinBox(self.page_2)
        self.spinBox_7.setGeometry(QtCore.QRect(10, 60, 121, 31))
        self.spinBox_7.setObjectName("spinBox_7")
        self.toolBox.addItem(self.page_2, "")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 161, 21))
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 30, 641, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 410, 66, 18))
        self.label_2.setObjectName("label_2")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(20, 430, 641, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 699, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton_6.released.connect(self.btnFirst_go)
        self.pushButton_7.released.connect(self.btnSecond_go)

    def btnFirst_go(self):
            fs = so.firstSample 
            num = self.spinBox_6.value()
            fs.restype = ctypes.c_void_p
            fs.argtypes=[ctypes.c_int]
            fsout = fs(num)
            self.progressBar_6.setValue(0)
            time.sleep(0.025)
            self.progressBar_6.setValue(100)
            fbytes = ctypes.string_at(fsout)
            fstring = fbytes.decode('utf-8')
            time2,fstring = strconv(fstring)
            if fstring=="no such k-core found\n":
                 self.label_18.setText("")
            else:
                self.label_18.setText(time2)
            self.plainTextEdit_2.setPlainText(fstring)
    
    def btnSecond_go(self):
            fs = so.SecondSample 
            num = self.spinBox_7.value()
            fs.restype = ctypes.c_void_p
            fs.argtypes=[ctypes.c_int]
            fsout = fs(num)
            self.progressBar_7.setValue(0)
            time.sleep(0.025)
            self.progressBar_7.setValue(100)
            fbytes = ctypes.string_at(fsout)
            fstring = fbytes.decode('utf-8')
            time2,fstring = strconv(fstring)
            if fstring=="no such k-core found\n":
                 self.label_24.setText("")
            else:
                self.label_24.setText(time2)
            self.plainTextEdit_3.setPlainText(fstring)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Decomposition"))
        self.label_6.setText(_translate("MainWindow", "Time processing"))
        self.label_7.setText(_translate("MainWindow", "Set parameter"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Big Density"))
        self.label_10.setText(_translate("MainWindow", "Set parameter"))
        self.label_9.setText(_translate("MainWindow", "Time processing"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Almost sparse"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Erdos-Renyi"))
        self.label_11.setText(_translate("MainWindow", "Time processing"))
        self.label_13.setText(_translate("MainWindow", "Set parameter"))
        self.groupBox_3.setTitle(_translate("MainWindow", "LastFm_Sample"))
        self.label_16.setText(_translate("MainWindow", "Set parameter"))
        self.label_15.setText(_translate("MainWindow", "Time processing"))
        self.label_20.setText(_translate("MainWindow", "Set parameter"))
        self.label_17.setText(_translate("MainWindow", "Result"))
        self.label_19.setText(_translate("MainWindow", "Time processing"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "First sample"))
        self.label_21.setText(_translate("MainWindow", "Set parameter"))
        self.label_23.setText(_translate("MainWindow", "Time processing"))
        self.label_22.setText(_translate("MainWindow", "Result"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "Second sample"))
        self.label.setText(_translate("MainWindow", "Random generators"))
        self.label_2.setText(_translate("MainWindow", "Samples"))
