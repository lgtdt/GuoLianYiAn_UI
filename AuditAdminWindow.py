# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\designer\AuditAdminWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AuditAdminWindow(object):
    def setupUi(self, AuditAdminWindow):
        AuditAdminWindow.setObjectName("AuditAdminWindow")
        AuditAdminWindow.resize(900, 600)
        AuditAdminWindow.setStyleSheet("QWidget{border-radius: 10px;}\n"
"border: none;")
        self.BackGroundFrame = QtWidgets.QFrame(AuditAdminWindow)
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\designer\\../statics/imgs/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.UserButton.setIcon(icon)
        self.UserButton.setIconSize(QtCore.QSize(30, 30))
        self.UserButton.setObjectName("UserButton")
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
        self.LogFrame = QtWidgets.QFrame(self.BackGroundFrame)
        self.LogFrame.setGeometry(QtCore.QRect(0, 120, 900, 460))
        self.LogFrame.setStyleSheet("background-color: qradialgradient(spread:pad, cx:0, cy:1, radius:1.02262, fx:0, fy:1, stop:0 rgba(60, 86, 222, 255), stop:0.995025 rgba(138, 206, 253, 250));\n"
"border: none;")
        self.LogFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LogFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LogFrame.setObjectName("LogFrame")
        self.ToolsBackFrame_2 = QtWidgets.QFrame(self.LogFrame)
        self.ToolsBackFrame_2.setGeometry(QtCore.QRect(0, 0, 900, 460))
        self.ToolsBackFrame_2.setStyleSheet("background-color: transparent;")
        self.ToolsBackFrame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ToolsBackFrame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ToolsBackFrame_2.setObjectName("ToolsBackFrame_2")
        self.XitongFuzhuFrame_2 = QtWidgets.QFrame(self.ToolsBackFrame_2)
        self.XitongFuzhuFrame_2.setGeometry(QtCore.QRect(40, 65, 821, 381))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.XitongFuzhuFrame_2.setFont(font)
        self.XitongFuzhuFrame_2.setStyleSheet("background-color: rgba(146, 178, 242, 80);\n"
"border-radius: 20;")
        self.XitongFuzhuFrame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.XitongFuzhuFrame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.XitongFuzhuFrame_2.setObjectName("XitongFuzhuFrame_2")
        self.LogTableWidget = QtWidgets.QTableWidget(self.XitongFuzhuFrame_2)
        self.LogTableWidget.setGeometry(QtCore.QRect(0, 0, 821, 381))
        self.LogTableWidget.setStyleSheet("background-color:transparent;")
        self.LogTableWidget.setObjectName("LogTableWidget")
        self.LogTableWidget.setColumnCount(0)
        self.LogTableWidget.setRowCount(0)
        self.label_38 = QtWidgets.QLabel(self.ToolsBackFrame_2)
        self.label_38.setGeometry(QtCore.QRect(50, 20, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label_38.setFont(font)
        self.label_38.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_38.setObjectName("label_38")
        self.BottomFrame.raise_()
        self.TopFrame.raise_()
        self.LogFrame.raise_()

        self.retranslateUi(AuditAdminWindow)
        QtCore.QMetaObject.connectSlotsByName(AuditAdminWindow)

    def retranslateUi(self, AuditAdminWindow):
        _translate = QtCore.QCoreApplication.translate
        AuditAdminWindow.setWindowTitle(_translate("AuditAdminWindow", "Form"))
        self.TitleLabel.setText(_translate("AuditAdminWindow", "国联易安"))
        self.VersionLabel.setText(_translate("AuditAdminWindow", "  (主机版) V2.0 "))
        self.SloganLabel.setText(_translate("AuditAdminWindow", "恶意代码辅助监测系统"))
        self.UserButtonName.setText(_translate("AuditAdminWindow", "日志审计"))
        self.LogoutButton.setText(_translate("AuditAdminWindow", "登出"))
        self.UserTypeLabel.setText(_translate("AuditAdminWindow", "安全审计员"))
        self.ChangePassButton.setText(_translate("AuditAdminWindow", "修改密码"))
        self.AboutButton.setText(_translate("AuditAdminWindow", "关于"))
        self.label_20.setText(_translate("AuditAdminWindow", "产品授权:"))
        self.label_21.setText(_translate("AuditAdminWindow", "产品版本:"))
        self.label_22.setText(_translate("AuditAdminWindow", "2.0.0.05041735"))
        self.label_23.setText(_translate("AuditAdminWindow", "未授权"))
        self.label_38.setText(_translate("AuditAdminWindow", "日志审计"))
