from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt, QPoint, QRectF, QPropertyAnimation, QObject, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QPainterPath, QRegion
import AuditAdminWindow

import sys


class AuditAdminFrame(QWidget):

    #自定义信号
    show_logoutFrame_signal = pyqtSignal(str)

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
        self.ui = AuditAdminWindow.Ui_AuditAdminWindow()
        self.ui.setupUi(self)
        self.ui.MoreMenuFrame.setVisible(False)
        self.ui.CloseButton.clicked.connect(self.CloseWindow)
        self.ui.SetButtuon.clicked.connect(self.OpenMoreMenu)

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
        self.resetPassFrame.show()
    def OpenAboutWindow(self):
        self.aboutFrame.show()

    def ShowLogoutFrame(self):
        self.show_logoutFrame_signal.emit("auditadmin")

    def ShowWindow(self):
        self.show()
    def CloseWindow(self):
        self.close()

