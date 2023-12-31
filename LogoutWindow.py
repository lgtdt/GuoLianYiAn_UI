# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\designer\LogoutWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LogoutWindow(object):
    def setupUi(self, LogoutWindow):
        LogoutWindow.setObjectName("LogoutWindow")
        LogoutWindow.resize(380, 325)
        self.BackGroundFrame = QtWidgets.QFrame(LogoutWindow)
        self.BackGroundFrame.setGeometry(QtCore.QRect(0, 0, 380, 325))
        self.BackGroundFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BackGroundFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.BackGroundFrame.setObjectName("BackGroundFrame")
        self.TopFrame = QtWidgets.QFrame(self.BackGroundFrame)
        self.TopFrame.setGeometry(QtCore.QRect(0, 0, 380, 50))
        self.TopFrame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.477273, x2:1, y2:0.471591, stop:0 rgba(80, 174, 247, 255), stop:1 rgba(15, 143, 242, 255));\n"
"border: none;")
        self.TopFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TopFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TopFrame.setObjectName("TopFrame")
        self.LoginNameLabel = QtWidgets.QLabel(self.TopFrame)
        self.LoginNameLabel.setGeometry(QtCore.QRect(20, 15, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.LoginNameLabel.setFont(font)
        self.LoginNameLabel.setStyleSheet("background-color: transparent;\n"
"font-size:17px;")
        self.LoginNameLabel.setObjectName("LoginNameLabel")
        self.CloseButton = QtWidgets.QPushButton(self.TopFrame)
        self.CloseButton.setGeometry(QtCore.QRect(330, 10, 30, 30))
        self.CloseButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CloseButton.setStyleSheet("background-color: transparent;")
        self.CloseButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\designer\\../statics/imgs/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CloseButton.setIcon(icon)
        self.CloseButton.setIconSize(QtCore.QSize(23, 23))
        self.CloseButton.setObjectName("CloseButton")
        self.BodyFrame = QtWidgets.QFrame(self.BackGroundFrame)
        self.BodyFrame.setGeometry(QtCore.QRect(0, 50, 380, 275))
        self.BodyFrame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:none;")
        self.BodyFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BodyFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.BodyFrame.setObjectName("BodyFrame")
        self.TitleLabel = QtWidgets.QLabel(self.BodyFrame)
        self.TitleLabel.setGeometry(QtCore.QRect(50, 20, 271, 29))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        self.TitleLabel.setFont(font)
        self.TitleLabel.setStyleSheet("color: rgb(0, 0, 0);\n"
"font-size:22px;")
        self.TitleLabel.setObjectName("TitleLabel")
        self.VersionLabel = QtWidgets.QLabel(self.BodyFrame)
        self.VersionLabel.setGeometry(QtCore.QRect(160, 54, 66, 27))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.VersionLabel.setFont(font)
        self.VersionLabel.setStyleSheet("color: rgb(43, 128, 247);\n"
"background-color: rgb(233, 242, 254);\n"
"border-radius: 13;\n"
"font-size:14px;")
        self.VersionLabel.setObjectName("VersionLabel")
        self.PasswordFrame = QtWidgets.QFrame(self.BodyFrame)
        self.PasswordFrame.setGeometry(QtCore.QRect(40, 120, 301, 36))
        self.PasswordFrame.setStyleSheet("background-color: rgb(245, 245, 245);\n"
"border: none;")
        self.PasswordFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PasswordFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PasswordFrame.setObjectName("PasswordFrame")
        self.PasswordInput = QtWidgets.QLineEdit(self.PasswordFrame)
        self.PasswordInput.setGeometry(QtCore.QRect(40, 0, 261, 36))
        self.PasswordInput.setStyleSheet("color: black;\n"
"border: none;")
        self.PasswordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PasswordInput.setObjectName("PasswordInput")
        self.PasswordIcon = QtWidgets.QLabel(self.PasswordFrame)
        self.PasswordIcon.setGeometry(QtCore.QRect(8, 7, 20, 22))
        self.PasswordIcon.setText("")
        self.PasswordIcon.setPixmap(QtGui.QPixmap(".\\designer\\../statics/imgs/passinput.png"))
        self.PasswordIcon.setScaledContents(True)
        self.PasswordIcon.setObjectName("PasswordIcon")
        self.ConfirmButton = QtWidgets.QPushButton(self.BodyFrame)
        self.ConfirmButton.setGeometry(QtCore.QRect(140, 220, 100, 32))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.ConfirmButton.setFont(font)
        self.ConfirmButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ConfirmButton.setStyleSheet("QPushButton{\n"
"    font-size:17px;\n"
"    border: none;\n"
"    border-radius: 15;\n"
"    background-color: rgb(43, 128, 247);\n"
"}\n"
":hover{\n"
"    font-size:17px;\n"
"    background-color: rgb(146, 212, 255);\n"
"}\n"
"\n"
"\n"
"")
        self.ConfirmButton.setObjectName("ConfirmButton")
        self.MessageLabel = QtWidgets.QLabel(self.BodyFrame)
        self.MessageLabel.setGeometry(QtCore.QRect(40, 160, 291, 16))
        self.MessageLabel.setStyleSheet("color: red;\n"
"font-size:13px;")
        self.MessageLabel.setObjectName("MessageLabel")
        self.label = QtWidgets.QLabel(self.BodyFrame)
        self.label.setGeometry(QtCore.QRect(40, 90, 291, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setStyleSheet("color: red;\n"
"font-size:16px;")
        self.label.setObjectName("label")

        self.retranslateUi(LogoutWindow)
        QtCore.QMetaObject.connectSlotsByName(LogoutWindow)

    def retranslateUi(self, LogoutWindow):
        _translate = QtCore.QCoreApplication.translate
        LogoutWindow.setWindowTitle(_translate("LogoutWindow", "Form"))
        self.LoginNameLabel.setText(_translate("LogoutWindow", "登出"))
        self.TitleLabel.setText(_translate("LogoutWindow", "国联恶意代码辅助监测系统"))
        self.VersionLabel.setText(_translate("LogoutWindow", "   主机版"))
        self.PasswordInput.setPlaceholderText(_translate("LogoutWindow", "密码"))
        self.ConfirmButton.setText(_translate("LogoutWindow", "确认"))
        self.MessageLabel.setText(_translate("LogoutWindow", "MessageLabel"))
        self.label.setText(_translate("LogoutWindow", "确认密码"))
