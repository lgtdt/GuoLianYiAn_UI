import random
import time

from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QMessageBox, QFileDialog, QHBoxLayout, QVBoxLayout, QFrame, QLabel, QPushButton
from PyQt5.QtCore import Qt, QPoint, QRectF, QPropertyAnimation, QObject, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QPainterPath, QRegion, QPixmap
import MainWindow
from RunLoginWindow import LoginFrame
from RunLogoutWindow import LogoutFrame
from RunResetPassWindow import ResetPassFrame
from RunAboutWindow import AboutFrame
from RunSysAdminWindow import SysAdminFrame
from RunSecAdminWindow import SecAdminFrame
from RunAuditAdminWindow import AuditAdminFrame


from Tools import GetTimeFromTimeStamp, CheckConfig
from db.optr_logs_Function import GetLogs

import os
import sys
import subprocess
from threading import Thread, Event

class IndexWindow(QWidget):

    #自定义信号
    print_file_signal = pyqtSignal(str)
    print_processNum_signal = pyqtSignal(str)


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
        self.CheckConfigFile()

        #一些全局变量
        self.skinname = "origin"
        self.draggable = True
        self.offset = None
        self.ifMoreMenuOpen = False
        self.logoutName = ""

        # 控制线程的标志running 和 子线程
        self.running = False
        self.command = ""
        self.process = None
        self.thread_Core = Thread()
        self.thread_FilePrint = Thread()
        self.thread_ProcessNum = Thread()
        self.if_done = False
        self.exit_flag = False
        self.output_list = []
        self.viurs_file = [
            {"name": "clam.exe", "path": "W:\python\GuoLianYiAn_UI\\virus\\testttttttttttttt"},
            {"name": "clam.exe", "path": "W:\python\GuoLianYiAn_"},
            {"name": "clam.exe", "path": "W:\python\GuoLianYiAn_UI\\virus\\test"},
            {"name": "clam.exe", "path": "W:\python\GuoLianYiAn_UI\\virus\\test"},
            {"name": "clam.exe", "path": "W:\python\GuoLianYiAn_UI\\virus\\test"},
            {"name": "clam.exe", "path": "W:\python\GuoLianYiAn_UI\\virus\\test"},
        ]




        # 加载子页面
        self.loginFrame = LoginFrame()
        self.logoutFrame = LogoutFrame()
        self.resetPassFrame = ResetPassFrame()
        self.aboutFrame = AboutFrame()
        self.sysAdminFrame = SysAdminFrame()
        self.secAdminFrame = SecAdminFrame()
        self.auditAdminFrame = AuditAdminFrame()


        # 自定义槽
        self.loginFrame.login_singnal.connect(self.logToOtherWindow)
        self.loginFrame.showResetPass_signal.connect(self.OpenResetPassWindow)
        self.logoutFrame.logout_signal.connect(self.logout)
        self.resetPassFrame.resetSuccess_signal.connect(self.logToOtherWindow)
        self.sysAdminFrame.show_logoutFrame_signal.connect(self.ShowLogoutFrame)
        self.sysAdminFrame.resetPass_signal.connect(self.OpenResetPassWindow)
        self.secAdminFrame.show_logoutFrame_signal.connect(self.ShowLogoutFrame)
        self.secAdminFrame.resetPass_signal.connect(self.OpenResetPassWindow)
        self.auditAdminFrame.show_logoutFrame_signal.connect(self.ShowLogoutFrame)
        self.auditAdminFrame.resetPass_signal.connect(self.OpenResetPassWindow)
        self.print_file_signal.connect(self.File_Print_Slot)
        self.print_processNum_signal.connect(self.ProcessNum_Print_Slot)


    def init_ui(self):
        self.ui = MainWindow.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.MoreMenuFrame.setVisible(False)
        self.ui.ScanningFrame.setVisible(False)
        self.ui.ResultFrame.setVisible(False)
        self.ui.CloseButton.clicked.connect(self.QuitWindow)
        self.ui.MiniButtuon.clicked.connect(self.MinimizeWindow)
        self.ui.SkinButton.clicked.connect(self.ChangeSkin)
        self.ui.LoginButton.clicked.connect(self.OpenLoginWindow)
        self.ui.SetButtuon.clicked.connect(self.OpenMoreMenu)
        self.ui.ChangePassButton.clicked.connect(self.OpenResetPassWindow)
        self.ui.AboutButton.clicked.connect(self.OpenAboutWindow)
        self.ui.ScanButton.clicked.connect(self.SwitchToScanningFrameAndScanAll)
        self.ui.KillButton.clicked.connect(self.SwitchToIndexFrame)
        self.ui.CancelScanButton.clicked.connect(self.BlockThread)
        self.ui.ProcessButton.clicked.connect(self.SwitchToResultFrame)
        self.ui.PartScanButton.clicked.connect(self.PickPathScan)




    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self.draggable:
            self.offset = event.pos()

    def mouseMoveEvent(self, event):
        if self.offset is not None and self.draggable:
            self.move(self.pos() + event.pos() - self.offset)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.offset = None

    def CheckConfigFile(self):
        result = CheckConfig()
        if result != "success":
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Information)
            msg_box.setWindowTitle('Error')
            msg_box.setText(result)
            msg_box.setStandardButtons(QMessageBox.Ok)
            # 显示信息框
            msg_box.exec_()

    def logToOtherWindow(self, name):
        self.loginFrame.ui.MessageLabel1.setVisible(False)
        self.loginFrame.ui.MessageLabel2.setVisible(False)
        self.loginFrame.ui.UserNameInput.setText("")
        self.loginFrame.ui.PasswordInput.setText("")
        self.close()
        if name == "sysadmin":
            self.sysAdminFrame.show()
        elif name == "secadmin":
            self.secAdminFrame.show()
        elif name == "auditadmin":
            results = GetLogs("secadmin")

            self.auditAdminFrame.ui.LogTableWidget.setRowCount(len(results))

            for row_idx, row_data in enumerate(results):
                for col_idx, col_data in enumerate(row_data):
                    if col_idx == 2:
                        item = QTableWidgetItem(GetTimeFromTimeStamp(col_data))
                    else:
                        item = QTableWidgetItem(str(col_data))
                    item.setTextAlignment(Qt.AlignCenter)  # 设置内容居中对齐
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)  # 设置单元格为只读
                    self.auditAdminFrame.ui.LogTableWidget.setItem(row_idx, col_idx, item)
            self.auditAdminFrame.show()
    def ShowLogoutFrame(self, name):
        self.logoutFrame.ui.PasswordInput.setText("")
        self.logoutFrame.ui.MessageLabel.setVisible(False)
        self.logoutFrame.show()
        self.logoutName = name
        self.logoutFrame.logoutUser = name
    def logout(self):
        self.show()
        if self.logoutName == "sysadmin":
            self.sysAdminFrame.close()
        if self.logoutName == "secadmin":
            self.secAdminFrame.close()
        if self.logoutName == "auditadmin":
            self.auditAdminFrame.close()
    # 关闭按钮的实现
    def QuitWindow(self):
        QApplication.quit()

    #最小化按钮的实现
    def MinimizeWindow(self):
        self.showMinimized()

    def ChangeSkin(self):
        if self.skinname == "origin":
            self.ui.ProcessButton.setStyleSheet("")
            self.ui.ProcessButton.setStyleSheet("QPushButton{\n"
                                             "    background-color: red;\n"
                                             "    border-radius: 18;\n"
                                             "}\n"
                                             ":hover{\n"
                                             "    \n"
                                             "    background-color: black;\n"
                                             "}")
            self.skinname = "test-skin"
        else:
            self.ui.ProcessButton.setStyleSheet("")
            self.ui.ProcessButton.setStyleSheet("QPushButton{\n"
                                             "    background-color: rgb(43, 128, 247);\n"
                                             "    border-radius: 18;\n"
                                             "}\n"
                                             ":hover{\n"
                                             "    \n"
                                             "    background-color: rgb(126, 216, 255);\n"
                                             "}")
            self.skinname = "origin"
    def OpenLoginWindow(self):
        # self.close()
        self.loginFrame.show()

    def OpenMoreMenu(self):
        if not self.ifMoreMenuOpen:
            self.ui.MoreMenuFrame.setVisible(True)
            self.ifMoreMenuOpen = True
        else:
            self.ui.MoreMenuFrame.setVisible(False)
            self.ifMoreMenuOpen = False

    def OpenResetPassWindow(self, name):
        self.resetPassFrame.show()
        self.resetPassFrame.resetUserName = name
    def OpenAboutWindow(self):
        self.aboutFrame.show()

    def File_Print_Slot(self, file_path):
        self.ui.FilePathLabel.setVisible(True)
        self.ui.FilePathLabel.setText(file_path)
    def ProcessNum_Print_Slot(self, str):
        self.ui.ProcessNumberLabel.setText(str)

    def BlockThread(self):
        # -------阻塞子线程---------
        print(2)
        self.exit_flag = True
        try:
            self.process.terminate()
        except Exception as e:
            print(str(e))
        print(3)

        self.running = False
        # -------------------------
    def SwitchToScanningFrameAndScanAll(self):
        self.ui.ScanningFrame.setVisible(True)
        self.ui.ScanningFrame.raise_()
        self.ui.BodyFrame.setVisible(False)
        self.ui.ResultFrame.setVisible(False)

        #------全局扫描逻辑代码--------------
        self.running = True
        self.command = ".\\engine\\clamav\\clamscan.exe .\\virus\\test"

        def run():
            if self.running is True:
                try:
                    self.process = subprocess.Popen(self.command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True,
                                               text=True)
                    while True:
                        line = self.process.stdout.readline()
                        if line == '' or self.process.poll() is not None:
                            print("Done")
                            break
                        self.print_file_signal.emit(line.strip())
                except Exception as e:
                    print(str(e))

        self.thread_Core = Thread(target=run)
        self.thread_Core.start()


    def PickPathScan(self):
        folder_path = QFileDialog.getExistingDirectory(self, "选择文件夹", "")
        if folder_path:
            self.ui.ScanningFrame.setVisible(True)
            self.ui.ScanningFrame.raise_()
            self.ui.BodyFrame.setVisible(False)
            self.ui.ResultFrame.setVisible(False)

            # ------自选路径扫描逻辑代码--------------
            self.running = True
            self.command = ".\\engine\\clamav\\clamscan.exe " + folder_path.replace("/", "\\\\")

            def run():
                if self.running is True:
                    try:
                        self.process = subprocess.Popen(self.command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                                   shell=True,
                                                   text=True)
                        while True:
                            line = self.process.stdout.readline()
                            self.output_list.append(line)
                            if line == '' or self.process.poll() is not None:
                                for line in self.output_list:
                                    print(line)
                                print("Done")
                                break
                    except Exception as e:
                        print(str(e))
                else:
                    return

            def run2():
                try:
                    if self.running is True:
                        for root, _, files in os.walk(folder_path):
                            for file in files:
                                file_path = os.path.join(root, file)
                                self.print_file_signal.emit(file_path)
                                time.sleep(random.random())
                    else:
                        return
                except Exception as e:
                    print(str(e))

            def run3():
                try:
                    if self.running is True:
                        process_num = 1

                        while(process_num <= 100):
                            self.print_processNum_signal.emit(f"{process_num}%")
                            time.sleep(random.random())
                            process_num += 1
                    else:
                        return
                except Exception as e:
                    print(str(e))


            self.thread_FilePrint = Thread(target=run2)
            self.thread_Core = Thread(target=run)
            self.thread_ProcessNum = Thread(target=run3)
            self.thread_Core.start()
            self.thread_FilePrint.start()
            self.thread_ProcessNum.start()
        else:
            QMessageBox.information(self, "Error", "路径不存在！")



    def SwitchToResultFrame(self):
        self.ui.ResultFrame.show()
        self.ui.scrollArea.setWidgetResizable(True)
        container_widget = QWidget(self)
        container_layout = QVBoxLayout(container_widget)
        try:
            for virus in self.viurs_file:
                #row_layout 用于填充每行的元素
                row_layout = QHBoxLayout()
                row_layout.addSpacing(30)

                #填充图标
                icon_label = QLabel(self)
                pixmap = QPixmap("./statics/imgs/right.png")
                icon_label.setPixmap(pixmap.scaled(19, 19))
                icon_label.setFixedSize(19, 19)
                row_layout.addWidget(icon_label)

                #填充病毒文件名和路径
                virus_widget = QWidget(self)
                virus_display = QVBoxLayout(virus_widget)
                virus_widget.setFixedSize(330, 60)
                virus_widget.setStyleSheet('''
                    background-color : transparent;
                ''')
                vname_label = QLabel(virus["name"], self)
                vname_label.setStyleSheet('''
                    color: white;
                ''')
                vpath_label = QLabel(virus["path"], self)
                vpath_label.setStyleSheet('''
                    color: rgb(0, 104, 139);
                ''')
                virus_display.addWidget(vname_label)
                virus_display.addWidget(vpath_label)
                row_layout.addWidget(virus_widget)

                #病毒类型
                type_name = " 黑客工具"
                virus_type = QLabel(type_name, self)
                virus_type.setFixedSize(75, 22)
                virus_type.setStyleSheet('''
                    background-color: orange;
                    font-size: 15px;
                    border-radius: 10px;
                    color: white;
                ''')
                row_layout.addWidget(virus_type)
                row_layout.addSpacing(170)

                #按钮
                button1 = QPushButton("详情", self)
                button1.setCursor(Qt.PointingHandCursor)
                button1.setStyleSheet('''
                    color: rgb(0, 104, 139);
                ''')
                button2 = QPushButton("信任", self)
                button2.setCursor(Qt.PointingHandCursor)
                button2.setStyleSheet('''
                    color: rgb(0, 104, 139);
                ''')
                row_layout.addWidget(button1)
                row_layout.addWidget(button2)
                row_layout.addSpacing(30)

                #分割线
                line = QFrame()
                line.setFrameShape(QFrame.HLine)
                line.setStyleSheet('''
                    border: 1px  #CCCCCC;
                    background-color:  #CCCCCC;
                ''')

                container_layout.addLayout(row_layout)
                container_layout.addWidget(line)
                container_layout.setSpacing(10)

        except Exception as e:
            print(str(e))


        self.ui.scrollArea.setWidget(container_widget)
        self.ui.scrollArea.setStyleSheet('''
            QScrollBar:vertical {
                border: 2px solid grey;
                background: lightgrey;
                border-radius: 5px;
                width: 0px;
                margin: 22px 0 22px 0;
            }
            QScrollBar::handle:vertical {
                background: grey;
                min-height: 20px;
                border-radius: 5px;
            }

            QScrollBar::add-line:vertical {
                background: none;
            }

            QScrollBar::sub-line:vertical {
                background: none;
            }
        ''')



    def SwitchToIndexFrame(self):
        self.ui.KillButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.985075, y1:1, x2:1, y2:0, stop:0 rgba(118, 180, 242, 255), stop:1 rgba(167, 203, 240, 255));")
        self.ui.BodyFrame.setVisible(True)
        self.ui.ResultFrame.setVisible(False)
        self.ui.ScanningFrame.setVisible(False)




if __name__ == '__main__':


    app = QApplication(sys.argv)
    indexWindow = IndexWindow()
    indexWindow.setWindowFlags(Qt.FramelessWindowHint)
    indexWindow.show()
    sys.exit(app.exec_())