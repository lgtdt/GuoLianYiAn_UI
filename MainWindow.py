# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\designer\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        MainWindow.setStyleSheet("QWidget{border-radius: 10px;}\n"
"border: none;")
        self.BackGroundFrame = QtWidgets.QFrame(MainWindow)
        self.BackGroundFrame.setGeometry(QtCore.QRect(0, 0, 900, 600))
        self.BackGroundFrame.setStyleSheet("border-radius: 0;")
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
        self.ButtonFrame = QtWidgets.QFrame(self.TopFrame)
        self.ButtonFrame.setGeometry(QtCore.QRect(300, 0, 360, 120))
        self.ButtonFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ButtonFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ButtonFrame.setObjectName("ButtonFrame")
        self.KillButton = QtWidgets.QPushButton(self.ButtonFrame)
        self.KillButton.setGeometry(QtCore.QRect(0, 0, 120, 120))
        self.KillButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.KillButton.setStyleSheet(":hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0.985075, y1:1, x2:1, y2:0, stop:0 rgba(118, 180, 242, 255), stop:1 rgba(167, 203, 240, 255));\n"
"}")
        self.KillButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\designer\\../statics/imgs/Lock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.KillButton.setIcon(icon)
        self.KillButton.setIconSize(QtCore.QSize(30, 30))
        self.KillButton.setObjectName("KillButton")
        self.KillButtonName = QtWidgets.QLabel(self.ButtonFrame)
        self.KillButtonName.setGeometry(QtCore.QRect(21, 88, 81, 16))
        self.KillButtonName.setStyleSheet("background-color: transparent;\n"
"font-size:13px;")
        self.KillButtonName.setObjectName("KillButtonName")
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\designer\\../statics/imgs/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CloseButton.setIcon(icon1)
        self.CloseButton.setIconSize(QtCore.QSize(23, 23))
        self.CloseButton.setObjectName("CloseButton")
        self.MiniButtuon = QtWidgets.QPushButton(self.MenuFrame)
        self.MiniButtuon.setGeometry(QtCore.QRect(155, 5, 30, 30))
        self.MiniButtuon.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.MiniButtuon.setStyleSheet(":hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0.985075, y1:1, x2:1, y2:0, stop:0 rgba(118, 180, 242, 255), stop:1 rgba(167, 203, 240, 255));\n"
"}")
        self.MiniButtuon.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(".\\designer\\../statics/imgs/mini.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MiniButtuon.setIcon(icon2)
        self.MiniButtuon.setIconSize(QtCore.QSize(18, 18))
        self.MiniButtuon.setObjectName("MiniButtuon")
        self.SetButtuon = QtWidgets.QPushButton(self.MenuFrame)
        self.SetButtuon.setGeometry(QtCore.QRect(115, 5, 30, 30))
        self.SetButtuon.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SetButtuon.setStyleSheet(":hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0.985075, y1:1, x2:1, y2:0, stop:0 rgba(118, 180, 242, 255), stop:1 rgba(167, 203, 240, 255));\n"
"}")
        self.SetButtuon.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(".\\designer\\../statics/imgs/more.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SetButtuon.setIcon(icon3)
        self.SetButtuon.setIconSize(QtCore.QSize(20, 20))
        self.SetButtuon.setObjectName("SetButtuon")
        self.SkinButton = QtWidgets.QPushButton(self.MenuFrame)
        self.SkinButton.setGeometry(QtCore.QRect(75, 5, 30, 30))
        self.SkinButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SkinButton.setStyleSheet(":hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0.985075, y1:1, x2:1, y2:0, stop:0 rgba(118, 180, 242, 255), stop:1 rgba(167, 203, 240, 255));\n"
"}")
        self.SkinButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(".\\designer\\../statics/imgs/skin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SkinButton.setIcon(icon4)
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
        self.line = QtWidgets.QFrame(self.MenuFrame)
        self.line.setEnabled(True)
        self.line.setGeometry(QtCore.QRect(160, 75, 2, 20))
        self.line.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.MoreMenuFrame = QtWidgets.QFrame(self.MenuFrame)
        self.MoreMenuFrame.setEnabled(True)
        self.MoreMenuFrame.setGeometry(QtCore.QRect(79, 35, 111, 60))
        self.MoreMenuFrame.setStyleSheet("background-color: rgb(154, 209, 252);")
        self.MoreMenuFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MoreMenuFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MoreMenuFrame.setObjectName("MoreMenuFrame")
        self.ChangePassButton = QtWidgets.QPushButton(self.MoreMenuFrame)
        self.ChangePassButton.setGeometry(QtCore.QRect(0, 0, 111, 30))
        self.ChangePassButton.setStyleSheet(":hover{\n"
" color: black;\n"
"}")
        self.ChangePassButton.setObjectName("ChangePassButton")
        self.AboutButton = QtWidgets.QPushButton(self.MoreMenuFrame)
        self.AboutButton.setGeometry(QtCore.QRect(0, 30, 111, 30))
        self.AboutButton.setStyleSheet(":hover{\n"
" color: black;\n"
"}")
        self.AboutButton.setObjectName("AboutButton")
        self.LogoFrame = QtWidgets.QFrame(self.TopFrame)
        self.LogoFrame.setGeometry(QtCore.QRect(0, 0, 300, 120))
        self.LogoFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LogoFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LogoFrame.setObjectName("LogoFrame")
        self.TitleLabel = QtWidgets.QLabel(self.LogoFrame)
        self.TitleLabel.setGeometry(QtCore.QRect(30, 25, 131, 36))
        font = QtGui.QFont()
        font.setFamily("YouSheBiaoTiHei")
        font.setPointSize(-1)
        self.TitleLabel.setFont(font)
        self.TitleLabel.setStyleSheet("background-color: transparent;\n"
"color: rgb(255, 255, 255);\n"
"font-size:35px;")
        self.TitleLabel.setObjectName("TitleLabel")
        self.VersionLabel = QtWidgets.QLabel(self.LogoFrame)
        self.VersionLabel.setGeometry(QtCore.QRect(170, 35, 89, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.VersionLabel.setFont(font)
        self.VersionLabel.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.505682, stop:0 rgba(250, 193, 31, 255), stop:1 rgba(252, 228, 4, 255));\n"
"color: rgb(156, 69, 21);\n"
"border-radius: 10;\n"
"font-size:13px;")
        self.VersionLabel.setObjectName("VersionLabel")
        self.SloganLabel = QtWidgets.QLabel(self.LogoFrame)
        self.SloganLabel.setGeometry(QtCore.QRect(30, 70, 171, 16))
        font = QtGui.QFont()
        font.setFamily("YouSheBiaoTiHei")
        font.setPointSize(-1)
        self.SloganLabel.setFont(font)
        self.SloganLabel.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-size:19px;")
        self.SloganLabel.setObjectName("SloganLabel")
        self.BodyFrame = QtWidgets.QFrame(self.BackGroundFrame)
        self.BodyFrame.setGeometry(QtCore.QRect(0, 120, 900, 460))
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
        font.setPointSize(-1)
        self.WarningLabel.setFont(font)
        self.WarningLabel.setStyleSheet("font-size:32px;")
        self.WarningLabel.setObjectName("WarningLabel")
        self.describe1 = QtWidgets.QLabel(self.TextFrame)
        self.describe1.setGeometry(QtCore.QRect(10, 100, 91, 16))
        self.describe1.setStyleSheet("font-size:13px;")
        self.describe1.setObjectName("describe1")
        self.DaysLabel = QtWidgets.QLabel(self.TextFrame)
        self.DaysLabel.setGeometry(QtCore.QRect(110, 100, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.DaysLabel.setFont(font)
        self.DaysLabel.setStyleSheet("color: rgb(252, 225, 7);\n"
"font-size:17px;")
        self.DaysLabel.setObjectName("DaysLabel")
        self.describe2 = QtWidgets.QLabel(self.TextFrame)
        self.describe2.setGeometry(QtCore.QRect(150, 100, 121, 16))
        self.describe2.setStyleSheet("font-size:13px;")
        self.describe2.setObjectName("describe2")
        self.TimesLabel = QtWidgets.QLabel(self.TextFrame)
        self.TimesLabel.setGeometry(QtCore.QRect(280, 100, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.TimesLabel.setFont(font)
        self.TimesLabel.setStyleSheet("color: rgb(252, 225, 7);\n"
"font-size:17px;")
        self.TimesLabel.setObjectName("TimesLabel")
        self.describe3 = QtWidgets.QLabel(self.TextFrame)
        self.describe3.setGeometry(QtCore.QRect(310, 100, 81, 16))
        self.describe3.setStyleSheet("font-size:13px;")
        self.describe3.setObjectName("describe3")
        self.DateLabel = QtWidgets.QLabel(self.TextFrame)
        self.DateLabel.setGeometry(QtCore.QRect(390, 100, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.DateLabel.setFont(font)
        self.DateLabel.setStyleSheet("color: rgb(252, 225, 7);\n"
"font-size:17px;")
        self.DateLabel.setObjectName("DateLabel")
        self.describe4 = QtWidgets.QLabel(self.TextFrame)
        self.describe4.setGeometry(QtCore.QRect(10, 160, 91, 16))
        self.describe4.setStyleSheet("font-size:13px;")
        self.describe4.setObjectName("describe4")
        self.TotelLabel = QtWidgets.QLabel(self.TextFrame)
        self.TotelLabel.setGeometry(QtCore.QRect(110, 159, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.TotelLabel.setFont(font)
        self.TotelLabel.setStyleSheet("color: rgb(231, 57, 66);\n"
"font-size:17px;")
        self.TotelLabel.setObjectName("TotelLabel")
        self.ProcessButton = QtWidgets.QPushButton(self.TextFrame)
        self.ProcessButton.setGeometry(QtCore.QRect(180, 147, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.ProcessButton.setFont(font)
        self.ProcessButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ProcessButton.setStyleSheet("QPushButton{\n"
"    font-size:19px;\n"
"    background-color: rgb(43, 128, 247);\n"
"    border-radius: 18;\n"
"}\n"
":hover{\n"
"    font-size:19px;\n"
"    background-color: rgb(126, 216, 255);\n"
"}")
        self.ProcessButton.setObjectName("ProcessButton")
        self.ScanButton = QtWidgets.QPushButton(self.UpperFrame)
        self.ScanButton.setGeometry(QtCore.QRect(100, 10, 220, 220))
        self.ScanButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ScanButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(".\\designer\\../statics/imgs/ScanButton.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ScanButton.setIcon(icon5)
        self.ScanButton.setIconSize(QtCore.QSize(220, 220))
        self.ScanButton.setObjectName("ScanButton")
        self.DownFrame = QtWidgets.QFrame(self.BodyFrame)
        self.DownFrame.setGeometry(QtCore.QRect(0, 240, 900, 220))
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
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(".\\designer\\../statics/imgs/PartScanButton.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PartScanButton.setIcon(icon6)
        self.PartScanButton.setIconSize(QtCore.QSize(200, 200))
        self.PartScanButton.setObjectName("PartScanButton")
        self.AllSacnButton = QtWidgets.QPushButton(self.DownFrame)
        self.AllSacnButton.setGeometry(QtCore.QRect(500, 10, 200, 200))
        self.AllSacnButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.AllSacnButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.506975, y1:0.903, x2:0.502, y2:0.25, stop:0 rgba(48, 147, 230, 255), stop:1 rgba(144, 195, 250, 0));\n"
"border-radius: 100;")
        self.AllSacnButton.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(".\\designer\\../statics/imgs/AllScanButton.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.AllSacnButton.setIcon(icon7)
        self.AllSacnButton.setIconSize(QtCore.QSize(200, 200))
        self.AllSacnButton.setObjectName("AllSacnButton")
        self.PartButtonName = QtWidgets.QLabel(self.DownFrame)
        self.PartButtonName.setGeometry(QtCore.QRect(260, 180, 81, 16))
        self.PartButtonName.setStyleSheet("font-size:13px;")
        self.PartButtonName.setObjectName("PartButtonName")
        self.AllButtonName = QtWidgets.QLabel(self.DownFrame)
        self.AllButtonName.setGeometry(QtCore.QRect(576, 180, 61, 16))
        self.AllButtonName.setStyleSheet("font-size:13px;")
        self.AllButtonName.setObjectName("AllButtonName")
        self.ResultFrame = QtWidgets.QFrame(self.BackGroundFrame)
        self.ResultFrame.setGeometry(QtCore.QRect(0, 120, 900, 460))
        self.ResultFrame.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0, cy:1, radius:1.02262, fx:0, fy:1, stop:0 rgba(60, 86, 222, 255), stop:0.995025 rgba(138, 206, 253, 250));\n"
"border: none;")
        self.ResultFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ResultFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ResultFrame.setObjectName("ResultFrame")
        self.label_10 = QtWidgets.QLabel(self.ResultFrame)
        self.label_10.setGeometry(QtCore.QRect(50, 30, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: transparent;\n"
"font-size:23px;")
        self.label_10.setObjectName("label_10")
        self.BugCountLabel = QtWidgets.QLabel(self.ResultFrame)
        self.BugCountLabel.setGeometry(QtCore.QRect(130, 30, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.BugCountLabel.setFont(font)
        self.BugCountLabel.setStyleSheet("background-color: transparent;\n"
"color: red;\n"
"font-size:23px;")
        self.BugCountLabel.setObjectName("BugCountLabel")
        self.label_12 = QtWidgets.QLabel(self.ResultFrame)
        self.label_12.setGeometry(QtCore.QRect(190, 30, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color: transparent;\n"
"font-size:23px;")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.ResultFrame)
        self.label_13.setGeometry(QtCore.QRect(50, 70, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color: transparent;\n"
"font-size:13px;")
        self.label_13.setObjectName("label_13")
        self.TimeCostLabel = QtWidgets.QLabel(self.ResultFrame)
        self.TimeCostLabel.setGeometry(QtCore.QRect(80, 70, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.TimeCostLabel.setFont(font)
        self.TimeCostLabel.setStyleSheet("background-color: transparent;\n"
"color: yellow;\n"
"font-size:13px;")
        self.TimeCostLabel.setObjectName("TimeCostLabel")
        self.label_15 = QtWidgets.QLabel(self.ResultFrame)
        self.label_15.setGeometry(QtCore.QRect(140, 70, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("background-color: transparent;\n"
"font-size:13px;")
        self.label_15.setObjectName("label_15")
        self.FileCountLabel = QtWidgets.QLabel(self.ResultFrame)
        self.FileCountLabel.setGeometry(QtCore.QRect(170, 70, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.FileCountLabel.setFont(font)
        self.FileCountLabel.setStyleSheet("background-color: transparent;\n"
"color: yellow;\n"
"font-size:13px;")
        self.FileCountLabel.setObjectName("FileCountLabel")
        self.label_17 = QtWidgets.QLabel(self.ResultFrame)
        self.label_17.setGeometry(QtCore.QRect(210, 70, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("background-color: transparent;\n"
"font-size:13px;")
        self.label_17.setObjectName("label_17")
        self.NotDealResButton = QtWidgets.QPushButton(self.ResultFrame)
        self.NotDealResButton.setGeometry(QtCore.QRect(610, 50, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setUnderline(True)
        self.NotDealResButton.setFont(font)
        self.NotDealResButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.NotDealResButton.setStyleSheet("font-size:13px;\n"
"background-color: transparent;\n"
"text-decoration: underline;\n"
"color: grey;")
        self.NotDealResButton.setObjectName("NotDealResButton")
        self.DealResButton = QtWidgets.QPushButton(self.ResultFrame)
        self.DealResButton.setGeometry(QtCore.QRect(710, 40, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.DealResButton.setFont(font)
        self.DealResButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.DealResButton.setStyleSheet("QPushButton{\n"
"font-size:19px;\n"
"    background-color: rgb(43, 128, 247);\n"
"    border-radius: 18;\n"
"}\n"
":hover{\n"
"font-size:19px;\n"
"    background-color: rgb(126, 216, 255);\n"
"}")
        self.DealResButton.setObjectName("DealResButton")
        self.BugListFrame = QtWidgets.QFrame(self.ResultFrame)
        self.BugListFrame.setGeometry(QtCore.QRect(50, 100, 801, 351))
        self.BugListFrame.setStyleSheet("background-color: rgba(149, 196, 250, 77);\n"
"border-radius: 15;")
        self.BugListFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BugListFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.BugListFrame.setObjectName("BugListFrame")
        self.frame = QtWidgets.QFrame(self.BugListFrame)
        self.frame.setGeometry(QtCore.QRect(20, 10, 761, 35))
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0.517045, x2:0, y2:0.517, stop:0 rgba(101, 150, 242, 249), stop:1 rgba(106, 171, 239, 234));")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 8, 19, 19))
        self.label_2.setStyleSheet("background-color: transparent;")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(".\\designer\\../statics/imgs/right.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(50, 9, 58, 16))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: transparent;\n"
"font-size:13px;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(640, 10, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font-size:13px;\n"
"background-color: transparent;")
        self.label_4.setObjectName("label_4")
        self.ResBugCountLabel = QtWidgets.QLabel(self.frame)
        self.ResBugCountLabel.setGeometry(QtCore.QRect(680, 10, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.ResBugCountLabel.setFont(font)
        self.ResBugCountLabel.setStyleSheet("font-size:13px;\n"
"background-color: transparent;\n"
"color: red;")
        self.ResBugCountLabel.setObjectName("ResBugCountLabel")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(710, 10, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("font-size:13px;\n"
"background-color: transparent;")
        self.label_6.setObjectName("label_6")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.BugListFrame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 50, 801, 301))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.verticalLayoutWidget)
        self.scrollArea.setStyleSheet("background-color: transparent;\n"
"border-top-left-radius: 0px;\n"
" border-top-right-radius: 0px;\n"
" border-bottom-left-radius: 15px; \n"
"border-bottom-right-radius: 15px;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 799, 299))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.BottomFrame = QtWidgets.QFrame(self.BackGroundFrame)
        self.BottomFrame.setGeometry(QtCore.QRect(0, 120, 900, 480))
        self.BottomFrame.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0, cy:1, radius:1.02262, fx:0, fy:1, stop:0 rgba(60, 86, 222, 255), stop:0.995025 rgba(138, 206, 253, 250));\n"
"border: none;")
        self.BottomFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BottomFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.BottomFrame.setObjectName("BottomFrame")
        self.label_20 = QtWidgets.QLabel(self.BottomFrame)
        self.label_20.setGeometry(QtCore.QRect(760, 460, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("background-color:transparent;\n"
"font-size:10px;")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.BottomFrame)
        self.label_21.setGeometry(QtCore.QRect(620, 460, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("background-color:transparent;\n"
"font-size:10px;")
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.BottomFrame)
        self.label_22.setGeometry(QtCore.QRect(670, 460, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("background-color:transparent;\n"
"font-size:10px;")
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.BottomFrame)
        self.label_23.setGeometry(QtCore.QRect(810, 460, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("background-color:transparent;\n"
"font-size:10px;")
        self.label_23.setObjectName("label_23")
        self.ScanningFrame = QtWidgets.QFrame(self.BackGroundFrame)
        self.ScanningFrame.setGeometry(QtCore.QRect(0, 120, 900, 460))
        font = QtGui.QFont()
        font.setFamily("宋体")
        self.ScanningFrame.setFont(font)
        self.ScanningFrame.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0, cy:1, radius:1.02262, fx:0, fy:1, stop:0 rgba(60, 86, 222, 255), stop:0.995025 rgba(138, 206, 253, 250));\n"
"border: none;")
        self.ScanningFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ScanningFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ScanningFrame.setObjectName("ScanningFrame")
        self.label_5 = QtWidgets.QLabel(self.ScanningFrame)
        self.label_5.setGeometry(QtCore.QRect(40, 20, 241, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(-1)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: transparent;\n"
"font-size: 20px;")
        self.label_5.setObjectName("label_5")
        self.FilePathLabel = QtWidgets.QLabel(self.ScanningFrame)
        self.FilePathLabel.setGeometry(QtCore.QRect(40, 50, 561, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(-1)
        self.FilePathLabel.setFont(font)
        self.FilePathLabel.setStyleSheet("background-color: transparent;\n"
"font-size:13px;")
        self.FilePathLabel.setText("")
        self.FilePathLabel.setObjectName("FilePathLabel")
        self.CancelScanButton = QtWidgets.QPushButton(self.ScanningFrame)
        self.CancelScanButton.setGeometry(QtCore.QRect(750, 33, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.CancelScanButton.setFont(font)
        self.CancelScanButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CancelScanButton.setStyleSheet("QPushButton{\n"
"    font-size:17px;\n"
"    background-color: rgb(43, 128, 247);\n"
"    border-radius: 10;\n"
"}\n"
":hover{\n"
"    background-color: rgb(126, 216, 255);\n"
"}")
        self.CancelScanButton.setObjectName("CancelScanButton")
        self.ProcessNumberLabel = QtWidgets.QLabel(self.ScanningFrame)
        self.ProcessNumberLabel.setGeometry(QtCore.QRect(380, 140, 151, 151))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.ProcessNumberLabel.setFont(font)
        self.ProcessNumberLabel.setStyleSheet("background-color:transparent;")
        self.ProcessNumberLabel.setObjectName("ProcessNumberLabel")
        self.BottomFrame.raise_()
        self.TopFrame.raise_()
        self.BodyFrame.raise_()
        self.ScanningFrame.raise_()
        self.ResultFrame.raise_()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Form"))
        self.KillButtonName.setText(_translate("MainWindow", "恶意代码查杀"))
        self.LoginButton.setText(_translate("MainWindow", "登录"))
        self.label.setText(_translate("MainWindow", "普通用户"))
        self.ChangePassButton.setText(_translate("MainWindow", "修改密码"))
        self.AboutButton.setText(_translate("MainWindow", "关于"))
        self.TitleLabel.setText(_translate("MainWindow", "国联易安"))
        self.VersionLabel.setText(_translate("MainWindow", "  (主机版) V2.0 "))
        self.SloganLabel.setText(_translate("MainWindow", "恶意代码辅助监测系统"))
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
        self.label_10.setText(_translate("MainWindow", "共发现"))
        self.BugCountLabel.setText(_translate("MainWindow", "23"))
        self.label_12.setText(_translate("MainWindow", "威胁文件"))
        self.label_13.setText(_translate("MainWindow", "用时"))
        self.TimeCostLabel.setText(_translate("MainWindow", "00:31:38"))
        self.label_15.setText(_translate("MainWindow", "扫描"))
        self.FileCountLabel.setText(_translate("MainWindow", "9765"))
        self.label_17.setText(_translate("MainWindow", "文件，建议立即进行处理"))
        self.NotDealResButton.setText(_translate("MainWindow", "暂不处理"))
        self.DealResButton.setText(_translate("MainWindow", "立即处理"))
        self.label_3.setText(_translate("MainWindow", "系统安全"))
        self.label_4.setText(_translate("MainWindow", "发现"))
        self.ResBugCountLabel.setText(_translate("MainWindow", "28"))
        self.label_6.setText(_translate("MainWindow", "威胁"))
        self.label_20.setText(_translate("MainWindow", "产品授权:"))
        self.label_21.setText(_translate("MainWindow", "产品版本:"))
        self.label_22.setText(_translate("MainWindow", "2.0.0.05041735"))
        self.label_23.setText(_translate("MainWindow", "未授权"))
        self.label_5.setText(_translate("MainWindow", "正在进行快速扫描..."))
        self.CancelScanButton.setText(_translate("MainWindow", "取消扫描"))
        self.ProcessNumberLabel.setText(_translate("MainWindow", "1%"))
