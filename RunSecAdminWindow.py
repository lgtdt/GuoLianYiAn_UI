from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QHeaderView, QMessageBox
from PyQt5.QtCore import Qt, QPoint, QRectF, QPropertyAnimation, QObject, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QPainterPath, QRegion
import SecAdminWindow
from db.optr_logs_Function import GetLogs
from db.password_policy_Function import Save_Password_Policy, Get_Password_Policy
from db.UserManager_Function import ResetUserPasswd, UnLockUser
from Tools import GetTimeFromTimeStamp

import sys
import datetime


class SecAdminFrame(QWidget):
    UserName = "secadmin"
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
        self.ui.ChangePassButton.clicked.connect(self.OpenResetPassWindow)
        self.ui.LogoutButton.clicked.connect(self.ShowLogoutFrame)
        self.ui.KillButton.clicked.connect(self.ShowKillFrame)
        self.ui.ToolsButton.clicked.connect(self.ShowSecToolsFrame)
        self.ui.UserButton.clicked.connect(self.ShowUserFrame)
        self.ui.LogButton.clicked.connect(self.ShowLogFrame)
        self.ui.SysSetButton.clicked.connect(self.ShowSysSetFrame)
        self.ui.SaveButton.clicked.connect(self.SavePassPolicy)
        self.ui.ResetButton1.clicked.connect(self.ResetSysPass)
        self.ui.UnlockButton1.clicked.connect(self.UnlockSysAdmin)


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

        self.ui.LogTableWidget.setStyleSheet("""
                QTableWidget {
                    border: none; /* 移除表格整体边框 */
                }
                QTableWidget QHeaderView::section {
                    background-color: blue;
                    }
               QTableWidget::item {
                border: none; /* 移除单元格边框 */
                padding: 5px;
            }
                """)

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
        policy_dict = Get_Password_Policy()
        self.ui.upper_num.setText(str(policy_dict[0]))
        self.ui.lower_num.setText(str(policy_dict[1]))
        self.ui.symbol_num.setText(str(policy_dict[2]))
        self.ui.digit_num.setText(str(policy_dict[3]))
        self.ui.min_len_num.setText(str(policy_dict[4]))
        self.ui.pass_change_time.setText(str(policy_dict[5]))
        self.ui.wrong_time.setText(str(policy_dict[6]))
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


    def SavePassPolicy(self):
        policy_dict = {}
        policy_dict['upper_num'] = int(self.ui.upper_num.text())
        policy_dict['lower_num'] = int(self.ui.lower_num.text())
        policy_dict['symbol_num'] = int(self.ui.symbol_num.text())
        policy_dict['digit_num'] = int(self.ui.digit_num.text())
        policy_dict['min_len_num'] = int(self.ui.min_len_num.text())
        policy_dict['passwd_limit'] = int(self.ui.pass_change_time.text())
        policy_dict['err_num'] = int(self.ui.wrong_time.text())

        result = Save_Password_Policy(policy_dict)
        if result == "success":
            QMessageBox.information(self, "Success", "保存成功!")
        else:
            QMessageBox.critical(self, "Error", f"Error updating record: {result}")

    def ResetSysPass(self):
        try:
            ResetUserPasswd("sysadmin")
            QMessageBox.information(self, "Success", "密码重置成功！")
        except Exception as e:
            print(str(e))
    def UnlockSysAdmin(self):
        try:
            UnLockUser("sysadmin")
            QMessageBox.information(self, "Success", "用户解锁成功！")
        except Exception as e:
            print(str(e))




    def ShowWindow(self):
        self.show()
    def CloseWindow(self):
        self.close()

