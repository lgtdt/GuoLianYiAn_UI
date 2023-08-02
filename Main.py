from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt, QPoint, QRectF, QPropertyAnimation, QObject, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QPainterPath, QRegion
import MainWindow
from RunLoginWindow import LoginFrame
from RunResetPassWindow import ResetPassFrame
from RunAboutWindow import AboutFrame
from RunSysAdminWindow import SysAdminFrame
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

        # 加载子页面
        self.loginFrame = LoginFrame()
        self.resetPassFrame = ResetPassFrame()
        self.aboutFrame = AboutFrame()
        self.sysAdminFrame = SysAdminFrame()

        # 自定义槽
        self.loginFrame.close_MainWindow_signal.connect(self.CloseWindow)
        self.sysAdminFrame.logoutBackToMainFrame_signal.connect(self.Test)



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

    def ShowWindow(self):
        print("111")
        self.show()
    def Test(self):
        print(333)
    # 关闭按钮的实现
    def QuitWindow(self):
        QApplication.quit()
    def CloseWindow(self):
        self.close()

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
    sys.exit(app.exec_())