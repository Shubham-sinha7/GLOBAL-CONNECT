# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zizzyUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_zizzyUi(object):
    def setupUi(self, zizzyUi):
        zizzyUi.setObjectName("zizzyUi")
        zizzyUi.resize(1097, 636)
        self.centralwidget = QtWidgets.QWidget(zizzyUi)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1091, 681))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../gifs/gif3.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(850, 550, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Showcard Gothic")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(940, 550, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Showcard Gothic")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 36, 28);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 241, 181))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../gifs/GIF4.gif"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 460, 251, 171))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../gifs/GIF5.gif"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(890, 20, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Jokerman")
        font.setPointSize(16)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background:transparent;\n"
"border-radius:none;")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(710, 20, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Jokerman")
        font.setPointSize(16)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setStyleSheet("background:transparent;\n"
"border-radius:none;")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(840, 400, 241, 141))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../more gifs/gif12.gif"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(840, 280, 241, 151))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("../more gifs/gif10.gif"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(850, 100, 231, 151))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("../more gifs/gif11.gif"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 250, 301, 171))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("../gifs/load.gif"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        zizzyUi.setCentralWidget(self.centralwidget)

        self.retranslateUi(zizzyUi)
        QtCore.QMetaObject.connectSlotsByName(zizzyUi)

    def retranslateUi(self, zizzyUi):
        _translate = QtCore.QCoreApplication.translate
        zizzyUi.setWindowTitle(_translate("zizzyUi", "MainWindow"))
        self.pushButton.setText(_translate("zizzyUi", "RUN"))
        self.pushButton_2.setText(_translate("zizzyUi", "EXIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    zizzyUi = QtWidgets.QMainWindow()
    ui = Ui_zizzyUi()
    ui.setupUi(zizzyUi)
    zizzyUi.show()
    sys.exit(app.exec_())
