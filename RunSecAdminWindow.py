from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QHeaderView
from PyQt5.QtCore import Qt, QPoint, QRectF, QPropertyAnimation, QObject, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QPainterPath, QRegion
import SecAdminWindow
from db.optr_logs_Function import GetLogs
from Tools import GetTimeFromTimeStamp

import sys
import datetime


class SecAdminFrame(QWidget):

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
        self.ui.KillFrame.raise_()



        #自定义槽


    def init_ui(self):
        self.ui = SecAdminWindow.Ui_SecAdminWindow()
        self.ui.setupUi(self)
        self.ui.LogTableWidget.setColumnCount(5)
        self.ui.LogTableWidget.setHorizontalHeaderLabels(["ID", "用户", "时间", "事件", "事件描述"])
        self.ui.LogTableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.MoreMenuFrame.setVisible(False)
        self.ui.CloseButton.clicked.connect(self.CloseWindow)
        self.ui.SetButtuon.clicked.connect(self.OpenMoreMenu)
        self.ui.LogoutButton.clicked.connect(self.ShowLogoutFrame)
        self.ui.KillButton.clicked.connect(self.ShowKillFrame)
        self.ui.ToolsButton.clicked.connect(self.ShowSecToolsFrame)
        self.ui.UserButton.clicked.connect(self.ShowUserFrame)
        self.ui.LogButton.clicked.connect(self.ShowLogFrame)
        self.ui.SysSetButton.clicked.connect(self.ShowSysSetFrame)


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

    def ShowSecToolsFrame(self):
        self.ui.SecToolsFrame.raise_()
        self.ui.ToolsButton.setStyleSheet("QPushButton{\n"
                                      "background-color: qlineargradient(spread:pad, x1:0.985075, y1:1, x2:1, y2:0, stop:0 rgba(118, 180, 242, 255), stop:1 rgba(167, 203, 240, 255));\n"
                                      "}\n"
                                      ":hover{\n"
                                      "    background-color: qlineargradient(spread:pad, x1:0.985075, y1:1, x2:1, y2:0, stop:0 rgba(118, 180, 242, 255), stop:1 rgba(167, 203, 240, 255));\n"
                                      "}")
        self.ui.KillButton.setStyleSheet(":hover{\n"
                                       "    background-color: qlineargradient(spread:pad, x1:0.985075, y1:1, x2:1, y2:0, stop:0 rgba(118, 180, 242, 255), stop:1 rgba(167, 203, 240, 255));\n"
                                       "}")
        self.ui.UserButton.setStyleSheet(":hover{\n"
                                       "    background-color: qlineargradient(spread:pad, x1:0.985075, y1:1, x2:1, y2:0, stop:0 rgba(118, 180, 242, 255), stop:1 rgba(167, 203, 240, 255));\n"
                                       "}")
        self.ui.LogButton.setStyleSheet(":hover{\n"
                                       "    background-color: qlineargradient(spread:pad, x1:0.985075, y1:1, x2:1, y2:0, stop:0 rgba(118, 180, 242, 255), stop:1 rgba(167, 203, 240, 255));\n"
                                       "}")
        self.ui.SysSetButton.setStyleSheet(":hover{\n"
                                       "    background-color: qlineargradient(spread:pad, x1:0.985075, y1:1, x2:1, y2:0, stop:0 rgba(118, 180, 242, 255), stop:1 rgba(167, 203, 240, 255));\n"
                                       "}")
    def ShowKillFrame(self):
        self.ui.KillFrame.raise_()
        self.ui.KillButton.setStyleSheet("QPushButton{\n"
                                          "background-color: qlineargradient(spread:pad, x1:0.985075, y1:1, x2:1, y2:0, stop:0 rgba(118, 180, 242, 255), stop:1 rgba(167, 203, 240, 255));\n"
                                          "}\n"
                                          ":hover{\n"
                                          "    background-color: qlineargradient(spread:pad, x1:0.985075, y1:1, x2:1, y2:0, stop:0 rgba(118, 180, 242, 255), stop:1 rgba(167, 203, 240, 255));\n"
                                          "}")
        self.ui.ToolsButton.setStyleSheet(":hover{\n"
                                         "    background-color: qlineargradient(spread:pad, x1:0.985075, y1:1, x2:1, y2:0, stop:0 rgba(118, 180, 242, 255), stop:1 rgba(167, 203, 240, 255));\n"
                                         "}")
        self.ui.UserButton.setStyleSheet(":hover{\n"
                                         "    background-color: qlineargradient(spread:pad, x1:0.985075, y1:1, x2:1, y2:0, stop:0 rgba(118, 180, 242, 255), stop:1 rgba(167, 203, 240, 255));\n"
                                         "}")
        self.ui.LogButton.setStyleSheet(":hover{\n"
                                        "    background-color: qlineargradient(spread:pad, x1:0.985075, y1:1, x2:1, y2:0, stop:0 rgba(118, 180, 242, 255), stop:1 rgba(167, 203, 240, 255));\n"
                                        "}")
        self.ui.SysSetButton.setStyleSheet(":hover{\n"
                                           "    background-color: qlineargradient(spread:pad, x1:0.985075, y1:1, x2:1, y2:0, stop:0 rgba(118, 180, 242, 255), stop:1 rgba(167, 203, 240, 255));\n"
                                           "}")

    def ShowUserFrame(self):
        self.ui.UserFrame.raise_()
        self.ui.UserButton.setStyleSheet("QPushButton{\n"
                                         "background-color: qlineargradient(spread:pad, x1:0.985075, y1:1, x2:1, y2:0, stop:0 rgba(118, 180, 242, 255), stop:1 rgba(167, 203, 240, 255));\n"
                                         "}\n"
                                         ":hover{\n"
                                         "    background-color: qlineargradient(spread:pad, x1:0.985075, y1:1, x2:1, y2:0, stop:0 rgba(118, 180, 242, 255), stop:1 rgba(167, 203, 240, 255));\n"
                                         "}")
        self.ui.ToolsButton.setStyleSheet(":hover{\n"
                                          "    background-color: qlineargradient(spread:pad, x1:0.985075, y1:1, x2:1, y2:0, stop:0 rgba(118, 180, 242, 255), stop:1 rgba(167, 203, 240, 255));\n"
                                          "}")
        self.ui.KillButton.setStyleSheet(":hover{\n"
                                         "    background-color: qlineargradient(spread:pad, x1:0.985075, y1:1, x2:1, y2:0, stop:0 rgba(118, 180, 242, 255), stop:1 rgba(167, 203, 240, 255));\n"
                                         "}")
        self.ui.LogButton.setStyleSheet(":hover{\n"
                                        "    background-color: qlineargradient(spread:pad, x1:0.985075, y1:1, x2:1, y2:0, stop:0 rgba(118, 180, 242, 255), stop:1 rgba(167, 203, 240, 255));\n"
                                        "}")
        self.ui.SysSetButton.setStyleSheet(":hover{\n"
                                           "    background-color: qlineargradient(spread:pad, x1:0.985075, y1:1, x2:1, y2:0, stop:0 rgba(118, 180, 242, 255), stop:1 rgba(167, 203, 240, 255));\n"
                                           "}")

    def ShowLogFrame(self):
        self.ui.LogFrame.raise_()
        self.ui.LogButton.setStyleSheet("QPushButton{\n"
                                         "background-color: qlineargradient(spread:pad, x1:0.985075, y1:1, x2:1, y2:0, stop:0 rgba(118, 180, 242, 255), stop:1 rgba(167, 203, 240, 255));\n"
                                         "}\n"
                                         ":hover{\n"
                                         "    background-color: qlineargradient(spread:pad, x1:0.985075, y1:1, x2:1, y2:0, stop:0 rgba(118, 180, 242, 255), stop:1 rgba(167, 203, 240, 255));\n"
                                         "}")
        self.ui.ToolsButton.setStyleSheet(":hover{\n"
                                          "    background-color: qlineargradient(spread:pad, x1:0.985075, y1:1, x2:1, y2:0, stop:0 rgba(118, 180, 242, 255), stop:1 rgba(167, 203, 240, 255));\n"
                                          "}")
        self.ui.KillButton.setStyleSheet(":hover{\n"
                                         "    background-color: qlineargradient(spread:pad, x1:0.985075, y1:1, x2:1, y2:0, stop:0 rgba(118, 180, 242, 255), stop:1 rgba(167, 203, 240, 255));\n"
                                         "}")
        self.ui.UserButton.setStyleSheet(":hover{\n"
                                        "    background-color: qlineargradient(spread:pad, x1:0.985075, y1:1, x2:1, y2:0, stop:0 rgba(118, 180, 242, 255), stop:1 rgba(167, 203, 240, 255));\n"
                                        "}")
        self.ui.SysSetButton.setStyleSheet(":hover{\n"
                                           "    background-color: qlineargradient(spread:pad, x1:0.985075, y1:1, x2:1, y2:0, stop:0 rgba(118, 180, 242, 255), stop:1 rgba(167, 203, 240, 255));\n"
                                           "}")

        results = GetLogs("sysadmin")
        
        self.ui.LogTableWidget.setRowCount(len(results))

        for row_idx, row_data in enumerate(results):
            for col_idx, col_data in enumerate(row_data):
                if col_idx == 2:
                    item = QTableWidgetItem(GetTimeFromTimeStamp(col_data))
                else:
                    item = QTableWidgetItem(str(col_data))
                item.setTextAlignment(Qt.AlignCenter)  # 设置内容居中对齐
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)  # 设置单元格为只读
                self.ui.LogTableWidget.setItem(row_idx, col_idx, item)



    def ShowSysSetFrame(self):
        self.ui.MimaSetFrame.raise_()
        self.ui.SysSetButton.setStyleSheet("QPushButton{\n"
                                        "background-color: qlineargradient(spread:pad, x1:0.985075, y1:1, x2:1, y2:0, stop:0 rgba(118, 180, 242, 255), stop:1 rgba(167, 203, 240, 255));\n"
                                        "}\n"
                                        ":hover{\n"
                                        "    background-color: qlineargradient(spread:pad, x1:0.985075, y1:1, x2:1, y2:0, stop:0 rgba(118, 180, 242, 255), stop:1 rgba(167, 203, 240, 255));\n"
                                        "}")
        self.ui.ToolsButton.setStyleSheet(":hover{\n"
                                          "    background-color: qlineargradient(spread:pad, x1:0.985075, y1:1, x2:1, y2:0, stop:0 rgba(118, 180, 242, 255), stop:1 rgba(167, 203, 240, 255));\n"
                                          "}")
        self.ui.KillButton.setStyleSheet(":hover{\n"
                                         "    background-color: qlineargradient(spread:pad, x1:0.985075, y1:1, x2:1, y2:0, stop:0 rgba(118, 180, 242, 255), stop:1 rgba(167, 203, 240, 255));\n"
                                         "}")
        self.ui.UserButton.setStyleSheet(":hover{\n"
                                         "    background-color: qlineargradient(spread:pad, x1:0.985075, y1:1, x2:1, y2:0, stop:0 rgba(118, 180, 242, 255), stop:1 rgba(167, 203, 240, 255));\n"
                                         "}")
        self.ui.LogButton.setStyleSheet(":hover{\n"
                                           "    background-color: qlineargradient(spread:pad, x1:0.985075, y1:1, x2:1, y2:0, stop:0 rgba(118, 180, 242, 255), stop:1 rgba(167, 203, 240, 255));\n"
                                           "}")
    def ShowLogoutFrame(self):
        self.show_logoutFrame_signal.emit("secadmin")

    def ShowWindow(self):
        self.show()
    def CloseWindow(self):
        self.close()

