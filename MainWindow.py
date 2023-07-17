# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        MainWindow.setStyleSheet("border: none;")
        self.BackGroundFrame = QtWidgets.QFrame(MainWindow)
        self.BackGroundFrame.setGeometry(QtCore.QRect(0, 0, 900, 600))
        self.BackGroundFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BackGroundFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.BackGroundFrame.setObjectName("BackGroundFrame")
        self.TopFrame = QtWidgets.QFrame(self.BackGroundFrame)
        self.TopFrame.setGeometry(QtCore.QRect(0, 0, 900, 120))
        self.TopFrame.setStyleSheet("background-color: rgb(102, 169, 239);\n"
"border: none;")
        self.TopFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TopFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TopFrame.setObjectName("TopFrame")
        self.LogoFrame = QtWidgets.QFrame(self.TopFrame)
        self.LogoFrame.setGeometry(QtCore.QRect(0, 0, 300, 120))
        self.LogoFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LogoFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LogoFrame.setObjectName("LogoFrame")
        self.TitleLabel = QtWidgets.QLabel(self.LogoFrame)
        self.TitleLabel.setGeometry(QtCore.QRect(30, 25, 131, 36))
        font = QtGui.QFont()
        font.setFamily("YouSheBiaoTiHei")
        font.setPointSize(35)
        self.TitleLabel.setFont(font)
        self.TitleLabel.setStyleSheet("background-color: transparent;\n"
"")
        self.TitleLabel.setObjectName("TitleLabel")
        self.VersionLabel = QtWidgets.QLabel(self.LogoFrame)
        self.VersionLabel.setGeometry(QtCore.QRect(170, 35, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.VersionLabel.setFont(font)
        self.VersionLabel.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.505682, stop:0 rgba(250, 193, 31, 255), stop:1 rgba(252, 228, 4, 255));\n"
"color: rgb(156, 69, 21);\n"
"border-radius: 10;")
        self.VersionLabel.setObjectName("VersionLabel")
        self.SloganLabel = QtWidgets.QLabel(self.LogoFrame)
        self.SloganLabel.setGeometry(QtCore.QRect(30, 70, 171, 16))
        font = QtGui.QFont()
        font.setFamily("YouSheBiaoTiHei")
        font.setPointSize(18)
        self.SloganLabel.setFont(font)
        self.SloganLabel.setObjectName("SloganLabel")
        self.ButtonFrame = QtWidgets.QFrame(self.TopFrame)
        self.ButtonFrame.setGeometry(QtCore.QRect(300, 0, 360, 120))
        self.ButtonFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ButtonFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ButtonFrame.setObjectName("ButtonFrame")
        self.ToolsButton = QtWidgets.QPushButton(self.ButtonFrame)
        self.ToolsButton.setGeometry(QtCore.QRect(120, 0, 120, 120))
        self.ToolsButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ToolsButton.setStyleSheet(":hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0.985075, y1:1, x2:1, y2:0, stop:0 rgba(118, 180, 242, 255), stop:1 rgba(167, 203, 240, 255));\n"
"}")
        self.ToolsButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./statics/imgs/tool.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ToolsButton.setIcon(icon)
        self.ToolsButton.setIconSize(QtCore.QSize(30, 30))
        self.ToolsButton.setObjectName("ToolsButton")
        self.UserButton = QtWidgets.QPushButton(self.ButtonFrame)
        self.UserButton.setGeometry(QtCore.QRect(240, 0, 120, 120))
        self.UserButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.UserButton.setStyleSheet(":hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0.985075, y1:1, x2:1, y2:0, stop:0 rgba(118, 180, 242, 255), stop:1 rgba(167, 203, 240, 255));\n"
"}")
        self.UserButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./statics/imgs/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.UserButton.setIcon(icon1)
        self.UserButton.setIconSize(QtCore.QSize(30, 30))
        self.UserButton.setObjectName("UserButton")
        self.KillButton = QtWidgets.QPushButton(self.ButtonFrame)
        self.KillButton.setGeometry(QtCore.QRect(0, 0, 120, 120))
        self.KillButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.KillButton.setStyleSheet(":hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0.985075, y1:1, x2:1, y2:0, stop:0 rgba(118, 180, 242, 255), stop:1 rgba(167, 203, 240, 255));\n"
"}")
        self.KillButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./statics/imgs/Lock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.KillButton.setIcon(icon2)
        self.KillButton.setIconSize(QtCore.QSize(30, 30))
        self.KillButton.setObjectName("KillButton")
        self.KillButtonName = QtWidgets.QLabel(self.ButtonFrame)
        self.KillButtonName.setGeometry(QtCore.QRect(21, 88, 81, 16))
        self.KillButtonName.setStyleSheet("background-color: transparent;")
        self.KillButtonName.setObjectName("KillButtonName")
        self.ToolsButtonName = QtWidgets.QLabel(self.ButtonFrame)
        self.ToolsButtonName.setGeometry(QtCore.QRect(156, 88, 61, 16))
        self.ToolsButtonName.setStyleSheet("background-color: transparent;")
        self.ToolsButtonName.setObjectName("ToolsButtonName")
        self.UserButtonName = QtWidgets.QLabel(self.ButtonFrame)
        self.UserButtonName.setGeometry(QtCore.QRect(273, 88, 61, 16))
        self.UserButtonName.setStyleSheet("background-color: transparent;")
        self.UserButtonName.setObjectName("UserButtonName")
        self.MenuFrame = QtWidgets.QFrame(self.TopFrame)
        self.MenuFrame.setGeometry(QtCore.QRect(660, 0, 240, 120))
        self.MenuFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MenuFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MenuFrame.setObjectName("MenuFrame")
        self.CloseButton = QtWidgets.QPushButton(self.MenuFrame)
        self.CloseButton.setGeometry(QtCore.QRect(195, 5, 30, 30))
        self.CloseButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CloseButton.setStyleSheet(":hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0.985075, y1:1, x2:1, y2:0, stop:0 rgba(118, 180, 242, 255), stop:1 rgba(167, 203, 240, 255));\n"
"}")
        self.CloseButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./statics/imgs/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CloseButton.setIcon(icon3)
        self.CloseButton.setIconSize(QtCore.QSize(23, 23))
        self.CloseButton.setObjectName("CloseButton")
        self.MiniButtuon = QtWidgets.QPushButton(self.MenuFrame)
        self.MiniButtuon.setGeometry(QtCore.QRect(155, 5, 30, 30))
        self.MiniButtuon.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.MiniButtuon.setStyleSheet(":hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0.985075, y1:1, x2:1, y2:0, stop:0 rgba(118, 180, 242, 255), stop:1 rgba(167, 203, 240, 255));\n"
"}")
        self.MiniButtuon.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("./statics/imgs/mini.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MiniButtuon.setIcon(icon4)
        self.MiniButtuon.setIconSize(QtCore.QSize(18, 18))
        self.MiniButtuon.setObjectName("MiniButtuon")
        self.SetButtuon = QtWidgets.QPushButton(self.MenuFrame)
        self.SetButtuon.setGeometry(QtCore.QRect(115, 5, 30, 30))
        self.SetButtuon.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SetButtuon.setStyleSheet(":hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0.985075, y1:1, x2:1, y2:0, stop:0 rgba(118, 180, 242, 255), stop:1 rgba(167, 203, 240, 255));\n"
"}")
        self.SetButtuon.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("./statics/imgs/more.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SetButtuon.setIcon(icon5)
        self.SetButtuon.setIconSize(QtCore.QSize(20, 20))
        self.SetButtuon.setObjectName("SetButtuon")
        self.SkinButton = QtWidgets.QPushButton(self.MenuFrame)
        self.SkinButton.setGeometry(QtCore.QRect(75, 5, 30, 30))
        self.SkinButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SkinButton.setStyleSheet(":hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0.985075, y1:1, x2:1, y2:0, stop:0 rgba(118, 180, 242, 255), stop:1 rgba(167, 203, 240, 255));\n"
"}")
        self.SkinButton.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("./statics/imgs/skin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SkinButton.setIcon(icon6)
        self.SkinButton.setIconSize(QtCore.QSize(20, 20))
        self.SkinButton.setObjectName("SkinButton")
        self.LoginButton = QtWidgets.QPushButton(self.MenuFrame)
        self.LoginButton.setGeometry(QtCore.QRect(165, 70, 60, 30))
        self.LoginButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.LoginButton.setStyleSheet("QPushButton{\n"
"    color: yellow;\n"
"    border-radius: 15;\n"
"}\n"
":hover{\n"
"    background-color: rgb(145, 193, 243);\n"
"}")
        self.LoginButton.setObjectName("LoginButton")
        self.label = QtWidgets.QLabel(self.MenuFrame)
        self.label.setGeometry(QtCore.QRect(90, 70, 52, 30))
        self.label.setObjectName("label")
        self.AvatarLabel = QtWidgets.QLabel(self.MenuFrame)
        self.AvatarLabel.setGeometry(QtCore.QRect(40, 60, 40, 40))
        self.AvatarLabel.setText("")
        self.AvatarLabel.setObjectName("AvatarLabel")
        self.AvatarLabel.setStyleSheet("border-image: url(./statics/imgs/avatar.png)")
        self.line = QtWidgets.QFrame(self.MenuFrame)
        self.line.setEnabled(True)
        self.line.setGeometry(QtCore.QRect(160, 75, 2, 20))
        self.line.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.BodyFrame = QtWidgets.QFrame(self.BackGroundFrame)
        self.BodyFrame.setGeometry(QtCore.QRect(0, 120, 900, 480))
        self.BodyFrame.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0, cy:1, radius:1.02262, fx:0, fy:1, stop:0 rgba(60, 86, 222, 255), stop:0.995025 rgba(138, 206, 253, 250));\n"
"border: none;")
        self.BodyFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BodyFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.BodyFrame.setObjectName("BodyFrame")
        self.UpperFrame = QtWidgets.QFrame(self.BodyFrame)
        self.UpperFrame.setGeometry(QtCore.QRect(0, 0, 900, 240))
        self.UpperFrame.setStyleSheet("background-color: transparent;")
        self.UpperFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.UpperFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.UpperFrame.setObjectName("UpperFrame")
        self.TextFrame = QtWidgets.QFrame(self.UpperFrame)
        self.TextFrame.setGeometry(QtCore.QRect(350, 20, 541, 211))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        self.TextFrame.setFont(font)
        self.TextFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TextFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TextFrame.setObjectName("TextFrame")
        self.WarningLabel = QtWidgets.QLabel(self.TextFrame)
        self.WarningLabel.setGeometry(QtCore.QRect(10, 45, 461, 41))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.WarningLabel.setFont(font)
        self.WarningLabel.setObjectName("WarningLabel")
        self.describe1 = QtWidgets.QLabel(self.TextFrame)
        self.describe1.setGeometry(QtCore.QRect(10, 100, 91, 16))
        self.describe1.setObjectName("describe1")
        self.DaysLabel = QtWidgets.QLabel(self.TextFrame)
        self.DaysLabel.setGeometry(QtCore.QRect(110, 100, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.DaysLabel.setFont(font)
        self.DaysLabel.setStyleSheet("color: rgb(252, 225, 7);")
        self.DaysLabel.setObjectName("DaysLabel")
        self.describe2 = QtWidgets.QLabel(self.TextFrame)
        self.describe2.setGeometry(QtCore.QRect(150, 100, 121, 16))
        self.describe2.setObjectName("describe2")
        self.TimesLabel = QtWidgets.QLabel(self.TextFrame)
        self.TimesLabel.setGeometry(QtCore.QRect(280, 100, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.TimesLabel.setFont(font)
        self.TimesLabel.setStyleSheet("color: rgb(252, 225, 7);")
        self.TimesLabel.setObjectName("TimesLabel")
        self.describe3 = QtWidgets.QLabel(self.TextFrame)
        self.describe3.setGeometry(QtCore.QRect(310, 100, 81, 16))
        self.describe3.setObjectName("describe3")
        self.DateLabel = QtWidgets.QLabel(self.TextFrame)
        self.DateLabel.setGeometry(QtCore.QRect(390, 100, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.DateLabel.setFont(font)
        self.DateLabel.setStyleSheet("color: rgb(252, 225, 7);")
        self.DateLabel.setObjectName("DateLabel")
        self.describe4 = QtWidgets.QLabel(self.TextFrame)
        self.describe4.setGeometry(QtCore.QRect(10, 160, 91, 16))
        self.describe4.setObjectName("describe4")
        self.TotelLabel = QtWidgets.QLabel(self.TextFrame)
        self.TotelLabel.setGeometry(QtCore.QRect(110, 159, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.TotelLabel.setFont(font)
        self.TotelLabel.setStyleSheet("color: rgb(231, 57, 66);")
        self.TotelLabel.setObjectName("TotelLabel")
        self.ProcessButton = QtWidgets.QPushButton(self.TextFrame)
        self.ProcessButton.setGeometry(QtCore.QRect(180, 147, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.ProcessButton.setFont(font)
        self.ProcessButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ProcessButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(43, 128, 247);\n"
"    border-radius: 18;\n"
"}\n"
":hover{\n"
"    \n"
"    background-color: rgb(126, 216, 255);\n"
"}")
        self.ProcessButton.setObjectName("ProcessButton")
        self.ScanButton = QtWidgets.QPushButton(self.UpperFrame)
        self.ScanButton.setGeometry(QtCore.QRect(100, 10, 220, 220))
        self.ScanButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ScanButton.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("./statics/imgs/ScanButton.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ScanButton.setIcon(icon7)
        self.ScanButton.setIconSize(QtCore.QSize(220, 220))
        self.ScanButton.setObjectName("ScanButton")
        self.DownFrame = QtWidgets.QFrame(self.BodyFrame)
        self.DownFrame.setGeometry(QtCore.QRect(0, 240, 900, 240))
        self.DownFrame.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.DownFrame.setStyleSheet("background-color: transparent;")
        self.DownFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.DownFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.DownFrame.setObjectName("DownFrame")
        self.PartScanButton = QtWidgets.QPushButton(self.DownFrame)
        self.PartScanButton.setGeometry(QtCore.QRect(200, 10, 200, 200))
        self.PartScanButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PartScanButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.502488, y1:0.864, x2:0.487562, y2:0.3125, stop:0 rgba(20, 87, 188, 255), stop:1 rgba(118, 156, 243, 22));\n"
"border-radius: 100;")
        self.PartScanButton.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("./statics/imgs/PartScanButton.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PartScanButton.setIcon(icon8)
        self.PartScanButton.setIconSize(QtCore.QSize(200, 200))
        self.PartScanButton.setObjectName("PartScanButton")
        self.AllSacnButton = QtWidgets.QPushButton(self.DownFrame)
        self.AllSacnButton.setGeometry(QtCore.QRect(500, 10, 200, 200))
        self.AllSacnButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.AllSacnButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.506975, y1:0.903, x2:0.502, y2:0.25, stop:0 rgba(48, 147, 230, 255), stop:1 rgba(144, 195, 250, 0));\n"
"border-radius: 100;")
        self.AllSacnButton.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("./statics/imgs/AllScanButton.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AllSacnButton.setIcon(icon9)
        self.AllSacnButton.setIconSize(QtCore.QSize(200, 200))
        self.AllSacnButton.setObjectName("AllSacnButton")
        self.PartButtonName = QtWidgets.QLabel(self.DownFrame)
        self.PartButtonName.setGeometry(QtCore.QRect(260, 180, 81, 16))
        self.PartButtonName.setObjectName("PartButtonName")
        self.AllButtonName = QtWidgets.QLabel(self.DownFrame)
        self.AllButtonName.setGeometry(QtCore.QRect(576, 180, 61, 16))
        self.AllButtonName.setObjectName("AllButtonName")
        self.label_2 = QtWidgets.QLabel(self.DownFrame)
        self.label_2.setGeometry(QtCore.QRect(650, 220, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.DownFrame)
        self.label_3.setGeometry(QtCore.QRect(700, 220, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.DownFrame)
        self.label_4.setGeometry(QtCore.QRect(790, 220, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.DownFrame)
        self.label_5.setGeometry(QtCore.QRect(840, 220, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Form"))
        self.TitleLabel.setText(_translate("MainWindow", "国联易安"))
        self.VersionLabel.setText(_translate("MainWindow", "  (主机版) V2.0 "))
        self.SloganLabel.setText(_translate("MainWindow", "恶意代码辅助监测系统"))
        self.KillButtonName.setText(_translate("MainWindow", "恶意代码查杀"))
        self.ToolsButtonName.setText(_translate("MainWindow", "安全工具"))
        self.UserButtonName.setText(_translate("MainWindow", "用户管理"))
        self.LoginButton.setText(_translate("MainWindow", "登录"))
        self.label.setText(_translate("MainWindow", "普通用户"))
        self.WarningLabel.setText(_translate("MainWindow", "您的电脑存在威胁,建议立即处理"))
        self.describe1.setText(_translate("MainWindow", "已保护您的电脑"))
        self.DaysLabel.setText(_translate("MainWindow", "17"))
        self.describe2.setText(_translate("MainWindow", "天，已成功拦截威胁"))
        self.TimesLabel.setText(_translate("MainWindow", "0"))
        self.describe3.setText(_translate("MainWindow", "次上次扫描在"))
        self.DateLabel.setText(_translate("MainWindow", "2023/01/01"))
        self.describe4.setText(_translate("MainWindow", "未处理恶意代码"))
        self.TotelLabel.setText(_translate("MainWindow", "56"))
        self.ProcessButton.setText(_translate("MainWindow", "立即处理"))
        self.PartButtonName.setText(_translate("MainWindow", "指定位置扫描"))
        self.AllButtonName.setText(_translate("MainWindow", "全盘扫描"))
        self.label_2.setText(_translate("MainWindow", "产品版本:"))
        self.label_3.setText(_translate("MainWindow", "2.0.0.05041735"))
        self.label_4.setText(_translate("MainWindow", "产品授权:"))
        self.label_5.setText(_translate("MainWindow", "未授权"))
