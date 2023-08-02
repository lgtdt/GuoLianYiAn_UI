from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt, QPoint, QRectF, QPropertyAnimation, QObject, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QPainterPath, QRegion
import LogoutWindow


from Tools import md5_encrypt
import sys

class LogoutFrame(QWidget):

    # 自定义信号
    logout_signal = pyqtSignal()
    # close_SysAdminFrame_signal = pyqtSignal()
    # show_MainFrame_signal = pyqtSignal()


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
        self.ui.MessageLabel.setVisible(False)


        #加载其他界面



    def init_ui(self):
        self.ui = LogoutWindow.Ui_LogoutWindow()
        self.ui.setupUi(self)
        self.ui.CloseButton.clicked.connect(self.CloseWindow)
        self.ui.ConfirmButton.clicked.connect(self.LogoutFunc)

    def CloseWindow(self):
        self.ui.PasswordInput.setText("")
        self.ui.MessageLabel.setVisible(False)
        self.close()

    def LogoutFunc(self):
        self.logout_signal.emit()
        # self.close_SysAdminFrame_signal.emit()
        self.close()