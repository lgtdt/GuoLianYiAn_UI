from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import Qt, QRectF,  pyqtSignal, pyqtSlot
from PyQt5.QtGui import QPainterPath, QRegion
import ResetPassWindow
import sys
from Tools import if_Passwd_Right, md5_encrypt, CheckPass
from db.UserManager_Function import GetPasswd, UpdatePasswd


class ResetPassFrame(QWidget):
    resetUserName = ""
    resetSuccess_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        # ---设置窗口圆角---
        rect = QRectF(0, 0, 380, 430)
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
        self.ui.MessageLabel3.setVisible(False)

    def init_ui(self):
        self.ui = ResetPassWindow.Ui_ResetPassWindow()
        self.ui.setupUi(self)
        self.ui.CloseButton.clicked.connect(self.CloseWindow)
        self.ui.CancelButton.clicked.connect(self.CloseWindow)
        self.ui.ConfirmButton.clicked.connect(self.ResetPassFunc)

    def ResetPassFunc(self):
        self.ui.MessageLabel1.setVisible(False)
        self.ui.MessageLabel3.setVisible(False)
        old_passwd = self.ui.OldPassInput.text()
        new_passwd = self.ui.NewPassInput.text()
        con_passwd = self.ui.ConfirmPassInput.text()
        true_passwd = GetPasswd(self.resetUserName)
        if if_Passwd_Right(md5_encrypt(old_passwd), true_passwd):
            if(if_Passwd_Right(new_passwd, con_passwd)):
                try:
                    if(CheckPass(new_passwd) and new_passwd != old_passwd):
                        QMessageBox.information(self, "Success", "修改成功!")
                        UpdatePasswd(self.resetUserName, md5_encrypt(new_passwd))
                        self.resetSuccess_signal.emit(self.resetUserName)
                        self.ui.MessageLabel1.setVisible(False)
                        self.ui.MessageLabel3.setVisible(False)
                        self.ui.OldPassInput.setText("")
                        self.ui.NewPassInput.setText("")
                        self.ui.ConfirmPassInput.setText("")
                        self.close()
                    else:
                        self.ui.MessageLabel3.setVisible(True)
                        self.ui.MessageLabel3.setText("密码设置不符合规定，请重新设置")
                except Exception as e:
                    print(str(e))
            else:
                self.ui.MessageLabel3.setVisible(True)
                self.ui.MessageLabel3.setText("两次密码不一致")
        else:
            self.ui.MessageLabel1.setVisible(True)
            self.ui.MessageLabel1.setText("密码错误")
    def CloseWindow(self):
        self.ui.MessageLabel1.setVisible(False)
        self.ui.MessageLabel3.setVisible(False)
        self.ui.OldPassInput.setText("")
        self.ui.NewPassInput.setText("")
        self.ui.ConfirmPassInput.setText("")
        self.close()

