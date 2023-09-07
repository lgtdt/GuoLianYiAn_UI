from PyQt5.QtWidgets import QApplication, QWidget,QHeaderView
from PyQt5.QtCore import Qt, QPoint, QRectF, QPropertyAnimation, QObject, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QPainterPath, QRegion
import AuditAdminWindow

import sys


class AuditAdminFrame(QWidget):
    UserName = "aduitadmin"

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




        #自定义槽


    def init_ui(self):
        self.ui = AuditAdminWindow.Ui_AuditAdminWindow()
        self.ui.setupUi(self)
        self.ui.LogTableWidget.setColumnCount(5)
        self.ui.LogTableWidget.setHorizontalHeaderLabels(["ID", "用户", "时间", "事件", "事件描述"])
        self.ui.LogTableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.MoreMenuFrame.setVisible(False)
        self.ui.CloseButton.clicked.connect(self.CloseWindow)
        self.ui.SetButtuon.clicked.connect(self.OpenMoreMenu)
        self.ui.ChangePassButton.clicked.connect(self.OpenResetPassWindow)

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

    def ShowLogoutFrame(self):
        self.show_logoutFrame_signal.emit("auditadmin")

    def ShowWindow(self):
        self.show()
    def CloseWindow(self):
        self.close()

