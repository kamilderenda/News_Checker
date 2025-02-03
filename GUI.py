from PyQt5 import QtCore, QtGui, QtWidgets
import Model

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1099, 893)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: #3a78d3;")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 1081, 81))
        self.label.setStyleSheet("color: white; font-size: 20px;")
        self.label.setText("Check the Article: Is it Fake or Real?")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 1081, 51))
        self.label_2.setStyleSheet("color: white; font-size: 16px;")
        self.label_2.setText("Enter the Title")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 250, 1081, 51))
        self.label_3.setStyleSheet("color: white; font-size: 16px;")
        self.label_3.setText("Enter the Article Text")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 160, 1071, 87))
        self.textEdit.setStyleSheet("font-size: 16px;")

        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 310, 1071, 87))
        self.textEdit_2.setStyleSheet("font-size: 16px;")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(390, 660, 341, 141))
        self.pushButton.setStyleSheet("background-color: #ffcc00; font-size: 20px; color: white;")
        self.pushButton.setText("Check")
        self.pushButton.clicked.connect(self.check_fake_news)

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 440, 1061, 181))
        self.label_4.setStyleSheet("color: white; font-size: 30px; font-weight: bold; text-align: center;")
        self.label_4.setText("")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

    def check_fake_news(self):
        title = self.textEdit.toPlainText()
        article_text = self.textEdit_2.toPlainText()

        if title.strip() == "" or article_text.strip() == "":
            self.label_4.setText("Please enter both title and article text!")
            self.label_4.setStyleSheet("color: yellow; font-size: 30px; font-weight: bold;")
            return

        result = Model.check_fake_news(title, article_text)

        if result == "FAKE":
            self.label_4.setText("FAKE NEWS")
            self.label_4.setStyleSheet("color: red; font-size: 30px; font-weight: bold;")
        else:
            self.label_4.setText("APPROVED")
            self.label_4.setStyleSheet("color: green; font-size: 30px; font-weight: bold;")
