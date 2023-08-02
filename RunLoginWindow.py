from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt, QPoint, QRectF, QPropertyAnimation, QObject, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QPainterPath, QRegion
import LoginWindow
from db.UserManager_Function import GetPasswd
from Tools import md5_encrypt, if_Passwd_Right
import sys


class LoginFrame(QWidget):
    # 信号
    close_MainWindow_signal = pyqtSignal()
    show_SysAdminFrame_signal = pyqtSignal()
    login_singnal = pyqtSignal(str)


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


    def init_ui(self):
        self.ui = LoginWindow.Ui_LoginWindow()
        self.ui.setupUi(self)
        self.ui.CloseButton.clicked.connect(self.CloseWindow)
        self.ui.QuitButton.clicked.connect(self.CloseWindow)
        self.ui.LoginButton.clicked.connect(self.LoginFunc)

    def CloseWindow(self):
        self.ui.MessageLabel1.setVisible(False)
        self.ui.MessageLabel2.setVisible(False)
        self.ui.UserNameInput.setText("")
        self.ui.PasswordInput.setText("")
        self.close()
    def LoginFunc(self):

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
            true_passwd = GetPasswd("SysAdmin")
            if if_Passwd_Right(input_passwd, true_passwd) == True:
                self.login_singnal.emit("sysadmin")
                self.close()
            else:
                self.ui.MessageLabel2.setVisible(True)
                self.ui.MessageLabel2.setText("密码不正确")
        elif user_name == "secadmin":
            true_passwd = GetPasswd("SecAdmin")
            if if_Passwd_Right(input_passwd, true_passwd) == True:
                self.login_singnal.emit("secadmin")
                self.close()
            else:
                self.ui.MessageLabel2.setVisible(True)
                self.ui.MessageLabel2.setText("密码不正确")
        elif user_name == "auditadmin":
            true_passwd = GetPasswd("AuditAdmin")
            if if_Passwd_Right(input_passwd, true_passwd) == True:
                self.login_singnal.emit("auditadmin")
                self.close()
            else:
                self.ui.MessageLabel2.setVisible(True)
                self.ui.MessageLabel2.setText("密码不正确")
        else:
            self.ui.MessageLabel1.setVisible(True)
            self.ui.MessageLabel1.setText("请输入正确的用户名")




