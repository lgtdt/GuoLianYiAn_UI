from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt, QPoint, QRectF, QPropertyAnimation, QObject, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QPainterPath, QRegion
import LoginWindow
from db.UserManager_Function import GetPasswd, IsUserLocked, WrongPassFunc, UnLockUser
from Tools import md5_encrypt, if_Passwd_Right
import time
from threading import Thread
import sys


class LoginFrame(QWidget):
    # 信号
    close_MainWindow_signal = pyqtSignal()
    show_SysAdminFrame_signal = pyqtSignal()
    login_singnal = pyqtSignal(str)
    print_lefttime_signal = pyqtSignal(str)

    # 控制倒计时线程的标志running 和 三个用户线程
    running = False
    threadSys = Thread()
    threadSec = Thread()
    threadAudit = Thread()


    def __init__(self):
        super().__init__()
        # ---设置窗口圆角---
        rect = QRectF(0, 0, 380, 325)
        path = QPainterPath()
        path.addRoundedRect(rect, 8, 8)
        polygon = path.toFillPolygon().toPolygon()
        region = QRegion(polygon)
        self.setMask(region)
        # ----------------

        self.init_ui()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.ui.MessageLabel1.setVisible(False)
        self.ui.MessageLabel2.setVisible(False)
        self.ui.UserNameInput.setText("")
        self.ui.PasswordInput.setText("")

        self.print_lefttime_signal.connect(self.PrintLeftTime)


    def init_ui(self):
        self.ui = LoginWindow.Ui_LoginWindow()
        self.ui.setupUi(self)
        self.ui.CloseButton.clicked.connect(self.CloseWindow)
        self.ui.QuitButton.clicked.connect(self.CloseWindow)
        self.ui.LoginButton.clicked.connect(self.LoginFunc)

    def CloseWindow(self):

        self.BlockThread()
        self.ui.MessageLabel1.setVisible(False)
        self.ui.MessageLabel2.setVisible(False)
        self.ui.UserNameInput.setText("")
        self.ui.PasswordInput.setText("")
        self.close()

    def PrintLeftTime(self, str):
        self.ui.MessageLabel1.setVisible(True)
        self.ui.MessageLabel1.setText(str)
    def BlockThread(self):
        # -------阻塞子线程---------
        self.running = False
        if self.threadSys.is_alive():
            self.threadSys.join()
        if self.threadSec.is_alive():
            self.threadSec.join()
        if self.threadAudit.is_alive():
            self.threadAudit.join()
        # -------------------------
    def LoginFunc(self):

        self.BlockThread()

        self.ui.MessageLabel1.setVisible(False)
        self.ui.MessageLabel2.setVisible(False)

        user_name = self.ui.UserNameInput.text().strip().lower()
        input_passwd = self.ui.PasswordInput.text()

        if input_passwd == "":
            self.ui.MessageLabel2.setVisible(True)
            self.ui.MessageLabel2.setText("密码不能为空")
        else:
            input_passwd = md5_encrypt(input_passwd)

        if user_name == "":
            self.ui.MessageLabel1.setVisible(True)
            self.ui.MessageLabel1.setText("用户名不能为空")

        elif user_name == "sysadmin":
            if IsUserLocked("sysadmin") != False:
                self.running = True
                def run():
                    LOCK_TIME_LEFT = IsUserLocked("sysadmin")
                    while (LOCK_TIME_LEFT > 0 and self.running):
                        self.print_lefttime_signal.emit(f"用户被锁定，锁定时间剩余{LOCK_TIME_LEFT}秒")
                        time.sleep(1)
                        LOCK_TIME_LEFT -= 1

                self.threadSys = Thread(target=run)
                self.threadSys.start()
            else:
                true_passwd = GetPasswd("sysadmin")
                if if_Passwd_Right(input_passwd, true_passwd) == True:
                    self.login_singnal.emit("sysadmin")
                    self.close()
                else:
                    WrongPassFunc("sysadmin")
                    self.ui.MessageLabel2.setVisible(True)
                    self.ui.MessageLabel2.setText("密码不正确")

        elif user_name == "secadmin":
            if IsUserLocked("secadmin") != False:
                self.running = True
                def run():
                    LOCK_TIME_LEFT = IsUserLocked("secadmin")
                    while (LOCK_TIME_LEFT > 0 and self.running):
                        self.print_lefttime_signal.emit(f"用户被锁定，锁定时间剩余{LOCK_TIME_LEFT}秒")
                        time.sleep(1)
                        LOCK_TIME_LEFT -= 1
                self.threadSec = Thread(target=run)
                self.threadSec.start()
            else:
                true_passwd = GetPasswd("secadmin")
                if if_Passwd_Right(input_passwd, true_passwd) == True:
                    self.login_singnal.emit("secadmin")
                    self.close()
                else:
                    WrongPassFunc("secadmin")
                    self.ui.MessageLabel2.setVisible(True)
                    self.ui.MessageLabel2.setText("密码不正确")

        elif user_name == "auditadmin":
            if IsUserLocked("auditadmin") != False:
                self.running = True
                def run():
                    LOCK_TIME_LEFT = IsUserLocked("auditadmin")
                    while (LOCK_TIME_LEFT > 0 and self.running):
                        self.print_lefttime_signal.emit(f"用户被锁定，锁定时间剩余{LOCK_TIME_LEFT}秒")
                        time.sleep(1)
                        LOCK_TIME_LEFT -= 1

                self.threadAudit = Thread(target=run)
                self.threadAudit.start()
            else:
                true_passwd = GetPasswd("auditadmin")
                if if_Passwd_Right(input_passwd, true_passwd) == True:
                    self.login_singnal.emit("auditadmin")
                    self.close()
                else:
                    WrongPassFunc("auditadmin")
                    self.ui.MessageLabel2.setVisible(True)
                    self.ui.MessageLabel2.setText("密码不正确")
        else:
            self.ui.MessageLabel1.setVisible(True)
            self.ui.MessageLabel1.setText("请输入正确的用户名")




