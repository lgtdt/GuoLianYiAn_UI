# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SysAdminWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SysAdminWindow(object):
    def setupUi(self, SysAdminWindow):
        SysAdminWindow.setObjectName("SysAdminWindow")
        SysAdminWindow.resize(900, 600)
        SysAdminWindow.setStyleSheet("QWidget{border-radius: 10px;}\n"
"border: none;")
        self.BackGroundFrame = QtWidgets.QFrame(SysAdminWindow)
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
        self.SysSetButton = QtWidgets.QPushButton(self.ButtonFrame)
        self.SysSetButton.setGeometry(QtCore.QRect(120, 0, 120, 120))
        self.SysSetButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SysSetButton.setStyleSheet(":hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0.985075, y1:1, x2:1, y2:0, stop:0 rgba(118, 180, 242, 255), stop:1 rgba(167, 203, 240, 255));\n"
"}")
        self.SysSetButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./statics/imgs/tool.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SysSetButton.setIcon(icon)
        self.SysSetButton.setIconSize(QtCore.QSize(30, 30))
        self.SysSetButton.setObjectName("SysSetButton")
        self.UserButton = QtWidgets.QPushButton(self.ButtonFrame)
        self.UserButton.setGeometry(QtCore.QRect(0, 0, 120, 120))
        self.UserButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.UserButton.setStyleSheet("QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0.985075, y1:1, x2:1, y2:0, stop:0 rgba(118, 180, 242, 255), stop:1 rgba(167, 203, 240, 255));\n"
"}\n"
":hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0.985075, y1:1, x2:1, y2:0, stop:0 rgba(118, 180, 242, 255), stop:1 rgba(167, 203, 240, 255));\n"
"}")
        self.UserButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./statics/imgs/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.UserButton.setIcon(icon1)
        self.UserButton.setIconSize(QtCore.QSize(30, 30))
        self.UserButton.setObjectName("UserButton")
        self.SysSetButtonName = QtWidgets.QLabel(self.ButtonFrame)
        self.SysSetButtonName.setGeometry(QtCore.QRect(156, 88, 61, 16))
        self.SysSetButtonName.setStyleSheet("background-color: transparent;")
        self.SysSetButtonName.setObjectName("SysSetButtonName")
        self.UserButtonName = QtWidgets.QLabel(self.ButtonFrame)
        self.UserButtonName.setGeometry(QtCore.QRect(35, 88, 61, 16))
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./statics/imgs/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.CloseButton.setIcon(icon2)
        self.CloseButton.setIconSize(QtCore.QSize(23, 23))
        self.CloseButton.setObjectName("CloseButton")
        self.MiniButtuon = QtWidgets.QPushButton(self.MenuFrame)
        self.MiniButtuon.setGeometry(QtCore.QRect(155, 5, 30, 30))
        self.MiniButtuon.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.MiniButtuon.setStyleSheet(":hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0.985075, y1:1, x2:1, y2:0, stop:0 rgba(118, 180, 242, 255), stop:1 rgba(167, 203, 240, 255));\n"
"}")
        self.MiniButtuon.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./statics/imgs/mini.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MiniButtuon.setIcon(icon3)
        self.MiniButtuon.setIconSize(QtCore.QSize(18, 18))
        self.MiniButtuon.setObjectName("MiniButtuon")
        self.SetButtuon = QtWidgets.QPushButton(self.MenuFrame)
        self.SetButtuon.setGeometry(QtCore.QRect(115, 5, 30, 30))
        self.SetButtuon.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SetButtuon.setStyleSheet(":hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0.985075, y1:1, x2:1, y2:0, stop:0 rgba(118, 180, 242, 255), stop:1 rgba(167, 203, 240, 255));\n"
"}")
        self.SetButtuon.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("./statics/imgs/more.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SetButtuon.setIcon(icon4)
        self.SetButtuon.setIconSize(QtCore.QSize(20, 20))
        self.SetButtuon.setObjectName("SetButtuon")
        self.SkinButton = QtWidgets.QPushButton(self.MenuFrame)
        self.SkinButton.setGeometry(QtCore.QRect(75, 5, 30, 30))
        self.SkinButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SkinButton.setStyleSheet(":hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0.985075, y1:1, x2:1, y2:0, stop:0 rgba(118, 180, 242, 255), stop:1 rgba(167, 203, 240, 255));\n"
"}")
        self.SkinButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("./statics/imgs/skin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SkinButton.setIcon(icon5)
        self.SkinButton.setIconSize(QtCore.QSize(20, 20))
        self.SkinButton.setObjectName("SkinButton")
        self.LogoutButton = QtWidgets.QPushButton(self.MenuFrame)
        self.LogoutButton.setGeometry(QtCore.QRect(165, 70, 60, 30))
        self.LogoutButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.LogoutButton.setStyleSheet("QPushButton{\n"
"    color: red;\n"
"    border-radius: 15;\n"
"}\n"
":hover{\n"
"    background-color: rgb(145, 193, 243);\n"
"}")
        self.LogoutButton.setObjectName("LogoutButton")
        self.UserTypeLabel = QtWidgets.QLabel(self.MenuFrame)
        self.UserTypeLabel.setGeometry(QtCore.QRect(80, 70, 71, 30))
        self.UserTypeLabel.setObjectName("UserTypeLabel")
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
        self.ChangePassButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ChangePassButton.setStyleSheet(":hover{\n"
" color: black;\n"
"}")
        self.ChangePassButton.setObjectName("ChangePassButton")
        self.AboutButton = QtWidgets.QPushButton(self.MoreMenuFrame)
        self.AboutButton.setGeometry(QtCore.QRect(0, 30, 111, 30))
        self.AboutButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.AboutButton.setStyleSheet(":hover{\n"
" color: black;\n"
"}")
        self.AboutButton.setObjectName("AboutButton")
        self.BodyFrame = QtWidgets.QFrame(self.BackGroundFrame)
        self.BodyFrame.setGeometry(QtCore.QRect(0, 120, 900, 460))
        self.BodyFrame.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0, cy:1, radius:1.02262, fx:0, fy:1, stop:0 rgba(60, 86, 222, 255), stop:0.995025 rgba(138, 206, 253, 250));\n"
"border: none;")
        self.BodyFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BodyFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.BodyFrame.setObjectName("BodyFrame")
        self.SysSetFrame = QtWidgets.QFrame(self.BodyFrame)
        self.SysSetFrame.setGeometry(QtCore.QRect(0, 0, 900, 460))
        self.SysSetFrame.setStyleSheet("background-color: transparent;")
        self.SysSetFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SysSetFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SysSetFrame.setObjectName("SysSetFrame")
        self.LeftFrame = QtWidgets.QFrame(self.SysSetFrame)
        self.LeftFrame.setGeometry(QtCore.QRect(40, 75, 151, 331))
        self.LeftFrame.setStyleSheet("background-color: rgba(146, 178, 242, 80);\n"
"border-radius: 20;")
        self.LeftFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LeftFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LeftFrame.setObjectName("LeftFrame")
        self.ScanSetButton = QtWidgets.QPushButton(self.LeftFrame)
        self.ScanSetButton.setGeometry(QtCore.QRect(20, 20, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.ScanSetButton.setFont(font)
        self.ScanSetButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ScanSetButton.setStyleSheet("background-color: rgb(67, 126, 239);\n"
"border-radius:10;")
        self.ScanSetButton.setObjectName("ScanSetButton")
        self.AuthorizeSetButton = QtWidgets.QPushButton(self.LeftFrame)
        self.AuthorizeSetButton.setGeometry(QtCore.QRect(20, 80, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.AuthorizeSetButton.setFont(font)
        self.AuthorizeSetButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.AuthorizeSetButton.setStyleSheet("background-color:transparent;\n"
"")
        self.AuthorizeSetButton.setObjectName("AuthorizeSetButton")
        self.SacnSetRightFrame = QtWidgets.QFrame(self.SysSetFrame)
        self.SacnSetRightFrame.setGeometry(QtCore.QRect(230, 75, 631, 331))
        self.SacnSetRightFrame.setStyleSheet("background-color: rgba(146, 178, 242, 80);\n"
"border-radius: 20;")
        self.SacnSetRightFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SacnSetRightFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SacnSetRightFrame.setObjectName("SacnSetRightFrame")
        self.label_2 = QtWidgets.QLabel(self.SacnSetRightFrame)
        self.label_2.setGeometry(QtCore.QRect(60, 20, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.SacnSetRightFrame)
        self.label_3.setGeometry(QtCore.QRect(60, 90, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.SacnSetRightFrame)
        self.label_4.setGeometry(QtCore.QRect(60, 170, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.checkBox11 = QtWidgets.QCheckBox(self.SacnSetRightFrame)
        self.checkBox11.setGeometry(QtCore.QRect(170, 20, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBox11.setFont(font)
        self.checkBox11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox11.setStyleSheet("background-color:transparent;")
        self.checkBox11.setObjectName("checkBox11")
        self.checkBox12 = QtWidgets.QCheckBox(self.SacnSetRightFrame)
        self.checkBox12.setGeometry(QtCore.QRect(300, 20, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBox12.setFont(font)
        self.checkBox12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox12.setStyleSheet("background-color:transparent;")
        self.checkBox12.setObjectName("checkBox12")
        self.checkBox13 = QtWidgets.QCheckBox(self.SacnSetRightFrame)
        self.checkBox13.setGeometry(QtCore.QRect(170, 50, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBox13.setFont(font)
        self.checkBox13.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox13.setStyleSheet("background-color:transparent;")
        self.checkBox13.setObjectName("checkBox13")
        self.radioButton21 = QtWidgets.QRadioButton(self.SacnSetRightFrame)
        self.radioButton21.setGeometry(QtCore.QRect(170, 90, 99, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton21.setFont(font)
        self.radioButton21.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton21.setObjectName("radioButton21")
        self.radioButton22 = QtWidgets.QRadioButton(self.SacnSetRightFrame)
        self.radioButton22.setGeometry(QtCore.QRect(300, 90, 99, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.radioButton22.setFont(font)
        self.radioButton22.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radioButton22.setObjectName("radioButton22")
        self.checkBox31 = QtWidgets.QCheckBox(self.SacnSetRightFrame)
        self.checkBox31.setGeometry(QtCore.QRect(170, 170, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBox31.setFont(font)
        self.checkBox31.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox31.setStyleSheet("background-color:transparent;")
        self.checkBox31.setObjectName("checkBox31")
        self.checkBox21 = QtWidgets.QCheckBox(self.SacnSetRightFrame)
        self.checkBox21.setGeometry(QtCore.QRect(170, 120, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBox21.setFont(font)
        self.checkBox21.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox21.setStyleSheet("background-color:transparent;")
        self.checkBox21.setObjectName("checkBox21")
        self.label = QtWidgets.QLabel(self.SysSetFrame)
        self.label.setGeometry(QtCore.QRect(50, 20, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.AuthorizeRightFrame = QtWidgets.QFrame(self.SysSetFrame)
        self.AuthorizeRightFrame.setGeometry(QtCore.QRect(230, 75, 631, 331))
        self.AuthorizeRightFrame.setStyleSheet("background-color: rgba(146, 178, 242, 80);\n"
"border-radius: 20;")
        self.AuthorizeRightFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.AuthorizeRightFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.AuthorizeRightFrame.setObjectName("AuthorizeRightFrame")
        self.label_8 = QtWidgets.QLabel(self.AuthorizeRightFrame)
        self.label_8.setGeometry(QtCore.QRect(60, 20, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.AuthorizeRightFrame)
        self.label_9.setGeometry(QtCore.QRect(170, 20, 341, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: rgb(170, 170, 170);")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.AuthorizeRightFrame)
        self.label_10.setGeometry(QtCore.QRect(50, 70, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.AuthorizeRightFrame)
        self.label_11.setGeometry(QtCore.QRect(170, 70, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.TryDaysNumberLabel = QtWidgets.QLabel(self.AuthorizeRightFrame)
        self.TryDaysNumberLabel.setGeometry(QtCore.QRect(240, 70, 16, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.TryDaysNumberLabel.setFont(font)
        self.TryDaysNumberLabel.setObjectName("TryDaysNumberLabel")
        self.label_13 = QtWidgets.QLabel(self.AuthorizeRightFrame)
        self.label_13.setGeometry(QtCore.QRect(260, 70, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.InputAuthorityButton = QtWidgets.QPushButton(self.AuthorizeRightFrame)
        self.InputAuthorityButton.setGeometry(QtCore.QRect(430, 60, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.InputAuthorityButton.setFont(font)
        self.InputAuthorityButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.InputAuthorityButton.setStyleSheet("background-color: rgb(67, 126, 239);\n"
"border-radius:10;")
        self.InputAuthorityButton.setObjectName("InputAuthorityButton")
        self.LeftFrame.raise_()
        self.label.raise_()
        self.AuthorizeRightFrame.raise_()
        self.SacnSetRightFrame.raise_()
        self.UserManageFrame = QtWidgets.QFrame(self.BodyFrame)
        self.UserManageFrame.setGeometry(QtCore.QRect(0, 0, 900, 460))
        self.UserManageFrame.setStyleSheet("background-color: transparent;")
        self.UserManageFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.UserManageFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.UserManageFrame.setObjectName("UserManageFrame")
        self.UserListFrame = QtWidgets.QFrame(self.UserManageFrame)
        self.UserListFrame.setGeometry(QtCore.QRect(40, 75, 821, 331))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.UserListFrame.setFont(font)
        self.UserListFrame.setStyleSheet("background-color: rgba(146, 178, 242, 80);\n"
"border-radius: 20;")
        self.UserListFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.UserListFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.UserListFrame.setObjectName("UserListFrame")
        self.frame = QtWidgets.QFrame(self.UserListFrame)
        self.frame.setGeometry(QtCore.QRect(20, 0, 781, 41))
        self.frame.setStyleSheet("background-color: rgb(121, 169, 233);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(20, 10, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_14 = QtWidgets.QLabel(self.frame)
        self.label_14.setGeometry(QtCore.QRect(120, 10, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setGeometry(QtCore.QRect(230, 10, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_17 = QtWidgets.QLabel(self.frame)
        self.label_17.setGeometry(QtCore.QRect(380, 10, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.frame)
        self.label_18.setGeometry(QtCore.QRect(510, 10, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.frame)
        self.label_19.setGeometry(QtCore.QRect(630, 10, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.frame_2 = QtWidgets.QFrame(self.UserListFrame)
        self.frame_2.setGeometry(QtCore.QRect(20, 40, 781, 41))
        self.frame_2.setStyleSheet("background-color:transparent;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_24 = QtWidgets.QLabel(self.frame_2)
        self.label_24.setGeometry(QtCore.QRect(20, 10, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("color:black;")
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.frame_2)
        self.label_25.setGeometry(QtCore.QRect(120, 10, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("color:black;")
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.frame_2)
        self.label_26.setGeometry(QtCore.QRect(230, 10, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet("color:black;")
        self.label_26.setObjectName("label_26")
        self.label_28 = QtWidgets.QLabel(self.frame_2)
        self.label_28.setGeometry(QtCore.QRect(510, 10, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("color:black;")
        self.label_28.setObjectName("label_28")
        self.SecUnlockButton = QtWidgets.QPushButton(self.frame_2)
        self.SecUnlockButton.setGeometry(QtCore.QRect(390, 10, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        self.SecUnlockButton.setFont(font)
        self.SecUnlockButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SecUnlockButton.setStyleSheet("color: rgb(67, 126, 239);")
        self.SecUnlockButton.setObjectName("SecUnlockButton")
        self.SecResetButton = QtWidgets.QPushButton(self.frame_2)
        self.SecResetButton.setGeometry(QtCore.QRect(640, 10, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        self.SecResetButton.setFont(font)
        self.SecResetButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SecResetButton.setStyleSheet("color: rgb(67, 126, 239);")
        self.SecResetButton.setObjectName("SecResetButton")
        self.frame_3 = QtWidgets.QFrame(self.UserListFrame)
        self.frame_3.setGeometry(QtCore.QRect(20, 80, 781, 41))
        self.frame_3.setStyleSheet("background-color:transparent;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_27 = QtWidgets.QLabel(self.frame_3)
        self.label_27.setGeometry(QtCore.QRect(20, 10, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("color:black;")
        self.label_27.setObjectName("label_27")
        self.label_29 = QtWidgets.QLabel(self.frame_3)
        self.label_29.setGeometry(QtCore.QRect(120, 10, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("color:black;")
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.frame_3)
        self.label_30.setGeometry(QtCore.QRect(230, 10, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("color:black;")
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.frame_3)
        self.label_31.setGeometry(QtCore.QRect(510, 10, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("color:black;")
        self.label_31.setObjectName("label_31")
        self.AuditUnlockButton = QtWidgets.QPushButton(self.frame_3)
        self.AuditUnlockButton.setGeometry(QtCore.QRect(390, 10, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        self.AuditUnlockButton.setFont(font)
        self.AuditUnlockButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.AuditUnlockButton.setStyleSheet("color: rgb(67, 126, 239);")
        self.AuditUnlockButton.setObjectName("AuditUnlockButton")
        self.AuditResetButton = QtWidgets.QPushButton(self.frame_3)
        self.AuditResetButton.setGeometry(QtCore.QRect(640, 10, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        self.AuditResetButton.setFont(font)
        self.AuditResetButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.AuditResetButton.setStyleSheet("color: rgb(67, 126, 239);")
        self.AuditResetButton.setObjectName("AuditResetButton")
        self.frame_4 = QtWidgets.QFrame(self.UserListFrame)
        self.frame_4.setGeometry(QtCore.QRect(20, 120, 781, 41))
        self.frame_4.setStyleSheet("background-color:transparent;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_32 = QtWidgets.QLabel(self.frame_4)
        self.label_32.setGeometry(QtCore.QRect(20, 10, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("color:black;")
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.frame_4)
        self.label_33.setGeometry(QtCore.QRect(120, 10, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("color:black;")
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.frame_4)
        self.label_34.setGeometry(QtCore.QRect(230, 10, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("color:black;")
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.frame_4)
        self.label_35.setGeometry(QtCore.QRect(510, 10, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_35.setFont(font)
        self.label_35.setStyleSheet("color:black;")
        self.label_35.setObjectName("label_35")
        self.AdminUnlockButton = QtWidgets.QPushButton(self.frame_4)
        self.AdminUnlockButton.setGeometry(QtCore.QRect(390, 10, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        self.AdminUnlockButton.setFont(font)
        self.AdminUnlockButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.AdminUnlockButton.setStyleSheet("color: rgb(67, 126, 239);")
        self.AdminUnlockButton.setObjectName("AdminUnlockButton")
        self.AdminResetButton = QtWidgets.QPushButton(self.frame_4)
        self.AdminResetButton.setGeometry(QtCore.QRect(640, 10, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        self.AdminResetButton.setFont(font)
        self.AdminResetButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.AdminResetButton.setStyleSheet("color: rgb(67, 126, 239);")
        self.AdminResetButton.setObjectName("AdminResetButton")
        self.label_16 = QtWidgets.QLabel(self.UserManageFrame)
        self.label_16.setGeometry(QtCore.QRect(50, 20, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
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
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("background-color:transparent;")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.BottomFrame)
        self.label_21.setGeometry(QtCore.QRect(620, 460, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("background-color:transparent;")
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.BottomFrame)
        self.label_22.setGeometry(QtCore.QRect(670, 460, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("background-color:transparent;")
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.BottomFrame)
        self.label_23.setGeometry(QtCore.QRect(810, 460, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("background-color:transparent;")
        self.label_23.setObjectName("label_23")
        self.BottomFrame.raise_()
        self.TopFrame.raise_()
        self.BodyFrame.raise_()

        self.retranslateUi(SysAdminWindow)
        QtCore.QMetaObject.connectSlotsByName(SysAdminWindow)

    def retranslateUi(self, SysAdminWindow):
        _translate = QtCore.QCoreApplication.translate
        SysAdminWindow.setWindowTitle(_translate("SysAdminWindow", "Form"))
        self.TitleLabel.setText(_translate("SysAdminWindow", "国联易安"))
        self.VersionLabel.setText(_translate("SysAdminWindow", "  (主机版) V2.0 "))
        self.SloganLabel.setText(_translate("SysAdminWindow", "恶意代码辅助监测系统"))
        self.SysSetButtonName.setText(_translate("SysAdminWindow", "系统设置"))
        self.UserButtonName.setText(_translate("SysAdminWindow", "用户管理"))
        self.LogoutButton.setText(_translate("SysAdminWindow", "登出"))
        self.UserTypeLabel.setText(_translate("SysAdminWindow", "系统管理员"))
        self.ChangePassButton.setText(_translate("SysAdminWindow", "修改密码"))
        self.AboutButton.setText(_translate("SysAdminWindow", "关于"))
        self.ScanSetButton.setText(_translate("SysAdminWindow", "病毒查杀"))
        self.AuthorizeSetButton.setText(_translate("SysAdminWindow", "产品授权"))
        self.label_2.setText(_translate("SysAdminWindow", "扫描类型："))
        self.label_3.setText(_translate("SysAdminWindow", "处理方式："))
        self.label_4.setText(_translate("SysAdminWindow", "扫描压缩包："))
        self.checkBox11.setText(_translate("SysAdminWindow", "扫描PUA"))
        self.checkBox12.setText(_translate("SysAdminWindow", "递归扫描目录"))
        self.checkBox13.setText(_translate("SysAdminWindow", "扫描大于20M的文件"))
        self.radioButton21.setText(_translate("SysAdminWindow", "手动处理"))
        self.radioButton22.setText(_translate("SysAdminWindow", "自动处理"))
        self.checkBox31.setText(_translate("SysAdminWindow", "进入压缩包扫描"))
        self.checkBox21.setText(_translate("SysAdminWindow", "清除病毒前自动备份至恢复区（推荐）"))
        self.label.setText(_translate("SysAdminWindow", "系统设置"))
        self.label_8.setText(_translate("SysAdminWindow", "机器码："))
        self.label_9.setText(_translate("SysAdminWindow", "ABCDE12345ABCDE12345ABCDE12345"))
        self.label_10.setText(_translate("SysAdminWindow", "产品授权："))
        self.label_11.setText(_translate("SysAdminWindow", "已经试用"))
        self.TryDaysNumberLabel.setText(_translate("SysAdminWindow", "7"))
        self.label_13.setText(_translate("SysAdminWindow", "天，请导出机器码！"))
        self.InputAuthorityButton.setText(_translate("SysAdminWindow", "导入产品授权"))
        self.label_12.setText(_translate("SysAdminWindow", "序号"))
        self.label_14.setText(_translate("SysAdminWindow", "用户名"))
        self.label_15.setText(_translate("SysAdminWindow", "账号类型"))
        self.label_17.setText(_translate("SysAdminWindow", "帐号解锁"))
        self.label_18.setText(_translate("SysAdminWindow", "更新周期"))
        self.label_19.setText(_translate("SysAdminWindow", "重置密码"))
        self.label_24.setText(_translate("SysAdminWindow", "1"))
        self.label_25.setText(_translate("SysAdminWindow", "SecAdmin"))
        self.label_26.setText(_translate("SysAdminWindow", "安全保密管理员"))
        self.label_28.setText(_translate("SysAdminWindow", "已逾期"))
        self.SecUnlockButton.setText(_translate("SysAdminWindow", "解锁"))
        self.SecResetButton.setText(_translate("SysAdminWindow", "重置"))
        self.label_27.setText(_translate("SysAdminWindow", "2"))
        self.label_29.setText(_translate("SysAdminWindow", "AuditAdmin"))
        self.label_30.setText(_translate("SysAdminWindow", "审计管理员"))
        self.label_31.setText(_translate("SysAdminWindow", "已逾期"))
        self.AuditUnlockButton.setText(_translate("SysAdminWindow", "解锁"))
        self.AuditResetButton.setText(_translate("SysAdminWindow", "重置"))
        self.label_32.setText(_translate("SysAdminWindow", "3"))
        self.label_33.setText(_translate("SysAdminWindow", "Admin"))
        self.label_34.setText(_translate("SysAdminWindow", "普通用户"))
        self.label_35.setText(_translate("SysAdminWindow", "已逾期"))
        self.AdminUnlockButton.setText(_translate("SysAdminWindow", "解锁"))
        self.AdminResetButton.setText(_translate("SysAdminWindow", "重置"))
        self.label_16.setText(_translate("SysAdminWindow", "用户管理"))
        self.label_20.setText(_translate("SysAdminWindow", "产品授权:"))
        self.label_21.setText(_translate("SysAdminWindow", "产品版本:"))
        self.label_22.setText(_translate("SysAdminWindow", "2.0.0.05041735"))
        self.label_23.setText(_translate("SysAdminWindow", "未授权"))
