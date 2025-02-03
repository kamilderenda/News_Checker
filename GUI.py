from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1099, 893)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Blue background
        self.centralwidget.setStyleSheet("background-color: #3a78d3;")

        # Labels for Title and Article text
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 1081, 81))
        self.label.setObjectName("label")
        self.label.setStyleSheet("color: white; font-size: 20px;")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 1081, 51))
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("color: white; font-size: 16px;")

        # Text input for Title
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 160, 1071, 87))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setStyleSheet("font-size: 16px;")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 250, 1081, 51))
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("color: white; font-size: 16px;")

        # Text input for article text
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 310, 1071, 87))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setStyleSheet("font-size: 16px;")

        # Button to check the article
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(390, 660, 341, 141))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("background-color: #ffcc00; font-size: 20px; color: white;")

        # Label to display the result
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 440, 1061, 181))
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet("color: white; font-size: 30px; font-weight: bold;")

        # Setting the central widget
        MainWindow.setCentralWidget(self.centralwidget)

        # Menu bar and status bar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1099, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect the button click to the function
        self.pushButton.clicked.connect(self.check_fake_news)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fake News Classifier"))
        self.label.setText(_translate("MainWindow", "Check the Article: Is it Fake or Real?"))
        self.label_2.setText(_translate("MainWindow", "Enter the Title"))
        self.label_3.setText(_translate("MainWindow", "Enter the Article Text"))
        self.pushButton.setText(_translate("MainWindow", "Check"))
        self.label_4.setText(_translate("MainWindow", ""))  # Empty initially