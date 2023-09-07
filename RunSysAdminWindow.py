from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt, QPoint, QRectF, QPropertyAnimation, QObject, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QPainterPath, QRegion
import SysAdminWindow

import sys


class SysAdminFrame(QWidget):
    UserName = 'sysadmin'
    #自定义信号
    show_logoutFrame_signal = pyqtSignal(str)
    resetPass_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        # ---设置窗口圆角---
        rect = QRectF(0, 0, 900, 600)
        path = QPainterPath()
        path.addRoundedRect(rect, 8, 8)
        polygon = path.toFillPolygon().toPolygon()
        region = QRegion(polygon)
        self.setMask(region)
        # ----------------

        self.init_ui()
        self.draggable = True
        self.offset = None
        self.ifMoreMenuOpen = False

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.ui.SysSetFrame.setVisible(False)
        self.ui.AuthorizeRightFrame.setVisible(False)



        #自定义槽


    def init_ui(self):
        self.ui = SysAdminWindow.Ui_SysAdminWindow()
        self.ui.setupUi(self)
        self.ui.MoreMenuFrame.setVisible(False)
        self.ui.CloseButton.clicked.connect(self.CloseWindow)
        self.ui.SetButtuon.clicked.connect(self.OpenMoreMenu)
        self.ui.ChangePassButton.clicked.connect(self.OpenResetPassWindow)
        self.ui.UserButton.clicked.connect(self.ShowUserManageFrame)
        self.ui.SysSetButton.clicked.connect(self.ShowSysSetFrame)
        self.ui.ScanSetButton.clicked.connect(self.ShowScanSetFrame)
        self.ui.AuthorizeSetButton.clicked.connect(self.ShowAuthorizeSetFrame)
        self.ui.LogoutButton.clicked.connect(self.ShowLogoutFrame)



    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self.draggable:
            self.offset = event.pos()

    def mouseMoveEvent(self, event):
        if self.offset is not None and self.draggable:
            self.move(self.pos() + event.pos() - self.offset)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.offset = None
    def OpenMoreMenu(self):
        if not self.ifMoreMenuOpen:
            self.ui.MoreMenuFrame.setVisible(True)
            self.ifMoreMenuOpen = True
        else:
            self.ui.MoreMenuFrame.setVisible(False)
            self.ifMoreMenuOpen = False

    def OpenResetPassWindow(self):
        try:
            self.resetPass_signal.emit(self.UserName)
        except Exception as e:
            print(str(e))
    def OpenAboutWindow(self):
        self.aboutFrame.show()

    def ShowUserManageFrame(self):
        self.ui.SysSetButton.setStyleSheet(":hover{\n"
                                        "    background-color: qlineargradient(spread:pad, x1:0.985075, y1:1, x2:1, y2:0, stop:0 rgba(118, 180, 242, 255), stop:1 rgba(167, 203, 240, 255));\n"
                                        "}")
        self.ui.UserButton.setStyleSheet("QPushButton{\n"
                                      "background-color: qlineargradient(spread:pad, x1:0.985075, y1:1, x2:1, y2:0, stop:0 rgba(118, 180, 242, 255), stop:1 rgba(167, 203, 240, 255));\n"
                                      "}\n"
                                      ":hover{\n"
                                      "    background-color: qlineargradient(spread:pad, x1:0.985075, y1:1, x2:1, y2:0, stop:0 rgba(118, 180, 242, 255), stop:1 rgba(167, 203, 240, 255));\n"
                                      "}")
        self.ui.UserManageFrame.setVisible(True)
        self.ui.UserManageFrame.raise_()
        self.ui.SysSetFrame.setVisible(False)

    def ShowSysSetFrame(self):
        self.ui.UserButton.setStyleSheet(":hover{\n"
                                           "    background-color: qlineargradient(spread:pad, x1:0.985075, y1:1, x2:1, y2:0, stop:0 rgba(118, 180, 242, 255), stop:1 rgba(167, 203, 240, 255));\n"
                                           "}")
        self.ui.SysSetButton.setStyleSheet("QPushButton{\n"
                                         "background-color: qlineargradient(spread:pad, x1:0.985075, y1:1, x2:1, y2:0, stop:0 rgba(118, 180, 242, 255), stop:1 rgba(167, 203, 240, 255));\n"
                                         "}\n"
                                         ":hover{\n"
                                         "    background-color: qlineargradient(spread:pad, x1:0.985075, y1:1, x2:1, y2:0, stop:0 rgba(118, 180, 242, 255), stop:1 rgba(167, 203, 240, 255));\n"
                                         "}")
        self.ui.UserManageFrame.setVisible(False)
        self.ui.SysSetFrame.raise_()
        self.ui.SysSetFrame.setVisible(True)

    def ShowScanSetFrame(self):
        self.ui.ScanSetButton.setStyleSheet("background-color: rgb(67, 126, 239);\n"
                                         "border-radius:10;")
        self.ui.AuthorizeSetButton.setStyleSheet("background-color:transparent;\n"
"")
        self.ui.SacnSetRightFrame.setVisible(True)
        self.ui.SacnSetRightFrame.raise_()
        self.ui.AuthorizeRightFrame.setVisible(False)

    def ShowAuthorizeSetFrame(self):
        self.ui.AuthorizeSetButton.setStyleSheet("background-color: rgb(67, 126, 239);\n"
                                            "border-radius:10;")
        self.ui.ScanSetButton.setStyleSheet("background-color:transparent;\n"
                                                 "")
        self.ui.SacnSetRightFrame.setVisible(False)
        self.ui.SacnSetRightFrame.raise_()
        self.ui.AuthorizeRightFrame.setVisible(True)

    def ShowLogoutFrame(self):
        self.show_logoutFrame_signal.emit("sysadmin")

    def ShowWindow(self):
        self.show()
    def CloseWindow(self):
        self.close()

