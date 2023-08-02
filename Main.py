from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt, QPoint, QRectF, QPropertyAnimation, QObject, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QPainterPath, QRegion
import MainWindow
from RunLoginWindow import LoginFrame
from RunLogoutWindow import LogoutFrame
from RunResetPassWindow import ResetPassFrame
from RunAboutWindow import AboutFrame
from RunSysAdminWindow import SysAdminFrame
from RunSecAdminWindow import SecAdminFrame
from RunAuditAdminWindow import AuditAdminFrame

from db.CreatDB import CreatDB

import sys

class IndexWindow(QWidget):
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

        self.skinname = "origin"
        self.draggable = True
        self.offset = None
        self.ifMoreMenuOpen = False
        self.logoutName = ""

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
        self.logoutFrame.logout_signal.connect(self.logout)
        self.sysAdminFrame.show_logoutFrame_signal.connect(self.ShowLogoutFrame)
        self.secAdminFrame.show_logoutFrame_signal.connect(self.ShowLogoutFrame)
        self.auditAdminFrame.show_logoutFrame_signal.connect(self.ShowLogoutFrame)


    def init_ui(self):
        self.ui = MainWindow.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.MoreMenuFrame.setVisible(False)
        self.ui.CloseButton.clicked.connect(self.QuitWindow)
        self.ui.MiniButtuon.clicked.connect(self.MinimizeWindow)
        self.ui.SkinButton.clicked.connect(self.ChangeSkin)
        self.ui.LoginButton.clicked.connect(self.OpenLoginWindow)
        self.ui.SetButtuon.clicked.connect(self.OpenMoreMenu)
        self.ui.ChangePassButton.clicked.connect(self.OpenResetPassWindow)
        self.ui.AboutButton.clicked.connect(self.OpenAboutWindow)
        self.ui.ScanButton.clicked.connect(self.SwitchToResultFrame)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self.draggable:
            self.offset = event.pos()

    def mouseMoveEvent(self, event):
        if self.offset is not None and self.draggable:
            self.move(self.pos() + event.pos() - self.offset)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.offset = None

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
            self.auditAdminFrame.show()
    def ShowLogoutFrame(self, name):
        self.logoutFrame.ui.PasswordInput.setText("")
        self.logoutFrame.ui.MessageLabel.setVisible(False)
        self.logoutFrame.show()
        self.logoutName = name
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

    def OpenResetPassWindow(self):
        self.resetPassFrame.show()
    def OpenAboutWindow(self):
        self.aboutFrame.show()
    def SwitchToResultFrame(self):
        self.ui.ResultFrame.raise_()




if __name__ == '__main__':


    app = QApplication(sys.argv)
    indexWindow = IndexWindow()
    indexWindow.setWindowFlags(Qt.FramelessWindowHint)
    indexWindow.show()
    #CreatDB()
    sys.exit(app.exec_())